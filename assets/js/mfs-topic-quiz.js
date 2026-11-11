/**
 * MASTER FUNCTIONAL SKILLS — INTERACTIVE 5-QUESTION TOPIC CHECK ENGINE
 * Dynamically builds an authentic Pearson Edexcel aligned self-marking Topic Test
 * from each module's verified answer sheet (worksheets/<stem>-answers.html).
 */
(function() {
  'use strict';

  var modalEl = null;

  function ensureQuizModal() {
    if (modalEl) return modalEl;
    var st = document.createElement('style');
    st.textContent = [
      '.mfs-quiz-backdrop{position:fixed;inset:0;background:rgba(10,15,29,0.78);backdrop-filter:blur(6px);z-index:99998;display:none;align-items:center;justify-content:center;padding:16px;}',
      '.mfs-quiz-backdrop.open{display:flex;}',
      '.mfs-quiz-dialog{background:#ffffff;color:#0f172a;width:100%;max-width:740px;max-height:90vh;border-radius:18px;border:2px solid #0284c7;box-shadow:0 24px 60px rgba(0,0,0,0.45);display:flex;flex-direction:column;overflow:hidden;font-family:Lexend,system-ui,sans-serif;}',
      '.mfs-quiz-head{background:linear-gradient(135deg,#0a0f1d 0%,#0f172a 100%);color:#fff;padding:16px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px;border-bottom:2px solid #0284c7;}',
      '.mfs-quiz-body{padding:20px 22px;overflow-y:auto;flex:1;background:#fdfbf7;}',
      '.mfs-quiz-qcard{background:#fff;border:1.5px solid #cbd5e1;border-radius:12px;padding:16px 18px;margin-bottom:16px;}',
      '.mfs-quiz-opt{display:flex;align-items:flex-start;gap:10px;width:100%;text-align:left;background:#f8fafc;border:1.5px solid #cbd5e1;border-radius:10px;padding:10px 14px;margin-top:8px;cursor:pointer;font-family:inherit;font-size:0.92rem;color:#0f172a;transition:all 0.15s ease;}',
      '.mfs-quiz-opt:hover{border-color:#0284c7;background:#f0f9ff;}',
      '.mfs-quiz-opt.selected{border-color:#0284c7;background:#e0f2fe;font-weight:700;}',
      '.mfs-quiz-opt.correct{border-color:#059669 !important;background:#ecfdf5 !important;color:#065f46 !important;font-weight:700;}',
      '.mfs-quiz-opt.wrong{border-color:#dc2626 !important;background:#fef2f2 !important;color:#991b1b !important;}',
      '.mfs-quiz-exp{display:none;margin-top:10px;padding:10px 12px;border-radius:8px;background:#f0fdf4;border-left:4px solid #0f766e;font-size:0.85rem;color:#1e293b;line-height:1.55;}',
      '.mfs-quiz-foot{padding:14px 22px;background:#f8fafc;border-top:1px solid #e2e8f0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}'
    ].join('\n');
    document.head.appendChild(st);

    modalEl = document.createElement('div');
    modalEl.className = 'mfs-quiz-backdrop';
    modalEl.id = 'mfsTopicQuizModal';
    modalEl.innerHTML = [
      '<div class="mfs-quiz-dialog" role="dialog" aria-modal="true" aria-labelledby="mfsQuizTitle">',
      '  <div class="mfs-quiz-head">',
      '    <div>',
      '      <div style="font-size:0.74rem;font-weight:800;color:#38bdf8;text-transform:uppercase;letter-spacing:0.05em;">Instant Self-Marking Assessment</div>',
      '      <h3 id="mfsQuizTitle" style="margin:2px 0 0;font-size:1.1rem;font-weight:800;color:#fff;">Topic Check</h3>',
      '    </div>',
      '    <button type="button" id="mfsQuizClose" aria-label="Close quiz" style="background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);color:#fff;width:36px;height:36px;border-radius:8px;cursor:pointer;font-size:1.05rem;">&times;</button>',
      '  </div>',
      '  <div class="mfs-quiz-body" id="mfsQuizBody"></div>',
      '  <div class="mfs-quiz-foot">',
      '    <div id="mfsQuizScore" style="font-size:0.92rem;font-weight:800;color:#0f172a;">Select an answer for each question, then click Check Answers.</div>',
      '    <div style="display:flex;gap:10px;">',
      '      <a id="mfsQuizFullSheet" href="#" target="_blank" rel="noopener" style="padding:9px 14px;border-radius:8px;border:1.5px solid #cbd5e1;background:#fff;color:#0f172a;text-decoration:none;font-size:0.85rem;font-weight:700;">Full Printable Exam Sheet</a>',
      '      <button type="button" id="mfsQuizSubmit" style="padding:9px 18px;border-radius:8px;border:none;background:#0284c7;color:#fff;font-family:inherit;font-size:0.88rem;font-weight:800;cursor:pointer;">Check Answers</button>',
      '    </div>',
      '  </div>',
      '</div>'
    ].join('');
    document.body.appendChild(modalEl);

    document.getElementById('mfsQuizClose').addEventListener('click', function() {
      modalEl.classList.remove('open');
    });
    modalEl.addEventListener('click', function(e) {
      if (e.target === modalEl) modalEl.classList.remove('open');
    });
    return modalEl;
  }

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  function buildNumericDistractors(ansText) {
    var m = ansText.match(/-?\d+(?:\.\d+)?/);
    if (!m) return ['None of the given statements', 'Insufficient data provided', 'Requires inverse operation'];
    var val = parseFloat(m[0]);
    var d1 = ansText.replace(m[0], String(Math.round((val * 1.25 + 2) * 100) / 100));
    var d2 = ansText.replace(m[0], String(Math.round((Math.abs(val - 3) || 5) * 100) / 100));
    var d3 = ansText.replace(m[0], String(Math.round((val * 0.5 + 1) * 100) / 100));
    return [d1, d2, d3];
  }

  function openTopicQuiz(stem, title, topicSlug) {
    var m = ensureQuizModal();
    var body = document.getElementById('mfsQuizBody');
    var titleEl = document.getElementById('mfsQuizTitle');
    var scoreEl = document.getElementById('mfsQuizScore');
    var submitBtn = document.getElementById('mfsQuizSubmit');
    var sheetLink = document.getElementById('mfsQuizFullSheet');

    titleEl.textContent = title + ' — 5-Question Topic Test';
    sheetLink.href = 'worksheets/' + stem + '-worksheet.html';
    scoreEl.innerHTML = 'Answer all questions below, then click <strong>Check Answers</strong>.';
    submitBtn.style.display = 'inline-block';
    body.innerHTML = '<div style="padding:28px;text-align:center;color:#475569;font-weight:700;">Loading verified Pearson Edexcel assessment items...</div>';
    m.classList.add('open');

    fetch('worksheets/' + stem + '-answers.html')
      .then(function(r) { return r.ok ? r.text() : Promise.reject('missing'); })
      .then(function(html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var cards = Array.prototype.slice.call(doc.querySelectorAll('.ans-card')).slice(0, 5);
        if (!cards.length) throw new Error('empty');

        var allCorrects = cards.map(function(c) {
          var av = c.querySelector('.award-val');
          return av ? av.textContent.trim() : 'Model response verified';
        });

        var qData = cards.map(function(c, idx) {
          var stemEl = c.querySelector('.ans-stem-quote');
          var qHtml = stemEl ? stemEl.innerHTML : 'Complete question ' + (idx + 1);
          var correct = allCorrects[idx];
          var steps = Array.prototype.slice.call(c.querySelectorAll('.step-row span:first-child')).map(function(s) { return s.textContent.trim(); }).join(' ');
          var pool = allCorrects.filter(function(x, i) { return i !== idx && x !== correct; });
          if (pool.length < 3) {
            pool = pool.concat(buildNumericDistractors(correct));
          }
          var distractors = [];
          pool.forEach(function(p) {
            if (p !== correct && distractors.indexOf(p) === -1 && distractors.length < 3) distractors.push(p);
          });
          while (distractors.length < 3) {
            distractors.push('Alternative distractor ' + (distractors.length + 1));
          }
          var opts = shuffle([
            { text: correct, isCorrect: true },
            { text: distractors[0], isCorrect: false },
            { text: distractors[1], isCorrect: false },
            { text: distractors[2], isCorrect: false }
          ]);
          return { qHtml: qHtml, opts: opts, steps: steps, correct: correct };
        });

        body.innerHTML = qData.map(function(q, qi) {
          var optsHtml = q.opts.map(function(o, oi) {
            var letter = ['A', 'B', 'C', 'D'][oi];
            return '<button type="button" class="mfs-quiz-opt" data-qi="' + qi + '" data-correct="' + (o.isCorrect ? '1' : '0') + '">' +
              '<span style="background:#e2e8f0;color:#0f172a;font-weight:800;padding:2px 8px;border-radius:5px;font-size:0.8rem;flex-shrink:0;">' + letter + '</span>' +
              '<span>' + o.text.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</span></button>';
          }).join('');
          return '<div class="mfs-quiz-qcard" data-qcard="' + qi + '">' +
            '<div style="font-size:0.78rem;font-weight:800;color:#0284c7;text-transform:uppercase;margin-bottom:6px;">Question ' + (qi + 1) + ' of ' + qData.length + '</div>' +
            '<div style="font-size:0.95rem;line-height:1.6;color:#0f172a;margin-bottom:8px;">' + q.qHtml + '</div>' +
            '<div class="mfs-quiz-opts">' + optsHtml + '</div>' +
            '<div class="mfs-quiz-exp" id="mfsQuizExp' + qi + '"><strong>Model Method:</strong> ' + q.steps.replace(/</g, '&lt;') + '</div>' +
            '</div>';
        }).join('');

        body.querySelectorAll('.mfs-quiz-opt').forEach(function(btn) {
          btn.addEventListener('click', function() {
            var qi = btn.getAttribute('data-qi');
            body.querySelectorAll('.mfs-quiz-opt[data-qi="' + qi + '"]').forEach(function(b) { b.classList.remove('selected'); });
            btn.classList.add('selected');
          });
        });

        submitBtn.onclick = function() {
          var score = 0;
          qData.forEach(function(_, qi) {
            var opts = body.querySelectorAll('.mfs-quiz-opt[data-qi="' + qi + '"]');
            opts.forEach(function(b) {
              var isC = b.getAttribute('data-correct') === '1';
              if (isC) b.classList.add('correct');
              if (b.classList.contains('selected')) {
                if (isC) score++;
                else b.classList.add('wrong');
              }
            });
            var exp = document.getElementById('mfsQuizExp' + qi);
            if (exp) exp.style.display = 'block';
          });
          var pct = Math.round((score / qData.length) * 100);
          scoreEl.innerHTML = 'Score: <span style="color:' + (pct >= 80 ? '#059669' : '#d97706') + ';">' + score + ' / ' + qData.length + ' (' + pct + '%)</span>' +
            (pct >= 80 ? ' — Topic Mastered! Checked off on your tracker.' : ' — Review the green model methods above.');
          if (pct >= 80 && topicSlug) {
            var cb = document.querySelector('input[data-topic-slug="' + topicSlug + '"]');
            if (cb && !cb.checked) {
              cb.checked = true;
              if (window.toggleMfsMastery) window.toggleMfsMastery(cb);
            }
          }
        };
      })
      .catch(function() {
        body.innerHTML = '<div style="padding:24px;text-align:center;"><p style="margin-bottom:14px;color:#334155;">Open the full exam-style practice paper &amp; mark scheme for <strong>' + title + '</strong>:</p>' +
          '<a href="worksheets/' + stem + '-worksheet.html" target="_blank" style="display:inline-block;background:#0284c7;color:#fff;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:800;">Open Practice Questions</a></div>';
        submitBtn.style.display = 'none';
      });
  }

  document.addEventListener('click', function(e) {
    var btn = e.target.closest && e.target.closest('.btn-mfs-test');
    if (!btn) return;
    var row = btn.closest('.topic-row');
    if (!row) return;
    var wsLink = row.querySelector('a[href*="-worksheet.html"]');
    if (!wsLink) return;
    e.preventDefault();
    var m = wsLink.getAttribute('href').match(/worksheets\/(.+)-worksheet\.html/);
    if (!m) return;
    var stem = m[1];
    var titleEl = row.querySelector('.topic-title');
    var title = titleEl ? titleEl.textContent.trim() : stem;
    var revLink = row.querySelector('.btn-mfs-revise');
    var slug = revLink ? revLink.getAttribute('href').replace('.html', '') : '';
    openTopicQuiz(stem, title, slug);
  });
})();
