/**
 * MASTER FUNCTIONAL SKILLS (UK) — GLOBAL INSTANT SEARCH (Ctrl+K / Cmd+K)
 * Real-time searchable directory of all 174 topics, past papers, tools, and courses.
 */
(function() {
  'use strict';

  var SEARCH_ITEMS = [
    // Tools & Interactive
    { title: "Pass Mark & Grade Boundary Calculator", cat: "Tool", url: "pass-mark-calculator.html", desc: "Calculate raw mock marks against official Ofqual boundaries (Edexcel, C&G, Open Awards)." },
    { title: "Free Diagnostic Skill Checker", cat: "Tool", url: "diagnostic-test.html", desc: "10-question rapid assessment identifying Entry 3, Level 1, or Level 2 skill gaps." },
    { title: "BKSB / OneAdvanced Bridge & Remediation", cat: "Tool", url: "bksb-remediation.html", desc: "Automated software bridge converting BKSB / OneAdvanced diagnostics into targeted retry sheets." },
    { title: "Master Revision Hub", cat: "Directory", url: "revise.html", desc: "Central revision landing page connecting all Maths, English, and Digital Skills." },
    { title: "Revision Cards & Study Books Shop", cat: "Shop", url: "shop.html", desc: "Order pocket revision flashcards, 5-mock exam packs, and complete study bundles." },

    // Past Papers — Level 2
    { title: "Pearson Edexcel Maths Level 2 Past Papers", cat: "Past Papers", url: "edexcel-functional-skills-maths-level-2-past-papers.html", desc: "20 Practice Papers, non-calc & calc sections, mark schemes, video walkthroughs." },
    { title: "City & Guilds Maths Level 2 Past Papers", cat: "Past Papers", url: "city-and-guilds-functional-skills-maths-level-2-past-papers.html", desc: "Official 4748-02 sample papers, Section 1 & 2 worked solutions." },
    { title: "Open Awards Maths Level 2 Past Papers & Online Tests", cat: "Past Papers", url: "open-awards-functional-skills-maths-level-2-past-papers.html", desc: "Interactive XAMS onscreen live exam simulator + downloadable PDF question papers." },
    { title: "AQA Maths Level 2 Past Papers", cat: "Past Papers", url: "aqa-functional-skills-maths-level-2-past-papers.html", desc: "29 genuine question papers, Paper 1 & 2 mark schemes." },
    { title: "NCFE Maths Level 2 Past Papers", cat: "Past Papers", url: "ncfe-functional-skills-maths-level-2-past-papers.html", desc: "Comprehensive sample papers, Section A non-calc and Section B calc." },

    // Past Papers — English Level 2
    { title: "Pearson Edexcel English Level 2 Past Papers", cat: "Past Papers", url: "edexcel-functional-skills-english-level-2-past-papers.html", desc: "56 Reading and Writing papers, insert texts, and model answers." },
    { title: "City & Guilds English Level 2 Past Papers", cat: "Past Papers", url: "city-and-guilds-functional-skills-english-level-2-past-papers.html", desc: "4748-02 Reading & Writing assessment papers with examiner marking guidance." },
    { title: "Open Awards English Level 2 Online Tests & Papers", cat: "Past Papers", url: "open-awards-functional-skills-english-level-2-past-papers.html", desc: "Interactive XAMS onscreen Reading & Writing exams + PDF question booklets." },

    // Past Papers — Level 1
    { title: "Pearson Edexcel Maths Level 1 Past Papers", cat: "Past Papers", url: "edexcel-functional-skills-maths-level-1-past-papers.html", desc: "19 Practice Papers, Section A & B questions and mark schemes." },
    { title: "Pearson Edexcel English Level 1 Past Papers", cat: "Past Papers", url: "edexcel-functional-skills-english-level-1-past-papers.html", desc: "30 Reading & Writing question booklets and mark schemes." },
    { title: "Open Awards Maths Level 1 Online Tests", cat: "Past Papers", url: "open-awards-functional-skills-maths-level-1-past-papers.html", desc: "Live XAMS mock exams 1, 2, 3 and graph practice tool." },
    { title: "Open Awards English Level 1 Online Tests", cat: "Past Papers", url: "open-awards-functional-skills-english-level-1-past-papers.html", desc: "Live XAMS Reading & Writing mock exams." },

    // Digital Skills
    { title: "Digital Functional Skills Hub (DFSQ)", cat: "Digital Skills", url: "digital-functional-skills.html", desc: "Complete national standards guide (Level 1 & Entry 3) with Edexcel SAM downloads." },
    { title: "Digital Functional Skills Level 1", cat: "Digital Skills", url: "digital-functional-skills-level-1.html", desc: "Level 1 course guide, online exam booking, and syllabus breakdown." },

    // Entry 3 Maths
    { title: "Entry Level 3 Maths Revise Hub", cat: "Maths E3", url: "entry-level-3-maths.html", desc: "24 topic revision guides, PDFs, video solutions, and category filters." },

    // Maths Topics (Level 2)
    { title: "Percentages (Reverse, Percentage Change)", cat: "Maths L2", url: "functional-skills-percentages.html", desc: "Calculate percentage increases, decreases, and reverse percentages." },
    { title: "Fractions & Operations", cat: "Maths L2", url: "functional-skills-fractions.html", desc: "Add, subtract, multiply, and divide fractions and mixed numbers." },
    { title: "Ratio & Direct Proportion", cat: "Maths L2", url: "functional-skills-ratio.html", desc: "Sharing in ratios (e.g. 2:3:5), map scales, and proportional recipes." },
    { title: "Area & Perimeter (Rectangles, Triangles, Compound)", cat: "Maths L2", url: "functional-skills-area.html", desc: "Perimeter of composite shapes, area of rectangles and triangles." },
    { title: "Circles (Circumference & Area)", cat: "Maths L2", url: "functional-skills-circles.html", desc: "Using Pi (3.14) to find circle radius, diameter, area and circumference." },
    { title: "Volume & Capacity (Prisms, Cylinders)", cat: "Maths L2", url: "functional-skills-volume.html", desc: "Calculate volume of cuboids, cylinders, and convert cm³ to litres." },
    { title: "Mean, Median, Mode & Range", cat: "Maths L2", url: "functional-skills-mean-median-mode-and-range.html", desc: "Calculate averages and compare two data sets using mean and range." },
    { title: "Compound Interest & Simple Interest", cat: "Maths L2", url: "functional-skills-interest-and-compound-interest.html", desc: "Bank loans, savings interest rates, and multi-year compound interest." },
    { title: "Unit Conversions (Metric & Imperial)", cat: "Maths L2", url: "functional-skills-unit-conversions.html", desc: "Convert between kg and g, metres and cm, litres and ml, miles and km." },
    { title: "BIDMAS / Order of Operations", cat: "Maths L2", url: "functional-skills-bidmas.html", desc: "Brackets, Indices, Division, Multiplication, Addition, Subtraction." },
    { title: "Probability & Tree Diagrams", cat: "Maths L2", url: "functional-skills-probability.html", desc: "Single events, combined probability, and fractional outcomes." },
    { title: "Speed, Distance & Time", cat: "Maths L2", url: "functional-skills-speed.html", desc: "Using S = D / T formula, travel graphs, and average journey speeds." },
    { title: "Scale Drawings & Maps", cat: "Maths L2", url: "functional-skills-maps-and-scale-drawings.html", desc: "Using 1:50 and 1:100 architectural scales and compass bearings." },
    { title: "Best Buys & Value for Money", cat: "Maths L2", url: "functional-skills-best-buys.html", desc: "Compare unit prices and multipack discounts to determine best value." },

    // English Topics (Level 2)
    { title: "Reading: Fact vs Opinion", cat: "English L2", url: "reading-fact-or-opinion.html", desc: "Distinguish between verified factual statements and subjective writer opinions." },
    { title: "Reading: Language Features & Techniques", cat: "English L2", url: "reading-language-features.html", desc: "Identify metaphors, similes, rule of three, hyperbole, and rhetorical questions." },
    { title: "Reading: Investigating Layout & Organisation", cat: "English L2", url: "reading-investigating-layout.html", desc: "Analyze subheadings, bullet points, captions, text boxes, and diagrams." },
    { title: "Writing: Perfecting Your Punctuation (SPaG)", cat: "English L2", url: "writing-perfecting-your-punctuation.html", desc: "Apostrophes, commas, colons, semicolons, and sentence boundaries." },
    { title: "Writing: Formal Letters, Emails & Articles", cat: "English L2", url: "writing-communicating.html", desc: "Structure, professional register, salutations, and persuasive conventions." },
    { title: "Writing: Linking Up Your Answer (Connectives)", cat: "English L2", url: "writing-linking-up-your-answer.html", desc: "Use however, furthermore, consequently, and nevertheless effectively." },
    { title: "Speaking, Listening & Communicating (SLC)", cat: "English L2", url: "slc-the-exam.html", desc: "Official SLC criteria: presentation delivery and group discussion assessment." }
  ];

  function createSearchModal() {
    if (document.getElementById('mfsSearchOverlay')) return;

    var style = document.createElement('style');
    style.textContent = 
      '#mfsSearchOverlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(7, 13, 30, 0.65); backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); z-index: 999999; display: none; align-items: flex-start; justify-content: center; padding-top: 12vh; }' +
      '#mfsSearchOverlay.show { display: flex !important; }' +
      '.mfs-search-box { width: 92%; max-width: 640px; background: #ffffff; border-radius: 18px; box-shadow: 0 20px 50px rgba(7, 13, 30, 0.25); border: 1px solid var(--border, #e2e8f0); overflow: hidden; display: flex; flex-direction: column; max-height: 75vh; animation: mfsSearchPop 0.18s cubic-bezier(0.16, 1, 0.3, 1); }' +
      '@keyframes mfsSearchPop { from { opacity: 0; transform: scale(0.96) translateY(-8px); } to { opacity: 1; transform: scale(1) translateY(0); } }' +
      '.mfs-search-input-wrap { display: flex; align-items: center; padding: 16px 20px; border-bottom: 1px solid var(--border, #e2e8f0); background: #faf8f2; }' +
      '.mfs-search-input-wrap i { color: var(--accent, #00b87c); font-size: 1.15rem; margin-right: 14px; }' +
      '#mfsGlobalSearchInput { border: none; background: transparent; font-size: 1.05rem; font-family: inherit; width: 100%; color: var(--navy-dark, #070d1e); outline: none; }' +
      '.mfs-search-results { overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 4px; }' +
      '.mfs-search-result-item { display: flex; align-items: center; justify-content: space-between; padding: 12px 14px; border-radius: 10px; text-decoration: none; color: inherit; transition: background 0.15s ease; border: 1px solid transparent; }' +
      '.mfs-search-result-item:hover, .mfs-search-result-item.highlighted { background: #f4efe6; border-color: var(--border, #e6dfd1); }' +
      '.mfs-search-item-info { flex-grow: 1; min-width: 0; margin-right: 12px; }' +
      '.mfs-search-item-title { font-weight: 700; font-size: 0.92rem; color: var(--navy, #0b1528); margin-bottom: 2px; }' +
      '.mfs-search-item-desc { font-size: 0.78rem; color: var(--text-muted, #64748b); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }' +
      '.mfs-search-item-badge { font-size: 0.7rem; font-weight: 800; padding: 3px 8px; border-radius: 100px; background: rgba(0, 184, 124, 0.12); color: var(--accent, #00b87c); text-transform: uppercase; white-space: nowrap; }' +
      '.mfs-search-footer { padding: 10px 18px; border-top: 1px solid var(--border, #e2e8f0); font-size: 0.75rem; color: var(--text-muted, #64748b); display: flex; justify-content: space-between; align-items: center; background: #faf8f2; }' +
      '.search-kbd { background: #ffffff; border: 1px solid var(--border, #cbd5e1); border-radius: 4px; padding: 2px 6px; font-weight: 700; font-size: 0.72rem; }';
    document.head.appendChild(style);

    var overlay = document.createElement('div');
    overlay.id = 'mfsSearchOverlay';
    overlay.innerHTML = 
      '<div class="mfs-search-box" onclick="event.stopPropagation()">' +
        '<div class="mfs-search-input-wrap">' +
          '<i class="fa-solid fa-magnifying-glass"></i>' +
          '<input type="text" id="mfsGlobalSearchInput" placeholder="Search 174 topics, past papers, calculators, tools (e.g. Edexcel, fractions, area)..." autocomplete="off">' +
        '</div>' +
        '<div class="mfs-search-results" id="mfsSearchResults"></div>' +
        '<div class="mfs-search-footer">' +
          '<span>Navigate with <span class="search-kbd">↑</span> <span class="search-kbd">↓</span>, select with <span class="search-kbd">Enter</span></span>' +
          '<span>Close with <span class="search-kbd">Esc</span></span>' +
        '</div>' +
      '</div>';

    overlay.onclick = function() {
      closeSearch();
    };

    document.body.appendChild(overlay);

    var input = document.getElementById('mfsGlobalSearchInput');
    input.addEventListener('input', function() {
      renderResults(this.value.trim().toLowerCase());
    });

    input.addEventListener('keydown', function(e) {
      var items = document.querySelectorAll('.mfs-search-result-item');
      if (items.length === 0) return;
      var current = document.querySelector('.mfs-search-result-item.highlighted');
      var idx = Array.prototype.indexOf.call(items, current);

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (current) current.classList.remove('highlighted');
        var nextIdx = idx < items.length - 1 ? idx + 1 : 0;
        items[nextIdx].classList.add('highlighted');
        items[nextIdx].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (current) current.classList.remove('highlighted');
        var prevIdx = idx > 0 ? idx - 1 : items.length - 1;
        items[prevIdx].classList.add('highlighted');
        items[prevIdx].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (current) {
          window.location.href = current.getAttribute('href');
        } else if (items[0]) {
          window.location.href = items[0].getAttribute('href');
        }
      }
    });
  }

  function renderResults(q) {
    var container = document.getElementById('mfsSearchResults');
    if (!container) return;

    var filtered = SEARCH_ITEMS;
    if (q) {
      filtered = SEARCH_ITEMS.filter(function(item) {
        return item.title.toLowerCase().indexOf(q) !== -1 ||
               item.desc.toLowerCase().indexOf(q) !== -1 ||
               item.cat.toLowerCase().indexOf(q) !== -1;
      });
    }

    if (filtered.length === 0) {
      container.innerHTML = '<div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 0.9rem;">No matching topics or papers found for "<strong>' + q + '</strong>". Try searching for <em>Fractions</em>, <em>Edexcel</em>, or <em>Calculator</em>.</div>';
      return;
    }

    var html = '';
    filtered.slice(0, 12).forEach(function(item, i) {
      var isHl = i === 0 ? ' highlighted' : '';
      html += 
        '<a href="' + item.url + '" class="mfs-search-result-item' + isHl + '">' +
          '<div class="mfs-search-item-info">' +
            '<div class="mfs-search-item-title">' + item.title + '</div>' +
            '<div class="mfs-search-item-desc">' + item.desc + '</div>' +
          '</div>' +
          '<span class="mfs-search-item-badge">' + item.cat + '</span>' +
        '</a>';
    });
    container.innerHTML = html;
  }

  function openSearch() {
    createSearchModal();
    var overlay = document.getElementById('mfsSearchOverlay');
    if (overlay) {
      overlay.classList.add('show');
      var input = document.getElementById('mfsGlobalSearchInput');
      input.value = '';
      renderResults('');
      setTimeout(function() { input.focus(); }, 50);
    }
  }

  function closeSearch() {
    var overlay = document.getElementById('mfsSearchOverlay');
    if (overlay) {
      overlay.classList.remove('show');
    }
  }

  window.openGlobalSearch = openSearch;
  window.closeGlobalSearch = closeSearch;

  // Global hotkey: Ctrl+K or Cmd+K
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      var overlay = document.getElementById('mfsSearchOverlay');
      if (overlay && overlay.classList.contains('show')) {
        closeSearch();
      } else {
        openSearch();
      }
    } else if (e.key === 'Escape') {
      closeSearch();
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createSearchModal);
  } else {
    createSearchModal();
  }
})();
