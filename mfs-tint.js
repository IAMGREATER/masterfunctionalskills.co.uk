/**
 * MASTER FUNCTIONAL SKILLS (UK) — DYSLEXIA READING TINT ENGINE
 * Soft glare-reduction background tints (Default: Light Cream, Peach, Cool Mist, Sage, No Tint)
 * Accessible via top navigation bar & subtle floating pill across all pages.
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
    cream: { name: 'Cream', swatch: '#faf8f2', border: '#e6dfd1', isDefault: true },
    peach: { name: 'Soft Peach', swatch: '#fdf6ee', border: '#ead9c7' },
    cool:  { name: 'Cool Mist', swatch: '#f1f6fa', border: '#cfe0ec' },
    sage:  { name: 'Soft Sage', swatch: '#f2f7f3', border: '#d0e3d4' },
    none:  { name: 'No Tint', swatch: '#ffffff', border: '#cbd5e1', isNone: true }
  };

  function getSavedTint() {
    var saved = localStorage.getItem('mfs_tint');
    if (saved && TINTS[saved]) {
      return saved;
    }
    return 'cream'; // Default is very light cream tint for dyslexia-friendly reading
  }

  function applyTint(tintKey, save) {
    if (!TINTS[tintKey]) tintKey = 'cream';
    if (save !== false) {
      try {
        localStorage.setItem('mfs_tint', tintKey);
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

    // Update Top Bar elements if present
    var label = document.getElementById('tintLabel');
    if (label) {
      label.textContent = tintKey === 'none' ? 'No Tint' : (TINTS[tintKey].name + ' Tint');
    }
    var currentSwatch = document.getElementById('tintCurrentSwatch');
    if (currentSwatch) {
      currentSwatch.style.background = TINTS[tintKey].swatch;
      currentSwatch.style.borderColor = tintKey === 'none' ? '#cbd5e1' : 'rgba(255,255,255,0.85)';
    }

    // Update Floating Pill elements if present
    var floatSwatch = document.getElementById('floatTintSwatch');
    if (floatSwatch) {
      floatSwatch.style.background = TINTS[tintKey].swatch;
      floatSwatch.style.borderColor = tintKey === 'none' ? '#cbd5e1' : 'rgba(0,0,0,0.18)';
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

  // Floating widget removed per user request (kept in top navigation bar only)
  function ensureFloatingWidget() {
    var existing = document.getElementById('floatingTintWidget');
    if (existing) existing.remove();
  }

  // ==========================================================================
  // THEME ENGINE (Matched to Official Subject & Level Book Accents)
  // ==========================================================================
  function getSavedTheme() {
    var docTheme = document.documentElement.getAttribute('data-theme');
    // If this page specifically sets a curriculum subject theme (maths, english, digital, etc.), honor it
    if (docTheme) {
      return docTheme;
    }
    var saved = localStorage.getItem('mfs_theme');
    var validThemes = ['maths', 'english', 'digital', 'sapphire', 'emerald', 'crimson', 'teal', 'oxford-blue', 'violet', 'cyan'];
    if (saved && validThemes.includes(saved)) {
      return saved;
    }
    return 'maths'; // Default is Maths Sapphire
  }

  function applyTheme(themeKey, save) {
    var validThemes = ['maths', 'english', 'digital', 'sapphire', 'emerald', 'crimson', 'teal', 'oxford-blue', 'violet', 'cyan'];
    if (!validThemes.includes(themeKey)) themeKey = 'maths';
    if (save !== false) {
      try {
        localStorage.setItem('mfs_theme', themeKey);
      } catch (e) {}
    }
    document.documentElement.setAttribute('data-theme', themeKey);
    var lbl = document.getElementById('themeLabel');
    if (lbl) {
      var nameMap = {
        'maths': 'Maths (Sapphire)',
        'english': 'English (Violet)',
        'digital': 'Digital (Cyan)',
        'sapphire': 'Sapphire',
        'emerald': 'Emerald',
        'crimson': 'Crimson',
        'teal': 'Teal',
        'oxford-blue': 'Oxford Blue',
        'violet': 'Violet',
        'cyan': 'Cyan'
      };
      lbl.textContent = nameMap[themeKey] || 'Theme';
    }
    var toggleBtn = document.getElementById('themeToggle');
    if (toggleBtn) {
      toggleBtn.title = 'Current Theme: ' + themeKey;
    }
  }

  window.toggleTheme = function(ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    var current = document.documentElement.getAttribute('data-theme') || getSavedTheme();
    var next = current === 'emerald' ? 'sapphire' : 'emerald';
    applyTheme(next, true);
  };

  // Early execution to eliminate any flash of unstyled tint or theme
  var initialTint = getSavedTint();
  document.documentElement.setAttribute('data-tint', initialTint);

  var initialTheme = getSavedTheme();
  document.documentElement.setAttribute('data-theme', initialTheme);

  // Auto-load Global Instant Search engine (Ctrl+K)
  if (!document.getElementById('mfsSearchScript')) {
    var searchScript = document.createElement('script');
    searchScript.id = 'mfsSearchScript';
    searchScript.src = 'assets/js/mfs-search.js';
    document.head.appendChild(searchScript);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      ensureFloatingWidget();
      applyTint(initialTint, false);
      applyTheme(initialTheme, false);
    });
  } else {
    ensureFloatingWidget();
    applyTint(initialTint, false);
    applyTheme(initialTheme, false);
  }
})();
