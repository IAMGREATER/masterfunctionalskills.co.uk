#!/usr/bin/env python3
import os
import glob
import re

BASE_DIR = '/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk'
WORKSHEETS_DIR = os.path.join(BASE_DIR, 'worksheets')

PILL_CSS_TEMPLATE = '''    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 0;
      width: 115px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: none;
      background: transparent;
      box-sizing: border-box;
    }}
    .nav-pill-btn:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      text-decoration: none;
    }}
    .nav-pill-btn.active {{
      background: {active_color};
      color: #ffffff;
      cursor: default;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    }}
    .btn-action-mode,
    .btn-action-practice,
    .btn-action-answers,
    .btn-action-sheet {{
      color: #ffffff !important;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none !important;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 12px;
      transition: background 0.2s;
    }}
    .btn-action-practice {{
      background: #7c3aed;
    }}
    .btn-action-practice:hover {{
      background: #6d28d9;
      color: #ffffff !important;
      text-decoration: none !important;
    }}
    .btn-action-mode:hover,
    .btn-action-answers:hover,
    .btn-action-sheet:hover {{
      color: #ffffff !important;
      text-decoration: none !important;
      filter: brightness(0.9);
    }}

    @media (max-width: 900px) {{
      .print-bar {{
        padding: 10px 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .print-bar > div:first-child {{
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .print-bar > div:first-child a {{
        font-size: 0.85rem;
        display: inline-flex;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }}
      .print-bar > div:last-child {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
      }}
      .print-bar > div:last-child > * {{
        margin-right: 0 !important;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        padding: 6px 12px;
        font-size: 0.85rem;
      }}
      .nav-pill-group {{
        margin-right: 0;
      }}
      .nav-pill-btn {{
        width: 100px;
        font-size: 0.82rem;
        padding: 5px 0;
      }}
    }}
    @media (max-width: 480px) {{
      .print-bar > div:last-child {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }}
      .nav-pill-group {{
        grid-column: span 2;
        width: 100%;
      }}
      .nav-pill-btn {{
        flex: 1;
        width: auto;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        justify-content: center;
        width: 100%;
      }}
    }}
'''

def main():
    parent_files = set(os.listdir(BASE_DIR))
    all_files = glob.glob(os.path.join(WORKSHEETS_DIR, '*.html'))
    target_files = [f for f in all_files if os.path.basename(f) != 'printable-cube-nets.html']

    print(f"Total worksheet files to process: {len(target_files)}")

    # Step 1: Collect revision guide info from question sheets
    rev_guides = {}
    for f in target_files:
        name = os.path.basename(f)
        slug = None
        for ext in ['-workout.html', '-worksheet.html']:
            if name.endswith(ext):
                slug = name[:-len(ext)]
                break
        if slug:
            with open(f, 'r', encoding='utf-8') as fp:
                c = fp.read()
            m = re.search(r'<div class="print-bar">[\s\S]*?<a href="([^"]+)"><i class="fa-solid fa-arrow-left"></i>([^<]+)</a>', c)
            if m:
                href = m.group(1).strip()
                title_text = m.group(2).strip()
                # Resolve parent file if possible
                if href.startswith('../'):
                    target_name = href[3:]
                    if target_name not in parent_files:
                        if f"{slug}.html" in parent_files:
                            href = f"../{slug}.html"
                        elif f"functional-skills-{slug}.html" in parent_files:
                            href = f"../functional-skills-{slug}.html"
                rev_guides[slug] = (href, title_text)

    # Step 2: Process each file
    updated_count = 0
    for f in target_files:
        name = os.path.basename(f)
        category = None
        slug = None
        if name.endswith('-workout-answers.html'):
            category = 'workout-answers'
            slug = name[:-len('-workout-answers.html')]
        elif name.endswith('-workout.html'):
            category = 'workout'
            slug = name[:-len('-workout.html')]
        elif name.endswith('-answers.html'):
            category = 'worksheet-answers'
            slug = name[:-len('-answers.html')]
        elif name.endswith('-worksheet.html'):
            category = 'worksheet'
            slug = name[:-len('-worksheet.html')]

        if not category:
            continue

        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()

        rev_url, rev_text = rev_guides.get(slug, (f"../functional-skills-{slug}.html", f"Back to Revision Guide"))

        active_color = "#059669" if ("answers" in category) else "#2563eb"
        pill_css = PILL_CSS_TEMPLATE.format(active_color=active_color)

        # 1. Update CSS: remove previous injected .nav-pill-group and related classes
        content = re.sub(r'\s*\.nav-pill-group\s*\{[\s\S]*?@media print \{', '\n@media print {', content)
        # Inject right before @media print
        content = content.replace('@media print {', pill_css + '    @media print {')

        # 2. Build new .print-bar HTML
        if category == 'workout':
            new_print_bar = f'''  <!-- Top Action Navigation Bar -->
  <div class="print-bar">
    <div>
      <a href="{rev_url}"><i class="fa-solid fa-arrow-left"></i> {rev_text}</a>
    </div>
    <div>
      <a href="{slug}-worksheet.html" class="btn-action-practice"><i class="fa-solid fa-file-pen"></i> Switch to Exam Practice</a>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-file-lines"></i> Questions</span>
        <a href="{slug}-workout-answers.html" class="nav-pill-btn"><i class="fa-solid fa-check-double"></i> Answers</a>
      </div>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save as PDF</button>
    </div>
  </div>'''
        elif category == 'workout-answers':
            new_print_bar = f'''  <!-- Top Action Navigation Bar -->
  <div class="print-bar">
    <div>
      <a href="{rev_url}"><i class="fa-solid fa-arrow-left"></i> {rev_text}</a>
    </div>
    <div>
      <a href="{slug}-answers.html" class="btn-action-practice"><i class="fa-solid fa-file-shield"></i> Exam Mark Scheme</a>
      <div class="nav-pill-group">
        <a href="{slug}-workout.html" class="nav-pill-btn"><i class="fa-solid fa-file-lines"></i> Questions</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-check-double"></i> Answers</span>
      </div>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save as PDF</button>
    </div>
  </div>'''
        elif category == 'worksheet':
            new_print_bar = f'''  <div class="print-bar">
    <div>
      <a href="{rev_url}"><i class="fa-solid fa-arrow-left"></i> {rev_text}</a>
    </div>
    <div>
      <a href="{slug}-workout.html" class="btn-action-answers" style="background:#2563eb; margin-right:12px;"><i class="fa-solid fa-repeat"></i> Switch to Skill Workout</a>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-file-lines"></i> Questions</span>
        <a href="{slug}-answers.html" class="nav-pill-btn"><i class="fa-solid fa-check-double"></i> Answers</a>
      </div>
      <button type="button" class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save to PDF</button>
    </div>
  </div>'''
        elif category == 'worksheet-answers':
            new_print_bar = f'''  <div class="print-bar">
    <div>
      <a href="{rev_url}"><i class="fa-solid fa-arrow-left"></i> {rev_text}</a>
    </div>
    <div>
      <a href="{slug}-workout-answers.html" class="btn-action-answers" style="background:#2563eb; margin-right:12px;"><i class="fa-solid fa-repeat"></i> Workout Answers</a>
      <div class="nav-pill-group">
        <a href="{slug}-worksheet.html" class="nav-pill-btn"><i class="fa-solid fa-file-lines"></i> Questions</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-check-double"></i> Answers</span>
      </div>
      <button type="button" class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save to PDF</button>
    </div>
  </div>'''

        # Replace print-bar block in content
        content = re.sub(
            r'(?:<!--\s*Top Action Navigation Bar\s*-->\s*)?<div class="print-bar">[\s\S]*?</div>\s*</div>',
            new_print_bar,
            content,
            count=1
        )

        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)

        updated_count += 1

    print(f"Successfully updated {updated_count} worksheet HTML files with responsive pill navigation!")

if __name__ == '__main__':
    main()
