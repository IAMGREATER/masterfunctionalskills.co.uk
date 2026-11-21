/**
 * Master Functional Skills - Unified Revision Interactive Scripts
 * Handles Dyslexia Tints, High-Readability Mode, Sidebar TOC ScrollSpy,
 * Solution Drawer Toggles, and Scratchpad Persistence.
 */

// Resolve relative root prefix dynamically so root & nested (/digital-skills/*/) pages load links cleanly
const _mfsRevScript = document.currentScript || document.querySelector('script[src*="mfs-revision.js"]');
const MFS_REV_ROOT = (_mfsRevScript && _mfsRevScript.getAttribute('src'))
  ? _mfsRevScript.getAttribute('src').replace(/assets\/js\/mfs-revision\.js.*$/, '')
  : '';
var MFS_STEALTH_PREVIEW = true; // Toggled by scripts/toggle_public_seo.py

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

  // Find the button that triggered this (supports DOM node or string element ID)
  let btn = (typeof btnElement === 'string') ? document.getElementById(btnElement) : btnElement;
  if (!btn && typeof event !== 'undefined' && event && event.target) {
    btn = event.target.closest('button');
  }
  if (!btn) {
    btn = document.querySelector(`button[onclick*="${drawerId}"]`);
  }

  const isHidden = !drawer.classList.contains('open') && (drawer.style.display === 'none' || getComputedStyle(drawer).display === 'none');
  const isDfsBtn = Boolean(btn && btn.classList.contains('dfs-solution-toggle-btn'));

  if (isHidden) {
    drawer.style.display = 'block';
    drawer.classList.add('open');
    if (btn) {
      btn.innerHTML = isDfsBtn
        ? '<i class="fa-solid fa-chevron-up"></i> Hide Model Solution &amp; Marking Criteria'
        : '<i class="fa-solid fa-eye-slash"></i> Hide Solution';
      btn.setAttribute('aria-expanded', 'true');
    }
  } else {
    drawer.style.display = 'none';
    drawer.classList.remove('open');
    if (btn) {
      btn.innerHTML = isDfsBtn
        ? '<i class="fa-solid fa-chevron-down"></i> View Accredited Model Solution &amp; Mark Scheme'
        : '<i class="fa-solid fa-eye"></i> Show Solution';
      btn.setAttribute('aria-expanded', 'false');
    }
  }
}

// Aliases for compatibility
window.toggleSolution = toggleSolution;
window.toggleSolutionDrawer = toggleSolution;

// Interactive DFS Fluency Drill Evaluator
window.checkDrill = function (btn, isCorrect, feedbackId) {
  const parentContainer = btn && btn.closest ? btn.closest('.dfs-drill-options') : null;
  if (!parentContainer) return;

  const allButtons = parentContainer.querySelectorAll('.dfs-drill-opt-btn');
  allButtons.forEach(b => {
    b.disabled = true;
    b.style.cursor = 'default';
  });

  const feedbackBox = document.getElementById(feedbackId);
  const explanation = feedbackBox ? (feedbackBox.getAttribute('data-explanation') || '') : '';

  if (isCorrect) {
    btn.classList.add('correct');
    if (feedbackBox) {
      feedbackBox.className = 'dfs-drill-feedback show correct';
      feedbackBox.innerHTML = '<strong><i class="fa-solid fa-circle-check"></i> Correct!</strong> ' + explanation;
    }
  } else {
    btn.classList.add('incorrect');
    allButtons.forEach(b => {
      if (b.getAttribute('data-correct') === 'true') {
        b.classList.add('correct');
      }
    });
    if (feedbackBox) {
      feedbackBox.className = 'dfs-drill-feedback show incorrect';
      feedbackBox.innerHTML = '<strong><i class="fa-solid fa-circle-xmark"></i> Not quite.</strong> ' + explanation;
    }
  }
};

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

// Global Search Launcher (loads full index overlay without window.prompt fallback)
function openGlobalSearch(ev) {
  if (ev && ev.stopPropagation) ev.stopPropagation();
  if (window.MfsSearch && typeof window.MfsSearch.open === 'function') {
    window.MfsSearch.open();
    return;
  }
  var existing = document.getElementById('mfsSearchScript');
  if (existing) {
    existing.addEventListener('load', function() {
      if (window.MfsSearch && typeof window.MfsSearch.open === 'function') {
        window.MfsSearch.open();
      }
    }, { once: true });
    return;
  }
  var s = document.createElement('script');
  s.id = 'mfsSearchScript';
  s.src = MFS_REV_ROOT + 'assets/js/mfs-search.js?v=20261120v12';
  s.onload = function() {
    if (window.MfsSearch && typeof window.MfsSearch.open === 'function') {
      window.MfsSearch.open();
    }
  };
  document.head.appendChild(s);
}
window.openGlobalSearch = openGlobalSearch;

if (!document.getElementById('mfsSearchScript') && !window.MfsSearch) {
  var autoSearchScript = document.createElement('script');
  autoSearchScript.id = 'mfsSearchScript';
  autoSearchScript.src = MFS_REV_ROOT + 'assets/js/mfs-search.js?v=20261120v12';
  document.head.appendChild(autoSearchScript);
}

function mfsInitStealthGate() {
  if (!MFS_STEALTH_PREVIEW || document.getElementById('mfsPrivateGateScript')) return;
  var gateScript = document.createElement('script');
  gateScript.id = 'mfsPrivateGateScript';
  gateScript.src = MFS_REV_ROOT + 'assets/js/mfs-private-gate.js?v=20261120v12';
  (document.body || document.head).appendChild(gateScript);
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', mfsInitStealthGate);
} else {
  mfsInitStealthGate();
}

// Scratchpad Autosave (unified across Maths, English & Digital Functional Skills)
function initScratchpads() {
  const pageKey = window.location.pathname.split('/').pop() || 'revision';
  document.querySelectorAll('.working-scratchpad-input, .practice-scratchpad, .dfs-scratchpad-area').forEach((area, idx) => {
    const key = area.getAttribute('data-storage-key') || `mfs_scratch_${pageKey}_${idx}`;
    const wrap = area.closest('.dfs-scratchpad-wrap');
    const statusIndicator = wrap ? wrap.querySelector('.dfs-autosave-status') : null;
    try {
      const saved = localStorage.getItem(key);
      if (saved) area.value = saved;
    } catch (e) {}
    let timer;
    area.addEventListener('input', () => {
      if (statusIndicator) {
        statusIndicator.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="color:#d97706;"></i> Saving...';
      }
      clearTimeout(timer);
      timer = setTimeout(() => {
        try { localStorage.setItem(key, area.value); } catch (e) {}
        if (statusIndicator) {
          statusIndicator.innerHTML = '<i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Saved in browser';
        }
      }, 400);
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

  // Auto-tag dense visual math boards (.math-pv-row >= 6 cols, .math-bar-model >= 7 cells) for mobile fit
  document.querySelectorAll('.math-pv-row').forEach(row => {
    if (row.children.length >= 7) {
      row.classList.add('math-pv-wide');
    }
  });
  document.querySelectorAll('.math-bar-model').forEach(bar => {
    if (bar.querySelectorAll('.math-bar-cell').length >= 7) {
      bar.classList.add('math-bar-dense');
    }
  });

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
    if (window.innerWidth >= 1280 && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      if (s) {
        s.style.display = '';
        s.classList.remove('open-mobile', 'active');
      }
      if (btn) btn.classList.remove('active');
    }
  });

  // Progressive Disclosure on Mobile: Keep Worked Model 1 open, make Worked Models 2+ tap-to-expand on phones
  document.querySelectorAll('#worked-exam-models, section.revision-section').forEach(sec => {
    const models = sec.querySelectorAll(':scope > .model-example-card');
    if (models.length > 1) {
      models.forEach((card, idx) => {
        if (idx === 0 || card.querySelector('.mfs-model-expand-btn')) return;
        const steps = card.querySelector('.model-steps-container');
        if (!steps) return;
        card.classList.add('mfs-mobile-extra-model', 'mfs-model-collapsed');
        const toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.className = 'mfs-model-expand-btn';
        toggleBtn.setAttribute('aria-expanded', 'false');
        toggleBtn.innerHTML = '<i class="fa-solid fa-eye"></i> <span>Show Step-by-Step Worked Solution</span> <i class="fa-solid fa-chevron-down mfs-chevron"></i>';
        toggleBtn.addEventListener('click', () => {
          const isCollapsed = card.classList.toggle('mfs-model-collapsed');
          toggleBtn.setAttribute('aria-expanded', isCollapsed ? 'false' : 'true');
          toggleBtn.innerHTML = isCollapsed
            ? '<i class="fa-solid fa-eye"></i> <span>Show Step-by-Step Worked Solution</span> <i class="fa-solid fa-chevron-down mfs-chevron"></i>'
            : '<i class="fa-solid fa-eye-slash"></i> <span>Hide Worked Solution</span> <i class="fa-solid fa-chevron-up mfs-chevron"></i>';
        });
        steps.parentNode.insertBefore(toggleBtn, steps);
      });
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
  const stationBtn = document.getElementById('topicVideoStationBtn');
  const ytBtn = document.getElementById('topicVideoYouTubeBtn');
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
    if (stationBtn) {
      stationBtn.href = 'video-solution.html?topic=slc-task1-presentation-model';
      stationBtn.innerHTML = '<i class="fa-solid fa-circle-play"></i> Video Station: Task 1';
    }
    if (ytBtn) {
      ytBtn.href = 'https://youtu.be/l7VRzidsFno';
      ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Watch Task 1 on YouTube';
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
    if (stationBtn) {
      stationBtn.href = 'video-solution.html?topic=slc-task2-discussion-model';
      stationBtn.innerHTML = '<i class="fa-solid fa-circle-play"></i> Video Station: Task 2';
    }
    if (ytBtn) {
      ytBtn.href = 'https://youtu.be/labg8nxHII0';
      ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Watch Task 2 on YouTube';
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

/* ==========================================================================
   TOPIC MASTERCLASS CLICK-TO-PLAY YOUTUBE POSTER FACADE ENGINE
   Replaces eager youtube-nocookie iframes with instant local poster cards.
   ========================================================================== */
(function() {
  function mfsBuildYtEmbedSrc(ytid, startSec) {
    var s = (typeof startSec === 'number' && !isNaN(startSec) && startSec > 0) ? Math.floor(startSec) : 0;
    var origin = (window.location.protocol === 'http:' || window.location.protocol === 'https:')
      ? '&origin=' + encodeURIComponent(window.location.origin)
      : '';
    return 'https://www.youtube-nocookie.com/embed/' + ytid + '?rel=0&autoplay=1&playsinline=1&enablejsapi=1' + origin + (s > 0 ? '&start=' + s : '');
  }

  function mfsActivateTopicVideo(el, startSec) {
    var target = el || document.getElementById('topicMasterclassIframe');
    if (!target) return null;

    var start = (typeof startSec === 'number' && !isNaN(startSec) && startSec > 0) ? Math.floor(startSec) : 0;

    if (target.tagName && target.tagName.toLowerCase() === 'iframe') {
      if (window.MfsVideoChecks && typeof window.MfsVideoChecks.seekTopicPlayer === 'function' && window.MfsVideoChecks.seekTopicPlayer(start)) {
        return target;
      }
      var curYt = target.getAttribute('data-ytid');
      if (!curYt) {
        var m = (target.src || '').match(/embed\/([a-zA-Z0-9_-]+)/);
        curYt = m ? m[1] : '';
      }
      if (curYt) {
        target.src = mfsBuildYtEmbedSrc(curYt, start);
        if (window.MfsVideoChecks && typeof window.MfsVideoChecks.onTopicIframeActivated === 'function') {
          window.MfsVideoChecks.onTopicIframeActivated(target);
        }
      }
      return target;
    }

    var ytid = target.getAttribute('data-ytid') || '';
    if (!ytid) return null;
    var title = target.getAttribute('data-title') || 'Master Functional Skills Video Walkthrough';
    var poster = target.getAttribute('data-poster') || '';

    var iframe = document.createElement('iframe');
    iframe.id = target.id || 'topicMasterclassIframe';
    iframe.setAttribute('data-ytid', ytid);
    if (poster) iframe.setAttribute('data-poster', poster);
    iframe.style.cssText = 'position:absolute; top:0; left:0; width:100%; height:100%; border:0; display:block;';
    iframe.src = mfsBuildYtEmbedSrc(ytid, start);
    iframe.title = title;
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');

    if (target.parentNode) {
      target.parentNode.replaceChild(iframe, target);
    }
    if (window.MfsVideoChecks && typeof window.MfsVideoChecks.onTopicIframeActivated === 'function') {
      window.MfsVideoChecks.onTopicIframeActivated(iframe);
    }
    return iframe;
  }

  function mfsUpdateTopicFacade(ytid, title, posterUrl, startSec) {
    var el = document.getElementById('topicMasterclassIframe');
    if (!el || !ytid) return null;
    if (el.tagName && el.tagName.toLowerCase() === 'iframe') {
      el.setAttribute('data-ytid', ytid);
      if (posterUrl) el.setAttribute('data-poster', posterUrl);
      if (title) el.title = title;
      el.src = mfsBuildYtEmbedSrc(ytid, startSec);
      if (window.MfsVideoChecks && typeof window.MfsVideoChecks.refreshTopicByYtId === 'function') {
        window.MfsVideoChecks.refreshTopicByYtId(ytid);
      }
      return el;
    }
    el.setAttribute('data-ytid', ytid);
    if (title) {
      el.setAttribute('data-title', title);
      el.setAttribute('aria-label', 'Play video: ' + title);
    }
    if (posterUrl) {
      el.setAttribute('data-poster', posterUrl);
      var img = el.querySelector('img.mfs-yt-poster');
      if (img) {
        img.src = posterUrl;
        if (title) img.alt = title + ' poster thumbnail';
      }
    }
    if (window.MfsVideoChecks && typeof window.MfsVideoChecks.refreshTopicByYtId === 'function') {
      window.MfsVideoChecks.refreshTopicByYtId(ytid);
    }
    return el;
  }

  function mfsLoadVideoChecksAssets() {
    if (!document.getElementById('topicMasterclassIframe')) return;
    if (!document.querySelector('link[href*="mfs-video-checks.css"]')) {
      var lk = document.createElement('link');
      lk.rel = 'stylesheet';
      lk.href = MFS_REV_ROOT + 'assets/css/mfs-video-checks.css?v=20261121v1';
      document.head.appendChild(lk);
    }
    if (!window.MfsVideoChecks && !document.querySelector('script[src*="mfs-video-checks.js"]')) {
      var sc = document.createElement('script');
      sc.src = MFS_REV_ROOT + 'assets/js/mfs-video-checks.js?v=20261121v1';
      sc.defer = true;
      document.body.appendChild(sc);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mfsLoadVideoChecksAssets);
  } else {
    mfsLoadVideoChecksAssets();
  }

  window.mfsActivateTopicVideo = mfsActivateTopicVideo;
  window.mfsUpdateTopicFacade = mfsUpdateTopicFacade;

  document.addEventListener('click', function(ev) {
    var facade = ev.target && ev.target.closest ? ev.target.closest('.mfs-yt-facade') : null;
    if (!facade) return;
    ev.preventDefault();
    var defaultStart = parseInt(facade.getAttribute('data-start') || '0', 10) || 0;
    mfsActivateTopicVideo(facade, defaultStart);
  });

  document.addEventListener('keydown', function(ev) {
    if (ev.key !== 'Enter' && ev.key !== ' ') return;
    var facade = ev.target && ev.target.closest ? ev.target.closest('.mfs-yt-facade') : null;
    if (!facade) return;
    ev.preventDefault();
    var defaultStart = parseInt(facade.getAttribute('data-start') || '0', 10) || 0;
    mfsActivateTopicVideo(facade, defaultStart);
  });

  function initMobileVideoSimplifier() {
    var station = document.getElementById('videoMasterclassStation');
    if (!station) return;

    var jumpBar = document.getElementById('mcJumpBar');
    if (jumpBar && !station.querySelector('.mfs-chapters-toggle')) {
      var toggleBtn = document.createElement('button');
      toggleBtn.type = 'button';
      toggleBtn.className = 'mfs-chapters-toggle';
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.setAttribute('aria-controls', 'mcJumpBar');

      function updateToggleLabel() {
        var isOpen = jumpBar.classList.contains('is-mobile-open');
        var count = jumpBar.querySelectorAll('.jump-btn').length;
        toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        toggleBtn.innerHTML = '<span><i class="fa-solid fa-list-ul"></i> Video Chapters (' + count + ')</span><i class="fa-solid fa-chevron-down mfs-chapters-chev"></i>';
      }

      updateToggleLabel();
      toggleBtn.addEventListener('click', function() {
        jumpBar.classList.toggle('is-mobile-open');
        updateToggleLabel();
      });

      if (jumpBar.parentNode) {
        jumpBar.parentNode.insertBefore(toggleBtn, jumpBar);
      }

      if (window.MutationObserver) {
        var jbObs = new MutationObserver(function() {
          updateToggleLabel();
        });
        jbObs.observe(jumpBar, { childList: true });
      }
    }

    var metaEl = document.getElementById('mcTutorMeta');
    if (metaEl) {
      var mq = window.matchMedia ? window.matchMedia('(max-width: 768px)') : null;
      function syncCompactMeta() {
        var rawFull = metaEl.getAttribute('data-mfs-full-meta') || metaEl.innerHTML;
        if (!metaEl.getAttribute('data-mfs-full-meta')) {
          metaEl.setAttribute('data-mfs-full-meta', rawFull);
        }
        var currentText = metaEl.textContent || '';
        var isAlreadyCondensed = metaEl.getAttribute('data-mfs-condensed') === '1';
        if (!isAlreadyCondensed) {
          metaEl.setAttribute('data-mfs-full-meta', metaEl.innerHTML);
        }
        if (mq && mq.matches) {
          var fullStr = metaEl.getAttribute('data-mfs-full-meta') || '';
          var tmp = document.createElement('div');
          tmp.innerHTML = fullStr;
          var txt = (tmp.textContent || '').replace(/\s+/g, ' ').trim();
          var tutorMatch = txt.match(/Presented by\s+([A-Za-z]+)/i);
          var durMatch = txt.match(/\((\d+m\s*\d+s)\)/i);
          if (tutorMatch || durMatch) {
            var parts = [];
            if (tutorMatch) parts.push('Tutor ' + tutorMatch[1]);
            if (durMatch) parts.push(durMatch[1]);
            metaEl.textContent = parts.join(' \u2022 ');
            metaEl.setAttribute('data-mfs-condensed', '1');
          }
        } else if (metaEl.getAttribute('data-mfs-condensed') === '1') {
          metaEl.innerHTML = metaEl.getAttribute('data-mfs-full-meta') || currentText;
          metaEl.removeAttribute('data-mfs-condensed');
        }
      }

      syncCompactMeta();
      if (mq && mq.addEventListener) {
        mq.addEventListener('change', syncCompactMeta);
      }
      if (window.MutationObserver) {
        var syncing = false;
        var metaObs = new MutationObserver(function() {
          if (syncing) return;
          if (metaEl.getAttribute('data-mfs-condensed') === '1' && mq && mq.matches) {
            return;
          }
          syncing = true;
          metaEl.removeAttribute('data-mfs-condensed');
          metaEl.setAttribute('data-mfs-full-meta', metaEl.innerHTML);
          syncCompactMeta();
          syncing = false;
        });
        metaObs.observe(metaEl, { childList: true, characterData: true, subtree: true });
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileVideoSimplifier);
  } else {
    initMobileVideoSimplifier();
  }
})();

