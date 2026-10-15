#!/usr/bin/env python3
"""
MFS Video Watermark Generator
Creates high-contrast, transparent video watermarks calibrated for YouTube Studio:
- Option 1: Iconic 'M' Graduation Cap Emblem (Transparent, High-Contrast Glow)
- Option 2: Circular 'M' Metallic Badge (Transparent)
- Option 3: Red 'SUBSCRIBE + M' High-Converting Action Button (Transparent)
Generates both 150x150 px (YouTube requirement) and 300x300 px (Retina/High-DPI).
"""

import os
import shutil
import subprocess

OUT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/youtube"
USER_PIC_DIR = "/home/subi/Pictures/MFS_YouTube_Branding"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(USER_PIC_DIR, exist_ok=True)

def render(svg_code, filename_base):
    svg_path = os.path.join(OUT_DIR, f"{filename_base}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_code)

    # 150x150
    png_150 = os.path.join(OUT_DIR, f"{filename_base}_150x150.png")
    subprocess.run(["rsvg-convert", "-w", "150", "-h", "150", svg_path, "-o", png_150], check=True)
    shutil.copyfile(png_150, os.path.join(USER_PIC_DIR, f"{filename_base}_150x150.png"))

    # 300x300
    png_300 = os.path.join(OUT_DIR, f"{filename_base}_300x300.png")
    subprocess.run(["rsvg-convert", "-w", "300", "-h", "300", svg_path, "-o", png_300], check=True)
    shutil.copyfile(png_300, os.path.join(USER_PIC_DIR, f"{filename_base}_300x300.png"))
    
    print(f"Generated: {filename_base} (150x150 & 300x300)")

# ------------------------------------------------------------------------------
# OPTION 1: PURE 'M' EMBLEM WITH CONTRAST SHADOW (TRANSPARENT)
# Works on any video background (light or dark)
# ------------------------------------------------------------------------------
svg_opt1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <defs>
    <linearGradient id="capGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <filter id="watermarkShadow" x="-30%" y="-30%" width="160%" height="160%">
      <!-- Strong dark outline drop shadow so white M and blue cap are visible on white backgrounds -->
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.85" />
      <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#000000" flood-opacity="0.9" />
    </filter>
  </defs>

  <g transform="translate(150, 150) scale(5.4) translate(-32, -29.5)" filter="url(#watermarkShadow)">
    <!-- Cap Diamond -->
    <path d="M 32 9 L 49 16.5 L 32 24 L 15 16.5 Z" fill="url(#capGrad)" stroke="#93c5fd" stroke-width="0.9" />
    <path d="M 32 10.5 L 46.5 16.5 L 32 22.5 L 17.5 16.5 Z" fill="#0f172a" fill-opacity="0.4" />
    <!-- Cap Skullcap -->
    <path d="M 44 20 L 44 27.5 C 44 30.5 38 32.5 32 32.5 C 26 32.5 20 30.5 20 27.5 L 20 20" 
          fill="none" stroke="url(#capGrad)" stroke-width="2.6" stroke-linecap="round" />
    <!-- Tassel -->
    <path d="M 49 16.5 C 50 20 50.5 22 51 24.5" fill="none" stroke="url(#goldGrad)" stroke-width="2.2" stroke-linecap="round" />
    <circle cx="51.2" cy="25.5" r="1.8" fill="url(#goldGrad)" />
    <circle cx="32" cy="16.5" r="1.5" fill="url(#goldGrad)" />

    <!-- Bold White 'M' -->
    <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" 
          fill="#ffffff" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" />
  </g>
</svg>'''
render(svg_opt1, "mfs_watermark_emblem_transparent")

# ------------------------------------------------------------------------------
# OPTION 2: CIRCULAR METALLIC 'M' BADGE (TRANSPARENT BACKGROUND)
# Distinct badge icon that looks like a high-end stamp in the video corner
# ------------------------------------------------------------------------------
svg_opt2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <defs>
    <radialGradient id="badgeBg" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1e3a8a" />
      <stop offset="60%" stop-color="#0a192f" />
      <stop offset="100%" stop-color="#020817" />
    </radialGradient>
    <linearGradient id="goldGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="40%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="capGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa" />
      <stop offset="50%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <filter id="badgeShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.75" />
    </filter>
  </defs>

  <!-- Circular Base Badge -->
  <circle cx="150" cy="150" r="140" fill="url(#badgeBg)" stroke="url(#goldGrad2)" stroke-width="6" filter="url(#badgeShadow)" />
  <circle cx="150" cy="150" r="130" fill="none" stroke="#38bdf8" stroke-width="2" stroke-opacity="0.7" />

  <!-- Center 'M' Emblem -->
  <g transform="translate(150, 142) scale(4.4) translate(-32, -29.5)">
    <path d="M 32 9 L 49 16.5 L 32 24 L 15 16.5 Z" fill="url(#capGrad2)" stroke="#93c5fd" stroke-width="0.8" />
    <path d="M 44 20 L 44 27.5 C 44 30.5 38 32.5 32 32.5 C 26 32.5 20 30.5 20 27.5 L 20 20" 
          fill="none" stroke="url(#capGrad2)" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 49 16.5 C 50 20 50.5 22 51 24.5" fill="none" stroke="url(#goldGrad2)" stroke-width="2.2" stroke-linecap="round" />
    <circle cx="51.2" cy="25.5" r="1.8" fill="url(#goldGrad2)" />
    <circle cx="32" cy="16.5" r="1.5" fill="url(#goldGrad2)" />
    <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff" />
  </g>

  <!-- Bottom Mini Text -->
  <text x="150" y="258" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="15" font-weight="900" letter-spacing="3" fill="#38bdf8">MFS</text>
</svg>'''
render(svg_opt2, "mfs_watermark_circle_badge")

# ------------------------------------------------------------------------------
# OPTION 3: HIGH-CONVERTING "SUBSCRIBE" WATERMARK BUTTON (TRANSPARENT BACKGROUND)
# Highly recommended by YouTube creators to drive direct 1-click video subscribes
# ------------------------------------------------------------------------------
svg_opt3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <defs>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff0000" />
      <stop offset="100%" stop-color="#b91c1c" />
    </linearGradient>
    <linearGradient id="goldTassel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="100%" stop-color="#f59e0b" />
    </linearGradient>
    <filter id="subBtnShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#000000" flood-opacity="0.75" />
    </filter>
  </defs>

  <!-- Button Card -->
  <rect x="15" y="15" width="270" height="270" rx="44" fill="#0f172a" stroke="#38bdf8" stroke-width="3" filter="url(#subBtnShadow)" />

  <!-- Mini 'M' Emblem at Top -->
  <g transform="translate(150, 95) scale(2.8) translate(-32, -29.5)">
    <path d="M 32 9 L 49 16.5 L 32 24 L 15 16.5 Z" fill="#38bdf8" stroke="#ffffff" stroke-width="0.8" />
    <path d="M 44 20 L 44 27.5 C 44 30.5 38 32.5 32 32.5 C 26 32.5 20 30.5 20 27.5 L 20 20" 
          fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 49 16.5 C 50 20 50.5 22 51 24.5" fill="none" stroke="url(#goldTassel)" stroke-width="2.2" stroke-linecap="round" />
    <circle cx="51.2" cy="25.5" r="1.8" fill="url(#goldTassel)" />
    <circle cx="32" cy="16.5" r="1.5" fill="url(#goldTassel)" />
    <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff" />
  </g>

  <!-- Channel Name -->
  <text x="150" y="180" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" letter-spacing="2" fill="#94a3b8">MASTER FUNCTIONAL SKILLS</text>

  <!-- Red YouTube Subscribe Pill Inside Card -->
  <g transform="translate(35, 198)">
    <rect x="0" y="0" width="230" height="60" rx="16" fill="url(#redGrad)" />
    <!-- YouTube Play Icon -->
    <rect x="22" y="14" width="40" height="30" rx="7" fill="#ffffff" />
    <polygon points="37,22 49,29 37,36" fill="#b91c1c" />
    <!-- Text -->
    <text x="76" y="38" font-family="'Montserrat', sans-serif" font-size="19" font-weight="900" letter-spacing="1.5" fill="#ffffff">SUBSCRIBE</text>
  </g>
</svg>'''
render(svg_opt3, "mfs_watermark_subscribe_button")

print("=== All Video Watermarks Ready ===")
