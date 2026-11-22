/**
 * Master Functional Skills (MFS) — Digital Skills Basics & Essential Apps Interactive Labs
 * Auto-mounts onto [data-basics-lab="..."] elements across b01-b10 units.
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

  function pill(ok, msg) {
    const bg = ok ? '#ecfdf5' : '#fef2f2';
    const bd = ok ? '#10b981' : '#ef4444';
    const col = ok ? '#065f46' : '#991b1b';
    const ic = ok ? 'fa-circle-check' : 'fa-triangle-exclamation';
    return `<div style="margin-top:12px; padding:12px 14px; border-radius:10px; background:${bg}; border:1px solid ${bd}; color:${col}; font-weight:600; font-size:0.95rem; display:flex; align-items:flex-start; gap:10px;"><i class="fa-solid ${ic}" style="margin-top:3px;"></i><span>${msg}</span></div>`;
  }

  /* 1. b01: Mouse Click & UK Keyboard Check */
  function mountMouseKeyboard(host) {
    let clicks = { single: false, dbl: false, right: false };
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-computer-mouse"></i> Try Real Mouse Actions &amp; UK Keyboard Rules</div>
        <p class="dfs-lab-sub">Test all three mouse buttons on the blue tiles below, then test the common UK key trap.</p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(170px,1fr)); gap:12px; margin-bottom:14px;">
          <button type="button" class="b-btn b-single" style="padding:16px 12px; border-radius:12px; border:2px solid #0284c7; background:#f0f9ff; color:#0c4a6e; font-weight:700; cursor:pointer;">1. Single Left-Click Me</button>
          <button type="button" class="b-btn b-dbl" style="padding:16px 12px; border-radius:12px; border:2px solid #059669; background:#ecfdf5; color:#064e3b; font-weight:700; cursor:pointer;">2. Double-Click Me Fast</button>
          <button type="button" class="b-btn b-right" style="padding:16px 12px; border-radius:12px; border:2px solid #d97706; background:#fffbeb; color:#78350f; font-weight:700; cursor:pointer;">3. Right-Click Me</button>
        </div>
        <div class="b-mouse-fb"></div>
        <hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">
        <div style="font-weight:700; color:#0f172a; margin-bottom:8px;">Quick Keyboard Check: On a UK keyboard, which keys type the <code>@</code> symbol for an email address?</div>
        <div style="display:flex; flex-wrap:wrap; gap:10px;">
          <button type="button" class="b-k" data-ok="0" style="padding:10px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer; font-weight:600;">Shift + 2</button>
          <button type="button" class="b-k" data-ok="1" style="padding:10px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer; font-weight:600;">Shift + ' (apostrophe key near Enter)</button>
          <button type="button" class="b-k" data-ok="0" style="padding:10px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer; font-weight:600;">Caps Lock + A</button>
        </div>
        <div class="b-key-fb"></div>
      </div>`;
    const mfb = host.querySelector('.b-mouse-fb');
    function updateMouse(txt) {
      const doneCount = [clicks.single, clicks.dbl, clicks.right].filter(Boolean).length;
      mfb.innerHTML = pill(doneCount === 3, `${txt} — Progress: ${doneCount} of 3 mouse actions tested.`);
    }
    host.querySelector('.b-single').addEventListener('click', () => {
      clicks.single = true;
      host.querySelector('.b-single').style.background = '#bbf7d0';
      updateMouse('Single Left-Click detected (selects buttons/links)');
    });
    host.querySelector('.b-dbl').addEventListener('dblclick', () => {
      clicks.dbl = true;
      host.querySelector('.b-dbl').style.background = '#bbf7d0';
      updateMouse('Double Left-Click detected (opens folders/files)');
    });
    host.querySelector('.b-right').addEventListener('contextmenu', (e) => {
      e.preventDefault();
      clicks.right = true;
      host.querySelector('.b-right').style.background = '#fde68a';
      updateMouse('Right-Click menu trigger detected (Rename / New Folder)');
    });
    const kfb = host.querySelector('.b-key-fb');
    host.querySelectorAll('.b-k').forEach(btn => {
      btn.addEventListener('click', () => {
        const ok = btn.getAttribute('data-ok') === '1';
        kfb.innerHTML = pill(ok, ok
          ? "Spot on! On UK keyboards, <strong>Shift + '</strong> types <code>@</code> (whereas Shift + 2 types speech marks <code>\"</code>)."
          : "Not quite — Shift + 2 gives <code>@</code> on US keyboards, but on a <strong>UK keyboard</strong> hold <strong>Shift + '</strong> near Enter.");
      });
    });
  }

  /* 2. b02: Forgotten Password & Passphrase Tester */
  function mountForgotPassword(host) {
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-key"></i> Interactive Forgotten Password Reset &amp; Passphrase Lab</div>
        <p class="dfs-lab-sub">Part A: Walk through choosing a safe new password, then Part B: pick the genuine reset message.</p>
        <label for="mfsPwTest" style="display:block; font-weight:700; color:#0f172a; margin-bottom:6px;">Type a sample passphrase to test strength (try 3 random words + a number, e.g. <code>RedMugRiver29!</code>):</label>
        <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center;">
          <input id="mfsPwTest" type="password" placeholder="Type a practice passphrase..." style="flex:1 1 240px; min-height:46px; padding:10px 14px; border:2px solid #cbd5e1; border-radius:10px; font-size:16px; box-sizing:border-box;">
          <button type="button" class="b-eye" style="padding:10px 14px; border-radius:10px; border:1px solid #94a3b8; background:#f8fafc; font-weight:700; cursor:pointer;"><i class="fa-regular fa-eye"></i> Show / Hide</button>
        </div>
        <div class="b-pw-fb" style="margin-top:8px;"></div>
        <hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">
        <div style="font-weight:700; color:#0f172a; margin-bottom:8px;">Reset Safety Scenario: You locked yourself out after 2 failed tries. What is the BEST next step?</div>
        <div style="display:flex; flex-direction:column; gap:8px;">
          <button type="button" class="b-rst" data-ok="0" style="text-align:left; padding:11px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">A. Keep guessing 10 more times quickly until the account locks.</button>
          <button type="button" class="b-rst" data-ok="1" style="text-align:left; padding:11px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">B. Check Caps Lock, click the eye icon, and if still stuck click <strong>Forgotten password?</strong> on the real login screen.</button>
          <button type="button" class="b-rst" data-ok="0" style="text-align:left; padding:11px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">C. Click an unsolicited text link saying "Update banking PIN now or close in 2 hours".</button>
        </div>
        <div class="b-rst-fb"></div>
      </div>`;
    const inp = host.querySelector('#mfsPwTest');
    const pwFb = host.querySelector('.b-pw-fb');
    host.querySelector('.b-eye').addEventListener('click', () => {
      inp.type = inp.type === 'password' ? 'text' : 'password';
    });
    inp.addEventListener('input', () => {
      const v = inp.value;
      if (!v) { pwFb.innerHTML = ''; return; }
      const longEnough = v.length >= 12;
      const hasNum = /[0-9]/.test(v);
      const hasMix = /[A-Z]/.test(v) && /[a-z]/.test(v);
      const common = /password|123456|qwerty|admin/i.test(v);
      const ok = longEnough && hasNum && hasMix && !common;
      const tips = [];
      if (common) tips.push('Avoid obvious words like password or 123456.');
      if (!longEnough) tips.push(`Make it at least 12 characters (currently ${v.length}).`);
      if (!hasMix) tips.push('Mix uppercase + lowercase letters.');
      if (!hasNum) tips.push('Add at least one number.');
      pwFb.innerHTML = pill(ok, ok
        ? 'Strong memorable passphrase! Long (12+ chars), mixed case, with a number.'
        : tips.join(' '));
    });
    const rfb = host.querySelector('.b-rst-fb');
    host.querySelectorAll('.b-rst').forEach(btn => {
      btn.addEventListener('click', () => {
        const ok = btn.getAttribute('data-ok') === '1';
        rfb.innerHTML = pill(ok, ok
          ? 'Correct! Check Caps Lock/Eye Icon first, then use the official <strong>Forgotten password?</strong> link on the website.'
          : 'Careful — guessing repeatedly locks accounts out, and unsolicited urgent links are common phishing scams.');
      });
    });
  }

  /* 3. b03: Windows Desktop & Everyday Programmes Matcher */
  function mountWindowsApps(host) {
    const qs = [
      { q: 'Which top-right button hides your window down onto the Taskbar WITHOUT closing it?', opts: ['Close (X)', 'Minimise (_)', 'Delete'], ans: 1, why: 'Minimise (_) keeps your app open on the Taskbar so you never lose unsaved work.' },
      { q: 'Which free Windows/Linux programme helps you find saved files and create folders?', opts: ['File Explorer / File Manager', 'Calculator', 'PowerPoint'], ans: 0, why: 'File Explorer (Windows yellow folder icon) manages folders, Documents, Downloads, and files.' },
      { q: 'If you want a free app on your home PC to practise Word documents or Excel sheets without paying Microsoft 365:', opts: ['Notepad only', 'LibreOffice Writer & Calc', 'Paint'], ans: 1, why: 'LibreOffice Writer matches Microsoft Word, Calc matches Excel, and Impress matches PowerPoint.' }
    ];
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-brands fa-windows"></i> Windows Desktop &amp; Basic Programmes Checker</div>
        ${qs.map((item, i) => `
          <div style="margin-bottom:14px; padding:12px; border:1px solid #e2e8f0; border-radius:10px; background:#fff;">
            <div style="font-weight:700; margin-bottom:8px;">${i + 1}. ${item.q}</div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
              ${item.opts.map((o, oi) => `<button type="button" class="b-wa" data-q="${i}" data-o="${oi}" style="padding:8px 12px; border-radius:8px; border:1px solid #cbd5e1; background:#f8fafc; cursor:pointer; font-weight:600;">${o}</button>`).join('')}
            </div>
            <div class="b-wa-fb-${i}"></div>
          </div>`).join('')}
      </div>`;
    host.querySelectorAll('.b-wa').forEach(btn => {
      btn.addEventListener('click', () => {
        const qi = Number(btn.getAttribute('data-q'));
        const oi = Number(btn.getAttribute('data-o'));
        const item = qs[qi];
        const ok = oi === item.ans;
        host.querySelector(`.b-wa-fb-${qi}`).innerHTML = pill(ok, ok ? `Correct! ${item.why}` : `Try again — check which tool matches the task. (${item.why})`);
      });
    });
  }

  /* 4. b04: Folders, File Names & Recovery Lab */
  function mountFilesFolders(host) {
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-folder-open"></i> File Search, Tidy Folders &amp; Filename Lab</div>
        <p class="dfs-lab-sub">Step 1: Type a clean filename for Samira's CV saved in November 2026 (avoid spaces/messy words like "new final 1" or forbidden slashes):</p>
        <div style="display:flex; flex-wrap:wrap; gap:10px;">
          <input type="text" class="b-fname" placeholder="e.g. Samira Patel CV Nov 2026" style="flex:1 1 240px; min-height:46px; padding:10px 14px; border:2px solid #cbd5e1; border-radius:10px; font-size:16px; box-sizing:border-box;">
          <button type="button" class="b-fname-chk" style="padding:10px 18px; border-radius:10px; border:none; background:#0284c7; color:#fff; font-weight:700; cursor:pointer;">Check Filename</button>
        </div>
        <div class="b-fname-fb"></div>
        <hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">
        <div style="font-weight:700; margin-bottom:8px;">Step 2: Where should you look FIRST when a file you just downloaded from an email cannot be seen on your Desktop?</div>
        <div style="display:flex; flex-wrap:wrap; gap:8px;">
          <button type="button" class="b-loc" data-ok="0" style="padding:9px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">Recycle Bin</button>
          <button type="button" class="b-loc" data-ok="1" style="padding:9px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">Downloads folder in File Explorer</button>
          <button type="button" class="b-loc" data-ok="0" style="padding:9px 14px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;">Calculator app</button>
        </div>
        <div class="b-loc-fb"></div>
      </div>`;
    host.querySelector('.b-fname-chk').addEventListener('click', () => {
      const val = host.querySelector('.b-fname').value.trim();
      const badChars = /[\\/:*?"<>|]/.test(val);
      const vague = /^(doc|file|new|document|untitled|final)\b/i.test(val);
      const ok = val.length >= 6 && !badChars && !vague;
      let msg = 'Clear, descriptive, and valid on Windows, Mac, and Linux!';
      if (badChars) msg = 'Avoid forbidden symbols <code>\\ / : * ? " &lt; &gt; |</code> inside filenames.';
      else if (vague || val.length < 6) msg = 'Include who or what the file is for (e.g. <code>Samira CV 2026</code>), never just "doc" or "final".';
      host.querySelector('.b-fname-fb').innerHTML = pill(ok, msg);
    });
    host.querySelectorAll('.b-loc').forEach(btn => {
      btn.addEventListener('click', () => {
        const ok = btn.getAttribute('data-ok') === '1';
        host.querySelector('.b-loc-fb').innerHTML = pill(ok, ok
          ? 'Yes! Browsers automatically put saved email attachments and internet files into <strong>Downloads</strong> — use Search in File Explorer if needed, and move important items into a named folder in Documents.'
          : 'Downloads is the default home for files downloaded from websites or webmail; check Recycle Bin only if you deleted a file.');
      });
    });
  }

  /* 5. b05: Universal Shortcuts Sandbox */
  function mountUniversalShortcuts(host) {
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-keyboard"></i> Universal Copy, Paste &amp; Undo Practice Pad</div>
        <p class="dfs-lab-sub">Highlight the phone number below, click <strong>Copy (Ctrl+C)</strong> (or press Ctrl+C), then click inside the lower box and click <strong>Paste (Ctrl+V)</strong>:</p>
        <textarea class="b-src" rows="3" style="width:100%; min-height:96px; padding:12px; border:2px solid #cbd5e1; border-radius:10px; font-size:16px; box-sizing:border-box;">Community Learning Helpline: 0800 111 4040</textarea>
        <div style="display:flex; flex-wrap:wrap; gap:8px; margin:10px 0;">
          <button type="button" class="b-sc" data-act="selectall" style="padding:8px 12px; border-radius:8px; border:1px solid #0284c7; background:#f0f9ff; color:#0369a1; font-weight:700; cursor:pointer;">Ctrl + A (Select All)</button>
          <button type="button" class="b-sc" data-act="copy" style="padding:8px 12px; border-radius:8px; border:1px solid #0284c7; background:#f0f9ff; color:#0369a1; font-weight:700; cursor:pointer;">Ctrl + C (Copy)</button>
          <button type="button" class="b-sc" data-act="paste" style="padding:8px 12px; border-radius:8px; border:1px solid #059669; background:#ecfdf5; color:#065f46; font-weight:700; cursor:pointer;">Ctrl + V (Paste Below)</button>
          <button type="button" class="b-sc" data-act="undo" style="padding:8px 12px; border-radius:8px; border:1px solid #d97706; background:#fffbeb; color:#92400e; font-weight:700; cursor:pointer;">Ctrl + Z (Undo)</button>
        </div>
        <textarea class="b-dst" rows="3" placeholder="Paste text here..." style="width:100%; min-height:96px; padding:12px; border:2px solid #cbd5e1; border-radius:10px; font-size:16px; box-sizing:border-box;"></textarea>
        <div class="b-sc-fb"></div>
      </div>`;
    const src = host.querySelector('.b-src');
    const dst = host.querySelector('.b-dst');
    const fb = host.querySelector('.b-sc-fb');
    let clip = '';
    let prevDst = '';
    host.querySelectorAll('.b-sc').forEach(btn => {
      btn.addEventListener('click', () => {
        const act = btn.getAttribute('data-act');
        if (act === 'selectall') {
          src.focus(); src.select();
          fb.innerHTML = pill(true, 'All text highlighted! Now press Ctrl + C (Copy).');
        } else if (act === 'copy') {
          const sel = src.value.substring(src.selectionStart, src.selectionEnd) || src.value;
          clip = sel;
          fb.innerHTML = pill(true, `Copied "${esc(clip)}" safely! Now click Paste.`);
        } else if (act === 'paste') {
          if (!clip) { fb.innerHTML = pill(false, 'Clipboard is empty — click Select All or highlight text, then Copy first.'); return; }
          prevDst = dst.value;
          dst.value = (dst.value ? dst.value + '\n' : '') + clip;
          fb.innerHTML = pill(true, 'Pasted cleanly! Try Ctrl + Z (Undo) if you ever change your mind.');
        } else if (act === 'undo') {
          dst.value = prevDst;
          fb.innerHTML = pill(true, 'Undid last paste! Notice Ctrl + Z always steps backwards safely.');
        }
      });
    });
  }

  /* 6. b06: Web Search & Mini Form Lab */
  function mountWebSearchForms(host) {
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-magnifying-glass"></i> Official Search &amp; Mini Online Form Practice</div>
        <div style="font-weight:700; margin-bottom:8px;">1. You searched "renew UK passport". Which result is the official government website (not an advert charging extra fees)?</div>
        <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:16px;">
          <button type="button" class="b-sr" data-ok="0" style="text-align:left; padding:10px 12px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;"><strong>Sponsored</strong> • Fast-Passport-Help-UK.com — Express Checking Service (£45 fee)</button>
          <button type="button" class="b-sr" data-ok="1" style="text-align:left; padding:10px 12px; border-radius:8px; border:1px solid #cbd5e1; background:#fff; cursor:pointer;"><strong>GOV.UK</strong> • https://www.gov.uk/renew-adult-passport — Official UK Government Service</button>
        </div>
        <div class="b-sr-fb"></div>
        <hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">
        <div style="font-weight:700; margin-bottom:8px;">2. Mini Form Validation Check (Required * fields):</div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px;">
          <input type="text" class="b-f-name" placeholder="Full Name *" style="min-height:46px; padding:10px 14px; font-size:16px; border:1.5px solid #cbd5e1; border-radius:8px; box-sizing:border-box;">
          <input type="text" class="b-f-dob" placeholder="Date (DD/MM/YYYY) *" style="min-height:46px; padding:10px 14px; font-size:16px; border:1.5px solid #cbd5e1; border-radius:8px; box-sizing:border-box;">
          <input type="text" class="b-f-pc" placeholder="Postcode (e.g. OX1 4AA) *" style="min-height:46px; padding:10px 14px; font-size:16px; border:1.5px solid #cbd5e1; border-radius:8px; box-sizing:border-box;">
        </div>
        <button type="button" class="b-f-sub" style="margin-top:10px; padding:10px 18px; border-radius:8px; border:none; background:#0284c7; color:#fff; font-weight:700; cursor:pointer;">Check &amp; Submit Form</button>
        <div class="b-f-fb"></div>
      </div>`;
    host.querySelectorAll('.b-sr').forEach(b => {
      b.addEventListener('click', () => {
        const ok = b.getAttribute('data-ok') === '1';
        host.querySelector('.b-sr-fb').innerHTML = pill(ok, ok
          ? 'Correct! Official UK government services always end in <strong>.gov.uk</strong> — skip "Sponsored" advert boxes at the top.'
          : 'Watch out! "Sponsored" results are paid adverts that often add unnecessary agency fees.');
      });
    });
    host.querySelector('.b-f-sub').addEventListener('click', () => {
      const nm = host.querySelector('.b-f-name').value.trim();
      const dob = host.querySelector('.b-f-dob').value.trim();
      const pc = host.querySelector('.b-f-pc').value.trim();
      const okDate = /^\d{2}\/\d{2}\/\d{4}$/.test(dob);
      const okPc = /^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$/i.test(pc);
      const ok = nm.length >= 2 && okDate && okPc;
      const errs = [];
      if (nm.length < 2) errs.push('Enter your Full Name.');
      if (!okDate) errs.push('Use DD/MM/YYYY format (e.g. 14/06/1992).');
      if (!okPc) errs.push('Enter a valid UK postcode (e.g. OX1 4AA).');
      host.querySelector('.b-f-fb').innerHTML = pill(ok, ok ? 'Form check passed! Ready for confirmation screenshot evidence.' : errs.join(' '));
    });
  }

  /* 7. b07: Email & Everyday Troubleshooting */
  function mountEmailTroubleshoot(host) {
    const scenarios = [
      { s: 'You hear NO sound during a tutor video call.', ans: 1, opts: ['Delete the browser', 'Check speaker icon in bottom-right tray isn\'t muted & volume slider is up', 'Turn off Wi-Fi'] },
      { s: 'You need to email a photo attachment to your tutor.', ans: 2, opts: ['Drag the laptop screen', 'Put the filename in the Subject box only', 'Click the Paperclip (Attach) button, open Pictures/Downloads, and wait for upload to finish before clicking Send'] }
    ];
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-envelope-circle-check"></i> Everyday Email &amp; Quick Troubleshooting Check</div>
        ${scenarios.map((it, i) => `
          <div style="margin-bottom:12px; padding:12px; background:#fff; border:1px solid #e2e8f0; border-radius:10px;">
            <div style="font-weight:700; margin-bottom:8px;">Scenario ${i + 1}: ${it.s}</div>
            <div style="display:flex; flex-direction:column; gap:6px;">
              ${it.opts.map((o, oi) => `<button type="button" class="b-et" data-q="${i}" data-o="${oi}" style="text-align:left; padding:9px 12px; border-radius:8px; border:1px solid #cbd5e1; background:#f8fafc; cursor:pointer;">${o}</button>`).join('')}
            </div>
            <div class="b-et-fb-${i}"></div>
          </div>`).join('')}
      </div>`;
    host.querySelectorAll('.b-et').forEach(btn => {
      btn.addEventListener('click', () => {
        const qi = Number(btn.getAttribute('data-q'));
        const oi = Number(btn.getAttribute('data-o'));
        const ok = oi === scenarios[qi].ans;
        host.querySelector(`.b-et-fb-${qi}`).innerHTML = pill(ok, ok ? 'Spot on — calm first-aid check!' : 'Try another option that solves the cause directly.');
      });
    });
  }

  /* 8. b08: Word & LibreOffice Writer Preflight Lab */
  function mountWordWriter(host) {
    const items = [
      { id: 'title', label: 'Main heading made Bold + larger (18–24pt) than body text (11–12pt)', ok: true },
      { id: 'ratio', label: 'Photo resized with "Keep / Lock Aspect Ratio" ticked (using corner handles)', ok: true },
      { id: 'spell', label: 'Red squiggly typos fixed and extra empty blank pages removed', ok: true },
      { id: 'save', label: 'Saved with exact requested name inside the right folder (Ctrl + S)', ok: true },
    ];
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-file-word"></i> Word &amp; LibreOffice Writer Makeover Preflight</div>
        <p class="dfs-lab-sub">Tick every check you completed on your starter <code>.docx</code> practice file to verify exam-ready quality:</p>
        <div style="display:flex; flex-direction:column; gap:8px;">
          ${items.map(it => `<label style="display:flex; align-items:center; gap:10px; padding:10px 12px; background:#fff; border:1px solid #cbd5e1; border-radius:8px; cursor:pointer;"><input type="checkbox" class="b-ww-cb" style="width:18px;height:18px;"> <span>${it.label}</span></label>`).join('')}
        </div>
        <div class="b-ww-fb" style="margin-top:10px;"></div>
      </div>`;
    const cbs = host.querySelectorAll('.b-ww-cb');
    const fb = host.querySelector('.b-ww-fb');
    cbs.forEach(cb => cb.addEventListener('change', () => {
      const n = Array.from(cbs).filter(x => x.checked).length;
      fb.innerHTML = pill(n === items.length, `${n} of ${items.length} professional layout checks complete.${n === items.length ? ' Document is ready to print or export as PDF!' : ''}`);
    }));
  }

  /* 9. b09: PowerPoint & LibreOffice Impress Doctor */
  function mountPowerPointImpress(host) {
    host.innerHTML = `
      <div class="dfs-lab-card">
        <div class="dfs-lab-head"><i class="fa-solid fa-file-powerpoint"></i> Slide Design &amp; Contrast Doctor</div>
        <div style="font-weight:700; margin-bottom:8px;">Which slide design gives learners maximum readability in PowerPoint or LibreOffice Impress?</div>
        <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px;">
          <button type="button" class="b-pp" data-ok="0" style="text-align:left; padding:14px; border-radius:10px; border:2px solid #cbd5e1; background:#facc15; color:#ffffff; cursor:pointer; font-weight:700;">Option A: Bright yellow text on white or lemon background with 180-word paragraph.</button>
          <button type="button" class="b-pp" data-ok="1" style="text-align:left; padding:14px; border-radius:10px; border:2px solid #0284c7; background:#0f172a; color:#f8fafc; cursor:pointer; font-weight:700;">Option B: High-contrast text, clear 28pt+ title, and 3–4 short bullet points + one clean photo.</button>
        </div>
        <div class="b-pp-fb"></div>
      </div>`;
    host.querySelectorAll('.b-pp').forEach(b => {
      b.addEventListener('click', () => {
        const ok = b.getAttribute('data-ok') === '1';
        host.querySelector('.b-pp-fb').innerHTML = pill(ok, ok
          ? 'Spot on! Slides need strong colour contrast, short bullet lines (never long essays), and consistent slide titles.'
          : 'Hard to read! Low contrast colours and walls of tiny text lose layout quality.');
      });
    });
  }

  /* 10. b10: Interactive Multi-Exercise Excel / Calc Sandbox */
  function mountExcelCalc(host) {
    const exercises = [
      { id: 'ex1', tab: '1. Multiply (=B2*C2)', prompt: 'In <strong>01 Corner Shop Sales</strong>, type the formula for <code>D2</code> to multiply Unit Price (<code>B2</code> = £1.35) by Quantity (<code>C2</code> = 14):', hint: '=B2*C2', expect: '=B2*C2', alt: '=C2*B2', result: '£18.90' },
      { id: 'ex2', tab: '2. Total (=SUM)', prompt: 'In <strong>02 Community Cafe Orders</strong>, write the <code>SUM</code> formula for cells <code>B5</code> down to <code>B10</code>:', hint: '=SUM(B5:B10)', expect: '=SUM(B5:B10)', result: '314 orders' },
      { id: 'ex3', tab: '3. Average (=AVERAGE)', prompt: 'Calculate the daily average takings across cells <code>C5</code> through <code>C10</code>:', hint: '=AVERAGE(C5:C10)', expect: '=AVERAGE(C5:C10)', result: '£400.16' },
      { id: 'ex4', tab: '4. Min / Max', prompt: 'In <strong>03 Household Budget</strong>, write the formula to find the <strong>highest</strong> actual spend in <code>C5:C10</code>:', hint: '=MAX(C5:C10)', expect: '=MAX(C5:C10)', result: '£680.00' },
      { id: 'ex5', tab: '5. Conditional (=IF)', prompt: 'In <strong>05 Stock Check</strong>, write the <code>=IF</code> formula showing <code>"Reorder"</code> when stock <code>C5</code> is less than minimum <code>B5</code>, else <code>"OK"</code>:', hint: '=IF(C5<B5,"Reorder","OK")', expect: '=IF(C5<B5,"REORDER","OK")', result: 'Reorder' },
    ];
    let active = 0;
    function render() {
      const ex = exercises[active];
      host.innerHTML = `
        <div class="dfs-lab-card">
          <div class="dfs-lab-head"><i class="fa-solid fa-table"></i> Interactive Excel &amp; LibreOffice Calc Formula Lab (5 Drills)</div>
          <div style="display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 14px;">
            ${exercises.map((e, i) => `<button type="button" class="b-ex-tab" data-idx="${i}" style="padding:8px 12px; border-radius:8px; border:1px solid ${i === active ? '#0284c7' : '#cbd5e1'}; background:${i === active ? '#0284c7' : '#fff'}; color:${i === active ? '#fff' : '#0f172a'}; font-weight:700; cursor:pointer; font-size:0.86rem;">${e.tab}</button>`).join('')}
          </div>
          <p class="dfs-lab-sub">${ex.prompt}</p>
          <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center;">
            <span style="padding:10px 12px; background:#0f172a; color:#38bdf8; border-radius:8px; font-weight:800; font-family:monospace;">fx</span>
            <input type="text" class="b-ex-inp" placeholder="Type formula starting with = ..." style="flex:1 1 240px; min-height:46px; padding:10px 14px; border:2px solid #cbd5e1; border-radius:10px; font-family:monospace; font-size:16px; box-sizing:border-box;">
            <button type="button" class="b-ex-run" style="padding:10px 18px; border-radius:10px; border:none; background:#059669; color:#fff; font-weight:700; cursor:pointer;">Press Enter</button>
          </div>
          <div class="b-ex-fb"></div>
        </div>`;
      host.querySelectorAll('.b-ex-tab').forEach(btn => {
        btn.addEventListener('click', () => { active = Number(btn.getAttribute('data-idx')); render(); });
      });
      const inp = host.querySelector('.b-ex-inp');
      const run = () => {
        const clean = inp.value.replace(/\s+/g, '').toUpperCase();
        const ok = clean === ex.expect || (ex.alt && clean === ex.alt);
        host.querySelector('.b-ex-fb').innerHTML = pill(ok, ok
          ? `Spot on! Displays <strong>${ex.result}</strong> dynamically — press Enter, then use the bottom-right corner fill handle (+) to drag across other rows.`
          : `Check your syntax — remember to start with <code>=</code> and use exact cell references. Example answer: <code>${esc(ex.hint)}</code>`);
      };
      host.querySelector('.b-ex-run').addEventListener('click', run);
      inp.addEventListener('keydown', (e) => { if (e.key === 'Enter') run(); });
    }
    render();
  }

  function init() {
    const map = {
      'mouse-keyboard': mountMouseKeyboard,
      'forgot-password': mountForgotPassword,
      'windows-apps': mountWindowsApps,
      'files-folders': mountFilesFolders,
      'universal-shortcuts': mountUniversalShortcuts,
      'web-search-forms': mountWebSearchForms,
      'email-troubleshoot': mountEmailTroubleshoot,
      'word-writer-lab': mountWordWriter,
      'powerpoint-impress-lab': mountPowerPointImpress,
      'excel-calc-lab': mountExcelCalc,
    };
    document.querySelectorAll('[data-basics-lab]').forEach(el => {
      const kind = el.getAttribute('data-basics-lab');
      if (map[kind]) map[kind](el);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
