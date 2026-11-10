/**
 * MASTER FUNCTIONAL SKILLS — PRIVATE EARLY ACCESS GATE
 * Restricts access to authorised tutors and QA reviewers during development.
 */
(function () {
  'use strict';

  var AUTH_KEY = 'mfs_stealth_auth';
  var VALID_CODES = ['2026', 'mfs2026', 'subi', 'darknight'];

  function isAuthorized() {
    try {
      return localStorage.getItem(AUTH_KEY) === 'true';
    } catch (e) {
      return false;
    }
  }

  function setAuthorized(state) {
    try {
      if (state) {
        localStorage.setItem(AUTH_KEY, 'true');
      } else {
        localStorage.removeItem(AUTH_KEY);
      }
    } catch (e) {}
  }

  function initGate() {
    // If already authorized, show discrete relock control and exit
    if (isAuthorized()) {
      showRelockControl();
      return;
    }

    // Ensure CSS is loaded
    if (!document.getElementById('mfsGateCss')) {
      var link = document.createElement('link');
      link.id = 'mfsGateCss';
      link.rel = 'stylesheet';
      link.href = 'assets/css/mfs-private-gate.css';
      document.head.appendChild(link);
    }

    // Prevent body scrolling
    document.body.classList.add('mfs-gate-locked');

    // Create overlay
    var overlay = document.createElement('div');
    overlay.id = 'mfsGateOverlay';
    overlay.innerHTML = [
      '<div class="mfs-gate-modal" id="mfsGateModal">',
      '  <div class="mfs-gate-badge">',
      '    <i class="fa-solid fa-lock"></i> Private Pre-Release Access',
      '  </div>',
      '  <h1 class="mfs-gate-logo">Master Functional <span>Skills</span></h1>',
      '  <p class="mfs-gate-subtitle">',
      '    This platform is currently undergoing Pearson Edexcel syllabus calibration. Access is restricted to authorised educators, QA reviewers, and registered students.',
      '  </p>',
      '  <form class="mfs-gate-form" id="mfsGateForm">',
      '    <div class="mfs-gate-input-wrapper">',
      '      <input type="password" id="mfsGatePass" class="mfs-gate-input" placeholder="Enter Access PIN" autocomplete="off" autofocus />',
      '    </div>',
      '    <button type="submit" class="mfs-gate-submit-btn">',
      '      <i class="fa-solid fa-key"></i> Unlock Learning Portal',
      '    </button>',
      '    <div class="mfs-gate-error" id="mfsGateError">Incorrect PIN. Please contact your coordinator.</div>',
      '  </form>',
      '  <div class="mfs-gate-footer-note">',
      '    Tutor & Learner Development Environment • Session Active',
      '  </div>',
      '</div>'
    ].join('\n');

    document.body.appendChild(overlay);

    var form = document.getElementById('mfsGateForm');
    var input = document.getElementById('mfsGatePass');
    var error = document.getElementById('mfsGateError');
    var modal = document.getElementById('mfsGateModal');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var entered = (input.value || '').trim().toLowerCase();

      if (VALID_CODES.indexOf(entered) !== -1) {
        // Correct Passcode
        setAuthorized(true);
        error.classList.remove('visible');
        overlay.classList.add('unlocked');
        document.body.classList.remove('mfs-gate-locked');
        setTimeout(function () {
          if (overlay.parentNode) {
            overlay.parentNode.removeChild(overlay);
          }
          showRelockControl();
        }, 400);
      } else {
        // Incorrect Passcode
        error.classList.add('visible');
        modal.classList.add('mfs-shake');
        input.value = '';
        input.focus();
        setTimeout(function () {
          modal.classList.remove('mfs-shake');
        }, 450);
      }
    });
  }

  function showRelockControl() {
    if (document.getElementById('mfsRelockBtn')) return;
    var btn = document.createElement('button');
    btn.id = 'mfsRelockBtn';
    btn.type = 'button';
    btn.className = 'mfs-gate-relock-btn';
    btn.title = 'Click to lock site again for security';
    btn.innerHTML = '<i class="fa-solid fa-lock"></i> QA Mode Active (Lock)';
    btn.addEventListener('click', function () {
      if (confirm('Lock the site again? You will need your access PIN to re-enter.')) {
        setAuthorized(false);
        location.reload();
      }
    });
    document.body.appendChild(btn);
  }

  // Self-initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGate);
  } else {
    initGate();
  }
})();
