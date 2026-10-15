import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Read NAV_HEADER and FOOTER from generate_modern_services_pages.py
with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    code = f.read()

import re
nav_match = re.search(r'NAV_HEADER = """(.*?)"""', code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

revise_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Revision Hub | Master Functional Skills</title>
  <meta name="description" content="Access complete Functional Skills revision directories for Maths, English, and Digital Functional Skills. Topic guides, worksheets, video tutorials, and past papers.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <div class="hero-chip" style="display:inline-flex; align-items:center; gap:8px; padding:6px 14px; background:var(--accent-light); color:var(--accent); border-radius:30px; font-size:0.85rem; font-weight:700; margin-bottom:14px;">
          <i class="fa-solid fa-graduation-cap"></i> Structured Learning Directories
        </div>
        <h1>Functional Skills <span>Revision Hub</span></h1>
        <p class="hero-description">
          The UK's most comprehensive revision directory for Ofqual-regulated Functional Skills. Select your subject and qualification level below to access dedicated topic revision guides, downloadable PDF question worksheets, model answer keys, and tutor video solutions.
        </p>

        <div class="hero-reviews-bar">
          <div class="star-rating">
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star-half-stroke"></i>
          </div>
          <div class="reviews-stat">
            Average rating: <strong>4.9 / 5</strong> from <strong>1,420+ Verified Reviews</strong>
          </div>
        </div>

        

        <div class="hero-buttons">
          <a href="#directories" class="btn-hero-accent"><i class="fa-solid fa-book-open"></i> Browse Revision Directories</a>
          <a href="functional-skills-past-papers.html" class="btn-hero-navy"><i class="fa-regular fa-file-pdf"></i> Free Past Papers</a>
          <a href="diagnostic-test.html" class="btn-hero-outline"><i class="fa-solid fa-chart-line"></i> Free Diagnostic Test</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/whiteboard-stylus-tablet.jpg" alt="Learner studying interactive functional skills revision" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-layer-group"></i></div>
            <div>
              <strong>Complete Step-by-Step Curriculum</strong>
              <span>Maths • English • Digital Functional Skills</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- DIRECTORIES GRID -->
  <section class="mfs-features-section" id="directories" style="padding:60px 0; background:var(--bg-page);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:750px; margin:0 auto 40px auto;">
        <span style="color:var(--accent); font-weight:700; text-transform:uppercase; font-size:0.85rem; letter-spacing:0.05em;">Curriculum Directories</span>
        <h2 style="font-size:2rem; margin-top:6px; margin-bottom:12px;">Choose Your Subject & Level to Revise</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Each directory features topic video lessons, free downloadable question worksheets, model answers, and interactive topic tests.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px;">
        
        <!-- Maths Level 2 Card -->
        <div style="background:#ffffff; border-radius:16px; border:2px solid var(--accent); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between; position:relative;">
          <div style="position:absolute; top:-12px; right:20px; background:var(--accent); color:#ffffff; font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:12px;">POPULAR • GCSE EQUIVALENT</div>
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-calculator"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">Maths Level 2</h3>
                <span style="font-size:0.85rem; color:var(--accent); font-weight:700;">39 Comprehensive Topics</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              The complete GCSE Grade 4/C equivalent syllabus: percentages, ratio, fractions, algebra, geometry, compound measures, probability, and statistics.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 39 Topic Guides & Formula Traps</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Non-Calculator & Calculator Drills</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Free PDF Worksheets & Video Solutions</li>
            </ul>
          </div>
          <div>
            <a href="functional-skills-maths-level-2.html" class="btn-card-action" style="display:block; text-align:center;">Revise Maths Level 2 (39 Topics) →</a>
          </div>
        </div>

        <!-- Maths Level 1 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-square-root-variable"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">Maths Level 1</h3>
                <span style="font-size:0.85rem; color:var(--accent); font-weight:700;">38 Structured Topics</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              Build solid numerical mastery: decimals, fractions, basic ratios, area, perimeter, volume, scales, bar charts, and data handling.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 38 Topic Revision Lessons</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Practical everyday problem solving</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Question worksheets & model answers</li>
            </ul>
          </div>
          <div>
            <a href="functional-skills-maths-level-1.html" class="btn-card-action" style="display:block; text-align:center;">Revise Maths Level 1 (38 Topics) →</a>
          </div>
        </div>

        <!-- Maths Entry Level 3 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:#eff6ff; color:#2563eb; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-seedling"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">Maths Entry Level 3</h3>
                <span style="font-size:0.85rem; color:#2563eb; font-weight:700;">24 Essential Topics</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              Essential foundation numeracy: addition, subtraction, times tables, division, money, time, 2D/3D shapes, and reading tables and charts.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> 24 Step-by-Step Lessons</li>
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> Printable PDF worksheets with answer keys</li>
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> Dedicated video walkthroughs for every topic</li>
            </ul>
          </div>
          <div>
            <a href="entry-level-3-maths.html" class="btn-card-action" style="display:block; text-align:center;">Revise Entry 3 Maths (24 Topics) →</a>
          </div>
        </div>

        <!-- English Level 2 Card -->
        <div style="background:#ffffff; border-radius:16px; border:2px solid var(--accent); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between; position:relative;">
          <div style="position:absolute; top:-12px; right:20px; background:var(--accent); color:#ffffff; font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:12px;">POPULAR • GCSE EQUIVALENT</div>
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-pen-nib"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">English Level 2</h3>
                <span style="font-size:0.85rem; color:var(--accent); font-weight:700;">34 Intensive Topics</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              Master Reading (fact vs opinion, implicit meaning, organisational devices) and Writing (reports, formal letters, articles, SPaG excellence).
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Complete Reading & Writing Coverage</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Model answers with examiner annotations</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Speaking, Listening & Communicating (SLC) guides</li>
            </ul>
          </div>
          <div>
            <a href="functional-skills-english-level-2.html" class="btn-card-action" style="display:block; text-align:center;">Revise English Level 2 (34 Topics) →</a>
          </div>
        </div>

        <!-- English Level 1 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-book-open-reader"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">English Level 1</h3>
                <span style="font-size:0.85rem; color:var(--accent); font-weight:700;">33 Essential Topics</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              Essential literacy skills: text comprehension, locating details, sentence construction, punctuation, vocabulary, and workplace writing.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 33 Reading and Writing lessons</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Spelling, Punctuation & Grammar (SPaG) checklists</li>
              <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Practice texts and comprehension tests</li>
            </ul>
          </div>
          <div>
            <a href="functional-skills-english-level-1.html" class="btn-card-action" style="display:block; text-align:center;">Revise English Level 1 (33 Topics) →</a>
          </div>
        </div>

        <!-- Digital Skills Hub Card -->
        <div style="background:#ffffff; border-radius:16px; border:2px solid #2563eb; padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between; position:relative;">
          <div style="position:absolute; top:-12px; right:20px; background:#2563eb; color:#ffffff; font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:12px;">NEW REFORMED QUALIFICATION</div>
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:#eff6ff; color:#2563eb; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-laptop-code"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">Digital Skills</h3>
                <span style="font-size:0.85rem; color:#2563eb; font-weight:700;">Entry Level 3 & Level 1</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:18px;">
              The official reformed computer literacy qualification covering 5 National Standards: Devices & Information, Creating & Editing, Communicating, Transacting, and Safety.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> 5 National Digital Curriculum Standards</li>
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> Digital Skills Entry Level 3 (Essential Foundation)</li>
              <li><i class="fa-solid fa-check" style="color:#2563eb; margin-right:8px;"></i> Digital Skills Level 1 (Workplace & Apprenticeships)</li>
            </ul>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a href="digital-functional-skills.html" class="btn-card-action" style="flex:1; text-align:center; background:#eff6ff; color:#2563eb; border:1px solid #2563eb; min-width:140px;">Digital Skills Entry 3 →</a>
            <a href="digital-functional-skills-level-1.html" class="btn-card-action" style="flex:1; text-align:center; background:#2563eb; color:#ffffff; min-width:140px;">Digital Skills Level 1 →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- OFFICIAL AWARDING BODIES ACCREDITATION BAR -->
  <section style="background:#ffffff; padding:45px 0; border-top:1px solid var(--border); border-bottom:1px solid var(--border);">
    <div class="mfs-container" style="text-align:center;">
      <p style="font-size:0.85rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--text-muted); font-weight:700; margin-bottom:24px;">
        Curriculum Fully Aligned with Official UK Awarding Organisations
      </p>
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:36px;">
        <img src="assets/img/boards/edexcel.png" alt="Pearson Edexcel" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/city-and-guilds.png" alt="City & Guilds" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/aqa.png" alt="AQA" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/ncfe.png" alt="NCFE" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/open-awards.png" alt="Open Awards" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/tquk.png" alt="TQUK" style="height:38px; object-fit:contain; filter:grayscale(10%);">
        <img src="assets/img/boards/nocn.png" alt="NOCN" style="height:38px; object-fit:contain; filter:grayscale(10%);">
      </div>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="mfs-faq-section">
    <div class="mfs-container">
      <div class="faq-header">
        <h2>Functional Skills Revision — Frequently Asked Questions</h2>
        <p>Everything you need to know about preparing for your Functional Skills exams.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> How do I know which level to start with?</h3>
          <p>We recommend taking our <a href="diagnostic-test.html" style="color:var(--accent); font-weight:700;">Free Diagnostic Assessment</a>. It takes 15–20 minutes and pinpoint your exact current skill level (Entry 3, Level 1, or Level 2) with a tailored revision study plan.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Are all resources free on Master Functional Skills?</h3>
          <p>Yes. All of our topic revision overviews, downloadable question worksheets, model answer sheets, video solutions, and official awarding body past papers are 100% free to view and download with 1-click access and no email paywalls.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Which exam board does Master Functional Skills follow?</h3>
          <p>The Functional Skills subject content is established by the Department for Education (DfE) and regulated by Ofqual. Our curriculum directly covers Pearson Edexcel, City & Guilds, AQA, NCFE, Open Awards, TQUK, and NOCN specifications.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What if I need 1-to-1 specialist tutor support?</h3>
          <p>We offer 1-to-1 specialist tuition with certified tutors through our partner platform Sterling English. Visit <a href="https://sterlingenglish.org" target="_blank" rel="noopener" style="color:var(--accent); font-weight:700;">Sterling English ↗</a> or call us on <strong>020 XXXX XXXX</strong>.</p>
        </div>
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>
"""

with open(os.path.join(PROJECT_DIR, "revise.html"), "w", encoding="utf-8") as f:
    f.write(revise_html)

print("Generated modern master revise.html successfully!")
