import os
import re
import glob

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Load NAV_HEADER and FOOTER
with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

BOARDS_DATA = {
    "edexcel": {
        "name": "Pearson Edexcel",
        "short_name": "Edexcel",
        "badge": "Most Popular",
        "color": "#00b87c",
        "logo": "assets/img/boards/edexcel.png",
        "specs": {
            "maths": {"qn": "603/4267/5 (L1) / 603/4268/7 (L2)", "sections": "Section A (Non-Calc 25m), Section B (Calc 75m)", "marks": "64 Marks", "time": "1 hr 45 mins"},
            "english": {"qn": "603/4284/5 (L1) / 603/4285/7 (L2)", "sections": "Reading (1 hr), Writing (1 hr 20m), SLC", "marks": "Reading (35m) + Writing (50m)", "time": "2 hrs 20 mins"}
        },
        "desc": "Pearson Edexcel is the UK's leading exam board for Functional Skills. Papers test real-world problem solving and practical literacy."
    },
    "city-and-guilds": {
        "name": "City & Guilds",
        "short_name": "City & Guilds",
        "badge": "City & Guilds",
        "color": "#0284c7",
        "logo": "assets/img/boards/city-and-guilds.png",
        "specs": {
            "maths": {"qn": "4748-01 (L1) / 4748-02 (L2)", "sections": "Section 1 Non-Calc (25 mins), Section 2 Calc (1 hr 20m)", "marks": "60 Marks", "time": "1 hr 45 mins"},
            "english": {"qn": "4748-11 (L1) / 4748-12 (L2)", "sections": "Reading (1 hr 15m), Writing (1 hr 20m), SLC", "marks": "Reading (30m) + Writing (54m)", "time": "2 hrs 35 mins"}
        },
        "desc": "City and Guilds 4748 qualifications are widely recognised across apprenticeships, healthcare, construction, and university entry."
    },
    "aqa": {
        "name": "AQA",
        "short_name": "AQA",
        "badge": "AQA",
        "color": "#8b5cf6",
        "logo": "assets/img/boards/aqa.png",
        "specs": {
            "maths": {"qn": "8361 (L1) / 8362 (L2)", "sections": "Paper 1 Non-Calc (30m), Paper 2 Calc (1 hr 30m)", "marks": "80 Marks", "time": "2 hrs"},
            "english": {"qn": "8720 (L1) / 8725 (L2)", "sections": "Paper 1 Reading (1 hr), Paper 2 Writing (1 hr), SLC", "marks": "Reading (26m) + Writing (30m)", "time": "2 hrs"}
        },
        "desc": "AQA Functional Skills assessments are designed to develop practical application of core mathematical and English principles."
    },
    "ncfe": {
        "name": "NCFE",
        "short_name": "NCFE",
        "badge": "NCFE",
        "color": "#f59e0b",
        "logo": "assets/img/boards/ncfe.png",
        "specs": {
            "maths": {"qn": "603/5056/8 (L1) / 603/5060/X (L2)", "sections": "Section A Non-Calc (30 mins), Section B Calc (1 hr 30m)", "marks": "60 Marks", "time": "2 hrs"},
            "english": {"qn": "603/5052/0 (L1) / 603/5060/X (L2)", "sections": "Reading (1 hr 15m), Writing (1 hr 15m), SLC", "marks": "Reading (30m) + Writing (40m)", "time": "2 hrs 30 mins"}
        },
        "desc": "NCFE Functional Skills qualifications equip learners with the vital practical skills required for employment and further education."
    },
    "open-awards": {
        "name": "Open Awards",
        "short_name": "Open Awards",
        "badge": "Open Awards",
        "color": "#10b981",
        "logo": "assets/img/boards/open-awards.png",
        "specs": {
            "maths": {"qn": "603/4806/9 (L1) / 603/4808/2 (L2)", "sections": "Section A Non-Calc (30m), Section B Calc (1 hr 30m)", "marks": "60 Marks", "time": "2 hrs"},
            "english": {"qn": "603/4638/3 (L1) / 603/4639/5 (L2)", "sections": "Reading (1 hr), Writing (1 hr), SLC", "marks": "Reading (30m) + Writing (30m)", "time": "2 hrs"}
        },
        "desc": "Open Awards assessments provide accessible, high-quality assessment with clear mark schemes and flexible examination pathways."
    },
    "tquk": {
        "name": "TQUK",
        "short_name": "TQUK",
        "badge": "TQUK",
        "color": "#ec4899",
        "logo": "assets/img/boards/tquk.png",
        "specs": {
            "maths": {"qn": "603/3929/9 (L1) / 603/3928/7 (L2)", "sections": "Section A Non-Calc (30 mins), Section B Calc (1 hr 30m)", "marks": "56 Marks", "time": "2 hrs"},
            "english": {"qn": "603/3930/5 (L1) / 603/3931/7 (L2)", "sections": "Reading (1 hr), Writing (1 hr 20m), SLC", "marks": "Reading (30m) + Writing (36m)", "time": "2 hrs 20 mins"}
        },
        "desc": "Training Qualifications UK (TQUK) offers progressive, regulated qualifications tailored for apprenticeships and career advancement."
    },
    "nocn": {
        "name": "NOCN",
        "short_name": "NOCN",
        "badge": "NOCN",
        "color": "#06b6d4",
        "logo": "assets/img/boards/nocn.png",
        "specs": {
            "maths": {"qn": "603/5267/X (L1) / 603/5268/1 (L2)", "sections": "Section 1 Non-Calc (35m), Section 2 Calc (1 hr 25m)", "marks": "60 Marks", "time": "2 hrs"},
            "english": {"qn": "603/5264/4 (L1) / 603/5265/6 (L2)", "sections": "Reading (1 hr 15m), Writing (1 hr 15m), SLC", "marks": "Reading (30m) + Writing (30m)", "time": "2 hrs 30 mins"}
        },
        "desc": "NOCN Functional Skills qualifications provide vocational learners with the numeracy and literacy demanded across UK industries."
    }
}

ALL_BOARD_KEYS = ["edexcel", "city-and-guilds", "aqa", "ncfe", "open-awards", "tquk", "nocn"]

SUBJECTS_CONFIG = {
    "maths-level-2": {
        "subject_name": "Maths",
        "level_name": "Level 2",
        "subject_key": "maths",
        "parent_hub": "functional-skills-maths-level-2-past-papers.html",
        "parent_title": "Maths Level 2 Past Papers",
        "course_link": "functional-skills-maths-level-2.html"
    },
    "english-level-2": {
        "subject_name": "English",
        "level_name": "Level 2",
        "subject_key": "english",
        "parent_hub": "functional-skills-english-level-2-past-papers.html",
        "parent_title": "English Level 2 Past Papers",
        "course_link": "functional-skills-english-level-2.html"
    },
    "maths-level-1": {
        "subject_name": "Maths",
        "level_name": "Level 1",
        "subject_key": "maths",
        "parent_hub": "functional-skills-maths-level-1-past-papers.html",
        "parent_title": "Maths Level 1 Past Papers",
        "course_link": "functional-skills-maths-level-1.html"
    },
    "english-level-1": {
        "subject_name": "English",
        "level_name": "Level 1",
        "subject_key": "english",
        "parent_hub": "functional-skills-english-level-1-past-papers.html",
        "parent_title": "English Level 1 Past Papers",
        "course_link": "functional-skills-english-level-1.html"
    }
}

def clean_pdf_url(url):
    """Ensure all remote PDF URLs point to passfunctionalskills.co.uk so they load reliably."""
    url = url.strip()
    if not url or url.startswith("#"):
        return url
    
    # Fix masterfunctionalskills -> passfunctionalskills for upload directories
    if "masterfunctionalskills.co.uk/app/uploads/" in url:
        url = url.replace("https://masterfunctionalskills.co.uk/app/uploads/", "https://passfunctionalskills.co.uk/app/uploads/")
    elif "masterfunctionalskills.co.uk/wp-content/uploads/" in url:
        url = url.replace("https://masterfunctionalskills.co.uk/wp-content/uploads/", "https://passfunctionalskills.co.uk/wp-content/uploads/")
    elif url.startswith("/app/uploads/"):
        url = "https://passfunctionalskills.co.uk" + url
    elif url.startswith("/wp-content/uploads/"):
        url = "https://passfunctionalskills.co.uk" + url
    elif url.endswith(".pdf") and "masterfunctionalskills.co.uk" in url:
        url = url.replace("masterfunctionalskills.co.uk", "passfunctionalskills.co.uk")
    
    return url

OPEN_AWARDS_ONLINE_TESTS = {
    # Maths Level 2
    "open awards online functional skills maths level 2 practice exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315953&downloadResult=true",
    "open awards online functional skills maths level 2 practice exam - 2": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=328571&downloadResult=true",
    "open awards online functional skills maths level 2 practice exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419856&downloadResult=true",
    "open awards online functional skills maths level 2 practice exam": "https://app.xams.co.uk/learner/exam/demo?userid=832321&examid=228050&downloadResult=true",
    "open awards graph practice": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=287181",

    # Maths Level 1
    "open awards online functional skills maths level 1 mock exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315947&downloadResult=true",
    "open awards online functional skills maths level 1 mock exam - 2": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315948&downloadResult=true",
    "open awards online functional skills maths level 1 mock exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419888&downloadResult=true",
    "open awards online functional skills maths level 1 exam 2020": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=228049&downloadResult=true",

    # English Level 2
    "open awards online functional skills english level 2 reading exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315949&downloadResult=true",
    "open awards online functional skills english level 2 writing exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315951&downloadResult=true",
    "open awards online functional skills english level 2 reading exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419891&downloadResult=true",
    "open awards online functional skills english level 2 writing exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419892&downloadResult=true",
    "open awards online functional skills english level 2 reading exam - 4": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419893&downloadResult=true",
    "open awards online functional skills english level 2 writing exam - 4": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419895&downloadResult=true",
    "open awards online functional skills english level 2 reading exam": "https://player.xams.co.uk/learner/exam/demo?userid=832321&examid=227753&downloadResult=true",
    "open awards online functional skills english level 2 writing exam": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=228048&downloadResult=true",

    # English Level 1
    "online functional skills english level 1 reading mock exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315927&downloadResult=true",
    "online functional skills english level 1 writing mock exam - 1": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315945&downloadResult=true",
    "online functional skills english level 1 reading mock exam - 2": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=315928&downloadResult=true",
    "online functional skills english level 1 writing mock exam - 2": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419890&downloadResult=true",
    "online functional skills english level 1 reading mock exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419889&downloadResult=true",
    "online functional skills english level 1 writing mock exam - 3": "https://openawards.xams.co.uk/learner/exam/demo?userid=491030&examid=419894&downloadResult=true",
    "online functional skills english level 1 reading exam": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=227733&downloadResult=true",
    "online functional skills english level 1 writing exam": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=227738&downloadResult=true"
}

def enrich_paper_links(title, links):
    t_clean = title.lower().strip()
    if "graph practice" in t_clean:
        return [{"text": "Graph Practice Tool", "url": "https://fs2019.xams.co.uk/learner/exam/demo?userid=832321&examid=287181"}]

    matched_xams = None
    for k, xurl in OPEN_AWARDS_ONLINE_TESTS.items():
        if k in t_clean or t_clean in k:
            matched_xams = xurl
            break

    if not matched_xams:
        return links

    enriched = []
    has_online = False
    for lk in links:
        lt = lk["text"].lower()
        lu = lk["url"].lower()
        if "mock-exam" in lu or "xams" in lu or "sit mock" in lt or (lt == "question paper" and "mock-exam" in lu):
            enriched.append({"text": "Take Online Test", "url": matched_xams})
            has_online = True
        else:
            enriched.append(lk)

    if not has_online:
        enriched.insert(0, {"text": "Take Online Test", "url": matched_xams})

    return enriched

def parse_page_content(fpath):
    """Extract sections, papers, and individual links with highest fidelity."""
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # If the file already has modern .past-paper-row elements, parse them directly
    if '<div class="past-paper-row"' in html or "<div class='past-paper-row'" in html:
        sections = {}
        sec_blocks = re.findall(r'<section class=[\"\']paper-group-section[\"\']>(.*?)</section>', html, re.DOTALL)
        for sb in sec_blocks:
            t_m = re.search(r'<h3 class=[\"\']paper-group-title[\"\'][^>]*>\s*<i[^>]*></i>\s*(.*?)\s*</h3>', sb)
            sec_title = t_m.group(1).strip() if t_m else 'Official Practice Papers'
            row_chunks = sb.split('<div class="past-paper-row"')[1:]
            papers = []
            for rc in row_chunks:
                h4_m = re.search(r'<h4 class=[\"\']past-paper-title[\"\']>(.*?)</h4>', rc)
                title = h4_m.group(1).strip() if h4_m else ''
                actions_m = re.search(r'<div class=[\"\']past-paper-actions[\"\']>(.*?)</div>', rc, re.DOTALL)
                if actions_m:
                    links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', actions_m.group(1), re.DOTALL)
                    clean_links = [{'text': re.sub(r'<[^>]+>', '', l[1]).strip(), 'url': clean_pdf_url(l[0])} for l in links]
                    if clean_links:
                        papers.append({'title': title, 'links': enrich_paper_links(title, clean_links)})
            if papers:
                sections[sec_title] = papers
        if sections:
            return sections

    # Otherwise parse legacy WordPress layout
    tokens = re.findall(
        r'(<div class=[\"\']mt-4[\"\'][^>]*>\s*<h3[^>]*>.*?</h3>\s*</div>|<div class=[\"\']py-2 py-lg-0 border-bottom[\"\']>.*?</div>\s*</div>\s*</div>)',
        html,
        re.DOTALL
    )

    current_section = "Official Practice & Past Papers"
    sections = {current_section: []}

    for t in tokens:
        if "mt-4" in t:
            h3_m = re.search(r'<h3[^>]*>(.*?)</h3>', t)
            if h3_m:
                raw_name = re.sub(r'<[^>]+>', '', h3_m.group(1)).strip().replace('&amp;', '&')
                if raw_name:
                    current_section = raw_name
                    if current_section not in sections:
                        sections[current_section] = []
        else:
            title_m = re.search(r'<div class=[\"\']col-lg text-dark text-lg-left my-2[\"\']>(.*?)</div>', t, re.DOTALL)
            if not title_m:
                continue
            title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
            if "Sit Mock Exam Online" in title or "Sit Exam Online" in title:
                continue

            links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', t, re.DOTALL)
            parsed_links = []
            for href, text in links:
                clean_t = re.sub(r'<[^>]+>', '', text).strip()
                if not clean_t or clean_t == title:
                    continue
                parsed_links.append({"text": clean_t, "url": clean_pdf_url(href)})

            if parsed_links:
                sections[current_section].append({
                    "title": title,
                    "links": enrich_paper_links(title, parsed_links)
                })

    non_empty = {k: v for k, v in sections.items() if v}
    return non_empty

def render_board_switcher(current_board_key, subj_slug, config):
    pills_html = []
    for b_key in ALL_BOARD_KEYS:
        b_info = BOARDS_DATA[b_key]
        b_file = f"{b_key}-functional-skills-{subj_slug}-past-papers.html"
        is_active = (b_key == current_board_key)
        active_cls = " active" if is_active else ""
        pills_html.append(f'<a href="{b_file}" class="board-pill{active_cls}"><img src="{b_info["logo"]}" alt="{b_info["short_name"]} Logo"> {b_info["short_name"]}</a>')
    
    pills_html.append(f'<a href="{config["parent_hub"]}" class="board-pill pill-all">All {config["subject_name"]} {config["level_name"]} Boards →</a>')

    return f"""
    <nav class="board-switcher-nav" aria-label="Exam Boards Navigation">
      <div class="mfs-container">
        <div class="board-switcher-inner">
          <span class="board-switcher-label"><i class="fa-solid fa-building-columns" style="color:var(--accent); margin-right:4px;"></i> Awarding Bodies:</span>
          <div class="board-switcher-pills">
            {"".join(pills_html)}
          </div>
        </div>
      </div>
    </nav>
    """

def button_sort_key(item):
    """Enforce exact tab ordering: Online Test (0) -> QP/Insert (1-3) -> MS (4) -> Model (5) -> Video (6)."""
    t = item["text"].lower()
    url = item["url"].lower()
    if any(w in t for w in ["online test", "take online test", "start online test", "graph practice tool"]) or "xams" in url:
        return 0
    if "non-calc" in t or "non calc" in t or "section a" in t:
        return 1
    if "calc" in t or "section b" in t:
        return 2
    if "reading" in t:
        return 1
    if "writing" in t:
        return 2
    if "insert" in t:
        return 3
    if any(w in t for w in ["past paper", "question paper", "question", "answer booklet"]):
        return 1
    if any(w in t for w in ["mark scheme", "markscheme", "answers", "answer"]) and not any(w in t for w in ["borderline", "fail", "good", "sample answer"]):
        return 4
    if any(w in t for w in ["model solution", "model solutions", "sample answer", "answer - good", "answer - borderline", "answer - fail"]):
        return 5
    if any(w in t for w in ["video", "walkthrough", "solution"]) or "youtu" in url:
        return 6
    if any(w in t for w in ["sit exam", "sit mock", "mock", "resource"]):
        return 7
    return 8

def format_action_buttons(links):
    # Sort links so Online Test is FIRST, Model Solution is before Video Walkthrough
    sorted_links = sorted(links, key=button_sort_key)
    btns_html = []
    for item in sorted_links:
        t = item["text"]
        url = item["url"]

        # 0. Online Test / XAMS Simulator (Top Priority)
        if any(w in t.lower() for w in ["online test", "take online test", "start online test", "graph practice tool"]) or "xams" in url.lower():
            if "graph" in t.lower() or "graph" in url.lower():
                icon = "fa-solid fa-chart-line"
                cls = "btn-paper-online"
                label = "Graph Practice Tool"
            else:
                icon = "fa-solid fa-laptop-code"
                cls = "btn-paper-online"
                label = "Take Online Test"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        # 1. Question Paper / Insert
        elif any(w in t.lower() for w in ["past paper", "question paper", "question", "answer booklet", "reading paper", "writing paper", "insert"]):
            icon = "fa-regular fa-file-pdf"
            cls = "btn-paper-qp"
            label = t
            if "non-calc" in t.lower() or "non calc" in t.lower():
                label = "Non-Calc Paper"
            elif "calc" in t.lower() and "non" not in t.lower():
                label = "Calc Paper"
            elif "insert" in t.lower():
                label = "Source Insert"
            elif "reading" in t.lower() and "insert" not in t.lower():
                label = "Reading Paper"
            elif "writing" in t.lower():
                label = "Writing Paper"
            elif t.lower() in ["past paper", "question paper", "question"]:
                label = "Question Paper"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        # 2. Mark Scheme
        elif any(w in t.lower() for w in ["mark scheme", "markscheme", "answers", "answer"]) and not any(w in t.lower() for w in ["borderline", "fail", "good", "sample answer"]):
            icon = "fa-solid fa-clipboard-check"
            cls = "btn-paper-ms"
            label = "Mark Scheme"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        # 3. Model Solution / Exemplar
        elif any(w in t.lower() for w in ["model solution", "model solutions", "sample answer", "answer - good", "answer - borderline", "answer - fail"]):
            icon = "fa-solid fa-lightbulb"
            cls = "btn-paper-model"
            label = t if "answer -" in t.lower() else "Model Solution"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        # 4. Video Solution (Always to the right of Model Solution)
        elif any(w in t.lower() for w in ["video", "walkthrough"]) or "youtu" in url:
            icon = "fa-brands fa-youtube"
            cls = "btn-paper-video"
            label = "Video Walkthrough"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        # 5. Online Mock Exam / Other
        elif any(w in t.lower() for w in ["sit exam", "sit mock", "mock", "resource"]):
            icon = "fa-solid fa-laptop-code"
            cls = "btn-paper-qp"
            label = "Sit Mock Online"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {label}</a>')

        else:
            icon = "fa-solid fa-arrow-up-right-from-square"
            cls = "btn-paper-qp"
            btns_html.append(f'<a href="{url}" target="_blank" rel="noopener" class="btn-paper {cls}"><i class="{icon}"></i> {t}</a>')

    return "".join(btns_html)

def build_single_board_page(board_key, subj_slug):
    board = BOARDS_DATA[board_key]
    subj = SUBJECTS_CONFIG[subj_slug]
    filename = f"{board_key}-functional-skills-{subj_slug}-past-papers.html"
    filepath = os.path.join(PROJECT_DIR, filename)

    if not os.path.exists(filepath):
        print(f"Skipping {filename} (not found)")
        return

    sections_data = parse_page_content(filepath)
    total_papers = sum(len(papers) for papers in sections_data.values())

    board_specs = board["specs"][subj["subject_key"]]
    page_title = f"{board['name']} Functional Skills {subj['subject_name']} {subj['level_name']} Past Papers & Mark Schemes | Master Functional Skills"
    meta_desc = f"Download official {board['name']} Functional Skills {subj['subject_name']} {subj['level_name']} past papers, mark schemes, model solutions and video walkthroughs. 100% free PDF downloads."

    # Build sections HTML
    sections_html = []
    for sec_title, papers in sections_data.items():
        paper_rows = []
        for p in papers:
            title = p["title"]
            search_term = f"{title.lower()} {sec_title.lower()} {board['short_name'].lower()} {subj['subject_name'].lower()} {subj['level_name'].lower()}"
            if any("xams" in lk["url"] or "online" in lk["text"].lower() for lk in p["links"]):
                search_term += " online test xams mock exam interactive onscreen"
            actions_html = format_action_buttons(p["links"])

            spec_tag = "New 2019+ Reform Spec"
            if "old spec" in title.lower() or "old spec" in sec_title.lower():
                spec_tag = "Legacy Specification"

            paper_rows.append(f"""
            <div class="past-paper-row" data-search-term="{search_term}">
              <div class="past-paper-meta">
                <div class="past-paper-tags">
                  <span class="past-paper-tag-board">{board['short_name']}</span>
                  <span class="past-paper-tag-spec">{spec_tag}</span>
                </div>
                <h4 class="past-paper-title">{title}</h4>
              </div>
              <div class="past-paper-actions">
                {actions_html}
              </div>
            </div>
            """)

        sections_html.append(f"""
        <section class="paper-group-section">
          <div class="paper-group-header">
            <h3 class="paper-group-title">
              <i class="fa-solid fa-folder-open"></i> {sec_title}
            </h3>
            <span class="paper-group-count">{len(papers)} Papers</span>
          </div>
          <div class="paper-group-list">
            {"".join(paper_rows)}
          </div>
        </section>
        """)

    switcher_html = render_board_switcher(board_key, subj_slug, subj)

    open_awards_chip = ""
    open_awards_banner = ""
    if board_key == "open-awards":
        open_awards_chip = '<button type="button" class="filter-chip" data-filter="online|xams|mock" style="color:#2563eb; border-color:#2563eb; font-weight:700;"><i class="fa-solid fa-laptop-code"></i> Online Tests</button>'
        open_awards_banner = f"""
        <div style="background: linear-gradient(135deg, rgba(37,99,235,0.07) 0%, rgba(0,184,124,0.07) 100%); border: 1.5px solid #2563eb; border-radius: 14px; padding: 20px 24px; margin-bottom: 24px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">
          <div style="display:flex; align-items:center; gap:16px;">
            <div style="width:48px; height:48px; border-radius:12px; background:#2563eb; color:#ffffff; display:flex; align-items:center; justify-content:center; font-size:1.4rem; flex-shrink:0;">
              <i class="fa-solid fa-laptop-code"></i>
            </div>
            <div>
              <h4 style="margin:0; font-size:1.15rem; color:var(--navy-dark); font-weight:800;">Official Open Awards Onscreen Exam Simulator (XAMS)</h4>
              <p style="margin:4px 0 0 0; font-size:0.88rem; color:var(--text-muted); line-height:1.5;">
                Practice on the genuine Open Awards computer-based testing interface. Click <strong>"Take Online Test"</strong> on any practice paper below to launch the live interactive simulation in your browser.
              </p>
            </div>
          </div>
          <button type="button" class="btn-paper btn-paper-online" style="padding:10px 20px; font-size:0.88rem; cursor:pointer;" onclick="document.querySelector('[data-filter*=\\'online\\']').click()">
            <i class="fa-solid fa-play"></i> Filter Online Tests
          </button>
        </div>
        """

    page_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <header class="past-papers-hero">
    <div class="mfs-container">
      <nav class="past-papers-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="separator"><i class="fa-solid fa-chevron-right"></i></span>
        <a href="functional-skills-past-papers.html">Past Papers</a>
        <span class="separator"><i class="fa-solid fa-chevron-right"></i></span>
        <a href="{subj['parent_hub']}">{subj['subject_name']} {subj['level_name']}</a>
        <span class="separator"><i class="fa-solid fa-chevron-right"></i></span>
        <span class="current">{board['name']}</span>
      </nav>

      <!-- OFFICIAL EXAM BOARD BADGE (NO REDUNDANT TEXT) -->
      <div class="board-hero-logo-badge" style="padding:14px 26px; background:#ffffff; border-radius:18px; display:inline-flex; align-items:center; gap:16px;">
        <img src="{board['logo']}" alt="{board['name']} Official Logo" style="height:56px; max-width:210px; width:auto; object-fit:contain;">
        <span style="border-left:2px solid var(--border); padding-left:14px; font-size:0.82rem; font-weight:800; text-transform:uppercase; letter-spacing:0.06em; color:var(--accent);">
          Ofqual Regulated
        </span>
      </div>

      <h1 class="past-papers-hero-title">
        {board['name']} Functional Skills <span>{subj['subject_name']} {subj['level_name']} Past Papers</span>
      </h1>
      <p class="past-papers-hero-subtitle">
        Free authentic {board['name']} Functional Skills {subj['subject_name']} {subj['level_name']} past papers, official examiner mark schemes, worked model answers, and step-by-step video solutions.
      </p>

      <!-- WHAT TO ADD (YOUR MOAT) -->
      <div class="moat-strip">
        <span class="moat-badge"><i class="fa-solid fa-bolt"></i> 1-Click Direct PDF Open (No Paywalls)</span>
        <span class="moat-badge"><i class="fa-solid fa-universal-access"></i> Dyslexia-Friendly Layout</span>
        <span class="moat-badge"><i class="fa-solid fa-magnifying-glass"></i> Instant Year & Series Search Bar</span>
        <span class="moat-badge"><i class="fa-solid fa-file-circle-check"></i> Official Mark Schemes & Model Solutions</span>
      </div>

      <div class="past-papers-badges-bar">
        <div class="past-papers-badge-item">
          <i class="fa-solid fa-certificate"></i> Ofqual Code: <strong>{board_specs['qn']}</strong>
        </div>
        <div class="past-papers-badge-item">
          <i class="fa-solid fa-clock"></i> Duration: <strong>{board_specs['time']}</strong>
        </div>
        <div class="past-papers-badge-item">
          <i class="fa-solid fa-list-check"></i> Structure: <strong>{board_specs['sections']}</strong>
        </div>
        <div class="past-papers-badge-item">
          <i class="fa-solid fa-circle-check"></i> Total Marks: <strong>{board_specs['marks']}</strong>
        </div>
      </div>
    </div>
  </header>

  <!-- EXAM BOARD SWITCHER SUBNAV -->
  {switcher_html}

  <!-- MAIN PAPERS CONTENT -->
  <main class="past-papers-container" id="main-content">

    <!-- SEARCH & FILTER BAR (THE MOAT) -->
    <div class="paper-filter-bar">
      <div class="paper-search-wrap">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="paperSearchInput" class="paper-search-input" placeholder="Search papers by series (e.g. 2023, June, Non-Calc, Calc, Sample)...">
        <button type="button" id="clearSearchBtn" style="display:none; background:none; border:none; color:var(--text-muted); cursor:pointer; padding:6px 12px; font-size:1.1rem;" title="Clear search"><i class="fa-solid fa-xmark"></i></button>
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
      {open_awards_chip}
      <button type="button" class="filter-chip" data-filter="2023|2022|2021">2021–2023 Reform</button>
      <button type="button" class="filter-chip" data-filter="non-calc|non calc|section a">Non-Calculator</button>
      <button type="button" class="filter-chip" data-filter="calc|section b">Calculator</button>
      <button type="button" class="filter-chip" data-filter="reading">Reading</button>
      <button type="button" class="filter-chip" data-filter="writing">Writing</button>
      <button type="button" class="filter-chip" data-filter="sample|practice|specimen">Practice Papers</button>
      <button type="button" class="filter-chip" data-filter="video|walkthrough">Video Solutions</button>
    </div>

    {open_awards_banner}

    <!-- PAPERS DIRECTORY -->
    <div id="papersDirectory">
      {"".join(sections_html)}
    </div>

    <!-- SPECIFICATION & OVERVIEW CARD -->
    <div class="paper-info-card">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-size:0.8rem; font-weight:800; color:var(--accent); text-transform:uppercase; letter-spacing:0.5px;">Awarding Body Specifications</span>
          <h3 style="margin-top:4px;">About {board['name']} Functional Skills {subj['subject_name']} {subj['level_name']}</h3>
        </div>
        <a href="{subj['course_link']}" class="btn-card-action" style="padding:10px 20px;">
          View {subj['subject_name']} {subj['level_name']} Revision Course →
        </a>
      </div>
      <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.65; margin-top:12px;">
        {board['desc']} All past paper PDFs, mark schemes, and video solutions on this page are provided free of charge to assist candidates in exam preparation. Candidates should practise completing papers under strict exam timings without revision notes to gauge real examination readiness.
      </p>

      <div class="paper-info-grid">
        <div class="paper-info-item">
          <strong>Exam Board</strong>
          <span>{board['name']}</span>
        </div>
        <div class="paper-info-item">
          <strong>Qualification Code</strong>
          <span>{board_specs['qn']}</span>
        </div>
        <div class="paper-info-item">
          <strong>Format & Timing</strong>
          <span>{board_specs['time']}</span>
        </div>
        <div class="paper-info-item">
          <strong>Available Papers</strong>
          <span>{total_papers} Authentic Assessments</span>
        </div>
      </div>
    </div>

    <!-- FAQ CARD -->
    <div class="paper-info-card" style="margin-top:28px;">
      <h3>Frequently Asked Questions</h3>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:24px; margin-top:20px;">
        <div>
          <h4 style="font-size:1.05rem; font-weight:700; color:var(--navy); margin-bottom:8px;">
            <i class="fa-solid fa-circle-question" style="color:var(--accent); margin-right:6px;"></i> Are these authentic past papers?
          </h4>
          <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
            Yes. Every practice assessment, insert, and official mark scheme is genuine examination material aligned with the {board['name']} Functional Skills {subj['subject_name']} {subj['level_name']} specification.
          </p>
        </div>
        <div>
          <h4 style="font-size:1.05rem; font-weight:700; color:var(--navy); margin-bottom:8px;">
            <i class="fa-solid fa-circle-question" style="color:var(--accent); margin-right:6px;"></i> How should I use the mark schemes?
          </h4>
          <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
            Sit the paper under timed conditions first. Afterwards, compare your answers with the official examiner mark scheme and worked model solutions to understand how marks are awarded for method and accuracy.
          </p>
        </div>
        <div>
          <h4 style="font-size:1.05rem; font-weight:700; color:var(--navy); margin-bottom:8px;">
            <i class="fa-solid fa-circle-question" style="color:var(--accent); margin-right:6px;"></i> Can I sit my official exam online?
          </h4>
          <p style="font-size:0.9rem; color:var(--text-muted); line-height:1.6;">
            Yes! Master Functional Skills offers official Ofqual-regulated Functional Skills exams online with secure remote invigilation from home 6 days a week, with fast results turnaround.
          </p>
        </div>
      </div>
    </div>

    <!-- EXAM BOOKING CALLOUT -->
    <div style="background:linear-gradient(135deg, var(--navy-dark) 0%, #0d1b3e 100%); border-radius:16px; padding:36px; margin-top:32px; color:#ffffff; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px; border-left:4px solid var(--accent);">
      <div>
        <span style="font-size:0.8rem; font-weight:800; color:var(--accent); text-transform:uppercase; letter-spacing:0.5px;">Ready to Pass?</span>
        <h3 style="color:#ffffff; font-size:1.6rem; font-weight:800; margin:6px 0 8px;">Book Your Official {subj['subject_name']} {subj['level_name']} Exam</h3>
        <p style="color:rgba(255,255,255,0.85); font-size:0.95rem; margin:0; max-width:650px;">
          Book your Ofqual-regulated exam with Master Functional Skills. Sit online from home, choose your preferred date, and get your GCSE-equivalent certificate.
        </p>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a href="functional-skills-exam.html" class="btn-card-action" style="padding:14px 28px; font-size:1rem; box-shadow:0 4px 14px rgba(0,184,124,0.4);">
          Book Official Exam Now →
        </a>
        <a href="https://sterlingenglish.org" target="_blank" rel="noopener" style="background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.25); color:#ffffff; padding:14px 24px; border-radius:var(--radius-full); font-weight:700; text-decoration:none; font-size:0.95rem; display:inline-flex; align-items:center; gap:8px;">
          1-to-1 Specialist Tuition ↗
        </a>
      </div>
    </div>

  </main>

{FOOTER}

  <!-- LIVE INSTANT SEARCH & SERIES FILTER SCRIPT -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      const searchInput = document.getElementById("paperSearchInput");
      const clearBtn = document.getElementById("clearSearchBtn");
      const chips = document.querySelectorAll(".filter-chip");
      const rows = document.querySelectorAll(".past-paper-row");
      const sections = document.querySelectorAll(".paper-group-section");
      const counterEl = document.getElementById("visiblePapersCount");

      let currentChipFilter = "";

      function filterPapers() {{
        const query = (searchInput ? searchInput.value.toLowerCase().trim() : "");
        if (clearBtn) {{
          clearBtn.style.display = query.length > 0 ? "inline-block" : "none";
        }}

        let visibleCount = 0;
        const chipRegex = currentChipFilter ? new RegExp(currentChipFilter, "i") : null;

        rows.forEach(function(row) {{
          const searchData = (row.getAttribute("data-search-term") || row.textContent).toLowerCase();
          
          let matchesQuery = !query || searchData.includes(query);
          let matchesChip = !chipRegex || chipRegex.test(searchData);

          if (matchesQuery && matchesChip) {{
            row.style.display = "flex";
            visibleCount++;
          }} else {{
            row.style.display = "none";
          }}
        }});

        sections.forEach(function(sec) {{
          const secRows = sec.querySelectorAll(".past-paper-row");
          const hasVisible = Array.from(secRows).some(function(r) {{ return r.style.display !== "none"; }});
          sec.style.display = hasVisible ? "block" : "none";
        }});

        if (counterEl) {{
          counterEl.textContent = visibleCount;
        }}
      }}

      if (searchInput) {{
        searchInput.addEventListener("input", filterPapers);
      }}

      if (clearBtn) {{
        clearBtn.addEventListener("click", function() {{
          searchInput.value = "";
          filterPapers();
          searchInput.focus();
        }});
      }}

      chips.forEach(function(chip) {{
        chip.addEventListener("click", function() {{
          chips.forEach(function(c) {{ c.classList.remove("active"); }});
          this.classList.add("active");
          currentChipFilter = this.getAttribute("data-filter") || "";
          filterPapers();
        }});
      }});
    }});
  </script>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"  [OK] Successfully rebuilt {filename} ({total_papers} papers)")

def build_all_boards():
    count = 0
    for subj_slug in SUBJECTS_CONFIG:
        for b_key in ALL_BOARD_KEYS:
            build_single_board_page(b_key, subj_slug)
            count += 1
    print(f"\nAll {count} exam board past paper pages rebuilt successfully with clean formatting and working PDF links!")

if __name__ == "__main__":
    build_all_boards()
