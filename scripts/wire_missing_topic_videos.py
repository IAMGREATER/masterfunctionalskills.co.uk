#!/usr/bin/env python3
"""Clone verified #video-station masterclasses onto the 7 missing Level 2 topic pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAIRS = [
    ("assessing-the-basics-level-1.html", "assessing-the-basics.html", "replace_placeholder"),
    ("piecing-it-together-comparing-texts-level-1.html", "piecing-it-together-comparing-texts.html", "replace_placeholder"),
    ("functional-skills-capacity-level-1.html", "functional-skills-capacity.html", "before_spec"),
    ("functional-skills-length-level-1.html", "functional-skills-length.html", "before_spec"),
    ("functional-skills-line-graphs-level-1.html", "functional-skills-line-graphs.html", "before_spec"),
    ("functional-skills-time-level-1.html", "functional-skills-time.html", "before_spec"),
    ("functional-skills-weight-level-1.html", "functional-skills-weight.html", "before_spec"),
]

VIDEO_SEC_RE = re.compile(
    r'([ \t]*<!-- TOPIC VIDEO WALKTHROUGH STATION -->\s*)?<section id="video-station".*?</section>',
    re.S,
)
PLACEHOLDER_RE = re.compile(
    r'<section id="videoMasterclassStation"[^>]*>.*?</section>',
    re.S,
)
SPEC_RE = re.compile(r'(<section\b[^>]*id="specification"[^>]*>)')
TOC_SPEC_RE = re.compile(r'([ \t]*<li>\s*<a href="#specification"[^>]*>.*?</li>)', re.S)
REV_JS_RE = re.compile(r'assets/js/mfs-revision\.js(?:\?v=[^"\']+)?')


def adapt_block_for_l2(block: str) -> str:
    block = block.replace("mfs-pill-l1", "mfs-pill-l2")
    block = re.sub(
        r'(<span[^>]*class="[^"]*mfs-pill-l2[^"]*"[^>]*>)(.*?)(</span>)',
        lambda m: f"{m.group(1)}Level 2{m.group(3)}"
        if "level 1" in m.group(2).lower() and "&amp; 2" not in m.group(2).lower()
        else m.group(0),
        block,
        flags=re.I | re.S,
    )
    block = block.replace("Level 1 &amp; 2", "Level 2").replace("Level 1 & 2", "Level 2")
    block = re.sub(r"\bLevel 1\b", "Level 2", block)
    return block


def main() -> None:
    updated = 0
    for src_name, dst_name, mode in PAIRS:
        src_path = ROOT / src_name
        dst_path = ROOT / dst_name
        src_html = src_path.read_text(encoding="utf-8")
        dst_html = dst_path.read_text(encoding="utf-8")

        m_src = VIDEO_SEC_RE.search(src_html)
        if not m_src:
            raise RuntimeError(f"Could not find #video-station in {src_name}")
        adapted = adapt_block_for_l2(m_src.group(0))

        new_html = dst_html
        if 'id="video-station"' not in new_html:
            if mode == "replace_placeholder":
                if not PLACEHOLDER_RE.search(new_html):
                    raise RuntimeError(f"Could not find #videoMasterclassStation in {dst_name}")
                new_html = PLACEHOLDER_RE.sub(adapted.lstrip(), new_html, count=1)
            else:
                if not SPEC_RE.search(new_html):
                    raise RuntimeError(f"Could not find #specification in {dst_name}")
                new_html = SPEC_RE.sub(f"{adapted}\n\n        \\1", new_html, count=1)

        if 'href="#video-station"' not in new_html:
            toc_item = (
                '          <li>\n'
                '            <a href="#video-station" class="sidebar-toc-link">\n'
                '              <i class="fa-brands fa-youtube"></i> Video Masterclass\n'
                '            </a>\n'
                '          </li>\n'
            )
            new_html, n_toc = TOC_SPEC_RE.subn(f"{toc_item}\\1", new_html, count=1)
            if n_toc == 0:
                raise RuntimeError(f"Could not insert #video-station TOC link in {dst_name}")

        new_html = REV_JS_RE.sub("assets/js/mfs-revision.js?v=20261120v11", new_html)

        if new_html != dst_html:
            dst_path.write_text(new_html, encoding="utf-8")
            updated += 1
            print(f"UPDATED: {dst_name} ({mode})")
        else:
            print(f"UNCHANGED: {dst_name}")

    print(f"WIRE_MISSING_VIDEOS_UPDATED={updated}")


if __name__ == "__main__":
    main()
