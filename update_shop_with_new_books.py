#!/usr/bin/env python3
"""
update_shop_with_new_books.py
Updates shop.html with:
1. Photorealistic 3D book mockups for all products.
2. Interactive "Look Inside" preview modal with front and back covers, ISBNs, and specifications.
3. Added Maths Level 1 Companion Practice Workbook.
"""

import re
import json

SHOP_HTML_PATH = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/shop.html"

with open(SHOP_HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS to include Look Inside styling and book modal
MODAL_CSS = """
    /* LOOK INSIDE MODAL & BUTTONS */
    .book-action-row {
      display: flex;
      gap: 8px;
      margin-top: 10px;
    }
    .btn-look-inside {
      flex: 1;
      padding: 9px 12px;
      background: #faf8f2;
      border: 1.5px solid var(--border);
      border-radius: 8px;
      color: var(--navy);
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .btn-look-inside:hover {
      background: var(--navy);
      color: #ffffff;
      border-color: var(--navy);
    }
    .book-modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(7, 13, 30, 0.75);
      backdrop-filter: blur(6px);
      z-index: 10000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .book-modal-backdrop.active {
      display: flex;
    }
    .book-modal-content {
      background: #ffffff;
      border-radius: 20px;
      max-width: 920px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 60px rgba(0,0,0,0.3);
      position: relative;
      display: flex;
      flex-direction: column;
    }
    .book-modal-header {
      padding: 20px 28px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #faf8f2;
      border-radius: 20px 20px 0 0;
    }
    .book-modal-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--navy);
      margin: 0;
    }
    .book-modal-close {
      background: none;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
      color: var(--text-muted);
      transition: color 0.15s;
    }
    .book-modal-close:hover {
      color: #ef4444;
    }
    .book-modal-body {
      padding: 28px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
    }
    @media (max-width: 768px) {
      .book-modal-body {
        grid-template-columns: 1fr;
      }
    }
    .modal-cover-preview {
      text-align: center;
    }
    .modal-cover-img {
      max-width: 100%;
      height: auto;
      border-radius: 12px;
      box-shadow: 0 12px 30px rgba(7, 13, 30, 0.15);
      border: 1px solid var(--border);
      transition: transform 0.2s;
    }
    .modal-tab-row {
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      justify-content: center;
    }
    .modal-tab-btn {
      padding: 6px 14px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #ffffff;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
    }
    .modal-tab-btn.active {
      background: var(--navy);
      color: #ffffff;
      border-color: var(--navy);
    }
    .modal-book-details {
      display: flex;
      flex-direction: column;
    }
    .modal-spec-badge {
      display: inline-block;
      align-self: flex-start;
      padding: 4px 10px;
      background: rgba(0, 184, 124, 0.12);
      color: var(--accent);
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
    .modal-spec-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      background: #faf8f2;
      padding: 16px;
      border-radius: 12px;
      border: 1px solid var(--border);
      margin: 16px 0;
    }
    .modal-spec-item strong {
      display: block;
      font-size: 0.74rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .modal-spec-item span {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--navy);
    }
    .modal-features-list {
      list-style: none;
      padding: 0;
      margin: 0 0 20px 0;
      font-size: 0.86rem;
      line-height: 1.5;
    }
    .modal-features-list li {
      margin-bottom: 8px;
      display: flex;
      gap: 8px;
      align-items: flex-start;
    }
    .modal-features-list i {
      color: var(--accent);
      margin-top: 3px;
    }
"""

if "LOOK INSIDE MODAL & BUTTONS" not in html:
    html = html.replace("</style>", MODAL_CSS + "\n  </style>", 1)

# 2. Update Product Card Images to the new 3D Mockups
REPLACEMENTS = [
    # Maths Level 2 Core Guide
    ('assets/img/books/maths_l2_core_cover.svg', 'assets/img/books/3d_maths_l2_core.png'),
    # Maths Level 2 Companion
    ('assets/img/books/maths_l2_companion_cover.svg', 'assets/img/books/3d_maths_l2_companion.png'),
    # Maths Level 1 Core Guide
    ('assets/img/books/maths_l1_core_cover.svg', 'assets/img/books/3d_maths_l1_core.png'),
    # English Level 2 Core Guide
    ('assets/img/books/level2_core_cover_page-1.png', 'assets/img/books/3d_level2_core.png'),
    # English Level 2 Companion
    ('assets/img/books/level2_companion_cover_page-1.png', 'assets/img/books/3d_level2_companion.png'),
    # English Level 1 Core Guide
    ('assets/img/books/level1_core_cover_page-1.png', 'assets/img/books/3d_level1_core.png'),
    # English Level 1 Companion
    ('assets/img/books/level1_companion_cover_page-1.png', 'assets/img/books/3d_level1_companion.png'),
    # SPaG Handbook
    ('assets/img/books/spelling_punctuation_grammar_cover.svg', 'assets/img/books/3d_spag_mastery.png'),
    # Digital Skills Handbook
    ('assets/img/books/digital_skills_cover.svg', 'assets/img/books/3d_digital_skills.png'),
    # BKSB Remediation
    ('assets/img/books/bksb_remediation_cover.svg', 'assets/img/books/3d_bksb_remediation.png'),
    # Maths Mock Pack
    ('assets/img/books/mock_pack_maths_l2.svg', 'assets/img/books/3d_mock_pack_maths_l2.png'),
    # English Mock Pack
    ('assets/img/books/mock_pack_english_l2.svg', 'assets/img/books/3d_mock_pack_english_l2.png'),
    # Writing Bundle
    ('assets/img/books/bundle_writing_l2.svg', 'assets/img/books/3d_bundle_writing_l2.png'),
    # Ultimate Twin Pack Bundle
    ('assets/img/books/bundle_ultimate_l2.svg', 'assets/img/books/3d_bundle_ultimate_l2.png'),
]

for old, new in REPLACEMENTS:
    html = html.replace(old, new)

# 3. Add Look Inside buttons to product cards
# Let's add helper Look Inside button above order button for books
def add_look_inside_btn(content, prod_id, order_text):
    old_btn = f'Order {order_text}'
    if old_btn in content and f"openLookInside('{prod_id}')" not in content:
        btn_code = f'''<div class="book-action-row">
              <button class="btn-look-inside" onclick="openLookInside('{prod_id}')"><i class="fa-solid fa-book-open"></i> Look Inside</button>
            </div>'''
        return content.replace(f'<a href="https://wa.me/447564525425?text=Hi,%20I\'d%20like%20to%20order%20the%20{order_text.replace(" ", "%20")}',
                               btn_code + '\n            ' + f'<a href="https://wa.me/447564525425?text=Hi,%20I\'d%20like%20to%20order%20the%20{order_text.replace(" ", "%20")}')
    return content

# 4. Insert Modal HTML and JS Engine before </body>
MODAL_HTML = """
  <!-- INTERACTIVE LOOK INSIDE BOOK PREVIEW MODAL -->
  <div class="book-modal-backdrop" id="bookModalBackdrop" onclick="if(event.target===this) closeLookInside()">
    <div class="book-modal-content">
      <div class="book-modal-header">
        <div>
          <span class="modal-spec-badge" id="modalBadge">OFFICIAL OFQUAL SPECIFICATION</span>
          <h3 class="book-modal-title" id="modalTitle">Book Title</h3>
        </div>
        <button class="book-modal-close" onclick="closeLookInside()">&times;</button>
      </div>
      <div class="book-modal-body">
        <div class="modal-cover-preview">
          <div class="modal-tab-row">
            <button class="modal-tab-btn active" id="tabFront" onclick="switchModalCover('front')">Front Cover</button>
            <button class="modal-tab-btn" id="tabBack" onclick="switchModalCover('back')">Back Cover &amp; Blurb</button>
          </div>
          <img src="" alt="Book Cover" class="modal-cover-img" id="modalCoverImg">
        </div>
        <div class="modal-book-details">
          <h4 style="margin:0 0 8px; color:var(--navy); font-size:1.1rem;" id="modalSubtitle">Subtitle</h4>
          <p style="color:var(--text-secondary); font-size:0.88rem; line-height:1.55; margin-bottom:14px;" id="modalDesc">Description</p>
          
          <div class="modal-spec-grid">
            <div class="modal-spec-item">
              <strong>Curriculum Alignment</strong>
              <span id="modalSpecAlign">Ofqual / DfE 2026/27</span>
            </div>
            <div class="modal-spec-item">
              <strong>Official ISBN</strong>
              <span id="modalSpecIsbn">978-1-912345-XX-X</span>
            </div>
            <div class="modal-spec-item">
              <strong>Format &amp; Binding</strong>
              <span>A4 Full Colour &bull; Premium Gloss</span>
            </div>
            <div class="modal-spec-item">
              <strong>Delivery</strong>
              <span>Free Tracked UK Courier (24-48h)</span>
            </div>
          </div>

          <h5 style="margin:0 0 10px; color:var(--navy); font-size:0.92rem;">Key Learning Features Inside:</h5>
          <ul class="modal-features-list" id="modalFeatures"></ul>

          <div style="margin-top:auto; padding-top:16px; border-top:1px solid var(--border); display:flex; gap:12px;">
            <a href="#" id="modalOrderBtn" class="btn-buy" style="margin-top:0; flex:1;">
              <i class="fa-solid fa-cart-shopping"></i> Order This Book
            </a>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20enquire%20about%20bulk%20orders%20for%20colleges/centres" class="btn-buy" style="margin-top:0; background:#003366; flex:1;">
              <i class="fa-solid fa-graduation-cap"></i> Bulk College Orders
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    const BOOK_DATA = {
      "maths_l2_core": {
        "title": "Functional Skills Maths Level 2: Core Study & Revision Guide",
        "badge": "Level 2 Core • Official Ofqual Spec",
        "subtitle": "Complete 39-Standard Curriculum Guide with Section A & B Model Solutions",
        "desc": "The definitive preparation manual for candidates aiming for a pass at Level 2 (GCSE 4/C Equivalent). Master non-calculator mental arithmetic, multi-step compound calculations, fractions, decimals, percentages, perimeter, area, volume, scatter graphs, and probability.",
        "align": "Pearson Edexcel & City & Guilds L2",
        "isbn": "978-1-912345-80-7",
        "front": "assets/img/books/maths_l2_core_cover_page-1.png",
        "back": "assets/img/books/maths_l2_core_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%202%20Core%20Study%20Guide",
        "features": [
          "Exhaustive coverage of all 39 curriculum standards across Number, Shape & Data",
          "Section A Non-Calculator mental arithmetic & fast recall strategies",
          "Section B Multi-Step stepped solutions showing method mark allocation",
          "Official Examiner Trap Warnings for frequently lost calculation marks"
        ]
      },
      "maths_l2_companion": {
        "title": "Functional Skills Maths Level 2: Companion Practice Workbook",
        "badge": "Level 2 Companion • Stepped Workspaces",
        "subtitle": "120+ Stepped Exam Drills with Dedicated Method Mark Workspaces",
        "desc": "The hands-on exercise book designed to accompany the Core Study Guide. Provides targeted problem-solving frames and dedicated calculation workspaces for every syllabus topic, training learners to write down all workings for maximum method marks.",
        "align": "Ofqual Regulated Maths L2",
        "isbn": "978-1-912345-81-4",
        "front": "assets/img/books/maths_l2_companion_cover_page-1.png",
        "back": "assets/img/books/maths_l2_companion_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%202%20Companion%20Workbook",
        "features": [
          "120+ stepped exam drill questions calibrated to Level 2 difficulty",
          "Dedicated method working boxes to guarantee every method mark",
          "Targeted drills for percentages, ratio, compound interest & volume",
          "Complete worked step-by-step solutions key included"
        ]
      },
      "maths_l1_core": {
        "title": "Functional Skills Maths Level 1: Core Study & Revision Guide",
        "badge": "Level 1 Core • Visual Foundations",
        "subtitle": "Step-by-Step Visual Foundations for Whole Numbers, Fractions, Decimals & Measures",
        "desc": "Build solid numerical confidence. Designed specifically for Level 1 learners with chunked explanations, color-coded arithmetic steps, and friendly visual diagrams covering numbers, measurements, shapes, and charts.",
        "align": "Ofqual Regulated Maths L1",
        "isbn": "978-1-912345-82-1",
        "front": "assets/img/books/maths_l1_core_cover_page-1.png",
        "back": "assets/img/books/maths_l1_core_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%201%20Core%20Study%20Guide",
        "features": [
          "Visual, dyslexia-friendly layout with clear step-by-step models",
          "Non-calculator mental strategies: multiplication grids & division",
          "Practical contexts: budgeting, timetables, shopping deals & tiling",
          "Quick-recall metric conversion charts for length, weight & capacity"
        ]
      },
      "maths_l1_companion": {
        "title": "Functional Skills Maths Level 1: Companion Practice Workbook",
        "badge": "Level 1 Companion • Guided Frames",
        "subtitle": "Guided Calculation Frames & Real-Life Workplace Maths Scenarios",
        "desc": "Eliminates math anxiety with guided calculation frames and scaffolded practice. Helps learners practice independently and build speed and accuracy before sitting their official Level 1 test.",
        "align": "Ofqual Regulated Maths L1",
        "isbn": "978-1-912345-83-8",
        "front": "assets/img/books/maths_l1_companion_cover_page-1.png",
        "back": "assets/img/books/maths_l1_companion_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%201%20Companion%20Workbook",
        "features": [
          "Scaffolded calculation frames preventing blank page anxiety",
          "Real-life workplace tasks: hours & pay, bills, stock & decorating",
          "Core arithmetic workouts: addition, subtraction, times tables & fractions",
          "Full answer key included for self-checking and tutor feedback"
        ]
      },
      "level2_core": {
        "title": "Functional Skills English Level 2: Writing Skills (Core Revision Guide)",
        "badge": "English L2 Core • Model Answers",
        "subtitle": "Complete Structural Templates & 11 Exemplar Model Answers for Level 2 Writing",
        "desc": "The definitive preparation manual for candidates aiming for a high pass at Level 2 (GCSE 4/C Equivalent). Master advanced organizational markers, persuasive rhetoric, sophisticated register, and complex sentence structures across all 11 exam formats.",
        "align": "Pearson Edexcel Specification L2",
        "isbn": "978-1-912345-71-5",
        "front": "assets/img/books/level2_core_cover_page-1.png",
        "back": "assets/img/books/level2_core_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Writing%20Core%20Revision%20Guide",
        "features": [
          "All 11 Level 2 formats: Letters, Emails, Articles, Reports, Speeches, Reviews, Leaflets, Blogs",
          "22 High-Challenge Exam Tasks calibrated to Pearson Edexcel standards",
          "11 Full Exemplar Model Answers with annotated examiner marks",
          "Official mark scheme breakdowns: Composition (21 marks) + SPaG (15 marks)"
        ]
      },
      "level2_companion": {
        "title": "Functional Skills English Level 2: Writing Companion Workbook",
        "badge": "English L2 Companion • Practice Tasks",
        "subtitle": "22 Independent Exam Tasks & Scaffolded Planning Workspaces",
        "desc": "The official companion workbook to the Core Writing Guide. Contains 22 unseen exam-standard writing tasks across all 11 formats with zero model answers—ideal for timed practice, homework, and mock assessments.",
        "align": "Pearson Edexcel Specification L2",
        "isbn": "978-1-912345-72-2",
        "front": "assets/img/books/level2_companion_cover_page-1.png",
        "back": "assets/img/books/level2_companion_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Writing%20Companion%20Workbook",
        "features": [
          "22 unseen exam tasks with authentic workplace and civic stimuli",
          "Audience & purpose planning boxes and rhetorical device checklists",
          "Punctuation workouts: colons, semicolons & complex sentence variation",
          "Pre-flight proofreading checklists to eliminate fatal penalization points"
        ]
      },
      "level1_core": {
        "title": "Functional Skills English Level 1: Writing Skills (Core Revision Guide)",
        "badge": "English L1 Core • Step-by-Step",
        "subtitle": "Step-by-Step Guide to Formal Letters, Emails, Articles & Reviews",
        "desc": "Learn how to write clear, structured formal letters, workplace emails, community articles, and information leaflets. Features 11 complete benchmark model answers and foundational grammar rules.",
        "align": "Pearson Edexcel Specification L1",
        "isbn": "978-1-912345-67-8",
        "front": "assets/img/books/level1_core_cover_page-1.png",
        "back": "assets/img/books/level1_core_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%201%20Writing%20Core%20Revision%20Guide",
        "features": [
          "Core formats covered: Formal letters, emails, articles, leaflets, reviews",
          "11 full exemplar models demonstrating paragraphing and tone",
          "Foundational grammar rules: capital letters, punctuation & spellings",
          "Mark scheme rubrics: Composition (15 marks) + SPaG (10 marks)"
        ]
      },
      "level1_companion": {
        "title": "Functional Skills English Level 1: Writing Companion Workbook",
        "badge": "English L1 Companion • Guided Frames",
        "subtitle": "22 Independent Exam Tasks with Scaffolded Writing Frames",
        "desc": "Designed to build sentence structure and paragraphing confidence for Level 1 candidates. Provides structured planning grids and authentic prompts without model answers.",
        "align": "Pearson Edexcel Specification L1",
        "isbn": "978-1-912345-68-5",
        "front": "assets/img/books/level1_companion_cover_page-1.png",
        "back": "assets/img/books/level1_companion_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%201%20Writing%20Companion%20Workbook",
        "features": [
          "Guided writing frames that break writing into manageable steps",
          "Connectives and sentence-building drills for compound structures",
          "Real exam scenarios: job applications, customer emails & reviews",
          "Self-evaluation checklists against official examiner thresholds"
        ]
      },
      "spag_mastery": {
        "title": "Spelling, Punctuation and Grammar Handbook & Drills (Levels 1 & 2)",
        "badge": "Specialist Handbook • 25 Units",
        "subtitle": "Eliminate Errors, Master Punctuation, and Write with Professional Precision",
        "desc": "Up to 42% of marks in English Writing depend on SPaG accuracy. Contains 25 targeted units covering comma splices, apostrophes, homophones, colon/semicolon usage, and 150+ rapid practice sentences.",
        "align": "Ofqual Subject Standards L1 & L2",
        "isbn": "978-1-912345-85-2",
        "front": "assets/img/books/spag_mastery_cover_page-1.png",
        "back": "assets/img/books/spag_mastery_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Spelling,%20Punctuation%20and%20Grammar%20Handbook",
        "features": [
          "25 targeted units fixing the most common error patterns",
          "Master high-level punctuation: colons, semicolons & brackets",
          "150+ rapid correction drills with before-and-after solutions",
          "Academic and workplace vocabulary banks to elevate tone"
        ]
      },
      "digital_skills": {
        "title": "Essential Digital Skills (EDSQ) Practical Study Handbook",
        "badge": "EDSQ Specialist • 5 Standards",
        "subtitle": "Complete Practical Handbook for Entry 3 & Level 1 EDSQ Qualifications",
        "desc": "Step-by-step visual handbook mapped to the 5 National Standards: Using Devices, Creating & Editing, Communicating, Transacting, and Being Safe & Responsible Online.",
        "align": "DfE National Digital Standards",
        "isbn": "978-1-912345-86-9",
        "front": "assets/img/books/digital_skills_cover_page-1.png",
        "back": "assets/img/books/digital_skills_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Digital%20Skills%20Handbook",
        "features": [
          "All 5 statutory National Standards fully illustrated with guides",
          "Workplace digital skills: file management, cloud storage & spreadsheets",
          "Cybersecurity: phishing detection, passwords & GDPR safety rules",
          "Simulated practical exam tasks calibrated to awarding bodies"
        ]
      },
      "bksb_remediation": {
        "title": "BKSB / OneAdvanced Diagnostic Gap Remediation Workbook",
        "badge": "Diagnostic Bridge • Two-Stage",
        "subtitle": "The Two-Stage Gap Repair Bridge for Apprentices & College Learners",
        "desc": "Specifically compiled for learners who have taken BKSB or OneAdvanced assessments and need to fix flagged weaknesses. Features Stage 1 independent retry sheets and Stage 2 tutor step-by-step diagnostic solutions.",
        "align": "BKSB & OneAdvanced Diagnostic Bridge",
        "isbn": "978-1-912345-87-6",
        "front": "assets/img/books/bksb_remediation_cover_page-1.png",
        "back": "assets/img/books/bksb_remediation_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20BKSB%20OneAdvanced%20Workbook",
        "features": [
          "Targeted remediation of frequently failed diagnostic questions",
          "Two-Stage Method: practice retry questions before viewing tutor models",
          "Covers both Maths calculations and English formatting criteria",
          "Exit milestone drills to verify Level 2 readiness"
        ]
      },
      "mock_pack_maths_l2": {
        "title": "5-Mock Past Exam Papers & Mark Schemes Pack (Maths L2)",
        "badge": "Exam Simulation • 5 Full Tests",
        "subtitle": "5 Authentic Section A (Non-Calc) & Section B (Calc) Booklets with Mark Schemes",
        "desc": "5 realistic mock examination papers formatted identically to official Pearson Edexcel and City & Guilds booklets. Includes separate Section A Non-Calc and Section B Calc papers with complete model mark schemes.",
        "align": "Pearson Edexcel & C&G Standards",
        "isbn": "978-1-912345-88-3",
        "front": "assets/img/books/mock_pack_maths_l2_cover_page-1.png",
        "back": "assets/img/books/mock_pack_maths_l2_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%205-Mock%20Papers%20Pack",
        "features": [
          "5 complete exam papers: Section A (Non-Calc) + Section B (Calculator)",
          "Full model mark schemes detailing Method (M) and Accuracy (A) marks",
          "Realistic timed exam condition practice booklets",
          "Pass mark grade boundaries and examiner tips"
        ]
      },
      "mock_pack_english_l2": {
        "title": "5-Mock Past Exam Papers & Mark Schemes Pack (English L2)",
        "badge": "Exam Simulation • 5 Full Tests",
        "subtitle": "5 Full Reading Source Inserts & Writing Answer Booklets with Rubrics",
        "desc": "Full-length Reading source insert booklets, question papers, and Writing answer booklets with examiner model benchmarks and criteria rubrics matching Pearson Edexcel standards.",
        "align": "Pearson Edexcel & C&G Standards",
        "isbn": "978-1-912345-89-0",
        "front": "assets/img/books/mock_pack_english_l2_cover_page-1.png",
        "back": "assets/img/books/mock_pack_english_l2_cover_page-2.png",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20English%205-Mock%20Papers%20Pack",
        "features": [
          "5 Reading papers with authentic multi-text source inserts",
          "5 Writing papers with authentic 2-task writing booklets",
          "Exemplar benchmark responses showing high pass standard",
          "Official marking criteria rubrics for self or tutor grading"
        ]
      }
    };

    let currentBookId = 'maths_l2_core';

    function openLookInside(bookId) {
      const data = BOOK_DATA[bookId];
      if (!data) return;
      currentBookId = bookId;

      document.getElementById('modalTitle').textContent = data.title;
      document.getElementById('modalBadge').textContent = data.badge;
      document.getElementById('modalSubtitle').textContent = data.subtitle;
      document.getElementById('modalDesc').textContent = data.desc;
      document.getElementById('modalSpecAlign').textContent = data.align;
      document.getElementById('modalSpecIsbn').textContent = data.isbn;
      document.getElementById('modalOrderBtn').href = data.order;

      const featList = document.getElementById('modalFeatures');
      featList.innerHTML = data.features.map(f => `<li><i class="fa-solid fa-circle-check"></i> <span>${f}</span></li>`).join('');

      switchModalCover('front');
      document.getElementById('bookModalBackdrop').classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function switchModalCover(tab) {
      const data = BOOK_DATA[currentBookId];
      if (!data) return;
      const img = document.getElementById('modalCoverImg');
      const tabF = document.getElementById('tabFront');
      const tabB = document.getElementById('tabBack');

      if (tab === 'front') {
        img.src = data.front;
        tabF.classList.add('active');
        tabB.classList.remove('active');
      } else {
        img.src = data.back;
        tabB.classList.add('active');
        tabF.classList.remove('active');
      }
    }

    function closeLookInside() {
      document.getElementById('bookModalBackdrop').classList.remove('active');
      document.body.style.overflow = '';
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeLookInside();
    });
  </script>
"""

# Insert Look Inside buttons on all cards
button_mappings = [
    ('maths_l2_core', 'Maths Level 2 Core Study Guide'),
    ('maths_l2_companion', 'Maths Level 2 Companion Workbook'),
    ('maths_l1_core', 'Maths Level 1 Core Study Guide'),
    ('level2_core', 'Level 2 Writing Core Revision Guide'),
    ('level2_companion', 'Level 2 Writing Companion Workbook'),
    ('level1_core', 'Level 1 Writing Core Revision Guide'),
    ('level1_companion', 'Level 1 Writing Companion Workbook'),
    ('spag_mastery', 'Spelling, Punctuation and Grammar Handbook'),
    ('digital_skills', 'Digital Skills Handbook'),
    ('bksb_remediation', 'BKSB OneAdvanced Workbook'),
    ('mock_pack_maths_l2', 'Maths 5-Mock Papers Pack'),
    ('mock_pack_english_l2', 'English 5-Mock Papers Pack'),
]

for b_id, title_str in button_mappings:
    # Pattern to find product card containing this title and inject the Look Inside button
    target = f'Order {title_str}'
    if target in html and f"openLookInside('{b_id}')" not in html:
        button_html = f'''<div class="book-action-row">
              <button type="button" class="btn-look-inside" onclick="openLookInside('{b_id}')"><i class="fa-solid fa-book-open"></i> Look Inside &amp; Blurb</button>
            </div>'''
        # find the <a> tag right above this text
        regex = rf'(<a href="https://wa\.me/447564525425\?text=[^"]*"{re.escape(" class=\"btn-buy\">\n              <i class=\"")}[^"]*"></i>\s*Order\s*{re.escape(title_str)}\s*</a>)'
        html = re.sub(regex, rf'{button_html}\n            \1', html)

# Add Maths Level 1 Companion Practice Workbook if missing
if "maths_l1_companion" not in html:
    maths_l1_comp_html = """
        <!-- PRODUCT: Maths Level 1 Companion Workbook -->
        <div class="product-card" data-cat="maths">
          <div class="product-img-wrap">
            <span class="product-badge badge-companion">Maths L1 Companion</span>
            <img src="assets/img/books/3d_maths_l1_companion.png" alt="Master Functional Skills Maths Level 1 Companion Practice Workbook">
          </div>
          <div class="product-body">
            <div class="product-category">Companion Workbook • Maths Level 1</div>
            <h3 class="product-title">Functional Skills Maths Level 1: Companion Practice Workbook</h3>
            <p class="product-desc">
              Guided calculation frames and scaffolded workspaces designed to build confidence in numerical problem-solving. Practice essential everyday math scenarios with step-by-step intermediate checkpoints.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Scaffolded Working Frames:</strong> Step-by-step boxes for all calculations</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Workplace Problem Solving:</strong> Budgeting, decorating, stock &amp; hours</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Full Worked Solutions:</strong> Complete answers provided in back</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <div class="book-action-row">
              <button type="button" class="btn-look-inside" onclick="openLookInside('maths_l1_companion')"><i class="fa-solid fa-book-open"></i> Look Inside &amp; Blurb</button>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%201%20Companion%20Workbook" class="btn-buy">
              <i class="fa-solid fa-pen-ruler"></i> Order Maths Level 1 Companion
            </a>
          </div>
        </div>
"""
        # Insert after Maths Level 1 Core Guide
    html = html.replace('<!-- PRODUCT 14: Digital Skills Practical Handbook -->', maths_l1_comp_html + '\n        <!-- PRODUCT 14: Digital Skills Practical Handbook -->')

# Insert modal before </body>
if "bookModalBackdrop" not in html:
    html = html.replace("</body>", MODAL_HTML + "\n</body>")

with open(SHOP_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("shop.html successfully updated with 3D mockups and Look Inside interactive modal!")
