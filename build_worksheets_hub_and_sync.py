#!/usr/bin/env python3
"""
Master Functional Skills - Master Worksheets Hub Generator & Topic Page Synchronizer.
Builds the Corbett-inspired /worksheets.html directory and updates all topic pages with
the 2 distinct worksheet styles (Skill Workout + Exam Practice).
"""

import os, glob, re
import generate_all_curriculum_worksheets_final as c_final

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSHEETS_DIR = os.path.join(BASE_DIR, "worksheets")

def get_domain_category(slug, subject):
    s = slug.lower()
    sub = subject.lower()
    
    if "reading" in sub or "reading" in s:
        return "english-reading", "English: Reading Comprehension"
    if "writing" in sub or "writing" in s:
        return "english-writing", "English: Writing & SPaG"
    if "slc" in sub or "slc" in s or "speaking" in sub or "speaking" in s or "listening" in sub:
        return "english-slc", "English: Speaking, Listening & Communicating (SLC)"
    if "digital" in sub or "digital" in s:
        return "digital-skills", "Digital Functional Skills (DFS)"
    
    # Maths domains
    number_keywords = ['number', 'fraction', 'decimal', 'percentage', 'ratio', 'proportion', 'formula', 'money', 'bidmas', 'interest', 'multiplication', 'division', 'addition', 'subtraction', 'rounding', 'estimating', 'place-value']
    measures_keywords = ['area', 'perimeter', 'volume', 'capacity', 'surface', 'length', 'weight', 'speed', 'density', 'time', 'shape', 'angle', 'bearing', 'scale', 'map', 'temperature', 'conversion', 'unit', 'net', 'symmetry', 'coordinate']
    data_keywords = ['mean', 'median', 'mode', 'range', 'average', 'data', 'chart', 'graph', 'table', 'probability', 'tally', 'list', 'scatter']
    
    for kw in number_keywords:
        if kw in s:
            return "maths-number", "Maths: Number & Calculations"
    for kw in measures_keywords:
        if kw in s:
            return "maths-measures", "Maths: Measures, Shape & Space"
    for kw in data_keywords:
        if kw in s:
            return "maths-data", "Maths: Handling Data & Statistics"
            
    return "maths-number", "Maths: Number & Calculations"

def generate_worksheets_hub():
    all_topics = c_final.ALL_TOPICS
    print(f"Generating master worksheets hub for {len(all_topics)} topics...")
    
    # Group topics
    categories = {
        "maths-number": {"title": "Maths: Number and Calculations", "icon": "fa-calculator", "topics": []},
        "maths-measures": {"title": "Maths: Measures, Shape and Space", "icon": "fa-ruler-combined", "topics": []},
        "maths-data": {"title": "Maths: Handling Data and Statistics", "icon": "fa-chart-column", "topics": []},
        "english-reading": {"title": "English: Reading Comprehension", "icon": "fa-book-open-reader", "topics": []},
        "english-writing": {"title": "English: Writing & Technical Accuracy", "icon": "fa-pen-nib", "topics": []},
        "english-slc": {"title": "English: Speaking, Listening & Communicating (SLC)", "icon": "fa-comments", "topics": []},
        "digital-skills": {"title": "Digital Functional Skills (DFS)", "icon": "fa-laptop-code", "topics": []}
    }
    
    for slug, t_data in sorted(all_topics.items(), key=lambda x: x[1].get('title', x[0])):
        cat_key, cat_name = get_domain_category(slug, t_data.get('subject', 'Mathematics'))
        categories[cat_key]["topics"].append((slug, t_data))
        
    # Build Directory HTML
    sections_html = ""
    for cat_key, cat_info in categories.items():
        topics_list = cat_info["topics"]
        if not topics_list:
            continue
            
        topic_cards = []
        for slug, t_data in topics_list:
            title = t_data.get('title', slug.replace('-', ' ').title())
            spec = t_data.get('spec_codes', 'Pearson Edexcel Reformed')
            level = "Level 1 & Level 2"
            
            # Guide link
            candidates = [
                f"{slug}.html",
                f"functional-skills-{slug}.html",
                f"reading-{slug.replace('reading-', '')}.html",
                f"writing-{slug.replace('writing-', '')}.html",
                f"slc-{slug.replace('slc-', '')}.html",
            ]
            if slug == 'fdp-conversions':
                candidates.insert(0, 'functional-skills-fractions-decimals-and-percentages.html')
            if slug in ('english-level-2-writing-blog', 'writing-blog', 'blog'):
                candidates.insert(0, 'functional-skills-english-level-2-writing-blog.html')
            if slug == 'formulas' or slug == 'algebra':
                candidates.insert(0, 'functional-skills-formulas.html')
            if slug == 'division-and-remainders':
                candidates.insert(0, 'functional-skills-division.html')
            if slug == 'money-invoicing-payroll':
                candidates.insert(0, 'functional-skills-money.html')
            if cat_key == 'english-reading':
                candidates.insert(0, f"reading-{slug.replace('reading-', '')}.html")
                candidates.insert(1, f"{slug}.html")

            guide_url = f"{slug}.html"
            for cand in candidates:
                if os.path.exists(os.path.join(BASE_DIR, cand)):
                    guide_url = cand
                    break
                
            workout_url = f"worksheets/{slug}-workout.html"
            workout_ans_url = f"worksheets/{slug}-workout-answers.html"
            practice_url = f"worksheets/{slug}-worksheet.html"
            practice_ans_url = f"worksheets/{slug}-answers.html"
            
            topic_cards.append(f"""
            <div class="hub-topic-card" data-topic-name="{title.lower()} {slug}">
              <div class="hub-topic-header">
                <div>
                  <h3 class="hub-topic-title"><a href="{guide_url}">{title}</a></h3>
                  <div class="hub-topic-badges">
                    <span class="hub-badge-level">{level}</span>
                    <span class="hub-badge-spec">{spec}</span>
                  </div>
                </div>
                <a href="{guide_url}" class="hub-btn-guide" title="View interactive study guide">
                  <i class="fa-solid fa-book-bookmark"></i> Study Guide
                </a>
              </div>
              
              <div class="hub-action-row">
                <!-- Style 1: Skill Workout -->
                <div class="hub-style-group style-workout">
                  <div class="hub-style-label"><i class="fa-solid fa-repeat text-blue"></i> Style 1: Skill Workout</div>
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
                  <div class="hub-style-label"><i class="fa-solid fa-file-shield text-purple"></i> Style 2: Exam Booklet</div>
                  <div class="hub-btn-pair">
                    <a href="{practice_url}" target="_blank" class="hub-btn btn-practice" title="Pearson Edexcel exam questions">
                      <i class="fa-solid fa-file-pen"></i> Exam Booklet
                    </a>
                    <a href="{practice_ans_url}" target="_blank" class="hub-btn btn-ans" title="Step-by-step mark scheme">
                      <i class="fa-solid fa-award"></i> Mark Scheme
                    </a>
                  </div>
                </div>
              </div>
            </div>""")

        grid_html = "\n".join(topic_cards)
        
        sections_html += f"""
        <section class="hub-domain-section" id="{cat_key}">
          <div class="hub-domain-header">
            <div class="domain-icon-circle"><i class="fa-solid {cat_info['icon']}"></i></div>
            <div>
              <h2 class="domain-title">{cat_info['title']}</h2>
              <div class="domain-count">{len(topics_list)} Core Curriculum Topics</div>
            </div>
          </div>
          <div class="hub-topics-grid">
            {grid_html}
          </div>
        </section>
"""

    hub_html = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Worksheets Directory: Fluency Workouts &amp; Exam Practice | Master Functional Skills</title>
  <meta name="description" content="Complete directory of free Functional Skills worksheets for Maths (Level 1 &amp; Level 2), English, and Digital Skills. Every topic features 2 distinct worksheet styles: high-repetition skill workouts and authentic Pearson Edexcel exam practice booklets.">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="assets/css/mfs-revision.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <style>
    .hub-hero {{
      background: radial-gradient(circle at 50% 28%, rgba(37, 99, 235, 0.3) 0%, transparent 70%),
                  linear-gradient(135deg, #070d1e 0%, #0d1e48 50%, #1e3a8a 100%);
      color: #ffffff;
      padding: 60px 20px 50px 20px;
      text-align: center;
      position: relative;
    }}
    .hub-hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 18px;
    }}
    .hub-hero-title-box {{
      display: inline-block;
      margin: 0 auto 16px auto;
      padding: 12px 28px;
      background: rgba(7, 13, 30, 0.72);
      border: 2px solid rgba(96, 165, 250, 0.55);
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 0 25px rgba(59, 130, 246, 0.25);
      backdrop-filter: blur(10px);
      max-width: 95%;
    }}
    .hub-hero h1,
    .hub-hero-title {{
      font-size: clamp(1.85rem, 3.8vw, 2.85rem) !important;
      font-weight: 900 !important;
      line-height: 1.2 !important;
      margin: 0 !important;
      color: #ffffff !important;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
      letter-spacing: -0.02em;
    }}
    .hub-title-accent {{
      color: #38bdf8 !important;
      background: linear-gradient(135deg, #93c5fd 0%, #38bdf8 50%, #60a5fa 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline;
    }}
    body.dyslexia-mode .hub-hero h1,
    html[data-dyslexia="true"] body .hub-hero h1 {{
      color: #ffffff !important;
    }}
    .hub-hero p {{
      font-size: 1.1rem;
      color: #bfdbfe;
      max-width: 780px;
      margin: 0 auto 30px auto;
      line-height: 1.6;
    }}
    .hub-search-box {{
      max-width: 600px;
      margin: 0 auto;
      position: relative;
    }}
    .hub-search-box input {{
      width: 100%;
      padding: 16px 20px 16px 50px;
      border-radius: 50px;
      border: 2px solid #3b82f6;
      font-size: 1.05rem;
      outline: none;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }}
    .hub-search-icon {{
      position: absolute;
      left: 20px;
      top: 50%;
      transform: translateY(-50%);
      color: #3b82f6;
      font-size: 1.2rem;
    }}
    
    /* 2 Styles Explainer Box */
    .styles-explainer {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 28px 36px;
      margin: -25px auto 40px auto;
      max-width: 1050px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.06);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 30px;
      position: relative;
      z-index: 10;
    }}
    @media (max-width: 768px) {{
      .styles-explainer {{
        grid-template-columns: 1fr;
        padding: 20px;
        margin-top: 15px;
      }}
    }}
    .explainer-col {{
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }}
    .explainer-icon {{
      width: 48px;
      height: 48px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      flex-shrink: 0;
    }}
    .icon-workout-bg {{ background: #eff6ff; color: #2563eb; }}
    .icon-exam-bg {{ background: #f5f3ff; color: #7c3aed; }}
    .explainer-text h4 {{
      font-size: 1.08rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 6px;
    }}
    .explainer-text p {{
      font-size: 0.92rem;
      color: #64748b;
      line-height: 1.5;
      margin: 0;
    }}

    /* Domain Section */
    .hub-domain-section {{
      max-width: 1100px;
      margin: 0 auto 50px auto;
      padding: 0 20px;
    }}
    .hub-domain-header {{
      display: flex;
      align-items: center;
      gap: 16px;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 14px;
      margin-bottom: 24px;
    }}
    .domain-icon-circle {{
      width: 46px;
      height: 46px;
      background: #0f172a;
      color: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
    }}
    .domain-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #0f172a;
      margin: 0;
    }}
    .domain-count {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #64748b;
    }}

    /* Topics Grid */
    .hub-topics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 20px;
    }}
    .hub-topic-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .hub-topic-card:hover {{
      border-color: #3b82f6;
      box-shadow: 0 8px 18px rgba(0,0,0,0.08);
      transform: translateY(-2px);
    }}
    .hub-topic-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
    }}
    .hub-topic-title {{
      font-size: 1.12rem;
      font-weight: 800;
      margin: 0 0 6px 0;
      line-height: 1.25;
    }}
    .hub-topic-title a {{
      color: #0f172a;
      text-decoration: none;
    }}
    .hub-topic-title a:hover {{
      color: #2563eb;
      text-decoration: underline;
    }}
    .hub-topic-badges {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .hub-badge-level {{
      font-size: 0.72rem;
      font-weight: 800;
      background: #eff6ff;
      color: #1e40af;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid #bfdbfe;
    }}
    .hub-badge-spec {{
      font-size: 0.72rem;
      font-weight: 700;
      color: #64748b;
    }}
    .hub-btn-guide {{
      font-size: 0.78rem;
      font-weight: 700;
      color: #475569;
      background: #f1f5f9;
      padding: 4px 9px;
      border-radius: 6px;
      text-decoration: none;
      white-space: nowrap;
      border: 1px solid #cbd5e1;
    }}
    .hub-btn-guide:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    /* Action Rows */
    .hub-action-row {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding-top: 14px;
      border-top: 1px solid #f1f5f9;
    }}
    .hub-style-group {{
      background: #f8fafc;
      border-radius: 8px;
      padding: 10px 12px;
      border: 1px solid #e2e8f0;
    }}
    .hub-style-label {{
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #475569;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .text-blue {{ color: #2563eb; }}
    .text-purple {{ color: #7c3aed; }}
    .hub-btn-pair {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 8px;
    }}
    .hub-btn {{
      padding: 7px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: background 0.15s ease;
    }}
    .btn-workout {{
      background: #2563eb;
      color: #ffffff;
    }}
    .btn-workout:hover {{
      background: #1d4ed8;
    }}
    .btn-practice {{
      background: #7c3aed;
      color: #ffffff;
    }}
    .btn-practice:hover {{
      background: #6d28d9;
    }}
    .btn-ans {{
      background: #059669;
      color: #ffffff;
    }}
    .btn-ans:hover {{
      background: #047857;
    }}

    /* ==========================================================================
       TOOLBAR: VIEW TOGGLE & DOMAIN NAVIGATION
       ========================================================================== */
    .hub-toolbar-container {{
      max-width: 1100px;
      margin: -10px auto 30px auto;
      padding: 0 20px;
      position: relative;
      z-index: 10;
    }}
    .hub-toolbar {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 4px 16px rgba(7, 13, 30, 0.04);
      flex-wrap: wrap;
    }}
    .hub-toolbar-left {{
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }}
    .hub-stats-badge {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-size: 0.86rem;
      font-weight: 700;
      color: #0f172a;
      background: #f1f5f9;
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1px solid #cbd5e1;
      white-space: nowrap;
    }}
    .hub-stats-badge i {{
      color: #2563eb;
    }}
    .hub-domain-pills {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .hub-domain-pill {{
      font-size: 0.76rem;
      font-weight: 700;
      color: #475569;
      background: #f8fafc;
      padding: 5px 11px;
      border-radius: 9999px;
      border: 1px solid #e2e8f0;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .hub-domain-pill:hover {{
      background: #eff6ff;
      border-color: #93c5fd;
      color: #1d4ed8;
      transform: translateY(-1px);
    }}
    .hub-toolbar-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .view-toggle-wrapper {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .view-toggle-caption {{
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #64748b;
    }}
    .view-toggle-pills {{
      display: inline-flex;
      background: #0f172a;
      padding: 3px;
      border-radius: 10px;
      border: 1px solid #1e293b;
      gap: 3px;
    }}
    .view-pill-btn {{
      padding: 6px 14px;
      border: none;
      background: transparent;
      color: #94a3b8;
      font-size: 0.82rem;
      font-weight: 700;
      border-radius: 7px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-family: inherit;
      user-select: none;
    }}
    .view-pill-btn:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }}
    .view-pill-btn.active {{
      background: #2563eb;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.45);
    }}
    .view-pill-btn i {{
      font-size: 0.88rem;
    }}

    /* ==========================================================================
       SUB-NAV STRIP (Direct Revision Hubs)
       ========================================================================== */
    .mfs-subnav-strip {{
      background: #0b152d;
      border-bottom: 1px solid #1e293b;
      padding: 9px 0;
    }}
    .mfs-subnav-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .subnav-title {{
      font-size: 0.8rem;
      font-weight: 800;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }}
    .subnav-links {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .subnav-link {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #f1f5f9;
      text-decoration: none;
      padding: 5px 13px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.14);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .subnav-link:hover {{
      background: #2563eb;
      color: #ffffff;
      border-color: #3b82f6;
      transform: translateY(-1px);
    }}
    .subnav-link.subnav-highlight {{
      background: #2563eb;
      border-color: #3b82f6;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.35);
    }}
    .subnav-link.subnav-highlight:hover {{
      background: #1d4ed8;
    }}

    /* ==========================================================================
       LIST VIEW STYLES (Refined & Modernized)
       ========================================================================== */
    .view-list .hub-topics-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .view-list .hub-topic-card {{
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      padding: 16px 24px;
      gap: 20px;
      border-radius: 12px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #2563eb;
      box-shadow: 0 2px 6px rgba(7, 13, 30, 0.03);
      transition: all 0.2s ease;
    }}
    #maths-number .view-list .hub-topic-card,
    .view-list #maths-number .hub-topic-card {{
      border-left-color: #2563eb;
    }}
    #maths-measures .view-list .hub-topic-card,
    .view-list #maths-measures .hub-topic-card {{
      border-left-color: #0284c7;
    }}
    #maths-data .view-list .hub-topic-card,
    .view-list #maths-data .hub-topic-card {{
      border-left-color: #059669;
    }}
    #english-reading .view-list .hub-topic-card,
    .view-list #english-reading .hub-topic-card {{
      border-left-color: #d97706;
    }}
    #english-writing .view-list .hub-topic-card,
    .view-list #english-writing .hub-topic-card {{
      border-left-color: #7c3aed;
    }}
    #english-slc .view-list .hub-topic-card,
    .view-list #english-slc .hub-topic-card {{
      border-left-color: #e11d48;
    }}
    #digital-skills .view-list .hub-topic-card,
    .view-list #digital-skills .hub-topic-card {{
      border-left-color: #0d9488;
    }}
    .view-list .hub-topic-card:hover {{
      border-color: #93c5fd;
      border-left-color: #1d4ed8;
      box-shadow: 0 8px 20px rgba(37, 99, 235, 0.1);
      transform: translateY(-2px);
    }}
    .view-list .hub-topic-header {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 0;
      flex: 1 1 360px;
      min-width: 240px;
    }}
    .view-list .hub-topic-title {{
      font-size: 1.15rem;
      font-weight: 800;
      margin: 0;
      line-height: 1.3;
      white-space: normal;
    }}
    .view-list .hub-topic-title a {{
      color: #0f172a;
      text-decoration: none;
      transition: color 0.15s ease;
    }}
    .view-list .hub-topic-title a:hover {{
      color: #2563eb;
      text-decoration: underline;
    }}
    .view-list .hub-topic-badges {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .view-list .hub-badge-level {{
      font-size: 0.74rem;
      font-weight: 800;
      background: #eff6ff;
      color: #1e40af;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #bfdbfe;
    }}
    .view-list .hub-badge-spec {{
      font-size: 0.74rem;
      font-weight: 700;
      color: #64748b;
    }}
    .view-list .hub-btn-guide {{
      font-size: 0.76rem;
      font-weight: 700;
      color: #475569;
      background: #f1f5f9;
      padding: 3px 9px;
      border-radius: 5px;
      text-decoration: none;
      white-space: nowrap;
      border: 1px solid #cbd5e1;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
    }}
    .view-list .hub-btn-guide:hover {{
      background: #e2e8f0;
      color: #0f172a;
      border-color: #94a3b8;
    }}
    .view-list .hub-action-row {{
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 12px;
      padding-top: 0;
      border-top: none;
      flex-shrink: 0;
    }}
    .view-list .hub-style-group {{
      border-radius: 10px;
      padding: 7px 12px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 6px;
      border: 1px solid #e2e8f0;
      background: #f8fafc;
      flex-shrink: 0;
      transition: all 0.15s ease;
    }}
    .view-list .hub-style-group.style-workout {{
      background: #f0f7ff;
      border-color: #dbeafe;
    }}
    .view-list .hub-style-group.style-exam {{
      background: #faf5ff;
      border-color: #f3e8ff;
    }}
    .view-list .hub-style-label {{
      margin-bottom: 0;
      font-size: 0.69rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}
    .view-list .hub-btn-pair {{
      display: flex;
      gap: 6px;
    }}
    .view-list .hub-btn {{
      padding: 6px 11px;
      font-size: 0.79rem;
      font-weight: 700;
      border-radius: 6px;
      white-space: nowrap;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
      text-decoration: none;
    }}

    /* Responsive adjustments for List View and Toolbar */
    @media (max-width: 1120px) {{
      .view-list .hub-topic-card {{
        flex-direction: column;
        align-items: stretch;
        gap: 14px;
        padding: 16px 20px;
      }}
      .view-list .hub-action-row {{
        flex-direction: row;
        width: 100%;
      }}
      .view-list .hub-style-group {{
        flex: 1 1 50%;
        justify-content: space-between;
      }}
    }}

    @media (max-width: 768px) {{
      .hub-toolbar {{
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        padding: 12px;
      }}
      .hub-toolbar-left {{
        justify-content: space-between;
      }}
      .hub-domain-pills {{
        display: none;
      }}
      .hub-toolbar-right {{
        justify-content: space-between;
        width: 100%;
      }}
      .view-toggle-wrapper {{
        width: 100%;
        justify-content: space-between;
      }}
      .view-toggle-pills {{
        flex: 1;
        justify-content: center;
      }}
      .view-pill-btn {{
        flex: 1;
        justify-content: center;
      }}
      .mfs-subnav-inner {{
        flex-direction: column;
        align-items: flex-start;
      }}
      .subnav-links {{
        width: 100%;
        overflow-x: auto;
        padding-bottom: 4px;
        flex-wrap: nowrap;
      }}
      .subnav-link {{
        flex-shrink: 0;
      }}
      .view-list .hub-action-row {{
        flex-direction: column;
        align-items: stretch;
      }}
      .view-list .hub-style-group {{
        flex: 1 1 100%;
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
      }}
      .view-list .hub-btn-pair {{
        display: grid;
        grid-template-columns: 2fr 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- TOP TRUST BAR WITH ACCESSIBILITY & CONTACT (Standard Site Header) -->
  <div class="mfs-top-bar">
    <div class="mfs-container mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel &amp; City &amp; Guilds Aligned</span>
      </div>
      <div class="top-contacts">
        <div class="mfs-access-bar">
          <!-- DYSLEXIA BACKGROUND TINT PICKER -->
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
          <button id="dyslexiaToggle" class="btn-dyslexia-toggle" onclick="toggleDyslexiaMode()" title="Toggle Dyslexia High-Readability Mode">
            <i class="fa-solid fa-universal-access"></i> Dyslexia
          </button>
          <button id="themeToggle" class="mfs-theme-pill" onclick="toggleTheme()" title="Switch Palette: Sapphire vs Emerald">
            <i class="fa-solid fa-palette"></i> <span id="themeLabel">Sapphire</span>
          </button>
        </div>
        <a href="contact-us.html" class="top-contact-link"><i class="fa-solid fa-envelope"></i> <strong>Contact Us</strong></a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION (Standard Site Navbar) -->
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
          <!-- 1. SUBJECTS (VISUAL MEGA-MENU) -->
          <li class="mfs-nav-item">
            <a href="courses.html" class="mfs-nav-link">
              <i class="fa-solid fa-book-open-reader" style="color:#0284c7; margin-right:5px;"></i> Subjects <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i>
            </a>
            <div class="mfs-dropdown-menu mfs-dropdown-revision-hub">
              <div class="mfs-revision-grid">
                <!-- Maths Column -->
                <div class="mfs-revision-col mfs-revision-col-maths">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-calculator"></i> Maths Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-maths-level-2.html" class="mfs-dropdown-item">Maths Level 2</a>
                    <a href="functional-skills-maths-level-1.html" class="mfs-dropdown-item">Maths Level 1</a>
                    <a href="entry-level-3-maths.html" class="mfs-dropdown-item">Entry Level 3 Maths</a>
                  </div>
                </div>
                <!-- English Column -->
                <div class="mfs-revision-col mfs-revision-col-english">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-pen-nib"></i> English Revision</div>
                  <div class="mfs-revision-col-links">
                    <a href="functional-skills-english-level-2.html" class="mfs-dropdown-item">English Level 2</a>
                    <a href="functional-skills-english-level-1.html" class="mfs-dropdown-item">English Level 1</a>
                  </div>
                </div>
                <!-- Digital Skills Column -->
                <div class="mfs-revision-col mfs-revision-col-digital">
                  <div class="mfs-revision-col-title"><i class="fa-solid fa-laptop-code"></i> Digital Skills</div>
                  <div class="mfs-revision-col-links">
                    <a href="digital-functional-skills.html" class="mfs-dropdown-item">Digital Skills Hub</a>
                    <a href="digital-functional-skills-mock-exam.html" class="mfs-dropdown-item">Pearson Mock Exam</a>
                    <a href="digital-functional-skills-past-papers.html" class="mfs-dropdown-item">Past Papers &amp; Files</a>
                  </div>
                </div>
              </div>
            </div>
          </li>

          <!-- 2. PAST PAPERS (DIRECT ACCESS) -->
          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link">
              <i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers
            </a>
          </li>

          <!-- 2b. WORKSHEETS DIRECTORY (CORBETT STYLE DUAL ENGINE) -->
          <li class="mfs-nav-item">
            <a href="worksheets.html" class="mfs-nav-link active" style="color:#2563eb; font-weight:800;">
              <i class="fa-solid fa-layer-group" style="color:#2563eb; margin-right:5px;"></i> Worksheets
            </a>
          </li>

          <!-- 3. FREE TOOLS (COMPACT DROPDOWN) -->
          <li class="mfs-nav-item">
            <a href="tools.html" class="mfs-nav-link">
              <i class="fa-solid fa-screwdriver-wrench" style="color:#0284c7; margin-right:5px;"></i> Free Tools <i class="fa-solid fa-chevron-down" style="font-size:0.72rem; margin-left:3px;"></i>
            </a>
            <div class="mfs-dropdown-menu mfs-dropdown-compact">
              <a href="tools.html" class="mfs-dropdown-item" style="font-weight:700; color:var(--accent);"><i class="fa-solid fa-layer-group" style="font-size:0.85rem; margin-right:6px;"></i> All Free Tools &amp; Simulators &rarr;</a>
              <div class="mfs-dropdown-divider" style="margin:4px 0; border-top:1px solid #e2e8f0;"></div>
              <a href="pass-mark-calculator.html" class="mfs-dropdown-item"><i class="fa-solid fa-calculator" style="color:var(--accent); font-size:0.85rem; margin-right:6px;"></i> Pass Mark Calculator</a>
              <a href="diagnostic-test.html" class="mfs-dropdown-item"><i class="fa-solid fa-chart-pie" style="color:#059669; font-size:0.85rem; margin-right:6px;"></i> Diagnostic Skill Checker</a>
              <a href="functional-skills-nets.html" class="mfs-dropdown-item"><i class="fa-solid fa-cube" style="color:#0284c7; font-size:0.85rem; margin-right:6px;"></i> 3D Net Folding Tool</a>
            </div>
          </li>

          <!-- 4. REVISION CARDS -->
          <li class="mfs-nav-item">
            <a href="revision-cards.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#d97706; font-weight:700;">
              <i class="fa-solid fa-layer-group" style="color:#d97706; margin-right:5px;"></i> Revision Cards
            </a>
          </li>

          <!-- 5. SHOP -->
          <li class="mfs-nav-item">
            <a href="shop.html" class="mfs-nav-link mfs-nav-link-amber" style="color:#d97706; font-weight:700;">
              <i class="fa-solid fa-basket-shopping" style="color:#d97706; margin-right:5px;"></i> Shop
            </a>
          </li>
        </ul>
      </nav>

      <!-- 6. BOOK EXAM ACTION BUTTON -->
      <div class="mfs-nav-actions">
        <a href="exams.html" class="btn-nav-exam">
          <i class="fa-solid fa-calendar-check"></i> Book Exam
        </a>
      </div>
    </div>
  </header>

  <!-- DIRECT REVISION HUBS SUB-NAV (Moved below menu bar) -->
  <div class="mfs-subnav-strip">
    <div class="revision-page-wrapper mfs-subnav-inner" style="max-width:1100px;margin:0 auto;padding:0 20px;">
      <div class="subnav-title"><i class="fa-solid fa-compass"></i> Direct Revision Hubs:</div>
      <div class="subnav-links">
        <a href="functional-skills-maths-level-2.html" class="subnav-link"><i class="fa-solid fa-calculator"></i> Maths L2</a>
        <a href="functional-skills-maths-level-1.html" class="subnav-link"><i class="fa-solid fa-calculator"></i> Maths L1</a>
        <a href="functional-skills-english-level-2.html" class="subnav-link"><i class="fa-solid fa-pen-nib"></i> English L2</a>
        <a href="functional-skills-past-papers.html" class="subnav-link subnav-highlight"><i class="fa-solid fa-file-pdf"></i> Past Papers</a>
      </div>
    </div>
  </div>

  <!-- HERO -->
  <section class="hub-hero">
    <div class="hub-hero-title-box">
      <h1 class="hub-hero-title">The Functional Skills <span class="hub-title-accent">Worksheets Directory</span></h1>
    </div>
    <p>Over 100 curriculum topics across Maths (Level 1 &amp; Level 2), English, and Digital Skills. Every single topic provides two distinct worksheet styles designed for procedural mastery and exam success.</p>
    
    <div class="hub-search-box">
      <i class="fa-solid fa-magnifying-glass hub-search-icon"></i>
      <input type="text" id="topicSearchInput" placeholder="Search topics (e.g. percentages, ratio, area, probability)..." onkeyup="filterTopics()">
    </div>
  </section>

  <!-- 2 STYLES EXPLAINER -->
  <div class="styles-explainer">
    <div class="explainer-col">
      <div class="explainer-icon icon-workout-bg"><i class="fa-solid fa-repeat"></i></div>
      <div class="explainer-text">
        <h4>Style 1: Skill Workout (Repetition &amp; Fluency)</h4>
        <p>Over 25 rapid calculation drills (a–h) with systematic number variation to eliminate hesitation, followed by realistic adult vocational applications.</p>
      </div>
    </div>
    <div class="explainer-col">
      <div class="explainer-icon icon-exam-bg"><i class="fa-solid fa-file-shield"></i></div>
      <div class="explainer-text">
        <h4>Style 2: Exam Practice Booklet (Pearson Reformed)</h4>
        <p>Authentic Pearson Edexcel exam questions with official [M1][A1] mark scheme allocations, working boxes, and reverse calculation checks.</p>
      </div>
    </div>
  </div>

  <!-- TOOLBAR: VIEW TOGGLE & DOMAIN NAVIGATION -->
  <div class="hub-toolbar-container">
    <div class="hub-toolbar">
      <div class="hub-toolbar-left">
        <div class="hub-stats-badge">
          <i class="fa-solid fa-layer-group"></i>
          <span><strong id="visibleTopicsCount">120</strong> Topics Available</span>
        </div>
        <div class="hub-domain-pills" role="navigation" aria-label="Jump to Subject Domain">
          <a href="#maths-number" class="hub-domain-pill"><i class="fa-solid fa-calculator"></i> Number</a>
          <a href="#maths-measures" class="hub-domain-pill"><i class="fa-solid fa-ruler-combined"></i> Measures</a>
          <a href="#maths-data" class="hub-domain-pill"><i class="fa-solid fa-chart-column"></i> Data</a>
          <a href="#english-reading" class="hub-domain-pill"><i class="fa-solid fa-book-open-reader"></i> Reading</a>
          <a href="#english-writing" class="hub-domain-pill"><i class="fa-solid fa-pen-nib"></i> Writing</a>
          <a href="#english-slc" class="hub-domain-pill"><i class="fa-solid fa-comments"></i> Speaking (SLC)</a>
          <a href="#digital-skills" class="hub-domain-pill"><i class="fa-solid fa-laptop-code"></i> Digital</a>
        </div>
      </div>

      <div class="hub-toolbar-right">
        <div class="view-toggle-wrapper">
          <span class="view-toggle-caption">View:</span>
          <div class="view-toggle-pills" role="group" aria-label="Worksheet layout options">
            <button type="button" id="btnViewTile" class="view-pill-btn active" onclick="setViewMode('tile')" title="Tile / Grid View">
              <i class="fa-solid fa-table-cells-large"></i> <span>Tile View</span>
            </button>
            <button type="button" id="btnViewList" class="view-pill-btn" onclick="setViewMode('list')" title="List / Compact Row View">
              <i class="fa-solid fa-list"></i> <span>List View</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- DIRECTORY SECTIONS -->
  <main id="directoryContent">
    {sections_html}
  </main>

  <footer class="mfs-footer" style="background:#070d1e;color:#94a3b8;padding:40px 20px;text-align:center;font-size:0.9rem;margin-top:60px;">
    <p>&copy; Master Functional Skills &bull; masterfunctionalskills.co.uk &bull; Pearson Edexcel &amp; City &amp; Guilds Aligned</p>
  </footer>

  <script>
    function setViewMode(mode) {{
      const dirContent = document.getElementById('directoryContent');
      const btnTile = document.getElementById('btnViewTile');
      const btnList = document.getElementById('btnViewList');
      
      if (!dirContent || !btnTile || !btnList) return;

      if (mode === 'list') {{
        dirContent.classList.add('view-list');
        btnList.classList.add('active');
        btnTile.classList.remove('active');
        try {{ localStorage.setItem('mfs_worksheets_view', 'list'); }} catch(e){{}}
      }} else {{
        dirContent.classList.remove('view-list');
        btnTile.classList.add('active');
        btnList.classList.remove('active');
        try {{ localStorage.setItem('mfs_worksheets_view', 'tile'); }} catch(e){{}}
      }}
    }}

    // Initialize saved view mode on load
    (function initViewMode() {{
      try {{
        const saved = localStorage.getItem('mfs_worksheets_view');
        if (saved === 'list') {{
          setViewMode('list');
        }} else {{
          setViewMode('tile');
        }}
      }} catch(e) {{
        setViewMode('tile');
      }}
    }})();

    function filterTopics() {{
      const input = document.getElementById('topicSearchInput');
      const query = input ? input.value.toLowerCase().trim() : '';
      const cards = document.querySelectorAll('.hub-topic-card');
      let visibleCount = 0;
      
      cards.forEach(card => {{
        const topicName = card.getAttribute('data-topic-name') || '';
        if (!query || topicName.includes(query)) {{
          card.style.display = '';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      const countEl = document.getElementById('visibleTopicsCount');
      if (countEl) {{
        countEl.textContent = visibleCount;
      }}

      // Hide domain sections if all their cards are hidden
      const sections = document.querySelectorAll('.hub-domain-section');
      sections.forEach(section => {{
        const sectionCards = section.querySelectorAll('.hub-topic-card');
        let sectionHasVisible = false;
        sectionCards.forEach(c => {{
          if (c.style.display !== 'none') sectionHasVisible = true;
        }});
        section.style.display = sectionHasVisible ? '' : 'none';
      }});
    }}
  </script>
  <script src="assets/js/mfs-revision.js"></script>
</body>
</html>
"""
    
    hub_path = os.path.join(BASE_DIR, "worksheets.html")
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(hub_html)
    print(f"✅ Created master worksheets directory at {hub_path}")

def update_topic_pages_with_dual_downloads():
    print("Updating all topic revision pages to feature dual worksheet download cards...")
    curriculum_pages = c_final.curriculum_pages
    updated_count = 0
    
    for cat, slug, bn, fpath in curriculum_pages:
        workout_file = f"worksheets/{slug}-workout.html"
        workout_ans_file = f"worksheets/{slug}-workout-answers.html"
        sheet_file = f"worksheets/{slug}-worksheet.html"
        ans_file = f"worksheets/{slug}-answers.html"
        
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        if 'id="downloads"' in content:
            clean_title = slug.replace('reading-', '').replace('writing-', '').replace('slc-', '').replace('functional-skills-', '').replace('-', ' ').title()
            
            if slug.startswith(('reading-', 'writing-', 'slc-')):
                rep_title = f"{clean_title} Practice Drills (PDF)"
                rep_desc = "Over 25 targeted practice questions + real-life workplace tasks to build confidence"
            elif slug.startswith(('digital-', 'dfs-')):
                rep_title = f"{clean_title} Practice Tasks (PDF)"
                rep_desc = "Over 25 practical tasks + workplace drills to build confidence"
            else:
                rep_title = f"{clean_title} Practice Drills (PDF)"
                rep_desc = "Over 25 quick calculation drills + real-life maths problems to build confidence"

            # Pattern matching download tiles grid
            downloads_pattern = re.compile(
                r'(<section id="downloads"[\s\S]*?<div class="download-tiles-grid[^"]*">)[\s\S]*?(<\/div>\s*<\/section>)',
                re.IGNORECASE
            )
            
            new_tiles = f"""\\1
            <!-- STYLE 1: SKILL WORKOUT -->
            <a href="{workout_file}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-workout"><i class="fa-solid fa-repeat"></i></div>
              <div class="download-tile-info">
                <div class="tile-badge-wrap"><span class="badge-tile-type">Style 1: Skill Workout</span></div>
                <strong>{rep_title}</strong>
                <span>{rep_desc}</span>
              </div>
            </a>

            <a href="{workout_ans_file}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers"><i class="fa-solid fa-check-double"></i></div>
              <div class="download-tile-info">
                <div class="tile-badge-wrap"><span class="badge-tile-type ans">Workout Answers</span></div>
                <strong>Skill Workout Answer Key (PDF)</strong>
                <span>Quick-check marking grid + worked solutions for everyday applications</span>
              </div>
            </a>

            <!-- STYLE 2: EXAM PRACTICE BOOKLET -->
            <a href="{sheet_file}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-pdf"><i class="fa-regular fa-file-pdf"></i></div>
              <div class="download-tile-info">
                <div class="tile-badge-wrap"><span class="badge-tile-type exam">Style 2: Exam Booklet</span></div>
                <strong>{clean_title} Exam Practice Booklet (PDF)</strong>
                <span>Authentic Pearson Edexcel exam questions with official [M1][A1] mark allocations</span>
              </div>
            </a>

            <a href="{ans_file}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers"><i class="fa-solid fa-award"></i></div>
              <div class="download-tile-info">
                <div class="tile-badge-wrap"><span class="badge-tile-type ans">Exam Mark Scheme</span></div>
                <strong>Step-by-Step Exam Mark Scheme (PDF)</strong>
                <span>Official tutor model answers with step-by-step methods, common mistakes to avoid, and quick checks</span>
              </div>
            </a>
          \\2"""
            
            content = downloads_pattern.sub(new_tiles, content)
            
            if content != original_content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                updated_count += 1

    print(f"✅ Updated {updated_count} topic pages with the Dual-Format 4-Card download grid!")

if __name__ == "__main__":
    generate_worksheets_hub()
    update_topic_pages_with_dual_downloads()
