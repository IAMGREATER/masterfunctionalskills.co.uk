/**
 * Master Functional Skills — Interactive Video Comprehension & CCQ Engine
 * Zero-re-render overlay/drawer powered by assets/data/mfs-video-checks.json + .vtt chapters.
 */
(function () {
  'use strict';

  var STORAGE_PROGRESS = 'mfs_vc_progress_v1';
  var STORAGE_AUTOPAUSE = 'mfs_ccq_auto_pause';
  var DATA_VERSION = '2026-11-20-v1';
  var LETTERS = ['A', 'B', 'C', 'D'];

  var _scriptEl = document.currentScript || document.querySelector('script[src*="mfs-video-checks.js"]');
  var ROOT_PREFIX = (_scriptEl && _scriptEl.getAttribute('src'))
    ? _scriptEl.getAttribute('src').replace(/assets\/js\/mfs-video-checks\.js.*$/, '')
    : (typeof window.MFS_REV_ROOT === 'string' ? window.MFS_REV_ROOT : '');

  var dataPromise = null;
  var dataCache = null;

  // Active playback tracking per surface: 'topic' | 'station' | 'modal'
  var contexts = {
    topic: null,
    station: null,
    modal: null
  };

  var ytApiPromise = null;

  function escapeHtml(str) {
    return String(str == null ? '' : str).replace(/[&<>"']/g, function (m) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m];
    });
  }

  function formatMMSS(sec) {
    var s = Math.max(0, Math.floor(Number(sec) || 0));
    var mins = Math.floor(s / 60);
    var rem = s % 60;
    return mins + ':' + (rem < 10 ? '0' : '') + rem;
  }

  function readProgressMap() {
    try {
      var raw = localStorage.getItem(STORAGE_PROGRESS);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function writeProgressMap(map) {
    try {
      localStorage.setItem(STORAGE_PROGRESS, JSON.stringify(map));
    } catch (e) {}
  }

  function getVideoProgress(slug) {
    var map = readProgressMap();
    return map[slug] || { answers: {}, correct: {} };
  }

  function saveCheckAnswer(slug, checkId, optIdx, isCorrect) {
    var map = readProgressMap();
    if (!map[slug]) map[slug] = { answers: {}, correct: {} };
    map[slug].answers[checkId] = optIdx;
    map[slug].correct[checkId] = Boolean(isCorrect);
    writeProgressMap(map);
  }

  function resetVideoProgress(slug) {
    var map = readProgressMap();
    delete map[slug];
    writeProgressMap(map);
  }

  function getAutoPausePref() {
    try {
      return localStorage.getItem(STORAGE_AUTOPAUSE) === 'true';
    } catch (e) {
      return false;
    }
  }

  function setAutoPausePref(val) {
    try {
      localStorage.setItem(STORAGE_AUTOPAUSE, val ? 'true' : 'false');
    } catch (e) {}
  }

  function loadData() {
    if (dataCache) return Promise.resolve(dataCache);
    if (dataPromise) return dataPromise;
    var url = ROOT_PREFIX + 'assets/data/mfs-video-checks.json?v=' + DATA_VERSION;
    dataPromise = fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function (json) {
        dataCache = json;
        return json;
      })
      .catch(function (err) {
        dataPromise = null;
        throw err;
      });
    return dataPromise;
  }

  function lookupVideo(data, identifier) {
    if (!data || !identifier) return null;
    if (data.videos && data.videos[identifier]) return data.videos[identifier];
    if (data.byYtId && data.byYtId[identifier] && data.videos[data.byYtId[identifier]]) {
      return data.videos[data.byYtId[identifier]];
    }
    return null;
  }

  function ensureYouTubeApi() {
    if (window.location.protocol !== 'http:' && window.location.protocol !== 'https:') {
      return Promise.resolve(null);
    }
    if (window.YT && typeof window.YT.Player === 'function') {
      return Promise.resolve(window.YT);
    }
    if (ytApiPromise) return ytApiPromise;
    ytApiPromise = new Promise(function (resolve) {
      var prev = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = function () {
        if (typeof prev === 'function') {
          try { prev(); } catch (e) {}
        }
        resolve(window.YT);
      };
      if (!document.querySelector('script[src*="youtube.com/iframe_api"]')) {
        var tag = document.createElement('script');
        tag.src = 'https://www.youtube.com/iframe_api';
        tag.async = true;
        tag.onerror = function () { resolve(null); };
        document.head.appendChild(tag);
      }
      setTimeout(function () {
        if (window.YT && typeof window.YT.Player === 'function') resolve(window.YT);
      }, 4500);
    });
    return ytApiPromise;
  }

  function cleanupPlayer(ctx) {
    if (!ctx) return;
    if (ctx.pollTimer) {
      clearInterval(ctx.pollTimer);
      ctx.pollTimer = null;
    }
    if (ctx.videoEl && ctx.onTimeUpdateFn) {
      ctx.videoEl.removeEventListener('timeupdate', ctx.onTimeUpdateFn);
      ctx.onTimeUpdateFn = null;
    }
    if (ctx.ytPlayer && typeof ctx.ytPlayer.destroy === 'function') {
      try { ctx.ytPlayer.destroy(); } catch (e) {}
    }
    ctx.ytPlayer = null;
    ctx.ytReady = false;
    ctx.videoEl = null;
  }

  function attachPlayback(ctx) {
    if (!ctx) return;
    cleanupPlayer(ctx);

    var mediaEl = ctx.getMediaEl ? ctx.getMediaEl() : null;
    if (!mediaEl) return;

    var tag = mediaEl.tagName ? mediaEl.tagName.toLowerCase() : '';
    if (tag === 'video') {
      ctx.videoEl = mediaEl;
      ctx.onTimeUpdateFn = function () {
        handleTimeUpdateForCtx(ctx, mediaEl.currentTime);
      };
      mediaEl.addEventListener('timeupdate', ctx.onTimeUpdateFn);
      return;
    }

    if (tag === 'iframe' && mediaEl.id && (window.location.protocol === 'http:' || window.location.protocol === 'https:')) {
      var attachYtId = ctx.video ? ctx.video.ytId : '';
      ensureYouTubeApi().then(function (YT) {
        if (!YT || typeof YT.Player !== 'function') return;
        // Ensure context was not torn down or replaced while waiting
        var currentMedia = ctx.getMediaEl ? ctx.getMediaEl() : null;
        if (!currentMedia || currentMedia !== mediaEl || !document.body.contains(mediaEl)) return;
        if (ctx.video && ctx.video.ytId !== attachYtId) return;
        try {
          ctx.ytPlayer = new YT.Player(mediaEl.id, {
            events: {
              onReady: function () {
                ctx.ytReady = true;
              },
              onStateChange: function (ev) {
                if (ev.data === 1) {
                  if (!ctx.pollTimer) {
                    ctx.pollTimer = setInterval(function () {
                      if (ctx.ytPlayer && typeof ctx.ytPlayer.getCurrentTime === 'function') {
                        try {
                          handleTimeUpdateForCtx(ctx, ctx.ytPlayer.getCurrentTime());
                        } catch (e) {}
                      }
                    }, 400);
                  }
                } else {
                  if (ctx.pollTimer) {
                    clearInterval(ctx.pollTimer);
                    ctx.pollTimer = null;
                  }
                }
              }
            }
          });
        } catch (err) {}
      });
    }
  }

  function handleTimeUpdateForCtx(ctx, curSec) {
    if (!ctx || !ctx.video || ctx.video.mode !== 'mock') return;
    var chapters = ctx.video.chapters || [];
    if (!chapters.length) return;
    var t = Number(curSec);
    if (isNaN(t) || t < 0) return;

    // Identify currently playing chapter
    var activeIdx = null;
    for (var i = 0; i < chapters.length; i++) {
      if (t >= chapters[i].start && t < chapters[i].end) {
        activeIdx = chapters[i].idx;
        break;
      }
    }
    if (activeIdx !== null && activeIdx !== ctx.activeChapterIdx) {
      ctx.activeChapterIdx = activeIdx;
      var qMatch = ctx.video.checks.findIndex(function (c) { return c.chapterIdx === activeIdx; });
      if (qMatch !== -1 && qMatch !== ctx.selectedCheckIdx && !ctx.pausedChapter) {
        ctx.selectedCheckIdx = qMatch;
      }
      renderCtx(ctx);
    }

    // Chapter boundary auto-pause (strictly gated by autoPauseEnabled === true)
    if (ctx.autoPauseEnabled && ctx.lastTime !== null) {
      var prev = ctx.lastTime;
      // Only trigger on natural forward playback crossing a chapter end (skip manual jumps > 3s)
      if (t >= prev && (t - prev) <= 3.0) {
        for (var j = 0; j < chapters.length; j++) {
          var ch = chapters[j];
          if (!ch.isQuestion) continue;
          if (ctx.pausedChapterIdxs[ch.idx]) continue;
          if (prev < ch.end - 0.1 && t >= ch.end - 0.25) {
            ctx.pausedChapterIdxs[ch.idx] = true;
            ctx.pausedChapter = ch;
            var checkIdx = ctx.video.checks.findIndex(function (c) { return c.chapterIdx === ch.idx; });
            if (checkIdx !== -1) ctx.selectedCheckIdx = checkIdx;
            pauseCtxPlayer(ctx);
            renderCtx(ctx);
            break;
          }
        }
      }
    }

    ctx.lastTime = t;
  }

  function pauseCtxPlayer(ctx) {
    if (!ctx) return;
    if (ctx.videoEl && typeof ctx.videoEl.pause === 'function') {
      try { ctx.videoEl.pause(); } catch (e) {}
      return;
    }
    if (ctx.ytPlayer && ctx.ytReady && typeof ctx.ytPlayer.pauseVideo === 'function') {
      try { ctx.ytPlayer.pauseVideo(); } catch (e) {}
    }
  }

  function playCtxPlayer(ctx) {
    if (!ctx) return;
    if (ctx.videoEl && typeof ctx.videoEl.play === 'function') {
      try { ctx.videoEl.play().catch(function () {}); } catch (e) {}
      return;
    }
    if (ctx.ytPlayer && ctx.ytReady && typeof ctx.ytPlayer.playVideo === 'function') {
      try { ctx.ytPlayer.playVideo(); } catch (e) {}
    }
  }

  function buildEmbedUrl(ytId, startSec, autoplay) {
    var origin = (window.location.protocol === 'http:' || window.location.protocol === 'https:')
      ? '&origin=' + encodeURIComponent(window.location.origin)
      : '';
    var st = (typeof startSec === 'number' && !isNaN(startSec) && startSec > 0) ? '&start=' + Math.floor(startSec) : '';
    return 'https://www.youtube-nocookie.com/embed/' + ytId +
      '?rel=0&playsinline=1&enablejsapi=1' + origin +
      '&autoplay=' + (autoplay ? '1' : '0') + st;
  }

  function seekCtxTo(ctx, seconds, shouldScroll) {
    if (!ctx) return;
    var sec = Math.max(0, Math.floor(Number(seconds) || 0));
    ctx.pausedChapter = null;
    ctx.lastTime = sec;

    if (shouldScroll && ctx.scrollTarget) {
      var targetEl = ctx.scrollTarget();
      if (targetEl && typeof targetEl.scrollIntoView === 'function') {
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    var mediaEl = ctx.getMediaEl ? ctx.getMediaEl() : null;
    if (!mediaEl) return;

    var tag = mediaEl.tagName ? mediaEl.tagName.toLowerCase() : '';
    if (tag === 'video') {
      mediaEl.currentTime = sec;
      mediaEl.play().catch(function () {});
      return;
    }

    // Topic facade not yet activated
    if (tag !== 'iframe' && mediaEl.classList && mediaEl.classList.contains('mfs-yt-facade')) {
      if (typeof window.mfsActivateTopicVideo === 'function') {
        window.mfsActivateTopicVideo(mediaEl, sec);
      }
      return;
    }

    if (tag === 'iframe') {
      if (ctx.ytPlayer && ctx.ytReady && typeof ctx.ytPlayer.seekTo === 'function') {
        try {
          ctx.ytPlayer.seekTo(sec, true);
          ctx.ytPlayer.playVideo();
          return;
        } catch (e) {}
      }
      var ytId = (ctx.video && ctx.video.ytId) || mediaEl.getAttribute('data-ytid') || '';
      if (!ytId) {
        var m = (mediaEl.src || '').match(/embed\/([a-zA-Z0-9_-]+)/);
        ytId = m ? m[1] : '';
      }
      if (ytId) {
        cleanupPlayer(ctx);
        mediaEl.src = buildEmbedUrl(ytId, sec, true);
        attachPlayerDelayed(ctx);
      }
    }
  }

  function attachPlayerDelayed(ctx) {
    setTimeout(function () {
      attachPlayerSafe(ctx);
    }, 150);
  }

  function attachPlayerSafe(ctx) {
    if (!ctx || !ctx.container || !document.body.contains(ctx.container)) return;
    attachPlayback(ctx);
  }

  function continueAfterPause(ctx) {
    if (!ctx || !ctx.video) return;
    var paused = ctx.pausedChapter;
    ctx.pausedChapter = null;
    var chapters = ctx.video.chapters || [];
    var nextCh = null;
    if (paused) {
      for (var i = 0; i < chapters.length; i++) {
        if (chapters[i].idx > paused.idx) {
          nextCh = chapters[i];
          break;
        }
      }
    }
    if (nextCh) {
      var qIdx = ctx.video.checks.findIndex(function (c) { return c.chapterIdx === nextCh.idx; });
      if (qIdx !== -1) ctx.selectedCheckIdx = qIdx;
      ctx.activeChapterIdx = nextCh.idx;
      renderCtx(ctx);
      seekCtxTo(ctx, nextCh.start, false);
    } else {
      renderCtx(ctx);
      playCtxPlayer(ctx);
    }
  }

  function renderQuestionBox(ctx, ch, qIdx, totalCount, prog) {
    var chosenIdx = Object.prototype.hasOwnProperty.call(prog.answers, ch.id) ? prog.answers[ch.id] : null;
    var isAnswered = chosenIdx !== null;
    var isRight = isAnswered && chosenIdx === ch.correct;
    var tutorName = (ctx.video && ctx.video.tutor) || 'Subi';

    var optsHtml = ch.options.map(function (optText, oi) {
      var cls = 'mfs-vc-opt';
      if (isAnswered) {
        if (oi === ch.correct) cls += ' is-correct';
        else if (oi === chosenIdx) cls += ' is-wrong';
      }
      return (
        '<button type="button" class="' + cls + '" data-vc-qid="' + escapeHtml(ch.id) + '" data-vc-opt="' + oi + '">' +
        '<span class="mfs-vc-opt-letter">' + LETTERS[oi] + '</span>' +
        '<span>' + escapeHtml(optText) + '</span>' +
        '</button>'
      );
    }).join('');

    var feedbackHtml = '';
    if (isAnswered) {
      var fbCls = 'mfs-vc-feedback ' + (isRight ? 'is-good' : 'is-bad');
      var statusText = isRight
        ? '<i class="fa-solid fa-circle-check" style="color:#34d399;"></i> Spot on!'
        : '<i class="fa-solid fa-circle-xmark" style="color:#f87171;"></i> Not quite — check the examiner trap below';
      var jumpBtn = '';
      if (typeof ch.cueSec === 'number' && !isNaN(ch.cueSec)) {
        var btnCls = isRight ? 'mfs-vc-btn-rewatch is-subtle' : 'mfs-vc-btn-rewatch';
        var btnLabel = isRight
          ? 'Review step (' + formatMMSS(ch.cueSec) + ')'
          : 'Watch ' + tutorName + ' explain this step (' + formatMMSS(ch.cueSec) + ')';
        jumpBtn =
          '<div class="mfs-vc-rewatch-row">' +
          '<button type="button" class="' + btnCls + '" data-vc-jump="' + ch.cueSec + '">' +
          '<i class="fa-solid fa-play"></i> ' + escapeHtml(btnLabel) +
          '</button>' +
          (ch.cueLabel ? '<span style="font-size:0.78rem; color:#94a3b8;">Chapter: ' + escapeHtml(ch.cueLabel) + '</span>' : '') +
          '</div>';
      }
      feedbackHtml =
        '<div class="' + fbCls + '">' +
        '<div class="mfs-vc-feedback-status">' + statusText + '</div>' +
        '<div><strong>Why:</strong> ' + escapeHtml(ch.why) + '</div>' +
        jumpBtn +
        '</div>';
    }

    var qPrefix = ctx.video.mode === 'topic' ? ('Q' + (qIdx + 1) + ' of ' + totalCount + ' · ') : '';

    return (
      '<div class="mfs-vc-qbox ' + (isRight ? 'is-done-correct' : '') + '" data-vc-qcard="' + escapeHtml(ch.id) + '">' +
      '<div class="mfs-vc-qmeta">' +
      '<span class="mfs-vc-stage-tag"><i class="fa-solid fa-bolt"></i> ' + escapeHtml(qPrefix + ch.stage) + '</span>' +
      '<span class="mfs-vc-arch-badge" data-arch="' + escapeHtml(ch.archetype) + '">' + escapeHtml(ch.archetype) + '</span>' +
      '</div>' +
      '<p class="mfs-vc-qtext">' + escapeHtml(ch.question) + '</p>' +
      '<div class="mfs-vc-opts">' + optsHtml + '</div>' +
      feedbackHtml +
      '</div>'
    );
  }

  function renderCtx(ctx) {
    if (!ctx || !ctx.container) return;
    var v = ctx.video;
    if (!v || !v.checks || !v.checks.length) {
      ctx.container.innerHTML = '';
      return;
    }

    var prog = getVideoProgress(v.id);
    var total = v.checks.length;
    var clearedCount = v.checks.filter(function (c) {
      return prog.answers[c.id] === c.correct;
    }).length;
    var answeredCount = v.checks.filter(function (c) {
      return Object.prototype.hasOwnProperty.call(prog.answers, c.id);
    }).length;
    var allCleared = clearedCount === total;

    var isMock = v.mode === 'mock';
    var pillLabel = isMock ? 'Examiner Trap CCQs' : '60-Second Concept Check';
    var headingTitle = isMock
      ? 'Per-Question Examiner Trap Checks'
      : 'Quick Concept Check: ' + v.title;

    var collapseIcon = ctx.collapsed ? 'fa-chevron-down' : 'fa-chevron-up';
    var collapseTxt = ctx.collapsed ? 'Open Check' : 'Hide';

    var autoPauseBtn = '';
    if (isMock && v.chapters && v.chapters.length > 0) {
      autoPauseBtn =
        '<button type="button" class="mfs-vc-pause-switch" role="switch" aria-checked="' + (ctx.autoPauseEnabled ? 'true' : 'false') + '" data-vc-toggle-autopause="1">' +
        '<span>Pause after each question for a quick check</span>' +
        '<span class="mfs-vc-switch-track"><span class="mfs-vc-switch-thumb"></span></span>' +
        '<span class="mfs-vc-switch-state">' + (ctx.autoPauseEnabled ? 'ON' : 'OFF') + '</span>' +
        '</button>';
    }

    var pauseBannerHtml = '';
    if (isMock && ctx.pausedChapter) {
      pauseBannerHtml =
        '<div class="mfs-vc-pause-banner">' +
        '<div class="mfs-vc-pause-banner-text">' +
        '<i class="fa-solid fa-circle-pause" style="color:#38bdf8; font-size:1.05rem;"></i>' +
        '<span>Paused after <strong>' + escapeHtml(ctx.pausedChapter.label) + '</strong> — Quick Examiner Check</span>' +
        '</div>' +
        '<div class="mfs-vc-pause-actions">' +
        '<button type="button" class="mfs-vc-btn-continue" data-vc-continue="1">Continue to next question <i class="fa-solid fa-arrow-right"></i></button>' +
        '<button type="button" class="mfs-vc-btn-skip" data-vc-skip-pause="1">Skip check &amp; keep watching</button>' +
        '</div>' +
        '</div>';
    }

    var bodyInner = '';
    if (isMock) {
      // Chapter jump strip for VTT-backed mocks
      var stripHtml = '';
      if (v.checks.some(function (c) { return typeof c.cueSec === 'number'; })) {
        stripHtml = '<div class="mfs-vc-chapter-strip">' +
          v.checks.map(function (c, idx) {
            var isAct = idx === ctx.selectedCheckIdx;
            var isAns = Object.prototype.hasOwnProperty.call(prog.answers, c.id);
            var isCor = prog.answers[c.id] === c.correct;
            var timeTxt = typeof c.cueSec === 'number' ? ' <span class="mfs-vc-chap-time">' + formatMMSS(c.cueSec) + '</span>' : '';
            var dot = isAns
              ? (isCor ? '<i class="fa-solid fa-circle-check mfs-vc-chap-dot" style="color:#34d399;"></i>' : '<i class="fa-solid fa-circle-exclamation mfs-vc-chap-dot" style="color:#fbbf24;"></i>')
              : '<i class="fa-regular fa-circle mfs-vc-chap-dot" style="color:#64748b;"></i>';
            return (
              '<button type="button" class="mfs-vc-chap-btn' + (isAct ? ' is-active' : '') + (isAns ? ' is-answered' : '') + '" data-vc-select-idx="' + idx + '">' +
              dot + ' <span>' + escapeHtml(c.stage) + '</span>' + timeTxt +
              '</button>'
            );
          }).join('') +
          '</div>';
      }

      var curIdx = Math.min(Math.max(ctx.selectedCheckIdx || 0, 0), v.checks.length - 1);
      var activeCheck = v.checks[curIdx];
      var navHtml = v.checks.length > 1 ? (
        '<div class="mfs-vc-mock-nav">' +
        '<button type="button" class="mfs-vc-btn-icon" data-vc-prev-q="1" ' + (curIdx === 0 ? 'disabled style="opacity:0.45;cursor:not-allowed;"' : '') + '>' +
        '<i class="fa-solid fa-arrow-left"></i> Previous Question' +
        '</button>' +
        '<span style="font-size:0.8rem; color:#94a3b8; font-weight:700;">Trap Check ' + (curIdx + 1) + ' of ' + v.checks.length + '</span>' +
        '<button type="button" class="mfs-vc-btn-icon" data-vc-next-q="1" ' + (curIdx >= v.checks.length - 1 ? 'disabled style="opacity:0.45;cursor:not-allowed;"' : '') + '>' +
        'Next Question <i class="fa-solid fa-arrow-right"></i>' +
        '</button>' +
        '</div>'
      ) : '';

      bodyInner = pauseBannerHtml + stripHtml +
        '<div class="mfs-vc-questions-list">' + renderQuestionBox(ctx, activeCheck, curIdx, total, prog) + '</div>' +
        navHtml;
    } else {
      // Topic Mode: All 3 progressive questions visible together
      bodyInner =
        '<div class="mfs-vc-questions-list">' +
        v.checks.map(function (c, idx) {
          return renderQuestionBox(ctx, c, idx, total, prog);
        }).join('') +
        '</div>';
    }

    var completeHtml = allCleared ? (
      '<div class="mfs-vc-complete-banner">' +
      '<span><i class="fa-solid fa-award" style="color:#34d399;"></i> ' + total + '/' + total + ' Concept Checks Cleared! Ready for exam-style practice.</span>' +
      '<button type="button" class="mfs-vc-btn-icon" data-vc-reset="1"><i class="fa-solid fa-rotate-left"></i> Reset Check</button>' +
      '</div>'
    ) : (answeredCount > 0 ? (
      '<div style="margin-top:10px; display:flex; justify-content:flex-end;">' +
      '<button type="button" class="mfs-vc-btn-icon" data-vc-reset="1"><i class="fa-solid fa-rotate-left"></i> Reset Answers</button>' +
      '</div>'
    ) : '');

    var wrapCls = 'mfs-vc-wrap' + (ctx.compact ? ' is-modal' : '');
    var cardCls = 'mfs-vc-card' + (ctx.collapsed ? ' is-collapsed' : '') + (ctx.pausedChapter ? ' is-paused-alert' : '');

    ctx.container.innerHTML =
      '<div class="' + wrapCls + '">' +
      '<div class="' + cardCls + '" data-vc-slug="' + escapeHtml(v.id) + '" data-vc-mode="' + escapeHtml(v.mode) + '">' +
      '<div class="mfs-vc-head">' +
      '<div class="mfs-vc-head-left">' +
      '<div class="mfs-vc-badges">' +
      '<span class="mfs-vc-pill"><i class="fa-solid fa-brain"></i> ' + escapeHtml(pillLabel) + '</span>' +
      '<span class="mfs-vc-tutor-pill"><i class="fa-solid fa-user-graduate" style="color:#38bdf8;"></i> Tutor ' + escapeHtml(v.tutor) + '</span>' +
      '</div>' +
      '<h3 class="mfs-vc-title">' + escapeHtml(headingTitle) + '</h3>' +
      '</div>' +
      '<div class="mfs-vc-head-right">' +
      autoPauseBtn +
      '<span class="mfs-vc-progress' + (allCleared ? ' is-complete' : '') + '">' +
      '<i class="fa-solid ' + (allCleared ? 'fa-circle-check' : 'fa-list-check') + '"></i> ' +
      clearedCount + ' / ' + total + ' Cleared' +
      '</span>' +
      '<button type="button" class="mfs-vc-btn-icon" data-vc-collapse="1" aria-expanded="' + (ctx.collapsed ? 'false' : 'true') + '">' +
      '<i class="fa-solid ' + collapseIcon + '"></i> <span>' + collapseTxt + '</span>' +
      '</button>' +
      '</div>' +
      '</div>' +
      '<div class="mfs-vc-body">' + bodyInner + completeHtml + '</div>' +
      '</div>' +
      '</div>';

    bindCtxEvents(ctx);
  }

  function bindCtxEvents(ctx) {
    var root = ctx.container;
    if (!root) return;

    var collapseBtn = root.querySelector('[data-vc-collapse]');
    if (collapseBtn) {
      collapseBtn.addEventListener('click', function () {
        ctx.collapsed = !ctx.collapsed;
        renderCtx(ctx);
      });
    }

    var autoBtn = root.querySelector('[data-vc-toggle-autopause]');
    if (autoBtn) {
      autoBtn.addEventListener('click', function () {
        ctx.autoPauseEnabled = !ctx.autoPauseEnabled;
        setAutoPausePref(ctx.autoPauseEnabled);
        if (!ctx.autoPauseEnabled) ctx.pausedChapter = null;
        renderCtx(ctx);
      });
    }

    var contBtn = root.querySelector('[data-vc-continue]');
    if (contBtn) {
      contBtn.addEventListener('click', function () {
        continueAfterPause(ctx);
      });
    }

    var skipBtn = root.querySelector('[data-vc-skip-pause]');
    if (skipBtn) {
      skipBtn.addEventListener('click', function () {
        ctx.pausedChapter = null;
        renderCtx(ctx);
        playCtxPlayer(ctx);
      });
    }

    var resetBtn = root.querySelector('[data-vc-reset]');
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        resetVideoProgress(ctx.video.id);
        renderCtx(ctx);
      });
    }

    root.querySelectorAll('[data-vc-select-idx]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var idx = parseInt(btn.getAttribute('data-vc-select-idx'), 10);
        if (!isNaN(idx)) {
          ctx.selectedCheckIdx = idx;
          ctx.pausedChapter = null;
          renderCtx(ctx);
        }
      });
    });

    var prevQ = root.querySelector('[data-vc-prev-q]');
    if (prevQ) {
      prevQ.addEventListener('click', function () {
        if (ctx.selectedCheckIdx > 0) {
          ctx.selectedCheckIdx--;
          renderCtx(ctx);
        }
      });
    }

    var nextQ = root.querySelector('[data-vc-next-q]');
    if (nextQ) {
      nextQ.addEventListener('click', function () {
        if (ctx.selectedCheckIdx < ctx.video.checks.length - 1) {
          ctx.selectedCheckIdx++;
          renderCtx(ctx);
        }
      });
    }

    root.querySelectorAll('[data-vc-opt]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var qid = btn.getAttribute('data-vc-qid');
        var oi = parseInt(btn.getAttribute('data-vc-opt'), 10);
        var ch = ctx.video.checks.find(function (c) { return c.id === qid; });
        if (!ch || isNaN(oi)) return;
        saveCheckAnswer(ctx.video.id, qid, oi, oi === ch.correct);
        renderCtx(ctx);
      });
    });

    root.querySelectorAll('[data-vc-jump]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var sec = parseInt(btn.getAttribute('data-vc-jump'), 10);
        if (!isNaN(sec)) {
          seekCtxTo(ctx, sec, ctx.surface === 'topic');
        }
      });
    });
  }

  function createContext(surface, container, video, opts) {
    return {
      surface: surface,
      container: container,
      video: video,
      compact: Boolean(opts && opts.compact),
      collapsed: Boolean(opts && opts.collapsed),
      autoPauseEnabled: getAutoPausePref(),
      selectedCheckIdx: 0,
      activeChapterIdx: null,
      pausedChapter: null,
      pausedChapterIdxs: {},
      lastTime: null,
      ytPlayer: null,
      ytReady: false,
      videoEl: null,
      pollTimer: null,
      onTimeUpdateFn: null,
      getMediaEl: opts && opts.getMediaEl,
      scrollTarget: opts && opts.scrollTarget
    };
  }

  function findTopicMountContainer() {
    var existing = document.getElementById('mfsTopicConceptCheck');
    if (existing) return existing;

    var videoSec = document.getElementById('video-station');
    var playerEl = document.getElementById('topicMasterclassIframe') || document.getElementById('topicSlcVideoPlayer');
    if (!playerEl) return null;

    var mount = document.createElement('div');
    mount.id = 'mfsTopicConceptCheck';

    if (videoSec) {
      var jumpBar = document.getElementById('mcJumpBar');
      var cardContainer = jumpBar ? jumpBar.parentElement : null;
      if (cardContainer && cardContainer.parentNode) {
        cardContainer.parentNode.insertBefore(mount, cardContainer.nextSibling);
        return mount;
      }
      videoSec.appendChild(mount);
      return mount;
    }

    var wrap = playerEl.closest('.video-exemplar-card, .video-screen-wrap, section') || playerEl.parentNode;
    if (wrap && wrap.parentNode) {
      wrap.parentNode.insertBefore(mount, wrap.nextSibling);
    }
    return mount;
  }

  function resolveTopicIdentifier() {
    var el = document.getElementById('topicMasterclassIframe');
    if (el) {
      var yt = el.getAttribute('data-ytid');
      if (yt) return yt;
      var m = (el.src || '').match(/embed\/([a-zA-Z0-9_-]+)/);
      if (m) return m[1];
    }
    var stLink = document.getElementById('mcStationLink');
    if (stLink) {
      var hm = (stLink.getAttribute('href') || '').match(/[?&]topic=([^&#]+)/);
      if (hm) return decodeURIComponent(hm[1]);
    }
    return null;
  }

  function mountTopicPage(overrideIdentifier) {
    var mount = findTopicMountContainer();
    if (!mount) return Promise.resolve(null);
    var ident = overrideIdentifier || resolveTopicIdentifier();
    if (!ident) return Promise.resolve(null);

    return loadData().then(function (data) {
      var video = lookupVideo(data, ident);
      if (!video) {
        mount.innerHTML = '';
        return null;
      }
      if (contexts.topic) cleanupPlayer(contexts.topic);
      var isMobileViewport = Boolean(window.matchMedia && window.matchMedia('(max-width: 768px)').matches);
      var ctx = createContext('topic', mount, video, {
        compact: false,
        collapsed: isMobileViewport,
        getMediaEl: function () {
          return document.getElementById('topicMasterclassIframe');
        },
        scrollTarget: function () {
          var el = document.getElementById('topicMasterclassIframe');
          return (el && el.parentElement) || el;
        }
      });
      contexts.topic = ctx;
      renderCtx(ctx);
      attachPlayerSafe(ctx);
      return ctx;
    }).catch(function () { return null; });
  }

  function mountStation(itemOrSlug) {
    var mount = document.getElementById('mfsStationConceptCheck');
    if (!mount) return Promise.resolve(null);
    var ident = typeof itemOrSlug === 'string'
      ? itemOrSlug
      : ((itemOrSlug && (itemOrSlug.id || itemOrSlug.ytId)) || '');
    if (!ident) return Promise.resolve(null);

    return loadData().then(function (data) {
      var video = lookupVideo(data, ident) || (itemOrSlug && itemOrSlug.ytId ? lookupVideo(data, itemOrSlug.ytId) : null);
      if (!video) {
        if (contexts.station) cleanupPlayer(contexts.station);
        contexts.station = null;
        mount.innerHTML = '';
        return null;
      }
      if (contexts.station) cleanupPlayer(contexts.station);
      var ctx = createContext('station', mount, video, {
        compact: false,
        collapsed: false,
        getMediaEl: function () {
          return document.getElementById('stationLocalPlayer') ||
                 document.getElementById('stationYtPlayer') ||
                 document.querySelector('#mainPlayerContainer iframe, #mainPlayerContainer video');
        },
        scrollTarget: function () {
          return document.getElementById('mainPlayerContainer');
        }
      });
      contexts.station = ctx;
      renderCtx(ctx);
      attachPlayerDelayed(ctx);
      return ctx;
    }).catch(function () { return null; });
  }

  function mountModal(container, opts) {
    if (!container) return Promise.resolve(null);
    var slug = opts && opts.slug;
    var ytId = opts && opts.ytId;
    if (!slug && !ytId) {
      container.innerHTML = '';
      return Promise.resolve(null);
    }

    return loadData().then(function (data) {
      var video = lookupVideo(data, slug) || lookupVideo(data, ytId);
      if (!video) {
        if (contexts.modal) cleanupPlayer(contexts.modal);
        contexts.modal = null;
        container.innerHTML = '';
        return null;
      }
      if (contexts.modal) cleanupPlayer(contexts.modal);
      var ctx = createContext('modal', container, video, {
        compact: true,
        collapsed: true,
        getMediaEl: function () {
          return document.getElementById('mfsModalYtPlayer') ||
                 document.querySelector('#mfsPlayerBox video, #mfsPlayerBox iframe');
        },
        scrollTarget: function () {
          return document.getElementById('mfsPlayerBox');
        }
      });
      contexts.modal = ctx;
      renderCtx(ctx);
      attachPlayerDelayed(ctx);
      return ctx;
    }).catch(function () { return null; });
  }

  function unmountModal() {
    if (contexts.modal) {
      cleanupPlayer(contexts.modal);
      if (contexts.modal.container) contexts.modal.container.innerHTML = '';
      contexts.modal = null;
    }
  }

  function seekTopicPlayer(seconds) {
    var ctx = contexts.topic;
    if (ctx && ctx.ytPlayer && ctx.ytReady && typeof ctx.ytPlayer.seekTo === 'function') {
      try {
        ctx.ytPlayer.seekTo(Math.max(0, Math.floor(seconds || 0)), true);
        ctx.ytPlayer.playVideo();
        return true;
      } catch (e) {}
    }
    return false;
  }

  function onTopicIframeActivated(iframeEl) {
    var ctx = contexts.topic;
    if (!ctx) return;
    if (iframeEl && ctx.video) {
      attachPlayerDelayed(ctx);
    }
  }

  function refreshTopicByYtId(ytId) {
    if (!ytId) return;
    mountTopicPage(ytId);
  }

  function refreshTopicBySlug(slug) {
    if (!slug) return;
    mountTopicPage(slug);
  }

  // Deterministic hook for live polling & automated verification
  function handleTimeUpdate(seconds, surface) {
    var target = surface ? contexts[surface] : (contexts.station || contexts.modal || contexts.topic);
    if (target) {
      handleTimeUpdateForCtx(target, seconds);
      return true;
    }
    return false;
  }

  window.MfsVideoChecks = {
    loadData: loadData,
    mountTopicPage: mountTopicPage,
    mountStation: mountStation,
    mountModal: mountModal,
    unmountModal: unmountModal,
    seekTopicPlayer: seekTopicPlayer,
    onTopicIframeActivated: onTopicIframeActivated,
    refreshTopicByYtId: refreshTopicByYtId,
    refreshTopicBySlug: refreshTopicBySlug,
    _handleTimeUpdate: handleTimeUpdate
  };

  // Auto-mount on revision topic pages (or station fallback) once DOM is ready
  function autoBoot() {
    var stationMount = document.getElementById('mfsStationConceptCheck');
    if (stationMount) {
      if (!stationMount.hasChildNodes() && window.MFS_STATION_CURRENT_ITEM) {
        mountStation(window.MFS_STATION_CURRENT_ITEM);
      }
      return;
    }
    if (document.getElementById('topicMasterclassIframe')) {
      mountTopicPage();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoBoot);
  } else {
    autoBoot();
  }
})();
