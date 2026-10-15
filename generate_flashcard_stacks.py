import os

def render_flashcard_stack_svg(
    subject_title="MATHEMATICS",
    level_str="LEVEL 2",
    accent_color="#38bdf8",
    box_color=("#002855", "#001833"),
    card_count="64 POCKET CARDS",
    cards_data=[
        {
            "tag": "MEASURE, SHAPE & SPACE",
            "tag_bg": "#0284c7",
            "title": "Trapezium Area & Volume",
            "formula": "Area = ((a + b) / 2) × h",
            "tip": "⚠ Add parallel sides (a+b) FIRST before multiplying by height!",
            "num": "Card 28 of 64"
        },
        {
            "tag": "NUMBER & PERCENTAGES",
            "tag_bg": "#059669",
            "title": "Percentage Change Formula",
            "formula": "% Change = (Actual Difference / Original) × 100%",
            "num": "Card 19 of 64"
        },
        {
            "tag": "HANDLING DATA",
            "tag_bg": "#7c3aed",
            "title": "Mean from Frequency Table",
            "formula": "Estimated Mean = Σ(Midpoint × Frequency) / Σ(Frequency)",
            "num": "Card 42 of 64"
        },
        {
            "tag": "RATIO & PROPORTION",
            "tag_bg": "#d97706",
            "title": "Sharing into a Given Ratio (3:2)",
            "formula": "1) Add parts (3+2=5)  2) Divide total  3) Multiply",
            "num": "Card 08 of 64"
        }
    ]
):
    top_c = cards_data[0]
    c2 = cards_data[1]
    c3 = cards_data[2]
    c4 = cards_data[3]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 440" width="620" height="440">
  <defs>
    <!-- Background Shadow -->
    <filter id="stackShadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#070d1e" flood-opacity="0.38"/>
    </filter>
    <filter id="cardDropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="8" stdDeviation="8" flood-color="#070d1e" flood-opacity="0.22"/>
    </filter>
    <filter id="boxDropShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="-6" dy="16" stdDeviation="14" flood-color="#070d1e" flood-opacity="0.45"/>
    </filter>

    <!-- Box Gradients -->
    <linearGradient id="boxGradMain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{box_color[0]}"/>
      <stop offset="100%" stop-color="{box_color[1]}"/>
    </linearGradient>
    <linearGradient id="boxLidGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="goldSheen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="cardFrontBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="85%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <linearGradient id="deckEdgeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="30%" stop-color="#f1f5f9"/>
      <stop offset="70%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>

  <!-- AMBIENT BASE GROUND SHADOW -->
  <ellipse cx="310" cy="405" rx="270" ry="22" fill="#070d1e" opacity="0.22" filter="blur(8px)"/>

  <!-- ========================================== -->
  <!-- LEFT: 3D FLASHCARD DECK PACKAGING BOX      -->
  <!-- ========================================== -->
  <g transform="translate(35, 60)" filter="url(#boxDropShadow)">
    <!-- Main Box Body -->
    <rect x="0" y="20" width="180" height="290" rx="14" fill="url(#boxGradMain)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>

    <!-- 3D Perspective Box Side Edge -->
    <path d="M 180 28 L 202 12 L 202 292 L 180 310 Z" fill="#001226" stroke="rgba(255,255,255,0.08)"/>

    <!-- Gold Foil Top Lid Strip -->
    <path d="M 0 28 Q 90 38 180 28 L 180 62 L 0 62 Z" fill="url(#boxLidGrad)"/>
    <path d="M 180 28 L 202 12 L 202 46 L 180 62 Z" fill="#b45309"/>

    <!-- Box Header Branding -->
    <text x="90" y="48" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" letter-spacing="1.5" fill="#070d1e" text-anchor="middle">MASTER FUNCTIONAL SKILLS</text>

    <!-- Box Level Badge -->
    <g transform="translate(25, 85)">
      <rect x="0" y="0" width="130" height="26" rx="13" fill="{accent_color}"/>
      <text x="65" y="17" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#070d1e" text-anchor="middle">{level_str}</text>
    </g>

    <!-- Box Title -->
    <g transform="translate(18, 145)">
      <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="20" font-weight="900" fill="#ffffff" letter-spacing="0.5">{subject_title}</text>
      <text x="0" y="20" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" letter-spacing="1">POCKET REVISION</text>
      <text x="0" y="34" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" letter-spacing="1">FLASHCARDS</text>
    </g>

    <!-- Card Count Pill -->
    <g transform="translate(25, 215)">
      <rect x="0" y="0" width="130" height="28" rx="6" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
      <text x="65" y="18" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">★ {card_count} ★</text>
    </g>

    <!-- Bottom Features -->
    <g transform="translate(18, 275)">
      <text x="72" y="0" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="rgba(255,255,255,0.8)" text-anchor="middle">Double-Sided • Formulas</text>
      <text x="72" y="14" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="rgba(255,255,255,0.8)" text-anchor="middle">Color-Coded Topic Strands</text>
    </g>

    <!-- Glossy Box Sheen Line -->
    <path d="M 0 62 L 60 62 L 0 160 Z" fill="#ffffff" opacity="0.06"/>
  </g>

  <!-- ========================================== -->
  <!-- RIGHT: THICK 3D CASCADING CARD STACK       -->
  <!-- ========================================== -->

  <!-- 1. The Block of Paper Deck Underneath (Stack Depth) -->
  <g transform="translate(260, 240)">
    <!-- 3D Card Edge Thickness Block -->
    <path d="M 12 110 L 320 110 L 338 128 L 30 128 Z" fill="url(#deckEdgeGrad)" filter="url(#cardDropShadow)"/>
    <line x1="30" y1="113" x2="322" y2="113" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="30" y1="117" x2="324" y2="117" stroke="#cbd5e1" stroke-width="0.8"/>
    <line x1="30" y1="121" x2="328" y2="121" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="30" y1="125" x2="334" y2="125" stroke="#cbd5e1" stroke-width="0.8"/>
  </g>

  <!-- 2. Stack Card 4 (Deepest Back Card) -->
  <g transform="translate(275, 45)" filter="url(#cardDropShadow)">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <!-- Colored Category Banner -->
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c4['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c4['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c4['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c4['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c4['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c4['formula']}</text>
  </g>

  <!-- 3. Stack Card 3 (Third Back Card) -->
  <g transform="translate(265, 85)" filter="url(#cardDropShadow)">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c3['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c3['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c3['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c3['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c3['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c3['formula']}</text>
  </g>

  <!-- 4. Stack Card 2 (Second Back Card) -->
  <g transform="translate(255, 125)" filter="url(#cardDropShadow)">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c2['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c2['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c2['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c2['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c2['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c2['formula']}</text>
  </g>

  <!-- 5. Stack Card 1 (TOP FULL HERO CARD) -->
  <g transform="translate(245, 165)" filter="url(#stackShadow)">
    <!-- Card Base -->
    <rect x="0" y="0" width="320" height="205" rx="14" fill="url(#cardFrontBg)" stroke="#cbd5e1" stroke-width="1.5"/>

    <!-- Category Header Strip -->
    <rect x="0" y="0" width="320" height="38" rx="14" fill="{top_c['tag_bg']}"/>
    <rect x="0" y="26" width="320" height="12" fill="{top_c['tag_bg']}"/>

    <!-- Card Brand & Topic -->
    <text x="16" y="24" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#ffffff">{top_c['tag']}</text>
    <text x="304" y="24" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{top_c['num']}</text>

    <!-- Card Content Body -->
    <g transform="translate(18, 56)">
      <!-- Topic Title -->
      <text x="0" y="14" font-family="Montserrat, Arial, sans-serif" font-size="15" font-weight="800" fill="#070d1e">{top_c['title']}</text>
      
      <!-- Key Formula Box -->
      <rect x="0" y="28" width="284" height="42" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
      <text x="142" y="54" font-family="'Courier New', Courier, monospace" font-size="14" font-weight="800" fill="#0369a1" text-anchor="middle">{top_c['formula']}</text>

      <!-- Exam Warning / Golden Rule Note -->
      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="284" height="40" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
        <text x="8" y="16" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="700" fill="#991b1b">EXAM TRAP WARNING:</text>
        <text x="8" y="30" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="#7f1d1d">{top_c['tip']}</text>
      </g>

      <!-- Card Sub-Footer -->
      <g transform="translate(0, 134)">
        <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="8" font-weight="700" letter-spacing="1" fill="#94a3b8">MASTER FUNCTIONAL SKILLS • REVISION DECK</text>
        <circle cx="276" cy="-4" r="5" fill="#22c55e"/>
      </g>
    </g>
  </g>
</svg>
"""

if __name__ == "__main__":
    out_dir = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/img/books"
    # Maths L2
    svg1 = render_flashcard_stack_svg(
        subject_title="MATHEMATICS",
        level_str="LEVEL 2",
        accent_color="#38bdf8",
        box_color=("#002855", "#001833"),
        card_count="64 POCKET CARDS",
        cards_data=[
            {
                "tag": "MEASURE & SHAPE",
                "tag_bg": "#0284c7",
                "title": "Trapezium Area & Volume",
                "formula": "Area = ((a + b) / 2) × h",
                "tip": "Add parallel sides (a+b) FIRST before multiplying by height!",
                "num": "Card 28 of 64"
            },
            {
                "tag": "NUMBER & RATIO",
                "tag_bg": "#059669",
                "title": "Percentage Change",
                "formula": "% Change = (Difference / Original) × 100%",
                "num": "Card 19 of 64"
            },
            {
                "tag": "HANDLING DATA",
                "tag_bg": "#7c3aed",
                "title": "Mean from Frequency Table",
                "formula": "Mean = Σ(Midpoint × f) / Σf",
                "num": "Card 42 of 64"
            },
            {
                "tag": "PROBABILITY",
                "tag_bg": "#d97706",
                "title": "Combined Independent Events",
                "formula": "P(A and B) = P(A) × P(B)",
                "num": "Card 08 of 64"
            }
        ]
    )
    with open(os.path.join(out_dir, "flashcards_maths_l2.svg"), "w") as f:
        f.write(svg1)

    # English L2
    svg2 = render_flashcard_stack_svg(
        subject_title="ENGLISH",
        level_str="LEVEL 2",
        accent_color="#fbbf24",
        box_color=("#1e1b4b", "#0f172a"),
        card_count="64 POCKET CARDS",
        cards_data=[
            {
                "tag": "WRITING FORMATS",
                "tag_bg": "#4338ca",
                "title": "Formal Letter Structure",
                "formula": "Sender ➔ Date ➔ Recipient ➔ Salutation ➔ Body ➔ Sign-off",
                "tip": "'Dear Sir/Madam' ends with 'Yours faithfully'. Named person: 'Yours sincerely'.",
                "num": "Card 14 of 64"
            },
            {
                "tag": "PERSUASIVE RHETORIC",
                "tag_bg": "#b45309",
                "title": "DAFOREST Devices",
                "formula": "Direct Address, Alliteration, Facts, Opinions, Rhetorical Q...",
                "num": "Card 23 of 64"
            },
            {
                "tag": "SPaG MASTERY",
                "tag_bg": "#047857",
                "title": "Semicolon vs Comma Splice",
                "formula": "Use semicolon (;) to link 2 independent clauses without 'and'.",
                "num": "Card 39 of 64"
            },
            {
                "tag": "READING TECHNIQUES",
                "tag_bg": "#be123c",
                "title": "Detecting Bias vs Fact",
                "formula": "Look for emotive language, selective evidence, and author stance.",
                "num": "Card 06 of 64"
            }
        ]
    )
    with open(os.path.join(out_dir, "flashcards_english_l2.svg"), "w") as f:
        f.write(svg2)

    # Maths L1
    svg3 = render_flashcard_stack_svg(
        subject_title="MATHEMATICS",
        level_str="LEVEL 1",
        accent_color="#34d399",
        box_color=("#064e3b", "#022c22"),
        card_count="54 POCKET CARDS",
        cards_data=[
            {
                "tag": "FRACTIONS & DECIMALS",
                "tag_bg": "#059669",
                "title": "Fractions of Amounts",
                "formula": "Divide by Denominator, Multiply by Numerator",
                "tip": "3/4 of £240: 240 ÷ 4 = 60, then 60 × 3 = £180.",
                "num": "Card 12 of 54"
            },
            {
                "tag": "PERIMETER & AREA",
                "tag_bg": "#0284c7",
                "title": "Rectangle Perimeter & Area",
                "formula": "Perimeter = 2(L + W)  |  Area = Length × Width",
                "num": "Card 21 of 54"
            },
            {
                "tag": "METRIC CONVERSIONS",
                "tag_bg": "#d97706",
                "title": "Weight & Capacity Units",
                "formula": "1 kg = 1000 g  |  1 L = 1000 ml  |  1 m = 100 cm",
                "num": "Card 33 of 54"
            },
            {
                "tag": "NUMBER OPERATIONS",
                "tag_bg": "#7c3aed",
                "title": "Simple Ratio Sharing (2:1)",
                "formula": "Add parts: 2+1=3. Divide total by 3, multiply by 2 and 1.",
                "num": "Card 05 of 54"
            }
        ]
    )
    with open(os.path.join(out_dir, "flashcards_maths_l1.svg"), "w") as f:
        f.write(svg3)

    print("[OK] Generated stunning 3D flashcard stack SVGs!")
