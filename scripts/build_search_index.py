#!/usr/bin/env python3
"""Build a unified, minified search index for Global Instant Search (Ctrl+K)."""

from __future__ import annotations

import glob
import html
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_FILE = ROOT / "assets" / "data" / "mfs-search-index.json"

SKIP_NAMES = {
    "404.html",
    "booking-confirmation.html",
    "past-papers.html",
}

FLAGSHIP_URLS = {
    "index.html",
    "revise.html",
    "online-mock-simulator.html",
    "video-solution.html",
    "revision-cards.html",
    "functional-skills-past-papers.html",
    "worksheets.html",
    "pass-mark-calculator.html",
    "diagnostic-test.html",
    "bksb-remediation.html",
    "shop.html",
    "tools.html",
    "courses.html",
    "exams.html",
    "book-exam.html",
    "functional-skills-maths-level-2.html",
    "functional-skills-maths-level-1.html",
    "entry-level-3-maths.html",
    "functional-skills-english-level-2.html",
    "functional-skills-english-level-1.html",
    "entry-level-3-english.html",
    "digital-functional-skills.html",
    "digital-functional-skills-level-1.html",
    "digital-functional-skills-entry-3.html",
    "digital-functional-skills-mock-exam.html",
}

ENGLISH_PREFIXES = (
    "reading-",
    "writing-",
    "slc-",
    "assessing-the-basics",
    "common-mistakes",
    "detecting-language-techniques",
    "piecing-it-together",
    "types-of-and-navigating-sources",
    "functional-skills-english-",
)

GUIDE_URLS = {
    "index.html",
    "revise.html",
    "about.html",
    "contact-us.html",
    "tutors.html",
    "reviews.html",
    "colleges.html",
    "partnerships.html",
    "training-providers-and-employers.html",
    "career-functional-skills.html",
    "centre-policies.html",
    "open-awards-functional-skills.html",
    "functional-skills-maths-and-english.html",
}

TOOL_URLS = {
    "online-mock-simulator.html",
    "video-solution.html",
    "pass-mark-calculator.html",
    "diagnostic-test.html",
    "bksb-remediation.html",
    "revision-cards.html",
    "tools.html",
    "worksheets.html",
    "digital-functional-skills-mock-exam.html",
}


def clean_title(raw: str) -> str:
    txt = html.unescape(re.sub(r"\s+", " ", raw).strip())
    txt = re.sub(r"\s*\|\s*Master Functional Skills(?:\s*\(UK\))?.*$", "", txt, flags=re.I)
    txt = re.sub(r"\s*[—–-]\s*Master Functional Skills.*$", "", txt, flags=re.I)
    txt = re.sub(r"^Master Functional Skills\s*[—–|-]\s*", "", txt, flags=re.I)
    txt = re.sub(r"\s*\|\s*Functional Skills (?:Maths|English) Level [12] Revision.*$", "", txt, flags=re.I)
    txt = re.sub(r"\s*\|\s*(?:Level 1|Entry Level 3) Digital Skills Revision$", "", txt, flags=re.I)
    return txt.strip()


def clean_desc(raw: str) -> str:
    txt = html.unescape(re.sub(r"\s+", " ", raw).strip())
    if len(txt) <= 140:
        return txt
    cut = txt[:137].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return f"{cut}..."


def classify(rel: str, text: str, title: str) -> tuple[str, str, int, str]:
    bn = os.path.basename(rel)
    low_title = title.lower()
    theme_m = re.search(r'<html[^>]+data-theme="([^"]+)"', text, re.I)
    level_m = re.search(r'<html[^>]+data-level="([^"]+)"', text, re.I)
    theme = theme_m.group(1).lower() if theme_m else ""
    level = level_m.group(1).lower() if level_m else ""

    extra_kw: list[str] = []
    if rel in TOOL_URLS:
        cat, tier = "Tool", "tool"
        extra_kw.extend(["tool", "interactive"])
        if "simulator" in rel or "mock-exam" in rel:
            extra_kw.extend(["simulator", "exam", "mock", "onscreen"])
        if "video" in rel:
            extra_kw.extend(["video", "walkthrough", "youtube", "masterclass", "ccq"])
    elif bn == "shop.html":
        cat, tier = "Shop", "course"
        extra_kw.extend(["books", "flashcards", "revision cards", "mock pack", "bundle"])
    elif bn == "courses.html" or bn.startswith("course-"):
        cat, tier = "Course", "course"
        extra_kw.extend(["course", "tuition", "tutor", "enrol"])
    elif bn == "exams.html" or bn == "book-exam.html" or bn.startswith("exam-"):
        cat, tier = "Exam", "course"
        extra_kw.extend(["exam", "booking", "ofqual", "open awards", "remote invigilation"])
    elif bn.endswith("-past-papers.html"):
        cat, tier = "Past Papers", "papers"
        extra_kw.extend(["past papers", "mark scheme", "model solutions", "mock", "pdf"])
        for board in ("edexcel", "aqa", "ncfe", "city and guilds", "open awards", "tquk", "nocn"):
            if board.replace(" ", "-") in bn:
                extra_kw.append(board)
    elif rel.startswith("digital-skills/entry-3/") or bn == "digital-functional-skills-entry-3.html":
        cat, tier = "Digital E3", "dfs-e3"
        extra_kw.extend(["dfs", "dfsq", "digital functional skills", "entry 3", "e3"])
    elif rel.startswith("digital-skills/level-1/") or bn in (
        "digital-functional-skills-level-1.html",
        "digital-functional-skills.html",
    ):
        cat, tier = "Digital L1", "dfs-l1"
        extra_kw.extend(["dfs", "dfsq", "digital functional skills", "level 1", "l1"])
    elif bn.startswith("e3-english") or bn == "entry-level-3-english.html":
        cat, tier = "English E3", "e3"
        extra_kw.extend(["english", "entry 3", "entry level 3", "e3"])
    elif bn.startswith("e3-") or bn == "entry-level-3-maths.html":
        cat, tier = "Maths E3", "e3"
        extra_kw.extend(["maths", "entry 3", "entry level 3", "e3"])
    elif rel in GUIDE_URLS:
        cat, tier = "Guide", "tool"
        extra_kw.extend(["guide", "help", "master functional skills"])
        if "open-awards" in rel:
            extra_kw.extend(["open awards", "xams", "ofqual"])
    else:
        is_english = theme == "english" or bn.startswith(ENGLISH_PREFIXES) or "english" in low_title
        is_l1 = "-level-1" in bn or level == "level-1" or "level 1" in low_title
        if is_english:
            cat = "English L1" if is_l1 else "English L2"
            tier = "l1" if is_l1 else "l2"
            extra_kw.extend(["english", "level 1 l1" if is_l1 else "level 2 l2"])
        else:
            cat = "Maths L1" if is_l1 else "Maths L2"
            tier = "l1" if is_l1 else "l2"
            extra_kw.extend(["maths", "level 1 l1" if is_l1 else "level 2 l2"])

    if "mfs-yt-facade" in text or "video" in bn:
        extra_kw.append("video")
    if "worksheets/" in text:
        extra_kw.append("worksheets")

    if rel in FLAGSHIP_URLS:
        priority = 10
    elif bn.endswith("-past-papers.html") or bn.startswith(("course-", "exam-")) or rel in GUIDE_URLS:
        priority = 5
    else:
        priority = 1

    kw = " ".join(dict.fromkeys(" ".join(extra_kw).split()))
    return cat, tier, priority, kw


def main() -> None:
    candidates = sorted(glob.glob(str(ROOT / "*.html"))) + sorted(
        glob.glob(str(ROOT / "digital-skills" / "*" / "*.html"))
    )
    items: list[dict[str, object]] = []
    seen_urls: set[str] = set()

    for path_str in candidates:
        p = Path(path_str)
        rel = p.relative_to(ROOT).as_posix()
        bn = p.name
        if bn in SKIP_NAMES or bn.startswith(("test_", "printable-")):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in text.lower() or "http-equiv='refresh'" in text.lower():
            continue
        if rel in seen_urls:
            raise RuntimeError(f"Duplicate URL detected: {rel}")
        seen_urls.add(rel)

        title_m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
        desc_m = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']',
            text,
            re.S | re.I,
        )
        raw_title = title_m.group(1) if title_m else bn.replace(".html", "").replace("-", " ").title()
        raw_desc = desc_m.group(1) if desc_m else "Master Functional Skills revision guide, worked models and practice."
        title = clean_title(raw_title)
        desc = clean_desc(raw_desc)
        cat, tier, priority, kw = classify(rel, text, title)

        items.append(
            {
                "title": title,
                "cat": cat,
                "tier": tier,
                "url": rel,
                "desc": desc,
                "kw": kw,
                "p": priority,
            }
        )

    items.sort(key=lambda x: (-int(x["p"]), str(x["cat"]), str(x["title"])))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(
        json.dumps(items, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"SEARCH_INDEX_WRITTEN={len(items)} bytes={OUT_FILE.stat().st_size}")


if __name__ == "__main__":
    main()
