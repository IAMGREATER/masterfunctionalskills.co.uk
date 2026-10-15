import os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

NAV_BAR = """
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
"""

FOOTER = """
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
            <li><a href="digital-functional-skills-level-1.html">DFS Level 1 Course</a></li>
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

  <!-- THEME & DYSLEXIA SCRIPT -->
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

# ==============================================================================
# 1. DIGITAL FUNCTIONAL SKILLS HUB (digital-functional-skills.html)
# ==============================================================================
dfs_hub_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Digital Functional Skills Qualifications (DFSQ Entry 3 & DFS Level 1) | Master Functional Skills</title>
  <meta name="description" content="Prepare and pass your Ofqual-regulated Digital Functional Skills qualifications. Online courses, curriculum guides, practice tasks, and Pearson Edexcel sample papers for DFSQ Entry 3 & DFS Level 1.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

{NAV_BAR}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <div class="hero-chip" style="display:inline-flex; align-items:center; gap:8px; padding:6px 14px; background:var(--accent-light); color:var(--accent); border-radius:30px; font-size:0.85rem; font-weight:700; margin-bottom:14px;">
          <i class="fa-solid fa-microchip"></i> Modernised 2023+ Qualification Standard
        </div>
        <h1>Digital Functional Skills <span>Qualifications (DFSQ)</span></h1>
        <p class="hero-description">
          The UK's official qualification for modern computer literacy and workplace digital competence. Replaces legacy ICT with high-impact, practical skills: cloud collaboration, document styling, spreadsheet formulas, cybersecurity, and digital transactions.
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
            Average rating: <strong>4.9 / 5</strong> from <strong>1,200+ Verified Learners</strong>
          </div>
        </div>

        

        <div class="hero-buttons">
          <a href="digital-functional-skills-level-1.html" class="btn-hero-accent"><i class="fa-solid fa-play"></i> Level 1 Digital Course</a>
          <a href="#past-papers" class="btn-hero-navy"><i class="fa-regular fa-file-pdf"></i> Sample Assessment Papers</a>
          <a href="#curriculum" class="btn-hero-outline"><i class="fa-solid fa-list-check"></i> Explore 5 Standards</a>
        </div>
      </div>

      <!-- Right Column: Real Photo & Stats -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/student-laptop.jpg" alt="Adult learner mastering digital skills on laptop" style="height:220px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-laptop-code"></i></div>
            <div>
              <strong>DfE & Ofqual Regulated DFSQ</strong>
              <span>Available at DFSQ Entry 3 & DFS Level 1</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- 2 QUALIFICATION LEVELS CARDS -->
  <section style="padding:50px 0; background:var(--bg-card); border-bottom:1px solid var(--border);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
        <h2 style="font-size:1.8rem; margin-bottom:10px;">Choose Your Digital Qualification Level</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Digital Functional Skills Qualifications are available at two official Ofqual levels designed for different career and educational stages.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px;">
        <!-- Entry Level 3 Card (Foundation) -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:#eff6ff; color:#2563eb; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-seedling"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">DFSQ Entry 3</h3>
                <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Foundation Level / Essential User</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:18px;">
              Ideal for beginners seeking to build solid confidence using smartphones, tablets, laptops, safe web browsing, online health services (NHS app), and introductory email.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.9rem; display:flex; flex-direction:column; gap:10px;">
              <li><i class="fa-solid fa-circle-check" style="color:#2563eb; margin-right:8px;"></i> Basic device navigation, touchscreen, mouse & keyboard</li>
              <li><i class="fa-solid fa-circle-check" style="color:#2563eb; margin-right:8px;"></i> Simple word processing, text styling & saving files</li>
              <li><i class="fa-solid fa-circle-check" style="color:#2563eb; margin-right:8px;"></i> Creating and sending basic emails with attachments</li>
              <li><i class="fa-solid fa-circle-check" style="color:#2563eb; margin-right:8px;"></i> Simple digital transactions & filling in web forms</li>
              <li><i class="fa-solid fa-circle-check" style="color:#2563eb; margin-right:8px;"></i> Recognizing basic scams & protecting personal passwords</li>
            </ul>
          </div>
          <div>
            <a href="contact-us.html" class="btn-hero-navy" style="width:100%; text-align:center; display:block;"><i class="fa-solid fa-phone"></i> Inquire About Entry 3 Digital</a>
          </div>
        </div>

        <!-- Level 1 Card (Workplace Standard) -->
        <div style="background:#ffffff; border-radius:16px; border:2px solid var(--accent); padding:32px; box-shadow:0 8px 24px rgba(0,0,0,0.06); position:relative; display:flex; flex-direction:column; justify-content:space-between;">
          <div style="position:absolute; top:-12px; right:24px; background:var(--accent); color:#ffffff; font-size:0.75rem; font-weight:700; text-transform:uppercase; padding:4px 12px; border-radius:12px;">Most Popular for Work</div>
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
              <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
                <i class="fa-solid fa-certificate"></i>
              </div>
              <div>
                <h3 style="font-size:1.3rem; margin:0;">DFS Level 1</h3>
                <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Equivalent to GCSE Grade 1-3 / Level 1 Standard</span>
              </div>
            </div>
            <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:18px;">
              Designed for adult learners and apprentices who need autonomous digital capability for modern employment, office tasks, spreadsheet analysis, and secure online collaboration.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.9rem; display:flex; flex-direction:column; gap:10px;">
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Spreadsheet formulas: SUM, AVERAGE, COUNT, Sort & Filter</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Hierarchical file folder management & cloud storage units</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Advanced workplace email etiquette & calendar scheduling</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Cybersecurity threats, phishing analysis & 2FA protection</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> 100% online invigilated exam from home</li>
            </ul>
          </div>
          <div>
            <a href="digital-functional-skills-level-1.html" class="btn-hero-accent" style="width:100%; text-align:center; display:block;"><i class="fa-solid fa-arrow-right"></i> View Level 1 Course & Exams</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- THE 5 CORE NATIONAL SKILL STANDARDS -->
  <section class="mfs-directory-section" id="curriculum" style="background:#ffffff; padding:60px 0;">
    <div class="mfs-container">
      <div style="text-align:center; max-width:750px; margin:0 auto 40px auto;">
        <span style="color:var(--accent); font-weight:700; text-transform:uppercase; font-size:0.85rem; letter-spacing:0.05em;">National Curriculum Framework</span>
        <h2 style="font-size:2rem; margin-top:6px; margin-bottom:12px;">The 5 Core Digital Functional Skills Standards</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Both DFSQ Entry 3 and DFS Level 1 are structured around the 5 government national standards for digital skills:</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px;">
        <!-- Standard 1 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); transition:all 0.2s ease;">
          <div style="width:44px; height:44px; border-radius:10px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.3rem; margin-bottom:14px;">
            <i class="fa-solid fa-folder-tree"></i>
          </div>
          <h3 style="font-size:1.15rem; margin-bottom:8px;">1. Using Devices & Handling Information</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
            Learn to navigate operating systems, manage system settings, organize folders hierarchically, understand data storage metrics (KB, MB, GB, TB), perform effective internet queries, and evaluate online source reliability.
          </p>
        </div>

        <!-- Standard 2 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); transition:all 0.2s ease;">
          <div style="width:44px; height:44px; border-radius:10px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.3rem; margin-bottom:14px;">
            <i class="fa-solid fa-pen-ruler"></i>
          </div>
          <h3 style="font-size:1.15rem; margin-bottom:8px;">2. Creating & Editing</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
            Produce workplace-ready documents, crop and insert digital images, master spreadsheet formulas (SUM, AVERAGE, COUNT, sorting), and format charts to present commercial information clearly.
          </p>
        </div>

        <!-- Standard 3 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); transition:all 0.2s ease;">
          <div style="width:44px; height:44px; border-radius:10px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.3rem; margin-bottom:14px;">
            <i class="fa-solid fa-comments"></i>
          </div>
          <h3 style="font-size:1.15rem; margin-bottom:8px;">3. Communicating</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
            Master professional email etiquette, manage attachments and subject lines, organize video conference invitations (Teams / Zoom), control group messaging, and understand personal digital footprints.
          </p>
        </div>

        <!-- Standard 4 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); transition:all 0.2s ease;">
          <div style="width:44px; height:44px; border-radius:10px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.3rem; margin-bottom:14px;">
            <i class="fa-solid fa-cart-shopping"></i>
          </div>
          <h3 style="font-size:1.15rem; margin-bottom:8px;">4. Transacting</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
            Confidently complete complex online application forms, upload verification documents, manage e-commerce checkouts safely, utilize the NHS App, and verify secure SSL padlock indicators.
          </p>
        </div>

        <!-- Standard 5 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); transition:all 0.2s ease;">
          <div style="width:44px; height:44px; border-radius:10px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.3rem; margin-bottom:14px;">
            <i class="fa-solid fa-shield-virus"></i>
          </div>
          <h3 style="font-size:1.15rem; margin-bottom:8px;">5. Being Safe & Responsible Online</h3>
          <p style="font-size:0.88rem; color:var(--text-muted); line-height:1.6;">
            Implement strong password strategies and two-factor authentication (2FA), spot suspicious phishing communications, understand GDPR rights, protect privacy, and practice physical ergonomics and screen wellbeing.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- OFFICIAL SAMPLE PAPERS (SAMS) SECTION -->
  <section class="mfs-features-section" id="past-papers" style="padding:60px 0; background:var(--bg-page);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
        <span class="top-badge-gold" style="display:inline-block; margin-bottom:10px;">1-Click Direct Downloads</span>
        <h2 style="font-size:1.8rem; margin-bottom:10px;">Official Digital Functional Skills Sample Papers</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Download official Pearson Edexcel and awarding body sample assessment materials (SAMs) to see the exact test format.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
        <!-- Edexcel Entry 3 SAM -->
        <div style="background:#ffffff; border-radius:14px; border:1px solid var(--border); padding:24px; box-shadow:0 6px 18px rgba(0,0,0,0.05); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="board-pill board-pill-edexcel"><img src="assets/img/boards/edexcel.png" alt="Edexcel"> Pearson Edexcel</span>
              <span style="font-size:0.75rem; background:#eff6ff; color:#2563eb; font-weight:700; padding:2px 8px; border-radius:10px;">DFSQ Entry 3</span>
            </div>
            <h4 style="font-size:1.05rem; margin:0;">DFSQ Entry 3 Sample Assessment Material</h4>
            <p style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">Official foundational sample paper and assessment criteria.</p>
          </div>
          <a href="https://qualifications.pearson.com/content/dam/pdf/Functional-skills/digital/2023/specification-and-sample-assessments/dfsq-e3-sam.pdf" target="_blank" rel="noopener" class="btn-card-action" style="padding:10px 18px; white-space:nowrap;">
            <i class="fa-regular fa-file-pdf"></i> Download PDF
          </a>
        </div>

        <!-- Edexcel Level 1 SAM -->
        <div style="background:#ffffff; border-radius:14px; border:1px solid var(--border); padding:24px; box-shadow:0 6px 18px rgba(0,0,0,0.05); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
              <span class="board-pill board-pill-edexcel"><img src="assets/img/boards/edexcel.png" alt="Edexcel"> Pearson Edexcel</span>
              <span style="font-size:0.75rem; background:var(--accent-light); color:var(--accent); font-weight:700; padding:2px 8px; border-radius:10px;">Level 1</span>
            </div>
            <h4 style="font-size:1.05rem; margin:0;">DFSQ Level 1 Sample Assessment Material</h4>
            <p style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">Complete official test paper, scenario data, and marking guide.</p>
          </div>
          <a href="https://qualifications.pearson.com/content/dam/pdf/Functional-skills/digital/2023/specification-and-sample-assessments/dfsq-l1-sam.pdf" target="_blank" rel="noopener" class="btn-card-action" style="padding:10px 18px; white-space:nowrap;">
            <i class="fa-regular fa-file-pdf"></i> Download PDF
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- COMPARISON TABLE SECTION -->
  <section style="padding:60px 0; background:#ffffff; border-top:1px solid var(--border);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:700px; margin:0 auto 36px auto;">
        <h2 style="font-size:1.8rem; margin-bottom:10px;">DFSQ Entry 3 vs DFS Level 1 Comparison</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Key differences in exam structure, independence requirements, and duration.</p>
      </div>

      <div style="overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; text-align:left; background:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 4px 16px rgba(0,0,0,0.06); border:1px solid var(--border);">
          <thead>
            <tr style="background:var(--navy-dark); color:#ffffff; font-size:0.95rem;">
              <th style="padding:16px 20px;">Feature</th>
              <th style="padding:16px 20px;">DFSQ Entry 3 (Digital Functional Skills Entry 3)</th>
              <th style="padding:16px 20px;">DFS Level 1 (Digital Functional Skills Level 1)</th>
            </tr>
          </thead>
          <tbody style="font-size:0.92rem; color:var(--text-dark);">
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:14px 20px; font-weight:700;">Qualification Equivalence</td>
              <td style="padding:14px 20px;">Foundation / Entry Level Standard</td>
              <td style="padding:14px 20px; color:var(--accent); font-weight:700;">GCSE Grade 1–3 / Level 1 Standard</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border); background:var(--bg-card);">
              <td style="padding:14px 20px; font-weight:700;">Independence Level</td>
              <td style="padding:14px 20px;">Guided; explicit step-by-step instructions</td>
              <td style="padding:14px 20px;">Autonomous; selecting appropriate tools without guidance</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:14px 20px; font-weight:700;">Spreadsheet Skills</td>
              <td style="padding:14px 20px;">Entering data and simple cell edits</td>
              <td style="padding:14px 20px;">Formulas (SUM, AVERAGE), formatting, sorting data</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border); background:var(--bg-card);">
              <td style="padding:14px 20px; font-weight:700;">Assessment Duration</td>
              <td style="padding:14px 20px;">Approximately 1 hour to 1 hour 30 mins</td>
              <td style="padding:14px 20px;">Approximately 1 hour 30 mins to 2 hours</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:14px 20px; font-weight:700;">Assessment Format</td>
              <td style="padding:14px 20px;">100% onscreen digital exam with guided tasks</td>
              <td style="padding:14px 20px;">100% onscreen digital exam with real software tasks</td>
            </tr>
            <tr>
              <td style="padding:14px 20px; font-weight:700;">Apprenticeship Requirement</td>
              <td style="padding:14px 20px;">Foundation preparation for Level 1 study</td>
              <td style="padding:14px 20px; color:var(--accent); font-weight:700;">Satisfies Level 2 apprenticeship digital gateway</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="mfs-faq-section">
    <div class="mfs-container">
      <div class="faq-header">
        <h2>Digital Functional Skills — Frequently Asked Questions</h2>
        <p>Common questions about the reformed qualification, funding, exam format, and certificate.</p>
      </div>

      <div class="faq-grid">
        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> What happened to Functional Skills ICT?</h3>
          <p>Functional Skills ICT was officially retired by Ofqual and the Department for Education in 2023. It was replaced by <strong>Digital Functional Skills Qualifications (DFSQ)</strong>, which reflect modern cloud computing, smartphones, online privacy, and workplace digital tools.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Is the Digital Functional Skills exam taken online?</h3>
          <p>Yes. The entire assessment is completed onscreen. You can sit your exam securely from home using our remote invigilation system, provided you have a computer with a webcam and microphone.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Do employers and universities accept DFSQ?</h3>
          <p>Yes. Digital Functional Skills qualifications are regulated by Ofqual and listed on the Register of Regulated Qualifications. They are widely recognized by employers, apprenticeship providers, NHS trusts, and colleges across the UK.</p>
        </div>

        <div class="faq-card">
          <h3><i class="fa-solid fa-circle-question"></i> Which awarding bodies offer DFSQ?</h3>
          <p>Major UK awarding bodies including Pearson Edexcel, City & Guilds, NCFE, and Open Awards offer accredited Digital Functional Skills Qualifications. Master Functional Skills prepares you for and delivers Pearson Edexcel and City & Guilds assessments.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA STRIP -->
  <section style="background:var(--navy-dark); color:#ffffff; padding:50px 0; text-align:center;">
    <div class="mfs-container">
      <h2 style="color:#ffffff; font-size:1.8rem; margin-bottom:12px;">Boost Your Digital Career Credentials Today</h2>
      <p style="color:#cbd5e1; max-width:650px; margin:0 auto 24px auto; font-size:1.05rem;">
        Enroll in our structured Level 1 Digital Course with interactive task training, video lessons, and mock exams.
      </p>
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <a href="digital-functional-skills-level-1.html" class="btn-hero-accent"><i class="fa-solid fa-graduation-cap"></i> Explore Level 1 Course</a>
        <a href="tel:020XXXXXXXX" class="btn-hero-outline" style="border-color:#ffffff; color:#ffffff;"><i class="fa-solid fa-phone"></i> Call 020 XXXX XXXX</a>
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>
"""

# ==============================================================================
# 2. DIGITAL FUNCTIONAL SKILLS LEVEL 1 (digital-functional-skills-level-1.html)
# ==============================================================================
dfs_l1_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Digital Functional Skills Level 1 Online Course & Exam | Master Functional Skills</title>
  <meta name="description" content="Complete Digital Functional Skills Level 1 online course and Ofqual-regulated exam. Master spreadsheets, cloud file management, cybersecurity, and workplace communication with our pass guarantee.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

{NAV_BAR}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <div class="hero-chip" style="display:inline-flex; align-items:center; gap:8px; padding:6px 14px; background:var(--accent-light); color:var(--accent); border-radius:30px; font-size:0.85rem; font-weight:700; margin-bottom:14px;">
          <i class="fa-solid fa-bolt"></i> Complete Online Course & Accredited Exam
        </div>
        <h1>Digital Functional Skills <span>Level 1 Course</span></h1>
        <p class="hero-description">
          Fast-track your workplace computer confidence. Learn to navigate spreadsheets, cloud file systems, professional email etiquette, online safety, and transactional web apps with our interactive, self-paced Level 1 course.
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
            Rated <strong>4.9 / 5</strong> by adult learners & apprenticeship candidates
          </div>
        </div>

        

        <div class="hero-buttons">
          <a href="#enroll" class="btn-hero-accent"><i class="fa-solid fa-check"></i> Enroll in Course (£199)</a>
          <a href="https://qualifications.pearson.com/content/dam/pdf/Functional-skills/digital/2023/specification-and-sample-assessments/dfsq-l1-sam.pdf" target="_blank" rel="noopener" class="btn-hero-navy"><i class="fa-regular fa-file-pdf"></i> Download Level 1 SAM</a>
          <a href="#modules" class="btn-hero-outline"><i class="fa-solid fa-book"></i> Course Syllabus</a>
        </div>
      </div>

      <!-- Right Column: Real Photo Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/student-learning-online.jpg" alt="Student completing Level 1 digital coursework" style="height:230px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-shield-halved"></i></div>
            <div>
              <strong>Ofqual Level 1 Accreditation</strong>
              <span>Pearson Edexcel & City & Guilds Aligned</span>
            </div>
          </div>
        </div>

        <!-- Course Highlights Box -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:16px; padding:22px; box-shadow:var(--shadow-md);">
          <h4 style="margin:0 0 12px 0; font-size:1.1rem; color:var(--navy-dark);"><i class="fa-solid fa-box-open" style="color:var(--accent); margin-right:8px;"></i> What's Included:</h4>
          <ul style="list-style:none; padding:0; margin:0; font-size:0.88rem; display:flex; flex-direction:column; gap:8px;">
            <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 25+ Interactive video lessons across all 5 standards</li>
            <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Practice downloadable spreadsheet & document exercise files</li>
            <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 5 End-of-module assessment quizzes</li>
            <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> 2 Full-length timed mock exams with tutor feedback</li>
            <li><i class="fa-solid fa-check" style="color:var(--accent); margin-right:8px;"></i> Official Pearson Edexcel Level 1 Exam Booking Included</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- MODULE BY MODULE SYLLABUS -->
  <section class="mfs-directory-section" id="modules" style="padding:60px 0; background:#ffffff;">
    <div class="mfs-container">
      <div style="text-align:center; max-width:700px; margin:0 auto 40px auto;">
        <span style="color:var(--accent); font-weight:700; text-transform:uppercase; font-size:0.85rem; letter-spacing:0.05em;">Curriculum Syllabus</span>
        <h2 style="font-size:2rem; margin-top:6px; margin-bottom:12px;">Level 1 Course Modules</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Step-by-step training designed to take you from foundational understanding to autonomous competence.</p>
      </div>

      <div style="display:flex; flex-direction:column; gap:20px; max-width:960px; margin:0 auto;">
        <!-- Module 1 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); display:flex; gap:20px; align-items:flex-start;">
          <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
            <i class="fa-solid fa-laptop"></i>
          </div>
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <h3 style="font-size:1.15rem; margin:0;">Module 1: Devices and Handling Information</h3>
              <span style="font-size:0.8rem; background:rgba(0,184,124,0.12); color:var(--accent); padding:3px 10px; border-radius:12px; font-weight:700;">6 Lessons</span>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:10px;">
              System preferences, operating system utilities, organizing hierarchical folders, identifying file formats (.docx, .xlsx, .pdf, .zip), cloud file sync, and evaluating source copyright and accuracy.
            </p>
            <div style="font-size:0.82rem; color:var(--text-dark); display:flex; gap:16px; flex-wrap:wrap;">
              <span><i class="fa-solid fa-circle-play" style="color:var(--accent);"></i> Video Tutorials</span>
              <span><i class="fa-solid fa-file-arrow-down" style="color:var(--accent);"></i> Practice Exercise Files</span>
              <span><i class="fa-solid fa-square-check" style="color:var(--accent);"></i> Module 1 Quiz</span>
            </div>
          </div>
        </div>

        <!-- Module 2 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); display:flex; gap:20px; align-items:flex-start;">
          <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
            <i class="fa-solid fa-table-cells"></i>
          </div>
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <h3 style="font-size:1.15rem; margin:0;">Module 2: Creating and Editing with Spreadsheets & Documents</h3>
              <span style="font-size:0.8rem; background:rgba(0,184,124,0.12); color:var(--accent); padding:3px 10px; border-radius:12px; font-weight:700;">8 Lessons</span>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:10px;">
              Creating styled workplace reports, formatting typography, editing images, and mastering essential spreadsheet formulas: SUM, AVERAGE, COUNT, formatting currency/decimals, and generating bar charts.
            </p>
            <div style="font-size:0.82rem; color:var(--text-dark); display:flex; gap:16px; flex-wrap:wrap;">
              <span><i class="fa-solid fa-circle-play" style="color:var(--accent);"></i> Spreadsheet Walkthroughs</span>
              <span><i class="fa-solid fa-file-excel" style="color:var(--accent);"></i> 4 Downloadable Workbooks</span>
              <span><i class="fa-solid fa-square-check" style="color:var(--accent);"></i> Module 2 Quiz</span>
            </div>
          </div>
        </div>

        <!-- Module 3 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); display:flex; gap:20px; align-items:flex-start;">
          <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
            <i class="fa-solid fa-envelope-open-text"></i>
          </div>
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <h3 style="font-size:1.15rem; margin:0;">Module 3: Professional Communication & Collaboration</h3>
              <span style="font-size:0.8rem; background:rgba(0,184,124,0.12); color:var(--accent); padding:3px 10px; border-radius:12px; font-weight:700;">5 Lessons</span>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:10px;">
              Business email writing, CC and BCC protocols, managing file attachments within size limits, creating meeting invites on calendar apps, and managing public vs private sharing permissions.
            </p>
            <div style="font-size:0.82rem; color:var(--text-dark); display:flex; gap:16px; flex-wrap:wrap;">
              <span><i class="fa-solid fa-circle-play" style="color:var(--accent);"></i> Video Lessons</span>
              <span><i class="fa-solid fa-square-check" style="color:var(--accent);"></i> Module 3 Quiz</span>
            </div>
          </div>
        </div>

        <!-- Module 4 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); display:flex; gap:20px; align-items:flex-start;">
          <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
            <i class="fa-solid fa-credit-card"></i>
          </div>
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <h3 style="font-size:1.15rem; margin:0;">Module 4: Secure Digital Transactions</h3>
              <span style="font-size:0.8rem; background:rgba(0,184,124,0.12); color:var(--accent); padding:3px 10px; border-radius:12px; font-weight:700;">4 Lessons</span>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:10px;">
              Navigating online banking, filling in government & NHS digital portals, recognizing payment gateways, SSL/TLS certificates, consumer rights online, and verifying payment confirmations.
            </p>
            <div style="font-size:0.82rem; color:var(--text-dark); display:flex; gap:16px; flex-wrap:wrap;">
              <span><i class="fa-solid fa-circle-play" style="color:var(--accent);"></i> Interactive Form Practice</span>
              <span><i class="fa-solid fa-square-check" style="color:var(--accent);"></i> Module 4 Quiz</span>
            </div>
          </div>
        </div>

        <!-- Module 5 -->
        <div style="border:1px solid var(--border); border-radius:14px; padding:24px; background:var(--bg-card); display:flex; gap:20px; align-items:flex-start;">
          <div style="width:48px; height:48px; border-radius:12px; background:var(--accent-light); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
            <i class="fa-solid fa-user-shield"></i>
          </div>
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <h3 style="font-size:1.15rem; margin:0;">Module 5: Cybersecurity, Safety & Wellbeing</h3>
              <span style="font-size:0.8rem; background:rgba(0,184,124,0.12); color:var(--accent); padding:3px 10px; border-radius:12px; font-weight:700;">5 Lessons</span>
            </div>
            <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.6; margin-bottom:10px;">
              Generating strong passphrases, setting up Two-Factor Authentication (2FA), recognizing malware, social engineering and phishing emails, managing GDPR privacy settings, and workspace posture.
            </p>
            <div style="font-size:0.82rem; color:var(--text-dark); display:flex; gap:16px; flex-wrap:wrap;">
              <span><i class="fa-solid fa-circle-play" style="color:var(--accent);"></i> Threat Scenarios</span>
              <span><i class="fa-solid fa-square-check" style="color:var(--accent);"></i> Module 5 Quiz</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ENROLLMENT PRICING OPTIONS -->
  <section id="enroll" style="padding:60px 0; background:var(--bg-page); border-top:1px solid var(--border);">
    <div class="mfs-container">
      <div style="text-align:center; max-width:700px; margin:0 auto 40px auto;">
        <span class="top-badge-gold" style="display:inline-block; margin-bottom:10px;">Transparent Pricing</span>
        <h2 style="font-size:2rem; margin-bottom:10px;">Select Your Level 1 Digital Package</h2>
        <p style="color:var(--text-muted); font-size:0.95rem;">Choose the standalone exam or the all-inclusive course package with our pass guarantee.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px; max-width:850px; margin:0 auto;">
        <!-- Package 1: Standalone Exam -->
        <div style="background:#ffffff; border:1px solid var(--border); border-radius:16px; padding:32px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <span style="font-size:0.85rem; font-weight:700; color:var(--text-muted); text-transform:uppercase;">Exam Only</span>
            <h3 style="font-size:1.4rem; margin:6px 0 14px 0;">Level 1 Digital Exam</h3>
            <div style="font-size:2.2rem; font-weight:800; color:var(--navy-dark); margin-bottom:16px;">
              £149 <span style="font-size:0.9rem; font-weight:500; color:var(--text-muted);">one-off</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:20px;">
              For candidates who already have digital skills and only need the official Ofqual-regulated exam and certificate.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:10px;">
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Official Pearson Edexcel Level 1 Exam</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Online invigilation from home</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Fast results within 6–10 working days</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Ofqual accredited e-certificate</li>
            </ul>
          </div>
          <a href="functional-skills-exam.html" class="btn-hero-navy" style="width:100%; text-align:center; display:block;">Book Level 1 Exam (£149)</a>
        </div>

        <!-- Package 2: Course + Exam Pass Guarantee Bundle -->
        <div style="background:#ffffff; border:2px solid var(--accent); border-radius:16px; padding:32px; box-shadow:var(--shadow-lg); display:flex; flex-direction:column; justify-content:space-between; position:relative;">
          <div style="position:absolute; top:-12px; right:20px; background:var(--accent); color:#ffffff; font-size:0.75rem; font-weight:700; padding:4px 12px; border-radius:12px;">RECOMMENDED</div>
          <div>
            <span style="font-size:0.85rem; font-weight:700; color:var(--accent); text-transform:uppercase;">Course + Exam Bundle</span>
            <h3 style="font-size:1.4rem; margin:6px 0 14px 0;">Complete Pass Guarantee</h3>
            <div style="font-size:2.2rem; font-weight:800; color:var(--navy-dark); margin-bottom:16px;">
              £199 <span style="font-size:0.9rem; font-weight:500; color:var(--text-muted); text-decoration:line-through;">£279</span>
            </div>
            <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:20px;">
              Full comprehensive training, all 5 module video lessons, interactive practice exercises, mock exams, plus your official exam booking.
            </p>
            <ul style="list-style:none; padding:0; margin:0 0 24px 0; font-size:0.88rem; display:flex; flex-direction:column; gap:10px;">
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> <strong>Everything in Exam Only</strong></li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Full 28-lesson interactive video course</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> Downloadable practice spreadsheets & docs</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> 2 Full mock exams marked with tutor notes</li>
              <li><i class="fa-solid fa-circle-check" style="color:var(--accent); margin-right:8px;"></i> <strong>100% Pass Guarantee</strong> (Free resit if needed)</li>
            </ul>
          </div>
          <a href="functional-skills-courses.html" class="btn-hero-accent" style="width:100%; text-align:center; display:block;">Enroll Now (£199)</a>
        </div>
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>
"""

# Write out the files
hub_file = os.path.join(PROJECT_DIR, "digital-functional-skills.html")
with open(hub_file, "w", encoding="utf-8") as f:
    f.write(dfs_hub_html)
print(f"Generated {hub_file} ({len(dfs_hub_html)} bytes)")

l1_file = os.path.join(PROJECT_DIR, "digital-functional-skills-level-1.html")
with open(l1_file, "w", encoding="utf-8") as f:
    f.write(dfs_l1_html)
print(f"Generated {l1_file} ({len(dfs_l1_html)} bytes)")
