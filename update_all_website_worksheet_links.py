#!/usr/bin/env python3
"""
Updates all worksheet question and answer links across the entire website.
Ensures every topic page has live, direct links to:
- worksheets/<slug>-worksheet.html
- worksheets/<slug>-answers.html
"""

import os, sys, glob, re

BASE_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
WORKSHEETS_DIR = os.path.join(BASE_DIR, "worksheets")

all_html = sorted(glob.glob(os.path.join(BASE_DIR, "*.html")))
exclude_files = {
    'index.html', 'revise.html', 'shop.html', 'reviews.html', 'contact.html',
    'about.html', 'training-providers-and-employers.html',
    'courses.html', 'exam.html', 'maths-and-english.html', 'maths-level-1.html',
    'maths-level-2.html', 'english-level-1.html', 'english-level-2.html', 'entry-level-3.html',
    'functional-skills-courses.html', 'functional-skills-exam.html',
    'functional-skills-maths-and-english.html',
    'functional-skills-maths-level-1.html', 'functional-skills-maths-level-2.html',
    'functional-skills-english-level-1.html', 'functional-skills-english-level-2.html',
    'functional-skills-entry-level-3.html', 'entry-level-3-maths.html',
    'pass-mark-calculator.html', 'diagnostic-test.html', 'bksb-remediation.html',
    'partnerships.html', 'colleges.html', 'tutors.html', 'contact-us.html',
    'grade-boundaries.html', 'exams.html', 'career-functional-skills.html',
    'pass-functional-skills-reviews.html', 'revision-cards.html', 'video-solution.html'
}

updated_files = []

for fpath in all_html:
    bn = os.path.basename(fpath)
    if bn in exclude_files or 'past-papers' in bn:
        continue
    
    # Determine slug
    if bn.startswith('functional-skills-'):
        slug = bn.replace('functional-skills-', '').replace('.html', '')
    else:
        slug = bn.replace('.html', '')
    
    sheet_rel = f"worksheets/{slug}-worksheet.html"
    ans_rel = f"worksheets/{slug}-answers.html"
    sheet_abs = os.path.join(BASE_DIR, sheet_rel)
    ans_abs = os.path.join(BASE_DIR, ans_rel)
    
    # Ensure worksheet and answer files exist
    if not os.path.exists(sheet_abs) or not os.path.exists(ans_abs):
        print(f"Warning: Missing worksheet files for {bn} (slug: {slug})")
        continue
    
    content = open(fpath, 'r', encoding='utf-8', errors='ignore').read()
    orig = content
    
    clean_title = slug.replace('reading-', '').replace('writing-', '').replace('slc-', '').replace('functional-skills-', '').replace('-', ' ').title()
    clean_title = clean_title.replace(' And ', ' & ').replace('2d', '2D').replace('3d', '3D').replace('Bidmas', 'BIDMAS')
    
    downloads_block = f"""        <!-- DOWNLOADS -->
        <section id="downloads" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-regular fa-file-pdf"></i> Free Revision Worksheets &amp; Exam Papers</h2>
          </div>

          <div class="download-tiles-grid">
            <a href="{sheet_rel}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-pdf"><i class="fa-regular fa-file-pdf"></i></div>
              <div class="download-tile-info">
                <strong>{clean_title} Exam Practice Worksheet (PDF)</strong>
                <span>Original practice questions calibrated for L1 &amp; L2 examinations</span>
              </div>
            </a>

            <a href="{ans_rel}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers"><i class="fa-solid fa-check-double"></i></div>
              <div class="download-tile-info">
                <strong>Step-by-Step Worked Mark Scheme (PDF)</strong>
                <span>Official tutor model answers with method marks breakdown</span>
              </div>
            </a>
          </div>
        </section>"""

    if '<section id="downloads"' in content:
        # Replace existing downloads section (including any preceding duplicate download comments)
        pattern = re.compile(r'(?:<!--\s*DOWNLOADS\s*-->\s*)*<section id="downloads"[\s\S]*?<\/section>', re.IGNORECASE)
        content = pattern.sub(downloads_block, content)
    else:
        # Insert downloads section before next topic / curriculum links or before </main> / </body>
        if '<section id="curriculum-links"' in content:
            content = content.replace('<section id="curriculum-links"', f'{downloads_block}\n\n        <section id="curriculum-links"')
        elif '<div class="next-topic-banner">' in content:
            content = content.replace('<div class="next-topic-banner">', f'{downloads_block}\n\n        <div class="next-topic-banner">')
        elif '</main>' in content:
            content = content.replace('</main>', f'{downloads_block}\n      </main>')
        elif '</body>' in content:
            content = content.replace('</body>', f'{downloads_block}\n</body>')

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_files.append(bn)

print(f"✅ Successfully updated {len(updated_files)} pages with direct worksheet & answers links!")
