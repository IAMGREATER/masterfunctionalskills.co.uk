import os
import re
import glob

SCRATCH_DIR = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch"
PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
PFS_IMG_DIR = os.path.join(PROJECT_DIR, "assets/img/pfs")
NEXTCLOUD_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"

PAGE_MAP = {
    "homepage_source.html": "index.html",
    "maths_l2_source.html": "functional-skills-maths-level-2.html",
    "functional-skills-english-level-2.html": "functional-skills-english-level-2.html",
    "functional-skills-maths-level-1.html": "functional-skills-maths-level-1.html",
    "functional-skills-english-level-1.html": "functional-skills-english-level-1.html",
    "functional-skills-entry-level-3.html": "functional-skills-entry-level-3.html",
    "maths-and-english.html": "functional-skills-maths-and-english.html",
    "courses-exact.html": "functional-skills-courses.html",
    "exams-exact.html": "functional-skills-exam.html",
    "past-papers-exact.html": "functional-skills-past-papers.html",
    "exam-maths-l2.html": "exam-maths-l2.html",
    "exam-english-l2.html": "exam-english-l2.html",
    "course-maths-l2.html": "course-maths-l2.html",
    "course-english-l2.html": "course-english-l2.html",
    "contact-us.html": "contact-us.html",
    "diagnostic-test.html": "diagnostic-test.html",
    "training-providers.html": "training-providers-and-employers.html",
    "colleges.html": "colleges.html",
    "career-functional-skills.html": "career-functional-skills.html",
    "reviews.html": "pass-functional-skills-reviews.html",
}

URL_REWRITES = [
    (r'https://passfunctionalskills\.co\.uk/shop/exams/functional-skills-maths-level-2-online-exam/?', 'exam-maths-l2.html'),
    (r'https://passfunctionalskills\.co\.uk/shop/exams/functional-skills-english-level-2-online-exam/?', 'exam-english-l2.html'),
    (r'https://passfunctionalskills\.co\.uk/shop/courses/functional-skills-maths-level-2-course/?', 'course-maths-l2.html'),
    (r'https://passfunctionalskills\.co\.uk/shop/courses/functional-skills-english-level-2-course/?', 'course-english-l2.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/?', 'functional-skills-maths-level-2.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-2/?', 'functional-skills-english-level-2.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-1/?', 'functional-skills-maths-level-1.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-1/?', 'functional-skills-english-level-1.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-entry-level-3/?', 'functional-skills-entry-level-3.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-maths-and-english/?', 'functional-skills-maths-and-english.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-courses/?', 'functional-skills-courses.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-exam/?', 'functional-skills-exam.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-past-papers/?', 'functional-skills-past-papers.html'),
    (r'https://passfunctionalskills\.co\.uk/contact-us/?', 'contact-us.html'),
    (r'https://passfunctionalskills\.co\.uk/diagnostic-test/?', 'diagnostic-test.html'),
    (r'https://passfunctionalskills\.co\.uk/training-providers-and-employers/?', 'training-providers-and-employers.html'),
    (r'https://passfunctionalskills\.co\.uk/colleges/?', 'colleges.html'),
    (r'https://passfunctionalskills\.co\.uk/career-functional-skills/?', 'career-functional-skills.html'),
    (r'https://passfunctionalskills\.co\.uk/pass-functional-skills-reviews/?', 'pass-functional-skills-reviews.html'),
    (r'https://passfunctionalskills\.co\.uk/?(?=["\'\s])', 'index.html'),
]

NAV_DROPDOWN_CSS = '''
<style id="pfs-nav-dropdown-styles">
/* ===== NAVIGATION MEGA-MENU & DROPDOWN POPUPS ON HOVER ===== */
@media (min-width: 992px) {
  /* Crucial: Prevent clipping from ancestor containers */
  .hs-has-sub-menu, 
  .hs-has-mega-menu, 
  .navbar-nav-item.hs-has-sub-menu, 
  .navbar-nav-item.hs-has-mega-menu,
  .admin-nav-item.hs-has-sub-menu,
  .admin-nav-item.hs-has-mega-menu,
  .hs-sub-menu-opened {
    position: relative !important;
    overflow: visible !important;
  }

  /* Base dropdown hidden state */
  .hs-sub-menu, 
  .hs-mega-menu, 
  .hs-has-sub-menu > .dropdown-menu, 
  .hs-has-mega-menu > .dropdown-menu {
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

  .hs-sub-menu-medium {
    min-width: 480px !important;
  }

  .hs-sub-menu-large {
    min-width: 780px !important;
  }

  .hs-mega-menu {
    min-width: 960px !important;
    left: -200px !important;
  }

  /* Show state on hover or when .show class is added */
  .hs-has-sub-menu:hover > .hs-sub-menu,
  .hs-has-mega-menu:hover > .hs-mega-menu,
  .hs-has-sub-menu:hover > .dropdown-menu,
  .hs-has-mega-menu:hover > .dropdown-menu,
  .hs-sub-menu:hover,
  .hs-mega-menu:hover,
  .hs-sub-menu.show,
  .hs-mega-menu.show,
  .hs-has-sub-menu > .dropdown-menu.show,
  .hs-has-mega-menu > .dropdown-menu.show {
    display: block !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    visibility: visible !important;
  }

  /* Dropdown Link Items Styling */
  .hs-sub-menu .dropdown-item, 
  .hs-mega-menu .dropdown-item {
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

  .hs-sub-menu .dropdown-item:hover, 
  .hs-mega-menu .dropdown-item:hover {
    background-color: #f0fdf4 !important;
    color: #16a34a !important;
    padding-left: 1.15rem !important;
  }

  /* Subheadings inside mega menu */
  .mega-menu-body h5, 
  .hs-sub-menu h5, 
  .hs-mega-menu h5 {
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
    // 1. Navigation Hover & Click Dropdowns
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
                e.preventDefault();
                e.stopPropagation();
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

    // 2. Live Topic Search Filter
    var searchInputs = document.querySelectorAll('input[type="search"], input[name="search-query"], input[placeholder*="Search"]');
    searchInputs.forEach(function(input) {
        input.addEventListener("input", function() {
            var q = this.value.toLowerCase().trim();
            var listGroup = document.querySelector(".list-group.list-group-flush, [id^='results-']");
            if (listGroup) {
                var items = listGroup.querySelectorAll(".list-group-item:not(.bg-light)");
                items.forEach(function(item) {
                    var text = item.textContent.toLowerCase();
                    if (text.indexOf(q) !== -1) {
                        item.style.setProperty("display", "block", "important");
                    } else {
                        item.style.setProperty("display", "none", "important");
                    }
                });
            }
        });
        var form = input.closest("form");
        if (form) {
            form.addEventListener("submit", function(e) { e.preventDefault(); });
        }
    });

    // 3. Mobile Dropdown Toggle (Resource buttons)
    document.querySelectorAll("[data-toggle='dropdown']").forEach(function(btn) {
        btn.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            var menu = this.nextElementSibling;
            if (menu) {
                var isShown = menu.classList.contains("show");
                document.querySelectorAll(".dropdown-menu.show").forEach(function(m) {
                    m.classList.remove("show");
                });
                if (!isShown) menu.classList.add("show");
            }
        });
    });

    // 4. Smooth Anchor Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener("click", function(e) {
            var href = this.getAttribute("href");
            if (!href || href === "#") return;
            var targetEl = document.getElementById(href.substring(1));
            if (targetEl) {
                e.preventDefault();
                targetEl.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
</script>
'''

FA_LINK = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />'

def clean_page(html):
    # Fix images
    def fix_img_tag(m):
        tag = m.group(0)
        lazy_m = re.search(r'data-lazy-src=[\x22\x27]([^\x22\x27]+)[\x22\x27]', tag)
        if lazy_m:
            img_url = lazy_m.group(1)
            filename = os.path.basename(img_url.split("?")[0])
            local_path = f"assets/img/pfs/{filename}"
            tag = re.sub(r'src=[\x22\x27][^\x22\x27]*[\x22\x27]', f'src="{local_path}"', tag)
            tag = re.sub(r'data-lazy-src=[\x22\x27][^\x22\x27]*[\x22\x27]', '', tag)
            tag = re.sub(r'class=[\x22\x27]([^\x22\x27]*)rocket-lazyload([^\x22\x27]*)[\x22\x27]', r'class="\1\2"', tag)
        else:
            src_m = re.search(r'src=[\x22\x27](https?://[^\x22\x27]+)[\x22\x27]', tag)
            if src_m:
                img_url = src_m.group(1)
                filename = os.path.basename(img_url.split("?")[0])
                local_file = os.path.join(PFS_IMG_DIR, filename)
                if os.path.exists(local_file):
                    tag = re.sub(r'src=[\x22\x27][^\x22\x27]*[\x22\x27]', f'src="assets/img/pfs/{filename}"', tag)
        return tag

    html = re.sub(r'<img[^>]+>', fix_img_tag, html)
    html = re.sub(r'<noscript><img[^>]+></noscript>', '', html)

    # Add FontAwesome CDN in <head>
    if "font-awesome" not in html.lower() or "kit.fontawesome.com" in html:
        html = html.replace("<head>", f"<head>\n    {FA_LINK}\n", 1)

    # Inject Hover Styles in <head>
    html = html.replace("</head>", f"{NAV_DROPDOWN_CSS}\n</head>", 1)

    # Remove blocking scripts
    html = re.sub(r'<script type=[\x22\x27]text/rocketlazyloadscript[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*wp-rocket[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*gtm4wp[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*google-analytics[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)

    # Rewrite URLs
    for pattern, repl in URL_REWRITES:
        html = re.sub(pattern, repl, html)

    # Externalize PDF and YouTube links
    def externalize(m):
        full = m.group(0)
        href = m.group(1)
        if (".pdf" in href or "youtu" in href) and 'target=' not in full:
            return full.replace('<a ', '<a target="_blank" rel="noopener" ')
        return full

    html = re.sub(r'<a\s+[^>]*href=[\x22\x27]([^\x22\x27]+)[\x22\x27][^>]*>', externalize, html)

    # Inject interactive JS
    html = html.replace("</body>", f"{NAV_DROPDOWN_JS}\n</body>", 1)

    return html

# Build all pages
for src_name, target_name in PAGE_MAP.items():
    src_path = os.path.join(SCRATCH_DIR, src_name)
    if os.path.exists(src_path):
        with open(src_path, "r", encoding="utf-8") as f:
            raw_html = f.read()
        cleaned = clean_page(raw_html)
        target_path = os.path.join(PROJECT_DIR, target_name)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Generated {target_name} ({len(cleaned)} bytes)")

# Ensure revise.html is synced with functional-skills-maths-level-2.html
m2_path = os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html")
if os.path.exists(m2_path):
    with open(m2_path, "r", encoding="utf-8") as f:
        rev_html = f.read()
    with open(os.path.join(PROJECT_DIR, "revise.html"), "w", encoding="utf-8") as f:
        f.write(rev_html)
    print("Updated revise.html")

print("All cloned pages generated successfully!")
