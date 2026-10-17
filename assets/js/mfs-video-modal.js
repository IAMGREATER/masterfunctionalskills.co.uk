/**
 * Master Functional Skills - Video Solution Modal Controller
 * Author: Master Functional Skills / DarkNight
 */

(function () {
  'use strict';

  // Available videos dictionary (slug/topic -> video details)
  const KNOWN_VIDEOS = {
    'numbers-and-place-value': {
      videoSrc: 'videos/Numbers_and_Place_Value_Video_Solution.mp4?v=4',
      posterSrc: 'videos/thumbnail_numbers_and_place_value.png',
      title: 'Numbers and Place Value • Video Solution Walkthrough',
      series: 'Pearson Edexcel Maths Level 1 & Level 2',
      tutor: 'Your Functional Skills Tutor'
    },
    'numbers and place value': {
      videoSrc: 'videos/Numbers_and_Place_Value_Video_Solution.mp4?v=4',
      posterSrc: 'videos/thumbnail_numbers_and_place_value.png',
      title: 'Numbers and Place Value • Video Solution Walkthrough',
      series: 'Pearson Edexcel Maths Level 1 & Level 2',
      tutor: 'Your Functional Skills Tutor'
    },
    'edexcel-maths-l2-past-paper-10-section-a': {
      videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_A_Walkthrough.mp4',
      posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_a.png',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Your Functional Skills Tutor',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A'
    },
    'past paper 10 • section a: non-calculator': {
      videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_A_Walkthrough.mp4',
      posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_a.png',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Your Functional Skills Tutor',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A'
    },
    'edexcel-maths-l2-past-paper-10-section-b': {
      videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_B_Full_Walkthrough.mp4',
      posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_b.png',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Your Functional Skills Tutor',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B'
    },
    'past paper 10 • section b: calculator': {
      videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_B_Full_Walkthrough.mp4',
      posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_b.png',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Your Functional Skills Tutor',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B'
    }
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
              <a href="https://www.youtube.com/@MasterFunctionalSkills" target="_blank" rel="noopener" class="btn-modal-yt">
                <i class="fa-brands fa-youtube"></i> Subscribe
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
    const tutor = options.tutor || 'Your Functional Skills Tutor';
    const sheetUrl = options.sheetUrl || '#';
    const answersUrl = options.answersUrl || '#';
    
    // Check known videos dict if videoSrc not directly given
    let videoSrc = options.videoSrc || '';
    let posterSrc = options.posterSrc || '';

    const normTopic = topic.trim().toLowerCase();
    if (!videoSrc && KNOWN_VIDEOS[normTopic]) {
      videoSrc = KNOWN_VIDEOS[normTopic].videoSrc;
      posterSrc = KNOWN_VIDEOS[normTopic].posterSrc;
    }

    // Set Header
    document.getElementById('mfsModalTitle').textContent = topic;
    document.getElementById('mfsModalSeries').textContent = series;
    document.getElementById('mfsModalTutor').textContent = tutor;

    // Section Switcher for Past Paper 10
    const switcherEl = document.getElementById('mfsModalSectionSwitcher');
    if (switcherEl) {
      if (videoSrc.indexOf('Past_Paper_10_Section_') !== -1) {
        const isSecB = videoSrc.indexOf('Section_B') !== -1;
        switcherEl.style.display = 'flex';
        switcherEl.innerHTML = `
          <button type="button" id="mfsSwitchSecA" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${!isSecB ? '#3b82f6' : '#334155'}; background:${!isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-circle-play"></i> Section A: Non-Calculator (Q1–Q4 • 13m)
          </button>
          <button type="button" id="mfsSwitchSecB" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${isSecB ? '#3b82f6' : '#334155'}; background:${isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-calculator"></i> Section B: Calculator (Q1–Q12 • 22m)
          </button>
        `;
        document.getElementById('mfsSwitchSecA').onclick = function () {
          openModal({
            topic: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
            series: 'Pearson Edexcel Functional Skills Maths Level 2',
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_A_Walkthrough.mp4',
            posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_a.png'
          });
        };
        document.getElementById('mfsSwitchSecB').onclick = function () {
          openModal({
            topic: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
            series: 'Pearson Edexcel Functional Skills Maths Level 2',
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            videoSrc: 'videos/Pearson_Edexcel_Maths_L2_Past_Paper_10_Section_B_Full_Walkthrough.mp4',
            posterSrc: 'videos/thumbnail_edexcel_maths_l2_paper_10_sec_b.png'
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

    // Set Player Box
    const playerBox = document.getElementById('mfsPlayerBox');
    playerBox.innerHTML = '';

    if (videoSrc) {
      // Live Video Player
      const videoEl = document.createElement('video');
      videoEl.id = 'mfsActiveVideo';
      videoEl.controls = true;
      videoEl.playsInline = true;
      videoEl.autoplay = true;
      if (posterSrc) {
        videoEl.poster = posterSrc;
      }
      videoEl.src = videoSrc;
      playerBox.appendChild(videoEl);
    } else {
      // In Production State
      playerBox.innerHTML = `
        <div class="mfs-video-placeholder-card">
          <div class="mfs-placeholder-icon-wrap">
            <i class="fa-solid fa-clapperboard"></i>
          </div>
          <span class="mfs-placeholder-badge">
            <i class="fa-solid fa-circle-play"></i> High-Definition Walkthrough in Production
          </span>
          <h4 class="mfs-placeholder-heading">${escapeHtml(topic)}</h4>
          <p class="mfs-placeholder-text">
            Our specialist Functional Skills tutor is recording the complete step-by-step video solution with Pearson Edexcel method marks [M1/A1], examiner trap alerts, and reverse sanity checks.
          </p>
          <div style="display:flex; gap:12px; flex-wrap:wrap; justify-content:center; margin-top:8px;">
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

    // Pause and clear video playback
    const activeVideo = document.getElementById('mfsActiveVideo');
    if (activeVideo) {
      try {
        activeVideo.pause();
        activeVideo.src = '';
        activeVideo.load();
      } catch (e) {
        // ignore
      }
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
        const hasVideoAttr = !!this.getAttribute('data-video');
        if (this.classList.contains('btn-paper-video') && !hasVideoAttr && /^https?:\/\//i.test(href)) {
          return; // allow external video link to open normally
        }
        e.preventDefault();

        // Extract topic metadata from attributes or DOM context
        let topic = this.getAttribute('data-topic');
        let sheetUrl = this.getAttribute('data-sheet');
        let answersUrl = this.getAttribute('data-answers');
        let videoSrc = this.getAttribute('data-video') || '';
        let posterSrc = this.getAttribute('data-poster') || '';
        let series = this.getAttribute('data-series') || 'Pearson Edexcel Functional Skills';

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
          videoSrc: videoSrc,
          posterSrc: posterSrc,
          series: series,
          tutor: 'Your Functional Skills Tutor'
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
