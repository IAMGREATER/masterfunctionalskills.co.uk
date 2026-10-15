#!/usr/bin/env python3
"""
MFS (Master Functional Skills) YouTube Assets Generator — Website 'M' Emblem Edition
Replaces MFS text with the iconic 'M' graduation cap emblem from masterfunctionalskills.co.uk.
Generates:
- mfs_logo_square.png & mfs_logo_square_icon.png (1024x1024 & 800x800 & Transparent)
- mfs_logo_circle.png & mfs_logo_circle_icon.png (1024x1024 & 800x800 & Transparent)
- mfs_logo_rectangular.png (1920x600 & 1200x375 & Transparent)
- mfs_video_watermark_150x150.png
- mfs_youtube_banner_cinematic.png (2560x1440, AI 3D cyber-mesh composite)
- mfs_youtube_banner_vector.png (2560x1440, Vector Studio)
- mfs_youtube_banner_with_guides.png (2560x1440, Safe-area guide overlay)
"""

import os
import shutil
import subprocess
from PIL import Image

OUT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/assets/youtube"
USER_PIC_DIR = "/home/subi/Pictures/MFS_YouTube_Branding"
AI_SOURCE_BG = "/home/subi/.gemini/antigravity-cli/brain/981b362a-0863-4ce2-820c-b45d1abbd595/mfs_ai_banner_art_1791924769541.jpg"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(USER_PIC_DIR, exist_ok=True)

def render_svg_to_png(svg_content, out_png_path, width, height):
    svg_path = out_png_path.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    cmd = ["rsvg-convert", "-w", str(width), "-h", str(height), svg_path, "-o", out_png_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {out_png_path}: {res.stderr}")
    else:
        print(f"Generated: {out_png_path} ({width}x{height})")
    # Also sync to Pictures directory
    user_png = os.path.join(USER_PIC_DIR, os.path.basename(out_png_path))
    user_svg = os.path.join(USER_PIC_DIR, os.path.basename(svg_path))
    shutil.copyfile(out_png_path, user_png)
    shutil.copyfile(svg_path, user_svg)
    return svg_path

# ==============================================================================
# CORE M EMBLEM DEFINITION (Derived directly from website logo.svg)
# ==============================================================================
def get_m_emblem_svg(scale=1.0, cx=0, cy=0):
    """
    Returns the SVG <g> group for the website's iconic 'M' with graduation cap.
    Original base is 64x64 centered at (32, 29.5).
    """
    return f'''
    <g transform="translate({cx}, {cy}) scale({scale}) translate(-32, -29.5)" filter="url(#mfsGlow)">
      <!-- Graduation Cap Diamond Top -->
      <path d="M 32 9 L 49 16.5 L 32 24 L 15 16.5 Z" fill="url(#capBlueGrad)" stroke="#93c5fd" stroke-width="0.8" />
      <path d="M 32 10.5 L 46.5 16.5 L 32 22.5 L 17.5 16.5 Z" fill="#1e3a8a" fill-opacity="0.5" />

      <!-- Cap Skullcap -->
      <path d="M 44 20 L 44 27.5 C 44 30.5 38 32.5 32 32.5 C 26 32.5 20 30.5 20 27.5 L 20 20" 
            fill="none" stroke="url(#capBlueGrad)" stroke-width="2.5" stroke-linecap="round" />

      <!-- Golden Tassel Cord & Bead -->
      <path d="M 49 16.5 C 50 20 50.5 22 51 24.5" fill="none" stroke="url(#goldGrad)" stroke-width="2.2" stroke-linecap="round" />
      <circle cx="51.2" cy="25.5" r="1.8" fill="url(#goldGrad)" />
      <!-- Cap Center Button -->
      <circle cx="32" cy="16.5" r="1.5" fill="url(#goldGrad)" />

      <!-- Bold White Letter 'M' -->
      <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" 
            fill="#ffffff" />
      
      <!-- Subtle 3D Bevel on 'M' -->
      <path d="M 17 29 L 24 29 L 32 41 L 24 37 L 24 50 L 17 50 Z" fill="#e2e8f0" fill-opacity="0.25" />
      <path d="M 30 46 L 34 46 L 40 37 L 40 29 L 32 41 Z" fill="#cbd5e1" fill-opacity="0.3" />
    </g>
    '''

SHARED_DEFS = '''
  <defs>
    <!-- Background Gradient (Deep Navy/Slate) -->
    <radialGradient id="navyRadBg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#172e54" />
      <stop offset="50%" stop-color="#0a192f" />
      <stop offset="100%" stop-color="#030712" />
    </radialGradient>

    <!-- Website Linear Gradient -->
    <linearGradient id="websiteGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a" />
      <stop offset="50%" stop-color="#1d4ed8" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>

    <!-- Cap Blue Gradient -->
    <linearGradient id="capBlueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa" />
      <stop offset="50%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>

    <!-- Metallic Gold Gradient -->
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="35%" stop-color="#f59e0b" />
      <stop offset="70%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>

    <!-- Electric Cyan Gradient -->
    <linearGradient id="cyanBlueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>

    <!-- Filters -->
    <filter id="mfsGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.45" />
    </filter>

    <filter id="heavyShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#000000" flood-opacity="0.65" />
    </filter>

    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#38bdf8" flood-opacity="0.4" />
    </filter>
  </defs>
'''

# ==============================================================================
# 1. PURE ICON SQUARE (Exactly like website logo, high-res 1024x1024)
# ==============================================================================
def generate_square_icon():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  {SHARED_DEFS}
  <!-- Rounded Square Frame (Identical aspect & curvature to website logo) -->
  <rect x="32" y="32" width="960" height="960" rx="224" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="24" filter="url(#heavyShadow)" />
  <rect x="56" y="56" width="912" height="912" rx="200" fill="none" stroke="#60a5fa" stroke-width="4" stroke-opacity="0.35" />

  <!-- Ambient Flare behind M -->
  <circle cx="512" cy="480" r="320" fill="#38bdf8" fill-opacity="0.12" />

  <!-- Website 'M' Emblem Scaled up (Scale ~18.5) -->
  {get_m_emblem_svg(scale=18.5, cx=512, cy=490)}
</svg>'''
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_square_icon.png"), 1024, 1024)
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_square_icon_800x800.png"), 800, 800)

    # Transparent icon
    svg_trans = svg.replace('<rect x="32" y="32" width="960" height="960" rx="224" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="24" filter="url(#heavyShadow)" />', '')
    svg_trans = svg_trans.replace('<rect x="56" y="56" width="912" height="912" rx="200" fill="none" stroke="#60a5fa" stroke-width="4" stroke-opacity="0.35" />', '')
    render_svg_to_png(svg_trans, os.path.join(OUT_DIR, "mfs_logo_square_icon_transparent.png"), 1024, 1024)

# ==============================================================================
# 2. SQUARE LOGO WITH BRAND TYPOGRAPHY (1024x1024)
# ==============================================================================
def generate_square_logo():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  {SHARED_DEFS}
  <!-- Dark Studio Base -->
  <rect width="1024" height="1024" rx="160" fill="url(#navyRadBg)" />
  <rect x="32" y="32" width="960" height="960" rx="140" fill="none" stroke="url(#cyanBlueGrad)" stroke-width="4" stroke-opacity="0.4" />
  <rect x="44" y="44" width="936" height="936" rx="130" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-opacity="0.3" stroke-dasharray="12,12" />

  <!-- Ambient Light -->
  <circle cx="512" cy="380" r="280" fill="#2563eb" fill-opacity="0.18" />
  <circle cx="512" cy="350" r="160" fill="#38bdf8" fill-opacity="0.12" />

  <!-- Inner Badge Frame for M -->
  <rect x="232" y="100" width="560" height="560" rx="130" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="14" filter="url(#heavyShadow)" />
  <rect x="246" y="114" width="532" height="532" rx="116" fill="none" stroke="#60a5fa" stroke-width="2.5" stroke-opacity="0.4" />

  <!-- Website 'M' Emblem inside Badge -->
  {get_m_emblem_svg(scale=11.0, cx=512, cy=380)}

  <!-- Accent Divider Bar -->
  <g transform="translate(180, 715)">
    <rect x="0" y="0" width="664" height="6" rx="3" fill="url(#cyanBlueGrad)" />
    <rect x="220" y="-1" width="224" height="8" rx="4" fill="url(#goldGrad)" filter="url(#subtleGlow)" />
  </g>

  <!-- Title: MASTER FUNCTIONAL SKILLS -->
  <text x="512" y="785" 
        text-anchor="middle" 
        font-family="'Montserrat', 'Poppins', sans-serif" 
        font-size="46" 
        font-weight="900" 
        letter-spacing="4" 
        fill="#ffffff">MASTER <tspan fill="#38bdf8">FUNCTIONAL</tspan> SKILLS</text>

  <!-- Slogan -->
  <text x="512" y="845" 
        text-anchor="middle" 
        font-family="'Montserrat', sans-serif" 
        font-size="22" 
        font-weight="700" 
        letter-spacing="5" 
        fill="#f59e0b">DELIVERING SKILLS • ACHIEVING GOALS</text>

  <!-- Subject Badges -->
  <g transform="translate(232, 885)">
    <rect x="0" y="0" width="160" height="42" rx="21" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8" />
    <text x="80" y="27" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="16" font-weight="800" fill="#38bdf8" letter-spacing="1">MATHS</text>

    <rect x="195" y="0" width="170" height="42" rx="21" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8" />
    <text x="280" y="27" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="16" font-weight="800" fill="#f59e0b" letter-spacing="1">ENGLISH</text>

    <rect x="400" y="0" width="160" height="42" rx="21" fill="#1e293b" stroke="#10b981" stroke-width="1.8" />
    <text x="480" y="27" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="16" font-weight="800" fill="#10b981" letter-spacing="1">DIGITAL FS</text>
  </g>
</svg>'''
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_square.png"), 1024, 1024)
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_square_800x800.png"), 800, 800)

    svg_trans = svg.replace('<rect width="1024" height="1024" rx="160" fill="url(#navyRadBg)" />', '')
    render_svg_to_png(svg_trans, os.path.join(OUT_DIR, "mfs_logo_square_transparent.png"), 1024, 1024)

# ==============================================================================
# 3. CIRCULAR / ROUND LOGO (YouTube Profile Avatar Safe)
# ==============================================================================
def generate_circle_logo():
    # Variant A: Pure 'M' Emblem Circular Avatar (High impact for YouTube app icon)
    svg_icon = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  {SHARED_DEFS}
  <!-- Base Circle Fill -->
  <circle cx="512" cy="512" r="500" fill="url(#navyRadBg)" />

  <!-- Outer Double Rings -->
  <circle cx="512" cy="512" r="490" fill="none" stroke="url(#goldGrad)" stroke-width="14" />
  <circle cx="512" cy="512" r="466" fill="none" stroke="url(#cyanBlueGrad)" stroke-width="5" stroke-opacity="0.8" />
  <circle cx="512" cy="512" r="444" fill="none" stroke="#38bdf8" stroke-width="2" stroke-opacity="0.3" stroke-dasharray="8,8" />

  <!-- Inner Website Grad Disc -->
  <circle cx="512" cy="512" r="420" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="8" filter="url(#heavyShadow)" />

  <!-- Ambient Light -->
  <circle cx="512" cy="480" r="260" fill="#38bdf8" fill-opacity="0.18" />

  <!-- Website 'M' Emblem Scaled up (Scale ~15.5) -->
  {get_m_emblem_svg(scale=15.5, cx=512, cy=500)}

  <!-- Subtle Bottom Arch Text -->
  <text x="512" y="855" 
        text-anchor="middle" 
        font-family="'Montserrat', sans-serif" 
        font-size="28" 
        font-weight="900" 
        letter-spacing="6" 
        fill="#ffffff">MASTER <tspan fill="#f59e0b">FUNCTIONAL</tspan> SKILLS</text>
  
  <text x="512" y="890" 
        text-anchor="middle" 
        font-family="'Montserrat', sans-serif" 
        font-size="16" 
        font-weight="700" 
        letter-spacing="4" 
        fill="#94a3b8">DELIVERING SKILLS • ACHIEVING GOALS</text>
</svg>'''
    render_svg_to_png(svg_icon, os.path.join(OUT_DIR, "mfs_logo_circle.png"), 1024, 1024)
    render_svg_to_png(svg_icon, os.path.join(OUT_DIR, "mfs_logo_circle_800x800.png"), 800, 800)

    # Transparent circle version
    svg_trans = svg_icon.replace('<circle cx="512" cy="512" r="500" fill="url(#navyRadBg)" />', '')
    render_svg_to_png(svg_trans, os.path.join(OUT_DIR, "mfs_logo_circle_transparent.png"), 1024, 1024)

    # YouTube Video Watermark (150x150)
    render_svg_to_png(svg_trans, os.path.join(OUT_DIR, "mfs_video_watermark_150x150.png"), 150, 150)

# ==============================================================================
# 4. RECTANGULAR LOGO (1920 x 600) — Horizontal Lockup with 'M' Emblem
# ==============================================================================
def generate_rectangular_logo():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 600" width="1920" height="600">
  {SHARED_DEFS}
  <!-- Dark Studio Base -->
  <rect width="1920" height="600" rx="40" fill="url(#navyRadBg)" />
  <rect x="20" y="20" width="1880" height="560" rx="30" fill="none" stroke="url(#cyanBlueGrad)" stroke-width="2.5" stroke-opacity="0.3" />

  <!-- Ambient Flare behind Emblem -->
  <circle cx="280" cy="300" r="220" fill="#2563eb" fill-opacity="0.22" />
  <circle cx="280" cy="270" r="100" fill="#38bdf8" fill-opacity="0.15" />

  <!-- LEFT EMBLEM BADGE (Rounded Square matching website logo) -->
  <rect x="90" y="110" width="380" height="380" rx="88" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="10" filter="url(#heavyShadow)" />
  <rect x="104" y="124" width="352" height="352" rx="76" fill="none" stroke="#60a5fa" stroke-width="2" stroke-opacity="0.4" />

  <!-- Website 'M' Emblem inside Left Badge -->
  {get_m_emblem_svg(scale=7.5, cx=280, cy=300)}

  <!-- RIGHT TYPOGRAPHY LOCKUP -->
  <g transform="translate(540, 140)">
    <!-- Sub-heading Tagline -->
    <g transform="translate(0, 30)">
      <rect x="0" y="0" width="220" height="34" rx="17" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8" />
      <circle cx="18" cy="17" r="6" fill="#10b981" />
      <text x="120" y="23" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#ffffff" letter-spacing="2">UK OFFICIAL REVISION</text>
    </g>

    <!-- Main Title -->
    <text x="0" y="130" 
          font-family="'Montserrat', 'Poppins', sans-serif" 
          font-size="76" 
          font-weight="900" 
          letter-spacing="2" 
          fill="#ffffff">MASTER <tspan fill="#38bdf8">FUNCTIONAL</tspan> SKILLS</text>

    <!-- Slogan / Tagline -->
    <text x="2" y="195" 
          font-family="'Montserrat', sans-serif" 
          font-size="30" 
          font-weight="700" 
          letter-spacing="6" 
          fill="url(#goldGrad)">DELIVERING SKILLS • ACHIEVING GOALS</text>

    <!-- Divider Bar -->
    <g transform="translate(0, 225)">
      <rect x="0" y="0" width="1280" height="4" rx="2" fill="url(#cyanBlueGrad)" opacity="0.6" />
      <rect x="0" y="-1" width="380" height="6" rx="3" fill="url(#goldGrad)" />
    </g>

    <!-- Subject Badges & Offerings -->
    <g transform="translate(0, 260)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="210" height="48" rx="24" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
        <circle cx="28" cy="24" r="8" fill="#38bdf8" />
        <text x="120" y="31" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="18" font-weight="800" fill="#ffffff" letter-spacing="1.5">MATHS L1 &amp; L2</text>
      </g>

      <g transform="translate(230, 0)">
        <rect x="0" y="0" width="225" height="48" rx="24" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
        <circle cx="28" cy="24" r="8" fill="#f59e0b" />
        <text x="130" y="31" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="18" font-weight="800" fill="#ffffff" letter-spacing="1.5">ENGLISH L1 &amp; L2</text>
      </g>

      <g transform="translate(475, 0)">
        <rect x="0" y="0" width="235" height="48" rx="24" fill="#0f172a" stroke="#10b981" stroke-width="2" />
        <circle cx="28" cy="24" r="8" fill="#10b981" />
        <text x="134" y="31" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="18" font-weight="800" fill="#ffffff" letter-spacing="1.5">DIGITAL SKILLS</text>
      </g>

      <g transform="translate(740, 12)">
        <text x="0" y="20" font-family="'Montserrat', sans-serif" font-size="16" font-weight="600" fill="#94a3b8" letter-spacing="1">Edexcel • City &amp; Guilds • NCFE • AQA • Open Awards • TQUK</text>
      </g>
    </g>
  </g>
</svg>'''
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_rectangular.png"), 1920, 600)
    render_svg_to_png(svg, os.path.join(OUT_DIR, "mfs_logo_rectangular_1200x400.png"), 1200, 375)

    svg_trans = svg.replace('<rect width="1920" height="600" rx="40" fill="url(#navyRadBg)" />', '')
    render_svg_to_png(svg_trans, os.path.join(OUT_DIR, "mfs_logo_rectangular_transparent.png"), 1920, 600)

# ==============================================================================
# 5. YOUTUBE CHANNEL BANNER (2560 x 1440) — With Website 'M' Emblem
# ==============================================================================
def get_banner_svg(with_guides=False, transparent_backdrop=False):
    guide_svg = ""
    if with_guides:
        guide_svg = '''
    <!-- YOUTUBE GUIDELINE OVERLAYS -->
    <rect x="507" y="508" width="1546" height="423" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="16,8" opacity="0.85" />
    <text x="525" y="538" font-family="'Montserrat', sans-serif" font-size="18" font-weight="800" fill="#ef4444">MOBILE &amp; DESKTOP SAFE AREA (1546 x 423)</text>
    <rect x="0" y="508" width="2560" height="423" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="10,10" opacity="0.6" />
    <text x="30" y="538" font-family="'Montserrat', sans-serif" font-size="18" font-weight="700" fill="#3b82f6">DESKTOP FULL WIDTH (2560 x 423)</text>
    <text x="30" y="70" font-family="'Montserrat', sans-serif" font-size="22" font-weight="800" fill="#94a3b8">TV DISPLAY CANVAS (2560 x 1440)</text>
        '''

    bg_rect = '<rect width="2560" height="1440" fill="url(#navyRadBg)" />' if not transparent_backdrop else ''
    safe_bg = '<rect x="0" y="508" width="2560" height="423" fill="url(#safeAreaBg)" />' if not transparent_backdrop else '<rect x="0" y="508" width="2560" height="423" fill="#071326" fill-opacity="0.82" />'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2560 1440" width="2560" height="1440">
  {SHARED_DEFS}
  <defs>
    <linearGradient id="safeAreaBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#071326" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0c1e3d" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#071326" stop-opacity="0.95" />
    </linearGradient>

    <linearGradient id="ytRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff0000" />
      <stop offset="100%" stop-color="#cc0000" />
    </linearGradient>

    <filter id="bannerGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="25" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- 1. FULL CANVAS BACKGROUND -->
  {bg_rect}

  <!-- Abstract Grid & Ambient Lights (TV Canvas) -->
  <g stroke="#38bdf8" stroke-opacity="0.04" stroke-width="1.5">
    <line x1="320" y1="0" x2="320" y2="1440" />
    <line x1="640" y1="0" x2="640" y2="1440" />
    <line x1="960" y1="0" x2="960" y2="1440" />
    <line x1="1280" y1="0" x2="1280" y2="1440" />
    <line x1="1600" y1="0" x2="1600" y2="1440" />
    <line x1="1920" y1="0" x2="1920" y2="1440" />
    <line x1="2240" y1="0" x2="2240" y2="1440" />
    <line x1="0" y1="240" x2="2560" y2="240" />
    <line x1="0" y1="480" x2="2560" y2="480" />
    <line x1="0" y1="720" x2="2560" y2="720" />
    <line x1="0" y1="960" x2="2560" y2="960" />
    <line x1="0" y1="1200" x2="2560" y2="1200" />
  </g>

  <circle cx="600" cy="300" r="380" fill="#1d4ed8" fill-opacity="0.12" filter="url(#bannerGlow)" />
  <circle cx="1960" cy="350" r="420" fill="#0284c7" fill-opacity="0.10" filter="url(#bannerGlow)" />
  <circle cx="1280" cy="720" r="450" fill="#2563eb" fill-opacity="0.18" filter="url(#bannerGlow)" />
  <circle cx="800" cy="1150" r="350" fill="#1e3a8a" fill-opacity="0.15" filter="url(#bannerGlow)" />
  <circle cx="1800" cy="1150" r="350" fill="#f59e0b" fill-opacity="0.08" filter="url(#bannerGlow)" />

  <g opacity="0.15" stroke="#38bdf8" fill="none" stroke-width="2">
    <circle cx="260" cy="720" r="180" stroke-dasharray="12,12" />
    <circle cx="260" cy="720" r="260" />
    <circle cx="2300" cy="720" r="180" stroke-dasharray="12,12" stroke="#f59e0b" />
    <circle cx="2300" cy="720" r="260" stroke="#f59e0b" />
  </g>

  <!-- 2. CENTRAL SAFE ZONE STRIP (Height 423, Y: 508 to 931) -->
  {safe_bg}
  <line x1="0" y1="508" x2="2560" y2="508" stroke="url(#cyanBlueGrad)" stroke-width="3" stroke-opacity="0.7" />
  <line x1="507" y1="508" x2="2053" y2="508" stroke="url(#goldGrad)" stroke-width="4" />
  
  <line x1="0" y1="931" x2="2560" y2="931" stroke="url(#cyanBlueGrad)" stroke-width="3" stroke-opacity="0.7" />
  <line x1="507" y1="931" x2="2053" y2="931" stroke="url(#goldGrad)" stroke-width="4" />

  <!-- ======================================================== -->
  <!-- PERFECT SAFE CONTENT (X: 520 to 2040, Y: 518 to 920) -->
  <!-- ======================================================== -->

  <!-- LEFT: ICON EMBLEM (Website 'M' Badge, Center X: 690, Y: 720) -->
  <g transform="translate(535, 545)" filter="url(#heavyShadow)">
    <circle cx="165" cy="165" r="155" fill="#0a192f" stroke="url(#goldGrad)" stroke-width="5" />
    <circle cx="165" cy="165" r="143" fill="none" stroke="url(#cyanBlueGrad)" stroke-width="3" stroke-opacity="0.7" />
    <circle cx="165" cy="165" r="132" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8,6" stroke-opacity="0.4" />

    <!-- Inner Rounded Square / Disc matching website -->
    <rect x="50" y="50" width="230" height="230" rx="55" fill="url(#websiteGrad)" stroke="#3b82f6" stroke-width="6" />

    <!-- Website 'M' Emblem inside Circular Crest -->
    {get_m_emblem_svg(scale=4.6, cx=165, cy=165)}

    <text x="165" y="296" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="900" letter-spacing="2.5" fill="#38bdf8">MASTER FUNCTIONAL SKILLS</text>
  </g>

  <!-- CENTER: BRANDING & HEADLINE (X: 885 to 1680) -->
  <g transform="translate(885, 542)">
    <!-- Pill: UK OFFICIAL REVISION -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="280" height="28" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.6" />
      <circle cx="16" cy="14" r="4.5" fill="#10b981" />
      <text x="148" y="19" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="#ffffff" letter-spacing="1.8">UK FUNCTIONAL SKILLS REVISION</text>
    </g>

    <!-- Channel Name -->
    <text x="0" y="72" 
          font-family="'Montserrat', 'Poppins', sans-serif" 
          font-size="43" 
          font-weight="900" 
          letter-spacing="1" 
          fill="#ffffff">MASTER <tspan fill="#38bdf8">FUNCTIONAL</tspan> SKILLS</text>

    <!-- Channel Slogan -->
    <text x="2" y="114" 
          font-family="'Montserrat', sans-serif" 
          font-size="20" 
          font-weight="700" 
          letter-spacing="4" 
          fill="url(#goldGrad)">DELIVERING SKILLS • ACHIEVING GOALS</text>

    <!-- Divider Bar -->
    <g transform="translate(0, 134)">
      <rect x="0" y="0" width="760" height="3" rx="1.5" fill="url(#cyanBlueGrad)" opacity="0.6" />
      <rect x="0" y="-1" width="280" height="5" rx="2.5" fill="url(#goldGrad)" />
    </g>

    <!-- Subject Badges -->
    <g transform="translate(0, 158)">
      <rect x="0" y="0" width="140" height="34" rx="17" fill="#0f172a" stroke="#ffffff" stroke-width="1.4" stroke-opacity="0.8" />
      <text x="70" y="22" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#ffffff" letter-spacing="1">LEVEL 1 &amp; L2</text>

      <rect x="155" y="0" width="120" height="34" rx="17" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" />
      <text x="215" y="22" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#38bdf8" letter-spacing="1">MATHS</text>

      <rect x="290" y="0" width="125" height="34" rx="17" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8" />
      <text x="352" y="22" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#f59e0b" letter-spacing="1">ENGLISH</text>

      <rect x="430" y="0" width="155" height="34" rx="17" fill="#0f172a" stroke="#10b981" stroke-width="1.8" />
      <text x="507" y="22" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#10b981" letter-spacing="1">DIGITAL SKILLS</text>
    </g>

    <!-- Channel Features List -->
    <g transform="translate(2, 226)">
      <text x="0" y="0" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="600" fill="#cbd5e1" letter-spacing="0.5">
        ✓ Full Past Paper Walkthroughs   •   ✓ Step-by-Step Model Solutions   •   ✓ Topic Masterclasses
      </text>
      <!-- Exam Boards Footprint -->
      <text x="0" y="26" font-family="'Montserrat', sans-serif" font-size="12" font-weight="600" fill="#94a3b8" letter-spacing="0.8">
        Exam Boards: Pearson Edexcel • City &amp; Guilds • NCFE • AQA • Open Awards • TQUK
      </text>
    </g>
  </g>

  <!-- RIGHT: CALL TO ACTION & SUBSCRIBE (X: 1700 to 2040) -->
  <g transform="translate(1705, 545)">
    <!-- Schedule Card -->
    <rect x="0" y="0" width="330" height="125" rx="18" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" stroke-opacity="0.6" filter="url(#heavyShadow)" />
    
    <circle cx="28" cy="30" r="12" fill="#1d4ed8" />
    <polygon points="25,24 35,30 25,36" fill="#ffffff" />
    
    <text x="50" y="28" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#38bdf8" letter-spacing="1.5">NEW VIDEOS WEEKLY</text>
    <text x="50" y="45" font-family="'Montserrat', sans-serif" font-size="11" font-weight="500" fill="#94a3b8">Past Papers &amp; Model Solutions</text>

    <line x1="16" y1="62" x2="314" y2="62" stroke="#334155" stroke-width="1.2" />

    <text x="18" y="84" font-family="'Montserrat', sans-serif" font-size="11" font-weight="700" fill="#94a3b8">Free Practice &amp; Revision Hub:</text>
    <text x="18" y="106" font-family="'Montserrat', sans-serif" font-size="14.5" font-weight="800" fill="url(#goldGrad)" letter-spacing="0.8">masterfunctionalskills.co.uk</text>

    <!-- YouTube SUBSCRIBE Button -->
    <g transform="translate(0, 142)" filter="url(#heavyShadow)">
      <rect x="0" y="0" width="330" height="66" rx="16" fill="url(#ytRed)" />
      <path d="M 0 16 C 0 7 7 0 16 0 L 314 0 C 323 0 330 7 330 16 L 330 30 L 0 30 Z" fill="#ffffff" opacity="0.15" />
      
      <rect x="38" y="15" width="48" height="34" rx="8" fill="#ffffff" />
      <polygon points="57,24 70,32 57,40" fill="#cc0000" />

      <text x="110" y="42" font-family="'Montserrat', sans-serif" font-size="22" font-weight="900" fill="#ffffff" letter-spacing="3">SUBSCRIBE</text>
    </g>

    <!-- Bell Reminder -->
    <g transform="translate(25, 230)">
      <circle cx="10" cy="10" r="9" fill="#f59e0b" opacity="0.2" />
      <text x="26" y="14" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="700" fill="#f59e0b">Turn on 🔔 Notifications for Walkthroughs</text>
    </g>
  </g>

  <!-- GUIDES (IF ENABLED) -->
  {guide_svg}
</svg>'''

def generate_youtube_banners():
    # 1. Clean Vector Studio Banner
    svg_clean = get_banner_svg(with_guides=False, transparent_backdrop=False)
    render_svg_to_png(svg_clean, os.path.join(OUT_DIR, "mfs_youtube_banner_2560x1440.png"), 2560, 1440)
    shutil.copyfile(os.path.join(OUT_DIR, "mfs_youtube_banner_2560x1440.png"), os.path.join(OUT_DIR, "mfs_youtube_banner_vector.png"))
    shutil.copyfile(os.path.join(OUT_DIR, "mfs_youtube_banner_2560x1440.png"), os.path.join(USER_PIC_DIR, "mfs_youtube_banner_vector.png"))

    # 2. Guide Verification Banner
    svg_guides = get_banner_svg(with_guides=True, transparent_backdrop=False)
    render_svg_to_png(svg_guides, os.path.join(OUT_DIR, "mfs_youtube_banner_with_guides.png"), 2560, 1440)

    # 3. 3D Cinematic Cyber-Glow Banner (Compositing the AI 3D Backdrop)
    if os.path.exists(AI_SOURCE_BG):
        print("Compositing 3D Cinematic YouTube Banner...")
        svg_overlay = get_banner_svg(with_guides=False, transparent_backdrop=True)
        overlay_png = os.path.join(OUT_DIR, "banner_fg_overlay.png")
        render_svg_to_png(svg_overlay, overlay_png, 2560, 1440)

        bg_img = Image.open(AI_SOURCE_BG).convert("RGBA")
        bg_resized = bg_img.resize((2560, 1440), Image.Resampling.LANCZOS)

        fg_img = Image.open(overlay_png).convert("RGBA")
        final_banner = Image.alpha_composite(bg_resized, fg_img)

        cinematic_path = os.path.join(OUT_DIR, "mfs_youtube_banner_cinematic.png")
        final_banner.save(cinematic_path, "PNG", optimize=True)
        shutil.copyfile(cinematic_path, os.path.join(USER_PIC_DIR, "mfs_youtube_banner_cinematic.png"))
        print(f"Generated: {cinematic_path} (2560x1440)")

        if os.path.exists(overlay_png):
            os.remove(overlay_png)

if __name__ == "__main__":
    print("=== Generating 'M' Emblem Edition YouTube Brand Package ===")
    generate_square_icon()
    generate_square_logo()
    generate_circle_logo()
    generate_rectangular_logo()
    generate_youtube_banners()
    print("=== All Assets Finished ===")
