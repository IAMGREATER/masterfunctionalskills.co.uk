#!/usr/bin/env python3
"""
Adds big, high-visibility SVG diagrams for the Speed-Distance-Time (SDT) triangle
and Mass-Density-Volume (MDV) triangle across the revision pages and cards.
"""
import sys, os, pprint

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

def get_big_sdt_svg_html():
    return """
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#eff6ff; color:#1e40af; border:1px solid #bfdbfe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-gauge" style="margin-right:6px; color:#2563eb;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Speed, Distance &amp; Time (S-D-T) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Place your finger or thumb over the letter you want to find. The remaining letters give you the exact calculation formula.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between S and T -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#b45309" text-anchor="middle">×</text>

          <!-- Top Chamber: Distance (D) -->
          <circle cx="160" cy="98" r="44" fill="#dbeafe" stroke="#2563eb" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#1e40af" text-anchor="middle">D</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">DISTANCE</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#3b82f6" text-anchor="middle">(miles, km, m)</text>

          <!-- Bottom Left Chamber: Speed (S) -->
          <circle cx="95" cy="235" r="40" fill="#fef3c7" stroke="#d97706" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#b45309" text-anchor="middle">S</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">SPEED</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#b45309" text-anchor="middle">(mph, km/h)</text>

          <!-- Bottom Right Chamber: Time (T) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">T</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">TIME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(hours, mins)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Distance -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#1d4ed8">1. COVER DISTANCE (D)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Distance = Speed × Time</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#2563eb"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = S × T</text>

            <!-- Box 2: Speed -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#b45309">2. COVER SPEED (S)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Speed = Distance ÷ Time</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#d97706"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">S = D ÷ T</text>

            <!-- Box 3: Time -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER TIME (T)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Time = Distance ÷ Speed</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">T = D ÷ S</text>

            <!-- Decimal Time Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">⏱️ DECIMAL TIME RULE (DIVIDE MINS BY 60):</text>
            <text x="177" y="268" font-size="11" font-weight="800" fill="#b91c1c" text-anchor="middle">15m = 0.25h &bull; 30m = 0.5h &bull; 45m = 0.75h (NEVER 0.45!)</text>
          </g>
        </svg>
      </div>
    </div>
    """

def get_big_mdv_svg_html():
    return """
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#f5f3ff; color:#5b21b6; border:1px solid #ddd6fe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-cube" style="margin-right:6px; color:#7c3aed;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Mass, Density &amp; Volume (M-D-V) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Remember: <strong>Mass is always on top (M)</strong>. Cover the quantity you need to find with your finger.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between D and V -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#0369a1" text-anchor="middle">×</text>

          <!-- Top Chamber: Mass (M) -->
          <circle cx="160" cy="98" r="44" fill="#ede9fe" stroke="#7c3aed" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#5b21b6" text-anchor="middle">M</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#4c1d95" text-anchor="middle">MASS</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#7c3aed" text-anchor="middle">(grams, kg, tonnes)</text>

          <!-- Bottom Left Chamber: Density (D) -->
          <circle cx="95" cy="235" r="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#0369a1" text-anchor="middle">D</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#075985" text-anchor="middle">DENSITY</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">(g/cm³, kg/m³)</text>

          <!-- Bottom Right Chamber: Volume (V) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">V</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">VOLUME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(cm³, m³, litres)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Mass -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#5b21b6">1. COVER MASS (M)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Mass = Density × Volume</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#7c3aed"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">M = D × V</text>

            <!-- Box 2: Density -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#0369a1">2. COVER DENSITY (D)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Density = Mass ÷ Volume</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#0284c7"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = M ÷ V</text>

            <!-- Box 3: Volume -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER VOLUME (V)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Volume = Mass ÷ Density</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">V = M ÷ D</text>

            <!-- Units Matching Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">⚖️ CHECK MATCHING UNITS BEFORE CALCULATING:</text>
            <text x="177" y="268" font-size="10.5" font-weight="800" fill="#15803d" text-anchor="middle">g with cm³ &rarr; g/cm³  |  kg with m³ &rarr; kg/m³ (1 L water = 1 kg)</text>
          </g>
        </svg>
      </div>
    </div>
    """

def apply_to_domain3():
    import maths_domain3_measures as d3
    topics = d3.TOPICS_DOMAIN3

    sdt_svg = get_big_sdt_svg_html()
    mdv_svg = get_big_mdv_svg_html()

    for t in topics:
        if t['filename'] == 'functional-skills-speed.html':
            t['skills'] = [
                {
                    'title': 'The Speed, Distance & Time Formula Triangle (S-D-T)',
                    'summary': 'Use the big triangle to find Speed, Distance, or Time with complete confidence.',
                    'content_html': sdt_svg + """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px 22px; margin:18px 0;">
                  <h4 style="margin:0 0 10px 0; color:#0f172a; font-size:1.1rem; font-weight:800;">Working with Compound Speed Units (mph and km/h)</h4>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>Finding Speed:</strong> <em>Average Speed = Total Distance (miles) ÷ Total Time (hours).</em></li>
                    <li><strong>Hours &amp; Minutes to Decimal:</strong> 2 hours 15 mins = 2 + (15 ÷ 60) = 2.25 hours.</li>
                    <li><strong>Decimal Time to Minutes:</strong> If Time = 1.4 hours, Minutes = 0.4 × 60 = 24 mins &rarr; 1 hr 24 mins.</li>
                  </ul>
                </div>
                    """
                }
            ]
        elif t['filename'] == 'functional-skills-density.html':
            t['skills'] = [
                {
                    'title': 'The Mass, Density & Volume Formula Triangle (M-D-V)',
                    'summary': 'Mass is always on top. Use the big triangle to find Mass, Density, or Volume.',
                    'content_html': mdv_svg + """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px 22px; margin:18px 0;">
                  <h4 style="margin:0 0 10px 0; color:#0f172a; font-size:1.1rem; font-weight:800;">Density, Pressure &amp; Compound Measure Relationships</h4>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>Density:</strong> How heavy an object is for its size: <em>Density = Mass (g) ÷ Volume (cm³).</em></li>
                    <li><strong>Pressure:</strong> Force applied over a given surface: <em>Pressure (N/m²) = Force (N) ÷ Area (m²).</em></li>
                    <li><strong>Water Benchmark:</strong> 1 litre of pure water has a volume of 1,000 cm³ and a mass of exactly 1 kg (density = 1 kg/L).</li>
                  </ul>
                </div>
                    """
                }
            ]

    with open('maths_domain3_measures.py', 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n"""Maths Domain 3: Measures, Instruments & Compound Units (7 Core Topics)"""\n')
        f.write('TOPICS_DOMAIN3 = ' + repr(topics) + '\n')
    print('✓ Embedded big SDT and MDV triangles into maths_domain3_measures.py')

def apply_to_domain2():
    import maths_domain2_finance_ratio as d2
    topics = d2.TOPICS_DOMAIN2

    sdt_svg = get_big_sdt_svg_html()
    mdv_svg = get_big_mdv_svg_html()

    for t in topics:
        if t['filename'] == 'functional-skills-formulas.html':
            # Add Skill 2 with both triangles!
            t['skills'] = [
                {
                    'title': 'Step-by-Step Substitution Method',
                    'summary': 'Converting formulas into solvable numerical equations.',
                    'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Write the formula clearly:</strong> e.g. <em>Cost = Callout + (Hourly Rate × Hours).</em></li>
                    <li><strong>Replace letters with numbers:</strong> Write numbers directly below the corresponding variables.</li>
                    <li><strong>Apply BIDMAS:</strong> Perform bracketed terms and multiplications before additions.</li>
                  </ol>
                </div>
                    """
                },
                {
                    'title': 'Formula Triangles: Speed (SDT) & Density (MDV)',
                    'summary': 'Two essential formula triangles frequently assessed in Level 1 & Level 2 Functional Skills.',
                    'content_html': sdt_svg + "<div style='height:20px;'></div>" + mdv_svg
                }
            ]

    with open('maths_domain2_finance_ratio.py', 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n"""Maths Domain 2: Financial Maths, Ratio & Proportion (7 Core Topics)"""\n')
        f.write('TOPICS_DOMAIN2 = ' + repr(topics) + '\n')
    print('✓ Embedded big SDT and MDV triangles into functional-skills-formulas.html in domain 2')

if __name__ == '__main__':
    apply_to_domain3()
    apply_to_domain2()
