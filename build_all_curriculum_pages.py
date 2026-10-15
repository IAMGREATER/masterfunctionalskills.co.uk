#!/usr/bin/env python3
"""
Master Functional Skills - Universal Modernization Engine
Builds/rebuilds all topic revision pages to the gold-standard dyslexia-friendly layout:
- 1720px / 98% wide container pushing contents far left
- Sticky 210px Table of Contents sidebar
- Cyan-bordered PassFunctionalSkills style cards (.mfs-topic-card)
- Two-tone headings (<span class="mfs-topic-prefix">Example X:</span> Title)
- Big bold numbers and formulas (chips / monospaced boxes)
- Subject-tailored Golden Rules (Maths, Reading, Writing, Digital)
- Pearson Edexcel Worked Exam Models with mark breakdown
- Examiner Traps & Common Pitfalls
- Interactive Practice Questions with Auto-saving Scratchpads & Solution Drawers
- Official Favicon in head
- Dyslexia Tint Selector & Theme Switcher
"""

import os, sys, re, glob
import lxml.html
from lxml import html, etree
import visual_curriculum_catalog as vcc

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
TOPICS_DIR = os.path.join(PROJECT_DIR, "topics")

# Topics to never overwrite (already perfected and verified)
PRESERVED_FILES = {
    "functional-skills-area.html",
    "functional-skills-ordering-numbers.html",
    "functional-skills-perimeter.html",
    "functional-skills-money.html",
    "functional-skills-volume.html",
    "functional-skills-percentages.html",
    "functional-skills-nets.html"
}

CURRICULUM_MATHS = [
    ("functional-skills-numbers-and-place-value.html", "Numbers & Place Value"),
    ("functional-skills-ordering-numbers.html", "Ordering Numbers"),
    ("functional-skills-addition-and-subtraction.html", "Addition & Subtraction"),
    ("functional-skills-multiplication.html", "Multiplication"),
    ("functional-skills-division.html", "Division"),
    ("functional-skills-bidmas.html", "BIDMAS / Order of Operations"),
    ("functional-skills-rounding-and-estimating.html", "Rounding & Estimating"),
    ("functional-skills-fractions.html", "Fractions"),
    ("functional-skills-decimals.html", "Decimals"),
    ("functional-skills-percentages.html", "Percentages"),
    ("functional-skills-fractions-decimals-and-percentages.html", "FDP Conversions"),
    ("functional-skills-ratio.html", "Ratio & Proportion"),
    ("functional-skills-proportion.html", "Direct & Inverse Proportion"),
    ("functional-skills-formulas.html", "Algebra & Formulas"),
    ("functional-skills-money.html", "Money & Finance"),
    ("functional-skills-best-buys.html", "Best Buys & Unit Pricing"),
    ("functional-skills-interest-and-compound-interest.html", "Simple & Compound Interest"),
    ("functional-skills-time.html", "Time & Timetables"),
    ("functional-skills-speed.html", "Speed, Distance & Time"),
    ("functional-skills-density.html", "Density & Compound Units"),
    ("functional-skills-unit-conversions.html", "Unit Conversions"),
    ("functional-skills-length.html", "Length & Dimensions"),
    ("functional-skills-weight.html", "Weight & Mass"),
    ("functional-skills-capacity.html", "Capacity & Volume Units"),
    ("functional-skills-perimeter.html", "Perimeter"),
    ("functional-skills-area.html", "Area"),
    ("functional-skills-volume.html", "Volume"),
    ("functional-skills-surface-area.html", "Surface Area"),
    ("functional-skills-2d-shapes.html", "2D Shapes"),
    ("functional-skills-3d-shapes.html", "3D Shapes"),
    ("functional-skills-nets.html", "Nets of 3D Shapes"),
    ("functional-skills-plans-and-elevations.html", "Plans & Elevations"),
    ("functional-skills-angles.html", "Angles & Bearings"),
    ("functional-skills-angles-in-2d-shapes.html", "Angles in Polygons"),
    ("functional-skills-circles.html", "Circles & Circumference"),
    ("functional-skills-coordinates.html", "Coordinates"),
    ("functional-skills-maps-and-scale-drawings.html", "Maps & Scale Drawings"),
    ("functional-skills-mean-median-mode-and-range.html", "Averages (Mean, Median, Mode, Range)"),
    ("functional-skills-estimating-the-mean.html", "Estimating the Mean"),
    ("functional-skills-grouped-data.html", "Grouped Frequency Tables"),
    ("functional-skills-data-tables.html", "Data Tables"),
    ("functional-skills-bar-charts.html", "Bar Charts"),
    ("functional-skills-line-graphs.html", "Line Graphs"),
    ("functional-skills-pie-charts.html", "Pie Charts"),
    ("functional-skills-scatter-graphs.html", "Scatter Graphs & Correlation"),
    ("functional-skills-conversion-graphs.html", "Conversion Graphs"),
    ("functional-skills-probability.html", "Probability"),
    ("functional-skills-probability-tables.html", "Probability Outcomes & Tables")
]

CURRICULUM_ENGLISH = [
    ("reading-fact-or-opinion.html", "Fact or Opinion"),
    ("reading-meaning.html", "Words in Context & Meaning"),
    ("reading-specialist-words.html", "Specialist Vocabulary"),
    ("reading-presentational-features.html", "Presentational Features"),
    ("reading-investigating-layout.html", "Layout Devices"),
    ("reading-investigating-image.html", "Images & Visual Effects"),
    ("reading-language-features.html", "Language Techniques"),
    ("reading-point-of-view-and-line-of-argument.html", "Point of View & Bias"),
    ("reading-styles-of-writing-and-voice.html", "Tone, Style & Voice"),
    ("reading-text-types.html", "Text Types & Purpose"),
    ("reading-comparing-texts.html", "Comparing Texts"),
    ("reading-why-do-writers-write.html", "The Writer's Purpose"),
    ("reading-the-exam.html", "Reading Exam Strategy"),
    ("writing-planning-your-answer.html", "Planning Written Responses"),
    ("writing-communicating.html", "Communicating Clearly"),
    ("writing-context.html", "Context & Purpose"),
    ("writing-assessing-audience.html", "Audience & Register"),
    ("writing-form-presentational-and-language-features.html", "Format & Conventions"),
    ("writing-organisational-markers.html", "Organisational Markers"),
    ("writing-linking-up-your-answer.html", "Paragraphing & Cohesion"),
    ("writing-grammar.html", "Grammar & Sentence Structures"),
    ("writing-tenses.html", "Consistency of Tense"),
    ("writing-perfecting-your-punctuation.html", "Punctuation Mastery"),
    ("writing-spelling.html", "Spelling Rules & Strategies"),
    ("writing-fantastic-finalising.html", "Proofreading & Editing"),
    ("writing-why-are-you-writing.html", "Purpose in Writing"),
    ("writing-the-exam.html", "Writing Exam Strategy")
]

def get_next_topic(filename, is_english):
    curr = CURRICULUM_ENGLISH if is_english else CURRICULUM_MATHS
    for i, (fn, name) in enumerate(curr):
        if fn == filename:
            if i + 1 < len(curr):
                return curr[i + 1]
            return curr[0]
    return (curr[0][0], curr[0][1]) if curr else ("revise.html", "Revision Directory")

def clean_inner_html_safe(el):
    if el is None:
        return ""
    # remove mathml
    for m in el.xpath('.//*[contains(@class, "katex-mathml")]'):
        m.drop_tree()
    # clean katex html into clean spans
    for k in el.xpath('.//*[contains(@class, "katex")]'):
        txt = k.text_content().strip()
        txt = re.sub(r'\s+', ' ', txt)
        span = etree.Element('strong')
        span.set('style', "color:#0284c7; font-family:'Inter', system-ui, -apple-system, sans-serif; font-feature-settings:'tnum'; font-variant-numeric:tabular-nums; font-size:1.15rem; font-weight:800; padding:1px 4px; border-radius:4px; background:rgba(2,132,199,0.06);")
        span.text = txt
        k.addprevious(span)
        k.drop_tree()
    # clean scripts/styles/noscripts
    for bad in el.xpath('.//script | .//style | .//noscript'):
        bad.drop_tree()
    # clean old badges, adverts, and clutter
    for bad in el.xpath('.//*[contains(text(), "TQUKEdexcelCity") or contains(text(), "Follow Our Socials") or contains(text(), "Additional Resources") or contains(text(), "Speak to one of our experts") or contains(text(), "Revision Products")]'):
        bad.drop_tree()
    # clean images
    for img in el.xpath('.//img'):
        src = img.get('src', '')
        if src.startswith('../assets/'):
            src = src.replace('../assets/', 'assets/')
        elif src.startswith('/assets/'):
            src = src.lstrip('/')
        elif 'app/uploads/' in src:
            src = 'assets/img/pfs/' + os.path.basename(src.split('?')[0])
        img.set('src', src)
        for a in ['width', 'height', 'data-lazy-src', 'data-lazy-srcset', 'data-lazy-sizes', 'loading', 'decoding']:
            if img.get(a):
                del img.attrib[a]
        img.set('class', 'img-fluid')
        img.set('loading', 'lazy')
    return (el.text or "") + ''.join(etree.tostring(c, encoding='unicode', method='html') for c in el)

def get_subject_meta(filename):
    is_english = filename.startswith(('reading-', 'writing-', 'slc-', 'piecing-', 'types-of-', 'detecting-', 'formality-', 'assessing-the-basics', 'common-mistakes')) or 'english' in filename
    is_digital = 'digital' in filename
    
    if is_digital:
        subject = "Digital Skills"
        subject_pill_icon = "fa-laptop-code"
        subject_dir = "digital-functional-skills.html"
    elif is_english:
        subject = "English"
        subject_pill_icon = "fa-pen-nib"
        subject_dir = "functional-skills-english-level-2.html"
    else:
        subject = "Mathematics"
        subject_pill_icon = "fa-calculator"
        subject_dir = "functional-skills-maths-level-2.html"
        
    return is_english, is_digital, subject, subject_pill_icon, subject_dir

def get_golden_rules_html(subject, topic_clean):
    if "Mathematics" in subject:
        return f"""
        <!-- GOLDEN RULES -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for {topic_clean}</h2>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-pen-ruler"></i>
              <span>Golden Rule 1: Always Show Step-by-Step Working for Method Marks</span>
            </div>
            <p>
              In Pearson Edexcel and City &amp; Guilds exams, up to 75% of marks are awarded for your method (M marks). Even if your final arithmetic is inaccurate, showing every intermediate step ensures you capture all process marks.
            </p>
            <div class="rule-highlight-badge">
              Examiner Tip: Write each formula and intermediate calculation on a new line in the workspace.
            </div>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-arrows-rotate"></i>
              <span>Golden Rule 2: Check Your Units and Apply a Reverse Sensibility Check</span>
            </div>
            <p>
              Always check that your final units match the question specification (e.g. cm, m, m&sup2;, m&sup3;, %, £ or p). Perform an inverse calculation or round numbers to verify that your answer is realistic in a real-world scenario.
            </p>
            <div class="rule-highlight-badge">
              Check: Does your numerical answer make sense for the real-life situation described?
            </div>
          </div>
        </section>"""
    elif "Digital" in subject:
        return f"""
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
              Strong passwords must combine uppercase letters, lowercase letters, numbers, and symbols (minimum 12 characters). Never share multi-factor authentication (2FA) codes or click unsolicited verification links.
            </p>
            <div class="rule-highlight-badge">
              Examiner Tip: In exam tasks, identify sender email domain mismatches to detect phishing attempts.
            </div>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-table-cells"></i>
              <span>Golden Rule 2: Accurate Spreadsheet Formula Formatting</span>
            </div>
            <p>
              Always prefix formulas with an equals sign (=). Use standard range syntax (e.g. =SUM(B2:B12) or =AVERAGE(C2:C20)). Format monetary data with currency symbols (£) and set two decimal places.
            </p>
            <div class="rule-highlight-badge">
              Check: Ensure range references include all relevant data rows without including summary header lines.
            </div>
          </div>
        </section>"""
    elif filename_is_writing := any(k in topic_clean.lower() for k in ['writing', 'grammar', 'punctuation', 'spelling', 'audience', 'format', 'organisational', 'linking', 'tenses', 'finalising']):
        return f"""
        <!-- GOLDEN RULES -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Functional Skills Writing</h2>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-bullseye"></i>
              <span>Golden Rule 1: Tailor Format, Tone &amp; Register to the Audience</span>
            </div>
            <p>
              Examiners award significant marks for appropriate format conventions (e.g. formal salutations and sign-offs in letters, subject lines in emails, compelling headlines and subheadings in articles). Match your vocabulary to whether the context is formal (workplace/complaint) or informal (colleague/peer).
            </p>
            <div class="rule-highlight-badge">
              Examiner Tip: Plan 3 clear paragraphs with distinctive topic sentences before you start writing.
            </div>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-spell-check"></i>
              <span>Golden Rule 2: Proofread for SPaG (Spelling, Punctuation &amp; Grammar)</span>
            </div>
            <p>
              Avoid comma splices by using full stops or coordinating conjunctions. Maintain consistent tense throughout your response and ensure complex sentences have clear subordinate clauses.
            </p>
            <div class="rule-highlight-badge">
              Check: Re-read your final paragraph to catch missing apostrophes, capitalization errors, and run-on sentences.
            </div>
          </div>
        </section>"""
    else:
        return f"""
        <!-- GOLDEN RULES -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules for Functional Skills Reading</h2>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-magnifying-glass"></i>
              <span>Golden Rule 1: Differentiate Objective Facts from Subjective Opinions</span>
            </div>
            <p>
              A Fact is verifiable using evidence, statistics, dates, or scientific data. An Opinion reflects a personal belief, viewpoint, or judgment that cannot be proven true or false. Look for evaluative adjectives (e.g. 'exceptional', 'appalling', 'vital').
            </p>
            <div class="rule-highlight-badge">
              Examiner Tip: Quotes must directly evidence the point requested. Do not quote half a clause that alters the author's meaning.
            </div>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-file-lines"></i>
              <span>Golden Rule 2: Identify the Writer's Purpose and Organizational Layout</span>
            </div>
            <p>
              Consider why the writer chose specific presentational features (bullet points, captions, bold subheadings). In comparison questions, identify contrasting perspectives between Text A and Text B on the same topic.
            </p>
            <div class="rule-highlight-badge">
              Check: When comparing texts, use comparative connectives ('similarly', 'in contrast', 'whereas').
            </div>
          </div>
        </section>"""

print("Golden rules helper defined.")

def build_full_html(filename, clean_topic, subject, subject_pill_icon, subject_dir, hero_title, intro_lead, toc_items, content_sections_html, next_file, next_name):
    slug = filename.replace('functional-skills-', '').replace('.html', '')
    sheet_rel = f"worksheets/{slug}-worksheet.html"
    ans_rel = f"worksheets/{slug}-answers.html"

    # Construct sidebar list
    sidebar_html = ""
    for idx, (t_id, t_title, t_icon) in enumerate(toc_items):
        active_cls = " active" if idx == 0 else ""
        sidebar_html += f"""
          <li>
            <a href="#{t_id}" class="sidebar-toc-link{active_cls}">
              <i class="fa-solid {t_icon}"></i> {t_title}
            </a>
          </li>"""

    # Topic Visual Setup
    v_photo, v_caption, v_char, v_quote, v_sketch = vcc.get_topic_visual(filename or clean_topic)
    
    is_subfolder = "/" in filename and not filename.startswith("/")
    rel_pfx = "../" if is_subfolder else ""
    photo_src = f"{rel_pfx}assets/img/book_photos/{v_photo}"

    theme_attr = "english" if "English" in subject else "sapphire"

    html = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="{theme_attr}" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{clean_topic}: Key Rules, Models &amp; Exam Practice | Master Functional Skills</title>
  <meta name="description" content="Dyslexia-friendly {clean_topic} revision guide for Functional Skills {subject} Level 1 &amp; Level 2. Clear spacing, structured cards, large numbers, worked models, and interactive practice.">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192x192.png">
  <link rel="apple-touch-icon" href="assets/img/favicon-192x192.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="assets/css/mfs-revision.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

    <!-- TOP TRUST BAR WITH ACCESSIBILITY & CONTACT -->
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

  <!-- NAVIGATION -->  <!-- MAIN NAVIGATION -->
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

          <!-- 2. PAST PAPERS & MOCKS (DIRECT ACCESS) -->
          <li class="mfs-nav-item">
            <a href="functional-skills-past-papers.html" class="mfs-nav-link">
              <i class="fa-regular fa-file-lines" style="color:#0284c7; margin-right:5px;"></i> Past Papers &amp; Mocks
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

  <!-- BREADCRUMBS -->
  <div class="revision-breadcrumb-bar">
    <div class="revision-page-wrapper">
      <div class="revision-breadcrumbs">
        <a href="index.html"><i class="fa-solid fa-house"></i> Home</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="revise.html">Revise Hub</a>
        <i class="fa-solid fa-chevron-right"></i>
        <a href="{subject_dir}">{subject} Level 2</a>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="current">{clean_topic}</span>
      </div>
    </div>
  </div>

  <!-- HERO SECTION -->
  <section class="revision-hero-card">
    <div class="revision-page-wrapper">
      <div class="revision-hero-grid">
        <div class="revision-hero-content">
          <div class="revision-hero-pill-row">
            <span class="badge-pill-accent"><i class="fa-solid {subject_pill_icon}"></i> {subject.upper()}</span>
            <span class="badge-pill-gold">LEVEL 1 &amp; LEVEL 2</span>
            <span class="badge-pill-outline">OFQUAL SPECIFICATION STANDARDS</span>
          </div>

          <h1 class="revision-hero-title">
            {hero_title}
          </h1>

          <p class="revision-hero-desc">
            {intro_lead}
          </p>

          <div class="revision-hero-meta-bar">
            <div class="hero-meta-item">
              <i class="fa-solid fa-clock"></i> <strong>Est. Study Time:</strong> 25-35 Mins
            </div>
            <div class="hero-meta-item">
              <i class="fa-solid fa-book-open"></i> <strong>Curriculum Standards:</strong> Pearson Edexcel &amp; City &amp; Guilds
            </div>
            <div class="hero-meta-item">
              <i class="fa-solid fa-circle-check"></i> <strong>Interactive Practice Tasks Included</strong>
            </div>

            <div class="hero-quick-actions">
              <a href="#downloads" class="btn-hero-action">
                <i class="fa-regular fa-file-pdf"></i> Free Worksheet &amp; Answers (PDF)
              </a>
              <a href="#practice-questions" class="btn-hero-action-secondary">
                <i class="fa-solid fa-pencil"></i> Start Practice Tasks
              </a>
            </div>
          </div>
        </div>

        <div class="revision-hero-visual-card">
          <div class="revision-hero-img-wrap">
            <img src="{photo_src}" alt="{clean_topic} Workplace Application" loading="lazy" />
          </div>
          <div class="revision-hero-caption-bar">
            <strong><i class="fa-solid fa-shapes"></i> Key Visual Concept</strong>
            {v_caption}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MOBILE TABLE OF CONTENTS BAR -->
  <div class="mobile-toc-bar">
    <div style="font-weight:700; color:var(--navy-dark); font-size:0.9rem;">
      <i class="fa-solid fa-list-check" style="color:var(--accent);"></i> {clean_topic} Blueprint
    </div>
    <button type="button" class="btn-mobile-toc" onclick="toggleMobileToc()">
      <span>Table of Contents</span> <i class="fa-solid fa-bars"></i>
    </button>
  </div>

  <!-- MAIN 2-COLUMN RESPONSIVE LAYOUT -->
  <main class="revision-page-wrapper">
    <div class="revision-layout">

      <!-- LEFT COLUMN: STICKY BLUEPRINT TOC -->
      <aside class="revision-sidebar" id="sidebarNav">
        <div class="sidebar-toc-title">
          <span><i class="fa-solid fa-compass-drafting" style="color:var(--accent);"></i> Topic Contents</span>
          <span style="font-size:0.75rem; color:#64748b; font-weight:700;">{len(toc_items)} Sections</span>
        </div>

        <ul class="sidebar-toc-list" id="tocList">
          {sidebar_html}
        </ul>
      </aside>

      <!-- RIGHT COLUMN: MAIN LEARNING CONTENT -->
      <div class="revision-content">
        {content_sections_html}

        <!-- DOWNLOADS -->
        <section id="downloads" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-regular fa-file-pdf"></i> Free Revision Worksheets &amp; Exam Papers</h2>
          </div>

          <div class="download-tiles-grid">
            <a href="{sheet_rel}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-pdf"><i class="fa-regular fa-file-pdf"></i></div>
              <div class="download-tile-info">
                <strong>{clean_topic} Exam Practice Worksheet (PDF)</strong>
                <span>Official practice questions calibrated for L1 &amp; L2 examinations</span>
              </div>
            </a>

            <a href="{ans_rel}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers"><i class="fa-solid fa-check-double"></i></div>
              <div class="download-tile-info">
                <strong>Step-by-Step Worked Mark Scheme (PDF)</strong>
                <span>Complete tutor model answers with method marks breakdown</span>
              </div>
            </a>
          </div>
        </section>

        <!-- NEXT TOPIC BANNER -->
        <div class="next-topic-banner">
          <div class="next-topic-info">
            <strong>Next Curriculum Topic</strong>
            <span>{next_name}</span>
          </div>
          <a href="{next_file}" class="btn-next-topic">
            Continue Revision <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>

      </div>
    </div>
  </main>

  <!-- FOOTER -->
  <footer class="mfs-footer" id="site-footer">
    <div class="mfs-container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="mfs-brand" style="margin-bottom:16px;">
            <div class="mfs-brand-icon"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="mfs-brand-text">
              <div class="mfs-brand-title" style="color:#ffffff;">MASTER<span>FUNCTIONALSKILLS</span></div>
              <div class="mfs-brand-subtitle" style="color:#94a3b8;">Delivering Skills • Achieving Goals</div>
            </div>
          </div>
          <p style="font-size:0.88rem; line-height:1.6; margin-bottom:16px;">
            The UK's dedicated Functional Skills revision specialist. Providing realistic mock exams, step-by-step revision flashcards, diagnostic assessments, and 1-to-1 specialist tuition for Pearson Edexcel, City &amp; Guilds, and all major exam boards.
          </p>
          <div style="font-size:0.85rem; color:#cbd5e1;">
            <p><a href="https://wa.me/447564525425" target="_blank" rel="noopener" style="color:#cbd5e1; text-decoration:none;"><i class="fa-brands fa-whatsapp" style="color:var(--accent); margin-right:8px;"></i> WhatsApp: +44 (0)7564 525425</a></p>
            <p style="margin-top:6px;"><a href="contact-us.html" style="color:#cbd5e1; text-decoration:none;"><i class="fa-solid fa-envelope" style="color:var(--accent); margin-right:8px;"></i> Contact Tutor Team</a></p>
          </div>
        </div>

        <div class="footer-col">
          <h4>Maths Revision</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-maths-level-2.html">Maths Level 2 Revision</a></li>
            <li><a href="functional-skills-maths-level-1.html">Maths Level 1 Revision</a></li>
            <li><a href="entry-level-3-maths.html">Entry Level 3 Maths</a></li>
            <li><a href="pass-mark-calculator.html">Pass Mark Calculator</a></li>
            <li><a href="functional-skills-past-papers.html">Free Maths Past Papers</a></li>
            <li><a href="exam-maths-l2.html">Book Level 2 Maths Exam</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>English &amp; Digital</h4>
          <ul class="footer-links">
            <li><a href="functional-skills-english-level-2.html">English Level 2 Revision</a></li>
            <li><a href="functional-skills-english-level-1.html">English Level 1 Revision</a></li>
            <li><a href="digital-functional-skills.html">Digital Skills Hub (L1 &amp; E3)</a></li>
            <li><a href="digital-functional-skills-past-papers.html">DFS Past Papers &amp; Data Files</a></li>
            <li><a href="functional-skills-past-papers.html?format=online#mock-finder">Online Exam Simulator</a></li>
            <li><a href="exam-english-l2.html">Book Level 2 English Exam</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Student Support &amp; Tools</h4>
          <ul class="footer-links">
            <li><a href="tools.html" style="color:var(--accent); font-weight:700;"><i class="fa-solid fa-screwdriver-wrench" style="margin-right:6px;"></i>All Interactive Tools Hub</a></li>
            <li><a href="pass-mark-calculator.html">Pass Mark Calculator</a></li>
            <li><a href="diagnostic-test.html">Diagnostic Skill Checker</a></li>
            <li><a href="functional-skills-nets.html">3D Net Folding Tool</a></li>
            <li><a href="digital-functional-skills-mock-exam.html">Pearson DFS Simulator</a></li>
            <li><a href="revision-cards.html">Revision Cards &amp; Flashcards</a></li>
            <li><a href="shop.html">Revision Books &amp; Study Packs</a></li>
            <li><a href="tutors.html">1-to-1 Specialist Tuition</a></li>
            <li><a href="exams.html">Book Official Online Exam</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 Master Functional Skills. All rights reserved. Registered in England &amp; Wales. Ofqual Regulated Qualification Standards.</div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <a href="index.html">Home</a>
          <a href="tools.html" style="color:var(--accent); font-weight:700;">Tools</a>
          <a href="functional-skills-past-papers.html">Past Papers</a>
          <a href="revision-cards.html">Revision Cards</a>
          <a href="shop.html">Study Shop</a>
          <a href="tutors.html">Tutors</a>
          <a href="contact-us.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="assets/js/mfs-revision.js"></script>
</body>
</html>
"""
    return html

print("Full HTML generator defined.")

def clean_text_from_html(text):
    if not text:
        return ""
    text = re.sub(r'^(?:Functional\s+Skills(?::)?\s*|Reading(?::)?\s*|Writing(?::)?\s*|SLC(?::)?\s*)', '', text, flags=re.I).strip()
    text = re.sub(r'\s+Revision(?:\s+and\s+Practice)?(?:\s+Guide)?(?:\s*&.*)?$', '', text, flags=re.I).strip()
    text = re.sub(r':\s*Formulas,\s*Models.*$', '', text, flags=re.I).strip()
    text = re.sub(r':\s*Key\s*Rules.*$', '', text, flags=re.I).strip()
    text = text.replace(':', ' –')
    return text.strip()

def format_curriculum_solution(sol_html, marks_str):
    if not sol_html:
        sol_html = "<p>Check intermediate steps and verify against the final calculation.</p>"
    if 'solution-steps-list' in sol_html:
        return sol_html
    try:
        sol_html = sol_html.replace('Â', ' ').replace('Ã—', '&times;').replace('âˆ’', '&minus;').replace('\u00a0', ' ')
        sol_tree = html.fragment_fromstring(f"<div>{sol_html}</div>")
        for t in sol_tree.xpath('.//div[contains(@class, "solution-drawer-title")]'):
            t.drop_tree()
        paras = []
        for p in sol_tree.xpath('.//p | .//li'):
            txt = p.text_content().strip()
            # Ignore empty or whitespace-only paragraphs
            if txt and txt != '&nbsp;' and txt != 'Â':
                paras.append(p)
        final_answer = ""
        step_items_html = ""
        if len(paras) >= 2:
            last_text = paras[-1].text_content().strip()
            if any(k in last_text.lower() for k in ['=', 'answer', 'hence', 'total', 'mean', 'median', 'mode', 'range', 'cm', 'm', '£', '$', '%']):
                final_answer = clean_inner_html_safe(paras[-1]).strip()
                step_paras = paras[:-1]
            else:
                step_paras = paras
            step_count = 1
            for p in step_paras:
                p_text = clean_inner_html_safe(p).strip()
                raw_txt = p.text_content().strip()
                if not raw_txt or raw_txt == '&nbsp;':
                    continue
                is_math = bool(re.search(r'(=|\+|-|×|÷|\*|/)', raw_txt) and len(raw_txt) < 80)
                step_items_html += f"""
                <div class="solution-step-item">
                  <div class="solution-step-header">
                    <span class="solution-step-tag">Step {step_count} (Method)</span>
                    <span class="solution-step-mark">M1 Mark</span>
                  </div>
                  {'<div class="solution-step-math">' + p_text + '</div>' if is_math else '<div class="solution-step-content">' + p_text + '</div>'}
                </div>"""
                step_count += 1
        elif len(paras) == 1:
            step_items_html = f"""
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Worked Method &amp; Calculation</span>
                <span class="solution-step-mark">Method &amp; Accuracy</span>
              </div>
              <div class="solution-step-content">{clean_inner_html_safe(paras[0])}</div>
            </div>"""
        else:
            step_items_html = f"""
            <div class="solution-step-item">
              <div class="solution-step-header">
                <span class="solution-step-tag">Step-by-Step Method</span>
                <span class="solution-step-mark">Method Mark</span>
              </div>
              <div class="solution-step-content">{clean_inner_html_safe(sol_tree)}</div>
            </div>"""
        
        final_box_html = f"""
        <div class="solution-final-answer-box">
          <div class="solution-final-label"><i class="fa-solid fa-award"></i> Correct Final Answer:</div>
          <div class="solution-final-value">{final_answer}</div>
        </div>""" if final_answer else ""

        return f"""
        <div class="solution-drawer-title">
          <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
          <span class="solution-marks-badge">{marks_str} Full Marks</span>
        </div>
        <div class="solution-steps-list">
          {step_items_html}
        </div>
        {final_box_html}
        <div class="solution-tutor-tip">
          <i class="fa-solid fa-lightbulb"></i>
          <span><strong>Examiner Marking Tip:</strong> Always show intermediate calculations and write your units clearly. Accurate method steps ensure partial credit method marks (M1) even if an arithmetic slip occurs.</span>
        </div>"""
    except Exception as e:
        return f"""
        <div class="solution-drawer-title">
          <div style="display:flex; align-items:center; gap:8px;"><i class="fa-solid fa-circle-check"></i> Official Tutor Step-by-Step Mark Scheme</div>
          <span class="solution-marks-badge">{marks_str} Full Marks</span>
        </div>
        <div class="solution-steps-list">
          <div class="solution-step-item">
            <div class="solution-step-content">{sol_html}</div>
          </div>
        </div>
        <div class="solution-tutor-tip">
          <i class="fa-solid fa-lightbulb"></i>
          <span><strong>Examiner Marking Tip:</strong> Show all your step-by-step working clearly for maximum method marks.</span>
        </div>"""

def transform_generic_topic(filename):
    src_path = os.path.join(TOPICS_DIR, filename)
    if not os.path.exists(src_path):
        src_path = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(src_path):
        print(f"[SKIP] {filename} not found.")
        return False

    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    tree = lxml.html.fromstring(content)
    
    # Subject info
    is_english, is_digital, subject, subject_pill_icon, subject_dir = get_subject_meta(filename)
    
    # Title extraction
    title_el = tree.find('.//title')
    raw_title = title_el.text_content().strip() if title_el is not None else filename
    clean_topic = clean_text_from_html(raw_title.split('|')[0].strip())
    if not clean_topic or len(clean_topic) < 3:
        clean_topic = filename.replace('functional-skills-', '').replace('.html', '').replace('-', ' ').title()

    hero_title = f"{clean_topic}: <span>Key Rules, Models &amp; Exam Practice</span>"
    intro_lead = f"Comprehensive revision guide for {clean_topic} calibrated to Pearson Edexcel &amp; City &amp; Guilds Functional Skills standards. Master core principles, worked models, and interactive practice."

    # Content container
    home_content = tree.find('.//*[@id="home-content"]')
    if home_content is None:
        home_content = tree.find('.//main')
    if home_content is None:
        home_content = tree.find('.//body')

    # Remove all katex-mathml
    for m in home_content.xpath('.//*[contains(@class, "katex-mathml")]'):
        m.drop_tree()

    # Extract spec points
    spec_points = []
    spec_headings = home_content.xpath('.//*[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "specification points covered")]')
    if spec_headings:
        parent_spec = spec_headings[0].getparent()
        for p in parent_spec.xpath('.//li | .//p'):
            t = p.text_content().strip()
            if t and not 'specification points' in t.lower() and len(t) > 6:
                spec_points.append(t)

    # Extract skills / lesson blocks
    skill_blocks = []
    # Find all sections or divs with skill titles
    top_sections = home_content.xpath('./section | ./div[contains(@class, "topic-box") or contains(@class, "page_builder_section")]')
    if not top_sections:
        top_sections = home_content.xpath('.//section')
        
    for s in top_sections:
        # Check title
        h_nodes = s.xpath('.//h2 | .//h3')
        if not h_nodes:
            continue
        h_title = h_nodes[0].text_content().strip()
        h_lower = h_title.lower()
        if any(bad in h_lower for bad in ['follow our socials', 'revision products', 'speak to one of our experts', 'additional resources', 'specification points']):
            continue
        if 'example questions' in h_lower or 'practice questions' in h_lower:
            continue
            
        # Clean heading inside section so it doesn't duplicate
        h_nodes[0].drop_tree()

        # Drop any leftover raw badge divs inside the skill explanation body
        for b in s.xpath('.//*[contains(@class, "badge") or contains(@class, "filter-item")]/..'):
            b_cls = b.get('class', '')
            if 'mt-3' in b_cls or 'badge' in b_cls:
                b.drop_tree()
        for b in s.xpath('.//*[contains(@class, "badge") or contains(@class, "filter-item")]'):
            b.drop_tree()

        clean_html = clean_inner_html_safe(s)
        if len(s.text_content().strip()) > 25:
            skill_blocks.append({
                'title': clean_text_from_html(h_title),
                'html': clean_html
            })

    # Extract practice questions
    questions = []
    q_sections = home_content.xpath('.//section[contains(@class, "example-question")] | .//div[contains(@class, "example-question")]')
    if not q_sections:
        # Fallback to collapses
        q_sections = home_content.xpath('.//div[contains(@class, "collapse")]/..')

    for q_idx, q_sec in enumerate(q_sections):
        q_text = q_sec.text_content()
        marks_match = re.search(r'\[(\d+)\s*marks?\]', q_text, re.I)
        marks_str = f"[{marks_match.group(1)} Marks]" if marks_match else "[2 Marks]"

        # Extract badges from q_sec before cleaning
        badge_nodes = q_sec.xpath('.//*[contains(@class, "badge") or contains(@class, "filter-item")]')
        q_badges = []
        for b in badge_nodes:
            txt = b.text_content().strip()
            if txt and txt not in [x['name'] for x in q_badges]:
                b_cls = b.get('class', '').lower()
                is_l1 = 'level-1' in b_cls or txt == 'FS Level 1'
                is_l2 = 'level-2' in b_cls or txt == 'FS Level 2'
                q_badges.append({'name': txt, 'is_l1': is_l1, 'is_l2': is_l2})

        # Remove old badges, filter items, and collapse buttons
        for b in q_sec.xpath('.//*[contains(@class, "badge") or contains(@class, "filter-item") or contains(@class, "btn")]'):
            b.drop_tree()
                
        # Solution
        sol_el = q_sec.xpath('.//div[contains(@class, "collapse")]')
        sol_html = ""
        if sol_el:
            sol_html = clean_inner_html_safe(sol_el[0])
            sol_el[0].drop_tree()
            
        # Clean Stem Paragraphs & Images
        elements = []
        for p in q_sec.xpath('.//p'):
            txt = p.text_content().strip()
            if not txt and not p.xpath('.//img'):
                continue
            p_html = clean_inner_html_safe(p)
            p_html = p_html.replace('Â', ' ').replace('Ã—', '&times;').replace('âˆ’', '&minus;')
            p_html = re.sub(r'^\s*(?:<strong>)?\s*Question\s*\d+\s*:\s*(?:</strong>)?\s*', '', p_html, flags=re.I)
            p_html = re.sub(r'\[\s*\d+\s*marks?\s*\]', '', p_html, flags=re.I).strip()
            if p_html and p_html != '<br>':
                elements.append(f"<p>{p_html}</p>")

        # Check for any images outside paragraphs
        for im in q_sec.xpath('.//img'):
            src = im.get('src', '')
            if src and not any(src in el for el in elements):
                elements.append(f'<img src="{src}" alt="Practice question diagram">')

        stem_html = '\n'.join(elements)
        if len(q_sec.text_content().strip()) < 10 and not elements:
            stem_html = f"<p>A workplace task requires applying <strong>{clean_topic}</strong> principles. Calculate the required value and show your step-by-step working below.</p>"
            
        questions.append({
            'num': q_idx + 1,
            'marks': marks_str,
            'stem': stem_html,
            'solution': sol_html or "<p>Check intermediate calculation steps and verify against the final answer.</p>",
            'badges': q_badges
        })

    next_file, next_name = get_next_topic(filename, is_english)

    # Build TOC Items
    toc_items = []
    if spec_points:
        toc_items.append(('specification', 'Specification', 'fa-clipboard-check'))
    toc_items.append(('golden-rules', 'Golden Rules', 'fa-lightbulb'))
    for idx, b in enumerate(skill_blocks[:6]):
        b_id = f"skill-{idx+1}"
        short_title = b['title'][:20] if len(b['title']) > 20 else b['title']
        toc_items.append((b_id, short_title or f"Skill {idx+1}", 'fa-shapes'))
    if questions:
        toc_items.append(('practice-questions', 'Exam Practice', 'fa-pencil'))
    toc_items.append(('downloads', 'Downloads (PDF)', 'fa-file-pdf'))

    # Build Sections HTML
    content_html = ""

    # 1. Spec
    if spec_points:
        content_html += f"""
        <!-- SPECIFICATION -->
        <section id="specification" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
          </div>
          <div class="skill-card-container">
            <p>Students must demonstrate mastery of the following regulated outcomes:</p>
            <ul style="padding-left:20px; line-height:1.75; color:#334155;">"""
        for sp in spec_points[:8]:
            content_html += f"<li>{sp}</li>"
        content_html += """
            </ul>
          </div>
        </section>"""

    # 2. Golden Rules
    content_html += get_golden_rules_html(subject, clean_topic)

    # 3. Core Skills in PFS-Cards
    for idx, b in enumerate(skill_blocks[:6]):
        b_id = f"skill-{idx+1}"
        content_html += f"""
        <!-- SKILL {idx+1}: {b['title'].upper()} -->
        <section id="{b_id}" class="revision-section">
          <div class="mfs-topic-card">
            <div class="mfs-topic-head">
              <div class="mfs-topic-title">
                <span class="mfs-topic-prefix">Example {idx+1}:</span> {b['title']}
              </div>
            </div>
            <div class="mfs-topic-stem">
              {b['html']}
            </div>
            <div class="mfs-topic-footer">
              <span class="mfs-pill-l1">Level 1</span>
              <span class="mfs-pill-l2">Level 2</span>
              <span class="mfs-pill-board">Pearson Edexcel &bull; City &amp; Guilds</span>
            </div>
          </div>
        </section>"""

    # 4. Practice Questions
    if questions:
        content_html += f"""
        <!-- EXAM PRACTICE QUESTIONS -->
        <section id="practice-questions" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
            <span style="font-size:0.9rem; color:#64748b; font-weight:700;">{len(questions)} Practice Tasks</span>
          </div>"""

        for q in questions[:6]:
            drawer_id = f"drawer-q{q['num']}"
            formatted_sol = format_curriculum_solution(q['solution'], q['marks'])
            
            # Format practice question footer pills
            footer_pills = []
            if q.get('badges'):
                for bg in q['badges']:
                    if bg['is_l1']:
                        footer_pills.append(f'<span class="mfs-pill-l1">{bg["name"]}</span>')
                    elif bg['is_l2']:
                        footer_pills.append(f'<span class="mfs-pill-l2">{bg["name"]}</span>')
                    else:
                        footer_pills.append(f'<span class="mfs-pill-board">{bg["name"]}</span>')
            else:
                footer_pills = [
                    '<span class="mfs-pill-l1">FS Level 1</span>',
                    '<span class="mfs-pill-l2">FS Level 2</span>',
                    '<span class="mfs-pill-board">Edexcel</span>',
                    '<span class="mfs-pill-board">City &amp; Guilds</span>',
                    '<span class="mfs-pill-board">NCFE</span>',
                    '<span class="mfs-pill-board">Open Awards</span>',
                    '<span class="mfs-pill-board">Highfield</span>'
                ]
            footer_html = '\n              '.join(footer_pills)

            content_html += f"""
          <div class="practice-q-card">
            <div class="practice-q-header">
              <div class="practice-q-title"><span class="mfs-topic-prefix">Question {q['num']}:</span> Practice Task</div>
              <span class="practice-marks-pill"><i class="fa-solid fa-award"></i> {q['marks']}</span>
            </div>
            <div class="practice-q-stem">
              {q['stem']}
            </div>

            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
              <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
            </div>

            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('{drawer_id}')">
                <i class="fa-solid fa-eye"></i> Reveal Step-by-Step Solution &amp; Mark Scheme
              </button>
            </div>

            <div id="{drawer_id}" class="solution-drawer">
              {formatted_sol}
            </div>

            <div class="practice-q-footer">
              {footer_html}
            </div>
          </div>"""

        content_html += """
        </section>"""

    # Assemble HTML
    full_html = build_full_html(
        filename=filename,
        clean_topic=clean_topic,
        subject=subject,
        subject_pill_icon=subject_pill_icon,
        subject_dir=subject_dir,
        hero_title=hero_title,
        intro_lead=intro_lead,
        toc_items=toc_items,
        content_sections_html=content_html,
        next_file=next_file,
        next_name=next_name
    )

    dest_path = os.path.join(PROJECT_DIR, filename)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"[GENERIC TRANSFORMED] {filename} ({len(full_html)} bytes)")
    return True

print("Generic topic transformer defined.")
