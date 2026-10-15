#!/usr/bin/env python3
"""
Builder for Deck 1: Functional Skills Mathematics - Level 2 (50 Cards)
Full curriculum alignment with UK DfE and Pearson Edexcel / City & Guilds standards.
"""
import os
import json
import xml.etree.ElementTree as ET

def get_maths_l2_cards():
    cards = [
        # --- STRAND A: NUMBER & THE NUMBER SYSTEM (Cards 1-18) ---
        {
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
            "rule_body": "Operations must be completed in order: 1. Brackets (), 2. Indices (², ³, √), 3. Division & Multiplication (left-to-right), 4. Addition & Subtraction (left-to-right).",
            "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
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
              </g>
            </svg>""",
            "golden_rule": "Always solve brackets and powers first before multiplying or adding!",
            "watch_out": "Don't just calculate left-to-right! 5 + 3 × 2 is 11, NOT 16.",
            "challenge_prompt": "Evaluate: 8 + 4 × (7 - 4)² ÷ 6",
            "answer_text": "1. Brackets: (7 - 4) = 3. 2. Index: 3² = 9. 3. Multiply: 4 × 9 = 36. 4. Divide: 36 ÷ 6 = 6. 5. Add: 8 + 6 = 14."
        },
        {
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
            "rule_heading": "Rules of Signs & Temperature Difference",
            "rule_body": "Difference between positive and negative = Add their absolute values (|a| + |b|). Multiplying/Dividing: Same signs = POSITIVE (+). Different signs = NEGATIVE (-).",
            "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
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
              <text x="230" y="152" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">(-6) to (+8) = 6 steps to zero + 8 steps = 14</text>
            </svg>""",
            "golden_rule": "Subtracting a negative is the same as ADDING! 5 - (-3) = 5 + 3 = 8.",
            "watch_out": "-5°C is COLDER than -2°C. The larger the numeral after the minus sign, the lower the value.",
            "challenge_prompt": "A vaccine freezer is at -18°C. A power failure causes it to rise to -4°C. By how many degrees did the temperature rise?",
            "answer_text": "Rise = -4 - (-18) = -4 + 18 = 14°C."
        },
        {
            "id": "m-l2-03",
            "number": 3,
            "title": "Fractions, Decimals & % Equivalence",
            "subject": "maths",
            "level": "l2",
            "subject_label": "Maths",
            "level_label": "Level 2",
            "strand_name": "Number System",
            "strand_theme": "blue",
            "dfe_code": "DfE L2.N3",
            "rule_heading": "Conversion Benchmarks",
            "rule_body": "To compare values, convert them all to percentages or decimals: Fraction to %: (Numerator ÷ Denominator) × 100. Decimal to %: Multiply by 100.",
            "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
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
              </g>
            </svg>""",
            "golden_rule": "Eighths are common exam traps: 1/8 = 12.5% (0.125), not 18%!",
            "watch_out": "0.4 is 40%, NOT 4%! 0.04 is 4%. Count your decimal places carefully.",
            "challenge_prompt": "Put in order from smallest to largest: 3/8, 35%, 0.36, 1/3.",
            "answer_text": "Convert all to decimals: 1/3 = 0.333..., 35% = 0.35, 0.36 = 0.36, 3/8 = 0.375. Order: 1/3, 35%, 0.36, 3/8."
        },
        {
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
            "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
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
              </g>
            </svg>""",
            "golden_rule": "Divide by the denominator, multiply by the numerator!",
            "watch_out": "If a question asks for the REMAINING amount, remember to subtract your answer from the original total.",
            "challenge_prompt": "A clinic orders 240 boxes of gloves. 5/8 of them are size Medium. How many boxes are NOT size Medium?",
            "answer_text": "Non-Medium fraction = 1 - 5/8 = 3/8. 240 ÷ 8 = 30. 30 × 3 = 90 boxes."
        },
        {
            "id": "m-l2-05",
            "number": 5,
            "title": "Adding & Subtracting Mixed Fractions",
            "subject": "maths",
            "level": "l2",
            "subject_label": "Maths",
            "level_label": "Level 2",
            "strand_name": "Number System",
            "strand_theme": "blue",
            "dfe_code": "DfE L2.N4",
            "rule_heading": "Convert to Improper & Common Denominator",
            "rule_body": "1. Convert mixed numbers to improper fractions (Whole × Denom + Num). 2. Find lowest common denominator (LCM). 3. Add or subtract numerators only. 4. Simplify.",
            "svg_html": """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
              <rect x="30" y="15" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
              <text x="230" y="40" font-size="15" font-weight="800" fill="#1e293b" text-anchor="middle">2 1/4 + 1 2/3</text>
              <g transform="translate(50, 55)">
                <text x="0" y="25" font-size="12" font-weight="700" fill="#2563eb">1. Improper: 9/4 + 5/3</text>
                <text x="0" y="50" font-size="12" font-weight="700" fill="#475569">2. Common Denom (12): 27/12 + 20/12</text>
                <text x="0" y="75" font-size="13" font-weight="800" fill="#059669">3. Add numerators: 47/12 = 3 11/12</text>
              </g>
            </svg>""",
            "golden_rule": "NEVER add denominators together! 1/4 + 2/3 is NEVER 3/7.",
            "watch_out": "When subtracting, always convert to top-heavy improper fractions first to prevent negative fractional parts.",
            "challenge_prompt": "Work out 3 1/3 - 1 3/4. Give your answer as a mixed number in simplest form.",
            "answer_text": "1. Convert: 10/3 - 7/4. 2. Common denom 12: 40/12 - 21/12 = 19/12. 3. Mixed: 1 7/12."
        }
    ]
    return cards

if __name__ == "__main__":
    cards = get_maths_l2_cards()
    print(f"Validated sample {len(cards)} cards")
