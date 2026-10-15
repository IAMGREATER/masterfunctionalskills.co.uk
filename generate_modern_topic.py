#!/usr/bin/env python3
"""
Master Functional Skills — Original Topic Page & Worksheet Generator
Generates:
1. Modern, dyslexia-friendly revision topic HTML (replacing scraped PFS pages)
2. Branded printable A4 Worksheet HTML (with 1-click Save to PDF)
3. Branded printable A4 Answer Key HTML with Tutor model solutions & mark schemes
"""

import os
import sys

def build_topic_page(topic_data):
    slug = topic_data['slug']
    title = topic_data['title']
    subject = topic_data.get('subject', 'Maths')
    levels = topic_data.get('levels', ['Level 1', 'Level 2'])
    level_str = " & ".join(levels)
    spec_codes = topic_data.get('spec_codes', 'Pearson Edexcel: L1.1, L2.1')
    intro_summary = topic_data['intro_summary']
    video_duration = topic_data.get('video_duration', '14:20')
    video_chapters = topic_data.get('video_chapters', [])
    key_rules = topic_data.get('key_rules', [])
    worked_examples = topic_data.get('worked_examples', [])
    examiner_traps = topic_data.get('examiner_traps', [])
    practice_questions = topic_data.get('practice_questions', [])
    
    # Chapter markup
    chapters_html = ""
    for ch in video_chapters:
        chapters_html += f"""
        <div class="video-chapter-item">
          <span class="chapter-time">{ch['time']}</span>
          <span class="chapter-title">{ch['title']}</span>
        </div>"""

    # Key rules markup
    rules_html = ""
    for r in key_rules:
        rules_html += f"""
        <div class="mfs-rule-card">
          <div class="rule-icon"><i class="{r.get('icon', 'fa-solid fa-lightbulb')}"></i></div>
          <div class="rule-content">
            <h4>{r['title']}</h4>
            <p>{r['desc']}</p>
          </div>
        </div>"""

    # Worked examples markup
    worked_html = ""
    for i, ex in enumerate(worked_examples, 1):
        steps_html = ""
        for st in ex['steps']:
            steps_html += f"""
            <div class="step-item">
              <div class="step-badge">{st['step']}</div>
              <div class="step-body">
                <strong>{st['action']}</strong>
                <div class="step-math">{st['math']}</div>
                <div class="step-mark-tag"><i class="fa-solid fa-check"></i> {st['mark']}</div>
              </div>
            </div>"""

        worked_html += f"""
        <div class="worked-model-box">
          <div class="worked-model-header">
            <span class="model-badge">Worked Exam Model #{i}</span>
            <span class="exam-level-pill">{ex.get('level', 'Level 2 Exam Standard')}</span>
          </div>
          <div class="worked-question-stem">
            <strong>Question:</strong> {ex['question']}
          </div>
          <div class="steps-container">
            {steps_html}
          </div>
          <div class="worked-final-answer">
            <i class="fa-solid fa-award"></i> <strong>Final Exam Answer:</strong> {ex['final_answer']}
          </div>
        </div>"""

    # Examiner traps markup
    traps_html = ""
    for tr in examiner_traps:
        traps_html += f"""
        <div class="trap-card">
          <div class="trap-header">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span>{tr['title']}</span>
          </div>
          <p>{tr['desc']}</p>
          <div class="trap-how-to-fix">
            <strong><i class="fa-solid fa-shield-check"></i> How to avoid:</strong> {tr['solution']}
          </div>
        </div>"""

    # Interactive Practice markup
    practice_html = ""
    for idx, q in enumerate(practice_questions, 1):
        practice_html += f"""
        <div class="interactive-q-card" id="q{idx}">
          <div class="q-header">
            <span class="q-number">Practice Question {idx}</span>
            <span class="q-marks">{q.get('marks', 3)} Marks</span>
          </div>
          <div class="q-text">
            {q['question']}
          </div>
          <div class="q-workspace">
            <label for="workspace-q{idx}"><i class="fa-solid fa-pen-to-square"></i> Student Working Out Area:</label>
            <textarea id="workspace-q{idx}" class="q-scratchpad" placeholder="Type your step-by-step calculations and notes here..."></textarea>
          </div>
          <div class="q-actions">
            <button type="button" class="btn-reveal-solution" onclick="toggleSolution('sol{idx}')">
              <i class="fa-solid fa-eye"></i> Show Tutor Method & Mark Scheme
            </button>
            <div class="video-sol-pill">
              <i class="fa-brands fa-youtube"></i> Video Solution Walkthrough (In Production)
            </div>
          </div>
          <div id="sol{idx}" class="revealed-solution" style="display:none;">
            <div class="sol-inner">
              <div class="sol-header">
                <i class="fa-solid fa-circle-check"></i> Step-by-Step Mark Scheme (Pearson Edexcel Standard)
              </div>
              <div class="sol-steps">
                {q['solution_steps']}
              </div>
              <div class="sol-final">
                <strong>Correct Answer:</strong> {q['correct_answer']}
              </div>
              <div class="sol-tutor-tip">
                <i class="fa-solid fa-comment-dots"></i> <strong>Tutor's Golden Rule:</strong> {q['tutor_tip']}
              </div>
            </div>
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} Revision Guide & Worksheets | Master Functional Skills</title>
  <meta name="description" content="Master Functional Skills {title} revision. Complete step-by-step guide, Tutor video masterclass, practice worksheets, answer schemes, and exam questions.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <style>
    /* TOPIC REVISION PAGE STYLES */
    .topic-hero {{
      background: linear-gradient(135deg, #0b172d 0%, #102345 100%);
      color: #ffffff;
      padding: 48px 0 40px;
      border-bottom: 3px solid var(--accent);
    }}
    .topic-breadcrumbs {{
      display: flex;
      gap: 8px;
      align-items: center;
      font-size: 0.85rem;
      color: #94a3b8;
      margin-bottom: 16px;
    }}
    .topic-breadcrumbs a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .topic-breadcrumbs a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .topic-hero-title {{
      font-size: 2.3rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
      line-height: 1.25;
    }}
    .topic-meta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 16px;
    }}
    .topic-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
    }}
    .topic-pill-level {{
      background: rgba(37, 99, 235, 0.25);
      border: 1px solid var(--accent);
      color: #93c5fd;
    }}
    .topic-pill-spec {{
      background: rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    .topic-hero-desc {{
      font-size: 1.05rem;
      line-height: 1.6;
      color: #cbd5e1;
      max-width: 820px;
      margin-bottom: 24px;
    }}
    .topic-quick-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .btn-topic-action {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.9rem;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }}
    .btn-topic-action-primary {{
      background: var(--accent);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}
    .btn-topic-action-primary:hover {{
      background: var(--accent-hover);
      transform: translateY(-1px);
    }}
    .btn-topic-action-worksheet {{
      background: #ffffff;
      color: #0b172d;
      border: 1px solid #cbd5e1;
    }}
    .btn-topic-action-worksheet:hover {{
      background: #f8fafc;
      border-color: var(--accent);
      color: var(--accent);
    }}
    .btn-topic-action-answers {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #065f46;
    }}
    .btn-topic-action-answers:hover {{
      background: #10b981;
      color: #ffffff;
    }}

    /* MAIN LAYOUT */
    .topic-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 36px;
      padding: 40px 0 60px;
    }}
    @media (max-width: 991px) {{
      .topic-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    /* SECTION HEADERS */
    .section-h2 {{
      font-size: 1.55rem;
      font-weight: 800;
      color: var(--navy-dark);
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px solid var(--border-light);
      padding-bottom: 10px;
    }}

    /* VIDEO MASTERCLASS PLACEHOLDER */
    .video-masterclass-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      margin-bottom: 36px;
    }}
    .video-placeholder-frame {{
      position: relative;
      background: #0b172d;
      aspect-ratio: 16/9;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 24px;
      color: #ffffff;
      background-image: radial-gradient(circle at center, rgba(37, 99, 235, 0.25) 0%, rgba(11, 23, 45, 0.95) 80%);
    }}
    .video-play-btn {{
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: var(--accent);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      margin-bottom: 16px;
      box-shadow: 0 0 0 10px rgba(37, 99, 235, 0.25);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .video-play-btn:hover {{
      transform: scale(1.08);
      background: var(--accent-hover);
    }}
    .video-badge-prod {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: rgba(239, 68, 68, 0.2);
      border: 1px solid #ef4444;
      color: #fca5a5;
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .video-frame-title {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .video-frame-sub {{
      font-size: 0.9rem;
      color: #94a3b8;
    }}
    .video-card-body {{
      padding: 24px;
      background: var(--bg-card);
    }}
    .video-tutor-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-light);
      margin-bottom: 16px;
    }}
    .tutor-info {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .tutor-avatar {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--accent-light);
      color: var(--accent);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      border: 2px solid var(--accent);
    }}
    .video-chapters-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 10px;
      margin-top: 12px;
    }}
    .video-chapter-item {{
      background: var(--bg-page);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 8px 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
    }}
    .chapter-time {{
      font-family: monospace;
      font-weight: 700;
      color: var(--accent);
      background: var(--accent-light);
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .chapter-title {{
      color: var(--text-primary);
      font-weight: 500;
    }}

    /* KEY RULES */
    .mfs-rule-card {{
      display: flex;
      gap: 16px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-left: 4px solid var(--accent);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      margin-bottom: 14px;
      box-shadow: var(--shadow-sm);
    }}
    .rule-icon {{
      font-size: 1.4rem;
      color: var(--accent);
      padding-top: 2px;
    }}
    .rule-content h4 {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--navy-dark);
      margin-bottom: 6px;
    }}
    .rule-content p {{
      font-size: 0.92rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin: 0;
    }}

    /* WORKED EXAMPLES */
    .worked-model-box {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .worked-model-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}
    .model-badge {{
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
      background: var(--accent-light);
      padding: 4px 10px;
      border-radius: var(--radius-full);
      border: 1px solid var(--accent-border);
    }}
    .exam-level-pill {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 600;
    }}
    .worked-question-stem {{
      font-size: 1.02rem;
      color: var(--text-primary);
      line-height: 1.6;
      background: var(--bg-page);
      padding: 14px 18px;
      border-radius: var(--radius-md);
      border-left: 3px solid var(--accent);
      margin-bottom: 18px;
    }}
    .steps-container {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 18px;
    }}
    .step-item {{
      display: flex;
      gap: 14px;
      padding: 10px 14px;
      border-radius: var(--radius-md);
      background: #faf8f2;
      border: 1px solid var(--border-light);
    }}
    .step-badge {{
      background: var(--navy);
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 2px 8px;
      height: fit-content;
      border-radius: 4px;
      margin-top: 2px;
    }}
    .step-body {{
      flex: 1;
    }}
    .step-math {{
      font-family: 'Courier New', monospace;
      font-size: 1rem;
      font-weight: 700;
      color: var(--navy-dark);
      background: #ffffff;
      padding: 6px 12px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
      margin: 6px 0;
      display: inline-block;
    }}
    .step-mark-tag {{
      font-size: 0.78rem;
      color: #059669;
      font-weight: 700;
    }}
    .worked-final-answer {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
      padding: 12px 18px;
      border-radius: var(--radius-md);
      font-size: 0.98rem;
    }}

    /* EXAMINER TRAPS */
    .trap-card {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-radius: var(--radius-md);
      padding: 18px 20px;
      margin-bottom: 14px;
    }}
    .trap-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: #b45309;
      font-weight: 800;
      font-size: 0.98rem;
      margin-bottom: 8px;
    }}
    .trap-card p {{
      color: #78350f;
      font-size: 0.9rem;
      line-height: 1.55;
      margin-bottom: 8px;
    }}
    .trap-how-to-fix {{
      background: #ffffff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.88rem;
      color: #1e293b;
      border: 1px solid #fed7aa;
    }}

    /* INTERACTIVE PRACTICE QUESTIONS */
    .interactive-q-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .q-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .q-number {{
      font-weight: 800;
      color: var(--navy-dark);
      font-size: 1.05rem;
    }}
    .q-marks {{
      font-size: 0.8rem;
      font-weight: 700;
      background: var(--accent-light);
      color: var(--accent);
      padding: 3px 8px;
      border-radius: var(--radius-full);
      border: 1px solid var(--accent-border);
    }}
    .q-text {{
      font-size: 1rem;
      color: var(--text-primary);
      line-height: 1.6;
      margin-bottom: 16px;
    }}
    .q-workspace {{
      margin-bottom: 16px;
    }}
    .q-workspace label {{
      display: block;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-secondary);
      margin-bottom: 6px;
    }}
    .q-scratchpad {{
      width: 100%;
      min-height: 90px;
      border: 1px solid var(--border);
      background: var(--bg-page);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      font-family: inherit;
      font-size: 0.9rem;
      color: var(--text-primary);
      resize: vertical;
      box-sizing: border-box;
    }}
    .q-actions {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .btn-reveal-solution {{
      background: var(--navy);
      color: #ffffff;
      border: none;
      padding: 9px 16px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .btn-reveal-solution:hover {{
      background: var(--navy-soft);
    }}
    .video-sol-pill {{
      font-size: 0.82rem;
      color: #64748b;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .revealed-solution {{
      margin-top: 18px;
      animation: fadeIn 0.3s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .sol-inner {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: var(--radius-md);
      padding: 18px 20px;
    }}
    .sol-header {{
      font-weight: 800;
      color: #166534;
      font-size: 0.95rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .sol-steps {{
      font-size: 0.92rem;
      color: #14532d;
      line-height: 1.6;
      margin-bottom: 12px;
    }}
    .sol-final {{
      background: #ffffff;
      padding: 8px 14px;
      border-radius: 6px;
      border: 1px solid #86efac;
      font-size: 0.95rem;
      color: #065f46;
      margin-bottom: 12px;
    }}
    .sol-tutor-tip {{
      font-size: 0.85rem;
      color: #166534;
      background: rgba(22, 101, 52, 0.08);
      padding: 8px 12px;
      border-radius: 6px;
    }}

    /* SIDEBAR RESOURCES CARD */
    .sidebar-sticky {{
      position: sticky;
      top: 24px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .sidebar-resource-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      box-shadow: var(--shadow-md);
    }}
    .sidebar-h3 {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--navy-dark);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid var(--border-light);
      padding-bottom: 10px;
    }}
    .worksheet-download-tile {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 14px;
      background: var(--bg-page);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin-bottom: 12px;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s ease;
    }}
    .worksheet-download-tile:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }}
    .tile-icon {{
      width: 44px;
      height: 44px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      flex-shrink: 0;
    }}
    .icon-worksheet {{
      background: #eff6ff;
      color: var(--accent);
    }}
    .icon-answers {{
      background: #ecfdf5;
      color: #059669;
    }}
    .icon-video {{
      background: #fef2f2;
      color: #ef4444;
    }}
    .tile-meta strong {{
      display: block;
      font-size: 0.92rem;
      color: var(--navy-dark);
    }}
    .tile-meta span {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .sidebar-promo-box {{
      background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy) 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 24px;
      text-align: center;
    }}
    .sidebar-promo-box h4 {{
      font-size: 1.15rem;
      font-weight: 800;
      margin-bottom: 8px;
      color: #ffffff;
    }}
    .sidebar-promo-box p {{
      font-size: 0.85rem;
      color: #cbd5e1;
      margin-bottom: 16px;
      line-height: 1.5;
    }}
    .btn-promo-cta {{
      display: block;
      background: var(--accent);
      color: #ffffff;
      padding: 10px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.88rem;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .btn-promo-cta:hover {{
      background: var(--accent-hover);
    }}
  </style>
</head>
<body>

  <!-- TOP TRUST BAR -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel & City & Guilds Aligned</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <!-- DYSLEXIA BACKGROUND TINT PICKER -->
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint or remove tint">
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Cream Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.62rem; opacity:0.75; margin-left:2px;"></i>
            </button>
            <div id="tintMenu" class="tint-picker-menu">
              <div class="tint-picker-title"><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</div>
              <button type="button" class="tint-option-btn active" data-tint="cream" onclick="setSiteTint('cream', event)">
                <span class="swatch swatch-cream"></span>
                <span class="tint-name">Cream <small class="tint-badge-def">Default</small></span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="peach" onclick="setSiteTint('peach', event)">
                <span class="swatch swatch-peach"></span>
                <span class="tint-name">Soft Peach</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="cool" onclick="setSiteTint('cool', event)">
                <span class="swatch swatch-cool"></span>
                <span class="tint-name">Cool Mist</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <button type="button" class="tint-option-btn" data-tint="sage" onclick="setSiteTint('sage', event)">
                <span class="swatch swatch-sage"></span>
                <span class="tint-name">Soft Sage</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
              <div class="tint-divider"></div>
              <button type="button" class="tint-option-btn" data-tint="none" onclick="setSiteTint('none', event)">
                <span class="swatch swatch-none"></span>
                <span class="tint-name">No Tint (White)</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
            </div>
          </div>
          <button type="button" class="btn-dyslexia-toggle" onclick="openGlobalSearch()" title="Search topics (Ctrl+K)">
            <i class="fa-solid fa-magnifying-glass"></i> Search
          </button>
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
          <button id="themeToggle" class="mfs-theme-pill" onclick="toggleTheme()" title="Switch Palette: Sapphire vs Emerald">
            <i class="fa-solid fa-palette"></i> <span id="themeLabel">Sapphire</span>
          </button>
        </div>
        <a href="tel:020XXXXXXXX" class="top-contact-link"><i class="fa-solid fa-phone"></i> <strong>020 XXXX XXXX</strong></a>
        <a href="https://wa.me/447564525425" target="_blank" rel="noopener" class="top-contact-link"><i class="fa-brands fa-whatsapp"></i> <strong>+44 (0)7564 525425</strong></a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <!-- MAIN NAVIGATION -->
  <header class="mfs-navbar">
    <div class="revision-page-wrapper mfs-navbar-inner">
      <a href="index.html" class="mfs-brand">
        <div class="mfs-brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
        <div class="mfs-brand-text">
          <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
          <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
        </div>
      </a>

      <nav class="mfs-nav-wrapper">
        <ul class="mfs-nav-menu">
          <li class="mfs-nav-item">
            <a href="functional-skills-maths-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-calculator" style="color:#0284c7; margin-right:5px;"></i> Maths <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
              <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
              <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folder</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="functional-skills-english-level-2.html" class="mfs-nav-link"><i class="fa-solid fa-pen-nib" style="color:#0284c7; margin-right:5px;"></i> English <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
              <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html#english" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Test</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="digital-functional-skills.html" class="mfs-nav-link"><i class="fa-solid fa-laptop-code" style="color:#0284c7; margin-right:5px;"></i> Digital Skills <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Mock Simulator</a>
              <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Data Files</a>
            </div>
          </li>
          <li class="mfs-nav-item">
            <a href="pass-mark-calculator.html" class="mfs-nav-link"><i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item"><i class="fa-solid fa-laptop-code" style="color:#2563eb; font-size:0.85rem; margin-right:6px;"></i> Pearson Exam Simulator</a>
              <a href="bksb-remediation.html" class="mfs-dropdown-item"><i class="fa-solid fa-arrows-split-up-and-left" style="color:#8b5cf6; font-size:0.85rem; margin-right:6px;"></i> BKSB Remediation Bridge</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folding Tool</a>
            </div>
          </li>
          <li class="mfs-nav-item"><a href="tutors.html" class="mfs-nav-link"><i class="fa-solid fa-chalkboard-user" style="color:#0284c7; margin-right:5px;"></i> Tutor Hub</a></li>
          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link"><i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i></a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="functional-skills-past-papers.html" class="mfs-dropdown-item">All Past Papers Hub</a>
              <a href="edexcel-functional-skills-maths-level-2-past-papers.html" class="mfs-dropdown-item">Pearson Edexcel Papers</a>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Grade Boundaries Calculator</a>
            </div>
          </li>
          <li class="mfs-nav-item"><a href="revision-cards.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-layer-group" style="color:#f59e0b; margin-right:5px;"></i> Revision Cards</a></li>
          <li class="mfs-nav-item"><a href="shop.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#f59e0b; font-weight:700;"><i class="fa-solid fa-basket-shopping" style="color:#f59e0b; margin-right:5px;"></i> Shop</a></li>
        </ul>
      </nav>

      <div class="mfs-nav-actions">
        <a href="functional-skills-exam.html" class="btn-nav-exam"><i class="fa-solid fa-calendar-check"></i> Book Exam</a>
      </div>
    </div>
  </header>

  <!-- TOPIC HERO HEADER -->
  <section class="topic-hero">
    <div class="mfs-container">
      <div class="topic-breadcrumbs">
        <a href="index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i>
        <a href="revise.html">Revise Hub</a>
        <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i>
        <a href="functional-skills-maths-level-2.html">{subject}</a>
        <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i>
        <span>{title}</span>
      </div>

      <div class="topic-meta-row">
        <span class="topic-pill topic-pill-level"><i class="fa-solid fa-layer-group"></i> {level_str}</span>
        <span class="topic-pill topic-pill-spec"><i class="fa-solid fa-clipboard-check"></i> {spec_codes}</span>
      </div>

      <h1 class="topic-hero-title">{title}</h1>
      <p class="topic-hero-desc">{intro_summary}</p>

      <div class="topic-quick-actions">
        <a href="#video-masterclass" class="btn-topic-action btn-topic-action-primary">
          <i class="fa-solid fa-play"></i> Watch Video Masterclass
        </a>
        <a href="worksheets/{slug}-worksheet.html" target="_blank" class="btn-topic-action btn-topic-action-worksheet">
          <i class="fa-regular fa-file-pdf"></i> Printable Worksheet (PDF)
        </a>
        <a href="worksheets/{slug}-answers.html" target="_blank" class="btn-topic-action btn-topic-action-answers">
          <i class="fa-solid fa-circle-check"></i> Answer Key & Mark Scheme
        </a>
        <a href="#practice-questions" class="btn-topic-action btn-topic-action-worksheet">
          <i class="fa-solid fa-laptop-code"></i> Interactive Practice
        </a>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT CONTAINER -->
  <main class="mfs-container">
    <div class="topic-layout">
      <!-- LEFT COLUMN: PEDAGOGY, VIDEO, MODELS & PRACTICE -->
      <div class="topic-main-col">

        <!-- 1. VIDEO MASTERCLASS CARD -->
        <div id="video-masterclass" class="video-masterclass-card">
          <div class="video-placeholder-frame">
            <div class="video-badge-prod">
              <i class="fa-solid fa-film"></i> VIDEO MASTERCLASS • COMING SOON
            </div>
            <div class="video-play-btn" title="Click to watch trailer or subscribe">
              <i class="fa-solid fa-play" style="margin-left: 4px;"></i>
            </div>
            <div class="video-frame-title">{title} — Full Step-by-Step Masterclass</div>
            <div class="video-frame-sub">Pearson Edexcel {level_str} Exam Preparation • Runtime: ~{video_duration}</div>
          </div>
          <div class="video-card-body">
            <div class="video-tutor-row">
              <div class="tutor-info">
                <div class="tutor-avatar"><i class="fa-solid fa-chalkboard-user"></i></div>
                <div>
                  <div style="font-weight:700; color:var(--navy-dark);">Master Functional Skills • Specialist Tutor Team</div>
                  <div style="font-size:0.82rem; color:var(--text-muted);">Specialist Functional Skills Maths & English Lecturer</div>
                </div>
              </div>
              <div>
                <a href="https://www.youtube.com/@MasterFunctionalSkills?sub_confirmation=1" target="_blank" rel="noopener" class="btn-topic-action btn-topic-action-primary" style="padding:6px 14px; font-size:0.82rem;">
                  <i class="fa-brands fa-youtube"></i> Subscribe on YouTube
                </a>
              </div>
            </div>
            <div style="font-size:0.88rem; font-weight:700; color:var(--navy-dark); margin-bottom:6px;">
              <i class="fa-solid fa-list-ol"></i> Video Chapters & Timestamps:
            </div>
            <div class="video-chapters-grid">
              {chapters_html}
            </div>
          </div>
        </div>

        <!-- 2. CORE METHOD RULES -->
        <section class="topic-section">
          <h2 class="section-h2"><i class="fa-solid fa-compass-drafting" style="color:var(--accent);"></i> Golden Rules & Core Concepts</h2>
          <div class="rules-container">
            {rules_html}
          </div>
        </section>

        <!-- 3. WORKED EXAM MODELS -->
        <section class="topic-section" style="margin-top:36px;">
          <h2 class="section-h2"><i class="fa-solid fa-pen-ruler" style="color:var(--accent);"></i> Pearson Edexcel Step-by-Step Worked Models</h2>
          <div class="models-container">
            {worked_html}
          </div>
        </section>

        <!-- 4. EXAMINER TRAPS & PITFALLS -->
        <section class="topic-section" style="margin-top:36px;">
          <h2 class="section-h2"><i class="fa-solid fa-triangle-exclamation" style="color:#f59e0b;"></i> Common Examiner Traps (Where Students Lose Marks)</h2>
          <div class="traps-container">
            {traps_html}
          </div>
        </section>

        <!-- 5. INTERACTIVE PRACTICE MODULE -->
        <section id="practice-questions" class="topic-section" style="margin-top:36px;">
          <h2 class="section-h2"><i class="fa-solid fa-graduation-cap" style="color:var(--accent);"></i> Interactive Practice Questions & Step-by-Step Mark Schemes</h2>
          <p style="font-size:0.92rem; color:var(--text-secondary); margin-bottom:20px;">
            Attempt each question in your scratchpad below, then reveal the Tutor method breakdown to verify your M1 (Method) and A1 (Accuracy) marks.
          </p>
          <div class="questions-container">
            {practice_html}
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: SIDEBAR RESOURCES -->
      <aside class="topic-sidebar">
        <div class="sidebar-sticky">

          <!-- Worksheet Download Card -->
          <div class="sidebar-resource-card">
            <h3 class="sidebar-h3"><i class="fa-solid fa-file-arrow-down" style="color:var(--accent);"></i> Printable Resources</h3>
            
            <a href="worksheets/{slug}-worksheet.html" target="_blank" class="worksheet-download-tile">
              <div class="tile-icon icon-worksheet"><i class="fa-regular fa-file-pdf"></i></div>
              <div class="tile-meta">
                <strong>Topic Worksheet</strong>
                <span>Printable A4 Exam Questions</span>
              </div>
            </a>

            <a href="worksheets/{slug}-answers.html" target="_blank" class="worksheet-download-tile">
              <div class="tile-icon icon-answers"><i class="fa-solid fa-check-double"></i></div>
              <div class="tile-meta">
                <strong>Worked Answer Key</strong>
                <span>Full Examiner Mark Scheme</span>
              </div>
            </a>

            <a href="#video-masterclass" class="worksheet-download-tile">
              <div class="tile-icon icon-video"><i class="fa-brands fa-youtube"></i></div>
              <div class="tile-meta">
                <strong>Video Solutions</strong>
                <span>Tutor Walkthroughs</span>
              </div>
            </a>
          </div>

          <!-- Diagnostic Check Promo -->
          <div class="sidebar-promo-box">
            <i class="fa-solid fa-chart-pie" style="font-size:2rem; color:#93c5fd; margin-bottom:12px;"></i>
            <h4>Need to Check Your Level?</h4>
            <p>Take our free 10-minute diagnostic check to identify your exact strengths and knowledge gaps before booking an exam.</p>
            <a href="diagnostic-test.html" class="btn-promo-cta">Start Free Diagnostic Check →</a>
          </div>

          <!-- 1-to-1 Specialist Tuition Card -->
          <div class="sidebar-resource-card" style="border-left:4px solid #10b981;">
            <div style="font-size:0.8rem; font-weight:800; color:#059669; text-transform:uppercase; margin-bottom:6px;">
              <i class="fa-solid fa-user-tie"></i> 1-to-1 Specialist Tuition
            </div>
            <h4 style="font-size:1.05rem; font-weight:800; color:var(--navy-dark); margin-bottom:8px;">Struggling with {title}?</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.5; margin-bottom:14px;">
              Book an individual online tuition session with an expert specialist tutor. Guaranteed dyslexia-friendly methods and high pass rate.
            </p>
            <a href="https://wa.me/447564525425?text=Hello,%20I%20would%20like%20to%20enquire%20about%201-to-1%20tuition%20for%20Functional%20Skills%20{title}" target="_blank" rel="noopener" class="btn-topic-action btn-topic-action-primary" style="width:100%; justify-content:center; box-sizing:border-box;">
              <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
            </a>
          </div>

        </div>
      </aside>
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="mfs-footer">
    <div class="mfs-container">
      <div class="footer-grid">
        <div class="footer-col footer-col-brand">
          <div class="footer-brand">MASTER<span>FUNCTIONALSKILLS</span></div>
          <p class="footer-tagline">The UK's leading dedicated Functional Skills training and examination service. Delivering regulated qualifications across London, Oxford, and nationwide.</p>
          <div style="font-size:0.88rem; color:#94a3b8; margin-top:8px;">
            <i class="fa-solid fa-graduation-cap"></i> Senior Academic Lead & Specialist Tutor Team
          </div>
        </div>
        <div class="footer-col">
          <h4>Maths Revision</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-maths-level-2.html">Maths Level 2 Directory</a></li>
            <li><a href="functional-skills-maths-level-1.html">Maths Level 1 Directory</a></li>
            <li><a href="entry-level-3-maths.html">Entry Level 3 Maths</a></li>
            <li><a href="functional-skills-past-papers.html">Maths Past Papers</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>English & Digital</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-english-level-2.html">English Level 2 Directory</a></li>
            <li><a href="functional-skills-english-level-1.html">English Level 1 Directory</a></li>
            <li><a href="digital-functional-skills.html">Digital Functional Skills Hub</a></li>
            <li><a href="diagnostic-test.html">Diagnostic Skill Assessment</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Student Support</h4>
          <ul class="footer-links">
            <li><a href="tel:020XXXXXXXX">020 XXXX XXXX</a></li>
            <li><a href="contact-us.html">Contact Tutor Team</a></li>
            <li><a href="bksb-remediation.html">BKSB / OneAdvanced Bridge</a></li>
            <li><a href="pass-functional-skills-reviews.html">Learner Reviews</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; 2026 Master Functional Skills. All rights reserved. Registered in England & Wales. Ofqual Regulated Qualification Standards.</div>
      </div>
    </div>
  </footer>

  <!-- DYSLEXIA TINT ENGINE & INTERACTIVE SCRIPTS -->
  <script src="assets/js/mfs-tint.js"></script>
  <script>
    function toggleSolution(solId) {{
      const el = document.getElementById(solId);
      if (el) {{
        el.style.display = (el.style.display === 'none' || el.style.display === '') ? 'block' : 'none';
      }}
    }}
    function toggleDyslexiaMode() {{
      const isDys = document.body.classList.toggle('dyslexia-mode');
      localStorage.setItem('mfs_dyslexia', isDys ? '1' : '0');
      const btn = document.getElementById('dyslexiaToggle');
      if (btn) btn.classList.toggle('active', isDys);
    }}
    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'sapphire';
      const next = current === 'emerald' ? 'sapphire' : 'emerald';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('mfs_theme', next);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = next === 'emerald' ? 'Emerald' : 'Sapphire';
    }}
    (function() {{
      if (localStorage.getItem('mfs_dyslexia') === '1') {{
        document.body.classList.add('dyslexia-mode');
        const btn = document.getElementById('dyslexiaToggle');
        if (btn) btn.classList.add('active', true);
      }}
      const th = localStorage.getItem('mfs_theme') || 'sapphire';
      document.documentElement.setAttribute('data-theme', th);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = th === 'emerald' ? 'Emerald' : 'Sapphire';
    }})();
  </script>
</body>
</html>"""
    return html

def build_printable_worksheet(topic_data):
    title = topic_data['title']
    slug = topic_data['slug']
    levels = topic_data.get('levels', ['Level 1', 'Level 2'])
    level_str = " & ".join(levels)
    questions = topic_data.get('worksheet_questions', topic_data.get('practice_questions', []))
    total_marks = sum(q.get('marks', 3) for q in questions)
    
    questions_html = ""
    for idx, q in enumerate(questions, 1):
        questions_html += f"""
        <div class="worksheet-q-item">
          <div class="q-bar">
            <span class="q-num">Question {idx}</span>
            <span class="q-mark-box">[{q.get('marks', 3)} Marks]</span>
          </div>
          <div class="q-stem">
            {q['question']}
          </div>
          <div class="q-working-lines">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
          </div>
          <div class="q-answer-box">
            Answer: ____________________________________
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <title>Master Functional Skills — {title} Printable Worksheet ({level_str})</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 15mm 15mm 15mm 15mm;
    }}
    body {{
      font-family: 'Segoe UI', Arial, sans-serif;
      color: #1e293b;
      margin: 0;
      padding: 0;
      background: #faf8f2;
      font-size: 11pt;
      line-height: 1.5;
    }}
    .print-controls {{
      background: #102345;
      color: #ffffff;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .btn-print {{
      background: #2563eb;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 10pt;
      cursor: pointer;
    }}
    .btn-back {{
      color: #93c5fd;
      text-decoration: none;
      font-size: 10pt;
    }}
    @media print {{
      .print-controls {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .worksheet-q-item {{
        page-break-inside: avoid;
      }}
    }}
    .sheet-wrapper {{
      max-width: 800px;
      margin: 20px auto;
      background: #ffffff;
      padding: 30px 36px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.06);
      border: 1px solid #e2e8f0;
      border-radius: 8px;
    }}
    .sheet-header {{
      border-bottom: 2px solid #102345;
      padding-bottom: 14px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .sheet-brand-title {{
      font-size: 16pt;
      font-weight: 800;
      color: #102345;
      letter-spacing: -0.5px;
    }}
    .sheet-brand-title span {{
      color: #2563eb;
    }}
    .sheet-sub {{
      font-size: 9.5pt;
      color: #64748b;
      margin-top: 2px;
    }}
    .sheet-topic-badge {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1d4ed8;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 10pt;
      text-align: right;
    }}
    .student-info-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 12px;
      background: #faf8f2;
      border: 1px solid #e2e8f0;
      padding: 12px 16px;
      border-radius: 6px;
      margin-bottom: 24px;
      font-size: 10pt;
    }}
    .info-line {{
      border-bottom: 1px dashed #94a3b8;
      display: inline-block;
      width: 60%;
      height: 14px;
      margin-left: 6px;
    }}
    .instructions-box {{
      background: #f8fafc;
      border-left: 3px solid #2563eb;
      padding: 10px 14px;
      font-size: 9.5pt;
      color: #334155;
      margin-bottom: 24px;
    }}
    .instructions-box ul {{
      margin: 4px 0 0;
      padding-left: 18px;
    }}
    .worksheet-q-item {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 16px;
      margin-bottom: 22px;
      background: #ffffff;
    }}
    .q-bar {{
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
      margin-bottom: 10px;
    }}
    .q-num {{
      font-weight: 800;
      color: #102345;
    }}
    .q-mark-box {{
      font-weight: 700;
      color: #2563eb;
    }}
    .q-stem {{
      font-size: 10.5pt;
      margin-bottom: 14px;
      color: #0f172a;
    }}
    .q-working-lines {{
      margin: 12px 0;
    }}
    .q-working-lines .line {{
      border-bottom: 1px dashed #e2e8f0;
      height: 22px;
    }}
    .q-answer-box {{
      text-align: right;
      font-weight: 700;
      color: #0f172a;
      margin-top: 12px;
      padding-top: 8px;
      border-top: 1px solid #f1f5f9;
    }}
    .sheet-footer {{
      margin-top: 30px;
      border-top: 1px solid #e2e8f0;
      padding-top: 12px;
      display: flex;
      justify-content: space-between;
      font-size: 8.5pt;
      color: #94a3b8;
    }}
  </style>
</head>
<body>

  <div class="print-controls">
    <a href="../functional-skills-{slug}.html" class="btn-back">← Back to {title} Revision Guide</a>
    <div>
      <span style="margin-right:16px; font-size:9.5pt; color:#cbd5e1;">Master Functional Skills Original IP</span>
      <button type="button" class="btn-print" onclick="window.print()">🖨️ Print / Save to PDF</button>
    </div>
  </div>

  <div class="sheet-wrapper">
    <div class="sheet-header">
      <div>
        <div class="sheet-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
        <div class="sheet-sub">Ofqual Regulated Standards • Pearson Edexcel Curriculum</div>
      </div>
      <div class="sheet-topic-badge">
        <div>{title}</div>
        <small>{level_str} Practice Worksheet</small>
      </div>
    </div>

    <div class="student-info-grid">
      <div><strong>Learner:</strong> <span class="info-line"></span></div>
      <div><strong>Date:</strong> <span class="info-line"></span></div>
      <div><strong>Score:</strong> _____ / {total_marks}</div>
    </div>

    <div class="instructions-box">
      <strong>Instructions to Learners:</strong>
      <ul>
        <li>Show your full working out in the spaces provided to secure Method Marks (M1).</li>
        <li>Check your units (e.g. £, cm, kg) before writing your final answer.</li>
        <li>When completed, check against the <strong>Master Functional Skills Answer Key & Mark Scheme</strong>.</li>
      </ul>
    </div>

    {questions_html}

    <div class="sheet-footer">
      <div>&copy; 2026 Master Functional Skills — All Rights Reserved.</div>
      <div>Tutor Video Walkthroughs Available Online: masterfunctionalskills.co.uk</div>
    </div>
  </div>

</body>
</html>"""
    return html

def build_printable_answers(topic_data):
    title = topic_data['title']
    slug = topic_data['slug']
    levels = topic_data.get('levels', ['Level 1', 'Level 2'])
    level_str = " & ".join(levels)
    questions = topic_data.get('worksheet_questions', topic_data.get('practice_questions', []))
    
    answers_html = ""
    for idx, q in enumerate(questions, 1):
        answers_html += f"""
        <div class="answer-item">
          <div class="ans-bar">
            <span class="ans-num">Question {idx} Model Solution</span>
            <span class="ans-marks">[{q.get('marks', 3)} Marks Total]</span>
          </div>
          <div class="ans-q-stem">
            <em>Question: {q['question']}</em>
          </div>
          <div class="ans-mark-breakdown">
            <strong>Step-by-Step Marking Criteria:</strong>
            <div style="margin-top:6px; font-size:10pt; line-height:1.6;">
              {q['solution_steps']}
            </div>
          </div>
          <div class="ans-final-line">
            <strong>Award A1 for Final Answer:</strong> <span class="highlight-ans">{q['correct_answer']}</span>
          </div>
          <div class="ans-tutor-note">
            <strong>Tutor Examiner Note:</strong> {q['tutor_tip']}
          </div>
          <div class="ans-video-ref">
            🎥 Video Solution Walkthrough: <em>youtube.com/@MasterFunctionalSkills — Chapter: {title} Q{idx}</em>
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <title>Master Functional Skills — {title} Answer Key & Mark Scheme ({level_str})</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 15mm 15mm 15mm 15mm;
    }}
    body {{
      font-family: 'Segoe UI', Arial, sans-serif;
      color: #1e293b;
      margin: 0;
      padding: 0;
      background: #faf8f2;
      font-size: 11pt;
      line-height: 1.5;
    }}
    .print-controls {{
      background: #064e3b;
      color: #ffffff;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .btn-print {{
      background: #10b981;
      color: #ffffff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 10pt;
      cursor: pointer;
    }}
    .btn-back {{
      color: #a7f3d0;
      text-decoration: none;
      font-size: 10pt;
    }}
    @media print {{
      .print-controls {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
      }}
      .answer-item {{
        page-break-inside: avoid;
      }}
    }}
    .sheet-wrapper {{
      max-width: 800px;
      margin: 20px auto;
      background: #ffffff;
      padding: 30px 36px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.06);
      border: 1px solid #e2e8f0;
      border-radius: 8px;
    }}
    .sheet-header {{
      border-bottom: 2px solid #064e3b;
      padding-bottom: 14px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .sheet-brand-title {{
      font-size: 16pt;
      font-weight: 800;
      color: #064e3b;
      letter-spacing: -0.5px;
    }}
    .sheet-brand-title span {{
      color: #10b981;
    }}
    .sheet-sub {{
      font-size: 9.5pt;
      color: #64748b;
      margin-top: 2px;
    }}
    .sheet-topic-badge {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      color: #065f46;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 10pt;
      text-align: right;
    }}
    .answer-item {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 16px;
      margin-bottom: 22px;
      background: #ffffff;
    }}
    .ans-bar {{
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}
    .ans-num {{
      font-weight: 800;
      color: #064e3b;
    }}
    .ans-marks {{
      font-weight: 700;
      color: #059669;
    }}
    .ans-q-stem {{
      font-size: 9.5pt;
      color: #475569;
      margin-bottom: 10px;
    }}
    .ans-mark-breakdown {{
      background: #f8fafc;
      border-left: 3px solid #10b981;
      padding: 10px 14px;
      margin-bottom: 12px;
    }}
    .ans-final-line {{
      background: #ecfdf5;
      padding: 8px 12px;
      border-radius: 4px;
      border: 1px solid #a7f3d0;
      font-size: 10.5pt;
      color: #065f46;
      margin-bottom: 10px;
    }}
    .highlight-ans {{
      font-weight: 800;
      color: #047857;
      text-decoration: underline;
    }}
    .ans-tutor-note {{
      font-size: 9.5pt;
      color: #334155;
      background: #fffbeb;
      border: 1px solid #fef3c7;
      padding: 8px 12px;
      border-radius: 4px;
      margin-bottom: 8px;
    }}
    .ans-video-ref {{
      font-size: 8.5pt;
      color: #64748b;
      margin-top: 6px;
    }}
    .sheet-footer {{
      margin-top: 30px;
      border-top: 1px solid #e2e8f0;
      padding-top: 12px;
      display: flex;
      justify-content: space-between;
      font-size: 8.5pt;
      color: #94a3b8;
    }}
  </style>
</head>
<body>

  <div class="print-controls">
    <a href="../functional-skills-{slug}.html" class="btn-back">← Back to {title} Revision Guide</a>
    <div>
      <span style="margin-right:16px; font-size:9.5pt; color:#a7f3d0;">Official Tutor Examiner Mark Scheme</span>
      <button type="button" class="btn-print" onclick="window.print()">🖨️ Print / Save to PDF</button>
    </div>
  </div>

  <div class="sheet-wrapper">
    <div class="sheet-header">
      <div>
        <div class="sheet-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
        <div class="sheet-sub">Official Tutor Worked Answer Key & Method Mark Scheme</div>
      </div>
      <div class="sheet-topic-badge">
        <div>{title}</div>
        <small>{level_str} Worked Solutions</small>
      </div>
    </div>

    {answers_html}

    <div class="sheet-footer">
      <div>&copy; 2026 Master Functional Skills — All Rights Reserved.</div>
      <div>Official Edexcel & City & Guilds Marking Criteria (M1 / A1 / B1)</div>
    </div>
  </div>

</body>
</html>"""
    return html
