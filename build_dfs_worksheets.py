#!/usr/bin/env python3
"""
Master Functional Skills (MFS) - DFS Worksheet Suite Generator
Author: Abdul (MFS Pedagogical Systems)
Builds the Corbett-Style Dual-Engine Worksheets for Entry 3 (18 topics) and Level 1 (21 topics)
Total: 39 topics x 4 = 156 standalone printable A4 HTML files + updates worksheets.html
Strict Separation: Style 1 (Fluency Drills) and Style 2 (Practice Exam) never link to one another on worksheet pages.
Doubled Exam Practice: Each Practice Exam worksheet features 4 comprehensive tasks [12 Marks].
"""

import os
import sys
import re
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSHEETS_DIR = os.path.join(BASE_DIR, "worksheets")
os.makedirs(WORKSHEETS_DIR, exist_ok=True)

sys.path.insert(0, BASE_DIR)
from dfs_data_entry3 import ALL_ENTRY_3_TOPICS
from dfs_data_level1 import ALL_LEVEL_1_TOPICS
from dfs_drills_expansion import EXTRA_DRILLS


def clean_html_text(text):
    if not text:
        return ""
    # Convert breaks to newlines and strip remaining tags
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    return re.sub(r'<[^>]+>', '', text).strip()


def render_workout_html(topic, level_code, level_title):
    slug = topic['slug']
    title = topic['title']
    code = topic['code']
    skill_area = topic['skill_area']
    drills = list(topic.get('drills', [])) + EXTRA_DRILLS.get(slug, [])
    guide_url = f"../digital-skills/{level_code}/{slug}.html"
    answers_url = f"{slug}-workout-answers.html"

    # Rules / Key Method summary items
    rules_html = ""
    step_items = topic.get('steps', [])
    for s in step_items:
        callout = s.get('callout', {})
        t_title = callout.get('title') or s.get('title', 'Key Rule')
        t_text = callout.get('text') or re.sub(r'<[^>]+>', '', s.get('body', ''))[:150]
        clean_text = clean_html_text(t_text)
        rules_html += f'<li><i class="fa-solid fa-circle-check" style="color:#16a34a; margin-right:8px;"></i><strong>{html.escape(t_title)}:</strong> {html.escape(clean_text)}</li>\n'
    if not rules_html and 'exam_model' in topic:
        t_rule = topic['exam_model'].get('tutor_rule', '')
        if t_rule:
            rules_html += f'<li><i class="fa-solid fa-circle-check" style="color:#16a34a; margin-right:8px;"></i><strong>Tutor Abdul\'s Golden Rule:</strong> {html.escape(t_rule)}</li>\n'

    # Drill Questions
    drills_html = ""
    for idx, d in enumerate(drills, 1):
        options_html = ""
        for opt_idx, opt in enumerate(d.get('options', [])):
            letter = chr(65 + opt_idx)
            options_html += f'''
            <div class="drill-option-item">
              <span class="option-check-box"></span>
              <span class="option-letter">{letter}.</span>
              <span class="option-text">{html.escape(opt.get('text', ''))}</span>
            </div>'''

        drills_html += f'''
        <div class="workout-question-card">
          <div class="wq-header">
            <span class="wq-number">Task {idx}</span>
            <span class="wq-marks">[2 Marks]</span>
          </div>
          <p class="wq-prompt">{html.escape(d.get('question', ''))}</p>
          <div class="wq-options-grid">
            {options_html}
          </div>
          <div class="wq-working-space">
            <span class="working-hint">Reasoning / Notes:</span>
            <div class="write-lines"></div>
          </div>
        </div>
        '''

    # Rapid recall check section
    rapid_recall_html = f'''
    <div class="workout-question-card">
      <div class="wq-header">
        <span class="wq-number">Task {len(drills)+1} — Rapid Terminology &amp; Rule Check</span>
        <span class="wq-marks">[3 Marks]</span>
      </div>
      <p class="wq-prompt">State three essential digital rules or guidelines to follow when dealing with <strong>{html.escape(title)}</strong>:</p>
      <div class="rapid-lines-box">
        <div class="rapid-line"><strong>1.</strong> <span class="write-line"></span></div>
        <div class="rapid-line"><strong>2.</strong> <span class="write-line"></span></div>
        <div class="rapid-line"><strong>3.</strong> <span class="write-line"></span></div>
      </div>
    </div>
    '''

    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {html.escape(title)} Fluency Drills ({level_title})</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/mfs-worksheets.css?v=20261024c">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
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
    .print-bar a:hover {{ color: #ffffff; text-decoration: underline; }}
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
    .btn-action-print:hover {{ background: #1d4ed8; }}
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
      margin-left: 10px;
      transition: background 0.2s;
    }}
    .btn-action-answers:hover {{ background: #047857; color: #ffffff; }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
      transition: all 0.15s ease;
    }}
    .nav-pill-btn:hover:not(.active) {{ background: rgba(255, 255, 255, 0.18); color: #ffffff; }}
    .nav-pill-btn.active {{
      background: #2563eb;
      color: #ffffff;
      cursor: default;
    }}

    @media print {{
      .print-bar {{ display: none !important; }}
      body {{ background: #ffffff !important; }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .workout-question-card {{ page-break-inside: avoid; }}
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
    .brand-title i {{ color: #2563eb; }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{ text-align: right; }}
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

    .candidate-info-box {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 16px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 20px;
    }}
    .candidate-info-item {{
      font-size: 0.88rem;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .field-line {{
      flex: 1;
      border-bottom: 1px dotted #94a3b8;
      height: 18px;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0369a1 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.35rem;
      font-weight: 800;
      margin: 0;
    }}
    .hero-subtitle {{
      font-size: 0.85rem;
      color: #bae6fd;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .rules-card {{
      background: #f0fdf4;
      border: 1.5px solid #86efac;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 24px;
    }}
    .rules-card-title {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #166534;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .rules-list {{
      margin: 0;
      padding-left: 0;
      list-style: none;
    }}
    .rules-list li {{
      font-size: 0.9rem;
      color: #14532d;
      margin-bottom: 8px;
      line-height: 1.45;
    }}

    .workout-question-card {{
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 20px;
    }}
    .wq-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .wq-number {{
      font-size: 1rem;
      font-weight: 800;
      color: #1e3a8a;
    }}
    .wq-marks {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #64748b;
      background: #f1f5f9;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .wq-prompt {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #0f172a;
      margin: 0 0 14px 0;
      line-height: 1.5;
    }}
    .wq-options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }}
    @media (max-width: 600px) {{
      .wq-options-grid {{ grid-template-columns: 1fr; }}
    }}
    .drill-option-item {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      background: #ffffff;
    }}
    .option-check-box {{
      width: 18px;
      height: 18px;
      border: 2px solid #64748b;
      border-radius: 4px;
      display: inline-block;
      flex-shrink: 0;
    }}
    .option-letter {{
      font-weight: 800;
      color: #1e3a8a;
      width: 18px;
      flex-shrink: 0;
    }}
    .option-text {{
      font-size: 0.92rem;
      color: #1e293b;
    }}
    .wq-working-space {{
      border-top: 1px dashed #cbd5e1;
      padding-top: 10px;
      margin-top: 12px;
    }}
    .working-hint {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .write-lines {{
      height: 38px;
      border-bottom: 1px dotted #cbd5e1;
    }}

    .rapid-lines-box {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 12px;
    }}
    .rapid-line {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
    }}
    .write-line {{
      flex: 1;
      border-bottom: 1px dotted #94a3b8;
      height: 20px;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation & Print Bar (Strictly Fluency Drills Only) -->
  <div class="print-bar">
    <div>
      <a href="../worksheets.html#digital-skills"><i class="fa-solid fa-arrow-left"></i> Worksheets Directory</a>
    </div>
    <div>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-bolt"></i> Fluency Drills</span>
        <a href="{answers_url}" class="nav-pill-btn"><i class="fa-solid fa-check"></i> Worked Answers</a>
      </div>
      <a href="{guide_url}" class="btn-action-answers" target="_blank" style="background:#0284c7;"><i class="fa-solid fa-book-open"></i> Study Guide</a>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-graduation-cap"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Pearson Edexcel &amp; City &amp; Guilds Aligned Corbett-Style Fluency Workout</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level_title} DFSQ</div><br>
        <span class="badge-spec">Ofqual Regulated Criteria</span>
      </div>
    </div>

    <!-- Candidate Info (6 Drills + Recall: 15 Marks Total) -->
    <div class="candidate-info-box">
      <div class="candidate-info-item"><strong>Candidate Name:</strong> <span class="field-line"></span></div>
      <div class="candidate-info-item"><strong>Date:</strong> <span class="field-line"></span></div>
      <div class="candidate-info-item" style="max-width:140px;"><strong>Marks:</strong> <span class="field-line"></span> / 15</div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{html.escape(title)}</h1>
        <div class="hero-subtitle">{skill_area} &bull; Standard Code: {code}</div>
      </div>
      <div class="hero-tag">Style 1: Workout (6 Drills)</div>
    </div>

    <!-- Key Method Rules Summary -->
    <div class="rules-card">
      <div class="rules-card-title"><i class="fa-solid fa-lightbulb"></i> Core Rules &amp; Methods to Remember:</div>
      <ul class="rules-list">
        {rules_html}
      </ul>
    </div>

    <!-- Drill Questions -->
    {drills_html}

    <!-- Rapid Recall Check -->
    {rapid_recall_html}

  </div>

</body>
</html>
'''


def render_workout_answers_html(topic, level_code, level_title):
    slug = topic['slug']
    title = topic['title']
    code = topic['code']
    skill_area = topic['skill_area']
    drills = list(topic.get('drills', [])) + EXTRA_DRILLS.get(slug, [])
    workout_url = f"{slug}-workout.html"
    guide_url = f"../digital-skills/{level_code}/{slug}.html"

    # Answers content
    drills_answers_html = ""
    for idx, d in enumerate(drills, 1):
        options_html = ""
        correct_explanation = d.get('explanation', '')
        for opt_idx, opt in enumerate(d.get('options', [])):
            letter = chr(65 + opt_idx)
            is_corr = opt.get('correct') or opt.get('is_correct') or False
            if is_corr:
                if not correct_explanation:
                    correct_explanation = opt.get('why') or opt.get('explanation', '')
                options_html += f'''
                <div class="drill-option-item correct">
                  <span class="option-check-box correct"><i class="fa-solid fa-check"></i></span>
                  <span class="option-letter correct">{letter}.</span>
                  <span class="option-text correct"><strong>{html.escape(opt.get('text', ''))}</strong> (CORRECT)</span>
                </div>'''
            else:
                options_html += f'''
                <div class="drill-option-item">
                  <span class="option-check-box"></span>
                  <span class="option-letter">{letter}.</span>
                  <span class="option-text">{html.escape(opt.get('text', ''))}</span>
                </div>'''

        drills_answers_html += f'''
        <div class="workout-question-card">
          <div class="wq-header">
            <span class="wq-number">Task {idx} — Model Solution</span>
            <span class="wq-marks">[2 Marks]</span>
          </div>
          <p class="wq-prompt">{html.escape(d.get('question', ''))}</p>
          <div class="wq-options-grid">
            {options_html}
          </div>
          <div class="answer-diagnostic-box">
            <div class="diag-header"><i class="fa-solid fa-circle-info"></i> Tutor Diagnostic Explanation:</div>
            <p class="diag-body">{html.escape(correct_explanation)}</p>
          </div>
        </div>
        '''

    # Rapid recall model answer
    recall_answers_html = ""
    step_items = topic.get('steps', [])
    for r_idx, s in enumerate(step_items[:3], 1):
        callout = s.get('callout', {})
        t_text = callout.get('text') or clean_html_text(s.get('body', ''))[:140]
        clean_text = clean_html_text(t_text)
        recall_answers_html += f'<li><strong>Rule {r_idx}:</strong> {html.escape(s.get("title", f"Rule {r_idx}"))} &mdash; {html.escape(clean_text)}</li>\n'
    if not recall_answers_html and 'exam_model' in topic:
        t_rule = topic['exam_model'].get('tutor_rule', '')
        recall_answers_html = f'<li><strong>Core Rule:</strong> {html.escape(t_rule)}</li>'

    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {html.escape(title)} Fluency Answers Key ({level_title})</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/mfs-worksheets.css?v=20261024c">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
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
    .print-bar a:hover {{ color: #ffffff; text-decoration: underline; }}
    .btn-action-print {{
      background: #059669;
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
    .btn-action-print:hover {{ background: #047857; }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
    }}
    .nav-pill-btn:hover:not(.active) {{ background: rgba(255, 255, 255, 0.18); color: #ffffff; }}
    .nav-pill-btn.active {{
      background: #059669;
      color: #ffffff;
      cursor: default;
    }}

    @media print {{
      .print-bar {{ display: none !important; }}
      body {{ background: #ffffff !important; }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .workout-question-card {{ page-break-inside: avoid; }}
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
    .brand-title i {{ color: #059669; }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{ text-align: right; }}
    .badge-level {{
      background: #dcfce7;
      color: #166534;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.82rem;
      border: 1px solid #86efac;
      display: inline-block;
      margin-bottom: 4px;
    }}
    .badge-spec {{
      font-size: 0.78rem;
      color: #64748b;
      font-weight: 600;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #064e3b 0%, #0f766e 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.35rem;
      font-weight: 800;
      margin: 0;
    }}
    .hero-subtitle {{
      font-size: 0.85rem;
      color: #a7f3d0;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .workout-question-card {{
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 20px;
    }}
    .wq-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .wq-number {{
      font-size: 1rem;
      font-weight: 800;
      color: #064e3b;
    }}
    .wq-marks {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #166534;
      background: #dcfce7;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .wq-prompt {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #0f172a;
      margin: 0 0 14px 0;
      line-height: 1.5;
    }}
    .wq-options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }}
    @media (max-width: 600px) {{
      .wq-options-grid {{ grid-template-columns: 1fr; }}
    }}
    .drill-option-item {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      background: #ffffff;
    }}
    .drill-option-item.correct {{
      border: 2px solid #16a34a;
      background: #f0fdf4;
    }}
    .option-check-box {{
      width: 18px;
      height: 18px;
      border: 2px solid #94a3b8;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .option-check-box.correct {{
      background: #16a34a;
      border-color: #16a34a;
      color: #ffffff;
      font-size: 11px;
    }}
    .option-letter {{
      font-weight: 800;
      color: #64748b;
      width: 18px;
      flex-shrink: 0;
    }}
    .option-letter.correct {{ color: #166534; }}
    .option-text {{ font-size: 0.92rem; color: #334155; }}
    .option-text.correct {{ color: #14532d; font-weight: 600; }}

    .answer-diagnostic-box {{
      background: #eff6ff;
      border-left: 4px solid #2563eb;
      padding: 12px 16px;
      border-radius: 4px;
      margin-top: 12px;
    }}
    .diag-header {{
      font-weight: 800;
      color: #1e40af;
      font-size: 0.88rem;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .diag-body {{
      margin: 0;
      font-size: 0.9rem;
      color: #1e293b;
      line-height: 1.45;
    }}

    .recall-box {{
      background: #fdf4ff;
      border: 1.5px solid #f0abfc;
      border-radius: 8px;
      padding: 16px 20px;
      margin-top: 20px;
    }}
    .recall-title {{
      font-weight: 800;
      color: #86198f;
      font-size: 0.95rem;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .recall-list {{
      margin: 0;
      padding-left: 20px;
      color: #701a75;
      font-size: 0.92rem;
      line-height: 1.55;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation & Print Bar (Strictly Fluency Answers Only) -->
  <div class="print-bar">
    <div>
      <a href="../worksheets.html#digital-skills"><i class="fa-solid fa-arrow-left"></i> Worksheets Directory</a>
    </div>
    <div>
      <div class="nav-pill-group">
        <a href="{workout_url}" class="nav-pill-btn"><i class="fa-solid fa-bolt"></i> Fluency Drills</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-check"></i> Worked Answers</span>
      </div>
      <a href="{guide_url}" class="btn-action-answers" target="_blank" style="background:#0284c7;"><i class="fa-solid fa-book-open"></i> Study Guide</a>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-graduation-cap"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Tutor Abdul &bull; Fluency Workout Answer Key &amp; Diagnostics</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level_title} Worked Key</div><br>
        <span class="badge-spec">Ofqual Regulated Criteria</span>
      </div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{html.escape(title)} — Answer Key</h1>
        <div class="hero-subtitle">{skill_area} &bull; Standard Code: {code}</div>
      </div>
      <div class="hero-tag">Style 1: Solutions (6 Drills)</div>
    </div>

    <!-- Drills Answers List -->
    {drills_answers_html}

    <!-- Rapid Recall Answers -->
    <div class="recall-box">
      <div class="recall-title"><i class="fa-solid fa-star"></i> Rapid Recall Model Rules:</div>
      <ul class="recall-list">
        {recall_answers_html}
      </ul>
    </div>

  </div>

</body>
</html>
'''


def build_doubled_practice_tasks(topic):
    """
    Constructs 4 distinct, authentic exam tasks per worksheet doubling the practice questions [12 Marks].
    """
    title = topic['title']
    practice = topic.get('practice', {})
    exam_model = topic.get('exam_model', {})
    steps = topic.get('steps', [])

    # Task 1: Core Workplace Task
    raw_task = practice.get('task') or practice.get('scenario', '')
    clean_task1 = clean_html_text(raw_task)
    starter = practice.get('scaffold_starter', '')

    # Task 2: Applied Workplace Problem
    raw_task2 = exam_model.get('scenario', '')
    clean_task2 = clean_html_text(raw_task2)
    if not clean_task2:
        clean_task2 = f"A department administrator must carry out an urgent workflow task involving {title}. Explain the step-by-step method they must apply to complete this task efficiently without disrupting office systems."

    # Task 3: Troubleshooting & Error Prevention
    step2 = steps[1] if len(steps) > 1 else steps[0]
    step2_title = step2.get('title', 'Technical Configuration')
    callout2 = step2.get('callout', {})
    c2_text = clean_html_text(callout2.get('text', ''))
    if c2_text:
        clean_task3 = f"A colleague is encountering an issue related to {step2_title}. They are concerned that:\n\"{c2_text[:200]}\"\nDescribe two practical actions or checks the colleague should carry out to resolve this issue and prevent errors."
    else:
        clean_task3 = f"During a busy workplace shift, a team member makes an error while handling {step2_title}. Identify one risk associated with this mistake, and describe the exact troubleshooting procedure required to correct it."

    # Task 4: Workplace Quality Assurance & Policy Evaluation
    tutor_rule = clean_html_text(exam_model.get('tutor_rule', ''))
    if tutor_rule:
        clean_task4 = f"Before confirming completion of any task involving {title}, the organisation requires all staff to verify their work. Consider Tutor Abdul's standard rule:\n\"{tutor_rule[:200]}\"\nState two quality checks an employee must complete to verify their work meets workplace data security and operational standards."
    else:
        clean_task4 = f"Explain two essential data security or digital etiquette guidelines an employee must follow when performing tasks related to {title} in a professional environment."

    return [
        {
            "num": 1,
            "title": "Task 1 — Core Workplace Scenario Task",
            "marks": 3,
            "prompt": clean_task1,
            "starter": starter
        },
        {
            "num": 2,
            "title": "Task 2 — Applied Workplace Problem",
            "marks": 3,
            "prompt": clean_task2,
            "starter": ""
        },
        {
            "num": 3,
            "title": "Task 3 — Troubleshooting & Error Resolution",
            "marks": 3,
            "prompt": clean_task3,
            "starter": ""
        },
        {
            "num": 4,
            "title": "Task 4 — Quality Assurance & Workplace Policy",
            "marks": 3,
            "prompt": clean_task4,
            "starter": ""
        }
    ]


def render_worksheet_html(topic, level_code, level_title):
    slug = topic['slug']
    title = topic['title']
    code = topic['code']
    skill_area = topic['skill_area']
    answers_url = f"{slug}-answers.html"
    guide_url = f"../digital-skills/{level_code}/{slug}.html"

    tasks = build_doubled_practice_tasks(topic)
    tasks_html = ""
    for t in tasks:
        starter_html = ""
        if t.get('starter'):
            starter_html = f'''
            <div style="background:#f8fafc; border:1px dashed #94a3b8; border-radius:6px; padding:10px 14px; margin:12px 0; font-family:monospace; font-size:0.9rem; color:#334155; white-space:pre-wrap;">
              <strong>Starter Template / Candidate Workspace:</strong>\n{html.escape(t['starter'])}
            </div>'''

        tasks_html += f'''
        <div class="exam-task-box">
          <div class="task-number-row">
            <span class="task-num">{html.escape(t['title'])}</span>
            <span class="task-marks">[{t['marks']} Marks]</span>
          </div>
          <p class="task-text">{html.escape(t['prompt'])}</p>
          {starter_html}
          <div class="lined-working-area">
            <div class="rule-line"></div>
            <div class="rule-line"></div>
            <div class="rule-line"></div>
            <div class="rule-line"></div>
          </div>
        </div>
        '''

    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {html.escape(title)} Exam Practice ({level_title})</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/mfs-worksheets.css?v=20261024c">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
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
    .print-bar a:hover {{ color: #ffffff; text-decoration: underline; }}
    .btn-action-print {{
      background: #7c3aed;
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
    .btn-action-print:hover {{ background: #6d28d9; }}
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
      margin-left: 10px;
    }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
    }}
    .nav-pill-btn:hover:not(.active) {{ background: rgba(255, 255, 255, 0.18); color: #ffffff; }}
    .nav-pill-btn.active {{
      background: #7c3aed;
      color: #ffffff;
      cursor: default;
    }}

    @media print {{
      .print-bar {{ display: none !important; }}
      body {{ background: #ffffff !important; }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .exam-task-box {{ page-break-inside: avoid; }}
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
    .brand-title i {{ color: #7c3aed; }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{ text-align: right; }}
    .badge-level {{
      background: #f5f3ff;
      color: #6d28d9;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.82rem;
      border: 1px solid #ddd6fe;
      display: inline-block;
      margin-bottom: 4px;
    }}
    .badge-spec {{
      font-size: 0.78rem;
      color: #64748b;
      font-weight: 600;
    }}

    .candidate-info-box {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 16px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 20px;
    }}
    .candidate-info-item {{
      font-size: 0.88rem;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .field-line {{
      flex: 1;
      border-bottom: 1px dotted #94a3b8;
      height: 18px;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.35rem;
      font-weight: 800;
      margin: 0;
    }}
    .hero-subtitle {{
      font-size: 0.85rem;
      color: #e9d5ff;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .exam-task-box {{
      background: #ffffff;
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      padding: 20px 22px;
      margin-bottom: 20px;
    }}
    .task-number-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid #e2e8f0;
    }}
    .task-num {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #4c1d95;
    }}
    .task-marks {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #6d28d9;
      background: #f5f3ff;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .task-text {{
      font-size: 1rem;
      color: #0f172a;
      line-height: 1.6;
      margin: 0 0 16px 0;
      white-space: pre-wrap;
    }}
    .lined-working-area {{
      display: flex;
      flex-direction: column;
      gap: 18px;
      padding-top: 10px;
    }}
    .rule-line {{
      border-bottom: 1px solid #cbd5e1;
      height: 12px;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation & Print Bar (Strictly Practice Exam Only) -->
  <div class="print-bar">
    <div>
      <a href="../worksheets.html#digital-skills"><i class="fa-solid fa-arrow-left"></i> Worksheets Directory</a>
    </div>
    <div>
      <div class="nav-pill-group">
        <span class="nav-pill-btn active"><i class="fa-solid fa-file-pen"></i> Practice Exam</span>
        <a href="{answers_url}" class="nav-pill-btn"><i class="fa-solid fa-award"></i> Mark Scheme</a>
      </div>
      <a href="{guide_url}" class="btn-action-answers" target="_blank" style="background:#0284c7;"><i class="fa-solid fa-book-open"></i> Study Guide</a>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-graduation-cap"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Pearson Edexcel &amp; City &amp; Guilds Aligned Practice Exam Tasks (4 Comprehensive Tasks)</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level_title} DFSQ Exam</div><br>
        <span class="badge-spec">Ofqual Regulated Criteria</span>
      </div>
    </div>

    <!-- Candidate Info (Doubled Tasks: 12 Marks Total) -->
    <div class="candidate-info-box">
      <div class="candidate-info-item"><strong>Candidate Name:</strong> <span class="field-line"></span></div>
      <div class="candidate-info-item"><strong>Date:</strong> <span class="field-line"></span></div>
      <div class="candidate-info-item" style="max-width:140px;"><strong>Marks:</strong> <span class="field-line"></span> / 12</div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{html.escape(title)}</h1>
        <div class="hero-subtitle">{skill_area} &bull; Standard Code: {code}</div>
      </div>
      <div class="hero-tag">Style 2: Practice (4 Tasks)</div>
    </div>

    <!-- Doubled Exam Tasks -->
    {tasks_html}

  </div>

</body>
</html>
'''


def render_answers_html(topic, level_code, level_title):
    slug = topic['slug']
    title = topic['title']
    code = topic['code']
    skill_area = topic['skill_area']
    practice = topic.get('practice', {})
    exam_model = topic.get('exam_model', {})
    steps = topic.get('steps', [])

    worksheet_url = f"{slug}-worksheet.html"
    guide_url = f"../digital-skills/{level_code}/{slug}.html"

    # Doubled Model Answers
    ans1 = clean_html_text(practice.get('model_answer', ''))
    
    # Task 2 answer from exam_model steps
    em_steps = exam_model.get('steps', [])
    ans2_parts = []
    for s in em_steps:
        s_title = s.get('title', '')
        s_desc = clean_html_text(s.get('desc', ''))
        ans2_parts.append(f"{s_title}: {s_desc}")
    ans2 = "\n".join(ans2_parts) if ans2_parts else f"Follow accurate procedural sequence for {title} according to system protocols."

    # Task 3 answer from step 2
    step2 = steps[1] if len(steps) > 1 else steps[0]
    callout2 = step2.get('callout', {})
    c2_text = clean_html_text(callout2.get('text', ''))
    ans3 = c2_text if c2_text else f"Identify the faulty setting or input, open the corresponding device options or preferences, and reset the parameter accurately to restore normal operation."

    # Task 4 answer from tutor rule
    tutor_rule = clean_html_text(exam_model.get('tutor_rule', ''))
    ans4 = tutor_rule if tutor_rule else f"Check 1: Confirm accurate data formatting and precise terminology. Check 2: Verify that file access permissions and data security requirements are fully met."

    model_answers_html = f'''
    <div class="model-answer-card">
      <div class="model-card-title"><i class="fa-solid fa-star"></i> Task 1 Benchmark Solution:</div>
      <div class="model-body-text">{html.escape(ans1)}</div>
    </div>

    <div class="model-answer-card">
      <div class="model-card-title"><i class="fa-solid fa-star"></i> Task 2 Applied Scenario Solution:</div>
      <div class="model-body-text">{html.escape(ans2)}</div>
    </div>

    <div class="model-answer-card">
      <div class="model-card-title"><i class="fa-solid fa-star"></i> Task 3 Troubleshooting Solution:</div>
      <div class="model-body-text">{html.escape(ans3)}</div>
    </div>

    <div class="model-answer-card">
      <div class="model-card-title"><i class="fa-solid fa-star"></i> Task 4 Quality Assurance &amp; Policy Solution:</div>
      <div class="model-body-text">{html.escape(ans4)}</div>
    </div>
    '''

    # 4 Rows Mark Scheme Table
    scheme_rows_html = f'''
    <tr>
      <td style="font-weight:700; color:#0f172a;">Task 1</td>
      <td>Accurate classification, structured execution, and adherence to specified workplace criteria.</td>
      <td style="font-weight:700; color:#16a34a; text-align:center;">[3 Marks]</td>
    </tr>
    <tr>
      <td style="font-weight:700; color:#0f172a;">Task 2</td>
      <td>Appropriate method selection, step-by-step problem resolution, and clear written justification.</td>
      <td style="font-weight:700; color:#16a34a; text-align:center;">[3 Marks]</td>
    </tr>
    <tr>
      <td style="font-weight:700; color:#0f172a;">Task 3</td>
      <td>Accurate identification of digital error/risk, and application of proper troubleshooting workflow.</td>
      <td style="font-weight:700; color:#16a34a; text-align:center;">[3 Marks]</td>
    </tr>
    <tr>
      <td style="font-weight:700; color:#0f172a;">Task 4</td>
      <td>Rigorous quality assurance verification and compliance with workplace data protection and security policies.</td>
      <td style="font-weight:700; color:#16a34a; text-align:center;">[3 Marks]</td>
    </tr>
    '''

    tutor_tip = tutor_rule if tutor_rule else "Award full marks when the candidate demonstrates accurate methodology and uses correct digital workplace terminology. Ensure spelling of key commands and formulas is precise."

    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Functional Skills — {html.escape(title)} Mark Scheme ({level_title})</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/mfs-worksheets.css?v=20261024c">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 12mm 15mm;
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
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
    .print-bar a:hover {{ color: #ffffff; text-decoration: underline; }}
    .btn-action-print {{
      background: #059669;
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
    .btn-action-print:hover {{ background: #047857; }}
    .nav-pill-group {{
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      border-radius: 8px;
      padding: 3px;
      margin-right: 12px;
    }}
    .nav-pill-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.88rem;
      color: #cbd5e1;
      text-decoration: none;
    }}
    .nav-pill-btn:hover:not(.active) {{ background: rgba(255, 255, 255, 0.18); color: #ffffff; }}
    .nav-pill-btn.active {{
      background: #059669;
      color: #ffffff;
      cursor: default;
    }}

    @media print {{
      .print-bar {{ display: none !important; }}
      body {{ background: #ffffff !important; }}
      .page-sheet {{
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}
      .mark-scheme-box, .model-answer-card {{ page-break-inside: avoid; }}
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
    .brand-title i {{ color: #059669; }}
    .sheet-sub {{
      font-size: 0.9rem;
      color: #475569;
      font-weight: 600;
      margin-top: 4px;
    }}
    .header-badges {{ text-align: right; }}
    .badge-level {{
      background: #dcfce7;
      color: #166534;
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.82rem;
      border: 1px solid #86efac;
      display: inline-block;
      margin-bottom: 4px;
    }}
    .badge-spec {{
      font-size: 0.78rem;
      color: #64748b;
      font-weight: 600;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #064e3b 0%, #0f766e 100%);
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .hero-title {{
      font-size: 1.35rem;
      font-weight: 800;
      margin: 0;
    }}
    .hero-subtitle {{
      font-size: 0.85rem;
      color: #a7f3d0;
      margin-top: 4px;
    }}
    .hero-tag {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .model-answer-card {{
      background: #f0fdf4;
      border: 1.5px solid #86efac;
      border-radius: 8px;
      padding: 16px 18px;
      margin-bottom: 18px;
    }}
    .model-card-title {{
      font-weight: 800;
      color: #166534;
      font-size: 0.95rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .model-body-text {{
      font-size: 0.92rem;
      color: #14532d;
      line-height: 1.55;
      white-space: pre-wrap;
    }}

    .mark-scheme-box {{
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 20px;
    }}
    .scheme-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }}
    .scheme-table th {{
      background: #0f172a;
      color: #ffffff;
      padding: 10px 14px;
      text-align: left;
      font-weight: 700;
    }}
    .scheme-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: top;
      color: #334155;
    }}
    .scheme-table tr:nth-child(even) td {{
      background: #f8fafc;
    }}

    .tutor-note-card {{
      background: #f8fafc;
      border-left: 4px solid #0284c7;
      padding: 12px 16px;
      border-radius: 6px;
      font-size: 0.88rem;
      color: #475569;
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation & Print Bar (Strictly Mark Scheme Only) -->
  <div class="print-bar">
    <div>
      <a href="../worksheets.html#digital-skills"><i class="fa-solid fa-arrow-left"></i> Worksheets Directory</a>
    </div>
    <div>
      <div class="nav-pill-group">
        <a href="{worksheet_url}" class="nav-pill-btn"><i class="fa-solid fa-file-pen"></i> Practice Exam</a>
        <span class="nav-pill-btn active"><i class="fa-solid fa-award"></i> Mark Scheme</span>
      </div>
      <a href="{guide_url}" class="btn-action-answers" target="_blank" style="background:#0284c7;"><i class="fa-solid fa-book-open"></i> Study Guide</a>
      <button class="btn-action-print" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save PDF</button>
    </div>
  </div>

  <div class="page-sheet">
    <!-- Sheet Header -->
    <div class="sheet-header">
      <div>
        <div class="brand-title"><i class="fa-solid fa-award"></i> MASTER FUNCTIONAL SKILLS</div>
        <div class="sheet-sub">Official Pearson Edexcel Aligned Marking Scheme &amp; Model Solutions (12 Marks Total)</div>
      </div>
      <div class="header-badges">
        <div class="badge-level">{level_title} Mark Scheme</div><br>
        <span class="badge-spec">Tutor Abdul &bull; Accredited Guide</span>
      </div>
    </div>

    <!-- Hero Title Banner -->
    <div class="hero-banner">
      <div>
        <h1 class="hero-title">{html.escape(title)} — Mark Scheme</h1>
        <div class="hero-subtitle">{skill_area} &bull; Standard Code: {code}</div>
      </div>
      <div class="hero-tag">Style 2: Solutions (4 Tasks)</div>
    </div>

    <!-- 4 Doubled Model Answers -->
    {model_answers_html}

    <!-- Mark Scheme Criteria Table -->
    <div class="mark-scheme-box">
      <table class="scheme-table">
        <thead>
          <tr>
            <th style="width:100px;">Task</th>
            <th>Assessment Criteria &amp; Expected Candidate Performance</th>
            <th style="width:90px; text-align:center;">Marks</th>
          </tr>
        </thead>
        <tbody>
          {scheme_rows_html}
        </tbody>
      </table>
    </div>

    <!-- Tutor Guidance Note -->
    <div class="tutor-note-card">
      <strong><i class="fa-solid fa-chalkboard-user"></i> Tutor Abdul's Marking Tip:</strong>
      {html.escape(tutor_tip)}
    </div>

  </div>

</body>
</html>
'''


def generate_worksheets_html_section(e3_topics, l1_topics):
    def build_topic_cards(topics, level_code, level_title):
        cards = ""
        for t in topics:
            slug = t['slug']
            title = t['title']
            code = t['code']
            skill_area = t['skill_area']

            guide_url = f"digital-skills/{level_code}/{slug}.html"
            workout_url = f"worksheets/{slug}-workout.html"
            workout_ans_url = f"worksheets/{slug}-workout-answers.html"
            worksheet_url = f"worksheets/{slug}-worksheet.html"
            answers_url = f"worksheets/{slug}-answers.html"

            cards += f'''
            <div class="hub-topic-card" data-topic-name="{slug} {title.lower()} {code.lower()} {level_title.lower()}">
              <div class="hub-topic-header">
                <div>
                  <h3 class="hub-topic-title"><a href="{guide_url}">{html.escape(title)}</a></h3>
                  <div class="hub-topic-badges">
                    <span class="hub-badge-level">{level_title} DFSQ</span>
                    <span class="hub-badge-spec">{html.escape(skill_area.split('.')[0])} &bull; {code}</span>
                  </div>
                </div>
                <a href="{guide_url}" class="hub-btn-guide" title="View interactive study guide">
                  <i class="fa-solid fa-book-bookmark"></i> Study Guide
                </a>
              </div>
              
              <div class="hub-action-row">
                <!-- Style 1: Fluency Drills -->
                <div class="hub-style-group style-workout">
                  <div class="hub-style-label"><i class="fa-solid fa-repeat text-blue"></i> Style 1: Fluency Drills</div>
                  <div class="hub-btn-pair">
                    <a href="{workout_url}" target="_blank" class="hub-btn btn-workout" title="High-repetition fluency drills">
                      <i class="fa-solid fa-pen-ruler"></i> Fluency Drills
                    </a>
                    <a href="{workout_ans_url}" target="_blank" class="hub-btn btn-ans" title="Worked answer key">
                      <i class="fa-solid fa-check"></i> Answers
                    </a>
                  </div>
                </div>

                <!-- Style 2: Exam Practice -->
                <div class="hub-style-group style-exam">
                  <div class="hub-style-label"><i class="fa-solid fa-file-shield text-purple"></i> Style 2: Practice Questions</div>
                  <div class="hub-btn-pair">
                    <a href="{worksheet_url}" target="_blank" class="hub-btn btn-practice" title="Pearson Edexcel exam questions">
                      <i class="fa-solid fa-file-pen"></i> Practice Questions
                    </a>
                    <a href="{answers_url}" target="_blank" class="hub-btn btn-ans" title="Step-by-step mark scheme">
                      <i class="fa-solid fa-award"></i> Mark Scheme
                    </a>
                  </div>
                </div>
              </div>
            </div>
            '''
        return cards

    e3_cards_html = build_topic_cards(e3_topics, "entry-3", "Entry 3")
    l1_cards_html = build_topic_cards(l1_topics, "level-1", "Level 1")

    section_html = f'''        <section class="hub-domain-section" id="digital-skills">
          <div class="hub-domain-header">
            <div class="domain-icon-circle"><i class="fa-solid fa-laptop-code"></i></div>
            <div>
              <h2 class="domain-title">Digital Functional Skills (DFSQ)</h2>
              <div class="domain-count">39 Dedicated Topics &bull; Entry 3 (18) &amp; Level 1 (21)</div>
            </div>
          </div>

          <!-- DFS Level Switcher Navigation Bar inside worksheets -->
          <div style="background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:12px; padding:14px 20px; margin-bottom:24px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div style="font-weight:700; color:#0f172a; font-size:0.95rem;">
              <i class="fa-solid fa-filter" style="color:#0284c7; margin-right:6px;"></i> Select Digital Qualification Level:
            </div>
            <div style="display:flex; gap:8px;">
              <a href="#dfs-level-1-section" class="hub-btn" style="background:#0284c7; color:#ffffff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:700; text-decoration:none;">
                <i class="fa-solid fa-award"></i> Jump to Level 1 (21 Topics)
              </a>
              <a href="#dfs-entry-3-section" class="hub-btn" style="background:#0f766e; color:#ffffff; padding:6px 14px; border-radius:6px; font-size:0.85rem; font-weight:700; text-decoration:none;">
                <i class="fa-solid fa-seedling"></i> Jump to Entry 3 (18 Topics)
              </a>
            </div>
          </div>

          <!-- 1. LEVEL 1 DFSQ WORKSHEETS -->
          <div id="dfs-level-1-section" style="margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px; padding-bottom:8px; border-bottom:2px solid #0284c7;">
              <span class="hub-badge-level" style="background:#0284c7; color:#ffffff; font-size:0.9rem; padding:4px 12px;">Level 1 DFSQ</span>
              <h3 style="margin:0; font-size:1.3rem; font-weight:800; color:#0f172a;">Level 1 Digital Functional Skills (21 Topics)</h3>
            </div>
            <div class="hub-topics-grid">
              {l1_cards_html}
            </div>
          </div>

          <!-- 2. ENTRY 3 DFSQ WORKSHEETS -->
          <div id="dfs-entry-3-section">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px; padding-bottom:8px; border-bottom:2px solid #0f766e;">
              <span class="hub-badge-level" style="background:#0f766e; color:#ffffff; font-size:0.9rem; padding:4px 12px;">Entry 3 DFSQ</span>
              <h3 style="margin:0; font-size:1.3rem; font-weight:800; color:#0f172a;">Entry 3 Digital Functional Skills (18 Topics)</h3>
            </div>
            <div class="hub-topics-grid">
              {e3_cards_html}
            </div>
          </div>
        </section>'''

    return section_html


def update_worksheets_hub(section_html):
    hub_path = os.path.join(BASE_DIR, "worksheets.html")
    if not os.path.exists(hub_path):
        print(f"Error: {hub_path} not found")
        return False

    with open(hub_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r'<section class="hub-domain-section" id="digital-skills">.*?</section>',
        re.DOTALL
    )

    if not pattern.search(content):
        print("Error: Could not locate <section class='hub-domain-section' id='digital-skills'> in worksheets.html")
        return False

    new_content = pattern.sub(section_html, content)
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully updated worksheets.html with Entry 3 & Level 1 DFS sections!")
    return True


def main():
    print(f"Generating Entry 3 Worksheets ({len(ALL_ENTRY_3_TOPICS)} topics x 4 files = 72 files)...")
    e3_files = []
    for topic in ALL_ENTRY_3_TOPICS:
        slug = topic['slug']
        # 1. Workout (Fluency Drills)
        w_html = render_workout_html(topic, "entry-3", "Entry 3")
        w_path = os.path.join(WORKSHEETS_DIR, f"{slug}-workout.html")
        with open(w_path, "w", encoding="utf-8") as f: f.write(w_html)
        e3_files.append(w_path)

        # 2. Workout Answers
        wa_html = render_workout_answers_html(topic, "entry-3", "Entry 3")
        wa_path = os.path.join(WORKSHEETS_DIR, f"{slug}-workout-answers.html")
        with open(wa_path, "w", encoding="utf-8") as f: f.write(wa_html)
        e3_files.append(wa_path)

        # 3. Worksheet (4 Doubled Practice Exam Tasks)
        ws_html = render_worksheet_html(topic, "entry-3", "Entry 3")
        ws_path = os.path.join(WORKSHEETS_DIR, f"{slug}-worksheet.html")
        with open(ws_path, "w", encoding="utf-8") as f: f.write(ws_html)
        e3_files.append(ws_path)

        # 4. Answers (4 Tasks Mark Scheme)
        ans_html = render_answers_html(topic, "entry-3", "Entry 3")
        ans_path = os.path.join(WORKSHEETS_DIR, f"{slug}-answers.html")
        with open(ans_path, "w", encoding="utf-8") as f: f.write(ans_html)
        e3_files.append(ans_path)

    print(f"Successfully created {len(e3_files)} Entry 3 worksheet files.")

    print(f"\nGenerating Level 1 Worksheets ({len(ALL_LEVEL_1_TOPICS)} topics x 4 files = 84 files)...")
    l1_files = []
    for topic in ALL_LEVEL_1_TOPICS:
        slug = topic['slug']
        # 1. Workout (Fluency Drills)
        w_html = render_workout_html(topic, "level-1", "Level 1")
        w_path = os.path.join(WORKSHEETS_DIR, f"{slug}-workout.html")
        with open(w_path, "w", encoding="utf-8") as f: f.write(w_html)
        l1_files.append(w_path)

        # 2. Workout Answers
        wa_html = render_workout_answers_html(topic, "level-1", "Level 1")
        wa_path = os.path.join(WORKSHEETS_DIR, f"{slug}-workout-answers.html")
        with open(wa_path, "w", encoding="utf-8") as f: f.write(wa_html)
        l1_files.append(wa_path)

        # 3. Worksheet (4 Doubled Practice Exam Tasks)
        ws_html = render_worksheet_html(topic, "level-1", "Level 1")
        ws_path = os.path.join(WORKSHEETS_DIR, f"{slug}-worksheet.html")
        with open(ws_path, "w", encoding="utf-8") as f: f.write(ws_html)
        l1_files.append(ws_path)

        # 4. Answers (4 Tasks Mark Scheme)
        ans_html = render_answers_html(topic, "level-1", "Level 1")
        ans_path = os.path.join(WORKSHEETS_DIR, f"{slug}-answers.html")
        with open(ans_path, "w", encoding="utf-8") as f: f.write(ans_html)
        l1_files.append(ans_path)

    print(f"Successfully created {len(l1_files)} Level 1 worksheet files.")
    print(f"Total worksheet files generated: {len(e3_files) + len(l1_files)} files.")

    print("\nUpdating worksheets.html with Entry 3 & Level 1 DFS domains...")
    section_html = generate_worksheets_html_section(ALL_ENTRY_3_TOPICS, ALL_LEVEL_1_TOPICS)
    update_worksheets_hub(section_html)
    print("\nBuild complete!")


if __name__ == "__main__":
    main()
