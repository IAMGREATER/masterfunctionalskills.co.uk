import os
from build_all_curriculum_pages import build_full_html

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

def build_digital_skills_revision():
    clean_topic = "Digital Functional Skills"
    subject = "Digital Skills"
    subject_pill_icon = "fa-laptop-code"
    subject_dir = "digital-functional-skills.html"
    hero_title = "Digital Skills: <span>Core Standards, Models &amp; Exam Practice</span>"
    intro_lead = "Comprehensive revision guide for Ofqual-regulated Digital Functional Skills (Entry 3 &amp; Level 1) calibrated to Pearson Edexcel &amp; City &amp; Guilds standards. Master cybersecurity, spreadsheets, file management, online safety, worked models, and interactive practice."

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
        ("skill-1", "1. Cybersecurity", "fa-shield-halved"),
        ("skill-2", "2. Spreadsheets", "fa-table-cells"),
        ("skill-3", "3. File Management", "fa-folder-tree"),
        ("skill-4", "4. Phishing Detection", "fa-envelope-open-text"),
        ("worked-exam-models", "Worked Exam Models", "fa-graduation-cap"),
        ("examiner-traps", "Examiner Traps", "fa-triangle-exclamation"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ]

    content_html = """
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> 5 Core National Digital Standards</h2>
      </div>
      <div class="skill-card-container">
        <p>Students must demonstrate competence across the 5 regulated government digital skills standards:</p>
        <ul style="padding-left:20px; line-height:1.75; color:#334155;">
          <li><strong>Standard 1: Using Devices &amp; Handling Information</strong> – File management, searching, cloud storage, selecting appropriate applications.</li>
          <li><strong>Standard 2: Creating &amp; Editing</strong> – Word processing, formatting documents, spreadsheet formulas (SUM, AVERAGE, MIN, MAX), charts, sorting and filtering.</li>
          <li><strong>Standard 3: Communicating</strong> – Professional email etiquette, CC vs BCC, calendar invitations, video conferencing netiquette.</li>
          <li><strong>Standard 4: Transacting</strong> – Completing digital forms, verification checks, online purchasing, account management.</li>
          <li><strong>Standard 5: Being Safe &amp; Responsible Online</strong> – Password security, two-factor authentication (2FA), identifying phishing scams, protecting privacy and physical wellbeing.</li>
        </ul>
      </div>
    </section>

    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Digital Functional Skills</h2>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-shield-halved"></i>
          <span>Golden Rule 1: Cybersecurity &amp; Credential Hygiene</span>
        </div>
        <p>
          Always create passwords with at least 12 characters combining uppercase, lowercase, numbers, and symbols (passphrase technique). Never reveal 2FA codes. In phishing scenarios, inspect the sender email header for subtle domain spoofing (e.g. support@paypaI-sec.com instead of paypal.com).
        </p>
        <div class="rule-highlight-badge">
          Examiner Tip: If an email asks for urgent action with a link to confirm passwords, it is always a phishing attempt.
        </div>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-table-cells"></i>
          <span>Golden Rule 2: Accurate Spreadsheet Formula Formatting</span>
        </div>
        <p>
          Every spreadsheet formula must start with an equals sign (=). When calculating totals or averages, use uppercase function names with accurate colon ranges: =SUM(C2:C14) or =AVERAGE(D2:D20). Always format currency columns with &pound; and two decimal places.
        </p>
        <div class="rule-highlight-badge">
          Check: Ensure range references include all relevant data rows without including summary header lines.
        </div>
      </div>
    </section>

    <!-- SKILL 1: CYBERSECURITY -->
    <section id="skill-1" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 1:</span> Password Security &amp; Multi-Factor Authentication (2FA)
          </div>
          <p class="pfs-card-stem">
            An NHS healthcare assistant needs to set up a new password for the clinical patient management system. Evaluate which password meets high-security compliance criteria.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>
            <div class="pfs-formula-display">
              Strong Passwords = 12+ Characters + Mixed Case + Numbers + Special Characters
            </div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Option A:</span>
                <span style="color:#e11d48; text-decoration:line-through;">Hospital2026! (Weak: predictable dictionary word).</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Option B:</span>
                <span style="color:#059669; font-weight:700;">Tr@in!Blue#98Pine (Strong: 16 characters, 3 unrelated words, mixed case &amp; symbols).</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">2FA Rule:</span>
                <span>Two-Factor Authentication requires two different categories: Something you KNOW (password) + Something you HAVE (authenticator app / phone token).</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Compliant Password:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">Tr@in!Blue#98Pine</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <div style="background:#f8fafc; border:2px solid #00a8ff; border-radius:12px; padding:20px; text-align:center; width:100%;">
              <i class="fa-solid fa-lock" style="font-size:3rem; color:#00a8ff; margin-bottom:12px;"></i>
              <div style="font-weight:800; color:#0f172a; margin-bottom:6px;">Multi-Factor Authentication</div>
              <div style="font-size:0.88rem; color:#64748b;">Password + Authenticator Code = 99.9% Protection Against Account Compromise</div>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Entry 3</span>
          <span class="pfs-pill-l2">Level 1</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 2: SPREADSHEETS -->
    <section id="skill-2" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 2:</span> Core Spreadsheet Formulas (SUM, AVERAGE, MIN, MAX)
          </div>
          <p class="pfs-card-stem">
            You are managing a medical supply inventory spreadsheet. Column C contains item costs from row 3 to row 14. What formulas should be entered into the summary rows?
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Total Cost:</span>
                <span style="font-family:monospace; font-weight:800; color:#0284c7; font-size:1.1rem;">=SUM(C3:C14)</span>
                <span>Adds all values in the specified cell range.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Average Cost:</span>
                <span style="font-family:monospace; font-weight:800; color:#0284c7; font-size:1.1rem;">=AVERAGE(C3:C14)</span>
                <span>Calculates the arithmetic mean of the range.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Lowest Cost:</span>
                <span style="font-family:monospace; font-weight:800; color:#0284c7; font-size:1.1rem;">=MIN(C3:C14)</span>
                <span>Identifies the lowest price in the dataset.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Highest Cost:</span>
                <span style="font-family:monospace; font-weight:800; color:#0284c7; font-size:1.1rem;">=MAX(C3:C14)</span>
                <span>Identifies the highest price in the dataset.</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Golden Rule:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">Always start with =</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <div style="background:#f0fdf4; border:2px solid #10b981; border-radius:12px; padding:20px; text-align:center; width:100%;">
              <i class="fa-solid fa-table-cells" style="font-size:3rem; color:#10b981; margin-bottom:12px;"></i>
              <div style="font-weight:800; color:#065f46; margin-bottom:6px;">Spreadsheet Formatting</div>
              <div style="font-size:0.88rem; color:#047857;">Format monetary data as Currency (&pound;) with 2 decimal places. Center align headers.</div>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 1 Workplace Standard</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 3: FILE MANAGEMENT -->
    <section id="skill-3" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 3:</span> Hierarchical Folder Structures &amp; Cloud Storage
          </div>
          <p class="pfs-card-stem">
            You need to organize hospital patient training records so all staff can find files quickly. Which folder hierarchy is logical, professional, and compliant?
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Root:</span>
                <span><strong>NHS_Training_2026/</strong></span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Subfolder:</span>
                <span>NHS_Training_2026/<strong>01_Clinical_Skills/</strong></span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">File Naming:</span>
                <span style="font-family:monospace; color:#0284c7; font-weight:700;">2026-10-15_Hand_Hygiene_Protocols_v1.2.pdf</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Best Practice:</span>
                <span>Use YYYY-MM-DD date prefixes so files sort chronologically. Use version numbers (_v1.0) and avoid vague names like 'doc1.docx' or 'final.pdf'.</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Standard Format:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">YYYY-MM-DD_Topic_vX</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <div style="background:#eff6ff; border:2px solid #2563eb; border-radius:12px; padding:20px; text-align:center; width:100%;">
              <i class="fa-solid fa-folder-tree" style="font-size:3rem; color:#2563eb; margin-bottom:12px;"></i>
              <div style="font-weight:800; color:#1e3a8a; margin-bottom:6px;">Cloud Collaboration</div>
              <div style="font-size:0.88rem; color:#1d4ed8;">OneDrive / SharePoint: Set permission to 'View Only' for sensitive records.</div>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Entry 3</span>
          <span class="pfs-pill-l2">Level 1</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- WORKED EXAM MODELS -->
    <section id="worked-exam-models" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Pearson Edexcel Worked Exam Model</h2>
      </div>

      <div class="worked-exam-model-card">
        <div class="model-header-bar">
          <span class="badge-worked-model">Pearson Edexcel Level 1 Practical Simulator</span>
          <span class="model-marks-pill">[4 Marks &bull; Digital Practical Task]</span>
        </div>
        <div class="model-question-stem">
          <strong>Workplace Scenario:</strong> You are an administrative assistant at a community clinic. 
          Your manager asks you to prepare a staff shift attendance spreadsheet. 
          <ol style="margin-top:10px; padding-left:20px; line-height:1.7;">
            <li>Enter a formula in cell <strong>B15</strong> to calculate the total hours worked across rows B3 to B14.</li>
            <li>Enter a formula in cell <strong>B16</strong> to calculate the average hours worked.</li>
            <li>Sort the table by Staff Surname in alphabetical order (A to Z).</li>
            <li>Apply currency formatting (&pound;) with 2 decimal places to the hourly wage column D.</li>
          </ol>
        </div>

        <div class="model-steps-list">
          <div class="model-step-row">
            <span class="step-number-bubble">Step 1</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Total Hours Formula [1 Mark]</div>
              <div class="step-math-line">=SUM(B3:B14)</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> 1 mark awarded for correct uppercase formula syntax and accurate range.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 2</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Average Hours Formula [1 Mark]</div>
              <div class="step-math-line">=AVERAGE(B3:B14)</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> 1 mark awarded for =AVERAGE with matching data range.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 3</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Table Sorting [1 Mark]</div>
              <div class="step-math-line">Highlight range A3:E14 &rarr; Data &rarr; Sort &rarr; Column A &rarr; Ascending (A-Z)</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> 1 mark awarded for expanding selection so related data rows stay intact.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 4</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Currency Number Formatting [1 Mark]</div>
              <div class="step-math-line" style="background:#dcfce7; color:#166534; border-color:#86efac;">Right click Column D &rarr; Format Cells &rarr; Currency &rarr; Symbol: &pound; &rarr; Decimals: 2</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> 1 mark awarded for professional UK currency formatting.</div>
            </div>
          </div>
        </div>

        <div class="model-final-answer-callout">
          <div class="model-final-text">Official Examiner Award: 4 / 4 Marks</div>
          <div style="font-size:0.92rem; color:#94a3b8;">Common Mistake: Typing =SUM(B3+B14) or including row 15 in the average range!</div>
        </div>
      </div>
    </section>

    <!-- EXAMINER TRAPS -->
    <section id="examiner-traps" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation"></i> Examiner Traps &amp; Common Pitfalls</h2>
      </div>

      <div class="trap-card-coral">
        <div class="trap-card-coral-header">
          <i class="fa-solid fa-circle-xmark"></i>
          <span>Trap 1: Sorting Only One Column Without Expanding the Selection</span>
        </div>
        <p>
          If you highlight only names and click sort without selecting the entire table, the names will sort but their addresses, hours, and pay will stay put — corrupting all patient records!
        </p>
        <div class="trap-solution-badge">
          <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Solution: Always click 'Expand the Selection' when prompted by spreadsheet software.
        </div>
      </div>

      <div class="trap-card-coral">
        <div class="trap-card-coral-header">
          <i class="fa-solid fa-circle-xmark"></i>
          <span>Trap 2: Replying 'ALL' or CC'ing Confidentially Sensitive Emails</span>
        </div>
        <p>
          Sending patient records or group feedback using the 'To' or 'CC' field exposes everyone's private email address to the entire list, breaching UK GDPR data protection legislation.
        </p>
        <div class="trap-solution-badge">
          <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Solution: Always use BCC (Blind Carbon Copy) when emailing multiple external recipients.
        </div>
      </div>
    </section>

    <!-- PRACTICE QUESTIONS -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
        <span style="font-size:0.9rem; color:#64748b; font-weight:700;">2 Practice Tasks</span>
      </div>

      <!-- Question 1 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-num">Question 1</span>
          <span class="practice-q-marks">[2 Marks]</span>
        </div>
        <div class="practice-q-stem">
          You receive an email from <code>security-update@nhs-net-verify.org</code> stating: <em>"Urgent: Your NHS Smartcard login expires today. Click here immediately to enter your password and prevent suspension."</em><br><br>
          Give TWO reasons why this is a phishing scam, and state what action you should take.
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q1')">
            <i class="fa-solid fa-eye"></i> Reveal Full Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q1" class="solution-drawer">
          <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Tutor Worked Solution</div>
          <div style="line-height:1.7; color:#166534;">
            <p><strong>Reason 1:</strong> Fake sender domain (official NHS domains end in <code>@nhs.net</code> or <code>@nhs.uk</code>, not <code>.org</code>). [1 Mark]</p>
            <p><strong>Reason 2:</strong> Creates artificial urgency and threatens account closure to provoke panic. [1 Mark]</p>
            <p><strong>Action:</strong> Do not click the link; report the email to the IT security officer and delete it. [1 Mark]</p>
          </div>
        </div>
      </div>

      <!-- Question 2 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-num">Question 2</span>
          <span class="practice-q-marks">[2 Marks]</span>
        </div>
        <div class="practice-q-stem">
          A spreadsheet lists staff overtime hours in cells <code>D4:D18</code>.<br>
          Write the exact formula required to calculate the AVERAGE overtime hours.
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q2')">
            <i class="fa-solid fa-eye"></i> Reveal Full Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q2" class="solution-drawer">
          <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Tutor Worked Solution</div>
          <div style="line-height:1.7; color:#166534;">
            <p><strong>Formula:</strong> <code>=AVERAGE(D4:D18)</code> [2 Marks]</p>
            <p><em>(Award 1 mark for correct function name without equals sign, full 2 marks for exact syntax).</em></p>
          </div>
        </div>
      </div>
    </section>
    """

    full_html = build_full_html(
        filename="digital-functional-skills.html",
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file="digital-functional-skills-level-1.html",
        next_name="Digital Skills Level 1 Online Course"
    )

    out_path = os.path.join(PROJECT_DIR, "digital-functional-skills-revision.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] Digital Functional Skills revision generated ({len(full_html)} bytes)")

if __name__ == "__main__":
    build_digital_skills_revision()
