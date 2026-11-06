/**
 * Master Functional Skills (MFS) - Digital Skills Dedicated Revision Engine
 * Handles Dyslexia Tints, Fluency Drills, Auto-Saving Scratchpads & Solution Drawers.
 */

(function () {
  'use strict';

  // --------------------------------------------------------------------------
  // 1. Dyslexia Background Tint & Font Mode System
  // --------------------------------------------------------------------------
  function initTint() {
    const savedTint = localStorage.getItem('mfs_site_tint') || 'cream';
    applyTint(savedTint);

    const savedDyslexia = localStorage.getItem('mfs_dyslexia_mode') === 'true';
    if (savedDyslexia) {
      document.body.classList.add('dyslexia-mode');
    }

    // Close menu when clicking outside
    document.addEventListener('click', function (e) {
      const menu = document.getElementById('tintMenu');
      const toggle = document.getElementById('tintToggle');
      if (menu && menu.classList.contains('show') && !menu.contains(e.target) && !toggle.contains(e.target)) {
        menu.classList.remove('show');
      }
    });
  }

  function applyTint(tint) {
    document.documentElement.setAttribute('data-tint', tint);
    document.body.setAttribute('data-tint', tint);
    localStorage.setItem('mfs_site_tint', tint);

    const swatchMap = {
      cream: '#fdfbf7',
      peach: '#fff7ed',
      cool: '#f0f9ff',
      sage: '#f0fdf4',
      none: '#ffffff'
    };

    const labelMap = {
      cream: 'Cream Tint',
      peach: 'Soft Peach',
      cool: 'Cool Mist',
      sage: 'Soft Sage',
      none: 'No Tint'
    };

    const indicator = document.getElementById('tintCurrentSwatch');
    if (indicator) {
      indicator.style.backgroundColor = swatchMap[tint] || '#fdfbf7';
    }

    const label = document.getElementById('tintLabel');
    if (label) {
      label.textContent = labelMap[tint] || 'Cream Tint';
    }

    document.querySelectorAll('.tint-option-btn').forEach(btn => {
      if (btn.getAttribute('data-tint') === tint) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  window.setSiteTint = function (tint, event) {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    applyTint(tint);
    const menu = document.getElementById('tintMenu');
    if (menu) menu.classList.remove('show');
  };

  window.toggleTintMenu = function (event) {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    const menu = document.getElementById('tintMenu');
    if (menu) {
      menu.classList.toggle('show');
    }
  };

  window.toggleDyslexiaMode = function () {
    const isDyslexia = document.body.classList.toggle('dyslexia-mode');
    localStorage.setItem('mfs_dyslexia_mode', isDyslexia ? 'true' : 'false');
  };

  // --------------------------------------------------------------------------
  // 2. Interactive Fluency Drill Evaluator
  // --------------------------------------------------------------------------
  window.checkDrill = function (btn, isCorrect, feedbackId) {
    const parentContainer = btn.closest('.dfs-drill-options');
    if (!parentContainer) return;

    // Prevent repeated clicking
    const allButtons = parentContainer.querySelectorAll('.dfs-drill-opt-btn');
    allButtons.forEach(b => {
      b.disabled = true;
      b.style.cursor = 'default';
    });

    const feedbackBox = document.getElementById(feedbackId);

    if (isCorrect) {
      btn.classList.add('correct');
      if (feedbackBox) {
        feedbackBox.className = 'dfs-drill-feedback show correct';
        feedbackBox.innerHTML = `<strong><i class="fa-solid fa-circle-check"></i> Correct!</strong> ` + feedbackBox.getAttribute('data-explanation');
      }
    } else {
      btn.classList.add('incorrect');
      // Highlight the correct answer for clarity
      allButtons.forEach(b => {
        if (b.getAttribute('data-correct') === 'true') {
          b.classList.add('correct');
        }
      });
      if (feedbackBox) {
        feedbackBox.className = 'dfs-drill-feedback show incorrect';
        feedbackBox.innerHTML = `<strong><i class="fa-solid fa-circle-xmark"></i> Not quite.</strong> ` + feedbackBox.getAttribute('data-explanation');
      }
    }
  };

  // --------------------------------------------------------------------------
  // 3. Auto-Saving Learner Scratchpad (localStorage)
  // --------------------------------------------------------------------------
  function initScratchpads() {
    const pads = document.querySelectorAll('.dfs-scratchpad-area');
    pads.forEach(pad => {
      const storageKey = pad.getAttribute('data-storage-key') || 'dfs_scratch_' + window.location.pathname;
      const statusIndicator = pad.closest('.dfs-scratchpad-wrap')?.querySelector('.dfs-autosave-status');

      // Restore saved content
      const savedText = localStorage.getItem(storageKey);
      if (savedText) {
        pad.value = savedText;
      }

      // Auto-save on typing (debounced)
      let debounceTimer;
      pad.addEventListener('input', function () {
        if (statusIndicator) {
          statusIndicator.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="color:#d97706;"></i> Saving...';
        }
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(function () {
          localStorage.setItem(storageKey, pad.value);
          if (statusIndicator) {
            statusIndicator.innerHTML = '<i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Saved in browser';
          }
        }, 500);
      });
    });
  }

  // --------------------------------------------------------------------------
  // 4. Model Solution & Mark Scheme Drawer Toggle
  // --------------------------------------------------------------------------
  window.toggleSolutionDrawer = function (drawerId, btnId) {
    const drawer = document.getElementById(drawerId);
    const btn = document.getElementById(btnId);
    if (!drawer) return;

    drawer.classList.toggle('open');
    const isOpen = drawer.classList.contains('open');

    if (btn) {
      if (isOpen) {
        btn.innerHTML = '<i class="fa-solid fa-chevron-up"></i> Hide Model Solution & Marking Criteria';
        btn.style.background = '#334155';
      } else {
        btn.innerHTML = '<i class="fa-solid fa-chevron-down"></i> View Accredited Model Solution & Mark Scheme';
        btn.style.background = '#0f172a';
      }
    }
  };

  // --------------------------------------------------------------------------
  // Initialize on DOM Ready
  // --------------------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', function () {
    initTint();
    initScratchpads();
  });
})();
