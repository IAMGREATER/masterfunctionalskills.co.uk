import os
from generate_modern_services_pages import PROJECT_DIR, NAV_HEADER, FOOTER

def generate_maths_and_english_hub():
    html = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Maths and English | Master Functional Skills</title>
  <meta name="description" content="Official Ofqual-regulated Functional Skills Maths and English Level 2 & Level 1 qualifications. GCSE Grade 4/C equivalent accepted for university, nursing, police, and apprenticeships.">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png">
  <link rel="apple-touch-icon" href="assets/img/favicon-192x192.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <style>
    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2.5rem 0;
      background: #ffffff;
      border-radius: 12px;
      border: 1px solid var(--border-color, #e2e8f0);
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }}
    .comp-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}
    .comp-table th, .comp-table td {{
      padding: 16px 20px;
      border-bottom: 1px solid #e2e8f0;
      font-size: 0.95rem;
    }}
    .comp-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #0f172a;
    }}
    .comp-table th.highlight-col, .comp-table td.highlight-col {{
      background: rgba(14, 165, 233, 0.06);
      font-weight: 600;
      color: #0369a1;
    }}
    .badge-check {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #059669;
      font-weight: 600;
    }}
    .badge-cross {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #dc2626;
      font-weight: 500;
    }}
    .hub-grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 2rem;
    }}
    .hub-feature-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .hub-feature-box:hover {{
      transform: translateY(-4px);
      box-shadow: 0 10px 20px -3px rgba(0,0,0,0.08);
      border-color: #0284c7;
    }}
    .hub-feature-box .icon-wrap {{
      width: 52px;
      height: 52px;
      border-radius: 10px;
      background: #e0f2fe;
      color: #0284c7;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      margin-bottom: 16px;
    }}
    .hub-feature-box h3 {{
      font-size: 1.25rem;
      margin-bottom: 10px;
      color: #0f172a;
    }}
    .hub-feature-box p {{
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.55;
      margin-bottom: 20px;
      flex-grow: 1;
    }}
    .faq-list {{
      max-width: 860px;
      margin: 2rem auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      overflow: hidden;
    }}
    .faq-question {{
      padding: 18px 20px;
      font-weight: 600;
      font-size: 1.05rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }}
    .faq-question:hover {{
      background: #f8fafc;
    }}
    .faq-answer {{
      padding: 0 20px 18px 20px;
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.6;
    }}
  </style>
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <div class="hero-badge"><i class="fa-solid fa-graduation-cap"></i> Ofqual Regulated GCSE Grade 4/C Equivalent</div>
        <h1>Functional Skills <span>Maths and English</span></h1>
        <p class="hero-description">
          The UK's trusted pathway to GCSE equivalence. Secure the qualifications you need for university entry, nursing degrees, teaching credentials, police recruitment, and apprenticeship gateway completion without taking 2-year school GCSEs.
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
          <a href="functional-skills-courses.html" class="btn-hero-accent"><i class="fa-solid fa-book-open"></i> Explore Courses</a>
          <a href="functional-skills-exam.html" class="btn-hero-navy"><i class="fa-solid fa-laptop"></i> Book Online Exam</a>
          <a href="diagnostic-test.html" class="btn-hero-outline"><i class="fa-solid fa-chart-line"></i> Free Diagnostic</a>
        </div>
      </div>

      <div class="hero-visual">
        <div class="hero-stat-card">
          <div class="stat-badge"><i class="fa-solid fa-award"></i> Recognized Nationwide</div>
          <div class="stat-main">Level 2 = GCSE Grade C/4</div>
          <p class="stat-sub">Valid for UCAS, NHS England, Department for Education, and UK employers.</p>
          <div class="stat-pillars">
            <div class="pillar-item">
              <i class="fa-solid fa-calculator" style="color:#0284c7;"></i>
              <div>
                <strong>Maths L2 &amp; L1</strong>
                <span>Non-calc &amp; Calculator</span>
              </div>
            </div>
            <div class="pillar-item">
              <i class="fa-solid fa-feather-pointed" style="color:#059669;"></i>
              <div>
                <strong>English L2 &amp; L1</strong>
                <span>Reading, Writing &amp; SLC</span>
              </div>
            </div>
            <div class="pillar-item">
              <i class="fa-solid fa-bolt" style="color:#eab308;"></i>
              <div>
                <strong>Fast Track Results</strong>
                <span>6 to 10 Working Days</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- KEY PATHWAYS SECTION -->
  <section class="mfs-section bg-light" id="pathways">
    <div class="mfs-container">
      <div class="section-header-center">
        <span class="badge-subtitle">Why Take Functional Skills</span>
        <h2>Open Doors to Higher Education &amp; Career Growth</h2>
        <p>Functional Skills qualifications are designed for real-world application, offering a fast, stress-free route to meeting UK gateway criteria.</p>
      </div>

      <div class="hub-grid-3">
        <!-- Card 1 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap"><i class="fa-solid fa-user-doctor"></i></div>
            <h3>University &amp; Healthcare</h3>
            <p>Meet strict university entry requirements for BSc Nursing, Midwifery, Social Work, Paramedic Science, and Primary Teaching degrees across UK universities.</p>
          </div>
          <a href="functional-skills-exam.html" class="btn-card-action">Book University Exam →</a>
        </div>

        <!-- Card 2 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#ecfdf5; color:#059669;"><i class="fa-solid fa-briefcase"></i></div>
            <h3>Career Progression</h3>
            <p>Boost your CV and qualify for promotions in the NHS (Agenda for Change Bands 3-7), Police Constable Entry Programme (PCEP), Civil Service, and corporate roles.</p>
          </div>
          <a href="functional-skills-courses.html" class="btn-card-action">View Online Courses →</a>
        </div>

        <!-- Card 3 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#fef3c7; color:#d97706;"><i class="fa-solid fa-certificate"></i></div>
            <h3>Apprenticeship Gateways</h3>
            <p>Most UK Level 3, 4, and Degree Apprenticeships require Level 2 in Maths and English before you can reach the End-Point Assessment (EPA) gateway.</p>
          </div>
          <a href="diagnostic-test.html" class="btn-card-action">Take Free Diagnostic →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- QUALIFICATION COMPARISON -->
  <section class="mfs-section">
    <div class="mfs-container">
      <div class="section-header-center">
        <span class="badge-subtitle">Comparison</span>
        <h2>Functional Skills vs Traditional GCSE</h2>
        <p>Why hundreds of thousands of adult learners choose Functional Skills over retaking school GCSEs.</p>
      </div>

      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th style="width:30%;">Feature</th>
              <th class="highlight-col" style="width:35%;">Functional Skills Level 2 (MFS)</th>
              <th style="width:35%;">Traditional GCSE (Retake)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>GCSE Grade Equivalent</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> Official Grade C / Grade 4 Equivalent</span></td>
              <td>Grade 4 (Standard Pass) or above</td>
            </tr>
            <tr>
              <td><strong>Typical Study Time</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> 2 to 8 weeks (Self-paced)</span></td>
              <td><span class="badge-cross"><i class="fa-solid fa-xmark"></i> 9 months to 2 academic years</span></td>
            </tr>
            <tr>
              <td><strong>Exam Availability</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> Year-round, Monday to Saturday on-demand</span></td>
              <td><span class="badge-cross"><i class="fa-solid fa-xmark"></i> Fixed dates only (May/June &amp; Nov)</span></td>
            </tr>
            <tr>
              <td><strong>Exam Location</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> Online from home (remote invigilation)</span></td>
              <td><span class="badge-cross"><i class="fa-solid fa-xmark"></i> Physical exam centre attendance</span></td>
            </tr>
            <tr>
              <td><strong>Results Turnaround</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> 6 to 10 working days</span></td>
              <td><span class="badge-cross"><i class="fa-solid fa-xmark"></i> 8 to 10 weeks (August results day)</span></td>
            </tr>
            <tr>
              <td><strong>Content Focus</strong></td>
              <td class="highlight-col"><span class="badge-check"><i class="fa-solid fa-check"></i> Practical everyday workplace maths &amp; communication</span></td>
              <td>Abstract academic literature &amp; theoretical algebra</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- QUICK NAVIGATION TO REVISION DIRECTORIES -->
  <section class="mfs-section bg-light">
    <div class="mfs-container">
      <div class="section-header-center">
        <span class="badge-subtitle">Learning Hubs</span>
        <h2>Explore Our Complete Subject Directories</h2>
        <p>Each directory contains comprehensive curriculum tables, practice worksheets, answer keys, video masterclasses, and exam-level topic tests.</p>
      </div>

      <div class="hub-grid-3">
        <!-- Maths L2 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap"><i class="fa-solid fa-calculator"></i></div>
            <h3>Maths Level 2</h3>
            <p>39 structured topics covering fractions, decimals, percentages, ratio, area, perimeter, volume, probability, mean, median, range, and scatter diagrams.</p>
          </div>
          <a href="functional-skills-maths-level-2.html" class="btn-card-action">Go to Maths Level 2 Directory →</a>
        </div>

        <!-- English L2 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#ecfdf5; color:#059669;"><i class="fa-solid fa-pen-nib"></i></div>
            <h3>English Level 2</h3>
            <p>35 topics covering Reading analysis, organizational devices, biases, tone, practical writing formats (articles, speeches, reports, emails), and punctuation rules.</p>
          </div>
          <a href="functional-skills-english-level-2.html" class="btn-card-action">Go to English Level 2 Directory →</a>
        </div>

        <!-- Maths L1 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#fef3c7; color:#d97706;"><i class="fa-solid fa-square-root-variable"></i></div>
            <h3>Maths Level 1</h3>
            <p>38 core foundation topics to build fundamental confidence before progressing to Level 2. Full worked examples and step-by-step guidance.</p>
          </div>
          <a href="functional-skills-maths-level-1.html" class="btn-card-action">Go to Maths Level 1 Directory →</a>
        </div>

        <!-- English L1 -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#f3e8ff; color:#7c3aed;"><i class="fa-solid fa-book-open-reader"></i></div>
            <h3>English Level 1</h3>
            <p>33 foundation modules covering sentence structures, spelling rules, punctuation conventions, format features, and reading comprehension techniques.</p>
          </div>
          <a href="functional-skills-english-level-1.html" class="btn-card-action">Go to English Level 1 Directory →</a>
        </div>

        <!-- Entry 3 Maths -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#e0f2fe; color:#0369a1;"><i class="fa-solid fa-shapes"></i></div>
            <h3>Entry Level 3 Maths</h3>
            <p>24 confidence-building modules covering place value, rounding, four operations, money calculations, simple time, units, and simple charts.</p>
          </div>
          <a href="entry-level-3-maths.html" class="btn-card-action">Go to Entry 3 Maths Directory →</a>
        </div>

        <!-- Digital Skills -->
        <div class="hub-feature-box">
          <div>
            <div class="icon-wrap" style="background:#ffe4e6; color:#e11d48;"><i class="fa-solid fa-laptop-code"></i></div>
            <h3>Digital Functional Skills</h3>
            <p>Essential digital skills for life and work: online safety, device configuration, searching the internet, creating digital documents, and communication tools.</p>
          </div>
          <a href="digital-functional-skills.html" class="btn-card-action">Go to Digital Skills Hub →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQS -->
  <section class="mfs-section">
    <div class="mfs-container">
      <div class="section-header-center">
        <span class="badge-subtitle">Common Questions</span>
        <h2>Frequently Asked Questions</h2>
        <p>Everything you need to know about Functional Skills Maths and English.</p>
      </div>

      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-question">
            <span>Is Functional Skills Level 2 genuinely equivalent to a GCSE?</span>
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            Yes. Functional Skills Level 2 is officially recognised by Ofqual (the Office of Qualifications and Examinations Regulation) as equivalent to a GCSE grade 4 or grade C. It is accepted by UK universities, UCAS, NHS trusts, police forces, colleges, and national employers.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>Can I take both Maths and English exams online from home?</span>
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            Yes. Both Maths and English exams can be sat online from home using secure remote invigilation. All you need is a computer or laptop with a working webcam, microphone, and a stable broadband internet connection.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>How fast can I get my official certificate?</span>
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            Official exam results are released within 6 to 10 working days of sitting your exam. Once results are confirmed, your official e-certificate and printed certificate are dispatched promptly.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            <span>What if I have dyslexia or require extra time?</span>
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            Our platform features built-in dyslexia tints (Cream, Soft Peach, Cool Mist, Soft Sage) and dyslexia-friendly typography. If you have a formal diagnosis or evidence of special educational needs, we can arrange reasonable adjustments (e.g. 25% extra time) with the awarding exam board.
          </div>
        </div>
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""
    out_path = os.path.join(PROJECT_DIR, "functional-skills-maths-and-english.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_maths_and_english_hub()
