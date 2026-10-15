import os
import re
import glob

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
TOPICS_DIR = os.path.join(PROJECT_DIR, "topics")
os.makedirs(TOPICS_DIR, exist_ok=True)
PFS_IMG_DIR = os.path.join(PROJECT_DIR, "assets/img/pfs")
SCRATCH_TOPICS = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch/topics"

FA_LINK = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />'

NAV_DROPDOWN_CSS_ROOT = '''
<style id="pfs-nav-dropdown-styles">
@media (min-width: 992px) {
  .hs-has-sub-menu, .hs-has-mega-menu, .navbar-nav-item.hs-has-sub-menu, .navbar-nav-item.hs-has-mega-menu, .admin-nav-item.hs-has-sub-menu, .admin-nav-item.hs-has-mega-menu, .hs-sub-menu-opened {
    position: relative !important;
    overflow: visible !important;
  }
  .hs-sub-menu, .hs-mega-menu, .hs-has-sub-menu > .dropdown-menu, .hs-has-mega-menu > .dropdown-menu {
    display: none;
    position: absolute !important;
    top: 100% !important;
    left: 0 !important;
    background: #ffffff !important;
    border-radius: 12px !important;
    box-shadow: 0 20px 45px -5px rgba(15, 23, 42, 0.25), 0 0 1px 1px rgba(15, 23, 42, 0.08) !important;
    border: 1px solid rgba(226, 232, 240, 0.9) !important;
    padding: 1.5rem !important;
    z-index: 10050 !important;
  }
  .hs-sub-menu-medium { min-width: 480px !important; }
  .hs-sub-menu-large { min-width: 780px !important; }
  .hs-mega-menu { min-width: 960px !important; left: -200px !important; }
  .hs-has-sub-menu:hover > .hs-sub-menu, .hs-has-mega-menu:hover > .hs-mega-menu, .hs-has-sub-menu:hover > .dropdown-menu, .hs-has-mega-menu:hover > .dropdown-menu, .hs-sub-menu:hover, .hs-mega-menu:hover, .hs-sub-menu.show, .hs-mega-menu.show {
    display: block !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    visibility: visible !important;
  }
  .hs-sub-menu .dropdown-item, .hs-mega-menu .dropdown-item {
    display: block !important;
    padding: 0.55rem 0.85rem !important;
    color: #1e293b !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    border-radius: 6px !important;
    transition: all 0.15s ease !important;
    white-space: normal !important;
    text-decoration: none !important;
  }
  .hs-sub-menu .dropdown-item:hover, .hs-mega-menu .dropdown-item:hover {
    background-color: #f0fdf4 !important;
    color: #16a34a !important;
    padding-left: 1.15rem !important;
  }
  .mega-menu-body h5, .hs-sub-menu h5, .hs-mega-menu h5 {
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    color: #0284c7 !important;
    margin-bottom: 0.75rem !important;
    padding-bottom: 0.35rem !important;
    border-bottom: 2px solid #e0f2fe !important;
  }
}
</style>
'''

NAV_DROPDOWN_JS = '''
<script>
document.addEventListener("DOMContentLoaded", function() {
    var navItems = document.querySelectorAll(".hs-has-sub-menu, .hs-has-mega-menu, .navbar-nav-item.admin-nav-item");
    navItems.forEach(function(item) {
        var menu = item.querySelector(".hs-sub-menu, .hs-mega-menu, .dropdown-menu");
        if (!menu) return;
        var timer = null;
        function showMenu() {
            if (timer) clearTimeout(timer);
            document.querySelectorAll(".hs-sub-menu.show, .hs-mega-menu.show").forEach(function(m) {
                if (m !== menu) {
                    m.classList.remove("show");
                    m.style.removeProperty("display");
                }
            });
            menu.classList.add("show");
            menu.style.setProperty("display", "block", "important");
            item.classList.add("hs-sub-menu-opened");
        }
        function hideMenu() {
            timer = setTimeout(function() {
                menu.classList.remove("show");
                menu.style.removeProperty("display");
                item.classList.remove("hs-sub-menu-opened");
            }, 180);
        }
        item.addEventListener("mouseenter", showMenu);
        item.addEventListener("mouseleave", hideMenu);
        menu.addEventListener("mouseenter", showMenu);
        menu.addEventListener("mouseleave", hideMenu);
        var trigger = item.querySelector(".hs-mega-menu-invoker, .nav-link-toggle");
        if (trigger) {
            trigger.addEventListener("click", function(e) {
                if (menu.classList.contains("show")) {
                    menu.classList.remove("show");
                    menu.style.removeProperty("display");
                    item.classList.remove("hs-sub-menu-opened");
                } else {
                    showMenu();
                }
            });
        }
    });
    document.addEventListener("click", function(e) {
        if (!e.target.closest(".navbar-nav")) {
            document.querySelectorAll(".hs-sub-menu.show, .hs-mega-menu.show").forEach(function(m) {
                m.classList.remove("show");
                m.style.removeProperty("display");
            });
            document.querySelectorAll(".hs-sub-menu-opened").forEach(function(el) {
                el.classList.remove("hs-sub-menu-opened");
            });
        }
    });
});
</script>
'''

# 1. Process all 39 topic revision pages
topic_srcs = glob.glob(os.path.join(SCRATCH_TOPICS, "*.html"))
print(f"Processing {len(topic_srcs)} topic revision pages...")

for ts in topic_srcs:
    slug = os.path.basename(ts).replace(".html", "")
    with open(ts, "r", encoding="utf-8") as f:
        html = f.read()

    # Image replacement
    def fix_img(m):
        tag = m.group(0)
        lazy_m = re.search(r'data-lazy-src=[\x22\x27]([^\x22\x27]+)[\x22\x27]', tag)
        if lazy_m:
            img_url = lazy_m.group(1)
            fn = os.path.basename(img_url.split("?")[0])
            tag = re.sub(r'src=[\x22\x27][^\x22\x27]*[\x22\x27]', f'src="assets/img/pfs/{fn}"', tag)
            tag = re.sub(r'data-lazy-src=[\x22\x27][^\x22\x27]*[\x22\x27]', '', tag)
            tag = re.sub(r'class=[\x22\x27]([^\x22\x27]*)rocket-lazyload([^\x22\x27]*)[\x22\x27]', r'class="\1\2"', tag)
        else:
            src_m = re.search(r'src=[\x22\x27](https?://[^\x22\x27]+)[\x22\x27]', tag)
            if src_m:
                fn = os.path.basename(src_m.group(1).split("?")[0])
                if os.path.exists(os.path.join(PFS_IMG_DIR, fn)):
                    tag = re.sub(r'src=[\x22\x27][^\x22\x27]*[\x22\x27]', f'src="assets/img/pfs/{fn}"', tag)
        return tag

    html = re.sub(r'<img[^>]+>', fix_img, html)
    html = re.sub(r'<noscript><img[^>]+></noscript>', '', html)

    # Add FontAwesome CDN in <head>
    if "font-awesome" not in html.lower() or "kit.fontawesome.com" in html:
        html = html.replace("<head>", f"<head>\n    {FA_LINK}\n", 1)

    html = html.replace("</head>", f"{NAV_DROPDOWN_CSS_ROOT}\n</head>", 1)

    # Clean scripts
    html = re.sub(r'<script type=[\x22\x27]text/rocketlazyloadscript[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*wp-rocket[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*gtm4wp[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*google-analytics[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)

    # Rewrites: navbar and main routes
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/?(?=["\'\s#])', 'functional-skills-maths-level-2.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-2/?(?=["\'\s#])', 'functional-skills-english-level-2.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-1/?(?=["\'\s#])', 'functional-skills-maths-level-1.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-1/?(?=["\'\s#])', 'functional-skills-english-level-1.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-courses/?(?=["\'\s#])', 'functional-skills-courses.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-exam/?(?=["\'\s#])', 'functional-skills-exam.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-past-papers/?(?=["\'\s#])', 'functional-skills-past-papers.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/?(?=["\'\s])', 'index.html', html)

    # Rewrites for sibling topic revision links
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/([a-zA-Z0-9_-]+)/?', r'\1.html', html)

    # Ensure external target for PDFs and YouTube
    def externalize(m):
        full = m.group(0)
        href = m.group(1)
        if (".pdf" in href or "youtu" in href) and 'target=' not in full:
            return full.replace('<a ', '<a target="_blank" rel="noopener" ')
        return full
    html = re.sub(r'<a\s+[^>]*href=[\x22\x27]([^\x22\x27]+)[\x22\x27][^>]*>', externalize, html)

    html = html.replace("</body>", f"{NAV_DROPDOWN_JS}\n</body>", 1)

    # Save as root file (e.g. functional-skills-numbers-and-place-value.html)
    root_target = os.path.join(PROJECT_DIR, f"{slug}.html")
    with open(root_target, "w", encoding="utf-8") as f:
        f.write(html)

    # Also save inside topics/ folder with ../ paths
    topic_html = html.replace('src="assets/img/pfs/', 'src="../assets/img/pfs/')
    topic_html = re.sub(r'href="([a-zA-Z0-9_-]+\.html)"', r'href="../\1"', topic_html)
    sub_target = os.path.join(TOPICS_DIR, f"{slug}.html")
    with open(sub_target, "w", encoding="utf-8") as f:
        f.write(topic_html)

print("All 39 topic revision pages generated in both root and topics/ directory!")

# 2. Update functional-skills-maths-level-2.html and revise.html to point each "Revise" button to <slug>.html
with open(os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html"), "r", encoding="utf-8") as f:
    m2_html = f.read()

# Fix navbar Revise link from href="javascript:" to href="revise.html"
m2_html = m2_html.replace('href="javascript:"\n        id="navbarReviseDropdown"', 'href="revise.html"\n        id="navbarReviseDropdown"')
m2_html = m2_html.replace('href="javascript:" id="navbarReviseDropdown"', 'href="revise.html" id="navbarReviseDropdown"')

# Fix any broken topic revise links: functional-skills-maths-level-2.htmlfunctional-skills-* -> functional-skills-*.html
m2_html = re.sub(
    r'href=[\x22\x27]functional-skills-maths-level-2\.html(functional-skills-[a-zA-Z0-9_-]+)/?[\x22\x27]',
    r'href="\1.html"',
    m2_html
)

# Also fix raw live links if any remain: https://passfunctionalskills.co.uk/functional-skills-maths-level-2/functional-skills-*
m2_html = re.sub(
    r'href=[\x22\x27]https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/(functional-skills-[a-zA-Z0-9_-]+)/?[\x22\x27]',
    r'href="\1.html"',
    m2_html
)

with open(os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html"), "w", encoding="utf-8") as f:
    f.write(m2_html)

with open(os.path.join(PROJECT_DIR, "revise.html"), "w", encoding="utf-8") as f:
    f.write(m2_html)

# Also fix index.html navbar Revise link
with open(os.path.join(PROJECT_DIR, "index.html"), "r", encoding="utf-8") as f:
    idx_html = f.read()
idx_html = idx_html.replace('href="javascript:"\n        id="navbarReviseDropdown"', 'href="revise.html"\n        id="navbarReviseDropdown"')
idx_html = idx_html.replace('href="javascript:" id="navbarReviseDropdown"', 'href="revise.html" id="navbarReviseDropdown"')
with open(os.path.join(PROJECT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(idx_html)

print("Updated functional-skills-maths-level-2.html, revise.html, and index.html successfully!")
