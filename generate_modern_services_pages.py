import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

NAV_HEADER = """
  <!-- TOP TRUST BAR WITH ACCESSIBILITY & CONTACT -->
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
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
          <button id="themeToggle" class="mfs-theme-pill" onclick="toggleTheme()" title="Switch Palette: Sapphire vs Emerald">
            <i class="fa-solid fa-palette"></i> <span id="themeLabel">Sapphire</span>
          </button>
        </div>
        <a href="contact-us.html" class="top-contact-link"><i class="fa-solid fa-envelope"></i> <strong>Contact Us</strong></a>
      </div>
    </div>
  </div>

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
  </header>

  <!-- PROMOTIONAL SALE ACCENT BANNER -->
  <div class="mfs-promo-banner"><div class="mfs-container mfs-promo-inner"></div></div>
"""

FOOTER = """
  <!-- FOOTER -->
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
            <li><a href="revision-cards.html">Revision Cards &amp; Flashcards</a></li>
            <li><a href="shop.html">Revision Books &amp; Study Packs</a></li>
            <li><a href="diagnostic-test.html">Diagnostic Skill Checker</a></li>
            <li><a href="functional-skills-nets.html">3D Net Folding Tool</a></li>
            <li><a href="tutors.html">1-to-1 Specialist Tuition</a></li>
            <li><a href="functional-skills-exam.html">Book Official Online Exam</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Master Functional Skills. All rights reserved. Registered in England &amp; Wales. Ofqual Regulated Qualification Standards.</div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="index.html">Home</a>
          <a href="functional-skills-past-papers.html">Past Papers</a>
          <a href="revision-cards.html">Revision Cards</a>
          <a href="shop.html">Study Shop</a>
          <a href="tutors.html">Tutors</a>
          <a href="contact-us.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>
"""
  <!-- DYSLEXIA TINT ENGINE -->
  <script src="assets/js/mfs-tint.js"></script>

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
"""

def generate_courses():
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Courses | Master Functional Skills</title>
  <meta name="description" content="The UK's leading Ofqual-regulated Functional Skills courses for Maths and English Level 2 and Level 1. high pass rate with AI learning plans and mock exams.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>Functional Skills <span>Online Courses</span></h1>
        <p class="hero-description">
          The UK's highest rated online courses for Functional Skills Maths and English. Powered by adaptive diagnostic assessments, topic video masterclasses, interactive worksheet drills, and unlimited AI-marked mock exams.
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
          <a href="#course-list" class="btn-hero-accent"><i class="fa-solid fa-play"></i> Explore All Courses</a>
          <a href="diagnostic-test.html" class="btn-hero-navy"><i class="fa-solid fa-chart-line"></i> Free Diagnostic Test</a>
          <a href="functional-skills-exam.html" class="btn-hero-outline"><i class="fa-solid fa-pencil"></i> Book Online Exam</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/student-learning-online.jpg" alt="Learner studying Functional Skills online courses" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-graduation-cap"></i></div>
            <div>
              <strong>Structured Step-by-Step Learning</strong>
              <span>Interactive videos, exam drills, and unlimited AI mock marking</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- COURSES LIST SECTION -->
  <section class="mfs-features-section" id="course-list">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Choose Your Dedicated Course</h2>
        <p>Interactive study, video tutorials, practice worksheets, and full pass guarantee included.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px; margin-top:32px;">
        
        <!-- Course 1 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative; overflow:hidden;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Most Popular</div>
          <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; margin-bottom:20px;">
            <i class="fa-solid fa-calculator"></i>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Maths Level 2 Online Course</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Complete Ofqual-aligned curriculum covering all 39 Level 2 topics: numbers, fractions, ratio, percentages, geometry, and statistics. Includes 5 full mock exams.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Access from</span>
              <strong style="font-size:1.4rem; color:var(--navy); font-weight:800;">£19.99 <span style="font-size:0.85rem; font-weight:500; color:var(--text-muted);">/mo</span></strong>
            </div>
            <a href="course-maths-l2.html" class="btn-card-action" style="padding:10px 18px;">Enrol Now →</a>
          </div>
        </div>

        <!-- Course 2 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative; overflow:hidden;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Pass Guarantee</div>
          <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; margin-bottom:20px;">
            <i class="fa-solid fa-pen-nib"></i>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">English Level 2 Online Course</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Comprehensive preparation for Reading, Writing, and Speaking components. Model answers, SPaG drills, examiner marking criteria, and simulated past paper mocks.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Access from</span>
              <strong style="font-size:1.4rem; color:var(--navy); font-weight:800;">£19.99 <span style="font-size:0.85rem; font-weight:500; color:var(--text-muted);">/mo</span></strong>
            </div>
            <a href="course-english-l2.html" class="btn-card-action" style="padding:10px 18px;">Enrol Now →</a>
          </div>
        </div>

        <!-- Course 3 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative; overflow:hidden;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(11,21,40,0.08); color:var(--navy); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Best Value Bundle</div>
          <div style="width:48px; height:48px; border-radius:12px; background:rgba(7,13,30,0.06); color:var(--navy); display:flex; align-items:center; justify-content:center; font-size:1.4rem; margin-bottom:20px;">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Dual Maths & English Bundle</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Unlock both complete courses at a discounted rate. Satisfy all university, apprenticeship, and healthcare prerequisites with a unified personal learning dashboard.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Access from</span>
              <strong style="font-size:1.4rem; color:var(--navy); font-weight:800;">£34.99 <span style="font-size:0.85rem; font-weight:500; color:var(--text-muted);">/mo</span></strong>
            </div>
            <a href="functional-skills-courses.html" class="btn-card-action" style="padding:10px 18px;">Enrol Bundle →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section style="padding:70px 0; background:#ffffff;">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>How The Platform Works</h2>
        <p>A proven step-by-step methodology that guarantees you become ExamReady.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:24px; margin-top:40px;">
        <div style="padding:24px; border-radius:12px; border:1px solid var(--border); background:#f8fafc;">
          <div style="font-size:1.8rem; font-weight:800; color:var(--accent); margin-bottom:12px;">01</div>
          <h4 style="font-size:1.1rem; font-weight:700; color:var(--navy); margin-bottom:8px;">Diagnostic Test</h4>
          <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.5;">Identify your current baseline level and pin down specific topics requiring reinforcement.</p>
        </div>
        <div style="padding:24px; border-radius:12px; border:1px solid var(--border); background:#f8fafc;">
          <div style="font-size:1.8rem; font-weight:800; color:var(--accent); margin-bottom:12px;">02</div>
          <h4 style="font-size:1.1rem; font-weight:700; color:var(--navy); margin-bottom:8px;">Personalized Plan</h4>
          <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.5;">Get an intelligent roadmap organized topic by topic, skipping what you already know.</p>
        </div>
        <div style="padding:24px; border-radius:12px; border:1px solid var(--border); background:#f8fafc;">
          <div style="font-size:1.8rem; font-weight:800; color:var(--accent); margin-bottom:12px;">03</div>
          <h4 style="font-size:1.1rem; font-weight:700; color:var(--navy); margin-bottom:8px;">Interactive Practice</h4>
          <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.5;">Learn through concise video tutorials, worked model solutions, and topic practice tests.</p>
        </div>
        <div style="padding:24px; border-radius:12px; border:1px solid var(--border); background:#f8fafc;">
          <div style="font-size:1.8rem; font-weight:800; color:var(--accent); margin-bottom:12px;">04</div>
          <h4 style="font-size:1.1rem; font-weight:700; color:var(--navy); margin-bottom:8px;">Mock Exams & ExamReady</h4>
          <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.5;">Complete authentic past paper mocks under exam conditions before booking your official exam.</p>
        </div>
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""
    with open(os.path.join(PROJECT_DIR, "functional-skills-courses.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated functional-skills-courses.html successfully!")

def generate_exam():
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Exam | Master Functional Skills</title>
  <meta name="description" content="Book official Ofqual-regulated Functional Skills Maths and English Level 2 exams online. Sit from home with remote invigilation or at 50+ UK test centres.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>Functional Skills <span>Online Exams</span></h1>
        <p class="hero-description">
          Sit your official Ofqual-regulated Functional Skills Maths and English exams online from the comfort of your own home. Fast-track booking, Monday–Saturday exam slots, and results released in 6–14 working days.
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
          <a href="#exam-cards" class="btn-hero-accent"><i class="fa-solid fa-calendar-check"></i> Choose Exam & Book</a>
          <a href="functional-skills-courses.html" class="btn-hero-navy"><i class="fa-solid fa-play"></i> Preparation Courses</a>
          <a href="tel:020XXXXXXXX" class="btn-hero-outline"><i class="fa-solid fa-phone"></i> 020 XXXX XXXX</a>
        </div>
      </div>

      <!-- Right Column: Real Exam Candidate & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/student-laptop.jpg" alt="Student sitting official Functional Skills exam online from home" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-laptop-code"></i></div>
            <div>
              <strong>Sit From Home • Fast Results</strong>
              <span>Secure webcam invigilation Monday–Saturday with official certificate</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- EXAMS GRID -->
  <section class="mfs-features-section" id="exam-cards">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Official Ofqual-Regulated Exams</h2>
        <p>Direct GCSE Grade 4 / C equivalent qualifications accepted by all UK universities and employers.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px; margin-top:32px;">
        
        <!-- Exam Card 1 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Popular</div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Maths Level 2 Online Exam</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Non-calculator & calculator sections invigilated remotely. Regulated by Ofqual, Pearson Edexcel & Open Awards aligned.
          </p>
          <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; color:var(--navy);">
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Online remote invigilation from home</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Results in 6–14 working days</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Free mock paper & practice software test</li>
          </ul>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Total Fee</span>
              <strong style="font-size:1.5rem; color:var(--navy); font-weight:800;">£149</strong>
            </div>
            <a href="exam-maths-l2.html" class="btn-hero-accent" style="padding:10px 20px; font-size:0.9rem;">Book Now →</a>
          </div>
        </div>

        <!-- Exam Card 2 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Popular</div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">English Level 2 Online Exam</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Includes Reading, Writing, and Speaking, Listening & Communicating (SLC) assessments. Recognized by NHS and universities.
          </p>
          <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; color:var(--navy);">
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> All 3 components included in one fee</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Online SLC conducted with friendly assessors</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Ofqual certified e-certificate</li>
          </ul>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Total Fee</span>
              <strong style="font-size:1.5rem; color:var(--navy); font-weight:800;">£149</strong>
            </div>
            <a href="exam-english-l2.html" class="btn-hero-accent" style="padding:10px 20px; font-size:0.9rem;">Book Now →</a>
          </div>
        </div>

        <!-- Exam Card 3 -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="position:absolute; top:16px; right:16px; background:rgba(11,21,40,0.08); color:var(--navy); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Save £49</div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Dual Maths & English Bundle</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Book both Maths Level 2 and English Level 2 exams together. Meet all entry criteria for nursing, PGCE teaching, and university.
          </p>
          <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; color:var(--navy);">
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Complete dual qualification pathway</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Flexible sitting dates (book dates when ready)</li>
            <li style="margin-bottom:8px;"><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Priority fast-track results option</li>
          </ul>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <div>
              <span style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.04em; display:block;">Bundle Price</span>
              <strong style="font-size:1.5rem; color:var(--navy); font-weight:800;">£249 <s style="font-size:0.95rem; color:var(--text-muted); font-weight:400;">£298</s></strong>
            </div>
            <a href="functional-skills-exam.html" class="btn-hero-accent" style="padding:10px 20px; font-size:0.9rem;">Book Bundle →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""
    with open(os.path.join(PROJECT_DIR, "functional-skills-exam.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated functional-skills-exam.html successfully!")

def generate_past_papers():
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Past Papers & Mark Schemes | Master Functional Skills</title>
  <meta name="description" content="Download free genuine past papers and official mark schemes for Pearson Edexcel, City & Guilds, Open Awards, and NCFE Functional Skills Maths and English.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>Functional Skills <span>Past Papers</span></h1>
        <p class="hero-description">
          Access genuine Functional Skills past papers, official mark schemes, and video model solutions for Pearson Edexcel, City & Guilds, Open Awards, and NCFE. Free to view and download.
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
            Over <strong>50,000+ past paper practice downloads</strong> this year
          </div>
        </div>

        

        <div class="hero-buttons">
          <a href="#papers-grid" class="btn-hero-accent"><i class="fa-solid fa-download"></i> View Past Papers</a>
          <a href="functional-skills-maths-level-2.html" class="btn-hero-navy"><i class="fa-solid fa-calculator"></i> Maths Revision</a>
          <a href="functional-skills-english-level-2.html" class="btn-hero-outline"><i class="fa-solid fa-pen-nib"></i> English Revision</a>
        </div>
      </div>

      <!-- Right Column: Pass Rates Comparison Card -->
      
    </div>
  </section>

  <!-- PAPERS DIRECTORY -->
  <section class="mfs-features-section" id="papers-grid">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Free Past Papers by Level & Subject</h2>
        <p>Select your subject and level to access authentic past exam papers and examiner mark schemes.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-top:32px;">
        
        <!-- Maths L2 Card -->
        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge"><i class="fa-solid fa-calculator"></i></div>
            <div class="feature-card-body">
              <h3>Maths Level 2 Past Papers</h3>
              <p>Download Pearson Edexcel, City & Guilds, and Open Awards past papers with full mark schemes.</p>
            </div>
          </div>
          <a href="functional-skills-maths-level-2.html#revision" class="btn-card-action">Access Maths Level 2 Papers →</a>
        </div>

        <!-- English L2 Card -->
        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge"><i class="fa-solid fa-pen-nib"></i></div>
            <div class="feature-card-body">
              <h3>English Level 2 Past Papers</h3>
              <p>Practice authentic Reading and Writing exam papers with model student answers and examiner notes.</p>
            </div>
          </div>
          <a href="functional-skills-english-level-2.html#revision" class="btn-card-action">Access English Level 2 Papers →</a>
        </div>

        <!-- Maths L1 Card -->
        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge"><i class="fa-solid fa-square-root-variable"></i></div>
            <div class="feature-card-body">
              <h3>Maths Level 1 Past Papers</h3>
              <p>Authentic foundation papers to prepare you for Level 1 certification and stepping up to Level 2.</p>
            </div>
          </div>
          <a href="functional-skills-maths-level-1.html#revision" class="btn-card-action">Access Maths Level 1 Papers →</a>
        </div>

        <!-- English L1 Card -->
        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge"><i class="fa-solid fa-book"></i></div>
            <div class="feature-card-body">
              <h3>English Level 1 Past Papers</h3>
              <p>Reading texts, comprehension worksheets, and practical writing tasks with official mark criteria.</p>
            </div>
          </div>
          <a href="functional-skills-english-level-1.html#revision" class="btn-card-action">Access English Level 1 Papers →</a>
        </div>

      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""
    with open(os.path.join(PROJECT_DIR, "functional-skills-past-papers.html"), "w", encoding="utf-8") as f:
        f.write(html)
    # Also update past-papers.html
    with open(os.path.join(PROJECT_DIR, "past-papers.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated functional-skills-past-papers.html and past-papers.html successfully!")

if __name__ == "__main__":
    generate_courses()
    generate_exam()
    generate_past_papers()
