/**
 * Master Functional Skills - Authentic Pearson Onscreen Test Player App Engine
 * Replicates the official Pearson Onscreen Platform (POP) screen-by-screen environment.
 */

let popCurrentScreen = 0;
let popTotalScreens = 20;
let popUserAnswers = {}; // { qNum: optionIdx }
let popFlaggedQuestions = {}; // { qNum: boolean }
let popTaskEvidence = {}; // { taskCode: boolean }
let popRubricChecked = {}; // { rubricCode: boolean }
let popTimerSeconds = 90 * 60;
let popTimerActive = false;
let popTimerHandle = null;
let popIsFullscreen = false;
let popCandidateName = "Learner Candidate";
let popCurrentSetKey = "set1";

// Test numbers mapping to replicate official Pearson Diagnostic Report (e.g. 203114, 203115...)
const PEARSON_TEST_NUMBERS = [
  "203114", "203115", "203116", "203117", "203118", 
  "203119", "203120", "203121", "203122", "203123",
  "203124", "203125", "203126", "203127", "203128"
];

document.addEventListener("DOMContentLoaded", () => {
  initPearsonApp();
});

function initPearsonApp() {
  const urlParams = new URLSearchParams(window.location.search);
  const startScreen = parseInt(urlParams.get("screen") || "0", 10);
  const startSet = urlParams.get("set") || (document.getElementById("popSetSelector")?.value || "mfs_mock1");
  const startFs = urlParams.get("fullscreen") === "true";

  loadSetData(startSet);
  const selector = document.getElementById("popSetSelector");
  if (selector) selector.value = startSet;

  popCurrentScreen = startScreen;
  renderScreen(startScreen);
  startPopTimer();

  if (startFs) {
    togglePopFullscreen();
  }
}

function loadSetData(setKey) {
  popCurrentSetKey = setKey;
  popUserAnswers = {};
  popFlaggedQuestions = {};
  popTaskEvidence = {};
  popRubricChecked = {};
  
  const set = DFS_MOCK_DATA[setKey] || DFS_MOCK_DATA["set1"];
  popTimerSeconds = set.durationMinutes * 60;
  updatePopTimerDisplay();
  
  // Update Titlebar
  const titleEl = document.getElementById("popWindowSubtitle");
  if (titleEl) {
    titleEl.textContent = `Pearson Test Player - ${set.level}: ${set.name.split(":")[1] || set.name}`;
  }
}

function handleSetChange(newSetKey) {
  loadSetData(newSetKey);
  popCurrentScreen = 0;
  renderScreen(0);
}

function renderScreen(index) {
  popCurrentScreen = index;
  const canvas = document.getElementById("popCanvas");
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  if (!canvas || !set) return;

  // Auto-scroll player smoothly into comfortable viewport view when active
  if (index > 0 && !popIsFullscreen) {
    const shell = document.getElementById("popAppShell");
    if (shell) {
      const rect = shell.getBoundingClientRect();
      if (rect.top < 0 || rect.top > 120) {
        shell.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }
  }

  // Screen 0: Test Welcome Screen
  if (index === 0) {
    canvas.innerHTML = `
      <div class="pearson-splash-screen">
        <div class="pearson-logo-row">
          <div class="pearson-p-logo">?</div>
          <div class="pearson-brand-word">Pearson</div>
        </div>

        <div class="pearson-splash-title">Digital Functional Skills Qualification at ${set.level}</div>
        <div style="font-size:1.15rem; color:#444444; margin-bottom:24px;">${set.name}</div>

        <p style="font-size:1.05rem; line-height:1.6; margin-bottom:16px;">This assessment has two sections:</p>
        <ul class="pearson-bullet-list">
          <li><strong>Section A (questions)</strong> — 10 questions (10 marks)</li>
          <li><strong>Section B (tasks)</strong> — Workplace practical skills (${set.totalMarks - 10} marks)</li>
        </ul>

        <p style="font-size:1.05rem; margin-bottom:8px;"><strong>The total marks for this assessment is ${set.totalMarks} marks.</strong></p>
        <p style="font-size:1.05rem; margin-bottom:24px;"><strong>The total time allowed for this assessment is ${set.durationMinutes} minutes.</strong></p>

        <p style="font-size:0.85rem; color:#666666; line-height:1.5; margin-top:30px;">
          The copyright in the questions is either owned or licensed by Pearson.<br>
          Every effort has been made to contact the copyright holders to obtain their permission.
        </p>

        <div class="pearson-start-btn-wrap">
          <button type="button" class="btn-pearson-start" onclick="goToNextScreen()">Start Test</button>
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screen 1: Section A Splash
  if (index === 1) {
    canvas.innerHTML = `
      <div class="pearson-splash-screen">
        <div class="pearson-splash-title">Digital Functional Skills Qualification at ${set.level}</div>
        <div class="pearson-splash-subtitle">Section A</div>

        <ul class="pearson-bullet-list">
          <li>This section is <strong>15 minutes</strong>.</li>
          <li>The time you have left will be shown at the bottom of the screen.</li>
          <li>There are <strong>10 questions</strong> in this section.</li>
        </ul>

        <div class="pearson-splash-heading">Instructions</div>
        <ul class="pearson-bullet-list">
          <li>Answer <strong>all</strong> questions.</li>
          <li>You must <strong>not</strong> use the internet in Section A.</li>
          <li>Click on the question mark icon to access the help screen.</li>
        </ul>

        <div class="pearson-splash-heading">Information</div>
        <ul class="pearson-bullet-list">
          <li>The total number of marks for this section is <strong>10</strong>.</li>
          <li>The number of marks available for each question is shown in brackets.</li>
          <li>After you have moved onto Section B, you will <strong>not</strong> be able to return to Section A.</li>
        </ul>

        <div class="pearson-start-btn-wrap">
          <button type="button" class="btn-pearson-start" onclick="goToNextScreen()">Start Section</button>
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screens 2 to 11: Section A Questions 1 to 10
  if (index >= 2 && index <= 11) {
    const qIndex = index - 2; // 0 to 9
    const q = set.sectionA[qIndex];
    const qNum = q.qNum;
    const selectedOpt = popUserAnswers[qNum];
    const isFlagged = !!popFlaggedQuestions[qNum];

    canvas.innerHTML = `
      <div style="max-width:860px; margin:0 auto; width:100%;">
        <div class="pearson-scenario-text">Section A • Knowledge and Understanding</div>
        
        <div class="pearson-qbox">
          <div class="pearson-qbox-text">${q.stem}</div>
          <div class="pearson-qbox-mark">(${q.mark})</div>
        </div>

        <div class="pearson-select-prompt">Select one option.</div>

        <div class="pearson-pill-options">
          ${q.options.map((opt, optIdx) => `
            <div class="pearson-pill-btn ${selectedOpt === optIdx ? "selected" : ""}" 
                 onclick="selectPearsonOption(${qNum}, ${optIdx})">
              ${opt.text}
            </div>
          `).join("")}
        </div>

        <div class="pearson-rationale-box ${selectedOpt !== undefined ? "show" : ""}" id="rationaleBox">
          <strong><i class="fa-solid fa-graduation-cap"></i> Pearson Examiner Rationale:</strong><br>
          ${q.explanation}
        </div>
      </div>
    `;
    updateBottomBar(index, qNum, isFlagged);
    return;
  }

  // Screen 12: Section A Summary Screen
  if (index === 12) {
    canvas.innerHTML = `
      <div class="pearson-summary-wrap">
        <div class="pearson-summary-title">Section Summary</div>
        <div class="pearson-summary-subtitle">You have reached the end of this section. You can review your answers here.</div>

        <div class="pearson-summary-legend">
          <div class="legend-row">
            <span class="legend-badge-blue">#</span>
            <span>Numbers on a <strong>BLUE Background</strong> with <strong>✖</strong> indicate that you have <strong>NOT</strong> attempted question.</span>
          </div>
          <div class="legend-row">
            <span style="font-size:1.1rem; color:#475569;">⚑</span>
            <span>Identifies questions you have <strong>flagged for review</strong>.</span>
          </div>
          <div class="legend-row">
            <span class="legend-badge-orange">#</span>
            <span>Numbers on an <strong>ORANGE Background</strong> with <strong>✔</strong> indicate that you <strong>HAVE</strong> attempted question.</span>
          </div>
        </div>

        <div class="pearson-summary-grid">
          ${set.sectionA.map((q, qIdx) => {
            const isAttempted = popUserAnswers[q.qNum] !== undefined;
            const isFl = !!popFlaggedQuestions[q.qNum];
            return `
              <div class="summary-grid-cell ${isAttempted ? "attempted" : "unattempted"} ${isFl ? "flagged" : ""}" 
                   onclick="goToScreen(${qIdx + 2})" title="Click to view Question ${q.qNum}">
                <span>${q.qNum}</span>
                <span class="status-icon">${isAttempted ? "✔" : "✖"}</span>
              </div>
            `;
          }).join("")}
        </div>

        <p style="text-align:center; font-size:0.95rem; color:#333333; margin-top:20px;">
          Please note that once you complete a section, you will not be able to review your answers again.
        </p>

        <div class="pearson-summary-actions">
          <button type="button" class="btn-summary-action" onclick="goToScreen(11)">
            <i class="fa-solid fa-circle-chevron-left"></i> BACK
          </button>
          <button type="button" class="btn-summary-action" onclick="showPearsonReportModal()">
            GENERATE REPORT <i class="fa-solid fa-circle-chevron-right"></i>
          </button>
          <button type="button" class="btn-summary-action" onclick="goToNextScreen()" style="color:#d85c13; font-weight:800;">
            COMPLETE SECTION <i class="fa-solid fa-circle-chevron-right"></i>
          </button>
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screen 13: Section B Splash
  if (index === 13) {
    canvas.innerHTML = `
      <div class="pearson-splash-screen">
        <div class="pearson-splash-title">Digital Functional Skills Qualification at ${set.level}</div>
        <div class="pearson-splash-subtitle">Section B</div>

        <ul class="pearson-bullet-list">
          <li>This section is <strong>90 minutes</strong>.</li>
          <li>The time you have left will be shown at the bottom of the screen.</li>
          <li>There are <strong>${set.tasks.length} tasks</strong> in this section (${set.tasks.map(t => t.letter).join(", ")}).</li>
        </ul>

        <div class="pearson-splash-heading">Instructions</div>
        <ul class="pearson-bullet-list">
          <li>Complete <strong>all</strong> tasks.</li>
          <li>You <strong>may</strong> use the internet in Section B.</li>
          <li>Click on the question mark icon to access the help screen.</li>
        </ul>

        <div class="pearson-splash-heading">Information</div>
        <ul class="pearson-bullet-list">
          <li>The total number of marks for this section is <strong>${set.totalMarks - 10}</strong>.</li>
          <li>The number of marks available for each task is shown in brackets.</li>
        </ul>

        <div class="pearson-splash-heading">Advice</div>
        <ul class="pearson-bullet-list">
          <li>Read the instructions carefully before you start each task.</li>
          <li>Use the tick boxes at the end of each task to check that you have all the evidence you need.</li>
          <li>Check your answers if you have time at the end.</li>
        </ul>

        <div class="pearson-start-btn-wrap">
          <button type="button" class="btn-pearson-start" onclick="goToNextScreen()">Start Section</button>
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screen 14: Section B Tasks Overview & Data Folder Files
  if (index === 14) {
    canvas.innerHTML = `
      <div style="max-width:860px; margin:0 auto; width:100%;">
        <p style="font-size:1.1rem; font-weight:700;">Complete ALL tasks within the assessment.</p>
        <p style="font-size:1rem; margin-bottom:12px;">This assessment has ${set.tasks.length} tasks:</p>

        <table class="pearson-task-table">
          <thead>
            <tr>
              <th>Task</th>
              <th>Marks</th>
            </tr>
          </thead>
          <tbody>
            ${set.tasks.map(t => `
              <tr>
                <td><strong>${t.letter}</strong></td>
                <td>${t.marks}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>

        <div class="pearson-splash-heading">Information</div>
        <p style="font-size:0.95rem; line-height:1.5;">
          The data folder contains the files you need for Section B:
        </p>
        <ul class="pearson-bullet-list">
          ${set.dataFiles.map(f => `<li><code>${f}</code></li>`).join("")}
        </ul>

        <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:16px; margin:20px 0; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <strong>Download Candidate Data Files:</strong><br>
            <span style="font-size:0.85rem; color:#475569;">Extract to your computer or practice directly in the simulators below</span>
          </div>
          <a href="${set.dataPackUrl}" class="btn-pearson-start" style="padding:8px 18px; font-size:0.95rem; text-decoration:none;" download>
            <i class="fa-solid fa-cloud-arrow-down"></i> Download Data Files (.ZIP)
          </a>
        </div>

        <div class="pearson-next-task-prompt">
          Continue to ${set.tasks[0].letter} on the next screen &gt;&gt;
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screens 15 to 19: Tasks A, B, C, D, E
  if (index >= 15 && index < 15 + set.tasks.length) {
    const taskIdx = index - 15;
    const task = set.tasks[taskIdx];
    const taskMarksEarned = task.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0);

    canvas.innerHTML = `
      <div style="max-width:920px; margin:0 auto; width:100%;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
          <h2 style="margin:0; font-size:1.35rem; color:#111111;">${task.letter}: ${task.title}</h2>
          <span style="font-size:1.05rem; font-weight:700; color:#0f172a; background:#f1f5f9; padding:4px 12px; border-radius:6px; border:1px solid #cbd5e1;">
            Awarded: <strong style="color:${taskMarksEarned === task.marks ? '#16a34a' : '#d97706'};">${taskMarksEarned} / ${task.marks} Marks</strong>
          </span>
        </div>

        <p style="font-size:1.02rem; margin:0 0 16px 0; color:#222222;">
          <strong>Context:</strong> ${task.brief}
        </p>

        <div class="pearson-task-intro-box">
          <ol style="margin:0; padding-left:22px; line-height:1.7; font-size:0.98rem;">
            ${task.instructions.map(inst => `<li>${inst}</li>`).join("")}
          </ol>
        </div>

        <!-- Integrated Simulator for this Task -->
        ${renderSimulatorForTask(task)}

        <!-- Pearson Assessor Rubric Criteria Checklist -->
        <div class="pearson-rubric-card" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:16px; margin:16px 0;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <div style="font-weight:700; font-size:0.95rem; color:#0f172a;">
              <i class="fa-solid fa-list-check" style="color:var(--pop-orange);"></i> 
              Pearson Edexcel Assessor Criteria Checklist (${task.marks} Marks Available)
            </div>
            <button type="button" class="btn-award-task-all" onclick="awardAllTaskRubric('${task.id}')" style="background:#e0f2fe; color:#0369a1; border:1px solid #bae6fd; border-radius:4px; padding:4px 12px; font-size:0.82rem; font-weight:700; cursor:pointer;">
              <i class="fa-solid fa-check-double"></i> Award All Evidence for ${task.letter}
            </button>
          </div>
          <div style="display:grid; grid-template-columns:1fr; gap:6px;">
            ${task.rubric.map(r => `
              <label style="display:flex; align-items:flex-start; gap:10px; font-size:0.88rem; cursor:pointer; color:#334155; padding:6px 10px; border-radius:4px; background:#ffffff; border:1px solid ${popRubricChecked[r.code] ? '#86efac' : '#e2e8f0'};">
                <input type="checkbox" id="popRubric_${r.code}" 
                       ${popRubricChecked[r.code] ? "checked" : ""} 
                       onchange="togglePopRubricCriterion('${task.id}', '${r.code}', this.checked)"
                       style="margin-top:2px;">
                <span style="flex:1;"><strong>[${r.code}]</strong> ${r.desc}</span>
                <span style="font-weight:700; color:#0284c7; white-space:nowrap;">${r.mark} ${r.mark === 1 ? 'mark' : 'marks'}</span>
              </label>
            `).join("")}
          </div>
        </div>

        <div class="pearson-evidence-check">
          <label style="cursor:pointer; display:flex; align-items:center; gap:10px;">
            <input type="checkbox" id="evCheck_${task.id}" 
                   ${popTaskEvidence[task.id] ? "checked" : ""} 
                   onchange="handleTaskEvidenceToggle('${task.id}', this.checked)">
            <span>Evidence: I have completed and verified my output for ${task.letter} (${task.marks} Marks)</span>
          </label>
        </div>

        <div class="pearson-next-task-prompt">
          ${taskIdx < set.tasks.length - 1 
            ? `Continue to ${set.tasks[taskIdx + 1].letter} on the next screen &gt;&gt;` 
            : `Continue to Section B Summary on the next screen &gt;&gt;`}
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }

  // Screen 20: Section B Summary & Final Generate Report Screen
  if (index >= 15 + set.tasks.length) {
    let totalSecBScored = 0;
    set.tasks.forEach(t => {
      t.rubric.forEach(r => {
        if (popRubricChecked[r.code]) totalSecBScored += r.mark;
      });
    });

    canvas.innerHTML = `
      <div class="pearson-summary-wrap">
        <div class="pearson-summary-title">Section B Summary</div>
        <div class="pearson-summary-subtitle">You have completed all assessment tasks. Review your evidence and generate your official report below.</div>

        <div style="background:#ffffff; border:1px solid #bfbfbf; border-radius:8px; padding:20px; max-width:760px; margin:20px auto; text-align:left;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
            <h4 style="margin:0; font-size:1.1rem; color:#0f172a;"><i class="fa-solid fa-clipboard-check" style="color:var(--pop-orange);"></i> Section B Practical Task Evidence Breakdown:</h4>
            <button type="button" class="btn-pop-action" onclick="awardAllSectionBEvidence(); renderScreen(popCurrentScreen);" style="padding:4px 12px; font-size:0.82rem;">
              <i class="fa-solid fa-check-double"></i> Award All Section B Evidence (44/44)
            </button>
          </div>

          ${set.tasks.map(t => {
            const tMarks = t.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0);
            return `
              <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 0; border-bottom:1px solid #f1f5f9; font-size:0.95rem;">
                <div>
                  <strong>${t.letter}:</strong> ${t.title}
                  <span style="color:#64748b; font-size:0.85rem; margin-left:6px;">(${t.marks} Marks Available)</span>
                </div>
                <div style="display:flex; align-items:center; gap:12px;">
                  <span style="font-weight:700; color:${tMarks === t.marks ? "#16a34a" : (tMarks > 0 ? "#0284c7" : "#d97706")};">
                    ${tMarks} / ${t.marks} Marks Awarded
                  </span>
                  <button type="button" onclick="goToScreen(${15 + set.tasks.indexOf(t)})" style="background:none; border:1px solid #cbd5e1; border-radius:4px; padding:2px 8px; font-size:0.8rem; cursor:pointer;">
                    Edit
                  </button>
                </div>
              </div>
            `;
          }).join("")}

          <div style="margin-top:14px; padding-top:10px; display:flex; justify-content:space-between; font-weight:800; font-size:1.05rem; color:#0f172a;">
            <span>Section B Subtotal:</span>
            <span style="color:#0284c7;">${totalSecBScored} / 44 Marks</span>
          </div>
        </div>

        <div class="pearson-summary-actions" style="margin-top:28px;">
          <button type="button" class="btn-summary-action" onclick="goToScreen(${index - 1})">
            <i class="fa-solid fa-circle-chevron-left"></i> BACK TO TASKS
          </button>
          <button type="button" class="btn-summary-action" onclick="showPearsonReportModal()" style="color:#d85c13; font-size:1.15rem; font-weight:800;">
            <i class="fa-solid fa-file-lines"></i> GENERATE REPORT <i class="fa-solid fa-circle-chevron-right"></i>
          </button>
        </div>
      </div>
    `;
    updateBottomBar(index, 0, false);
    return;
  }
}

function updateBottomBar(screenIndex, qNum, isFlagged) {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  const totalScreens = 15 + set.tasks.length; // Screen 0 to final summary

  // Counter
  const counterEl = document.getElementById("popCounterDisplay");
  if (counterEl) {
    if (qNum > 0) {
      counterEl.textContent = `${qNum} / 10`;
    } else {
      counterEl.textContent = `${screenIndex + 1} / ${totalScreens + 1}`;
    }
  }

  // Nav buttons
  const prevBtn = document.getElementById("popPrevBtn");
  const nextBtn = document.getElementById("popNextBtn");
  if (prevBtn) prevBtn.disabled = screenIndex === 0;
  if (nextBtn) nextBtn.disabled = screenIndex >= totalScreens;

  // Flag button
  const flagBtn = document.getElementById("popFlagBtn");
  if (flagBtn) {
    flagBtn.classList.toggle("active-flag", isFlagged);
    flagBtn.style.color = isFlagged ? "#f59e0b" : "#d1d5db";
  }
}

function goToNextScreen() {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  const maxScreen = 15 + set.tasks.length;
  if (popCurrentScreen < maxScreen) {
    renderScreen(popCurrentScreen + 1);
  }
}

function goToPrevScreen() {
  if (popCurrentScreen > 0) {
    renderScreen(popCurrentScreen - 1);
  }
}

function goToScreen(idx) {
  renderScreen(idx);
}

function selectPearsonOption(qNum, optIdx) {
  popUserAnswers[qNum] = optIdx;
  renderScreen(popCurrentScreen);
}

function togglePearsonFlag() {
  if (popCurrentScreen >= 2 && popCurrentScreen <= 11) {
    const qNum = popCurrentScreen - 1;
    popFlaggedQuestions[qNum] = !popFlaggedQuestions[qNum];
    updateBottomBar(popCurrentScreen, qNum, popFlaggedQuestions[qNum]);
  }
}

// Timer Controls
function startPopTimer() {
  if (popTimerActive) return;
  popTimerActive = true;
  popTimerHandle = setInterval(() => {
    if (popTimerSeconds > 0) {
      popTimerSeconds--;
      updatePopTimerDisplay();
    } else {
      clearInterval(popTimerHandle);
      popTimerActive = false;
      alert("Exam time elapsed! Please generate your Pearson diagnostic report.");
    }
  }, 1000);
}

function updatePopTimerDisplay() {
  const mins = Math.floor(popTimerSeconds / 60);
  const secs = popTimerSeconds % 60;
  const str = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  const el = document.getElementById("popTimerDisplay");
  if (el) el.textContent = str;
}

// Fullscreen & Fill Screen Toggle
function togglePopFullscreen() {
  const shell = document.getElementById("popAppShell");
  if (!shell) return;

  const isFs = !!(document.fullscreenElement || shell.classList.contains("fullscreen"));

  if (!isFs) {
    // Enter Full Screen (Monitor Takeover)
    if (shell.requestFullscreen) {
      shell.requestFullscreen().catch(() => {});
    } else if (shell.webkitRequestFullscreen) {
      shell.webkitRequestFullscreen();
    } else if (shell.msRequestFullscreen) {
      shell.msRequestFullscreen();
    }
    shell.classList.add("fullscreen");
    popIsFullscreen = true;
  } else {
    // Exit Full Screen
    if (document.exitFullscreen && document.fullscreenElement) {
      document.exitFullscreen().catch(() => {});
    } else if (document.webkitExitFullscreen && document.webkitFullscreenElement) {
      document.webkitExitFullscreen();
    }
    shell.classList.remove("fullscreen");
    popIsFullscreen = false;
  }
  updateFullscreenButtons();
}

function updateFullscreenButtons() {
  const shell = document.getElementById("popAppShell");
  const isFs = shell ? (shell.classList.contains("fullscreen") || !!document.fullscreenElement) : false;

  // Titlebar button
  const titleBtn = document.getElementById("btnFillScreen");
  if (titleBtn) {
    titleBtn.classList.toggle("active", isFs);
    titleBtn.innerHTML = isFs 
      ? '<i class="fa-solid fa-compress"></i> <span>Exit Fill Screen</span>' 
      : '<i class="fa-solid fa-expand"></i> <span>Fill Screen</span>';
  }

  // Titlebar Windows Maximize button
  const maxBtn = document.getElementById("popWinMaximizeBtn");
  if (maxBtn) {
    maxBtn.textContent = isFs ? "🗗" : "□";
    maxBtn.title = isFs ? "Restore Down" : "Maximize / Fill Screen";
  }

  // Hero button
  const heroBtn = document.getElementById("heroFillScreenBtn");
  if (heroBtn) {
    heroBtn.innerHTML = isFs
      ? '<i class="fa-solid fa-compress"></i> <span>Exit Fill Screen</span>'
      : '<i class="fa-solid fa-expand"></i> <span>Fill Screen</span>';
  }

  // Bottom bar button
  const bottomFsBtn = document.getElementById("popBottomFsBtn");
  if (bottomFsBtn) {
    bottomFsBtn.innerHTML = isFs
      ? '<i class="fa-solid fa-compress"></i>'
      : '<i class="fa-solid fa-expand"></i>';
    bottomFsBtn.title = isFs ? "Exit Fill Screen" : "Fill Screen (POP Mode)";
  }
}

// Synchronize with native fullscreen change events (e.g. Esc key pressed)
document.addEventListener("fullscreenchange", () => {
  const shell = document.getElementById("popAppShell");
  if (!shell) return;
  if (!document.fullscreenElement) {
    shell.classList.remove("fullscreen");
    popIsFullscreen = false;
  } else {
    shell.classList.add("fullscreen");
    popIsFullscreen = true;
  }
  updateFullscreenButtons();
});

// Section B Task Evidence and Rubric Toggles
function togglePopRubricCriterion(taskId, code, isChecked) {
  popRubricChecked[code] = isChecked;
  if (typeof rubricChecked !== "undefined") {
    rubricChecked[code] = isChecked;
  }
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  const task = set.tasks.find(t => t.id === taskId);
  if (task) {
    const allChecked = task.rubric.every(r => popRubricChecked[r.code]);
    popTaskEvidence[taskId] = allChecked;
    const evBox = document.getElementById("evCheck_" + taskId);
    if (evBox) evBox.checked = allChecked;
  }
}

function handleTaskEvidenceToggle(taskId, isChecked) {
  popTaskEvidence[taskId] = isChecked;
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  const task = set.tasks.find(t => t.id === taskId);
  if (task) {
    task.rubric.forEach(r => {
      popRubricChecked[r.code] = isChecked;
      if (typeof rubricChecked !== "undefined") {
        rubricChecked[r.code] = isChecked;
      }
      const el = document.getElementById("popRubric_" + r.code);
      if (el) el.checked = isChecked;
    });
  }
  // Re-render task canvas to update awarded badge
  if (popCurrentScreen >= 15 && popCurrentScreen < 15 + set.tasks.length) {
    renderScreen(popCurrentScreen);
  }
}

function awardAllTaskRubric(taskId) {
  handleTaskEvidenceToggle(taskId, true);
}

function toggleReportRubric(taskId, code, isChecked) {
  togglePopRubricCriterion(taskId, code, isChecked);
  showPearsonReportModal();
}

function awardAllSectionBEvidence() {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  set.tasks.forEach(t => {
    popTaskEvidence[t.id] = true;
    t.rubric.forEach(r => {
      popRubricChecked[r.code] = true;
      if (typeof rubricChecked !== "undefined") rubricChecked[r.code] = true;
    });
  });
  showPearsonReportModal();
}

function clearAllSectionBEvidence() {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  set.tasks.forEach(t => {
    popTaskEvidence[t.id] = false;
    t.rubric.forEach(r => {
      popRubricChecked[r.code] = false;
      if (typeof rubricChecked !== "undefined") rubricChecked[r.code] = false;
    });
  });
  showPearsonReportModal();
}

// Official Pearson Diagnostic Report Generation (54 Marks: Section A + Section B)
function showPearsonReportModal() {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];

  // 1. Calculate Section A (Computer-Marked Knowledge: 10 Marks)
  let secAScore = 0;
  let secARowsHtml = "";
  set.sectionA.forEach((q, idx) => {
    const testNum = PEARSON_TEST_NUMBERS[idx] || (203114 + idx).toString();
    const ans = popUserAnswers[q.qNum];
    const isSkipped = ans === undefined;
    const isFlagged = !!popFlaggedQuestions[q.qNum];
    const isCorrect = !isSkipped && q.options[ans]?.isCorrect;

    if (isCorrect) secAScore += q.mark;

    secARowsHtml += `
      <tr>
        <td>${testNum} (Q${q.qNum})</td>
        <td style="text-align:left;">${q.title || "Digital Functional Skill"}</td>
        <td>Yes</td>
        <td style="font-weight:700; color:${isCorrect ? "#15803d" : "#b91c1c"};">${isCorrect ? "1" : "0"}</td>
        <td>${isSkipped ? '<span style="color:#d97706; font-weight:700;">Yes</span>' : "—"}</td>
        <td>${isFlagged ? '<span style="color:#f59e0b; font-weight:700;">Yes</span>' : "—"}</td>
      </tr>
    `;
  });

  // 2. Calculate Section B (Practical Tasks & Criteria Rubric: 44 Marks)
  let secBScore = 0;
  let secBRowsHtml = "";
  set.tasks.forEach((t) => {
    let taskScored = 0;
    let criteriaRows = "";

    t.rubric.forEach((r) => {
      const isChecked = !!popRubricChecked[r.code];
      if (isChecked) {
        secBScore += r.mark;
        taskScored += r.mark;
      }
      criteriaRows += `
        <tr style="font-size:0.83rem; background:#fafafa;">
          <td style="text-align:left; padding-left:24px;">
            <label style="cursor:pointer; display:flex; align-items:center; gap:8px;">
              <input type="checkbox" ${isChecked ? "checked" : ""} 
                     onchange="toggleReportRubric('${t.id}', '${r.code}', this.checked)"
                     class="pop-no-print">
              <span><strong>[${r.code}]</strong> ${r.desc}</span>
            </label>
          </td>
          <td>${r.mark}</td>
          <td style="font-weight:700; color:${isChecked ? "#15803d" : "#94a3b8"};">${isChecked ? r.mark : 0}</td>
          <td colspan="2">${isChecked ? '<span style="color:#15803d; font-weight:700;">Awarded</span>' : '<span style="color:#94a3b8;">Pending Evidence</span>'}</td>
        </tr>
      `;
    });

    secBRowsHtml += `
      <tr style="background:#f1f5f9; font-weight:700;">
        <td style="text-align:left;">
          <i class="fa-solid fa-folder-open" style="color:var(--pop-orange); margin-right:6px;"></i>
          ${t.letter}: ${t.title}
        </td>
        <td>${t.marks}</td>
        <td style="color:${taskScored === t.marks ? "#15803d" : "#0284c7"}; font-size:0.95rem;">${taskScored}</td>
        <td colspan="2" style="font-size:0.82rem;">
          <button type="button" class="btn-pop-action pop-no-print" style="padding:2px 8px; font-size:0.75rem;" onclick="awardAllTaskRubric('${t.id}'); showPearsonReportModal();">
            Award Task (${t.marks}m)
          </button>
        </td>
      </tr>
      ${criteriaRows}
    `;
  });

  // 3. Overall Totals & Standard Evaluation
  const totalScore = secAScore + secBScore;
  const grandTotalPossible = set.totalMarks || 54;
  const overallPct = Math.round((totalScore / grandTotalPossible) * 100);
  const passMark = set.passMark || 35;
  const isPass = totalScore >= passMark;

  // 4. Ofqual 5 Core DFS Competency Domains Calculation
  const isQCorrect = (qNum) => {
    const q = set.sectionA.find(item => item.qNum === qNum);
    const ans = popUserAnswers[qNum];
    return (q && ans !== undefined && q.options[ans]?.isCorrect) ? 1 : 0;
  };

  const taskAScore = set.tasks.find(t => t.id === "taskA")?.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0) || 0;
  const taskBScore = set.tasks.find(t => t.id === "taskB")?.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0) || 0;
  const taskCScore = set.tasks.find(t => t.id === "taskC")?.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0) || 0;
  const taskDScore = set.tasks.find(t => t.id === "taskD")?.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0) || 0;
  const taskEScore = set.tasks.find(t => t.id === "taskE")?.rubric.reduce((acc, r) => acc + (popRubricChecked[r.code] ? r.mark : 0), 0) || 0;

  const d1Score = taskEScore + isQCorrect(1) + isQCorrect(4);
  const d1Max = 8;
  const d2Score = taskBScore + taskCScore + isQCorrect(5) + isQCorrect(7);
  const d2Max = 26;
  const d3Score = taskAScore + isQCorrect(2) + isQCorrect(8);
  const d3Max = 9;
  const d4Score = taskDScore + isQCorrect(6);
  const d4Max = 8;
  const d5Score = isQCorrect(3) + isQCorrect(9) + isQCorrect(10);
  const d5Max = 3;

  const domains = [
    { name: "Using Devices & Handling Information", score: d1Score, max: d1Max },
    { name: "Creating & Editing (Word Processing & Spreadsheets)", score: d2Score, max: d2Max },
    { name: "Communicating (Email & Information Search)", score: d3Score, max: d3Max },
    { name: "Transacting (Digital Portals & Web Form Submissions)", score: d4Score, max: d4Max },
    { name: "Being Safe & Responsible Online (Cybersecurity & Health)", score: d5Score, max: d5Max }
  ];

  const modalBody = document.getElementById("popReportModalBody");
  if (modalBody) {
    modalBody.innerHTML = `
      <div class="pop-report-header">
        <div>
          <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em; color:#64748b; font-weight:700;">Pearson Onscreen Platform (POP) Assessment Standard</div>
          <h2 style="margin:2px 0 4px 0; font-size:1.35rem; color:#0f172a;">Diagnostic Assessment & Marking Report</h2>
          <div style="font-size:0.92rem; color:#334155;"><strong>${set.level}:</strong> ${set.name}</div>
        </div>
        <button type="button" onclick="closePearsonReportModal()" class="pop-no-print" style="background:none; border:none; font-size:1.6rem; cursor:pointer; color:#64748b;">✕</button>
      </div>

      <!-- Candidate Metadata Table -->
      <table class="pop-report-table" style="margin-top:0;">
        <tr>
          <td style="width:220px;"><strong>Candidate Name:</strong></td>
          <td style="text-align:left;">
            <input type="text" value="${popCandidateName}" onchange="popCandidateName = this.value" style="width:100%; border:none; font-weight:bold; font-size:0.95rem; background:transparent;">
          </td>
          <td style="width:160px;"><strong>Total Available:</strong></td>
          <td style="font-weight:700; width:120px;">${grandTotalPossible} Marks</td>
        </tr>
        <tr>
          <td><strong>Assessment Centre:</strong></td>
          <td style="text-align:left;">Master Functional Skills (Accredited Centre Standard)</td>
          <td><strong>Pass Benchmark:</strong></td>
          <td style="font-weight:700; color:#0284c7;">${passMark} Marks (~65%)</td>
        </tr>
      </table>

      <!-- Overall Result Banner -->
      <div class="pop-result-banner ${isPass ? "pass" : "fail"}">
        <div class="pop-result-banner-title">
          <i class="fa-solid ${isPass ? "fa-circle-check" : "fa-triangle-exclamation"}"></i>
          ${isPass ? "OVERALL ASSESSMENT RESULT: PASS STANDARD (ACHIEVED)" : "OVERALL ASSESSMENT RESULT: WORKING TOWARDS PASS (REVISION REQUIRED)"}
        </div>
        <div class="pop-result-banner-meta">
          Overall Achieved: <strong>${totalScore} / ${grandTotalPossible} Marks (${overallPct}%)</strong> • Pearson Level 1 Pass Threshold: <strong>${passMark} / ${grandTotalPossible} Marks</strong>
        </div>
      </div>

      <!-- Summary Stat Cards -->
      <div class="pop-stat-grid">
        <div class="pop-stat-card">
          <div class="pop-stat-num" style="color:${isPass ? "#16a34a" : "#dc2626"};">${totalScore} / ${grandTotalPossible}</div>
          <div class="pop-stat-label">Total Marks (${overallPct}%)</div>
        </div>
        <div class="pop-stat-card">
          <div class="pop-stat-num" style="color:#0284c7;">${secAScore} / 10</div>
          <div class="pop-stat-label">Section A (Knowledge)</div>
        </div>
        <div class="pop-stat-card">
          <div class="pop-stat-num" style="color:#059669;">${secBScore} / 44</div>
          <div class="pop-stat-label">Section B (Practical)</div>
        </div>
        <div class="pop-stat-card">
          <div class="pop-stat-num" style="color:#475569;">${passMark} / 54</div>
          <div class="pop-stat-label">Pass Standard (65%)</div>
        </div>
      </div>

      <!-- Section A Breakdown Table -->
      <h3 style="margin:20px 0 8px 0; font-size:1.08rem; color:#0f172a; display:flex; justify-content:space-between; align-items:center;">
        <span><i class="fa-solid fa-list-ol" style="color:var(--pop-orange);"></i> Section A: Knowledge & Understanding (Computer Markable)</span>
        <span style="font-size:0.95rem; font-weight:700; color:#0284c7;">Score: ${secAScore} / 10 Marks</span>
      </h3>
      <table class="pop-report-table">
        <thead>
          <tr>
            <th style="width:160px;">Test Number</th>
            <th>Digital Competency Focus</th>
            <th style="width:140px;">Computer Markable</th>
            <th style="width:110px;">Marks Awarded</th>
            <th style="width:80px;">Skipped</th>
            <th style="width:80px;">Flagged</th>
          </tr>
        </thead>
        <tbody>
          ${secARowsHtml}
          <tr style="background:#f1f5f9; font-weight:800; font-size:0.95rem;">
            <td colspan="3" style="text-align:right;">Section A Subtotal:</td>
            <td style="color:${secAScore >= 7 ? "#16a34a" : "#dc2626"};">${secAScore} / 10</td>
            <td colspan="2">${Math.round((secAScore / 10) * 100)}%</td>
          </tr>
        </tbody>
      </table>

      <!-- Section B Breakdown Table -->
      <div style="display:flex; justify-content:space-between; align-items:center; margin:24px 0 8px 0; flex-wrap:wrap; gap:8px;">
        <h3 style="margin:0; font-size:1.08rem; color:#0f172a;">
          <i class="fa-solid fa-laptop-code" style="color:var(--pop-orange);"></i> Section B: Practical Application & Evidence Tasks (44 Marks)
        </h3>
        <div class="pop-no-print" style="display:flex; gap:8px;">
          <button type="button" class="btn-pop-action" onclick="awardAllSectionBEvidence()" style="padding:4px 10px; font-size:0.8rem; background:#ecfdf5; color:#047857; border-color:#a7f3d0;">
            <i class="fa-solid fa-check-double"></i> Award All Section B Evidence (44/44)
          </button>
          <button type="button" class="btn-pop-action" onclick="clearAllSectionBEvidence()" style="padding:4px 10px; font-size:0.8rem;">
            <i class="fa-solid fa-arrow-rotate-left"></i> Reset
          </button>
        </div>
      </div>

      <div style="font-size:0.85rem; color:#64748b; margin-bottom:8px;">
        <em>Examiner Guidance: Individual mark scheme criteria can be toggled below to reflect candidate evidence documents and simulator outputs.</em>
      </div>

      <table class="pop-report-table">
        <thead>
          <tr>
            <th>Task & Assessment Criteria Rubric</th>
            <th style="width:80px;">Available</th>
            <th style="width:90px;">Awarded</th>
            <th colspan="2" style="width:140px;">Evidence Status</th>
          </tr>
        </thead>
        <tbody>
          ${secBRowsHtml}
          <tr style="background:#f1f5f9; font-weight:800; font-size:0.95rem;">
            <td style="text-align:right;">Section B Subtotal:</td>
            <td>44</td>
            <td style="color:${secBScore >= 28 ? "#16a34a" : "#dc2626"};">${secBScore}</td>
            <td colspan="2">${Math.round((secBScore / 44) * 100)}%</td>
          </tr>
        </tbody>
      </table>

      <!-- Ofqual 5 Competency Domains -->
      <h3 style="margin:24px 0 12px 0; font-size:1.08rem; color:#0f172a;">
        <i class="fa-solid fa-chart-simple" style="color:var(--pop-orange);"></i> Ofqual Digital Functional Skills Competency Domain Breakdown:
      </h3>
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px; margin-bottom:20px;">
        ${domains.map(d => {
          const pct = Math.round((d.score / d.max) * 100);
          const color = pct >= 70 ? "#16a34a" : (pct >= 50 ? "#0284c7" : "#d97706");
          return `
            <div class="pop-domain-row">
              <div class="pop-domain-meta">
                <span>${d.name}</span>
                <span style="color:${color}; font-weight:700;">${d.score} / ${d.max} Marks (${pct}%)</span>
              </div>
              <div class="pop-domain-track">
                <div class="pop-domain-fill" style="width:${pct}%; background:${color};"></div>
              </div>
            </div>
          `;
        }).join("")}
      </div>

      <!-- Tutor & Quality Assurance Sign-off -->
      <div style="background:#ffffff; border:1px dashed #94a3b8; border-radius:6px; padding:12px 16px; font-size:0.85rem; line-height:1.6; margin-bottom:20px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div>
          <strong>Tutor Assessor:</strong> Abdul (Master Functional Skills)<br>
          <strong>Internal Quality Assurance:</strong> Verified against Pearson Edexcel DFS L1 Criteria
        </div>
        <div>
          <strong>Report Timestamp:</strong> ${new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })}<br>
          <strong>Assessment Method:</strong> Onscreen Simulation + Practical Candidate Evidence
        </div>
      </div>

      <!-- Actions Toolbar -->
      <div style="display:flex; justify-content:center; gap:12px; margin-top:20px;" class="pop-no-print">
        <button type="button" class="btn-pearson-start" onclick="window.print()"><i class="fa-solid fa-print"></i> Print Official Report (PDF)</button>
        <button type="button" class="btn-pop-action" onclick="closePearsonReportModal()">Close</button>
      </div>
    `;
  }

  const modal = document.getElementById("popReportModal");
  if (modal) modal.classList.add("active");
}

function closePearsonReportModal() {
  const modal = document.getElementById("popReportModal");
  if (modal) modal.classList.remove("active");
}
