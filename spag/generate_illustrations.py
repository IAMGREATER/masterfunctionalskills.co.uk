# generate_illustrations.py
# Bespoke SVG illustrations for the 11 Functional Skills English Writing Formats

def get_illustration_svg(fmt_num, level=1, size=56):
    """
    Returns an SVG illustration string tailored for each format.
    fmt_num: 1 to 11
    level: 1 (Teal theme) or 2 (Blue theme)
    size: width and height in px
    """
    if level == 1:
        p_main = "#0f766e"      # primary teal
        p_sec = "#0d9488"       # teal 600
        p_bg = "#ccfbf1"        # teal light bg
        p_border = "#99f6e4"    # teal border
        p_dark = "#134e4a"      # teal dark
        p_acc = "#f59e0b"       # amber accent
        p_soft = "#e6fffa"
    else:
        p_main = "#1e3a8a"      # primary deep blue
        p_sec = "#2563eb"       # royal blue
        p_bg = "#dbeafe"        # blue light bg
        p_border = "#bfdbfe"    # blue border
        p_dark = "#172554"      # navy dark
        p_acc = "#f59e0b"       # amber accent
        p_soft = "#eff6ff"

    # Common viewBox: 0 0 56 56
    s = str(size)

    if fmt_num == 1:
        # Format 1: ARTICLE — Newspaper & Journalism Pen
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <rect x="10" y="9" width="36" height="38" rx="4" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Newspaper Header / Masthead -->
  <rect x="14" y="13" width="28" height="5" rx="1.5" fill="{p_main}"/>
  <!-- Sub-headline line -->
  <line x1="14" y1="21" x2="32" y2="21" stroke="{p_sec}" stroke-width="1.8" stroke-linecap="round"/>
  <!-- Photo / Image Thumbnail box -->
  <rect x="14" y="25" width="13" height="12" rx="2" fill="{p_soft}" stroke="{p_sec}" stroke-width="1.2"/>
  <circle cx="18" cy="28.5" r="1.5" fill="{p_acc}"/>
  <path d="M14 34L19 30L27 36H14V34Z" fill="{p_main}" opacity="0.7"/>
  <!-- 2-column article text lines -->
  <line x1="30" y1="26" x2="42" y2="26" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="30" y1="30" x2="41" y2="30" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="30" y1="34" x2="42" y2="34" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="14" y1="41" x2="42" y2="41" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Fountain Pen / Stylus -->
  <g transform="translate(33, 23) rotate(35)">
    <rect x="0" y="0" width="4.5" height="16" rx="1" fill="{p_acc}" stroke="{p_dark}" stroke-width="0.8"/>
    <path d="M0 16L2.25 21L4.5 16H0Z" fill="{p_dark}"/>
    <circle cx="2.25" cy="18" r="0.6" fill="#ffffff"/>
  </g>
</svg>'''

    elif fmt_num == 2:
        # Format 2: EMAIL — Digital Envelope & Sent Paper Aeroplane
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Modern Envelope Body -->
  <rect x="8" y="16" width="40" height="26" rx="3" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Envelope Flap / Fold lines -->
  <path d="M8 17L28 31L48 17" stroke="{p_main}" stroke-width="2" stroke-linejoin="round"/>
  <path d="M8 41L21 28" stroke="{p_sec}" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M48 41L35 28" stroke="{p_sec}" stroke-width="1.5" stroke-linecap="round"/>
  <!-- @ symbol badge -->
  <circle cx="28" cy="24" r="5" fill="{p_bg}" stroke="{p_sec}" stroke-width="1.2"/>
  <text x="28" y="27" font-family="'Open Sans', sans-serif" font-size="7" font-weight="bold" fill="{p_main}" text-anchor="middle">@</text>
  <!-- Flying Paper Plane / Send indicator at top right -->
  <g transform="translate(34, 6)">
    <path d="M0 8L16 0L9 16L7 10L0 8Z" fill="{p_acc}" stroke="{p_dark}" stroke-width="1" stroke-linejoin="round"/>
    <path d="M7 10L16 0" stroke="{p_dark}" stroke-width="1"/>
  </g>
</svg>'''

    elif fmt_num == 3:
        # Format 3: FORMAL LETTER — Royal Letterhead, Wax Seal & Pen
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Classic Formal Letter Paper -->
  <rect x="11" y="7" width="34" height="42" rx="2.5" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Header Crest / Double Rule -->
  <line x1="15" y1="12" x2="41" y2="12" stroke="{p_main}" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="15" y1="14" x2="41" y2="14" stroke="{p_sec}" stroke-width="0.8"/>
  <!-- Sender address lines (right) -->
  <line x1="28" y1="18" x2="40" y2="18" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="30" y1="21" x2="40" y2="21" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Recipient lines (left) -->
  <line x1="15" y1="25" x2="27" y2="25" stroke="{p_main}" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="15" y1="28" x2="25" y2="28" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Formal Body Paragraph lines -->
  <line x1="15" y1="33" x2="41" y2="33" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="15" y1="36" x2="41" y2="36" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="15" y1="39" x2="35" y2="39" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Red / Wax Seal Stamp (bottom right) -->
  <circle cx="37" cy="42" r="5" fill="#dc2626" stroke="#991b1b" stroke-width="1"/>
  <circle cx="37" cy="42" r="3.2" fill="#ef4444"/>
  <path d="M35.5 42H38.5M37 40.5V43.5" stroke="#ffffff" stroke-width="0.9" stroke-linecap="round"/>
</svg>'''

    elif fmt_num == 4:
        # Format 4: REPORT — Clipboard with Bar Chart & Trend
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Clipboard Backing -->
  <rect x="9" y="10" width="38" height="40" rx="4" fill="{p_dark}"/>
  <!-- Clip at Top -->
  <rect x="21" y="7" width="14" height="6" rx="2" fill="{p_acc}" stroke="{p_dark}" stroke-width="1.2"/>
  <circle cx="28" cy="10" r="1.5" fill="#ffffff"/>
  <!-- Paper Sheet -->
  <rect x="12" y="13" width="32" height="34" rx="2" fill="#ffffff"/>
  <!-- Report Title Line -->
  <rect x="16" y="17" width="18" height="3" rx="1" fill="{p_main}"/>
  <!-- Bar Chart Columns -->
  <rect x="17" y="34" width="4" height="8" rx="1" fill="{p_border}" stroke="{p_sec}" stroke-width="0.8"/>
  <rect x="23" y="28" width="4" height="14" rx="1" fill="{p_sec}"/>
  <rect x="29" y="24" width="4" height="18" rx="1" fill="{p_main}"/>
  <rect x="35" y="20" width="4" height="22" rx="1" fill="{p_acc}"/>
  <!-- Upward Trend Line -->
  <path d="M16 33L24 27L30 23L38 18" stroke="#ef4444" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="38" cy="18" r="1.6" fill="#ef4444"/>
</svg>'''

    elif fmt_num == 5:
        # Format 5: INCIDENT REPORT — Health & Safety Shield & Hazard Alert
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Report Sheet Base -->
  <rect x="10" y="8" width="36" height="40" rx="3" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Safety Stripes Top Banner -->
  <rect x="10" y="8" width="36" height="6" rx="2" fill="{p_main}"/>
  <line x1="14" y1="11" x2="42" y2="11" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="3 2"/>
  <!-- Central HSE Shield -->
  <path d="M28 17L39 21V28C39 35 28 41 28 41C28 41 17 35 17 28V21L28 17Z" fill="{p_soft}" stroke="{p_sec}" stroke-width="1.8"/>
  <!-- Safety Cross / Exclamation within shield -->
  <rect x="25.5" y="23" width="5" height="12" rx="1" fill="#ef4444"/>
  <rect x="22" y="26.5" width="12" height="5" rx="1" fill="#ef4444"/>
  <!-- Hazard Cone / Warning Badge bottom-right -->
  <g transform="translate(34, 34)">
    <path d="M8 14L4 4L0 14H8Z" fill="{p_acc}" stroke="{p_dark}" stroke-width="1" stroke-linejoin="round"/>
    <line x1="2" y1="9" x2="6" y2="9" stroke="#ffffff" stroke-width="1.2"/>
    <rect x="-1" y="14" width="10" height="2" rx="1" fill="{p_dark}"/>
  </g>
</svg>'''

    elif fmt_num == 6:
        # Format 6: ADVICE LEAFLET — Tri-Fold Brochure & Idea Lightbulb
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- 3D Tri-Fold Leaflet Panels -->
  <!-- Left panel (angled) -->
  <path d="M9 13L19 10V42L9 45V13Z" fill="{p_soft}" stroke="{p_sec}" stroke-width="1.5"/>
  <!-- Center panel -->
  <rect x="19" y="10" width="18" height="32" fill="#ffffff" stroke="{p_main}" stroke-width="1.8"/>
  <!-- Right panel (angled) -->
  <path d="M37 10L47 13V45L37 42V10Z" fill="{p_soft}" stroke="{p_sec}" stroke-width="1.5"/>
  <!-- Center Leaflet Content -->
  <rect x="22" y="13" width="12" height="4" rx="1" fill="{p_main}"/>
  <line x1="22" y1="20" x2="34" y2="20" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="22" y1="23" x2="32" y2="23" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="22" y1="26" x2="34" y2="26" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Lightbulb / Advice Icon in center bottom -->
  <circle cx="28" cy="33" r="4.5" fill="{p_acc}" stroke="{p_dark}" stroke-width="1"/>
  <path d="M26 37.5H30" stroke="{p_dark}" stroke-width="1.2" stroke-linecap="round"/>
  <!-- Checkmarks on left panel -->
  <path d="M12 20L14 22L17 19" stroke="{p_sec}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M12 27L14 29L17 26" stroke="{p_sec}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

    elif fmt_num == 7:
        # Format 7: REVIEW — 5 Golden Stars & Feedback Speech Bubble
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Review Speech Bubble -->
  <path d="M10 13C10 10.79 11.79 9 14 9H42C44.21 9 46 10.79 46 13V33C46 35.21 44.21 37 42 37H24L15 44V37H14C11.79 37 10 35.21 10 33V13Z" fill="#ffffff" stroke="{p_main}" stroke-width="2" stroke-linejoin="round"/>
  <!-- 5 Gold Stars Row -->
  <g fill="{p_acc}" stroke="{p_dark}" stroke-width="0.5">
    <!-- Star 1 -->
    <path d="M16 16L17.2 19.5H20.8L17.9 21.6L19 25L16 22.8L13 25L14.1 21.6L11.2 19.5H14.8L16 16Z"/>
    <!-- Star 2 -->
    <path d="M22 16L23.2 19.5H26.8L23.9 21.6L25 25L22 22.8L19 25L20.1 21.6L17.2 19.5H20.8L22 16Z"/>
    <!-- Star 3 -->
    <path d="M28 16L29.2 19.5H32.8L29.9 21.6L31 25L28 22.8L25 25L26.1 21.6L23.2 19.5H26.8L28 16Z"/>
    <!-- Star 4 -->
    <path d="M34 16L35.2 19.5H38.8L35.9 21.6L37 25L34 22.8L31 25L32.1 21.6L29.2 19.5H32.8L34 16Z"/>
    <!-- Star 5 -->
    <path d="M40 16L41.2 19.5H44.8L41.9 21.6L43 25L40 22.8L37 25L38.1 21.6L35.2 19.5H38.8L40 16Z"/>
  </g>
  <!-- Review comment quote lines -->
  <line x1="16" y1="28" x2="40" y2="28" stroke="#475569" stroke-width="1.6" stroke-linecap="round"/>
  <line x1="16" y1="32" x2="34" y2="32" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Thumbs Up Badge -->
  <circle cx="43" cy="38" r="5" fill="{p_sec}" stroke="#ffffff" stroke-width="1.2"/>
  <path d="M41 38.5V36.5C41 35.8 42 35 42.5 35C43 35 43 36 43 36.5L44.5 36.5C45 36.5 45.5 37 45.5 37.5L44.8 40.5C44.7 40.8 44.4 41 44 41H42C41.4 41 41 40.6 41 40V38.5Z" fill="#ffffff"/>
</svg>'''

    elif fmt_num == 8:
        # Format 8: ONLINE FEEDBACK FORM — Interactive Web Form & Rating
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Web Browser Window -->
  <rect x="8" y="9" width="40" height="38" rx="3.5" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Browser top tab bar -->
  <rect x="8" y="9" width="40" height="7" rx="2" fill="{p_main}"/>
  <circle cx="12" cy="12.5" r="1.2" fill="#ef4444"/>
  <circle cx="16" cy="12.5" r="1.2" fill="{p_acc}"/>
  <circle cx="20" cy="12.5" r="1.2" fill="#22c55e"/>
  <!-- Form input field 1 with checkbox -->
  <rect x="13" y="19" width="7" height="7" rx="1.5" fill="{p_bg}" stroke="{p_sec}" stroke-width="1.2"/>
  <path d="M14.5 22.5L16.5 24.5L19 20.5" stroke="{p_main}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="23" y1="22.5" x2="42" y2="22.5" stroke="#475569" stroke-width="1.6" stroke-linecap="round"/>
  <!-- Form input field 2 (radio) -->
  <circle cx="16.5" cy="29.5" r="3.5" fill="{p_bg}" stroke="{p_sec}" stroke-width="1.2"/>
  <circle cx="16.5" cy="29.5" r="1.8" fill="{p_main}"/>
  <line x1="23" y1="29.5" x2="38" y2="29.5" stroke="#64748b" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Comment box area -->
  <rect x="13" y="34" width="30" height="7" rx="1.5" fill="{p_soft}" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="16" y1="37.5" x2="35" y2="37.5" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/>
  <!-- Green Submit Button -->
  <rect x="29" y="42" width="16" height="5" rx="1.5" fill="#22c55e"/>
  <text x="37" y="45.8" font-family="'Open Sans', sans-serif" font-size="3.5" font-weight="bold" fill="#ffffff" text-anchor="middle">SUBMIT</text>
</svg>'''

    elif fmt_num == 9:
        # Format 9: ONLINE FORUM / BLOG — Community Speech Threads & Upvote
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Primary Forum Discussion Bubble (Back) -->
  <path d="M14 12C14 9.79 15.79 8 18 8H42C44.21 8 46 9.79 46 12V28C46 30.21 44.21 32 42 32H36L30 37V32H18C15.79 32 14 30.21 14 28V12Z" fill="{p_soft}" stroke="{p_sec}" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="20" y1="14" x2="40" y2="14" stroke="{p_main}" stroke-width="1.6" stroke-linecap="round"/>
  <line x1="20" y1="18" x2="36" y2="18" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="20" y1="22" x2="38" y2="22" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Overlapping Reply Bubble (Front) -->
  <path d="M8 24C8 21.79 9.79 20 12 20H34C36.21 20 38 21.79 38 24V38C38 40.21 36.21 42 34 42H24L16 47V42H12C9.79 42 8 40.21 8 38V24Z" fill="#ffffff" stroke="{p_main}" stroke-width="2" stroke-linejoin="round"/>
  <!-- User Avatar inside reply -->
  <circle cx="15" cy="27" r="3" fill="{p_bg}" stroke="{p_sec}" stroke-width="1"/>
  <circle cx="15" cy="26" r="1.2" fill="{p_main}"/>
  <line x1="21" y1="26" x2="33" y2="26" stroke="{p_main}" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="14" y1="33" x2="33" y2="33" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="14" y1="37" x2="28" y2="37" stroke="#64748b" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Orange Reddit-style Upvote Arrow on right -->
  <g transform="translate(38, 30)">
    <path d="M5 0L10 6H7V12H3V6H0L5 0Z" fill="#f97316"/>
  </g>
</svg>'''

    elif fmt_num == 10:
        # Format 10: NEWSLETTER — Community Gazette & Megaphone
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Folded Newsletter Sheet -->
  <rect x="9" y="8" width="38" height="40" rx="3" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Newsletter Header Banner -->
  <rect x="9" y="8" width="38" height="8" rx="2" fill="{p_main}"/>
  <text x="28" y="14" font-family="'Montserrat', sans-serif" font-size="4.5" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">NEWSLETTER</text>
  <!-- Main Story Headline -->
  <rect x="13" y="19" width="20" height="3" rx="0.8" fill="{p_sec}"/>
  <line x1="13" y1="25" x2="31" y2="25" stroke="#64748b" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="13" y1="28" x2="31" y2="28" stroke="#64748b" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="13" y1="31" x2="27" y2="31" stroke="#64748b" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Sidebar 'What is on' Box -->
  <rect x="33" y="19" width="10" height="15" rx="1.5" fill="{p_soft}" stroke="{p_border}" stroke-width="1"/>
  <line x1="35" y1="22" x2="41" y2="22" stroke="{p_main}" stroke-width="1.2"/>
  <line x1="35" y1="25" x2="40" y2="25" stroke="#94a3b8" stroke-width="1"/>
  <line x1="35" y1="28" x2="41" y2="28" stroke="#94a3b8" stroke-width="1"/>
  <!-- Megaphone in foreground at bottom -->
  <g transform="translate(18, 33)">
    <path d="M4 7L14 3V13L4 9H0V7H4Z" fill="{p_acc}" stroke="{p_dark}" stroke-width="1.1" stroke-linejoin="round"/>
    <path d="M14 3C15.5 5 15.5 11 14 13" stroke="{p_dark}" stroke-width="1.2"/>
    <path d="M4 9L6 14H3L2 9" fill="{p_dark}"/>
    <!-- Broadcast sound waves -->
    <path d="M17 5C18.5 6.5 18.5 9.5 17 11" stroke="{p_main}" stroke-width="1.2" stroke-linecap="round"/>
  </g>
</svg>'''

    elif fmt_num == 11:
        # Format 11: DIARY / LEARNING LOG — Bound Journal & Ribbon Bookmark
        return f'''<svg width="{s}" height="{s}" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="56" height="56" rx="10" fill="{p_bg}"/>
  <!-- Hardcover Book / Journal Body -->
  <rect x="11" y="8" width="34" height="40" rx="3.5" fill="#ffffff" stroke="{p_main}" stroke-width="2"/>
  <!-- Journal Spine (Left) -->
  <rect x="11" y="8" width="6" height="40" rx="2" fill="{p_main}"/>
  <!-- Spine Stitching marks -->
  <line x1="14" y1="14" x2="14" y2="17" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="14" y1="22" x2="14" y2="25" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="14" y1="30" x2="14" y2="33" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="14" y1="38" x2="14" y2="41" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round"/>
  <!-- Red Bookmark Ribbon hanging from top -->
  <path d="M22 8V25L25 22L28 25V8H22Z" fill="#ef4444"/>
  <!-- Journal Ruled Page Lines -->
  <line x1="20" y1="16" x2="41" y2="16" stroke="{p_sec}" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="29" y1="20" x2="41" y2="20" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="20" y1="28" x2="41" y2="28" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="20" y1="32" x2="41" y2="32" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="20" y1="36" x2="35" y2="36" stroke="#94a3b8" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Diagonal Pencil resting at bottom-right -->
  <g transform="translate(35, 34) rotate(40)">
    <rect x="0" y="0" width="3.5" height="14" rx="0.8" fill="{p_acc}" stroke="{p_dark}" stroke-width="0.8"/>
    <path d="M0 14L1.75 18L3.5 14H0Z" fill="{p_dark}"/>
    <circle cx="1.75" cy="15.5" r="0.5" fill="#ffffff"/>
  </g>
</svg>'''

    return ""
