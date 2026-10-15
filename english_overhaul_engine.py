#!/usr/bin/env python3
import os, sys

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from build_all_curriculum_pages import build_full_html

def render_english_topic(data):
    filename = data["filename"]
    clean_topic = data["clean_topic"]
    subject = data.get("subject", "English")
    subject_pill_icon = "fa-pen-nib"
    subject_dir = "functional-skills-english-level-2.html"
    hero_title = f"{clean_topic}: <span>Rules, Worked Models &amp; Exam Practice</span>"
    intro_lead = data["intro_lead"]
    next_file = data.get("next_file", "functional-skills-english-level-2.html")
    next_name = data.get("next_name", "English Level 2 Directory")

    toc_items = [
        ("specification", "Specification", "fa-clipboard-check"),
        ("golden-rules", "Golden Rules", "fa-lightbulb"),
    ]
    for idx, sk in enumerate(data.get("skills", []), 1):
        toc_items.append((f"skill-{idx}", f"{idx}. {sk['title']}", "fa-book-open"))

    toc_items.extend([
        ("worked-exam-models", "Exam Models", "fa-graduation-cap"),
        ("examiner-traps", "Examiner Traps", "fa-triangle-exclamation"),
        ("practice-questions", "Exam Practice", "fa-pencil"),
        ("downloads", "Downloads (PDF)", "fa-file-pdf")
    ])

    # Specification
    spec_items = "".join(f"<li><strong>{code}</strong> – {desc}</li>" for code, desc in data["spec_points"])
    spec_html = f"""
    <!-- SPECIFICATION -->
    <section id="specification" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
      </div>
      <div class="skill-card-container">
        <p>Candidates must demonstrate mastery of the following regulated Functional Skills English outcomes:</p>
        <ul style="padding-left:20px; line-height:1.8; color:#334155;">
          {spec_items}
        </ul>
      </div>
    </section>
    """

    # Golden Rules
    rules_cards = ""
    for r in data["golden_rules"]:
        rules_cards += f"""
        <div class="rule-card-amber">
          <div class="rule-card-amber-header">
            <i class="fa-solid {r['icon']}"></i>
            <span>{r['title']}</span>
          </div>
          <p>{r['desc']}</p>
          <div class="rule-highlight-badge">
            <strong>Golden Rule / Technique:</strong> {r['badge']}
          </div>
        </div>
        """
    rules_html = f"""
    <!-- GOLDEN RULES -->
    <section id="golden-rules" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for {clean_topic}</h2>
      </div>
      {rules_cards}
    </section>
    """

    # Skills
    skills_html = ""
    for idx, sk in enumerate(data.get("skills", []), 1):
        skills_html += f"""
        <!-- SKILL {idx}: {sk['title']} -->
        <section id="skill-{idx}" class="revision-section">
          <div class="mfs-topic-card">
            <div class="mfs-topic-head">
              <h3 class="mfs-topic-title"><span class="mfs-topic-prefix">Core Skill {idx}:</span> {sk['title']}</h3>
              <p class="mfs-topic-stem">{sk['summary']}</p>
            </div>
            <div class="mfs-topic-body" style="padding:20px 24px;">
              {sk['content_html']}
            </div>
            <div class="mfs-topic-footer" style="display:flex; gap:8px; flex-wrap:wrap; padding-top:14px; border-top:1px solid #e2e8f0; margin-top:16px;">
              <span class="mfs-pill-l1">Level 1</span>
              <span class="mfs-pill-l2">Level 2</span>
              <span class="mfs-pill-board">Pearson Edexcel</span>
              <span class="mfs-pill-board">City &amp; Guilds</span>
              <span class="mfs-pill-board">NCFE</span>
            </div>
          </div>
        </section>
        """

    # Worked Models
    models_cards = ""
    for m_idx, m in enumerate(data["worked_models"], 1):
        steps_html = ""
        for step_item in m["steps"]:
            if len(step_item) == 4:
                s_num, s_title, s_calc, s_mark = step_item
            elif len(step_item) == 3:
                s_num, s_title, s_calc = step_item
                s_mark = "Pass Criteria"
            else:
                s_num, s_title, s_calc, s_mark = "Step", "Method", str(step_item), ""
            steps_html += f"""
            <div class="model-step-row model-step-grid-row">
              <div class="model-step-col-step">
                <span class="example-step-pill">{s_num}</span>
                <span class="model-step-title">{s_title}</span>
              </div>
              <div class="model-step-col-desc">
                {s_calc}
              </div>
              <div class="model-step-col-criteria">
                <span class="criteria-badge-teal"><i class="fa-solid fa-award" style="font-size:0.78rem; margin-right:4px; opacity:0.85;"></i><strong>Criteria:</strong> {s_mark}</span>
              </div>
            </div>
            """
        models_cards += f"""
        <div class="model-example-card" style="margin-bottom:24px;">
          <div class="model-card-header">
            <span class="model-badge"><i class="fa-solid fa-graduation-cap"></i> Benchmark Exam Model {m_idx}</span>
            <span class="model-marks-pill">{m['marks']}</span>
          </div>
          <div class="model-scenario" style="padding:16px 20px; background:#fff; border-bottom:1px solid #e2e8f0;">
            <p style="font-weight:600; color:#0f172a; margin-bottom:8px;">Vocational Context: <span style="color:#0369a1;">{m['context']}</span></p>
            <div class="model-q-stem" style="font-size:1.05rem; line-height:1.7; color:#334155;">{m['question']}</div>
          </div>
          <div class="model-steps-container" style="padding:18px 20px; background:#ffffff;">
            <!-- 3-Column Header: Step, Description, Criteria -->
            <div class="model-steps-header-row">
              <div><i class="fa-solid fa-list-ol" style="color:#0284c7; margin-right:6px;"></i> Step</div>
              <div><i class="fa-solid fa-pen-nib" style="color:#0284c7; margin-right:6px;"></i> Description / Working</div>
              <div><i class="fa-solid fa-clipboard-check" style="color:#0284c7; margin-right:6px;"></i> Criteria</div>
            </div>
            {steps_html}
            <div class="model-final-answer" style="margin-top:16px; padding:12px 18px; background:#f0fdf4; border:1px solid #86efac; border-radius:6px; font-weight:700; color:#166534; font-size:1.05rem;">
              <i class="fa-solid fa-check-circle"></i> Final Accredited Response: {m['final_answer']}
            </div>
            <div class="examiner-guidance-box">
              <div class="examiner-guidance-header">
                <i class="fa-solid fa-clipboard-check"></i>
                <span>Marking Scheme Guidance &amp; Assessment Criteria</span>
              </div>
              <div class="examiner-guidance-text">
                {m['tutor_tip']}
              </div>
            </div>
          </div>
        </div>
        """

    models_html = f"""
    <!-- WORKED EXAM MODELS -->
    <section id="worked-exam-models" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Pearson Edexcel Step-by-Step Worked Models</h2>
      </div>
      {models_cards}
    </section>
    """

    # Examiner Traps
    traps_cards = ""
    for t in data["examiner_traps"]:
        traps_cards += f"""
        <div class="examiner-pitfall-box">
          <div class="examiner-pitfall-title">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span>Examiner Pitfall: {t['title']}</span>
          </div>
          <div class="examiner-pitfall-desc">
            {t['desc']}
          </div>
          <div class="examiner-pitfall-fix">
            <i class="fa-solid fa-shield-halved" style="color:#e11d48; margin-top:2px;"></i>
            <div><strong>How to Avoid This Pitfall:</strong> {t['fix']}</div>
          </div>
        </div>
        """

    traps_html = f"""
    <!-- EXAMINER TRAPS -->
    <section id="examiner-traps" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-triangle-exclamation"></i> Critical Examiner Traps &amp; Common Pitfalls</h2>
      </div>
      {traps_cards}
    </section>
    """

    # Practice Questions (ensure 3 questions per topic)
    p_questions = list(data.get("practice_questions", []))
    if len(p_questions) < 3:
        base_name = filename.replace("functional-skills-", "").replace(".html", "")
        ws_ans_file = os.path.join(PROJECT_DIR, "worksheets", f"{base_name}-answers.html")
        if not os.path.exists(ws_ans_file):
            ws_ans_file = os.path.join(PROJECT_DIR, "worksheets", f"{filename.replace('.html', '')}-answers.html")
        if os.path.exists(ws_ans_file):
            import re
            with open(ws_ans_file, "r", encoding="utf-8") as af:
                af_html = af.read()
            raw_cards = re.findall(r'<div class="ans-card">(.*?)</div>\s*(?=<div class="(?:ans-card|tier-divider|sheet-footer)"|\s*</div>\s*</body>)', af_html, re.DOTALL)
            for extra_card in raw_cards[1:3]:
                if len(p_questions) >= 3:
                    break
                m_marks = re.search(r'<span class="ans-marks-badge">\[?(.*?)\]?</span>', extra_card, re.DOTALL)
                m_stem = re.search(r'<div class="ans-stem-quote">(.*?)</div>', extra_card, re.DOTALL)
                m_steps = re.findall(r'<div class="step-row">\s*<span>(.*?)</span>\s*<span class="mark-code">(.*?)</span>\s*</div>', extra_card, re.DOTALL)
                m_award = re.search(r'<span class="award-val">(.*?)</span>', extra_card, re.DOTALL)
                m_pitfall = re.search(r'<div class="pitfall-box">(.*?)</div>', extra_card, re.DOTALL)

                q_marks = m_marks.group(1).replace("Total", "").strip() if m_marks else "2 Marks"
                if not q_marks.endswith("Marks") and not q_marks.endswith("Mark"):
                    q_marks += " Marks"
                q_stem = m_stem.group(1).strip() if m_stem else ""
                steps_lines = [f"{i+1}. {re.sub(r'^\d+\.\s*', '', s[0].strip())} <span style=\"color:#0f766e; font-weight:600;\">({s[1].strip()})</span>" for i, s in enumerate(m_steps)] if m_steps else ["1. Apply standard mark scheme criteria."]
                q_steps = "<br>".join(steps_lines)
                q_award = m_award.group(1).strip() if m_award else ""
                q_tip = f"Examiner Tip: {re.sub(r'<strong[^>]*>.*?</strong>', '', m_pitfall.group(1), flags=re.DOTALL).strip()}" if m_pitfall else "Ensure accurate spelling, punctuation, and tone throughout."

                p_questions.append({
                    "marks": q_marks,
                    "question": q_stem,
                    "solution_steps": q_steps,
                    "correct_answer": q_award,
                    "tutor_tip": q_tip
                })

    practice_cards = ""
    for p_idx, p in enumerate(p_questions, 1):
        practice_cards += f"""
        <div class="practice-q-card" style="margin-bottom:20px; border:1px solid #cbd5e1; border-radius:8px; overflow:hidden; background:#fff;">
          <div class="practice-q-header" style="padding:12px 18px; background:#f8fafc; border-bottom:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-weight:700; color:#1e293b;"><i class="fa-solid fa-pencil"></i> Exam Practice Question {p_idx}</span>
            <span class="practice-marks-pill">{p['marks']}</span>
          </div>
          <div class="practice-q-body" style="padding:18px 20px;">
            <div class="practice-q-stem" style="font-size:1.05rem; line-height:1.7; color:#334155; margin-bottom:16px;">
              {p['question']}
            </div>
            <div class="practice-interactive-wrap">
              <label style="display:block; font-weight:600; font-size:0.9rem; color:#475569; margin-bottom:6px;">Your Written Draft / Notes (Auto-saves):</label>
              <textarea class="practice-scratchpad" rows="4" style="width:100%; border:1px solid #cbd5e1; border-radius:6px; padding:10px; font-size:0.95rem; line-height:1.6;" placeholder="Write your practice response or quotation analysis here..."></textarea>
              <div style="margin-top:12px; display:flex; gap:10px;">
                <button type="button" class="btn-solution-toggle" onclick="toggleSolution('sol-{p_idx}')" style="padding:8px 16px; background:#0284c7; color:#fff; border:none; border-radius:6px; font-weight:600; cursor:pointer;">
                  <i class="fa-solid fa-eye"></i> Show Solution
                </button>
              </div>
              <div id="sol-{p_idx}" class="practice-solution-drawer" style="display:none; margin-top:14px; padding:16px; background:#f0fdf4; border:1px solid #86efac; border-radius:6px;">
                <div style="font-weight:700; color:#166534; margin-bottom:6px;"><i class="fa-solid fa-check"></i> Marking Scheme Criteria:</div>
                <div style="line-height:1.7; color:#14532d;">{p['solution_steps']}</div>
                <div style="margin-top:10px; font-weight:800; color:#166534;">Final Model Answer: {p['correct_answer']}</div>
                <div style="margin-top:8px; font-size:0.88rem; color:#15803d; font-style:italic;">Examiner Tip: {p['tutor_tip']}</div>
              </div>
            </div>
          </div>
        </div>
        """

    practice_html = f"""
    <!-- PRACTICE QUESTIONS -->
    <section id="practice-questions" class="revision-section">
      <div class="section-header-row">
        <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
      </div>
      {practice_cards}
    </section>
    """

    content_sections = f"{spec_html}\n{rules_html}\n{skills_html}\n{models_html}\n{traps_html}\n{practice_html}"

    full_html = build_full_html(
        filename=filename,
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_sections,
        next_file=next_file,
        next_name=next_name
    )

    dest_path = os.path.join(PROJECT_DIR, filename)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] Generated overhauled English page: {filename}")
