import os

BASE_DIR = '/home/subi/Projects/masterfunctionalskills.co.uk'

SHARED_HEAD = '''<!DOCTYPE html>
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
        <a href="courses.html"{active_courses}>Courses & Classes</a>
        <a href="exams.html"{active_exams}>Book Online Exams</a>
        <a href="revise.html"{active_revise}>Revise Hub</a>
        <a href="shop.html"{active_shop}>Revision Cards & Shop</a>
        <a href="past-papers.html"{active_papers}>Free Past Papers</a>
        <a href="partnerships.html"{active_partnerships}>Colleges & Universities</a>
        <a href="about.html"{active_about}>Methodology</a>
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

print('Generator base components defined.')
EOF
