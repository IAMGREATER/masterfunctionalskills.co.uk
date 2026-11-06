# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Digital Skills Dedicated Page Templates & Hub Engine
Author: Abdul (MFS Pedagogical Systems)
Strictly adheres to:
- Official level names: Entry 3 (never "Entry Level 3") and Level 1
- High-engagement Hub & Spoke dual-view landing page architecture
- MFS brand identity, dyslexia readability & visual hierarchy
"""

def render_revision_page(data, prev_topic, next_topic, level_code, level_title):
    """
    Renders an individual dedicated Digital Skills revision page.
    level_code: 'entry-3' or 'level-1'
    level_title: 'Entry 3' or 'Level 1'
    """
    slug = data['slug']
    spec_code = data['code']
    title = data['title']
    skill_area = data['skill_area']
    time_est = data.get('time', '15 Mins')
    lead = data['lead']
    objectives = data.get('objectives', [])
    youtube_id = data.get('youtube_id', 'https://www.youtube.com/@MasterFunctionalSkills')
    youtube_title = data.get('youtube_title', f'{level_title} Digital Skills - {title}')
    steps = data.get('steps', [])
    exam_model = data.get('exam_model', {})
    drills = data.get('drills', [])
    practice = data.get('practice', {})
    revision_links = data.get('revision_links', [])

    # Breadcrumb pill style
    level_badge_class = 'e3' if level_code == 'entry-3' else 'l1'

    # Objectives HTML
    objectives_html = "".join([
        f'<span class="dfs-obj-tag"><i class="fa-solid fa-check"></i> {obj}</span>'
        for obj in objectives
    ])

    # Steps HTML
    steps_html = ""
    for idx, s in enumerate(steps, 1):
        ui_box_html = ""
        if s.get('ui_sim'):
            ui = s['ui_sim']
            ui_box_html = f'''
            <div class="dfs-ui-sim">
              <div class="dfs-ui-sim-bar">
                <div class="dfs-ui-sim-dots"><span></span><span></span><span></span></div>
                <div>{ui.get("title", "Software Interface")}</div>
                <div><i class="fa-solid fa-desktop"></i></div>
              </div>
              <div class="dfs-ui-sim-content">
                {ui.get("content", "")}
              </div>
            </div>
            '''
        
        shortcut_html = ""
        if s.get('shortcuts'):
            sc_items = " &bull; ".join([f'<strong>{sc["label"]}:</strong> <kbd class="dfs-kbd">{sc["key"]}</kbd>' for sc in s['shortcuts']])
            shortcut_html = f'<div style="margin-top:10px; font-size:0.88rem; color:#475569;"><i class="fa-regular fa-keyboard" style="color:#0284c7; margin-right:4px;"></i> {sc_items}</div>'

        callout_html = ""
        if s.get('callout'):
            c = s['callout']
            ctype = c.get('type', 'tutor')
            cicon = 'fa-lightbulb' if ctype == 'tutor' else ('fa-triangle-exclamation' if ctype == 'warning' else 'fa-user-nurse')
            callout_html = f'''
            <div class="dfs-callout dfs-callout-{ctype}">
              <i class="fa-solid {cicon}"></i>
              <div><strong>{c.get("title", "Key Tip")}:</strong> {c.get("text", "")}</div>
            </div>
            '''

        steps_html += f'''
        <div class="dfs-step-card">
          <div class="dfs-step-header">
            <div class="dfs-step-num">{idx}</div>
            <div class="dfs-step-title">{s.get("title", f"Step {idx}")}</div>
          </div>
          <div class="dfs-step-body">
            {s.get("body", "")}
            {ui_box_html}
            {shortcut_html}
            {callout_html}
          </div>
        </div>
        '''

    # Exam Model HTML
    model_steps_html = ""
    for m_idx, m_step in enumerate(exam_model.get('steps', []), 1):
        mark_tag = f'<span class="dfs-mark-tag">{m_step.get("mark", "[B1]")}</span>' if m_step.get("mark") else ""
        model_steps_html += f'''
        <div class="dfs-model-step-card">
          <div class="dfs-model-step-title">
            <span>Step {m_idx}: {m_step.get("action", "")}</span>
            {mark_tag}
          </div>
          <div class="dfs-model-solution-text">{m_step.get("solution", "")}</div>
          <div class="dfs-tutor-rationale">
            <i class="fa-solid fa-circle-check"></i>
            <div><strong>Tutor Marking Rationale:</strong> {m_step.get("rationale", "")}</div>
          </div>
        </div>
        '''

    exam_model_html = f'''
    <div class="dfs-exam-model">
      <div class="dfs-model-stem">
        <strong><i class="fa-solid fa-clipboard-question"></i> Exam Scenario Prompt:</strong> {exam_model.get("scenario", "")}
      </div>
      {model_steps_html}
      <div class="dfs-callout dfs-callout-tutor" style="margin-top:16px;">
        <i class="fa-solid fa-award"></i>
        <div><strong>Tutor Abdul's Exam Golden Rule:</strong> {exam_model.get("tutor_rule", "Always check your work carefully before moving to the next section.")}</div>
      </div>
    </div>
    '''

    # Fluency Drills HTML
    drills_html = ""
    for d_idx, d in enumerate(drills, 1):
        feedback_id = f"drillFeedback_{slug}_{d_idx}"
        options_html = ""
        for opt in d.get('options', []):
            is_corr = "true" if opt.get('correct') else "false"
            options_html += f'''
            <button type="button" class="dfs-drill-opt-btn" data-correct="{is_corr}" onclick="checkDrill(this, {is_corr}, '{feedback_id}')">
              <span>{opt.get("text", "")}</span>
              <i class="fa-solid fa-arrow-right" style="opacity:0.4; font-size:0.8rem;"></i>
            </button>
            '''

        drills_html += f'''
        <div class="dfs-drill-question-card">
          <div class="dfs-drill-q-title">
            <span class="dfs-drill-q-num">Drill {d_idx}</span>
            <span>{d.get("question", "")}</span>
          </div>
          <div class="dfs-drill-options">
            {options_html}
          </div>
          <div id="{feedback_id}" class="dfs-drill-feedback" data-explanation="{d.get("explanation", "")}"></div>
        </div>
        '''

    # Practice Question HTML
    marking_items_html = "".join([
        f'<li><i class="fa-solid fa-check"></i> <div><strong>{crit.get("tag", "[1 Mark]")}:</strong> {crit.get("desc", "")}</div></li>'
        for crit in practice.get('marking_scheme', [])
    ])

    practice_html = f'''
    <div class="dfs-practice-box">
      <div class="dfs-task-stem">
        <div style="font-weight:700; color:#0f172a; margin-bottom:6px;"><i class="fa-solid fa-pen-to-square" style="color:#0284c7;"></i> Onscreen Assessment Task:</div>
        <div>{practice.get("task", "")}</div>
      </div>

      <div class="dfs-scratchpad-wrap">
        <div class="dfs-scratchpad-label">
          <span><i class="fa-solid fa-keyboard"></i> Your Working &amp; Answer Scratchpad:</span>
          <span class="dfs-autosave-status"><i class="fa-solid fa-circle-check"></i> Auto-saves in browser</span>
        </div>
        <textarea class="dfs-scratchpad-area" data-storage-key="dfs_scratch_{slug}" placeholder="Type your step-by-step working, method, or draft response here...">{practice.get("scaffold_starter", "")}</textarea>
      </div>

      <button type="button" id="solBtn_{slug}" class="dfs-solution-toggle-btn" onclick="toggleSolutionDrawer('solDrawer_{slug}', 'solBtn_{slug}')">
        <i class="fa-solid fa-chevron-down"></i> View Accredited Model Solution &amp; Mark Scheme
      </button>

      <div id="solDrawer_{slug}" class="dfs-solution-drawer">
        <h4><i class="fa-solid fa-circle-check"></i> Pearson Edexcel Benchmark Solution</h4>
        <div style="font-size:0.95rem; color:#14532d; line-height:1.6; margin-bottom:14px; background:#ffffff; padding:14px; border-radius:6px; border:1px solid #bbf7d0;">
          {practice.get("model_answer", "")}
        </div>
        <div style="font-weight:700; color:#166534; font-size:0.92rem; margin-bottom:6px;">Official Marking Criteria:</div>
        <ul class="dfs-marking-criteria-list">
          {marking_items_html}
        </ul>
      </div>
    </div>
    '''

    # Revision Pills HTML
    pills_html = "".join([
        f'<a href="{link.get("href", "#")}" class="dfs-pill-link"><i class="fa-solid fa-bookmark" style="font-size:0.75rem;"></i> {link.get("label", "")}</a>'
        for link in revision_links
    ])

    # Prev / Next Navigation HTML
    prev_btn_html = f'<a href="{prev_topic["slug"]}.html" class="dfs-nav-btn"><i class="fa-solid fa-arrow-left"></i> Previous: {prev_topic["title"]}</a>' if prev_topic else f'<a href="index.html" class="dfs-nav-btn"><i class="fa-solid fa-list-check"></i> Back to {level_title} Directory</a>'
    next_btn_html = f'<a href="{next_topic["slug"]}.html" class="dfs-nav-btn primary">Next: {next_topic["title"]} <i class="fa-solid fa-arrow-right"></i></a>' if next_topic else f'<a href="index.html" class="dfs-nav-btn primary">Finish {level_title} Revision <i class="fa-solid fa-flag-checkered"></i></a>'

    # Video Embed / Player HTML
    yt_vid_id = None
    if "watch?v=" in youtube_id:
        yt_vid_id = youtube_id.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_id:
        yt_vid_id = youtube_id.split("youtu.be/")[1].split("?")[0]
    elif len(youtube_id) == 11 and not youtube_id.startswith("http"):
        yt_vid_id = youtube_id

    if yt_vid_id:
        video_embed_html = f'''
        <iframe src="https://www.youtube-nocookie.com/embed/{yt_vid_id}?rel=0" title="{youtube_title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        '''
    else:
        video_embed_html = f'''
        <div class="dfs-video-card-fallback">
          <i class="fa-brands fa-youtube play-icon"></i>
          <h3 style="font-size:1.3rem; margin-bottom:8px;">{youtube_title}</h3>
          <p style="color:#94a3b8; max-width:580px; font-size:0.92rem; margin-bottom:16px;">Watch step-by-step visual demonstration with clear instructional narration and exam mark scheme commentary.</p>
          <a href="{youtube_id}" target="_blank" rel="noopener noreferrer" class="btn-yt-direct">
            <i class="fa-brands fa-youtube"></i> Watch on Master Functional Skills YouTube
          </a>
        </div>
        '''

    # Master HTML template
    return f'''<!DOCTYPE html>
<html lang="en-GB" data-theme="maths" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{title} | {level_title} Digital Skills Revision | Master Functional Skills</title>
  <meta name="description" content="Master {title} for {level_title} Digital Functional Skills. Step-by-step explanations, authentic visual UI breakdowns, video walkthroughs, fluency drills, and Pearson Edexcel aligned mock questions.">
  <link rel="icon" type="image/svg+xml" href="../../assets/img/favicon.svg">
  <link rel="alternate icon" href="../../favicon.ico">
  <meta name="theme-color" content="#0f172a">
  
  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  
  <!-- Dedicated Digital Skills Revision Styles -->
  <link rel="stylesheet" href="../../assets/css/mfs-dfs-revision.css?v=20261106_v2">
</head>
<body data-tint="cream">

  <!-- TOP TRUST BAR & ACCESSIBILITY CONTROLS -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel &amp; City &amp; Guilds Aligned</span>
        <span class="top-trust-item"><i class="fa-solid fa-graduation-cap"></i> Specialist Functional Skills Tuition</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint">
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Cream Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.62rem; opacity:0.75; margin-left:2px;"></i>
            </button>
            <div id="tintMenu" class="tint-picker-menu">
              <div class="tint-picker-title"><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</div>
              <button type="button" class="tint-option-btn active" data-tint="cream" onclick="setSiteTint('cream', event)">
                <span class="swatch swatch-cream"></span>
                <span class="tint-name">Cream (Recommended)</span>
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
              <div class="tint-divider" style="height:1px; background:#e2e8f0; margin:6px 0;"></div>
              <button type="button" class="tint-option-btn" data-tint="none" onclick="setSiteTint('none', event)">
                <span class="swatch swatch-none"></span>
                <span class="tint-name">No Tint (White)</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
            </div>
          </div>
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
        </div>
        <a href="../../contact-us.html" class="btn-tint-toggle" style="text-decoration:none;"><i class="fa-solid fa-envelope"></i> Contact</a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <header class="mfs-navbar">
    <div class="mfs-container mfs-navbar-inner">
      <a href="../../index.html" class="mfs-brand">
        <div class="mfs-brand-icon"><i class="fa-solid fa-laptop-code"></i></div>
        <div class="mfs-brand-text">
          <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
          <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
        </div>
      </a>

      <nav class="mfs-nav-wrapper">
        <ul class="mfs-nav-menu">
          <li><a href="../../revise.html" class="mfs-nav-link"><i class="fa-solid fa-book-open-reader"></i> Revision Hub</a></li>
          <li><a href="index.html" class="mfs-nav-link active"><i class="fa-solid fa-list-check"></i> {level_title} Directory</a></li>
          <li><a href="../../digital-functional-skills-past-papers.html" class="mfs-nav-link"><i class="fa-solid fa-file-lines"></i> Past Papers</a></li>
          <li><a href="../../digital-functional-skills-mock-exam.html" class="mfs-nav-link btn-nav-exam"><i class="fa-solid fa-desktop"></i> Mock Simulator</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- SUBNAV & BREADCRUMBS -->
  <div class="dfs-subnav-bar">
    <div class="mfs-container dfs-subnav-inner">
      <div class="dfs-breadcrumbs">
        <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="../../revise.html">Revision</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="index.html">{level_title} Digital Skills</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span style="color:#ffffff; font-weight:600;">{title}</span>
      </div>
      <div>
        <span class="dfs-level-badge-pill {level_badge_class}">{level_title} DFSQ</span>
      </div>
    </div>
  </div>

  <!-- HERO SECTION -->
  <section class="dfs-hero-header">
    <div class="mfs-container">
      <div class="dfs-hero-meta">
        <span class="dfs-spec-code">{spec_code}</span>
        <span style="color:#38bdf8; font-size:0.85rem; font-weight:600;"><i class="fa-solid fa-folder-open"></i> {skill_area}</span>
        <span class="dfs-time-tag"><i class="fa-regular fa-clock"></i> {time_est} Study Time</span>
      </div>
      <h1 class="dfs-hero-title">{title}</h1>
      <p class="dfs-hero-lead">{lead}</p>
      <div class="dfs-hero-objectives">
        {objectives_html}
      </div>
    </div>
  </section>

  <!-- MAIN LEARNING CONTENT -->
  <main class="dfs-layout-wrap">
    <div class="mfs-container">
      <div class="dfs-grid">

        <!-- 1. YOUTUBE VIDEO WALKTHROUGH EMBED -->
        <section id="video" class="dfs-section">
          <div class="dfs-section-header">
            <h2 class="dfs-section-title"><i class="fa-brands fa-youtube" style="color:#dc2626;"></i> Video Lesson &amp; Walkthrough</h2>
            <span class="dfs-section-badge">Tutor Guided Video</span>
          </div>
          <div class="dfs-video-box">
            <div class="dfs-video-player-wrap">
              {video_embed_html}
            </div>
            <div class="dfs-video-bar">
              <div><strong>Topic Focus:</strong> {title} ({spec_code})</div>
              <div><i class="fa-solid fa-volume-high" style="color:#38bdf8; margin-right:5px;"></i> Sonia Neural Clear British RP Cadence</div>
            </div>
          </div>
        </section>

        <!-- 2. STEP-BY-STEP TEACHING & VISUAL UI MOCKUPS -->
        <section id="teaching" class="dfs-section">
          <div class="dfs-section-header">
            <h2 class="dfs-section-title"><i class="fa-solid fa-book-open"></i> Step-by-Step Teaching &amp; Key Concepts</h2>
            <span class="dfs-section-badge">Core Knowledge</span>
          </div>
          
          <div class="dfs-steps-flow">
            {steps_html}
          </div>
        </section>

        <!-- 3. AUTHENTIC EXAM MODEL WALKTHROUGH -->
        <section id="model" class="dfs-section">
          <div class="dfs-section-header">
            <h2 class="dfs-section-title"><i class="fa-solid fa-award"></i> Authentic Pearson Edexcel Exam Model</h2>
            <span class="dfs-section-badge" style="background:#fee2e2; color:#dc2626;">Accredited Model</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:14px;">Here is how this skill is tested in the real Pearson Edexcel onscreen digital assessment, broken down with official examiner mark codes (<span class="dfs-mark-tag" style="display:inline-block; margin:0 3px;">[B1]</span> knowledge, <span class="dfs-mark-tag" style="background:#0284c7; display:inline-block; margin:0 3px;">[M1]</span> process, <span class="dfs-mark-tag" style="background:#0f766e; display:inline-block; margin:0 3px;">[A1]</span> accuracy).</p>
          {exam_model_html}
        </section>

        <!-- 4. INTERACTIVE FLUENCY DRILLS -->
        <section id="drills" class="dfs-section">
          <div class="dfs-section-header">
            <h2 class="dfs-section-title"><i class="fa-solid fa-bolt"></i> Interactive Fluency Drills</h2>
            <span class="dfs-section-badge" style="background:#d1fae5; color:#065f46;">Instant Check</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:14px;">Test your knowledge right now. Select an answer to receive immediate diagnostic feedback and tutor explanations.</p>
          <div class="dfs-drill-box">
            {drills_html}
          </div>
        </section>

        <!-- 5. EXAM-STYLE PRACTICE QUESTION & AUTO-SAVING SCRATCHPAD -->
        <section id="practice" class="dfs-section">
          <div class="dfs-section-header">
            <h2 class="dfs-section-title"><i class="fa-solid fa-pen-ruler"></i> Independent Practice Exam Task</h2>
            <span class="dfs-section-badge">Auto-Saving Scratchpad</span>
          </div>
          <p style="color:#475569; font-size:0.95rem; margin-bottom:14px;">Complete this practice task under exam conditions. Your working is saved automatically in your browser so you can return to it anytime.</p>
          {practice_html}
        </section>

        <!-- OFFICIAL ASSESSMENT & MOCK TESTING BRIDGE -->
        <div class="dfs-exam-bridge-card">
          <div class="exam-bridge-icon"><i class="fa-solid fa-desktop"></i></div>
          <div class="exam-bridge-content">
            <h4>Ready to test in the official Pearson exam environment?</h4>
            <p>Put your knowledge into timed exam practice using authentic candidate data files (.ZIP) in the Pearson onscreen test player.</p>
            <div class="exam-bridge-actions">
              <a href="../../digital-functional-skills-mock-exam.html" class="btn-exam-bridge primary" target="_blank"><i class="fa-solid fa-play"></i> Launch Online Mock Simulator &rarr;</a>
              <a href="../../digital-functional-skills-past-papers.html" class="btn-exam-bridge secondary" target="_blank"><i class="fa-solid fa-file-zipper"></i> Past Papers &amp; Data Files (.ZIP) &rarr;</a>
            </div>
          </div>
        </div>

        <!-- 6. LINKS TO REVISE & CONTINUOUS LEARNING -->
        <div class="dfs-rev-links-wrap">
          <div class="dfs-rev-links-title"><i class="fa-solid fa-diagram-project"></i> Links to Revise &amp; Connected Topics</div>
          <div class="dfs-pills-row">
            {pills_html}
            <a href="../../assets/downloads/past-papers/digital-skills/DFS_Handbook_MFS.pdf" class="dfs-pill-link" style="border-color:#86efac; color:#166534;"><i class="fa-solid fa-file-pdf"></i> Download {level_title} Revision Notes PDF</a>
            <a href="index.html" class="dfs-pill-link" style="border-color:#cbd5e1; color:#475569;"><i class="fa-solid fa-table-cells"></i> View All {level_title} Topics</a>
          </div>
        </div>

        <!-- TOPIC NAVIGATION BAR -->
        <div class="dfs-topic-nav-bar">
          <div>{prev_btn_html}</div>
          <div>{next_btn_html}</div>
        </div>

      </div>
    </div>
  </main>

  <!-- FOOTER -->
  <footer style="background:#0f172a; color:#94a3b8; padding:40px 0 24px; border-top:1px solid #1e293b; font-size:0.88rem;">
    <div class="mfs-container">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px; margin-bottom:24px; padding-bottom:20px; border-bottom:1px solid #1e293b;">
        <div class="mfs-brand">
          <div class="mfs-brand-icon"><i class="fa-solid fa-laptop-code"></i></div>
          <div class="mfs-brand-text">
            <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
            <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
          </div>
        </div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="index.html" style="color:#cbd5e1; text-decoration:none;">{level_title} Hub</a>
          <a href="../../digital-functional-skills-past-papers.html" style="color:#cbd5e1; text-decoration:none;">Past Papers &amp; Data Files</a>
          <a href="../../digital-functional-skills-mock-exam.html" style="color:#cbd5e1; text-decoration:none;">Online Mock Simulator</a>
          <a href="../../revise.html" style="color:#cbd5e1; text-decoration:none;">All Subjects</a>
          <a href="../../contact-us.html" style="color:#cbd5e1; text-decoration:none;">Contact Tutor</a>
        </div>
      </div>
      <div style="text-align:center; font-size:0.78rem; color:#64748b;">
        &copy; 2026 Master Functional Skills. All rights reserved. Pearson Edexcel and City &amp; Guilds aligned Digital Functional Skills Qualifications (DFSQ).
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../../assets/js/dfs-revision-engine.js?v=20261106_v1"></script>
</body>
</html>
'''

def render_hub_page(topics_by_area, level_code, level_title, is_root=False):
    """
    Renders the Integrated Dual-View Landing Page for Entry 3 or Level 1.
    Includes searchable table with direct topic actions and modern visual cards.
    """
    path_prefix = "" if is_root else "../../"
    subpath_prefix = f"digital-skills/{level_code}/" if is_root else ""
    root_prefix = "" if is_root else "../"

    self_landing_url = f"digital-functional-skills-{level_code}.html" if is_root else "index.html"
    other_level_code = "level-1" if level_code == "entry-3" else "entry-3"
    other_level_title = "Level 1" if level_code == "entry-3" else "Entry 3"
    if is_root:
        other_landing_url = f"digital-functional-skills-{other_level_code}.html"
    else:
        other_landing_url = f"../{other_level_code}/index.html"
    past_papers_url = f"{path_prefix}digital-functional-skills-past-papers.html"
    mock_exam_url = f"{path_prefix}digital-functional-skills-mock-exam.html"

    level_badge_class = 'e3' if level_code == 'entry-3' else 'l1'
    all_flat_topics = [t for t_list in topics_by_area.values() for t in t_list]
    total_topics = len(all_flat_topics)

    category_slug_map = {
        "1. Using Devices and Handling Information": "devices",
        "2. Creating and Editing": "creating",
        "3. Communicating": "communicating",
        "4. Transacting": "transacting",
        "5. Being Safe and Responsible Online": "safety"
    }

    category_short_name = {
        "1. Using Devices and Handling Information": "Using Devices",
        "2. Creating and Editing": "Creating & Editing",
        "3. Communicating": "Communicating",
        "4. Transacting": "Transacting",
        "5. Being Safe and Responsible Online": "Being Safe Online"
    }

    # 1. Generate Table Rows HTML
    table_rows_html = ""
    for t in all_flat_topics:
        area_slug = category_slug_map.get(t['skill_area'], "devices")
        clean_area = category_short_name.get(t['skill_area'], t['skill_area'])
        topic_url = f"{subpath_prefix}{t['slug']}.html"

        table_rows_html += f'''
        <div class="topic-row" data-cat="{area_slug}">
          <div class="topic-meta">
            <div class="topic-title">{t["title"]}</div>
            <div class="topic-category-tag tag-{area_slug}">
              <i class="fa-solid fa-tag"></i> {clean_area} ({t["code"]})
            </div>
          </div>
          <div class="topic-actions-group">
            <a href="{topic_url}" class="btn-mfs-revise"><i class="fa-solid fa-book-open"></i> Revise</a>
            <a href="{topic_url}#drills" class="btn-mfs-sheet btn-mfs-workout" title="Interactive Fluency Drill"><i class="fa-solid fa-bolt"></i> Fluency Drill</a>
            <a href="{topic_url}#practice" class="btn-mfs-sheet" title="Exam Practice &amp; Scratchpad"><i class="fa-solid fa-pen-ruler"></i> Practice Exam</a>
            <a href="{topic_url}#video" class="btn-mfs-video" title="Video Lesson"><i class="fa-brands fa-youtube"></i> Video Lesson</a>
          </div>
        </div>
        '''

    # 2. Generate Visual Cards Grid Sections HTML
    skill_area_icons = {
        "1. Using Devices and Handling Information": "fa-desktop",
        "2. Creating and Editing": "fa-file-lines",
        "3. Communicating": "fa-envelope",
        "4. Transacting": "fa-credit-card",
        "5. Being Safe and Responsible Online": "fa-shield-halved"
    }

    cards_sections_html = ""
    for skill_name, t_list in topics_by_area.items():
        area_num = skill_name.split(".")[0].strip()
        clean_name = skill_name.split(".", 1)[1].strip() if "." in skill_name else skill_name
        icon = skill_area_icons.get(skill_name, "fa-layer-group")

        cards_html = ""
        for t in t_list:
            topic_url = f"{subpath_prefix}{t['slug']}.html"
            cards_html += f'''
            <a href="{topic_url}" class="dfs-topic-card">
              <div class="dfs-card-top-meta">
                <span class="dfs-card-code">{t["code"]}</span>
                <span class="dfs-card-time"><i class="fa-regular fa-clock"></i> {t.get("time", "15 Mins")}</span>
              </div>
              <h3 class="dfs-card-title">{t["title"]}</h3>
              <p class="dfs-card-desc">{t["lead"][:140]}...</p>
              <div class="dfs-card-footer">
                <span>Start Topic Revision</span>
                <i class="fa-solid fa-arrow-right"></i>
              </div>
            </a>
            '''

        cards_sections_html += f'''
        <div class="dfs-hub-section">
          <div class="dfs-hub-skill-header">
            <span class="dfs-hub-skill-num">Skill Area {area_num}</span>
            <h2 class="dfs-hub-skill-title"><i class="fa-solid {icon}" style="color:#0284c7; margin-right:8px;"></i> {clean_name}</h2>
          </div>
          <div class="dfs-topic-cards-grid">
            {cards_html}
          </div>
        </div>
        '''

    other_level_code = "level-1" if level_code == "entry-3" else "entry-3"
    other_level_title = "Level 1" if level_code == "entry-3" else "Entry 3"
    other_landing_url = f"digital-functional-skills-{other_level_code}.html" if is_root else f"../{other_level_code}/index.html"

    # Master Hub HTML
    return f'''<!DOCTYPE html>
<html lang="en-GB" data-theme="maths" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Functional Skills Digital {level_title} | Master Functional Skills</title>
  <meta name="description" content="Master Functional Skills Digital {level_title}. Complete topic-by-topic revision guides, software UI simulations, video walkthroughs, fluency drills, and accredited onscreen practice tests.">
  <link rel="icon" type="image/svg+xml" href="{path_prefix}assets/img/favicon.svg">
  <link rel="alternate icon" href="{path_prefix}favicon.ico">
  <meta name="theme-color" content="#0f172a">
  
  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  
  <!-- Dedicated Digital Skills Revision Styles -->
  <link rel="stylesheet" href="{path_prefix}assets/css/mfs-dfs-revision.css?v=20261106_v2">
</head>
<body data-tint="cream">

  <!-- TOP TRUST BAR & ACCESSIBILITY CONTROLS -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel &amp; City &amp; Guilds Aligned</span>
        <span class="top-trust-item"><i class="fa-solid fa-award"></i> Accredited DFSQ Course Material</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <div class="mfs-tint-dropdown-wrap">
            <button type="button" id="tintToggle" class="btn-tint-toggle" onclick="toggleTintMenu(event)" title="Change dyslexia background tint">
              <span class="tint-swatch-indicator" id="tintCurrentSwatch"></span>
              <span id="tintLabel">Cream Tint</span>
              <i class="fa-solid fa-chevron-down" style="font-size:0.62rem; opacity:0.75; margin-left:2px;"></i>
            </button>
            <div id="tintMenu" class="tint-picker-menu">
              <div class="tint-picker-title"><i class="fa-solid fa-glasses"></i> Dyslexia Reading Tint</div>
              <button type="button" class="tint-option-btn active" data-tint="cream" onclick="setSiteTint('cream', event)">
                <span class="swatch swatch-cream"></span>
                <span class="tint-name">Cream (Recommended)</span>
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
              <div class="tint-divider" style="height:1px; background:#e2e8f0; margin:6px 0;"></div>
              <button type="button" class="tint-option-btn" data-tint="none" onclick="setSiteTint('none', event)">
                <span class="swatch swatch-none"></span>
                <span class="tint-name">No Tint (White)</span>
                <i class="fa-solid fa-check check-icon"></i>
              </button>
            </div>
          </div>
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
        </div>
        <a href="{path_prefix}contact-us.html" class="btn-tint-toggle" style="text-decoration:none;"><i class="fa-solid fa-envelope"></i> Contact</a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <header class="mfs-navbar">
    <div class="mfs-container mfs-navbar-inner">
      <a href="{path_prefix}index.html" class="mfs-brand">
        <div class="mfs-brand-icon"><i class="fa-solid fa-laptop-code"></i></div>
        <div class="mfs-brand-text">
          <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
          <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
        </div>
      </a>

      <nav class="mfs-nav-wrapper">
        <ul class="mfs-nav-menu">
          <li><a href="{path_prefix}revise.html" class="mfs-nav-link"><i class="fa-solid fa-book-open-reader"></i> Revision Hub</a></li>
          <li><a href="{self_landing_url}" class="mfs-nav-link active"><i class="fa-solid fa-list-check"></i> {level_title} Directory</a></li>
          <li><a href="{other_landing_url}" class="mfs-nav-link"><i class="fa-solid fa-arrow-right-arrow-left"></i> Switch to {other_level_title}</a></li>
          <li><a href="{past_papers_url}" class="mfs-nav-link"><i class="fa-solid fa-file-lines"></i> Past Papers</a></li>
          <li><a href="{mock_exam_url}" class="mfs-nav-link btn-nav-exam"><i class="fa-solid fa-desktop"></i> Mock Simulator</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- SUBNAV & BREADCRUMBS -->
  <div class="dfs-subnav-bar">
    <div class="mfs-container dfs-subnav-inner">
      <div class="dfs-breadcrumbs">
        <a href="{path_prefix}index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="{path_prefix}revise.html">Revision</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="{path_prefix}digital-skills/index.html">Digital Skills Hub</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span style="color:#ffffff; font-weight:600;">{level_title} Digital Skills</span>
      </div>
      <div>
        <span class="dfs-level-badge-pill {level_badge_class}">{level_title} DFSQ</span>
      </div>
    </div>
  </div>

  <!-- HERO SECTION -->
  <section class="dfs-hero-header">
    <div class="mfs-container">
      <div class="dfs-hero-meta">
        <span class="dfs-spec-code">Pearson Edexcel &amp; City &amp; Guilds Specification</span>
        <span class="dfs-time-tag"><i class="fa-solid fa-layer-group"></i> {total_topics} Dedicated Topics</span>
      </div>
      <h1 class="dfs-hero-title">Functional Skills Digital {level_title} Revision Portal</h1>
      <p class="dfs-hero-lead">Every criterion has its own dedicated master revision page featuring clear explanations, software UI guides, video walkthroughs, fluency drills, and Pearson Edexcel style practice tasks.</p>

      <!-- 3 Feature Action Cards -->
      <div class="feature-cards-row">
        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge"><i class="fa-solid fa-book-open"></i></div>
            <div class="feature-card-body">
              <h3>Revise {level_title} Topics</h3>
              <p>Explore {total_topics} dedicated guides with UI simulations, tutor rules, and worked models.</p>
            </div>
          </div>
          <a href="#curriculumSection" class="btn-card-action">View Topic Directory &darr;</a>
        </div>

        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge" style="background:#d1fae5; color:#065f46;"><i class="fa-solid fa-desktop"></i></div>
            <div class="feature-card-body">
              <h3>Onscreen Mock Simulator</h3>
              <p>Practice authentic computer-based exams directly in your browser with self-marking solutions.</p>
            </div>
          </div>
          <a href="{mock_exam_url}" class="btn-card-action" style="color:#0f766e;">Launch Exam Simulator &rarr;</a>
        </div>

        <div class="feature-action-card">
          <div class="feature-card-top">
            <div class="feature-icon-badge" style="background:#fee2e2; color:#dc2626;"><i class="fa-regular fa-file-pdf"></i></div>
            <div class="feature-card-body">
              <h3>Past Papers &amp; Data Files</h3>
              <p>Download official sample assessment materials, mark schemes, and practice datasets.</p>
            </div>
          </div>
          <a href="{past_papers_url}" class="btn-card-action" style="color:#dc2626;">Download Past Papers &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- INTERACTIVE SEARCHABLE DIRECTORY SECTION -->
  <main class="mfs-directory-section" id="curriculumSection">
    <div class="mfs-container">
      
      <!-- DUAL MOCK TESTING & PAST PAPERS CHANNELS BANNER -->
      <div class="dfs-mocks-hero-banner">
        <div class="dfs-mocks-banner-header">
          <div class="dfs-mocks-banner-title">
            <i class="fa-solid fa-laptop-code" style="color:#38bdf8;"></i> Authentic Pearson DFSQ Examination Environment
          </div>
          <div class="dfs-mocks-banner-badge">Essential Assessment Links</div>
        </div>
        <div class="dfs-mocks-banner-grid">
          <div class="dfs-mock-channel-card">
            <div>
              <div class="dfs-mock-card-icon icon-simulator"><i class="fa-solid fa-desktop"></i></div>
              <div class="dfs-mock-card-title">Browser Mock Exam Simulator</div>
              <p class="dfs-mock-card-desc">
                Experience the authentic Pearson Edexcel onscreen test player in your browser. Screen-by-screen navigation, grey question banners, option pills, section review screen, and official diagnostic score report.
              </p>
            </div>
            <a href="{mock_exam_url}" class="btn-mock-channel btn-mock-channel-primary">
              <i class="fa-solid fa-play"></i> Launch Online Mock Exam Simulator &rarr;
            </a>
          </div>

          <div class="dfs-mock-channel-card">
            <div>
              <div class="dfs-mock-card-icon icon-papers"><i class="fa-solid fa-file-zipper"></i></div>
              <div class="dfs-mock-card-title">Past Papers, Data Files &amp; Mark Schemes</div>
              <p class="dfs-mock-card-desc">
                Download authentic Pearson Edexcel Digital Functional Skills question papers, full candidate data file packages (.ZIP) with starter spreadsheets, images, and official examiner mark schemes.
              </p>
            </div>
            <a href="{past_papers_url}" class="btn-mock-channel btn-mock-channel-secondary">
              <i class="fa-solid fa-download"></i> Download Papers &amp; Data Files (.ZIP) &rarr;
            </a>
          </div>
        </div>
      </div>
      
      <!-- Directory Head Card with Search & Dual-View Toggle -->
      <div class="directory-head-card">
        <div class="directory-head-title-wrap">
          <h2>
            <i class="fa-solid fa-list-check" style="color:#0284c7;"></i>
            Functional Skills Digital {level_title} Curriculum
            <span class="badge-count" id="badgeTopicCount">{total_topics} Topics</span>
          </h2>
        </div>

        <div class="directory-controls-wrap">
          <!-- View Switcher -->
          <div class="view-mode-toggle-group">
            <button type="button" id="btnViewTable" class="btn-view-toggle active" onclick="switchView('table')">
              <i class="fa-solid fa-table-list"></i> Table View
            </button>
            <button type="button" id="btnViewCards" class="btn-view-toggle" onclick="switchView('cards')">
              <i class="fa-solid fa-grip"></i> Visual Cards
            </button>
          </div>

          <!-- Instant Search -->
          <div class="directory-search-wrapper">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input type="search" class="directory-search-input" id="topicSearchInput" placeholder="Search topics, formulas, keywords...">
          </div>
        </div>
      </div>

      <!-- Category Filter Bar -->
      <div class="category-filter-bar">
        <button type="button" class="btn-cat-filter active" data-filter="all" onclick="filterCategory('all', this)">
          <i class="fa-solid fa-asterisk"></i> All Topics ({total_topics})
        </button>
        <button type="button" class="btn-cat-filter" data-filter="devices" onclick="filterCategory('devices', this)">
          <i class="fa-solid fa-desktop" style="color:#0284c7;"></i> 1. Using Devices
        </button>
        <button type="button" class="btn-cat-filter" data-filter="creating" onclick="filterCategory('creating', this)">
          <i class="fa-solid fa-file-lines" style="color:#0f766e;"></i> 2. Creating &amp; Editing
        </button>
        <button type="button" class="btn-cat-filter" data-filter="communicating" onclick="filterCategory('communicating', this)">
          <i class="fa-solid fa-envelope" style="color:#d97706;"></i> 3. Communicating
        </button>
        <button type="button" class="btn-cat-filter" data-filter="transacting" onclick="filterCategory('transacting', this)">
          <i class="fa-solid fa-credit-card" style="color:#dc2626;"></i> 4. Transacting
        </button>
        <button type="button" class="btn-cat-filter" data-filter="safety" onclick="filterCategory('safety', this)">
          <i class="fa-solid fa-shield-halved" style="color:#7c3aed;"></i> 5. Being Safe Online
        </button>
      </div>

      <!-- VIEW 1: SEARCHABLE TABLE VIEW (Corbett / Action Row Style) -->
      <div id="tableViewContainer">
        <div class="topic-table-bar">
          <span>Topic Name &amp; Skill Area</span>
          <span>Dedicated Revision &amp; Study Resources</span>
        </div>
        <div class="topic-rows-container" id="topicsContainer">
          {table_rows_html}
        </div>
      </div>

      <!-- VIEW 2: VISUAL CARDS GRID (Modern Card Style) -->
      <div id="cardsViewContainer" style="display:none; padding-top:24px;">
        {cards_sections_html}
      </div>

    </div>
  </main>

  <!-- FOOTER -->
  <footer style="background:#0f172a; color:#94a3b8; padding:40px 0 24px; border-top:1px solid #1e293b; font-size:0.88rem;">
    <div class="mfs-container">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px; margin-bottom:24px; padding-bottom:20px; border-bottom:1px solid #1e293b;">
        <div class="mfs-brand">
          <div class="mfs-brand-icon"><i class="fa-solid fa-laptop-code"></i></div>
          <div class="mfs-brand-text">
            <div class="mfs-brand-title">MASTER<span>FUNCTIONALSKILLS</span></div>
            <div class="mfs-brand-subtitle">Delivering Skills • Achieving Goals</div>
          </div>
        </div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="{path_prefix}revise.html" style="color:#cbd5e1; text-decoration:none;">Revision Hub</a>
          <a href="{other_landing_url}" style="color:#cbd5e1; text-decoration:none;">{other_level_title} Digital Skills</a>
          <a href="{past_papers_url}" style="color:#cbd5e1; text-decoration:none;">Past Papers &amp; Data Files</a>
          <a href="{mock_exam_url}" style="color:#cbd5e1; text-decoration:none;">Online Mock Simulator</a>
          <a href="{path_prefix}contact-us.html" style="color:#cbd5e1; text-decoration:none;">Contact Tutor</a>
        </div>
      </div>
      <div style="text-align:center; font-size:0.78rem; color:#64748b;">
        &copy; 2026 Master Functional Skills. All rights reserved.
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="{path_prefix}assets/js/dfs-revision-engine.js?v=20261106_v1"></script>
  <script>
    // Dual View Switcher Logic
    function switchView(mode) {{
      var tableContainer = document.getElementById('tableViewContainer');
      var cardsContainer = document.getElementById('cardsViewContainer');
      var btnTable = document.getElementById('btnViewTable');
      var btnCards = document.getElementById('btnViewCards');

      if (mode === 'cards') {{
        tableContainer.style.display = 'none';
        cardsContainer.style.display = 'block';
        btnTable.classList.remove('active');
        btnCards.classList.add('active');
      }} else {{
        tableContainer.style.display = 'block';
        cardsContainer.style.display = 'none';
        btnTable.classList.add('active');
        btnCards.classList.remove('active');
      }}
    }}

    // Instant Search & Category Filter Logic
    var activeCategory = 'all';

    function filterCategory(cat, btn) {{
      activeCategory = cat;
      document.querySelectorAll('.btn-cat-filter').forEach(function(b) {{
        b.classList.remove('active');
      }});
      if (btn) btn.classList.add('active');
      applyCombinedFilter();
    }}

    function applyCombinedFilter() {{
      var searchInput = document.getElementById('topicSearchInput');
      var query = searchInput ? searchInput.value.toLowerCase().trim() : '';
      var rows = document.querySelectorAll('#topicsContainer .topic-row');
      var count = 0;

      rows.forEach(function(row) {{
        var rowCat = row.getAttribute('data-cat');
        var rowText = row.textContent.toLowerCase();

        var matchesCat = (activeCategory === 'all' || rowCat === activeCategory);
        var matchesQuery = (query === '' || rowText.includes(query));

        if (matchesCat && matchesQuery) {{
          row.style.display = 'flex';
          count++;
        }} else {{
          row.style.display = 'none';
        }}
      }});

      var badge = document.getElementById('badgeTopicCount');
      if (badge) {{
        badge.textContent = count + ' Topics';
      }}
    }}

    document.addEventListener('DOMContentLoaded', function() {{
      var searchInput = document.getElementById('topicSearchInput');
      if (searchInput) {{
        searchInput.addEventListener('input', applyCombinedFilter);
      }}
    }});
  </script>
</body>
</html>
'''
