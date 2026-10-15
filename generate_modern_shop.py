import os
import re

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

shop_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pocket Revision Cards, Study Guides &amp; Companion Workbooks | Master Functional Skills</title>
  <meta name="description" content="Order official Master Functional Skills Pocket Revision Cards for Maths &amp; English Level 1 &amp; Level 2. 64 double-sided, color-coded revision cards, study guides, and companion workbooks. Free UK delivery.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <style>
    .shop-filter-bar {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 36px;
      justify-content: center;
    }}
    .shop-filter-btn {{
      padding: 9px 20px;
      border-radius: 100px;
      border: 1.5px solid var(--border);
      background: #ffffff;
      color: var(--text-secondary);
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .shop-filter-btn:hover, .shop-filter-btn.active {{
      background: var(--navy);
      color: #ffffff;
      border-color: var(--navy);
      box-shadow: 0 4px 14px rgba(7, 13, 30, 0.15);
    }}
    .product-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 30px;
    }}
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 6px 24px rgba(7, 13, 30, 0.05);
      display: flex;
      flex-direction: column;
      transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
    }}
    .product-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 14px 34px rgba(7, 13, 30, 0.12);
      border-color: var(--accent);
    }}
    .product-img-wrap {{
      height: 290px;
      background: #faf8f2;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      border-bottom: 1px solid var(--border);
      position: relative;
      overflow: hidden;
    }}
    .product-img-wrap img {{
      max-height: 100%;
      max-width: 100%;
      object-fit: contain;
      filter: drop-shadow(0 8px 18px rgba(7, 13, 30, 0.18));
      transition: transform 0.25s ease;
    }}
    .product-card:hover .product-img-wrap img {{
      transform: scale(1.03);
    }}
    .product-badge {{
      position: absolute;
      top: 14px;
      left: 14px;
      padding: 5px 12px;
      border-radius: 100px;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      z-index: 2;
    }}
    .badge-bestseller {{
      background: #f59e0b;
      color: #070d1e;
      box-shadow: 0 2px 8px rgba(245, 158, 11, 0.35);
    }}
    .badge-companion {{
      background: #003366;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    .badge-popular {{
      background: rgba(0, 184, 124, 0.15);
      color: var(--accent);
      border: 1px solid rgba(0, 184, 124, 0.3);
    }}
    .product-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    .product-category {{
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
    }}
    .product-title {{
      font-size: 1.18rem;
      font-weight: 800;
      color: var(--navy);
      margin: 0 0 10px 0;
      line-height: 1.35;
    }}
    .product-desc {{
      color: var(--text-muted);
      font-size: 0.88rem;
      line-height: 1.55;
      margin-bottom: 16px;
      flex-grow: 1;
    }}
    .product-features {{
      list-style: none;
      padding: 0;
      margin: 0 0 18px 0;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.83rem;
      color: var(--text-secondary);
    }}
    .product-features li {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .product-features li i {{
      color: var(--accent);
      font-size: 0.78rem;
    }}
    .product-price {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--navy);
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 16px;
      padding-top: 14px;
      border-top: 1px solid var(--border);
    }}
    .product-price-old {{
      font-size: 0.95rem;
      text-decoration: line-through;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .btn-buy {{
      width: 100%;
      padding: 12px 18px;
      border-radius: 12px;
      background: var(--accent);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.92rem;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .btn-buy:hover {{
      background: var(--accent-hover);
      box-shadow: 0 4px 16px var(--accent-glow);
      color: #ffffff;
    }}
    .shop-faq-wrap {{
      margin-top: 56px;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 36px;
      box-shadow: 0 6px 24px rgba(7, 13, 30, 0.05);
    }}
  </style>
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION: POCKET REVISION CARDS AS PRIMARY HERO -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <span class="moat-badge" style="background:rgba(0,184,124,0.1); color:var(--accent); font-weight:800; margin-bottom:12px;">
          <i class="fa-solid fa-layer-group"></i> #1 Flagship Study Resource
        </span>
        <h1 style="font-size: 2.6rem;">Pocket <span>Revision Cards</span> &amp; Study Packs</h1>
        <p class="hero-description">
          Our bestselling <strong>Pocket Revision Cards</strong> condense the entire Ofqual specification into rapid, color-coded study flashcards. Packed with step-by-step model methods, key formulas, and exam trap alerts, they are the single most effective way to revise on the go and pass first time.
        </p>
        <div class="moat-strip">
          <span class="moat-badge"><i class="fa-solid fa-layer-group"></i> 64 Double-Sided Revision Cards</span>
          <span class="moat-badge"><i class="fa-solid fa-palette"></i> Color-Coded Topic Strands</span>
          <span class="moat-badge"><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Warnings</span>
          <span class="moat-badge"><i class="fa-solid fa-truck-fast"></i> Free Fast UK Tracked Delivery</span>
        </div>
      </div>
      <div>
        <!-- HERO SHOWCASE CARD: 3D STACK PRESENTATION -->
        <div style="background:#ffffff; border-radius:20px; border:1px solid var(--border); padding:26px 20px 22px; box-shadow:0 14px 40px rgba(7,13,30,0.08); text-align:center;">
          <div style="display:flex; justify-content:center; align-items:center; margin-bottom:14px;">
            <img src="assets/img/books/flashcards_hero_stack.svg" alt="Master Functional Skills Pocket Revision Cards 3D Stack" style="max-height:260px; width:auto; filter:drop-shadow(0 14px 28px rgba(7,13,30,0.25));">
          </div>
          <div style="font-weight:800; color:var(--navy); font-size:1.05rem;">
            Over 35,000+ Pocket Revision Cards Packs Delivered Across the UK
          </div>
          <p style="color:var(--text-muted); font-size:0.86rem; margin:4px 0 0;">
            Official Master Functional Skills 3D Revision Decks • Dispatched Same Day
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- PRODUCTS SECTION -->
  <section style="padding: 56px 0; background: var(--bg-page);">
    <div class="mfs-container">

      <!-- FILTER CHIPS: POCKET REVISION CARDS AT THE FRONT -->
      <div class="shop-filter-bar">
        <button class="shop-filter-btn active" onclick="filterShop('all', this)">All Revision Materials</button>
        <button class="shop-filter-btn" onclick="filterShop('cards', this)">Pocket Revision Cards</button>
        <button class="shop-filter-btn" onclick="filterShop('writing', this)">Writing &amp; Companion Books</button>
        <button class="shop-filter-btn" onclick="filterShop('maths', this)">Maths Study Guides</button>
        <button class="shop-filter-btn" onclick="filterShop('bundle', this)">Complete Bundles</button>
        <button class="shop-filter-btn" onclick="filterShop('mocks', this)">Printed Mock Packs</button>
        <button class="shop-filter-btn" onclick="filterShop('specialist', this)">Spelling, Punctuation &amp; Grammar</button>
      </div>

      <!-- PRODUCT GRID -->
      <div class="product-grid" id="productGrid">

        <!-- ============================================== -->
        <!-- FLAGSHIP REVISION CARDS (FEATURED FIRST)       -->
        <!-- ============================================== -->

        <!-- PRODUCT 1: Maths Level 2 Revision Cards -->
        <div class="product-card" data-cat="cards">
          <div class="product-img-wrap">
            <span class="product-badge badge-bestseller">#1 Bestseller • Flagship</span>
            <img src="assets/img/books/flashcards_maths_l2.svg" alt="Functional Skills Maths Level 2 Pocket Revision Cards 3D Stack">
          </div>
          <div class="product-body">
            <div class="product-category">Pocket Revision Cards • Maths Level 2</div>
            <h3 class="product-title">Functional Skills Maths Level 2 Pocket Revision Cards</h3>
            <p class="product-desc">
              64 double-sided, color-coded pocket revision cards covering every single topic on the Ofqual specification. Includes key formulas, quick recall conversions, stepped model solutions, and prominent exam trap alerts.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>64 High-Gloss Revision Cards:</strong> Color-coded by curriculum strand</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Essential Formulas:</strong> Area, volume, percentages, speed &amp; density</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Exam Trap Warnings:</strong> Avoid common calculation errors that cost marks</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Sturdy Pocket Box:</strong> Easy to carry and revise anywhere</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£19.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%202%20Pocket%20Revision%20Cards" class="btn-buy">
              <i class="fa-solid fa-layer-group"></i> Order Revision Cards Pack
            </a>
          </div>
        </div>

        <!-- PRODUCT 2: English Level 2 Revision Cards -->
        <div class="product-card" data-cat="cards">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">English Bestseller</span>
            <img src="assets/img/books/flashcards_english_l2.svg" alt="Functional Skills English Level 2 Pocket Revision Cards 3D Stack">
          </div>
          <div class="product-body">
            <div class="product-category">Pocket Revision Cards • English Level 2</div>
            <h3 class="product-title">Functional Skills English Level 2 Pocket Revision Cards</h3>
            <p class="product-desc">
              Comprehensive double-sided pocket revision cards covering Reading language techniques, organizational features, and Writing frameworks (letters, emails, articles, and speeches) with full spelling, punctuation and grammar checklists.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>64 Double-Sided Revision Cards:</strong> Reading analysis &amp; Writing templates</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Persuasive Devices:</strong> DAFOREST techniques with high-scoring examples</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Punctuation &amp; Grammar Golden Rules:</strong> Instant memory anchors</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Format Checklists:</strong> Structural markers for all 11 Level 2 formats</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£19.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20English%20Level%202%20Pocket%20Revision%20Cards" class="btn-buy">
              <i class="fa-solid fa-layer-group"></i> Order Revision Cards Pack
            </a>
          </div>
        </div>

        <!-- PRODUCT 3: Maths Level 1 Revision Cards -->
        <div class="product-card" data-cat="cards">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Level 1 Bestseller</span>
            <img src="assets/img/books/flashcards_maths_l1.svg" alt="Functional Skills Maths Level 1 Pocket Revision Cards 3D Stack">
          </div>
          <div class="product-body">
            <div class="product-category">Pocket Revision Cards • Maths Level 1</div>
            <h3 class="product-title">Functional Skills Maths Level 1 Pocket Revision Cards</h3>
            <p class="product-desc">
              54 visual, color-coded pocket revision cards designed to build numerical confidence. Covers times tables, fractions of amounts, decimal arithmetic, metric unit conversions, and simple perimeter and area calculations.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>54 Visual Revision Cards:</strong> Clear, dyslexia-friendly step-by-step models</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Fractions &amp; Decimals:</strong> Step-by-step methods for non-calc questions</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Measurement &amp; Conversions:</strong> Length, weight, capacity &amp; time charts</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%201%20Pocket%20Revision%20Cards" class="btn-buy">
              <i class="fa-solid fa-layer-group"></i> Order Revision Cards Pack
            </a>
          </div>
        </div>

        <!-- PRODUCT 4: Revision Cards Twin Pack -->
        <div class="product-card" data-cat="bundle">
          <div class="product-img-wrap">
            <span class="product-badge badge-bestseller">Save 25% • Both Subjects</span>
            <img src="assets/img/books/bundle_ultimate_l2.svg" alt="Master Functional Skills Revision Cards Twin Pack">
          </div>
          <div class="product-body">
            <div class="product-category">Revision Cards Bundle • Level 2</div>
            <h3 class="product-title">Master Level 2 Revision Cards Twin Pack (Maths &amp; English)</h3>
            <p class="product-desc">
              Get both official Level 2 Pocket Revision Card decks together in one complete study pack. 128 total double-sided revision cards covering the complete Pearson Edexcel and City &amp; Guilds curriculum.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Both Complete Decks:</strong> 64 Maths Revision Cards + 64 English Revision Cards</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>128 Total Double-Sided Cards:</strong> Color-coded by topic strand</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Free Tracked Delivery:</strong> Dispatched direct to your door</li>
            </ul>
            <div class="product-price">
              £24.99 <span class="product-price-old">£34.98</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Revision%20Cards%20Twin%20Pack" class="btn-buy">
              <i class="fa-solid fa-box-open"></i> Order Revision Cards Twin Pack
            </a>
          </div>
        </div>

        <!-- ============================================== -->
        <!-- OFFICIAL WRITING & COMPANION BOOKS             -->
        <!-- ============================================== -->

        <!-- PRODUCT 5: Level 2 Writing Core Guide -->
        <div class="product-card" data-cat="writing">
          <div class="product-img-wrap">
            <span class="product-badge badge-bestseller">#1 Bestseller • Official</span>
            <img src="assets/img/books/level2_core_cover_page-1.png" alt="Functional Skills English Level 2 Writing Skills Core Revision Guide">
          </div>
          <div class="product-body">
            <div class="product-category">English Writing • Level 2</div>
            <h3 class="product-title">Functional Skills English Level 2: Writing Skills (Core Revision Guide)</h3>
            <p class="product-desc">
              The definitive preparation manual for candidates aiming for a high pass at Level 2 (GCSE 4/C Equivalent). Master advanced organizational markers, persuasive rhetoric, sophisticated register, and complex sentence structures across all 11 exam formats.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>All 11 Level 2 Formats:</strong> Letters, Emails, Articles, Reports, Speeches, Reviews, Leaflets, Blogs</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>22 High-Challenge Exam Tasks:</strong> Calibrated to Pearson Edexcel &amp; C&amp;G standards</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>11 Full Exemplar Model Answers:</strong> Demonstrating sophisticated vocabulary &amp; cohesion</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Official Examiner Rubrics:</strong> Spelling, Punctuation and Grammar criteria checklists &amp; mark schemes</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£19.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Writing%20Core%20Revision%20Guide" class="btn-buy">
              <i class="fa-solid fa-book"></i> Order Writing Core Guide
            </a>
          </div>
        </div>

        <!-- PRODUCT 6: Level 2 Writing Companion Workbook -->
        <div class="product-card" data-cat="writing">
          <div class="product-img-wrap">
            <span class="product-badge badge-companion">Essential Companion</span>
            <img src="assets/img/books/level2_companion_cover_page-1.png" alt="Functional Skills English Level 2 Writing Companion Workbook">
          </div>
          <div class="product-body">
            <div class="product-category">Companion Workbook • Level 2</div>
            <h3 class="product-title">Functional Skills English Level 2: Writing Companion Workbook</h3>
            <p class="product-desc">
              The official companion workbook designed to accompany the Core Writing Guide. Provides hands-on practice workspaces, sentence variety workouts, paragraph planning templates, error-correction drills, and full exam writing frames.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Scaffolded Writing Workspaces:</strong> Plan-and-write layout for each format</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Punctuation &amp; Grammar Drills:</strong> Colon, semicolon &amp; complex sentence workouts</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Error-Correction Challenges:</strong> Spot and repair typical learner mistakes</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Self-Assessment Checklists:</strong> Verify your writing against mark scheme thresholds</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Writing%20Companion%20Workbook" class="btn-buy">
              <i class="fa-solid fa-pen-ruler"></i> Order Companion Workbook
            </a>
          </div>
        </div>

        <!-- PRODUCT 7: Level 2 Writing & Companion Mastery Bundle -->
        <div class="product-card" data-cat="bundle">
          <div class="product-img-wrap">
            <span class="product-badge badge-bestseller">Save 30% • Best Value</span>
            <img src="assets/img/books/bundle_writing_l2.svg" alt="Master Functional Skills English Level 2 Writing and Companion Bundle">
          </div>
          <div class="product-body">
            <div class="product-category">Complete Package • English Level 2</div>
            <h3 class="product-title">English Level 2 Writing &amp; Companion Mastery Bundle</h3>
            <p class="product-desc">
              Get both official books together for complete writing mastery. Includes the <strong>Core Revision Guide</strong> (with 11 exemplar model answers) plus the <strong>Companion Workbook</strong> (with scaffolding drills and exam workspaces) plus the Spelling, Punctuation and Grammar formula drillbook.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Both Volumes Included:</strong> Core Revision Guide + Companion Practice Workbook</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Bonus Spelling, Punctuation &amp; Grammar Drillbook:</strong> High-frequency workplace vocabulary banks</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Free Tracked UK Courier:</strong> Delivered within 24–48 hours</li>
            </ul>
            <div class="product-price">
              £24.99 <span class="product-price-old">£36.98</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%202%20Writing%20and%20Companion%20Bundle" class="btn-buy">
              <i class="fa-solid fa-box-archive"></i> Order Writing Mastery Bundle
            </a>
          </div>
        </div>

        <!-- PRODUCT 8: Level 1 Writing Core Guide -->
        <div class="product-card" data-cat="writing">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Level 1 Core</span>
            <img src="assets/img/books/level1_core_cover_page-1.png" alt="Functional Skills English Level 1 Writing Skills Core Revision Guide">
          </div>
          <div class="product-body">
            <div class="product-category">English Writing • Level 1</div>
            <h3 class="product-title">Functional Skills English Level 1: Writing Skills (Core Revision Guide)</h3>
            <p class="product-desc">
              Step-by-step master guide for Level 1 English candidates. Learn how to write clear, structured formal letters, workplace emails, community articles, information leaflets, and reviews with complete exemplar benchmark answers.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Core Writing Formats:</strong> Formal letters, emails, articles, leaflets, reviews</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Step-by-Step Exemplar Models:</strong> Clear paragraph structure &amp; tone</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Foundational Rules:</strong> Capital letters, full stops, question marks &amp; spelling lists</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£19.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%201%20Writing%20Core%20Revision%20Guide" class="btn-buy">
              <i class="fa-solid fa-book"></i> Order Level 1 Guide
            </a>
          </div>
        </div>

        <!-- PRODUCT 9: Level 1 Writing Companion Workbook -->
        <div class="product-card" data-cat="writing">
          <div class="product-img-wrap">
            <span class="product-badge badge-companion">Level 1 Companion</span>
            <img src="assets/img/books/level1_companion_cover_page-1.png" alt="Functional Skills English Level 1 Writing Companion Workbook">
          </div>
          <div class="product-body">
            <div class="product-category">Companion Workbook • Level 1</div>
            <h3 class="product-title">Functional Skills English Level 1: Writing Companion Workbook</h3>
            <p class="product-desc">
              Designed specifically for Level 1 learners to build sentence structure and vocabulary step-by-step. Features guided writing frames, spelling practice, punctuation worksheets, and real exam prompt workspaces.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Guided Writing Frames:</strong> Eliminates the blank page fear</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Sentence Building Workouts:</strong> Connectives, compound sentences &amp; paragraphs</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Real Exam Scenarios:</strong> Job application letters, customer emails, event reviews</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Level%201%20Writing%20Companion%20Workbook" class="btn-buy">
              <i class="fa-solid fa-pen-ruler"></i> Order Level 1 Companion
            </a>
          </div>
        </div>

        <!-- PRODUCT 10: Spelling, Punctuation and Grammar Handbook -->
        <div class="product-card" data-cat="specialist">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Spelling, Punctuation &amp; Grammar</span>
            <img src="assets/img/books/spelling_punctuation_grammar_cover.svg" alt="Master Functional Skills Spelling, Punctuation and Grammar Handbook &amp; Drills">
          </div>
          <div class="product-body">
            <div class="product-category">English Language • Levels 1 &amp; 2</div>
            <h3 class="product-title">Spelling, Punctuation and Grammar Handbook &amp; Drills</h3>
            <p class="product-desc">
              Overcome comma splices, apostrophe confusion, and homophone errors permanently. Contains 25 targeted units covering spelling patterns, punctuation accuracy, and grammatical structures with before-and-after corrections and 150+ rapid practice sentences.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Eliminate Fatal Errors:</strong> Comma splices, run-ons &amp; misplaced apostrophes</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>High-Level Punctuation:</strong> Colons, semicolons &amp; brackets mastered</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Academic &amp; Workplace Vocabulary:</strong> Tone and register calibration</li>
            </ul>
            <div class="product-price">
              £11.99 <span class="product-price-old">£15.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Spelling,%20Punctuation%20and%20Grammar%20Handbook" class="btn-buy">
              <i class="fa-solid fa-spell-check"></i> Order Spelling, Punctuation &amp; Grammar Handbook
            </a>
          </div>
        </div>

        <!-- PRODUCT 11: Maths Level 2 Core Guide -->
        <div class="product-card" data-cat="maths">
          <div class="product-img-wrap">
            <span class="product-badge badge-bestseller">Maths Level 2 Core</span>
            <img src="assets/img/books/maths_l2_core_cover.svg" alt="Master Functional Skills Maths Level 2 Core Study Guide">
          </div>
          <div class="product-body">
            <div class="product-category">Mathematics • Level 2</div>
            <h3 class="product-title">Functional Skills Maths Level 2: Core Study &amp; Revision Guide</h3>
            <p class="product-desc">
              Comprehensive syllabus coverage across all 39 curriculum standards. Master Section A Non-Calculator mental arithmetic, long division, and fractions, alongside Section B Calculator multi-step compound problems, percentages, geometry, and probability.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>All 39 Curriculum Standards:</strong> Number, Measure &amp; Shape, Handling Data</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Section A &amp; B Strategy:</strong> Worked examples showing method mark steps</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Common Trap Alerts:</strong> Pitfalls that cost marks in official sittings</li>
            </ul>
            <div class="product-price">
              £15.99 <span class="product-price-old">£21.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%202%20Core%20Study%20Guide" class="btn-buy">
              <i class="fa-solid fa-calculator"></i> Order Maths Core Guide
            </a>
          </div>
        </div>

        <!-- PRODUCT 12: Maths Level 2 Companion Workbook -->
        <div class="product-card" data-cat="maths">
          <div class="product-img-wrap">
            <span class="product-badge badge-companion">Maths Companion</span>
            <img src="assets/img/books/maths_l2_companion_cover.svg" alt="Master Functional Skills Maths Level 2 Companion Workbook">
          </div>
          <div class="product-body">
            <div class="product-category">Companion Workbook • Maths Level 2</div>
            <h3 class="product-title">Functional Skills Maths Level 2: Companion Practice Workbook</h3>
            <p class="product-desc">
              Stepped problem-solving frames and dedicated calculation workspaces for every Maths topic. Includes 120+ stepped exam drill questions designed to train you to write out all intermediate working for full method marks.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>120+ Stepped Drills:</strong> Practice multi-step workplace calculations</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Working Method Boxes:</strong> Guarantee every method mark on exam day</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Full Worked Answers:</strong> Complete step-by-step solutions included</li>
            </ul>
            <div class="product-price">
              £13.99 <span class="product-price-old">£18.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%202%20Companion%20Workbook" class="btn-buy">
              <i class="fa-solid fa-pen-ruler"></i> Order Maths Companion
            </a>
          </div>
        </div>

        <!-- PRODUCT 13: Maths Level 1 Core Guide -->
        <div class="product-card" data-cat="maths">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Maths Level 1</span>
            <img src="assets/img/books/maths_l1_core_cover.svg" alt="Master Functional Skills Maths Level 1 Core Study Guide">
          </div>
          <div class="product-body">
            <div class="product-category">Mathematics • Level 1</div>
            <h3 class="product-title">Functional Skills Maths Level 1: Core Study &amp; Revision Guide</h3>
            <p class="product-desc">
              Build unshakable numerical foundations. Step-by-step visual models for whole numbers, decimals, basic fractions, simple percentages, ratio, perimeter, area, volume, and unit conversions.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Full Level 1 Syllabus:</strong> Clear, visual, dyslexia-friendly layout</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Non-Calc Mental Strategies:</strong> Multiplication grids, division &amp; fractions</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Real-Life Contexts:</strong> Budgeting, timetables, shopping, tiling &amp; fencing</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£19.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Level%201%20Core%20Study%20Guide" class="btn-buy">
              <i class="fa-solid fa-calculator"></i> Order Level 1 Maths
            </a>
          </div>
        </div>

        <!-- PRODUCT 14: Digital Skills Practical Handbook -->
        <div class="product-card" data-cat="specialist">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Digital Skills EDSQ</span>
            <img src="assets/img/books/digital_skills_cover.svg" alt="Master Essential Digital Skills Practical Handbook">
          </div>
          <div class="product-body">
            <div class="product-category">Digital Skills • Level 1 &amp; Entry 3</div>
            <h3 class="product-title">Essential Digital Skills (EDSQ) Practical Study Handbook</h3>
            <p class="product-desc">
              Step-by-step practical manual for Essential Digital Skills Qualifications. Covers all 5 official skill areas: Using Devices, Creating &amp; Editing, Communicating, Transacting, and Being Safe &amp; Responsible Online.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>All 5 National Standards:</strong> Fully illustrated with step-by-step guides</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Workplace Digital Literacy:</strong> Cloud storage, email etiquette &amp; spreadsheets</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Online Safety &amp; Security:</strong> Phishing detection, passwords &amp; GDPR basics</li>
            </ul>
            <div class="product-price">
              £14.99 <span class="product-price-old">£18.99</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Digital%20Skills%20Handbook" class="btn-buy">
              <i class="fa-solid fa-laptop-code"></i> Order Digital Handbook
            </a>
          </div>
        </div>

        <!-- PRODUCT 15: BKSB / OneAdvanced Remediation Workbook -->
        <div class="product-card" data-cat="specialist">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">BKSB / OneAdvanced</span>
            <img src="assets/img/books/bksb_remediation_cover.svg" alt="BKSB / OneAdvanced Diagnostic Mastery &amp; Skill Remediation Workbook">
          </div>
          <div class="product-body">
            <div class="product-category">Diagnostic Remediation • L1 &amp; L2</div>
            <h3 class="product-title">BKSB / OneAdvanced Diagnostic Gap Remediation Workbook</h3>
            <p class="product-desc">
              Specifically compiled for apprentices and adult learners preparing for or reviewing initial and diagnostic assessments. Features stepped remediation models for frequently failed questions across Maths and English.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>Targeted Gap Repair:</strong> Fix the specific errors flagged on BKSB / OneAdvanced</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Two-Stage Method:</strong> Practice retry questions before reviewing model answers</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Exit Milestone Drills:</strong> Verify you have achieved the Level 2 standard</li>
            </ul>
            <div class="product-price">
              £16.99 <span class="product-price-old">£22.00</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20BKSB%20OneAdvanced%20Workbook" class="btn-buy">
              <i class="fa-solid fa-list-check"></i> Order BKSB Workbook
            </a>
          </div>
        </div>

        <!-- PRODUCT 16: Maths 5-Mock Exam Pack -->
        <div class="product-card" data-cat="mocks">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">5 Full Tests</span>
            <img src="assets/img/books/mock_pack_maths_l2.svg" alt="Master Functional Skills Maths Level 2 5-Mock Exam Papers Pack">
          </div>
          <div class="product-body">
            <div class="product-category">Printed Exam Booklets • Maths Level 2</div>
            <h3 class="product-title">5-Mock Past Exam Papers &amp; Mark Schemes Pack (Maths L2)</h3>
            <p class="product-desc">
              5 realistic mock examination papers formatted exactly as official Pearson Edexcel and City &amp; Guilds booklets. Includes separate Section A Non-Calc and Section B Calc papers with complete model mark schemes.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>5 Complete Exam Papers:</strong> Section A (Non-Calc) + Section B (Calculator)</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Full Model Solutions:</strong> Demonstrating exactly where marks are awarded</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Printed on Premium Paper:</strong> Realistic timed exam condition practice</li>
            </ul>
            <div class="product-price">
              £19.99 <span class="product-price-old">£25.00</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%205-Mock%20Papers%20Pack" class="btn-buy">
              <i class="fa-solid fa-file-lines"></i> Order Maths Mock Pack
            </a>
          </div>
        </div>

        <!-- PRODUCT 17: English 5-Mock Exam Pack -->
        <div class="product-card" data-cat="mocks">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular">Reading &amp; Writing</span>
            <img src="assets/img/books/mock_pack_english_l2.svg" alt="Master Functional Skills English Level 2 5-Mock Exam Papers Pack">
          </div>
          <div class="product-body">
            <div class="product-category">Printed Exam Booklets • English Level 2</div>
            <h3 class="product-title">5-Mock Past Exam Papers &amp; Mark Schemes Pack (English L2)</h3>
            <p class="product-desc">
              Full-length Reading source insert booklets, question papers, and Writing answer booklets with examiner model benchmarks and criteria rubrics matching Pearson Edexcel standards.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check"></i> <strong>5 Reading Papers:</strong> Authentic multi-text source inserts and questions</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>5 Writing Papers:</strong> Authentic 2-task writing booklets with ruled pages</li>
              <li><i class="fa-solid fa-circle-check"></i> <strong>Exemplar Benchmarks:</strong> Pass/Fail criteria rubrics for self-evaluation</li>
            </ul>
            <div class="product-price">
              £19.99 <span class="product-price-old">£25.00</span>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20English%205-Mock%20Papers%20Pack" class="btn-buy">
              <i class="fa-solid fa-file-lines"></i> Order English Mock Pack
            </a>
          </div>
        </div>

      </div>

      <!-- FAQ & BUYER GUIDE SECTION -->
      <div class="shop-faq-wrap">
        <h3 style="font-size: 1.35rem; color: var(--navy); margin-bottom: 8px;">
          <i class="fa-solid fa-circle-question" style="color:var(--accent); margin-right:8px;"></i>
          Frequently Asked Questions About Our Pocket Revision Cards &amp; Publications
        </h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
          Everything you need to know about our Pocket Revision Cards, Core Revision Guides, and Fast Tracked Delivery.
        </p>

        <div style="display: grid; gap: 18px;">
          <div style="background:#faf8f2; border:1px solid var(--border); border-radius:12px; padding:20px;">
            <h4 style="font-size:1.05rem; color:var(--navy); margin-bottom:8px; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-layer-group" style="color:var(--accent);"></i>
              Why are Pocket Revision Cards the most effective way to revise?
            </h4>
            <p style="margin:0 0 8px; color:var(--text-primary); font-size:0.92rem; line-height:1.6;">
              Our <strong>Pocket Revision Cards</strong> utilize active recall and spaced repetition. By breaking down daunting topics (like trapezium area, percentage change, or formal letters) onto individual, double-sided cards with exam trap warnings and worked steps, you can quickly test yourself anywhere—on your commute, at lunch, or before exam day.
            </p>
          </div>

          <div style="background:#faf8f2; border:1px solid var(--border); border-radius:12px; padding:20px;">
            <h4 style="font-size:1.05rem; color:var(--navy); margin-bottom:8px; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-book" style="color:var(--accent);"></i>
              What is the difference between the Core Revision Guide and the Companion Workbook?
            </h4>
            <p style="margin:0 0 8px; color:var(--text-primary); font-size:0.92rem; line-height:1.6;">
              The <strong>Core Revision Guide</strong> is your complete teaching manual: it breaks down every single format or topic, teaches you the structural markers and examiners' expectations, and provides complete, unshortened <strong>Exemplar Model Answers</strong>.
            </p>
            <p style="margin:0; color:var(--text-muted); font-size:0.88rem; line-height:1.5;">
              The <strong>Companion Workbook</strong> is your hands-on exercise book: it provides scaffolded planning frames, sentence builders, error-correction tasks, and exam workspaces so you can practice independently without having to guess what to write.
            </p>
          </div>

          <div style="background:#faf8f2; border:1px solid var(--border); border-radius:12px; padding:20px;">
            <h4 style="font-size:1.05rem; color:var(--navy); margin-bottom:8px; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-award" style="color:var(--accent);"></i>
              Are these Pocket Revision Cards and books aligned with Pearson Edexcel?
            </h4>
            <p style="margin:0; color:var(--text-primary); font-size:0.92rem; line-height:1.6;">
              Yes, 100%. All materials are meticulously mapped to the reformed Ofqual subject criteria. While our writing formats and exemplars are calibrated to Pearson Edexcel's rigorous standard, they are fully applicable to City &amp; Guilds, Open Awards, NCFE, and AQA.
            </p>
          </div>

          <div style="background:#faf8f2; border:1px solid var(--border); border-radius:12px; padding:20px;">
            <h4 style="font-size:1.05rem; color:var(--navy); margin-bottom:8px; display:flex; align-items:center; gap:8px;">
              <i class="fa-solid fa-truck" style="color:var(--accent);"></i>
              How fast is delivery and can I order for my college or training provider?
            </h4>
            <p style="margin:0; color:var(--text-primary); font-size:0.92rem; line-height:1.6;">
              Individual orders are dispatched via Royal Mail Tracked 24/48 with free delivery across the UK. For bulk orders for colleges, NHS trusts, training providers, or apprenticeship cohorts, contact us via WhatsApp or phone (020 XXXX XXXX) for institutional invoicing and bulk educational discounts.
            </p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <script>
    function filterShop(cat, btn) {{
      document.querySelectorAll('.shop-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.product-card').forEach(card => {{
        if (cat === 'all' || card.getAttribute('data-cat') === cat) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>

{FOOTER}
</body>
</html>
"""

target = os.path.join(PROJECT_DIR, "shop.html")
with open(target, "w", encoding="utf-8") as f:
    f.write(shop_html)

print(f"[OK] Generated modern Master Functional Skills shop.html with Revision Cards as primary focus ({len(shop_html)} bytes)")
