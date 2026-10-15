#!/usr/bin/env python3
"""
unify_all_footers.py
Replaces the footer across all website pages with the clean, accurate canonical Master Functional Skills footer.
Removes:
- Fake telephone placeholders ('020 XXXX XXXX')
- PFS corporate institutional boilerplate ('Colleges & Universities', 'NHS & Employer Services', 'Nursing & Police Pathways')
- Dead '#' privacy/terms links
- Old inline navy-dark footers

Applies clean 4-column structure:
1. Brand & Contact (clickable WhatsApp +44 (0)7564 525425, Contact Tutor Team)
2. Maths Revision (Maths L2, Maths L1, Entry Level 3, Pass Mark Calculator, Free Past Papers, Book L2 Maths Exam)
3. English & Digital (English L2, English L1, Digital Skills Hub, DFS Past Papers, Online Exam Simulator, Book L2 English Exam)
4. Student Support & Tools (Revision Cards & Flashcards, Study Packs, Diagnostic Skill Checker, 3D Net Folder, 1-to-1 Tuition, Book Official Online Exam)
Footer Bottom: Home, Past Papers, Revision Cards, Study Shop, Tutors, Contact Us.
"""

import os
import glob
import re

CANONICAL_FOOTER = """  <!-- FOOTER -->
  <footer class="mfs-footer" id="site-footer">
    <div class="mfs-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="mfs-brand" style="margin-bottom:16px;">
            <div class="mfs-brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="mfs-brand-text">
              <div class="mfs-brand-title" style="color:#ffffff;">MASTER<span>FUNCTIONALSKILLS</span></div>
              <div class="mfs-brand-subtitle" style="color:#94a3b8;">Delivering Skills • Achieving Goals</div>
            </div>
          </div>
          <p style="font-size:0.88rem; line-height:1.6; margin-bottom:16px;">
            The UK's dedicated Functional Skills revision specialist. Providing realistic mock exams, step-by-step revision flashcards, diagnostic assessments, and 1-to-1 specialist tuition for Pearson Edexcel, City &amp; Guilds, and all major exam boards.
          </p>
          <div style="font-size:0.85rem; color:#cbd5e1;">
            <p><a href="https://wa.me/447564525425" target="_blank" rel="noopener" style="color:#cbd5e1; text-decoration:none;"><i class="fa-brands fa-whatsapp" style="color:var(--accent); margin-right:8px;"></i> WhatsApp: +44 (0)7564 525425</a></p>
            <p style="margin-top:6px;"><a href="contact-us.html" style="color:#cbd5e1; text-decoration:none;"><i class="fa-solid fa-envelope" style="color:var(--accent); margin-right:8px;"></i> Contact Tutor Team</a></p>
          </div>
        </div>

        <div class="footer-col">
          <h4>Maths Revision</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-maths-level-2.html">Maths Level 2 Revision</a></li>
            <li><a href="functional-skills-maths-level-1.html">Maths Level 1 Revision</a></li>
            <li><a href="entry-level-3-maths.html">Entry Level 3 Maths</a></li>
            <li><a href="pass-mark-calculator.html">Pass Mark Calculator</a></li>
            <li><a href="functional-skills-past-papers.html">Free Maths Past Papers</a></li>
            <li><a href="exam-maths-l2.html">Book Level 2 Maths Exam</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>English &amp; Digital</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-english-level-2.html">English Level 2 Revision</a></li>
            <li><a href="functional-skills-english-level-1.html">English Level 1 Revision</a></li>
            <li><a href="digital-functional-skills.html">Digital Skills Hub (L1 &amp; E3)</a></li>
            <li><a href="digital-functional-skills-past-papers.html">DFS Past Papers &amp; Data Files</a></li>
            <li><a href="functional-skills-past-papers.html?format=online#mock-finder">Online Exam Simulator</a></li>
            <li><a href="exam-english-l2.html">Book Level 2 English Exam</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Student Support &amp; Tools</h4>
          <ul class="footer-links">
            <li><a href="tools.html" style="color:var(--accent); font-weight:700;"><i class="fa-solid fa-screwdriver-wrench" style="margin-right:6px;"></i>All Interactive Tools Hub</a></li>
            <li><a href="pass-mark-calculator.html">Pass Mark Calculator</a></li>
            <li><a href="diagnostic-test.html">Diagnostic Skill Checker</a></li>
            <li><a href="functional-skills-nets.html">3D Net Folding Tool</a></li>
            <li><a href="digital-functional-skills-mock-exam.html">Pearson DFS Simulator</a></li>
            <li><a href="revision-cards.html">Revision Cards &amp; Flashcards</a></li>
            <li><a href="shop.html">Revision Books &amp; Study Packs</a></li>
            <li><a href="tutors.html">1-to-1 Specialist Tuition</a></li>
            <li><a href="exams.html">Book Official Online Exam</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Master Functional Skills. All rights reserved. Registered in England &amp; Wales. Ofqual Regulated Qualification Standards.</div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="index.html">Home</a>
          <a href="tools.html" style="color:var(--accent); font-weight:700;">Tools</a>
          <a href="functional-skills-past-papers.html">Past Papers</a>
          <a href="revision-cards.html">Revision Cards</a>
          <a href="shop.html">Study Shop</a>
          <a href="tutors.html">Tutors</a>
          <a href="contact-us.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>"""

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
    "image_audit_catalog.html",
    "books_image_audit_catalog.html",
    "books_image_audit_suggestions.html",
    "pass-functional-skills-reviews.html",
    "maths-level-2.html",
    "functional-skills-entry-level-3.html",
    "book-functional-skills-exam.html",
    "functional-skills-exam.html",
    "grade-boundaries.html",
    "past-papers.html",
    "netfold.html",
    "netfolding.html",
    "functional-skills-courses.html"
}

TARGET_DIRS = [
    "/home/subi/Projects/masterfunctionalskills.co.uk",
    "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
]

def update_directory(target_dir):
    print(f"\n==========================================")
    print(f"Processing Directory: {target_dir}")
    print(f"==========================================")
    
    html_files = sorted(glob.glob(os.path.join(target_dir, "*.html")))
    updated_count = 0
    skipped_count = 0
    inserted_count = 0

    footer_regex = re.compile(r'(?:\s*<!--\s*FOOTER\s*-->)*\s*<footer[\s>].*?</footer>', re.DOTALL | re.IGNORECASE)

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname in SKIP_FILES:
            skipped_count += 1
            continue

        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        if fname == "revision-cards.html":
            # revision-cards.html has no footer by default, insert before data/logic engines
            if footer_regex.search(content):
                new_content = footer_regex.sub(CANONICAL_FOOTER, content, count=1)
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                updated_count += 1
            else:
                marker = "  <!-- DATA & LOGIC ENGINES -->"
                if marker in content:
                    new_content = content.replace(marker, f"{CANONICAL_FOOTER}\n\n{marker}")
                    with open(fpath, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    inserted_count += 1
                    print(f"  [INSERTED] Added canonical footer to {fname}")
                elif "</main>" in content:
                    new_content = content.replace("</main>", f"</main>\n\n{CANONICAL_FOOTER}")
                    with open(fpath, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    inserted_count += 1
                    print(f"  [INSERTED] Added canonical footer to {fname}")
            continue

        if footer_regex.search(content):
            new_content = footer_regex.sub(CANONICAL_FOOTER, content, count=1)
            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                updated_count += 1
        else:
            print(f"  [WARNING] No footer found in {fname}")

    print(f"Directory summary for {os.path.basename(target_dir)}:")
    print(f"  Total HTML files : {len(html_files)}")
    print(f"  Footers Updated  : {updated_count}")
    print(f"  Footers Inserted : {inserted_count}")
    print(f"  Skipped Files    : {skipped_count}")

def main():
    for d in TARGET_DIRS:
        if os.path.exists(d):
            update_directory(d)
        else:
            print(f"Directory not found: {d}")

if __name__ == "__main__":
    main()
