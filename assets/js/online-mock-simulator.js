/**
 * Master Functional Skills - Online Mock Exam Simulator Engine
 * Provides authentic onscreen mock examination simulation with dedicated
 * typed working areas, mathematical symbol helpers, calculator, and model solution comparison.
 */

// Global State
let simCurrentPaperKey = 'edexcel-maths-l1-paper-1';
let simCurrentQuestionIndex = 0;
let simTimerSeconds = 25 * 60; // default 25 mins for Sec A
let simTimerActive = true;
let simTimerInterval = null;
let simIsPdfView = false;

// Mock Papers Dataset (Reformed Pearson Edexcel Level 1 & Level 2 Authentic Sets)
const MFS_MOCK_DATA = {
  'edexcel-maths-l1-paper-1': {
    title: 'Edexcel Functional Skills Maths Level 1 — Past Paper 1',
    board: 'Pearson Edexcel',
    subject: 'Mathematics',
    level: 'Level 1',
    paperNumber: 1,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/01/FS-Maths-Level-1-Past-Paper-1.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-1/FS_Maths_Level_1_Past_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: '',
    durationMinutes: 105,
    questions: [
      {
        num: 1,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 3,
        markTags: '[M1, A1, B1]',
        scenarioTitle: 'Healthcare Facility Logistics: Cold Storage Monitoring',
        scenarioText: 'A healthcare logistics coordinator monitors clinical freezers for temperature-sensitive medications. At 07:00, the temperature in Freezer A is -18 °C. During morning inventory maintenance, the temperature rises by 5 °C. Later, cooling is boosted, dropping the temperature by a further 4 °C.',
        promptText: '(a) Work out the temperature after the 5 °C rise.\n(b) Work out the final temperature after the 4 °C drop.\n(c) A standard vaccine fridge is kept at +4 °C. Calculate the difference between +4 °C and the original -18 °C.',
        unit: '°C',
        defaultAnswer: '',
        modelSolution: 'Step 1: -18 + 5 = -13 °C [A1]\nStep 2: -13 - 4 = -17 °C [A1]\nStep 3: Distance from -18 to 0 is 18, and 0 to +4 is 4. Difference = 18 + 4 = 22 °C [B1]',
        finalBenchmark: '22 °C'
      },
      {
        num: 2,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[M1, A1]',
        scenarioTitle: 'Departmental Budgeting: Translating Word Numbers',
        scenarioText: 'The clinical trust approves an annual pharmaceutical logistics expenditure of "four hundred and five thousand, and twelve pounds and fifty pence".',
        promptText: 'Write this total budget amount in figures. Remember to check your zero placeholders carefully.',
        unit: '£',
        defaultAnswer: '',
        modelSolution: 'Breakdown:\nFour hundred and five thousand = 405,000\nTwelve pounds and fifty pence = 12.50\nTotal in figures = £405,012.50 [A1, M1 for zero in hundreds/tens-of-thousands]',
        finalBenchmark: '£405,012.50'
      },
      {
        num: 3,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 3,
        markTags: '[M1, M1, A1]',
        scenarioTitle: 'Community Health Nurse: Mileage & Route Addition',
        scenarioText: 'A community nurse departs from base to visit three patients before returning to the health centre. She drives 12.4 km to Patient A, 8.75 km to Patient B, and 15.5 km back to the health centre.',
        promptText: '(a) Show your vertical column working with decimals aligned to calculate the total journey distance.\n(b) If her travel allowance pays £0.45 per kilometre, calculate her total claim rounded to the nearest penny.',
        unit: '£',
        defaultAnswer: '',
        modelSolution: 'Step 1: Align decimal points:\n  12.40\n+  8.75\n+ 15.50\n= 36.65 km [M1 for vertical layout, A1 for 36.65 km]\nStep 2: Travel allowance = 36.65 × 0.45 = £16.4925 --> £16.49 [A1]',
        finalBenchmark: '£16.49'
      },
      {
        num: 4,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 2,
        markTags: '[M1, A1]',
        scenarioTitle: 'Pharmacy Stock Ratio: Diluting Antiseptic Solution',
        scenarioText: 'A pharmacy assistant must prepare 600 ml of cleaning fluid by diluting concentrated antiseptic with sterile water in the ratio 1 : 5.',
        promptText: 'How much sterile water does the assistant need? Show your step-by-step working below.',
        unit: 'ml',
        defaultAnswer: '',
        modelSolution: 'Step 1: Total parts = 1 + 5 = 6 parts [M1]\nStep 2: Value of 1 part = 600 ÷ 6 = 100 ml\nStep 3: Sterile water (5 parts) = 5 × 100 = 500 ml [A1]',
        finalBenchmark: '500 ml'
      },
      {
        num: 5,
        section: 'Section B: Calculator Allowed',
        isCalcAllowed: true,
        marks: 4,
        markTags: '[M2, A1, B1]',
        scenarioTitle: 'Clinical Clinic Refurbishment: Flooring & Scale Grids',
        scenarioText: 'An estates manager is ordering non-slip vinyl flooring for a treatment room measuring 6.5 metres long by 4.2 metres wide. Vinyl flooring costs £18.50 per square metre. The installer advises adding 10% extra area to allow for cutting and trimming.',
        promptText: '(a) Calculate the total area of the floor.\n(b) Calculate the total area needed including the 10% cutting waste.\n(c) Calculate the total cost of the flooring.',
        unit: '£',
        defaultAnswer: '',
        modelSolution: 'Step 1: Area = 6.5 × 4.2 = 27.3 m² [M1]\nStep 2: Waste (10%) = 0.10 × 27.3 = 2.73 m²\nTotal area required = 27.3 + 2.73 = 30.03 m² [M1]\nStep 3: Total Cost = 30.03 × £18.50 = £555.555 --> £555.56 [A1]',
        finalBenchmark: '£555.56'
      },
      {
        num: 6,
        section: 'Section B: Calculator Allowed',
        isCalcAllowed: true,
        marks: 3,
        markTags: '[M1, A1, B1]',
        scenarioTitle: 'Patient Waiting Times: Range and Mean Comparison',
        scenarioText: 'A medical centre records the consultation waiting times (in minutes) for 8 patients on Monday: 14, 22, 18, 9, 31, 25, 16, 21. On Friday, the mean waiting time was 18 minutes and the range was 15 minutes.',
        promptText: '(a) Work out the mean waiting time for Monday.\n(b) Compare the waiting times between Monday and Friday using your calculations.',
        unit: 'minutes',
        defaultAnswer: '',
        modelSolution: 'Step 1: Sum for Monday = 14 + 22 + 18 + 9 + 31 + 25 + 16 + 21 = 156 minutes [M1]\nStep 2: Mean Monday = 156 ÷ 8 = 19.5 minutes [A1]\nStep 3: Range Monday = 31 - 9 = 22 minutes\nComparison: Friday had a shorter average waiting time (18 mins vs 19.5 mins) and more consistent times (range 15 mins vs 22 mins) [B1]',
        finalBenchmark: '19.5 minutes'
      }
    ]
  },
  'edexcel-maths-l2-paper-1': {
    title: 'Edexcel Functional Skills Maths Level 2 — Past Paper 1',
    board: 'Pearson Edexcel',
    subject: 'Mathematics',
    level: 'Level 2',
    paperNumber: 1,
    pdfUrl: 'https://passfunctionalskills.co.uk/app/uploads/2024/01/Edexcel-Functional-Skills-Maths-Level-2-Past-Paper-1-QP.pdf',
    modelSolutionPdf: 'assets/downloads/past-papers/edexcel/maths-level-2/FS_Maths_Level_2_Past_Paper_1_Model_Solution_MFS.pdf',
    videoSolutionSlug: 'edexcel-maths-l2-past-paper-1-section-a',
    durationMinutes: 110,
    questions: [
      {
        num: 1,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 3,
        markTags: '[M1, M1, A1]',
        scenarioTitle: 'Medical Diagnostics Facility: High-Precision Dilutions',
        scenarioText: 'A laboratory technician must prepare a chemical disinfectant by mixing concentrate, saline solution, and purified water in the ratio 2 : 5 : 8. The total volume required for the shift is 4.5 litres.',
        promptText: 'Calculate how many millilitres of saline solution are required. Show your multi-step working below.',
        unit: 'ml',
        defaultAnswer: '',
        modelSolution: 'Step 1: Total parts = 2 + 5 + 8 = 15 parts [M1]\nStep 2: Total volume in ml = 4.5 × 1000 = 4,500 ml\nValue of 1 part = 4,500 ÷ 15 = 300 ml [M1]\nStep 3: Saline solution (5 parts) = 5 × 300 = 1,500 ml [A1]',
        finalBenchmark: '1,500 ml'
      },
      {
        num: 2,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 4,
        markTags: '[M2, A1, B1]',
        scenarioTitle: 'Logistics Depot Scheduling: Delivery Van Routing',
        scenarioText: 'A logistics distribution van leaves the central depot at 08:35 to make three community clinic deliveries. Driving time is 45 minutes, clinic unload takes 25 minutes, second leg takes 35 minutes, second unload takes 20 minutes, and return leg takes 50 minutes.',
        promptText: '(a) Work out the total time taken for the full run in hours and minutes.\n(b) What time does the van return to the central depot?',
        unit: 'time',
        defaultAnswer: '',
        modelSolution: 'Step 1: Total minutes = 45 + 25 + 35 + 20 + 50 = 175 minutes [M1]\nStep 2: Convert to hours: 175 ÷ 60 = 2 hours and 55 minutes [M1]\nStep 3: Return time = 08:35 + 2h 55m = 11:30 [A1]',
        finalBenchmark: '11:30'
      },
      {
        num: 3,
        section: 'Section B: Calculator Allowed',
        isCalcAllowed: true,
        marks: 5,
        markTags: '[M2, A2, B1]',
        scenarioTitle: 'Estates Maintenance: Cylindrical Water Tank & Volume',
        scenarioText: 'An estates maintenance engineer needs to treat a cylindrical backup rainwater tank. The tank has an internal radius of 1.4 metres and a depth of 2.5 metres. The chemical treatment requires 75 grams of powder per cubic metre of water. (Use formula: Volume = πr²h, where π = 3.142).',
        promptText: '(a) Calculate the internal volume of the cylinder in m³ to 2 decimal places.\n(b) Calculate the total mass of powder needed in kilograms.',
        unit: 'kg',
        defaultAnswer: '',
        modelSolution: 'Step 1: Volume = π × r² × h = 3.142 × 1.4² × 2.5\n= 3.142 × 1.96 × 2.5 = 15.3958 m³ [M1, A1]\nStep 2: Total powder in grams = 15.3958 × 75 = 1,154.685 g [M1]\nStep 3: Convert to kilograms = 1,154.685 ÷ 1000 = 1.15 kg (rounded to 2 d.p.) [A1]',
        finalBenchmark: '1.15 kg'
      }
    ]
  }
};

// Generate Fallback Generic Mock for any requested paper
function getOrCreatePaper(paperKey) {
  if (MFS_MOCK_DATA[paperKey]) {
    return MFS_MOCK_DATA[paperKey];
  }
  
  // Format readable title from paperKey
  const parts = paperKey.split('-');
  const board = parts[0] ? parts[0].toUpperCase() : 'EDEXCEL';
  const subj = parts[1] ? parts[1].charAt(0).toUpperCase() + parts[1].slice(1) : 'Maths';
  const level = parts[2] ? parts[2].toUpperCase() : 'L1';
  const pNum = parts.find(p => !isNaN(p)) || '1';

  return {
    title: `${board} Functional Skills ${subj} ${level} — Paper ${pNum}`,
    board: board,
    subject: subj,
    level: level,
    paperNumber: parseInt(pNum, 10),
    pdfUrl: '',
    modelSolutionPdf: '',
    videoSolutionSlug: '',
    durationMinutes: 90,
    questions: [
      {
        num: 1,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 3,
        markTags: '[M1, A1, B1]',
        scenarioTitle: `Authentic Exam Task: Question 1`,
        scenarioText: `Review Question 1 from the official ${board} ${level} ${subj} Question Paper. Use the working space below to show all your calculation steps and reasoning clearly.`,
        promptText: 'Type your method and intermediate calculation steps into the space below. Enter your final answer with correct units in the box.',
        unit: 'units',
        defaultAnswer: '',
        modelSolution: 'Review the official Master Functional Skills Model Solution PDF for complete step-by-step guidance.',
        finalBenchmark: 'Refer to Model Solution'
      },
      {
        num: 2,
        section: 'Section A: Non-Calculator',
        isCalcAllowed: false,
        marks: 4,
        markTags: '[M2, A1, B1]',
        scenarioTitle: `Authentic Exam Task: Question 2`,
        scenarioText: `Review Question 2 from the official ${board} ${level} ${subj} Question Paper. Type your calculations below.`,
        promptText: 'Show all calculation steps and state your final answer.',
        unit: 'units',
        defaultAnswer: '',
        modelSolution: 'Review the official Master Functional Skills Model Solution PDF for complete step-by-step guidance.',
        finalBenchmark: 'Refer to Model Solution'
      },
      {
        num: 3,
        section: 'Section B: Calculator Allowed',
        isCalcAllowed: true,
        marks: 5,
        markTags: '[M2, A2, B1]',
        scenarioTitle: `Authentic Exam Task: Question 3 (Calculator)`,
        scenarioText: `Review Question 3 from the official ${board} ${level} ${subj} Question Paper. The onscreen calculator is enabled for this section.`,
        promptText: 'Work out the problem and record your full calculation steps.',
        unit: 'units',
        defaultAnswer: '',
        modelSolution: 'Review the official Master Functional Skills Model Solution PDF for complete step-by-step guidance.',
        finalBenchmark: 'Refer to Model Solution'
      }
    ]
  };
}

// Initialise Simulator on Page Load
document.addEventListener('DOMContentLoaded', () => {
  initSimulator();
});

function initSimulator() {
  const urlParams = new URLSearchParams(window.location.search);
  const requestedPaper = urlParams.get('paper') || urlParams.get('id');
  const requestedBoard = urlParams.get('board');
  const requestedSubject = urlParams.get('subject');
  const requestedLevel = urlParams.get('level');
  const requestedNum = urlParams.get('num') || urlParams.get('p');
  const requestedQp = urlParams.get('qp');
  const requestedTitle = urlParams.get('title');

  let key = 'edexcel-maths-l1-paper-1';
  if (requestedPaper) {
    key = requestedPaper;
  } else if (requestedBoard && requestedSubject && requestedLevel) {
    key = `${requestedBoard}-${requestedSubject}-${requestedLevel}-paper-${requestedNum || 1}`;
  }

  simCurrentPaperKey = key;
  const paper = getOrCreatePaper(key);
  if (requestedQp) paper.pdfUrl = requestedQp;
  if (requestedTitle) paper.title = requestedTitle;

  // Set selector value
  const dropdown = document.getElementById('simPaperSelector');
  if (dropdown) {
    dropdown.value = key;
  }

  // Set Title and Meta
  document.getElementById('simPaperTitleDisplay').innerText = paper.title;

  // Timer setup
  simTimerSeconds = paper.durationMinutes * 60;
  startSimTimer();

  // Render question 0
  renderQuestion(0);
}

function handlePaperChange(newKey) {
  simCurrentPaperKey = newKey;
  simCurrentQuestionIndex = 0;
  const paper = getOrCreatePaper(newKey);
  document.getElementById('simPaperTitleDisplay').innerText = paper.title;
  simTimerSeconds = paper.durationMinutes * 60;
  renderQuestion(0);
}

function renderQuestion(qIdx) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const questions = paper.questions;
  if (qIdx < 0 || qIdx >= questions.length) return;

  simCurrentQuestionIndex = qIdx;
  const q = questions[qIdx];

  // Update Meta Bar
  document.getElementById('simQNumBadge').innerText = `Question ${q.num} of ${questions.length}`;
  document.getElementById('simQSectionTag').innerText = q.section;
  document.getElementById('simQMarksBadge').innerText = `${q.marks} Marks • ${q.markTags}`;

  // Update Scenario & Prompt
  document.getElementById('simScenarioTitle').innerHTML = `<i class="fa-solid fa-file-circle-check" style="color:var(--sim-blue);"></i> ${q.scenarioTitle}`;
  document.getElementById('simScenarioText').innerText = q.scenarioText;
  document.getElementById('simPromptText').innerText = q.promptText;

  // Update Working Space
  const storageKeyWorking = `mfs_sim_${simCurrentPaperKey}_q${q.num}_working`;
  const storageKeyAnswer = `mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`;
  const storageKeyFlag = `mfs_sim_${simCurrentPaperKey}_q${q.num}_flag`;

  const savedWorking = localStorage.getItem(storageKeyWorking) || '';
  const savedAns = localStorage.getItem(storageKeyAnswer) || '';
  const isFlagged = localStorage.getItem(storageKeyFlag) === 'true';

  const workingArea = document.getElementById('simWorkingTextarea');
  workingArea.value = savedWorking;
  workingArea.placeholder = `Type your working here for Question ${q.num}...\nExample:\nStep 1: State the formula or method\nStep 2: Carry out calculations\nStep 3: State final value with units`;

  const ansInput = document.getElementById('simFinalInput');
  ansInput.value = savedAns;
  document.getElementById('simUnitBadge').innerText = q.unit;

  // Flag Button
  const flagBtn = document.getElementById('simFlagBtn');
  if (isFlagged) {
    flagBtn.classList.add('flagged');
    flagBtn.innerHTML = '<i class="fa-solid fa-flag"></i> Flagged';
  } else {
    flagBtn.classList.remove('flagged');
    flagBtn.innerHTML = '<i class="fa-regular fa-flag"></i> Flag Question';
  }

  // Calculator State (Section A locked vs Section B enabled)
  const calcDrawer = document.getElementById('simCalcDrawer');
  const calcLockedBanner = document.getElementById('simCalcLockedBanner');
  if (q.isCalcAllowed) {
    calcDrawer.style.display = 'flex';
    calcLockedBanner.style.display = 'none';
  } else {
    calcDrawer.style.display = 'none';
    calcLockedBanner.style.display = 'flex';
  }

  // Update Navigation Buttons
  document.getElementById('simPrevBtn').disabled = (qIdx === 0);
  const nextBtn = document.getElementById('simNextBtn');
  if (qIdx === questions.length - 1) {
    nextBtn.innerHTML = 'Review Mock <i class="fa-solid fa-clipboard-check"></i>';
    nextBtn.onclick = () => openSubmitModal();
  } else {
    nextBtn.innerHTML = 'Next Question <i class="fa-solid fa-chevron-right"></i>';
    nextBtn.onclick = () => renderQuestion(simCurrentQuestionIndex + 1);
  }

  renderQuestionPills();
}

function renderQuestionPills() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const pillsContainer = document.getElementById('simPillsContainer');
  pillsContainer.innerHTML = '';

  paper.questions.forEach((q, idx) => {
    const pill = document.createElement('button');
    pill.type = 'button';
    pill.className = 'sim-q-pill';
    pill.innerText = q.num;

    const storageKeyWorking = `mfs_sim_${simCurrentPaperKey}_q${q.num}_working`;
    const storageKeyAns = `mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`;
    const storageKeyFlag = `mfs_sim_${simCurrentPaperKey}_q${q.num}_flag`;

    const hasWorking = localStorage.getItem(storageKeyWorking);
    const hasAns = localStorage.getItem(storageKeyAns);
    const isFlagged = localStorage.getItem(storageKeyFlag) === 'true';

    if (idx === simCurrentQuestionIndex) {
      pill.classList.add('active');
    } else if (hasWorking || hasAns) {
      pill.classList.add('answered');
    }
    if (isFlagged) {
      pill.classList.add('flagged');
    }

    pill.onclick = () => renderQuestion(idx);
    pillsContainer.appendChild(pill);
  });
}

// Auto-save handlers
function handleWorkingInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_working`, val);
  triggerSaveStatus();
  renderQuestionPills();
}

function handleAnswerInput(val) {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  localStorage.setItem(`mfs_sim_${simCurrentPaperKey}_q${qNum}_ans`, val);
  triggerSaveStatus();
  renderQuestionPills();
}

function triggerSaveStatus() {
  const statusEl = document.getElementById('simSaveStatus');
  if (statusEl) {
    statusEl.innerHTML = '<i class="fa-solid fa-check"></i> Saved';
    setTimeout(() => {
      statusEl.innerHTML = '<i class="fa-solid fa-circle" style="font-size:0.5rem; color:#86efac;"></i> Autosaved';
    }, 1500);
  }
}

// Math Symbol Inserters
function insertSymbol(sym) {
  const textarea = document.getElementById('simWorkingTextarea');
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  const text = textarea.value;
  textarea.value = text.substring(0, start) + sym + text.substring(end);
  textarea.selectionStart = textarea.selectionEnd = start + sym.length;
  textarea.focus();
  handleWorkingInput(textarea.value);
}

function insertPlaceValueGrid() {
  const template = '\n[M:  ]  [HTh:  ]  [TTh:  ]  [Th:  ]  [H:  ]  [T:  ]  [U:  ]\n';
  insertSymbol(template);
}

function insertFractionTemplate() {
  const template = ' [Numerator] / [Denominator] ';
  insertSymbol(template);
}

function clearWorkingSpace() {
  if (confirm('Are you sure you want to clear your typed working for this question?')) {
    const textarea = document.getElementById('simWorkingTextarea');
    textarea.value = '';
    handleWorkingInput('');
  }
}

// Flagging
function toggleFlag() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const qNum = paper.questions[simCurrentQuestionIndex].num;
  const key = `mfs_sim_${simCurrentPaperKey}_q${qNum}_flag`;
  const isFlagged = localStorage.getItem(key) === 'true';
  localStorage.setItem(key, !isFlagged);
  renderQuestion(simCurrentQuestionIndex);
}

// Timer Controls
function startSimTimer() {
  if (simTimerInterval) clearInterval(simTimerInterval);
  simTimerInterval = setInterval(() => {
    if (!simTimerActive) return;
    if (simTimerSeconds > 0) {
      simTimerSeconds--;
      updateTimerDisplay();
    } else {
      clearInterval(simTimerInterval);
      alert('Time is up for this section! Please review and submit your mock.');
      openSubmitModal();
    }
  }, 1000);
  updateTimerDisplay();
}

function updateTimerDisplay() {
  const mins = Math.floor(simTimerSeconds / 60);
  const secs = simTimerSeconds % 60;
  const display = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  const el = document.getElementById('simTimerDisplay');
  if (el) el.innerText = display;

  const box = document.getElementById('simTimerBox');
  if (box) {
    if (simTimerSeconds <= 300) {
      box.classList.add('warning');
    } else {
      box.classList.remove('warning');
    }
  }
}

function toggleTimerPause() {
  simTimerActive = !simTimerActive;
  const icon = document.getElementById('simTimerPauseIcon');
  if (icon) {
    icon.className = simTimerActive ? 'fa-solid fa-pause' : 'fa-solid fa-play';
  }
}

// Fullscreen Toggle
function toggleSimFullscreen() {
  const shell = document.getElementById('simAppShell');
  if (!document.fullscreenElement) {
    if (shell.requestFullscreen) {
      shell.requestFullscreen();
    } else if (shell.webkitRequestFullscreen) {
      shell.webkitRequestFullscreen();
    }
    shell.classList.add('fullscreen');
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
    shell.classList.remove('fullscreen');
  }
}

// Built-in Calculator
let calcCurrentVal = '0';
let calcMemory = 0;
let calcPendingOp = null;
let calcWaitingForOperand = false;

function calcDigit(digit) {
  const screen = document.getElementById('simCalcScreen');
  if (calcWaitingForOperand) {
    calcCurrentVal = String(digit);
    calcWaitingForOperand = false;
  } else {
    calcCurrentVal = calcCurrentVal === '0' ? String(digit) : calcCurrentVal + digit;
  }
  screen.innerText = calcCurrentVal;
}

function calcDecimal() {
  const screen = document.getElementById('simCalcScreen');
  if (calcWaitingForOperand) {
    calcCurrentVal = '0.';
    calcWaitingForOperand = false;
  } else if (!calcCurrentVal.includes('.')) {
    calcCurrentVal += '.';
  }
  screen.innerText = calcCurrentVal;
}

function calcOp(op) {
  const screen = document.getElementById('simCalcScreen');
  const inputVal = parseFloat(calcCurrentVal);

  if (calcPendingOp && !calcWaitingForOperand) {
    calcCalculate();
  } else {
    calcMemory = inputVal;
  }

  calcPendingOp = op;
  calcWaitingForOperand = true;
}

function calcCalculate() {
  const screen = document.getElementById('simCalcScreen');
  const inputVal = parseFloat(calcCurrentVal);

  if (calcPendingOp === '+') calcMemory += inputVal;
  else if (calcPendingOp === '-') calcMemory -= inputVal;
  else if (calcPendingOp === '×') calcMemory *= inputVal;
  else if (calcPendingOp === '÷') calcMemory = inputVal !== 0 ? calcMemory / inputVal : 'Error';

  calcCurrentVal = String(calcMemory);
  calcPendingOp = null;
  calcWaitingForOperand = true;
  screen.innerText = calcCurrentVal;
}

function calcClear() {
  calcCurrentVal = '0';
  calcMemory = 0;
  calcPendingOp = null;
  calcWaitingForOperand = false;
  document.getElementById('simCalcScreen').innerText = '0';
}

function calcSqrt() {
  const val = parseFloat(calcCurrentVal);
  if (val >= 0) {
    calcCurrentVal = String(Math.sqrt(val));
    calcWaitingForOperand = true;
    document.getElementById('simCalcScreen').innerText = calcCurrentVal;
  }
}

// Submit Modal & Side-by-Side Model Solution Comparison
function openSubmitModal() {
  const paper = getOrCreatePaper(simCurrentPaperKey);
  const container = document.getElementById('simReviewList');
  container.innerHTML = '';

  paper.questions.forEach((q) => {
    const userWorking = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_working`) || '(No working entered)';
    const userAns = localStorage.getItem(`mfs_sim_${simCurrentPaperKey}_q${q.num}_ans`) || '(No answer)';

    const row = document.createElement('div');
    row.className = 'sim-review-row';
    row.innerHTML = `
      <div>
        <div class="sim-review-col-title" style="color:var(--sim-navy);">
          <i class="fa-solid fa-user-pen" style="color:var(--sim-blue);"></i> Question ${q.num}: Your Working &amp; Answer
        </div>
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px;">${userWorking}</div>
        <div style="font-size:0.9rem; font-weight:800; color:var(--sim-navy);">
          Your Final Answer: <span style="background:#e0f2fe; padding:2px 8px; border-radius:4px; color:#0369a1;">${userAns} ${q.unit}</span>
        </div>
      </div>
      <div>
        <div class="sim-review-col-title" style="color:var(--sim-emerald);">
          <i class="fa-solid fa-award" style="color:var(--sim-green);"></i> Accredited Master Solution &amp; Mark Scheme [${q.markTags}]
        </div>
        <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:6px; padding:10px; font-size:0.85rem; font-family:'Courier New', monospace; white-space:pre-wrap; min-height:80px; margin-bottom:8px; color:#14532d;">${q.modelSolution}</div>
        <div style="font-size:0.9rem; font-weight:800; color:#15803d;">
          Model Benchmark: <span style="background:#dcfce7; padding:2px 8px; border-radius:4px;">${q.finalBenchmark}</span>
        </div>
      </div>
    `;
    container.appendChild(row);
  });

  // Watch Walkthrough button
  const videoBtn = document.getElementById('simModalWatchVideoBtn');
  if (paper.videoSolutionSlug) {
    videoBtn.style.display = 'inline-flex';
    videoBtn.href = `video-solution.html?topic=${paper.videoSolutionSlug}`;
  } else {
    videoBtn.style.display = 'none';
  }

  // Open modal
  document.getElementById('simSubmitModal').classList.add('open');
}

function closeSubmitModal() {
  document.getElementById('simSubmitModal').classList.remove('open');
}
