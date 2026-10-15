import os
import html

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
BOOKS_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
os.makedirs(BOOKS_DIR, exist_ok=True)

def esc(s):
    if s is None:
        return ""
    return html.escape(str(s), quote=True)

def create_pfs_style_stack(
    subject="MATHS",
    level_str="LEVEL 2",
    accent="#38bdf8",
    box_grad=("#002855", "#001428"),
    card_count="64",
    center_card=None,
    left_card=None,
    right_card=None
):
    center_card = center_card or {}
    left_card = left_card or {}
    right_card = right_card or {}

    subject_esc = esc(subject)
    level_str_esc = esc(level_str)
    card_count_esc = esc(card_count)

    # Center Card details
    c_title = esc(center_card.get("title", "Trapezium Area & Volume"))
    c_strand = esc(center_card.get("strand", "MEASURE & SHAPE"))
    c_color = center_card.get("color", "#0284c7")
    c_num = esc(center_card.get("num", "Card 28 of 64"))
    c_formula = esc(center_card.get("formula", "Area = ((a + b) / 2) × h"))
    c_calc = esc(center_card.get("calc", "((6 + 10) / 2) × 5 = 8 × 5 = 40 cm²"))
    c_trap = esc(center_card.get("trap", "Add (a+b) FIRST before multiplying by height!"))

    # Left Card details
    l_strand = esc(left_card.get("strand", "NUMBER & RATIO"))
    l_color = left_card.get("color", "#059669")
    l_title = esc(left_card.get("title", "Percentage Change"))
    l_formula = esc(left_card.get("formula", "(Difference / Original) × 100%"))

    # Right Card details
    r_strand = esc(right_card.get("strand", "HANDLING DATA"))
    r_color = right_card.get("color", "#7c3aed")
    r_title = esc(right_card.get("title", "Averages & Range"))
    r_formula = esc(right_card.get("formula", "Mean = Total ÷ Count"))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 540" width="740" height="540">
  <defs>
    <!-- Realistic Multi-Stage Drop Shadows -->
    <filter id="groundShadow" x="-20%" y="-20%" width="140%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="16"/>
      <feOffset dx="0" dy="24" result="offsetblur"/>
      <feFlood flood-color="#070d1e" flood-opacity="0.32"/>
      <feComposite in2="offsetblur" operator="in"/>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="boxShadow" x="-30%" y="-20%" width="160%" height="150%">
      <feDropShadow dx="-8" dy="20" stdDeviation="18" flood-color="#070d1e" flood-opacity="0.45"/>
    </filter>

    <filter id="cardShadowSoft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="3" dy="12" stdDeviation="12" flood-color="#070d1e" flood-opacity="0.25"/>
    </filter>

    <filter id="heroCardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#070d1e" flood-opacity="0.38"/>
    </filter>

    <!-- Box Gradients -->
    <linearGradient id="boxGrad_{level_str.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{box_grad[0]}"/>
      <stop offset="100%" stop-color="{box_grad[1]}"/>
    </linearGradient>

    <linearGradient id="goldLidGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>

    <linearGradient id="cardStockGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="90%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>

    <linearGradient id="deckEdgeBlock" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="25%" stop-color="#f1f5f9"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="85%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>

  <!-- AMBIENT BASE GROUND CONTACT SHADOW -->
  <ellipse cx="370" cy="495" rx="340" ry="24" fill="#070d1e" opacity="0.25" filter="blur(10px)"/>

  <!-- ============================================== -->
  <!-- 1. STANDING PACKAGING TUCK-BOX (REAR CENTER)   -->
  <!-- ============================================== -->
  <g transform="translate(180, 45)" filter="url(#boxShadow)">
    <!-- 3D Left Perspective Edge -->
    <path d="M 0 35 L -36 14 L -36 304 L 0 325 Z" fill="#001020" stroke="rgba(255,255,255,0.06)"/>
    <text x="-160" y="-14" transform="rotate(-90)" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="800" letter-spacing="2" fill="rgba(255,255,255,0.4)">{subject_esc} {level_str_esc} REVISION CARDS</text>

    <!-- Main Front Box Face -->
    <rect x="0" y="24" width="220" height="305" rx="14" fill="url(#boxGrad_{level_str.replace(' ', '')})" stroke="rgba(255,255,255,0.18)" stroke-width="1.5"/>

    <!-- Gold Foil Top Lid Strip -->
    <path d="M 0 24 Q 110 36 220 24 L 220 66 L 0 66 Z" fill="url(#goldLidGrad)"/>
    <path d="M 0 24 L -36 14 L -36 48 L 0 66 Z" fill="#b45309"/>

    <text x="110" y="50" font-family="Montserrat, Arial, sans-serif" font-size="10.5" font-weight="900" letter-spacing="2" fill="#070d1e" text-anchor="middle">MASTER FUNCTIONAL SKILLS</text>

    <!-- Box Level Badge -->
    <g transform="translate(35, 90)">
      <rect x="0" y="0" width="150" height="30" rx="15" fill="{accent}"/>
      <text x="75" y="20" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="900" letter-spacing="1.5" fill="#070d1e" text-anchor="middle">{level_str_esc}</text>
    </g>

    <!-- Box Subject Title -->
    <g transform="translate(20, 155)">
      <text x="90" y="0" font-family="Montserrat, Arial, sans-serif" font-size="25" font-weight="900" fill="#ffffff" letter-spacing="0.5" text-anchor="middle">{subject_esc}</text>
      <text x="90" y="24" font-family="Montserrat, Arial, sans-serif" font-size="13" font-weight="800" fill="{accent}" letter-spacing="1.5" text-anchor="middle">POCKET REVISION CARDS</text>
    </g>

    <!-- 64 Cards Deck Pill -->
    <g transform="translate(30, 215)">
      <rect x="0" y="0" width="160" height="32" rx="8" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.22)" stroke-width="1.2"/>
      <text x="80" y="21" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#ffffff" text-anchor="middle">★ {card_count_esc} REVISION CARDS ★</text>
    </g>

    <!-- Features Subtitle -->
    <g transform="translate(20, 275)">
      <text x="90" y="0" font-family="'Open Sans', Arial, sans-serif" font-size="9" font-weight="600" fill="rgba(255,255,255,0.85)" text-anchor="middle">Formulas • Step Models • Trap Warnings</text>
      <text x="90" y="14" font-family="'Open Sans', Arial, sans-serif" font-size="9" font-weight="600" fill="rgba(255,255,255,0.85)" text-anchor="middle">Ofqual Regulated Specification</text>
    </g>

    <!-- Specular Highlight Sheen -->
    <path d="M 0 66 L 75 66 L 0 190 Z" fill="#ffffff" opacity="0.05"/>
  </g>

  <!-- ============================================== -->
  <!-- 2. THICK PAPER CARDSTOCK BLOCK (STACK DEPTH)   -->
  <!-- ============================================== -->
  <g transform="translate(195, 395)" filter="url(#cardShadowSoft)">
    <path d="M 0 75 L 360 75 L 385 105 L 25 105 Z" fill="url(#deckEdgeBlock)"/>
    <line x1="25" y1="80" x2="363" y2="80" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="25" y1="85" x2="367" y2="85" stroke="#cbd5e1" stroke-width="0.8"/>
    <line x1="25" y1="90" x2="371" y2="90" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="25" y1="95" x2="376" y2="95" stroke="#cbd5e1" stroke-width="0.8"/>
    <line x1="25" y1="100" x2="381" y2="100" stroke="#94a3b8" stroke-width="0.8"/>
  </g>

  <!-- ============================================== -->
  <!-- 3. LEFT FANNED REVISION CARD (ANGLED -15°)     -->
  <!-- ============================================== -->
  <g transform="translate(110, 205) rotate(-14)" filter="url(#cardShadowSoft)">
    <rect x="0" y="0" width="290" height="190" rx="12" fill="url(#cardStockGrad)" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="290" height="34" rx="12" fill="{l_color}"/>
    <rect x="0" y="24" width="290" height="10" fill="{l_color}"/>
    <text x="14" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{l_strand}</text>
    <text x="276" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">Card 14</text>
    <g transform="translate(16, 52)">
      <text x="0" y="14" font-family="Montserrat, Arial, sans-serif" font-size="13" font-weight="800" fill="#0f172a">{l_title}</text>
      <rect x="0" y="26" width="258" height="36" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="129" y="49" font-family="'Courier New', monospace" font-size="11.5" font-weight="800" fill="{l_color}" text-anchor="middle">{l_formula}</text>
      <text x="0" y="85" font-family="'Open Sans', sans-serif" font-size="9.5" fill="#64748b">Turn over for exam-style question ➔</text>
    </g>
  </g>

  <!-- ============================================== -->
  <!-- 4. RIGHT FANNED REVISION CARD (ANGLED +15°)    -->
  <!-- ============================================== -->
  <g transform="translate(370, 160) rotate(13)" filter="url(#cardShadowSoft)">
    <rect x="0" y="0" width="290" height="190" rx="12" fill="url(#cardStockGrad)" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="290" height="34" rx="12" fill="{r_color}"/>
    <rect x="0" y="24" width="290" height="10" fill="{r_color}"/>
    <text x="14" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{r_strand}</text>
    <text x="276" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">Card 42</text>
    <g transform="translate(16, 52)">
      <text x="0" y="14" font-family="Montserrat, Arial, sans-serif" font-size="13" font-weight="800" fill="#0f172a">{r_title}</text>
      <rect x="0" y="26" width="258" height="36" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="129" y="49" font-family="'Courier New', monospace" font-size="11.5" font-weight="800" fill="{r_color}" text-anchor="middle">{r_formula}</text>
      <text x="0" y="85" font-family="'Open Sans', sans-serif" font-size="9.5" fill="#64748b">Turn over for exam-style question ➔</text>
    </g>
  </g>

  <!-- ============================================== -->
  <!-- 5. CENTER FRONT HERO REVISION CARD (MAIN VIEW) -->
  <!-- ============================================== -->
  <g transform="translate(205, 235) rotate(-2)" filter="url(#heroCardShadow)">
    <!-- Base Card Body -->
    <rect x="0" y="0" width="345" height="235" rx="14" fill="url(#cardStockGrad)" stroke="#94a3b8" stroke-width="1.8"/>

    <!-- Category Header Strip -->
    <rect x="0" y="0" width="345" height="42" rx="14" fill="{c_color}"/>
    <rect x="0" y="28" width="345" height="14" fill="{c_color}"/>

    <text x="18" y="27" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#ffffff">{c_strand}</text>
    <text x="327" y="27" font-family="Montserrat, Arial, sans-serif" font-size="9.5" font-weight="800" fill="#ffffff" text-anchor="end">{c_num}</text>

    <!-- Card Inner Content -->
    <g transform="translate(20, 60)">
      <!-- Topic Title -->
      <text x="0" y="16" font-family="Montserrat, Arial, sans-serif" font-size="16" font-weight="900" fill="#070d1e">{c_title}</text>

      <!-- Key Formula Box with Diagram Icon -->
      <rect x="0" y="28" width="305" height="46" rx="8" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.2"/>
      <text x="152" y="56" font-family="'Courier New', Courier, monospace" font-size="15" font-weight="900" fill="#0369a1" text-anchor="middle">{c_formula}</text>

      <!-- Worked Calculation Example -->
      <g transform="translate(0, 84)">
        <rect x="0" y="0" width="305" height="30" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
        <text x="10" y="19" font-family="'Courier New', Courier, monospace" font-size="10.5" font-weight="800" fill="#334155">Example: {c_calc}</text>
      </g>

      <!-- Exam Trap Warning Note -->
      <g transform="translate(0, 122)">
        <rect x="0" y="0" width="305" height="34" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
        <text x="10" y="15" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="800" fill="#991b1b">EXAM TRAP WARNING:</text>
        <text x="10" y="27" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="#7f1d1d">{c_trap}</text>
      </g>

      <!-- Card Sub-Footer Prompt -->
      <g transform="translate(0, 166)">
        <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="8.5" font-weight="800" letter-spacing="0.5" fill="#64748b">MASTER FUNCTIONAL SKILLS • OFFICIAL REVISION DECK</text>
        <text x="305" y="0" font-family="'Open Sans', sans-serif" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="end">Turn over ➔</text>
      </g>
    </g>
  </g>
</svg>
"""
    return svg

# 1. Maths Level 2
maths_l2_svg = create_pfs_style_stack(
    subject="MATHS",
    level_str="LEVEL 2",
    accent="#38bdf8",
    box_grad=("#002855", "#001428"),
    card_count="64",
    center_card={
        "title": "Trapezium Area & Volume",
        "strand": "MEASURE, SHAPE & SPACE",
        "color": "#0284c7",
        "num": "Card 28 of 64",
        "formula": "Area = ((a + b) / 2) × h",
        "calc": "((6 + 10) / 2) × 5 = 8 × 5 = 40 cm²",
        "trap": "Add parallel sides (a+b) FIRST before multiplying by height!"
    },
    left_card={
        "strand": "NUMBER & RATIO",
        "color": "#059669",
        "title": "Percentage Change",
        "formula": "(Difference / Original) × 100%"
    },
    right_card={
        "strand": "HANDLING DATA",
        "color": "#7c3aed",
        "title": "Mean from Frequency Table",
        "formula": "Estimated Mean = Σ(fx) / Σf"
    }
)

with open(os.path.join(BOOKS_DIR, "flashcards_maths_l2.svg"), "w") as f:
    f.write(maths_l2_svg)

# 2. English Level 2
english_l2_svg = create_pfs_style_stack(
    subject="ENGLISH",
    level_str="LEVEL 2",
    accent="#fbbf24",
    box_grad=("#1e1b4b", "#0f172a"),
    card_count="64",
    center_card={
        "title": "Formal Letter Framework",
        "strand": "WRITING FORMATS",
        "color": "#4338ca",
        "num": "Card 14 of 64",
        "formula": "Sender ➔ Date ➔ Recipient ➔ Salutation ➔ Body ➔ Sign-off",
        "calc": "Tone: Objective, authoritative & professional",
        "trap": "'Dear Sir/Madam' ends 'Yours faithfully'. Named person: 'Yours sincerely'."
    },
    left_card={
        "strand": "PERSUASIVE RHETORIC",
        "color": "#b45309",
        "title": "DAFOREST Devices",
        "formula": "Direct Address, Facts, Opinions, Rhetorical Q..."
    },
    right_card={
        "strand": "PUNCTUATION & GRAMMAR",
        "color": "#047857",
        "title": "Semicolon vs Comma Splice",
        "formula": "Link 2 independent clauses without 'and'"
    }
)

with open(os.path.join(BOOKS_DIR, "flashcards_english_l2.svg"), "w") as f:
    f.write(english_l2_svg)

# 3. Maths Level 1
maths_l1_svg = create_pfs_style_stack(
    subject="MATHS",
    level_str="LEVEL 1",
    accent="#34d399",
    box_grad=("#064e3b", "#022c22"),
    card_count="54",
    center_card={
        "title": "Fractions of Amounts",
        "strand": "FRACTIONS & DECIMALS",
        "color": "#059669",
        "num": "Card 12 of 54",
        "formula": "Divide by bottom, multiply by top",
        "calc": "3/4 of £240: 240 ÷ 4 = 60 ➔ 60 × 3 = £180",
        "trap": "Always divide by the denominator first to find 1 part!"
    },
    left_card={
        "strand": "PERIMETER & AREA",
        "color": "#0284c7",
        "title": "Perimeter of Rectangles",
        "formula": "Perimeter = 2 × (Length + Width)"
    },
    right_card={
        "strand": "METRIC UNITS",
        "color": "#d97706",
        "title": "Metric Conversions",
        "formula": "1 kg = 1000 g  |  1 L = 1000 ml"
    }
)

with open(os.path.join(BOOKS_DIR, "flashcards_maths_l1.svg"), "w") as f:
    f.write(maths_l1_svg)

# 4. Hero Stack Showcase (Hero Deck Visual)
with open(os.path.join(BOOKS_DIR, "flashcards_hero_stack.svg"), "w") as f:
    f.write(maths_l2_svg)

print("[OK] Generated high-fidelity PassFunctionalSkills-style 3D stack SVGs with Master Functional Skills branding!")
