/**
 * Master Functional Skills (MFS) — Digital Functional Skills Interactive Mini-Labs
 * Provides live hands-on practice sandboxes across all 39 Entry 3 & Level 1 topics:
 *  1. spreadsheet-formula (live formulas, formatting toolbar, chart validator)
 *  2. email-validator     (To/CC/BCC/GDPR/attachments/calendar/cloud sharing)
 *  3. folder-zip          (file naming, folder tree, ZIP extraction, doc preflight)
 *  4. security-inspector  (phishing red-flags, password strength, IT/GDPR scenarios)
 */
(function () {
  'use strict';

  function esc(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function feedbackHtml(passed, items) {
    const cls = passed ? 'pass' : 'fail';
    const icon = passed ? 'fa-circle-check' : 'fa-triangle-exclamation';
    const heading = passed
      ? 'All Exam Criteria Met — Full Marks Achieved!'
      : 'Review Highlighted Examiner Feedback Below:';
    const rows = items.map(it => {
      const ok = it.ok;
      const ic = ok ? 'fa-check' : 'fa-xmark';
      const co = ok ? '#0f766e' : '#b91c1c';
      return `<li style="color:${co};"><i class="fa-solid ${ic}"></i> <span>${it.msg}</span></li>`;
    }).join('');
    return `<div class="dfs-lab-feedback ${cls}">
      <div class="dfs-lab-fb-head"><i class="fa-solid ${icon}"></i> ${heading}</div>
      <ul class="dfs-lab-fb-list">${rows}</ul>
    </div>`;
  }

  /* =========================================================================
     1. SPREADSHEET FORMULA, FORMATTING & CHARTS SANDBOX
     ========================================================================= */
  function renderSpreadsheet(host, preset) {
    if (preset === 'l1-design') {
      return renderSpreadsheetDesign(host);
    }
    if (preset === 'l1-charts') {
      return renderSpreadsheetCharts(host);
    }

    const isE3 = (preset === 'e3-basic');
    const tasks = isE3
      ? [
          {
            id: 'sum',
            label: 'SUM Total (B6)',
            prompt: 'Type the exact spreadsheet formula in cell <strong>B6</strong> to calculate the total number of weekly appointments across cells <code>B2:B5</code>.',
            hint: '=SUM(B2:B5)',
            targetLabel: 'Cell B6',
            validate: (raw) => {
              const s = raw.replace(/\s+/g, '').toUpperCase();
              const issues = [];
              if (!s.startsWith('=')) issues.push({ ok: false, msg: 'Formulas must always begin with an <strong>=</strong> sign.' });
              else issues.push({ ok: true, msg: 'Starts cleanly with <code>=</code>.' });
              if (/[0-9]{2}\+[0-9]{2}/.test(s) || s === '=12+18+15+20') {
                issues.push({ ok: false, msg: '<strong>[B1] Trap:</strong> Never hardcode values — use the cell range <code>B2:B5</code>.' });
              }
              const okSum = s === '=SUM(B2:B5)' || s === '=B2+B3+B4+B5';
              if (okSum) {
                issues.push({ ok: true, msg: '<strong>[M1][A1]</strong> Valid range reference computes <strong>65</strong> dynamically.' });
              } else {
                issues.push({ ok: false, msg: 'Expected function <code>=SUM(B2:B5)</code> to add Monday to Thursday visits.' });
              }
              return { ok: okSum, val: okSum ? '65' : '#CHECK', items: issues };
            }
          }
        ]
      : [
          {
            id: 'mul',
            label: '1. Multiply (D2)',
            prompt: 'Write the formula for cell <strong>D2</strong> to multiply Unit Price (<code>B2</code> = £4.50) by Quantity (<code>C2</code> = 12).',
            hint: '=B2*C2',
            targetLabel: 'Cell D2',
            validate: (raw) => {
              const s = raw.replace(/\s+/g, '').toUpperCase();
              const okMul = (s === '=B2*C2' || s === '=C2*B2');
              const items = [
                s.startsWith('=') ? { ok: true, msg: 'Formula begins with <code>=</code>.' } : { ok: false, msg: 'Missing leading <code>=</code> sign.' },
                /[X×]/.test(s) ? { ok: false, msg: 'Use the asterisk <code>*</code> for multiplication, never <code>x</code>.' } : { ok: true, msg: 'Operator syntax valid.' },
                okMul ? { ok: true, msg: '<strong>[M1][A1]</strong> Uses dynamic cell references <code>=B2*C2</code> &rarr; <strong>£54.00</strong>.' } : { ok: false, msg: 'Multiply cells <code>B2</code> and <code>C2</code> using <code>=B2*C2</code>.' }
              ];
              return { ok: okMul, val: okMul ? '£54.00' : '#CHECK', items };
            }
          },
          {
            id: 'stats',
            label: '2. =SUM / =AVERAGE',
            prompt: 'Calculate the <strong>mean average</strong> cost of the four items listed in cells <code>D2:D5</code> (cell <strong>D6</strong>).',
            hint: '=AVERAGE(D2:D5)',
            targetLabel: 'Cell D6',
            validate: (raw) => {
              const s = raw.replace(/\s+/g, '').toUpperCase();
              const okAvg = s === '=AVERAGE(D2:D5)';
              const items = [
                /^=MEAN\(/.test(s) ? { ok: false, msg: 'Excel uses <code>=AVERAGE(...)</code>, not <code>=MEAN(...)</code>.' } : { ok: true, msg: 'Function keyword checked.' },
                okAvg ? { ok: true, msg: '<strong>[M1][A1]</strong> <code>=AVERAGE(D2:D5)</code> evaluates the mean across 4 rows correctly (<strong>£39.50</strong>).' } : { ok: false, msg: 'Use <code>=AVERAGE(D2:D5)</code> covering all four rows.' }
              ];
              return { ok: okAvg, val: okAvg ? '£39.50' : '#CHECK', items };
            }
          },
          {
            id: 'if',
            label: '3. =IF Decision',
            prompt: 'In cell <strong>E2</strong>, display <code>"Reorder"</code> if Stock <code>C2</code> is less than <code>15</code>, otherwise display <code>"OK"</code>.',
            hint: '=IF(C2<15,"Reorder","OK")',
            targetLabel: 'Cell E2',
            validate: (raw) => {
              const clean = raw.trim().replace(/’|‘|“|”/g, '"');
              const upper = clean.replace(/\s+/g, '').toUpperCase();
              const okIf = /^=IF\((C2<15|15>C2),"REORDER","OK"\)$/.test(upper) || /^=IF\((C2>=15|15<=C2),"OK","REORDER"\)$/.test(upper);
              const items = [
                upper.startsWith('=IF(') ? { ok: true, msg: 'Starts with <code>=IF(condition, true_text, false_text)</code>.' } : { ok: false, msg: 'Begin with <code>=IF(...)</code>.' },
                clean.includes('"') ? { ok: true, msg: 'Text outputs correctly enclosed in double quotes <code>"..."</code>.' } : { ok: false, msg: 'Wrap text outputs in double quotes, e.g. <code>"Reorder"</code>.' },
                okIf ? { ok: true, msg: '<strong>[B1][A1]</strong> Condition compares <code>C2 &lt; 15</code> correctly (since 12 &lt; 15 &rarr; <strong>Reorder</strong>).' } : { ok: false, msg: 'Expected <code>=IF(C2&lt;15,"Reorder","OK")</code>.' }
              ];
              return { ok: okIf, val: okIf ? 'Reorder' : '#CHECK', items };
            }
          }
        ];

    let activeIdx = 0;

    function draw() {
      const t = tasks[activeIdx];
      const tabsHtml = tasks.length > 1
        ? `<div class="dfs-lab-tabs">${tasks.map((tk, i) => `<button type="button" class="dfs-lab-tab ${i === activeIdx ? 'active' : ''}" data-idx="${i}">${esc(tk.label)}</button>`).join('')}</div>`
        : '';

      const gridHtml = isE3
        ? `<div class="dfs-table-scroll"><table class="dfs-sheet-grid">
            <thead><tr><th></th><th>A</th><th>B</th></tr></thead>
            <tbody>
              <tr><th>1</th><td><strong>Day</strong></td><td><strong>Appointments</strong></td></tr>
              <tr><th>2</th><td>Monday</td><td>12</td></tr>
              <tr><th>3</th><td>Tuesday</td><td>18</td></tr>
              <tr><th>4</th><td>Wednesday</td><td>15</td></tr>
              <tr><th>5</th><td>Thursday</td><td>20</td></tr>
              <tr class="dfs-sheet-target-row"><th>6</th><td><strong>Weekly Total</strong></td><td class="dfs-target-cell" id="dfsCellOut">?</td></tr>
            </tbody>
          </table></div>`
        : `<div class="dfs-table-scroll"><table class="dfs-sheet-grid">
            <thead><tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr></thead>
            <tbody>
              <tr><th>1</th><td><strong>Item</strong></td><td><strong>Unit (&pound;)</strong></td><td><strong>Qty</strong></td><td><strong>Cost</strong></td><td><strong>Status</strong></td></tr>
              <tr><th>2</th><td>Saline 500ml</td><td>&pound;4.50</td><td>12</td><td class="${activeIdx === 0 ? 'dfs-target-cell' : ''}" id="dfsCellD2">${activeIdx === 0 ? '?' : '£54.00'}</td><td class="${activeIdx === 2 ? 'dfs-target-cell' : ''}" id="dfsCellE2">${activeIdx === 2 ? '?' : 'Reorder'}</td></tr>
              <tr><th>3</th><td>Dressings</td><td>&pound;3.20</td><td>20</td><td>&pound;64.00</td><td>OK</td></tr>
              <tr><th>4</th><td>Gloves Box</td><td>&pound;5.00</td><td>4</td><td>&pound;20.00</td><td>Reorder</td></tr>
              <tr><th>5</th><td>Swabs Pack</td><td>&pound;2.50</td><td>8</td><td>&pound;20.00</td><td>Reorder</td></tr>
              <tr><th>6</th><td colspan="3"><strong>Mean Item Cost</strong></td><td class="${activeIdx === 1 ? 'dfs-target-cell' : ''}" id="dfsCellD6">${activeIdx === 1 ? '?' : '£39.50'}</td><td>&mdash;</td></tr>
            </tbody>
          </table></div>`;

      host.innerHTML = `
        ${tabsHtml}
        <p class="dfs-lab-prompt">${t.prompt}</p>
        <div class="dfs-fx-bar">
          <span class="dfs-fx-cellref">${esc(t.targetLabel)}</span>
          <span class="dfs-fx-badge">fx</span>
          <input type="text" class="dfs-fx-input" id="dfsFxInput" placeholder="Type formula starting with = ..." autocomplete="off" spellcheck="false">
        </div>
        ${gridHtml}
        <div class="dfs-lab-actions">
          <button type="button" class="dfs-lab-btn primary" id="dfsRunFormulaBtn"><i class="fa-solid fa-play"></i> Evaluate Formula</button>
          <button type="button" class="dfs-lab-btn" id="dfsHintFormulaBtn"><i class="fa-solid fa-lightbulb"></i> Show Formula Hint</button>
        </div>
        <div id="dfsLabOut"></div>
      `;

      host.querySelectorAll('.dfs-lab-tab').forEach(btn => {
        btn.addEventListener('click', () => {
          activeIdx = Number(btn.getAttribute('data-idx')) || 0;
          draw();
        });
      });

      const runBtn = host.querySelector('#dfsRunFormulaBtn');
      const hintBtn = host.querySelector('#dfsHintFormulaBtn');
      const input = host.querySelector('#dfsFxInput');
      const out = host.querySelector('#dfsLabOut');

      function evaluate() {
        const res = t.validate(input.value || '');
        const targetId = isE3 ? '#dfsCellOut' : (activeIdx === 0 ? '#dfsCellD2' : activeIdx === 1 ? '#dfsCellD6' : '#dfsCellE2');
        const cell = host.querySelector(targetId);
        if (cell) cell.textContent = res.val;
        out.innerHTML = feedbackHtml(res.ok, res.items);
      }

      runBtn.addEventListener('click', evaluate);
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          evaluate();
        }
      });
      hintBtn.addEventListener('click', () => {
        input.value = t.hint;
        input.focus();
      });
    }
    draw();
  }

  function renderSpreadsheetDesign(host) {
    const state = { bold: false, currency: false, wrap: false, sorted: false };
    const baseRows = [
      { name: 'Medical Syringes (Pack 100)', val: 45 },
      { name: 'Clinic Thermometer Digital', val: 18.5 },
      { name: 'First Aid Wall Cabinet Pro', val: 62.5 }
    ];

    function draw() {
      const rows = state.sorted ? [...baseRows].sort((a, b) => b.val - a.val) : baseRows;
      const fmtVal = (v) => state.currency ? '&pound;' + v.toFixed(2) : String(v);
      const wrapStyle = state.wrap ? 'white-space:normal;' : 'white-space:nowrap; max-width:115px; overflow:hidden; text-overflow:ellipsis;';
      const thStyle = state.bold ? 'font-weight:800; background:#0f172a; color:#ffffff;' : 'font-weight:400; background:#ffffff; color:#475569;';

      host.innerHTML = `
        <p class="dfs-lab-prompt">Toggle the spreadsheet formatting toolbar so this table meets Pearson Level 1 presentation standards: <strong>Bold &amp; shaded headers</strong>, <strong>Wrap Text</strong> on item names, <strong>Currency (£0.00)</strong> format, and sorted <strong>Highest to Lowest cost</strong>.</p>
        <div class="dfs-toolbar-sim">
          <button type="button" class="dfs-lab-btn ${state.bold ? 'active' : ''}" data-k="bold"><i class="fa-solid fa-bold"></i> Bold Headers</button>
          <button type="button" class="dfs-lab-btn ${state.wrap ? 'active' : ''}" data-k="wrap"><i class="fa-solid fa-text-width"></i> Wrap Text</button>
          <button type="button" class="dfs-lab-btn ${state.currency ? 'active' : ''}" data-k="currency"><i class="fa-solid fa-sterling-sign"></i> Currency (£0.00)</button>
          <button type="button" class="dfs-lab-btn ${state.sorted ? 'active' : ''}" data-k="sorted"><i class="fa-solid fa-arrow-down-9-1"></i> Sort Highest &rarr; Lowest</button>
        </div>
        <div class="dfs-table-scroll"><table class="dfs-sheet-grid">
          <thead><tr><th style="${thStyle}">Equipment Item Description</th><th style="${thStyle}">Unit Cost</th></tr></thead>
          <tbody>
            ${rows.map(r => `<tr><td style="${wrapStyle}">${esc(r.name)}</td><td>${fmtVal(r.val)}</td></tr>`).join('')}
          </tbody>
        </table></div>
        <div class="dfs-lab-actions">
          <button type="button" class="dfs-lab-btn primary" id="dfsCheckDesign"><i class="fa-solid fa-check-double"></i> Check Formatting Criteria</button>
        </div>
        <div id="dfsDesignOut"></div>
      `;

      host.querySelectorAll('.dfs-toolbar-sim button').forEach(b => {
        b.addEventListener('click', () => {
          const k = b.getAttribute('data-k');
          state[k] = !state[k];
          draw();
        });
      });

      host.querySelector('#dfsCheckDesign').addEventListener('click', () => {
        const items = [
          { ok: state.bold, msg: state.bold ? '<strong>[B1]</strong> Column headers clearly bolded with dark header contrast.' : 'Missing bold/shaded column header formatting.' },
          { ok: state.wrap, msg: state.wrap ? '<strong>[B1]</strong> Wrap Text enabled — no cropped label text (`...`).' : 'Long item text is cut off — enable <strong>Wrap Text</strong>.' },
          { ok: state.currency, msg: state.currency ? '<strong>[B1]</strong> Numeric money formatted to exact <code>£0.00</code> (2 d.p.).' : 'Numbers lack GBP <code>£</code> symbol and trailing 2 decimal places.' },
          { ok: state.sorted, msg: state.sorted ? '<strong>[M1]</strong> Rows sorted Z&rarr;A by highest unit price (£62.50 top).' : 'Rows are unsorted — sort Highest &rarr; Lowest cost.' }
        ];
        host.querySelector('#dfsDesignOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
      });
    }
    draw();
  }

  function renderSpreadsheetCharts(host) {
    host.innerHTML = `
      <p class="dfs-lab-prompt">Scenario: Present <strong>Quarterly Clinic Appointments</strong> (Q1: 120, Q2: 180, Q3: 150, Q4: 210) clearly. Pick the right chart type and add accurate title &amp; axis labels:</p>
      <div class="dfs-form-grid">
        <label><span>Chart Type</span>
          <select id="dfsChType">
            <option value="">-- Select Chart --</option>
            <option value="bar">Column / Bar Chart (Compare Categories)</option>
            <option value="pie">Pie Chart (Proportions adding to 100%)</option>
            <option value="line">Line Graph (Continuous Change Over Time)</option>
          </select>
        </label>
        <label><span>Chart Title</span><input type="text" id="dfsChTitle" placeholder="e.g. Quarterly Clinic Appointments 2026"></label>
        <label><span>Horizontal X-Axis Label</span><input type="text" id="dfsChX" placeholder="e.g. Quarter"></label>
        <label><span>Vertical Y-Axis Label</span><input type="text" id="dfsChY" placeholder="e.g. Number of Appointments"></label>
      </div>
      <div class="dfs-lab-actions">
        <button type="button" class="dfs-lab-btn primary" id="dfsChVerify"><i class="fa-solid fa-chart-column"></i> Check Chart Criteria</button>
      </div>
      <div id="dfsChOut"></div>
    `;
    host.querySelector('#dfsChVerify').addEventListener('click', () => {
      const ty = host.querySelector('#dfsChType').value;
      const ti = host.querySelector('#dfsChTitle').value.trim();
      const x = host.querySelector('#dfsChX').value.trim();
      const y = host.querySelector('#dfsChY').value.trim();
      const items = [
        { ok: ty === 'bar' || ty === 'line', msg: (ty === 'bar' || ty === 'line') ? '<strong>[B1]</strong> Appropriate chart type chosen for comparing quarterly totals.' : 'Select a Column/Bar Chart (or Line Graph for time trend), not a Pie Chart when comparing exact quarterly totals.' },
        { ok: ti.length >= 10 && !/^chart title$/i.test(ti), msg: (ti.length >= 10 && !/^chart title$/i.test(ti)) ? `<strong>[B1]</strong> Informative chart title added: "${esc(ti)}".` : 'Replace generic/empty title with a descriptive chart title.' },
        { ok: x.length >= 3 && y.length >= 3, msg: (x.length >= 3 && y.length >= 3) ? '<strong>[M1]</strong> Both X-axis and Y-axis carry clear units/labels.' : 'Examiners penalise missing X-axis or Y-axis labels.' }
      ];
      host.querySelector('#dfsChOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
    });
  }

  /* =========================================================================
     2. EMAIL, CALENDAR & CLOUD COLLABORATION VALIDATOR
     ========================================================================= */
  function renderEmailLab(host, preset) {
    if (preset === 'l1-calendar') {
      host.innerHTML = `
        <p class="dfs-lab-prompt">Scenario: Schedule a <strong>30-minute Online Health &amp; Safety Briefing</strong> tomorrow at <strong>10:00</strong> with colleague <code>taniya@clinic.org</code>, including a video link and a 15-minute reminder.</p>
        <div class="dfs-form-grid">
          <label><span>Event Title</span><input type="text" id="calTitle" placeholder="Health & Safety Briefing"></label>
          <label><span>Start &rarr; End Duration</span>
            <select id="calDur">
              <option value="30">10:00 &ndash; 10:30 (30 mins)</option>
              <option value="60">10:00 &ndash; 11:00 (60 mins)</option>
            </select>
          </label>
          <label><span>Invite Attendees</span><input type="text" id="calAtt" placeholder="taniya@clinic.org"></label>
          <label><span>Location / Link</span><input type="text" id="calLoc" placeholder="Teams / Online Video Link"></label>
          <label><span>Reminder</span>
            <select id="calRem">
              <option value="none">No Reminder</option>
              <option value="15">15 minutes before</option>
            </select>
          </label>
        </div>
        <div class="dfs-lab-actions">
          <button type="button" class="dfs-lab-btn primary" id="calVerify"><i class="fa-solid fa-calendar-check"></i> Validate Calendar Invite</button>
        </div>
        <div id="calOut"></div>
      `;
      host.querySelector('#calVerify').addEventListener('click', () => {
        const ti = host.querySelector('#calTitle').value.trim();
        const dur = host.querySelector('#calDur').value;
        const att = host.querySelector('#calAtt').value.trim();
        const loc = host.querySelector('#calLoc').value.trim();
        const rem = host.querySelector('#calRem').value;
        const items = [
          { ok: ti.length >= 5, msg: ti.length >= 5 ? 'Descriptive event title provided.' : 'Enter a clear meeting title.' },
          { ok: dur === '30', msg: dur === '30' ? 'End time matches the requested 30-minute slot.' : 'Brief requested 30 minutes (10:00 to 10:30).' },
          { ok: /@/.test(att) && !/\s/.test(att), msg: /@/.test(att) ? 'Attendee email formatted accurately.' : 'Include valid attendee email address.' },
          { ok: loc.length >= 4, msg: loc.length >= 4 ? 'Meeting link / location included.' : 'Add Teams / Zoom video meeting location.' },
          { ok: rem === '15', msg: rem === '15' ? '15-minute notification reminder enabled.' : 'Set the reminder to 15 minutes before.' }
        ];
        host.querySelector('#calOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
      });
      return;
    }

    if (preset === 'l1-collab') {
      host.innerHTML = `
        <p class="dfs-lab-prompt">Scenario: Share <code>Patient_Rota_Draft.docx</code> so your line manager can suggest edits <strong>using Comments only</strong> without overwriting your figures, expiring in <strong>7 days</strong>.</p>
        <div class="dfs-form-grid">
          <label><span>Access Scope</span>
            <select id="colScope"><option value="anyone">Anyone with link (Public)</option><option value="specific">Specific People (sarah@clinic.org)</option></select>
          </label>
          <label><span>Permission Level</span>
            <select id="colPerm"><option value="view">Can View (No comment/edit)</option><option value="comment">Can Comment (Review only)</option><option value="edit">Can Edit (Full modify)</option></select>
          </label>
          <label><span>Link Expiry</span>
            <select id="colExp"><option value="never">Never expires</option><option value="7">Expires in 7 days</option></select>
          </label>
        </div>
        <div class="dfs-lab-actions"><button type="button" class="dfs-lab-btn primary" id="colBtn"><i class="fa-solid fa-share-nodes"></i> Check Cloud Sharing Settings</button></div>
        <div id="colOut"></div>
      `;
      host.querySelector('#colBtn').addEventListener('click', () => {
        const sc = host.querySelector('#colScope').value;
        const pe = host.querySelector('#colPerm').value;
        const ex = host.querySelector('#colExp').value;
        const items = [
          { ok: sc === 'specific', msg: sc === 'specific' ? '<strong>[B1]</strong> Restricted to named internal recipient (least privilege).' : 'Avoid public "Anyone with link" for internal draft files.' },
          { ok: pe === 'comment', msg: pe === 'comment' ? '<strong>[M1]</strong> "Can Comment" protects source figures from accidental edits.' : 'Use "Can Comment" rather than full "Can Edit" or "View only".' },
          { ok: ex === '7', msg: ex === '7' ? '<strong>[B1]</strong> Time-limited 7-day link reduces stale exposure.' : 'Set a 7-day expiry on shared draft links.' }
        ];
        host.querySelector('#colOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
      });
      return;
    }

    const isBcc = (preset === 'l1-etiquette');
    const isAttach = (preset === 'e3-attach');
    const isMsg = (preset === 'e3-messaging');
    const promptTxt = isBcc
      ? 'Scenario (UK GDPR BCC Test): Send the monthly bulletin to <strong>20 external community clients</strong> without revealing their email addresses to each other.'
      : (isAttach
        ? 'Scenario: Compose a polite email to <code>tutor@clinic.org</code> with a clear subject and attach the required file <code>Budget_2026.pdf</code>.'
        : (isMsg
          ? 'Scenario: Reply politely to a colleague on workplace chat/email confirming attendance, with zero ALL-CAPS shouting and clear greeting/sign-off.'
          : 'Scenario: Your manager asked only you if you can cover Saturday shift. Pick the right reply mode, recipient, subject, greeting, message, and sign-off.'));

    host.innerHTML = `
      <p class="dfs-lab-prompt">${promptTxt}</p>
      <div class="dfs-form-grid">
        <label><span>Action Mode</span>
          <select id="emMode">
            <option value="new">New Email</option>
            <option value="reply">Reply (Sender Only)</option>
            <option value="replyall">Reply All (Whole Thread)</option>
            <option value="forward">Forward (New Person)</option>
          </select>
        </label>
        <label><span>To:</span><input type="text" id="emTo" placeholder="${isBcc ? 'undisclosed-recipients / info@clinic.org' : 'sarah.manager@clinic.org'}"></label>
        <label><span>CC:</span><input type="text" id="emCc" placeholder="Optional colleague copy"></label>
        <label><span>BCC: (Hidden recipients)</span><input type="text" id="emBcc" placeholder="${isBcc ? '20-external-clients@list.org' : 'Hidden external list'}"></label>
        <label class="dfs-span-2"><span>Subject Line:</span><input type="text" id="emSub" placeholder="Enter concise descriptive subject..."></label>
        <label class="dfs-span-2"><span>Message Body:</span><textarea id="emBody" rows="3" placeholder="Good morning Sarah,\n...\nKind regards,\nJordan"></textarea></label>
      </div>
      ${isAttach ? `<label class="dfs-check-line"><input type="checkbox" id="emAttChk"> <span>Attach <code>Budget_2026.pdf</code> (840 KB)</span></label>` : ''}
      <div class="dfs-lab-actions">
        <button type="button" class="dfs-lab-btn primary" id="emVerify"><i class="fa-solid fa-paper-plane"></i> Check Exam Email Criteria</button>
      </div>
      <div id="emOut"></div>
    `;

    host.querySelector('#emVerify').addEventListener('click', () => {
      const mode = host.querySelector('#emMode').value;
      const to = host.querySelector('#emTo').value.trim();
      const cc = host.querySelector('#emCc').value.trim();
      const bcc = host.querySelector('#emBcc').value.trim();
      const sub = host.querySelector('#emSub').value.trim();
      const body = host.querySelector('#emBody').value.trim();
      const att = host.querySelector('#emAttChk') ? host.querySelector('#emAttChk').checked : true;

      const hasEmail = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+/.test(v);
      const hasGreet = /^(dear|hi|hello|good morning|good afternoon)/i.test(body);
      const hasSignOff = /(kind regards|best regards|yours sincerely|many thanks|thank you)/i.test(body);
      const allCaps = body.length > 10 && body === body.toUpperCase() && /[A-Z]/.test(body);

      const items = [];
      if (isBcc) {
        const bccOk = bcc.length > 0 && hasEmail(bcc) && !/external|client/i.test(cc);
        items.push({ ok: bccOk, msg: bccOk ? '<strong>[B1 GDPR]</strong> External client emails placed safely in <strong>BCC</strong>.' : '<strong>GDPR Trap!</strong> Never put external client lists in To/CC — place bulk external addresses in <strong>BCC</strong>.' });
      } else {
        if (!isAttach && !isMsg) {
          items.push({ ok: mode === 'reply', msg: mode === 'reply' ? '<strong>[B1]</strong> Correctly chose <strong>Reply</strong> to answer sender only (not Reply All).' : 'Only your manager asked — select <strong>Reply</strong> instead of spamming the entire thread.' });
        }
        items.push({ ok: hasEmail(to), msg: hasEmail(to) ? 'Valid email recipient format (<code>@</code>, no spaces).' : 'Enter a valid recipient email address (e.g. <code>name@clinic.org</code>).' });
      }
      if (isAttach) {
        items.push({ ok: att, msg: att ? '<strong>[M1]</strong> Required attachment <code>Budget_2026.pdf</code> attached cleanly.' : 'You forgot to tick/attach <code>Budget_2026.pdf</code>!' });
      }
      items.push({ ok: sub.length >= 4 && !allCaps, msg: (sub.length >= 4 && !allCaps) ? '<strong>[B1]</strong> Clear, non-empty subject line.' : 'Add a descriptive subject line (and avoid ALL CAPS).' });
      items.push({ ok: hasGreet && hasSignOff && !allCaps, msg: (hasGreet && hasSignOff && !allCaps) ? '<strong>[B1]</strong> Polite greeting, clear message, and professional sign-off.' : 'Include a greeting ("Dear..."), message, sign-off ("Kind regards..."), and avoid ALL CAPS.' });

      host.querySelector('#emOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
    });
  }

  /* =========================================================================
     3. FOLDER TREE, ZIP EXTRACTION & DOCUMENT PREFLIGHT WORKBENCH
     ========================================================================= */
  function renderFolderZipLab(host, preset) {
    const filePresets = new Set(['e3-files', 'e3-search', 'l1-hierarchy', 'l1-zip', 'l1-backup']);
    if (!filePresets.has(preset)) {
      return renderDocPreflightLab(host, preset);
    }

    if (preset === 'l1-zip') {
      let extracted = false;
      function drawZip() {
        host.innerHTML = `
          <p class="dfs-lab-prompt">Onscreen Exam Task: You downloaded <code>Assessment_Data.zip</code>. Open and edit <code>Clinic_Budget.xlsx</code> <strong>without</strong> risking lost changes inside a compressed archive.</p>
          <div class="dfs-explorer-sim">
            <div class="dfs-exp-row"><span><i class="fa-solid fa-file-zipper" style="color:#d97706;"></i> Assessment_Data.zip (${extracted ? 'Extracted to Working Folder' : 'Compressed Archive — Read-Only Preview'})</span></div>
            <div class="dfs-exp-actions">
              <button type="button" class="dfs-lab-btn" id="zipExtractBtn"><i class="fa-solid fa-folder-open"></i> 1. Click "Extract All..."</button>
              <button type="button" class="dfs-lab-btn primary" id="zipEditBtn"><i class="fa-solid fa-file-excel"></i> 2. Open Clinic_Budget.xlsx to Edit</button>
            </div>
          </div>
          <div id="zipOut"></div>
        `;
        host.querySelector('#zipExtractBtn').addEventListener('click', () => {
          extracted = true;
          drawZip();
          host.querySelector('#zipOut').innerHTML = feedbackHtml(true, [{ ok: true, msg: 'Archive extracted cleanly into an unzipped folder! Now click Step 2 to edit safely.' }]);
        });
        host.querySelector('#zipEditBtn').addEventListener('click', () => {
          const items = extracted
            ? [{ ok: true, msg: '<strong>[B1][M1]</strong> Opened from extracted working folder — all edits and formulas save properly!' }]
            : [{ ok: false, msg: '<strong>Common Exam Mistake!</strong> Opening files inside an unextracted <code>.zip</code> opens a temporary read-only copy. Click <strong>Extract All...</strong> first!' }];
          host.querySelector('#zipOut').innerHTML = feedbackHtml(extracted, items);
        });
      }
      drawZip();
      return;
    }

    host.innerHTML = `
      <p class="dfs-lab-prompt">File Naming &amp; Folder Inspector: Choose a sensible destination subfolder and type an exam-ready filename (avoiding illegal OS characters <code>\\ / : * ? " &lt; &gt; |</code> and vague names like <code>doc1</code>).</p>
      <div class="dfs-form-grid">
        <label><span>Save Location (Folder Hierarchy)</span>
          <select id="fldDir">
            <option value="downloads">C:\\Users\\Student\\Downloads\\</option>
            <option value="desktop">C:\\Users\\Student\\Desktop\\ (Unsorted)</option>
            <option value="project">OneDrive &gt; Functional Skills &gt; Clinic Budgets\\</option>
          </select>
        </label>
        <label><span>Filename (without extension)</span><input type="text" id="fldName" placeholder="e.g. Clinic_Quarterly_Report_2026"></label>
      </div>
      <div class="dfs-lab-actions">
        <button type="button" class="dfs-lab-btn primary" id="fldVerify"><i class="fa-solid fa-folder-tree"></i> Validate File Organisation</button>
      </div>
      <div id="fldOut"></div>
    `;
    host.querySelector('#fldVerify').addEventListener('click', () => {
      const dir = host.querySelector('#fldDir').value;
      const name = host.querySelector('#fldName').value.trim();
      const illegal = /[\\/:*?"<>|]/.test(name);
      const vague = /^(doc1|file|new|test|untitled|document)$/i.test(name);
      const items = [
        { ok: dir === 'project', msg: dir === 'project' ? '<strong>[B1]</strong> Stored inside logical topic subfolder (synced cloud + structured).' : 'Avoid dumping finished work on Desktop/Downloads — file cleanly inside its structured folder.' },
        { ok: !illegal && name.length >= 6 && !vague, msg: (!illegal && name.length >= 6 && !vague) ? `<strong>[B1][M1]</strong> Valid descriptive filename <code>${esc(name)}</code> with zero forbidden symbols.` : 'Use a descriptive 6+ char name without vague labels or forbidden symbols (<code>\\ / : * ? " &lt; &gt; |</code>).' }
      ];
      host.querySelector('#fldOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
    });
  }

  function renderDocPreflightLab(host, preset) {
    const isPdf = (preset === 'l1-pdf-export' || preset === 'l1-portal');
    const isSlides = (preset === 'l1-slides');
    const targetFmt = isPdf ? 'pdf' : (isSlides ? 'pptx' : 'docx');
    const promptTxt = isPdf
      ? 'Pre-Flight Check: Configure this finished customer leaflet for a read-only web portal (must preserve fonts/layout across devices & stay under 5 MB).'
      : (isSlides
        ? 'Pre-Flight Check: Prepare a 4-slide workplace presentation meeting contrast, bullet-point brevity, and layout criteria.'
        : 'Pre-Flight Check: Prepare a workplace notice/report with clear heading hierarchy, UK spelling check, proportional images, and right export format.');

    host.innerHTML = `
      <p class="dfs-lab-prompt">${promptTxt}</p>
      <div class="dfs-form-grid">
        <label><span>Export File Format</span>
          <select id="docFmt">
            <option value="docx">Word Document (.docx)</option>
            <option value="pdf">PDF Read-Only (.pdf)</option>
            <option value="pptx">Presentation (.pptx)</option>
            <option value="txt">Plain Text (.txt &mdash; strips styles)</option>
          </select>
        </label>
        <label><span>Image &amp; Proofreading</span>
          <select id="docProof">
            <option value="none">Unchecked + stretched corner drag</option>
            <option value="clean">UK Spellcheck + aspect-ratio lock + alt text</option>
          </select>
        </label>
      </div>
      <div class="dfs-lab-actions">
        <button type="button" class="dfs-lab-btn primary" id="docVerify"><i class="fa-solid fa-wand-magic-sparkles"></i> Run Document Pre-Flight</button>
      </div>
      <div id="docOut"></div>
    `;
    host.querySelector('#docVerify').addEventListener('click', () => {
      const fmt = host.querySelector('#docFmt').value;
      const prf = host.querySelector('#docProof').value;
      const items = [
        { ok: fmt === targetFmt || (!isPdf && !isSlides && (fmt === 'docx' || fmt === 'pdf')), msg: (fmt !== 'txt') ? `<strong>[B1]</strong> Format <code>.${esc(fmt)}</code> preserves formatting & hierarchy.` : 'Plain <code>.txt</code> destroys headings, bold, tables, and images!' },
        { ok: prf === 'clean', msg: prf === 'clean' ? '<strong>[M1]</strong> Aspect ratio locked (corner handles only), UK spelling verified, accessibility alt text included.' : 'Always proofread in UK English and resize images using corner handles only so proportions never distort.' }
      ];
      if (isPdf) items[0] = { ok: fmt === 'pdf', msg: fmt === 'pdf' ? '<strong>[B1]</strong> Exporting to <code>.pdf</code> locks layout cleanly for web/portal upload.' : 'Portal briefs requesting non-editable universal layout require exporting to <strong>.pdf</strong>.' };
      host.querySelector('#docOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
    });
  }

  /* =========================================================================
     4. CYBERSECURITY, PHISHING & IT SCENARIO INSPECTOR
     ========================================================================= */
  function renderSecurityLab(host, preset) {
    if (preset === 'l1-phishing' || preset === 'e3-passwords') {
      const flags = new Set();
      host.innerHTML = `
        <p class="dfs-lab-prompt">Click all <strong>4 suspicious phishing red flags</strong> inside this fake urgent message, then test a strong NCSC passphrase below:</p>
        <div class="dfs-phish-card">
          <div><strong>From:</strong> <button type="button" class="dfs-phish-clue" data-id="sender">security-alerts@paypa1-verify-uk.com</button></div>
          <div><strong>Greeting:</strong> <button type="button" class="dfs-phish-clue" data-id="greet">Dear Valued Customer,</button></div>
          <div><strong>Message:</strong> <button type="button" class="dfs-phish-clue" data-id="urgent">URGENT: Your account will be permanently SUSPENDED in 2 hours unless verified!</button></div>
          <div><strong>Link:</strong> <button type="button" class="dfs-phish-clue" data-id="link">http://198.51.100.4/login-update.exe</button></div>
        </div>
        <div class="dfs-form-grid" style="margin-top:14px;">
          <label class="dfs-span-2"><span>Test Password Strength (NCSC 3-Random-Words Rule &ge; 12 chars)</span><input type="text" id="secPwInput" placeholder="e.g. Purple!Train73RiverMeadow"></label>
        </div>
        <div class="dfs-lab-actions"><button type="button" class="dfs-lab-btn primary" id="secCheckBtn"><i class="fa-solid fa-shield-halved"></i> Check Security Audit</button></div>
        <div id="secOut"></div>
      `;
      host.querySelectorAll('.dfs-phish-clue').forEach(btn => {
        btn.addEventListener('click', () => {
          const id = btn.getAttribute('data-id');
          btn.classList.toggle('flagged');
          if (flags.has(id)) flags.delete(id); else flags.add(id);
        });
      });
      host.querySelector('#secCheckBtn').addEventListener('click', () => {
        const pw = host.querySelector('#secPwInput').value;
        const pwStrong = pw.length >= 12 && /[a-z]/.test(pw) && /[A-Z]/.test(pw) && /[0-9]/.test(pw) && !/password|1234|qwerty/i.test(pw);
        const items = [
          { ok: flags.size === 4, msg: `Clicked <strong>${flags.size}/4</strong> phishing indicators (lookalike <code>paypa1</code> domain, generic greeting, 2-hour panic threat, unencrypted <code>http://...exe</code> URL).` },
          { ok: pwStrong, msg: pwStrong ? `<strong>[B1]</strong> Strong passphrase (${pw.length} chars, mixed case + digits).` : 'Enter a test password with 12+ characters mixing uppercase, lowercase, and numbers (no "password123").' }
        ];
        host.querySelector('#secOut').innerHTML = feedbackHtml(items.every(i => i.ok), items);
      });
      return;
    }

    const scenarios = {
      'e3-hardware': {
        q: 'You connect a barcode scanner, monitor, and install a spreadsheet app on Windows 11. Which classification is 100% accurate?',
        opts: [
          { t: 'Barcode scanner = Input Hardware; Monitor = Output Hardware; Windows 11 = Operating System; Spreadsheet = Application Software', ok: true },
          { t: 'Spreadsheet = Output Hardware; Windows 11 = Application Software; Monitor = Storage Drive', ok: false },
          { t: 'Barcode scanner = System Software; Windows 11 = Input Hardware', ok: false }
        ]
      },
      'e3-controls': {
        q: 'You are stepping away from a reception computer displaying client names for a 10-minute tea break. What is the safest session control?',
        opts: [
          { t: 'Press Windows + L (or Start > Lock) so your password/PIN hides the screen while keeping your apps open', ok: true },
          { t: 'Switch off the monitor screen power button only while leaving Windows unlocked', ok: false },
          { t: 'Force hold the PC tower power button for 5 seconds without saving', ok: false }
        ]
      },
      'e3-wifi': {
        q: 'You are sitting in a train station café with free unencrypted public Wi-Fi (Cafe_Free_WiFi). What is the safest way to check your private bank app?',
        opts: [
          { t: 'Connect directly without password because the café sign listed it', ok: false },
          { t: 'Switch off Wi-Fi and use your own encrypted 4G/5G mobile data (or trusted VPN)', ok: true },
          { t: 'Turn Bluetooth discovery to Everyone so banking runs faster', ok: false }
        ]
      },
      'e3-accessibility': {
        q: 'A colleague with mild visual impairment finds menu buttons tiny across all Windows apps, while another has glare sensitivity. Which OS adjustments help cleanly?',
        opts: [
          { t: 'Increase Display Scale (e.g. 125%–150%) / Magnifier + enable Night Light / soft tint & High Contrast cleanly', ok: true },
          { t: 'Turn on Mono Audio and mute the speaker volume', ok: false },
          { t: 'Lower monitor brightness to 0% black so text cannot glare', ok: false }
        ]
      },
      'e3-forms': {
        q: 'When filling out a council portal form, a field marked with a red asterisk (*) turns red after you paste your email with an extra space at the end. What should you check?',
        opts: [
          { t: 'Fill every mandatory (*) field cleanly, remove trailing spaces after the email/postcode, and untick optional 3rd-party marketing', ok: true },
          { t: 'Click Submit five times quickly to force the red asterisk box through', ok: false },
          { t: 'Tick "Share my details with external advertisers" just to clear validation', ok: false }
        ]
      },
      'e3-shopping': {
        q: 'Before entering debit card details on a booking site, which combination confirms the safest checkout practice?',
        opts: [
          { t: 'Verify https:// + padlock + genuine official domain, check delivery fees/final total in basket, and never save cards on public PCs', ok: true },
          { t: 'Save your debit card inside the shared library browser and click Pay immediately on http://', ok: false },
          { t: 'Send cash by direct personal bank transfer to avoid official checkout fees', ok: false }
        ]
      },
      'e3-wellbeing': {
        q: 'An administrator gets daily neck pain from a low laptop facing a bright window behind her back. What improves ergonomics & eye comfort straight away?',
        opts: [
          { t: 'Turn desk perpendicular (90 deg) to window to stop screen glare, raise top of screen to eye level with external keyboard, and apply 20-20-20 breaks', ok: true },
          { t: 'Keep laptop flat on lap for 5 continuous hours and stare closer to fight glare', ok: false },
          { t: 'Tilt wrists sharply upward at 45 degrees while placing monitor directly in front of bright sun', ok: false }
        ]
      },
      'l1-eval': {
        q: 'Which two checks provide the strongest proof that an online employment-law article is reliable and up to date?',
        opts: [
          { t: 'Check authoritative official domain (.gov.uk / ACAS), author credentials, and recent publication/update date vs a second source', ok: true },
          { t: 'Trust it immediately because it sits in the top Sponsored "Ad" search position with 5-star onsite testimonials', ok: false },
          { t: 'Verify only that the page contains colourful graphics and a padlock icon', ok: false }
        ]
      },
      'l1-mfa': {
        q: 'Which Multi-Factor Authentication setup combines Knowledge (Something you know) + Possession (Something you have) most securely against SIM-swap attacks?',
        opts: [
          { t: 'Password + 6-digit code from an Authenticator App (or hardware security key)', ok: true },
          { t: 'Typing your password twice in a row on the same browser tab', ok: false },
          { t: 'Using your date of birth as a security PIN', ok: false }
        ]
      },
      'l1-malware': {
        q: 'A colleague sees a warning claiming files are locked/encrypted and demanding £500 Bitcoin. What should happen in the VERY FIRST 30 seconds?',
        opts: [
          { t: 'Disconnect Wi-Fi / unplug network cable immediately to stop spread across shared drives, alert IT Security, and never pay the ransom', ok: true },
          { t: 'Plug in your main office backup USB hard drive right away to test copying files', ok: false },
          { t: 'Pay the cryptocurrency wallet address calmly to get the files back', ok: false }
        ]
      },
      'l1-gdpr': {
        q: 'Under UK GDPR Article 5, which action breaches Lawful Data Minimisation & Security?',
        opts: [
          { t: 'Leaving unencrypted client spreadsheets on a shared family tablet or sending external contacts in To/CC', ok: true },
          { t: 'Collecting only the minimum fields needed and encrypting the spreadsheet with a strong password', ok: false },
          { t: 'Deleting temporary assessment copies once retention ends', ok: false }
        ]
      },
      'l1-copyright': {
        q: 'You need an image for an assessed brochure without infringing UK copyright law. Which source should you choose?',
        opts: [
          { t: 'A Creative Commons CC0 / royalty-free image (with attribution where CC-BY requires it)', ok: true },
          { t: 'Cropping out a stock photography watermark in Paint', ok: false },
          { t: 'Any photo found on Google Images because it appeared in search results', ok: false }
        ]
      },
      'l1-troubleshoot': {
        q: 'Your monitor says "No Signal" when the clinic PC tower turns on. What is the logical first-line troubleshooting step?',
        opts: [
          { t: 'Check monitor power LED and firmly re-seat the HDMI/DisplayPort cable at both ends before escalating', ok: true },
          { t: 'Immediately wipe the hard drive and reinstall Windows', ok: false },
          { t: 'Unplug the office router across the corridor', ok: false }
        ]
      }
    };

    const sc = scenarios[preset] || {
      q: 'In an official Digital Functional Skills assessment or workplace task, which practice meets Ofqual safety, accuracy & accessibility standards?',
      opts: [
        { t: 'Verify HTTPS/padlock + trusted source, follow accessibility & ergonomic guidance, and protect personal data', ok: true },
        { t: 'Ignore browser security warnings, skip form validation, and disable automatic OS security updates', ok: false },
        { t: 'Reuse one 6-character password across work email, shopping, and cloud storage', ok: false }
      ]
    };

    let selected = -1;
    host.innerHTML = `
      <p class="dfs-lab-prompt"><strong>Decision Simulator:</strong> ${esc(sc.q)}</p>
      <div class="dfs-drill-options">
        ${sc.opts.map((o, i) => `<button type="button" class="dfs-drill-opt-btn dfs-sec-opt" data-idx="${i}"><span>${esc(o.t)}</span><i class="fa-solid fa-circle-question" style="opacity:0.45;"></i></button>`).join('')}
      </div>
      <div id="secScenOut" style="margin-top:12px;"></div>
    `;
    host.querySelectorAll('.dfs-sec-opt').forEach(btn => {
      btn.addEventListener('click', () => {
        selected = Number(btn.getAttribute('data-idx'));
        const chosen = sc.opts[selected];
        host.querySelectorAll('.dfs-sec-opt').forEach((b, idx) => {
          b.classList.remove('correct', 'incorrect');
          if (sc.opts[idx].ok) b.classList.add('correct');
          else if (idx === selected) b.classList.add('incorrect');
        });
        host.querySelector('#secScenOut').innerHTML = feedbackHtml(chosen.ok, [
          {
            ok: chosen.ok,
            msg: chosen.ok
              ? '<strong>[B1][M1]</strong> Spot on! This decision satisfies Pearson Edexcel / Open Awards DFSQ marking criteria.'
              : 'Look carefully at the highlighted green option — security, data protection, and systematic checks earn full marks.'
          }
        ]);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.dfs-interactive-lab[data-widget]').forEach(function (host) {
      const widget = host.getAttribute('data-widget') || '';
      const preset = host.getAttribute('data-preset') || '';
      if (widget === 'spreadsheet-formula') renderSpreadsheet(host, preset);
      else if (widget === 'email-validator') renderEmailLab(host, preset);
      else if (widget === 'folder-zip') renderFolderZipLab(host, preset);
      else renderSecurityLab(host, preset);
    });
  });
})();
