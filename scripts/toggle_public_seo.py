#!/usr/bin/env python3
"""
Master Functional Skills — Public SEO, Stealth Gate & Sitemap Launch Switch
=============================================================================
Cleanly toggles the entire site between:
  1. `--private-preview`  : Stealth Gate ENABLED (`MFS_STEALTH_PREVIEW = true`) + Disallow: / + `noindex, nofollow, noarchive, nosnippet`
  2. `--enable-indexing`  : Allow: / in robots.txt + `index, follow` on canonical public pages + refresh sitemap
  3. `--go-live-public`   : Full Step 6A Launch Switch (Stealth Gate DISABLED + public indexing + clean sitemap refresh)
  4. `--refresh-sitemap`  : Regenerates canonical `sitemap.xml` (0 redirect shims, 0 build/prototype/scratch clutter)
  5. `--status`           : Prints current indexing mode, Stealth Gate state, sitemap URL count, and Exam Checkout status
"""

from __future__ import annotations

import argparse
import datetime
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

EXCLUDED_DIRS = {
    ".git",
    "build",
    "archive",
    "scratch",
    "scratch_images",
    "assets",
    "decks",
    "scripts",
    "node_modules",
    "__pycache__",
    "docs",
    "mfs_model_engine",
    "pilots",
    "inspect_samples",
    "topics",
    "tools",
    "functional-skills-maths-level-2",
    "books",
    "a4",
    "videos",
    "publish",
    "spag",
    "dfs",
    "maths_builders",
}

NON_INDEX_BASENAMES = {
    "404.html",
    "booking-confirmation.html",
    "past-papers.html",
    "pass-functional-skills-reviews.html",
    "digital-functional-skills-level-1-original.html",
    "test_dyslexia_bar.html",
    "test_dyslexia_visual.html",
}

NON_INDEX_RELPATHS = {
    "digital-skills/index.html",
    "digital-skills/level-1/index.html",
    "digital-skills/entry-3/index.html",
}

GATE_JS_FILES = [
    os.path.join(ROOT, "assets", "js", "mfs-tint.js"),
    os.path.join(ROOT, "assets", "js", "mfs-revision.js"),
]
STEALTH_VAR_RE = re.compile(r"(var\s+MFS_STEALTH_PREVIEW\s*=\s*)(true|false)(\s*;)")


def is_redirect_shim(abs_p: str) -> bool:
    with open(abs_p, "r", encoding="utf-8", errors="ignore") as f:
        head = f.read(2048).lower()
    return 'http-equiv="refresh"' in head or "http-equiv='refresh'" in head


def iter_public_html_files() -> list[tuple[str, str]]:
    """Yield (rel_path, abs_path) for canonical public HTML pages."""
    results: list[tuple[str, str]] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            if fn in NON_INDEX_BASENAMES or fn.startswith(("test_", "_")):
                continue
            abs_p = os.path.join(dirpath, fn)
            rel_p = os.path.relpath(abs_p, ROOT).replace(os.sep, "/")
            if rel_p in NON_INDEX_RELPATHS or rel_p.startswith("printable-"):
                continue
            if is_redirect_shim(abs_p):
                continue
            results.append((rel_p, abs_p))
    return sorted(results)


def refresh_sitemap(dry_run: bool = False) -> int:
    pages = iter_public_html_files()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    top_hubs = {
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
        "functional-skills-past-papers.html",
        "revise.html",
        "video-solution.html",
        "online-mock-simulator.html",
        "revision-cards.html",
        "worksheets.html",
        "courses.html",
        "shop.html",
        "exams.html",
    }
    for rel_p, _ in pages:
        if rel_p == "index.html":
            loc = "https://masterfunctionalskills.co.uk/"
            prio = "1.0"
        elif rel_p in top_hubs:
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

    if dry_run:
        print(f"[DRY-RUN][Sitemap] Would write {len(pages)} canonical public URLs to sitemap.xml.")
        return len(pages)

    out_p = os.path.join(ROOT, "sitemap.xml")
    with open(out_p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[Sitemap] Wrote {len(pages)} canonical public URLs to sitemap.xml (0 build/redirect/prototype clutter).")
    return len(pages)


def set_stealth_gate(enabled: bool, dry_run: bool = False) -> None:
    target_val = "true" if enabled else "false"
    changed = 0
    for path in GATE_JS_FILES:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing Stealth Gate controller script: {path}")
        txt = open(path, "r", encoding="utf-8").read()
        if not STEALTH_VAR_RE.search(txt):
            raise RuntimeError(f"Missing MFS_STEALTH_PREVIEW marker in {path}")
        new_txt = STEALTH_VAR_RE.sub(rf"\g<1>{target_val}\g<3>", txt, count=1)
        if new_txt != txt:
            changed += 1
            if not dry_run:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_txt)
    state = "ENABLED (true)" if enabled else "DISABLED (false)"
    prefix = "[DRY-RUN]" if dry_run else ""
    print(f"{prefix}[Stealth Gate] MFS_STEALTH_PREVIEW -> {state} across {len(GATE_JS_FILES)} scripts ({changed} would change).")


def set_indexing_mode(enable_public: bool, dry_run: bool = False) -> None:
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

    if not dry_run:
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
            if not dry_run:
                with open(abs_p, "w", encoding="utf-8") as f:
                    f.write(nc)
            updated += 1

    mode_str = "PUBLIC INDEXING (index, follow)" if enable_public else "PRIVATE PREVIEW (noindex, Disallow: /)"
    prefix = "[DRY-RUN]" if dry_run else ""
    print(f"{prefix}[SEO Toggle] Mode -> {mode_str}; robots.txt + {updated} HTML pages.")


def get_gate_state(path: str) -> str:
    if not os.path.exists(path):
        return "MISSING"
    txt = open(path, "r", encoding="utf-8").read()
    m = STEALTH_VAR_RE.search(txt)
    if not m:
        return "NO_MARKER"
    return "ENABLED" if m.group(2) == "true" else "DISABLED"


def get_bookings_state() -> str:
    book_p = os.path.join(ROOT, "book-exam.html")
    if not os.path.exists(book_p):
        return "MISSING"
    txt = open(book_p, "r", encoding="utf-8").read()
    m = re.search(r'BOOKINGS_OPEN\s*=\s*(true|false)', txt)
    return m.group(1) if m else "UNKNOWN"


def show_status() -> None:
    robots_path = os.path.join(ROOT, "robots.txt")
    rc = open(robots_path, "r", encoding="utf-8").read() if os.path.exists(robots_path) else ""
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm_count = open(sm_path, "r", encoding="utf-8").read().count("<url>") if os.path.exists(sm_path) else 0
    mode = "PRIVATE PREVIEW (Disallow: /)" if "Disallow: /\n" in rc or rc.strip().endswith("Disallow: /") else "PUBLIC INDEXING"
    tint_gate = get_gate_state(GATE_JS_FILES[0])
    rev_gate = get_gate_state(GATE_JS_FILES[1])
    bookings_open = get_bookings_state()
    print(f"Current SEO Mode : {mode}")
    print(f"Stealth Gate     : mfs-tint.js={tint_gate} / mfs-revision.js={rev_gate}")
    print(f"Sitemap URL Count: {sm_count}")
    print(f"Exam Checkout    : BOOKINGS_OPEN={bookings_open}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--refresh-sitemap", action="store_true")
    ap.add_argument("--enable-indexing", action="store_true")
    ap.add_argument("--go-live-public", action="store_true")
    ap.add_argument("--private-preview", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.refresh_sitemap:
        refresh_sitemap(dry_run=args.dry_run)
    if args.go_live_public:
        set_stealth_gate(False, dry_run=args.dry_run)
        set_indexing_mode(True, dry_run=args.dry_run)
        refresh_sitemap(dry_run=args.dry_run)
    elif args.enable_indexing:
        set_indexing_mode(True, dry_run=args.dry_run)
        refresh_sitemap(dry_run=args.dry_run)
    elif args.private_preview:
        set_stealth_gate(True, dry_run=args.dry_run)
        set_indexing_mode(False, dry_run=args.dry_run)

    if args.status or not (
        args.refresh_sitemap or args.enable_indexing or args.go_live_public or args.private_preview
    ):
        show_status()


if __name__ == "__main__":
    main()
