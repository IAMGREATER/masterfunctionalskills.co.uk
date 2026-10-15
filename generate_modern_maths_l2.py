import os
import re

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
SOURCE_HTML = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch/maths_l2_source.html"

with open(SOURCE_HTML, "r", encoding="utf-8") as f:
    raw_html = f.read()

pattern = re.compile(
    r"<h4[^>]*>\s*(?P<title>[^<]+?)\s*</h4>\s*"
    r"<small[^>]*>\s*(?P<category>[^<]+?)\s*</small>.*?"
    r"<ul class=\"list-inline mb-0 d-none d-lg-block\">(?P<links>.*?)</ul>",
    re.DOTALL
)

topics = []
for m in pattern.finditer(raw_html):
    title = m.group("title").strip()
    cat = m.group("category").strip()
    links_html = m.group("links")
    link_matches = re.findall(r"<a href=\"([^\"]+)\"[^>]*>(.*?)</a>", links_html)
    link_dict = {}
    for url, text in link_matches:
        link_dict[text.strip()] = url.strip()
    topics.append({
        "title": title,
        "category": cat,
        "links": link_dict
    })

print(f"Parsed {len(topics)} topics.")

def get_mfs_worksheet(title, revise_href):
    ws_dir = set(os.listdir(os.path.join(PROJECT_DIR, 'worksheets')))
    slug = ''
    if revise_href and revise_href != '#':
        slug = revise_href.replace('functional-skills-', '').replace('.html', '')
    if not slug:
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

    SPECIAL_MAP = {
        'fractions-decimals-and-percentages': 'worksheets/fdp-conversions-worksheet.html',
        'fdp-conversions': 'worksheets/fdp-conversions-worksheet.html',
        'speed-distance-and-time': 'worksheets/speed-distance-time-worksheet.html',
        'compound-measures': 'worksheets/speed-distance-time-worksheet.html',
        'drawing-and-measuring-angles': 'worksheets/angles-worksheet.html',
        'reading-and-interpreting-tables': 'worksheets/tables-worksheet.html',
        'bar-charts-and-histograms': 'worksheets/bar-charts-worksheet.html',
    }
    if slug in SPECIAL_MAP:
        return SPECIAL_MAP[slug]

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

    # Format category badge with distinct highlights and icons
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
      <div class="topic-row">
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
  <title>Functional Skills Maths Level 2 | Master Functional Skills</title>
  <meta name="description" content="Master Functional Skills Maths Level 2. Pass first time with topic-by-topic revision guides, worksheet questions, video solutions, and practice tests.">
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
        <h1>Functional Skills <span>Maths Level 2</span></h1>
        <p class="hero-description">
          The complete Functional Skills Maths Level 2 curriculum directory. Access dedicated topic revision guides, interactive video tutorials, practice worksheet questions, and worked solutions. Everything you need to secure your Ofqual-regulated Grade 4 / C equivalent qualification.
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
          <a href="exam-maths-l2.html" class="btn-hero-accent"><i class="fa-solid fa-check"></i> Book Level 2 Exam (£149)</a>
          <a href="course-maths-l2.html" class="btn-hero-navy"><i class="fa-solid fa-play"></i> Online Course</a>
          <a href="#revision" class="btn-hero-outline"><i class="fa-solid fa-arrow-down"></i> Revise Topics</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/whiteboard-stylus-tablet.jpg" alt="Interactive Maths Level 2 digital problem solving" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-calculator"></i></div>
            <div>
              <strong>Complete 39-Topic Curriculum</strong>
              <span>Interactive videos, worksheets, answers, and online tests</span>
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
            <h3>Revise Maths Level 2 Topics</h3>
            <p>Over 39 dedicated topic guides with clear golden rules, examiner traps, and step-by-step model answers.</p>
          </div>
        </div>
        <a href="#revision" class="btn-card-action">View Topic Directory →</a>
      </div>

      <!-- Card 2 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-regular fa-file-pdf"></i></div>
          <div class="feature-card-body">
            <h3>Maths Level 2 Past Papers</h3>
            <p>Download free Pearson Edexcel, City & Guilds, and Open Awards past papers with complete mark schemes.</p>
          </div>
        </div>
        <a href="functional-skills-past-papers.html" class="btn-card-action">View Past Papers →</a>
      </div>

      <!-- Card 3 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-solid fa-chart-line"></i></div>
          <div class="feature-card-body">
            <h3>Free Diagnostic Assessment</h3>
            <p>Pinpoint your exact strengths and target weak areas with our AI diagnostic test before booking your exam.</p>
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
        <h2>
          <i class="fa-solid fa-list-check" style="color:var(--accent);"></i>
          Functional Skills Maths Level 2 Curriculum
          <span class="badge-count">39 Topics</span>
        </h2>
        <div class="directory-search-wrapper">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="search" class="directory-search-input" id="topicSearchInput" placeholder="Search topics (e.g. Fractions, Ratio, Area)...">
        </div>
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
        <h2>Functional Skills Maths Level 2 — Frequently Asked Questions</h2>
        <p>Everything you need to know about the exam, syllabus, preparation, and certificate.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Is Functional Skills Maths Level 2 easier than GCSE?</h3>
          <p>Many adult learners find Functional Skills Maths Level 2 more manageable than GCSE because questions focus directly on practical workplace and everyday life contexts. There is less abstract algebra and trigonometry, allowing focused revision in weeks rather than years.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Are all resources and past papers accessible online?</h3>
          <p>Yes. All 39 topic revision guides, downloadable PDF worksheets, model answers, and video walkthroughs are 100% accessible online from your desktop, tablet, or smartphone anytime.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Can I sit the Level 2 exam online from home?</h3>
          <p>Yes. We provide official Ofqual-regulated Pearson Edexcel and Open Awards online exams invigilated via secure remote proctoring from Monday through Saturday.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Is Level 2 accepted for university, nursing, and apprenticeships?</h3>
          <p>Yes. Functional Skills Level 2 is officially recognized by UCAS, the NHS, police forces, apprenticeship standards, and UK universities as a direct equivalent to GCSE grade 4 / C.</p>
        </div>
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
            The UK's leading Ofqual-regulated Functional Skills specialist. Empowering adult learners, healthcare apprentices, and college students to achieve verified Level 2 qualifications first time.
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
          <h4>Digital & English</h4>
          <ul class="footer-links">
            <li><a href="digital-functional-skills.html">Digital Skills Hub (L1 & E3)</a></li>
            <li><a href="digital-functional-skills-level-1.html">Digital Skills Level 1 Course</a></li>
            <li><a href="functional-skills-english-level-2.html">English Level 2 Directory</a></li>
            <li><a href="functional-skills-english-level-1.html">English Level 1 Directory</a></li>
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

  <!-- CLIENT SEARCH & SMOOTH SCROLL JAVASCRIPT -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      var searchInput = document.getElementById("topicSearchInput");
      var container = document.getElementById("topicsContainer");
      if (searchInput && container) {
        var rows = container.querySelectorAll(".topic-row");
        searchInput.addEventListener("input", function() {
          var q = this.value.toLowerCase().trim();
          rows.forEach(function(row) {
            var text = row.textContent.toLowerCase();
            row.style.display = text.includes(q) ? "flex" : "none";
          });
        });
      }

      document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener("click", function(e) {
          var targetId = this.getAttribute("href").substring(1);
          if (!targetId) return;
          var targetEl = document.getElementById(targetId);
          if (targetEl) {
            e.preventDefault();
            targetEl.scrollIntoView({ behavior: "smooth" });
          }
        });
      });
    });
  </script>

  <!-- THEME & DYSLEXIA MODE ENGINE -->
  <script>
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
</html>"""

full_html = template.replace("__TOPIC_ROWS__", topic_rows_html)

target_file = os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html")
with open(target_file, "w", encoding="utf-8") as f:
    f.write(full_html)

# Also update maths-level-2.html
with open(os.path.join(PROJECT_DIR, "maths-level-2.html"), "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated modern functional-skills-maths-level-2.html and maths-level-2.html successfully!")
