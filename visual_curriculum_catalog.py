"""
visual_curriculum_catalog.py
Master visual catalog mapping every Functional Skills topic to:
1. Verified, pedagogically accurate real-life workplace photos (assets/img/book_photos/)
2. Hand-drawn whiteboard sketch graphics (SVGs for Grid Method, Bus Stop, Bar Models, BIDMAS, etc.)
Used synchronously by both the A4 Print Publication Suites and the Website Revision Pages.
"""

# =============================================================================
# 1. VECTOR WHITEBOARD SKETCH SVGS (MATHEMATICS WORKING OUT & VISUAL MODELS)
# =============================================================================

def get_grid_method_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect x="2" y="2" width="536" height="256" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2" filter="url(#shadow)"/>
  
  <pattern id="dot-grid-gm" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#e2e8f0"/>
  </pattern>
  <rect x="2" y="2" width="536" height="256" rx="14" fill="url(#dot-grid-gm)"/>

  <!-- Title Pill -->
  <rect x="18" y="14" width="250" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: GRID MULTIPLICATION</text>
  <text x="285" y="32" font-size="13" font-weight="700" fill="#0f172a">Calculating 46 × 35</text>

  <!-- Grid Header Row -->
  <rect x="25" y="52" width="60" height="42" rx="6" fill="#0284c7"/>
  <text x="55" y="79" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">×</text>

  <rect x="95" y="52" width="145" height="42" rx="6" fill="#0284c7"/>
  <text x="167" y="72" font-size="11" font-weight="700" fill="#bae6fd" text-anchor="middle">TENS</text>
  <text x="167" y="88" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">40</text>

  <rect x="250" y="52" width="110" height="42" rx="6" fill="#0284c7"/>
  <text x="305" y="72" font-size="11" font-weight="700" fill="#bae6fd" text-anchor="middle">UNITS</text>
  <text x="305" y="88" font-size="16" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>

  <rect x="370" y="52" width="145" height="42" rx="6" fill="#0369a1"/>
  <text x="442" y="78" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">ROW SUBTOTAL</text>

  <!-- Row 1: 30 -->
  <rect x="25" y="104" width="60" height="52" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <text x="55" y="128" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">TENS</text>
  <text x="55" y="146" font-size="17" font-weight="800" fill="#0c4a6e" text-anchor="middle">30</text>

  <rect x="95" y="104" width="145" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="167" y="126" font-size="11" fill="#64748b" text-anchor="middle">30 × 40 =</text>
  <text x="167" y="147" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">1,200</text>

  <rect x="250" y="104" width="110" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="305" y="126" font-size="11" fill="#64748b" text-anchor="middle">30 × 6 =</text>
  <text x="305" y="147" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">180</text>

  <rect x="370" y="104" width="145" height="52" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="442" y="126" font-size="11" fill="#475569" text-anchor="middle">1,200 + 180 =</text>
  <text x="442" y="147" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">1,380</text>

  <!-- Row 2: 5 -->
  <rect x="25" y="164" width="60" height="52" rx="6" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1.5"/>
  <text x="55" y="188" font-size="10" font-weight="700" fill="#0284c7" text-anchor="middle">UNITS</text>
  <text x="55" y="206" font-size="17" font-weight="800" fill="#0c4a6e" text-anchor="middle">5</text>

  <rect x="95" y="164" width="145" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="167" y="186" font-size="11" fill="#64748b" text-anchor="middle">5 × 40 =</text>
  <text x="167" y="207" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">200</text>

  <rect x="250" y="164" width="110" height="52" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="305" y="186" font-size="11" fill="#64748b" text-anchor="middle">5 × 6 =</text>
  <text x="305" y="207" font-size="18" font-weight="800" fill="#0284c7" text-anchor="middle">30</text>

  <rect x="370" y="164" width="145" height="52" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="442" y="186" font-size="11" fill="#475569" text-anchor="middle">200 + 30 =</text>
  <text x="442" y="207" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">230</text>

  <!-- Final Sum Footer Banner -->
  <rect x="25" y="222" width="490" height="28" rx="6" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="140" y="241" font-size="12" font-weight="700" fill="#166534">GRAND TOTAL: 1,380 + 230</text>
  <text x="442" y="242" font-size="15" font-weight="800" fill="#15803d" text-anchor="middle">= 1,610 ✓</text>
</svg>"""

def get_bus_stop_svg():
    return """<svg viewBox="0 0 460 210" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="456" height="206" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="235" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: BUS STOP</text>
  <text x="265" y="32" font-size="13" font-weight="700" fill="#0f172a">Short Division: 936 ÷ 4</text>

  <!-- Quotient on top (Centered above dividend digits) -->
  <text x="165" y="80" font-size="34" font-weight="800" fill="#0284c7" text-anchor="middle">2</text>
  <text x="255" y="80" font-size="34" font-weight="800" fill="#0284c7" text-anchor="middle">3</text>
  <text x="345" y="80" font-size="34" font-weight="800" fill="#0284c7" text-anchor="middle">4</text>

  <!-- Bus Stop Bracket -->
  <path d="M 115 165 L 115 95 L 390 95" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Divisor on far left, out of the way -->
  <text x="70" y="148" font-size="36" font-weight="800" fill="#0f172a" text-anchor="middle">4</text>

  <!-- Dividend digits with red carried remainders -->
  <text x="165" y="148" font-size="36" font-weight="800" fill="#0f172a" text-anchor="middle">9</text>
  <circle cx="215" cy="115" r="14" fill="#fee2e2"/>
  <text x="215" y="121" font-size="18" font-weight="800" fill="#e11d48" text-anchor="middle">¹</text>
  
  <text x="255" y="148" font-size="36" font-weight="800" fill="#0f172a" text-anchor="middle">3</text>
  <circle cx="305" cy="115" r="14" fill="#fee2e2"/>
  <text x="305" y="121" font-size="18" font-weight="800" fill="#e11d48" text-anchor="middle">¹</text>
  
  <text x="345" y="148" font-size="36" font-weight="800" fill="#0f172a" text-anchor="middle">6</text>

  <!-- Annotation note -->
  <rect x="25" y="174" width="410" height="24" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="230" y="190" font-size="11.5" font-weight="600" fill="#475569" text-anchor="middle">Step: 4 into 9 = 2 r 1 → 4 into 13 = 3 r 1 → 4 into 16 = 4. Final Answer = 234 ✓</text>
</svg>"""

def get_bidmas_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="220" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: BIDMAS</text>
  <text x="250" y="32" font-size="13" font-weight="700" fill="#0f172a">Evaluate: 5 + 3 × (10 − 4)² ÷ 9</text>

  <!-- 4 Hierarchy Step Blocks -->
  <!-- Step 1: B (Brackets) -->
  <g transform="translate(20, 52)">
    <rect width="118" height="66" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect x="6" y="6" width="30" height="20" rx="4" fill="#2563eb"/>
    <text x="21" y="20" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1. B</text>
    <text x="42" y="20" font-size="11" font-weight="700" fill="#1e3a8a">Brackets</text>
    <text x="59" y="44" font-size="12" fill="#334155" text-anchor="middle">(10 − 4) = <tspan font-weight="800" fill="#2563eb">6</tspan></text>
  </g>

  <!-- Arrow 1 -->
  <text x="145" y="90" font-size="16" fill="#94a3b8" font-weight="800">→</text>

  <!-- Step 2: I (Indices) -->
  <g transform="translate(155, 52)">
    <rect width="118" height="66" rx="8" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="6" y="6" width="30" height="20" rx="4" fill="#9333ea"/>
    <text x="21" y="20" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">2. I</text>
    <text x="42" y="20" font-size="11" font-weight="700" fill="#581c87">Indices</text>
    <text x="59" y="44" font-size="12" fill="#334155" text-anchor="middle">6² = 6 × 6 = <tspan font-weight="800" fill="#9333ea">36</tspan></text>
  </g>

  <!-- Arrow 2 -->
  <text x="280" y="90" font-size="16" fill="#94a3b8" font-weight="800">→</text>

  <!-- Step 3: DM (Divide & Multiply) -->
  <g transform="translate(290, 52)">
    <rect width="126" height="66" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="6" y="6" width="36" height="20" rx="4" fill="#16a34a"/>
    <text x="24" y="20" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">3. DM</text>
    <text x="48" y="20" font-size="11" font-weight="700" fill="#14532d">Multiply/Div</text>
    <text x="63" y="40" font-size="11" fill="#334155" text-anchor="middle">3 × 36 = 108</text>
    <text x="63" y="55" font-size="11" fill="#334155" text-anchor="middle">108 ÷ 9 = <tspan font-weight="800" fill="#16a34a">12</tspan></text>
  </g>

  <!-- Arrow 3 -->
  <text x="423" y="90" font-size="16" fill="#94a3b8" font-weight="800">→</text>

  <!-- Step 4: AS (Add & Subtract) -->
  <g transform="translate(433, 52)">
    <rect width="87" height="66" rx="8" fill="#fff7ed" stroke="#f97316" stroke-width="1.5"/>
    <rect x="6" y="6" width="32" height="20" rx="4" fill="#ea580c"/>
    <text x="22" y="20" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">4. AS</text>
    <text x="44" y="20" font-size="11" font-weight="700" fill="#7c2d12">Add</text>
    <text x="43" y="44" font-size="12" fill="#334155" text-anchor="middle">5 + 12 = <tspan font-weight="800" fill="#ea580c">17</tspan></text>
  </g>

  <!-- Step-by-step substitution summary card -->
  <rect x="20" y="130" width="500" height="74" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="35" y="152" font-size="12" font-weight="700" fill="#475569">Full Substitution Flow:</text>
  <text x="35" y="174" font-size="13" font-weight="600" fill="#0f172a">
    5 + 3 × <tspan fill="#2563eb" font-weight="800">(10 − 4)</tspan>² ÷ 9  →  5 + 3 × <tspan fill="#9333ea" font-weight="800">6²</tspan> ÷ 9  →  5 + <tspan fill="#16a34a" font-weight="800">108 ÷ 9</tspan>  →  5 + <tspan fill="#16a34a" font-weight="800">12</tspan>
  </text>
  <text x="35" y="194" font-size="11" fill="#64748b">Equal Priority Rule: Division and Multiplication have equal standing — execute left to right.</text>

  <!-- Final Result Banner -->
  <rect x="20" y="214" width="500" height="34" rx="6" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="270" y="236" font-size="14" font-weight="800" fill="#15803d" text-anchor="middle">FINAL ACCREDITED EVALUATION = 17 ✓</text>
</svg>"""

def get_rounding_estimating_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="270" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: NUMBER LINE ROUNDING</text>
  <text x="300" y="32" font-size="13" font-weight="700" fill="#0f172a">Rounding 47 to Nearest 10</text>

  <!-- Number line axis -->
  <line x1="50" y1="90" x2="490" y2="90" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Ticks -->
  <line x1="70" y1="80" x2="70" y2="100" stroke="#0f172a" stroke-width="3"/>
  <text x="70" y="122" font-size="16" font-weight="800" fill="#0284c7" text-anchor="middle">40</text>
  <text x="70" y="138" font-size="11" font-weight="600" fill="#64748b" text-anchor="middle">Round Down</text>

  <line x1="280" y1="82" x2="280" y2="98" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="280" y="122" font-size="14" font-weight="700" fill="#64748b" text-anchor="middle">45 (Midpoint)</text>
  <text x="280" y="138" font-size="10.5" fill="#94a3b8" text-anchor="middle">Cutoff: 5 or more rounds UP</text>

  <line x1="470" y1="80" x2="470" y2="100" stroke="#0f172a" stroke-width="3"/>
  <text x="470" y="122" font-size="16" font-weight="800" fill="#15803d" text-anchor="middle">50</text>
  <text x="470" y="138" font-size="11" font-weight="700" fill="#15803d" text-anchor="middle">Round Up ✓</text>

  <!-- Number 47 Marker -->
  <circle cx="376" cy="90" r="8" fill="#e11d48"/>
  <path d="M 376 78 L 376 56" stroke="#e11d48" stroke-width="2"/>
  <rect x="345" y="40" width="62" height="22" rx="4" fill="#fee2e2" stroke="#fca5a5"/>
  <text x="376" y="55" font-size="12" font-weight="800" fill="#9f1239" text-anchor="middle">47</text>
  <!-- Curving arrow from 47 to 50 -->
  <path d="M 385 65 Q 430 50 462 76" fill="none" stroke="#e11d48" stroke-width="2.5" stroke-dasharray="4,3"/>

  <!-- 1 Significant Figure Estimation Box -->
  <rect x="25" y="156" width="490" height="76" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="40" y="178" font-size="12" font-weight="800" fill="#0369a1">EXAM ESTIMATION BENCHMARK (1 SIGNIFICANT FIGURE):</text>
  <text x="40" y="200" font-size="13" font-weight="700" fill="#0f172a">
    Estimate 48.7 × 31.25  →  Round BEFORE calculating: 50 × 30 = <tspan fill="#15803d" font-weight="800">1,500</tspan>
  </text>
  <text x="40" y="220" font-size="11" fill="#64748b">Examiner Rule: Always round each number to 1 s.f. FIRST. Never multiply exact figures and round at the end!</text>
</svg>"""

def get_place_value_svg():
    return """<svg viewBox="0 0 540 240" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="236" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="240" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: PLACE VALUE</text>
  <text x="270" y="32" font-size="13" font-weight="700" fill="#0f172a">Partitioning: 3,485,270</text>

  <!-- 7 Place value columns -->
  <!-- Col 1: Millions -->
  <rect x="20" y="52" width="70" height="42" fill="#0284c7"/>
  <text x="55" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">MILLIONS</text>
  <text x="55" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1,000,000</text>
  <rect x="20" y="96" width="70" height="52" fill="#f0f9ff" stroke="#bae6fd"/>
  <text x="55" y="132" font-size="28" font-weight="800" fill="#0369a1" text-anchor="middle">3</text>

  <!-- Col 2: H-Th -->
  <rect x="92" y="52" width="70" height="42" fill="#0284c7"/>
  <text x="127" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">HND THOU</text>
  <text x="127" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">100,000</text>
  <rect x="92" y="96" width="70" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="127" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">4</text>

  <!-- Col 3: T-Th -->
  <rect x="164" y="52" width="70" height="42" fill="#0284c7"/>
  <text x="199" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">TEN THOU</text>
  <text x="199" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">10,000</text>
  <rect x="164" y="96" width="70" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="199" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">8</text>

  <!-- Col 4: Th -->
  <rect x="236" y="52" width="70" height="42" fill="#0284c7"/>
  <text x="271" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">THOUSANDS</text>
  <text x="271" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1,000</text>
  <rect x="236" y="96" width="70" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="271" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">5</text>

  <!-- Col 5: H -->
  <rect x="308" y="52" width="70" height="42" fill="#0369a1"/>
  <text x="343" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">HUNDREDS</text>
  <text x="343" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">100</text>
  <rect x="308" y="96" width="70" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="343" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">2</text>

  <!-- Col 6: T -->
  <rect x="380" y="52" width="70" height="42" fill="#0369a1"/>
  <text x="415" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">TENS</text>
  <text x="415" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">10</text>
  <rect x="380" y="96" width="70" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="415" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">7</text>

  <!-- Col 7: U -->
  <rect x="452" y="52" width="68" height="42" fill="#0369a1"/>
  <text x="486" y="70" font-size="10" font-weight="700" fill="#bae6fd" text-anchor="middle">UNITS</text>
  <text x="486" y="86" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">1</text>
  <rect x="452" y="96" width="68" height="52" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="486" y="132" font-size="28" font-weight="800" fill="#0f172a" text-anchor="middle">0</text>

  <!-- Breakdown text footer -->
  <rect x="20" y="160" width="500" height="64" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="35" y="182" font-size="12" font-weight="700" fill="#0369a1">Value of the digit 4: 4 × 100,000 = 400,000 (Four hundred thousand)</text>
  <text x="35" y="204" font-size="11" fill="#475569">Word form: Three million, four hundred and eighty-five thousand, two hundred and seventy.</text>
</svg>"""

def get_negative_numbers_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="280" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: NEGATIVES &amp; SCALES</text>
  <text x="310" y="32" font-size="13" font-weight="700" fill="#0f172a">Temperature &amp; Bank Balances</text>

  <!-- Thermometer graphic on left -->
  <rect x="45" y="55" width="24" height="150" rx="12" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="57" cy="205" r="22" fill="#0284c7"/>
  <!-- Mercury column up to 4°C -->
  <rect x="51" y="125" width="12" height="75" fill="#0284c7"/>
  <!-- Freezing threshold 0°C line -->
  <line x1="35" y1="140" x2="80" y2="140" stroke="#e11d48" stroke-width="2.5" stroke-dasharray="4,2"/>
  <text x="90" y="144" font-size="11" font-weight="800" fill="#e11d48">0°C (Freezing)</text>

  <text x="90" y="85" font-size="12" font-weight="700" fill="#15803d">+15°C Warm</text>
  <text x="90" y="120" font-size="12" font-weight="700" fill="#0284c7">+4°C Evening</text>
  <text x="90" y="175" font-size="12" font-weight="800" fill="#0369a1">−6°C Night (-10° drop)</text>

  <!-- Number line on right for bank balances -->
  <rect x="220" y="55" width="300" height="175" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="235" y="80" font-size="12" font-weight="800" fill="#0369a1">BANK OVERDRAFT CALCULATION:</text>
  
  <text x="235" y="106" font-size="13" fill="#334155">Starting Overdraft: <tspan font-weight="800" fill="#e11d48">−£140</tspan></text>
  <text x="235" y="130" font-size="13" fill="#334155">Client Payment Received: <tspan font-weight="800" fill="#15803d">+£250</tspan></text>
  <text x="235" y="154" font-size="13" fill="#334155">Material Bill Paid: <tspan font-weight="800" fill="#e11d48">−£180</tspan></text>

  <rect x="235" y="170" width="270" height="46" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
  <text x="245" y="190" font-size="11" font-weight="700" fill="#1e3a8a">Step: −140 + 250 = +110 → +110 − 180 = −70</text>
  <text x="245" y="208" font-size="13" font-weight="800" fill="#e11d48">Final Balance = −£70 (Overdraft) ✓</text>
</svg>"""

def get_fractions_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="270" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: FRACTION BAR MODELS</text>
  <text x="300" y="32" font-size="13" font-weight="700" fill="#0f172a">Common Denominator: ⅓ + ¼</text>

  <!-- Bar 1: 1/3 converted to 4/12 -->
  <text x="25" y="70" font-size="13" font-weight="800" fill="#0369a1">⅓  = ⁴⁄₁₂</text>
  <rect x="95" y="52" width="415" height="30" fill="#f1f5f9" stroke="#94a3b8" rx="4"/>
  <!-- 4 blocks of 12 filled -->
  <rect x="95" y="52" width="138" height="30" fill="#0284c7" rx="4"/>
  <text x="164" y="72" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">4 parts (⅓)</text>

  <!-- Bar 2: 1/4 converted to 3/12 -->
  <text x="25" y="118" font-size="13" font-weight="800" fill="#b45309">¼  = ³⁄₁₂</text>
  <rect x="95" y="100" width="415" height="30" fill="#f1f5f9" stroke="#94a3b8" rx="4"/>
  <!-- 3 blocks of 12 filled -->
  <rect x="95" y="100" width="103" height="30" fill="#f59e0b" rx="4"/>
  <text x="146" y="120" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">3 parts (¼)</text>

  <!-- Combined Bar: 4/12 + 3/12 = 7/12 -->
  <text x="25" y="166" font-size="13" font-weight="800" fill="#15803d">Sum = ⁷⁄₁₂</text>
  <rect x="95" y="148" width="415" height="30" fill="#f1f5f9" stroke="#94a3b8" rx="4"/>
  <rect x="95" y="148" width="138" height="30" fill="#0284c7" rx="4"/>
  <rect x="233" y="148" width="103" height="30" fill="#f59e0b"/>
  <text x="210" y="168" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">7 parts of 12 (⁷⁄₁₂)</text>

  <!-- Formula Summary footer -->
  <rect x="25" y="195" width="485" height="40" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="40" y="220" font-size="12.5" font-weight="700" fill="#166534">
    LCM of 3 and 4 is 12:  (1 × 4)/(3 × 4) + (1 × 3)/(4 × 3) = ⁴⁄₁₂ + ³⁄₁₂ = <tspan font-size="14" font-weight="800">⁷⁄₁₂</tspan> ✓
  </text>
</svg>"""

def get_decimals_svg():
    return """<svg viewBox="0 0 760 320" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:760px; height:auto; font-family:'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;">
  <!-- Main Container Card -->
  <rect x="2" y="2" width="756" height="316" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <!-- Top Title Badges -->
  <rect x="22" y="16" width="320" height="32" rx="16" fill="#e0f2fe"/>
  <text x="36" y="37" font-size="13.5" font-weight="800" fill="#0369a1" letter-spacing="0.5">✎ WORKED METHOD: DECIMAL ALIGNMENT</text>
  <text x="365" y="38" font-size="16" font-weight="700" fill="#0f172a">Adding £34.75 + £8.60 + £12.08</text>

  <!-- Left Column Calculation Card -->
  <rect x="22" y="62" width="310" height="238" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>

  <!-- Column Place Value Headers -->
  <text x="120" y="80" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle">T</text>
  <text x="156" y="80" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle">U</text>
  <text x="184" y="80" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">&bull;</text>
  <text x="212" y="80" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle">t</text>
  <text x="248" y="80" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle">h</text>
  <line x1="38" y1="86" x2="286" y2="86" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Red Vertical Decimal Guideline -->
  <line x1="184" y1="72" x2="184" y2="286" stroke="#ef4444" stroke-width="2" stroke-dasharray="5,4" opacity="0.85"/>

  <!-- Row 1: 34.75 -->
  <g font-size="28" font-weight="800" fill="#0f172a">
    <text x="120" y="112" text-anchor="middle">3</text>
    <text x="156" y="112" text-anchor="middle">4</text>
    <circle cx="184" cy="109" r="3.2" fill="#0f172a"/>
    <text x="212" y="112" text-anchor="middle">7</text>
    <text x="248" y="112" text-anchor="middle">5</text>
  </g>

  <!-- Row 2: 8.60 (padded zero) -->
  <g font-size="28" font-weight="800" fill="#0f172a">
    <text x="156" y="152" text-anchor="middle">8</text>
    <circle cx="184" cy="149" r="3.2" fill="#0f172a"/>
    <text x="212" y="152" text-anchor="middle">6</text>
    <rect x="236" y="129" width="24" height="30" rx="4" fill="#dcfce7"/>
    <text x="248" y="152" font-weight="800" fill="#15803d" text-anchor="middle">0</text>
  </g>

  <!-- Row 3: + 12.08 (Operation + to far left, out of the way) -->
  <text x="46" y="192" font-size="28" font-weight="900" fill="#0284c7" text-anchor="middle">+</text>
  <g font-size="28" font-weight="800" fill="#0f172a">
    <text x="120" y="192" text-anchor="middle">1</text>
    <text x="156" y="192" text-anchor="middle">2</text>
    <circle cx="184" cy="189" r="3.2" fill="#0f172a"/>
    <text x="212" y="192" text-anchor="middle">0</text>
    <text x="248" y="192" text-anchor="middle">8</text>
  </g>

  <!-- Calculation Divider Line -->
  <line x1="38" y1="210" x2="286" y2="210" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Carries row -->
  <g font-size="14" font-weight="800" fill="#dc2626">
    <text x="120" y="226" text-anchor="middle">¹</text>
    <text x="156" y="226" text-anchor="middle">¹</text>
    <text x="212" y="226" text-anchor="middle">¹</text>
  </g>

  <!-- Result Row: 55.43 (No currency inside calculation) -->
  <g font-size="30" font-weight="900" fill="#15803d">
    <text x="120" y="260" text-anchor="middle">5</text>
    <text x="156" y="260" text-anchor="middle">5</text>
    <circle cx="184" cy="257" r="3.4" fill="#15803d"/>
    <text x="212" y="260" text-anchor="middle">4</text>
    <text x="248" y="260" text-anchor="middle">3</text>
  </g>

  <!-- Double Underline -->
  <line x1="38" y1="274" x2="286" y2="274" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="38" y1="280" x2="286" y2="280" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Right Rules Card -->
  <rect x="350" y="62" width="388" height="238" rx="10" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
  <text x="372" y="98" font-size="15" font-weight="800" fill="#1e40af" letter-spacing="0.4">KEY EXAM RULES FOR DECIMALS:</text>
  
  <circle cx="380" cy="132" r="3.5" fill="#2563eb"/>
  <text x="394" y="137" font-size="14.5" font-weight="600" fill="#1e293b">Align decimal points vertically (red line).</text>
  
  <circle cx="380" cy="168" r="3.5" fill="#2563eb"/>
  <text x="394" y="173" font-size="14.5" font-weight="600" fill="#1e293b">Fill missing trailing zero: 8.6 → 8.60.</text>
  
  <circle cx="380" cy="204" r="3.5" fill="#2563eb"/>
  <text x="394" y="209" font-size="14.5" font-weight="600" fill="#1e293b">Currency MUST always have 2 decimal places.</text>
  
  <!-- Green Highlight Badge -->
  <rect x="372" y="232" width="344" height="46" rx="8" fill="#dcfce7" stroke="#86efac" stroke-width="1.5"/>
  <text x="544" y="261" font-size="15" font-weight="800" fill="#15803d" text-anchor="middle">Write £55.43, never £55.4 ✓</text>
</svg>"""

def get_percentages_svg():
    return """<svg viewBox="0 0 540 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="246" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  
  <rect x="18" y="14" width="260" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: BUBBLE METHOD</text>
  <text x="290" y="32" font-size="13" font-weight="700" fill="#0f172a">Find 35% of £240 (Non-Calc)</text>

  <!-- 100% root box -->
  <rect x="20" y="55" width="130" height="60" rx="8" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
  <text x="85" y="78" font-size="11" font-weight="700" fill="#0369a1" text-anchor="middle">100% (BASE TOTAL)</text>
  <text x="85" y="100" font-size="18" font-weight="800" fill="#0f172a" text-anchor="middle">£240</text>

  <!-- Arrow to 10% -->
  <text x="160" y="90" font-size="16" fill="#94a3b8" font-weight="800">→</text>

  <!-- 10% chunk -->
  <rect x="180" y="55" width="145" height="60" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="252" y="78" font-size="11" font-weight="700" fill="#b45309" text-anchor="middle">10% (÷ 10)</text>
  <text x="252" y="100" font-size="18" font-weight="800" fill="#b45309" text-anchor="middle">£24.00</text>

  <!-- Arrow to branches -->
  <text x="335" y="90" font-size="16" fill="#94a3b8" font-weight="800">→</text>

  <!-- 30% and 5% breakdown box -->
  <rect x="355" y="52" width="165" height="95" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="368" y="74" font-size="11" font-weight="700" fill="#475569">Build target 35%:</text>
  <text x="368" y="95" font-size="12" fill="#0f172a">• 30% = 3 × £24 = <tspan font-weight="800">£72</tspan></text>
  <text x="368" y="117" font-size="12" fill="#0f172a">• 5% = half of £24 = <tspan font-weight="800">£12</tspan></text>
  <text x="368" y="137" font-size="11" font-weight="700" fill="#15803d">30% + 5% = 35%</text>

  <!-- Total Banner -->
  <rect x="20" y="160" width="500" height="70" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="35" y="185" font-size="13" font-weight="700" fill="#166534">COMBINE CHUNKS: £72 (30%) + £12 (5%)</text>
  <text x="35" y="212" font-size="20" font-weight="800" fill="#15803d">= £84.00 ✓  <tspan font-size="12" font-weight="600" fill="#475569">(Calculator multiplier check: £240 × 0.35 = £84)</tspan></text>
</svg>"""

def get_compound_area_svg():
    return """<svg viewBox="0 0 540 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="266" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="270" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: COMPOUND L-SHAPE</text>
  <text x="300" y="33" font-size="13" font-weight="700" fill="#0f172a">Split into Shape A + Shape B</text>

  <!-- Dimension Arrow Top Width: 5m -->
  <line x1="45" y1="52" x2="145" y2="52" stroke="#0284c7" stroke-width="1.5"/>
  <text x="95" y="47" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle">5 m</text>

  <!-- Shape A: Left column (100 wide x 160 high) -->
  <rect x="45" y="58" width="100" height="160" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
  <text x="95" y="132" font-size="16" font-weight="800" fill="#0369a1" text-anchor="middle">Shape A</text>
  <text x="95" y="152" font-size="12.5" font-weight="700" fill="#0284c7" text-anchor="middle">5m × 8m</text>
  <text x="95" y="170" font-size="14" font-weight="900" fill="#0369a1" text-anchor="middle">= 40 m²</text>

  <!-- Dashed dividing line between A and B -->
  <line x1="145" y1="118" x2="145" y2="218" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>

  <!-- Shape B: Right extension (135 wide x 100 high) -->
  <rect x="145" y="118" width="135" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
  <text x="212" y="160" font-size="16" font-weight="800" fill="#b45309" text-anchor="middle">Shape B</text>
  <text x="212" y="180" font-size="12.5" font-weight="700" fill="#d97706" text-anchor="middle">7m × 3m</text>
  <text x="212" y="198" font-size="14" font-weight="900" fill="#b45309" text-anchor="middle">= 21 m²</text>

  <!-- Dimension: Left Height (8m) -->
  <text x="26" y="142" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">8 m</text>

  <!-- Dimension: Shape B Top Width (7m) -->
  <text x="212" y="110" font-size="12" font-weight="800" fill="#d97706" text-anchor="middle">7 m</text>

  <!-- Dimension: Right Height (3m) -->
  <text x="296" y="172" font-size="13" font-weight="800" fill="#0f172a">3 m</text>

  <!-- Dimension: Total Bottom Width (12m) -->
  <text x="162" y="238" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Total Width = 12 m (5m + 7m)</text>

  <!-- Calculation Summary Panel (Spacious on Right) -->
  <rect x="325" y="58" width="195" height="195" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="340" y="85" font-size="12.5" font-weight="800" fill="#0369a1">CALCULATING TOTAL AREA:</text>
  <text x="340" y="112" font-size="12" font-weight="700" fill="#0284c7">Step 1: Area A (Left)</text>
  <text x="340" y="128" font-size="12" fill="#334155">5 m × 8 m = 40 m²</text>
  <text x="340" y="152" font-size="12" font-weight="700" fill="#d97706">Step 2: Area B (Right)</text>
  <text x="340" y="168" font-size="12" fill="#334155">7 m × 3 m = 21 m²</text>
  <line x1="340" y1="180" x2="505" y2="180" stroke="#cbd5e1"/>
  <rect x="338" y="190" width="168" height="34" rx="6" fill="#dcfce7" stroke="#86efac"/>
  <text x="422" y="212" font-size="14" font-weight="900" fill="#15803d" text-anchor="middle">40 + 21 = 61 m² ✓</text>
</svg>"""

def get_perimeter_svg():
    return """<svg viewBox="0 0 520 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:520px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="516" height="246" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="250" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: PERIMETER BOUNDARY</text>
  <text x="280" y="32" font-size="13" font-weight="700" fill="#0f172a">L-Shape Outer Walk</text>

  <!-- L-Shape polygon with bold border -->
  <polygon points="50,60 150,60 150,120 290,120 290,210 50,210" fill="#f0f9ff" stroke="#0284c7" stroke-width="3"/>

  <!-- Dimension Labels -->
  <text x="100" y="52" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">5 m</text>
  <text x="30" y="140" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">8 m</text>
  <text x="170" y="228" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">12 m</text>
  <text x="305" y="170" font-size="13" font-weight="800" fill="#0284c7">3 m</text>
  
  <!-- Missing sides in red -->
  <text x="220" y="112" font-size="12" font-weight="800" fill="#e11d48" text-anchor="middle">12 − 5 = 7 m</text>
  <text x="175" y="90" font-size="12" font-weight="800" fill="#e11d48">8 − 3 = 5 m</text>

  <!-- Calculation Panel -->
  <rect x="330" y="60" width="170" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="345" y="85" font-size="12" font-weight="800" fill="#0369a1">SUM OF ALL SIDES:</text>
  <text x="345" y="110" font-size="12" fill="#334155">Top = 5 m</text>
  <text x="345" y="128" font-size="12" fill="#334155">Drop = 5 m</text>
  <text x="345" y="146" font-size="12" fill="#334155">Step = 7 m</text>
  <text x="345" y="164" font-size="12" fill="#334155">Right = 3 m, Base = 12 m</text>
  <text x="345" y="182" font-size="12" fill="#334155">Left = 8 m</text>
  <line x1="345" y1="190" x2="480" y2="190" stroke="#cbd5e1"/>
  <text x="345" y="206" font-size="13" font-weight="800" fill="#15803d">Total P = 40 m ✓</text>
</svg>"""

def get_ratio_bar_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="240" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: RATIO BAR SHARING</text>
  <text x="270" y="33" font-size="13" font-weight="700" fill="#0f172a">Share £450 in Ratio 3 : 2</text>

  <!-- Person A: 3 Parts -->
  <text x="25" y="82" font-size="13.5" font-weight="800" fill="#0369a1">A (3 parts):</text>
  <rect x="125" y="60" width="75" height="38" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="162" y="84" font-size="15" font-weight="800" fill="#0369a1" text-anchor="middle">£90</text>
  <rect x="206" y="60" width="75" height="38" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="243" y="84" font-size="15" font-weight="800" fill="#0369a1" text-anchor="middle">£90</text>
  <rect x="287" y="60" width="75" height="38" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="324" y="84" font-size="15" font-weight="800" fill="#0369a1" text-anchor="middle">£90</text>
  <text x="375" y="85" font-size="16" font-weight="900" fill="#0284c7">= £270</text>

  <!-- Person B: 2 Parts -->
  <text x="25" y="136" font-size="13.5" font-weight="800" fill="#b45309">B (2 parts):</text>
  <rect x="125" y="114" width="75" height="38" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="162" y="138" font-size="15" font-weight="800" fill="#b45309" text-anchor="middle">£90</text>
  <rect x="206" y="114" width="75" height="38" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="243" y="138" font-size="15" font-weight="800" fill="#b45309" text-anchor="middle">£90</text>
  <text x="295" y="139" font-size="16" font-weight="900" fill="#d97706">= £180</text>

  <!-- Summary Footer Box (Carefully wrapped so no text overflows) -->
  <rect x="20" y="172" width="500" height="68" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="34" y="196" font-size="12" font-weight="700" fill="#166534">Step 1: Total parts = 3 + 2 = 5 parts &bull; Step 2: Value of 1 part = £450 &divide; 5 = £90</text>
  <text x="34" y="222" font-size="13" font-weight="800" fill="#15803d">Verification Check: £270 + £180 = £450.00 ✓ (Matches original starting total)</text>
</svg>"""

def get_formula_triangle_dst_svg():
    return """<svg viewBox="0 0 540 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="256" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="240" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ FORMULA TRIANGLE: SPEED / DIST / TIME</text>

  <!-- Large Equilateral Triangle Outer Shape -->
  <polygon points="40,225 165,55 290,225" fill="#f0f9ff" stroke="#0284c7" stroke-width="3"/>
  <line x1="90" y1="150" x2="240" y2="150" stroke="#0284c7" stroke-width="3"/>
  <line x1="165" y1="150" x2="165" y2="225" stroke="#0284c7" stroke-width="3"/>

  <!-- Top Compartment: Distance (D) -->
  <text x="165" y="115" font-size="22" font-weight="900" fill="#0369a1" text-anchor="middle">Distance (D)</text>
  <text x="165" y="135" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">[miles or km]</text>

  <!-- Bottom Left: Speed (S) -->
  <text x="115" y="185" font-size="18" font-weight="900" fill="#0284c7" text-anchor="middle">Speed (S)</text>
  <text x="115" y="202" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">[mph or km/h]</text>

  <!-- Multiplication symbol -->
  <text x="165" y="192" font-size="20" font-weight="900" fill="#0284c7" text-anchor="middle">×</text>

  <!-- Bottom Right: Time (T) -->
  <text x="215" y="185" font-size="18" font-weight="900" fill="#0284c7" text-anchor="middle">Time (T)</text>
  <text x="215" y="202" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">[hours]</text>

  <!-- Right Formulas & Exam Trap Panel (Nicer & Well Spaced) -->
  <rect x="315" y="55" width="205" height="185" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="330" y="80" font-size="12" font-weight="800" fill="#0369a1">COVER WHAT YOU NEED:</text>
  
  <rect x="328" y="92" width="180" height="24" rx="4" fill="#eff6ff"/>
  <text x="338" y="108" font-size="12" font-weight="800" fill="#1e40af">&bull; Distance = Speed × Time</text>
  
  <rect x="328" y="122" width="180" height="24" rx="4" fill="#eff6ff"/>
  <text x="338" y="138" font-size="12" font-weight="800" fill="#1e40af">&bull; Speed = Distance ÷ Time</text>
  
  <rect x="328" y="152" width="180" height="24" rx="4" fill="#eff6ff"/>
  <text x="338" y="168" font-size="12" font-weight="800" fill="#1e40af">&bull; Time = Distance ÷ Speed</text>

  <rect x="328" y="184" width="180" height="42" rx="4" fill="#fef3c7" stroke="#fde68a"/>
  <text x="334" y="200" font-size="10" font-weight="800" fill="#92400e">DECIMAL TIME TRAP:</text>
  <text x="334" y="216" font-size="9.5" fill="#78350f">45 mins = 45÷60 = 0.75h (NOT 0.45h)</text>
</svg>"""

def get_volume_svg():
    return """<svg viewBox="0 0 540 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="266" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="250" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: 3D CUBOID VOLUME</text>
  <text x="280" y="33" font-size="13" font-weight="700" fill="#0f172a">Length × Width × Height</text>

  <!-- Isometric 3D Cuboid (Clear & Spacious) -->
  <!-- Front face: 130 wide x 90 high -->
  <polygon points="55,115 185,115 185,205 55,205" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
  <!-- Top face: depth 55 slant -->
  <polygon points="55,115 115,62 245,62 185,115" fill="#bae6fd" stroke="#0284c7" stroke-width="2.5"/>
  <!-- Right face -->
  <polygon points="185,115 245,62 245,152 185,205" fill="#7dd3fc" stroke="#0284c7" stroke-width="2.5"/>

  <!-- Length Dimension: along bottom front -->
  <text x="120" y="226" font-size="13" font-weight="800" fill="#0c4a6e" text-anchor="middle">Length = 8 cm</text>

  <!-- Height Dimension: along left edge -->
  <text x="42" y="164" font-size="13" font-weight="800" fill="#0c4a6e" text-anchor="end">Height = 5 cm</text>

  <!-- Width Dimension: Positioned cleanly with dedicated white pill so it is NEVER hidden -->
  <rect x="210" y="180" width="105" height="26" rx="5" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
  <text x="262" y="197" font-size="12" font-weight="800" fill="#0369a1" text-anchor="middle">Width = 4 cm</text>

  <!-- Calculation Summary Panel -->
  <rect x="325" y="58" width="195" height="190" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="340" y="85" font-size="12" font-weight="800" fill="#0369a1">VOLUME &amp; CAPACITY:</text>
  <text x="340" y="112" font-size="13" font-weight="700" fill="#0f172a">V = Length × Width × Height</text>
  <text x="340" y="136" font-size="13" fill="#334155">V = 8 cm × 4 cm × 5 cm</text>
  <line x1="340" y1="150" x2="505" y2="150" stroke="#cbd5e1"/>
  <rect x="338" y="160" width="170" height="34" rx="6" fill="#dcfce7" stroke="#86efac"/>
  <text x="423" y="182" font-size="15" font-weight="900" fill="#15803d" text-anchor="middle">Volume = 160 cm³ ✓</text>
  <text x="340" y="214" font-size="11.5" font-weight="700" fill="#0369a1">Capacity: 160 cm³ = 160 ml</text>
  <text x="340" y="232" font-size="10.5" fill="#64748b">1,000 cm³ = 1 Litre</text>
</svg>"""

def get_circles_svg():
    return """<svg viewBox="0 0 540 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="266" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="270" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: CIRCLE FORMULAS</text>
  <text x="300" y="33" font-size="13" font-weight="700" fill="#0f172a">Radius, Diameter, Circumference</text>

  <!-- Circle graphic (Bigger radius 76px) -->
  <circle cx="125" cy="145" r="76" fill="#f0f9ff" stroke="#0284c7" stroke-width="3"/>
  <circle cx="125" cy="145" r="4.5" fill="#0f172a"/>
  
  <!-- Radius line from centre to right -->
  <line x1="125" y1="145" x2="201" y2="145" stroke="#ef4444" stroke-width="2.5"/>
  <text x="163" y="138" font-size="12" font-weight="800" fill="#ef4444" text-anchor="middle">r = 7 cm</text>

  <!-- Full diameter dashed dimension line -->
  <line x1="49" y1="145" x2="125" y2="145" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3"/>
  
  <!-- Diameter callout below circle -->
  <rect x="35" y="226" width="180" height="24" rx="4" fill="#f1f5f9"/>
  <text x="125" y="242" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Diameter (d) = 2 × r = 14 cm</text>

  <!-- Formulas Panel on Right (Generous Spacing) -->
  <rect x="235" y="55" width="285" height="195" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="250" y="80" font-size="12" font-weight="800" fill="#0369a1">CIRCLE FORMULAS (π = 3.142):</text>
  
  <text x="250" y="104" font-size="12" font-weight="800" fill="#0f172a">1. Circumference (Outer Perimeter):</text>
  <text x="250" y="122" font-size="12" fill="#334155">C = π × d = 3.142 × 14 = <tspan font-weight="800" fill="#0284c7">43.99 cm</tspan></text>

  <text x="250" y="148" font-size="12" font-weight="800" fill="#0f172a">2. Area (Internal Surface Space):</text>
  <text x="250" y="166" font-size="12" fill="#334155">A = π × r² = 3.142 × 7² = <tspan font-weight="800" fill="#15803d">153.96 cm²</tspan></text>
  
  <rect x="246" y="184" width="262" height="48" rx="6" fill="#fff1f2" stroke="#fca5a5"/>
  <text x="256" y="202" font-size="10.5" font-weight="800" fill="#991b1b">⚠️ CRITICAL EXAM TRAP:</text>
  <text x="256" y="220" font-size="10.5" fill="#881337">r² means 7 × 7 = 49. NEVER calculate 7 × 2!</text>
</svg>"""

def get_angles_svg():
    return """<svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:520px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="516" height="226" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="250" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: ANGLE RULES</text>
  <text x="280" y="32" font-size="13" font-weight="700" fill="#0f172a">Straight Line (180°) &amp; Triangles (180°)</text>

  <!-- Left Side: Angles on a straight line -->
  <g transform="translate(30, 60)">
    <rect width="215" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="15" y="25" font-size="11" font-weight="800" fill="#0369a1">STRAIGHT LINE = 180°</text>
    <!-- Baseline -->
    <line x1="20" y1="100" x2="195" y2="100" stroke="#0f172a" stroke-width="3"/>
    <!-- Angled arm -->
    <line x1="110" y1="100" x2="150" y2="45" stroke="#0f172a" stroke-width="3"/>
    <!-- Angle arcs -->
    <path d="M 80 100 A 30 30 0 0 1 135 65" fill="none" stroke="#0284c7" stroke-width="2"/>
    <text x="75" y="85" font-size="12" font-weight="800" fill="#0284c7">115°</text>
    <path d="M 135 65 A 30 30 0 0 1 140 100" fill="none" stroke="#e11d48" stroke-width="2"/>
    <text x="150" y="88" font-size="12" font-weight="800" fill="#e11d48">x°</text>
    <text x="15" y="132" font-size="11.5" font-weight="700" fill="#15803d">x = 180° − 115° = 65° ✓</text>
  </g>

  <!-- Right Side: Triangle angles -->
  <g transform="translate(265, 60)">
    <rect width="225" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="15" y="25" font-size="11" font-weight="800" fill="#0369a1">TRIANGLE INTERIOR = 180°</text>
    <!-- Triangle -->
    <polygon points="30,105 185,105 110,40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
    <text x="45" y="100" font-size="10" font-weight="800" fill="#0c4a6e">75°</text>
    <text x="160" y="100" font-size="10" font-weight="800" fill="#0c4a6e">45°</text>
    <text x="110" y="60" font-size="11" font-weight="800" fill="#e11d48" text-anchor="middle">y°</text>
    <text x="15" y="132" font-size="11.5" font-weight="700" fill="#15803d">y = 180° − (75° + 45°) = 60° ✓</text>
  </g>
</svg>"""

def get_coordinates_svg():
    return """<svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:520px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="516" height="236" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="260" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: 4-QUADRANT GRID</text>
  <text x="290" y="32" font-size="13" font-weight="700" fill="#0f172a">(x, y) Along Corridor, Up Stairs</text>

  <!-- Coordinate Grid -->
  <g transform="translate(40, 50)">
    <!-- Axes -->
    <line x1="0" y1="85" x2="180" y2="85" stroke="#0f172a" stroke-width="2.5"/>
    <line x1="90" y1="0" x2="90" y2="170" stroke="#0f172a" stroke-width="2.5"/>
    <text x="175" y="80" font-size="12" font-weight="800" fill="#0f172a">x</text>
    <text x="95" y="12" font-size="12" font-weight="800" fill="#0f172a">y</text>
    <text x="80" y="98" font-size="10" font-weight="700" fill="#64748b">0</text>

    <!-- Point A (3, 2) -->
    <circle cx="150" cy="45" r="5" fill="#0284c7"/>
    <text x="156" y="42" font-size="11" font-weight="800" fill="#0369a1">A(3, 2)</text>

    <!-- Point B (-2, 3) -->
    <circle cx="50" cy="25" r="5" fill="#16a34a"/>
    <text x="10" y="25" font-size="11" font-weight="800" fill="#15803d">B(−2, 3)</text>

    <!-- Point C (-3, -2) -->
    <circle cx="30" cy="125" r="5" fill="#e11d48"/>
    <text x="5" y="142" font-size="11" font-weight="800" fill="#9f1239">C(−3, −2)</text>
  </g>

  <!-- Explanation box on right -->
  <rect x="250" y="55" width="245" height="165" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="265" y="80" font-size="12" font-weight="800" fill="#0369a1">GOLDEN COORDINATE RULES:</text>
  <text x="265" y="105" font-size="11.5" fill="#1e293b">1. Coordinates are written <tspan font-weight="800">(x, y)</tspan>.</text>
  <text x="265" y="128" font-size="11.5" fill="#1e293b">2. First number (<tspan font-weight="800">x</tspan>): Go left/right along corridor.</text>
  <text x="265" y="151" font-size="11.5" fill="#1e293b">3. Second number (<tspan font-weight="800">y</tspan>): Go up/down the stairs.</text>
  <rect x="265" y="170" width="215" height="36" rx="4" fill="#dcfce7"/>
  <text x="275" y="192" font-size="11" font-weight="700" fill="#15803d">Origin (0,0) is where axes cross ✓</text>
</svg>"""

def get_averages_svg():
    return """<svg viewBox="0 0 540 240" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="236" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="270" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: THE 4 STATISTICAL AVERAGES</text>
  <text x="300" y="32" font-size="13" font-weight="700" fill="#0f172a">Data: 4, 6, 6, 7, 9, 10</text>

  <!-- 4 Cards -->
  <!-- Mean -->
  <g transform="translate(20, 52)">
    <rect width="118" height="135" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="59" y="24" font-size="12" font-weight="800" fill="#1e3a8a" text-anchor="middle">MEAN</text>
    <text x="59" y="44" font-size="10.5" fill="#64748b" text-anchor="middle">Total ÷ Count</text>
    <line x1="15" y1="52" x2="103" y2="52" stroke="#bfdbfe"/>
    <text x="59" y="74" font-size="11" fill="#1e293b" text-anchor="middle">4+6+6+7+9+10</text>
    <text x="59" y="92" font-size="11" fill="#1e293b" text-anchor="middle">= 42 ÷ 6</text>
    <text x="59" y="120" font-size="18" font-weight="800" fill="#2563eb" text-anchor="middle">= 7 ✓</text>
  </g>

  <!-- Median -->
  <g transform="translate(148, 52)">
    <rect width="118" height="135" rx="8" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
    <text x="59" y="24" font-size="12" font-weight="800" fill="#581c87" text-anchor="middle">MEDIAN</text>
    <text x="59" y="44" font-size="10.5" fill="#64748b" text-anchor="middle">Middle in Order</text>
    <line x1="15" y1="52" x2="103" y2="52" stroke="#e9d5ff"/>
    <text x="59" y="74" font-size="11" fill="#1e293b" text-anchor="middle">4, 6, [6, 7], 9, 10</text>
    <text x="59" y="92" font-size="11" fill="#1e293b" text-anchor="middle">(6 + 7) ÷ 2</text>
    <text x="59" y="120" font-size="18" font-weight="800" fill="#9333ea" text-anchor="middle">= 6.5 ✓</text>
  </g>

  <!-- Mode -->
  <g transform="translate(276, 52)">
    <rect width="118" height="135" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="59" y="24" font-size="12" font-weight="800" fill="#14532d" text-anchor="middle">MODE</text>
    <text x="59" y="44" font-size="10.5" fill="#64748b" text-anchor="middle">Most Common</text>
    <line x1="15" y1="52" x2="103" y2="52" stroke="#bbf7d0"/>
    <text x="59" y="74" font-size="11" fill="#1e293b" text-anchor="middle">6 appears twice</text>
    <text x="59" y="92" font-size="11" fill="#1e293b" text-anchor="middle">Others once</text>
    <text x="59" y="120" font-size="18" font-weight="800" fill="#16a34a" text-anchor="middle">= 6 ✓</text>
  </g>

  <!-- Range -->
  <g transform="translate(404, 52)">
    <rect width="116" height="135" rx="8" fill="#fff7ed" stroke="#f97316" stroke-width="1.5"/>
    <text x="58" y="24" font-size="12" font-weight="800" fill="#7c2d12" text-anchor="middle">RANGE</text>
    <text x="58" y="44" font-size="10.5" fill="#64748b" text-anchor="middle">Highest − Lowest</text>
    <line x1="15" y1="52" x2="101" y2="52" stroke="#fed7aa"/>
    <text x="58" y="74" font-size="11" fill="#1e293b" text-anchor="middle">Highest = 10</text>
    <text x="58" y="92" font-size="11" fill="#1e293b" text-anchor="middle">Lowest = 4</text>
    <text x="58" y="120" font-size="18" font-weight="800" fill="#ea580c" text-anchor="middle">= 6 ✓</text>
  </g>

  <rect x="20" y="196" width="500" height="30" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="270" y="216" font-size="11.5" font-weight="600" fill="#475569" text-anchor="middle">Remember: Range is a measure of spread/consistency, NOT an average!</text>
</svg>"""

def get_probability_svg():
    return """<svg viewBox="0 0 520 230" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:520px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="516" height="226" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="250" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: PROBABILITY SCALE</text>
  <text x="280" y="32" font-size="13" font-weight="700" fill="#0f172a">Scale from 0 (Impossible) to 1 (Certain)</text>

  <!-- Probability Line -->
  <line x1="50" y1="90" x2="470" y2="90" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>

  <!-- Ticks -->
  <line x1="50" y1="78" x2="50" y2="102" stroke="#0f172a" stroke-width="3"/>
  <text x="50" y="122" font-size="14" font-weight="800" fill="#e11d48" text-anchor="middle">0</text>
  <text x="50" y="138" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">Impossible</text>

  <line x1="155" y1="82" x2="155" y2="98" stroke="#94a3b8" stroke-width="2"/>
  <text x="155" y="122" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">¼ (0.25)</text>
  <text x="155" y="138" font-size="11" fill="#64748b" text-anchor="middle">Unlikely</text>

  <line x1="260" y1="78" x2="260" y2="102" stroke="#0284c7" stroke-width="3"/>
  <text x="260" y="122" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">½ (0.5)</text>
  <text x="260" y="138" font-size="11" font-weight="700" fill="#0284c7" text-anchor="middle">Even Chance</text>

  <line x1="365" y1="82" x2="365" y2="98" stroke="#94a3b8" stroke-width="2"/>
  <text x="365" y="122" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">¾ (0.75)</text>
  <text x="365" y="138" font-size="11" fill="#64748b" text-anchor="middle">Likely</text>

  <line x1="470" y1="78" x2="470" y2="102" stroke="#0f172a" stroke-width="3"/>
  <text x="470" y="122" font-size="14" font-weight="800" fill="#15803d" text-anchor="middle">1</text>
  <text x="470" y="138" font-size="11" font-weight="700" fill="#15803d" text-anchor="middle">Certain</text>

  <!-- Formula Panel -->
  <rect x="25" y="158" width="470" height="52" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="38" y="180" font-size="12" font-weight="700" fill="#166534">Formula: P(Event) = (Number of Successful Outcomes) ÷ (Total Possible Outcomes)</text>
  <text x="38" y="198" font-size="11.5" fill="#15803d">Example: P(Rolling a 5 on a fair 6-sided die) = ⅙ ≈ 0.167 (16.7%) ✓</text>
</svg>"""

def get_scatter_graphs_svg():
    return """<svg viewBox="0 0 540 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="266" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="290" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: SCATTER &amp; CORRELATION</text>
  <text x="320" y="33" font-size="13" font-weight="700" fill="#0f172a">Study Hours vs Exam Score</text>

  <!-- High-Grade Graph Axes (Spacious Left) -->
  <g transform="translate(55, 60)">
    <!-- Gridlines -->
    <line x1="0" y1="35" x2="210" y2="35" stroke="#f1f5f9" stroke-width="1.5"/>
    <line x1="0" y1="70" x2="210" y2="70" stroke="#f1f5f9" stroke-width="1.5"/>
    <line x1="0" y1="105" x2="210" y2="105" stroke="#f1f5f9" stroke-width="1.5"/>
    <line x1="0" y1="140" x2="210" y2="140" stroke="#0f172a" stroke-width="2"/>
    <line x1="0" y1="0" x2="0" y2="140" stroke="#0f172a" stroke-width="2"/>

    <!-- Axis Labels -->
    <text x="105" y="165" font-size="12" font-weight="800" fill="#475569" text-anchor="middle">Revision Time (Hours)</text>
    <text x="-70" y="-14" font-size="12" font-weight="800" fill="#475569" transform="rotate(-90)" text-anchor="middle">Exam Score (%)</text>

    <!-- Ticks -->
    <text x="0" y="154" font-size="9" fill="#64748b" text-anchor="middle">0</text>
    <text x="50" y="154" font-size="9" fill="#64748b" text-anchor="middle">2</text>
    <text x="100" y="154" font-size="9" fill="#64748b" text-anchor="middle">4</text>
    <text x="150" y="154" font-size="9" fill="#64748b" text-anchor="middle">6</text>
    <text x="200" y="154" font-size="9" fill="#64748b" text-anchor="middle">8</text>

    <text x="-6" y="144" font-size="9" fill="#64748b" text-anchor="end">0%</text>
    <text x="-6" y="109" font-size="9" fill="#64748b" text-anchor="end">30%</text>
    <text x="-6" y="74" font-size="9" fill="#64748b" text-anchor="end">60%</text>
    <text x="-6" y="39" font-size="9" fill="#64748b" text-anchor="end">90%</text>

    <!-- Line of Best Fit (Bold Red) -->
    <line x1="15" y1="130" x2="195" y2="25" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,4"/>

    <!-- Projection Interpolation Line (Dashed Blue) -->
    <line x1="125" y1="140" x2="125" y2="65" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="125" y1="65" x2="0" y2="65" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,3"/>
    <circle cx="125" cy="65" r="5" fill="#0284c7"/>
    <text x="135" y="60" font-size="10" font-weight="800" fill="#0284c7">5h ➔ 68%</text>

    <!-- Data Points -->
    <circle cx="25" cy="120" r="4.5" fill="#0f172a"/>
    <circle cx="45" cy="110" r="4.5" fill="#0f172a"/>
    <circle cx="65" cy="115" r="4.5" fill="#0f172a"/>
    <circle cx="85" cy="90" r="4.5" fill="#0f172a"/>
    <circle cx="105" cy="80" r="4.5" fill="#0f172a"/>
    <circle cx="145" cy="55" r="4.5" fill="#0f172a"/>
    <circle cx="165" cy="40" r="4.5" fill="#0f172a"/>
    <circle cx="185" cy="30" r="4.5" fill="#0f172a"/>
  </g>

  <!-- Right Panel: High-Grade Interpretation -->
  <rect x="295" y="58" width="225" height="195" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="310" y="85" font-size="12" font-weight="800" fill="#0369a1">CORRELATION &amp; ESTIMATION:</text>
  
  <rect x="308" y="96" width="200" height="28" rx="4" fill="#dcfce7"/>
  <text x="318" y="115" font-size="11.5" font-weight="800" fill="#15803d">✓ Strong Positive Correlation</text>
  
  <text x="310" y="142" font-size="11.5" fill="#334155">As revision hours increase, exam scores steadily rise.</text>
  
  <text x="310" y="170" font-size="11.5" font-weight="800" fill="#0f172a">Line of Best Fit Strategy:</text>
  <text x="310" y="188" font-size="11" fill="#475569">• Draw straight through the trend.</text>
  <text x="310" y="204" font-size="11" fill="#475569">• Keep balanced points above &amp; below.</text>
  <text x="310" y="222" font-size="11" font-weight="700" fill="#0284c7">• Project from axis to estimate values.</text>
</svg>"""

def get_unit_conversions_svg():
    return """<svg viewBox="0 0 540 240" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="236" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="260" height="26" rx="13" fill="#e0f2fe"/>
  <text x="28" y="32" font-size="12" font-weight="800" fill="#0369a1">✎ VISUAL MODEL: METRIC STAIRCASE</text>
  <text x="290" y="32" font-size="13" font-weight="700" fill="#0f172a">Length, Weight &amp; Capacity</text>

  <!-- Length conversion row -->
  <text x="25" y="70" font-size="12" font-weight="800" fill="#0369a1">LENGTH:</text>
  
  <rect x="85" y="55" width="45" height="28" rx="4" fill="#0284c7"/>
  <text x="107" y="74" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">km</text>

  <text x="145" y="65" font-size="10.5" font-weight="800" fill="#16a34a">× 1,000 →</text>
  <text x="145" y="80" font-size="10.5" font-weight="800" fill="#dc2626">← ÷ 1,000</text>

  <rect x="200" y="55" width="45" height="28" rx="4" fill="#0284c7"/>
  <text x="222" y="74" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">m</text>

  <text x="258" y="65" font-size="10.5" font-weight="800" fill="#16a34a">× 100 →</text>
  <text x="258" y="80" font-size="10.5" font-weight="800" fill="#dc2626">← ÷ 100</text>

  <rect x="310" y="55" width="45" height="28" rx="4" fill="#0284c7"/>
  <text x="332" y="74" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">cm</text>

  <text x="368" y="65" font-size="10.5" font-weight="800" fill="#16a34a">× 10 →</text>
  <text x="368" y="80" font-size="10.5" font-weight="800" fill="#dc2626">← ÷ 10</text>

  <rect x="420" y="55" width="45" height="28" rx="4" fill="#0284c7"/>
  <text x="442" y="74" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">mm</text>

  <!-- Weight & Capacity rows in split card -->
  <g transform="translate(25, 105)">
    <rect width="235" height="110" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="15" y="24" font-size="11" font-weight="800" fill="#0369a1">MASS / WEIGHT (× 1,000):</text>
    <text x="15" y="50" font-size="12" fill="#0f172a">1 kilogram (kg) = <tspan font-weight="800" fill="#0284c7">1,000 grams (g)</tspan></text>
    <text x="15" y="72" font-size="12" fill="#0f172a">1 tonne (t) = <tspan font-weight="800" fill="#0284c7">1,000 kg</tspan></text>
    <text x="15" y="96" font-size="11" font-weight="700" fill="#15803d">Big to small: Multiply by 1,000</text>
  </g>

  <g transform="translate(275, 105)">
    <rect width="235" height="110" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="15" y="24" font-size="11" font-weight="800" fill="#0369a1">CAPACITY / LIQUID (× 1,000):</text>
    <text x="15" y="50" font-size="12" fill="#0f172a">1 litre (L) = <tspan font-weight="800" fill="#0284c7">1,000 millilitres (ml)</tspan></text>
    <text x="15" y="72" font-size="12" fill="#0f172a">1 centilitre (cl) = <tspan font-weight="800" fill="#0284c7">10 ml</tspan></text>
    <text x="15" y="96" font-size="11" font-weight="700" fill="#15803d">Small to big: Divide by 1,000</text>
  </g>
</svg>"""

def get_pie_charts_svg():
    return """<svg viewBox="0 0 540 270" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:540px; height:auto; font-family:'Plus Jakarta Sans', system-ui, sans-serif;">
  <rect x="2" y="2" width="536" height="266" rx="14" fill="#ffffff" stroke="#bae6fd" stroke-width="2"/>
  <rect x="18" y="14" width="270" height="28" rx="14" fill="#e0f2fe"/>
  <text x="28" y="33" font-size="12" font-weight="800" fill="#0369a1">✎ WORKED METHOD: PIE CHART ANGLES</text>
  <text x="300" y="33" font-size="13" font-weight="700" fill="#0f172a">Full Circle = 360°</text>

  <!-- Segmented pie chart on left (Radius 72px) -->
  <g transform="translate(135, 145)">
    <!-- Food: 180 deg (bottom half) -->
    <path d="M 0 0 L -72 0 A 72 72 0 0 0 72 0 Z" fill="#0284c7"/>
    <!-- Rent: 90 deg (top right) -->
    <path d="M 0 0 L 0 -72 A 72 72 0 0 1 72 0 Z" fill="#f59e0b"/>
    <!-- Transport: 54 deg -->
    <path d="M 0 0 L -58 -42 A 72 72 0 0 1 0 -72 Z" fill="#10b981"/>
    <!-- Bills: 36 deg -->
    <path d="M 0 0 L -72 0 A 72 72 0 0 1 -58 -42 Z" fill="#6366f1"/>

    <!-- Labels on Sectors -->
    <text x="0" y="38" font-size="11.5" font-weight="900" fill="#ffffff" text-anchor="middle">Food: 50% (180°)</text>
    <text x="36" y="-30" font-size="10.5" font-weight="800" fill="#ffffff" text-anchor="middle">Rent: 25% (90°)</text>
    <text x="-26" y="-45" font-size="9" font-weight="800" fill="#ffffff" text-anchor="middle">Travel: 54°</text>
    <text x="-48" y="-12" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle">Bills 36°</text>
  </g>

  <!-- Right Panel: High Quality Angle Formula & Calculation Table -->
  <rect x="270" y="55" width="250" height="195" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="285" y="80" font-size="12" font-weight="800" fill="#0369a1">SECTOR ANGLE FORMULA:</text>
  <rect x="282" y="90" width="225" height="24" rx="4" fill="#eff6ff"/>
  <text x="394" y="106" font-size="11.5" font-weight="800" fill="#1e40af" text-anchor="middle">Angle = (Frequency &divide; Total) &times; 360&deg;</text>

  <!-- Step-by-step example -->
  <text x="285" y="132" font-size="11.5" fill="#334155">Example: 15 out of 60 choose Travel:</text>
  <text x="285" y="152" font-size="12" font-weight="800" fill="#10b981">(15 &divide; 60) &times; 360&deg; = 0.25 &times; 360&deg; = 90&deg;</text>

  <line x1="285" y1="166" x2="505" y2="166" stroke="#e2e8f0"/>
  <rect x="282" y="174" width="225" height="42" rx="6" fill="#dcfce7" stroke="#86efac"/>
  <text x="394" y="193" font-size="11" font-weight="800" fill="#166534" text-anchor="middle">GOLDEN RULE OF PIE CHARTS:</text>
  <text x="394" y="208" font-size="10.5" fill="#15803d" text-anchor="middle">All sector angles MUST sum to exactly 360&deg; &check;</text>
</svg>"""



# =============================================================================
# 2. DEFINITIVE TOPIC VISUAL REGISTRY
# Maps every topic slug to:
# - photo: exact relative path in assets/img/book_photos/
# - photo_caption: real-world vocational context
# - character: character tag (legacy)
# - character_quote: mentor tip (legacy)
# - sketch: dedicated sketch SVG generator function
# =============================================================================

TOPIC_VISUAL_REGISTRY = {
    # --- NUMBER & NUMBER SYSTEMS ---
    "functional-skills-numbers-and-place-value": {
        "photo": "retail_shop/warehouse_stock.jpg",
        "photo_caption": "Warehouse inventory management auditing large unit quantities and stock numbers.",
        "character": "abdul",
        "character_quote": "Separate large numbers into groups of three digits from the right to read millions and thousands accurately.",
        "sketch": get_place_value_svg
    },
    "functional-skills-ordering-numbers": {
        "photo": "retail_shop/warehouse_stock.jpg",
        "photo_caption": "Arranging stock SKU codes and order quantities in ascending and descending order.",
        "character": "abdul",
        "character_quote": "Line up digits by place value column before comparing magnitudes.",
        "sketch": get_place_value_svg
    },
    "functional-skills-addition-and-subtraction": {
        "photo": "addition-subtraction-hero.jpg",
        "photo_caption": "Column addition & subtraction arithmetic with borrowing and carrying.",
        "character": "abdul",
        "character_quote": "Always apply an inverse check: subtract your added amount to ensure it returns to the starting total.",
        "sketch": get_decimals_svg
    },
    "functional-skills-multiplication": {
        "photo": "construction_trades/timber_lumber_stack.jpg",
        "photo_caption": "Contractor calculating bulk timber requirements, pack counts, and trade orders.",
        "character": "abdul",
        "character_quote": "Always partition 2-digit numbers into tens and units using the Grid Method to eliminate carried-number confusion.",
        "sketch": get_grid_method_svg
    },
    "functional-skills-division": {
        "photo": "healthcare_care/pharmacy_dispensing_bottles.jpg",
        "photo_caption": "Hospital pharmacy dispensing calculating dosage units and equal medicine distributions.",
        "character": "abdul",
        "character_quote": "Shift the decimal point in both divisor and dividend by multiplying by 10 or 100 first, then use short division.",
        "sketch": get_bus_stop_svg
    },
    "functional-skills-bidmas": {
        "photo": "money_shopping_bills/scientific_calculator_display.jpg",
        "photo_caption": "Executing multi-step financial formulas following statutory order of operations.",
        "character": "priya",
        "character_quote": "Evaluate brackets first, then indices, then multiplication and division left-to-right.",
        "sketch": get_bidmas_svg
    },
    "functional-skills-rounding-and-estimating": {
        "photo": "retail_shop/supermarket_price_tags.jpg",
        "photo_caption": "Estimating shopping basket expenditure by rounding shelf unit prices to 1 significant figure.",
        "character": "sam",
        "character_quote": "In Functional Skills Section A, round each number to 1 significant figure BEFORE multiplying or dividing.",
        "sketch": get_rounding_estimating_svg
    },
    "functional-skills-fractions": {
        "photo": "kitchen_cooking_recipes/baker_flour_dough.jpg",
        "photo_caption": "Catering kitchen measuring ingredient proportions and scaling fractional recipe batches.",
        "character": "abdul",
        "character_quote": "To add or subtract fractions, find a common denominator first. Never add the bottom denominators together.",
        "sketch": get_fractions_svg
    },
    "functional-skills-fraction-basics": {
        "photo": "kitchen_cooking_recipes/kitchen_scales.jpg",
        "photo_caption": "Proportional ingredient division and unit fraction representation.",
        "character": "abdul",
        "character_quote": "The denominator tells you total equal parts; the numerator tells you how many parts you have.",
        "sketch": get_fractions_svg
    },
    "functional-skills-decimals": {
        "photo": "money_shopping_bills/uk_currency_coins_drawer.jpg",
        "photo_caption": "Balancing till cash drawers, coin counts, and currency decimal transactions to 2 decimal places.",
        "character": "abdul",
        "character_quote": "Always quote currency to two decimal places: write £45.90, never £45.9.",
        "sketch": get_decimals_svg
    },
    "functional-skills-decimal-basics": {
        "photo": "money_shopping_bills/coins_pounds.jpg",
        "photo_caption": "Tenths and hundredths place value in coin calculations.",
        "character": "abdul",
        "character_quote": "Align the decimal points vertically when adding or subtracting money.",
        "sketch": get_decimals_svg
    },
    "functional-skills-percentages": {
        "photo": "retail_shop/retail_window_sale_sign.jpg",
        "photo_caption": "Retail storefront calculating promotional percentage discounts, markups, and VAT adjustments.",
        "character": "priya",
        "character_quote": "To find 35% without a calculator: find 10% (divide by 10), multiply by 3, and add 5% (half of 10%).",
        "sketch": get_percentages_svg
    },
    "functional-skills-fractions-decimals-and-percentages": {
        "photo": "money_shopping_bills/receipt_checking.jpg",
        "photo_caption": "Comparing financial discount percentages, fractional proportions, and decimal multipliers.",
        "character": "priya",
        "character_quote": "Convert all figures into decimals or percentages to compare them accurately.",
        "sketch": get_percentages_svg
    },
    "functional-skills-negative-numbers": {
        "photo": "measuring_tools/temperature_thermometer.jpg",
        "photo_caption": "Clinical cold-storage and meteorological thermometer monitoring sub-zero temperatures.",
        "character": "sarah",
        "character_quote": "Remember that -10°C is colder than -2°C. On a number line, values decrease as you move further left.",
        "sketch": get_negative_numbers_svg
    },

    # --- MEASURES, SHAPE & SPACE ---
    "functional-skills-perimeter": {
        "photo": "construction_trades/carpenter_laser_measure.jpg",
        "photo_caption": "Site carpenter measuring total room perimeter boundaries for skirting boards and trims.",
        "character": "marcus",
        "character_quote": "Perimeter is the distance ALL the way around the outside boundary. Always count sides to ensure none are missed.",
        "sketch": get_perimeter_svg
    },
    "functional-skills-area": {
        "photo": "home_diy_decorating/ceramic_floor_tiling.jpg",
        "photo_caption": "Trades installer measuring room dimensions and calculating square meterage for floor tiling.",
        "character": "marcus",
        "character_quote": "For L-shaped rooms, draw a dotted line to cut the shape into two simple rectangles, calculate each area, and add them together.",
        "sketch": get_compound_area_svg
    },
    "functional-skills-volume": {
        "photo": "everyday_objects/shipping_cargo_containers.jpg",
        "photo_caption": "Commercial freight logistics calculating cubic volume capacity of shipping containers.",
        "character": "marcus",
        "character_quote": "Volume of a cuboid is Length × Width × Height. Always check your units are cubed (cm³ or m³).",
        "sketch": get_volume_svg
    },
    "functional-skills-surface-area": {
        "photo": "everyday_objects/delivery_parcel.jpg",
        "photo_caption": "Packaging manufacture calculating total surface area of cardboard packaging boxes.",
        "character": "marcus",
        "character_quote": "Calculate the area of each of the 6 faces on a box and add them all together.",
        "sketch": get_volume_svg
    },
    "functional-skills-ratio": {
        "photo": "construction_trades/concrete_mixer_site.jpg",
        "photo_caption": "Construction mixer on site blending cement, sand, and aggregate in precise ratio parts.",
        "character": "marcus",
        "character_quote": "Three golden steps for ratio: 1) Add the parts. 2) Divide total by total parts to find 1 part. 3) Multiply by each ratio number.",
        "sketch": get_ratio_bar_svg
    },
    "functional-skills-proportion": {
        "photo": "kitchen_cooking_recipes/chopping_vegetables.jpg",
        "photo_caption": "Commercial catering kitchen scaling recipe ingredient proportions for large events.",
        "character": "marcus",
        "character_quote": "Direct proportion: find the quantity for 1 unit (unitary method), then multiply by the desired target quantity.",
        "sketch": get_ratio_bar_svg
    },
    "functional-skills-speed": {
        "photo": "travel_transport_timetables/train_speedometer_cockpit.jpg",
        "photo_caption": "Rail cab speedometer and timetable tracking journey distances, speeds, and transit times.",
        "character": "priya",
        "character_quote": "Remember to convert minutes into decimal hours before calculating speed (e.g. 45 mins = 0.75 hours, NOT 0.45 hours).",
        "sketch": get_formula_triangle_dst_svg
    },
    "functional-skills-density": {
        "photo": "measuring_tools/digital_scales.jpg",
        "photo_caption": "Laboratory and materials testing measuring mass and volume to calculate material density.",
        "character": "marcus",
        "character_quote": "Density = Mass ÷ Volume. Check whether units are g/cm³ or kg/m³.",
        "sketch": get_formula_triangle_dst_svg
    },
    "functional-skills-circles": {
        "photo": "measuring_tools/bicycle_wheel_spokes.jpg",
        "photo_caption": "Bicycle wheel rim and spokes demonstrating radius, diameter, and circular circumference.",
        "character": "priya",
        "character_quote": "Radius is from centre to edge (halfway). Diameter is all the way across. Circumference is C = π × d.",
        "sketch": get_circles_svg
    },
    "functional-skills-angles": {
        "photo": "measuring_tools/ruler_geometry.jpg",
        "photo_caption": "Technical drafting using protractors to measure acute, obtuse, and reflex angles.",
        "character": "marcus",
        "character_quote": "Angles on a straight line add to 180°. Angles inside any triangle always add to 180°.",
        "sketch": get_angles_svg
    },
    "functional-skills-angles-in-2d-shapes": {
        "photo": "measuring_tools/ruler_geometry.jpg",
        "photo_caption": "Calculating interior angle sums in triangles, quadrilaterals, and regular polygons.",
        "character": "marcus",
        "character_quote": "Quadrilaterals always sum to 360°. For regular polygons, divide 360° by number of sides to find exterior angles.",
        "sketch": get_angles_svg
    },
    "functional-skills-coordinates": {
        "photo": "maps_directions/marine_nautical_chart_compass.jpg",
        "photo_caption": "Marine navigational chart plotting latitude and longitude grid coordinates across four quadrants.",
        "character": "priya",
        "character_quote": "Along the corridor first (x), then up or down the stairs (y).",
        "sketch": get_coordinates_svg
    },
    "functional-skills-maps-and-scale-drawings": {
        "photo": "maps_directions/paper_map_route.jpg",
        "photo_caption": "Topographical route planning measuring scale distances and directional compass bearings.",
        "character": "marcus",
        "character_quote": "Always check the scale ratio on a map (e.g. 1 cm = 50 m) before measuring distances with your ruler.",
        "sketch": get_coordinates_svg
    },
    "functional-skills-unit-conversions": {
        "photo": "measuring_tools/tape_measure.jpg",
        "photo_caption": "Precision metric measurements converting between millimeters, centimeters, and meters.",
        "character": "marcus",
        "character_quote": "Big to small, multiply them all (1 m = 100 cm). Small to big, divide the rig (100 cm = 1 m).",
        "sketch": get_unit_conversions_svg
    },
    "functional-skills-length": {
        "photo": "measuring_tools/tape_measure.jpg",
        "photo_caption": "Carpentry and site measurements tracking linear dimensions and timber cuts.",
        "character": "marcus",
        "character_quote": "Check that all dimensions in a problem are converted to the same unit before calculating.",
        "sketch": get_unit_conversions_svg
    },
    "functional-skills-weight": {
        "photo": "measuring_tools/digital_scales.jpg",
        "photo_caption": "Clinical pharmacology and logistics scales recording kilograms, grams, and imperial pounds.",
        "character": "sarah",
        "character_quote": "1 kg = 1,000 g. For imperial conversions, remember 1 kg is approximately 2.2 lbs.",
        "sketch": get_unit_conversions_svg
    },
    "functional-skills-capacity": {
        "photo": "kitchen_cooking_recipes/measuring_jug.jpg",
        "photo_caption": "Hospital clinical dispensing and catering measuring liquid capacity in litres and millilitres.",
        "character": "sarah",
        "character_quote": "1 litre = 1,000 millilitres. 1 cm³ of water equals 1 ml.",
        "sketch": get_unit_conversions_svg
    },
    "functional-skills-temperature": {
        "photo": "measuring_tools/temperature_thermometer.jpg",
        "photo_caption": "Precision Celsius thermometer monitoring clinical ward and food storage standards.",
        "character": "sarah",
        "character_quote": "When checking temperature drops below zero, remember that -5°C is colder than -2°C.",
        "sketch": get_negative_numbers_svg
    },
    "functional-skills-time": {
        "photo": "everyday_objects/wall_clock.jpg",
        "photo_caption": "Analogue 12-hour and digital 24-hour clock faces for transport and shift schedules.",
        "character": "sarah",
        "character_quote": "For shift rotas, 24-hour time avoids morning and afternoon mix-ups: 08:30 is 8:30 am, 20:30 is 8:30 pm.",
        "sketch": None
    },
    "functional-skills-money": {
        "photo": "money_shopping_bills/coins_pounds.jpg",
        "photo_caption": "Personal budgeting, invoice receipts, and utility bills calculation.",
        "character": "abdul",
        "character_quote": "Always quote currency to two decimal places in Functional Skills exams: write £45.90, never £45.9.",
        "sketch": get_decimals_svg
    },
    "functional-skills-best-buys": {
        "photo": "retail_shop/supermarket_aisle.jpg",
        "photo_caption": "Supermarket comparative shopping calculating unit price per 100g to find best value.",
        "character": "sam",
        "character_quote": "To compare two packs of different sizes, find the cost per 100g or 100ml for both.",
        "sketch": get_decimals_svg
    },
    "functional-skills-interest-and-compound-interest": {
        "photo": "charts_data_screens/analytics_dashboard.jpg",
        "photo_caption": "Investment account monitoring annual compound interest growth and savings yields.",
        "character": "priya",
        "character_quote": "Compound interest applies interest to previous interest. Use the multiplier formula: P × (1 + r)^n.",
        "sketch": get_percentages_svg
    },
    "functional-skills-formulas": {
        "photo": "construction_trades/blueprints_plans.jpg",
        "photo_caption": "Engineering blueprint specifications using algebraic formulas to calculate structural loads.",
        "character": "priya",
        "character_quote": "Substitute known numbers into the formula carefully and evaluate using BIDMAS.",
        "sketch": get_bidmas_svg
    },
    "functional-skills-2d-shapes": {
        "photo": "measuring_tools/ruler_geometry.jpg",
        "photo_caption": "Architectural geometry identifying polygon properties, right angles, and symmetry.",
        "character": "marcus",
        "character_quote": "Identify lines of symmetry and rotational symmetry order for standard regular polygons.",
        "sketch": get_angles_svg
    },
    "functional-skills-3d-shapes": {
        "photo": "everyday_objects/delivery_parcel.jpg",
        "photo_caption": "Logistics parcel handling identifying vertices, edges, and faces of 3D geometric packages.",
        "character": "marcus",
        "character_quote": "A cuboid has 6 faces, 12 edges, and 8 vertices.",
        "sketch": get_volume_svg
    },
    "functional-skills-3d-shape-basics": {
        "photo": "everyday_objects/delivery_parcel.jpg",
        "photo_caption": "Everyday packaging shapes: cylinders, cuboids, prisms, and spheres.",
        "character": "marcus",
        "character_quote": "Prisms have the exact same cross-section running all the way through their length.",
        "sketch": get_volume_svg
    },
    "functional-skills-nets": {
        "photo": "construction_trades/blueprints_plans.jpg",
        "photo_caption": "Structural cardboard packaging design unfolding 3D containers into 2D nets.",
        "character": "marcus",
        "character_quote": "Visualise folding each flap up: opposite faces on a dice net must never touch directly.",
        "sketch": None
    },
    "functional-skills-plans-and-elevations": {
        "photo": "construction_trades/blueprints_plans.jpg",
        "photo_caption": "Architectural construction drawings showing plan view, front elevation, and side elevation.",
        "character": "marcus",
        "character_quote": "Plan view is looking straight down from above; front and side elevations are viewed horizontally.",
        "sketch": None
    },

    # --- STATISTICS & PROBABILITY ---
    "functional-skills-mean-median-mode-and-range": {
        "photo": "charts_data_screens/hospital_analytics_monitor.jpg",
        "photo_caption": "Clinical healthcare monitor tracking patient data averages, medians, and vital sign ranges.",
        "character": "priya",
        "character_quote": "Mean = Total ÷ Count. Median = Middle value in order. Mode = Most frequent. Range = Highest minus Lowest.",
        "sketch": get_averages_svg
    },
    "functional-skills-estimating-the-mean": {
        "photo": "charts_data_screens/tablet_spreadsheet.jpg",
        "photo_caption": "Grouped frequency data analysis finding midpoints to estimate sample mean values.",
        "character": "priya",
        "character_quote": "Find the midpoint of each class interval, multiply by frequency, sum the totals, and divide by total frequency.",
        "sketch": get_averages_svg
    },
    "functional-skills-grouped-data": {
        "photo": "charts_data_screens/tablet_spreadsheet.jpg",
        "photo_caption": "Survey frequency distribution table organizing clinical test results into grouped class intervals.",
        "character": "priya",
        "character_quote": "Make sure class intervals are equal in width and do not overlap.",
        "sketch": get_averages_svg
    },
    "functional-skills-data-tables": {
        "photo": "charts_data_screens/tablet_spreadsheet.jpg",
        "photo_caption": "Spreadsheet columns, inventory stock tables, and two-way frequency matrices.",
        "character": "abdul",
        "character_quote": "Read row headers and column headers like a map coordinate before pulling out figures.",
        "sketch": None
    },
    "functional-skills-bar-charts": {
        "photo": "charts_data_screens/pie_chart_analysis.jpg",
        "photo_caption": "Comparative bar chart illustrating quarterly department performance figures.",
        "character": "priya",
        "character_quote": "Check the scale on the vertical axis carefully: bars must have equal gaps between distinct categories.",
        "sketch": None
    },
    "functional-skills-line-graphs": {
        "photo": "charts_data_screens/scatter_plot_graph.jpg",
        "photo_caption": "Continuous time-series line graph tracking temperature variations over 24 hours.",
        "character": "priya",
        "character_quote": "Line graphs are used for continuous data over time; join points with neat straight lines.",
        "sketch": None
    },
    "functional-skills-pie-charts": {
        "photo": "charts_data_screens/pie_chart_analysis.jpg",
        "photo_caption": "Survey report showing segmented pie chart with angle distributions and percentage shares.",
        "character": "abdul",
        "character_quote": "A full circle has 360 degrees. To find the angle for each sector: (Frequency ÷ Total) × 360°.",
        "sketch": get_pie_charts_svg
    },
    "functional-skills-scatter-graphs": {
        "photo": "charts_data_screens/clinical_research_scatter.jpg",
        "photo_caption": "Clinical research laboratory analysing scatter plots to determine correlation and line of best fit.",
        "character": "priya",
        "character_quote": "Draw your line of best fit so roughly half the points lie above and half below. Follow the trend.",
        "sketch": get_scatter_graphs_svg
    },
    "functional-skills-conversion-graphs": {
        "photo": "charts_data_screens/scatter_plot_graph.jpg",
        "photo_caption": "Conversion line graph converting between currencies (GBP to EUR) and metric-imperial units.",
        "character": "priya",
        "character_quote": "Read from one axis to the line, then read across to the other axis using a straight ruler.",
        "sketch": None
    },
    "functional-skills-probability": {
        "photo": "everyday_objects/red_dice_roll.jpg",
        "photo_caption": "Rolling precision numbered dice to determine experimental and theoretical probability outcomes.",
        "character": "sam",
        "character_quote": "Probability is always between 0 (impossible) and 1 (certain). You can express it as a fraction, decimal, or percentage.",
        "sketch": get_probability_svg
    },
    "functional-skills-probability-tables": {
        "photo": "everyday_objects/probability_dice.jpg",
        "photo_caption": "Two-way probability outcome grids calculating combined likelihood of multiple events.",
        "character": "sam",
        "character_quote": "List all possible outcomes systematically in a two-way sample space table.",
        "sketch": get_probability_svg
    },

    # --- ENGLISH READING TOPICS ---
    "reading-fact-or-opinion": {
        "photo": "journalism_media/newspaper_editorial.jpg",
        "photo_caption": "Editorial column and news articles balancing verified objective facts against editorial opinions.",
        "character": "priya",
        "character_quote": "A fact can be proved with evidence, statistics, or dates. An opinion contains value words like 'best' or 'should'.",
        "sketch": None
    },
    "reading-meaning": {
        "photo": "classroom_studying_adults/dictionary_magnifier.jpg",
        "photo_caption": "Examining detailed dictionary entries and contextual definitions using a magnifier.",
        "character": "priya",
        "character_quote": "Read the sentences immediately before and after an unfamiliar word to identify contextual clues.",
        "sketch": None
    },
    "reading-specialist-words": {
        "photo": "workplace_office/technical_manual.jpg",
        "photo_caption": "Technical engineering manual highlighting domain-specific vocabulary and procedural definitions.",
        "character": "priya",
        "character_quote": "Look for glossaries, brackets, or explanatory phrases that define technical jargon in the text.",
        "sketch": None
    },
    "reading-presentational-features": {
        "photo": "workplace_office/magazine_layout_features.jpg",
        "photo_caption": "Magazine editorial layout showcasing headlines, callout boxes, subheadings, and formatting devices.",
        "character": "priya",
        "character_quote": "Examiners don't just want you to name a feature (like 'bold text') — you must state WHY the writer used it.",
        "sketch": None
    },
    "reading-investigating-layout": {
        "photo": "workplace_office/brochure_pamphlet.jpg",
        "photo_caption": "Workplace information leaflet demonstrating multi-column layout, bullet points, and headers.",
        "character": "priya",
        "character_quote": "Bullet points break complex information into easily digestible chunks for busy readers.",
        "sketch": None
    },
    "reading-investigating-image": {
        "photo": "workplace_office/photo_editor_proofs.jpg",
        "photo_caption": "Editorial proof sheet evaluating photo selection and visual impact in printed media.",
        "character": "priya",
        "character_quote": "Analyse how images reinforce or contradict the message conveyed in the written copy.",
        "sketch": None
    },
    "reading-language-features": {
        "photo": "retail_shop/advertising_billboard.jpg",
        "photo_caption": "High-impact outdoor marketing billboard using persuasive rhetoric, slogans, and emotive vocabulary.",
        "character": "priya",
        "character_quote": "Look for alliteration, rule of three, rhetorical questions, and emotive vocabulary.",
        "sketch": None
    },
    "reading-point-of-view-and-line-of-argument": {
        "photo": "workplace_office/boardroom_debate.jpg",
        "photo_caption": "Corporate meeting assessing stakeholder arguments, conflicting viewpoints, and balanced perspectives.",
        "character": "abdul",
        "character_quote": "Identify whether the writer presents a balanced view or selects evidence that favours one perspective.",
        "sketch": None
    },
    "reading-styles-of-writing-and-voice": {
        "photo": "workplace_office/formal_contract_letter.jpg",
        "photo_caption": "Formal legal contract and institutional correspondence exemplifying official register and professional voice.",
        "character": "abdul",
        "character_quote": "Formal writing avoids colloquialisms and contractions, maintaining a detached, professional register.",
        "sketch": None
    },
    "reading-text-types": {
        "photo": "everyday_objects/mixed_text_types.jpg",
        "photo_caption": "Diverse collection of text types: instruction manuals, brochures, news articles, and business letters.",
        "character": "priya",
        "character_quote": "An article informs and entertains; a report analyses facts; an instruction manual gives sequential imperatives.",
        "sketch": None
    },
    "reading-comparing-texts": {
        "photo": "workplace_office/dual_screen_research.jpg",
        "photo_caption": "Analyst evaluating two contrasting texts and cross-referencing information across dual screens.",
        "character": "abdul",
        "character_quote": "Use a comparison table with Text A vs Text B to track points of agreement and disagreement side by side.",
        "sketch": None
    },
    "reading-why-do-writers-write": {
        "photo": "journalism_media/journalist_writing.jpg",
        "photo_caption": "Journalist drafting investigative article to inform, persuade, and raise awareness.",
        "character": "abdul",
        "character_quote": "Examine the verbs used: is the writer trying to advise, warn, criticise, or sell?",
        "sketch": None
    },
    "reading-the-exam": {
        "photo": "classroom_studying_adults/exam_desk_clock.jpg",
        "photo_caption": "Focused exam desk with countdown clock, question booklet, and timed reading strategy notes.",
        "character": "abdul",
        "character_quote": "Read the questions first before tackling the texts, and check the mark tariff to gauge detail required.",
        "sketch": None
    },

    # --- ENGLISH WRITING TOPICS ---
    "writing-planning-your-answer": {
        "photo": "classroom_studying_adults/mindmap_planning.jpg",
        "photo_caption": "Detailed spider diagram and structured bullet outline planning an extended writing task.",
        "character": "abdul",
        "character_quote": "Spend the first 5 minutes planning your audience, tone, and bullet points. It saves you from rambling.",
        "sketch": None
    },
    "writing-communicating": {
        "photo": "workplace_office/formal_letterhead.jpg",
        "photo_caption": "Professional formal letterhead correspondence drafted for clear workplace communication.",
        "character": "marcus",
        "character_quote": "Always tailor your language to who is reading: formal for a manager or client, friendly for community volunteers.",
        "sketch": None
    },
    "writing-context": {
        "photo": "healthcare_care/hospital_noticeboard.jpg",
        "photo_caption": "Hospital department staff noticeboard displaying institutional memos, notices, and procedural guidelines.",
        "character": "abdul",
        "character_quote": "Consider the setting and purpose before deciding on formality and vocabulary choices.",
        "sketch": None
    },
    "writing-assessing-audience": {
        "photo": "workplace_office/audience_personas.jpg",
        "photo_caption": "Marketing team mapping demographic profiles and reader personas to tailor writing register.",
        "character": "marcus",
        "character_quote": "Writing for teenagers requires energetic, direct language; writing for council officials requires formal register.",
        "sketch": None
    },
    "writing-form-presentational-and-language-features": {
        "photo": "workplace_office/desktop_publishing.jpg",
        "photo_caption": "Desktop publishing layout designing formal workplace newsletters with structured headings and columns.",
        "character": "abdul",
        "character_quote": "Include all statutory format markers: date and addresses for letters, subject line for emails.",
        "sketch": None
    },
    "writing-organisational-markers": {
        "photo": "classroom_studying_adults/highlighted_transitions.jpg",
        "photo_caption": "Annotated article draft highlighting discourse markers, linking phrases, and paragraph transitions.",
        "character": "abdul",
        "character_quote": "Use organisational markers: 'Firstly', 'In addition', 'Consequently', 'On the other hand'.",
        "sketch": None
    },
    "writing-linking-up-your-answer": {
        "photo": "construction_trades/interlocking_masonry.jpg",
        "photo_caption": "Interlocking masonry blocks illustrating seamless sentence structure and cohesive paragraph building.",
        "character": "priya",
        "character_quote": "Each paragraph should focus on one main point introduced with a topic sentence.",
        "sketch": None
    },
    "writing-grammar": {
        "photo": "classroom_studying_adults/grammar_proofreading.jpg",
        "photo_caption": "Proofreader marking syntax, subject-verb agreement, and clause structure on printed proofs.",
        "character": "priya",
        "character_quote": "Avoid comma splices. Never join two complete sentences with just a comma — use a full stop, semicolon, or conjunction.",
        "sketch": None
    },
    "writing-tenses": {
        "photo": "healthcare_care/shift_handover_log.jpg",
        "photo_caption": "Hospital clinical shift handover log requiring strict consistency between past observations and current actions.",
        "character": "abdul",
        "character_quote": "Choose your primary tense based on the task and ensure you do not switch unnecessarily between past and present.",
        "sketch": None
    },
    "writing-perfecting-your-punctuation": {
        "photo": "workplace_office/typography_punctuation_blocks.jpg",
        "photo_caption": "Wooden movable type blocks highlighting colons, semicolons, speech marks, and apostrophes.",
        "character": "priya",
        "character_quote": "Use a colon to introduce a list or explanation, and a semicolon to connect two closely linked independent clauses.",
        "sketch": None
    },
    "writing-spelling": {
        "photo": "classroom_studying_adults/spelling_letter_tiles.jpg",
        "photo_caption": "Letter tiles spelling complex words illustrating phonics, silent letters, and spelling patterns.",
        "character": "priya",
        "character_quote": "Watch out for homophones: their/there/they're, practice (noun) vs practise (verb).",
        "sketch": None
    },
    "writing-fantastic-finalising": {
        "photo": "workplace_office/checklist_clipboard.jpg",
        "photo_caption": "Quality assurance checklist on clipboard verifying spelling, punctuation, and grammar before submission.",
        "character": "abdul",
        "character_quote": "Read your final draft backwards sentence-by-sentence to spot spelling errors your brain would otherwise auto-correct.",
        "sketch": None
    },
    "writing-why-are-you-writing": {
        "photo": "retail_shop/call_to_action_flyer.jpg",
        "photo_caption": "Community call-to-action campaign flyer with clear imperative purpose and persuasive appeal.",
        "character": "abdul",
        "character_quote": "State your core objective clearly in the opening paragraph and reinforce it in your final conclusion.",
        "sketch": None
    },
    "writing-the-exam": {
        "photo": "classroom_studying_adults/writing_exam_paper.jpg",
        "photo_caption": "Candidate completing Pearson Edexcel Functional Skills English writing exam paper under timed conditions.",
        "character": "abdul",
        "character_quote": "Allocate time strictly according to marks: Task 1 (around 25-30 mins), Task 2 (around 30-35 mins), proofreading (10 mins).",
        "sketch": None
    },

    # --- FORMAT DIRECTORY (REVIEWS, LETTERS, ARTICLES, ETC.) ---
    "format-article": {
        "photo": "workplace_office/desk_laptop.jpg",
        "photo_caption": "Remote professional working on community article with laptop and reference documents.",
        "character": "abdul",
        "character_quote": "Use an engaging headline, byline, and clear subheadings to guide your reader through the article.",
        "sketch": None
    },
    "format-email": {
        "photo": "email_online_safety/email_inbox_laptop.jpg",
        "photo_caption": "Professional workplace email communication and inbox correspondence.",
        "character": "priya",
        "character_quote": "Always include a clear Subject line and match your greeting to your relationship with the recipient.",
        "sketch": None
    },
    "format-letter": {
        "photo": "workplace_office/writing_notes.jpg",
        "photo_caption": "Formal business letter drafting with addresses, formal dates, and signature.",
        "character": "abdul",
        "character_quote": "Remember: Dear Mr/Ms [Name] ends with 'Yours sincerely'. Dear Sir/Madam ends with 'Yours faithfully'.",
        "sketch": None
    },
    "format-report": {
        "photo": "workplace_office/whiteboard_planning.jpg",
        "photo_caption": "Structured workplace report investigation with data headings and recommendations.",
        "character": "priya",
        "character_quote": "A formal report needs: To, From, Date, Purpose, factual subheadings, and numbered recommendations.",
        "sketch": None
    },
    "format-incident-report": {
        "photo": "construction_trades/safety_hardhat.jpg",
        "photo_caption": "Health and safety workplace incident documentation and hazard prevention.",
        "character": "marcus",
        "character_quote": "State facts in chronological order (date, time, what happened, first aid, preventative action). Keep emotion out.",
        "sketch": None
    },
    "format-leaflet": {
        "photo": "money_shopping_bills/calculator_finance.jpg",
        "photo_caption": "Informational advice leaflet outlining practical budgeting steps and guidance.",
        "character": "sarah",
        "character_quote": "Use imperative action verbs (Set up, Avoid, Calculate) and bullet points to make advice easy to follow.",
        "sketch": None
    },
    "format-review": {
        "photo": "retail_shop/clothing_store.jpg",
        "photo_caption": "Evaluating facilities, customer service, value for money, and overall ratings.",
        "character": "sam",
        "character_quote": "A great review balances pros and cons before giving an honest, reasoned star rating and recommendation.",
        "sketch": None
    },
    "format-feedback-form": {
        "photo": "everyday_objects/delivery_parcel.jpg",
        "photo_caption": "Customer feedback form documenting order delivery issues and resolution requests.",
        "character": "sam",
        "character_quote": "Reference your order number, state the defect clearly, explain the inconvenience, and request a specific fix.",
        "sketch": None
    },
    "format-blog-forum": {
        "photo": "classroom_studying_adults/student_studying_laptop.jpg",
        "photo_caption": "Online educational community discussion, debate thread, and collaborative learning.",
        "character": "priya",
        "character_quote": "In a forum post, open with a friendly greeting, explore both perspectives fairly, and invite replies at the end.",
        "sketch": None
    },
    "format-newsletter": {
        "photo": "kitchen_cooking_recipes/chopping_vegetables.jpg",
        "photo_caption": "Community garden harvest celebration and volunteer newsletter announcements.",
        "character": "marcus",
        "character_quote": "Use an enthusiastic tone, celebrate team achievements, and include a clear call to action with contact details.",
        "sketch": None
    },
    "format-diary": {
        "photo": "workplace_office/typing_keyboard.jpg",
        "photo_caption": "Workplace placement reflective diary entry tracking skill breakthroughs and goals.",
        "character": "sam",
        "character_quote": "Write in first person ('I felt', 'I learned') and conclude with two actionable goals for the coming week.",
        "sketch": None
    }
}

SEMANTIC_PATTERNS = [
    (r"\b(multipl|scaling|times table)\b", "functional-skills-multiplication"),
    (r"\b(divid|bus stop|quotient|sharing with remainder)\b", "functional-skills-division"),
    (r"\b(perimeters?)\b", "functional-skills-perimeter"),
    (r"\b(circles?|circumferences?|radius|diameter)\b", "functional-skills-circles"),
    (r"\b(surface areas?)\b", "functional-skills-surface-area"),
    (r"\b(areas?|rectangles?|triangles?|trapeziums?|compound shapes?)\b", "functional-skills-area"),
    (r"\b(volumes?|capacity|cuboids?|prisms?)\b", "functional-skills-volume"),
    (r"\b(ratios?)\b", "functional-skills-ratio"),
    (r"\b(proportions?|direct proportion|inverse proportion)\b", "functional-skills-proportion"),
    (r"\b(speeds?|distances?|journeys?|compound units)\b", "functional-skills-speed"),
    (r"\b(densit(?:y|ies)|mass|volume)\b", "functional-skills-density"),
    (r"\b(temperatures?|celsius|thermometers?)\b", "functional-skills-temperature"),
    (r"\b(negative numbers?|below zero|overdrafts?)\b", "functional-skills-negative-numbers"),
    (r"\b(probabilities?|tree diagrams?|chance|outcomes?)\b", "functional-skills-probability"),
    (r"\b(scatters?|correlations?|scatter graphs?)\b", "functional-skills-scatter-graphs"),
    (r"\b(pie charts?|sectors?)\b", "functional-skills-pie-charts"),
    (r"\b(times?|clocks?|24-hour|12-hour|timetables?)\b", "functional-skills-time"),
    (r"\b(moneys?|finances?|currency|change|coins|wage|salary)\b", "functional-skills-money"),
    (r"\b(best buys?|unit pric(?:e|ing))\b", "functional-skills-best-buys"),
    (r"\b(interests?|compound interest|depreciation)\b", "functional-skills-interest-and-compound-interest"),
    (r"\b(percentages?|discounts?|multipliers?|vat)\b", "functional-skills-percentages"),
    (r"\b(fractions?|mixed numbers?|improper fractions?)\b", "functional-skills-fractions"),
    (r"\b(fdp|fractions decimals percentages)\b", "functional-skills-fractions-decimals-and-percentages"),
    (r"\b(decimals?|decimal point)\b", "functional-skills-decimals"),
    (r"\b(tables?|tally|frequency|two-way|grouped data|data tables?)\b", "functional-skills-data-tables"),
    (r"\b(means?|medians?|modes?|ranges?|averages?)\b", "functional-skills-mean-median-mode-and-range"),
    (r"\b(unit conversions?|metrics?|imperials?)\b", "functional-skills-unit-conversions"),
    (r"\b(lengths?|millimetres?|centimetres?|metres?)\b", "functional-skills-length"),
    (r"\b(weights?|mass|grams?|kilograms?|tonnes?)\b", "functional-skills-weight"),
    (r"\b(capacit(?:y|ies)|litres?|millilitres?)\b", "functional-skills-capacity"),
    (r"\b(scale drawings?|maps?|bearings?|compass)\b", "functional-skills-maps-and-scale-drawings"),
    (r"\b(coordinates?|cartesian|axes|quadrants?)\b", "functional-skills-coordinates"),
    (r"\b(angles?|degrees?|protractors?)\b", "functional-skills-angles"),
    (r"\b(2d shapes?|polygons?|quadrilaterals?)\b", "functional-skills-2d-shapes"),
    (r"\b(3d shapes?|vertices|edges|faces)\b", "functional-skills-3d-shapes"),
    (r"\b(nets?|folding)\b", "functional-skills-nets"),
    (r"\b(plans? and elevations?|elevations?)\b", "functional-skills-plans-and-elevations"),
    (r"\b(formulas?|algebra|substitution)\b", "functional-skills-formulas"),
    (r"\b(place values?|large numbers?|ordering numbers?)\b", "functional-skills-numbers-and-place-value"),
    (r"\b(bidmas|order of operations)\b", "functional-skills-bidmas"),
    (r"\b(roundings?|estimat(?:e|ing|ion)|approximat(?:e|ing|ion))\b", "functional-skills-rounding-and-estimating"),
    (r"\b(facts?|opinions?)\b", "reading-fact-or-opinion"),
    (r"\b(presentationals?|layout devices?)\b", "reading-presentational-features"),
    (r"\b(comparing texts?)\b", "reading-comparing-texts"),
    (r"\b(plannings?|draftings?)\b", "writing-planning-your-answer"),
    (r"\b(grammars?|punctuations?|spellings?|spag)\b", "writing-grammar"),
    (r"\b(communicatings?)\b", "writing-communicating"),
    (r"\b(articles?)\b", "format-article"),
    (r"\b(emails?)\b", "format-email"),
    (r"\b(formal letters?|letters?)\b", "format-letter"),
    (r"\b(incident reports?)\b", "format-incident-report"),
    (r"\b(reports?)\b", "format-report"),
    (r"\b(leaflets?|brochures?)\b", "format-leaflet"),
    (r"\b(reviews?)\b", "format-review"),
    (r"\b(feedback forms?|forms?)\b", "format-feedback-form"),
    (r"\b(forums?|blogs?)\b", "format-blog-forum"),
    (r"\b(newsletters?)\b", "format-newsletter"),
    (r"\b(diar(?:y|ies)|reflective entries?)\b", "format-diary"),
]

import re

def get_topic_visual(slug_or_clean_topic):
    """Returns visual configuration tuple: (photo_rel_path, caption, char_name, char_quote, sketch_svg_html)"""
    norm = slug_or_clean_topic.lower().replace(".html", "").strip()
    
    # 1. Exact match in registry
    if norm in TOPIC_VISUAL_REGISTRY:
        v = TOPIC_VISUAL_REGISTRY[norm]
        svg = v["sketch"]() if v.get("sketch") else ""
        return v["photo"], v["photo_caption"], v["character"], v["character_quote"], svg
    
    # 2. Semantic regex pattern match
    for pattern, target_slug in SEMANTIC_PATTERNS:
        if re.search(pattern, norm, re.IGNORECASE):
            if target_slug in TOPIC_VISUAL_REGISTRY:
                v = TOPIC_VISUAL_REGISTRY[target_slug]
                svg = v["sketch"]() if v.get("sketch") else ""
                return v["photo"], v["photo_caption"], v["character"], v["character_quote"], svg

    # 3. Direct substring lookup
    for key, v in TOPIC_VISUAL_REGISTRY.items():
        if key in norm or norm in key:
            svg = v["sketch"]() if v.get("sketch") else ""
            return v["photo"], v["photo_caption"], v["character"], v["character_quote"], svg
            
    # 4. Default fallbacks
    if "reading" in norm:
        return "classroom_studying_adults/student_studying_laptop.jpg", "Adult learner analysing texts and comprehending non-fiction articles.", "priya", "Read the text actively with a pen in hand!", ""
    elif "writing" in norm or "slc" in norm:
        return "workplace_office/writing_notes.jpg", "Drafting structured workplace documents and reports.", "abdul", "Check every sentence has a capital letter and end punctuation!", ""
    else:
        return "money_shopping_bills/calculator_finance.jpg", "Applying functional mathematical skills to solve practical workplace problems.", "abdul", "Read the question twice and underline the units required in the final answer!", ""
