import os, sys, re, glob, lxml.html
from lxml import etree

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

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

def clean_element(el):
    if el is None:
        return
    # Remove mathml duplicates
    for m in el.xpath('.//*[contains(@class, "katex-mathml")]'):
        m.drop_tree()
    # Remove script, style, noscript
    for bad in el.xpath('.//script | .//style | .//noscript'):
        bad.drop_tree()
    # Remove old inline board/level strings
    for bad in el.xpath('.//*[contains(text(), "TQUKEdexcelCity") or contains(text(), "Highfield Qualifications")]'):
        bad.drop_tree()
    # Clean images
    for img in el.xpath('.//img'):
        src = img.get('src', '')
        if '%20' in src:
            src = src.split('%20')[0].strip()
        src = src.split(' ')[0].strip()
        img.set('src', src)
        for a in ['width', 'height', 'data-lazy-src', 'data-lazy-srcset', 'data-lazy-sizes', 'loading']:
            if img.get(a):
                del img.attrib[a]
        img.set('class', 'img-fluid')
        img.set('loading', 'lazy')

def clean_inner_html(el, drop_first_heading=True):
    if el is None:
        return ""
    clean_element(el)
    
    # If the first child is an H2 or H3, drop it since we render our own skill title
    if drop_first_heading:
        headings = el.xpath('.//h2 | .//h3')
        if headings:
            first_h = headings[0]
            # only drop if it's at the start
            first_h.drop_tree()
            
    return ''.join(etree.tostring(child, encoding='unicode') for child in el)

def extract_and_transform_page(filename):
    filepath = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: not found.")
        return False

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        raw_html = f.read()

    tree = lxml.html.fromstring(raw_html)
    
    # Clean mathml across entire document first
    for m in tree.xpath('.//*[contains(@class, "katex-mathml")]'):
        m.drop_tree()

    # Identify subject & level
    is_english = filename.startswith(('reading-', 'writing-')) or 'english' in filename
    subject = "English" if is_english else "Mathematics"
    subject_pill_icon = "fa-pen-nib" if is_english else "fa-calculator"
    subject_dir = "functional-skills-english-level-2.html" if is_english else "functional-skills-maths-level-2.html"

    # Title extraction
    title_el = tree.find('.//title')
    raw_title = title_el.text_content().strip() if title_el is not None else filename
    clean_topic = raw_title.split('|')[0].strip()
    clean_topic = re.sub(r'^(?:Functional\s+Skills(?::)?\s*|Reading(?::)?\s*|Writing(?::)?\s*)', '', clean_topic, flags=re.I).strip()
    clean_topic = re.sub(r'\s+Revision(?:\s+Guide)?(?:\s*&.*)?$', '', clean_topic, flags=re.I).strip()
    if not clean_topic:
        clean_topic = filename.replace('functional-skills-', '').replace('.html', '').replace('-', ' ').title()

    hero_title = f"{clean_topic}: <span>Formulas, Models &amp; Exam Practice</span>" if not is_english else f"{clean_topic}: <span>Key Rules, Models &amp; Exam Practice</span>"

    # Locate content root
    home_content = tree.find('.//*[@id="home-content"]')
    if home_content is None:
        home_content = tree.find('.//main')
    if home_content is None:
        home_content = tree.find('.//body')

    clean_element(home_content)

    # Extract Spec Points
    spec_points = []
    spec_container = home_content.xpath('.//*[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "specification points covered")]')
    if spec_container:
        parent_spec = spec_container[0].getparent()
        for li in parent_spec.xpath('.//li | .//p'):
            t = li.text_content().strip()
            if t and not 'specification points' in t.lower() and len(t) > 5:
                spec_points.append(t)

    # Extract Practice Questions
    questions = []
    q_sections = home_content.xpath('.//section[contains(@class, "example-question")] | .//div[contains(@class, "example-question")]')
    for q_idx, q_sec in enumerate(q_sections):
        clean_element(q_sec)
        q_text = q_sec.text_content()
        marks_match = re.search(r'\[(\d+)\s*marks?\]', q_text, re.I)
        marks_str = f"[{marks_match.group(1)} Marks]" if marks_match else "[2 Marks]"
        
        q_imgs = [img.get('src') for img in q_sec.xpath('.//img')]
        
        stem_html_parts = []
        for p in q_sec.xpath('./p | ./div[not(contains(@class, "collapse")) and not(contains(@class, "btn"))]/p'):
            clean_element(p)
            ptxt = p.text_content().strip()
            if ptxt and not re.search(r'\[\d+\s*marks?\]', ptxt, re.I) and not 'btn' in p.get('class', ''):
                stem_html_parts.append(etree.tostring(p, encoding='unicode'))
        
        sol_el = q_sec.xpath('.//div[contains(@class, "collapse")]')
        sol_html = ""
        if sol_el:
            sol_html = clean_inner_html(sol_el[0], drop_first_heading=False)
            
        questions.append({
            'num': q_idx + 1,
            'marks': marks_str,
            'stem': "".join(stem_html_parts),
            'imgs': q_imgs,
            'solution': sol_html
        })

    # Extract Worksheets
    worksheets = []
    ws_container = home_content.xpath('.//*[@id="worksheet-example-questions"]')
    if ws_container:
        for a in ws_container[0].xpath('.//a[contains(@href, ".pdf") or contains(@class, "btn")]'):
            href = a.get('href', '#')
            title = a.text_content().strip() or "Practice Worksheet & Mark Scheme (PDF)"
            worksheets.append({'href': href, 'title': title})

    # Extract Skills & Content sections
    top_sections = [s for s in home_content if isinstance(s, lxml.html.HtmlElement)]
    
    educational_blocks = []
    intro_lead = ""
    
    for sec in top_sections:
        clean_element(sec)
        txt = sec.text_content().lower()
        if any(bad in txt for bad in ['follow our socials', 'revision products', 'speak to one of our experts', 'additional resources']):
            continue
        if sec.get('id') == 'worksheet-example-questions':
            continue
        if 'example questions' in txt and sec.xpath('.//section[contains(@class, "example-question")]'):
            continue
            
        h_elements = sec.xpath('.//h2 | .//h3')
        if not h_elements:
            p_text = sec.text_content().strip()
            if len(p_text) > 40 and not intro_lead and not 'level 1' in p_text[:20].lower():
                intro_lead = p_text
            continue
            
        h_title = ' '.join(h_elements[0].itertext()).strip()
        h_title_clean = re.sub(r'\s+', ' ', h_title)
        
        # Check if it's the main intro heading
        if h_title_clean.lower() in [clean_topic.lower(), f"functional skills: {clean_topic.lower()}", f"functional skills {clean_topic.lower()}"]:
            p_list = [p.text_content().strip() for p in sec.xpath('.//p') if len(p.text_content().strip()) > 20]
            if p_list:
                intro_lead = " ".join(p_list)
            continue
            
        block_html = clean_inner_html(sec, drop_first_heading=True)
        if len(sec.text_content().strip()) > 30:
            educational_blocks.append({
                'title': h_title_clean,
                'html': block_html
            })

    if not intro_lead:
        intro_lead = f"Comprehensive revision guide for {clean_topic} calibrated to Pearson Edexcel & City & Guilds Functional Skills standards. Master core principles, worked exam models, and interactive practice."

    next_file, next_name = get_next_topic(filename, is_english)

    # BUILD TABLE OF CONTENTS
    toc_items = []
    if spec_points:
        toc_items.append(('specification', 'Specification', 'fa-clipboard-check'))
    toc_items.append(('golden-rules', 'Golden Rules', 'fa-lightbulb'))
    for idx, b in enumerate(educational_blocks):
        b_id = f"skill-{idx+1}"
        short_title = b['title'].split(':')[0].strip() if ':' in b['title'] else b['title'][:22]
        toc_items.append((b_id, short_title, 'fa-shapes'))
    if questions:
        toc_items.append(('practice-questions', 'Exam Practice', 'fa-pencil'))
    if worksheets:
        toc_items.append(('downloads', 'Downloads (PDF)', 'fa-file-pdf'))

    # GENERATE HTML
    html_out = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{clean_topic}: Formulas, Models &amp; Exam Practice | Master Functional Skills</title>
  <meta name="description" content="Dyslexia-friendly {clean_topic} revision guide for Functional Skills {subject} Level 1 &amp; Level 2. Clear spacing, structured cards, formulas, worked models, and interactive practice.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="assets/css/mfs-revision.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

  <!-- TOP TRUST BAR WITH DYSLEXIA TINT PICKER -->
  <div class="mfs-top-bar">
    <div class="revision-page-wrapper mfs-top-bar-inner">
      <div class="top-trust-items">
        <span class="top-trust-item"><i class="fa-solid fa-building-columns"></i> Pearson Edexcel &amp; City &amp; Guilds Aligned</span>
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

  <!-- NAVIGATION -->
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
          <i class="fa-solid fa-circle-check"></i> <strong>{len(questions)} Interactive Practice Tasks</strong>
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

        <ul class="sidebar-toc-list" id="tocList">"""

    for idx, (t_id, t_title, t_icon) in enumerate(toc_items):
        active_cls = " active" if idx == 0 else ""
        html_out += f"""
          <li>
            <a href="#{t_id}" class="sidebar-toc-link{active_cls}">
              <i class="fa-solid {t_icon}"></i> {t_title}
            </a>
          </li>"""

    html_out += """
        </ul>
      </aside>

      <!-- RIGHT COLUMN: MAIN LEARNING CONTENT -->
      <div class="revision-content">"""

    # 1. SPECIFICATION SECTION
    if spec_points:
        html_out += f"""
        <!-- SPECIFICATION -->
        <section id="specification" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Specification &amp; Learning Outcomes</h2>
          </div>
          <div class="skill-card-container">
            <p>Students must be able to demonstrate mastery of the following regulated outcomes:</p>
            <ul style="padding-left:20px; line-height:1.75; color:#334155;">"""
        for sp in spec_points[:8]:
            html_out += f"<li>{sp}</li>"
        html_out += """
            </ul>
          </div>
        </section>"""

    # 2. GOLDEN RULES / CORE CONCEPTS
    html_out += f"""
        <!-- GOLDEN RULES -->
        <section id="golden-rules" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-lightbulb"></i> Golden Rules &amp; Essential Concepts</h2>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-triangle-exclamation"></i>
              <span>Golden Rule 1: Always Read the Question Stem Carefully</span>
            </div>
            <p>
              Examiners award partial marks for setting out your working step-by-step. Even if your final calculation contains an arithmetic error, you will gain method marks if your process is clear.
            </p>
            <div class="rule-highlight-badge">
              Tip: Write every intermediate step in the working box provided.
            </div>
          </div>

          <div class="rule-card-amber">
            <div class="rule-card-amber-header">
              <i class="fa-solid fa-arrows-split-up-and-left"></i>
              <span>Golden Rule 2: Check Your Units and Format</span>
            </div>
            <p>
              Always state the correct units in your final answer (e.g. cm, m, m&sup2;, %, £ or decimal places as specified in the question).
            </p>
            <div class="rule-highlight-badge">
              Check: Does the question specify rounding or exact units?
            </div>
          </div>
        </section>"""

    # 3. CORE SKILLS & CONTENT BLOCKS
    for idx, b in enumerate(educational_blocks):
        b_id = f"skill-{idx+1}"
        html_out += f"""
        <!-- {b['title'].upper()} -->
        <section id="{b_id}" class="revision-section">
          <div class="skill-card-container">
            <div class="skill-header-meta">
              <span class="skill-badge-tag">Section {idx+1}</span>
              <span class="badge-level-tag">Level 1 &amp; Level 2</span>
              <span class="badge-board-tag">Edexcel &bull; City &amp; Guilds</span>
            </div>
            <h3 class="skill-title-text">{b['title']}</h3>
            {b['html']}
          </div>
        </section>"""

    # 4. EXAM PRACTICE QUESTIONS
    if questions:
        html_out += f"""
        <!-- EXAM PRACTICE QUESTIONS -->
        <section id="practice-questions" class="revision-section">
          <div class="section-header-row">
            <h2 class="section-title"><i class="fa-solid fa-pencil"></i> Interactive Exam Practice Questions</h2>
            <span style="font-size:0.9rem; color:#64748b; font-weight:700;">{len(questions)} Practice Tasks</span>
          </div>"""

        for q in questions:
            drawer_id = f"drawer-q{q['num']}"
            img_html = ""
            for im in q['imgs']:
                img_html += f'<img src="{im}" alt="Question {q["num"]} diagram" class="img-fluid" style="max-width:500px; display:block; margin:14px 0; border-radius:8px;">'

            html_out += f"""
          <div class="practice-q-card">
            <div class="practice-q-header">
              <span class="practice-q-num">Question {q['num']}</span>
              <span class="practice-q-marks">{q['marks']}</span>
            </div>
            <div class="practice-q-stem">
              {q['stem']}
              {img_html}
            </div>

            <div class="working-scratchpad-area">
              <label class="working-scratchpad-label"><i class="fa-solid fa-calculator"></i> Your Working Scratchpad (Auto-saved):</label>
              <textarea class="working-scratchpad-input" placeholder="Type your step-by-step working here..."></textarea>
            </div>

            <div class="practice-q-toolbar">
              <button type="button" class="btn-reveal-solution" onclick="toggleSolutionDrawer('{drawer_id}')">
                <i class="fa-solid fa-eye"></i> Reveal Full Solution &amp; Mark Scheme
              </button>
            </div>

            <div id="{drawer_id}" class="solution-drawer">
              <div class="solution-drawer-title"><i class="fa-solid fa-circle-check"></i> Official Tutor Worked Solution</div>
              <div style="line-height:1.7; color:#166534;">
                {q['solution']}
              </div>
            </div>
          </div>"""

        html_out += """
        </section>"""

    # 5. DOWNLOADS SECTION
    slug = filename.replace('functional-skills-', '').replace('.html', '')
    sheet_rel = f"worksheets/{slug}-worksheet.html"
    ans_rel = f"worksheets/{slug}-answers.html"

    html_out += f"""
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
                <span>Official questions calibrated for L1 &amp; L2 examinations</span>
              </div>
            </a>

            <a href="{ans_rel}" target="_blank" class="download-tile-card">
              <div class="download-tile-icon icon-answers"><i class="fa-solid fa-check-double"></i></div>
              <div class="download-tile-info">
                <strong>Step-by-Step Worked Mark Scheme (PDF)</strong>
                <span>Complete examiner model answers with method marks breakdown</span>
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
  <footer style="background:var(--navy-dark); color:#cbd5e1; padding:60px 0 20px; margin-top:80px; border-top:3px solid var(--accent);">
    <div class="revision-page-wrapper">
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:32px; margin-bottom:40px;">
        <div>
          <div style="font-size:1.25rem; font-weight:800; color:#ffffff; margin-bottom:12px;">
            MASTER<span style="color:#60a5fa;">FUNCTIONALSKILLS</span>
          </div>
          <p style="font-size:0.9rem; line-height:1.6; color:#94a3b8;">
            Empowering adult learners, NHS staff, and apprentices to achieve Pearson Edexcel &amp; City &amp; Guilds Functional Skills qualifications.
          </p>
        </div>
        <div>
          <h4 style="color:#ffffff; font-size:1rem; font-weight:700; margin-bottom:14px;">Maths Revision</h4>
          <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:0.9rem;">
            <li><a href="functional-skills-maths-level-2.html" style="color:#cbd5e1; text-decoration:none;">Maths Level 2 Directory</a></li>
            <li><a href="functional-skills-maths-level-1.html" style="color:#cbd5e1; text-decoration:none;">Maths Level 1 Directory</a></li>
            <li><a href="functional-skills-area.html" style="color:#cbd5e1; text-decoration:none;">Area Revision</a></li>
            <li><a href="functional-skills-perimeter.html" style="color:#cbd5e1; text-decoration:none;">Perimeter Revision</a></li>
          </ul>
        </div>
        <div>
          <h4 style="color:#ffffff; font-size:1rem; font-weight:700; margin-bottom:14px;">English Revision</h4>
          <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:0.9rem;">
            <li><a href="functional-skills-english-level-2.html" style="color:#cbd5e1; text-decoration:none;">English Level 2 Directory</a></li>
            <li><a href="functional-skills-english-level-1.html" style="color:#cbd5e1; text-decoration:none;">English Level 1 Directory</a></li>
            <li><a href="reading-fact-or-opinion.html" style="color:#cbd5e1; text-decoration:none;">Fact or Opinion</a></li>
            <li><a href="writing-grammar.html" style="color:#cbd5e1; text-decoration:none;">Grammar &amp; Punctuation</a></li>
          </ul>
        </div>
        <div>
          <h4 style="color:#ffffff; font-size:1rem; font-weight:700; margin-bottom:14px;">Quick Links</h4>
          <ul style="list-style:none; padding:0; margin:0; line-height:2; font-size:0.9rem;">
            <li><a href="shop.html" style="color:#f59e0b; text-decoration:none; font-weight:700;"><i class="fa-solid fa-basket-shopping"></i> Learning Shop</a></li>
            <li><a href="functional-skills-past-papers.html" style="color:#cbd5e1; text-decoration:none;">Past Papers</a></li>
            <li><a href="diagnostic-test.html" style="color:#cbd5e1; text-decoration:none;">Diagnostic Assessment</a></li>
            <li><a href="bksb-remediation.html" style="color:#cbd5e1; text-decoration:none;">BKSB Remediation</a></li>
            <li><a href="contact-us.html" style="color:#cbd5e1; text-decoration:none;">Contact Support</a></li>
          </ul>
        </div>
      </div>
      <div style="border-top:1px solid rgba(255,255,255,0.1); padding:20px 0; text-align:center; font-size:0.84rem; color:#64748b;">
        &copy; 2026 Master Functional Skills. All rights reserved. Registered Provider for Ofqual Regulated Qualifications.
      </div>
    </div>
  </footer>

  <script src="assets/js/mfs-revision.js"></script>
</body>
</html>
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_out)

    print(f"[OK] Modernized {filename} ({len(html_out)} bytes)")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            extract_and_transform_page(f)
    else:
        extract_and_transform_page("functional-skills-perimeter.html")
