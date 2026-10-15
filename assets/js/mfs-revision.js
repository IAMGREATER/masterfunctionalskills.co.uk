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
  if (sidebar) {
    sidebar.style.display = (sidebar.style.display === 'block') ? 'none' : 'block';
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
});
