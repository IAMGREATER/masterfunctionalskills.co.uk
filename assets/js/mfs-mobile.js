/**
 * MASTER FUNCTIONAL SKILLS (UK) — MINIMAL MOBILE & TABLET NAVIGATION ENGINE
 * Controls off-canvas slide-out drawer, touch ergonomics, mobile dyslexia tinting,
 * PWA installation prompt, and smooth mobile scroll helpers.
 * Auto-initializes on all mobile & tablet viewports (< 1025px / touch).
 */
(function() {
  'use strict';

  // Compute Root Path dynamically so drawer links resolve cleanly from subdirectories
  var ROOT_PATH = (function() {
    var p = window.location.pathname;
    if (p.includes('/worksheets/') || p.includes('/topics/')) {
      return '../';
    }
    return '';
  })();

  function getDrawerHtml(root) {
    return `
    <div id="mfsDrawerBackdrop" class="mfs-drawer-backdrop"></div>
    <aside id="mfsMobileDrawer" class="mfs-mobile-drawer" aria-label="Mobile Navigation Drawer">
      <!-- Drawer Header with Safe-Area Padding -->
      <div class="mfs-drawer-header">
        <a href="${root}index.html" class="mfs-drawer-brand">
          <div class="mfs-brand-icon" style="width:28px; height:28px; font-size:0.85rem;"><i class="fa-solid fa-graduation-cap"></i></div>
          <span>MFS Navigation</span>
        </a>
        <button type="button" class="mfs-drawer-close" id="mfsDrawerCloseBtn" aria-label="Close menu">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- PWA Install Prompt Card (Visible when installable) -->
      <div id="mfsDrawerInstallBox" class="mfs-drawer-install-box" style="display:none;">
        <button type="button" class="btn-drawer-install" onclick="window.__mfsTriggerInstall && window.__mfsTriggerInstall()">
          <i class="fa-solid fa-mobile-screen-button"></i>
          <span>Install MFS App on Phone</span>
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
            <a href="${root}functional-skills-maths-level-2.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Maths Level 2</a>
            <a href="${root}functional-skills-maths-level-1.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Maths Level 1</a>
            <a href="${root}entry-level-3-maths.html" class="mfs-drawer-sublink"><i class="fa-solid fa-calculator" style="margin-right:6px; color:#0284c7;"></i> Entry Level 3 Maths</a>
            <a href="${root}functional-skills-english-level-2.html" class="mfs-drawer-sublink"><i class="fa-solid fa-pen-nib" style="margin-right:6px; color:#7c3aed;"></i> English Level 2</a>
            <a href="${root}functional-skills-english-level-1.html" class="mfs-drawer-sublink"><i class="fa-solid fa-pen-nib" style="margin-right:6px; color:#7c3aed;"></i> English Level 1</a>
            <a href="${root}digital-functional-skills-level-1.html" class="mfs-drawer-sublink"><i class="fa-solid fa-laptop-code" style="margin-right:6px; color:#0891b2;"></i> Digital Skills Level 1</a>
            <a href="${root}entry-level-3-digital-skills.html" class="mfs-drawer-sublink"><i class="fa-solid fa-laptop-code" style="margin-right:6px; color:#0891b2;"></i> Digital Skills Entry 3</a>
            <a href="${root}digital-functional-skills.html" class="mfs-drawer-sublink"><i class="fa-solid fa-laptop-code" style="margin-right:6px; color:#0891b2;"></i> Digital Skills Hub</a>
            <a href="${root}revise.html" class="mfs-drawer-sublink" style="font-weight:700; color:#0284c7;">View All Subjects &rarr;</a>
          </div>
        </div>

        <!-- Past Papers -->
        <div class="mfs-drawer-item">
          <a href="${root}functional-skills-past-papers.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-regular fa-file-lines"></i>
              <span>Past Papers &amp; Models</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Worksheets -->
        <div class="mfs-drawer-item">
          <a href="${root}worksheets.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-layer-group"></i>
              <span>Worksheets Directory</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Revision Cards -->
        <div class="mfs-drawer-item">
          <a href="${root}revision-cards.html" class="mfs-drawer-link">
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
            <a href="${root}pass-mark-calculator.html" class="mfs-drawer-sublink">Pass Mark Calculator</a>
            <a href="${root}diagnostic-test.html" class="mfs-drawer-sublink">Diagnostic Skill Checker</a>
            <a href="${root}functional-skills-nets.html" class="mfs-drawer-sublink">3D Net Folding Tool</a>
            <a href="${root}video-solution.html" class="mfs-drawer-sublink">Video Walkthrough Station</a>
            <a href="${root}tools.html" class="mfs-drawer-sublink" style="font-weight:700; color:#0284c7;">All Tools &rarr;</a>
          </div>
        </div>

        <!-- Online Courses -->
        <div class="mfs-drawer-item">
          <a href="${root}courses.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-graduation-cap"></i>
              <span>Online Courses</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Shop -->
        <div class="mfs-drawer-item">
          <a href="${root}shop.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-basket-shopping" style="color:#d97706;"></i>
              <span>Revision Books Shop</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>

        <!-- Contact Us -->
        <div class="mfs-drawer-item">
          <a href="${root}contact-us.html" class="mfs-drawer-link">
            <div class="mfs-drawer-link-left">
              <i class="fa-solid fa-envelope"></i>
              <span>Contact &amp; Support</span>
            </div>
            <i class="fa-solid fa-arrow-right" style="font-size:0.75rem; color:#94a3b8;"></i>
          </a>
        </div>
      </nav>

      <!-- Drawer Footer CTA with Safe-Area Padding -->
      <div class="mfs-drawer-footer">
        <a href="${root}exams.html" class="btn-drawer-exam">
          <i class="fa-solid fa-calendar-check"></i> Book Official Exam (£149)
        </a>
      </div>
    </aside>
    <!-- Floating Back to Top Pill -->
    <button type="button" id="mfsScrollTopBtn" class="mfs-scroll-top-btn" aria-label="Scroll back to top" title="Back to top">
      <i class="fa-solid fa-arrow-up"></i>
    </button>
    `;
  }

  function initMobileNav() {
    // 1. Ensure Drawer markup exists in DOM
    if (!document.getElementById('mfsMobileDrawer')) {
      var wrapper = document.createElement('div');
      wrapper.innerHTML = getDrawerHtml(ROOT_PATH).trim();
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
    var scrollTopBtn = document.getElementById('mfsScrollTopBtn');

    function openDrawer() {
      if (!drawer || !backdrop) return;
      drawer.classList.add('active');
      backdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
      syncTintUI();
      // Check install prompt state
      if (window.__mfsInstallPrompt) {
        var installContainer = document.getElementById('mfsDrawerInstallBox');
        if (installContainer) installContainer.style.display = 'block';
      }
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

    // Auto-close drawer when any link is clicked
    if (drawer) {
      var drawerLinks = drawer.querySelectorAll('.mfs-drawer-nav a, .mfs-drawer-footer a');
      for (var i = 0; i < drawerLinks.length; i++) {
        drawerLinks[i].addEventListener('click', function() {
          closeDrawer();
        });
      }
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

    // Floating Back to Top Button Listener
    if (scrollTopBtn) {
      window.addEventListener('scroll', function() {
        if (window.pageYOffset > 350) {
          scrollTopBtn.classList.add('visible');
        } else {
          scrollTopBtn.classList.remove('visible');
        }
      }, { passive: true });

      scrollTopBtn.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }

    // Initialize Mobile Footer Accordions
    initMobileFooter();

    // Initialize Mobile Responsive Tables Engine
    initResponsiveTables();

    // Initialize PFS-Style Mobile Collapses, Dropdowns & Sub-Menus
    initPfsMobileComponents();
  }

  /**
   * PFS Mobile Collapses, Resource Dropdowns & Mega-Menu Accordion Controller
   * Supports [data-toggle="collapse"], [data-toggle="dropdown"], and .hs-has-sub-menu
   * across both MFS and PFS-cloned page templates.
   */
  function initPfsMobileComponents() {
    // 1. [data-toggle="collapse"] handler (FAQ accordions, Worked Examples, #navBar)
    var collapseBtns = document.querySelectorAll('[data-toggle="collapse"]');
    collapseBtns.forEach(function(btn) {
      if (btn.__mfsCollapseBound) return;
      btn.__mfsCollapseBound = true;
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        var targetSel = btn.getAttribute('data-target') || btn.getAttribute('href');
        if (!targetSel || targetSel === '#') return;
        var target = document.querySelector(targetSel);
        if (!target) return;

        var isShown = target.classList.contains('show');
        if (isShown) {
          target.classList.remove('show');
          btn.classList.add('collapsed');
          btn.setAttribute('aria-expanded', 'false');
        } else {
          target.classList.add('show');
          btn.classList.remove('collapsed');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });

    // 2. [data-toggle="dropdown"] handler (PFS Mobile "Choose Resource" dropdowns)
    var dropdownBtns = document.querySelectorAll('[data-toggle="dropdown"]');
    dropdownBtns.forEach(function(btn) {
      if (btn.__mfsDropdownBound) return;
      btn.__mfsDropdownBound = true;
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var menu = btn.nextElementSibling;
        if (!menu) return;
        var isOpen = menu.classList.contains('show');
        document.querySelectorAll('.dropdown-menu.show').forEach(function(m) {
          m.classList.remove('show');
          m.style.display = '';
        });
        if (!isOpen) {
          menu.classList.add('show');
          menu.style.display = 'block';
          btn.setAttribute('aria-expanded', 'true');
        } else {
          btn.setAttribute('aria-expanded', 'false');
        }
      });
    });

    // Close open dropdowns when tapping outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.dropdown, [data-toggle="dropdown"]')) {
        document.querySelectorAll('.dropdown-menu.show').forEach(function(m) {
          m.classList.remove('show');
          m.style.display = '';
        });
      }
    });
  }

  /**
   * Mobile Portrait Responsive Tables Engine
   * Ensures no table has data cut off or requires horizontal side-scrolling.
   * Automatically extracts column headers and sets data-label on every td,
   * pushing column data onto clean stacked lines in portrait mobile view.
   */
  function initResponsiveTables() {
    var tables = document.querySelectorAll('table');
    if (!tables || tables.length === 0) return;

    for (var t = 0; t < tables.length; t++) {
      var table = tables[t];

      // Check if explicitly marked as a matrix grid
      var isMatrix = table.classList.contains('math-matrix-table') || 
                     table.classList.contains('keep-table-grid');

      // Extract column headers
      var headers = [];
      var ths = table.querySelectorAll('thead th, tr:first-child th');
      if (ths.length > 0) {
        for (var h = 0; h < ths.length; h++) {
          headers.push(ths[h].textContent.replace(/\s+/g, ' ').trim());
        }
      }

      // Populate data-label attributes on every td
      var rows = table.querySelectorAll('tbody tr');
      if (rows.length === 0) {
        var allRows = table.querySelectorAll('tr');
        if (allRows.length > 1 && allRows[0].querySelector('th')) {
          rows = Array.prototype.slice.call(allRows, 1);
        }
      }

      if (rows.length > 0 && headers.length > 0) {
        for (var r = 0; r < rows.length; r++) {
          var tds = rows[r].querySelectorAll('td');
          for (var d = 0; d < tds.length; d++) {
            if (headers[d] && !tds[d].getAttribute('data-label')) {
              tds[d].setAttribute('data-label', headers[d]);
            }
          }
        }
      }

      // If not marked as a matrix grid, ensure table-stack-mobile is added
      if (!isMatrix) {
        table.classList.add('table-stack-mobile');
      }

      // Defeat any parent horizontal scroll clipping
      var parent = table.parentElement;
      if (parent) {
        if (parent.classList.contains('table-responsive') || 
            parent.classList.contains('boundaries-table-wrap') ||
            parent.classList.contains('comparison-table-container') ||
            (parent.style && (parent.style.overflowX === 'auto' || parent.style.overflowX === 'scroll'))) {
          parent.style.overflowX = 'visible';
        }
      }
    }
  }

  /**
   * Mobile Footer Accordion Engine
   * Collapses bulky link columns into tap-to-expand compact cards on mobile.
   */
  function initMobileFooter() {
    var footer = document.querySelector('.mfs-footer');
    if (!footer) return;
    var cols = footer.querySelectorAll('.footer-col, .footer-links-col');
    if (!cols || cols.length === 0) return;

    for (var i = 0; i < cols.length; i++) {
      var col = cols[i];
      if (col.classList.contains('footer-brand') || col.querySelector('.mfs-brand')) {
        continue;
      }

      var h4 = col.querySelector('h4');
      var links = col.querySelector('.footer-links, ul');
      if (!h4 || !links) continue;

      col.classList.add('mfs-footer-accordion');
      if (!h4.querySelector('.mfs-footer-chevron')) {
        var chevron = document.createElement('i');
        chevron.className = 'fa-solid fa-chevron-down mfs-footer-chevron';
        h4.appendChild(chevron);
      }

      h4.setAttribute('role', 'button');
      h4.setAttribute('tabindex', '0');
      h4.setAttribute('aria-expanded', 'false');

      (function(c, heading) {
        function toggle(e) {
          if (e) e.preventDefault();
          var isOpen = c.classList.toggle('is-open');
          heading.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        }

        heading.onclick = toggle;
        heading.onkeydown = function(e) {
          if (e.key === 'Enter' || e.key === ' ') {
            toggle(e);
          }
        };
      })(col, h4);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();
