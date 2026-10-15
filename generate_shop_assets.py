import os
import html

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
BOOKS_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
os.makedirs(BOOKS_DIR, exist_ok=True)

def esc(s):
    if s is None:
        return ""
    return html.escape(str(s), quote=True)

def create_book_svg(title_primary, title_sub, level_str, subtitle, badges, accent_color="#fbbf24", bg_gradient=(" #002244", "#003366", "#051329"), knockout="MATHEMATICS", title_primary_size=44, title_sub_size=34):
    badges_xml = "".join([f'<rect x="{35 + i*105}" y="490" width="98" height="28" rx="6" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/><text x="{84 + i*105}" y="508" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">{esc(b)}</text>' for i, b in enumerate(badges[:4])])
    
    title_primary = esc(title_primary)
    title_sub = esc(title_sub)
    level_str = esc(level_str)
    subtitle = esc(subtitle)
    knockout = esc(knockout)
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 680" width="500" height="680">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_gradient[0]}"/>
      <stop offset="60%" stop-color="{bg_gradient[1]}"/>
      <stop offset="100%" stop-color="{bg_gradient[2]}"/>
    </linearGradient>
    <linearGradient id="spineShadow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.6"/>
      <stop offset="3%" stop-color="#000000" stop-opacity="0.1"/>
      <stop offset="6%" stop-color="#ffffff" stop-opacity="0.15"/>
      <stop offset="9%" stop-color="#000000" stop-opacity="0.25"/>
      <stop offset="15%" stop-color="#000000" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="8" dy="16" stdDeviation="16" flood-color="#070d1e" flood-opacity="0.4"/>
    </filter>
  </defs>

  <g filter="url(#cardShadow)">
    <!-- Book Cover Base -->
    <rect x="15" y="15" width="470" height="650" rx="14" fill="url(#bgGrad)" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>

    <!-- Subtle Ambient Top Light -->
    <circle cx="450" cy="50" r="160" fill="url(#goldGrad)" opacity="0.08"/>

    <!-- Header Brand Strip -->
    <g transform="translate(45, 45)">
      <text x="0" y="24" font-family="Montserrat, Arial, sans-serif" font-size="14" font-weight="900" letter-spacing="3" fill="#ffffff" opacity="0.95">MASTER FUNCTIONAL SKILLS</text>
      <text x="0" y="44" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="700" letter-spacing="1.5" fill="{accent_color}">OFFICIAL OFQUAL SPECIFICATION</text>
      
      <!-- Level Badge -->
      <rect x="300" y="6" width="110" height="32" rx="16" fill="{accent_color}"/>
      <text x="355" y="27" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="900" letter-spacing="1" fill="#070d1e" text-anchor="middle">{level_str}</text>
    </g>

    <!-- Edition Pill -->
    <rect x="45" y="115" width="280" height="24" rx="4" fill="rgba(0,0,0,0.3)" stroke="{accent_color}" stroke-width="1.2"/>
    <text x="55" y="131" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="800" letter-spacing="1" fill="{accent_color}">CORE REVISION GUIDE • MODEL ANSWERS</text>

    <!-- Knockout Graphic Word -->
    <g transform="translate(45, 170)">
      <text x="0" y="70" font-family="'Oswald', Impact, sans-serif" font-size="74" font-weight="700" letter-spacing="4" fill="rgba(255,255,255,0.07)">{knockout}</text>
    </g>

    <!-- Main Title -->
    <g transform="translate(45, 290)">
      <text x="0" y="55" font-family="Montserrat, Arial, sans-serif" font-size="{title_primary_size}" font-weight="900" line-height="0.95" letter-spacing="0.5" fill="{accent_color}">{title_primary}</text>
      <text x="0" y="105" font-family="Montserrat, Arial, sans-serif" font-size="{title_sub_size}" font-weight="900" fill="#ffffff">{title_sub}</text>
      <text x="0" y="145" font-family="'Open Sans', Arial, sans-serif" font-size="15" font-weight="600" fill="rgba(255,255,255,0.85)">{subtitle}</text>
    </g>

    <!-- Features Badges -->
    <g>
      {badges_xml}
    </g>

    <!-- Footer Trust Info -->
    <line x1="45" y1="590" x2="455" y2="590" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <g transform="translate(45, 620)">
      <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" letter-spacing="1" fill="rgba(255,255,255,0.75)">PEARSON EDEXCEL &amp; CITY &amp; GUILDS ALIGNED</text>
      <text x="410" y="0" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" letter-spacing="1" fill="{accent_color}" text-anchor="end">2026/2027 EDITION</text>
    </g>

    <!-- 3D Book Spine Effect -->
    <rect x="15" y="15" width="40" height="650" rx="14" fill="url(#spineShadow)" pointer-events="none"/>
    <line x1="38" y1="15" x2="38" y2="665" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" pointer-events="none"/>
  </g>
</svg>
"""

def render_flashcard_stack_svg(
    subject_title="MATHEMATICS",
    level_str="LEVEL 2",
    accent_color="#38bdf8",
    box_color=("#002855", "#001833"),
    card_count="64 POCKET CARDS",
    cards_data=None
):
    if cards_data is None:
        cards_data = [
            {"tag": "TOPIC 1", "tag_bg": "#0284c7", "title": "Formula 1", "formula": "Formula definition", "tip": "Watch out for units", "num": "Card 1"},
            {"tag": "TOPIC 2", "tag_bg": "#059669", "title": "Formula 2", "formula": "Formula definition", "num": "Card 2"},
            {"tag": "TOPIC 3", "tag_bg": "#7c3aed", "title": "Formula 3", "formula": "Formula definition", "num": "Card 3"},
            {"tag": "TOPIC 4", "tag_bg": "#d97706", "title": "Formula 4", "formula": "Formula definition", "num": "Card 4"}
        ]
    top_c = cards_data[0]
    c2 = cards_data[1]
    c3 = cards_data[2]
    c4 = cards_data[3]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 440" width="620" height="440">
  <defs>
    <filter id="stackShadow_{level_str.replace(' ', '')}" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#070d1e" flood-opacity="0.38"/>
    </filter>
    <filter id="cardDropShadow_{level_str.replace(' ', '')}" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="8" stdDeviation="8" flood-color="#070d1e" flood-opacity="0.22"/>
    </filter>
    <filter id="boxDropShadow_{level_str.replace(' ', '')}" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="-6" dy="16" stdDeviation="14" flood-color="#070d1e" flood-opacity="0.45"/>
    </filter>

    <linearGradient id="boxGrad_{level_str.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{box_color[0]}"/>
      <stop offset="100%" stop-color="{box_color[1]}"/>
    </linearGradient>
    <linearGradient id="boxLidGrad_{level_str.replace(' ', '')}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="50%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="cardFrontBg_{level_str.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="85%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <linearGradient id="deckEdgeGrad_{level_str.replace(' ', '')}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="30%" stop-color="#f1f5f9"/>
      <stop offset="70%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>

  <!-- Ambient Ground Shadow -->
  <ellipse cx="310" cy="405" rx="270" ry="22" fill="#070d1e" opacity="0.22"/>

  <!-- Left: 3D Packaging Tuck-Box -->
  <g transform="translate(35, 60)" filter="url(#boxDropShadow_{level_str.replace(' ', '')})">
    <rect x="0" y="20" width="180" height="290" rx="14" fill="url(#boxGrad_{level_str.replace(' ', '')})" stroke="rgba(255,255,255,0.2)" stroke-width="1.5"/>
    <path d="M 180 28 L 202 12 L 202 292 L 180 310 Z" fill="#001226" stroke="rgba(255,255,255,0.08)"/>
    <path d="M 0 28 Q 90 38 180 28 L 180 62 L 0 62 Z" fill="url(#boxLidGrad_{level_str.replace(' ', '')})"/>
    <path d="M 180 28 L 202 12 L 202 46 L 180 62 Z" fill="#b45309"/>

    <text x="90" y="48" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" letter-spacing="1.5" fill="#070d1e" text-anchor="middle">MASTER FUNCTIONAL SKILLS</text>

    <g transform="translate(25, 85)">
      <rect x="0" y="0" width="130" height="26" rx="13" fill="{accent_color}"/>
      <text x="65" y="17" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#070d1e" text-anchor="middle">{level_str}</text>
    </g>

    <g transform="translate(18, 145)">
      <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="20" font-weight="900" fill="#ffffff" letter-spacing="0.5">{subject_title}</text>
      <text x="0" y="20" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" letter-spacing="1">POCKET REVISION</text>
      <text x="0" y="34" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" letter-spacing="1">FLASHCARDS</text>
    </g>

    <g transform="translate(25, 215)">
      <rect x="0" y="0" width="130" height="28" rx="6" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
      <text x="65" y="18" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">★ {card_count} ★</text>
    </g>

    <g transform="translate(18, 275)">
      <text x="72" y="0" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="rgba(255,255,255,0.8)" text-anchor="middle">Double-Sided • Formulas</text>
      <text x="72" y="14" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="rgba(255,255,255,0.8)" text-anchor="middle">Color-Coded Topic Strands</text>
    </g>

    <path d="M 0 62 L 60 62 L 0 160 Z" fill="#ffffff" opacity="0.06"/>
  </g>

  <!-- Right: Thick 3D Cascading Card Stack -->
  <g transform="translate(260, 240)">
    <path d="M 12 110 L 320 110 L 338 128 L 30 128 Z" fill="url(#deckEdgeGrad_{level_str.replace(' ', '')})" filter="url(#cardDropShadow_{level_str.replace(' ', '')})"/>
    <line x1="30" y1="113" x2="322" y2="113" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="30" y1="117" x2="324" y2="117" stroke="#cbd5e1" stroke-width="0.8"/>
    <line x1="30" y1="121" x2="328" y2="121" stroke="#94a3b8" stroke-width="0.8"/>
    <line x1="30" y1="125" x2="334" y2="125" stroke="#cbd5e1" stroke-width="0.8"/>
  </g>

  <!-- Card 4 (Deepest Back) -->
  <g transform="translate(275, 45)" filter="url(#cardDropShadow_{level_str.replace(' ', '')})">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c4['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c4['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c4['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c4['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c4['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c4['formula']}</text>
  </g>

  <!-- Card 3 -->
  <g transform="translate(265, 85)" filter="url(#cardDropShadow_{level_str.replace(' ', '')})">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c3['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c3['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c3['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c3['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c3['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c3['formula']}</text>
  </g>

  <!-- Card 2 -->
  <g transform="translate(255, 125)" filter="url(#cardDropShadow_{level_str.replace(' ', '')})">
    <rect x="0" y="0" width="315" height="195" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <rect x="0" y="0" width="315" height="34" rx="12" fill="{c2['tag_bg']}"/>
    <rect x="0" y="24" width="315" height="10" fill="{c2['tag_bg']}"/>
    <text x="16" y="22" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="900" fill="#ffffff">{c2['tag']}</text>
    <text x="300" y="22" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{c2['num']}</text>
    <text x="16" y="58" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="800" fill="#0f172a">{c2['title']}</text>
    <text x="16" y="78" font-family="'Open Sans', Arial, sans-serif" font-size="10.5" font-weight="600" fill="#475569">{c2['formula']}</text>
  </g>

  <!-- Card 1 (Top Hero Card) -->
  <g transform="translate(245, 165)" filter="url(#stackShadow_{level_str.replace(' ', '')})">
    <rect x="0" y="0" width="320" height="205" rx="14" fill="url(#cardFrontBg_{level_str.replace(' ', '')})" stroke="#cbd5e1" stroke-width="1.5"/>

    <rect x="0" y="0" width="320" height="38" rx="14" fill="{top_c['tag_bg']}"/>
    <rect x="0" y="26" width="320" height="12" fill="{top_c['tag_bg']}"/>

    <text x="16" y="24" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" letter-spacing="1" fill="#ffffff">{top_c['tag']}</text>
    <text x="304" y="24" font-family="Montserrat, Arial, sans-serif" font-size="9" font-weight="700" fill="#ffffff" text-anchor="end">{top_c['num']}</text>

    <g transform="translate(18, 56)">
      <text x="0" y="14" font-family="Montserrat, Arial, sans-serif" font-size="15" font-weight="800" fill="#070d1e">{top_c['title']}</text>
      
      <rect x="0" y="28" width="284" height="42" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
      <text x="142" y="54" font-family="'Courier New', Courier, monospace" font-size="13" font-weight="800" fill="#0369a1" text-anchor="middle">{top_c['formula']}</text>

      <g transform="translate(0, 80)">
        <rect x="0" y="0" width="284" height="40" rx="6" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
        <text x="8" y="16" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="700" fill="#991b1b">EXAM TRAP WARNING:</text>
        <text x="8" y="30" font-family="'Open Sans', Arial, sans-serif" font-size="8.5" font-weight="600" fill="#7f1d1d">{top_c.get('tip', 'Remember to show intermediate calculations for full method marks!')}</text>
      </g>

      <g transform="translate(0, 134)">
        <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="8" font-weight="700" letter-spacing="1" fill="#94a3b8">MASTER FUNCTIONAL SKILLS • REVISION DECK</text>
        <circle cx="276" cy="-4" r="5" fill="#22c55e"/>
      </g>
    </g>
  </g>
</svg>
"""

def create_bundle_svg(title, subtitle, accent_color="#f59e0b"):
    title = esc(title)
    subtitle = esc(subtitle)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400" width="500" height="400">
  <defs>
    <linearGradient id="bundleBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a192f"/>
      <stop offset="100%" stop-color="#020c1b"/>
    </linearGradient>
    <filter id="bundleShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#070d1e" flood-opacity="0.45"/>
    </filter>
  </defs>

  <g filter="url(#bundleShadow)">
    <rect x="25" y="25" width="450" height="350" rx="16" fill="url(#bundleBg)" stroke="{accent_color}" stroke-width="2"/>

    <!-- Badge -->
    <rect x="330" y="45" width="120" height="28" rx="14" fill="{accent_color}"/>
    <text x="390" y="64" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="900" fill="#070d1e" text-anchor="middle">COMPLETE PACK</text>

    <!-- Header -->
    <g transform="translate(55, 75)">
      <text x="0" y="0" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="900" letter-spacing="2" fill="#ffffff" opacity="0.9">MASTER FUNCTIONAL SKILLS</text>
      <text x="0" y="45" font-family="Montserrat, Arial, sans-serif" font-size="28" font-weight="900" fill="{accent_color}">{title}</text>
      <text x="0" y="78" font-family="Montserrat, Arial, sans-serif" font-size="18" font-weight="700" fill="#ffffff">{subtitle}</text>
    </g>

    <!-- Bundle Items Icons -->
    <g transform="translate(55, 195)">
      <rect x="0" y="0" width="115" height="110" rx="8" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.15)"/>
      <text x="57" y="45" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" text-anchor="middle">CORE GUIDE</text>
      <text x="57" y="68" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">Full Syllabus</text>
      <text x="57" y="84" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">&amp; Model Answers</text>

      <rect x="130" y="0" width="115" height="110" rx="8" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.15)"/>
      <text x="187" y="45" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" text-anchor="middle">COMPANION</text>
      <text x="187" y="68" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">Practice Drills</text>
      <text x="187" y="84" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">&amp; Workspaces</text>

      <rect x="260" y="0" width="130" height="110" rx="8" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.15)"/>
      <text x="325" y="45" font-family="Montserrat, Arial, sans-serif" font-size="11" font-weight="800" fill="{accent_color}" text-anchor="middle">MOCK PACK</text>
      <text x="325" y="68" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">5 Full Tests</text>
      <text x="325" y="84" font-family="'Open Sans', sans-serif" font-size="9" fill="#ffffff" text-anchor="middle">&amp; Mark Schemes</text>
    </g>

    <text x="55" y="345" font-family="Montserrat, Arial, sans-serif" font-size="10" font-weight="700" letter-spacing="1" fill="rgba(255,255,255,0.6)">FREE FAST TRACKED UK COURIER DELIVERY</text>
  </g>
</svg>
"""

# 1. Maths L2 Core
svg_maths_l2 = create_book_svg(
    title_primary="MATHEMATICS",
    title_sub="CORE STUDY GUIDE",
    level_str="LEVEL 2",
    subtitle="39 Curriculum Standards • Model Solutions",
    badges=["39 Standards", "Sec A Non-Calc", "Sec B Calculator", "Worked Solutions"],
    accent_color="#38bdf8",
    bg_gradient=("#002855", "#003b73", "#001833"),
    knockout="MATHEMATICS"
)
with open(os.path.join(BOOKS_DIR, "maths_l2_core_cover.svg"), "w") as f: f.write(svg_maths_l2)

# 2. Maths L2 Companion
svg_maths_l2_comp = create_book_svg(
    title_primary="MATHEMATICS",
    title_sub="COMPANION WORKBOOK",
    level_str="LEVEL 2",
    subtitle="Exam Problem-Solving Frames & Stepped Drills",
    badges=["120+ Drills", "Step Workspaces", "Method Marks", "Error Traps"],
    accent_color="#38bdf8",
    bg_gradient=("#022c43", "#053f5e", "#011627"),
    knockout="COMPANION"
)
with open(os.path.join(BOOKS_DIR, "maths_l2_companion_cover.svg"), "w") as f: f.write(svg_maths_l2_comp)

# 3. Maths L1 Core
svg_maths_l1 = create_book_svg(
    title_primary="MATHEMATICS",
    title_sub="CORE STUDY GUIDE",
    level_str="LEVEL 1",
    subtitle="Foundations to Pass First Time",
    badges=["Full Syllabus", "Non-Calc Drills", "Calculator Skills", "Model Answers"],
    accent_color="#34d399",
    bg_gradient=("#064e3b", "#047857", "#022c22"),
    knockout="MATHEMATICS"
)
with open(os.path.join(BOOKS_DIR, "maths_l1_core_cover.svg"), "w") as f: f.write(svg_maths_l1)

# 4. Maths L1 Companion
svg_maths_l1_comp = create_book_svg(
    title_primary="MATHEMATICS",
    title_sub="COMPANION WORKBOOK",
    level_str="LEVEL 1",
    subtitle="Confidence-Building Exam Workspaces",
    badges=["Stepped Tasks", "Calculation Grid", "Target Checks", "Mark Schemes"],
    accent_color="#34d399",
    bg_gradient=("#064e3b", "#047857", "#022c22"),
    knockout="COMPANION"
)
with open(os.path.join(BOOKS_DIR, "maths_l1_companion_cover.svg"), "w") as f: f.write(svg_maths_l1_comp)

# 5. Spelling, Punctuation and Grammar
svg_spag = create_book_svg(
    title_primary="SPELLING, PUNCTUATION",
    title_sub="& GRAMMAR HANDBOOK",
    level_str="LEVEL 1 & 2",
    subtitle="Essential Rules & Drills for Exam Accuracy",
    badges=["Comma Splices", "Apostrophes", "Colon/Semicolon", "Formal Vocab"],
    accent_color="#f59e0b",
    bg_gradient=("#451a03", "#78350f", "#1c0a00"),
    knockout="GRAMMAR",
    title_primary_size=28,
    title_sub_size=26
)
with open(os.path.join(BOOKS_DIR, "spag_mastery_cover.svg"), "w") as f: f.write(svg_spag)
with open(os.path.join(BOOKS_DIR, "spelling_punctuation_grammar_cover.svg"), "w") as f: f.write(svg_spag)

# 6. Digital Skills
svg_digital = create_book_svg(
    title_primary="DIGITAL SKILLS",
    title_sub="PRACTICAL HANDBOOK",
    level_str="LEVEL 1 & E3",
    subtitle="EDSQ Complete Standards & Workplace Skills",
    badges=["Using Devices", "Creating Media", "Communicating", "Online Safety"],
    accent_color="#a855f7",
    bg_gradient=("#3b0764", "#581c87", "#1e0438"),
    knockout="DIGITAL"
)
with open(os.path.join(BOOKS_DIR, "digital_skills_cover.svg"), "w") as f: f.write(svg_digital)

# 7. BKSB / OneAdvanced Remediation
svg_bksb = create_book_svg(
    title_primary="BKSB / ONEADVANCED",
    title_sub="DIAGNOSTIC MASTERY",
    level_str="REMEDIATION",
    subtitle="Targeted Gap Repair & Step-by-Step Models",
    badges=["Diagnostic Prep", "Gap Drills", "Golden Rules", "Exit Checks"],
    accent_color="#ec4899",
    bg_gradient=("#500724", "#831843", "#280212"),
    knockout="ONEADVANCED"
)
with open(os.path.join(BOOKS_DIR, "bksb_remediation_cover.svg"), "w") as f: f.write(svg_bksb)

# 8. Flashcards (PassFunctionalSkills-Style 3D Stacks)
import subprocess
subprocess.run(['python3', os.path.join(PROJECT_DIR, 'build_pfs_style_flashcard_stacks.py')], check=True)
# 9. Bundles & Mocks
with open(os.path.join(BOOKS_DIR, "bundle_writing_l2.svg"), "w") as f:
    f.write(create_bundle_svg("ENGLISH WRITING BUNDLE", "Core Guide + Companion Workbook + Grammar", "#fbbf24"))

with open(os.path.join(BOOKS_DIR, "bundle_ultimate_l2.svg"), "w") as f:
    f.write(create_bundle_svg("ULTIMATE PASS BUNDLE", "Maths + English Core Guides & Flashcards", "#f59e0b"))

with open(os.path.join(BOOKS_DIR, "mock_pack_maths_l2.svg"), "w") as f:
    f.write(create_bundle_svg("5-MOCK MATHS EXAM PACK", "Section A & B Booklets with Worked Schemes", "#38bdf8"))

with open(os.path.join(BOOKS_DIR, "mock_pack_english_l2.svg"), "w") as f:
    f.write(create_bundle_svg("5-MOCK ENGLISH EXAM PACK", "Reading & Writing Booklets with Exemplar Benchmarks", "#fbbf24"))

print("[OK] Generated all Master Functional Skills branded book, flashcard and pack covers!")
