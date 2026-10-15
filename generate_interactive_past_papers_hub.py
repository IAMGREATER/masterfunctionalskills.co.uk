#!/usr/bin/env python3
"""
generate_interactive_past_papers_hub.py

Generates the interactive, ultra-fast Past Papers & Mocks landing page
for masterfunctionalskills.co.uk (past-papers.html & functional-skills-past-papers.html).

Matches the requested menu bar layout:
1. Awarding Bodies selector pills with official board logos
2. Subject & Level selector pills
3. Test Format selector pills (Paper & Mark Scheme vs Online Onscreen Test)
4. Search bar card (the moat) with keyword search, live counter, and clear button
5. Quick Filter chips (All Series, 2021-2023 Reform, Non-Calc, Calc, Reading, Writing, Online Tests, Practice Papers, Video Solutions)
6. Dynamic dedicated hub jump link banner
7. Instant past paper rows with direct PDF and simulator links
8. Preserves the traditional 5-subject directory cards below
"""

import os
import re
import glob

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
SYNC_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Load NAV_HEADER and FOOTER
with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    services_code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', services_code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', services_code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

# Awarding bodies configuration
BOARDS_CONFIG = [
    {"key": "edexcel", "name": "Edexcel", "full_name": "Pearson Edexcel", "logo": "assets/img/boards/edexcel.png", "badge_color": "#00b87c"},
    {"key": "city-and-guilds", "name": "City & Guilds", "full_name": "City & Guilds", "logo": "assets/img/boards/city-and-guilds.png", "badge_color": "#0284c7"},
    {"key": "aqa", "name": "AQA", "full_name": "AQA", "logo": "assets/img/boards/aqa.png", "badge_color": "#8b5cf6"},
    {"key": "ncfe", "name": "NCFE", "full_name": "NCFE", "logo": "assets/img/boards/ncfe.png", "badge_color": "#f59e0b"},
    {"key": "open-awards", "name": "Open Awards", "full_name": "Open Awards", "logo": "assets/img/boards/open-awards.png", "badge_color": "#d97706"},
    {"key": "tquk", "name": "TQUK", "full_name": "TQUK", "logo": "assets/img/boards/tquk.png", "badge_color": "#0d9488"},
    {"key": "nocn", "name": "NOCN", "full_name": "NOCN", "logo": "assets/img/boards/nocn.png", "badge_color": "#06b6d4"}
]

BOARD_LOOKUP = {b["key"]: b for b in BOARDS_CONFIG}

# Subjects configuration
SUBJECTS_CONFIG = [
    {
        "slug": "maths-level-2",
        "name": "Maths Level 2",
        "short_name": "Maths L2",
        "icon": "fa-solid fa-calculator",
        "color": "#0284c7",
        "hub_file": "functional-skills-maths-level-2-past-papers.html"
    },
    {
        "slug": "english-level-2",
        "name": "English Level 2",
        "short_name": "English L2",
        "icon": "fa-solid fa-pen-nib",
        "color": "#059669",
        "hub_file": "functional-skills-english-level-2-past-papers.html"
    },
    {
        "slug": "maths-level-1",
        "name": "Maths Level 1",
        "short_name": "Maths L1",
        "icon": "fa-solid fa-square-root-variable",
        "color": "#2563eb",
        "hub_file": "functional-skills-maths-level-1-past-papers.html"
    },
    {
        "slug": "english-level-1",
        "name": "English Level 1",
        "short_name": "English L1",
        "icon": "fa-solid fa-book",
        "color": "#d97706",
        "hub_file": "functional-skills-english-level-1-past-papers.html"
    },
    {
        "slug": "digital-skills",
        "name": "Digital Skills",
        "short_name": "Digital Skills",
        "icon": "fa-solid fa-laptop-code",
        "color": "#8b5cf6",
        "hub_file": "digital-functional-skills-past-papers.html"
    }
]

SUBJECT_LOOKUP = {s["slug"]: s for s in SUBJECTS_CONFIG}

def get_board_and_subject(fname):
    base = os.path.basename(fname).replace("-past-papers.html", "")
    for b in BOARD_LOOKUP:
        prefix = b + "-functional-skills-"
        if base.startswith(prefix):
            sub = base[len(prefix):]
            if sub in SUBJECT_LOOKUP:
                return b, sub
    return None, None

def clean_paper_title(title, search_term="", actions=""):
    boards = [
        'Pearson Edexcel', 'Edexcel', 'City and Guilds', 'City & Guilds', 'City &amp; Guilds',
        'AQA', 'NCFE', 'Open Awards', 'TQUK', 'NOCN'
    ]
    subjects = [
        'Functional Skills Maths Level 2', 'Functional Skills Maths Level 1',
        'Functional Skills English Level 2', 'Functional Skills English Level 1',
        'Functional Skills English Entry Level 3', 'Functional Skills Maths Entry Level 3',
        'Digital Functional Skills Level 1', 'Digital Functional Skills Entry Level 3',
        'Functional Skills Digital Skills', 'Functional Skills Maths', 'Functional Skills English',
        'Functional Skills', 'Maths Level 2', 'Maths Level 1', 'English Level 2', 'English Level 1'
    ]
    s = title
    for b in boards:
        s = re.sub(r'\b' + re.escape(b) + r'\b', '', s, flags=re.IGNORECASE)
    for subj in subjects:
        s = re.sub(r'\b' + re.escape(subj) + r'\b', '', s, flags=re.IGNORECASE)
    s = re.sub(r'^\s*[-:–—]\s*', '', s.strip())
    s = re.sub(r'\s+', ' ', s).strip()

    if s in ['Paper 1', 'Paper 2', 'Reading Paper', 'Writing Paper']:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december',
                  'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        month_map = {
            'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 'may': 'May', 'jun': 'June',
            'jul': 'July', 'aug': 'August', 'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December',
            'january': 'January', 'february': 'February', 'march': 'March', 'april': 'April', 'june': 'June',
            'july': 'July', 'august': 'August', 'september': 'September', 'october': 'October', 'november': 'November', 'december': 'December'
        }
        search_str = f"{search_term} {actions}"
        m_match = re.search(r'\b(' + '|'.join(months) + r')[-_ ]*(20\d\d)\b', search_str, re.IGNORECASE)
        if m_match:
            m_name = month_map[m_match.group(1).lower()]
            yr = m_match.group(2)
            s = f"{m_name} {yr} - {s}"
        else:
            y_match = re.search(r'\b(20\d\d)\b', search_str)
            if y_match:
                s = f"{y_match.group(1)} - {s}"
    return s if s else title

def parse_all_past_papers():
    """Extract all past paper rows across 28 board files and DFS."""
    files = glob.glob(os.path.join(PROJECT_DIR, "*-functional-skills-*-past-papers.html"))
    row_pattern = re.compile(
        r'<div class=\"past-paper-row\" data-search-term=\"(.*?)\">\s*'
        r'<div class=\"past-paper-meta\">\s*'
        r'<div class=\"past-paper-tags\">(.*?)</div>\s*'
        r'<h4 class=\"past-paper-title\">(.*?)</h4>\s*'
        r'</div>\s*'
        r'<div class=\"past-paper-actions\">(.*?)</div>\s*'
        r'</div>',
        re.DOTALL
    )

    all_papers = []

    for fpath in sorted(files):
        board_key, subj_slug = get_board_and_subject(fpath)
        if not board_key or not subj_slug:
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        matches = row_pattern.findall(content)
        for term, tags, title, actions in matches:
            tags = tags.replace(chr(92) + chr(34), '"')
            # 1. Clean and deduplicate actions
            a_tags = re.findall(r'<a\s+[^>]*>.*?</a>', actions, re.DOTALL)
            seen_hrefs = set()
            seen_labels = set()
            clean_actions_list = []
            
            for a_tag in a_tags:
                href_match = re.search(r'href=[\"\']([^\"\']+)[\"\']', a_tag)
                href = href_match.group(1).strip() if href_match else ""
                clean_text = re.sub(r'<[^>]+>', '', a_tag).strip()

                # Clean doubled class attributes
                a_tag_cleaned = re.sub(r'class=[\"\']([^\"\']+)[\"\']\s+class=[\"\']([^\"\']+)[\"\']', r'class="\1 \2"', a_tag)
                # Deduplicate class tokens
                a_tag_cleaned = re.sub(
                    r'class=[\"\']([^\"\']+)[\"\']',
                    lambda m: f'class="{" ".join(dict.fromkeys(m.group(1).split()))}"',
                    a_tag_cleaned
                )

                # Skip exact duplicate href
                if href and href in seen_hrefs:
                    continue

                # Skip duplicate action labels (e.g. duplicate Take Online Test or Question Paper)
                standard_labels = ["Take Online Test", "Question Paper", "Mark Scheme", "Model Solution", "Video Walkthrough", "Practice Paper (PDF)"]
                if clean_text in standard_labels:
                    if clean_text in seen_labels:
                        continue
                    seen_labels.add(clean_text)

                if href:
                    seen_hrefs.add(href)
                clean_actions_list.append(a_tag_cleaned)

            enriched_actions = "".join(clean_actions_list)

            # 2. Determine genuine format (online vs paper)
            is_xams = "xams.co.uk" in enriched_actions
            is_dfs = "digital-functional-skills-mock-exam" in enriched_actions or "Launch Simulator" in enriched_actions
            is_take_online = "Take Online Test" in enriched_actions and "functional-skills-courses" not in enriched_actions
            has_online = is_xams or is_dfs or is_take_online

            has_paper = (
                "btn-paper-qp" in enriched_actions or
                "btn-paper-ms" in enriched_actions or
                ".pdf" in enriched_actions.lower() or
                "Question Paper" in enriched_actions or
                "Practice Paper" in enriched_actions or
                "Reading Paper" in enriched_actions or
                "Writing Paper" in enriched_actions or
                "Mark Scheme" in enriched_actions or
                "Model Solution" in enriched_actions or
                "Source Insert" in enriched_actions
            )

            formats = []
            if has_paper:
                formats.append("paper")
            if has_online:
                formats.append("online")
            format_str = " ".join(formats) if formats else "paper"

            # 3. Clean search term: If not genuine online, remove bogus online search tokens
            if not has_online:
                clean_term = re.sub(r'\b(online test xams mock exam interactive onscreen|sit mock online)\b', '', term, flags=re.I).strip()
            else:
                clean_term = term

            subj_info = SUBJECT_LOOKUP[subj_slug]
            board_info = BOARD_LOOKUP[board_key]
            full_search = f"{clean_term} {subj_info['name']} {subj_info['short_name']} {board_info['name']} {board_info['full_name']} {format_str}".lower()
            full_search = " ".join(full_search.split())

            all_papers.append({
                "board": board_key,
                "subject": subj_slug,
                "format": format_str,
                "title": clean_paper_title(title.strip(), term, enriched_actions),
                "tags": tags.strip(),
                "actions": enriched_actions.strip(),
                "search_term": full_search
            })

    # Add 5 Pearson Edexcel Digital Functional Skills Mocks
    dfs_mocks = [
        {
            "board": "edexcel",
            "subject": "digital-skills",
            "format": "paper online",
            "title": "Mock 1: Fresh Bite Sandwich Shop (SAM)",
            "tags": '<span class="past-paper-tag-board">Edexcel</span><span class="past-paper-tag-spec">New 2023+ DFS Spec</span>',
            "actions": '<a href="assets/downloads/dfs/dfsq-l1-sam.pdf" target="_blank" rel="noopener" class="btn-paper btn-paper-qp"><i class="fa-regular fa-file-pdf"></i> Question Paper &amp; MS</a><a href="assets/downloads/dfs/dfs-level-1-sam-data-files.zip" class="btn-paper btn-paper-model" download><i class="fa-solid fa-file-zipper"></i> Data Files (.ZIP)</a><a href="digital-functional-skills-mock-exam.html?set=set1" class="btn-paper btn-paper-online"><i class="fa-solid fa-laptop-code"></i> Launch Simulator</a>',
            "search_term": "edexcel digital functional skills level 1 mock 1 fresh bite sandwich shop sam sample assessment materials data files zip online onscreen simulator paper online"
        },
        {
            "board": "edexcel",
            "subject": "digital-skills",
            "format": "paper online",
            "title": "Mock 2: Annual Awards Ceremony & Catering (Practice Set 2)",
            "tags": '<span class="past-paper-tag-board">Edexcel</span><span class="past-paper-tag-spec">New 2023+ DFS Spec</span>',
            "actions": '<a href="assets/downloads/dfs/dfs-level-1-practice-set-2-mark-scheme.pdf" target="_blank" rel="noopener" class="btn-paper btn-paper-qp"><i class="fa-regular fa-file-pdf"></i> Mark Scheme</a><a href="assets/downloads/dfs/dfs-level-1-practice-set-2-data-files.zip" class="btn-paper btn-paper-model" download><i class="fa-solid fa-file-zipper"></i> Data Files (.ZIP)</a><a href="digital-functional-skills-mock-exam.html?set=set2" class="btn-paper btn-paper-online"><i class="fa-solid fa-laptop-code"></i> Launch Simulator</a>',
            "search_term": "edexcel digital functional skills level 1 mock 2 annual awards ceremony catering practice set 2 data files zip online onscreen simulator paper online"
        },
        {
            "board": "edexcel",
            "subject": "digital-skills",
            "format": "paper online",
            "title": "Mock 3: First Aid Training & Supplies (Practice Set 1)",
            "tags": '<span class="past-paper-tag-board">Edexcel</span><span class="past-paper-tag-spec">New 2023+ DFS Spec</span>',
            "actions": '<a href="digital-functional-skills-mock-exam.html?set=set3" class="btn-paper btn-paper-qp"><i class="fa-solid fa-eye"></i> View Tasks Brief</a><a href="assets/downloads/dfs/dfs-l1-sample-assessment-materials.zip" class="btn-paper btn-paper-model" download><i class="fa-solid fa-file-zipper"></i> Practice Pack (.ZIP)</a><a href="digital-functional-skills-mock-exam.html?set=set3" class="btn-paper btn-paper-online"><i class="fa-solid fa-laptop-code"></i> Launch Simulator</a>',
            "search_term": "edexcel digital functional skills level 1 mock 3 first aid training supplies practice set 1 data files zip online onscreen simulator paper online"
        },
        {
            "board": "edexcel",
            "subject": "digital-skills",
            "format": "paper online",
            "title": "Mock 4: Gelato & Ice Cream Business (Past Test Set 1)",
            "tags": '<span class="past-paper-tag-board">Edexcel</span><span class="past-paper-tag-spec">New 2023+ DFS Spec</span>',
            "actions": '<a href="digital-functional-skills-mock-exam.html?set=set5" class="btn-paper btn-paper-qp"><i class="fa-solid fa-eye"></i> View Tasks Brief</a><a href="assets/downloads/dfs/dfs-level-1-sam-data-files.zip" class="btn-paper btn-paper-model" download><i class="fa-solid fa-file-zipper"></i> Data Files (.ZIP)</a><a href="digital-functional-skills-mock-exam.html?set=set5" class="btn-paper btn-paper-online"><i class="fa-solid fa-laptop-code"></i> Launch Simulator</a>',
            "search_term": "edexcel digital functional skills level 1 mock 4 gelato ice cream business past test set 1 data files zip online onscreen simulator paper online"
        },
        {
            "board": "edexcel",
            "subject": "digital-skills",
            "format": "paper online",
            "title": "Entry Level 3 - Apprenticeships & Work Experience (SAM)",
            "tags": '<span class="past-paper-tag-board">Edexcel</span><span class="past-paper-tag-spec">New 2023+ DFS Spec</span>',
            "actions": '<a href="assets/downloads/dfs/dfsq-e3-sam.pdf" target="_blank" rel="noopener" class="btn-paper btn-paper-qp"><i class="fa-regular fa-file-pdf"></i> Question Paper &amp; MS</a><a href="assets/downloads/dfs/dfsq-entry-level-3-sam-data-files.zip" class="btn-paper btn-paper-model" download><i class="fa-solid fa-file-zipper"></i> Data Files (.ZIP)</a><a href="digital-functional-skills-mock-exam.html?set=set4" class="btn-paper btn-paper-online"><i class="fa-solid fa-laptop-code"></i> Launch Simulator</a>',
            "search_term": "edexcel digital functional skills entry level 3 e3 apprenticeships work experience sam sample assessment data files zip online onscreen simulator paper online"
        }
    ]

    all_papers.extend(dfs_mocks)
    return all_papers

def generate_paper_sections_html(papers):
    groups = {}
    for p in papers:
        key = (p["subject"], p["board"])
        if key not in groups:
            groups[key] = []
        groups[key].append(p)

    sections_html = []

    for subj in SUBJECTS_CONFIG:
        s_slug = subj["slug"]
        for board in BOARDS_CONFIG:
            b_key = board["key"]
            key = (s_slug, b_key)
            if key not in groups or not groups[key]:
                continue

            group_papers = groups[key]
            group_count = len(group_papers)
            b_name = board["name"]
            s_name = subj["name"]

            if s_slug == "digital-skills":
                dedicated_link = "digital-functional-skills-past-papers.html"
            else:
                dedicated_link = f"{b_key}-functional-skills-{s_slug}-past-papers.html"

            sec_html = f'''
      <section class="paper-group-section" data-subject="{s_slug}" data-board="{b_key}">
        <div class="paper-group-header">
          <h3 class="paper-group-title">
            <img src="{board['logo']}" alt="{b_name} Logo" class="paper-group-board-logo" style="height:68px; max-width:220px; object-fit:contain; border-radius:10px; vertical-align:middle; background:#ffffff; padding:6px 14px; border:2px solid #cbd5e1; box-shadow:0 3px 8px rgba(15,23,42,0.08); display:inline-block;">
            <span>{s_name}</span>
          </h3>
          <div style="display:flex; align-items:center; gap:12px;">
            <a href="{dedicated_link}" class="btn-paper btn-paper-qp" style="font-size:0.78rem; padding:4px 10px;" title="Open complete dedicated hub for {b_name} {s_name}">
              View Dedicated Board Hub &rarr;
            </a>
            <span class="paper-group-count">{group_count} Papers</span>
          </div>
        </div>
        <div class="paper-group-list">
'''
            for p in group_papers:
                s_key = "maths" if "maths" in p["subject"] else ("english" if "english" in p["subject"] else "digital")
                b_key = p["board"]
                board_name = BOARD_LOOKUP[b_key]["name"]

                # Extract spec tag cleanly if present
                spec_match = re.search(r'class=[\"\']?past-paper-tag-spec[\"\']?>([^<]+)</span>', p.get("tags", ""))
                spec_text = spec_match.group(1).strip() if spec_match else ("New 2023+ DFS Spec" if "digital" in p["subject"] else "New 2019+ Reform Spec")

                board_tag = f'<span class="past-paper-tag-board tag-board-{b_key}">{board_name}</span>'
                subj_tag = f'<span class="past-paper-tag-subject tag-subject-{s_key}">{subj["short_name"]}</span>'
                spec_tag = f'<span class="past-paper-tag-spec">{spec_text}</span>' if spec_text else ''
                tags_clean = f'{board_tag}{subj_tag}{spec_tag}'

                sec_html += f'''          <div class="past-paper-row" data-search-term="{p['search_term']}" data-subject="{p['subject']}" data-board="{p['board']}" data-format="{p['format']}">
            <div class="past-paper-meta">
              <div class="past-paper-tags">
                {tags_clean}
              </div>
              <h4 class="past-paper-title">{p['title']}</h4>
            </div>
            <div class="past-paper-actions">
              {p['actions']}
            </div>
          </div>
'''
            sec_html += '''        </div>
      </section>
'''
            sections_html.append(sec_html)

    return "\n".join(sections_html)

def build_interactive_past_papers_page():
    all_papers = parse_all_past_papers()
    total_papers = len(all_papers)
    sections_html = generate_paper_sections_html(all_papers)

    # HEAD HTML
    head_html = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Past Papers &amp; Official Mark Schemes | Master Functional Skills</title>
  <meta name="description" content="Download free genuine past papers, official mark schemes, and sit interactive online mock tests for Pearson Edexcel, City &amp; Guilds, Open Awards, NCFE, and AQA Functional Skills Maths, English, and Digital Skills.">
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="alternate icon" href="favicon.ico">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- CUSTOM FINDER STYLING TO MATCH UPLOADED DESIGN EXACTLY -->
  <style>
    /* Finder Container Section */
    .past-papers-finder-section {
      padding: 10px 0 40px;
    }
    .mfs-finder-card {
      background: var(--bg-card, #ffffff);
      border: 1px solid var(--border, #e2e8f0);
      border-radius: 20px;
      padding: 24px 28px;
      box-shadow: 0 6px 24px rgba(7, 13, 30, 0.05);
      margin-bottom: 28px;
    }

    /* Row Label Styling */
    .finder-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 0;
      flex-wrap: wrap;
    }
    .finder-row-divider {
      margin: 14px 0 16px 0;
      border: none;
      border-top: 1px solid var(--border, #e2e8f0);
      width: 100%;
    }
    .finder-row-label {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--navy-dark, #070d1e);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-width: 175px;
    }

    /* Interactive Pills */
    .finder-pills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .finder-pill {
      font-size: 0.82rem;
      font-weight: 700;
      color: #0f172a !important;
      padding: 7px 16px;
      border-radius: 9999px;
      background: #fdeedb; /* warm cream/peach tint matching screenshot */
      border: 1px solid #fed7aa;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap;
      cursor: pointer;
      font-family: inherit;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      user-select: none;
    }
    .finder-pill:hover {
      background: #fed7aa;
      border-color: #fdba74;
      transform: translateY(-1px);
    }
    .finder-pill.active {
      background: #1d4ed8 !important; /* solid royal blue as in screenshot */
      color: #ffffff !important;
      border-color: #1d4ed8 !important;
      box-shadow: 0 3px 10px rgba(29, 78, 216, 0.35);
    }
    .finder-pill.active i,
    .finder-pill.active span {
      color: #ffffff !important;
    }
    .finder-pill img {
      width: 18px;
      height: 18px;
      border-radius: 4px;
      object-fit: contain;
      background: #ffffff;
      vertical-align: middle;
      padding: 1px;
    }
    .finder-pill.active img {
      background: #ffffff;
    }

    /* Outline Pill for All / Reset */
    .finder-pill.pill-outline {
      background: transparent;
      border: 1.5px solid #0f172a;
      color: #0f172a !important;
    }
    .finder-pill.pill-outline:hover {
      background: #0f172a;
      color: #ffffff !important;
    }
    .finder-pill.pill-outline.active {
      background: #0f172a !important;
      color: #ffffff !important;
      border-color: #0f172a !important;
    }

    /* Awarding Bodies Big Tile Selector */
    .finder-board-section {
      width: 100%;
      margin-bottom: 6px;
    }
    .finder-board-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .finder-all-hubs-link {
      font-size: 0.82rem;
      font-weight: 700;
      color: #1d4ed8;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 5px 12px;
      border-radius: 8px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      transition: all 0.15s ease;
    }
    .finder-all-hubs-link:hover {
      background: #dbeafe;
      color: #1e40af;
      transform: translateY(-1px);
    }
    .finder-board-tiles {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 12px;
      width: 100%;
    }
    .finder-board-tile {
      background: #ffffff !important;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      height: 78px;
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
      outline: none;
      user-select: none;
      font-family: inherit;
      text-decoration: none;
    }
    .finder-board-tile:hover {
      border-color: #93c5fd;
      transform: translateY(-2px);
      box-shadow: 0 8px 18px rgba(37, 99, 235, 0.12);
    }
    .finder-board-tile.active {
      border-color: #2563eb !important;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.25), 0 8px 20px rgba(37, 99, 235, 0.16) !important;
      transform: translateY(-2px);
    }
    .finder-board-tile.active::after {
      content: "\\f058";
      font-family: "Font Awesome 6 Free";
      font-weight: 900;
      position: absolute;
      top: 5px;
      right: 6px;
      font-size: 0.82rem;
      color: #2563eb;
      line-height: 1;
    }
    .finder-board-tile img {
      max-width: 100%;
      max-height: 48px;
      width: auto;
      height: auto;
      object-fit: contain;
      pointer-events: none;
      transition: transform 0.2s ease;
      filter: contrast(1.02);
      display: block;
    }
    .finder-board-tile:hover img {
      transform: scale(1.04);
    }
    .finder-board-tile[data-board="tquk"] img {
      max-height: 50px;
    }
    /* All Boards Tile */
    .board-tile-all {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 5px;
      color: #1e293b;
      transition: color 0.15s ease;
    }
    .board-tile-all i {
      font-size: 1.3rem;
      color: #2563eb;
      transition: transform 0.2s ease;
    }
    .finder-board-tile:hover .board-tile-all i {
      transform: scale(1.1);
    }
    .board-tile-all span {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.2px;
      white-space: nowrap;
    }
    .finder-board-tile.active .board-tile-all {
      color: #1d4ed8;
    }
    .finder-board-tile.active .board-tile-all i {
      color: #1d4ed8;
    }

    @media (max-width: 1100px) {
      .finder-board-tiles {
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
      }
    }
    @media (max-width: 600px) {
      .finder-board-tiles {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
      }
      .finder-board-tile {
        height: 66px;
        padding: 6px 10px;
      }
      .finder-board-tile img {
        max-height: 38px;
      }
    }

    /* Search Bar Card Container */
    .paper-filter-bar {
      background: var(--bg-card, #ffffff);
      border: 1.5px solid var(--border, #e2e8f0);
      border-radius: 18px;
      padding: 16px 20px;
      box-shadow: 0 4px 16px rgba(7, 13, 30, 0.04);
      margin: 18px 0 12px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .paper-search-wrap {
      position: relative;
      flex: 1;
      min-width: 260px;
    }
    .paper-search-wrap i {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: #64748b;
      font-size: 1rem;
    }
    .paper-search-input {
      width: 100%;
      padding: 13px 18px 13px 44px;
      border-radius: 100px;
      border: 1.5px solid #fed7aa;
      background: #fdeddc; /* soft warm cream input background */
      font-size: 0.95rem;
      font-weight: 500;
      color: #0f172a;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .paper-search-input:focus {
      border-color: #1d4ed8;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.15);
    }
    .paper-search-input::placeholder {
      color: #64748b;
    }

    /* Counter Pill */
    .paper-counter-pill {
      font-size: 0.88rem;
      font-weight: 800;
      color: #065f46;
      background: #dcfce7; /* mint green */
      border: 1.5px solid #86efac;
      padding: 9px 18px;
      border-radius: 100px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }
    .paper-counter-pill i {
      color: #059669;
    }

    /* Quick Filter Chips */
    .paper-filter-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
      align-items: center;
    }
    .filter-chip-label {
      font-size: 0.78rem;
      font-weight: 800;
      color: #475569;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      margin-right: 4px;
    }
    .filter-chip {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: #1e293b;
      border-radius: 100px;
      padding: 6px 16px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
      user-select: none;
    }
    .filter-chip:hover {
      border-color: #1d4ed8;
      color: #1d4ed8;
    }
    .filter-chip.active {
      background: #0f172a;
      color: #ffffff;
      border-color: #0f172a;
      font-weight: 700;
    }

    /* Dynamic Hub Link Banner */
    .dynamic-hub-banner {
      background: linear-gradient(135deg, #0c1938 0%, #1e3a8a 100%);
      border-radius: 14px;
      padding: 14px 22px;
      margin-top: 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      color: #ffffff;
      border-left: 4px solid var(--accent, #00b87c);
      animation: fadeIn 0.2s ease;
    }
    .dynamic-hub-text {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.95rem;
      font-weight: 600;
      flex: 1;
    }
    .dynamic-hub-text strong {
      color: #38bdf8;
      font-weight: 800;
    }
    .dynamic-hub-btn {
      background: #00b87c;
      color: #ffffff !important;
      padding: 9px 20px;
      border-radius: 100px;
      font-weight: 700;
      font-size: 0.88rem;
      text-decoration: none;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      box-shadow: 0 4px 12px rgba(0, 184, 124, 0.35);
    }
    .dynamic-hub-btn:hover {
      background: #009966;
      transform: translateY(-1px);
    }

    /* Tag and Button Accents */
    .past-paper-tag-board {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-block;
      line-height: 1.3;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .past-paper-tag-subject {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-block;
      line-height: 1.3;
      white-space: nowrap;
      transition: all 0.15s ease;
    }

    /* 1. Exam Board Specific Highlights */
    .past-paper-tag-board.tag-board-edexcel,
    .past-paper-row[data-board="edexcel"] .past-paper-tag-board {
      background: #ecfdf5 !important;
      color: #047857 !important;
      border: 1px solid #a7f3d0 !important;
    }
    .past-paper-tag-board.tag-board-city-and-guilds,
    .past-paper-row[data-board="city-and-guilds"] .past-paper-tag-board {
      background: #fff1f2 !important;
      color: #be123c !important;
      border: 1px solid #fecdd3 !important;
    }
    .past-paper-tag-board.tag-board-aqa,
    .past-paper-row[data-board="aqa"] .past-paper-tag-board {
      background: #eef2ff !important;
      color: #3730a3 !important;
      border: 1px solid #c7d2fe !important;
    }
    .past-paper-tag-board.tag-board-ncfe,
    .past-paper-row[data-board="ncfe"] .past-paper-tag-board {
      background: #fffbeb !important;
      color: #b45309 !important;
      border: 1px solid #fde68a !important;
    }
    .past-paper-tag-board.tag-board-open-awards,
    .past-paper-row[data-board="open-awards"] .past-paper-tag-board {
      background: #fff7ed !important;
      color: #c2410c !important;
      border: 1px solid #fed7aa !important;
    }
    .past-paper-tag-board.tag-board-tquk,
    .past-paper-row[data-board="tquk"] .past-paper-tag-board {
      background: #fdf2f8 !important;
      color: #9d174d !important;
      border: 1px solid #fbcfe8 !important;
    }
    .past-paper-tag-board.tag-board-nocn,
    .past-paper-row[data-board="nocn"] .past-paper-tag-board {
      background: #f0fdfa !important;
      color: #0f766e !important;
      border: 1px solid #99f6e4 !important;
    }

    /* 2. Subject Specific Highlights (Matched to Revise Page Accents) */
    /* Maths (Levels 1 & 2): Royal Oxford Sapphire */
    .past-paper-tag-subject.tag-subject-maths,
    .past-paper-row[data-subject*="maths"] .past-paper-tag-subject {
      background: #eff6ff !important;
      color: #1d4ed8 !important;
      border: 1px solid #bfdbfe !important;
    }
    /* English (Levels 1 & 2): Imperial Royal Violet */
    .past-paper-tag-subject.tag-subject-english,
    .past-paper-row[data-subject*="english"] .past-paper-tag-subject {
      background: #f5f3ff !important;
      color: #6d28d9 !important;
      border: 1px solid #ddd6fe !important;
    }
    /* Digital Skills (Level 1 & E3): Modern Tech Cyan */
    .past-paper-tag-subject.tag-subject-digital,
    .past-paper-row[data-subject*="digital"] .past-paper-tag-subject {
      background: #ecfeff !important;
      color: #0e7490 !important;
      border: 1px solid #a5f3fc !important;
    }
    .btn-paper-online {
      background: #2563eb !important;
      color: #ffffff !important;
      border: 1px solid #1d4ed8 !important;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
    }
    .btn-paper-online:hover {
      background: #1d4ed8 !important;
      color: #ffffff !important;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>"""

    # HERO SECTION HTML
    hero_section_html = """  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>Functional Skills <span>Past Papers</span></h1>
        <p class="hero-description">
          Access genuine Functional Skills past papers, official mark schemes, and video model solutions for Pearson Edexcel, City &amp; Guilds, Open Awards, NCFE, and AQA. Filter instantly below by subject, awarding exam board, or test format (Paper PDF vs Online Onscreen Test).
        </p>

        <!-- WHAT TO ADD (YOUR MOAT) -->
        <div class="moat-strip">
          <span class="moat-badge"><i class="fa-solid fa-bolt"></i> 1-Click Direct PDF Open (No Paywalls)</span>
          <span class="moat-badge"><i class="fa-solid fa-universal-access"></i> Dyslexia-Friendly Layout</span>
          <span class="moat-badge"><i class="fa-solid fa-magnifying-glass"></i> Instant Year &amp; Series Search</span>
          <span class="moat-badge"><i class="fa-solid fa-certificate"></i> Official Awarding Body Specs</span>
        </div>

        <div class="hero-reviews-bar">
          <div class="star-rating">
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star"></i>
            <i class="fa-solid fa-star-half-stroke"></i>
          </div>
          <div class="reviews-stat">
            Over <strong>50,000+ past paper practice downloads</strong> this year
          </div>
        </div>

        <div class="hero-buttons">
          <a href="#mock-finder" class="btn-hero-accent"><i class="fa-solid fa-bolt"></i> Instant Mock Finder</a>
          <a href="#subjects-grid" class="btn-hero-outline"><i class="fa-solid fa-layer-group"></i> View by Subject</a>
          <a href="functional-skills-maths-level-2.html" class="btn-hero-navy"><i class="fa-solid fa-calculator"></i> Maths Revision</a>
          <a href="functional-skills-english-level-2.html" class="btn-hero-navy"><i class="fa-solid fa-pen-nib"></i> English Revision</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/adult-student-smiling.jpg" alt="Successful adult learner studying Functional Skills" style="height:220px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-graduation-cap"></i></div>
            <div>
              <strong>Complete National Past Paper Archive</strong>
              <span>Maths &amp; English • Levels 1 &amp; 2 • All Awarding Bodies</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""

    # FINDER SECTION HTML
    finder_section_html = f"""  <!-- FAST MOCK & PAST PAPER FINDER (INTERACTIVE MOAT) -->
  <section class="past-papers-finder-section" id="mock-finder">
    <div class="mfs-container">
      
      <div class="mfs-finder-card">
        
        <!-- TOP: SEARCH BAR & QUICK FILTERS -->
        <!-- SEARCH BAR CARD -->
        <div class="paper-filter-bar">
          <div class="paper-search-wrap">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input type="text" id="paperSearchInput" class="paper-search-input" placeholder="Search papers by series (e.g. 2023, June, Non-Calc, Calc, Sample)...">
            <button type="button" id="clearSearchBtn" style="display:none; background:none; border:none; color:var(--text-muted); cursor:pointer; padding:6px 12px; font-size:1.1rem; position:absolute; right:12px; top:50%; transform:translateY(-50%);" title="Clear search">
              <i class="fa-solid fa-xmark"></i>
            </button>
          </div>
          <div class="paper-counter-pill">
            <i class="fa-solid fa-file-pdf"></i>
            <span>Showing <strong id="visiblePapersCount">{total_papers}</strong> of {total_papers} Papers</span>
          </div>
        </div>

        <!-- QUICK FILTER CHIPS -->
        <div class="paper-filter-chips">
          <span class="filter-chip-label"><i class="fa-solid fa-sliders"></i> Filter:</span>
          <button type="button" class="filter-chip active" data-filter="">All Series</button>
          <button type="button" class="filter-chip" data-filter="2023|2022|2021">2021–2023 Reform</button>
          <button type="button" class="filter-chip" data-filter="non-calc|non calc|section a">Non-Calculator</button>
          <button type="button" class="filter-chip" data-filter="calc|section b">Calculator</button>
          <button type="button" class="filter-chip" data-filter="reading">Reading</button>
          <button type="button" class="filter-chip" data-filter="writing">Writing</button>
          <button type="button" class="filter-chip" data-filter="online|xams|simulator">Online Tests</button>
          <button type="button" class="filter-chip" data-filter="sample|practice|specimen">Practice Papers</button>
          <button type="button" class="filter-chip" data-filter="video|walkthrough">Video Solutions</button>
        </div>

        <!-- GAP & DIVIDER LINE -->
        <div class="finder-section-divider" style="margin: 24px 0 26px 0; border: none; border-top: 1.5px solid var(--border, #cbd5e1); width: 100%;"></div>

        <!-- SELECTION CRITERIA: AWARDING BODIES -->
        <div class="finder-board-section">
          <div class="finder-board-header">
            <span class="finder-row-label">
              <i class="fa-solid fa-building-columns" style="color:#2563eb;"></i> Awarding Bodies:
            </span>
            <a href="revise.html" class="finder-all-hubs-link">
              All Level 2 &amp; 1 Hubs &rarr;
            </a>
          </div>
          <div class="finder-board-tiles" id="boardFilterPills">
            <button type="button" class="finder-board-tile active" data-board="" title="All Awarding Bodies" aria-label="All Awarding Bodies">
              <div class="board-tile-all">
                <i class="fa-solid fa-layer-group"></i>
                <span>All Boards</span>
              </div>
            </button>
            <button type="button" class="finder-board-tile" data-board="edexcel" title="Pearson Edexcel" aria-label="Pearson Edexcel">
              <img src="assets/img/boards/edexcel.png" alt="Pearson Edexcel">
            </button>
            <button type="button" class="finder-board-tile" data-board="city-and-guilds" title="City &amp; Guilds" aria-label="City &amp; Guilds">
              <img src="assets/img/boards/city-and-guilds.png" alt="City &amp; Guilds">
            </button>
            <button type="button" class="finder-board-tile" data-board="aqa" title="AQA" aria-label="AQA">
              <img src="assets/img/boards/aqa.png" alt="AQA">
            </button>
            <button type="button" class="finder-board-tile" data-board="ncfe" title="NCFE" aria-label="NCFE">
              <img src="assets/img/boards/ncfe.png" alt="NCFE">
            </button>
            <button type="button" class="finder-board-tile" data-board="open-awards" title="Open Awards" aria-label="Open Awards">
              <img src="assets/img/boards/open-awards.png" alt="Open Awards">
            </button>
            <button type="button" class="finder-board-tile" data-board="tquk" title="TQUK" aria-label="TQUK">
              <img src="assets/img/boards/tquk.png" alt="TQUK">
            </button>
            <button type="button" class="finder-board-tile" data-board="nocn" title="NOCN" aria-label="NOCN">
              <img src="assets/img/boards/nocn.png" alt="NOCN">
            </button>
          </div>
        </div>

        <!-- DIVIDER LINE -->
        <div class="finder-row-divider" style="margin: 18px 0 16px 0; border: none; border-top: 1px solid var(--border, #e2e8f0); width: 100%;"></div>

        <!-- SELECTION CRITERIA: SUBJECT & LEVEL -->
        <div class="finder-row">
          <span class="finder-row-label">
            <i class="fa-solid fa-graduation-cap" style="color:#059669;"></i> Subject &amp; Level:
          </span>
          <div class="finder-pills" id="subjectFilterPills">
            <button type="button" class="finder-pill active" data-subject="">
              <i class="fa-solid fa-book-open" style="font-size:0.8rem; margin-right:2px;"></i> All Subjects
            </button>
            <button type="button" class="finder-pill" data-subject="maths-level-2">
              <i class="fa-solid fa-calculator" style="color:#0284c7;"></i> Maths Level 2
            </button>
            <button type="button" class="finder-pill" data-subject="english-level-2">
              <i class="fa-solid fa-pen-nib" style="color:#059669;"></i> English Level 2
            </button>
            <button type="button" class="finder-pill" data-subject="maths-level-1">
              <i class="fa-solid fa-square-root-variable" style="color:#2563eb;"></i> Maths Level 1
            </button>
            <button type="button" class="finder-pill" data-subject="english-level-1">
              <i class="fa-solid fa-book" style="color:#d97706;"></i> English Level 1
            </button>
            <button type="button" class="finder-pill" data-subject="digital-skills">
              <i class="fa-solid fa-laptop-code" style="color:#8b5cf6;"></i> Digital Skills
            </button>
          </div>
        </div>

        <!-- DIVIDER LINE -->
        <div class="finder-row-divider" style="margin: 14px 0 16px 0; border: none; border-top: 1px solid var(--border, #e2e8f0); width: 100%;"></div>

        <!-- SELECTION CRITERIA: TEST FORMAT -->
        <div class="finder-row">
          <span class="finder-row-label">
            <i class="fa-solid fa-laptop-file" style="color:#8b5cf6;"></i> Test Format:
          </span>
          <div class="finder-pills" id="formatFilterPills">
            <button type="button" class="finder-pill active" data-format="">
              <i class="fa-solid fa-list-check" style="font-size:0.8rem; margin-right:2px;"></i> All Formats
            </button>
            <button type="button" class="finder-pill" data-format="paper">
              <i class="fa-regular fa-file-pdf" style="color:#dc2626;"></i> Paper Test
            </button>
            <button type="button" class="finder-pill" data-format="online">
              <i class="fa-solid fa-laptop-code" style="color:#2563eb;"></i> Online test
            </button>
          </div>
        </div>

        <!-- DYNAMIC DEDICATED HUB JUMP LINK BANNER -->
        <div id="dynamicHubBanner" class="dynamic-hub-banner" style="display:none;">
          <div class="dynamic-hub-text">
            <i class="fa-solid fa-compass" style="color:var(--accent);"></i>
            <span id="dynamicHubLabel">Looking for the dedicated hub?</span>
          </div>
          <a id="dynamicHubLink" href="#" class="dynamic-hub-btn">
            Open Dedicated Hub &rarr;
          </a>
        </div>

      </div>

      <!-- PAPERS DIRECTORY (DISPLAYING THE MATCHED PAPERS INSTANTLY) -->
      <div id="papersDirectory">
{sections_html}
      </div>

      <!-- ZERO RESULTS EMPTY STATE -->
      <div id="noPapersNotice" style="display:none; text-align:center; padding: 48px 24px; background:#ffffff; border-radius:16px; border:1px solid var(--border); margin-top:24px;">
        <i class="fa-solid fa-folder-open" style="font-size:3rem; color:var(--text-muted); margin-bottom:12px;"></i>
        <h3 style="color:var(--navy); font-size:1.3rem;">No past papers match your current filters</h3>
        <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:16px;">Try clearing your search keyword or switching awarding bodies and test formats.</p>
        <button type="button" class="btn-hero-accent" onclick="resetAllFinderFilters()" style="padding:10px 24px; cursor:pointer;">
          <i class="fa-solid fa-rotate-left"></i> Reset All Filters
        </button>
      </div>

    </div>
  </section>"""

    # TRADITIONAL SUBJECT CARDS HTML (WITH DIGITAL SKILLS INCLUDED)
    subj_section_html = """  <!-- SUBJECTS DIRECTORY -->
  <section class="mfs-features-section" id="subjects-grid">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Functional Skills Past Papers by Subject &amp; Level</h2>
        <p>Each hub contains all regulated awarding bodies (Edexcel, City &amp; Guilds, NCFE, AQA, Open Awards, TQUK, NOCN) and their full past papers archive.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px; margin-top:32px;">
        
        <!-- Maths Level 2 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-calculator"></i>
            </div>
            <span style="background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">7 Exam Boards</span>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Functional Skills Maths Level 2</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Free past papers and mark schemes for Pearson Edexcel, City &amp; Guilds, Open Awards, NCFE, AQA, TQUK, and NOCN. Non-calc and calculator sections included.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Question Papers &amp; Mark Schemes</span>
            <a href="functional-skills-maths-level-2-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards &rarr;</a>
          </div>
        </div>

        <!-- English Level 2 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-pen-nib"></i>
            </div>
            <span style="background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">7 Exam Boards</span>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Functional Skills English Level 2</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Official Reading, Writing, and Speaking assessment papers, source texts, mark schemes, and examiner criteria for all major UK awarding organisations.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Reading &amp; Writing Papers</span>
            <a href="functional-skills-english-level-2-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards &rarr;</a>
          </div>
        </div>

        <!-- Maths Level 1 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-square-root-variable"></i>
            </div>
            <span style="background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">7 Exam Boards</span>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Functional Skills Maths Level 1</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Authentic Level 1 Maths past papers and mark schemes from Pearson Edexcel, City &amp; Guilds, NCFE, Open Awards, and AQA to build confidence for your test.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Question Papers &amp; Answers</span>
            <a href="functional-skills-maths-level-1-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards &rarr;</a>
          </div>
        </div>

        <!-- English Level 1 Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(0,184,124,0.1); color:var(--accent); display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-book"></i>
            </div>
            <span style="background:rgba(0,184,124,0.12); color:var(--accent); font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">7 Exam Boards</span>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Functional Skills English Level 1</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Past papers for Level 1 English reading comprehension and writing tasks with complete assessment criteria across all regulated awarding bodies.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Reading &amp; Writing Papers</span>
            <a href="functional-skills-english-level-1-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards &rarr;</a>
          </div>
        </div>

        <!-- Digital Skills Card -->
        <div style="background:#ffffff; border-radius:16px; border:1px solid var(--border); padding:32px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:rgba(139,92,246,0.1); color:#8b5cf6; display:flex; align-items:center; justify-content:center; font-size:1.4rem;">
              <i class="fa-solid fa-laptop-code"></i>
            </div>
            <span style="background:rgba(139,92,246,0.12); color:#8b5cf6; font-weight:700; font-size:0.75rem; padding:4px 10px; border-radius:100px;">Level 1 &amp; Entry 3</span>
          </div>
          <h3 style="font-size:1.35rem; font-weight:800; color:var(--navy); margin-bottom:8px;">Digital Functional Skills</h3>
          <p style="color:var(--text-muted); font-size:0.92rem; line-height:1.6; margin-bottom:20px;">
            Pearson Edexcel sample assessment materials, candidate data files (.ZIP), and official interactive onscreen exam simulators.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Papers &amp; Onscreen Simulators</span>
            <a href="digital-functional-skills-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Digital Papers &rarr;</a>
          </div>
        </div>

      </div>
    </div>
  </section>"""

    # LIVE FILTER SCRIPT
    filter_script_html = """  <!-- LIVE INSTANT MOCK FINDER ENGINE (0ms LATENCY) -->
  <script>
    (function() {
      const searchInput = document.getElementById("paperSearchInput");
      const clearBtn = document.getElementById("clearSearchBtn");
      const boardPills = document.querySelectorAll("#boardFilterPills [data-board]");
      const subjectPills = document.querySelectorAll("#subjectFilterPills .finder-pill[data-subject]");
      const formatPills = document.querySelectorAll("#formatFilterPills .finder-pill[data-format]");
      const chips = document.querySelectorAll(".paper-filter-chips .filter-chip");
      const rows = document.querySelectorAll(".past-paper-row");
      const sections = document.querySelectorAll(".paper-group-section");
      const counterEl = document.getElementById("visiblePapersCount");
      const noNotice = document.getElementById("noPapersNotice");
      const hubBanner = document.getElementById("dynamicHubBanner");
      const hubLabel = document.getElementById("dynamicHubLabel");
      const hubLink = document.getElementById("dynamicHubLink");

      let selectedBoard = "";
      let selectedSubject = "";
      let selectedFormat = "";
      let selectedChip = "";

      const HUB_MAP = {
        "maths-level-2": {
          "": { title: "Maths Level 2 Past Papers Hub", url: "functional-skills-maths-level-2-past-papers.html" },
          "edexcel": { title: "Pearson Edexcel Maths Level 2 Hub", url: "edexcel-functional-skills-maths-level-2-past-papers.html" },
          "city-and-guilds": { title: "City & Guilds Maths Level 2 Hub", url: "city-and-guilds-functional-skills-maths-level-2-past-papers.html" },
          "aqa": { title: "AQA Maths Level 2 Hub", url: "aqa-functional-skills-maths-level-2-past-papers.html" },
          "ncfe": { title: "NCFE Maths Level 2 Hub", url: "ncfe-functional-skills-maths-level-2-past-papers.html" },
          "open-awards": { title: "Open Awards Maths Level 2 Hub", url: "open-awards-functional-skills-maths-level-2-past-papers.html" },
          "tquk": { title: "TQUK Maths Level 2 Hub", url: "tquk-functional-skills-maths-level-2-past-papers.html" },
          "nocn": { title: "NOCN Maths Level 2 Hub", url: "nocn-functional-skills-maths-level-2-past-papers.html" }
        },
        "english-level-2": {
          "": { title: "English Level 2 Past Papers Hub", url: "functional-skills-english-level-2-past-papers.html" },
          "edexcel": { title: "Pearson Edexcel English Level 2 Hub", url: "edexcel-functional-skills-english-level-2-past-papers.html" },
          "city-and-guilds": { title: "City & Guilds English Level 2 Hub", url: "city-and-guilds-functional-skills-english-level-2-past-papers.html" },
          "aqa": { title: "AQA English Level 2 Hub", url: "aqa-functional-skills-english-level-2-past-papers.html" },
          "ncfe": { title: "NCFE English Level 2 Hub", url: "ncfe-functional-skills-english-level-2-past-papers.html" },
          "open-awards": { title: "Open Awards English Level 2 Hub", url: "open-awards-functional-skills-english-level-2-past-papers.html" },
          "tquk": { title: "TQUK English Level 2 Hub", url: "tquk-functional-skills-english-level-2-past-papers.html" },
          "nocn": { title: "NOCN English Level 2 Hub", url: "nocn-functional-skills-english-level-2-past-papers.html" }
        },
        "maths-level-1": {
          "": { title: "Maths Level 1 Past Papers Hub", url: "functional-skills-maths-level-1-past-papers.html" },
          "edexcel": { title: "Pearson Edexcel Maths Level 1 Hub", url: "edexcel-functional-skills-maths-level-1-past-papers.html" },
          "city-and-guilds": { title: "City & Guilds Maths Level 1 Hub", url: "city-and-guilds-functional-skills-maths-level-1-past-papers.html" },
          "aqa": { title: "AQA Maths Level 1 Hub", url: "aqa-functional-skills-maths-level-1-past-papers.html" },
          "ncfe": { title: "NCFE Maths Level 1 Hub", url: "ncfe-functional-skills-maths-level-1-past-papers.html" },
          "open-awards": { title: "Open Awards Maths Level 1 Hub", url: "open-awards-functional-skills-maths-level-1-past-papers.html" },
          "tquk": { title: "TQUK Maths Level 1 Hub", url: "tquk-functional-skills-maths-level-1-past-papers.html" },
          "nocn": { title: "NOCN Maths Level 1 Hub", url: "nocn-functional-skills-maths-level-1-past-papers.html" }
        },
        "english-level-1": {
          "": { title: "English Level 1 Past Papers Hub", url: "functional-skills-english-level-1-past-papers.html" },
          "edexcel": { title: "Pearson Edexcel English Level 1 Hub", url: "edexcel-functional-skills-english-level-1-past-papers.html" },
          "city-and-guilds": { title: "City & Guilds English Level 1 Hub", url: "city-and-guilds-functional-skills-english-level-1-past-papers.html" },
          "aqa": { title: "AQA English Level 1 Hub", url: "aqa-functional-skills-english-level-1-past-papers.html" },
          "ncfe": { title: "NCFE English Level 1 Hub", url: "ncfe-functional-skills-english-level-1-past-papers.html" },
          "open-awards": { title: "Open Awards English Level 1 Hub", url: "open-awards-functional-skills-english-level-1-past-papers.html" },
          "tquk": { title: "TQUK English Level 1 Hub", url: "tquk-functional-skills-english-level-1-past-papers.html" },
          "nocn": { title: "NOCN English Level 1 Hub", url: "nocn-functional-skills-english-level-1-past-papers.html" }
        },
        "digital-skills": {
          "": { title: "Digital Functional Skills Hub (L1 & Entry 3)", url: "digital-functional-skills-past-papers.html" },
          "edexcel": { title: "Pearson Edexcel Digital Skills Hub", url: "digital-functional-skills-past-papers.html" }
        }
      };

      function updateHubBanner() {
        if (!hubBanner) return;
        if (selectedSubject && HUB_MAP[selectedSubject]) {
          const subMap = HUB_MAP[selectedSubject];
          const info = subMap[selectedBoard] || subMap[""];
          if (info) {
            hubLabel.innerHTML = `Looking for the full syllabus &amp; courses? <strong>${info.title}</strong>`;
            hubLink.href = info.url;
            hubLink.textContent = `Open ${info.title} \\u2192`;
            hubBanner.style.display = "flex";
            return;
          }
        }
        hubBanner.style.display = "none";
      }

      function filterAll() {
        const query = (searchInput ? searchInput.value.toLowerCase().trim() : "");
        if (clearBtn) {
          clearBtn.style.display = query.length > 0 ? "block" : "none";
        }

        let visibleCount = 0;
        const chipRegex = selectedChip ? new RegExp(selectedChip, "i") : null;

        rows.forEach(function(row) {
          const rowBoard = row.getAttribute("data-board") || "";
          const rowSubject = row.getAttribute("data-subject") || "";
          const rowFormat = row.getAttribute("data-format") || "";
          const rowSearch = (row.getAttribute("data-search-term") || row.textContent).toLowerCase();

          const matchesBoard = !selectedBoard || rowBoard === selectedBoard;
          const matchesSubject = !selectedSubject || rowSubject === selectedSubject;

          let matchesFormat = true;
          if (selectedFormat === "paper") {
            matchesFormat = rowFormat.includes("paper");
          } else if (selectedFormat === "online") {
            matchesFormat = rowFormat.includes("online");
          }

          const matchesChip = !chipRegex || chipRegex.test(rowSearch);
          const matchesQuery = !query || rowSearch.includes(query);

          if (matchesBoard && matchesSubject && matchesFormat && matchesChip && matchesQuery) {
            row.style.display = "flex";
            visibleCount++;
          } else {
            row.style.display = "none";
          }
        });

        sections.forEach(function(sec) {
          const secRows = sec.querySelectorAll(".past-paper-row");
          const hasVisible = Array.from(secRows).some(function(r) { return r.style.display !== "none"; });
          sec.style.display = hasVisible ? "block" : "none";
        });

        if (counterEl) {
          counterEl.textContent = visibleCount;
        }

        if (noNotice) {
          noNotice.style.display = visibleCount === 0 ? "block" : "none";
        }

        updateHubBanner();
      }

      boardPills.forEach(function(btn) {
        btn.addEventListener("click", function() {
          const isAlreadyActive = this.classList.contains("active") && this.getAttribute("data-board") !== "";
          boardPills.forEach(function(b) { b.classList.remove("active"); });
          if (isAlreadyActive) {
            boardPills[0].classList.add("active");
            selectedBoard = "";
          } else {
            this.classList.add("active");
            selectedBoard = this.getAttribute("data-board") || "";
          }
          filterAll();
        });
      });

      subjectPills.forEach(function(btn) {
        btn.addEventListener("click", function() {
          subjectPills.forEach(function(s) { s.classList.remove("active"); });
          this.classList.add("active");
          selectedSubject = this.getAttribute("data-subject") || "";
          filterAll();
        });
      });

      formatPills.forEach(function(btn) {
        btn.addEventListener("click", function() {
          formatPills.forEach(function(f) { f.classList.remove("active"); });
          this.classList.add("active");
          selectedFormat = this.getAttribute("data-format") || "";
          filterAll();
        });
      });

      chips.forEach(function(chip) {
        chip.addEventListener("click", function() {
          chips.forEach(function(c) { c.classList.remove("active"); });
          this.classList.add("active");
          selectedChip = this.getAttribute("data-filter") || "";
          filterAll();
        });
      });

      if (searchInput) {
        searchInput.addEventListener("input", filterAll);
      }

      if (clearBtn) {
        clearBtn.addEventListener("click", function() {
          searchInput.value = "";
          filterAll();
          searchInput.focus();
        });
      }

      window.resetAllFinderFilters = function() {
        selectedBoard = "";
        selectedSubject = "";
        selectedFormat = "";
        selectedChip = "";

        boardPills.forEach(function(b, idx) { b.classList.toggle("active", idx === 0); });
        subjectPills.forEach(function(s, idx) { s.classList.toggle("active", idx === 0); });
        formatPills.forEach(function(f, idx) { f.classList.toggle("active", idx === 0); });
        chips.forEach(function(c, idx) { c.classList.toggle("active", idx === 0); });

        if (searchInput) searchInput.value = "";
        filterAll();
      };

      try {
        const urlParams = new URLSearchParams(window.location.search);
        const pBoard = urlParams.get("board");
        const pSubject = urlParams.get("subject");
        const pFormat = urlParams.get("format");
        const pQuery = urlParams.get("q");

        if (pBoard) {
          const bMatch = document.querySelector(`#boardFilterPills [data-board="${pBoard}"]`);
          if (bMatch) {
            boardPills.forEach(function(b) { b.classList.remove("active"); });
            bMatch.classList.add("active");
            selectedBoard = pBoard;
          }
        }
        if (pSubject) {
          const sMatch = document.querySelector(`#subjectFilterPills .finder-pill[data-subject="${pSubject}"]`);
          if (sMatch) {
            subjectPills.forEach(function(s) { s.classList.remove("active"); });
            sMatch.classList.add("active");
            selectedSubject = pSubject;
          }
        }
        if (pFormat) {
          const fMatch = document.querySelector(`#formatFilterPills .finder-pill[data-format="${pFormat}"]`);
          if (fMatch) {
            formatPills.forEach(function(f) { f.classList.remove("active"); });
            fMatch.classList.add("active");
            selectedFormat = pFormat;
          }
        }
        if (pQuery && searchInput) {
          searchInput.value = pQuery;
        }

        if (pBoard || pSubject || pFormat || pQuery) {
          filterAll();
        }
      } catch(e) {}

    })();
  </script>"""

    accessibility_scripts = """  <!-- DYSLEXIA TINT & ACCESSIBILITY ENGINE -->
  <script src="assets/js/mfs-tint.js"></script>

  <!-- THEME & DYSLEXIA MODE ENGINE -->
  <script>
    function toggleDyslexiaMode() {
      const isDys = document.body.classList.toggle('dyslexia-mode');
      localStorage.setItem('mfs_dyslexia', isDys ? '1' : '0');
      localStorage.setItem('mfs_dyslexia_mode', isDys ? 'true' : 'false');
      const btn = document.getElementById('dyslexiaToggle');
      if (btn) btn.classList.toggle('active', isDys);
    }
    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme') || 'sapphire';
      const next = current === 'emerald' ? 'sapphire' : 'emerald';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('mfs_theme', next);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = next === 'emerald' ? 'Emerald' : 'Sapphire';
    }
    (function() {
      if (localStorage.getItem('mfs_dyslexia') === '1' || localStorage.getItem('mfs_dyslexia_mode') === 'true') {
        document.body.classList.add('dyslexia-mode');
        const btn = document.getElementById('dyslexiaToggle');
        if (btn) btn.classList.add('active', true);
      }
      const th = localStorage.getItem('mfs_theme') || 'sapphire';
      document.documentElement.setAttribute('data-theme', th);
      const lbl = document.getElementById('themeLabel');
      if (lbl) lbl.textContent = th === 'emerald' ? 'Emerald' : 'Sapphire';
    })();
  </script>"""

    # Assemble complete page HTML
    complete_html = f"""<!DOCTYPE html>
<html lang="en-GB" data-theme="sapphire" data-tint="cream">
{head_html}
<body>
{NAV_HEADER}

{hero_section_html}

{finder_section_html}

{subj_section_html}

{FOOTER}

{filter_script_html}

{accessibility_scripts}
</body>
</html>"""

    # Write to target files
    out_files = [
        os.path.join(PROJECT_DIR, "past-papers.html"),
        os.path.join(PROJECT_DIR, "functional-skills-past-papers.html"),
        os.path.join(SYNC_DIR, "past-papers.html"),
        os.path.join(SYNC_DIR, "functional-skills-past-papers.html")
    ]

    for out_p in out_files:
        os.makedirs(os.path.dirname(out_p), exist_ok=True)
        with open(out_p, "w", encoding="utf-8") as f:
            f.write(complete_html)
        print(f"  [OK] Successfully wrote {out_p} ({len(complete_html):,} bytes)")

if __name__ == "__main__":
    build_interactive_past_papers_page()
