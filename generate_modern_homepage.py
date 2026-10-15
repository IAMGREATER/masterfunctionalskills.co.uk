import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

homepage_html = """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills | UK's #1 Ofqual Regulated Courses, Exams & Revision</title>
  <meta name="description" content="Pass your Functional Skills Maths & English Level 1 & Level 2 first time. Ofqual regulated, GCSE grade 4/C equivalent. Free past papers, revision cards, online courses and exams.">
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
        <h1>The UK's Leading <span>Functional Skills</span> Specialist. Pass First Time!</h1>
        <p class="hero-description">
          Fast-track your GCSE Grade 4/C equivalent qualification. Master Functional Skills gives you the interactive courses, topic-by-topic drills, verified tutor feedback, and official Ofqual-regulated online exams you need to progress into nursing, university, teaching, or higher apprenticeships.
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
          <a href="exam-maths-l2.html" class="btn-hero-accent"><i class="fa-solid fa-calculator"></i> Book Maths Exam (£149)</a>
          <a href="exam-english-l2.html" class="btn-hero-navy"><i class="fa-solid fa-pen-nib"></i> Book English Exam (£149)</a>
          <a href="functional-skills-maths-level-2.html" class="btn-hero-outline"><i class="fa-solid fa-book-open"></i> Revise Maths L2</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/adult-student-smiling.jpg" alt="Adult learner achieving Functional Skills Level 2" style="height:210px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-graduation-cap"></i></div>
            <div>
              <strong>Fast-Track GCSE Equivalency</strong>
              <span>Pass in 2-4 weeks with Ofqual-regulated certification</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- OFFICIAL AWARDING BODIES ACCREDITATION LOGO BAR -->
  <section style="background:#ffffff; border-top:1px solid var(--border); border-bottom:1px solid var(--border); padding:24px 0;">
    <div class="mfs-container">
      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">
        <span style="font-size:0.82rem; font-weight:800; text-transform:uppercase; letter-spacing:0.06em; color:var(--text-muted); display:flex; align-items:center; gap:8px;">
          <i class="fa-solid fa-building-columns" style="color:var(--accent);"></i> Regulated Awarding Bodies:
        </span>
        <div style="display:flex; align-items:center; gap:20px; flex-wrap:wrap; justify-content:center;">
          <a href="edexcel-functional-skills-maths-level-2-past-papers.html" title="Pearson Edexcel Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/edexcel.jpg" alt="Pearson Edexcel Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="city-and-guilds-functional-skills-maths-level-2-past-papers.html" title="City & Guilds Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/city-and-guilds.jpg" alt="City & Guilds Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="aqa-functional-skills-maths-level-2-past-papers.html" title="AQA Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/aqa.jpg" alt="AQA Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="ncfe-functional-skills-maths-level-2-past-papers.html" title="NCFE Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/ncfe.jpg" alt="NCFE Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="open-awards-functional-skills-maths-level-2-past-papers.html" title="Open Awards Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/open-awards.jpg" alt="Open Awards Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="tquk-functional-skills-maths-level-2-past-papers.html" title="TQUK Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/tquk.png" alt="TQUK Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
          <a href="nocn-functional-skills-maths-level-2-past-papers.html" title="NOCN Past Papers" style="height:38px; display:inline-flex; align-items:center; padding:4px 8px; border-radius:8px; border:1px solid #e2e8f0; background:#ffffff;">
            <img src="assets/img/boards/nocn.png" alt="NOCN Logo" style="height:28px; width:auto; object-fit:contain;">
          </a>
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
          <div class="feature-icon-badge"><i class="fa-solid fa-calculator"></i></div>
          <div class="feature-card-body">
            <h3>Maths Level 2 Revision Hub</h3>
            <p>39 dedicated topics with golden rules, worksheet questions, video walkthroughs, and online topic tests.</p>
          </div>
        </div>
        <a href="functional-skills-maths-level-2.html" class="btn-card-action">Explore Maths Level 2 →</a>
      </div>

      <!-- Card 2 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-solid fa-pen-nib"></i></div>
          <div class="feature-card-body">
            <h3>English Level 2 Revision Hub</h3>
            <p>Master Reading, Writing, and Speaking with 34 topic guides, model letters, articles, and examiner criteria.</p>
          </div>
        </div>
        <a href="functional-skills-english-level-2.html" class="btn-card-action">Explore English Level 2 →</a>
      </div>

      <!-- Card 3 -->
      <div class="feature-action-card">
        <div class="feature-card-top">
          <div class="feature-icon-badge"><i class="fa-solid fa-chart-line"></i></div>
          <div class="feature-card-body">
            <h3>Free Diagnostic Assessment</h3>
            <p>Identify your exact starting grade and target weak areas with our AI diagnostic test before booking.</p>
          </div>
        </div>
        <a href="diagnostic-test.html" class="btn-card-action">Take Free Diagnostic →</a>
      </div>
    </div>
  </section>

  <!-- POPULAR COURSES & EXAMS SECTION -->
  <section style="padding: 64px 0; background: #ffffff; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:750px; margin: 0 auto 40px;">
        <span style="background:var(--accent-light); color:var(--accent); font-weight:800; font-size:0.8rem; padding:4px 12px; border-radius:var(--radius-full); text-transform:uppercase; letter-spacing:0.06em;">ACCELERATED QUALIFICATIONS</span>
        <h2 style="font-size:2.3rem; margin:12px 0 14px;">Select Your Functional Skills Qualification</h2>
        <p style="color:var(--text-secondary); font-size:1.05rem;">
          Official Ofqual-regulated examinations invigilated securely from home with fast verified results issued within 3-5 working days.
        </p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
        <!-- Box 1 -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; justify-content:space-between; transition:all 0.2s ease;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <span style="font-size:0.75rem; font-weight:800; color:var(--accent); text-transform:uppercase; letter-spacing:0.06em;">LEVEL 2 EXAM</span>
              <span style="font-size:1.35rem; font-weight:800; color:var(--navy-dark);">£149</span>
            </div>
            <h3 style="font-size:1.25rem; margin-bottom:10px;">Functional Skills Maths Level 2 Online Exam</h3>
            <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.5; margin-bottom:20px;">
              GCSE Grade 4 / C direct equivalent. Includes Non-Calculator (Section A) and Calculator (Section B) papers.
            </p>
          </div>
          <a href="exam-maths-l2.html" class="btn-mfs-revise" style="justify-content:center; padding:10px; font-size:0.92rem;">Book Maths Level 2 Exam →</a>
        </div>

        <!-- Box 2 -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; justify-content:space-between; transition:all 0.2s ease;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <span style="font-size:0.75rem; font-weight:800; color:var(--accent); text-transform:uppercase; letter-spacing:0.06em;">LEVEL 2 EXAM</span>
              <span style="font-size:1.35rem; font-weight:800; color:var(--navy-dark);">£149</span>
            </div>
            <h3 style="font-size:1.25rem; margin-bottom:10px;">Functional Skills English Level 2 Online Exam</h3>
            <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.5; margin-bottom:20px;">
              Complete Level 2 English certification covering Reading, Writing, and Speaking, Listening & Communicating.
            </p>
          </div>
          <a href="exam-english-l2.html" class="btn-mfs-revise" style="justify-content:center; padding:10px; font-size:0.92rem;">Book English Level 2 Exam →</a>
        </div>

        <!-- Box 3 -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; justify-content:space-between; transition:all 0.2s ease;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <span style="font-size:0.75rem; font-weight:800; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.06em;">LEVEL 1 EXAM</span>
              <span style="font-size:1.35rem; font-weight:800; color:var(--navy-dark);">£149</span>
            </div>
            <h3 style="font-size:1.25rem; margin-bottom:10px;">Functional Skills Maths Level 1 Online Exam</h3>
            <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.5; margin-bottom:20px;">
              GCSE Grade 1-3 / D-G equivalent. Ideal stepping stone qualification for vocational apprenticeships.
            </p>
          </div>
          <a href="functional-skills-exam.html" class="btn-card-action" style="font-size:0.92rem;">Book Maths Level 1 Exam →</a>
        </div>

        <!-- Box 4 -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; justify-content:space-between; transition:all 0.2s ease;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <span style="font-size:0.75rem; font-weight:800; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.06em;">LEVEL 1 EXAM</span>
              <span style="font-size:1.35rem; font-weight:800; color:var(--navy-dark);">£149</span>
            </div>
            <h3 style="font-size:1.25rem; margin-bottom:10px;">Functional Skills English Level 1 Online Exam</h3>
            <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.5; margin-bottom:20px;">
              Essential English workplace qualification certified by Pearson Edexcel and Open Awards.
            </p>
          </div>
          <a href="functional-skills-exam.html" class="btn-card-action" style="font-size:0.92rem;">Book English Level 1 Exam →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SPECIALIST PATHWAYS WITH AUTHENTIC REAL PHOTOGRAPHY -->
  <section style="padding: 72px 0; background: var(--bg-page);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:750px; margin: 0 auto 48px;">
        <span style="background:rgba(0,184,124,0.1); color:var(--accent); font-weight:800; font-size:0.8rem; padding:5px 14px; border-radius:var(--radius-full); text-transform:uppercase; letter-spacing:0.06em;">CAREER & ACADEMIC SUCCESS</span>
        <h2 style="font-size:2.3rem; margin:12px 0 14px;">Tailored For Real Careers & University Entry</h2>
        <p style="color:var(--text-secondary); font-size:1.05rem;">
          Whether you need a Grade 4 equivalent for NHS healthcare apprenticeships, university admission, or career promotion, our specialist training gets you qualified fast.
        </p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:28px;">
        <!-- Photo Card 1: NHS Healthcare & Nursing -->
        <div class="real-photo-card" style="min-height:360px;">
          <img src="assets/img/oet-nurse-doctor.jpg" alt="NHS Nurses and Doctors achieving qualifications" style="height:380px;">
          <div class="real-photo-overlay" style="bottom:20px; left:20px; right:20px;">
            <div style="font-size:2rem; color:var(--accent);"><i class="fa-solid fa-user-nurse"></i></div>
            <div>
              <strong>NHS Healthcare & Nursing Entry</strong>
              <span>Fast-track GCSE Grade 4/C equivalence required for nursing degrees, midwifery, and NHS Band 3–5 roles.</span>
            </div>
          </div>
        </div>

        <!-- Photo Card 2: 1-to-1 Specialist Tuition & Dyslexia Support -->
        <div class="real-photo-card" style="min-height:360px;">
          <img src="assets/img/tutor-teaching.jpg" alt="Specialist 1-to-1 Functional Skills tutor coaching student" style="height:380px;">
          <div class="real-photo-overlay" style="bottom:20px; left:20px; right:20px;">
            <div style="font-size:2rem; color:var(--accent);"><i class="fa-solid fa-chalkboard-user"></i></div>
            <div>
              <strong>1-to-1 Specialist Tuition & Dyslexia Support</strong>
              <span>Dedicated coaching by accredited tutors with dyslexia-friendly worksheets and step-by-step methods.</span>
            </div>
          </div>
        </div>

        <!-- Photo Card 3: Modern Digital Learning & Online Exams -->
        <div class="real-photo-card" style="min-height:360px;">
          <img src="assets/img/whiteboard-stylus-tablet.jpg" alt="Digital whiteboard and interactive Functional Skills lessons" style="height:380px;">
          <div class="real-photo-overlay" style="bottom:20px; left:20px; right:20px;">
            <div style="font-size:2rem; color:var(--accent);"><i class="fa-solid fa-laptop-code"></i></div>
            <div>
              <strong>Interactive Video Masterclasses</strong>
              <span>Topic-by-topic worked solutions, examiner hints, and live webcam remote proctoring from home.</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="mfs-faq-section">
    <div class="mfs-container">
      <div class="faq-header">
        <h2>Frequently Asked Questions About Master Functional Skills</h2>
        <p>Everything you need to know about our courses, online exam sittings, and certification.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What is Functional Skills Level 2 equivalent to?</h3>
          <p>Functional Skills Level 2 is officially recognized across the UK as a direct equivalent to a GCSE Grade 4 or Grade C pass. It meets the university entry, NHS nursing, and apprenticeship gateway requirements.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> How quickly can I sit my exam and get results?</h3>
          <p>You can book an exam slot with as little as 3 working days notice. Once completed, official results and verified e-certificates are issued in approximately 3 to 5 working days.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Are exams taken online from home?</h3>
          <p>Yes. All examinations are administered online from the comfort of your home using secure remote proctoring software with live invigilation.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Do you provide 1-to-1 specialist tuition support?</h3>
          <p>Yes. In addition to our self-paced courses and topic directories, we provide 1-to-1 live tuition delivered by accredited Pearson Edexcel and City & Guilds specialist tutors.</p>
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

</body>
</html>"""

with open(os.path.join(PROJECT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(homepage_html)

print("Generated modern index.html successfully!")
