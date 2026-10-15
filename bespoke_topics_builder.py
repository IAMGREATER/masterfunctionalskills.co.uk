#!/usr/bin/env python3
"""
Bespoke flagship builders for Master Functional Skills revision pages.
Features 100% original numbers, spacious layouts, proportional solid-fill diagrams,
Pearson Edexcel worked exam models, examiner traps, and interactive practice.
"""

import os, sys
from build_all_curriculum_pages import build_full_html

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

def build_perimeter_page():
    clean_topic = "Perimeter"
    subject = "Mathematics"
    subject_pill_icon = "fa-calculator"
    subject_dir = "functional-skills-maths-level-2.html"
    hero_title = "Perimeter: <span>Formulas, Models &amp; Exam Practice</span>"
    intro_lead = "Comprehensive revision guide for Perimeter calibrated to Pearson Edexcel &amp; City &amp; Guilds Functional Skills standards. Master simple shapes, compound L-shapes, circular arcs, worked exam models, and interactive practice."

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
        ("skill-1", "1. Rectangles", "fa-shapes"),
        ("skill-2", "2. Parallelograms", "fa-shapes"),
        ("skill-3", "3. Compound L-Shapes", "fa-shapes"),
        ("skill-4", "4. Shapes with Arcs", "fa-shapes"),
        ("worked-exam-models", "Worked Exam Models", "fa-graduation-cap"),
        ("examiner-traps", "Examiner Traps", "fa-triangle-exclamation"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ]

    content_html = """
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
      </div>
      <div class="skill-card-container">
        <p>Students must be able to demonstrate mastery of the following regulated outcomes:</p>
        <ul style="padding-left:20px; line-height:1.75; color:#334155;">
          <li><strong>L1.22</strong> – Calculate the perimeter of simple shapes, including rectangles and combinations of rectangles.</li>
          <li><strong>L2.16</strong> – Calculate perimeters of 2D shapes including triangles, circles, and composite shapes (including circular boundaries and non-rectangular compounds).</li>
          <li>Set out step-by-step mathematical working clearly, stating appropriate units of linear measurement (mm, cm, m).</li>
        </ul>
      </div>
    </section>

    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Perimeter</h2>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-route"></i>
          <span>Golden Rule 1: Perimeter is the Outside Distance — Walk the Entire Boundary</span>
        </div>
        <p>
          Perimeter is strictly the total distance around the outside edge of a 2D shape. Imagine walking around the perimeter of the field or floor. Never add inside partition lines or dashed splitting lines used in working out compound shapes.
        </p>
        <div class="rule-highlight-badge">
          Examiner Tip: Mark each side with a small tick as you add it to your running total so you don't miss or double-count sides.
        </div>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-ruler-combined"></i>
          <span>Golden Rule 2: Slant Heights Count for Perimeter; Perpendicular Heights Do Not</span>
        </div>
        <p>
          When finding the perimeter of parallelograms or trapeziums, you must use the outer slanted side lengths. The perpendicular height inside the shape is only used for area calculations, never for perimeter!
        </p>
        <div class="rule-highlight-badge">
          Units Check: Perimeter is always measured in linear units (mm, cm, m) — never square units (cm&sup2; or m&sup2;).
        </div>
      </div>
    </section>

    <!-- SKILL 1: RECTANGLES -->
    <section id="skill-1" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 1:</span> Perimeter of a Rectangle (Garden Border)
          </div>
          <p class="pfs-card-stem">
            A healthcare facility garden bed is in the shape of a rectangle with length <strong>18 m</strong> and width <strong>7.5 m</strong>. Calculate the total perimeter of the garden bed.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>
            <div class="pfs-formula-display">
              Perimeter = 2 &times; (Length + Width) &nbsp;or&nbsp; Side + Side + Side + Side
            </div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Opposite sides of a rectangle are identical in length (18 m and 7.5 m).</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Add all four outer sides: 18 + 18 + 7.5 + 7.5 = <strong>51 m</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Alternative formula: 2 &times; (18 + 7.5) = 2 &times; 25.5 = <strong>51 m</strong>.</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Final Perimeter:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">51 m</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 180" width="340" height="180">
              <rect x="30" y="30" width="280" height="110" fill="#ea580c" fill-opacity="0.12" stroke="#ea580c" stroke-width="3" rx="4" />
              <text x="170" y="22" font-size="14" font-weight="800" fill="#ea580c" text-anchor="middle">18 m</text>
              <text x="170" y="162" font-size="14" font-weight="800" fill="#ea580c" text-anchor="middle">18 m</text>
              <text x="16" y="90" font-size="14" font-weight="800" fill="#ea580c" text-anchor="middle">7.5 m</text>
              <text x="324" y="90" font-size="14" font-weight="800" fill="#ea580c" text-anchor="middle">7.5 m</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 2: PARALLELOGRAMS -->
    <section id="skill-2" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 2:</span> Perimeter of a Parallelogram (Distractor Traps)
          </div>
          <p class="pfs-card-stem">
            Below is a parallelogram flower border with a horizontal base of <strong>14 m</strong>, a slanted side of <strong>9 m</strong>, and an internal perpendicular height of <strong>7 m</strong>. Calculate the perimeter.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>
            <div class="pfs-formula-display">
              Perimeter = 2 &times; (Base + Slanted Side)
            </div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Identify the boundary edges: Base = 14 m, Slant Side = 9 m.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span style="color:#e11d48; font-weight:700;">Discard the perpendicular height (7 m) — it is a trap intended for area!</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Add the 4 outer sides: 14 + 14 + 9 + 9 = <strong>46 m</strong>.</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Final Perimeter:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">46 m</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 180" width="340" height="180">
              <polygon points="70,30 310,30 250,140 10,140" fill="#0284c7" fill-opacity="0.12" stroke="#0284c7" stroke-width="3" />
              <line x1="70" y1="30" x2="70" y2="140" stroke="#e11d48" stroke-width="2" stroke-dasharray="4,4" />
              <text x="190" y="22" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">14 m</text>
              <text x="130" y="160" font-size="14" font-weight="800" fill="#0284c7" text-anchor="middle">14 m</text>
              <text x="295" y="90" font-size="14" font-weight="800" fill="#0284c7">9 m</text>
              <text x="82" y="90" font-size="13" font-weight="700" fill="#e11d48">7 m (Trap)</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 3: COMPOUND L-SHAPES -->
    <section id="skill-3" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 3:</span> Perimeter of a Compound L-Shape (Finding Missing Sides)
          </div>
          <p class="pfs-card-stem">
            An NHS clinic office suite is shaped like an L. The top edge is <strong>16 m</strong>, the left outer edge is <strong>12 m</strong>, the bottom-right step is <strong>9 m</strong> wide, and the bottom-left edge is <strong>7 m</strong> wide. Calculate the total perimeter.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Find missing horizontal side: Top (16 m) &minus; Bottom-left (7 m) = <strong>9 m</strong> (matches right overhang).</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Find missing vertical side: Total Left Height (12 m) &minus; Right Step Height (7 m) = <strong>5 m</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Add all 6 outer sides: 16 + 5 + 9 + 7 + 7 + 12 = <strong>56 m</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Rule:</span>
                <span>In any rectangular L-shape, Perimeter = 2 &times; (Max Width + Max Height) = 2 &times; (16 + 12) = <strong>56 m</strong>!</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Final Perimeter:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">56 m</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" width="340" height="220">
              <polygon points="20,20 300,20 300,80 150,80 150,190 20,190" fill="#0284c7" fill-opacity="0.12" stroke="#0284c7" stroke-width="3" />
              <text x="160" y="16" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">16 m (Top)</text>
              <text x="315" y="55" font-size="13" font-weight="800" fill="#e11d48">5 m (?)</text>
              <text x="225" y="74" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">9 m</text>
              <text x="165" y="140" font-size="13" font-weight="800" fill="#0284c7">7 m</text>
              <text x="85" y="206" font-size="13" font-weight="800" fill="#0284c7" text-anchor="middle">7 m</text>
              <text x="12" y="110" font-size="13" font-weight="800" fill="#0284c7" text-anchor="end">12 m</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 4: SHAPES WITH ARCS -->
    <section id="skill-4" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Example 4:</span> Compound Shape with Semicircular Arc (Level 2)
          </div>
          <p class="pfs-card-stem">
            A hospital emergency entrance door consists of a rectangle measuring <strong>4 m wide</strong> by <strong>6 m high</strong>, topped by a semicircular arch with diameter <strong>4 m</strong>. Calculate the perimeter of the doorway frame (to 2 decimal places).
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>
            <div class="pfs-formula-display">
              Semicircular Arc = &frac12; &times; &pi; &times; d &nbsp;(&pi; &asymp; 3.142)
            </div>
            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Full circle circumference = &pi; &times; d = 3.142 &times; 4 = 12.568 m.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Half circle arc = 12.568 &divide; 2 = <strong>6.284 m</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Add outer straight sides: Left (6 m) + Right (6 m) + Bottom (4 m) = 16 m.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 4:</span>
                <span>Total perimeter = 16 + 6.284 = <strong>22.28 m</strong>.</span>
              </div>
            </div>

            <div class="big-answer-row">
              <div class="big-answer-title"><i class="fa-solid fa-check"></i> Total Boundary:</div>
              <div class="big-answer-chips">
                <span class="big-answer-chip">22.28 m</span>
              </div>
            </div>
          </div>

          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 240" width="340" height="240">
              <path d="M 90,100 A 80,80 0 0,1 250,100 Z" fill="#7c3aed" fill-opacity="0.15" stroke="#7c3aed" stroke-width="3" />
              <rect x="90" y="100" width="160" height="120" fill="#7c3aed" fill-opacity="0.08" stroke="#7c3aed" stroke-width="3" />
              <line x1="90" y1="100" x2="250" y2="100" stroke="#7c3aed" stroke-width="2" stroke-dasharray="4,4" />
              <text x="170" y="15" font-size="13" font-weight="800" fill="#7c3aed" text-anchor="middle">Arc = &frac12;&pi;d</text>
              <text x="75" y="160" font-size="14" font-weight="800" fill="#7c3aed" text-anchor="end">6 m</text>
              <text x="265" y="160" font-size="14" font-weight="800" fill="#7c3aed">6 m</text>
              <text x="170" y="235" font-size="14" font-weight="800" fill="#7c3aed" text-anchor="middle">4 m</text>
              <text x="170" y="118" font-size="12" font-style="italic" fill="#64748b" text-anchor="middle">Internal line (Do Not Add!)</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Only</span>
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
          <span class="badge-worked-model">Pearson Edexcel Level 2 Realistic Scenario</span>
          <span class="model-marks-pill">[4 Marks &bull; Calculator Allowed]</span>
        </div>
        <div class="model-question-stem">
          <strong>Vocational Healthcare Context:</strong> An NHS trust is installing security perimeter fencing around a new staff car park. The car park is a rectangle measuring <strong>45 m</strong> long by <strong>28 m</strong> wide. 
          A gate opening of width <strong>4 m</strong> is left along one side (no fencing is needed across the gate).<br><br>
          The fencing contractor charges <strong>&pound;34 per metre</strong> of installed fence.<br>
          Calculate the total cost of installing the security fencing. Show all your working clearly.
        </div>

        <div class="model-steps-list">
          <div class="model-step-row">
            <span class="step-number-bubble">Step 1</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Calculate the Full Rectangular Perimeter [M1 Method Mark]</div>
              <div class="step-math-line">Perimeter = 2 &times; (45 + 28) = 2 &times; 73 = 146 m</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> M1 awarded for correct perimeter method of rectangle.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 2</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Subtract the Gate Opening [M1 Method Mark]</div>
              <div class="step-math-line">Fencing Required = 146 &minus; 4 = 142 m</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> M1 awarded for subtracting the 4 m opening.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 3</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Multiply by Unit Cost to Find Total [M1 Process Mark]</div>
              <div class="step-math-line">Total Cost = 142 &times; &pound;34 = &pound;4,828</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> M1 awarded for multiplying length by &pound;34.</div>
            </div>
          </div>

          <div class="model-step-row">
            <span class="step-number-bubble">Step 4</span>
            <div class="step-detail-body">
              <div class="step-detail-title">Accuracy Mark &amp; Currency Format [A1 Accuracy Mark]</div>
              <div class="step-math-line" style="background:#dcfce7; color:#166534; border-color:#86efac;">Final Answer: &pound;4,828</div>
              <div class="mark-scheme-tag"><i class="fa-solid fa-check"></i> A1 awarded for accurate numerical answer with &pound; symbol.</div>
            </div>
          </div>
        </div>

        <div class="model-final-answer-callout">
          <div class="model-final-text">Official Examiner Award: 4 / 4 Marks</div>
          <div style="font-size:0.92rem; color:#94a3b8;">Common Loss: Forgetting to subtract the gate opening loses 2 marks!</div>
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
          <span>Trap 1: Adding Inside Boundary Lines in Compound Shapes</span>
        </div>
        <p>
          When you split a compound shape into rectangles or triangles, students often accidentally add the dotted partition line into their perimeter sum. 
        </p>
        <div class="trap-solution-badge">
          <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Solution: Highlight only the exterior edge of the shape with a colored pen before doing your calculations.
        </div>
      </div>

      <div class="trap-card-coral">
        <div class="trap-card-coral-header">
          <i class="fa-solid fa-circle-xmark"></i>
          <span>Trap 2: Forgetting to Halve the Circle Circumference</span>
        </div>
        <p>
          The formula &pi; &times; d gives the circumference of a whole circle. For a semicircle, you must divide by 2. If the semicircle is standalone, remember to add the straight diameter across the bottom!
        </p>
        <div class="trap-solution-badge">
          <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Semicircle Perimeter = (&frac12; &times; &pi; &times; d) + d (if enclosed).
        </div>
      </div>
    </section>

    <!-- PRACTICE QUESTIONS -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
        <span style="font-size:0.9rem; color:#64748b; font-weight:700;">3 Practice Tasks</span>
      </div>

      <!-- Question 1 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <div class="practice-q-title"><span class="pfs-prefix">Question 1:</span> Warehouse Skirting Board</div>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [2 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>A storage warehouse room has a rectangular floor measuring <strong>22 m</strong> in length and <strong>8.5 m</strong> in width.</p>
          <p>Skirting board is to be installed around the perimeter of the room. Calculate the total metres of skirting board needed.</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q1')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q1" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">2 / 2 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Formula &amp; Method)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Perimeter = 2 &times; (Length + Width) = 2 &times; (22 + 8.5)</div>
              <div class="solution-step-content">Add the two perpendicular dimensions together (30.5 m), then double for both opposite pairs. (Alternative valid method: 22 + 22 + 8.5 + 8.5).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Calculate Final Total)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">2 &times; 30.5 = 61 m</div>
              <div class="solution-step-content">Compute final linear length. Ensure correct metric units (metres) are included.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">61 metres</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> Remember that perimeter is linear length (m), NOT square units (m&sup2;). Writing m&sup2; for perimeter will lose accuracy marks in Functional Skills exams!</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Question 2 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <div class="practice-q-title"><span class="pfs-prefix">Question 2:</span> Compound L-Shaped Reception Area</div>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>An L-shaped patient reception area has outer measurements: Top = <strong>14 m</strong>, Left = <strong>10 m</strong>, Bottom-left width = <strong>6 m</strong>, and Right-hand drop = <strong>4 m</strong>.</p>
          <p>Work out the perimeter of the room.</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q2')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q2" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Find Missing Horizontal Edge)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Missing horizontal = 14 &minus; 6 = 8 m</div>
              <div class="solution-step-content">Subtract the known bottom-left segment (6 m) from the total top width (14 m).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Find Missing Vertical Edge)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Missing vertical = 10 &minus; 4 = 6 m</div>
              <div class="solution-step-content">Subtract the known right-hand drop (4 m) from the total left height (10 m).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Sum All 6 Sides)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">14 + 4 + 8 + 6 + 6 + 10 = 48 m</div>
              <div class="solution-step-content">Add all outer edges together. (Shortcut check for rectilinear L-shapes: 2 &times; (14 + 10) = 48 m).</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">48 metres</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> When calculating compound perimeters, count tick marks around the perimeter to ensure all 6 sides are included. Never accidentally add internal boundary lines!</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Question 3 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <div class="practice-q-title"><span class="pfs-prefix">Question 3:</span> Circular Patio Lighting</div>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>A circular patio has a diameter of <strong>7 m</strong>. A decorative rope light is to be placed all the way around the outside edge of the patio.</p>
          <p>Calculate the length of rope light required to 2 decimal places. Use &pi; = 3.142.</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q3')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q3" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Circumference Formula)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Circumference = &pi; &times; d = 3.142 &times; 7</div>
              <div class="solution-step-content">Use the circumference formula for circles with given diameter (d = 7 m).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Perform Multiplication)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">3.142 &times; 7 = 21.994 m</div>
              <div class="solution-step-content">Calculate the raw product before rounding.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Rounding to 2 Decimal Places)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">21.994 &rarr; 21.99 m</div>
              <div class="solution-step-content">Round to 2 decimal places. The third decimal place is 4 (&lt; 5), so round down to 21.99 m.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">21.99 metres</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> When the exam states "Use &pi; = 3.142", always type 3.142 into your calculator instead of pressing the &pi; button. Pearson Edexcel mark schemes check against 3.142 arithmetic.</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>
    </section>
    """

    full_html = build_full_html(
        filename="functional-skills-perimeter.html",
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file="functional-skills-volume.html",
        next_name="Volume"
    )

    out_path = os.path.join(PROJECT_DIR, "functional-skills-perimeter.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[BESPOKE OK] Perimeter generated ({len(full_html)} bytes)")

def build_money_page():
    clean_topic = "Money"
    subject = "Mathematics"
    subject_pill_icon = "fa-calculator"
    subject_dir = "functional-skills-maths-level-2.html"
    hero_title = "Money: <span>Calculations, Currency &amp; Conversions</span>"
    intro_lead = "Master essential money calculations calibrated to Pearson Edexcel &amp; City &amp; Guilds Functional Skills standards. Learn currency unit conversions between pounds and pence (£ &amp; p), non-calculator addition &amp; subtraction, multi-item budgeting, change calculations, and rounding to make realistic financial decisions."

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
        ("skill-1", "1. Pounds &amp; Pence", "fa-coins"),
        ("skill-2", "2. Column Addition &amp; Subtraction", "fa-calculator"),
        ("skill-3", "3. Budgeting &amp; Change", "fa-receipt"),
        ("skill-4", "4. Rounding &amp; Estimation", "fa-arrow-up-right-dots"),
        ("worked-exam-models", "Worked Exam Models", "fa-graduation-cap"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ]

    content_html = """
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#059669;"><i class="fa-solid fa-check"></i> Regulated Standards</span>
      </div>
      <div class="skill-card-container">
        <p>Candidates must demonstrate mastery of the following regulated Functional Skills criteria:</p>
        <ul style="padding-left:20px; line-height:1.8; color:#334155; font-size:1.02rem;">
          <li><strong>L1.17:</strong> Add, subtract, multiply and divide with money using decimal notation, expressing currency correctly in pounds (£) and pence (p).</li>
          <li><strong>L1.18:</strong> Round amounts of money to the nearest £1 or 10p, and make realistic estimates to plan spending and check calculator outputs.</li>
          <li><strong>L2.14:</strong> Solve complex multi-step problems involving money, wages, overtime, percentage discounts, profit, and budgeting with and without a calculator.</li>
          <li>Accurately format currency values in answers: write two decimal places for pence (e.g. £14.50, never £14.5).</li>
        </ul>
      </div>
    </section>

    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Money Calculations</h2>
      </div>

      <!-- Rule 1 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-coins"></i>
          <span>Golden Rule 1: Always Write Two Decimal Places for Pence in Pounds (£)</span>
        </div>
        <p>
          In UK currency, whenever an amount is written with a pound sign (<strong>£</strong>), it <strong>must always have exactly two decimal places</strong> unless it is an exact whole pound without decimals.
        </p>
        <div class="rule-highlight-badge">
          Examiner Rule: £14.50 is correct. Writing £14.5 or £14.50p will lose accuracy marks in Pearson Edexcel exams!
        </div>
      </div>

      <!-- Rule 2 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-arrow-right-arrow-left"></i>
          <span>Golden Rule 2: Never Mix £ and p in One Calculation</span>
        </div>
        <p>
          Before adding, subtracting, or multiplying prices, ensure all values are in the <strong>same unit</strong>. The safest exam method is converting all pence into pounds by dividing by 100:
        </p>
        <div class="rule-highlight-badge">
          Example: 85p = £0.85 &bull; 65p = £0.65 &bull; 8p = £0.08 (Notice the leading zero for single-digit pence!)
        </div>
      </div>

      <!-- Rule 3 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-ban"></i>
          <span>Golden Rule 3: Never Combine £ and p Together</span>
        </div>
        <p>
          Write either <strong>£4.50</strong> OR <strong>450p</strong>. Never write <strong>£4.50p</strong> or <strong>£0.75p</strong>. Combining both symbols is a recognised notation penalty across all exam boards.
        </p>
      </div>

      <!-- Rule 4 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-align-left"></i>
          <span>Golden Rule 4: Line Up the Decimal Points in Non-Calculator Papers</span>
        </div>
        <p>
          In Paper 1 (Non-Calculator), write amounts in vertical columns with every decimal point aligned directly beneath each other. Add trailing placeholder zeros (e.g. £24 becomes £24.00) so columns align cleanly.
        </p>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 1: CONVERTING POUNDS & PENCE -->
    <!-- ============================================== -->
    <section id="skill-1" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 1:</span> Converting Between Pounds (£) and Pence (p)
          </h3>
          <p class="pfs-card-stem">
            A healthcare ward assistant is purchasing supplies for the patient lounge: 
            surgical medical tape for <strong>£3.40</strong>, antiseptic spray for <strong>85p</strong>, and a roll of cotton wool for <strong>75p</strong>. 
            Calculate the total cost in pounds (£).
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>

            <!-- Currency Conversion Flow Visual -->
            <div class="money-flow-grid">
              <div class="money-flow-card">
                <div class="money-flow-title"><i class="fa-solid fa-arrow-right"></i> Pence (p) to Pounds (£)</div>
                <div class="money-flow-step">
                  <span>Divide by <strong>100</strong>:</span>
                  <span class="pfs-math-text">85p &divide; 100 = £0.85</span>
                </div>
                <div class="money-flow-step">
                  <span>Divide by <strong>100</strong>:</span>
                  <span class="pfs-math-text">75p &divide; 100 = £0.75</span>
                </div>
              </div>
              <div class="money-flow-card">
                <div class="money-flow-title"><i class="fa-solid fa-arrow-left"></i> Pounds (£) to Pence (p)</div>
                <div class="money-flow-step">
                  <span>Multiply by <strong>100</strong>:</span>
                  <span class="pfs-math-text">£3.40 &times; 100 = 340p</span>
                </div>
                <div class="money-flow-step">
                  <span>Rule:</span>
                  <span style="color:#64748b; font-size:0.95rem;">Move decimal point 2 places right</span>
                </div>
              </div>
            </div>

            <div class="pfs-formula-display">
              Total Cost = £3.40 + £0.85 + £0.75 = £5.00
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Convert all values in pence to pounds (£): <strong>85p = £0.85</strong> and <strong>75p = £0.75</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Align and sum the three values: <strong>£3.40 + £0.85 + £0.75 = £5.00</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Ensure exactly two decimal places are written for currency: <strong>£5.00</strong>.</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Final Answer: £5.00</span>
              <span style="font-size:0.86rem;">Full 2 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 2: COLUMN ADDITION & SUBTRACTION -->
    <!-- ============================================== -->
    <section id="skill-2" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 2:</span> Non-Calculator Column Subtraction with Money (Paper 1)
          </h3>
          <p class="pfs-card-stem">
            A clinic practice manager wants to replace an old office workstation. 
            She sells the existing desk second-hand for <strong>£78</strong> and orders a new ergonomic desk costing <strong>£345</strong>. 
            Calculate the price difference without using a calculator.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>

            <p style="font-size:1.05rem; color:#334155; line-height:1.7;">
              To find the price difference, subtract the sale price (£78) from the new desk cost (£345) using the vertical column subtraction method:
            </p>

            <div style="display:flex; justify-content:center; margin:16px 0;">
              <div class="column-calc-box">
                <div style="display:flex; justify-content:space-between; width:130px;">
                  <span>&nbsp;</span>
                  <span>£ 3 4 5</span>
                </div>
                <div style="display:flex; justify-content:space-between; width:130px;">
                  <span>&minus;</span>
                  <span>£ &nbsp; 7 8</span>
                </div>
                <div class="column-calc-divider"></div>
                <div style="display:flex; justify-content:space-between; width:130px; color:#0284c7;">
                  <span>&nbsp;</span>
                  <span>£ 2 6 7</span>
                </div>
              </div>
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Units column: <strong>5 &minus; 8</strong> cannot be done without borrowing. Borrow 1 ten from the tens column (4 becomes 3), making 15 &minus; 8 = <strong>7</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Tens column: <strong>3 &minus; 7</strong> cannot be done. Borrow 1 hundred from the hundreds column (3 becomes 2), making 13 &minus; 7 = <strong>6</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Hundreds column: Remaining 2 drops down to make <strong>£267</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 4:</span>
                <span>Inverse check: <strong>£267 + £78 = £345</strong> (verified correct).</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Price Difference: £267</span>
              <span style="font-size:0.86rem;">Full 2 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 3: BUDGETING & CHANGE -->
    <!-- ============================================== -->
    <section id="skill-3" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 3:</span> Multi-Item Budgeting &amp; Calculating Change from a Banknote
          </h3>
          <p class="pfs-card-stem">
            A staff member orders the following uniform items: 
            <strong>2 healthcare polo shirts</strong> at <strong>£14.25</strong> each, 
            <strong>1 lanyard &amp; card pack</strong> for <strong>£4.80</strong>, and 
            <strong>1 engraved name badge</strong> for <strong>£3.70</strong>. 
            She pays using a <strong>£50 note</strong>. Work out how much change she should receive.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>

            <div class="pfs-formula-display">
              Change = Amount Paid (£50.00) &minus; Total Cost of Items
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Calculate polo shirts cost: <strong>2 &times; £14.25 = £28.50</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Sum all uniform items to find total expenditure: <br>
                  <strong>£28.50 + £4.80 + £3.70 = £37.00</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Subtract total cost from the £50 banknote to determine change due: <br>
                  <strong>£50.00 &minus; £37.00 = £13.00</strong>.
                </span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Change Due: £13.00</span>
              <span style="font-size:0.86rem;">Full 3 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 4: ROUNDING & ESTIMATION -->
    <!-- ============================================== -->
    <section id="skill-4" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 4:</span> Rounding Money &amp; Estimating Total Bills
          </h3>
          <p class="pfs-card-stem">
            A care home coordinator is ordering weekly activity materials online. The prices are: 
            <strong>£12.89</strong>, <strong>£4.15</strong>, <strong>£19.95</strong>, and <strong>£8.49</strong>. 
            By rounding each amount to the <strong>nearest pound (£)</strong>, estimate the total cost of the order.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>

            <div class="big-numbers-tray">
              <span class="big-num-chip">£12.89 &rarr; <strong>£13</strong></span>
              <span class="big-num-chip">£4.15 &rarr; <strong>£4</strong></span>
              <span class="big-num-chip">£19.95 &rarr; <strong>£20</strong></span>
              <span class="big-num-chip">£8.49 &rarr; <strong>£8</strong></span>
            </div>

            <div class="pfs-formula-display">
              Estimated Total = £13 + £4 + £20 + £8 = £45
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Inspect pence digits: if <strong>50p or more</strong>, round up to the next pound; if <strong>under 50p</strong>, round down.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Round each item: £12.89 &rarr; <strong>£13</strong>, £4.15 &rarr; <strong>£4</strong>, £19.95 &rarr; <strong>£20</strong>, £8.49 &rarr; <strong>£8</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Sum the rounded values: <strong>13 + 4 + 20 + 8 = £45</strong>.</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Estimated Total: £45</span>
              <span style="font-size:0.86rem;">Full 2 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- WORKED EXAM MODELS -->
    <!-- ============================================== -->
    <section id="worked-exam-models" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Pearson Edexcel Worked Exam Models</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#ea580c;"><i class="fa-solid fa-star"></i> Benchmark Solutions</span>
      </div>

      <!-- Model 1 -->
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Exam Model 1:</span> Workplace Overtime Pay Rate (Level 2)
          </h3>
          <p class="pfs-card-stem">
            Jordan works as a pharmacy dispenser on a basic wage of <strong>£12.40 per hour</strong> for <strong>35 hours per week</strong>. 
            On Saturday, he works an additional <strong>6 hours of overtime</strong> paid at <strong>time-and-a-half (1.5 &times; basic rate)</strong>. 
            Calculate Jordan's total gross pay for the week.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[4 Marks]</div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Basic wage: <strong>35 hours &times; £12.40 = £434.00</strong> [M1 Method Mark].</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Overtime hourly rate: <strong>£12.40 &times; 1.5 = £18.60 per hour</strong> [M1 Method Mark].</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Overtime pay: <strong>6 hours &times; £18.60 = £111.60</strong> [M1 Method Mark].</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 4:</span>
                <span>Total gross earnings: <strong>£434.00 + £111.60 = £545.60</strong> [A1 Accuracy Mark].</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Total Gross Pay: £545.60</span>
              <span style="font-size:0.86rem;">Full 4 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Focus</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- INTERACTIVE EXAM PRACTICE QUESTIONS -->
    <!-- ============================================== -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
        <span style="font-size:0.9rem; color:#64748b; font-weight:700;">3 Practice Tasks</span>
      </div>
      <p class="section-lead-text">
        Attempt these authentic Functional Skills money exam questions. Type your step-by-step method into the scratchpad, then click to reveal the official tutor mark scheme.
      </p>

      <!-- Practice Question 1 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 1:</span> NHS Team Workshop Catering Order</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            An administrator is ordering lunch refreshments for a team training session:
          </p>
          <ul style="padding-left:20px; line-height:1.75; color:#334155;">
            <li><strong>3 platters of sandwiches</strong> at <strong>£8.60</strong> each</li>
            <li><strong>2 fruit bowls</strong> at <strong>£4.75</strong> each</li>
            <li><strong>4 bottles of sparkling water</strong> at <strong>95p</strong> each</li>
          </ul>
          <p>Work out the total cost of the order in pounds (£).</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad1"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad1" class="working-scratchpad-input" placeholder="Type your step-by-step working here (e.g. sandwiches = 3 * £8.60 = £25.80...)..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q1')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q1" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Convert Pence to Pounds)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">95p &divide; 100 = £0.95</div>
              <div class="solution-step-content">Convert the water bottles to pounds so all items are in identical currency units.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Calculate Individual Sub-Totals)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Sandwiches: 3 &times; £8.60 = £25.80 &bull; Fruit: 2 &times; £4.75 = £9.50 &bull; Water: 4 &times; £0.95 = £3.80</div>
              <div class="solution-step-content">Multiply each quantity by its unit price.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Calculate Final Sum)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">Total = £25.80 + £9.50 + £3.80 = £39.10</div>
              <div class="solution-step-content">Add the three sub-totals together. Ensure the trailing zero in 10p is written explicitly.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">£39.10</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> Calculator displays will show <code>39.1</code>. You must write <code>£39.10</code> on your exam paper. Writing £39.1 will forfeit the final accuracy mark!</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Practice Question 2 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 2:</span> IT Equipment Purchase &amp; Change from Banknotes</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            An IT field engineer buys <strong>4 high-speed USB flash drives</strong> priced at <strong>£7.65</strong> each. 
            He pays the cashier using <strong>two £20 banknotes (£40 total)</strong>.
          </p>
          <p>Calculate how much change the engineer should receive.</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad2"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad2" class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q2')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q2" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Total Purchase Cost)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">4 &times; £7.65 = £30.60</div>
              <div class="solution-step-content">Multiply unit cost by quantity. (4 &times; 7 = £28; 4 &times; 0.65 = £2.60; 28 + 2.60 = £30.60).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Calculate Cash Tendered)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">2 &times; £20 = £40.00</div>
              <div class="solution-step-content">Total cash handed over to the cashier.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Calculate Change Due)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">Change = £40.00 &minus; £30.60 = £9.40</div>
              <div class="solution-step-content">Subtract total spend from money tendered. Include currency sign and two decimal places.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">£9.40</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> Remember to calculate the change! Many candidates calculate the total cost (£30.60) and stop there without performing the final subtraction. Always re-read the final question prompt.</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Practice Question 3 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 3:</span> Comparing Trade Offers &amp; Discounts (Level 2)</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [4 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            A clinic facilities team needs to purchase an adjustable medical trolley. Two trade suppliers sell the identical trolley:
          </p>
          <ul style="padding-left:20px; line-height:1.75; color:#334155;">
            <li><strong>MedSupply Co:</strong> Normal price <strong>£260</strong> with a <strong>15% trade discount</strong>.</li>
            <li><strong>HealthDirect:</strong> Normal price <strong>£275</strong> with a <strong>£50 promotional voucher</strong> deducted at checkout.</li>
          </ul>
          <p>Which supplier is cheaper, and by how much? Show all your step-by-step working.</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad3"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad3" class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q3')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q3" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">4 / 4 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Calculate 15% Discount for MedSupply Co)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">15% of £260 = 0.15 &times; £260 = £39.00</div>
              <div class="solution-step-content">Find 15% of the original cost (10% = £26, 5% = £13; £26 + £13 = £39).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (MedSupply Co Discounted Price)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">MedSupply Price = £260 &minus; £39 = £221.00</div>
              <div class="solution-step-content">Subtract discount from normal price.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (HealthDirect Voucher Price)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">HealthDirect Price = £275 &minus; £50 = £225.00</div>
              <div class="solution-step-content">Deduct voucher from HealthDirect normal price.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 4 (Comparison &amp; Difference)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">Difference = £225.00 &minus; £221.00 = £4.00</div>
              <div class="solution-step-content">Compare prices and state clear conclusion: MedSupply Co is cheaper by £4.00.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">MedSupply Co is cheaper by £4.00</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> On "Which is cheaper?" questions, you must state BOTH parts of the conclusion: (1) the winning store name, and (2) the exact difference in money with correct £ symbol!</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>
    </section>

    <!-- PROGRESSION BANNER -->
    <section id="curriculum-links" class="progression-banner">
      <div>
        <h3 class="progression-title">Ready for Your Next Revision Step?</h3>
        <p style="color:#cbd5e1; margin:0; line-height:1.6;">
          Solidify your money skills by tackling multi-step percentage problems, ratio sharing, and best buys.
        </p>
      </div>
      <a href="functional-skills-percentages.html" class="btn-progression">
        Next: Percentages <i class="fa-solid fa-arrow-right"></i>
      </a>
    </section>
    """

    full_html = build_full_html(
        filename="functional-skills-money.html",
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file="functional-skills-percentages.html",
        next_name="Percentages"
    )

    out_path = os.path.join(PROJECT_DIR, "functional-skills-money.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[BESPOKE OK] Money generated ({len(full_html)} bytes)")

def build_volume_page():
    clean_topic = "Volume"
    subject = "Mathematics"
    subject_pill_icon = "fa-calculator"
    subject_dir = "functional-skills-maths-level-2.html"
    hero_title = "Volume: <span>Formulas, 3D Models &amp; Exam Practice</span>"
    intro_lead = "Comprehensive Functional Skills revision guide for 3D Volume calibrated to Pearson Edexcel &amp; City &amp; Guilds standards. Master cubes, cuboids, triangular prisms, cylinders, compound 3D solids, capacity conversions, and exam problem solving."

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
        ("skill-1", "1. Cubes &amp; Cuboids", "fa-cube"),
        ("skill-2", "2. Triangular Prisms", "fa-shapes"),
        ("skill-3", "3. Cylinders", "fa-database"),
        ("skill-4", "4. Compound 3D Solids", "fa-layer-group"),
        ("worked-exam-models", "Worked Exam Models", "fa-graduation-cap"),
        ("examiner-traps", "Examiner Traps", "fa-triangle-exclamation"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ]

    content_html = """
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#059669;"><i class="fa-solid fa-check"></i> Regulated Standards</span>
      </div>
      <div class="skill-card-container">
        <p>Candidates are assessed on the following regulated Functional Skills criteria:</p>
        <ul style="padding-left:20px; line-height:1.8; color:#334155; font-size:1.02rem;">
          <li><strong>L1.23:</strong> Calculate the volume of cubes and cuboids in everyday workplace and practical contexts.</li>
          <li><strong>L2.17:</strong> Calculate the volume of 3D shapes including cuboids, triangular prisms, and cylinders (using &pi; = 3.142 or given formulas for complex shapes like spheres and cones).</li>
          <li><strong>L2.18:</strong> Solve practical multi-step problems involving capacity and liquid volume conversions (1 cm&sup3; = 1 ml, 1,000 cm&sup3; = 1 litre, 1 m&sup3; = 1,000 litres).</li>
          <li>State correct 3D volumetric units in final solutions (e.g. cm&sup3;, m&sup3;, litres).</li>
        </ul>
      </div>
    </section>

    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Volume of 3D Shapes</h2>
      </div>

      <!-- Rule 1 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-cube"></i>
          <span>Golden Rule 1: Volume is 3D Space — Always State Cubic Units</span>
        </div>
        <p>
          Volume measures total internal 3D capacity. Answers <strong>must always include cubic units</strong> (e.g. <strong>cm&sup3;</strong>, <strong>m&sup3;</strong>, <strong>mm&sup3;</strong>). Writing cm or cm&sup2; loses accuracy marks on Functional Skills papers!
        </p>
        <div class="rule-highlight-badge">
          Examiner Check: Linear = cm &bull; Area = cm&sup2; &bull; Volume = cm&sup3;
        </div>
      </div>

      <!-- Rule 2 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-shapes"></i>
          <span>Golden Rule 2: Volume of ANY Uniform Prism = Area of Cross-Section &times; Length</span>
        </div>
        <p>
          A prism has identical faces at each end. To find its volume, simply calculate the area of the 2D end face (cross-section) and multiply by how far it extends (length or depth):
        </p>
        <div class="rule-highlight-badge">
          General Prism Formula: Volume = Area of Cross-Section &times; Length (V = A &times; L)
        </div>
      </div>

      <!-- Rule 3 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-arrows-split-up-and-left"></i>
          <span>Golden Rule 3: For Cylinders, Always Use the Radius (r), Never the Diameter</span>
        </div>
        <p>
          The cylinder formula is <strong>V = &pi; r&sup2; h</strong>. Exam questions frequently provide the <strong>diameter</strong> (the distance all the way across). You <strong>must halve the diameter</strong> to find the radius before squaring:
        </p>
        <div class="rule-highlight-badge">
          Trap Warning: Diameter = 1.2 m &rarr; Radius = 1.2 &divide; 2 = 0.6 m &rarr; Area = &pi; &times; (0.6)&sup2;
        </div>
      </div>

      <!-- Rule 4 -->
      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-faucet-drip"></i>
          <span>Golden Rule 4: Master the Liquid Capacity Conversions</span>
        </div>
        <p>
          Exam questions often ask for capacity in <strong>litres</strong>:
          <br>&bull; <strong>1 cm&sup3; = 1 ml</strong>
          <br>&bull; <strong>1,000 cm&sup3; = 1 litre</strong>
          <br>&bull; <strong>1 m&sup3; = 1,000 litres</strong> (1 cubic metre holds exactly one thousand litres of water).
        </p>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 1: CUBES & CUBOIDS -->
    <!-- ============================================== -->
    <section id="skill-1" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 1:</span> Volume of a Cuboid (Workplace Storage Container)
          </h3>
          <p class="pfs-card-stem">
            An NHS pharmacy distribution crate measures <strong>18 cm</strong> in length, <strong>12 cm</strong> in width, and <strong>15 cm</strong> in height. 
            Calculate the total volume of the crate in cubic centimetres (cm&sup3;).
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[2 Marks]</div>

            <div class="pfs-formula-display">
              Volume of Cuboid = Length &times; Width &times; Height = l &times; w &times; h
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Identify the three linear dimensions: Length = <strong>18 cm</strong>, Width = <strong>12 cm</strong>, Height = <strong>15 cm</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Multiply all three dimensions: <strong>18 &times; 12 &times; 15 = 3,240</strong>.</span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>State correct units of volume: <strong>cm&sup3;</strong>.</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Final Volume: 3,240 cm&sup3;</span>
              <span style="font-size:0.86rem;">Full 2 Marks</span>
            </div>
          </div>

          <!-- 3D Proportional SVG Diagram of Cuboid -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" style="width:100%; height:auto;">
              <defs>
                <marker id="arrV1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                </marker>
                <marker id="arrV1Rev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                  <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                </marker>
              </defs>

              <!-- Cuboid 3D Faces -->
              <!-- Top Face -->
              <polygon points="60,90 140,40 290,40 210,90" fill="#fb923c" stroke="#c2410c" stroke-width="2"/>
              <!-- Right Face -->
              <polygon points="210,90 290,40 290,140 210,190" fill="#c2410c" stroke="#9a3412" stroke-width="2"/>
              <!-- Front Face -->
              <polygon points="60,90 210,90 210,190 60,190" fill="#ea580c" stroke="#9a3412" stroke-width="2"/>

              <!-- Length Arrow & Label (Front Bottom) -->
              <line x1="60" y1="205" x2="210" y2="205" stroke="#0f172a" stroke-width="2" marker-start="url(#arrV1Rev)" marker-end="url(#arrV1)"/>
              <text x="135" y="218" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">18 cm (Length)</text>

              <!-- Height Arrow & Label (Left Edge) -->
              <line x1="42" y1="90" x2="42" y2="190" stroke="#0f172a" stroke-width="2" marker-start="url(#arrV1Rev)" marker-end="url(#arrV1)"/>
              <text x="36" y="145" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="end">15 cm</text>

              <!-- Width Arrow & Label (Top Slanted Depth) -->
              <line x1="140" y1="26" x2="290" y2="26" stroke="#0f172a" stroke-width="1.8" marker-start="url(#arrV1Rev)" marker-end="url(#arrV1)"/>
              <text x="215" y="20" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">12 cm (Width)</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 2: TRIANGULAR PRISMS -->
    <!-- ============================================== -->
    <section id="skill-2" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 2:</span> Volume of a Triangular Prism (Ventilation Duct)
          </h3>
          <p class="pfs-card-stem">
            A ventilation duct in an industrial facility has the shape of a triangular prism. 
            The front triangular cross-section has a horizontal base of <strong>6 m</strong> and a perpendicular height of <strong>4 m</strong>. 
            The prism extends along a length of <strong>14 m</strong>. Calculate the volume of air inside the duct.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>

            <div class="pfs-formula-display">
              Volume = Cross-Section Area &times; Length = (&frac12; &times; b &times; h) &times; L
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Calculate the triangular front face area: <br>
                  <strong>Area = (6 &times; 4) &divide; 2 = 24 &divide; 2 = 12 m&sup2;</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Multiply cross-sectional area by the length of the duct: <br>
                  <strong>Volume = 12 m&sup2; &times; 14 m = 168 m&sup3;</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>State cubic units: <strong>168 m&sup3;</strong>.</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Final Volume: 168 m&sup3;</span>
              <span style="font-size:0.86rem;">Full 3 Marks</span>
            </div>
          </div>

          <!-- 3D Proportional SVG Diagram of Triangular Prism -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" style="width:100%; height:auto;">
              <defs>
                <marker id="arrV2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                </marker>
                <marker id="arrV2Rev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                  <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                </marker>
              </defs>

              <!-- Prism Slanted Top Face -->
              <polygon points="50,60 180,30 260,150 130,180" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
              <!-- Front Triangle -->
              <polygon points="50,180 130,180 50,60" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>

              <!-- Perpendicular Height Line & Symbol Inside Front Triangle -->
              <line x1="50" y1="60" x2="50" y2="180" stroke="#ffffff" stroke-width="2" stroke-dasharray="4,3"/>
              <rect x="50" y="166" width="14" height="14" fill="none" stroke="#ffffff" stroke-width="1.8"/>
              <text x="35" y="125" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#0f172a">h = 4 m</text>

              <!-- Base Dimension (Bottom Front) -->
              <line x1="50" y1="195" x2="130" y2="195" stroke="#0f172a" stroke-width="2" marker-start="url(#arrV2Rev)" marker-end="url(#arrV2)"/>
              <text x="90" y="210" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Base = 6 m</text>

              <!-- Length Dimension (Along Depth Edge) -->
              <line x1="145" y1="185" x2="275" y2="155" stroke="#0f172a" stroke-width="2" marker-start="url(#arrV2Rev)" marker-end="url(#arrV2)"/>
              <text x="215" y="190" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">Length = 14 m</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Focus</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 3: CYLINDERS -->
    <!-- ============================================== -->
    <section id="skill-3" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 3:</span> Volume &amp; Capacity of a Cylinder (Water Storage Tank)
          </h3>
          <p class="pfs-card-stem">
            A vertical water storage cylinder has a circular base with diameter <strong>1.2 m</strong> and a height of <strong>2.5 m</strong>. 
            Using <strong>&pi; = 3.142</strong>, calculate the total volume of the cylinder in cubic metres (m&sup3;), rounded to 2 decimal places. 
            Then state its capacity in litres (1 m&sup3; = 1,000 litres).
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[4 Marks]</div>

            <div class="pfs-formula-display">
              Volume of Cylinder = &pi; &times; r&sup2; &times; h &nbsp;(&pi; = 3.142)
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Find the radius by halving the diameter: <br>
                  <strong>Radius (r) = 1.2 m &divide; 2 = 0.6 m</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Calculate circular base area (&pi; r&sup2;): <br>
                  <strong>Base Area = 3.142 &times; 0.6&sup2; = 3.142 &times; 0.36 = 1.13112 m&sup2;</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Multiply by cylinder height: <br>
                  <strong>Volume = 1.13112 &times; 2.5 = 2.8278 m&sup3; &asymp; 2.83 m&sup3; (to 2 d.p.)</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 4:</span>
                <span>Convert to litres (multiply by 1,000): <br>
                  <strong>Capacity = 2.8278 &times; 1,000 = 2,828 litres (or 2,830 litres)</strong>.
                </span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Volume: 2.83 m&sup3; &nbsp;|&nbsp; Capacity: 2,828 Litres</span>
              <span style="font-size:0.86rem;">Full 4 Marks</span>
            </div>
          </div>

          <!-- 3D Proportional SVG Diagram of Cylinder -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" style="width:100%; height:auto;">
              <defs>
                <marker id="arrV3" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                  <polygon points="0 0, 6 3, 0 6" fill="#0f172a" />
                </marker>
                <marker id="arrV3Rev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
                  <polygon points="6 0, 0 3, 6 6" fill="#0f172a" />
                </marker>
              </defs>

              <!-- Bottom Ellipse -->
              <ellipse cx="140" cy="170" rx="70" ry="25" fill="#047857" stroke="#065f46" stroke-width="2"/>
              <!-- Cylinder Body -->
              <rect x="70" y="60" width="140" height="110" fill="#059669" stroke="none"/>
              <line x1="70" y1="60" x2="70" y2="170" stroke="#065f46" stroke-width="2"/>
              <line x1="210" y1="60" x2="210" y2="170" stroke="#065f46" stroke-width="2"/>
              <!-- Top Ellipse -->
              <ellipse cx="140" cy="60" rx="70" ry="25" fill="#34d399" stroke="#065f46" stroke-width="2"/>

              <!-- Radius Line & Center Point on Top Ellipse -->
              <circle cx="140" cy="60" r="3.5" fill="#0f172a"/>
              <line x1="140" y1="60" x2="210" y2="60" stroke="#0f172a" stroke-width="2"/>
              <text x="175" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">r = 0.6 m</text>

              <!-- Height Dimension Arrow (Right Side) -->
              <line x1="230" y1="60" x2="230" y2="170" stroke="#0f172a" stroke-width="2" marker-start="url(#arrV3Rev)" marker-end="url(#arrV3)"/>
              <text x="245" y="120" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#0f172a">h = 2.5 m</text>

              <!-- Diameter Indicator Along Top -->
              <text x="140" y="24" font-family="'Inter', sans-serif" font-size="13" font-weight="700" fill="#64748b" text-anchor="middle">Diameter = 1.2 m</text>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Focus</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SKILL 4: COMPOUND 3D SOLIDS -->
    <!-- ============================================== -->
    <section id="skill-4" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Example 4:</span> Compound 3D Solids (Splitting Stepped Shapes)
          </h3>
          <p class="pfs-card-stem">
            A warehouse loading dock extension consists of an L-shaped concrete ramp. 
            The structure can be split into two separate cuboids: 
            <strong>Block A</strong> measures <strong>8 m long, 5 m wide, and 4 m high</strong>. 
            <strong>Block B</strong> measures <strong>6 m long, 3 m wide, and 4 m high</strong>. 
            Calculate the total volume of concrete required.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[3 Marks]</div>

            <div class="pfs-formula-display">
              Total Volume = Volume of Block A + Volume of Block B
            </div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Calculate Block A volume: <br>
                  <strong>Volume(A) = 8 m &times; 5 m &times; 4 m = 160 m&sup3;</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Calculate Block B volume: <br>
                  <strong>Volume(B) = 6 m &times; 3 m &times; 4 m = 72 m&sup3;</strong>.
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Add both volumes together: <br>
                  <strong>Total Volume = 160 m&sup3; + 72 m&sup3; = 232 m&sup3;</strong>.
                </span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Total Volume: 232 m&sup3;</span>
              <span style="font-size:0.86rem;">Full 3 Marks</span>
            </div>
          </div>

          <!-- 3D Proportional SVG Diagram of Compound L-Solid -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" style="width:100%; height:auto;">
              <!-- Block A (Left Big Block) -->
              <polygon points="30,80 90,45 190,45 130,80" fill="#a855f7" stroke="#7e22ce" stroke-width="2"/>
              <polygon points="130,80 190,45 190,140 130,175" fill="#7e22ce" stroke="#6b21a8" stroke-width="2"/>
              <polygon points="30,80 130,80 130,175 30,175" fill="#9333ea" stroke="#6b21a8" stroke-width="2"/>
              <text x="80" y="132" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">Block A</text>

              <!-- Block B (Right Step Block) -->
              <polygon points="130,115 170,90 270,90 230,115" fill="#c084fc" stroke="#7e22ce" stroke-width="2"/>
              <polygon points="230,115 270,90 270,175 230,200" fill="#7e22ce" stroke="#6b21a8" stroke-width="2"/>
              <polygon points="130,115 230,115 230,200 130,200" fill="#a855f7" stroke="#6b21a8" stroke-width="2"/>
              <text x="180" y="162" font-family="'Inter', sans-serif" font-size="15" font-weight="900" fill="#ffffff" text-anchor="middle">Block B</text>

              <!-- Dashed Red Split Line -->
              <line x1="130" y1="80" x2="130" y2="175" stroke="#ef4444" stroke-width="3" stroke-dasharray="5,4"/>
            </svg>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Focus</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- WORKED EXAM MODELS -->
    <!-- ============================================== -->
    <section id="worked-exam-models" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Pearson Edexcel Worked Exam Models</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#ea580c;"><i class="fa-solid fa-star"></i> Benchmark Solutions</span>
      </div>

      <!-- Model 1 -->
      <div class="pfs-card">
        <div class="pfs-card-head">
          <h3 class="pfs-card-title">
            <span class="pfs-prefix">Exam Model 1:</span> Water Tank Capacity &amp; Filling Rate (Level 2)
          </h3>
          <p class="pfs-card-stem">
            A healthcare hydrotherapy tank measures <strong>3.5 m in length, 2 m in width, and 1.8 m in depth</strong>. 
            Water is pumped into the empty tank at a steady rate of <strong>420 litres per minute</strong>. 
            Given that <strong>1 m&sup3; = 1,000 litres</strong>, determine how many minutes it will take to fill the tank completely.
          </p>
        </div>

        <div class="pfs-card-body">
          <div class="pfs-math-col">
            <div class="pfs-marks-row">[4 Marks]</div>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1:</span>
                <span>Calculate total tank volume in cubic metres: <br>
                  <strong>Volume = 3.5 &times; 2 &times; 1.8 = 12.6 m&sup3;</strong> [M1 Method Mark].
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2:</span>
                <span>Convert cubic metres to litres (multiply by 1,000): <br>
                  <strong>Capacity = 12.6 &times; 1,000 = 12,600 litres</strong> [M1 Method Mark].
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3:</span>
                <span>Divide total litres by pump flow rate: <br>
                  <strong>Time = 12,600 &divide; 420 = 30 minutes</strong> [M1 Method Mark].
                </span>
              </div>
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 4:</span>
                <span>State clear final answer with units: <strong>30 minutes</strong> [A1 Accuracy Mark].</span>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <span><i class="fa-solid fa-circle-check"></i> Total Filling Time: 30 Minutes</span>
              <span style="font-size:0.86rem;">Full 4 Marks</span>
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Focus</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- EXAMINER TRAPS -->
    <!-- ============================================== -->
    <section id="examiner-traps" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation"></i> Common Examiner Traps &amp; How to Avoid Them</h2>
      </div>

      <div class="trap-card-rose">
        <div class="trap-card-rose-header">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>Trap 1: Forgetting to Divide by 2 on Triangular Prisms</span>
        </div>
        <p>
          The most frequent calculation loss on Paper 2 is multiplying Base &times; Height &times; Length without halving for the triangular cross-section face. Always write <strong>(b &times; h &divide; 2) &times; L</strong> first.
        </p>
      </div>

      <div class="trap-card-rose">
        <div class="trap-card-rose-header">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>Trap 2: Mixing Centimetres and Metres</span>
        </div>
        <p>
          Examiners love giving two dimensions in metres and one in centimetres (e.g. Length = 4 m, Width = 2.5 m, Depth = 60 cm). Convert <strong>60 cm = 0.6 m</strong> before multiplying. Multiplying mixed units produces a catastrophic answer that forfeits method marks!
        </p>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- INTERACTIVE EXAM PRACTICE QUESTIONS -->
    <!-- ============================================== -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
        <span style="font-size:0.9rem; color:#64748b; font-weight:700;">3 Practice Tasks</span>
      </div>
      <p class="section-lead-text">
        Apply your knowledge to these authentic Pearson Edexcel style exam questions. Type your working in the scratchpad, then reveal the model mark scheme to evaluate your marks.
      </p>

      <!-- Practice Question 1 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 1:</span> Medical Sample Insulated Dispatch Box</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [2 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            An insulated courier box used to transport refrigerated vaccine vials has external dimensions of: 
            length <strong>25 cm</strong>, width <strong>16 cm</strong>, and height <strong>14 cm</strong>.
          </p>
          <p>Calculate the total volume of the box in cubic centimetres (cm&sup3;).</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad1"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad1" class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q1')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q1" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">2 / 2 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Multiply Dimensions)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">25 &times; 16 &times; 14 = 5,600</div>
              <div class="solution-step-content">Multiply length by width by height.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Units &amp; Accuracy)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">5,600 cm&sup3;</div>
              <div class="solution-step-content">State correct numerical answer with cubic units (cm&sup3;).</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">5,600 cm&sup3;</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> In non-calculator papers, break the multiplication into easy stages: 25 &times; 16 = 400; then 400 &times; 14 = 5,600.</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Practice Question 2 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 2:</span> Horticultural Glasshouse Roof Air Space</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            A community greenhouse has a roof triangular prism section. 
            The front triangular gable end has a base of <strong>8 m</strong> and a perpendicular height of <strong>3.5 m</strong>. 
            The greenhouse is <strong>12 m long</strong>.
          </p>
          <p>Work out the total volume of the roof section in cubic metres (m&sup3;).</p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad2"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad2" class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q2')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q2" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Triangular Face Area)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Area = (8 &times; 3.5) &divide; 2 = 28 &divide; 2 = 14 m&sup2;</div>
              <div class="solution-step-content">Calculate the area of the triangular cross-section by dividing the product of base and height by 2.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Prism Volume Calculation)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Volume = 14 m&sup2; &times; 12 m = 168 m&sup3;</div>
              <div class="solution-step-content">Multiply cross-sectional area by the length of the prism.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Accuracy &amp; Units)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">168 m&sup3;</div>
              <div class="solution-step-content">Correct final answer with cubic metres units.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">168 m&sup3;</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> Be sure to write the formula <code>Area = (b &times; h) / 2</code> in your exam script. Even if you make an arithmetic error in the final multiplication, writing the formula guarantees M1 method credit.</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- Practice Question 3 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 3:</span> Chemical Storage Cylindrical Drum (Level 2)</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [4 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>
            An industrial cleaning supplier manufactures a cylindrical storage drum with:
            radius <strong>0.4 m</strong> and height <strong>1.5 m</strong>.
          </p>
          <p>
            (a) Using <strong>&pi; = 3.142</strong>, calculate the volume of the drum in cubic metres, rounded to 2 decimal places. <br>
            (b) Given that <strong>1 m&sup3; = 1,000 litres</strong>, calculate how many whole 25-litre containers can be filled from one completely full drum.
          </p>
        </div>

        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="pad3"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="pad3" class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
        </div>

        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('drawer-q3')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>

        <div id="drawer-q3" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">4 / 4 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Calculate Cylinder Volume)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">V = 3.142 &times; 0.4&sup2; &times; 1.5 = 3.142 &times; 0.16 &times; 1.5 = 0.75408 m&sup3;</div>
              <div class="solution-step-content">Apply cylinder volume formula &pi; &times; r&sup2; &times; h.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Round Volume to 2 d.p.)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">0.75 m&sup3;</div>
              <div class="solution-step-content">Round correctly: 0.75408 rounds to 0.75 m&sup3;.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Convert to Litres)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Capacity = 0.75408 &times; 1,000 = 754.08 litres (or 0.75 &times; 1,000 = 750 litres)</div>
              <div class="solution-step-content">Multiply cubic metres by 1,000 to convert to capacity in litres.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 4 (Whole Containers Filled)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">754.08 &divide; 25 = 30.16 &rarr; Exactly 30 whole containers</div>
              <div class="solution-step-content">Divide capacity by 25. Round DOWN to nearest integer because the remaining 0.16 does not fill a whole container.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">Volume: 0.75 m&sup3; &nbsp;|&nbsp; 30 whole containers</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> On "How many whole containers?" questions, always truncate/round DOWN to the nearest integer. You cannot sell or use a partial container as a whole one!</span>
          </div>
        </div>

        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>
    </section>

    <!-- PROGRESSION BANNER -->
    <section id="curriculum-links" class="progression-banner">
      <div>
        <h3 class="progression-title">Ready for Your Next Revision Step?</h3>
        <p style="color:#cbd5e1; margin:0; line-height:1.6;">
          Connect volume with real-world problems: examine surface area of 3D solids and compound unit density calculations.
        </p>
      </div>
      <a href="functional-skills-surface-area.html" class="btn-progression">
        Next: Surface Area <i class="fa-solid fa-arrow-right"></i>
      </a>
    </section>
    """

    full_html = build_full_html(
        filename="functional-skills-volume.html",
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file="functional-skills-surface-area.html",
        next_name="Surface Area"
    )

    out_path = os.path.join(PROJECT_DIR, "functional-skills-volume.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[BESPOKE OK] Volume generated ({len(full_html)} bytes)")


def build_percentages_page():
    clean_topic = "Percentages"
    subject = "Mathematics"
    subject_pill_icon = "fa-calculator"
    subject_dir = "functional-skills-maths-level-2.html"
    hero_title = "Percentages: <span>Calculations, Multipliers &amp; Exam Models</span>"
    intro_lead = "Master essential percentage calculations calibrated to Pearson Edexcel &amp; City &amp; Guilds Functional Skills standards. Learn mental non-calculator building blocks, percentage of amounts, one quantity as a percentage of another, percentage increase &amp; decrease with decimal multipliers, and reverse percentages."

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
        ("benchmark-guide", "Visual Benchmarks", "fa-chart-pie"),
        ("skill-1", "1. Percentage of Amount", "fa-percent"),
        ("skill-2", "2. Expressing as a %", "fa-chart-simple"),
        ("skill-3", "3. Percentage Increase", "fa-arrow-trend-up"),
        ("skill-4", "4. Percentage Decrease", "fa-arrow-trend-down"),
        ("skill-5", "5. Reverse Percentages", "fa-rotate-left"),
        ("worked-exam-models", "Worked Exam Models", "fa-graduation-cap"),
        ("examiner-traps", "Examiner Traps", "fa-triangle-exclamation"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ]

    content_html = """
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#059669;"><i class="fa-solid fa-check"></i> Regulated Standards</span>
      </div>
      <div class="skill-card-container">
        <p>Candidates must demonstrate mastery of the following regulated Functional Skills criteria:</p>
        <ul style="padding-left:20px; line-height:1.8; color:#334155; font-size:1.02rem;">
          <li><strong>L1.13:</strong> Read, write, order and compare percentages in whole numbers.</li>
          <li><strong>L1.14:</strong> Calculate percentages of quantities, including simple percentage increases and decreases by 5% and multiples thereof with and without a calculator.</li>
          <li><strong>L2.5:</strong> Work out percentages of amounts and express one amount as a percentage of another.</li>
          <li><strong>L2.6:</strong> Calculate percentage change (any size increase and decrease) and original value after percentage change (Reverse Percentages).</li>
          <li>Format all monetary outputs to two decimal places (e.g. £96.00) and verify answers against realistic workplace contexts.</li>
        </ul>
      </div>
    </section>

    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Percentage Mastery</h2>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-cubes-stacked"></i>
          <span>Golden Rule 1: Master the Non-Calculator Building Blocks (10%, 1%, 5%, 50%)</span>
        </div>
        <p style="margin-bottom:0.75rem; line-height:1.65; color:#334155;">
          For non-calculator exams, never multiply by large fractions manually. Build every percentage from basic building blocks:
        </p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px; margin-bottom:0.75rem;">
          <div style="background:#fff; border:1px solid #cbd5e1; border-radius:8px; padding:10px; text-align:center;">
            <strong style="color:#0284c7; font-size:1.1rem; display:block;">10%</strong>
            <span style="font-size:0.85rem; color:#64748b;">Divide by 10</span>
          </div>
          <div style="background:#fff; border:1px solid #cbd5e1; border-radius:8px; padding:10px; text-align:center;">
            <strong style="color:#0284c7; font-size:1.1rem; display:block;">1%</strong>
            <span style="font-size:0.85rem; color:#64748b;">Divide by 100</span>
          </div>
          <div style="background:#fff; border:1px solid #cbd5e1; border-radius:8px; padding:10px; text-align:center;">
            <strong style="color:#0284c7; font-size:1.1rem; display:block;">5%</strong>
            <span style="font-size:0.85rem; color:#64748b;">Half of 10%</span>
          </div>
          <div style="background:#fff; border:1px solid #cbd5e1; border-radius:8px; padding:10px; text-align:center;">
            <strong style="color:#0284c7; font-size:1.1rem; display:block;">50%</strong>
            <span style="font-size:0.85rem; color:#64748b;">Divide by 2</span>
          </div>
          <div style="background:#fff; border:1px solid #cbd5e1; border-radius:8px; padding:10px; text-align:center;">
            <strong style="color:#0284c7; font-size:1.1rem; display:block;">25%</strong>
            <span style="font-size:0.85rem; color:#64748b;">Half of 50%</span>
          </div>
        </div>
        <div class="rule-highlight-badge">
          Example: 15% of £480 = 10% (£48) + 5% (£24) = <strong>£72.00</strong>
        </div>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-calculator"></i>
          <span>Golden Rule 2: Multiplier Mastery for Calculator Papers</span>
        </div>
        <p style="margin-bottom:0.75rem; line-height:1.65; color:#334155;">
          On calculator papers, solve percentage increases and decreases in a single multiplication by converting the final percentage into a decimal multiplier:
        </p>
        <ul style="padding-left:20px; line-height:1.75; color:#334155; margin-bottom:0.75rem;">
          <li><strong>Increase by 6%:</strong> 100% + 6% = 106% &rarr; Multiplier is <strong>1.06</strong></li>
          <li><strong>Increase by 15%:</strong> 100% + 15% = 115% &rarr; Multiplier is <strong>1.15</strong></li>
          <li><strong>Decrease by 20%:</strong> 100% &minus; 20% = 80% &rarr; Multiplier is <strong>0.80</strong></li>
          <li><strong>Decrease by 7.5%:</strong> 100% &minus; 7.5% = 92.5% &rarr; Multiplier is <strong>0.925</strong></li>
        </ul>
        <div class="rule-highlight-badge">
          Examiner Check: An increase always produces a multiplier &gt; 1; a decrease always produces a multiplier &lt; 1.
        </div>
      </div>

      <div class="rule-card-amber">
        <div class="rule-card-amber-header">
          <i class="fa-solid fa-rotate-left"></i>
          <span>Golden Rule 3: The Golden Law of Reverse Percentages</span>
        </div>
        <p style="margin-bottom:0.5rem; line-height:1.65; color:#334155;">
          When an exam question gives the <strong>final value after</strong> a percentage increase or discount and asks for the <strong>original starting price</strong>:
        </p>
        <div style="background:#fff; border-left:4px solid #d97706; padding:10px 16px; border-radius:4px; font-weight:700; color:#92400e; margin-bottom:0.75rem;">
          Original Amount = Final Amount &divide; Multiplier
        </div>
        <p style="margin:0; line-height:1.65; color:#334155;">
          <strong>Fatal Mistake:</strong> NEVER calculate the percentage of the final price and subtract or add it. The percentage was taken from the original unknown amount, not the final amount!
        </p>
      </div>
    </section>

    <!-- VISUAL BENCHMARK GUIDE -->
    <section id="benchmark-guide" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-chart-pie"></i> Essential Visual Benchmarks (Fractions, Decimals &amp; %)</h2>
      </div>
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:24px; box-shadow:0 4px 16px rgba(0,0,0,0.04);">
        <p style="color:#475569; margin-top:0; margin-bottom:1.25rem; font-size:1.02rem;">
          These core benchmarks appear constantly across Pearson Edexcel Level 1 and Level 2 exam papers. Memorizing these equivalents guarantees swift method marks:
        </p>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">50%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">Half</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong>&frac12;</strong> &nbsp;|&nbsp; Decimal: <strong>0.50</strong><br>
              Mental rule: Divide total by <strong>2</strong>
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">25%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">Quarter</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong>&frac14;</strong> &nbsp;|&nbsp; Decimal: <strong>0.25</strong><br>
              Mental rule: Half of 50%, or divide total by <strong>4</strong>
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">75%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">Three Quarters</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong>&frac34;</strong> &nbsp;|&nbsp; Decimal: <strong>0.75</strong><br>
              Mental rule: 50% + 25%, or &times; 3 after finding &frac14;
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">10%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">One Tenth</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong><sup>1</sup>&frasl;<sub>10</sub></strong> &nbsp;|&nbsp; Decimal: <strong>0.10</strong><br>
              Mental rule: Shift decimal point 1 place left (&divide; 10)
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">20%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">One Fifth</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong><sup>1</sup>&frasl;<sub>5</sub></strong> &nbsp;|&nbsp; Decimal: <strong>0.20</strong><br>
              Mental rule: Double 10%, or divide total by <strong>5</strong>
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span style="font-weight:800; font-size:1.2rem; color:#0284c7;">5%</span>
              <span style="background:#e0f2fe; color:#0369a1; font-weight:700; padding:2px 8px; border-radius:6px; font-size:0.85rem;">One Twentieth</span>
            </div>
            <div style="font-size:0.95rem; color:#334155; line-height:1.6;">
              Fraction: <strong><sup>1</sup>&frasl;<sub>20</sub></strong> &nbsp;|&nbsp; Decimal: <strong>0.05</strong><br>
              Mental rule: Halve the 10% value
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SKILL 1: PERCENTAGE OF AN AMOUNT -->
    <section id="skill-1" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Skill 1:</span> Calculating a Percentage of an Amount
          </div>
          <span style="font-size:0.82rem; font-weight:700; background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:20px;">
            Level 1 &amp; Level 2 Core Skill
          </span>
        </div>

        <div class="pfs-card-body">
          <!-- LEFT MATH COLUMN -->
          <div class="pfs-math-col">
            <div class="pfs-formula-display">
              <div class="pfs-formula-label">Core Formula</div>
              <div class="pfs-formula-value">Amount = (Percentage &divide; 100) &times; Total</div>
            </div>

            <p style="font-size:1.02rem; line-height:1.65; color:#334155; margin-bottom:1rem;">
              <strong>Workplace Scenario:</strong> An NHS outpatient clinic is allocated a monthly consumable budget of <strong>£640.00</strong>. Management specifies that exactly <strong>15%</strong> of this budget must be reserved for surgical personal protective equipment (PPE).<br>
              How much money must be reserved for PPE?
            </p>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1</span>
                <div class="pfs-step-content">
                  <strong>Find 10% (The primary building block):</strong><br>
                  Divide the total sum by 10:<br>
                  <span class="solution-step-math">£640.00 &divide; 10 = £64.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2</span>
                <div class="pfs-step-content">
                  <strong>Find 5% (Half of 10%):</strong><br>
                  Halve the 10% figure calculated in Step 1:<br>
                  <span class="solution-step-math">£64.00 &divide; 2 = £32.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3</span>
                <div class="pfs-step-content">
                  <strong>Combine blocks to achieve 15%:</strong><br>
                  Add the 10% and 5% values together:<br>
                  <span class="solution-step-math">£64.00 + £32.00 = £96.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag" style="color:#0284c7;">Check:</span>
                <div class="pfs-step-content">
                  <strong>Calculator Method Verification:</strong><br>
                  Convert 15% to a decimal multiplier (15 &divide; 100 = 0.15):<br>
                  <span class="solution-step-math">0.15 &times; £640.00 = £96.00</span>
                </div>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <i class="fa-solid fa-circle-check"></i>
              <div>
                <strong>Reserved PPE Allocation:</strong>
                <span style="font-size:1.35rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">£96.00</span>
              </div>
            </div>
          </div>

          <!-- RIGHT DIAGRAM COLUMN -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 210" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
              <!-- Main 100% Bar -->
              <rect x="25" y="30" width="290" height="44" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="6"/>
              <text x="170" y="57" fill="#0369a1" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Total Budget = £640.00 (100%)</text>
              
              <!-- 10% slice: 105px -->
              <rect x="25" y="90" width="105" height="44" fill="#0284c7" stroke="#0369a1" stroke-width="1.5" rx="5"/>
              <text x="77" y="110" fill="#ffffff" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">10%</text>
              <text x="77" y="125" fill="#e0f2fe" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">£64.00</text>
              
              <!-- 5% slice: 60px -->
              <rect x="136" y="90" width="60" height="44" fill="#0ea5e9" stroke="#0284c7" stroke-width="1.5" rx="5"/>
              <text x="166" y="110" fill="#ffffff" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">5%</text>
              <text x="166" y="125" fill="#e0f2fe" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">£32.00</text>
              
              <!-- Remaining 85% slice -->
              <rect x="202" y="90" width="113" height="44" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3" rx="5"/>
              <text x="258" y="117" fill="#64748b" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">85% (£544)</text>
              
              <!-- Result Pill Box -->
              <rect x="25" y="150" width="290" height="46" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5" rx="6"/>
              <text x="170" y="170" fill="#065f46" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Combined 15% Allocation</text>
              <text x="170" y="186" fill="#047857" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">£64.00 + £32.00 = £96.00</text>
            </svg>
            <div style="font-size:0.86rem; color:#475569; margin-top:10px; line-height:1.5; text-align:center;">
              <strong>Mental Math Trick:</strong> To calculate 15% swiftly, always calculate 10% first, halve it for 5%, and add both figures together.
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 2: ONE AMOUNT AS A PERCENTAGE OF ANOTHER -->
    <section id="skill-2" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Skill 2:</span> Expressing One Amount as a Percentage of Another
          </div>
          <span style="font-size:0.82rem; font-weight:700; background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:20px;">
            Core Compliance &amp; Audit Skill
          </span>
        </div>

        <div class="pfs-card-body">
          <!-- LEFT MATH COLUMN -->
          <div class="pfs-math-col">
            <div class="pfs-formula-display">
              <div class="pfs-formula-label">Percentage of a Whole Formula</div>
              <div class="pfs-formula-value">Percentage = (Part &divide; Whole) &times; 100%</div>
            </div>

            <p style="font-size:1.02rem; line-height:1.65; color:#334155; margin-bottom:1rem;">
              <strong>Workplace Scenario:</strong> Meadow View Care Centre employs <strong>80</strong> healthcare support workers. An internal training audit reveals that <strong>68</strong> workers have completed mandatory Infection Prevention and Control certification.<br>
              What percentage of the workforce has completed the certification?
            </p>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1</span>
                <div class="pfs-step-content">
                  <strong>Formulate the fraction:</strong><br>
                  Place the compliant part over the total whole workforce:<br>
                  <span class="solution-step-math">Fraction = 68 &divide; 80</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2</span>
                <div class="pfs-step-content">
                  <strong>Convert the fraction to a decimal:</strong><br>
                  Divide the numerator by the denominator (use bus stop or calculator):<br>
                  <span class="solution-step-math">68 &divide; 80 = 0.85</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3</span>
                <div class="pfs-step-content">
                  <strong>Multiply by 100 to convert to a percentage:</strong><br>
                  Shift the decimal point two places to the right:<br>
                  <span class="solution-step-math">0.85 &times; 100% = 85%</span>
                </div>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <i class="fa-solid fa-circle-check"></i>
              <div>
                <strong>Workforce Certification Rate:</strong>
                <span style="font-size:1.35rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">85% Completed</span>
              </div>
            </div>
          </div>

          <!-- RIGHT DIAGRAM COLUMN -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 210" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
              <text x="170" y="24" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Staff Training Compliance Gauge</text>
              
              <rect x="25" y="44" width="290" height="42" fill="#e2e8f0" rx="8" stroke="#cbd5e1" stroke-width="1.5"/>
              <rect x="25" y="44" width="246" height="42" fill="#10b981" rx="8" stroke="#059669" stroke-width="1.5"/>
              
              <text x="145" y="70" fill="#ffffff" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">68 Certified (85%)</text>
              <text x="293" y="70" fill="#64748b" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">15%</text>
              
              <rect x="25" y="104" width="290" height="92" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="8"/>
              <text x="40" y="128" fill="#334155" font-size="12" font-weight="700" font-family="'Inter', sans-serif">Division Method:</text>
              <text x="170" y="152" fill="#0284c7" font-size="16" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">68 &divide; 80 = 0.85</text>
              
              <text x="170" y="178" fill="#059669" font-size="14" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">0.85 &times; 100 = 85% ✓ (Meets Target)</text>
            </svg>
            <div style="font-size:0.86rem; color:#475569; margin-top:10px; line-height:1.5; text-align:center;">
              <strong>Rule to Remember:</strong> Divide the quantity you are interested in (68) by the total possible amount (80), then multiply by 100.
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 3: PERCENTAGE INCREASE -->
    <section id="skill-3" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Skill 3:</span> Percentage Increase (Multiplier Method)
          </div>
          <span style="font-size:0.82rem; font-weight:700; background:#fef3c7; color:#92400e; padding:4px 10px; border-radius:20px;">
            High-Value Level 2 Exam Topic
          </span>
        </div>

        <div class="pfs-card-body">
          <!-- LEFT MATH COLUMN -->
          <div class="pfs-math-col">
            <div class="pfs-formula-display">
              <div class="pfs-formula-label">The Increase Multiplier</div>
              <div class="pfs-formula-value">Increased Value = Original Value &times; (1 + Percentage &divide; 100)</div>
            </div>

            <p style="font-size:1.02rem; line-height:1.65; color:#334155; margin-bottom:1rem;">
              <strong>Workplace Scenario:</strong> An NHS senior support worker earns <strong>£22,400.00</strong> annually. Following a national pay award, all staff receive a <strong>4.5%</strong> salary increase.<br>
              Calculate their new annual salary.
            </p>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1</span>
                <div class="pfs-step-content">
                  <strong>Determine the percentage multiplier:</strong><br>
                  Add the increase to the 100% original baseline and convert to a decimal:<br>
                  <span class="solution-step-math">100% + 4.5% = 104.5% &rarr; 104.5 &divide; 100 = 1.045</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2</span>
                <div class="pfs-step-content">
                  <strong>Multiply original salary by multiplier:</strong><br>
                  Single-step calculation for full method marks:<br>
                  <span class="solution-step-math">£22,400.00 &times; 1.045 = £23,408.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag" style="color:#0284c7;">Non-Calc:</span>
                <div class="pfs-step-content">
                  <strong>Non-Calculator Verification:</strong><br>
                  1% = £224.00 &rarr; 4% = £896.00 &rarr; 0.5% = £112.00<br>
                  Total increase = £896.00 + £112.00 = £1,008.00<br>
                  New salary = £22,400.00 + £1,008.00 = £23,408.00
                </div>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <i class="fa-solid fa-circle-check"></i>
              <div>
                <strong>New Increased Annual Salary:</strong>
                <span style="font-size:1.35rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">£23,408.00</span>
              </div>
            </div>
          </div>

          <!-- RIGHT DIAGRAM COLUMN -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 210" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
              <text x="170" y="24" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Percentage Increase Multiplier</text>
              
              <rect x="25" y="42" width="290" height="38" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5" rx="6"/>
              <text x="170" y="66" fill="#1e293b" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Baseline Original = 100% (1.00)</text>
              
              <rect x="25" y="94" width="290" height="100" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5" rx="6"/>
              <text x="40" y="120" fill="#065f46" font-size="13" font-weight="800" font-family="'Inter', sans-serif">▲ Percentage Increase (+4.5%)</text>
              <text x="40" y="145" fill="#047857" font-size="12" font-weight="600" font-family="'Inter', sans-serif">100% + 4.5% = 104.5% &rarr; Multiplier = <tspan font-weight="800">1.045</tspan></text>
              <text x="40" y="172" fill="#065f46" font-size="14" font-weight="800" font-family="'Inter', sans-serif">£22,400 &times; 1.045 = £23,408.00</text>
            </svg>
            <div style="font-size:0.86rem; color:#475569; margin-top:10px; line-height:1.5; text-align:center;">
              <strong>Speed Rule:</strong> For an increase, always add to 100%. The decimal multiplier will always be greater than 1 (1.045).
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 4: PERCENTAGE DECREASE -->
    <section id="skill-4" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Skill 4:</span> Percentage Decrease (Multiplier Method)
          </div>
          <span style="font-size:0.82rem; font-weight:700; background:#fee2e2; color:#991b1b; padding:4px 10px; border-radius:20px;">
            High-Value Level 2 Exam Topic
          </span>
        </div>

        <div class="pfs-card-body">
          <!-- LEFT MATH COLUMN -->
          <div class="pfs-math-col">
            <div class="pfs-formula-display" style="border-color:#f43f5e; background:rgba(244,63,94,0.04);">
              <div class="pfs-formula-label" style="color:#be123c;">The Decrease Multiplier</div>
              <div class="pfs-formula-value" style="color:#be123c;">Decreased Value = Original Value &times; (1 &minus; Percentage &divide; 100)</div>
            </div>

            <p style="font-size:1.02rem; line-height:1.65; color:#334155; margin-bottom:1rem;">
              <strong>Workplace Scenario:</strong> A patient transport service currently consumes <strong>5,200 litres</strong> of fuel per quarter. Route optimization and hybrid engines decrease fuel consumption by <strong>15%</strong>.<br>
              How many litres are used now?
            </p>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1</span>
                <div class="pfs-step-content">
                  <strong>Determine the decrease multiplier:</strong><br>
                  Subtract the percentage decrease from 100%:<br>
                  <span class="solution-step-math">100% &minus; 15% = 85% &rarr; Multiplier = 0.85</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2</span>
                <div class="pfs-step-content">
                  <strong>Calculate new reduced fuel volume:</strong><br>
                  Multiply the original amount by 0.85:<br>
                  <span class="solution-step-math">5,200 &times; 0.85 = 4,420 litres</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag" style="color:#0284c7;">Non-Calc:</span>
                <div class="pfs-step-content">
                  <strong>Non-Calculator Check:</strong><br>
                  10% of 5,200 = 520 L &rarr; 5% = 260 L<br>
                  15% = 520 + 260 = 780 L reduction<br>
                  5,200 &minus; 780 = 4,420 litres
                </div>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <i class="fa-solid fa-circle-check"></i>
              <div>
                <strong>Reduced Fuel Consumption:</strong>
                <span style="font-size:1.35rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">4,420 litres</span>
              </div>
            </div>
          </div>

          <!-- RIGHT DIAGRAM COLUMN -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 210" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
              <text x="170" y="24" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Percentage Decrease Multiplier</text>
              
              <rect x="25" y="42" width="290" height="38" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5" rx="6"/>
              <text x="170" y="66" fill="#1e293b" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Baseline Original = 100% (1.00)</text>
              
              <rect x="25" y="94" width="290" height="100" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5" rx="6"/>
              <text x="40" y="120" fill="#9f1239" font-size="13" font-weight="800" font-family="'Inter', sans-serif">▼ Percentage Decrease (&minus;15%)</text>
              <text x="40" y="145" fill="#be123c" font-size="12" font-weight="600" font-family="'Inter', sans-serif">100% &minus; 15% = 85% &rarr; Multiplier = <tspan font-weight="800">0.85</tspan></text>
              <text x="40" y="172" fill="#9f1239" font-size="14" font-weight="800" font-family="'Inter', sans-serif">5,200 L &times; 0.85 = 4,420 Litres</text>
            </svg>
            <div style="font-size:0.86rem; color:#475569; margin-top:10px; line-height:1.5; text-align:center;">
              <strong>Speed Rule:</strong> For a decrease, always subtract from 100%. The decimal multiplier will always be less than 1 (0.85).
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l1">Level 1</span>
          <span class="pfs-pill-l2">Level 2</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- SKILL 5: REVERSE PERCENTAGES -->
    <section id="skill-5" class="revision-section">
      <div class="pfs-card">
        <div class="pfs-card-head">
          <div class="pfs-card-title">
            <span class="pfs-prefix">Skill 5:</span> Reverse Percentages (Finding the Original Value)
          </div>
          <span style="font-size:0.82rem; font-weight:700; background:#fce7f3; color:#9d174d; padding:4px 10px; border-radius:20px;">
            Level 2 Distinction &amp; Pass Criterion
          </span>
        </div>

        <div class="pfs-card-body">
          <!-- LEFT MATH COLUMN -->
          <div class="pfs-math-col">
            <div class="pfs-formula-display" style="border-color:#ec4899; background:rgba(236,72,153,0.04);">
              <div class="pfs-formula-label" style="color:#be185d;">The Reverse Percentage Formula</div>
              <div class="pfs-formula-value" style="color:#be185d;">Original Amount = Final Amount &divide; Multiplier</div>
            </div>

            <p style="font-size:1.02rem; line-height:1.65; color:#334155; margin-bottom:1rem;">
              <strong>Workplace Scenario:</strong> An NHS trust purchases an ultrasonic diagnostic scanner. The total supplier invoice including <strong>20% VAT</strong> is <strong>£648.00</strong>.<br>
              Calculate the original pre-VAT price of the scanner before the tax was applied.
            </p>

            <div class="pfs-steps-box">
              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 1</span>
                <div class="pfs-step-content">
                  <strong>Recognise the percentage representation:</strong><br>
                  The final invoice represents 100% of the equipment price plus 20% VAT:<br>
                  <span class="solution-step-math">100% + 20% = 120% = £648.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 2</span>
                <div class="pfs-step-content">
                  <strong>Find the decimal multiplier:</strong><br>
                  Convert 120% into a decimal:<br>
                  <span class="solution-step-math">120 &divide; 100 = 1.20</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag">Step 3</span>
                <div class="pfs-step-content">
                  <strong>Divide the invoice amount by the multiplier:</strong><br>
                  <span class="solution-step-math">£648.00 &divide; 1.20 = £540.00</span>
                </div>
              </div>

              <div class="pfs-step-row">
                <span class="pfs-step-tag" style="color:#10b981;">Verify:</span>
                <div class="pfs-step-content">
                  <strong>Sanity Check (Add 20% back on):</strong><br>
                  10% of £540 = £54.00 &rarr; 20% = £108.00<br>
                  £540.00 + £108.00 = £648.00 (Matches invoice exactly!)
                </div>
              </div>
            </div>

            <div class="pfs-answer-banner">
              <i class="fa-solid fa-circle-check"></i>
              <div>
                <strong>Original Pre-VAT Price:</strong>
                <span style="font-size:1.35rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">£540.00</span>
              </div>
            </div>
          </div>

          <!-- RIGHT DIAGRAM COLUMN -->
          <div class="pfs-diagram-col">
            <svg viewBox="0 0 340 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
              <text x="170" y="22" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Invoice Total: £648.00 (120%)</text>
              
              <!-- 100% Original Block -->
              <rect x="25" y="36" width="225" height="46" fill="#0284c7" stroke="#0369a1" stroke-width="1.5" rx="6"/>
              <text x="137" y="56" fill="#ffffff" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Original Base (100%)</text>
              <text x="137" y="73" fill="#e0f2fe" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">£540.00</text>
              
              <!-- 20% VAT Block -->
              <rect x="255" y="36" width="60" height="46" fill="#f43f5e" stroke="#be123c" stroke-width="1.5" rx="6"/>
              <text x="285" y="56" fill="#ffffff" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+20%</text>
              <text x="285" y="72" fill="#ffe4e6" font-size="10" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">£108</text>
              
              <!-- Correct Operation Box -->
              <rect x="25" y="96" width="290" height="44" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5" rx="6"/>
              <text x="170" y="115" fill="#065f46" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Correct Step: Divide by 1.20</text>
              <text x="170" y="131" fill="#047857" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">£648.00 &divide; 1.20 = £540.00 ✓</text>
              
              <!-- Trap Warning Box -->
              <rect x="25" y="152" width="290" height="52" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5" rx="6"/>
              <text x="170" y="172" fill="#be123c" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">❌ Common Fatal Exam Error:</text>
              <text x="170" y="191" fill="#881337" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">£648 &minus; 20% (£129.60) = £518.40 (WRONG!)</text>
            </svg>
            <div style="font-size:0.86rem; color:#be123c; margin-top:10px; line-height:1.5; text-align:center;">
              <strong>Key Exam Takeaway:</strong> The 20% tax was calculated from the £540 base, NOT from the £648 total. Always divide by the multiplier!
            </div>
          </div>
        </div>

        <div class="pfs-card-footer">
          <span class="pfs-pill-l2">Level 2 Only</span>
          <span class="pfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
        </div>
      </div>
    </section>

    <!-- WORKED EXAM MODELS -->
    <section id="worked-exam-models" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Worked Exam Model: Multi-Step Evaluation</h2>
        <span style="font-size:0.88rem; font-weight:700; color:#0284c7;"><i class="fa-solid fa-award"></i> 5 Marks Pearson Edexcel Style</span>
      </div>

      <div class="exam-model-card">
        <div class="exam-model-badge">
          <i class="fa-solid fa-file-signature"></i> Real Exam Context: Commercial Procurement
        </div>
        <p style="font-size:1.05rem; line-height:1.7; color:#1e293b; margin-bottom:1.25rem;">
          A care facility needs to purchase <strong>15 new specialist profiling beds</strong>. The standard catalog price is <strong>£420.00 per bed</strong>.<br>
          Two medical suppliers submit bids for the order:
        </p>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:1.25rem;">
          <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; padding:14px;">
            <strong style="color:#0284c7; font-size:1.05rem; display:block; margin-bottom:6px;">Supplier Alpha:</strong>
            <p style="margin:0; font-size:0.95rem; color:#334155; line-height:1.5;">
              Offers a straight <strong>15% trade discount</strong> on the total list price of the entire order.
            </p>
          </div>
          <div style="background:#ffffff; border:1.5px solid #cbd5e1; border-radius:8px; padding:14px;">
            <strong style="color:#059669; font-size:1.05rem; display:block; margin-bottom:6px;">Supplier Beta:</strong>
            <p style="margin:0; font-size:0.95rem; color:#334155; line-height:1.5;">
              Offers a flat <strong>£50 cash rebate</strong> for every whole £500 spent on the order.
            </p>
          </div>
        </div>

        <p style="font-weight:700; color:#0f172a; margin-bottom:1rem;">
          Which supplier is cheaper, and by how much? Show complete step-by-step working to justify your answer.
        </p>

        <div class="pfs-steps-box" style="margin-bottom:1.25rem;">
          <div class="pfs-step-row">
            <span class="pfs-step-tag">Step 1</span>
            <div class="pfs-step-content">
              <strong>Calculate total undiscounted cost:</strong><br>
              15 beds &times; £420.00 per bed:<br>
              <span class="solution-step-math">15 &times; £420.00 = £6,300.00</span>
            </div>
          </div>

          <div class="pfs-step-row">
            <span class="pfs-step-tag">Step 2</span>
            <div class="pfs-step-content">
              <strong>Calculate Supplier Alpha's discounted price:</strong><br>
              Apply 15% discount using the multiplier 0.85 (100% &minus; 15% = 85%):<br>
              <span class="solution-step-math">£6,300.00 &times; 0.85 = £5,355.00</span>
            </div>
          </div>

          <div class="pfs-step-row">
            <span class="pfs-step-tag">Step 3</span>
            <div class="pfs-step-content">
              <strong>Calculate Supplier Beta's rebate price:</strong><br>
              Count how many whole £500 blocks exist in £6,300:<br>
              <span class="solution-step-math">£6,300 &divide; 500 = 12.6 &rarr; exactly 12 whole £500 blocks</span><br>
              Total rebate = 12 &times; £50.00 = <strong>£600.00</strong><br>
              Supplier Beta Final Cost = £6,300.00 &minus; £600.00 = <strong>£5,700.00</strong>
            </div>
          </div>

          <div class="pfs-step-row">
            <span class="pfs-step-tag">Step 4</span>
            <div class="pfs-step-content">
              <strong>Compare both suppliers and find the difference:</strong><br>
              <span class="solution-step-math">£5,700.00 &minus; £5,355.00 = £345.00</span>
            </div>
          </div>
        </div>

        <div class="pfs-answer-banner">
          <i class="fa-solid fa-award"></i>
          <div>
            <strong>Final Conclusion &amp; Justification:</strong>
            <span style="font-size:1.15rem; display:block; font-weight:800; font-family:'Inter', sans-serif;">
              Supplier Alpha is cheaper by £345.00 (£5,355.00 vs £5,700.00).
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- EXAMINER TRAPS -->
    <section id="examiner-traps" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation"></i> Examiner Traps &amp; Common Distractors</h2>
      </div>

      <div class="trap-card-rose">
        <div class="trap-card-rose-header">
          <i class="fa-solid fa-ban"></i>
          <span>Trap 1: The "Reverse Percentage Fallacy"</span>
        </div>
        <p style="margin-bottom:0.5rem; line-height:1.65; color:#334155;">
          If an item costs £120 including 20% VAT, students frequently calculate 20% of £120 (£24) and subtract it to get £96. This is fundamentally wrong!
        </p>
        <div style="background:#ffffff; border-left:4px solid #f43f5e; padding:8px 14px; border-radius:4px; font-weight:700; color:#be123c; margin-bottom:0.5rem;">
          Rule: £120 represents 120%. You must divide by 1.20 to find 100%: £120 &divide; 1.20 = £100.00.
        </div>
        <div class="trap-prevention-badge">
          Examiner Check: Always check your answer by adding 20% back onto your result. 20% of £100 is £20, which gives £120.
        </div>
      </div>

      <div class="trap-card-rose">
        <div class="trap-card-rose-header">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <span>Trap 2: Decimal Multiplier Slip for Single-Digit Percentages</span>
        </div>
        <p style="margin-bottom:0.5rem; line-height:1.65; color:#334155;">
          A very common slip under timed pressure is writing <strong>1.4</strong> for a 4% increase, or <strong>0.3</strong> for 3%.
        </p>
        <ul style="padding-left:20px; line-height:1.65; color:#334155; margin-bottom:0.5rem;">
          <li>4% increase multiplier is <strong>1.04</strong> (1.4 represents a massive 40% increase!).</li>
          <li>3% discount multiplier is <strong>0.97</strong> (0.3 represents a 70% reduction!).</li>
        </ul>
        <div class="trap-prevention-badge">
          Rule: If the percentage is less than 10%, remember the zero after the decimal point (e.g. 5% = 0.05).
        </div>
      </div>

      <div class="trap-card-rose">
        <div class="trap-card-rose-header">
          <i class="fa-solid fa-circle-exclamation"></i>
          <span>Trap 3: Stopping After Calculating the Change Value</span>
        </div>
        <p style="margin-bottom:0.5rem; line-height:1.65; color:#334155;">
          When asked for the <em>new price</em> after a 12% discount on a £350 coat, students often calculate 12% (£42.00) and stop there, writing £42.00 in the answer box.
        </p>
        <div class="trap-prevention-badge">
          Prevention: Re-read the question stem. Did it ask for the <em>amount of discount</em>, or the <em>final price paid</em>? £350 &minus; £42 = £308.00.
        </div>
      </div>
    </section>

    <!-- PRACTICE QUESTIONS -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Tasks</h2>
        <span style="font-size:0.88rem; font-weight:700; color:var(--accent);"><i class="fa-solid fa-clock"></i> Self-Paced Practice</span>
      </div>
      <p class="section-lead-text">
        Attempt these realistic Pearson Edexcel style exam questions. Type your working in the scratchpad, then reveal the model mark scheme to evaluate your marks.
      </p>

      <!-- PRACTICE QUESTION 1 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 1:</span> Access Ramp Maintenance Grant</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [3 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>A community health center receives a discretionary maintenance grant of <strong>£560.00</strong>. The board votes to allocate exactly <strong>35%</strong> of this grant towards improving wheelchair access ramps.</p>
          <p>Calculate how much money is allocated to wheelchair ramp improvements.</p>
        </div>
        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="scratchpad1"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="scratchpad1" class="working-scratchpad-input" placeholder="Type your step-by-step working here (e.g. 10% = 56, 30% = 168, 5% = 28...)"></textarea>
        </div>
        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('solDrawer1')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>
        <div id="solDrawer1" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">3 / 3 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Find 10%)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">£560.00 &divide; 10 = £56.00</div>
              <div class="solution-step-content">Divide the total grant by 10 to establish the primary non-calculator building block.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Calculate 30% and 5%)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">30% = 3 &times; £56.00 = £168.00 &nbsp;|&nbsp; 5% = £56.00 &divide; 2 = £28.00</div>
              <div class="solution-step-content">Multiply the 10% value by 3 for 30%, and halve the 10% value for 5%.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Combine Components)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">£168.00 + £28.00 = £196.00</div>
              <div class="solution-step-content">Sum both parts together to obtain the full 35% allocation.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">£196.00</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> Alternative valid method: 25% (half of half = £140.00) + 10% (£56.00) = £196.00. Both methods capture full method marks!</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l1">FS Level 1</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- PRACTICE QUESTION 2 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 2:</span> Ambulance Dispatch Satisfaction KPI</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [4 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>A regional ambulance call centre conducted a quarterly survey. Out of <strong>350</strong> patient family responses received, exactly <strong>287</strong> rated the dispatch communication as "Good" or "Outstanding".</p>
          <p>The regional NHS service target is for at least <strong>80%</strong> of callers to rate dispatch communication as Good or Outstanding.</p>
          <p>Has the call centre met the service target? You must show all your calculations to justify your answer.</p>
        </div>
        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="scratchpad2"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="scratchpad2" class="working-scratchpad-input" placeholder="Type your step-by-step working here (e.g. 287 / 350 = ...)..."></textarea>
        </div>
        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('solDrawer2')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>
        <div id="solDrawer2" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">4 / 4 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Formulate Fraction &amp; Divide)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">287 &divide; 350 = 0.82</div>
              <div class="solution-step-content">Divide the number of positive ratings by the total responses received.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Convert to Percentage)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">0.82 &times; 100 = 82%</div>
              <div class="solution-step-content">Multiply the decimal by 100 to convert into a percentage value.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Compare with KPI Target)</span>
                <span class="solution-step-mark">E1 Explanation Mark</span>
              </div>
              <div class="solution-step-math">82% &gt; 80% Target Benchmark</div>
              <div class="solution-step-content">State clearly that 82% is higher than the required 80% NHS service target.</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">Yes, target met (82% &gt; 80%)</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Marking Tip:</strong> On decision questions ("Has the centre met the target?"), stating just "Yes" scores 0 marks without the supporting 82% calculation and direct comparison.</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>

      <!-- PRACTICE QUESTION 3 -->
      <div class="practice-q-card">
        <div class="practice-q-header">
          <span class="practice-q-title"><span class="pfs-prefix">Practice Task 3:</span> Discounted Backup Generator</span>
          <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> [4 Marks]</span>
        </div>
        <div class="practice-q-stem">
          <p>A mobile health clinic purchases a backup diesel generator on a seasonal promotion. The promotional sale price is <strong>£408.00</strong> after a <strong>15% discount</strong> was taken off the original recommended retail price.</p>
          <p>Calculate the original price of the generator before the discount was applied.</p>
        </div>
        <div class="working-scratchpad-area">
          <label class="working-scratchpad-label" for="scratchpad3"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
          <textarea id="scratchpad3" class="working-scratchpad-input" placeholder="Type your step-by-step working here (e.g. 100% - 15% = 85%, £408 / 0.85 = ...)..."></textarea>
        </div>
        <div class="practice-q-toolbar">
          <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('solDrawer3')">
            <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
          </button>
        </div>
        <div id="solDrawer3" class="solution-drawer">
          <div class="solution-drawer-title">
            <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
            <span class="solution-marks-badge">4 / 4 Marks Awarded</span>
          </div>
          <div class="solution-steps-list">
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 1 (Identify Baseline Percentage)</span>
                <span class="solution-step-mark">P1 Process Mark</span>
              </div>
              <div class="solution-step-math">100% &minus; 15% = 85% of Original Price</div>
              <div class="solution-step-content">Recognize that £408.00 represents 85% of the pre-sale price.</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 2 (Formulate Multiplier &amp; Division)</span>
                <span class="solution-step-mark">M1 Method Mark</span>
              </div>
              <div class="solution-step-math">Original Price = £408.00 &divide; 0.85</div>
              <div class="solution-step-content">Divide the sale price by the decimal multiplier (0.85).</div>
            </div>
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step 3 (Calculate Final Value)</span>
                <span class="solution-step-mark">A1 Accuracy Mark</span>
              </div>
              <div class="solution-step-math">£408.00 &divide; 0.85 = £480.00</div>
              <div class="solution-step-content">Calculate the final quotient. State answer clearly formatted in pounds (£).</div>
            </div>
          </div>
          <div class="solution-final-answer-box">
            <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
            <div class="solution-final-value">£480.00</div>
          </div>
          <div class="solution-tutor-tip">
            <i class="fa-solid fa-lightbulb"></i>
            <span><strong>Examiner Verification Tip:</strong> Always double check: 15% of £480.00 is £72.00. Then £480.00 &minus; £72.00 = £408.00. This confirms your answer is 100% correct!</span>
          </div>
        </div>
        <div class="practice-q-footer">
          <span class="pfs-pill-l2">FS Level 2</span>
          <span class="pfs-pill-board">Edexcel</span>
          <span class="pfs-pill-board">City &amp; Guilds</span>
          <span class="pfs-pill-board">NCFE</span>
          <span class="pfs-pill-board">Open Awards</span>
          <span class="pfs-pill-board">Highfield</span>
        </div>
      </div>
    </section>

    <!-- PROGRESSION BANNER -->
    <section id="curriculum-links" class="progression-banner">
      <div>
        <h3 class="progression-title">Ready for Your Next Revision Step?</h3>
        <p style="color:#cbd5e1; margin:0; line-height:1.6;">
          Master converting seamlessly between fractions, decimals, and percentages (FDP) across both calculator and non-calculator exam sections.
        </p>
      </div>
      <a href="functional-skills-fractions-decimals-and-percentages.html" class="btn-progression">
        Next: FDP Conversions <i class="fa-solid fa-arrow-right"></i>
      </a>
    </section>
    """

    full_html = build_full_html(
        filename="functional-skills-percentages.html",
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file="functional-skills-fractions-decimals-and-percentages.html",
        next_name="FDP Conversions"
    )

    out_path = os.path.join(PROJECT_DIR, "functional-skills-percentages.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[BESPOKE OK] Percentages generated ({len(full_html)} bytes)")

if __name__ == "__main__":
    build_perimeter_page()
    build_money_page()
    build_volume_page()
    build_percentages_page()

