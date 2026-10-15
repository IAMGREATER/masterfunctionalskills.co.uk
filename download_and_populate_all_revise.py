import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SCRATCH_DIR = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch"
TOPICS_ALL_DIR = os.path.join(SCRATCH_DIR, "topics_all")
os.makedirs(TOPICS_ALL_DIR, exist_ok=True)
PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
TOPICS_DIR = os.path.join(PROJECT_DIR, "topics")
os.makedirs(TOPICS_DIR, exist_ok=True)
PFS_IMG_DIR = os.path.join(PROJECT_DIR, "assets/img/pfs")
os.makedirs(PFS_IMG_DIR, exist_ok=True)

# 1. Collect all Revise URLs across all subjects and levels
subject_pages = [
    os.path.join(SCRATCH_DIR, "maths_l2_source.html"),
    os.path.join(SCRATCH_DIR, "functional-skills-english-level-2.html"),
    os.path.join(SCRATCH_DIR, "functional-skills-maths-level-1.html"),
    os.path.join(SCRATCH_DIR, "functional-skills-english-level-1.html"),
    os.path.join(SCRATCH_DIR, "entry-level-3-maths.html"),
]

all_revise_urls = set()
for sp in subject_pages:
    if os.path.exists(sp):
        with open(sp, "r", encoding="utf-8") as f:
            html = f.read()
        links = re.findall(r"href=[\x22\x27](https://passfunctionalskills\.co\.uk/[^\x22\x27]+)[\x22\x27][^>]*>Revise</a>", html)
        all_revise_urls.update(links)

print(f"Total unique Revise URLs to populate: {len(all_revise_urls)}")

# 2. Download all pages in parallel
def download_url(url):
    slug = url.strip("/").split("/")[-1]
    target_path = os.path.join(TOPICS_ALL_DIR, f"{slug}.html")
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        return slug, True, os.path.getsize(target_path)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
            with open(target_path, "wb") as f_out:
                f_out.write(data)
            return slug, True, len(data)
    except Exception as e:
        print(f"Failed {slug}: {e}")
        return slug, False, 0

print("Starting parallel download of all topic revision pages...")
with ThreadPoolExecutor(max_workers=16) as ex:
    download_results = list(ex.map(download_url, sorted(all_revise_urls)))

successful_downloads = sum(1 for _, ok, _ in download_results if ok)
print(f"Successfully downloaded {successful_downloads} / {len(all_revise_urls)} pages.")

# 3. Collect & download all images referenced by these topic pages
all_topic_images = set()
for slug, ok, _ in download_results:
    if ok:
        fpath = os.path.join(TOPICS_ALL_DIR, f"{slug}.html")
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        lazy_imgs = re.findall(r"data-lazy-src=[\x22\x27]([^\x22\x27]+)[\x22\x27]", text)
        src_imgs = re.findall(r"src=[\x22\x27](https?://[^\x22\x27]+\.(?:png|jpg|jpeg|webp|svg))[\x22\x27]", text)
        all_topic_images.update(lazy_imgs)
        all_topic_images.update(src_imgs)

missing_images = [u for u in all_topic_images if not os.path.exists(os.path.join(PFS_IMG_DIR, os.path.basename(u.split("?")[0])))]
print(f"Found {len(missing_images)} new images to download across all subjects.")

def download_img(url):
    fn = os.path.basename(url.split("?")[0])
    target = os.path.join(PFS_IMG_DIR, fn)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            with open(target, "wb") as f_out:
                f_out.write(resp.read())
            return True
    except Exception:
        return False

with ThreadPoolExecutor(max_workers=16) as ex:
    img_res = list(ex.map(download_img, missing_images))

print(f"Downloaded {sum(1 for ok in img_res if ok)} new topic assets.")

# 4. Standard Clean & Asset Rewriter for Topic Pages
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
});
</script>
'''

for url in all_revise_urls:
    slug = url.strip("/").split("/")[-1]
    raw_path = os.path.join(TOPICS_ALL_DIR, f"{slug}.html")
    if not os.path.exists(raw_path):
        continue
    with open(raw_path, "r", encoding="utf-8") as f:
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

    if "font-awesome" not in html.lower() or "kit.fontawesome.com" in html:
        html = html.replace("<head>", f"<head>\n    {FA_LINK}\n", 1)

    html = html.replace("</head>", f"{NAV_DROPDOWN_CSS_ROOT}\n</head>", 1)

    # Clean delayed scripts
    html = re.sub(r'<script type=[\x22\x27]text/rocketlazyloadscript[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*wp-rocket[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*gtm4wp[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*google-analytics[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)

    # Rewrites: main links
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/?(?=["\'\s#])', 'functional-skills-maths-level-2.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-2/?(?=["\'\s#])', 'functional-skills-english-level-2.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-1/?(?=["\'\s#])', 'functional-skills-maths-level-1.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-1/?(?=["\'\s#])', 'functional-skills-english-level-1.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-courses/?(?=["\'\s#])', 'functional-skills-courses.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-exam/?(?=["\'\s#])', 'functional-skills-exam.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/functional-skills-past-papers/?(?=["\'\s#])', 'functional-skills-past-papers.html', html)
    html = re.sub(r'https://passfunctionalskills\.co\.uk/?(?=["\'\s])', 'index.html', html)

    # Rewrites: sibling topic links
    html = re.sub(r'https://passfunctionalskills\.co\.uk/(?:functional-skills-[a-zA-Z0-9_-]+|entry-level-3-[a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)/?', r'\1.html', html)

    # Externalize PDF and YouTube links
    def externalize(m):
        full = m.group(0)
        href = m.group(1)
        if (".pdf" in href or "youtu" in href) and 'target=' not in full:
            return full.replace('<a ', '<a target="_blank" rel="noopener" ')
        return full
    html = re.sub(r'<a\s+[^>]*href=[\x22\x27]([^\x22\x27]+)[\x22\x27][^>]*>', externalize, html)

    html = html.replace("</body>", f"{NAV_DROPDOWN_JS}\n</body>", 1)

    # Save to root: <slug>.html
    with open(os.path.join(PROJECT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Save to topics/<slug>.html with subfolder path adjustment
    topic_sub_html = html.replace('src="assets/img/pfs/', 'src="../assets/img/pfs/')
    topic_sub_html = re.sub(r'href="([a-zA-Z0-9_-]+\.html)"', r'href="../\1"', topic_sub_html)
    with open(os.path.join(TOPICS_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(topic_sub_html)

print("Generated all individual topic revision guides!")

# 5. Populate and link every "Revise" button in all subject/level overview pages
def link_subject_page(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()

    # Rewrite any passfunctionalskills.co.uk topic link to <slug>.html
    c = re.sub(
        r'href=[\x22\x27]https://passfunctionalskills\.co\.uk/(?:functional-skills-[a-zA-Z0-9_-]+|entry-level-3-[a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)/?[\x22\x27]',
        r'href="\1.html"',
        c
    )
    # Fix any concatenated names
    c = re.sub(
        r'href=[\x22\x27][a-zA-Z0-9_-]+\.html([a-zA-Z0-9_-]+)/?[\x22\x27]',
        r'href="\1.html"',
        c
    )
    # Fix navbar Revise link
    c = c.replace('href="javascript:"\n        id="navbarReviseDropdown"', 'href="revise.html"\n        id="navbarReviseDropdown"')
    c = c.replace('href="javascript:" id="navbarReviseDropdown"', 'href="revise.html" id="navbarReviseDropdown"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Updated all Revise links in {os.path.basename(filepath)}")

subject_targets = [
    os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html"),
    os.path.join(PROJECT_DIR, "functional-skills-english-level-2.html"),
    os.path.join(PROJECT_DIR, "functional-skills-maths-level-1.html"),
    os.path.join(PROJECT_DIR, "functional-skills-english-level-1.html"),
    os.path.join(PROJECT_DIR, "functional-skills-entry-level-3.html"),
    os.path.join(PROJECT_DIR, "entry-level-3-maths.html"),
    os.path.join(PROJECT_DIR, "revise.html"),
    os.path.join(PROJECT_DIR, "index.html"),
]

for st in subject_targets:
    link_subject_page(st)

print("All subjects and levels populated successfully!")
