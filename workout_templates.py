#!/usr/bin/env python3
"""
Master Functional Skills - Standardized HTML Templates for Skill Workouts & Workout Answers.
Emulates Corbettmaths "Textbook Exercises" (Workout + Apply) with adult vocational contexts,
dyslexia-friendly styling, A4 print optimization, and Pearson Edexcel alignment.
"""

import html

def render_drill_grid(items, prefix="", suffix=""):
    """
    Renders an array of drill items in a clean, high-density 2-column or 3-column grid.
    items: list of tuples (letter, question_text, answer_val)
    """
    cells = []
    for item in items:
        letter = item[0]
        q_text = item[1]
        pfx_html = f'<span class="drill-unit-prefix">{prefix}</span>' if prefix else ""
        sfx_html = f'<span class="drill-unit-suffix">{suffix}</span>' if suffix else ""
        
        cells.append(f"""
        <div class="drill-card">
          <div class="drill-letter">({letter})</div>
          <div class="drill-q">{q_text}</div>
          <div class="drill-ans-box">
            {pfx_html}<span class="drill-input-line"></span>{sfx_html}
          </div>
        </div>""")
    return "\n".join(cells)

def resolve_guide_url(slug, back_url=None):
    if back_url and not any(bad in back_url for bad in ['fdp-conversions', 'english-level-2-writing-blog', 'algebra', 'money-invoicing-payroll', 'division-and-remainders']):
        return back_url
    if slug == 'fdp-conversions':
        return "../functional-skills-fractions-decimals-and-percentages.html"
    if slug in ('english-level-2-writing-blog', 'writing-blog', 'blog'):
        return "../functional-skills-english-level-2-writing-blog.html"
    if slug in ('formulas', 'algebra'):
        return "../functional-skills-formulas.html"
    if slug in ('division', 'division-and-remainders'):
        return "../functional-skills-division.html"
    if slug in ('money', 'money-invoicing-payroll'):
        return "../functional-skills-money.html"
    if back_url:
        return back_url
    return f"../functional-skills-{slug}.html"

def render_skill_workout(data):
    title = data['title']
    slug = data['slug']
    subject = data.get('subject', 'Mathematics')
    spec_codes = data.get('spec_codes', 'Pearson Edexcel Functional Skills')
    level = data.get('level', 'Level 1 & Level 2')
    method_card = data.get('method_card', {})
    workout_blocks = data.get('workout_blocks', [])
    apply_questions = data.get('apply_questions', [])
    back_url = resolve_guide_url(slug, data.get('back_url'))
    practice_url = f"{slug}-worksheet.html"
    ans_url = f"{slug}-workout-answers.html"

    # Build Method Card HTML
    method_html = ""
    if method_card:
        m_title = method_card.get('title', 'Core Method & Golden Rules')
        m_points = method_card.get('points', [])
        points_li = "\n".join([f"<li><i class='fa-solid fa-check text-emerald'></i> <span>{pt}</span></li>" for pt in m_points])
        calc_tip = method_card.get('calc_tip', '')
        calc_html = f"<div class='method-calc-tip'><i class='fa-solid fa-calculator'></i> <strong>Calculator Strategy:</strong> {calc_tip}</div>" if calc_tip else ""
        
        method_html = f"""
    <!-- Method & Formula Card -->
    <div class="method-card">
      <div class="method-card-header">
        <i class="fa-solid fa-lightbulb"></i>
        <span>{m_title}</span>
      </div>
      <div class="method-card-body">
        <ul class="method-points">
          {points_li}
        </ul>
        {calc_html}
      </div>
    </div>
"""

    # Build Workout Blocks HTML
    workout_sections_html = ""
    for b_idx, block in enumerate(workout_blocks, 1):
        b_title = block.get('title', f'Question {b_idx}: Skills Practice')
        b_instr = block.get('instruction', 'Work out the answers without a calculator where possible:')
        items = block.get('items', [])
        grid_html = render_drill_grid(items, prefix=block.get('prefix', ''), suffix=block.get('suffix', ''))
        
        workout_sections_html += f"""
    <div class="workout-block">
      <div class="workout-block-header">
        <span class="block-q-num">Question {b_idx}</span>
        <span class="block-q-desc">{b_title}</span>
      </div>
      <div class="workout-instruction">{b_instr}</div>
      <div class="drill-grid">
        {grid_html}
      </div>
    </div>
"""

    # Build Apply Questions HTML
    apply_html = ""
    if apply_questions:
        apply_cards = []
        for q_idx, q in enumerate(apply_questions, 1):
            stem = q.get('stem', '')
            context_tag = q.get('context_tag', 'Vocational Context')
            marks = q.get('marks', 2)
            unit_suffix = q.get('unit', '')
            ans_prefix = q.get('prefix', '')
            
            ans_box_html = f"""
            <div class="apply-ans-line">
              <span class="ans-label">Final Answer =</span>
              {f'<span class="unit-pfx">{ans_prefix}</span>' if ans_prefix else ''}
              <div class="ans-write-box"></div>
              {f'<span class="unit-sfx">{unit_suffix}</span>' if unit_suffix else ''}
            </div>"""

            apply_cards.append(f"""
      <div class="apply-card">
        <div class="apply-card-head">
          <span class="apply-q-num">Question {q_idx}</span>
          <span class="apply-context-tag"><i class="fa-solid fa-briefcase"></i> {context_tag}</span>
          <span class="apply-marks">[{marks} Marks]</span>
        </div>
        <div class="apply-stem">{stem}</div>
        <div class="apply-working-area">
          <div class="apply-working-label">Show your step-by-step working:</div>
          <div class="apply-working-lines">
            <div class="work-line"></div>
            <div class="work-line"></div>
            <div class="work-line"></div>
          </div>
        </div>
        {ans_box_html}
      </div>""")
        
        apply_html = "\n".join(apply_cards)

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {title} Skill Workout & Repetition Drills</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0f172a;
      background: #f8fafc;
      margin: 0;
      padding: 0;
      font-size: 10.5pt;
      line-height: 1.5;
    }}
    .print-bar {{
      background: #0b172d;
      color: #f8fafc;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .print-bar a {{
      color: #93c5fd;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .print-bar a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .btn-action-print {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 20px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-action-print:hover {{
      background: #1d4ed8;
    }}
    .btn-action-answers {{
      background: #059669;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 10px;
    }}
    .btn-action-answers:hover {{
      background: #047857;
    }}
    .btn-action-practice {{
      background: #7c3aed;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 10px;
    }}
    .btn-action-practice:hover {{
      background: #6d28d9;
    }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 0;
      width: 115px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: none;
      background: transparent;
      box-sizing: border-box;
    }}
    .nav-pill-btn:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      text-decoration: none;
    }}
    .nav-pill-btn.active {{
      background: #2563eb;
      color: #ffffff;
      cursor: default;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    }}


    @media (max-width: 900px) {{
      .print-bar {{
        padding: 10px 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .print-bar > div:first-child {{
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .print-bar > div:first-child a {{
        font-size: 0.85rem;
        display: inline-flex;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }}
      .print-bar > div:last-child {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
      }}
      .print-bar > div:last-child > * {{
        margin-right: 0 !important;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        padding: 6px 12px;
        font-size: 0.85rem;
      }}
      .nav-pill-group {{
        margin-right: 0;
      }}
      .nav-pill-btn {{
        width: 100px;
        font-size: 0.82rem;
        padding: 5px 0;
      }}
    }}
    @media (max-width: 480px) {{
      .print-bar > div:last-child {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }}
      .nav-pill-group {{
        grid-column: span 2;
        width: 100%;
      }}
      .nav-pill-btn {{
        flex: 1;
        width: auto;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        justify-content: center;
        width: 100%;
      }}
    }}
    @media print {{
      .print-bar {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .workout-block, .apply-card {{
        page-break-inside: avoid;
      }}
      .page-break-before {{
        page-break-before: always;
      }}
    }}

    .page-sheet {{
      max-width: 900px;
      margin: 24px auto;
      background: #ffffff;
      padding: 32px 40px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      border-radius: 8px;
      border: 1px solid #e2e8f0;
    }}

    /* Header styling */
    .sheet-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .brand-title {{
      font-size: 1.35rem;
      font-weight: 900;
      color: #0b172d;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-title i {{
      color: #2563eb;
    }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{
      text-align: right;
    }}
    .badge-level {{
      background: #eff6ff;
      color: #1e40af;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.82rem;
      border: 1px solid #bfdbfe;
      display: inline-block;
      margin-bottom: 4px;
    }}
    .badge-spec {{
      font-size: 0.78rem;
      color: #64748b;
      font-weight: 600;
    }}

    /* Title banner */
    .hero-banner {{
      background: linear-gradient(135deg, #0b172d 0%, #1e3a8a 100%);
      color: #ffffff;
      padding: 18px 24px;
      border-radius: 8px;
      margin-bottom: 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.45rem;
      font-weight: 800;
      margin: 0;
      line-height: 1.2;
    }}
    .hero-subtitle {{
      font-size: 0.88rem;
      color: #bfdbfe;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      white-space: nowrap;
    }}

    /* Method Card */
    .method-card {{
      background: #f0fdf4;
      border: 1.5px solid #86efac;
      border-radius: 8px;
      margin-bottom: 24px;
      overflow: hidden;
    }}
    .method-card-header {{
      background: #dcfce7;
      padding: 8px 16px;
      font-weight: 800;
      color: #166534;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #86efac;
    }}
    .method-card-body {{
      padding: 12px 18px;
    }}
    .method-points {{
      margin: 0;
      padding: 0;
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 8px 20px;
    }}
    .method-points li {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.92rem;
      color: #1e293b;
    }}
    .text-emerald {{
      color: #059669;
      margin-top: 3px;
    }}
    .method-calc-tip {{
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px dashed #bbf7d0;
      font-size: 0.88rem;
      color: #166534;
    }}

    /* Section divider */
    .section-ribbon {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 28px 0 16px 0;
    }}
    .section-ribbon-tag {{
      background: #0f172a;
      color: #ffffff;
      padding: 6px 16px;
      border-radius: 4px;
      font-size: 0.95rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .section-ribbon-line {{
      flex: 1;
      height: 2px;
      background: #cbd5e1;
    }}
    .section-ribbon-info {{
      font-size: 0.85rem;
      color: #64748b;
      font-weight: 600;
    }}

    /* Workout block */
    .workout-block {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }}
    .workout-block-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 8px;
    }}
    .block-q-num {{
      background: #2563eb;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 2px 8px;
      border-radius: 4px;
    }}
    .block-q-desc {{
      font-weight: 800;
      color: #0f172a;
      font-size: 1rem;
    }}
    .workout-instruction {{
      font-size: 0.88rem;
      color: #64748b;
      font-style: italic;
      margin-bottom: 12px;
    }}

    /* Drill grid */
    .drill-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 10px;
    }}
    .drill-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 10px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .drill-letter {{
      font-weight: 800;
      color: #2563eb;
      font-size: 0.85rem;
      margin-bottom: 2px;
    }}
    .drill-q {{
      font-size: 0.95rem;
      font-weight: 600;
      color: #1e293b;
      margin-bottom: 8px;
      line-height: 1.3;
    }}
    .drill-ans-box {{
      display: flex;
      align-items: center;
      gap: 4px;
      margin-top: auto;
      border-top: 1px dashed #cbd5e1;
      padding-top: 6px;
    }}
    .drill-unit-prefix, .drill-unit-suffix {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #475569;
    }}
    .drill-input-line {{
      flex: 1;
      border-bottom: 1.5px solid #94a3b8;
      height: 16px;
    }}

    /* Apply Cards */
    .apply-card {{
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 18px;
    }}
    .apply-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 10px;
    }}
    .apply-q-num {{
      font-weight: 800;
      color: #0f172a;
      font-size: 1rem;
    }}
    .apply-context-tag {{
      background: #f1f5f9;
      color: #334155;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
    }}
    .apply-marks {{
      font-weight: 800;
      color: #dc2626;
      font-size: 0.88rem;
    }}
    .apply-stem {{
      font-size: 0.96rem;
      color: #1e293b;
      line-height: 1.55;
      margin-bottom: 12px;
    }}
    .apply-working-area {{
      background: #fafafa;
      border: 1px dashed #cbd5e1;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 12px;
    }}
    .apply-working-label {{
      font-size: 0.78rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .work-line {{
      border-bottom: 1px solid #e2e8f0;
      height: 22px;
    }}
    .apply-ans-line {{
      display: flex;
      align-items: center;
      gap: 8px;
      justify-content: flex-end;
      padding-top: 4px;
    }}
    .ans-label {{
      font-weight: 700;
      font-size: 0.92rem;
      color: #0f172a;
    }}
    .ans-write-box {{
      width: 140px;
      border-bottom: 2px solid #0f172a;
      height: 22px;
    }}
    .unit-pfx, .unit-sfx {{
      font-weight: 700;
      font-size: 0.95rem;
      color: #0f172a;
    }}

    /* Footer */
    .sheet-footer {{
      margin-top: 30px;
      padding-top: 14px;
      border-top: 1px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: #64748b;
    }}
    .footer-links a {{
      color: #2563eb;
      text-decoration: none;
      font-weight: 600;
      margin-left: 12px;
    }}
  </style>
</head>
<body>

  <!-- Top Action Navigation Bar -->
  <div class="print-bar">
    <div>
      <a href="{back_url}"><i class="fa-solid fa-arrow-left"></i> Back to {title} Revision Guide</a>
    </div>
    <div>
      <a href="{practice_url}" class="btn-action-practice"><i class="fa-solid fa-file-pen"></i> Switch to Exam Practice</a>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-file-lines"></i> Questions</span>
        <a href="{ans_url}" class="nav-pill-btn"><i class="fa-solid fa-check-double"></i> Answers</a>
      </div>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save as PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-graduation-cap"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Core Skills &amp; Practice Workout</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level}</div><br>
        <span class="badge-spec">{spec_codes}</span>
      </div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{title} Skill Workout</h1>
        <div class="hero-subtitle">Section 1: Quick Practice Drills &bull; Section 2: Real-Life Problems</div>
      </div>
      <div class="hero-tag">
        <i class="fa-solid fa-repeat"></i> Practice &amp; Repeat
      </div>
    </div>

    {method_html}

    <!-- PART 1: THE WORKOUT -->
    <div class="section-ribbon">
      <span class="section-ribbon-tag">Part 1: Quick Practice</span>
      <div class="section-ribbon-line"></div>
      <span class="section-ribbon-info">Quick calculation drills to build confidence</span>
    </div>

    {workout_sections_html}

    <!-- PART 2: THE APPLY -->
    <div class="section-ribbon page-break-before">
      <span class="section-ribbon-tag">Part 2: Real-Life Practice</span>
      <div class="section-ribbon-line"></div>
      <span class="section-ribbon-info">Everyday life and workplace questions</span>
    </div>

    {apply_html}

    <!-- Sheet Footer -->
    <div class="sheet-footer">
      <div>&copy; Master Functional Skills &bull; masterfunctionalskills.co.uk &bull; Pearson Edexcel Reformed Specification</div>
      <div class="footer-links">
        <a href="{ans_url}">Answers Key</a>
        <a href="{practice_url}">Exam Practice Booklet</a>
      </div>
    </div>
  </div>

</body>
</html>
"""


def render_skill_workout_answers(data):
    title = data['title']
    slug = data['slug']
    subject = data.get('subject', 'Mathematics')
    spec_codes = data.get('spec_codes', 'Pearson Edexcel Functional Skills')
    level = data.get('level', 'Level 1 & Level 2')
    workout_blocks = data.get('workout_blocks', [])
    apply_questions = data.get('apply_questions', [])
    rev_guide_url = resolve_guide_url(slug, data.get('back_url'))
    back_url = f"{slug}-workout.html"
    practice_ans_url = f"{slug}-answers.html"

    # Render Workout Quick-Check Answer Tables
    quick_check_tables = ""
    for b_idx, block in enumerate(workout_blocks, 1):
        b_title = block.get('title', f'Question {b_idx}')
        items = block.get('items', [])
        
        row_cells = []
        for it in items:
            letter = it[0]
            q_text = it[1]
            ans_val = it[2]
            row_cells.append(f"""
            <div class="ans-grid-cell">
              <span class="cell-letter">({letter})</span>
              <span class="cell-q">{q_text} &rarr;</span>
              <span class="cell-val">{ans_val}</span>
            </div>""")
        cells_html = "\n".join(row_cells)
        
        quick_check_tables += f"""
      <div class="ans-table-card">
        <div class="ans-table-head">
          <span class="ans-badge">Q{b_idx}</span>
          <span class="ans-head-title">{b_title}</span>
        </div>
        <div class="ans-grid">
          {cells_html}
        </div>
      </div>
"""

    # Render Apply Step-by-Step Solutions
    apply_solutions = ""
    for q_idx, q in enumerate(apply_questions, 1):
        stem = q.get('stem', '')
        context_tag = q.get('context_tag', 'Real-Life Context')
        marks = q.get('marks', 2)
        steps = q.get('steps', [])
        final_answer = q.get('final_answer', '')
        reverse_check = q.get('reverse_check', '')
        pitfall = q.get('pitfall', '')
        
        steps_rows = []
        for step_text, mark_tag in steps:
            steps_rows.append(f"""
            <div class="sol-step-row">
              <div class="step-text"><i class="fa-solid fa-chevron-right text-emerald"></i> {step_text}</div>
              <div class="step-mark">{mark_tag}</div>
            </div>""")
        steps_html = "\n".join(steps_rows)

        check_html = f"""
        <div class="callout-box check-box">
          <i class="fa-solid fa-shield-check"></i>
          <div><strong>Quick Check Method:</strong> {reverse_check}</div>
        </div>""" if reverse_check else ""

        pitfall_html = f"""
        <div class="callout-box pitfall-box">
          <i class="fa-solid fa-triangle-exclamation"></i>
          <div><strong>Common Mistake to Avoid:</strong> {pitfall}</div>
        </div>""" if pitfall else ""

        apply_solutions += f"""
      <div class="apply-sol-card">
        <div class="apply-sol-head">
          <div>
            <span class="sol-q-num">Question {q_idx} Worked Solution</span>
            <span class="sol-ctx"><i class="fa-solid fa-briefcase"></i> {context_tag}</span>
          </div>
          <span class="sol-marks">[{marks} Marks Available]</span>
        </div>
        <div class="sol-stem-summary">{stem}</div>
        <div class="sol-steps-wrap">
          {steps_html}
        </div>
        <div class="final-ans-box">
          <span class="final-lbl">Correct Final Answer:</span>
          <span class="final-val">{final_answer}</span>
        </div>
        {check_html}
        {pitfall_html}
      </div>
"""

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {title} Skill Workout Worked Answers &amp; Mark Scheme</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #0f172a;
      background: #f8fafc;
      margin: 0;
      padding: 0;
      font-size: 10.5pt;
      line-height: 1.5;
    }}
    .print-bar {{
      background: #0b172d;
      color: #f8fafc;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .print-bar a {{
      color: #93c5fd;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .print-bar a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .btn-action-print {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 20px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-action-print:hover {{
      background: #1d4ed8;
    }}
    .btn-action-workout {{
      background: #059669;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 10px;
    }}
    .btn-action-workout:hover {{
      background: #047857;
    }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
      vertical-align: middle;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 0;
      width: 115px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease-in-out;
      cursor: pointer;
      white-space: nowrap;
      user-select: none;
      border: none;
      background: transparent;
      box-sizing: border-box;
    }}
    .nav-pill-btn:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      text-decoration: none;
    }}
    .nav-pill-btn.active {{
      background: #059669;
      color: #ffffff;
      cursor: default;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    }}
    .btn-action-practice {{
      background: #7c3aed;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-right: 10px;
    }}
    .btn-action-practice:hover {{
      background: #6d28d9;
    }}


    @media (max-width: 900px) {{
      .print-bar {{
        padding: 10px 14px;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .print-bar > div:first-child {{
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }}
      .print-bar > div:first-child a {{
        font-size: 0.85rem;
        display: inline-flex;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }}
      .print-bar > div:last-child {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 6px;
      }}
      .print-bar > div:last-child > * {{
        margin-right: 0 !important;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        padding: 6px 12px;
        font-size: 0.85rem;
      }}
      .nav-pill-group {{
        margin-right: 0;
      }}
      .nav-pill-btn {{
        width: 100px;
        font-size: 0.82rem;
        padding: 5px 0;
      }}
    }}
    @media (max-width: 480px) {{
      .print-bar > div:last-child {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }}
      .nav-pill-group {{
        grid-column: span 2;
        width: 100%;
      }}
      .nav-pill-btn {{
        flex: 1;
        width: auto;
      }}
      .btn-action-mode,
      .btn-action-practice,
      .btn-action-answers,
      .btn-action-sheet,
      .btn-action-print {{
        justify-content: center;
        width: 100%;
      }}
    }}
    @media print {{
      .print-bar {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .ans-table-card, .apply-sol-card {{
        page-break-inside: avoid;
      }}
      .page-break-before {{
        page-break-before: always;
      }}
    }}

    .page-sheet {{
      max-width: 900px;
      margin: 24px auto;
      background: #ffffff;
      padding: 32px 40px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      border-radius: 8px;
      border: 1px solid #e2e8f0;
    }}

    /* Header styling */
    .sheet-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .brand-title {{
      font-size: 1.35rem;
      font-weight: 900;
      color: #0b172d;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-title i {{
      color: #059669;
    }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{
      text-align: right;
    }}
    .badge-level {{
      background: #f0fdf4;
      color: #166534;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.82rem;
      border: 1px solid #bbf7d0;
      display: inline-block;
      margin-bottom: 4px;
    }}
    .badge-spec {{
      font-size: 0.78rem;
      color: #64748b;
      font-weight: 600;
    }}

    /* Title banner */
    .hero-banner {{
      background: linear-gradient(135deg, #064e3b 0%, #047857 100%);
      color: #ffffff;
      padding: 18px 24px;
      border-radius: 8px;
      margin-bottom: 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.45rem;
      font-weight: 800;
      margin: 0;
      line-height: 1.2;
    }}
    .hero-subtitle {{
      font-size: 0.88rem;
      color: #a7f3d0;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.35);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      white-space: nowrap;
    }}

    /* Section divider */
    .section-ribbon {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 28px 0 16px 0;
    }}
    .section-ribbon-tag {{
      background: #064e3b;
      color: #ffffff;
      padding: 6px 16px;
      border-radius: 4px;
      font-size: 0.95rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .section-ribbon-line {{
      flex: 1;
      height: 2px;
      background: #cbd5e1;
    }}
    .section-ribbon-info {{
      font-size: 0.85rem;
      color: #64748b;
      font-weight: 600;
    }}

    /* Quick check grid */
    .ans-table-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 16px;
    }}
    .ans-table-head {{
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
      margin-bottom: 10px;
    }}
    .ans-badge {{
      background: #047857;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 2px 8px;
      border-radius: 4px;
    }}
    .ans-head-title {{
      font-weight: 800;
      color: #0f172a;
      font-size: 0.98rem;
    }}
    .ans-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 8px 12px;
    }}
    .ans-grid-cell {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 6px 10px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.88rem;
    }}
    .cell-letter {{
      font-weight: 800;
      color: #047857;
    }}
    .cell-q {{
      color: #64748b;
      font-size: 0.82rem;
    }}
    .cell-val {{
      font-weight: 800;
      color: #0f172a;
      margin-left: auto;
    }}

    /* Apply solutions */
    .apply-sol-card {{
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 20px;
    }}
    .apply-sol-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 10px;
      margin-bottom: 10px;
    }}
    .sol-q-num {{
      font-weight: 800;
      color: #0f172a;
      font-size: 1.05rem;
      margin-right: 8px;
    }}
    .sol-ctx {{
      background: #f1f5f9;
      color: #334155;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
    }}
    .sol-marks {{
      font-weight: 800;
      color: #dc2626;
      font-size: 0.88rem;
    }}
    .sol-stem-summary {{
      font-size: 0.92rem;
      color: #475569;
      margin-bottom: 14px;
      line-height: 1.5;
    }}
    .sol-steps-wrap {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 12px;
    }}
    .sol-step-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
      border-bottom: 1px dashed #e2e8f0;
      font-size: 0.92rem;
    }}
    .sol-step-row:last-child {{
      border-bottom: none;
    }}
    .step-text {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: #1e293b;
      font-weight: 600;
    }}
    .text-emerald {{
      color: #059669;
      font-size: 0.8rem;
    }}
    .step-mark {{
      font-weight: 800;
      color: #dc2626;
      background: #fef2f2;
      border: 1px solid #fecaca;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.8rem;
    }}
    .final-ans-box {{
      background: #ecfdf5;
      border: 1.5px solid #6ee7b7;
      border-radius: 6px;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .final-lbl {{
      font-weight: 800;
      color: #065f46;
      font-size: 0.95rem;
    }}
    .final-val {{
      font-weight: 900;
      color: #064e3b;
      font-size: 1.15rem;
    }}
    .callout-box {{
      border-radius: 6px;
      padding: 10px 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.88rem;
      margin-top: 8px;
    }}
    .check-box {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e40af;
    }}
    .check-box i {{
      color: #2563eb;
      margin-top: 3px;
    }}
    .pitfall-box {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      color: #92400e;
    }}
    .pitfall-box i {{
      color: #d97706;
      margin-top: 3px;
    }}

    /* Footer */
    .sheet-footer {{
      margin-top: 30px;
      padding-top: 14px;
      border-top: 1px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: #64748b;
    }}
    .footer-links a {{
      color: #059669;
      text-decoration: none;
      font-weight: 600;
      margin-left: 12px;
    }}
  </style>
</head>
<body>

  <!-- Top Action Navigation Bar -->
  <div class="print-bar">
    <div>
      <a href="{rev_guide_url}"><i class="fa-solid fa-arrow-left"></i> Back to {title} Revision Guide</a>
    </div>
    <div>
      <a href="{practice_ans_url}" class="btn-action-practice"><i class="fa-solid fa-file-shield"></i> Exam Mark Scheme</a>
      <div class="nav-pill-group">
        <a href="{back_url}" class="nav-pill-btn"><i class="fa-solid fa-file-lines"></i> Questions</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-check-double"></i> Answers</span>
      </div>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save as PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-circle-check"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Tutor Model Solutions &amp; Step-by-Step Mark Scheme</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level}</div><br>
        <span class="badge-spec">{spec_codes}</span>
      </div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{title} Workout Solutions</h1>
        <div class="hero-subtitle">Step-by-Step Worked Answers with Method Marks Breakdown</div>
      </div>
      <div class="hero-tag">
        <i class="fa-solid fa-check-double"></i> Complete Solutions
      </div>
    </div>

    <!-- PART 1: WORKOUT QUICK CHECK -->
    <div class="section-ribbon">
      <span class="section-ribbon-tag">Part 1: Quick-Check Answer Key</span>
      <div class="section-ribbon-line"></div>
      <span class="section-ribbon-info">Quick answers for practice questions</span>
    </div>

    {quick_check_tables}

    <!-- PART 2: APPLY WORKED SOLUTIONS -->
    <div class="section-ribbon page-break-before">
      <span class="section-ribbon-tag">Part 2: Real-Life Problem Solutions</span>
      <div class="section-ribbon-line"></div>
      <span class="section-ribbon-info">Step-by-step methods and mark breakdown</span>
    </div>

    {apply_solutions}

    <!-- Sheet Footer -->
    <div class="sheet-footer">
      <div>&copy; Master Functional Skills &bull; masterfunctionalskills.co.uk &bull; Pearson Edexcel Reformed Specification</div>
      <div class="footer-links">
        <a href="{back_url}">Return to Workout</a>
        <a href="{practice_ans_url}">Exam Scheme</a>
      </div>
    </div>
  </div>

</body>
</html>
"""
