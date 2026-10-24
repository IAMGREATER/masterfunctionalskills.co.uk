/**
 * MASTER FUNCTIONAL SKILLS (UK) — DYSLEXIA ACCESSIBILITY & TINT ENGINE
 * Glare-reduction background tints: Cream (#faf4e6), Soft Peach (#ffe8d6), Cool Mist (#e3f0f9), Soft Sage (#e3eee5), No Tint (#ffffff)
 * Controls top access bar: [⚪ Tint ⌵] [🚹 Dyslexia] [🎨 Sapphire] across all pages.
 */
(function() {
  'use strict';

  // Expose global tint variables so onclick calls like setSiteTint(peach, event) or setSiteTint('peach', event) both work
  window.cream = 'cream';
  window.peach = 'peach';
  window.cool = 'cool';
  window.sage = 'sage';
  window.none = 'none';

  var TINTS = {
    cream: { name: 'Cream', swatch: '#faf4e6', border: '#e6dfd1', isDefault: true },
    peach: { name: 'Soft Peach', swatch: '#ffe8d6', border: '#f0bca0' },
    cool:  { name: 'Cool Mist', swatch: '#e3f0f9', border: '#bedcf0' },
    sage:  { name: 'Soft Sage', swatch: '#e3eee5', border: '#bcdcc1' },
    none:  { name: 'No Tint', swatch: '#ffffff', border: '#cbd5e1', isNone: true }
  };

  function getSavedTint() {
    var saved = localStorage.getItem('mfs_tint') || localStorage.getItem('mfs_user_tint');
    if (saved && TINTS[saved]) {
      return saved;
    }
    return 'cream'; // Default is calming light cream tint
  }

  function applyTint(tintKey, save) {
    if (!TINTS[tintKey]) tintKey = 'cream';
    if (save !== false) {
      try {
        localStorage.setItem('mfs_tint', tintKey);
        localStorage.setItem('mfs_user_tint', tintKey);
      } catch (e) {}
    }

    // Apply attribute to html and class to body
    document.documentElement.setAttribute('data-tint', tintKey);
    if (document.body) {
      Object.keys(TINTS).forEach(function(k) {
        document.body.classList.remove('tint-' + k);
      });
      document.body.classList.add('tint-' + tintKey);
    }

    // Update Top Bar elements
    var label = document.getElementById('tintLabel');
    if (label) {
      label.textContent = tintKey === 'none' ? 'No Tint' : (TINTS[tintKey].name + ' Tint');
    }
    var currentSwatch = document.getElementById('tintCurrentSwatch');
    if (currentSwatch) {
      currentSwatch.style.background = TINTS[tintKey].swatch;
      currentSwatch.style.borderColor = TINTS[tintKey].border;
    }

    // Update Floating Pill elements if present
    var floatSwatch = document.getElementById('floatTintSwatch');
    if (floatSwatch) {
      floatSwatch.style.background = TINTS[tintKey].swatch;
      floatSwatch.style.borderColor = TINTS[tintKey].border;
    }
    var floatText = document.getElementById('floatTintText');
    if (floatText) {
      floatText.textContent = tintKey === 'none' ? 'No Tint' : (TINTS[tintKey].name + ' Tint');
    }

    // Update active state in all tint menus
    document.querySelectorAll('.tint-option-btn').forEach(function(btn) {
      var bTint = btn.getAttribute('data-tint');
      if (bTint === tintKey) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  window.setSiteTint = function(tintKey, ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    applyTint(tintKey, true);
    closeAllTintMenus();
  };

  window.toggleTintMenu = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var menu = document.getElementById('tintMenu');
    if (menu) {
      var isShow = menu.classList.contains('show');
      closeAllTintMenus();
      if (!isShow) menu.classList.add('show');
    }
  };

  window.toggleFloatingTintMenu = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var menu = document.getElementById('floatingTintMenu');
    if (menu) {
      var isShow = menu.classList.contains('show');
      closeAllTintMenus();
      if (!isShow) menu.classList.add('show');
    }
  };

  window.quickToggleTint = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var current = getSavedTint();
    var next = current === 'none' ? 'cream' : 'none';
    applyTint(next, true);
  };

  function closeAllTintMenus() {
    document.querySelectorAll('.tint-picker-menu').forEach(function(m) {
      m.classList.remove('show');
    });
  }

  // Dismiss on clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.mfs-tint-dropdown-wrap') && !e.target.closest('.mfs-floating-tint-wrap')) {
      closeAllTintMenus();
    }
  });

  // Dismiss on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      closeAllTintMenus();
    }
  });

  function ensureFloatingWidget() {
    var existing = document.getElementById('floatingTintWidget');
    if (existing) existing.remove();
  }

  // ==========================================================================
  // DYSLEXIA HIGH-READABILITY MODE
  // ==========================================================================
  function applyDyslexiaMode(enabled, save) {
    if (save !== false) {
      try {
        localStorage.setItem('mfs_dyslexia_mode', enabled ? 'true' : 'false');
      } catch (e) {}
    }
    if (enabled) {
      document.documentElement.setAttribute('data-dyslexia', 'true');
      if (document.body) document.body.classList.add('dyslexia-mode');
    } else {
      document.documentElement.removeAttribute('data-dyslexia');
      if (document.body) document.body.classList.remove('dyslexia-mode');
    }
    var btn = document.getElementById('dyslexiaToggle');
    if (btn) {
      if (enabled) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }
  }

  window.toggleDyslexiaMode = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var isCurrentlyOn = document.documentElement.getAttribute('data-dyslexia') === 'true' ||
                        (document.body && document.body.classList.contains('dyslexia-mode'));
    applyDyslexiaMode(!isCurrentlyOn, true);
  };

  // ==========================================================================
  // THEME ENGINE (Subject Suites & Palette Modes)
  // ==========================================================================
  function getSavedTheme() {
    var docTheme = document.documentElement.getAttribute('data-theme');
    // If page explicitly declares a subject theme, respect it unconditionally
    if (docTheme && (docTheme === 'english' || docTheme === 'maths' || docTheme === 'digital' || docTheme === 'violet' || docTheme === 'cyan')) {
      return docTheme;
    }
    var saved = localStorage.getItem('mfs_theme');
    if (saved && (saved === 'emerald' || saved === 'sapphire' || saved === 'crimson' || saved === 'teal' || saved === 'oxford-blue')) {
      return saved;
    }
    return docTheme || 'sapphire';
  }

  function applyTheme(themeKey, save) {
    var validThemes = ['sapphire', 'emerald', 'crimson', 'teal', 'oxford-blue', 'english', 'maths', 'digital', 'violet', 'cyan'];
    if (!validThemes.includes(themeKey)) themeKey = 'sapphire';
    if (save !== false && themeKey !== 'english' && themeKey !== 'maths' && themeKey !== 'digital') {
      try {
        localStorage.setItem('mfs_theme', themeKey);
      } catch (e) {}
    }
    document.documentElement.setAttribute('data-theme', themeKey);
    var lbl = document.getElementById('themeLabel');
    if (lbl) {
      var nameMap = {
        'sapphire': 'Sapphire',
        'emerald': 'Emerald',
        'crimson': 'Crimson',
        'teal': 'Teal',
        'oxford-blue': 'Oxford Blue',
        'english': 'English',
        'maths': 'Maths',
        'digital': 'Digital'
      };
      lbl.textContent = nameMap[themeKey] || 'Palette';
    }
    var toggleBtn = document.getElementById('themeToggle');
    if (toggleBtn) {
      toggleBtn.title = 'Switch Palette: ' + (themeKey === 'emerald' ? 'Sapphire' : 'Emerald');
    }
  }

  window.toggleTheme = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var current = document.documentElement.getAttribute('data-theme') || getSavedTheme();
    var orig = document.documentElement.getAttribute('data-orig-theme') || (current === 'english' || current === 'maths' || current === 'digital' ? current : 'sapphire');
    var next = (current === 'emerald') ? orig : 'emerald';
    applyTheme(next, true);
  };

  // ==========================================================================
  // GLOBAL SEARCH SHORTCUT (Ctrl+K)
  // ==========================================================================
  window.openGlobalSearch = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    if (window.MfsSearch && typeof window.MfsSearch.open === 'function') {
      window.MfsSearch.open();
    } else {
      var q = prompt('Search Functional Skills revision topics & resources:');
      if (q && q.trim()) {
        window.location.href = 'revise.html?q=' + encodeURIComponent(q.trim());
      }
    }
  };

  // Early execution to eliminate any flash of unstyled tint or theme
  var initialTint = getSavedTint();
  document.documentElement.setAttribute('data-tint', initialTint);

  var pageDeclaredTheme = document.documentElement.getAttribute('data-theme');
  if (pageDeclaredTheme) {
    document.documentElement.setAttribute('data-orig-theme', pageDeclaredTheme);
  }
  var initialTheme = getSavedTheme();
  document.documentElement.setAttribute('data-theme', initialTheme);

  var initialDyslexia = localStorage.getItem('mfs_dyslexia_mode') === 'true';
  if (initialDyslexia) {
    document.documentElement.setAttribute('data-dyslexia', 'true');
  }

  // Auto-load Global Instant Search engine (Ctrl+K)
  if (!document.getElementById('mfsSearchScript')) {
    var searchScript = document.createElement('script');
    searchScript.id = 'mfsSearchScript';
    searchScript.src = 'assets/js/mfs-search.js';
    document.head.appendChild(searchScript);
  }

  function initTouchDropdowns() {
    if (window.__MFS_TOUCH_DROPDOWNS_INIT) return;
    window.__MFS_TOUCH_DROPDOWNS_INIT = true;

    function isTouchInteraction(e) {
      if (e && (e.pointerType === 'touch' || e.pointerType === 'pen')) return true;
      if (window.matchMedia && window.matchMedia('(hover: none)').matches) return true;
      if (window.innerWidth <= 1080) return true;
      return false;
    }

    function closeAllDropdowns(exceptItem) {
      var openItems = document.querySelectorAll('.mfs-nav-item.open');
      for (var i = 0; i < openItems.length; i++) {
        if (openItems[i] !== exceptItem) {
          openItems[i].classList.remove('open');
          var link = openItems[i].querySelector('.mfs-nav-link');
          if (link) link.setAttribute('aria-expanded', 'false');
        }
      }
    }

    function adjustDropdownPosition(dropdown) {
      if (!dropdown || window.innerWidth <= 991) return;
      dropdown.style.left = '';
      dropdown.style.right = '';
      var rect = dropdown.getBoundingClientRect();
      var vw = window.innerWidth;
      if (rect.right > vw - 12) {
        var overflowX = rect.right - (vw - 12);
        dropdown.style.left = (-overflowX) + 'px';
      }
    }

    document.addEventListener('click', function(e) {
      var navLink = e.target.closest('.mfs-nav-item > .mfs-nav-link');
      var navItem = navLink ? navLink.closest('.mfs-nav-item') : null;
      var dropdown = navItem ? navItem.querySelector('.mfs-dropdown-menu') : null;

      if (navLink && dropdown) {
        if (isTouchInteraction(e)) {
          var isOpen = navItem.classList.contains('open');
          e.preventDefault();
          e.stopPropagation();

          if (isOpen) {
            navItem.classList.remove('open');
            navLink.setAttribute('aria-expanded', 'false');
          } else {
            closeAllDropdowns(navItem);
            navItem.classList.add('open');
            navLink.setAttribute('aria-expanded', 'true');
            adjustDropdownPosition(dropdown);
          }
          return;
        }
      }

      if (!e.target.closest('.mfs-nav-item')) {
        closeAllDropdowns(null);
      }
    });

    document.addEventListener('touchstart', function(e) {
      if (!e.target.closest('.mfs-navbar')) {
        closeAllDropdowns(null);
      }
    }, { passive: true });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc') {
        closeAllDropdowns(null);
      }
    });

    window.addEventListener('resize', function() {
      if (window.innerWidth > 1080) {
        closeAllDropdowns(null);
      }
    }, { passive: true });
  }

  function initDOM() {
    ensureFloatingWidget();
    applyTint(initialTint, false);
    applyTheme(initialTheme, false);
    if (initialDyslexia) {
      applyDyslexiaMode(true, false);
    }
    initTouchDropdowns();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDOM);
  } else {
    initDOM();
  }
})();
