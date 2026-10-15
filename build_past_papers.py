import json, re, html

# 1. Load mfs_unique_papers.json
with open('/tmp/mfs_unique_papers.json') as f:
    raw_papers = json.load(f)

# Filter out the 2 old placeholder Digital Skills cards
base_papers = [p for p in raw_papers if not (p.get('subject') == 'Digital Skills' or 'pearson dfs' in p.get('title','').lower())]
print(f"Base non-digital papers: {len(base_papers)}")

# 2. Extract Open Awards buttons from the 4 HTML files
oa_files = [
    'open-awards-functional-skills-maths-level-2-past-papers.html',
    'open-awards-functional-skills-maths-level-1-past-papers.html',
    'open-awards-functional-skills-english-level-2-past-papers.html',
    'open-awards-functional-skills-english-level-1-past-papers.html'
]

oa_buttons_map = {}
for fn in oa_files:
    content = open(fn).read()
    h4_matches = list(re.finditer(r'<h4[^>]*>(.*?)</h4>', content))
    subj = 'Maths' if 'maths' in fn else 'English'
    lvl = 'Level 2' if 'level-2' in fn else 'Level 1'
    for i, m in enumerate(h4_matches):
        title = m.group(1).strip()
        if title in ['Official Open Awards Onscreen Exam Simulator (XAMS)', 'Maths Revision', 'Digital & English', 'Institutional']:
            continue
        start_idx = m.end()
        end_idx = h4_matches[i+1].start() if i+1 < len(h4_matches) else start_idx + 1500
        section = content[start_idx:end_idx]
        btns = re.findall(r'<a\s+[^>]*href=\"([^\"]+)\"[^>]*class=\"([^\"]+)\"[^>]*>(.*?)</a>', section)
        clean_btns = []
        for b_url, b_class, b_html in btns:
            b_text = re.sub(r'<[^>]+>', '', b_html).strip()
            b_type = 'qp'
            if 'ms' in b_class: b_type = 'ms'
            elif 'model' in b_class: b_type = 'model'
            elif 'video' in b_class: b_type = 'video'
            elif 'online' in b_class: b_type = 'online'
            
            clean_btns.append({'text': b_text, 'url': b_url, 'type': b_type, 'class': b_class})
        
        seen = set()
        dedup_btns = []
        for b in clean_btns:
            if b['url'] not in seen:
                seen.add(b['url'])
                dedup_btns.append(b)
        
        key = (title.lower().strip(), subj, lvl)
        oa_buttons_map[key] = dedup_btns

print(f"Mapped Open Awards papers: {len(oa_buttons_map)}")

# Update Open Awards papers in base_papers with buttons
oa_updated = 0
for p in base_papers:
    if p.get('board') == 'Open Awards':
        key = (p['title'].lower().strip(), p['subject'], p['level'])
        if key in oa_buttons_map:
            p['buttons'] = oa_buttons_map[key]
            oa_updated += 1

print(f"Updated {oa_updated} Open Awards papers with their exact buttons.")

# 3. Define the 9 Digital Functional Skills papers
digital_papers = [
    {
        "board": "Pearson Edexcel",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "Pearson DFS Level 1 Mock 1: Fresh Bite Sandwich Shop (Official SAM)",
        "buttons": [
            {"text": "Question Paper", "url": "assets/downloads/dfs/dfsq-l1-sam.pdf", "type": "qp"},
            {"text": "Data Files (.ZIP)", "url": "assets/downloads/dfs/dfs-level-1-sam-data-files.zip", "type": "data"},
            {"text": "Mock Online Simulator", "url": "digital-functional-skills-mock-exam.html?set=set1", "type": "mock"},
            {"text": "Full Bundle (.ZIP)", "url": "assets/downloads/dfs/dfs-l1-sample-assessment-materials.zip", "type": "data"}
        ]
    },
    {
        "board": "Pearson Edexcel",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "Pearson DFS Level 1 Mock 2: Annual Awards Ceremony & Catering (Practice Set 2)",
        "buttons": [
            {"text": "Data Files (.ZIP)", "url": "assets/downloads/dfs/dfs-level-1-practice-set-2-data-files.zip", "type": "data"},
            {"text": "Mark Scheme", "url": "assets/downloads/dfs/dfs-level-1-practice-set-2-mark-scheme.pdf", "type": "ms"},
            {"text": "Mock Online Simulator", "url": "digital-functional-skills-mock-exam.html?set=set2", "type": "mock"}
        ]
    },
    {
        "board": "Pearson Edexcel",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "Pearson DFS Level 1 Mock 3: First Aid Training & Supplies (Practice Set 1)",
        "buttons": [
            {"text": "Interactive Simulator", "url": "digital-functional-skills-mock-exam.html?set=set3", "type": "mock"},
            {"text": "Full Materials (.ZIP)", "url": "assets/downloads/dfs/dfs-l1-sample-assessment-materials.zip", "type": "data"}
        ]
    },
    {
        "board": "Pearson Edexcel",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "Pearson DFS Level 1 Mock 4: Gelato & Ice Cream Business (Past Test Set 1)",
        "buttons": [
            {"text": "Interactive Simulator", "url": "digital-functional-skills-mock-exam.html?set=set5", "type": "mock"},
            {"text": "Data Files (.ZIP)", "url": "assets/downloads/dfs/dfs-level-1-sam-data-files.zip", "type": "data"}
        ]
    },
    {
        "board": "Pearson Edexcel",
        "subject": "Digital Skills",
        "level": "Entry 3",
        "title": "Pearson DFS Entry 3 Mock 5: Apprenticeships & Work Experience (Official SAM)",
        "buttons": [
            {"text": "Question Paper", "url": "assets/downloads/dfs/dfsq-e3-sam.pdf", "type": "qp"},
            {"text": "Data Files (.ZIP)", "url": "assets/downloads/dfs/dfsq-entry-level-3-sam-data-files.zip", "type": "data"},
            {"text": "Mock Online Simulator", "url": "digital-functional-skills-mock-exam.html?set=set4", "type": "mock"},
            {"text": "Full Bundle (.ZIP)", "url": "assets/downloads/dfs/dfs-entry-l3-sample-assessment-materials.zip", "type": "data"}
        ]
    },
    {
        "board": "City & Guilds",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "City & Guilds 4748 Digital Functional Skills Level 1 Handbook & Specification",
        "buttons": [
            {"text": "Qualification Handbook", "url": "https://www.cityandguilds.com/-/media/productdocuments/skills-for-work-and-life/ict/4748/4748-qualification-handbook-level-1-v1-2-pdf.ashx", "type": "qp"},
            {"text": "C&G DFS Framework", "url": "https://www.cityandguilds.com/qualifications-and-education-training/essential-skills/digital-functional-skills", "type": "online"}
        ]
    },
    {
        "board": "City & Guilds",
        "subject": "Digital Skills",
        "level": "Entry 3",
        "title": "City & Guilds 4748 Digital Functional Skills Entry Level 3 Handbook & Guidance",
        "buttons": [
            {"text": "Qualification Handbook", "url": "https://www.cityandguilds.com/-/media/productdocuments/skills-for-work-and-life/ict/4748/4748-qualification-handbook-entry-3-v1-2-pdf.ashx", "type": "qp"},
            {"text": "C&G DFS Framework", "url": "https://www.cityandguilds.com/qualifications-and-education-training/essential-skills/digital-functional-skills", "type": "online"}
        ]
    },
    {
        "board": "NCFE",
        "subject": "Digital Skills",
        "level": "Level 1",
        "title": "NCFE Digital Functional Skills Level 1 Qualification Specification & Assessment Criteria",
        "buttons": [
            {"text": "Qualification Spec (PDF)", "url": "https://www.qualhub.co.uk/media/12185/603-7140-5-qualification-specification-version-10.pdf", "type": "qp"},
            {"text": "NCFE Assessment Guide", "url": "https://www.qualhub.co.uk/qualification-search/qualification-detail/ncfe-functional-skills-qualification-in-digital-functional-skills-at-level-1-5185", "type": "online"}
        ]
    },
    {
        "board": "NCFE",
        "subject": "Digital Skills",
        "level": "Entry 3",
        "title": "NCFE Digital Functional Skills Entry Level 3 Specification & Content Guide",
        "buttons": [
            {"text": "Qualification Spec (PDF)", "url": "https://www.qualhub.co.uk/media/12184/603-7139-9-qualification-specification-version-10.pdf", "type": "qp"},
            {"text": "NCFE Assessment Guide", "url": "https://www.qualhub.co.uk/qualification-search/qualification-detail/ncfe-functional-skills-qualification-in-digital-functional-skills-at-entry-level-3-5184", "type": "online"}
        ]
    }
]

# Combine all papers
all_papers = digital_papers + base_papers
print(f"Total papers to render: {len(all_papers)}")

# Board logo map
board_logo_map = {
    'Pearson Edexcel': 'assets/img/boards/edexcel.png',
    'City & Guilds': 'assets/img/boards/city-and-guilds.png',
    'Open Awards': 'assets/img/boards/open-awards.png',
    'NCFE': 'assets/img/boards/ncfe.png',
    'AQA': 'assets/img/boards/aqa.png',
    'TQUK': 'assets/img/boards/tquk.png',
    'NOCN': 'assets/img/boards/nocn.png'
}

# Button renderer
def render_button(btn):
    t = btn.get('text', '')
    url = btn.get('url', '#')
    b_type = btn.get('type', '')
    b_class = btn.get('class', '')
    
    # Defaults
    icon = 'fa-regular fa-file-pdf'
    btn_css = 'btn-paper btn-paper-qp'
    target = '_blank'
    rel = 'noopener'
    download = ''
    
    if b_type == 'ms' or 'ms' in b_class or 'mark scheme' in t.lower():
        icon = 'fa-solid fa-check'
        btn_css = 'btn-paper btn-paper-ms'
    elif b_type == 'model' or 'model' in b_class or 'model' in t.lower():
        icon = 'fa-solid fa-file-signature'
        btn_css = 'btn-paper btn-paper-model'
    elif b_type == 'online' or 'online' in b_class or 'online' in t.lower() or 'graph practice' in t.lower():
        if 'graph' in t.lower():
            icon = 'fa-solid fa-chart-line'
        else:
            icon = 'fa-solid fa-laptop-code'
        btn_css = 'btn-paper btn-paper-online'
    elif b_type == 'video' or 'video' in b_class or 'video' in t.lower():
        icon = 'fa-solid fa-video'
        btn_css = 'btn-paper btn-paper-video'
    elif b_type == 'data' or 'data files' in t.lower() or 'bundle' in t.lower() or '.zip' in url.lower():
        icon = 'fa-solid fa-file-zipper'
        btn_css = 'btn-paper btn-paper-data'
        download = ' download'
    elif b_type == 'mock' or 'simulator' in t.lower() or 'mock-exam' in url.lower():
        icon = 'fa-solid fa-desktop'
        btn_css = 'btn-paper btn-paper-mock'
        target = ''
        rel = ''
    else:
        icon = 'fa-regular fa-file-pdf'
        btn_css = 'btn-paper btn-paper-qp'
    
    # Ensure text is clean
    clean_t = html.escape(t)
    target_attr = f' target="{target}"' if target else ''
    rel_attr = f' rel="{rel}"' if rel else ''
    
    return f'<a href="{url}"{target_attr}{rel_attr}{download} class="{btn_css}"><i class="{icon}"></i> {clean_t}</a>'

# Render card
def render_card(p):
    board = p.get('board', 'Pearson Edexcel')
    subj = p.get('subject', 'Maths')
    lvl = p.get('level', 'Level 2')
    title = p.get('title', '')
    
    logo = board_logo_map.get(board, 'assets/img/boards/edexcel.png')
    
    # Search title: contains board, subj, level, title
    search_str = f"{title} {board} {subj} {lvl}".lower()
    
    btns_html = "\n        ".join(render_button(b) for b in p.get('buttons', []))
    if not btns_html:
        # Default fallback button
        btns_html = f'<a href="#" class="btn-paper btn-paper-qp"><i class="fa-regular fa-file-pdf"></i> View Resources</a>'
    
    card_html = f'''    <div class="paper-card" data-board="{html.escape(board)}" data-subj="{html.escape(subj)}" data-level="{html.escape(lvl)}" data-title="{html.escape(search_str)}">
      <div class="paper-card-header">
        <div class="board-logo-card" title="Awarding Body: {html.escape(board)}">
          <img src="{logo}" alt="{html.escape(board)}" class="board-card-logo-lg">
        </div>
        <span class="badge-spec">{html.escape(subj)} • {html.escape(lvl)}</span>
      </div>
      <h3 class="paper-card-title">{html.escape(title)}</h3>
      <div class="paper-card-actions">
        {btns_html}
      </div>
    </div>'''
    return card_html

all_cards_html = "\n\n".join(render_card(p) for p in all_papers)
print(f"Generated {len(all_papers)} card blocks.")

# Save cards to scratch file
with open('/tmp/mfs_all_cards.html', 'w') as f:
    f.write(all_cards_html)

print("Saved rendered cards to /tmp/mfs_all_cards.html")
