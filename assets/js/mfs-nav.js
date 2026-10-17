/**
 * MASTER FUNCTIONAL SKILLS (UK) — TOUCH & TABLET DROPDOWN NAVIGATION ENGINE
 * Flawless navigation on iPad, Android tablets, touchscreens & desktop browsers:
 * - On touch/tablet: tapping 'Subjects' or 'Online Courses' toggles the dropdown smoothly.
 * - Prevents immediate href page unload on the first tap.
 * - Preserves desktop mouse hover interactions.
 * - Auto-aligns dropdown within the screen viewport to prevent clipping.
 * - Closes open menus on outside tap, swipe/scroll, or Escape key.
 * - Tapping any link inside the dropdown navigates immediately.
 */
(function() {
  'use strict';

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
      // On landscape tablets / laptops (>991px), ensure dropdown never overflows viewport right edge
      dropdown.style.left = '';
      dropdown.style.right = '';
      var rect = dropdown.getBoundingClientRect();
      var vw = window.innerWidth;
      if (rect.right > vw - 12) {
        var overflowX = rect.right - (vw - 12);
        dropdown.style.left = (-overflowX) + 'px';
      }
    }

    // Handle click / tap on nav links
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

      // Tapping outside navbar closes all dropdowns
      if (!e.target.closest('.mfs-nav-item')) {
        closeAllDropdowns(null);
      }
    });

    // Dismiss dropdown when scrolling or touching outside navbar
    document.addEventListener('touchstart', function(e) {
      if (!e.target.closest('.mfs-navbar')) {
        closeAllDropdowns(null);
      }
    }, { passive: true });

    // Escape key closes dropdowns
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' || e.key === 'Esc') {
        closeAllDropdowns(null);
      }
    });

    // Clean up on resize
    window.addEventListener('resize', function() {
      if (window.innerWidth > 1080) {
        closeAllDropdowns(null);
      }
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTouchDropdowns);
  } else {
    initTouchDropdowns();
  }

  window.initTouchDropdowns = initTouchDropdowns;
})();
