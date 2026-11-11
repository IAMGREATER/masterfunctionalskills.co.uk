#!/usr/bin/env python3
"""
Master Functional Skills — Public SEO & Sitemap Launch Switch
=============================================================
Cleanly toggles the entire site between:
  1. `--private-preview`  : Disallow: / in robots.txt + `noindex, nofollow` meta tags
  2. `--enable-indexing`  : Allow: / in robots.txt (blocking only build/archive/scratch) + `index, follow` on canonical public pages
  3. `--refresh-sitemap`  : Regenerates canonical `sitemap.xml` (excluding build/, archive/, scratch/, test_*, 404.html, prototypes)
  4. `--status`           : Prints current indexing mode and sitemap URL count
"""

import argparse
import datetime
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

EXCLUDED_DIRS = {".git", "build", "archive", "scratch", "assets", "decks", "scripts", "node_modules", "__pycache__"}
NON_INDEX_BASENAMES = {
    "404.html",
    "digital-functional-skills-level-1-original.html",
    "test_dyslexia_bar.html",
    "test_dyslexia_visual.html",
}
NON_INDEX_RELPATHS = {
    "digital-skills/index.html",
    "digital-skills/level-1/index.html",
    "digital-skills/entry-3/index.html",
}


def iter_public_html_files():
    """Yield (rel_path, abs_path) for canonical public HTML pages."""
    results = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            if fn in NON_INDEX_BASENAMES or fn.startswith("test_") or fn.startswith("_"):
                continue
            abs_p = os.path.join(dirpath, fn)
            rel_p = os.path.relpath(abs_p, ROOT).replace(os.sep, "/")
            if rel_p in NON_INDEX_RELPATHS:
                continue
            results.append((rel_p, abs_p))
    return sorted(results)


def refresh_sitemap() -> int:
    pages = iter_public_html_files()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for rel_p, _ in pages:
        if rel_p == "index.html":
            loc = "https://masterfunctionalskills.co.uk/"
            prio = "1.0"
        elif rel_p in (
            "functional-skills-maths-level-2.html",
            "functional-skills-english-level-2.html",
            "functional-skills-maths-level-1.html",
            "functional-skills-english-level-1.html",
            "entry-level-3-english.html",
            "entry-level-3-maths.html",
            "digital-functional-skills.html",
            "digital-functional-skills-level-1.html",
            "digital-functional-skills-entry-3.html",
            "open-awards-functional-skills.html",
            "past-papers.html",
            "exams.html",
        ):
            loc = f"https://masterfunctionalskills.co.uk/{rel_p}"
            prio = "0.95"
        elif "open-awards" in rel_p or "past-papers" in rel_p or rel_p == "centre-policies.html":
            loc = f"https://masterfunctionalskills.co.uk/{rel_p}"
            prio = "0.9"
        elif rel_p.startswith("worksheets/"):
            loc = f"https://masterfunctionalskills.co.uk/{rel_p}"
            prio = "0.75"
        else:
            loc = f"https://masterfunctionalskills.co.uk/{rel_p}"
            prio = "0.85"
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
    lines.append("</urlset>\n")
    out_p = os.path.join(ROOT, "sitemap.xml")
    with open(out_p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[Sitemap] Wrote {len(pages)} canonical public URLs to sitemap.xml (0 build/prototype clutter).")
    return len(pages)


def set_indexing_mode(enable_public: bool):
    robots_path = os.path.join(ROOT, "robots.txt")
    if enable_public:
        robots_txt = (
            "# Master Functional Skills — Public Search Indexing Enabled\n"
            "User-agent: *\n"
            "Allow: /\n"
            "Disallow: /archive/\n"
            "Disallow: /build/\n"
            "Disallow: /scratch/\n"
            "Disallow: /dfs-prototype-explorer.html\n\n"
            "Sitemap: https://masterfunctionalskills.co.uk/sitemap.xml\n"
        )
        meta_val = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    else:
        robots_txt = "# Strict search engine block - private preview\nUser-agent: *\nDisallow: /\n"
        meta_val = "noindex, nofollow, noarchive, nosnippet"

    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_txt)

    updated = 0
    meta_pat = re.compile(r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*["\']\s*/?>', re.I)
    for _, abs_p in iter_public_html_files():
        with open(abs_p, "r", encoding="utf-8") as f:
            c = f.read()
        if meta_pat.search(c):
            nc = meta_pat.sub(f'<meta name="robots" content="{meta_val}">', c)
        elif "</head>" in c:
            nc = c.replace("</head>", f'  <meta name="robots" content="{meta_val}">\n</head>', 1)
        else:
            nc = c
        if nc != c:
            with open(abs_p, "w", encoding="utf-8") as f:
                f.write(nc)
            updated += 1

    mode_str = "PUBLIC INDEXING (index, follow)" if enable_public else "PRIVATE PREVIEW (noindex, Disallow: /)"
    print(f"[SEO Toggle] Mode -> {mode_str}; updated robots.txt and {updated} HTML pages.")


def show_status():
    robots_path = os.path.join(ROOT, "robots.txt")
    rc = open(robots_path, "r", encoding="utf-8").read() if os.path.exists(robots_path) else ""
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm_count = open(sm_path, "r", encoding="utf-8").read().count("<url>") if os.path.exists(sm_path) else 0
    mode = "PRIVATE PREVIEW (Disallow: /)" if "Disallow: /\n" in rc or rc.strip().endswith("Disallow: /") else "PUBLIC INDEXING"
    print(f"Current SEO Mode : {mode}")
    print(f"Sitemap URL Count: {sm_count}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--refresh-sitemap", action="store_true")
    ap.add_argument("--enable-indexing", action="store_true")
    ap.add_argument("--private-preview", action="store_true")
    args = ap.parse_args()

    if args.refresh_sitemap:
        refresh_sitemap()
    if args.enable_indexing:
        set_indexing_mode(True)
        refresh_sitemap()
    elif args.private_preview:
        set_indexing_mode(False)
    if args.status or not (args.refresh_sitemap or args.enable_indexing or args.private_preview):
        show_status()


if __name__ == "__main__":
    main()
