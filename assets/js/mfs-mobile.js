/**
 * MASTER FUNCTIONAL SKILLS (UK) — MINIMAL MOBILE & TABLET NAVIGATION ENGINE
 * Controls off-canvas slide-out drawer, touch ergonomics, and mobile dyslexia tinting.
 * Auto-initializes on all mobile & tablet viewports (< 992px).
 */
(function() {
  'use strict';

  var DRAWER_HTML = `
    <div id="mfsDrawerBackdrop" class="mfs-drawer-backdrop"></div>
    <aside id="mfsMobileDrawer" class="mfs-mobile-drawer" aria-label="Mobile Navigation Drawer">
      <!-- Drawer Header -->
      <div class="mfs-drawer-header">
        <a href="index.html" class="mfs-drawer-brand">
          <div class="mfs-brand-icon" style="width:28px; height:28px; font-size:0.85rem;"><i class="fa-solid fa-graduation-cap"></i></div>
          <span>MFS Navigation</span>
        </a>
        <button type="button" class="mfs-drawer-close" id="mfsDrawerCloseBtn" aria-label="Close menu">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Dyslexia & Accessibility Quick Switcher -->
      <div class="mfs-drawer-dyslexia">
        <div class="mfs-drawer-dyslexia-head">
          <span><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</span>
          <span id="mfsDrawerTintCurrent" style="font-weight:700; color:#0284c7;">Cream</span>
        </div>
        <div class="mfs-drawer-tints-grid">
          <button type="button" class="mfs-drawer-tint-chip" data-tint="cream">
            <span class="chip-dot" style="background:#faf4e6;"></span>
            <span>Cream</span>
          </button>
          <button type="button" class="mfs-drawer-tint-chip" data-tint="peach">
            <span class="chip-dot" style="background:#ffe8d6;"></span>
            <span>Peach</span>
          </button>
          <button type="button" class="mfs-drawer-tint-chip" data-tint="cool">
            <span class="chip-dot" style="background:#e3f0f9;"></span>
            <span>Cool</span>
          </button>
          <button type="button" class="mfs-drawer-tint-chip" data-tint="sage">
            <span class="chip-dot" style="background:#e3eee5;"></span>
            <span>Sage</span>
          </button>
          <button type="button" class="mfs-drawer-tint-chip" data-tint="none">
            <span class="chip-dot" style="background:#ffffff; border-style:dashed;"></span>
            <span>White</span>
          </button>
        </div>
        <button type="button" class="mfs-drawer-dyslexia-toggle-btn" id="mfsDrawerDyslexiaToggle">
          <i class="fa-solid fa-universal-access"></i> High-Readability Mode
        </button>
      </div>

      <!-- Navigation Links -->
      <nav class="mfs-drawer-nav">
        <!-- Subjects Collapsible -->
        <div class="mfs-drawer-item" id="drawerItemSubjects">
          <div class="mfs-drawer-link" onclick="window.__mfsToggleSublist('drawerItemSubjects')">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-book-open-reader"></i>
              <span>Subjects &amp; Levels</span>
            </div>
            <i class="fa-solid fa-chevron-down mfs-drawer-chevron"></i>
          </div>
          <div class="mfs-drawer-sublist">
            <a href="functional-skills-maths-level-2.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Maths Level 2</a>
            <a href="functional-skills-maths-level-1.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Maths Level 1</a>
            <a href="entry-level-3-maths.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Entry Level 3 Maths</a>
            <a href="functional-skills-english-level-2.html" class="mfs-drawer-sublink"><i class="fa-solid fa-pen-nib" style="margin-right:6px; color:#7c3aed;"></i> English Level 2</a>
            <a href="functional-skills-english-level-1.html" class="mfs-drawer-sublink"><i class="fa-solid fa-pen-nib" style="margin-right:6px; color:#7c3aed;"></i> English Level 1</a>
            <a href="digital-functional-skills.html" class="mfs-drawer-sublink"><i class="fa-solid fa-laptop-code" style="margin-right:6px; color:#059669;"></i> Digital Skills Hub</a>
            <a href="revise.html" class="mfs-drawer-sublink" style="font-weight:700; color:#0284c7;">View All Subjects &rarr;</a>
          </div>
        </div>

        <!-- Past Papers -->
        <div class="mfs-drawer-item">
          <a href="functional-skills-past-papers.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-regular fa-file-lines"></i>
              <span>Past Papers &amp; Models</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Worksheets -->
        <div class="mfs-drawer-item">
          <a href="worksheets.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-layer-group"></i>
              <span>Worksheets Directory</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Revision Cards -->
        <div class="mfs-drawer-item">
          <a href="revision-cards.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-clone" style="color:#d97706;"></i>
              <span style="color:#b45309; font-weight:700;">Revision Cards</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Free Tools Collapsible -->
        <div class="mfs-drawer-item" id="drawerItemTools">
          <div class="mfs-drawer-link" onclick="window.__mfsToggleSublist('drawerItemTools')">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-screwdriver-wrench"></i>
              <span>Free Tools &amp; Simulators</span>
            </div>
            <i class="fa-solid fa-chevron-down mfs-drawer-chevron"></i>
          </div>
          <div class="mfs-drawer-sublist">
            <a href="pass-mark-calculator.html" class="mfs-drawer-sublink">Pass Mark Calculator</a>
            <a href="diagnostic-test.html" class="mfs-drawer-sublink">Diagnostic Skill Checker</a>
            <a href="functional-skills-nets.html" class="mfs-drawer-sublink">3D Net Folding Tool</a>
            <a href="video-solution.html" class="mfs-drawer-sublink">Video Walkthrough Station</a>
            <a href="tools.html" class="mfs-drawer-sublink" style="font-weight:700; color:#0284c7;">All Tools &rarr;</a>
          </div>
        </div>

        <!-- Online Courses -->
        <div class="mfs-drawer-item">
          <a href="courses.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-graduation-cap"></i>
              <span>Online Courses</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Shop -->
        <div class="mfs-drawer-item">
          <a href="shop.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-basket-shopping" style="color:#d97706;"></i>
              <span>Revision Books Shop</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Contact Us -->
        <div class="mfs-drawer-item">
          <a href="contact-us.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-envelope"></i>
              <span>Contact &amp; Support</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>
      </nav>

      <!-- Drawer Footer CTA -->
      <div class="mfs-drawer-footer">
        <a href="exams.html" class="btn-drawer-exam">
          <i class="fa-solid fa-calendar-check"></i> Book Official Exam (£149)
        </a>
      </div>
    </aside>
  `;

  function initMobileNav() {
    // 1. Ensure Drawer markup exists in DOM
    if (!document.getElementById('mfsMobileDrawer')) {
      var wrapper = document.createElement('div');
      wrapper.innerHTML = DRAWER_HTML.trim();
      while (wrapper.firstChild) {
        document.body.appendChild(wrapper.firstChild);
      }
    }

    // 2. Ensure Mobile Controls exist in .mfs-navbar-inner
    var navInner = document.querySelector('.mfs-navbar-inner');
    if (navInner && !document.getElementById('mfsMobileControls')) {
      var controls = document.createElement('div');
      controls.id = 'mfsMobileControls';
      controls.className = 'mfs-mobile-controls';
      controls.innerHTML = `
        <button type="button" class="btn-mobile-tint-toggle" id="mfsMobileTintBtn" title="Change Reading Tint" aria-label="Reading Tint">
          <i class="fa-solid fa-glasses"></i>
          <span class="mobile-tint-swatch" id="mfsMobileTintSwatch"></span>
        </button>
        <button type="button" class="mfs-menu-pill" id="mfsMobileToggleBtn" title="Open Navigation Menu" aria-label="Toggle Menu">
          <i class="fa-solid fa-bars"></i>
          <span>Menu</span>
        </button>
      `;
      navInner.appendChild(controls);
    }

    var drawer = document.getElementById('mfsMobileDrawer');
    var backdrop = document.getElementById('mfsDrawerBackdrop');
    var toggleBtn = document.getElementById('mfsMobileToggleBtn');
    var closeBtn = document.getElementById('mfsDrawerCloseBtn');
    var tintBtn = document.getElementById('mfsMobileTintBtn');

    function openDrawer() {
      if (!drawer || !backdrop) return;
      drawer.classList.add('active');
      backdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
      syncTintUI();
    }

    function closeDrawer() {
      if (!drawer || !backdrop) return;
      drawer.classList.remove('active');
      backdrop.classList.remove('active');
      document.body.style.overflow = '';
    }

    if (toggleBtn) {
      toggleBtn.addEventListener('click', function(e) {
        e.preventDefault();
        openDrawer();
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        closeDrawer();
      });
    }

    if (backdrop) {
      backdrop.addEventListener('click', function(e) {
        e.preventDefault();
        closeDrawer();
      });
    }

    // Quick Tint button in mobile header opens drawer to tint section
    if (tintBtn) {
      tintBtn.addEventListener('click', function(e) {
        e.preventDefault();
        openDrawer();
      });
    }

    // Escape key closes drawer
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc') {
        closeDrawer();
      }
    });

    // Touch swipe right to dismiss drawer
    var touchStartX = 0;
    var touchStartY = 0;
    if (drawer) {
      drawer.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }, { passive: true });

      drawer.addEventListener('touchend', function(e) {
        var diffX = e.changedTouches[0].screenX - touchStartX;
        var diffY = Math.abs(e.changedTouches[0].screenY - touchStartY);
        if (diffX > 60 && diffY < 50) {
          closeDrawer();
        }
      }, { passive: true });
    }

    // Sublist toggle helper
    window.__mfsToggleSublist = function(itemId) {
      var item = document.getElementById(itemId);
      if (item) {
        item.classList.toggle('open');
      }
    };

    // Tint Buttons inside drawer
    var tintChips = document.querySelectorAll('.mfs-drawer-tint-chip');
    tintChips.forEach(function(chip) {
      chip.addEventListener('click', function() {
        var tintKey = chip.getAttribute('data-tint');
        if (window.setSiteTint) {
          window.setSiteTint(tintKey);
        } else {
          document.documentElement.setAttribute('data-tint', tintKey);
          localStorage.setItem('mfs_tint', tintKey);
        }
        syncTintUI();
      });
    });

    // Dyslexia mode toggle inside drawer
    var dysToggle = document.getElementById('mfsDrawerDyslexiaToggle');
    if (dysToggle) {
      dysToggle.addEventListener('click', function() {
        if (window.toggleDyslexiaMode) {
          window.toggleDyslexiaMode();
        } else {
          document.body.classList.toggle('dyslexia-mode');
        }
        syncTintUI();
      });
    }

    function syncTintUI() {
      var curTint = document.documentElement.getAttribute('data-tint') || localStorage.getItem('mfs_tint') || 'cream';
      var tintNameElem = document.getElementById('mfsDrawerTintCurrent');
      var names = { cream: 'Cream', peach: 'Peach', cool: 'Cool', sage: 'Sage', none: 'White' };
      var colors = { cream: '#faf4e6', peach: '#ffe8d6', cool: '#e3f0f9', sage: '#e3eee5', none: '#ffffff' };
      if (tintNameElem) {
        tintNameElem.textContent = names[curTint] || 'Cream';
      }

      var mobileSwatch = document.getElementById('mfsMobileTintSwatch');
      if (mobileSwatch) {
        mobileSwatch.style.background = colors[curTint] || '#faf4e6';
      }

      tintChips.forEach(function(c) {
        if (c.getAttribute('data-tint') === curTint) {
          c.classList.add('active');
        } else {
          c.classList.remove('active');
        }
      });

      var isDys = document.body.classList.contains('dyslexia-mode') || localStorage.getItem('mfs_dyslexia') === '1';
      if (dysToggle) {
        if (isDys) {
          dysToggle.classList.add('active');
        } else {
          dysToggle.classList.remove('active');
        }
      }
    }

    // Initial sync
    syncTintUI();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();
