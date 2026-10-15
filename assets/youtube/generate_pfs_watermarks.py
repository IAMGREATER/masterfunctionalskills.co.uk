#!/usr/bin/env python3
"""
PFS (Pass Functional Skills) Official YouTube Video Watermarks Generator
Creates high-contrast, transparent video watermarks calibrated for YouTube Studio:
- Option 1: Iconic PFS Green Checkmark 'P' (Pure Transparent Icon)
- Option 2: Circular PFS Navy & Lime Badge (Transparent)
- Option 3: High-Converting Red 'SUBSCRIBE + PFS' Action Button (Transparent)
- Option 4: Full Brand Lockup 'PASS FUNCTIONAL SKILLS' (Transparent)
Outputs both 150x150 px (YouTube specification) and 300x300 px (Retina/High-DPI).
"""

import os
import shutil
import subprocess

PFS_OUT_DIR = "/home/subi/Pictures/PFS_YouTube_Watermarks"
USER_PIC_DIR = "/home/subi/Pictures/MFS_YouTube_Branding"
WEB_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/youtube"

os.makedirs(PFS_OUT_DIR, exist_ok=True)
os.makedirs(USER_PIC_DIR, exist_ok=True)
os.makedirs(WEB_DIR, exist_ok=True)

def render(svg_code, filename_base):
    svg_path = os.path.join(PFS_OUT_DIR, f"{filename_base}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_code)

    # 150x150 (Official YouTube upload size)
    png_150 = os.path.join(PFS_OUT_DIR, f"{filename_base}_150x150.png")
    subprocess.run(["rsvg-convert", "-w", "150", "-h", "150", svg_path, "-o", png_150], check=True)
    shutil.copyfile(png_150, os.path.join(USER_PIC_DIR, f"{filename_base}_150x150.png"))
    shutil.copyfile(png_150, os.path.join(WEB_DIR, f"{filename_base}_150x150.png"))

    # 300x300 (High-DPI)
    png_300 = os.path.join(PFS_OUT_DIR, f"{filename_base}_300x300.png")
    subprocess.run(["rsvg-convert", "-w", "300", "-h", "300", svg_path, "-o", png_300], check=True)
    shutil.copyfile(png_300, os.path.join(USER_PIC_DIR, f"{filename_base}_300x300.png"))
    shutil.copyfile(png_300, os.path.join(WEB_DIR, f"{filename_base}_300x300.png"))
    
    # Also copy SVGs
    shutil.copyfile(svg_path, os.path.join(USER_PIC_DIR, f"{filename_base}.svg"))
    shutil.copyfile(svg_path, os.path.join(WEB_DIR, f"{filename_base}.svg"))

    print(f"Generated: {filename_base} (150x150 & 300x300)")

# Core SVG snippet for the iconic PFS Checkmark 'P'
PFS_ICON_SNIPPET = '''
  <g filter="url(#pfsShadow)">
    <!-- White Checkmark -->
    <path d="M27.52,24.92l-1.35,1.75c-2.15,2.78-6.14,3.3-8.92,1.15l-8.92-6.88c-1.88-1.45-2.23-4.14-.78-6.01,1.45-1.88,4.14-2.22,6.02-.78l7.17,5.53L33.65,2.91c2.1,2.3 4.5,5.2 5.98,7.09l-12.11,15.71Z" fill="#ffffff" />
    <!-- Vibrant Green P -->
    <path d="M27.52,24.92l-1.35,1.75c-2.15,2.78-6.14,3.3-8.92,1.15l-8.92-6.88c-1.88-1.45-2.23-4.14-.78-6.01,1.45-1.88,4.14-2.22,6.02-.78l7.17,5.53L33.65,2.91c-2.85-1.84-6.25-2.91-9.89-2.91H4.28C1.91,0,0,1.91,0,4.28v37.75c0,2.36,1.91,4.28,4.28,4.28,4.71,0,8.85-3.13,10.13-7.67l.59-2.08h8.77c10.09,0,18.28-8.18,18.28-18.28h0c0-3.3-.88-6.39-2.41-9.07l-12.11,15.71Z" fill="url(#pfsGreen)" />
  </g>
'''

SHARED_DEFS = '''
  <defs>
    <linearGradient id="pfsGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f000" />
      <stop offset="100%" stop-color="#00a800" />
    </linearGradient>
    <linearGradient id="pfsLime" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4ade80" />
      <stop offset="100%" stop-color="#22c55e" />
    </linearGradient>
    <linearGradient id="ytRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff0000" />
      <stop offset="100%" stop-color="#b91c1c" />
    </linearGradient>
    <radialGradient id="navyBadgeBg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1e2e47" />
      <stop offset="60%" stop-color="#121f33" />
      <stop offset="100%" stop-color="#080e18" />
    </radialGradient>
    <filter id="pfsShadow" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="2.5" stdDeviation="3.5" flood-color="#000000" flood-opacity="0.8" />
    </filter>
    <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#000000" flood-opacity="0.75" />
    </filter>
  </defs>
'''

# ------------------------------------------------------------------------------
# 1. OPTION 1: PURE PFS ICON (TRANSPARENT BACKGROUND)
# ------------------------------------------------------------------------------
svg_opt1 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 50 54" width="300" height="300">
  {SHARED_DEFS}
  {PFS_ICON_SNIPPET}
</svg>'''
render(svg_opt1, "pfs_watermark_icon_transparent")

# ------------------------------------------------------------------------------
# 2. OPTION 2: CIRCULAR PFS BADGE (TRANSPARENT BACKGROUND)
# ------------------------------------------------------------------------------
svg_opt2 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  {SHARED_DEFS}
  <!-- Navy Circular Badge -->
  <circle cx="150" cy="150" r="140" fill="url(#navyBadgeBg)" stroke="url(#pfsGreen)" stroke-width="7" filter="url(#cardShadow)" />
  <circle cx="150" cy="150" r="128" fill="none" stroke="#22c55e" stroke-width="1.8" stroke-opacity="0.4" stroke-dasharray="6,6" />

  <!-- Centered PFS Icon -->
  <g transform="translate(150, 130) scale(3.8) translate(-21, -23)">
    {PFS_ICON_SNIPPET}
  </g>

  <!-- Bottom Brand Text -->
  <text x="150" y="248" 
        text-anchor="middle" 
        font-family="'Montserrat', 'Poppins', sans-serif" 
        font-size="22" 
        font-weight="900" 
        letter-spacing="5" 
        fill="#ffffff">PASS</text>
  
  <text x="150" y="268" 
        text-anchor="middle" 
        font-family="'Montserrat', sans-serif" 
        font-size="11" 
        font-weight="800" 
        letter-spacing="2.5" 
        fill="#22c55e">FUNCTIONAL SKILLS</text>
</svg>'''
render(svg_opt2, "pfs_watermark_circle_badge")

# ------------------------------------------------------------------------------
# 3. OPTION 3: HIGH-CONVERTING SUBSCRIBE BUTTON (TRANSPARENT BACKGROUND)
# ------------------------------------------------------------------------------
svg_opt3 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  {SHARED_DEFS}
  <!-- Dark Studio Card -->
  <rect x="15" y="15" width="270" height="270" rx="44" fill="#121f33" stroke="url(#pfsGreen)" stroke-width="3" filter="url(#cardShadow)" />

  <!-- PFS Icon at Top -->
  <g transform="translate(150, 92) scale(2.6) translate(-21, -23)">
    {PFS_ICON_SNIPPET}
  </g>

  <!-- Title -->
  <text x="150" y="172" 
        text-anchor="middle" 
        font-family="'Montserrat', 'Poppins', sans-serif" 
        font-size="15" 
        font-weight="900" 
        letter-spacing="2" 
        fill="#ffffff">PASS FUNCTIONAL SKILLS</text>

  <!-- Red YouTube Subscribe Pill -->
  <g transform="translate(35, 195)">
    <rect x="0" y="0" width="230" height="62" rx="16" fill="url(#ytRed)" />
    <!-- YouTube Play Icon -->
    <rect x="22" y="15" width="40" height="32" rx="7" fill="#ffffff" />
    <polygon points="37,23 50,31 37,39" fill="#b91c1c" />
    <!-- Text -->
    <text x="76" y="40" font-family="'Montserrat', sans-serif" font-size="19" font-weight="900" letter-spacing="1.5" fill="#ffffff">SUBSCRIBE</text>
  </g>
</svg>'''
render(svg_opt3, "pfs_watermark_subscribe_button")

# ------------------------------------------------------------------------------
# 4. OPTION 4: FULL BRAND SQUARE LOCKUP (TRANSPARENT BACKGROUND)
# ------------------------------------------------------------------------------
svg_opt4 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  {SHARED_DEFS}
  <rect x="15" y="15" width="270" height="270" rx="36" fill="#121f33" stroke="#22c55e" stroke-width="2.5" filter="url(#cardShadow)" />
  
  <!-- Large PFS Icon -->
  <g transform="translate(150, 115) scale(3.2) translate(-21, -23)">
    {PFS_ICON_SNIPPET}
  </g>

  <!-- Bold Brand Lockup -->
  <text x="150" y="215" 
        text-anchor="middle" 
        font-family="'Montserrat', 'Poppins', sans-serif" 
        font-size="34" 
        font-weight="900" 
        letter-spacing="4" 
        fill="#ffffff">PASS</text>

  <text x="150" y="248" 
        text-anchor="middle" 
        font-family="'Montserrat', sans-serif" 
        font-size="14.5" 
        font-weight="800" 
        letter-spacing="2.5" 
        fill="url(#pfsGreen)">FUNCTIONAL SKILLS</text>
</svg>'''
render(svg_opt4, "pfs_watermark_brand_lockup")

print("=== All PFS Video Watermarks Successfully Generated ===")
