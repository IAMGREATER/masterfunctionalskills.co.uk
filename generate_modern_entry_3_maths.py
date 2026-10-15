import json
import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
JSON_PATH = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch/entry_3_maths_topics.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    topics = json.load(f)

print(f"Loaded {len(topics)} Entry 3 topics.")

def get_mfs_worksheet(title, revise_href):
    ws_dir = set(os.listdir(os.path.join(PROJECT_DIR, 'worksheets')))
    slug = ''
    if revise_href and revise_href != '#':
        slug = revise_href.replace('functional-skills-', '').replace('.html', '')
    if not slug:
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

    ws_candidate = f"{slug}-worksheet.html"
    if ws_candidate in ws_dir:
        return f"worksheets/{ws_candidate}"

    ws_candidate_pre = f"functional-skills-{slug}-worksheet.html"
    if ws_candidate_pre in ws_dir:
        return f"worksheets/{ws_candidate_pre}"

    return f"worksheets/{slug}-worksheet.html"

topic_rows_html = ""
for t in topics:
    title = t["title"]
    cat = t["category"]
    links = t["links"]

    raw_revise = links.get("Revise", "#")
    slug = raw_revise.strip("/").split("/")[-1]
    revise_href = f"{slug}.html" if slug else "#"

    ws_url = get_mfs_worksheet(title, revise_href)
    video = links.get("Video Solution", "#")
    test = "functional-skills-courses.html"

    # Category code for filtering
    cat_class = "cat-numbers" if "number" in cat.lower() else ("cat-data" if "information" in cat.lower() or "data" in cat.lower() else "cat-measures")

    clean_cat = cat.strip().lower()
    if 'number' in clean_cat:
        cat_badge = '<div class="topic-category-tag tag-numbers" data-cat="numbers"><i class="fa-solid fa-arrow-down-1-9"></i> Using Numbers</div>'
    elif 'measure' in clean_cat or 'shape' in clean_cat or 'space' in clean_cat:
        cat_badge = '<div class="topic-category-tag tag-measures" data-cat="measures"><i class="fa-solid fa-ruler-combined"></i> Common Measures, Shape &amp; Space</div>'
    elif 'data' in clean_cat or 'handling' in clean_cat or 'information' in clean_cat:
        cat_badge = '<div class="topic-category-tag tag-data" data-cat="data"><i class="fa-solid fa-chart-column"></i> Handling Information &amp; Data</div>'
    else:
        cat_badge = f'<div class="topic-category-tag">{cat}</div>'

    topic_rows_html += f"""
      <div class="topic-row" data-category="{cat_class}" data-title="{title.lower()}">
        <div class="topic-meta">
          <div class="topic-title">{title}</div>
          {cat_badge}
        </div>
        <div class="topic-actions-group">
          <a href="{revise_href}" class="btn-mfs-revise"><i class="fa-solid fa-book-open"></i> Revise</a>
          <a href="{ws_url}" target="_blank" rel="noopener" class="btn-mfs-sheet"><i class="fa-regular fa-file-pdf"></i> Worksheet</a>
          <a href="{video}" target="_blank" rel="noopener" class="btn-mfs-video"><i class="fa-brands fa-youtube"></i> Video Solution</a>
          <a href="{test}" class="btn-mfs-test"><i class="fa-solid fa-list-check"></i> Topic Test</a>
        </div>
      </div>"""

template = """<!DOCTYPE html>
<html lang="en-GB" data-theme="maths" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Maths Entry Level 3 Revision & Worksheets | Master Functional Skills</title>
  <meta name="description" content="Master Functional Skills Maths Entry Level 3. Complete topic-by-topic revision guides, worksheet questions, video walkthroughs, and practice tests.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

  <!-- TOP TRUST BAR -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel & City & Guilds Aligned</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <!-- DYSLEXIA BACKGROUND TINT PICKER -->
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint or remove tint">
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Cream Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.62rem; opacity:0.75; margin-left:2px;"></i>
            </button>
            <div id="tintMenu" class="tint-picker-menu">
              <div class="tint-picker-title"><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</div>
              <button type="button" class="tint-option-btn active" data-tint="cream" onclick="setSiteTint('cream', event)">
                <span class="swatch swatch-cream"></span>
                <span class="tint-name">Cream <small class="tint-badge-def">Default</small></span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="peach" onclick="setSiteTint('peach', event)">
                <span class="swatch swatch-peach"></span>
                <span class="tint-name">Soft Peach</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="cool" onclick="setSiteTint('cool', event)">
                <span class="swatch swatch-cool"></span>
                <span class="tint-name">Cool Mist</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="sage" onclick="setSiteTint('sage', event)">
                <span class="swatch swatch-sage"></span>
                <span class="tint-name">Soft Sage</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <div class="tint-divider"></div>
              <button type="button" class="tint-option-btn" data-tint="none" onclick="setSiteTint('none', event)">
                <span class="swatch swatch-none"></span>
                <span class="tint-name">No Tint (White)</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
            </div>
          </div>
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia-Friendly High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
          <button id="themeToggle" class="mfs-theme-pill" onclick="toggleTheme()" title="Switch Palette: Sapphire vs Emerald">
            <i class="fa-solid fa-palette"></i> <span id="themeLabel">Sapphire</span>
          </button>
        </div>
        <a href="tel:020XXXXXXXX" class="top-contact-link"><i class="fa-solid fa-phone"></i> <strong>020 XXXX XXXX</strong></a>
        <a href="https://wa.me/447564525425" target="_blank" rel="noopener" class="top-contact-link"><i class="fa-brands fa-whatsapp"></i> <strong>+44 (0)7564 525425</strong></a>
        <a href="https://sterlingenglish.org" target="_blank" rel="noopener" class="top-badge-gold">1-to-1 Specialist Tuition ↗</a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <!-- MAIN NAVIGATION -->
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
            <a href="functional-skills-maths-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-calculator" style="color:#0284c7; margin-right:5px;"></i> Maths <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
              <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
              <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folder</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="functional-skills-english-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-pen-nib" style="color:#0284c7; margin-right:5px;"></i> English <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
              <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html#english" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="digital-functional-skills.html" class="mfs-nav-link"><i class="fa-solid fa-laptop-code" style="color:#0284c7; margin-right:5px;"></i> Digital Skills <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Mock Simulator</a>
              <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Data Files</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="pass-mark-calculator.html" class="mfs-nav-link"><i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Exam Simulator</a>
              <a href="bksb-remediation.html" class="mfs-dropdown-item"><i class="fa-solid fa-arrows-split-up-and-left" style="color:#8b5cf6; font-size:0.85rem; margin-right:6px;"></i> BKSB Remediation Bridge</a>
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
  </header>

  <!-- PROMOTIONAL SALE ACCENT BANNER -->
  <div class="mfs-promo-banner"><div class="mfs-container mfs-promo-inner"></div></div>

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <div class="hero-chip" style="display:inline-flex; align-items:center; gap:8px; padding:6px 14px; background:var(--accent-light); color:var(--accent); border-radius:30px; font-size:0.85rem; font-weight:700; margin-bottom:14px;">
          <i class="fa-solid fa-layer-group"></i> Foundation Numeracy Curriculum
        </div>
        <h1>Functional Skills <span>Maths Entry Level 3</span></h1>
        <p class="hero-description">
          Build unbreakable confidence in everyday numbers. Access our comprehensive Entry Level 3 maths curriculum with 24 dedicated topic modules, step-by-step revision lessons, downloadable question worksheets, model answer sheets, and video solutions.
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
            Average rating: <strong>4.9 / 5</strong> from <strong>980+ Entry 3 Learners</strong>
          </div>
        </div>

        

        <div class="hero-buttons">
          <a href="functional-skills-entry-level-3.html" class="btn-hero-accent"><i class="fa-solid fa-calendar-check"></i> Book Entry 3 Exam</a>
          <a href="functional-skills-courses.html" class="btn-hero-navy"><i class="fa-solid fa-graduation-cap"></i> Online Course</a>
          <a href="#revision" class="btn-hero-outline"><i class="fa-solid fa-arrow-down"></i> Browse 24 Topics</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/whiteboard-stylus-tablet.jpg" alt="Interactive Entry 3 Maths learning" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-calculator"></i></div>
            <div>
              <strong>Complete 24-Topic Curriculum</strong>
              <span>Numbers, Measures, Shape, Space & Data Handling</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- 3 ACTION CARDS -->
  <section class="mfs-features-section">
    <div class="mfs-container mfs-features-grid">
      <!-- Card 1 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-solid fa-book-open"></i></div>
          <div class="feature-card-body">
            <h3>Revise Entry 3 Topics</h3>
            <p>24 structured topic lessons covering four operations, decimals, money, scales, 2D/3D shapes, and charts.</p>
          </div>
        </div>
        <a href="#revision" class="btn-card-action">View Topic Directory →</a>
      </div>

      <!-- Card 2 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-regular fa-file-pdf"></i></div>
          <div class="feature-card-body">
            <h3>Download Past Papers</h3>
            <p>Direct 1-click access to official Pearson Edexcel and City & Guilds Entry Level 3 sample papers and mark schemes.</p>
          </div>
        </div>
        <a href="functional-skills-past-papers.html" class="btn-card-action">View Past Papers →</a>
      </div>

      <!-- Card 3 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-solid fa-chart-line"></i></div>
          <div class="feature-card-body">
            <h3>Free Diagnostic Check</h3>
            <p>Test your starting level in 15 minutes. Identify which topics you need to revise before sitting your assessment.</p>
          </div>
        </div>
        <a href="diagnostic-test.html" class="btn-card-action">Start Free Assessment →</a>
      </div>
    </div>
  </section>

  <!-- TOPIC REVISION DIRECTORY & TABLE -->
  <section class="mfs-directory-section" id="revision">
    <div class="mfs-container">
      
      <div class="directory-head-card">
        <div>
          <h2>
            <i class="fa-solid fa-list-check" style="color:var(--accent);"></i>
            Functional Skills Maths Entry Level 3 Curriculum
            <span class="badge-count">24 Topics</span>
          </h2>
          <p style="color:var(--text-muted); font-size:0.92rem; margin-top:4px;">Filter topics by category or search by keyword below.</p>
        </div>
        <div class="directory-search-wrapper">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="search" class="directory-search-input" id="topicSearchInput" placeholder="Search topics (e.g. Money, Decimals, Shapes)...">
        </div>
      </div>

      <!-- FILTER CHIPS -->
      <div style="display:flex; flex-wrap:wrap; gap:8px; margin: 16px 0 20px 0;">
        <button class="filter-chip active" onclick="filterCategory('all', this)">All Topics (24)</button>
        <button class="filter-chip" onclick="filterCategory('cat-numbers', this)">Using Numbers (8)</button>
        <button class="filter-chip" onclick="filterCategory('cat-measures', this)">Common Measures, Shape & Space (11)</button>
        <button class="filter-chip" onclick="filterCategory('cat-data', this)">Handling Information & Data (5)</button>
      </div>

      <div class="topic-table-bar">
        <span>Topic Name & Curriculum Cluster</span>
        <span>Revision & Study Resources</span>
      </div>

      <div class="topic-rows-container" id="topicsContainer">
__TOPIC_ROWS__
      </div>

    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="mfs-faq-section">
    <div class="mfs-container">
      <div class="faq-header">
        <h2>Functional Skills Maths Entry Level 3 — Frequently Asked Questions</h2>
        <p>Essential guidance on syllabus requirements, exam format, calculator rules, and progression pathways.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What is Functional Skills Maths Entry Level 3?</h3>
          <p>Entry Level 3 is a nationally recognised qualification regulated by Ofqual. It is designed for adult learners and students building their core foundation in everyday practical mathematics, preparing for Level 1 study, college entry, or employment.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What topics are tested in Entry 3 Maths?</h3>
          <p>The curriculum covers three main content domains: <strong>Using Numbers</strong> (whole numbers up to 1000, addition, subtraction, multiplication, division, simple fractions and decimals), <strong>Common Measures, Shape and Space</strong> (money, time, metric measurements, perimeter, 2D and 3D shapes), and <strong>Handling Information and Data</strong> (reading tables, tally charts, bar charts, and simple line graphs).</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Can I use a calculator in the exam?</h3>
          <p>Entry Level 3 Maths exams consist of two distinct sections: a short <strong>Non-Calculator section</strong> (testing basic mental and written arithmetic methods) and a longer <strong>Calculator section</strong> where you can use a standard scientific or four-function calculator.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> How do I take the Entry Level 3 exam?</h3>
          <p>You can sit your Entry Level 3 exam online from home with secure remote invigilation or at an accredited test centre. Exams can be booked with Master Functional Skills 6 days a week with fast turnaround results.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What can I do after passing Entry Level 3?</h3>
          <p>Passing Entry Level 3 demonstrates readiness for <strong>Functional Skills Maths Level 1</strong>, which is the direct stepping stone to Level 2 (the GCSE Grade 4/C equivalence needed for university courses, apprenticeships, and NHS nursing pathways).</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What revision resources are included?</h3>
          <p>Every single one of our 24 Entry 3 topics includes an in-depth lesson guide, a printable PDF question worksheet, a full model answer sheet, and an expert tutor video walkthrough breaking down problem solving step-by-step.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA FOOTER STRIP -->
  <section style="background:var(--navy-dark); color:#ffffff; padding:50px 0; text-align:center;">
    <div class="mfs-container">
      <h2 style="color:#ffffff; font-size:1.8rem; margin-bottom:12px;">Ready to Pass Your Entry Level 3 Maths?</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 24px auto; font-size:1.05rem;">
        Get unlimited access to interactive video tutorials, practice questions, and mock tests with our full online course or book your official exam today.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="functional-skills-entry-level-3.html" class="btn-hero-accent"><i class="fa-solid fa-calendar-check"></i> Book Entry 3 Exam</a>
        <a href="tel:020XXXXXXXX" class="btn-hero-outline" style="border-color:#ffffff; color:#ffffff;"><i class="fa-solid fa-phone"></i> Call 020 XXXX XXXX</a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="mfs-footer">
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
            The UK's leading Ofqual-regulated Functional Skills specialist. Empowering adult learners, healthcare apprentices, and college students to achieve verified qualifications first time.
          </p>
          <div style="font-size:0.85rem; color:#cbd5e1;">
            <p><i class="fa-solid fa-phone" style="color:var(--accent); margin-right:8px;"></i> 020 XXXX XXXX</p>
            <p style="margin-top:6px;"><i class="fa-brands fa-whatsapp" style="color:var(--accent); margin-right:8px;"></i> +44 (0)7564 525425</p>
          </div>
        </div>

        <div class="footer-col">
          <h4>Maths Revision</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-maths-level-2.html">Maths Level 2 Directory</a></li>
            <li><a href="functional-skills-maths-level-1.html">Maths Level 1 Directory</a></li>
            <li><a href="entry-level-3-maths.html">Entry Level 3 Maths</a></li>
            <li><a href="exam-maths-l2.html">Book Level 2 Maths Exam</a></li>
            <li><a href="functional-skills-past-papers.html">Free Maths Past Papers</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>English & Digital</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-english-level-2.html">English Level 2 Directory</a></li>
            <li><a href="functional-skills-english-level-1.html">English Level 1 Directory</a></li>
            <li><a href="digital-functional-skills.html">Digital Functional Skills Hub</a></li>
            <li><a href="digital-functional-skills-level-1.html">Digital Skills Level 1 Course</a></li>
            <li><a href="functional-skills-past-papers.html">Past Papers & Mark Schemes</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Institutional</h4>
          <ul class="footer-links">
            <li><a href="training-providers-and-employers.html">NHS & Employer Services</a></li>
            <li><a href="colleges.html">Colleges & Universities</a></li>
            <li><a href="career-functional-skills.html">Nursing & Police Pathways</a></li>
            <li><a href="pass-functional-skills-reviews.html">Verified Student Reviews</a></li>
            <li><a href="contact-us.html">Speak to a Tutor</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Master Functional Skills. All rights reserved. Registered in England & Wales. Ofqual Regulated Qualification Standards.</div>
        <div style="display:flex; gap:16px;">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms & Conditions</a>
          <a href="#">Cookie Policy</a>
          <a href="#">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- STYLES FOR FILTER CHIPS -->
  <style>
    .filter-chip {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 7px 16px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-dark);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .filter-chip:hover {
      border-color: var(--accent);
      color: var(--accent);
      background: var(--accent-light);
    }
    .filter-chip.active {
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
    }
  </style>

  <!-- LIVE SEARCH & CATEGORY FILTER JAVASCRIPT -->
  <script>
    let activeFilter = 'all';

    function filterCategory(cat, btn) {
      activeFilter = cat;
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      applyFilters();
    }

    const searchInput = document.getElementById('topicSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', applyFilters);
    }

    function applyFilters() {
      const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
      const rows = document.querySelectorAll('.topic-row');
      rows.forEach(row => {
        const title = row.getAttribute('data-title') || '';
        const cat = row.getAttribute('data-category') || '';
        const text = row.textContent.toLowerCase();

        const matchesQuery = !q || title.includes(q) || text.includes(q);
        const matchesCategory = activeFilter === 'all' || cat === activeFilter;

        if (matchesQuery && matchesCategory) {
          row.style.display = 'flex';
        } else {
          row.style.display = 'none';
        }
      });
    }

    // Dyslexia & Theme Toggles
    function toggleDyslexiaMode() {
      const isDys = document.body.classList.toggle('dyslexia-mode');
      localStorage.setItem('mfs_dyslexia', isDys ? '1' : '0');
      const btn = document.getElementById('dyslexiaToggle');
      if (btn) btn.classList.toggle('active', isDys);
    }
    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme') || 'sapphire';
      const next = current === 'emerald' ? 'sapphire' : 'emerald';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('mfs_theme', next);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = next === 'emerald' ? 'Emerald' : 'Sapphire';
    }
    (function() {
      if (localStorage.getItem('mfs_dyslexia') === '1') {
        document.body.classList.add('dyslexia-mode');
        const btn = document.getElementById('dyslexiaToggle');
        if (btn) btn.classList.add('active', true);
      }
      const th = localStorage.getItem('mfs_theme') || 'sapphire';
      document.documentElement.setAttribute('data-theme', th);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = th === 'emerald' ? 'Emerald' : 'Sapphire';
    })();
  </script>

  <!-- DYSLEXIA TINT ENGINE -->
  <script src="assets/js/mfs-tint.js"></script>
</body>
</html>
"""

full_html = template.replace("__TOPIC_ROWS__", topic_rows_html)
out_files = [
    os.path.join(PROJECT_DIR, "entry-level-3-maths.html"),
    os.path.join(PROJECT_DIR, "functional-skills-entry-level-3.html")
]
for out_file in out_files:
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully generated {out_file} ({len(full_html)} bytes)")
