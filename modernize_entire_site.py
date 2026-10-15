import os
import glob
import re

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"

# Handcrafted core pages that should not be touched by the bulk converter
SKIP_PAGES = {
    'index.html',
    'functional-skills-maths-level-2.html',
    'functional-skills-maths-level-1.html',
    'functional-skills-english-level-2.html',
    'functional-skills-english-level-1.html',
    'functional-skills-courses.html',
    'functional-skills-exam.html',
    'functional-skills-past-papers.html',
    'past-papers.html',
    'revise.html'
}

with open(os.path.join(PROJECT_DIR, "generate_modern_services_pages.py"), "r", encoding="utf-8") as f:
    services_code = f.read()

nav_match = re.search(r'NAV_HEADER = """(.*?)"""', services_code, re.DOTALL)
NAV_HEADER = nav_match.group(1).strip() if nav_match else ""

footer_match = re.search(r'FOOTER = """(.*?)"""', services_code, re.DOTALL)
FOOTER = footer_match.group(1).strip() if footer_match else ""

CLIENT_SCRIPT = """
<script>
  document.addEventListener("DOMContentLoaded", function() {
    // Vanilla accordion toggle support for exam questions and revision cards
    document.querySelectorAll('[data-toggle="collapse"], [data-bs-toggle="collapse"], .card-header[data-target], .card-header[href]').forEach(function(btn) {
      btn.style.cursor = "pointer";
      btn.addEventListener("click", function(e) {
        var targetId = this.getAttribute("data-target") || this.getAttribute("data-bs-target") || this.getAttribute("href");
        if (targetId && targetId.startsWith("#")) {
          var targetEl = document.querySelector(targetId);
          if (targetEl) {
            e.preventDefault();
            var isHidden = targetEl.classList.contains("collapse") && !targetEl.classList.contains("show");
            if (isHidden) {
              targetEl.classList.remove("collapse");
              targetEl.classList.add("show");
              targetEl.style.display = "block";
            } else {
              targetEl.classList.add("collapse");
              targetEl.classList.remove("show");
              targetEl.style.display = "none";
            }
          }
        }
      });
    });

    // Smooth scroll for hash anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
      anchor.addEventListener("click", function(e) {
        var targetId = this.getAttribute("href").substring(1);
        if (!targetId) return;
        var targetEl = document.getElementById(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: "smooth" });
        }
      });
    });
  });
</script>
"""

def modernize_file(file_path):
    filename = os.path.basename(file_path)
    if filename in SKIP_PAGES:
        return False, "Skipped (handcrafted core page)"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Must contain <header> and <footer>
    header_start_m = re.search(r"<header[^>]*>", content)
    header_end_m = re.search(r"</header>", content)
    footer_start_m = re.search(r"<footer[^>]*>", content)
    footer_end_m = re.search(r"</footer>", content)

    if not (header_start_m and header_end_m and footer_start_m and footer_end_m):
        return False, "Skipped (no standard header/footer found)"

    # 1. Update <title>
    content = re.sub(
        r"<title>(.*?)</title>",
        lambda m: f"<title>{m.group(1).replace('Pass Functional Skills', 'Master Functional Skills')}</title>",
        content,
        count=1
    )

    # 2. Inject mfs-theme.css into <head> if not already there
    if "assets/css/mfs-theme.css" not in content:
        content = content.replace("</head>", '<link rel="stylesheet" href="assets/css/mfs-theme.css">\n</head>')

    # 3. Ensure Font Awesome is in <head>
    if "font-awesome" not in content and "fontawesome" not in content:
        content = content.replace("</head>", '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />\n</head>')

    # 4. Replace from <body...> up to </header> with <body> + NAV_HEADER
    body_match = re.search(r"<body[^>]*>", content)
    if not body_match:
        return False, "No body tag found"
    
    header_end_idx = header_end_m.end()
    head_and_body_start = content[:body_match.start()]
    main_and_rest = content[header_end_idx:]

    content = head_and_body_start + "<body>\n" + NAV_HEADER + "\n" + main_and_rest

    # 5. Replace from <footer...> up to </body> with FOOTER + CLIENT_SCRIPT + </body>
    footer_start_m = re.search(r"<footer[^>]*>", content)
    body_end_m = re.search(r"</body>", content)
    if not (footer_start_m and body_end_m):
        return False, "Could not find footer/body close after replacement"

    pre_footer = content[:footer_start_m.start()]
    post_body = content[body_end_m.end():]

    content = pre_footer + FOOTER + "\n" + CLIENT_SCRIPT + "\n</body>" + post_body

    # 6. Clean legacy absolute links inside page content
    content = content.replace("https://passfunctionalskills.co.uk/functional-skills-maths-level-2/", "")
    content = content.replace("https://passfunctionalskills.co.uk/functional-skills-maths-level-1/", "")
    content = content.replace("https://passfunctionalskills.co.uk/functional-skills-english-level-2/", "")
    content = content.replace("https://passfunctionalskills.co.uk/functional-skills-english-level-1/", "")
    content = content.replace("https://passfunctionalskills.co.uk/", "")
    content = content.replace("Pass Functional Skills", "Master Functional Skills")
    content = content.replace("passfunctionalskills.co.uk", "masterfunctionalskills.co.uk")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return True, "Modernized successfully"

def main():
    html_files = sorted(glob.glob(os.path.join(PROJECT_DIR, "*.html")))
    total = len(html_files)
    updated = 0
    skipped = 0

    print(f"Starting bulk modernization of {total} HTML files...")
    for f in html_files:
        fname = os.path.basename(f)
        success, msg = modernize_file(f)
        if success:
            updated += 1
            print(f"  [OK] {fname}")
        else:
            skipped += 1
            print(f"  [-] {fname}: {msg}")

    print(f"\nCompleted! {updated} files modernized, {skipped} files skipped.")

if __name__ == "__main__":
    main()
