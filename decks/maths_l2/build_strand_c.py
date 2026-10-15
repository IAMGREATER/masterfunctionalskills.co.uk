#!/usr/bin/env python3
"""
Builder for Maths L2 Strand C: Handling Information and Data (Cards 37-50)
"""
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg) # validate XML
    return svg

CARDS = [
    # 37. Averages: Mean, Median, Mode & Range
    {
        "id": "m-l2-37",
        "number": 37,
        "title": "Averages: Mean, Median, Mode &amp; Range",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD34",
        "rule_heading": "The 4 Core Statistics",
        "rule_body": "Mean = Sum of values ÷ Count. Median = Middle value after ordering low to high. Mode = Most frequent value. Range = Highest - Lowest (spread, NOT an average).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 15)">
            <rect x="0" y="0" width="190" height="65" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="95" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">MEAN = Total ÷ Count</text>
            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">Add all up and share equally</text>
          </g>
          <g transform="translate(240, 15)">
            <rect x="0" y="0" width="190" height="65" rx="6" fill="#f0fdf4" stroke="#16a34a"/>
            <text x="95" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">MEDIAN = Middle Value</text>
            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">MUST put in order first!</text>
          </g>
          <g transform="translate(30, 90)">
            <rect x="0" y="0" width="190" height="65" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="95" y="24" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">MODE = Most Common</text>
            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">Number that appears most often</text>
          </g>
          <g transform="translate(240, 90)">
            <rect x="0" y="0" width="190" height="65" rx="6" fill="#fffbeb" stroke="#f59e0b"/>
            <text x="95" y="24" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">RANGE = High - Low</text>
            <text x="95" y="48" font-size="10.5" font-weight="700" fill="#dc2626" text-anchor="middle">Spread of data (NOT an average!)</text>
          </g>"""),
        "golden_rule": "Range is a measure of consistency/spread, NEVER an average!",
        "watch_out": "For the median with an even count of numbers, add the middle two and divide by 2.",
        "challenge_prompt": "Find the median and range of this dataset: 14, 8, 22, 19, 14, 27, 11.",
        "answer_text": "Ordered: 8, 11, 14, 14, 19, 22, 27 (7 numbers). Middle is 4th number = 14 (Median). Range = 27 - 8 = 19."
    },

    # 38. Mean from an Ungrouped Frequency Table
    {
        "id": "m-l2-38",
        "number": 38,
        "title": "Mean from a Frequency Table",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD35",
        "rule_heading": "Mean = Σfx ÷ Σf",
        "rule_body": "1. Multiply value (x) by frequency (f) to make an fx column. 2. Sum the fx column (Total score Σfx). 3. Sum the frequency column (Total count Σf). 4. Divide: Σfx ÷ Σf.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="70" y="26" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Score (x)</text>
            <text x="170" y="26" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">Freq (f)</text>
            <text x="290" y="26" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">x × f (fx)</text>
            <line x1="20" y1="35" x2="380" y2="35" stroke="#cbd5e1"/>
            <text x="70" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">1</text><text x="170" y="55" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">3</text><text x="290" y="55" font-size="11" font-weight="700" fill="#2563eb" text-anchor="middle">1 × 3 = 3</text>
            <text x="70" y="75" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">2</text><text x="170" y="75" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">5</text><text x="290" y="75" font-size="11" font-weight="700" fill="#2563eb" text-anchor="middle">2 × 5 = 10</text>
            <line x1="20" y1="90" x2="380" y2="90" stroke="#cbd5e1"/>
            <text x="170" y="112" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">Total f = 8</text>
            <text x="290" y="112" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">Total fx = 13</text>
            <text x="70" y="112" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">13 ÷ 8 = 1.625</text>
          </g>"""),
        "golden_rule": "Divide by total frequency (Σf), NEVER by the number of rows in the table!",
        "watch_out": "Don't just average the 'x' column — that ignores how many times each value occurred.",
        "challenge_prompt": "Cars per household: 0 cars (f=4), 1 car (f=10), 2 cars (f=6). Calculate the mean number of cars per household.",
        "answer_text": "fx: (0×4) + (1×10) + (2×6) = 0 + 10 + 12 = 22. Total frequency Σf = 4 + 10 + 6 = 20. Mean = 22 ÷ 20 = 1.1 cars."
    },

    # 39. Estimated Mean from Grouped Frequency Table
    {
        "id": "m-l2-39",
        "number": 39,
        "title": "Estimated Mean (Grouped Data)",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD36",
        "rule_heading": "Midpoints × Frequency ÷ Total Frequency",
        "rule_body": "1. Find midpoint of each group: (Lower bound + Upper bound) ÷ 2. 2. Multiply midpoint by frequency (mp × f). 3. Sum (mp × f). 4. Divide by total frequency.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Grouped Data: 10 &lt; t ≤ 20 (f = 4)</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11" font-weight="700" fill="#2563eb">1. Midpoint = (10 + 20) ÷ 2 = 15</text>
            <text x="0" y="45" font-size="11" font-weight="700" fill="#059669">2. mp × f = 15 × 4 = 60</text>
            <text x="0" y="70" font-size="12" font-weight="800" fill="#0f172a">Estimated Mean = Total (mp × f) ÷ Total Frequency</text>
          </g>"""),
        "golden_rule": "It is an 'ESTIMATE' because the exact individual raw values inside the group are unknown!",
        "watch_out": "Be careful finding midpoints: for 0 to 10, midpoint is 5. For 20 to 50, midpoint is 35 (not 30).",
        "challenge_prompt": "Times: 0–10 mins (f=2, mp=5), 10–20 mins (f=6, mp=15), 20–30 mins (f=2, mp=25). Calculate estimated mean.",
        "answer_text": "Total (mp × f) = (5×2) + (15×6) + (25×2) = 10 + 90 + 50 = 150. Total f = 2 + 6 + 2 = 10. Estimated Mean = 150 ÷ 10 = 15 mins."
    },

    # 40. Modal Class & Median Group
    {
        "id": "m-l2-40",
        "number": 40,
        "title": "Modal Class &amp; Median Group",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD37",
        "rule_heading": "Identifying Class Intervals",
        "rule_body": "Modal Class = The group interval with the HIGHEST frequency number. Median Group = The interval that contains the middle position ((Total f + 1) ÷ 2).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="95" y="28" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">MODAL CLASS</text>
            <text x="95" y="58" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Look down frequency column</text>
            <rect x="20" y="75" width="150" height="28" rx="4" fill="#3b82f6"/>
            <text x="95" y="94" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">HIGHEST Frequency</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="190" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="95" y="28" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">MEDIAN GROUP</text>
            <text x="95" y="58" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Find position: (n + 1) ÷ 2</text>
            <rect x="20" y="75" width="150" height="28" rx="4" fill="#16a34a"/>
            <text x="95" y="94" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Cumulative Count</text>
          </g>"""),
        "golden_rule": "Always write the ENTIRE interval inequality (e.g. 20 < t ≤ 30), not just one number!",
        "watch_out": "The modal class is the interval itself, NOT the frequency count.",
        "challenge_prompt": "Salaries: £15k–£20k (f=5), £20k–£25k (f=12), £25k–£30k (f=3). State: (a) Modal class, (b) Median group.",
        "answer_text": "(a) Modal class = £20k–£25k (highest frequency 12). (b) Total f = 20. Middle is 10.5th person. 5 in 1st group, next 12 in 2nd group. Median group = £20k–£25k."
    },

    # 41. Comparing Two Data Sets
    {
        "id": "m-l2-41",
        "number": 41,
        "title": "Comparing Two Data Sets",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD38",
        "rule_heading": "Average + Spread in Context",
        "rule_body": "To earn full marks on Pearson comparison questions, you MUST state: 1. One Average comparison in context ('Branch A has a higher mean sales by £50'). 2. One Range/Spread comparison ('Branch B is more consistent because its range is smaller').",
        "svg_html": wrap_svg("""
          <rect x="30" y="15" width="400" height="140" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
          <text x="230" y="38" font-size="13" font-weight="900" fill="#1e40af" text-anchor="middle">PEARSON GOLDEN 2-PART COMPARISON</text>
          <g transform="translate(50, 50)">
            <text x="0" y="25" font-size="11.5" font-weight="800" fill="#0f172a">1. AVERAGE: "Group A on average is higher/lower because mean is..."</text>
            <text x="0" y="55" font-size="11.5" font-weight="800" fill="#0f172a">2. SPREAD: "Group B is more consistent / reliable because range is smaller..."</text>
            <text x="0" y="80" font-size="11" font-weight="700" fill="#dc2626">⚠️ Must mention numbers AND the real-world context!</text>
          </g>"""),
        "golden_rule": "Smaller range = more consistent / reliable results!",
        "watch_out": "Always write comparison words (higher, lower, more consistent) in context!",
        "challenge_prompt": "Shift 1: Mean = 45 units, Range = 12. Shift 2: Mean = 41 units, Range = 5. Compare the two shifts.",
        "answer_text": "1. Shift 1 produced more units on average (mean of 45 vs 41). 2. Shift 2 was more consistent because its range was smaller (range of 5 vs 12)."
    },

    # 42. Probability of Single Events
    {
        "id": "m-l2-42",
        "number": 42,
        "title": "Probability of Single Events",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD39",
        "rule_heading": "P(Event) = Favourable ÷ Total",
        "rule_body": "Probability is always between 0 (Impossible) and 1 (Certain). Can be written as a fraction, decimal, or percentage. P(Not event) = 1 - P(Event).",
        "svg_html": wrap_svg("""
          <line x1="40" y1="85" x2="420" y2="85" stroke="#334155" stroke-width="3"/>
          <circle cx="40" cy="85" r="6" fill="#dc2626"/>
          <text x="40" y="115" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">0 (Impossible)</text>
          <circle cx="230" cy="85" r="6" fill="#f59e0b"/>
          <text x="230" y="115" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">0.5 (Even chance)</text>
          <circle cx="420" cy="85" r="6" fill="#16a34a"/>
          <text x="420" y="115" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">1 (Certain)</text>
          <rect x="110" y="20" width="240" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
          <text x="230" y="42" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">P = Favourable Outcomes ÷ Total</text>"""),
        "golden_rule": "Probabilities can NEVER be greater than 1 or negative!",
        "watch_out": "Don't write probability as a ratio (e.g. 1 : 4 is WRONG). Write as a fraction (1/5), decimal (0.2), or % (20%).",
        "challenge_prompt": "A bag contains 5 red, 7 blue, and 8 green tokens. What is the probability of picking a token that is NOT red? Give as a simplified fraction.",
        "answer_text": "Total tokens = 5 + 7 + 8 = 20. Non-red tokens = 7 + 8 = 15. Probability = 15/20 = 3/4."
    },

    # 43. Combined Independent Events
    {
        "id": "m-l2-43",
        "number": 43,
        "title": "Combined Independent Events",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD40",
        "rule_heading": "P(A and B) = P(A) × P(B)",
        "rule_body": "Independent events do not affect each other (e.g. flipping a coin and rolling a die). 'AND' rule = MULTIPLY probabilities. 'OR' rule = ADD probabilities.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="45" font-size="14" font-weight="900" fill="#0f172a" text-anchor="middle">P(A and B) = P(A) × P(B)</text>
          <g transform="translate(60, 65)">
            <text x="0" y="20" font-size="12" font-weight="700" fill="#2563eb">Flipping Heads AND rolling a 6:</text>
            <text x="0" y="45" font-size="12" font-weight="800" fill="#059669">P(Heads) = 1/2   •   P(Rolling a 6) = 1/6</text>
            <text x="0" y="70" font-size="13" font-weight="900" fill="#1e40af">Combined: 1/2 × 1/6 = 1/12</text>
          </g>"""),
        "golden_rule": "'AND' means MULTIPLY; 'OR' means ADD!",
        "watch_out": "Don't add when you need both to happen: 1/2 + 1/6 = 4/6 (which is much too high for both happening together).",
        "challenge_prompt": "The probability that train A is delayed is 0.2. The probability that train B is delayed is 0.15. What is the probability that BOTH trains are delayed?",
        "answer_text": "P(Both delayed) = 0.2 × 0.15 = 0.03 (or 3%)."
    },

    # 44. Probability Tree Diagrams
    {
        "id": "m-l2-44",
        "number": 44,
        "title": "Probability Tree Diagrams",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD41",
        "rule_heading": "Multiply Across, Add Down",
        "rule_body": "1. Branches from any single node must add up to 1. 2. MULTIPLY along branches to find outcome probability. 3. ADD individual outcome probabilities together if multiple paths satisfy the question.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <line x1="20" y1="65" x2="100" y2="30" stroke="#334155" stroke-width="2"/>
            <line x1="20" y1="65" x2="100" y2="100" stroke="#334155" stroke-width="2"/>
            <text x="60" y="38" font-size="10" font-weight="800" fill="#2563eb">0.7</text>
            <text x="60" y="98" font-size="10" font-weight="800" fill="#dc2626">0.3</text>
            <text x="110" y="32" font-size="10" font-weight="800" fill="#0f172a">Pass</text>
            <text x="110" y="104" font-size="10" font-weight="800" fill="#0f172a">Fail</text>
            <line x1="140" y1="30" x2="220" y2="15" stroke="#334155" stroke-width="1.8"/>
            <line x1="140" y1="30" x2="220" y2="45" stroke="#334155" stroke-width="1.8"/>
            <text x="230" y="18" font-size="10" font-weight="700" fill="#059669">P, P = 0.7 × 0.7 = 0.49</text>
            <text x="230" y="48" font-size="10" font-weight="700" fill="#d97706">P, F = 0.7 × 0.3 = 0.21</text>
          </g>"""),
        "golden_rule": "Every pair of branch splits MUST add up to 1 (100%)!",
        "watch_out": "Check whether picking is WITH replacement or WITHOUT replacement (fractions change on 2nd pick!).",
        "challenge_prompt": "A student has an 80% (0.8) chance of passing Theory, and a 70% (0.7) chance of passing Practical. What is the probability of passing AT LEAST ONE test?",
        "answer_text": "P(Fails both) = (1 - 0.8) × (1 - 0.7) = 0.2 × 0.3 = 0.06. P(At least one pass) = 1 - 0.06 = 0.94 (or 94%)."
    },

    # 45. Two-Way Tables
    {
        "id": "m-l2-45",
        "number": 45,
        "title": "Two-Way Tables &amp; Probability",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD42",
        "rule_heading": "Row Totals + Column Totals",
        "rule_body": "1. Every row must add up to its row total. 2. Every column must add up to its column total. 3. Grand total bottom-right must match both row totals and column totals.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 15)">
            <rect x="0" y="0" width="400" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <line x1="0" y1="35" x2="400" y2="35" stroke="#cbd5e1"/>
            <line x1="0" y1="70" x2="400" y2="70" stroke="#cbd5e1"/>
            <line x1="0" y1="105" x2="400" y2="105" stroke="#cbd5e1"/>
            <line x1="120" y1="0" x2="120" y2="140" stroke="#cbd5e1"/>
            <line x1="210" y1="0" x2="210" y2="140" stroke="#cbd5e1"/>
            <line x1="300" y1="0" x2="300" y2="140" stroke="#cbd5e1"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#0f172a">Group</text><text x="165" y="24" font-size="11" font-weight="800" fill="#0f172a">Bus</text><text x="255" y="24" font-size="11" font-weight="800" fill="#0f172a">Walk</text><text x="350" y="24" font-size="11" font-weight="900" fill="#1e40af">Total</text>
            <text x="60" y="58" font-size="11" font-weight="700" fill="#475569">Men</text><text x="165" y="58" font-size="11" font-weight="700" fill="#475569">18</text><text x="255" y="58" font-size="11" font-weight="700" fill="#475569">12</text><text x="350" y="58" font-size="11" font-weight="800" fill="#0f172a">30</text>
            <text x="60" y="92" font-size="11" font-weight="700" fill="#475569">Women</text><text x="165" y="92" font-size="11" font-weight="700" fill="#475569">22</text><text x="255" y="92" font-size="11" font-weight="700" fill="#475569">28</text><text x="350" y="92" font-size="11" font-weight="800" fill="#0f172a">50</text>
            <text x="60" y="126" font-size="11" font-weight="900" fill="#1e40af">Total</text><text x="165" y="126" font-size="11" font-weight="800" fill="#0f172a">40</text><text x="255" y="126" font-size="11" font-weight="800" fill="#0f172a">40</text><text x="350" y="126" font-size="12" font-weight="900" fill="#059669">80</text>
          </g>"""),
        "golden_rule": "Find the cell with only ONE missing number in its row or column first!",
        "watch_out": "For conditional probability ('Given that the person is a woman...'), divide by the WOMEN TOTAL (50), not the grand total (80)!",
        "challenge_prompt": "Using the table above: What is the probability that a person chosen at random is a man who walks to work?",
        "answer_text": "Men who walk = 12. Grand total = 80. Probability = 12/80 = 3/20 (or 0.15 / 15%)."
    },

    # 46. Scatter Diagrams & Correlation
    {
        "id": "m-l2-46",
        "number": 46,
        "title": "Scatter Diagrams &amp; Correlation",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD43",
        "rule_heading": "Positive • Negative • Zero Correlation",
        "rule_body": "Positive: As X goes up, Y goes up (slopes uphill). Negative: As X goes up, Y goes down (slopes downhill). Zero: Scattered random cloud with no trend.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <line x1="20" y1="100" x2="100" y2="20" stroke="#2563eb" stroke-width="2"/>
            <text x="60" y="112" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">POSITIVE (+)</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fef2f2" stroke="#ef4444"/>
            <line x1="20" y1="20" x2="100" y2="100" stroke="#dc2626" stroke-width="2"/>
            <text x="60" y="112" font-size="10" font-weight="800" fill="#991b1b" text-anchor="middle">NEGATIVE (-)</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
            <circle cx="35" cy="40" r="3" fill="#64748b"/><circle cx="85" cy="35" r="3" fill="#64748b"/><circle cx="50" cy="80" r="3" fill="#64748b"/><circle cx="95" cy="75" r="3" fill="#64748b"/>
            <text x="60" y="112" font-size="10" font-weight="800" fill="#475569" text-anchor="middle">NO CORRELATION</text>
          </g>"""),
        "golden_rule": "Draw a line of best fit with an equal balance of points above and below the line!",
        "watch_out": "Correlation does NOT prove causation! (e.g. ice cream sales and sunburn both correlate with hot weather).",
        "challenge_prompt": "Describe the relationship between temperature and heating fuel consumption: As temperature rises, heating fuel usage drops.",
        "answer_text": "Negative correlation (as temperature increases, heating fuel used decreases)."
    },

    # 47. Interpolation vs Extrapolation
    {
        "id": "m-l2-47",
        "number": 47,
        "title": "Interpolation vs Extrapolation",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD44",
        "rule_heading": "Inside Range (Reliable) vs Beyond (Unreliable)",
        "rule_body": "Interpolation: Estimating a value INSIDE the given data range (Reliable). Extrapolation: Extending line of best fit BEYOND the data points (Unreliable / Risky).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">INTERPOLATION</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">Within tested range</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#475569">e.g. data for 10–50 yrs</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#16a34a"/>
            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">RELIABLE PREDICTION</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="90" y="26" font-size="12" font-weight="800" fill="#b91c1c" text-anchor="middle">EXTRAPOLATION</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">Outside data range</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#475569">Predicting at 90 yrs</text>
            <rect x="15" y="92" width="150" height="24" rx="4" fill="#dc2626"/>
            <text x="90" y="108" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">UNRELIABLE / RISKY</text>
          </g>"""),
        "golden_rule": "Predictions outside the original data range are UNRELIABLE because trends may flatten or reverse!",
        "watch_out": "Examiners will ask 'Why might this prediction be unreliable?' — answer: 'It is extrapolated beyond the data range.'",
        "challenge_prompt": "A company measures sales between 2018 and 2023. They predict sales for 2035 using their line of best fit. Is this reliable?",
        "answer_text": "No, it is unreliable because 2035 is an extrapolation far beyond the recorded data range, and market conditions may change."
    },

    # 48. Pie Charts: Angles & Frequencies
    {
        "id": "m-l2-48",
        "number": 48,
        "title": "Pie Charts: Angles &amp; Frequencies",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD45",
        "rule_heading": "Angle = (Value ÷ Total) × 360°",
        "rule_body": "Total degrees in any circle = 360°. Degrees per item = 360° ÷ Total Frequency. To find angle for a category: Multiply its frequency by degrees per item.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <circle cx="65" cy="65" r="55" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
            <path d="M 65,65 L 65,10 A 55,55 0 0,1 120,65 Z" fill="#93c5fd"/>
            <text x="85" y="45" font-size="11" font-weight="800" fill="#1e3a8a">90°</text>
            <text x="65" y="95" font-size="11" font-weight="800" fill="#1e3a8a" text-anchor="middle">270°</text>
          </g>
          <g transform="translate(210, 30)">
            <rect x="0" y="0" width="210" height="100" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="105" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Degrees per 1 item:</text>
            <text x="105" y="50" font-size="13" font-weight="900" fill="#2563eb" text-anchor="middle">360° ÷ Total Frequency</text>
            <text x="105" y="78" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">e.g. 360° ÷ 72 people = 5° each</text>
          </g>"""),
        "golden_rule": "Sum of all pie chart sector angles MUST equal exactly 360°!",
        "watch_out": "A pie chart only shows PROPORTIONS, not raw quantities, unless the total sample size is given!",
        "challenge_prompt": "In a survey of 120 hospital patients, 45 travelled by bus. What angle should represent bus travel on a pie chart?",
        "answer_text": "Degrees per patient = 360° ÷ 120 = 3° per patient. Bus angle = 45 × 3° = 135°."
    },

    # 49. Dual & Grouped Bar Charts
    {
        "id": "m-l2-49",
        "number": 49,
        "title": "Dual &amp; Grouped Bar Charts",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD46",
        "rule_heading": "Side-by-Side Comparison with Key",
        "rule_body": "Dual bar charts place two bars side-by-side for each category to compare groups (e.g. Male vs Female, 2023 vs 2024). Always check the legend key and vertical axis scale.",
        "svg_html": wrap_svg("""
          <g transform="translate(50, 15)">
            <line x1="20" y1="120" x2="360" y2="120" stroke="#334155" stroke-width="2"/>
            <line x1="20" y1="20" x2="20" y2="120" stroke="#334155" stroke-width="2"/>
            <rect x="60" y="50" width="30" height="70" fill="#3b82f6"/>
            <rect x="92" y="30" width="30" height="90" fill="#10b981"/>
            <rect x="180" y="65" width="30" height="55" fill="#3b82f6"/>
            <rect x="212" y="45" width="30" height="75" fill="#10b981"/>
            <text x="91" y="135" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Quarter 1</text>
            <text x="211" y="135" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Quarter 2</text>
            <rect x="280" y="30" width="12" height="12" fill="#3b82f6"/>
            <text x="300" y="40" font-size="10" font-weight="700" fill="#0f172a">2023</text>
            <rect x="280" y="55" width="12" height="12" fill="#10b981"/>
            <text x="300" y="65" font-size="10" font-weight="700" fill="#0f172a">2024</text>
          </g>"""),
        "golden_rule": "Read the key carefully to avoid mixing up years or cohorts!",
        "watch_out": "Check the vertical axis scale increments — each grid square may represent 2, 5, 10, or 20 units.",
        "challenge_prompt": "In Quarter 1: 2023 sales were £35k, 2024 sales were £45k. What was the percentage increase from 2023 to 2024?",
        "answer_text": "Increase = £45k - £35k = £10k. % Increase = (10 ÷ 35) × 100 = 28.57% (or 28.6%)."
    },

    # 50. Misleading Graphs & Traps
    {
        "id": "m-l2-50",
        "number": 50,
        "title": "Misleading Graphs &amp; Traps",
        "subject": "maths",
        "level": "l2",
        "subject_label": "Maths",
        "level_label": "Level 2",
        "strand_name": "Handling Data",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.HD47",
        "rule_heading": "Non-Zero Baselines &amp; Uneven Scales",
        "rule_body": "Common tricks used to deceive: 1. Broken vertical axis (not starting at 0) exaggerates tiny differences. 2. Unequal scale increments. 3. 3D distortion making front slices look bigger.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="90" y="24" font-size="11" font-weight="800" fill="#b91c1c" text-anchor="middle">MISLEADING (Truncated)</text>
            <text x="15" y="50" font-size="10" font-weight="700" fill="#0f172a">Y-axis starts at 90%</text>
            <rect x="40" y="80" width="30" height="35" fill="#dc2626"/>
            <rect x="90" y="60" width="30" height="55" fill="#dc2626"/>
            <text x="90" y="115" font-size="9" font-weight="800" fill="#dc2626" text-anchor="middle">Looks like 2x difference!</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">HONEST (Starts at 0)</text>
            <text x="15" y="50" font-size="10" font-weight="700" fill="#0f172a">Y-axis starts at 0%</text>
            <rect x="40" y="65" width="30" height="50" fill="#16a34a"/>
            <rect x="90" y="62" width="30" height="53" fill="#16a34a"/>
            <text x="90" y="115" font-size="9" font-weight="800" fill="#15803d" text-anchor="middle">Shows true 92% vs 95%</text>
          </g>"""),
        "golden_rule": "Always check if the vertical axis starts at ZERO (0)!",
        "watch_out": "A graph that looks dramatic often only represents a 1% or 2% actual difference.",
        "challenge_prompt": "Explain one way a bar chart comparing company satisfaction could be misleading if one bar appears 4 times taller than another.",
        "answer_text": "The vertical axis does not start at zero (truncated/broken axis), which exaggerates the visual difference between the bars."
    }
]

if __name__ == "__main__":
    with open('decks/maths_l2/strand_c.py', 'w') as f:
        f.write('\"\"\"Strand C: Handling Information and Data (Cards 37-50)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS, indent=2, width=120) + '\n')
    print(f"Successfully generated Strand C ({len(CARDS)} cards)!")
