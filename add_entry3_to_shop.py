#!/usr/bin/env python3
"""
add_entry3_to_shop.py
Adds Entry Level 3 books and filter chip to shop.html, and updates BOOK_DATA.
"""

import re

SHOP_PATH = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/shop.html"

with open(SHOP_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Entry Level 3 filter chip if not present
if "filterShop('entry3'" not in html:
    html = html.replace(
        '<button class="shop-filter-btn" onclick="filterShop(\'cards\', this)">Pocket Revision Cards</button>',
        '<button class="shop-filter-btn" onclick="filterShop(\'entry3\', this)">Entry Level 3</button>\n        <button class="shop-filter-btn" onclick="filterShop(\'cards\', this)">Pocket Revision Cards</button>'
    )
    print("Added Entry Level 3 filter chip.")

# 2. Add Entry Level 3 product cards
ENTRY3_CARDS = """
        <!-- ============================================== -->
        <!-- ENTRY LEVEL 3 FOUNDATIONS (RED SCHEME)         -->
        <!-- ============================================== -->

        <!-- PRODUCT: Maths Entry Level 3 Core Guide -->
        <div class="product-card" data-cat="entry3">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular" style="background:rgba(220,38,38,0.15); color:#dc2626; border-color:rgba(220,38,38,0.3);">Entry 3 Core • Red Series</span>
            <img src="assets/img/books/3d_maths_e3_core.png" alt="Functional Skills Maths Entry Level 3 Foundations Study Guide">
          </div>
          <div class="product-body">
            <div class="product-category" style="color:#dc2626;">Mathematics • Entry Level 3</div>
            <h3 class="product-title">Functional Skills Maths Entry Level 3: Foundations Study Guide</h3>
            <p class="product-desc">
              Friendly, confidence-building visual guide to Entry Level 3 Maths. Master place value up to 1000, addition, subtraction, times tables, division with remainders, decimal money, and clock time with step-by-step illustrations.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>Visual Step-by-Step Models:</strong> Chunked explanations with zero math jargon</li>
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>Everyday Practical Maths:</strong> Calculating change, bus times &amp; recipes</li>
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>Confidence Checkpoints:</strong> Progress self-checks at the end of each unit</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <div class="book-action-row" style="margin-bottom:8px;">
              <button type="button" class="btn-look-inside" onclick="openLookInside('maths_e3_core')"><i class="fa-solid fa-book-open"></i> Look Inside &amp; Blurb</button>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Entry%20Level%203%20Guide" class="btn-buy">
              <i class="fa-solid fa-calculator"></i> Order Entry 3 Maths Guide
            </a>
          </div>
        </div>

        <!-- PRODUCT: English Entry Level 3 Core Guide -->
        <div class="product-card" data-cat="entry3">
          <div class="product-img-wrap">
            <span class="product-badge badge-popular" style="background:rgba(220,38,38,0.15); color:#dc2626; border-color:rgba(220,38,38,0.3);">Entry 3 Core • Red Series</span>
            <img src="assets/img/books/3d_english_e3_core.png" alt="Functional Skills English Entry Level 3 Foundations Study Guide">
          </div>
          <div class="product-body">
            <div class="product-category" style="color:#dc2626;">English Literacy • Entry Level 3</div>
            <h3 class="product-title">Functional Skills English Entry Level 3: Step-by-Step Foundations</h3>
            <p class="product-desc">
              The supportive guide for Entry Level 3 English candidates. Covers compound sentence formation with connectives (and, but, because), fundamental punctuation, high-frequency spelling lists, and workplace notes and forms.
            </p>
            <ul class="product-features">
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>Scaffolded Sentences:</strong> Connectives &amp; compound sentence structures</li>
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>Workplace Reading:</strong> Extracting key facts from notices, signs &amp; emails</li>
              <li><i class="fa-solid fa-circle-check" style="color:#dc2626;"></i> <strong>100 Common Spelling Words:</strong> High-frequency vocabulary for test day</li>
            </ul>
            <div class="product-price">
              £12.99 <span class="product-price-old">£16.99</span>
            </div>
            <div class="book-action-row" style="margin-bottom:8px;">
              <button type="button" class="btn-look-inside" onclick="openLookInside('english_e3_core')"><i class="fa-solid fa-book-open"></i> Look Inside &amp; Blurb</button>
            </div>
            <a href="https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20English%20Entry%20Level%203%20Guide" class="btn-buy">
              <i class="fa-solid fa-book"></i> Order Entry 3 English Guide
            </a>
          </div>
        </div>
"""

if "maths_e3_core" not in html:
    html = html.replace('<!-- PRODUCT 1: Maths Level 2 Revision Cards -->', ENTRY3_CARDS + '\n        <!-- PRODUCT 1: Maths Level 2 Revision Cards -->')
    print("Added Entry Level 3 product cards.")

# 3. Add Entry 3 data to BOOK_DATA in script
ENTRY3_DATA = """      "maths_e3_core": {
        "title": "Functional Skills Maths Entry Level 3: Foundations Study Guide",
        "badge": "Entry Level 3 Core • Red Series",
        "subtitle": "Step-by-Step Visual Numeracy Foundations for Entry Level 3 Candidates",
        "desc": "Engineered for adult learners, apprentices, and vocational students building foundational math skills. Takes you step-by-step through whole numbers up to 1000, addition, subtraction, multiplication grids, division remainders, decimal money, and clock time.",
        "align": "Ofqual Regulated Maths Entry 3",
        "isbn": "978-1-912345-78-4",
        "front": "assets/img/books/maths_e3_core_cover_page-1.png",
        "back": "assets/img/books/maths_e3_core_cover_page-2.png",
        "pdf": "entry-level-3-maths.html",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20Maths%20Entry%20Level%203%20Guide",
        "features": [
          "High-contrast visual models with chunked explanations and generous font spacing",
          "Whole numbers up to 1000: place value charts and number line jumps",
          "Everyday arithmetic: calculating change, bus timetables, and recipes",
          "Confidence-building checkpoints at the end of each unit"
        ]
      },
      "english_e3_core": {
        "title": "Functional Skills English Entry Level 3: Step-by-Step Foundations",
        "badge": "Entry Level 3 Core • Red Series",
        "subtitle": "Clear Sentence Building, Workplace Reading, and Basic Writing Guide",
        "desc": "The supportive step-by-step guide for Entry Level 3 English candidates. Covers compound sentence formation with connectives (and, but, because), fundamental punctuation, high-frequency spelling lists, and simple workplace emails, notes, and forms.",
        "align": "Ofqual Regulated English Entry 3",
        "isbn": "978-1-912345-79-1",
        "front": "assets/img/books/english_e3_core_cover_page-1.png",
        "back": "assets/img/books/english_e3_core_cover_page-2.png",
        "pdf": "entry-level-3-maths.html",
        "order": "https://wa.me/447564525425?text=Hi,%20I'd%20like%20to%20order%20the%20English%20Entry%20Level%203%20Guide",
        "features": [
          "Guided sentence building with connectives and compound structures",
          "Extracting key information from notices, signs, schedules, and instructions",
          "Essential punctuation: capital letters, full stops, question marks, and commas",
          "100 high-frequency test spelling words with memory anchors"
        ]
      },
"""

if '"maths_e3_core":' not in html:
    html = html.replace('const BOOK_DATA = {\n', 'const BOOK_DATA = {\n' + ENTRY3_DATA)
    print("Added Entry Level 3 book data to JS.")

with open(SHOP_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("shop.html successfully updated with Entry Level 3 Red series!")
