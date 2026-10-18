/**
 * Master Functional Skills - Video Solution Modal Controller
 * Author: Master Functional Skills / DarkNight
 */

(function () {
  'use strict';

  // Available videos dictionary (slug/topic -> video details)
  // Available videos dictionary (slug/topic -> video details)
  const KNOWN_VIDEOS = {
    // Past Paper 10
    'edexcel-maths-l2-past-paper-10-section-a': {
      ytId: 'muSRa0fEsSs',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 10 • section a: non-calculator': {
      ytId: 'muSRa0fEsSs',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-10-section-b': {
      ytId: 'b6Ma4VzxG8I',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-a',
      companionLabel: 'Section A: Non-Calculator (13m)'
    },
    'past paper 10 • section b: calculator': {
      ytId: 'b6Ma4VzxG8I',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-a',
      companionLabel: 'Section A: Non-Calculator (13m)'
    },

    // Past Paper 9
    'edexcel-maths-l2-past-paper-9-section-a': {
      ytId: '61c6xSMBz0I',
      title: 'Past Paper 9 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-b',
      companionLabel: 'Section B: Calculator (20m)'
    },
    'past paper 9 • section a: non-calculator': {
      ytId: '61c6xSMBz0I',
      title: 'Past Paper 9 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-b',
      companionLabel: 'Section B: Calculator (20m)'
    },
    'edexcel-maths-l2-past-paper-9-section-b': {
      ytId: 'how7uhzmyIQ',
      title: 'Past Paper 9 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 9 • section b: calculator': {
      ytId: 'how7uhzmyIQ',
      title: 'Past Paper 9 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // Past Paper 8
    'edexcel-maths-l2-past-paper-8-section-a': {
      ytId: 'nr8dqv5KIkI',
      title: 'Past Paper 8 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 8 • section a: non-calculator': {
      ytId: 'nr8dqv5KIkI',
      title: 'Past Paper 8 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-8-section-b': {
      ytId: 'KbPz2OxJRxc',
      title: 'Past Paper 8 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 8 • section b: calculator': {
      ytId: 'KbPz2OxJRxc',
      title: 'Past Paper 8 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // Past Paper 7
    'edexcel-maths-l2-past-paper-7-section-a': {
      ytId: 'bnxoprdRACk',
      title: 'Past Paper 7 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-b',
      companionLabel: 'Section B: Calculator (25m)'
    },
    'past paper 7 • section a: non-calculator': {
      ytId: 'bnxoprdRACk',
      title: 'Past Paper 7 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-b',
      companionLabel: 'Section B: Calculator (25m)'
    },
    'edexcel-maths-l2-past-paper-7-section-b': {
      ytId: 'IY2EjScrw4Y',
      title: 'Past Paper 7 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-a',
      companionLabel: 'Section A: Non-Calculator (12m)'
    },
    'past paper 7 • section b: calculator': {
      ytId: 'IY2EjScrw4Y',
      title: 'Past Paper 7 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-a',
      companionLabel: 'Section A: Non-Calculator (12m)'
    },
    // Past Paper 6
    'edexcel-maths-l2-past-paper-6-section-a': {
      ytId: 'TCwy_FiZ1eA',
      title: 'Past Paper 6 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 6 • section a: non-calculator': {
      ytId: 'TCwy_FiZ1eA',
      title: 'Past Paper 6 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-6-section-b': {
      ytId: 'r4bU8USCWvs',
      title: 'Past Paper 6 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 6 • section b: calculator': {
      ytId: 'r4bU8USCWvs',
      title: 'Past Paper 6 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
  };

  let modalOverlay = null;

  function initModalDom() {
    if (document.getElementById('mfsVideoModalOverlay')) {
      modalOverlay = document.getElementById('mfsVideoModalOverlay');
      return;
    }

    const overlay = document.createElement('div');
    overlay.id = 'mfsVideoModalOverlay';
    overlay.className = 'mfs-video-modal-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Video Solution Walkthrough');

    overlay.innerHTML = `
      <div class="mfs-video-modal-container" id="mfsModalContainer">
        <!-- Head -->
        <div class="mfs-video-modal-head">
          <div class="mfs-modal-branding">
            <div class="mfs-modal-logo-icon">
              <i class="fa-solid fa-play"></i>
            </div>
            <div class="mfs-modal-title-wrap">
              <span class="mfs-modal-series" id="mfsModalSeries">Pearson Edexcel Functional Skills</span>
              <h3 class="mfs-modal-title" id="mfsModalTitle">Topic Video Solution</h3>
            </div>
          </div>
          <button type="button" class="mfs-modal-close-btn" id="mfsModalCloseBtn" aria-label="Close modal">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Body -->
        <div class="mfs-video-modal-body">
          <div id="mfsModalSectionSwitcher" style="display:none; gap:10px; margin-bottom:12px; flex-wrap:wrap;"></div>
          <!-- Video Player Box -->
          <div class="mfs-player-ratio-box" id="mfsPlayerBox">
            <!-- Dynamic Content Injected Here -->
          </div>

          <!-- Metadata & Action Bar -->
          <div class="mfs-modal-meta-bar">
            <div class="mfs-meta-tutor-badge">
              <div class="mfs-tutor-avatar"><i class="fa-solid fa-graduation-cap"></i></div>
              <div class="mfs-tutor-details">
                <span class="mfs-tutor-name" id="mfsModalTutor">Your Functional Skills Tutor</span>
                <span class="mfs-tutor-role">Pearson Functional Skills Specialist</span>
              </div>
            </div>

            <div class="mfs-modal-actions">
              <a href="#" target="_blank" rel="noopener" class="btn-modal-sheet" id="mfsModalSheetBtn">
                <i class="fa-regular fa-file-pdf"></i> Question Worksheet
              </a>
              <a href="#" target="_blank" rel="noopener" class="btn-modal-answers" id="mfsModalAnswersBtn">
                <i class="fa-solid fa-circle-check"></i> Worked Answers [M1/A1]
              </a>
              <a href="https://www.youtube.com/@MasterFunctionalSkills" target="_blank" rel="noopener" class="btn-modal-yt" id="mfsModalYtBtn">
                <i class="fa-brands fa-youtube"></i> Watch on YouTube App
              </a>
            </div>
          </div>

          <!-- Features Cards -->
          <div class="mfs-modal-features-row">
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-bullseye" style="color:#38bdf8;"></i>
              <div>
                <span class="mfs-feat-title">Method Marks (M1/A1)</span>
                <span class="mfs-feat-desc">Pearson mark criteria breakdown for every working step.</span>
              </div>
            </div>
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-triangle-exclamation" style="color:#f59e0b;"></i>
              <div>
                <span class="mfs-feat-title">Examiner Trap Alerts</span>
                <span class="mfs-feat-desc">Identifies subtle exam traps and placeholder errors.</span>
              </div>
            </div>
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-rotate-left" style="color:#10b981;"></i>
              <div>
                <span class="mfs-feat-title">Reverse Sanity Checks</span>
                <span class="mfs-feat-desc">Proofing checks to verify answers before moving on.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);
    modalOverlay = overlay;

    // Attach Close Listeners
    document.getElementById('mfsModalCloseBtn').addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        closeModal();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('active')) {
        closeModal();
      }
    });
  }

  function openModal(options) {
    initModalDom();

    const topic = options.topic || 'Video Solution Walkthrough';
    const series = options.series || 'Pearson Edexcel Functional Skills';
    const tutor = options.tutor || 'Subi';
    const sheetUrl = options.sheetUrl || '#';
    const answersUrl = options.answersUrl || '#';
    
    // Detect YouTube ID from options or known dictionary
    let ytId = options.ytId || '';
    if (!ytId && options.videoSrc) {
      const m = options.videoSrc.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([a-zA-Z0-9_-]{11})/);
      if (m) ytId = m[1];
    }

    const normTopic = topic.trim().toLowerCase();
    const knownItem = KNOWN_VIDEOS[normTopic] || (options.slug && KNOWN_VIDEOS[options.slug]);
    if (!ytId && knownItem && knownItem.ytId) {
      ytId = knownItem.ytId;
    }

    // Set Header
    document.getElementById('mfsModalTitle').textContent = topic;
    document.getElementById('mfsModalSeries').textContent = series;
    document.getElementById('mfsModalTutor').textContent = tutor;

    // Section Switcher for Multi-Section Past Papers
    const switcherEl = document.getElementById('mfsModalSectionSwitcher');
    if (switcherEl) {
      if (knownItem && knownItem.companionSlug && KNOWN_VIDEOS[knownItem.companionSlug]) {
        const companion = KNOWN_VIDEOS[knownItem.companionSlug];
        const isSecB = knownItem.activeSection === 'B';
        const secA = isSecB ? companion : knownItem;
        const secB = isSecB ? knownItem : companion;
        switcherEl.style.display = 'flex';
        switcherEl.innerHTML = `
          <button type="button" id="mfsSwitchSecA" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${!isSecB ? '#3b82f6' : '#334155'}; background:${!isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-circle-play"></i> Section A: Non-Calculator
          </button>
          <button type="button" id="mfsSwitchSecB" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${isSecB ? '#3b82f6' : '#334155'}; background:${isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-calculator"></i> Section B: Calculator
          </button>
        `;
        document.getElementById('mfsSwitchSecA').onclick = function () {
          openModal({
            topic: secA.title,
            series: secA.series,
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            ytId: secA.ytId,
            slug: secA.companionSlug ? secA.companionSlug : undefined
          });
        };
        document.getElementById('mfsSwitchSecB').onclick = function () {
          openModal({
            topic: secB.title,
            series: secB.series,
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            ytId: secB.ytId,
            slug: secB.companionSlug ? secB.companionSlug : undefined
          });
        };
      } else {
        switcherEl.style.display = 'none';
        switcherEl.innerHTML = '';
      }
    }

    // Set Action Links
    const sheetBtn = document.getElementById('mfsModalSheetBtn');
    const answersBtn = document.getElementById('mfsModalAnswersBtn');
    const ytBtn = document.getElementById('mfsModalYtBtn');
    
    if (sheetUrl && sheetUrl !== '#') {
      sheetBtn.href = sheetUrl;
      sheetBtn.style.display = 'inline-flex';
    } else {
      sheetBtn.style.display = 'none';
    }

    if (answersUrl && answersUrl !== '#') {
      answersBtn.href = answersUrl;
      answersBtn.style.display = 'inline-flex';
    } else {
      answersBtn.style.display = 'none';
    }

    if (ytBtn) {
      if (ytId) {
        ytBtn.href = `https://youtu.be/${ytId}`;
        ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Watch on YouTube App';
      } else {
        ytBtn.href = 'https://www.youtube.com/@MasterFunctionalSkills';
        ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Visit MFS YouTube Channel';
      }
    }

    // Set Player Box
    const playerBox = document.getElementById('mfsPlayerBox');
    playerBox.innerHTML = '';

    if (ytId) {
      // Clean YouTube Embed (Never crashes mobile browsers with MIME type error)
      playerBox.innerHTML = `
        <iframe style="width:100%; height:100%; border:0; display:block;" src="https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&rel=0&playsinline=1" title="${escapeHtml(topic)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
      `;
    } else {
      // In Production State / Channel Fallback
      playerBox.innerHTML = `
        <div class="mfs-video-placeholder-card">
          <div class="mfs-placeholder-icon-wrap" style="color:#ef4444; border-color:#ef4444; background:rgba(239,68,68,0.15);">
            <i class="fa-brands fa-youtube"></i>
          </div>
          <span class="mfs-placeholder-badge">
            <i class="fa-solid fa-circle-play"></i> Video Walkthrough on Master Functional Skills
          </span>
          <h4 class="mfs-placeholder-heading">${escapeHtml(topic)}</h4>
          <p class="mfs-placeholder-text">
            Watch our step-by-step video solutions with Pearson Edexcel method marks [M1/A1], examiner trap alerts, and reverse sanity checks directly on our YouTube channel.
          </p>
          <div style="display:flex; gap:12px; flex-wrap:wrap; justify-content:center; margin-top:8px;">
            <a href="https://www.youtube.com/@MasterFunctionalSkills" target="_blank" rel="noopener" class="btn-modal-yt" style="padding:10px 18px; font-size:0.92rem; background:#dc2626; color:#fff; border-radius:8px; text-decoration:none; font-weight:700; display:inline-flex; align-items:center; gap:8px;">
              <i class="fa-brands fa-youtube"></i> Open YouTube Channel
            </a>
            ${answersUrl && answersUrl !== '#' ? `<a href="${answersUrl}" target="_blank" rel="noopener" class="btn-modal-answers" style="padding:10px 18px; font-size:0.92rem;"><i class="fa-solid fa-circle-check"></i> Open Step-by-Step Worked Answers</a>` : ''}
            ${sheetUrl && sheetUrl !== '#' ? `<a href="${sheetUrl}" target="_blank" rel="noopener" class="btn-modal-sheet" style="padding:10px 18px; font-size:0.92rem;"><i class="fa-regular fa-file-pdf"></i> Open Question Worksheet</a>` : ''}
          </div>
        </div>
      `;
    }

    // Show Overlay
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!modalOverlay) return;

    // Immediately stop iframe video/audio
    const playerBox = document.getElementById('mfsPlayerBox');
    if (playerBox) {
      playerBox.innerHTML = '';
    }

    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  function escapeHtml(str) {
    return (str || '').replace(/[&<>"']/g, function (m) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[m];
    });
  }

  // Intercept all video buttons on page load
  function bindVideoButtons() {
    initModalDom();

    const videoButtons = document.querySelectorAll('.btn-mfs-video, .open-video-modal, .btn-paper-video');
    videoButtons.forEach(btn => {
      // Prevent double binding
      if (btn.getAttribute('data-mfs-video-bound') === 'true') return;
      btn.setAttribute('data-mfs-video-bound', 'true');

      btn.addEventListener('click', function (e) {
        const href = this.getAttribute('href') || '';
        // If link points to video-solution.html, let browser navigate directly to the dedicated video app
        if (href.indexOf('video-solution.html') !== -1) {
          return;
        }

        // Check if link is an external non-YouTube URL
        if (/^https?:\/\//i.test(href) && !/(?:youtu\.be|youtube\.com)/i.test(href)) {
          return;
        }

        e.preventDefault();

        // Extract topic metadata from attributes or DOM context
        let topic = this.getAttribute('data-topic');
        let sheetUrl = this.getAttribute('data-sheet');
        let answersUrl = this.getAttribute('data-answers');
        let ytId = this.getAttribute('data-yt-id') || '';
        let series = this.getAttribute('data-series') || 'Pearson Edexcel Functional Skills';

        if (!ytId && href) {
          const m = href.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([a-zA-Z0-9_-]{11})/);
          if (m) ytId = m[1];
        }

        // Auto-detect topic from parent row if missing
        if (!topic) {
          const row = this.closest('.topic-row, .past-paper-row, .revision-topic-card');
          if (row) {
            const titleEl = row.querySelector('.topic-title, .past-paper-title, h3, h4');
            if (titleEl) {
              topic = titleEl.textContent.trim();
            }
            if (!sheetUrl) {
              const sheetEl = row.querySelector('.btn-mfs-sheet, .btn-paper-qp');
              if (sheetEl) sheetUrl = sheetEl.getAttribute('href');
            }
            if (!answersUrl) {
              const answersEl = row.querySelector('a[href*="-answers.html"], .btn-paper-ms, .btn-paper-model');
              if (answersEl) answersUrl = answersEl.getAttribute('href');
            }
          }
        }

        openModal({
          topic: topic || 'Video Solution Walkthrough',
          sheetUrl: sheetUrl,
          answersUrl: answersUrl,
          ytId: ytId,
          series: series,
          tutor: 'Subi'
        });
      });
    });
  }

  // Expose global API
  window.MfsVideoModal = {
    open: openModal,
    close: closeModal,
    registerVideo: function (topicSlug, details) {
      KNOWN_VIDEOS[topicSlug.trim().toLowerCase()] = details;
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindVideoButtons);
  } else {
    bindVideoButtons();
  }
})();
