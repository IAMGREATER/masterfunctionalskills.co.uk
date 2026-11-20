/**
 * MASTER FUNCTIONAL SKILLS (UK) — GLOBAL INSTANT SEARCH (Ctrl+K / Cmd+K)
 * Full-site searchable directory backed by assets/data/mfs-search-index.json.
 */
(function() {
  'use strict';

  var INDEX_VER = '20261120v11';

  function computeRootPrefix() {
    var scriptEl = document.currentScript || document.querySelector('script[src*="mfs-search.js"]');
    if (scriptEl) {
      var src = scriptEl.getAttribute('src') || '';
      var idx = src.indexOf('assets/js/mfs-search.js');
      if (idx !== -1) {
        return src.slice(0, idx);
      }
    }
    var path = window.location.pathname || '';
    if (path.indexOf('/digital-skills/') !== -1) return '../../';
    if (path.indexOf('/worksheets/') !== -1) return '../';
    return '';
  }

  var ROOT_PREFIX = computeRootPrefix();

  // Lightweight instant fallback until the full JSON index finishes loading
  var CORE_ITEMS = [
    { title: "Online Mock Exam Simulator", cat: "Tool", tier: "tool", url: "online-mock-simulator.html", desc: "Sit timed onscreen Pearson Edexcel, Open Awards & Highfield Functional Skills mocks.", kw: "simulator mock online exam", p: 10 },
    { title: "Masterclass Video Station", cat: "Tool", tier: "tool", url: "video-solution.html", desc: "Watch 161 step-by-step video walkthroughs with interactive Concept Checks.", kw: "video youtube walkthrough masterclass", p: 10 },
    { title: "Functional Skills Past Papers Hub", cat: "Past Papers", tier: "papers", url: "functional-skills-past-papers.html", desc: "Official Edexcel, AQA, NCFE, City & Guilds, Open Awards, TQUK & NOCN papers.", kw: "past papers model solutions mark scheme", p: 10 },
    { title: "Maths Level 2 Revision Hub", cat: "Maths L2", tier: "l2", url: "functional-skills-maths-level-2.html", desc: "44 Level 2 Maths guides, visual calculation boards, worksheets and video walkthroughs.", kw: "maths level 2 l2", p: 10 },
    { title: "Maths Level 1 Revision Hub", cat: "Maths L1", tier: "l1", url: "functional-skills-maths-level-1.html", desc: "38 Level 1 Maths guides, worked models, worksheets and Topic Check quizzes.", kw: "maths level 1 l1", p: 10 },
    { title: "Entry Level 3 Maths Hub", cat: "Maths E3", tier: "e3", url: "entry-level-3-maths.html", desc: "24 Entry Level 3 Maths foundation guides, videos and practice packs.", kw: "maths entry 3 e3", p: 10 },
    { title: "English Level 2 Revision Hub", cat: "English L2", tier: "l2", url: "functional-skills-english-level-2.html", desc: "46 Level 2 Reading, Writing, SPaG and Speaking & Listening revision modules.", kw: "english level 2 l2", p: 10 },
    { title: "English Level 1 Revision Hub", cat: "English L1", tier: "l1", url: "functional-skills-english-level-1.html", desc: "33 Level 1 Reading, Writing and SPaG guides with model answers.", kw: "english level 1 l1", p: 10 },
    { title: "Digital Functional Skills Hub (DFSQ)", cat: "Digital L1", tier: "dfs-l1", url: "digital-functional-skills.html", desc: "Complete Level 1 & Entry 3 Digital Skills guides, interactive labs and mocks.", kw: "dfs digital skills level 1 entry 3", p: 10 },
    { title: "Revision Cards & Printable Flashcards", cat: "Tool", tier: "tool", url: "revision-cards.html", desc: "Interactive flip flashcards and A4/A6 printable revision packs.", kw: "cards flashcards printable", p: 10 },
    { title: "Worksheets & Mark Schemes Directory", cat: "Tool", tier: "tool", url: "worksheets.html", desc: "Downloadable fluency drills, exam-style practice sheets and worked answers.", kw: "worksheets drills answers", p: 10 },
    { title: "Pass Mark & Grade Boundary Calculator", cat: "Tool", tier: "tool", url: "pass-mark-calculator.html", desc: "Check mock scores against official Ofqual boundaries across boards.", kw: "pass mark boundary calculator", p: 10 },
    { title: "Free Diagnostic Skill Checker", cat: "Tool", tier: "tool", url: "diagnostic-test.html", desc: "10-question diagnostic check to pinpoint Entry 3, Level 1 or Level 2 gaps.", kw: "diagnostic initial assessment", p: 10 },
    { title: "BKSB & OneAdvanced Remediation Bridge", cat: "Tool", tier: "tool", url: "bksb-remediation.html", desc: "Targeted skill remediation guides aligned to BKSB and OneAdvanced diagnostics.", kw: "bksb oneadvanced remediation", p: 10 },
    { title: "Open Awards Past Papers & XAMS Mocks", cat: "Past Papers", tier: "papers", url: "open-awards-functional-skills-maths-level-2-past-papers.html", desc: "Open Awards Maths & English Level 1-2 mocks and Model Solutions.", kw: "open awards xams model solutions", p: 5 },
    { title: "Revision Books & Study Shop", cat: "Shop", tier: "course", url: "shop.html", desc: "Complete study handbooks, 5-mock exam packs and revision card bundles.", kw: "shop books handbook", p: 10 }
  ];

  var INDEX_ITEMS = CORE_ITEMS;
  var indexLoaded = false;
  var indexPromise = null;

  function escapeHtml(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function resolveHref(url) {
    var u = String(url || '');
    if (!u || /^(?:https?:|mailto:|tel:|\/|#)/i.test(u)) {
      return u;
    }
    return ROOT_PREFIX + u;
  }

  function updateStatusText() {
    var input = document.getElementById('mfsGlobalSearchInput');
    if (input && indexLoaded) {
      input.placeholder = 'Search ' + INDEX_ITEMS.length + ' topics, past papers, videos & tools (e.g. L1 fractions, Open Awards, spreadsheet)...';
    }
  }

  function loadFullIndex() {
    if (indexLoaded) return Promise.resolve(INDEX_ITEMS);
    if (indexPromise) return indexPromise;
    var url = ROOT_PREFIX + 'assets/data/mfs-search-index.json?v=' + INDEX_VER;
    indexPromise = fetch(url)
      .then(function(res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      })
      .then(function(data) {
        if (Array.isArray(data) && data.length > 0) {
          INDEX_ITEMS = data;
          indexLoaded = true;
          updateStatusText();
          var overlay = document.getElementById('mfsSearchOverlay');
          var input = document.getElementById('mfsGlobalSearchInput');
          if (overlay && overlay.classList.contains('show') && input) {
            renderResults(input.value.trim().toLowerCase());
          }
        }
        return INDEX_ITEMS;
      })
      .catch(function() {
        return INDEX_ITEMS;
      });
    return indexPromise;
  }

  function scoreItem(item, tokens, rawQuery) {
    var title = (item.title || '').toLowerCase();
    var cat = (item.cat || '').toLowerCase();
    var desc = (item.desc || '').toLowerCase();
    var kw = (item.kw || '').toLowerCase();
    var url = (item.url || '').toLowerCase();
    var haystack = title + ' ' + cat + ' ' + desc + ' ' + kw + ' ' + url;

    for (var i = 0; i < tokens.length; i++) {
      if (haystack.indexOf(tokens[i]) === -1) return -1;
    }

    var score = Number(item.p) || 1;
    if (title === rawQuery) score += 200;
    else if (title.indexOf(rawQuery) === 0) score += 120;
    else if (title.indexOf(rawQuery) !== -1) score += 70;

    for (var j = 0; j < tokens.length; j++) {
      var tok = tokens[j];
      if (title.indexOf(tok) !== -1) score += 30;
      if (cat.indexOf(tok) !== -1) score += 20;
      if (kw.indexOf(tok) !== -1) score += 12;
      if (desc.indexOf(tok) !== -1) score += 6;
    }
    return score;
  }

  function createSearchModal() {
    if (document.getElementById('mfsSearchOverlay')) return;

    var style = document.createElement('style');
    style.id = 'mfsSearchStyles';
    style.textContent =
      '#mfsSearchOverlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(7, 13, 30, 0.65); backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); z-index: 999999; display: none; align-items: flex-start; justify-content: center; padding-top: 10vh; }' +
      '#mfsSearchOverlay.show { display: flex !important; }' +
      '.mfs-search-box { width: 92%; max-width: 680px; background: var(--surface, #ffffff); border-radius: 18px; box-shadow: 0 20px 50px rgba(7, 13, 30, 0.25); border: 1px solid var(--border, #e2e8f0); overflow: hidden; display: flex; flex-direction: column; max-height: 78vh; animation: mfsSearchPop 0.18s cubic-bezier(0.16, 1, 0.3, 1); }' +
      '@keyframes mfsSearchPop { from { opacity: 0; transform: scale(0.96) translateY(-8px); } to { opacity: 1; transform: scale(1) translateY(0); } }' +
      '.mfs-search-input-wrap { display: flex; align-items: center; padding: 16px 20px; border-bottom: 1px solid var(--border, #e2e8f0); background: var(--bg, #faf8f2); }' +
      '.mfs-search-input-wrap i { color: var(--accent, #00b87c); font-size: 1.15rem; margin-right: 14px; flex-shrink: 0; }' +
      '#mfsGlobalSearchInput { border: none; background: transparent; font-size: 1.02rem; font-family: inherit; width: 100%; color: var(--navy-dark, #070d1e); outline: none; }' +
      '.mfs-search-close-btn { border: none; background: transparent; color: var(--text-muted, #64748b); font-size: 1.1rem; cursor: pointer; padding: 4px 8px; border-radius: 6px; margin-left: 8px; }' +
      '.mfs-search-close-btn:hover { background: rgba(15, 23, 42, 0.08); color: var(--navy-dark, #070d1e); }' +
      '.mfs-search-results { overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 4px; }' +
      '.mfs-search-result-item { display: flex; align-items: center; justify-content: space-between; padding: 11px 14px; border-radius: 10px; text-decoration: none; color: inherit; transition: background 0.15s ease; border: 1px solid transparent; gap: 10px; }' +
      '.mfs-search-result-item:hover, .mfs-search-result-item.highlighted { background: var(--bg, #f4efe6); border-color: var(--border, #e6dfd1); }' +
      '.mfs-search-item-info { flex-grow: 1; min-width: 0; }' +
      '.mfs-search-item-title { font-weight: 700; font-size: 0.94rem; color: var(--navy, #0b1528); margin-bottom: 2px; }' +
      '.mfs-search-item-desc { font-size: 0.8rem; color: var(--text-muted, #64748b); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }' +
      '.mfs-search-item-badge { font-size: 0.69rem; font-weight: 800; padding: 3px 9px; border-radius: 100px; text-transform: uppercase; white-space: nowrap; flex-shrink: 0; background: #e0f2fe; color: #0369a1; }' +
      '.mfs-search-item-badge.tier-l1 { background: #dcfce7; color: #15803d; border: 1px solid #86efac; }' +
      '.mfs-search-item-badge.tier-l2 { background: #fef3c7; color: #b45309; border: 1px solid #fcd34d; }' +
      '.mfs-search-item-badge.tier-e3, .mfs-search-item-badge.tier-dfs-e3 { background: #ccfbf1; color: #0f766e; border: 1px solid #5eead4; }' +
      '.mfs-search-item-badge.tier-dfs-l1 { background: #e0e7ff; color: #4338ca; border: 1px solid #a5b4fc; }' +
      '.mfs-search-item-badge.tier-papers, .mfs-search-item-badge.tier-tool, .mfs-search-item-badge.tier-course { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }' +
      '.mfs-search-footer { padding: 10px 18px; border-top: 1px solid var(--border, #e2e8f0); font-size: 0.76rem; color: var(--text-muted, #64748b); display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap; background: var(--bg, #faf8f2); }' +
      '.search-kbd { background: #ffffff; border: 1px solid var(--border, #cbd5e1); border-radius: 4px; padding: 2px 6px; font-weight: 700; font-size: 0.72rem; color: #0f172a; }' +
      'html[data-tint="cream"] .mfs-search-box { background: #faf4e6; } html[data-tint="cream"] .mfs-search-input-wrap, html[data-tint="cream"] .mfs-search-footer { background: #f3ead6; }' +
      'html[data-tint="peach"] .mfs-search-box { background: #ffe8d6; } html[data-tint="peach"] .mfs-search-input-wrap, html[data-tint="peach"] .mfs-search-footer { background: #fbd9be; }' +
      'html[data-tint="cool"] .mfs-search-box { background: #e3f0f9; } html[data-tint="cool"] .mfs-search-input-wrap, html[data-tint="cool"] .mfs-search-footer { background: #d2e6f5; }' +
      'html[data-tint="sage"] .mfs-search-box { background: #e3eee5; } html[data-tint="sage"] .mfs-search-input-wrap, html[data-tint="sage"] .mfs-search-footer { background: #d4e4d7; }' +
      'html[data-dyslexia="true"] .mfs-search-box { letter-spacing: 0.03em; word-spacing: 0.08em; line-height: 1.75; }' +
      'html[data-dyslexia="true"] .mfs-search-item-title { font-size: 1rem; }';
    document.head.appendChild(style);

    var overlay = document.createElement('div');
    overlay.id = 'mfsSearchOverlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Search Functional Skills topics, past papers and tools');
    overlay.innerHTML =
      '<div class="mfs-search-box">' +
        '<div class="mfs-search-input-wrap">' +
          '<i class="fa-solid fa-magnifying-glass"></i>' +
          '<input type="text" id="mfsGlobalSearchInput" placeholder="Search topics, past papers, videos &amp; tools (e.g. L1 fractions, Open Awards)..." autocomplete="off">' +
          '<button type="button" class="mfs-search-close-btn" id="mfsSearchCloseBtn" aria-label="Close search">&times;</button>' +
        '</div>' +
        '<div class="mfs-search-results" id="mfsSearchResults"></div>' +
        '<div class="mfs-search-footer">' +
          '<span id="mfsSearchCount">' + INDEX_ITEMS.length + ' quick links ready</span>' +
          '<span><span class="search-kbd">↑</span> <span class="search-kbd">↓</span> <span class="search-kbd">Enter</span> &bull; <span class="search-kbd">Esc</span></span>' +
        '</div>' +
      '</div>';

    overlay.addEventListener('click', function(ev) {
      if (ev.target === overlay) closeSearch();
    });

    document.body.appendChild(overlay);

    var closeBtn = document.getElementById('mfsSearchCloseBtn');
    if (closeBtn) {
      closeBtn.addEventListener('click', closeSearch);
    }

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
        var target = current || items[0];
        if (target && target.getAttribute('href')) {
          window.location.href = target.getAttribute('href');
        }
      }
    });
  }

  function renderResults(rawQ) {
    var container = document.getElementById('mfsSearchResults');
    var countEl = document.getElementById('mfsSearchCount');
    if (!container) return;

    var q = (rawQ || '').trim().toLowerCase();
    var matches = [];

    if (!q) {
      matches = INDEX_ITEMS.slice().sort(function(a, b) {
        return (Number(b.p) || 1) - (Number(a.p) || 1);
      });
    } else {
      var tokens = q.split(/\s+/).filter(Boolean);
      var scored = [];
      for (var i = 0; i < INDEX_ITEMS.length; i++) {
        var sc = scoreItem(INDEX_ITEMS[i], tokens, q);
        if (sc >= 0) {
          scored.push({ item: INDEX_ITEMS[i], score: sc });
        }
      }
      scored.sort(function(a, b) {
        if (b.score !== a.score) return b.score - a.score;
        return (a.item.title || '').localeCompare(b.item.title || '');
      });
      matches = scored.map(function(s) { return s.item; });
    }

    if (countEl) {
      if (!q) {
        countEl.textContent = indexLoaded
          ? (INDEX_ITEMS.length + ' topics, past papers & tools indexed')
          : 'Loading full ' + INDEX_ITEMS.length + '+ page directory...';
      } else {
        countEl.textContent = matches.length === 0
          ? '0 matches'
          : ('Showing ' + Math.min(matches.length, 20) + ' of ' + matches.length + ' matches');
      }
    }

    if (matches.length === 0) {
      container.innerHTML =
        '<div style="padding: 24px; text-align: center; color: var(--text-muted, #64748b); font-size: 0.92rem;">' +
        'No matching topics or papers found for "<strong>' + escapeHtml(q) + '</strong>". Try <em>L1 fractions</em>, <em>Open Awards</em>, or <em>spreadsheet</em>.' +
        '</div>';
      return;
    }

    var html = '';
    matches.slice(0, 20).forEach(function(item, i) {
      var isHl = i === 0 ? ' highlighted' : '';
      var tierCls = item.tier ? (' tier-' + escapeHtml(item.tier)) : '';
      html +=
        '<a href="' + escapeHtml(resolveHref(item.url)) + '" class="mfs-search-result-item' + isHl + '">' +
          '<div class="mfs-search-item-info">' +
            '<div class="mfs-search-item-title">' + escapeHtml(item.title) + '</div>' +
            '<div class="mfs-search-item-desc">' + escapeHtml(item.desc) + '</div>' +
          '</div>' +
          '<span class="mfs-search-item-badge' + tierCls + '">' + escapeHtml(item.cat) + '</span>' +
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
      if (input) {
        input.value = '';
        renderResults('');
        setTimeout(function() { input.focus(); }, 50);
      }
      loadFullIndex();
    }
  }

  function closeSearch() {
    var overlay = document.getElementById('mfsSearchOverlay');
    if (overlay) {
      overlay.classList.remove('show');
    }
  }

  window.MfsSearch = {
    open: openSearch,
    close: closeSearch,
    loadIndex: loadFullIndex
  };
  window.openGlobalSearch = openSearch;
  window.closeGlobalSearch = closeSearch;

  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
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
