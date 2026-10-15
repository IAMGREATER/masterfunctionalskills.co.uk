#!/usr/bin/env python3
"""
propagate_canonical_navbar.py
Unifies the top navigation bar across all HTML pages on Master Functional Skills.
Features:
- Nested 'Revision Hub' mega dropdown (Maths, English, Digital Skills)
- Digital Skills key rules & practice page linked
- Tools dropdown without BKSB remediation tool
- Online Exam Simulator link pointing to format=online#mock-finder
- Tutor Hub, Past Papers, Revision Cards, Shop, Book Exam button
"""

import os
import glob
import re

CANONICAL_NAVBAR = """  <!-- MAIN NAVIGATION -->
  <header class="mfs-navbar">
    <div class="revision-page-wrapper mfs-navbar-inner">
      <a href="index.html" class="mfs-brand">
        <div class="mfs-brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="mfs-brand-text">
          <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
          <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
        </div>
      </a>

      <nav class="mfs-nav-wrapper">
        <ul class="mfs-nav-menu">
          <li class="mfs-nav-item">
            <a href="revise.html" class="mfs-nav-link"><i class="fa-solid fa-compass" style="color:#0284c7; margin-right:5px;"></i> Revision Hub <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-revision-hub">
              <div class="mfs-revision-grid">
                <!-- Maths Column -->
                <div class="mfs-revision-col mfs-revision-col-maths">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-calculator"></i> Maths Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
                    <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
                    <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
                    <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
                    <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.82rem; margin-right:4px;"></i> Pass Mark Calculator</a>
                    <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.82rem; margin-right:4px;"></i> 3D Net Folding Tool</a>
                  </div>
                </div>

                <!-- English Column -->
                <div class="mfs-revision-col mfs-revision-col-english">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-pen-nib"></i> English Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
                    <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
                    <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
                    <a href="pass-mark-calculator.html#english" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.82rem; margin-right:4px;"></i> English Boundaries</a>
                    <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.82rem; margin-right:4px;"></i> Diagnostic Test</a>
                  </div>
                </div>

                <!-- Digital Skills Column -->
                <div class="mfs-revision-col mfs-revision-col-digital">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-laptop-code"></i> Digital Skills</div>
                  <div class="mfs-revision-col-links">
                    <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
                    <a href="digital-functional-skills-revision.html" class="mfs-dropdown-item">DFS Key Rules &amp; Practice</a>
                    <a href="digital-functional-skills-level-1.html" class="mfs-dropdown-item">DFS Level 1 Course</a>
                    <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Data Files</a>
                    <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.82rem; margin-right:4px;"></i> Digital Skills Mock Simulator</a>
                  </div>
                </div>
              </div>

              <div class="mfs-revision-footer-bar">
                <a href="revision-cards.html" class="mfs-revision-footer-link" style="color:#d97706;"><i class="fa-solid fa-layer-group"></i> Revision Flashcards</a>
                <a href="revise.html" class="mfs-revision-footer-link"><i class="fa-solid fa-arrow-right"></i> All Revision Topics &rarr;</a>
              </div>
            </div>
          </li>

          <li class="mfs-nav-item">
            <a href="pass-mark-calculator.html" class="mfs-nav-link"><i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="functional-skills-past-papers.html?format=online#mock-finder" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Online Exam Simulator</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folding Tool</a>
            </div>
          </li>

          <li class="mfs-nav-item"><a href="tutors.html" class="mfs-nav-link"><i class="fa-solid fa-chalkboard-user" style="color:#0284c7; margin-right:5px;"></i> Tutor Hub</a></li>

          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link"><i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-past-papers.html" class="mfs-dropdown-item">All Past Papers Hub</a>
              <a href="edexcel-functional-skills-maths-level-2-past-papers.html" class="mfs-dropdown-item">Pearson Edexcel Papers</a>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Grade Boundaries Calculator</a>
            </div>
          </li>

          <li class="mfs-nav-item"><a href="revision-cards.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-layer-group" style="color:#f59e0b; margin-right:5px;"></i> Revision Cards</a></li>
          <li class="mfs-nav-item"><a href="shop.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-basket-shopping" style="color:#f59e0b; margin-right:5px;"></i> Shop</a></li>
        </ul>
      </nav>

      <div class="mfs-nav-actions">
        <a href="functional-skills-exam.html" class="btn-nav-exam"><i class="fa-solid fa-calendar-check"></i> Book Exam</a>
      </div>
    </div>
  </header>"""

SKIP_FILES = {
    "printable-all-cards.html",
    "printable-digital-skills.html",
    "printable-english-l1.html",
    "printable-english-l2.html",
    "printable-entry-level-3.html",
    "printable-maths-l1.html",
    "printable-maths-l2.html",
    "printable-a6-cards.html",
    "printable-overhauled-cards.html",
    "circles-worksheet.html",
    "volume-worksheet.html",
    "pfs_area.html",
    "scratch_runner.html",
    "scratch_nets_restored.html",
    "pass-functional-skills-reviews.html"
}

TARGET_DIRS = [
    "/home/subi/Projects/masterfunctionalskills.co.uk",
    "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
]

def update_navbars(target_dir):
    print(f"\n==========================================")
    print(f"Updating Navbars in: {target_dir}")
    print(f"==========================================")

    html_files = sorted(glob.glob(os.path.join(target_dir, "*.html")))
    updated = 0
    skipped = 0

    header_regex = re.compile(r'<header[\s>].*?</header>', re.DOTALL | re.IGNORECASE)

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname in SKIP_FILES:
            skipped += 1
            continue

        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        if header_regex.search(content):
            new_content = header_regex.sub(CANONICAL_NAVBAR.strip(), content, count=1)
            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                updated += 1
        else:
            print(f"  [NO HEADER] {fname}")

    print(f"Summary for {os.path.basename(target_dir)}: Updated {updated}, Skipped {skipped}, Total {len(html_files)}")

def main():
    for d in TARGET_DIRS:
        if os.path.exists(d):
            update_navbars(d)

if __name__ == "__main__":
    main()
