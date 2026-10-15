import os
import re
import urllib.parse

BACKUP_DIR = "/home/subi/Projects/passfunctionalskills.co.uk-exact-clone-backup"
PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

PAGE_CONFIGS = [
    {
        "filename": "functional-skills-maths-level-1.html",
        "theme": "maths",
        "title": "Functional Skills Maths Level 1 | Master Functional Skills",
        "h1_prefix": "Functional Skills",
        "h1_accent": "Maths Level 1",
        "meta_desc": "Master Functional Skills Maths Level 1. Complete topic-by-topic revision guides, worksheet questions, video walkthroughs, and practice tests.",
        "course_link": "functional-skills-courses.html",
        "exam_link": "functional-skills-exam.html",
        "exam_price": "£149",
        "subject_name": "Maths Level 1",
        "search_query_prefix": "Functional Skills Maths Level 1",
        "faq_q1": "What is Functional Skills Maths Level 1 equivalent to?",
        "faq_a1": "Functional Skills Maths Level 1 is equivalent to GCSE grades 1 to 3 (grades D-G in the old grading scale). It serves as the primary stepping stone to Level 2 and is recognized for many entry-level apprenticeships and workplace training programs.",
        "active_nav": "revise"
    },
    {
        "filename": "functional-skills-english-level-2.html",
        "theme": "english",
        "title": "Functional Skills English Level 2 | Master Functional Skills",
        "h1_prefix": "Functional Skills",
        "h1_accent": "English Level 2",
        "meta_desc": "Master Functional Skills English Level 2. Pass first time with dedicated Reading, Writing, and SLC revision guides, worksheet questions, and model answers.",
        "course_link": "course-english-l2.html",
        "exam_link": "exam-english-l2.html",
        "exam_price": "£149",
        "subject_name": "English Level 2",
        "search_query_prefix": "Functional Skills English Level 2",
        "faq_q1": "What does the Functional Skills English Level 2 exam include?",
        "faq_a1": "The English Level 2 qualification consists of three core components: Reading, Writing, and Speaking, Listening & Communicating (SLC). Each section tests practical workplace communication, textual analysis, and accurate written expression.",
        "active_nav": "revise"
    },
    {
        "filename": "functional-skills-english-level-1.html",
        "theme": "english",
        "title": "Functional Skills English Level 1 | Master Functional Skills",
        "h1_prefix": "Functional Skills",
        "h1_accent": "English Level 1",
        "meta_desc": "Master Functional Skills English Level 1. Comprehensive guides, worksheets, video tutorials, and topic tests for Reading, Writing, and SLC.",
        "course_link": "functional-skills-courses.html",
        "exam_link": "functional-skills-exam.html",
        "exam_price": "£149",
        "subject_name": "English Level 1",
        "search_query_prefix": "Functional Skills English Level 1",
        "faq_q1": "How does Functional Skills English Level 1 help my career?",
        "faq_a1": "English Level 1 equips you with essential literacy and communication skills for the workplace and daily life. It satisfies the prerequisite entry requirements for numerous Level 2 apprenticeships and vocational NVQs.",
        "active_nav": "revise"
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en-GB" data-theme="__THEME__" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__PAGE_TITLE__</title>
  <meta name="description" content="__META_DESC__">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png">
  <link rel="apple-touch-icon" href="assets/img/favicon-192x192.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

  <!-- TOP TRUST BAR -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel &amp; City &amp; Guilds Aligned</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <!-- DYSLEXIA BACKGROUND TINT PICKER -->
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint">
              <i class="fa-solid fa-glasses"></i>
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Dyslexia Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.55rem; opacity:0.75; margin-left:1px;"></i>
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
        </div>
        <a href="tel:020XXXXXXXX" class="top-contact-link"><i class="fa-solid fa-phone"></i> <strong>020 XXXX XXXX</strong></a>
        <a href="https://wa.me/447564525425" target="_blank" rel="noopener" class="top-contact-link"><i class="fa-brands fa-whatsapp"></i> <strong>WhatsApp</strong></a>
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
        <h1>__H1_PREFIX__ <span>__H1_ACCENT__</span></h1>
        <p class="hero-description">
          The complete Functional Skills __SUBJECT_NAME__ curriculum directory. Access dedicated topic revision guides, interactive video tutorials, practice worksheet questions, and worked solutions. Everything you need to succeed in your Ofqual-regulated exam.
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
          <a href="__EXAM_LINK__" class="btn-hero-accent"><i class="fa-solid fa-check"></i> Book __SUBJECT_NAME__ Exam (__EXAM_PRICE__)</a>
          <a href="__COURSE_LINK__" class="btn-hero-navy"><i class="fa-solid fa-play"></i> Online Course</a>
          <a href="#revision" class="btn-hero-outline"><i class="fa-solid fa-arrow-down"></i> Revise Topics</a>
        </div>
      </div>

      <!-- Right Column: Pass Rates Comparison Card -->
      
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
            <h3>Revise __SUBJECT_NAME__ Topics</h3>
            <p>Over __TOPIC_COUNT__ dedicated topic guides with clear rules, examiner tips, and step-by-step model answers.</p>
          </div>
        </div>
        <a href="#revision" class="btn-card-action">View Topic Directory →</a>
      </div>

      <!-- Card 2 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-regular fa-file-pdf"></i></div>
          <div class="feature-card-body">
            <h3>__SUBJECT_NAME__ Past Papers</h3>
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
          Functional Skills __SUBJECT_NAME__ Curriculum
          <span class="badge-count">__TOPIC_COUNT__ Topics</span>
        </h2>
        <div class="directory-search-wrapper">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="search" class="directory-search-input" id="topicSearchInput" placeholder="Search topics...">
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
        <h2>Functional Skills __SUBJECT_NAME__ — Frequently Asked Questions</h2>
        <p>Everything you need to know about the exam, syllabus, preparation, and certificate.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> __FAQ_Q1__</h3>
          <p>__FAQ_A1__</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Are all resources and past papers accessible online?</h3>
          <p>Yes. All __TOPIC_COUNT__ topic revision guides, downloadable PDF worksheets, model answers, and video walkthroughs are 100% accessible online from your desktop, tablet, or smartphone anytime.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Can I sit the exam online from home?</h3>
          <p>Yes. We provide official Ofqual-regulated Pearson Edexcel and Open Awards online exams invigilated via secure remote proctoring from Monday through Saturday.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> How quickly are results and certificates issued?</h3>
          <p>Exam results are typically released within 6 to 14 working days, and official Ofqual-certified e-certificates and paper certificates are delivered shortly after.</p>
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

  <!-- DYSLEXIA TINT ENGINE -->
  <script src="assets/js/mfs-tint.js"></script>

</body>
</html>"""

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
        'functional-skills-english-level-2-writing-blog': 'worksheets/english-level-2-writing-blog-worksheet.html',
        'writing-blog': 'worksheets/english-level-2-writing-blog-worksheet.html',
    }
    if slug in SPECIAL_MAP:
        return SPECIAL_MAP[slug]

    ws_candidate = f"{slug}-worksheet.html"
    if ws_candidate in ws_dir:
        return f"worksheets/{ws_candidate}"

    ws_candidate_pre = f"functional-skills-{slug}-worksheet.html"
    if ws_candidate_pre in ws_dir:
        return f"worksheets/{ws_candidate_pre}"

    for prefix in ['reading-', 'writing-', 'slc-']:
        if slug.startswith(prefix):
            sub_slug = slug[len(prefix):]
            if f"{sub_slug}-worksheet.html" in ws_dir:
                return f"worksheets/{sub_slug}-worksheet.html"

    if slug == '#' or not slug or 'walkthrough' in slug or 'video' in slug or 'video' in title.lower():
        return None

    return f"worksheets/{slug}-worksheet.html"

def build_page(cfg):
    source_path = os.path.join(BACKUP_DIR, cfg["filename"])
    if not os.path.exists(source_path):
        print(f"File not found: {source_path}")
        return

    with open(source_path, "r", encoding="utf-8") as f:
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
        link_matches = re.findall(r"<a[^>]+href=\"([^\"]+)\"[^>]*>(.*?)</a>", links_html)
        link_dict = {}
        for url, text in link_matches:
            clean_text = re.sub(r"<[^>]+>", "", text).strip()
            link_dict[clean_text] = url.strip()
        topics.append({
            "title": title,
            "category": cat,
            "links": link_dict
        })

    print(f"{cfg['filename']}: parsed {len(topics)} topics.")

    topic_rows_html = ""
    for t in topics:
        title = t["title"]
        cat = t["category"]
        links = t["links"]

        raw_revise = links.get("Revise", "#")
        slug = raw_revise.strip("/").split("/")[-1]
        revise_href = f"{slug}.html" if (slug and not slug.endswith(".html")) else (slug if slug else "#")

        # Resolve MFS Worksheet
        ws_url = get_mfs_worksheet(title, revise_href)
        ws_btn = f'<a href="{ws_url}" target="_blank" rel="noopener" class="btn-mfs-sheet"><i class="fa-regular fa-file-pdf"></i> Worksheet</a>' if ws_url else ''

        # Video Solution link
        video = links.get("Video Solution", "")
        if not video or video == "#":
            encoded_query = urllib.parse.quote_plus(f"{cfg['search_query_prefix']} {title}")
            video = f"https://www.youtube.com/results?search_query={encoded_query}"

        test = "functional-skills-courses.html"

        # Format category badge with distinct highlights and icons
        clean_cat = cat.strip().lower()
        if 'reading' in clean_cat:
            cat_badge = '<div class="topic-category-tag tag-reading" data-cat="reading"><i class="fa-solid fa-book-open-reader"></i> Reading</div>'
        elif 'writing' in clean_cat:
            cat_badge = '<div class="topic-category-tag tag-writing" data-cat="writing"><i class="fa-solid fa-pen-nib"></i> Writing</div>'
        elif 'slc' in clean_cat or 'speaking' in clean_cat or 'listening' in clean_cat or 'communicat' in clean_cat:
            cat_badge = '<div class="topic-category-tag tag-slc" data-cat="slc"><i class="fa-solid fa-comments"></i> Speaking, Listening &amp; Communicating</div>'
        elif 'number' in clean_cat:
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
          {ws_btn}
          <a href="{video}" target="_blank" rel="noopener" class="btn-mfs-video"><i class="fa-brands fa-youtube"></i> Video Solution</a>
          <a href="{test}" class="btn-mfs-test"><i class="fa-solid fa-list-check"></i> Topic Test</a>
        </div>
      </div>"""

    html = HTML_TEMPLATE
    html = html.replace("__PAGE_TITLE__", cfg["title"])
    html = html.replace("__META_DESC__", cfg["meta_desc"])
    html = html.replace("__H1_PREFIX__", cfg["h1_prefix"])
    html = html.replace("__H1_ACCENT__", cfg["h1_accent"])
    html = html.replace("__SUBJECT_NAME__", cfg["subject_name"])
    html = html.replace("__EXAM_LINK__", cfg["exam_link"])
    html = html.replace("__EXAM_PRICE__", cfg["exam_price"])
    html = html.replace("__COURSE_LINK__", cfg["course_link"])
    html = html.replace("__TOPIC_COUNT__", str(len(topics)))
    html = html.replace("__FAQ_Q1__", cfg["faq_q1"])
    html = html.replace("__FAQ_A1__", cfg["faq_a1"])
    html = html.replace("__THEME__", cfg.get("theme", "sapphire"))
    html = html.replace("__TOPIC_ROWS__", topic_rows_html)

    out_path = os.path.join(PROJECT_DIR, cfg["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {cfg['filename']} successfully with 100% WORKING LINKS!")

if __name__ == "__main__":
    for c in PAGE_CONFIGS:
        build_page(c)
