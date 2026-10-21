/**
 * Master Functional Skills - Authentic Pearson Onscreen Test Player App Engine
 * Replicates the official Pearson Onscreen Platform (POP) screen-by-screen environment.
 */

let popCurrentScreen = 0;
let popTotalScreens = 20;
let popUserAnswers = {}; // { qNum: optionIdx }
let popFlaggedQuestions = {}; // { qNum: boolean }
let popTaskEvidence = {}; // { taskCode: boolean }
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

    canvas.innerHTML = `
      <div style="max-width:920px; margin:0 auto; width:100%;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h2 style="margin:0; font-size:1.35rem; color:#111111;">${task.letter}: ${task.title}</h2>
          <span style="font-size:1.05rem; font-weight:700; color:#333333;">(${task.marks} Marks)</span>
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

        <div class="pearson-evidence-check">
          <label style="cursor:pointer; display:flex; align-items:center; gap:10px;">
            <input type="checkbox" id="evCheck_${task.id}" 
                   ${popTaskEvidence[task.id] ? "checked" : ""} 
                   onchange="popTaskEvidence['${task.id}'] = this.checked">
            <span>Evidence: I have completed and verified my output for ${task.letter}</span>
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
    canvas.innerHTML = `
      <div class="pearson-summary-wrap">
        <div class="pearson-summary-title">Section B Summary</div>
        <div class="pearson-summary-subtitle">You have completed all assessment tasks. Generate your official report below.</div>

        <div style="background:#ffffff; border:1px solid #bfbfbf; border-radius:6px; padding:20px; max-width:680px; margin:20px auto;">
          <h4 style="margin:0 0 12px 0;"><i class="fa-solid fa-clipboard-check" style="color:var(--pop-orange);"></i> Practical Task Evidence Checklist:</h4>
          ${set.tasks.map(t => `
            <div style="display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #f1f5f9; font-size:0.95rem;">
              <span><strong>${t.letter}:</strong> ${t.title}</span>
              <span style="font-weight:700; color:${popTaskEvidence[t.id] ? "#16a34a" : "#d97706"};">
                ${popTaskEvidence[t.id] ? "✔ Evidence Recorded" : "⚠ Review Task"}
              </span>
            </div>
          `).join("")}
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

// Official Pearson Diagnostic Report Generation
function showPearsonReportModal() {
  const set = DFS_MOCK_DATA[popCurrentSetKey] || DFS_MOCK_DATA["set1"];
  let scoreObtained = 0;

  let rowsHtml = "";
  set.sectionA.forEach((q, idx) => {
    const testNum = PEARSON_TEST_NUMBERS[idx] || (203114 + idx).toString();
    const ans = popUserAnswers[q.qNum];
    const isSkipped = ans === undefined;
    const isFlagged = !!popFlaggedQuestions[q.qNum];
    const isCorrect = !isSkipped && q.options[ans].isCorrect;

    if (isCorrect) scoreObtained += 1;

    rowsHtml += `
      <tr>
        <td>${testNum} (Q${q.qNum})</td>
        <td>Yes</td>
        <td style="font-weight:700; color:${isCorrect ? "#15803d" : "#b91c1c"};">${isCorrect ? "1" : "0"}</td>
        <td>${isSkipped ? "Yes" : ""}</td>
        <td>${isFlagged ? "Yes" : ""}</td>
      </tr>
    `;
  });

  const totalPossible = 10;
  const pct = Math.round((scoreObtained / totalPossible) * 100);

  const modalBody = document.getElementById("popReportModalBody");
  if (modalBody) {
    modalBody.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <h3 style="margin:0; font-size:1.3rem;">Pearson Onscreen Platform — Diagnostic Score Report</h3>
        <button type="button" onclick="closePearsonReportModal()" style="background:none; border:none; font-size:1.4rem; cursor:pointer;">✕</button>
      </div>

      <table class="pop-report-table">
        <tr>
          <td style="width:200px;"><strong>Candidate name</strong></td>
          <td colspan="4" style="text-align:left;">
            <input type="text" value="${popCandidateName}" onchange="popCandidateName = this.value" style="width:100%; border:none; font-weight:bold; font-size:0.95rem;">
          </td>
        </tr>
        <tr>
          <th>Test Number</th>
          <th>Computer Markable</th>
          <th>Marks Obtained</th>
          <th>Skipped</th>
          <th>Flagged</th>
        </tr>
        ${rowsHtml}
        <tr style="background:#f2f2f2; font-weight:700;">
          <td colspan="2" style="text-align:right;">Section A Total:</td>
          <td>${scoreObtained} / 10</td>
          <td colspan="2"></td>
        </tr>
        <tr style="background:#f2f2f2; font-weight:700;">
          <td colspan="2" style="text-align:right;">Section A Percentage:</td>
          <td>${pct}%</td>
          <td colspan="2">${scoreObtained >= 7 ? "PASS STANDARD" : "REVISION REQUIRED"}</td>
        </tr>
      </table>

      <div style="background:#f9f9f9; border:1px solid #e0e0e0; padding:12px; font-size:0.85rem; line-height:1.5; margin-top:12px;">
        <strong>Examiner Guidance:</strong> Test Numbers 203114–203123 form Section A (computer markable). Section B practical files must be assessed against Pearson criteria rubric checklists.
      </div>

      <div style="display:flex; justify-content:center; gap:12px; margin-top:20px;">
        <button type="button" class="btn-pearson-start" onclick="window.print()"><i class="fa-solid fa-print"></i> Print Official Report</button>
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
