import os
import re
import urllib.request
import time

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Read modern NAV_HEADER and FOOTER
with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

SUBJECT_HUBS = [
    {
        "filename": "functional-skills-maths-level-2-past-papers.html",
        "title": "Functional Skills Maths Level 2 Past Papers & Mark Schemes | Master Functional Skills",
        "h1": "Functional Skills Maths Level 2 Past Papers",
        "meta_desc": "Free Functional Skills Maths Level 2 past papers and official mark schemes for Pearson Edexcel, City & Guilds, NCFE, AQA, Open Awards, and TQUK.",
        "level": "Level 2",
        "subject": "Maths",
        "boards": [
            {
                "name": "Pearson Edexcel",
                "slug": "edexcel-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/edexcel-functional-skills-maths-level-2-past-papers/",
                "papers_count": "10 Practice Papers",
                "badge": "Most Popular",
                "desc": "Official Edexcel Functional Skills Maths Level 2 past exam papers, non-calc & calc questions, mark schemes and video solutions."
            },
            {
                "name": "City & Guilds",
                "slug": "city-and-guilds-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/city-and-guilds-functional-skills-maths-level-2-past-papers/",
                "papers_count": "Sample Papers & Tests",
                "badge": "City & Guilds",
                "desc": "Authentic City & Guilds Level 2 Maths past papers, sample papers and worked answers for 4748-02 qualifications."
            },
            {
                "name": "Open Awards",
                "slug": "open-awards-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/open-awards-functional-skills-maths-level-2-past-papers/",
                "papers_count": "Online Tests & PDFs",
                "badge": "Online Interactive",
                "desc": "Official Open Awards online onscreen interactive exams via XAMS simulator, plus downloadable question papers and mark schemes."
            },
            {
                "name": "NCFE",
                "slug": "ncfe-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/ncfe-functional-skills-maths-level-2-past-papers/",
                "papers_count": "Sample & Past Papers",
                "badge": "NCFE",
                "desc": "NCFE Level 2 Functional Skills Maths papers covering Section A (Non-calculator) and Section B (Calculator)."
            },
            {
                "name": "AQA",
                "slug": "aqa-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/aqa-functional-skills-maths-level-2-past-papers/",
                "papers_count": "AQA Past Papers",
                "badge": "AQA",
                "desc": "Download genuine AQA Functional Skills Mathematics Level 2 past question papers and mark schemes."
            },
            {
                "name": "TQUK",
                "slug": "tquk-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/tquk-functional-skills-maths-level-2-past-papers-2/",
                "papers_count": "TQUK Papers",
                "badge": "TQUK",
                "desc": "Training Qualifications UK (TQUK) Level 2 Maths past papers and assessment papers with marking guidance."
            },
            {
                "name": "NOCN",
                "slug": "nocn-functional-skills-maths-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/nocn-functional-skills-maths-level-2-past-papers/",
                "papers_count": "NOCN Papers",
                "badge": "NOCN",
                "desc": "NOCN Functional Skills Mathematics Level 2 practice papers and sample assessments."
            }
        ]
    },
    {
        "filename": "functional-skills-english-level-2-past-papers.html",
        "title": "Functional Skills English Level 2 Past Papers & Mark Schemes | Master Functional Skills",
        "h1": "Functional Skills English Level 2 Past Papers",
        "meta_desc": "Free Functional Skills English Level 2 past papers for Pearson Edexcel, City & Guilds, AQA, NCFE, and Open Awards. Reading, Writing, and SLC.",
        "level": "Level 2",
        "subject": "English",
        "boards": [
            {
                "name": "Pearson Edexcel",
                "slug": "edexcel-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/edexcel-english-level-2-past-papers/",
                "papers_count": "Reading & Writing Papers",
                "badge": "Most Popular",
                "desc": "Pearson Edexcel Functional Skills English Level 2 Reading and Writing papers, mark schemes, and model answers."
            },
            {
                "name": "City & Guilds",
                "slug": "city-and-guilds-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/city-and-guilds-english-level-2-past-papers/",
                "papers_count": "Reading & Writing Sets",
                "badge": "City & Guilds",
                "desc": "Authentic City & Guilds 4748-02 English Level 2 past exam papers and examiner marking guidance."
            },
            {
                "name": "NCFE",
                "slug": "ncfe-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/ncfe-english-level-2-past-papers/",
                "papers_count": "NCFE Papers",
                "badge": "NCFE",
                "desc": "NCFE Level 2 Functional Skills English past papers and sample assessments for Reading and Writing."
            },
            {
                "name": "AQA",
                "slug": "aqa-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/aqa-english-level-2-past-papers/",
                "papers_count": "AQA Papers",
                "badge": "AQA",
                "desc": "AQA Functional Skills English Level 2 exam papers, insert texts, mark schemes and examiner reports."
            },
            {
                "name": "Open Awards",
                "slug": "open-awards-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/open-awards-english-level-2-past-papers/",
                "papers_count": "Online Tests & PDFs",
                "badge": "Online Interactive",
                "desc": "Official Open Awards Level 2 online onscreen Reading & Writing interactive exams, plus PDF question papers and mark schemes."
            },
            {
                "name": "TQUK",
                "slug": "tquk-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/tquk-functional-skills-english-level-2-past-papers/",
                "papers_count": "TQUK Papers",
                "badge": "TQUK",
                "desc": "TQUK Functional Skills English Level 2 past papers and sample assessments."
            },
            {
                "name": "NOCN",
                "slug": "nocn-functional-skills-english-level-2-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/nocn-functional-skills-english-level-2-past-papers/",
                "papers_count": "NOCN Papers",
                "badge": "NOCN",
                "desc": "NOCN Level 2 English practice papers and mark schemes."
            }
        ]
    },
    {
        "filename": "functional-skills-maths-level-1-past-papers.html",
        "title": "Functional Skills Maths Level 1 Past Papers & Mark Schemes | Master Functional Skills",
        "h1": "Functional Skills Maths Level 1 Past Papers",
        "meta_desc": "Free Functional Skills Maths Level 1 past papers for Pearson Edexcel, City & Guilds, NCFE, AQA, Open Awards, and TQUK with complete mark schemes.",
        "level": "Level 1",
        "subject": "Maths",
        "boards": [
            {
                "name": "Pearson Edexcel",
                "slug": "edexcel-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/edexcel-functional-skills-maths-level-1-past-papers/",
                "papers_count": "10 Practice Papers",
                "badge": "Most Popular",
                "desc": "Edexcel Level 1 Maths past papers, Section A non-calc, Section B calc, and official mark schemes."
            },
            {
                "name": "City & Guilds",
                "slug": "city-and-guilds-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/city-and-guilds-functional-skills-maths-level-1-past-papers/",
                "papers_count": "Sample Papers",
                "badge": "City & Guilds",
                "desc": "City and Guilds Functional Skills Maths Level 1 past papers and assessment materials."
            },
            {
                "name": "NCFE",
                "slug": "ncfe-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/ncfe-functional-skills-maths-level-1-past-papers/",
                "papers_count": "NCFE Papers",
                "badge": "NCFE",
                "desc": "NCFE Functional Skills Maths Level 1 question papers and mark schemes."
            },
            {
                "name": "AQA",
                "slug": "aqa-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/aqa-functional-skills-maths-level-1-past-papers/",
                "papers_count": "AQA Papers",
                "badge": "AQA",
                "desc": "AQA Functional Skills Mathematics Level 1 past papers and mark schemes."
            },
            {
                "name": "Open Awards",
                "slug": "open-awards-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/open-awards-functional-skills-maths-level-1-past-papers/",
                "papers_count": "Online Tests & PDFs",
                "badge": "Online Interactive",
                "desc": "Open Awards Functional Skills Maths Level 1 online onscreen interactive exams via XAMS simulator, plus worked solutions."
            },
            {
                "name": "TQUK",
                "slug": "tquk-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/tquk-functional-skills-maths-level-1-past-papers/",
                "papers_count": "TQUK Papers",
                "badge": "TQUK",
                "desc": "TQUK Level 1 Maths past papers and sample assessment materials."
            },
            {
                "name": "NOCN",
                "slug": "nocn-functional-skills-maths-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/nocn-functional-skills-maths-level-1-past-papers/",
                "papers_count": "NOCN Papers",
                "badge": "NOCN",
                "desc": "NOCN Functional Skills Mathematics Level 1 practice papers."
            }
        ]
    },
    {
        "filename": "functional-skills-english-level-1-past-papers.html",
        "title": "Functional Skills English Level 1 Past Papers & Mark Schemes | Master Functional Skills",
        "h1": "Functional Skills English Level 1 Past Papers",
        "meta_desc": "Free Functional Skills English Level 1 past papers for Pearson Edexcel, City & Guilds, NCFE, AQA, and Open Awards with official mark schemes.",
        "level": "Level 1",
        "subject": "English",
        "boards": [
            {
                "name": "Pearson Edexcel",
                "slug": "edexcel-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/edexcel-english-level-1-past-papers/",
                "papers_count": "Reading & Writing Papers",
                "badge": "Most Popular",
                "desc": "Edexcel Level 1 English past papers, reading texts, writing tasks, and official mark schemes."
            },
            {
                "name": "City & Guilds",
                "slug": "city-and-guilds-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/city-and-guilds-english-level-1-past-papers/",
                "papers_count": "Sample Papers",
                "badge": "City & Guilds",
                "desc": "City and Guilds Functional Skills English Level 1 past papers and mark schemes."
            },
            {
                "name": "NCFE",
                "slug": "ncfe-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/ncfe-english-level-1-past-papers/",
                "papers_count": "NCFE Papers",
                "badge": "NCFE",
                "desc": "NCFE Level 1 English past papers and sample assessment materials."
            },
            {
                "name": "AQA",
                "slug": "aqa-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/aqa-english-level-1-past-papers/",
                "papers_count": "AQA Papers",
                "badge": "AQA",
                "desc": "AQA Functional Skills English Level 1 question papers and mark schemes."
            },
            {
                "name": "Open Awards",
                "slug": "open-awards-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/open-awards-english-level-1-past-papers/",
                "papers_count": "Online Tests & PDFs",
                "badge": "Online Interactive",
                "desc": "Open Awards Level 1 English online onscreen interactive exams, assessment papers, and examiner mark schemes."
            },
            {
                "name": "TQUK",
                "slug": "tquk-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/tquk-functional-skills-english-level-1-past-papers/",
                "papers_count": "TQUK Papers",
                "badge": "TQUK",
                "desc": "TQUK Functional Skills English Level 1 past papers and answers."
            },
            {
                "name": "NOCN",
                "slug": "nocn-functional-skills-english-level-1-past-papers",
                "remote_url": "https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/nocn-functional-skills-english-level-1-past-papers/",
                "papers_count": "NOCN Papers",
                "badge": "NOCN",
                "desc": "NOCN Level 1 English practice assessments and mark schemes."
            }
        ]
    }
]

def fetch_and_build_board_page(board, subject_name, level_name):
    target_filename = f"{board['slug']}.html"
    target_path = os.path.join(PROJECT_DIR, target_filename)

    print(f"Fetching board page: {board['name']} ({subject_name} {level_name})...")
    try:
        req = urllib.request.Request(board["remote_url"], headers=HEADERS)
        with urllib.request.urlopen(req) as resp:
            raw_html = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  Error fetching {board['remote_url']}: {e}")
        raw_html = ""

    main_html = ""
    styles_in_head = ""
    page_title = f"{board['name']} Functional Skills {subject_name} {level_name} Past Papers | Master Functional Skills"

    if raw_html:
        title_m = re.search(r"<title>(.*?)</title>", raw_html)
        if title_m:
            page_title = title_m.group(1).replace("Pass Functional Skills", "Master Functional Skills")
        
        head_m = re.search(r"<head[^>]*>(.*?)</head>", raw_html, re.DOTALL)
        if head_m:
            styles = re.findall(r"<style[^>]*>.*?</style>", head_m.group(1), re.DOTALL)
            styles_in_head = "\n".join(styles)

        main_m = re.search(r"<main[^>]*>(.*?)</main>", raw_html, re.DOTALL)
        if main_m:
            main_html = main_m.group(1)

    if not main_html:
        # Fallback clean content
        main_html = f"""
        <div class="container space-top-2 space-bottom-2">
          <h1>{board['name']} Functional Skills {subject_name} {level_name} Past Papers</h1>
          <p class="lead">{board['desc']}</p>
          <div class="alert alert-info">Past paper PDF downloads and mark schemes for {board['name']} {subject_name} {level_name}.</div>
        </div>
        """

    # Replace legacy absolute links with relative or clean links
    main_html = main_html.replace("https://passfunctionalskills.co.uk/functional-skills-maths-level-2-past-papers/", "functional-skills-maths-level-2-past-papers.html")
    main_html = main_html.replace("https://passfunctionalskills.co.uk/functional-skills-english-level-2-past-papers/", "functional-skills-english-level-2-past-papers.html")
    main_html = main_html.replace("https://passfunctionalskills.co.uk/functional-skills-maths-level-1-past-papers/", "functional-skills-maths-level-1-past-papers.html")
    main_html = main_html.replace("https://passfunctionalskills.co.uk/functional-skills-english-level-1-past-papers/", "functional-skills-english-level-1-past-papers.html")
    main_html = main_html.replace("https://passfunctionalskills.co.uk/functional-skills-past-papers/", "functional-skills-past-papers.html")
    main_html = main_html.replace("Pass Functional Skills", "Master Functional Skills")
    main_html = main_html.replace("passfunctionalskills.co.uk", "masterfunctionalskills.co.uk")

    page_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="Download free {board['name']} Functional Skills {subject_name} {level_name} past papers, mark schemes, and model solutions.">
  {styles_in_head}
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

<main id="content" role="main" class="main">
{main_html}
</main>

{FOOTER}

<script>
  document.addEventListener("DOMContentLoaded", function() {{
    document.querySelectorAll('[data-toggle="collapse"], [data-bs-toggle="collapse"], .card-header[data-target]').forEach(function(btn) {{
      btn.style.cursor = "pointer";
      btn.addEventListener("click", function(e) {{
        var targetId = this.getAttribute("data-target") || this.getAttribute("data-bs-target") || this.getAttribute("href");
        if (targetId && targetId.startsWith("#")) {{
          var targetEl = document.querySelector(targetId);
          if (targetEl) {{
            e.preventDefault();
            targetEl.classList.toggle("show");
            if (targetEl.style.display === "none" || !targetEl.style.display) {{
              targetEl.style.display = targetEl.classList.contains("show") ? "block" : "none";
            }}
          }}
        }}
      }});
    }});
  }});
</script>
</body>
</html>"""

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"  [OK] Saved {target_filename}")

def get_board_logo(slug):
    s = slug.lower()
    if "edexcel" in s:
        return "assets/img/boards/edexcel.png"
    if "city-and-guilds" in s:
        return "assets/img/boards/city-and-guilds.png"
    if "aqa" in s:
        return "assets/img/boards/aqa.png"
    if "ncfe" in s:
        return "assets/img/boards/ncfe.png"
    if "open-awards" in s:
        return "assets/img/boards/open-awards.png"
    if "tquk" in s:
        return "assets/img/boards/tquk.png"
    if "nocn" in s:
        return "assets/img/boards/nocn.png"
    return "assets/img/boards/edexcel.png"

def get_clean_board_desc(slug, subject, level):
    s = slug.lower()
    if "edexcel" in s:
        return f"Official {subject} {level} past exam papers covering Section A Non-Calculator and Section B Calculator, with complete examiner mark schemes and video model solutions."
    if "city-and-guilds" in s:
        return f"Complete 4748 qualification practice assessments, sample question papers, worked answers, and examiner marking guidelines."
    if "aqa" in s:
        return f"Genuine {subject} {level} question papers, source insert texts, official marking schemes, and examiner commentary."
    if "ncfe" in s:
        return f"Comprehensive {subject} {level} past question papers, calculator and non-calculator sections, and official sample assessment materials."
    if "open-awards" in s:
        return f"Interactive live onscreen XAMS mock exam simulator, Section A & B question booklets, worked solutions, and official examiner mark schemes."
    if "tquk" in s:
        return f"Regulated assessment papers and practice tests tailored for career advancement and healthcare apprenticeships."
    if "nocn" in s:
        return f"Vocational {subject} {level} assessment papers, real-world scenario questions, and official examiner mark schemes."
    return f"Official Functional Skills {subject} {level} past papers, marking schemes, and model solutions."

def build_subject_hub(hub):
    target_path = os.path.join(PROJECT_DIR, hub["filename"])

    boards_html = ""
    for b in hub["boards"]:
        board_link = f"{b['slug']}.html"
        board_logo = get_board_logo(b['slug'])
        clean_desc = get_clean_board_desc(b['slug'], hub['subject'], hub['level'])
        is_online = "Online" in b.get('badge', '')
        badge_style = "background:rgba(37,99,235,0.12); color:#2563eb;" if is_online else "background:rgba(0,184,124,0.12); color:var(--accent);"
        badge_icon = '<i class="fa-solid fa-laptop-code" style="margin-right:4px;"></i>' if is_online else ''
        count_icon = '<i class="fa-solid fa-laptop-code" style="color:#2563eb;"></i>' if is_online else '<i class="fa-solid fa-circle-check" style="color:var(--accent);"></i>'

        boards_html += f"""
        <div style="background:#ffffff; border-radius:18px; border:1px solid var(--border); padding:24px; box-shadow:0 8px 24px rgba(7,13,30,0.06); display:flex; flex-direction:column; position:relative; transition:transform 0.2s ease, box-shadow 0.2s ease;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
            <span style="{badge_style} font-weight:800; font-size:0.75rem; padding:4px 12px; border-radius:100px; text-transform:uppercase; letter-spacing:0.5px; display:inline-flex; align-items:center;">{badge_icon}{b['badge']}</span>
            <span style="font-size:0.85rem; color:var(--navy); font-weight:700; display:inline-flex; align-items:center; gap:5px;">
              {count_icon} {b['papers_count']}
            </span>
          </div>

          <!-- PROMINENT OFFICIAL EXAM BOARD LOGO (NO REDUNDANT TEXT HEADING) -->
          <div style="height:100px; width:100%; display:flex; align-items:center; justify-content:center; background:#ffffff; border-radius:12px; border:1px solid #f1f5f9; padding:12px 18px; margin-bottom:16px; box-shadow:inset 0 0 0 1px rgba(0,0,0,0.02);">
            <img src="{board_logo}" alt="{b['name']} Official Logo" style="max-height:76px; max-width:210px; width:auto; object-fit:contain;">
          </div>

          <p style="color:var(--text-muted); font-size:0.9rem; line-height:1.55; margin-bottom:20px; flex-grow:1;">
            {clean_desc}
          </p>

          <div style="margin-top:auto; padding-top:14px; border-top:1px solid var(--border);">
            <a href="{board_link}" class="btn-card-action" style="width:100%; justify-content:center; text-align:center; padding:11px 16px; font-size:0.92rem; font-weight:700;">
              View Past Papers & Schemes →
            </a>
          </div>
        </div>
        """

    hub_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{hub['title']}</title>
  <meta name="description" content="{hub['meta_desc']}">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>{hub['h1']} <span>Exam Boards</span></h1>
        <p class="hero-description">
          Free genuine past papers, official mark schemes, model solutions, and video walkthroughs for Functional Skills {hub['subject']} {hub['level']}. Select your awarding organisation below to download official practice papers.
        </p>

        <!-- WHAT TO ADD (YOUR MOAT) -->
        <div class="moat-strip">
          <span class="moat-badge"><i class="fa-solid fa-bolt"></i> 1-Click Direct PDF Open (No Paywalls)</span>
          <span class="moat-badge"><i class="fa-solid fa-universal-access"></i> Dyslexia-Friendly Layout</span>
          <span class="moat-badge"><i class="fa-solid fa-magnifying-glass"></i> Instant Year & Series Search</span>
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
          <a href="#boards-grid" class="btn-hero-accent"><i class="fa-solid fa-list-check"></i> Choose Exam Board</a>
          <a href="functional-skills-{hub['subject'].lower()}-{hub['level'].lower().replace(' ', '-')}.html" class="btn-hero-navy"><i class="fa-solid fa-book-open"></i> Revise {hub['subject']} {hub['level']}</a>
          <a href="functional-skills-past-papers.html" class="btn-hero-outline"><i class="fa-solid fa-arrow-left"></i> All Past Papers</a>
        </div>
      </div>

      <!-- Right Column: Real Learner Photo & Pass Rates Comparison Card -->
      <div style="display:flex; flex-direction:column; gap:20px;">
        <div class="real-photo-card">
          <img src="assets/img/student-laptop.jpg" alt="Learner revising Functional Skills Past Papers" style="height:220px; object-fit:cover;">
          <div class="real-photo-overlay">
            <div style="font-size:1.6rem; color:var(--accent);"><i class="fa-solid fa-award"></i></div>
            <div>
              <strong>Official Awarding Body Past Papers</strong>
              <span>100% Free Downloads • Mark Schemes & Video Walkthroughs</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- EXAM BOARDS GRID -->
  <section class="mfs-features-section" id="boards-grid">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Select Your Awarding Exam Board</h2>
        <p>Choose an exam board to view all authentic past question papers, mark schemes, and model solutions.</p>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:24px; margin-top:32px;">
        {boards_html}
      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(hub_html)

    print(f"[OK] Generated Subject Hub: {hub['filename']}")

def build_central_past_papers_hub():
    central_html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Functional Skills Past Papers & Official Mark Schemes | Master Functional Skills</title>
  <meta name="description" content="Download free genuine past papers and official mark schemes for Pearson Edexcel, City & Guilds, Open Awards, NCFE, and AQA Functional Skills Maths and English.">
  <link rel="stylesheet" href="assets/css/mfs-theme.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
{NAV_HEADER}

  <!-- HERO SECTION -->
  <section class="mfs-hero-section">
    <div class="mfs-container mfs-hero-grid">
      <div class="hero-content">
        <h1>Functional Skills <span>Past Papers</span></h1>
        <p class="hero-description">
          Access genuine Functional Skills past papers, official mark schemes, and video model solutions for Pearson Edexcel, City & Guilds, Open Awards, NCFE, and AQA. Select your subject and level below to view all exam boards and downloadable papers.
        </p>

        <!-- WHAT TO ADD (YOUR MOAT) -->
        <div class="moat-strip">
          <span class="moat-badge"><i class="fa-solid fa-bolt"></i> 1-Click Direct PDF Open (No Paywalls)</span>
          <span class="moat-badge"><i class="fa-solid fa-universal-access"></i> Dyslexia-Friendly Layout</span>
          <span class="moat-badge"><i class="fa-solid fa-magnifying-glass"></i> Instant Year & Series Search</span>
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
          <a href="#subjects-grid" class="btn-hero-accent"><i class="fa-solid fa-download"></i> View Past Papers by Subject</a>
          <a href="functional-skills-maths-level-2.html" class="btn-hero-navy"><i class="fa-solid fa-calculator"></i> Maths Revision</a>
          <a href="functional-skills-english-level-2.html" class="btn-hero-outline"><i class="fa-solid fa-pen-nib"></i> English Revision</a>
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
              <span>Maths & English • Levels 1 & 2 • All Awarding Bodies</span>
            </div>
          </div>
        </div>

        
      </div>
    </div>
  </section>

  <!-- SUBJECTS DIRECTORY -->
  <section class="mfs-features-section" id="subjects-grid">
    <div class="mfs-container">
      <div class="mfs-section-title">
        <h2>Functional Skills Past Papers by Subject & Level</h2>
        <p>Each page contains all awarding exam boards (Edexcel, City & Guilds, NCFE, AQA, Open Awards, TQUK, NOCN) and their full past papers.</p>
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
            Free past papers and mark schemes for Pearson Edexcel, City & Guilds, Open Awards, NCFE, AQA, TQUK, and NOCN. Non-calc and calculator sections included.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Question Papers & Mark Schemes</span>
            <a href="functional-skills-maths-level-2-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards →</a>
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
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Reading & Writing Papers</span>
            <a href="functional-skills-english-level-2-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards →</a>
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
            Authentic Level 1 Maths past papers and mark schemes from Pearson Edexcel, City & Guilds, NCFE, Open Awards, and AQA to build confidence for your test.
          </p>
          <div style="margin-top:auto; padding-top:20px; border-top:1px solid var(--border); display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Question Papers & Answers</span>
            <a href="functional-skills-maths-level-1-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards →</a>
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
            <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">Reading & Writing Papers</span>
            <a href="functional-skills-english-level-1-past-papers.html" class="btn-card-action" style="padding:10px 18px;">View Exam Boards →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

{FOOTER}
</body>
</html>"""

    with open(os.path.join(PROJECT_DIR, "functional-skills-past-papers.html"), "w", encoding="utf-8") as f:
        f.write(central_html)
    with open(os.path.join(PROJECT_DIR, "past-papers.html"), "w", encoding="utf-8") as f:
        f.write(central_html)

    print("[OK] Generated Central Hub: functional-skills-past-papers.html and past-papers.html")

def main():
    import sys
    print("=== BUILDING PAST PAPERS SYSTEM ===")
    
    if "--hubs-only" in sys.argv or "-h" in sys.argv:
        print("[INFO] Rebuilding SUBJECT HUBS and CENTRAL HUB only...")
        for hub in SUBJECT_HUBS:
            print(f"Building hub: {hub['filename']}...")
            build_subject_hub(hub)
        build_central_past_papers_hub()
        print("\n=== HUBS REBUILD COMPLETE! ===")
        return

    # 1. Fetch & build board pages for each subject hub
    for hub in SUBJECT_HUBS:
        print(f"\nProcessing {hub['subject']} {hub['level']} boards...")
        for board in hub["boards"]:
            fetch_and_build_board_page(board, hub["subject"], hub["level"])
            time.sleep(0.3)
        build_subject_hub(hub)

    # 2. Build the central Past Papers hub
    build_central_past_papers_hub()
    print("\n=== PAST PAPERS SYSTEM COMPLETE! ===")

if __name__ == "__main__":
    main()
