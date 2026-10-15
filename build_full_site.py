import os

BASE_DIR = '/home/subi/Projects/masterfunctionalskills.co.uk'

def get_header(title, description, active=''):
    active_attr = ' style="color:var(--mfs-green); font-weight:800;"'
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Master Functional Skills</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
  <!-- TOP TRUST BAR -->
  <div class="mfs-top-bar">
    <div class="mfs-container top-bar-content">
      <div class="trust-tags">
        <span class="trust-item"><i class="fa-solid fa-certificate"></i> Ofqual Regulated Qualifications</span>
        <span class="trust-item"><i class="fa-solid fa-shield-halved"></i> Pearson Edexcel, Open Awards & C&G Aligned</span>
      </div>
      <div class="top-contact">
        <a href="tel:020XXXXXXXX" class="top-link"><i class="fa-solid fa-phone"></i> <strong>020 XXXX XXXX</strong></a>
        <a href="https://wa.me/447564525425" target="_blank" rel="noopener" class="top-link"><i class="fa-brands fa-whatsapp"></i> <strong>+44 (0)7564 525425</strong></a>
        <a href="https://sterlingenglish.org" target="_blank" rel="noopener" class="top-link"><i class="fa-solid fa-graduation-cap"></i> 1-to-1 Specialist Tuition Practice ↗</a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <header class="mfs-header">
    <div class="mfs-container header-row">
      <a href="index.html" class="mfs-brand">
        <img src="assets/img/sterling-emblem-round.png" alt="Master Functional Skills Logo" class="brand-logo">
        <div class="brand-text">
          <span class="brand-name">MASTER FUNCTIONAL SKILLS</span>
          <span class="brand-tagline">UK's #1 Ofqual Regulated Courses, Exams & Revision</span>
        </div>
      </a>

      <nav class="mfs-nav-links">
        <a href="courses.html"{active_attr if active=='courses' else ''}>Courses & Classes</a>
        <a href="exams.html"{active_attr if active=='exams' else ''}>Book Online Exams</a>
        <a href="revise.html"{active_attr if active=='revise' else ''}>Revise Hub</a>
        <a href="shop.html"{active_attr if active=='shop' else ''}>Revision Cards & Shop</a>
        <a href="past-papers.html"{active_attr if active=='papers' else ''}>Free Past Papers</a>
        <a href="partnerships.html"{active_attr if active=='partnerships' else ''}>Colleges & Universities</a>
        <a href="about.html"{active_attr if active=='about' else ''}>Methodology</a>
      </nav>

      <div class="nav-cta-group">
        <a href="past-papers.html" class="btn-nav-outline">Free Diagnostic</a>
        <a href="exams.html" class="btn-nav-green">Book Level 2 Exam (£149)</a>
      </div>
    </div>
  </header>
'''

SHARED_FOOTER = '''
  <!-- FOOTER -->
  <footer class="mfs-footer">
    <div class="mfs-container">
      <div class="footer-grid">
        <div class="f-col brand-col">
          <div class="f-brand">
            <img src="assets/img/sterling-emblem-round.png" alt="Master Functional Skills" class="f-logo">
            <strong>MASTER FUNCTIONAL SKILLS</strong>
          </div>
          <p>The UK's specialist platform for Ofqual regulated Functional Skills Maths, English & Digital qualifications. Fully accredited alternative to GCSE Grade 4 / C.</p>
          <div class="trust-badge-box">
            <span class="trust-star">★★★★★</span> <strong>4.8 / 5 Rating</strong> (1,850+ Verified Reviews)
          </div>
          <p class="f-contact-note">💬 WhatsApp Enquiries: <a href="https://wa.me/447564525425" target="_blank" rel="noopener">+44 (0)7564 525425</a><br>📞 Office: <a href="tel:020XXXXXXXX">020 XXXX XXXX</a></p>
        </div>

        <div class="f-col">
          <h4>Online Exams</h4>
          <ul>
            <li><a href="exams.html">Maths Level 2 Online Exam</a></li>
            <li><a href="exams.html">English Level 2 Online Exam</a></li>
            <li><a href="exams.html">Dual Maths & English Bundle</a></li>
            <li><a href="exams.html">Level 1 Online Exams</a></li>
            <li><a href="exams.html">Entry Level 3 Exams</a></li>
            <li><a href="exams.html#test-centres">In-Person Test Centres (50+ Cities)</a></li>
          </ul>
        </div>

        <div class="f-col">
          <h4>Courses & Revise</h4>
          <ul>
            <li><a href="courses.html">Maths Level 2 Online Course</a></li>
            <li><a href="courses.html">English Level 2 Online Course</a></li>
            <li><a href="revise.html">Maths Revise Directory</a></li>
            <li><a href="revise.html">English Revise Directory</a></li>
            <li><a href="past-papers.html">Free Past Papers & Mark Schemes</a></li>
            <li><a href="shop.html">Pocket Revision Cards (£8.99)</a></li>
          </ul>
        </div>

        <div class="f-col">
          <h4>B2B & Universities</h4>
          <ul>
            <li><a href="partnerships.html">Universities & Degree Entry</a></li>
            <li><a href="partnerships.html#nursing">NHS Trusts & Nursing Gateways</a></li>
            <li><a href="partnerships.html#bksb">Free Alternative to BKSB / OneAdvanced</a></li>
            <li><a href="partnerships.html#itp">Apprenticeship Training Providers</a></li>
            <li><a href="partnerships.html#book-demo">Book a Corporate Demo</a></li>
            <li><a href="https://sterlingenglish.org" target="_blank" rel="noopener">1-to-1 Specialist Tuition Practice ↗</a></li>
          </ul>
        </div>

        <div class="f-col">
          <h4>Standards & Legal</h4>
          <ul>
            <li><a href="about.html">Our Educational Methodology</a></li>
            <li><a href="about.html#pass-guarantee">Pass Guarantee & Free Resit Policy</a></li>
            <li><a href="about.html#accreditation">Ofqual Regulation Framework</a></li>
            <li><a href="about.html#safeguarding">Safeguarding & Quality Assurance</a></li>
            <li><a href="index.html">Privacy Policy & Terms</a></li>
            <li><a href="index.html">Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="cert-logos">
          <span class="badge-accreditation">Ofqual Regulated</span>
          <span class="badge-accreditation">Pearson Edexcel Aligned</span>
          <span class="badge-accreditation">Open Awards Partner</span>
          <span class="badge-accreditation">City & Guilds Approved</span>
          <span class="badge-accreditation">TQUK Accredited</span>
        </div>
        <p class="copyright">© 2026 Master Functional Skills. All rights reserved. Functional Skills qualifications are regulated by Ofqual and equivalent to GCSE Grade 4/C.</p>
      </div>
    </div>
  </footer>
</body>
</html>
'''

# ==============================================================================
# 1. COURSES.HTML
# ==============================================================================
courses_body = '''
  <section class="mfs-hero" style="padding: 50px 0 40px; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
    <div class="mfs-container text-center" style="max-width: 860px; margin: 0 auto;">
      <span class="section-tag" style="background: #dcfce7; color: #16a34a;">100% ONLINE • SELF-PACED & ACCREDITED</span>
      <h1 style="font-size: 2.6rem; color: var(--mfs-navy); margin: 12px 0 16px; font-family: var(--font-heading); line-height: 1.2;">
        Functional Skills Online Courses (Level 1 & Level 2)
      </h1>
      <p style="font-size: 1.15rem; color: var(--mfs-gray); line-height: 1.6; margin-bottom: 24px;">
        Everything you need to pass your Ofqual regulated Maths and English exams on your first attempt. Built-in diagnostic assessment, video lessons, dynamic personal learning plan, and AI-marked mock exams.
      </p>
      <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
        <a href="#courses-grid" class="btn-hero-primary">Browse All Courses</a>
        <a href="past-papers.html" class="btn-hero-secondary">Take Free Initial Assessment</a>
      </div>
    </div>
  </section>

  <!-- FEATURES STRIP -->
  <section style="background: #ffffff; border-bottom: 1px solid var(--mfs-border); padding: 30px 0;">
    <div class="mfs-container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; text-align: center;">
        <div>
          <i class="fa-solid fa-brain" style="font-size: 2rem; color: var(--mfs-blue); margin-bottom: 8px;"></i>
          <h4 style="margin: 0 0 4px; font-size: 1.05rem; color: var(--mfs-navy);">Adaptive Diagnostics</h4>
          <p style="margin: 0; font-size: 0.88rem; color: var(--mfs-gray);">Pinpoints gaps and builds your custom pathway</p>
        </div>
        <div>
          <i class="fa-solid fa-circle-play" style="font-size: 2rem; color: var(--mfs-green); margin-bottom: 8px;"></i>
          <h4 style="margin: 0 0 4px; font-size: 1.05rem; color: var(--mfs-navy);">50+ Video Lessons</h4>
          <p style="margin: 0; font-size: 0.88rem; color: var(--mfs-gray);">Bite-sized micro-tutorials covering every topic</p>
        </div>
        <div>
          <i class="fa-solid fa-robot" style="font-size: 2rem; color: #9333ea; margin-bottom: 8px;"></i>
          <h4 style="margin: 0 0 4px; font-size: 1.05rem; color: var(--mfs-navy);">AI Mock Marking</h4>
          <p style="margin: 0; font-size: 0.88rem; color: var(--mfs-gray);">Instant marks and model solutions for essays & steps</p>
        </div>
        <div>
          <i class="fa-solid fa-chart-line" style="font-size: 2rem; color: #ea580c; margin-bottom: 8px;"></i>
          <h4 style="margin: 0 0 4px; font-size: 1.05rem; color: var(--mfs-navy);">Chance of Passing</h4>
          <p style="margin: 0; font-size: 0.88rem; color: var(--mfs-gray);">Real-time readiness index before sitting your exam</p>
        </div>
      </div>
    </div>
  </section>

  <!-- COURSES GRID -->
  <section class="mfs-section" id="courses-grid">
    <div class="mfs-container">
      <div class="section-head text-center" style="max-width: 760px; margin: 0 auto 40px;">
        <span class="section-tag">POPULAR COURSES</span>
        <h2 style="font-size: 2.2rem; color: var(--mfs-navy); margin: 10px 0;">Find Your Accredited Course</h2>
        <p style="color: var(--mfs-gray); font-size: 1.05rem;">Choose a standalone course or bundle with an official Ofqual regulated online exam.</p>
      </div>

      <div class="packages-grid">
        <!-- Maths L2 -->
        <div class="package-card featured">
          <div class="pkg-badge">MOST POPULAR</div>
          <div class="pkg-header">
            <h3>Maths Level 2 Complete Course</h3>
            <p class="pkg-sub">Equivalent to GCSE Grade 4 / C Maths</p>
            <div class="pkg-price">
              <span class="price-val">£284</span>
              <span class="price-period">/ 1-year access (or £99/mo)</span>
            </div>
            <div class="pkg-save">Save £71.00 (Was £355) • Exam Bundle available for £230</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> <strong>Initial & Diagnostic Baseline Test</strong></li>
              <li><i class="fa-solid fa-check"></i> Dynamic Personal Learning Plan (PLP)</li>
              <li><i class="fa-solid fa-check"></i> 39 Video Modules (Numbers, Shape, Data, Finance)</li>
              <li><i class="fa-solid fa-check"></i> 500+ Practice Questions with Step-by-Step Solutions</li>
              <li><i class="fa-solid fa-check"></i> 10 Full AI-Marked Mock Exam Papers</li>
              <li><i class="fa-solid fa-check"></i> Real-time "Chance of Passing" Tracker</li>
              <li><i class="fa-solid fa-check"></i> 100% Free Resit with Premium Exam Bundle</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20Maths%20Level%202%20Course" target="_blank" rel="noopener" class="btn-pkg">Enrol in Maths L2 Course →</a>
          </div>
        </div>

        <!-- English L2 -->
        <div class="package-card featured">
          <div class="pkg-badge">ESSENTIAL FOR NURSING & UNI</div>
          <div class="pkg-header">
            <h3>English Level 2 Complete Course</h3>
            <p class="pkg-sub">Equivalent to GCSE Grade 4 / C English Language</p>
            <div class="pkg-price">
              <span class="price-val">£284</span>
              <span class="price-period">/ 1-year access (or £99/mo)</span>
            </div>
            <div class="pkg-save">Save £71.00 (Was £355) • Exam Bundle available for £230</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> <strong>Initial & Subject Knowledge Assessment</strong></li>
              <li><i class="fa-solid fa-check"></i> Covers all 3 Components: Reading, Writing & SLC</li>
              <li><i class="fa-solid fa-check"></i> Punctuation, SPaG & Formal Letter/Report Writing</li>
              <li><i class="fa-solid fa-check"></i> Side-by-Side Model Answer Rewrites</li>
              <li><i class="fa-solid fa-check"></i> Instant AI Essay Feedback against Pearson & C&G bands</li>
              <li><i class="fa-solid fa-check"></i> Speaking & Listening Remote Preparation</li>
              <li><i class="fa-solid fa-check"></i> 100% Free Resit with Premium Exam Bundle</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20English%20Level%202%20Course" target="_blank" rel="noopener" class="btn-pkg">Enrol in English L2 Course →</a>
          </div>
        </div>

        <!-- Dual Maths & English Bundle -->
        <div class="package-card">
          <div class="pkg-badge" style="background:#0284c7;">BEST VALUE DUAL BUNDLE</div>
          <div class="pkg-header">
            <h3>Maths & English Level 2 Dual Course</h3>
            <p class="pkg-sub">Complete Double GCSE-Equivalent Pass System</p>
            <div class="pkg-price">
              <span class="price-val">£499</span>
              <span class="price-period">/ 1-year full access</span>
            </div>
            <div class="pkg-save">Save £211 vs purchasing separately!</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> <strong>Full Access to Both Maths L2 & English L2 Courses</strong></li>
              <li><i class="fa-solid fa-check"></i> Dual Personal Learning Plans</li>
              <li><i class="fa-solid fa-check"></i> 80+ Video Lessons across both subjects</li>
              <li><i class="fa-solid fa-check"></i> 20 AI-Marked Mock Exam Papers</li>
              <li><i class="fa-solid fa-check"></i> Free Physical Revision Flashcard Pack included (£17.98 value)</li>
              <li><i class="fa-solid fa-check"></i> Priority Tutor Marking on 2 Full Mock Papers</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20Dual%20Maths%20and%20English%20Course" target="_blank" rel="noopener" class="btn-pkg">Enrol in Dual Course (£499) →</a>
          </div>
        </div>

        <!-- Level 1 Foundation -->
        <div class="package-card">
          <div class="pkg-header">
            <h3>Functional Skills Level 1 Courses</h3>
            <p class="pkg-sub">Maths or English Level 1 (GCSE Grade 2–3 Equivalent)</p>
            <div class="pkg-price">
              <span class="price-val">£284</span>
              <span class="price-period">/ 1-year access</span>
            </div>
            <div class="pkg-save">Ideal stepping stone for apprenticeships</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> Complete Level 1 syllabus preparation</li>
              <li><i class="fa-solid fa-check"></i> Foundational arithmetic, fractions, decimals & measures</li>
              <li><i class="fa-solid fa-check"></i> Sentence structure, basic SPaG, and workplace emails</li>
              <li><i class="fa-solid fa-check"></i> Step-by-step video solutions</li>
              <li><i class="fa-solid fa-check"></i> Unlimited mock practice tests</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20Level%201%20Course" target="_blank" rel="noopener" class="btn-pkg">Enrol in Level 1 Course →</a>
          </div>
        </div>

        <!-- Entry Level 3 -->
        <div class="package-card">
          <div class="pkg-header">
            <h3>Entry Level 3 Foundation Courses</h3>
            <p class="pkg-sub">Maths or English Entry 3 (Confidence Building)</p>
            <div class="pkg-price">
              <span class="price-val">£184</span>
              <span class="price-period">/ 1-year access</span>
            </div>
            <div class="pkg-save">Save £46.00 (Was £230)</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> Core literacy and numeracy foundations</li>
              <li><i class="fa-solid fa-check"></i> Phonics, basic spelling, and simple reading</li>
              <li><i class="fa-solid fa-check"></i> Place value, times tables, and money calculations</li>
              <li><i class="fa-solid fa-check"></i> Dyslexia-friendly visual pacing</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20Entry%20Level%203%20Course" target="_blank" rel="noopener" class="btn-pkg">Enrol in Entry 3 (£184) →</a>
          </div>
        </div>

        <!-- Digital Skills L1 -->
        <div class="package-card">
          <div class="pkg-header">
            <h3>Digital Functional Skills (Level 1)</h3>
            <p class="pkg-sub">Modern Workplace Essential Qualification</p>
            <div class="pkg-price">
              <span class="price-val">£99</span>
              <span class="price-period">/ 1-year access</span>
            </div>
            <div class="pkg-save">Save £24.75 (Was £123.75)</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> Digital devices, file management & operating systems</li>
              <li><i class="fa-solid fa-check"></i> Word processing, spreadsheets & digital presentations</li>
              <li><i class="fa-solid fa-check"></i> Online safety, data privacy & cybersecurity basics</li>
              <li><i class="fa-solid fa-check"></i> Workplace digital communication (Email & Teams)</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20enrol%20in%20Digital%20Skills" target="_blank" rel="noopener" class="btn-pkg">Enrol in Digital Skills (£99) →</a>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

# ==============================================================================
# 2. EXAMS.HTML
# ==============================================================================
exams_body = '''
  <section class="mfs-hero" style="padding: 50px 0 40px; background: linear-gradient(180deg, #f0fdf4 0%, #e0f2fe 100%);">
    <div class="mfs-container text-center" style="max-width: 860px; margin: 0 auto;">
      <span class="section-tag" style="background: #16a34a; color: #ffffff;">OFQUAL REGULATED EXAM CENTRE</span>
      <h1 style="font-size: 2.6rem; color: var(--mfs-navy); margin: 12px 0 16px; font-family: var(--font-heading); line-height: 1.2;">
        Book Ofqual Regulated Functional Skills Exams (Sit from Home)
      </h1>
      <p style="font-size: 1.15rem; color: var(--mfs-gray); line-height: 1.6; margin-bottom: 24px;">
        Sit your official GCSE Grade 4 / C equivalent Functional Skills Maths or English exam 100% online from the comfort of your own home. Fast-track slots available 6 days a week, with verified results in 2 to 6 working days.
      </p>
      <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
        <a href="#exam-pricing" class="btn-hero-primary">View Exam Dates & Prices</a>
        <a href="#invigilation-modes" class="btn-hero-secondary">How Remote Invigilation Works</a>
      </div>
    </div>
  </section>

  <!-- EXAM PRICING TABLE -->
  <section class="mfs-section" id="exam-pricing">
    <div class="mfs-container">
      <div class="section-head text-center" style="max-width: 800px; margin: 0 auto 40px;">
        <span class="section-tag">INSTANT BOOKING</span>
        <h2 style="font-size: 2.2rem; color: var(--mfs-navy); margin: 10px 0;">Official Online Exam Bookings</h2>
        <p style="color: var(--mfs-gray); font-size: 1.05rem;">All exams are regulated by Ofqual, accredited on the Regulated Qualifications Framework (RQF), and accepted across UK Universities, the NHS, and Apprenticeships.</p>
      </div>

      <div class="packages-grid">
        <!-- Maths L2 Exam -->
        <div class="package-card featured">
          <div class="pkg-badge">POPULAR EXAM</div>
          <div class="pkg-header">
            <h3>Maths Level 2 Online Exam</h3>
            <p class="pkg-sub">100% Online • Ofqual Regulated</p>
            <div class="pkg-price">
              <span class="price-val">£149</span>
              <span class="price-period">promo rate (standard £229)</span>
            </div>
            <div class="pkg-save">Open Awards / TQUK accredited • 2-6 Day Results</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> <strong>Section A (Non-Calculator) & Section B (Calculator)</strong></li>
              <li><i class="fa-solid fa-check"></i> Sit online from home with remote invigilator</li>
              <li><i class="fa-solid fa-check"></i> Choose date now or book now & pick date later</li>
              <li><i class="fa-solid fa-check"></i> Official Ofqual e-certificate upon passing</li>
              <li><i class="fa-solid fa-check"></i> Add Course for £230 (Save £125)</li>
              <li><i class="fa-solid fa-shield"></i> Add Premium Bundle (+£125) for 1 FREE Resit</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20book%20the%20Maths%20Level%202%20Online%20Exam" target="_blank" rel="noopener" class="btn-pkg">Book Maths Exam (£149) →</a>
          </div>
        </div>

        <!-- English L2 Exam -->
        <div class="package-card featured">
          <div class="pkg-badge">HEALTHCARE & UNI GATEWAY</div>
          <div class="pkg-header">
            <h3>English Level 2 Online Exam</h3>
            <p class="pkg-sub">All 3 Components Included: Reading, Writing & SLC</p>
            <div class="pkg-price">
              <span class="price-val">£199</span>
              <span class="price-period">promo rate (standard £229)</span>
            </div>
            <div class="pkg-save">Accepted by all UK Nursing & Midwifery degrees</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> <strong>Reading Exam</strong> (1 hr 15 mins)</li>
              <li><i class="fa-solid fa-check"></i> <strong>Writing Exam</strong> (1 hr 20 mins)</li>
              <li><i class="fa-solid fa-check"></i> <strong>Speaking, Listening & Communicating (SLC)</strong> via Zoom</li>
              <li><i class="fa-solid fa-check"></i> Sit components back-to-back or split dates</li>
              <li><i class="fa-solid fa-check"></i> Official Ofqual certificate equivalent to GCSE English</li>
              <li><i class="fa-solid fa-shield"></i> Add Premium Bundle (+£125) for 1 FREE Resit</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20book%20the%20English%20Level%202%20Online%20Exam" target="_blank" rel="noopener" class="btn-pkg">Book English Exam (£199) →</a>
          </div>
        </div>

        <!-- Dual Exam Bundle -->
        <div class="package-card">
          <div class="pkg-badge" style="background:#0284c7;">DUAL QUALIFICATION</div>
          <div class="pkg-header">
            <h3>Maths & English L2 Dual Exam</h3>
            <p class="pkg-sub">Complete GCSE Equivalency Dual Pass</p>
            <div class="pkg-price">
              <span class="price-val">£349</span>
              <span class="price-period">bundled booking</span>
            </div>
            <div class="pkg-save">Save £49 compared to separate bookings</div>
          </div>
          <div class="pkg-body">
            <ul class="pkg-features">
              <li><i class="fa-solid fa-check"></i> Both Maths L2 & English L2 Official Exams</li>
              <li><i class="fa-solid fa-check"></i> Sit on flexible dates that suit your schedule</li>
              <li><i class="fa-solid fa-check"></i> Remote invigilation from home on PC/Mac/Chromebook</li>
              <li><i class="fa-solid fa-check"></i> Free diagnostic baseline test included</li>
              <li><i class="fa-solid fa-check"></i> Fast-track 2-6 working day turnaround</li>
            </ul>
          </div>
          <div class="pkg-footer">
            <a href="https://wa.me/447564525425?text=Hello,%20I%20want%20to%20book%20the%20Dual%20Maths%20and%20English%20Level%202%20Exam%20Bundle" target="_blank" rel="noopener" class="btn-pkg">Book Dual Bundle (£349) →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- THE £125 PREMIUM BUNDLE PROMO BOX -->
  <section style="background:#f8fafc; padding: 40px 0; border-top: 1px solid var(--mfs-border); border-bottom: 1px solid var(--mfs-border);">
    <div class="mfs-container">
      <div style="background: #ffffff; border: 2px solid var(--mfs-green); border-radius: 16px; padding: 36px; display: grid; grid-template-columns: 1fr auto; gap: 30px; align-items: center; box-shadow: 0 10px 25px rgba(22, 163, 74, 0.08);">
        <div>
          <span style="background: #dcfce7; color: #16a34a; font-weight: 800; font-size: 0.82rem; padding: 4px 12px; border-radius: 20px; text-transform: uppercase;">
            RECOMMENDED SAFETY NET
          </span>
          <h3 style="font-size: 1.8rem; color: var(--mfs-navy); margin: 10px 0 8px;">Upgrade to the Premium Pass Bundle (+£125)</h3>
          <p style="color: var(--mfs-gray); font-size: 1.02rem; line-height: 1.6; margin: 0 0 14px;">
            Eliminate exam anxiety with guaranteed retake protection. When you upgrade your exam booking to the Premium Bundle, you receive:
          </p>
          <ul style="margin: 0; padding-left: 20px; color: #334155; line-height: 1.8; font-size: 0.95rem;">
            <li><strong>1 Free Exam Resit</strong> included if you do not pass on your first attempt (saves £149–£229 out-of-pocket).</li>
            <li><strong>Complete Physical Exam Pack</strong> delivered to your door (workbook, worked models, 2 printed mock papers — worth £119.99).</li>
            <li><strong>Free 1-to-1 Specialist Tutor Remediation Session</strong> if you miss the pass mark before retaking.</li>
          </ul>
        </div>
        <div style="text-align: center; min-width: 240px;">
          <div style="font-size: 2.2rem; font-weight: 800; color: var(--mfs-navy); margin-bottom: 4px;">+£125</div>
          <div style="font-size: 0.85rem; color: var(--mfs-gray); margin-bottom: 16px;">One-off upgrade fee</div>
          <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20book%20an%20exam%20with%20the%20Premium%20Pass%20Bundle" target="_blank" rel="noopener" class="btn-pkg" style="width: 100%; display: block; text-align: center;">Add to Booking →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW REMOTE INVIGILATION WORKS -->
  <section class="mfs-section" id="invigilation-modes">
    <div class="mfs-container">
      <div class="section-head text-center" style="max-width: 800px; margin: 0 auto 40px;">
        <span class="section-tag">REMOTE PROCTORING</span>
        <h2 style="font-size: 2.2rem; color: var(--mfs-navy); margin: 10px 0;">How Your At-Home Online Exam Works</h2>
        <p style="color: var(--mfs-gray); font-size: 1.05rem;">We offer two accredited online examination formats depending on your technical setup and preferences.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
        <!-- Open Awards 1-on-1 -->
        <div style="background: #ffffff; border: 1px solid var(--mfs-border); border-radius: 14px; padding: 30px;">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            <div style="width: 44px; height: 44px; background: #e0f2fe; color: #0284c7; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">
              <i class="fa-solid fa-user-tie"></i>
            </div>
            <div>
              <h3 style="margin: 0; font-size: 1.25rem; color: var(--mfs-navy);">1-to-1 Live Human Invigilation</h3>
              <span style="font-size: 0.82rem; color: #0284c7; font-weight: 700;">Open Awards Certified</span>
            </div>
          </div>
          <p style="color: var(--mfs-gray); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
            A friendly human invigilator connects with you via Zoom to verify your ID, check your room environment, and guide you through the initial setup before your exam begins.
          </p>
          <ul style="margin: 0; padding-left: 20px; font-size: 0.9rem; color: #334155; line-height: 1.7;">
            <li>Compatible with <strong>PC, Mac, and Chromebooks</strong>.</li>
            <li>Ideal for candidates who appreciate human reassurance.</li>
            <li>Results delivered within 6 to 16 working days.</li>
          </ul>
        </div>

        <!-- TQUK Fast Track -->
        <div style="background: #ffffff; border: 1px solid var(--mfs-border); border-radius: 14px; padding: 30px;">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            <div style="width: 44px; height: 44px; background: #dcfce7; color: #16a34a; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">
              <i class="fa-solid fa-bolt"></i>
            </div>
            <div>
              <h3 style="margin: 0; font-size: 1.25rem; color: var(--mfs-navy);">Fast-Track Remote Proctoring</h3>
              <span style="font-size: 0.82rem; color: #16a34a; font-weight: 700;">TQUK / Saras System</span>
            </div>
          </div>
          <p style="color: var(--mfs-gray); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
            Asynchronous secure browser testing. Your webcam, audio, and screen are recorded and reviewed by compliance examiners, enabling 24/7 on-demand scheduling.
          </p>
          <ul style="margin: 0; padding-left: 20px; font-size: 0.9rem; color: #334155; line-height: 1.7;">
            <li><strong>Fastest results in the UK:</strong> Verified results in 2 to 6 working days.</li>
            <li>Guaranteed 2-day turnaround add-on available.</li>
            <li>Requires Windows PC or Laptop with webcam.</li>
          </ul>
        </div>
      </div>

      <!-- IN-PERSON TEST CENTRES -->
      <div id="test-centres" style="margin-top: 50px; background: #f8fafc; border-radius: 16px; padding: 36px; border: 1px solid var(--mfs-border);">
        <h3 style="font-size: 1.5rem; color: var(--mfs-navy); margin: 0 0 10px;">Prefer to sit in person? In-Person Test Centre Network (50+ Cities)</h3>
        <p style="color: var(--mfs-gray); font-size: 0.98rem; line-height: 1.6; margin-bottom: 18px;">
          If you prefer a physical exam room over testing from home, we partner with accredited testing centres across England, Wales, Scotland, and Northern Ireland:
        </p>
        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
          <span class="topic-badge badge-core">London</span>
          <span class="topic-badge badge-core">Birmingham</span>
          <span class="topic-badge badge-core">Manchester</span>
          <span class="topic-badge badge-core">Leeds</span>
          <span class="topic-badge badge-core">Bristol</span>
          <span class="topic-badge badge-core">Cardiff</span>
          <span class="topic-badge badge-core">Edinburgh</span>
          <span class="topic-badge badge-core">Belfast</span>
          <span class="topic-badge badge-core">Newcastle</span>
          <span class="topic-badge badge-core">Sheffield</span>
          <span class="topic-badge badge-core">Liverpool</span>
          <span class="topic-badge badge-core">Oxford</span>
          <span class="topic-badge badge-core">+ 40 More</span>
        </div>
        <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20book%20an%20in-person%20Functional%20Skills%20exam%20centre" target="_blank" rel="noopener" class="btn-hero-primary" style="display: inline-block;">Enquire for Physical Test Centre →</a>
      </div>
    </div>
  </section>
'''

# ==============================================================================
# 3. SHOP.HTML
# ==============================================================================
shop_body = '''
  <section class="mfs-hero" style="padding: 50px 0 40px; background: linear-gradient(180deg, #fff7ed 0%, #ffedd5 100%);">
    <div class="mfs-container text-center" style="max-width: 860px; margin: 0 auto;">
      <span class="section-tag" style="background: #ea580c; color: #ffffff;">REVISION STORE</span>
      <h1 style="font-size: 2.6rem; color: var(--mfs-navy); margin: 12px 0 16px; font-family: var(--font-heading); line-height: 1.2;">
        Functional Skills Revision Cards, Practice Papers & Books
      </h1>
      <p style="font-size: 1.15rem; color: var(--mfs-gray); line-height: 1.6; margin-bottom: 24px;">
        Accelerate your revision with our physical flashcard decks, board-tailored mock exam paper packs, and comprehensive topic workbooks. Free UK Royal Mail dispatch.
      </p>
    </div>
  </section>

  <!-- SHOP GRID -->
  <section class="mfs-section">
    <div class="mfs-container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <!-- Product 1: Maths Cards -->
        <div class="shop-card">
          <div class="shop-img-box">
            <span class="shop-badge">BESTSELLER</span>
            <i class="fa-solid fa-calculator" style="font-size: 4rem; color: #0284c7;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">Flashcards Deck</span>
            <h3>Maths Level 2 Revision Cards</h3>
            <p>Pocket-sized flashcards covering all 39 Level 2 Maths topics, key formulas, quick conversions, and visual method tricks.</p>
            <div class="shop-price-row">
              <span class="shop-price">£8.99</span>
              <span class="shop-old-price">£11.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20Maths%20Level%202%20Revision%20Cards%20(£8.99)" target="_blank" rel="noopener" class="btn-shop">Order Now (£8.99) →</a>
          </div>
        </div>

        <!-- Product 2: English Cards -->
        <div class="shop-card">
          <div class="shop-img-box">
            <span class="shop-badge">BESTSELLER</span>
            <i class="fa-solid fa-pen-nib" style="font-size: 4rem; color: #16a34a;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">Flashcards Deck</span>
            <h3>English Level 2 Revision Cards</h3>
            <p>Master formal letter layouts, PEEL paragraphs, apostrophe rules, eliminating comma splices, and persuasive techniques.</p>
            <div class="shop-price-row">
              <span class="shop-price">£8.99</span>
              <span class="shop-old-price">£11.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20English%20Level%202%20Revision%20Cards%20(£8.99)" target="_blank" rel="noopener" class="btn-shop">Order Now (£8.99) →</a>
          </div>
        </div>

        <!-- Product 3: Practice Papers -->
        <div class="shop-card">
          <div class="shop-img-box">
            <span class="shop-badge" style="background:#0284c7;">BOARD-SPECIFIC</span>
            <i class="fa-solid fa-file-invoice" style="font-size: 4rem; color: #ea580c;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">5 Full Mock Sets</span>
            <h3>Level 2 Practice Papers & Mark Schemes</h3>
            <p>5 authentic printed practice test papers tailored specifically to your chosen exam board (Pearson Edexcel, City & Guilds, Open Awards, or NCFE).</p>
            <div class="shop-price-row">
              <span class="shop-price">£29.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20Level%202%20Practice%20Papers%20(£29.99)" target="_blank" rel="noopener" class="btn-shop">Order Papers (£29.99) →</a>
          </div>
        </div>

        <!-- Product 4: Bundle Cards + Papers -->
        <div class="shop-card">
          <div class="shop-img-box">
            <span class="shop-badge" style="background:#9333ea;">POPULAR BUNDLE</span>
            <i class="fa-solid fa-box-open" style="font-size: 4rem; color: #9333ea;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">Bundle (Save 10%)</span>
            <h3>Practice Papers & Cards Bundle</h3>
            <p>5 printed mock test papers with mark schemes PLUS the complete pocket revision flashcard deck for your chosen subject.</p>
            <div class="shop-price-row">
              <span class="shop-price">£37.99</span>
              <span class="shop-old-price">£41.98</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20Papers%20and%20Cards%20Bundle%20(£37.99)" target="_blank" rel="noopener" class="btn-shop">Order Bundle (£37.99) →</a>
          </div>
        </div>

        <!-- Product 5: Workbook -->
        <div class="shop-card">
          <div class="shop-img-box">
            <i class="fa-solid fa-book" style="font-size: 4rem; color: #475569;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">Comprehensive Workbook</span>
            <h3>Maths Level 2 Worksheets by Topic</h3>
            <p>Comprehensive ring-bound workbook featuring hundreds of exam-style practice questions organized topic-by-topic with full mark schemes.</p>
            <div class="shop-price-row">
              <span class="shop-price">£34.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20Maths%20Level%202%20Workbook%20(£34.99)" target="_blank" rel="noopener" class="btn-shop">Order Workbook (£34.99) →</a>
          </div>
        </div>

        <!-- Product 6: Complete Exam Pack Box -->
        <div class="shop-card">
          <div class="shop-img-box">
            <span class="shop-badge" style="background:#e11d48;">PREMIUM BOX</span>
            <i class="fa-solid fa-gift" style="font-size: 4rem; color: #e11d48;"></i>
          </div>
          <div class="shop-body">
            <span class="shop-tag">Complete Physical Pack</span>
            <h3>Functional Skills Level 2 Exam Pack</h3>
            <p>The ultimate revision box: Complete revision guide, full topic workbook, 2 printed mock exams, and pen kit delivered to your home.</p>
            <div class="shop-price-row">
              <span class="shop-price">£119.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20order%20the%20Complete%20Exam%20Pack%20Box%20(£119.99)" target="_blank" rel="noopener" class="btn-shop">Order Exam Pack (£119.99) →</a>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

# ==============================================================================
# 4. PARTNERSHIPS.HTML (Universities, NHS, Colleges & BKSB)
# ==============================================================================
partnerships_body = '''
  <section class="mfs-hero" style="padding: 50px 0 40px; background: linear-gradient(180deg, #eff6ff 0%, #dbeafe 100%);">
    <div class="mfs-container text-center" style="max-width: 880px; margin: 0 auto;">
      <span class="section-tag" style="background: #0284c7; color: #ffffff;">INSTITUTIONAL & B2B DELIVERY</span>
      <h1 style="font-size: 2.6rem; color: var(--mfs-navy); margin: 12px 0 16px; font-family: var(--font-heading); line-height: 1.2;">
        Functional Skills for Universities, NHS Trusts & Training Providers
      </h1>
      <p style="font-size: 1.15rem; color: var(--mfs-gray); line-height: 1.6; margin-bottom: 24px;">
        Turnkey qualification delivery, free diagnostic baseline assessments (zero-cost BKSB / OneAdvanced alternative), ESFA/Ofsted compliance reporting, and high-volume remote exam invigilation.
      </p>
      <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
        <a href="#book-demo" class="btn-hero-primary">Book a Corporate Demo</a>
        <a href="#bksb" class="btn-hero-secondary">Free Alternative to BKSB / OneAdvanced</a>
      </div>
    </div>
  </section>

  <!-- BKSB ALTERNATIVE SECTION -->
  <section class="mfs-section" id="bksb" style="background: #ffffff;">
    <div class="mfs-container">
      <div style="background: #f8fafc; border: 2px solid #0284c7; border-radius: 16px; padding: 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
        <div>
          <span style="background: #e0f2fe; color: #0284c7; font-weight: 800; font-size: 0.82rem; padding: 4px 12px; border-radius: 20px; text-transform: uppercase;">
            FREE INSTITUTIONAL SOFTWARE
          </span>
          <h2 style="font-size: 2.2rem; color: var(--mfs-navy); margin: 12px 0 14px;">The Free Alternative to BKSB / OneAdvanced</h2>
          <p style="color: var(--mfs-gray); font-size: 1.02rem; line-height: 1.6; margin-bottom: 16px;">
            Stop paying expensive per-learner licence fees. Master Functional Skills provides FE colleges and Independent Training Providers (ITPs) with a completely free, Ofqual-aligned Initial Assessment and Subject Knowledge Diagnostic platform.
          </p>
          <ul style="margin: 0 0 20px; padding-left: 20px; color: #334155; line-height: 1.8; font-size: 0.95rem;">
            <li><strong>£0 Licence Fees:</strong> Zero cost for initial assessments or diagnostic tests.</li>
            <li><strong>ESFA Audit Ready:</strong> Instant export of learner baseline and prior learning evidence.</li>
            <li><strong>Ofsted Distance Travelled:</strong> Clear progress tracking from diagnostic baseline to exam pass.</li>
            <li><strong>OneFile Integration:</strong> Directly export learner evidence into your e-portfolio system.</li>
          </ul>
          <a href="#book-demo" class="btn-hero-primary">Request Free Provider Portal Access →</a>
        </div>
        <div style="background: #ffffff; border: 1px solid var(--mfs-border); border-radius: 12px; padding: 24px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
          <h4 style="margin: 0 0 14px; color: var(--mfs-navy); font-size: 1.1rem; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px;">
            Comparison: MasterFunctionalSkills vs BKSB / OneAdvanced
          </h4>
          <table style="width: 100%; font-size: 0.9rem; border-collapse: collapse;">
            <thead>
              <tr style="border-bottom: 2px solid #edf2f7; text-align: left;">
                <th style="padding: 8px 4px;">Feature</th>
                <th style="padding: 8px 4px; color: var(--mfs-green);">MasterFunctionalSkills</th>
                <th style="padding: 8px 4px; color: #e11d48;">BKSB / OneAdvanced</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid #f1f5f9;">
                <td style="padding: 8px 4px;">Licence Cost</td>
                <td style="padding: 8px 4px; font-weight: 700; color: var(--mfs-green);">FREE (£0)</td>
                <td style="padding: 8px 4px; color: #e11d48;">£15–£25 per seat</td>
              </tr>
              <tr style="border-bottom: 1px solid #f1f5f9;">
                <td style="padding: 8px 4px;">Diagnostic Assessment</td>
                <td style="padding: 8px 4px; color: var(--mfs-green);">Included (Free)</td>
                <td style="padding: 8px 4px;">Included (Paid)</td>
              </tr>
              <tr style="border-bottom: 1px solid #f1f5f9;">
                <td style="padding: 8px 4px;">Integrated Online Exams</td>
                <td style="padding: 8px 4px; color: var(--mfs-green);">Yes (On-demand)</td>
                <td style="padding: 8px 4px; color: #e11d48;">No (Software only)</td>
              </tr>
              <tr style="border-bottom: 1px solid #f1f5f9;">
                <td style="padding: 8px 4px;">Turnaround Time</td>
                <td style="padding: 8px 4px; color: var(--mfs-green);">2–6 Working Days</td>
                <td style="padding: 8px 4px;">Board dependent</td>
              </tr>
              <tr>
                <td style="padding: 8px 4px;">Dyslexia Optimization</td>
                <td style="padding: 8px 4px; color: var(--mfs-green);">Built-in high-contrast</td>
                <td style="padding: 8px 4px;">Standard UI</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- UNIVERSITY PROGRESSION & NHS SECTION -->
  <section class="mfs-section" id="nursing" style="background: #f8fafc;">
    <div class="mfs-container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 40px;">
        <!-- NHS -->
        <div style="background: #ffffff; border-radius: 14px; padding: 30px; border: 1px solid var(--mfs-border);">
          <div style="width: 50px; height: 50px; background: #e0f2fe; color: #0284c7; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 16px;">
            <i class="fa-solid fa-hospital"></i>
          </div>
          <h3 style="font-size: 1.4rem; color: var(--mfs-navy); margin: 0 0 10px;">NHS Trusts & Healthcare Assistants (HCAs)</h3>
          <p style="color: var(--mfs-gray); font-size: 0.95rem; line-height: 1.6; margin-bottom: 14px;">
            Solve the 12-hour rotational shift challenge. Our 24/7 on-demand exam slots allow Healthcare Assistants, Band 2/3 clinical staff, and Nursing Associates to sit Functional Skills exams around ward schedules.
          </p>
          <ul style="margin: 0; padding-left: 20px; font-size: 0.9rem; color: #334155; line-height: 1.7;">
            <li>Fast-tracks Nursing Degree Apprenticeship gateways.</li>
            <li>Satisfies Nursing and Midwifery Council (NMC) Level 2 entry criteria.</li>
            <li>Cohort dashboard for Trust Apprenticeship Lead monitoring.</li>
          </ul>
        </div>

        <!-- Universities -->
        <div style="background: #ffffff; border-radius: 14px; padding: 30px; border: 1px solid var(--mfs-border);">
          <div style="width: 50px; height: 50px; background: #dcfce7; color: #16a34a; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 16px;">
            <i class="fa-solid fa-university"></i>
          </div>
          <h3 style="font-size: 1.4rem; color: var(--mfs-navy); margin: 0 0 10px;">Universities & Conditional Offer Clearances</h3>
          <p style="color: var(--mfs-gray); font-size: 0.95rem; line-height: 1.6; margin-bottom: 14px;">
            Partner with UK admissions teams to clear conditional offers for prospective students needing GCSE Grade 4 / C equivalencies in Maths or English prior to autumn enrolment.
          </p>
          <ul style="margin: 0; padding-left: 20px; font-size: 0.9rem; color: #334155; line-height: 1.7;">
            <li>Accepted for BSc Nursing, Midwifery, Social Work, and Paramedic Science.</li>
            <li>Direct result verification letters provided within 48 hours to admissions offices.</li>
            <li>High completion pass rate ensures maximum student intake retention.</li>
          </ul>
        </div>
      </div>

      <!-- LEAD CAPTURE FORM -->
      <div id="book-demo" style="background: #ffffff; border: 1px solid var(--mfs-border); border-radius: 16px; padding: 40px; max-width: 760px; margin: 0 auto; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
        <div class="text-center" style="margin-bottom: 24px;">
          <h3 style="font-size: 1.8rem; color: var(--mfs-navy); margin: 0 0 8px;">Book a Corporate Demo / Partnership Consultation</h3>
          <p style="color: var(--mfs-gray); margin: 0;">Speak with our Academic Partnerships Director to arrange free provider portal access or cohort pricing.</p>
        </div>
        <form onsubmit="event.preventDefault(); window.open('https://wa.me/447564525425?text=' + encodeURIComponent('Hello, I am interested in an institutional partnership for: ' + document.getElementById('b2bOrg').value + ' (' + document.getElementById('b2bType').value + ')'), '_blank');">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; color:#334155; margin-bottom:6px;">Your Name</label>
              <input type="text" id="b2bName" required style="width:100%; padding:10px 14px; border:1px solid #cbd5e1; border-radius:8px; font-size:0.95rem;">
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; color:#334155; margin-bottom:6px;">Work Email</label>
              <input type="email" id="b2bEmail" required style="width:100%; padding:10px 14px; border:1px solid #cbd5e1; border-radius:8px; font-size:0.95rem;">
            </div>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; color:#334155; margin-bottom:6px;">Organisation / Trust / College Name</label>
              <input type="text" id="b2bOrg" required style="width:100%; padding:10px 14px; border:1px solid #cbd5e1; border-radius:8px; font-size:0.95rem;">
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; color:#334155; margin-bottom:6px;">Institution Type</label>
              <select id="b2bType" style="width:100%; padding:10px 14px; border:1px solid #cbd5e1; border-radius:8px; font-size:0.95rem;">
                <option value="FE College">FE College / Sixth Form</option>
                <option value="Independent Training Provider (ITP)">Apprenticeship Training Provider (ITP)</option>
                <option value="NHS Trust">NHS Trust / Healthcare Provider</option>
                <option value="University">University Admissions Department</option>
                <option value="Corporate Employer">Corporate Employer</option>
              </select>
            </div>
          </div>
          <button type="submit" class="btn-hero-primary" style="width:100%; border:none; cursor:pointer; font-size:1.05rem; padding:14px;">
            Submit Partnership Enquiry & Schedule Demo →
          </button>
        </form>
      </div>
    </div>
  </section>
'''

# ==============================================================================
# 5. ABOUT.HTML (Methodology, Standards & Pass Guarantee)
# ==============================================================================
about_body = '''
  <section class="mfs-hero" style="padding: 50px 0 40px; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
    <div class="mfs-container text-center" style="max-width: 860px; margin: 0 auto;">
      <span class="section-tag" style="background: #e0f2fe; color: #0284c7;">ACADEMIC EXCELLENCE & OFQUAL RIGOUR</span>
      <h1 style="font-size: 2.6rem; color: var(--mfs-navy); margin: 12px 0 16px; font-family: var(--font-heading); line-height: 1.2;">
        Our Educational Methodology & Pass Guarantee
      </h1>
      <p style="font-size: 1.15rem; color: var(--mfs-gray); line-height: 1.6; margin-bottom: 24px;">
        Designed specifically for adult learners, healthcare professionals, and apprentices. Combining adaptive diagnostic technology with specialist 1-to-1 pedagogical interventions.
      </p>
    </div>
  </section>

  <!-- 4-STAGE LEARNING CYCLE -->
  <section class="mfs-section">
    <div class="mfs-container">
      <div class="section-head text-center" style="max-width: 780px; margin: 0 auto 40px;">
        <span class="section-tag">PROVEN SYSTEM</span>
        <h2 style="font-size: 2.2rem; color: var(--mfs-navy); margin: 10px 0;">The MasterFunctionalSkills Mastery Framework</h2>
        <p style="color: var(--mfs-gray); font-size: 1.05rem;">How our learners consistently achieve a High First-Time Pass Rate.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px;">
        <div style="background:#ffffff; border:1px solid var(--mfs-border); border-radius:14px; padding:28px;">
          <div style="width:40px; height:40px; background:#e0f2fe; color:#0284c7; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.2rem; margin-bottom:14px;">1</div>
          <h4 style="margin:0 0 8px; color:var(--mfs-navy); font-size:1.15rem;">Diagnostic Baseline</h4>
          <p style="margin:0; font-size:0.92rem; color:var(--mfs-gray); line-height:1.6;">
            Adaptive Initial Assessment pinpoints exact curriculum strengths and knowledge gaps against DfE and Ofqual national standards.
          </p>
        </div>

        <div style="background:#ffffff; border:1px solid var(--mfs-border); border-radius:14px; padding:28px;">
          <div style="width:40px; height:40px; background:#dcfce7; color:#16a34a; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.2rem; margin-bottom:14px;">2</div>
          <h4 style="margin:0 0 8px; color:var(--mfs-navy); font-size:1.15rem;">Dynamic Personal Plan</h4>
          <p style="margin:0; font-size:0.92rem; color:var(--mfs-gray); line-height:1.6;">
            Generates a customized study roadmap. Mastered topics are bypassed; deficit skills are front-loaded with micro-video lessons and drills.
          </p>
        </div>

        <div style="background:#ffffff; border:1px solid var(--mfs-border); border-radius:14px; padding:28px;">
          <div style="width:40px; height:40px; background:#fef3c7; color:#d97706; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.2rem; margin-bottom:14px;">3</div>
          <h4 style="margin:0 0 8px; color:var(--mfs-navy); font-size:1.15rem;">3-Section Feedback Loop</h4>
          <p style="margin:0; font-size:0.92rem; color:var(--mfs-gray); line-height:1.6;">
            Side-by-side error highlighting (yellow for student slip; green for model benchmark) paired with tutor review cards and extension tasks.
          </p>
        </div>

        <div style="background:#ffffff; border:1px solid var(--mfs-border); border-radius:14px; padding:28px;">
          <div style="width:40px; height:40px; background:#f3e8ff; color:#9333ea; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.2rem; margin-bottom:14px;">4</div>
          <h4 style="margin:0 0 8px; color:var(--mfs-navy); font-size:1.15rem;">ExamReady Invigilation</h4>
          <p style="margin:0; font-size:0.92rem; color:var(--mfs-gray); line-height:1.6;">
            Predictive readiness scoring confirms when a learner has ≥90% probability of passing before booking remote Ofqual invigilation.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- PASS GUARANTEE TRANSPARENCY -->
  <section class="mfs-section bg-light" id="pass-guarantee">
    <div class="mfs-container">
      <div style="background:#ffffff; border:2px solid var(--mfs-green); border-radius:16px; padding:40px; max-width:840px; margin:0 auto;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:16px;">
          <i class="fa-solid fa-shield-halved" style="font-size:2.4rem; color:var(--mfs-green);"></i>
          <div>
            <h3 style="margin:0; font-size:1.8rem; color:var(--mfs-navy);">Our "No-Loophole" Transparent Pass Guarantee</h3>
            <span style="color:var(--mfs-green); font-weight:700; font-size:0.95rem;">Clear Criteria • 100% Free Resits • Human Tutor Support</span>
          </div>
        </div>
        <p style="color:var(--mfs-gray); font-size:1.02rem; line-height:1.6; margin-bottom:18px;">
          Unlike competitors who bury restrictive clauses in terms and conditions (such as restricting retakes to a single component or disclaiming responsibility for outcomes), MasterFunctionalSkills stands behind every learner:
        </p>
        <div style="background:#f0fdf4; border-left:4px solid var(--mfs-green); padding:18px 22px; border-radius:8px; margin-bottom:20px;">
          <h4 style="margin:0 0 8px; color:#166534; font-size:1.05rem;">How to Qualify:</h4>
          <ol style="margin:0; padding-left:20px; color:#1e3a2b; line-height:1.7; font-size:0.95rem;">
            <li>Complete 100% of your identified Personal Learning Plan (PLP) modules.</li>
            <li>Score ≥75% on at least 3 practice mock papers.</li>
            <li>Achieve an ExamReady Index of ≥85%.</li>
          </ol>
        </div>
        <p style="color:#334155; line-height:1.7; margin-bottom:0;">
          <strong>What happens if you don't pass?</strong> We provide a <strong>100% Free Resit</strong> across all failed components PLUS an automated <strong>45-minute 1-to-1 diagnostic coaching session</strong> with our lead specialist tutor to review your exam paper script before re-sitting.
        </p>
      </div>
    </div>
  </section>
'''

pages = [
    ('courses.html', 'Functional Skills Courses (Level 1 & Level 2 Online)', 'Accredited Functional Skills Maths and English online courses. Self-paced, video tutorials, AI-marked mock exams.', 'courses', courses_body),
    ('exams.html', 'Book Online Functional Skills Exams (Ofqual Regulated)', 'Sit your official Functional Skills Maths or English Level 2 exam online from home. Fast-track results in 2-6 days.', 'exams', exams_body),
    ('shop.html', 'Functional Skills Revision Cards, Practice Papers & Shop', 'Order pocket revision cards, 5-mock exam paper packs with mark schemes, and complete study workbooks. Free UK delivery.', 'shop', shop_body),
    ('partnerships.html', 'Functional Skills for Universities, NHS Trusts & Colleges', 'Institutional delivery, free BKSB / OneAdvanced alternative diagnostic software, ESFA audit compliance, and remote exam proctoring.', 'partnerships', partnerships_body),
    ('about.html', 'Our Educational Methodology & Transparent Pass Guarantee', 'Learn how our diagnostic baseline, 3-section model feedback, and transparent pass guarantee deliver a high pass rate.', 'about', about_body),
]

for filename, title, desc, active, body in pages:
    filepath = os.path.join(BASE_DIR, filename)
    full_html = get_header(title, desc, active) + body + SHARED_FOOTER
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generated {filename} successfully ({len(full_html)} bytes).')

print('All clone subpages generated successfully.')

