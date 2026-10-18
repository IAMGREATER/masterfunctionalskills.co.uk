/**
 * Master Functional Skills - Unified Revision Interactive Scripts
 * Handles Dyslexia Tints, High-Readability Mode, Sidebar TOC ScrollSpy,
 * Solution Drawer Toggles, and Scratchpad Persistence.
 */

// Expose global tint variables so onclick calls like setSiteTint(peach, event) or setSiteTint('peach', event) both work
window.cream = 'cream';
window.peach = 'peach';
window.cool = 'cool';
window.sage = 'sage';
window.none = 'none';

var MFS_TINTS = {
  cream: { name: 'Cream', swatch: '#faf4e6', border: '#e6dfd1', isDefault: true },
  peach: { name: 'Soft Peach', swatch: '#ffe8d6', border: '#f0bca0' },
  cool:  { name: 'Cool Mist', swatch: '#e3f0f9', border: '#bedcf0' },
  sage:  { name: 'Soft Sage', swatch: '#e3eee5', border: '#bcdcc1' },
  none:  { name: 'No Tint', swatch: '#ffffff', border: '#cbd5e1', isNone: true }
};

// Toggle Practice Question Solution Drawer
function toggleSolution(drawerId, btnElement) {
  const drawer = document.getElementById(drawerId);
  if (!drawer) return;

  // Find the button that triggered this
  let btn = btnElement;
  if (!btn && typeof event !== 'undefined' && event && event.target) {
    btn = event.target.closest('button');
  }
  if (!btn) {
    btn = document.querySelector(`button[onclick*="${drawerId}"]`);
  }

  const isHidden = drawer.style.display === 'none' || getComputedStyle(drawer).display === 'none';

  if (isHidden) {
    drawer.style.display = 'block';
    drawer.classList.add('open');
    if (btn) {
      btn.innerHTML = '<i class="fa-solid fa-eye-slash"></i> Hide Solution';
      btn.setAttribute('aria-expanded', 'true');
    }
  } else {
    drawer.style.display = 'none';
    drawer.classList.remove('open');
    if (btn) {
      btn.innerHTML = '<i class="fa-solid fa-eye"></i> Show Solution';
      btn.setAttribute('aria-expanded', 'false');
    }
  }
}

// Aliases for compatibility
window.toggleSolution = toggleSolution;
window.toggleSolutionDrawer = toggleSolution;

// Toggle Tint Menu
function toggleTintMenu(e) {
  if (e && e.stopPropagation) e.stopPropagation();
  const menu = document.getElementById('tintMenu');
  if (menu) {
    menu.classList.toggle('show');
  }
}
window.toggleTintMenu = toggleTintMenu;

// Set Dyslexia Tint
function setSiteTint(tintName, e) {
  if (e && e.stopPropagation) e.stopPropagation();
  if (!MFS_TINTS[tintName]) tintName = 'cream';

  try {
    localStorage.setItem('mfs_tint', tintName);
    localStorage.setItem('mfs_user_tint', tintName);
  } catch (err) {}

  document.documentElement.setAttribute('data-tint', tintName);
  if (document.body) {
    Object.keys(MFS_TINTS).forEach(function(k) {
      document.body.classList.remove('tint-' + k);
    });
    document.body.classList.add('tint-' + tintName);
  }
  
  const label = document.getElementById('tintLabel');
  if (label) {
    label.textContent = tintName === 'none' ? 'No Tint' : (MFS_TINTS[tintName].name + ' Tint');
  }

  const currentSwatch = document.getElementById('tintCurrentSwatch');
  if (currentSwatch) {
    currentSwatch.style.background = MFS_TINTS[tintName].swatch;
    currentSwatch.style.borderColor = tintName === 'none' ? '#cbd5e1' : 'rgba(255,255,255,0.85)';
  }

  // Update active button state
  document.querySelectorAll('.tint-option-btn').forEach(btn => {
    if (btn.getAttribute('data-tint') === tintName) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  const menu = document.getElementById('tintMenu');
  if (menu) menu.classList.remove('show');
}
window.setSiteTint = setSiteTint;

// Close tint menu on click outside
document.addEventListener('click', function(e) {
  const menu = document.getElementById('tintMenu');
  const toggle = document.getElementById('tintToggle');
  if (menu && menu.classList.contains('show')) {
    if (!menu.contains(e.target) && (!toggle || !toggle.contains(e.target))) {
      menu.classList.remove('show');
    }
  }
});

// Toggle Dyslexia High-Readability Mode
function toggleDyslexiaMode() {
  const isCurrentlyOn = document.documentElement.getAttribute('data-dyslexia') === 'true' ||
                        (document.body && document.body.classList.contains('dyslexia-mode'));
  const nextState = !isCurrentlyOn;

  if (nextState) {
    document.documentElement.setAttribute('data-dyslexia', 'true');
    if (document.body) document.body.classList.add('dyslexia-mode');
    try { localStorage.setItem('mfs_dyslexia_mode', 'true'); } catch (e) {}
  } else {
    document.documentElement.removeAttribute('data-dyslexia');
    if (document.body) document.body.classList.remove('dyslexia-mode');
    try { localStorage.setItem('mfs_dyslexia_mode', 'false'); } catch (e) {}
  }

  const btn = document.getElementById('dyslexiaToggle');
  if (btn) {
    if (nextState) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  }
}
window.toggleDyslexiaMode = toggleDyslexiaMode;

// Toggle Theme (Subject Palette vs Emerald)
function toggleTheme(ev) {
  if (ev && ev.stopPropagation) ev.stopPropagation();
  const current = document.documentElement.getAttribute('data-theme') || 'sapphire';
  const orig = document.documentElement.getAttribute('data-orig-theme') || (current === 'english' || current === 'maths' || current === 'digital' ? current : 'sapphire');
  const next = (current === 'emerald') ? orig : 'emerald';
  document.documentElement.setAttribute('data-theme', next);
  if (next === 'emerald' || next === 'sapphire') {
    try { localStorage.setItem('mfs_theme', next); } catch (e) {}
  }
  const label = document.getElementById('themeLabel');
  if (label) {
    label.textContent = next.charAt(0).toUpperCase() + next.slice(1);
  }
  const toggleBtn = document.getElementById('themeToggle');
  if (toggleBtn) {
    toggleBtn.title = 'Switch Palette: ' + (next === 'emerald' ? 'Original Palette' : 'Emerald');
  }
}
window.toggleTheme = toggleTheme;

// Mobile TOC Toggle
function toggleMobileToc() {
  const sidebar = document.getElementById('sidebarNav');
  const btn = document.querySelector('.btn-mobile-toc');
  if (sidebar) {
    const isCurrentlyOpen = sidebar.style.display === 'block' || sidebar.classList.contains('open-mobile') || sidebar.classList.contains('active');
    if (isCurrentlyOpen) {
      sidebar.style.display = 'none';
      sidebar.classList.remove('open-mobile', 'active');
      if (btn) btn.classList.remove('active');
    } else {
      sidebar.style.display = 'block';
      sidebar.classList.add('open-mobile', 'active');
      if (btn) btn.classList.add('active');
    }
  }
}
window.toggleMobileToc = toggleMobileToc;

// Global Search Stub
function openGlobalSearch(ev) {
  if (ev && ev.stopPropagation) ev.stopPropagation();
  if (window.MfsSearch && typeof window.MfsSearch.open === 'function') {
    window.MfsSearch.open();
  } else {
    const q = prompt('Search functional skills revision topics:');
    if (q && q.trim()) {
      window.location.href = 'revise.html?q=' + encodeURIComponent(q.trim());
    }
  }
}
window.openGlobalSearch = openGlobalSearch;

// Scratchpad Autosave
function initScratchpads() {
  const pageKey = window.location.pathname.split('/').pop() || 'revision';
  document.querySelectorAll('.working-scratchpad-input, .practice-scratchpad').forEach((area, idx) => {
    const key = `mfs_scratch_${pageKey}_${idx}`;
    const saved = localStorage.getItem(key);
    if (saved) area.value = saved;
    area.addEventListener('input', () => {
      localStorage.setItem(key, area.value);
    });
  });
}

// Early execution to eliminate flash of unstyled tint or theme
(function() {
  const savedTint = localStorage.getItem('mfs_tint') || localStorage.getItem('mfs_user_tint') || 'cream';
  document.documentElement.setAttribute('data-tint', savedTint);

  const docTheme = document.documentElement.getAttribute('data-theme');
  if (docTheme) {
    document.documentElement.setAttribute('data-orig-theme', docTheme);
  }
  let effectiveTheme = docTheme || 'sapphire';
  if (docTheme && (docTheme === 'english' || docTheme === 'maths' || docTheme === 'digital' || docTheme === 'violet' || docTheme === 'cyan')) {
    effectiveTheme = docTheme;
  } else {
    const savedTheme = localStorage.getItem('mfs_theme');
    if (savedTheme && (savedTheme === 'emerald' || savedTheme === 'sapphire')) {
      effectiveTheme = savedTheme;
    }
  }
  document.documentElement.setAttribute('data-theme', effectiveTheme);

  const savedDyslexia = localStorage.getItem('mfs_dyslexia_mode') === 'true';
  if (savedDyslexia) {
    document.documentElement.setAttribute('data-dyslexia', 'true');
  }
})();

// ScrollSpy & Preferences Init
window.addEventListener('DOMContentLoaded', () => {
  const savedTint = localStorage.getItem('mfs_tint') || localStorage.getItem('mfs_user_tint') || 'cream';
  setSiteTint(savedTint);

  const savedDyslexia = localStorage.getItem('mfs_dyslexia_mode');
  if (savedDyslexia === 'true') {
    document.documentElement.setAttribute('data-dyslexia', 'true');
    if (document.body) document.body.classList.add('dyslexia-mode');
    const dBtn = document.getElementById('dyslexiaToggle');
    if (dBtn) dBtn.classList.add('active');
  }

  const docTheme = document.documentElement.getAttribute('data-theme');
  let effectiveTheme = docTheme || 'sapphire';
  if (docTheme && (docTheme === 'english' || docTheme === 'maths' || docTheme === 'digital' || docTheme === 'violet' || docTheme === 'cyan')) {
    effectiveTheme = docTheme;
  } else {
    const savedTheme = localStorage.getItem('mfs_theme');
    if (savedTheme && (savedTheme === 'emerald' || savedTheme === 'sapphire')) {
      effectiveTheme = savedTheme;
    }
  }
  document.documentElement.setAttribute('data-theme', effectiveTheme);
  const tLabel = document.getElementById('themeLabel');
  if (tLabel) tLabel.textContent = effectiveTheme.charAt(0).toUpperCase() + effectiveTheme.slice(1);

  initScratchpads();

  // ScrollSpy for Left Sidebar TOC
  const sections = document.querySelectorAll('section[id], div[id].revision-section');
  const navLinks = document.querySelectorAll('.sidebar-toc-link');

  if (sections.length > 0 && navLinks.length > 0) {
    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 140;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      if (current) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  // Mobile / Landscape Table of Contents Interactions
  // Mobile & Tablet Landscape Table of Contents Interactions
  const sidebar = document.getElementById('sidebarNav');
  if (sidebar) {
    // Auto-close floating TOC dropdown when any section link is tapped
    sidebar.querySelectorAll('.sidebar-toc-link').forEach(link => {
      link.addEventListener('click', () => {
        const btn = document.querySelector('.btn-mobile-toc');
        const isFloatingDrawer = sidebar.classList.contains('open-mobile') || 
                                 sidebar.classList.contains('active') || 
                                 sidebar.style.display === 'block' ||
                                 (btn && window.getComputedStyle(btn).display !== 'none');
        if (isFloatingDrawer || window.innerWidth <= 1366 || window.innerHeight <= 900) {
          sidebar.style.display = 'none';
          sidebar.classList.remove('open-mobile', 'active');
          if (btn) btn.classList.remove('active');
        }
      });
    });
  }

  // Close floating TOC when tapping outside (supports click & touchstart on iOS/iPadOS/Android)
  function handleOutsideToc(e) {
    const s = document.getElementById('sidebarNav');
    if (!s || (s.style.display !== 'block' && !s.classList.contains('open-mobile') && !s.classList.contains('active'))) return;
    if (!s.contains(e.target) && !e.target.closest('.btn-mobile-toc')) {
      s.style.display = 'none';
      s.classList.remove('open-mobile', 'active');
      const btn = document.querySelector('.btn-mobile-toc');
      if (btn) btn.classList.remove('active');
    }
  }
  document.addEventListener('click', handleOutsideToc);
  document.addEventListener('touchstart', handleOutsideToc, { passive: true });

  // Close floating TOC on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const s = document.getElementById('sidebarNav');
      if (s && (s.style.display === 'block' || s.classList.contains('open-mobile') || s.classList.contains('active'))) {
        s.style.display = 'none';
        s.classList.remove('open-mobile', 'active');
        const btn = document.querySelector('.btn-mobile-toc');
        if (btn) btn.classList.remove('active');
      }
    }
  });

  // Handle window resize / rotation to cleanly restore desktop layout if transitioning to desktop
  window.addEventListener('resize', () => {
    const s = document.getElementById('sidebarNav');
    const btn = document.querySelector('.btn-mobile-toc');
    if (window.innerWidth > 1200 && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      if (s) {
        s.style.display = '';
        s.classList.remove('open-mobile', 'active');
      }
      if (btn) btn.classList.remove('active');
    }
  });
});

// ==========================================================================
// VIDEO EXEMPLAR SUITE CONTROLS
// ==========================================================================
function switchTopicVideo(task) {
  const player = document.getElementById('topicSlcVideoPlayer');
  const source = document.getElementById('topicSlcVideoSource');
  const t1Jumps = document.getElementById('topicTask1Jumps');
  const t2Jumps = document.getElementById('topicTask2Jumps');
  const dlBtn = document.getElementById('topicVideoDownloadBtn');
  const tabs = document.querySelectorAll('.video-exemplar-card .video-tab-btn');

  if (!player || !source) return;

  tabs.forEach(t => t.classList.remove('active'));

  if (task === 'task1') {
    tabs.forEach(t => { if (t.textContent.includes('Task 1')) t.classList.add('active'); });
    source.src = 'assets/video/slc-task1-presentation-model.mp4';
    player.poster = 'assets/img/slc-task1-poster.png';
    if (t1Jumps) t1Jumps.style.display = 'flex';
    if (t2Jumps) t2Jumps.style.display = 'none';
    if (dlBtn) {
      dlBtn.href = 'assets/video/slc-task1-presentation-model.mp4';
      dlBtn.innerHTML = '<i class="fa-solid fa-download"></i> Download Task 1 Video (1080p MP4)';
    }
  } else {
    tabs.forEach(t => { if (t.textContent.includes('Task 2')) t.classList.add('active'); });
    source.src = 'assets/video/slc-task2-discussion-model.mp4';
    player.poster = 'assets/img/slc-task2-poster.png';
    if (t1Jumps) t1Jumps.style.display = 'none';
    if (t2Jumps) t2Jumps.style.display = 'flex';
    if (dlBtn) {
      dlBtn.href = 'assets/video/slc-task2-discussion-model.mp4';
      dlBtn.innerHTML = '<i class="fa-solid fa-download"></i> Download Task 2 Video (1080p MP4)';
    }
  }
  player.load();
  player.play().catch(e => console.log('Autoplay handled:', e));
}

function jumpTopicTo(seconds) {
  const player = document.getElementById('topicSlcVideoPlayer');
  if (!player) return;
  player.currentTime = seconds;
  player.play().catch(e => console.log('Playback error:', e));
}

window.switchTopicVideo = switchTopicVideo;
window.jumpTopicTo = jumpTopicTo;

/* ==========================================================================
   HERO IMAGE FULL-RESOLUTION LIGHTBOX
   ========================================================================== */
document.addEventListener('DOMContentLoaded', function() {
  const heroImgWrap = document.querySelector('.revision-hero-img-wrap');
  if (!heroImgWrap) return;
  const heroImg = heroImgWrap.querySelector('img');
  if (!heroImg) return;

  heroImgWrap.setAttribute('title', 'Click to view full-resolution high-definition visual');

  heroImgWrap.addEventListener('click', function() {
    let overlay = document.getElementById('mfs-image-lightbox');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'mfs-image-lightbox';
      overlay.innerHTML = `
        <div class="mfs-lightbox-backdrop"></div>
        <div class="mfs-lightbox-content">
          <img src="" alt="Full-Resolution Visual" class="mfs-lightbox-img" />
          <button type="button" class="mfs-lightbox-close" aria-label="Close image"><i class="fa-solid fa-xmark"></i></button>
        </div>
      `;
      document.body.appendChild(overlay);

      const closeLightbox = () => {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
      };

      overlay.querySelector('.mfs-lightbox-backdrop').addEventListener('click', closeLightbox);
      overlay.querySelector('.mfs-lightbox-close').addEventListener('click', closeLightbox);
      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && overlay.classList.contains('active')) closeLightbox();
      });
    }

    const img = overlay.querySelector('.mfs-lightbox-img');
    img.src = heroImg.currentSrc || heroImg.src;
    img.alt = heroImg.alt;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  });
});

/* ==========================================================================
   TOUCH & TABLET DROPDOWN NAVIGATION ENGINE (INTEGRATED)
   ========================================================================== */
(function() {
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTouchDropdowns);
  } else {
    initTouchDropdowns();
  }
})();

