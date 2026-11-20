#!/usr/bin/env python3
"""
Sprint 6: Update the 6 Revision Hubs + sw.js:
  - Distinct L1 Emerald vs L2 Amber Gold hero & row tier pills
  - Accurate curriculum topic counts
  - Wire mfs-video-modal.{css,js} across all 6 hubs
  - Attach data-ytid / poster / title metadata on entry-level-3-english.html
  - Bump sw.js cache to mfs-cache-v20261120-v19
Idempotent: re-running produces 0 further edits.
"""

from pathlib import Path
import re

ROOT = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk")
VER = "20261120v10"


def bump_hub_assets(text: str) -> str:
    text = re.sub(r'(mfs-theme\.css\?v=)[^"\']+', rf'\g<1>{VER}', text)
    text = re.sub(r'(mfs-video-modal\.css\?v=)[^"\']+', rf'\g<1>{VER}', text)
    text = re.sub(r'(mfs-video-modal\.js)(?:\?v=[^"\']+)?', rf'\1?v={VER}', text)
    if "mfs-video-modal.css" not in text:
        text = text.replace(
            "</head>",
            f'  <link rel="stylesheet" href="assets/css/mfs-video-modal.css?v={VER}">\n</head>',
            1,
        )
    if "mfs-video-modal.js" not in text:
        text = text.replace(
            '<script src="assets/js/mfs-tint.js"></script>',
            f'<script src="assets/js/mfs-tint.js"></script>\n  <script src="assets/js/mfs-video-modal.js?v={VER}"></script>',
            1,
        )
    return text


def add_row_tier_pill(text: str, tier: str) -> str:
    # Wrap .topic-category-tag inside .topic-meta-tags if not already wrapped,
    # keeping data-cat intact on .topic-category-tag for filterMfsHubTopics().
    pill_html = (
        '<span class="topic-tier-pill tier-l1"><i class="fa-solid fa-seedling"></i> Level 1 &bull; Foundation</span>'
        if tier == "l1"
        else '<span class="topic-tier-pill tier-l2"><i class="fa-solid fa-trophy"></i> Level 2 &bull; Higher</span>'
    )
    pattern = re.compile(
        r'(<div class="topic-meta">[\s\S]*?<div class="topic-title">[^\n]*?</div>\s*)'
        r'(<div class="topic-category-tag[^"]*"[^>]*>[^\n]*?</div>)(\s*</div>)',
    )

    def repl(m: re.Match) -> str:
        block = m.group(0)
        # Ensure we didn't span across another topic-meta
        if block.count('<div class="topic-meta">') > 1:
            return block
        if "topic-meta-tags" in block or "topic-tier-pill" in block:
            return block
        return (
            f"{m.group(1)}"
            f'<div class="topic-meta-tags">{m.group(2)}{pill_html}</div>'
            f"{m.group(3)}"
        )

    # Better yet: split on '<div class="topic-meta">' so each block is strictly isolated!
    parts = text.split('<div class="topic-meta">')
    out = [parts[0]]
    cat_re = re.compile(r'(<div class="topic-category-tag[^"]*"[^>]*>[^\n]*?</div>)')
    for chunk in parts[1:]:
        end_idx = chunk.find('<div class="topic-actions-group">')
        if end_idx != -1:
            head = chunk[:end_idx]
            tail = chunk[end_idx:]
            if "topic-meta-tags" not in head and "topic-tier-pill" not in head:
                head = cat_re.sub(
                    rf'<div class="topic-meta-tags">\1{pill_html}</div>',
                    head,
                    count=1,
                )
            chunk = head + tail
        out.append('<div class="topic-meta">' + chunk)
    return "".join(out)


def parse_e3_english_modal_entries() -> dict[str, dict[str, str]]:
    vm = (ROOT / "assets/js/mfs-video-modal.js").read_text(encoding="utf-8")
    out: dict[str, dict[str, str]] = {}
    for slug in [
        "e3-english-reading-everyday-texts",
        "e3-english-sentence-basics",
        "e3-english-everyday-spellings",
        "e3-english-writing-emails-and-forms",
    ]:
        m = re.search(rf"'{re.escape(slug)}'\s*:\s*\{{(.*?)\}}", vm, re.S)
        if not m:
            raise RuntimeError(f"Missing {slug} in mfs-video-modal.js")
        block = m.group(1)
        ytid = re.search(r"ytId:\s*'([^']+)'", block).group(1)
        poster = re.search(r"poster:\s*'([^']+)'", block).group(1)
        title = re.search(r"title:\s*'([^']+)'", block).group(1)
        series = re.search(r"series:\s*'([^']+)'", block).group(1)
        out[slug] = {"ytid": ytid, "poster": poster, "title": title, "series": series}
    return out


def update_hubs() -> list[str]:
    changed: list[str] = []

    # 1. Maths Level 1
    p = ROOT / "functional-skills-maths-level-1.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    t = t.replace(
        '<div class="hero-level-badge">\n          <i class="fa-solid fa-graduation-cap"></i> Level 1 Foundation Curriculum\n        </div>',
        '<div class="hero-level-badge hero-level-badge-l1">\n          <i class="fa-solid fa-seedling"></i> Level 1 Foundation Curriculum &bull; Core Skills\n        </div>',
    )
    t = t.replace("Complete 32-Topic Curriculum", "Complete 38-Topic Curriculum")
    t = add_row_tier_pill(t, "l1")
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 2. Maths Level 2
    p = ROOT / "functional-skills-maths-level-2.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    if "hero-level-badge-l2" not in t:
        t = t.replace(
            '<h1>Functional Skills <span>Maths Level 2</span></h1>',
            '<div class="hero-level-badge hero-level-badge-l2">\n          <i class="fa-solid fa-trophy"></i> Level 2 Higher Curriculum &bull; GCSE Grade 4 Equivalent\n        </div>\n        <h1>Functional Skills <span>Maths Level 2</span></h1>',
            1,
        )
    t = t.replace("Complete 39-Topic Curriculum", "Complete 44-Module Curriculum")
    t = t.replace("Over 39 dedicated topic guides", "All 44 dedicated topic guides")
    t = add_row_tier_pill(t, "l2")
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 3. English Level 1
    p = ROOT / "functional-skills-english-level-1.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    t = t.replace(
        '<div class="hero-level-badge">\n          <i class="fa-solid fa-graduation-cap"></i> Level 1 Foundation Curriculum\n        </div>',
        '<div class="hero-level-badge hero-level-badge-l1">\n          <i class="fa-solid fa-seedling"></i> Level 1 Foundation Curriculum &bull; Reading, Writing &amp; SLC\n        </div>',
    )
    t = add_row_tier_pill(t, "l1")
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 4. English Level 2
    p = ROOT / "functional-skills-english-level-2.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    if "hero-level-badge-l2" not in t:
        t = t.replace(
            '<h1>Functional Skills <span>English Level 2</span></h1>',
            '<div class="hero-level-badge hero-level-badge-l2">\n          <i class="fa-solid fa-trophy"></i> Level 2 Higher Curriculum &bull; GCSE Grade 4 Equivalent\n        </div>\n        <h1>Functional Skills <span>English Level 2</span></h1>',
            1,
        )
    t = t.replace("Over 35 dedicated topic guides", "All 46 dedicated topic guides")
    t = t.replace('<span class="badge-count">35 Topics</span>', '<span class="badge-count">46 Topics</span>')
    t = add_row_tier_pill(t, "l2")
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 5. Entry Level 3 Maths
    p = ROOT / "entry-level-3-maths.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 6. Entry Level 3 English
    p = ROOT / "entry-level-3-english.html"
    orig = p.read_text(encoding="utf-8")
    t = bump_hub_assets(orig)
    e3_meta = parse_e3_english_modal_entries()
    for slug, info in e3_meta.items():
        old_tag = f'<a href="video-solution.html?topic={slug}" target="_blank" rel="noopener" class="btn-mfs-video">'
        new_tag = (
            f'<a href="video-solution.html?topic={slug}" target="_blank" rel="noopener" class="btn-mfs-video" '
            f'data-ytid="{info["ytid"]}" data-yt-id="{info["ytid"]}" '
            f'data-topic="{info["title"].replace("&", "&amp;")}" '
            f'data-series="{info["series"]}" '
            f'data-poster="{info["poster"]}">'
        )
        t = t.replace(old_tag, new_tag)
    if t != orig:
        p.write_text(t, encoding="utf-8")
        changed.append(p.name)

    # 7. Service Worker cache bump -> v19
    sw = ROOT / "sw.js"
    sw_orig = sw.read_text(encoding="utf-8")
    sw_new = re.sub(
        r"const CACHE_NAME = 'mfs-cache-v[^']+';",
        "const CACHE_NAME = 'mfs-cache-v20261120-v19';",
        sw_orig,
        count=1,
    )
    if sw_new != sw_orig:
        sw.write_text(sw_new, encoding="utf-8")
        changed.append("sw.js")

    return changed


if __name__ == "__main__":
    updated = update_hubs()
    print("HUBS_AND_SW_OK:", len(updated), updated)
