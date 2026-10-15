#!/usr/bin/env python3
"""
Unify Navigation Header across all Master Functional Skills pages.
Ensures every page has:
1. Subjects mega-menu
2. Past Papers
2b. Worksheets (Corbett style dual engine)
3. Free Tools (compact dropdown)
4. Revision Cards
5. Shop
6. Book Exam action button
"""

import os
import glob
import re

CANONICAL_HEADER = """  <header class="mfs-navbar">
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
          <!-- 1. SUBJECTS (VISUAL MEGA-MENU) -->
          <li class="mfs-nav-item">
            <a href="courses.html" class="mfs-nav-link">
              <i class="fa-solid fa-book-open-reader" style="color:#0284c7; margin-right:5px;"></i> Subjects <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i>
            </a>
            <div class="mfs-dropdown-menu mfs-dropdown-revision-hub">
              <div class="mfs-revision-grid">
                <!-- Maths Column -->
                <div class="mfs-revision-col mfs-revision-col-maths">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-calculator"></i> Maths Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
                    <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
                    <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
                  </div>
                </div>
                <!-- English Column -->
                <div class="mfs-revision-col mfs-revision-col-english">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-pen-nib"></i> English Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
                    <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
                  </div>
                </div>
                <!-- Digital Skills Column -->
                <div class="mfs-revision-col mfs-revision-col-digital">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-laptop-code"></i> Digital Skills</div>
                  <div class="mfs-revision-col-links">
                    <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
                    <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item">Pearson Mock Exam</a>
                    <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Files</a>
                  </div>
                </div>
              </div>
            </div>
          </li>

          <!-- 2. PAST PAPERS (DIRECT ACCESS) -->
          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link">
              <i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers
            </a>
          </li>

          <!-- 2b. WORKSHEETS DIRECTORY (CORBETT STYLE DUAL ENGINE) -->
          <li class="mfs-nav-item">
            <a href="worksheets.html" class="mfs-nav-link">
              <i class="fa-solid fa-layer-group" style="color:#0284c7; margin-right:5px;"></i> Worksheets
            </a>
          </li>

          <!-- 3. FREE TOOLS (COMPACT DROPDOWN) -->
          <li class="mfs-nav-item">
            <a href="tools.html" class="mfs-nav-link">
              <i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Free Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i>
            </a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="tools.html" class="mfs-dropdown-item" style="font-weight:700; color:var(--accent);"><i class="fa-solid fa-layer-group" style="font-size:0.85rem; margin-right:6px;"></i> All Free Tools &amp; Simulators &rarr;</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folding Tool</a>
            </div>
          </li>

          <!-- 4. REVISION CARDS -->
          <li class="mfs-nav-item">
            <a href="revision-cards.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#d97706; font-weight:700;">
              <i class="fa-solid fa-layer-group" style="color:#d97706; margin-right:5px;"></i> Revision Cards
            </a>
          </li>

          <!-- 5. SHOP -->
          <li class="mfs-nav-item">
            <a href="shop.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#d97706; font-weight:700;">
              <i class="fa-solid fa-basket-shopping" style="color:#d97706; margin-right:5px;"></i> Shop
            </a>
          </li>
        </ul>
      </nav>

      <!-- 6. BOOK EXAM ACTION BUTTON -->
      <div class="mfs-nav-actions">
        <a href="exams.html" class="btn-nav-exam">
          <i class="fa-solid fa-calendar-check"></i> Book Exam
        </a>
      </div>
    </div>
  </header>"""

DIRS = [
    "/home/subi/Projects/masterfunctionalskills.co.uk",
    "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
]

EXCLUDE_FILES = {
    "books_image_audit_catalog.html",
    "books_image_audit_suggestions.html",
    "image_audit_catalog.html",
    "pearson_dfs_dom.html",
    "circles-worksheet.html",
    "volume-worksheet.html",
    "pfs_area.html",
    "pass-functional-skills-reviews.html",
    "maths-level-2.html",
    "functional-skills-entry-level-3.html",
    "book-functional-skills-exam.html",
    "functional-skills-exam.html",
    "grade-boundaries.html",
    "functional-skills-courses.html",
    "printable-a6-cards.html",
    "printable-all-cards.html",
    "printable-digital-skills.html",
    "printable-english-l1.html",
    "printable-english-l2.html",
    "printable-entry-level-3.html",
    "printable-maths-l1.html",
    "printable-maths-l2.html",
    "printable-overhauled-cards.html",
    "scratch_runner.html",
    "test_card41_fixed.html",
    "test_card41_isolated.html",
    "netfold.html",
    "netfolding.html",
    "worksheets.html"  # Retains its dedicated active nav styling
}

def main():
    header_pattern = re.compile(r'^[ \t]*<header class=["\']mfs-navbar["\']>.*?</header>', re.MULTILINE | re.DOTALL)

    for d in DIRS:
        if not os.path.exists(d):
            continue
        files = sorted(glob.glob(os.path.join(d, "*.html")))
        updated_count = 0
        skipped_count = 0
        no_header_count = 0

        for fpath in files:
            fname = os.path.basename(fpath)
            if fname in EXCLUDE_FILES:
                skipped_count += 1
                continue

            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            if header_pattern.search(content):
                new_content = header_pattern.sub(CANONICAL_HEADER, content, count=1)
                if new_content != content:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    updated_count += 1
            else:
                no_header_count += 1
                print(f"[{d}] No <header class='mfs-navbar'> found in: {fname}")

        print(f"Directory {d}: Updated {updated_count} files, Skipped {skipped_count}, No header {no_header_count}")

    print("Done unifying all navbars across the entire website!")

if __name__ == "__main__":
    main()
