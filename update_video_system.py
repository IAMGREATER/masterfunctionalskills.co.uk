#!/usr/bin/env python3
"""
Master Functional Skills - Video Link Remediation Script
Replaces dead and competitor YouTube links across curriculum hub and past paper files
with the Master Functional Skills Video Solution modal and player suite.
"""

import os
import re
import glob

REPO_DIR = '/home/subi/Projects/masterfunctionalskills.co.uk'

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

# -------------------------------------------------------------
# 1. UPDATE 6 CURRICULUM HUB PAGES
# -------------------------------------------------------------
hub_files = [
    'functional-skills-maths-level-2.html',
    'maths-level-2.html',
    'functional-skills-maths-level-1.html',
    'entry-level-3-maths.html',
    'functional-skills-english-level-2.html',
    'functional-skills-english-level-1.html'
]

print("=== UPDATING CURRICULUM HUB FILES ===")

for fn in hub_files:
    file_path = os.path.join(REPO_DIR, fn)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure CSS is linked in head
    if 'mfs-video-modal.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="assets/css/mfs-theme.css">',
            '<link rel="stylesheet" href="assets/css/mfs-theme.css">\n  <link rel="stylesheet" href="assets/css/mfs-video-modal.css">'
        )

    # Ensure JS is linked before </body>
    if 'mfs-video-modal.js' not in content:
        content = content.replace(
            '</body>',
            '  <script src="assets/js/mfs-video-modal.js"></script>\n</body>'
        )

    # Replace video buttons inside topic rows
    def replace_topic_row(match):
        pre_content = match.group(1)
        topic_title = match.group(2).strip()
        revise_url = match.group(3).strip()
        sheet_url = match.group(4).strip()
        answers_url = match.group(5).strip()
        
        slug = slugify(topic_title)
        
        if slug == 'numbers-and-place-value':
            new_btn = (
                f'<a href="video-solution.html?topic={slug}" class="btn-mfs-video" '
                f'data-topic="{topic_title}" '
                f'data-sheet="{sheet_url}" '
                f'data-answers="{answers_url}" '
                f'data-video="videos/Numbers_and_Place_Value_Video_Solution.mp4" '
                f'data-poster="videos/thumbnail_numbers_and_place_value.png">'
                f'<i class="fa-solid fa-circle-play" style="color:#2563eb;"></i> Video Solution</a>'
            )
        else:
            new_btn = (
                f'<a href="video-solution.html?topic={slug}" class="btn-mfs-video" '
                f'data-topic="{topic_title}" '
                f'data-sheet="{sheet_url}" '
                f'data-answers="{answers_url}">'
                f'<i class="fa-solid fa-circle-play" style="color:#ef4444;"></i> Video Solution</a>'
            )
            
        return pre_content + new_btn

    row_pattern = re.compile(
        r'(<div class=\"topic-row\".*?'
        r'<div class=\"topic-title\">([^<]+)</div>.*?'
        r'<a href=\"([^\"]+)\"[^>]*class=\"btn-mfs-revise\".*?'
        r'<a href=\"([^\"]+)\"[^>]*class=\"btn-mfs-sheet\"[^>]*>.*?</a>.*?'
        r'<a href=\"([^\"]+)\"[^>]*class=\"btn-mfs-sheet\"[^>]*>.*?</a>.*?)'
        r'(<a\s+href=\"[^\"]*\"\s+target=\"_blank\"\s+rel=\"noopener\"\s+class=\"btn-mfs-video\"><i class=\"fa-brands fa-youtube\"></i> Video Solution</a>)',
        re.DOTALL
    )

    new_content, count = row_pattern.subn(replace_topic_row, content)
    print(f"  {fn}: updated {count} video buttons")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

# -------------------------------------------------------------
# 2. UPDATE PAST PAPER FILES
# -------------------------------------------------------------
print("\n=== UPDATING PAST PAPER FILES ===")
past_paper_files = glob.glob(os.path.join(REPO_DIR, '*past-papers*.html'))

for file_path in past_paper_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Ensure CSS is linked in head
    if 'mfs-video-modal.css' not in content and '<head>' in content:
        if '<link rel="stylesheet" href="assets/css/mfs-theme.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="assets/css/mfs-theme.css">',
                '<link rel="stylesheet" href="assets/css/mfs-theme.css">\n  <link rel="stylesheet" href="assets/css/mfs-video-modal.css">'
            )
            changed = True
        elif '</head>' in content:
            content = content.replace(
                '</head>',
                '  <link rel="stylesheet" href="assets/css/mfs-video-modal.css">\n</head>'
            )
            changed = True

    # Ensure JS is linked before </body>
    if 'mfs-video-modal.js' not in content and '</body>' in content:
        content = content.replace(
            '</body>',
            '  <script src="assets/js/mfs-video-modal.js"></script>\n</body>'
        )
        changed = True

    # Replace youtube video buttons in past paper rows
    # <a href="https://youtu.be/..." target="_blank" rel="noopener" class="btn-paper btn-paper-video"><i class="fa-brands fa-youtube"></i> Video Walkthrough</a>
    pp_video_pattern = re.compile(
        r'<a\s+href=\"https://youtu\.be/[^\"]*\"\s+target=\"_blank\"\s+rel=\"noopener\"\s+class=\"btn-paper btn-paper-video\"><i class=\"fa-brands fa-youtube\"></i> Video Walkthrough</a>'
    )

    matches = pp_video_pattern.findall(content)
    if matches:
        new_btn = '<a href="video-solution.html" class="btn-paper btn-paper-video"><i class="fa-solid fa-circle-play" style="color:#ef4444;"></i> Video Walkthrough</a>'
        content = pp_video_pattern.sub(new_btn, content)
        changed = True
        print(f"  {os.path.basename(file_path)}: replaced {len(matches)} video walkthrough links")

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("\n=== COMPLETED VIDEO REMEDIATION ===")
