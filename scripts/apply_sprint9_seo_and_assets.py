#!/usr/bin/env python3
"""
Sprint 9 — Sitewide Open Graph / Twitter Card Meta, PWA Manifest Parity & Cache-Buster Unification.

Idempotently updates all canonical non-redirect HTML pages (root + digital-skills/*) plus 404.html:
1. Unifies core CSS/JS cache-busters to ?v=20261120v12.
2. Adds manifest.json, apple-touch-icon, and theme-color to canonical pages missing them.
3. Inserts/replaces a clean delimited Open Graph & Twitter Card block on all 332 indexed public pages.
"""

from __future__ import annotations

import glob
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSET_VERSION = "20261120v12"
OG_IMAGE_URL = "https://masterfunctionalskills.co.uk/assets/img/mfs-og-card.png"
OG_IMAGE_ALT = "Master Functional Skills — UK Maths, English and Digital Functional Skills Revision, Past Papers and Exams"

CORE_ASSETS = [
    "mfs-theme.css",
    "mfs-mobile.css",
    "mfs-mobile.js",
    "mfs-revision.css",
    "mfs-revision.js",
    "mfs-tint.js",
    "mfs-video-modal.css",
    "mfs-video-modal.js",
    "mfs-video-checks.css",
    "mfs-video-checks.js",
]

OG_START = "<!-- MFS-OG-START -->"
OG_END = "<!-- MFS-OG-END -->"
OG_BLOCK_RE = re.compile(
    r"\n?\s*<!-- MFS-OG-START -->.*?<!-- MFS-OG-END -->",
    re.S,
)

PWA_START = "<!-- MFS-PWA-START -->"
PWA_END = "<!-- MFS-PWA-END -->"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
DESC_RE = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']',
    re.S | re.I,
)
CANON_RE = re.compile(
    r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']',
    re.S | re.I,
)

ASSET_ATTR_RE = re.compile(
    r'((?:href|src)=["\'][^"\']*?(?:'
    + "|".join(re.escape(a) for a in CORE_ASSETS)
    + r'))(?:\?v=[^"\']*)?(["\'])'
)


def is_redirect_shim(text: str) -> bool:
    head = text[:2048].lower()
    return 'http-equiv="refresh"' in head or "http-equiv='refresh'" in head


def clean_meta_val(raw: str) -> str:
    txt = html.unescape(re.sub(r"\s+", " ", raw).strip())
    return html.escape(txt, quote=True)


def unify_cache_busters(text: str) -> str:
    return ASSET_ATTR_RE.sub(rf"\1?v={ASSET_VERSION}\2", text)


def ensure_pwa_head(text: str, rel: str) -> str:
    prefix = "../../" if "/" in rel else ""
    head_close = text.find("</head>")
    if head_close == -1:
        return text

    head_chunk = text[:head_close]
    additions: list[str] = []
    if 'rel="manifest"' not in head_chunk and "rel='manifest'" not in head_chunk:
        additions.append(f'  <link rel="manifest" href="{prefix}manifest.json">')
    if 'name="theme-color"' not in head_chunk and "name='theme-color'" not in head_chunk:
        additions.append('  <meta name="theme-color" content="#0b172d">')
    if 'rel="apple-touch-icon"' not in head_chunk and "rel='apple-touch-icon'" not in head_chunk:
        additions.append(f'  <link rel="apple-touch-icon" href="{prefix}assets/img/favicon-192x192.png">')

    if not additions:
        return text

    block = f"\n  {PWA_START}\n" + "\n".join(additions) + f"\n  {PWA_END}\n"
    return text[:head_close] + block + text[head_close:]


def upsert_og_tags(text: str, rel: str) -> str:
    # Exclude non-indexed utility pages (booking-confirmation & 404)
    if rel in {"booking-confirmation.html", "404.html"}:
        return text

    title_m = TITLE_RE.search(text)
    desc_m = DESC_RE.search(text)
    canon_m = CANON_RE.search(text)

    title_esc = clean_meta_val(title_m.group(1)) if title_m else "Master Functional Skills"
    desc_esc = (
        clean_meta_val(desc_m.group(1))
        if desc_m
        else "Free Functional Skills Maths, English and Digital Functional Skills revision guides, past papers, video walkthroughs and online exams."
    )
    default_url = (
        "https://masterfunctionalskills.co.uk/"
        if rel == "index.html"
        else f"https://masterfunctionalskills.co.uk/{rel}"
    )
    url_esc = html.escape(canon_m.group(1).strip() if canon_m else default_url, quote=True)

    og_block = "\n".join(
        [
            f"  {OG_START}",
            '  <meta property="og:type" content="website">',
            '  <meta property="og:site_name" content="Master Functional Skills">',
            '  <meta property="og:locale" content="en_GB">',
            f'  <meta property="og:title" content="{title_esc}">',
            f'  <meta property="og:description" content="{desc_esc}">',
            f'  <meta property="og:url" content="{url_esc}">',
            f'  <meta property="og:image" content="{OG_IMAGE_URL}">',
            '  <meta property="og:image:width" content="1200">',
            '  <meta property="og:image:height" content="630">',
            f'  <meta property="og:image:alt" content="{html.escape(OG_IMAGE_ALT, quote=True)}">',
            '  <meta name="twitter:card" content="summary_large_image">',
            f'  <meta name="twitter:title" content="{title_esc}">',
            f'  <meta name="twitter:description" content="{desc_esc}">',
            f'  <meta name="twitter:image" content="{OG_IMAGE_URL}">',
            f"  {OG_END}",
        ]
    )

    if OG_START in text and OG_END in text:
        return OG_BLOCK_RE.sub("\n" + og_block, text, count=1)

    head_close = text.find("</head>")
    if head_close == -1:
        return text
    return text[:head_close] + og_block + "\n" + text[head_close:]


def main() -> None:
    candidates = sorted(glob.glob(str(ROOT / "*.html"))) + sorted(
        glob.glob(str(ROOT / "digital-skills" / "*" / "*.html"))
    )

    canonical_count = 0
    og_count = 0
    modified = 0

    for path_str in candidates:
        p = Path(path_str)
        rel = p.relative_to(ROOT).as_posix()
        bn = p.name

        if bn.startswith(("test_", "_")):
            continue
        if rel.startswith("printable-"):
            continue

        orig = p.read_text(encoding="utf-8", errors="ignore")
        if is_redirect_shim(orig):
            continue

        updated = unify_cache_busters(orig)
        if rel != "404.html":
            canonical_count += 1
            updated = ensure_pwa_head(updated, rel)
            updated = upsert_og_tags(updated, rel)
            if rel != "booking-confirmation.html":
                og_count += 1

        if updated != orig:
            p.write_text(updated, encoding="utf-8")
            modified += 1

    print(
        f"SPRINT9_SEO_ASSETS canonical_pages={canonical_count} og_pages={og_count} modified={modified}"
    )


if __name__ == "__main__":
    main()
