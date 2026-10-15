import os
import re
import glob

SOURCE_DIR = "/home/subi/.gemini/antigravity-cli/brain/cf91952a-80fe-45cf-b33f-b6f8ef716d1f/scratch"
PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
PFS_IMG_DIR = os.path.join(PROJECT_DIR, "assets/img/pfs")

# Map of source files to target filenames
PAGE_MAP = {
    "maths_l2_source.html": "functional-skills-maths-level-2.html",
    "homepage_source.html": "index.html",
    "functional-skills-english-level-2.html": "functional-skills-english-level-2.html",
    "functional-skills-maths-level-1.html": "functional-skills-maths-level-1.html",
    "functional-skills-english-level-1.html": "functional-skills-english-level-1.html",
    "past-papers-exact.html": "functional-skills-past-papers.html",
    "courses-exact.html": "functional-skills-courses.html",
    "exams-exact.html": "functional-skills-exam.html",
}

URL_REWRITES = [
    (r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-2/?', 'functional-skills-maths-level-2.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-2/?', 'functional-skills-english-level-2.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-maths-level-1/?', 'functional-skills-maths-level-1.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-english-level-1/?', 'functional-skills-english-level-1.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-past-papers/?', 'functional-skills-past-papers.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-courses/?', 'functional-skills-courses.html'),
    (r'https://passfunctionalskills\.co\.uk/functional-skills-exam/?', 'functional-skills-exam.html'),
    (r'https://passfunctionalskills\.co\.uk/?(?=["\'\s])', 'index.html'),
]

CLIENT_JS = '''
<script>
document.addEventListener("DOMContentLoaded", function() {
    // 1. Live Search Filter for Topic Tables
    var searchInputs = document.querySelectorAll('input[type="search"], input[name="search-query"], input[placeholder*="Search"]');
    searchInputs.forEach(function(input) {
        input.addEventListener("input", function() {
            var q = this.value.toLowerCase().trim();
            var listGroup = document.querySelector(".list-group.list-group-flush, [id^='results-']");
            if (listGroup) {
                var items = listGroup.querySelectorAll(".list-group-item:not(.bg-light)");
                items.forEach(function(item) {
                    var titleEl = item.querySelector("h4, h5, .topic-title");
                    var catEl = item.querySelector("small, .topic-cat");
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

    // 2. Mobile Dropdown Toggle
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

    document.addEventListener("click", function() {
        document.querySelectorAll(".dropdown-menu.show").forEach(function(m) {
            m.classList.remove("show");
        });
    });

    // 3. Smooth scroll
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

def clean_page(html, is_subfolder=False):
    prefix = "../" if is_subfolder else ""

    # Fix images
    def fix_img_tag(m):
        tag = m.group(0)
        lazy_m = re.search(r'data-lazy-src=[\x22\x27]([^\x22\x27]+)[\x22\x27]', tag)
        if lazy_m:
            img_url = lazy_m.group(1)
            filename = os.path.basename(img_url.split("?")[0])
            local_path = f"{prefix}assets/img/pfs/{filename}"
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
                    tag = re.sub(r'src=[\x22\x27][^\x22\x27]*[\x22\x27]', f'src="{prefix}assets/img/pfs/{filename}"', tag)
        return tag

    html = re.sub(r'<img[^>]+>', fix_img_tag, html)
    html = re.sub(r'<noscript><img[^>]+></noscript>', '', html)

    # Insert FontAwesome
    if "font-awesome" not in html.lower() or "kit.fontawesome.com" in html:
        html = html.replace("<head>", f"<head>\n    {FA_LINK}\n", 1)

    # Remove blocking rocket scripts and external tracking
    html = re.sub(r'<script type=[\x22\x27]text/rocketlazyloadscript[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*wp-rocket[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*gtm4wp[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*src=[\x22\x27][^\x22\x27]*google-analytics[^\x22\x27]*[\x22\x27][^>]*>.*?</script>', '', html, flags=re.DOTALL)

    # Rewrite URLs
    for pattern, repl in URL_REWRITES:
        html = re.sub(pattern, repl, html)

    # Ensure external target for PDFs and YouTube
    def externalize_links(m):
        full = m.group(0)
        href = m.group(1)
        if (".pdf" in href or "youtu" in href) and 'target=' not in full:
            return full.replace('<a ', '<a target="_blank" rel="noopener" ')
        return full

    html = re.sub(r'<a\s+[^>]*href=[\x22\x27]([^\x22\x27]+)[\x22\x27][^>]*>', externalize_links, html)

    # Add interactive client JS
    html = html.replace("</body>", f"{CLIENT_JS}\n</body>", 1)

    return html

# Process all pages
for src_name, target_name in PAGE_MAP.items():
    src_path = os.path.join(SOURCE_DIR, src_name)
    if os.path.exists(src_path):
        with open(src_path, "r", encoding="utf-8") as f:
            raw_html = f.read()
        cleaned = clean_page(raw_html, is_subfolder=False)
        target_path = os.path.join(PROJECT_DIR, target_name)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Processed {src_name} -> {target_name} ({len(cleaned)} bytes)")

# Also create revise.html as a direct clone or redirect to Maths L2 & curriculum
maths_l2_path = os.path.join(PROJECT_DIR, "functional-skills-maths-level-2.html")
if os.path.exists(maths_l2_path):
    with open(maths_l2_path, "r", encoding="utf-8") as f:
        m2_content = f.read()
    # Update title for Revise Hub
    rev_content = m2_content.replace(
        "<title>Functional Skills Maths Level 2 | Pass Functional Skills</title>",
        "<title>Functional Skills Revision Hub (Maths & English) | Pass Functional Skills</title>"
    )
    with open(os.path.join(PROJECT_DIR, "revise.html"), "w", encoding="utf-8") as f:
        f.write(rev_content)
    print("Updated revise.html with complete topic revision layout")

print("All site pages processed successfully!")
