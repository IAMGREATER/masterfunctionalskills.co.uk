#!/usr/bin/env python3
"""
Sprint 6: Uniform Design Language System, Tier Differentiation & Maths L1 Cleanup.
Idempotent sitewide transform across all MFS revision topic HTML pages.
"""

from pathlib import Path
import glob
import os
import re

ROOT = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk")

REQUIRED_AVATARS = [
    "assets/img/avatars/subi.png",
    "assets/img/avatars/sonya.png",
    "assets/img/avatars/tutor-emma.jpg",
]

UTILITY_PAGES = {
    "digital-functional-skills-mock-exam.html",
    "digital-functional-skills-past-papers.html",
    "digital-functional-skills.html",
    "digital-functional-skills-level-1.html",
    "digital-functional-skills-entry-3.html",
    "entry-level-3-maths.html",
    "entry-level-3-english.html",
    "online-mock-simulator.html",
    "worksheets.html",
}


def classify_tier(rel_path: str) -> str | None:
    if rel_path in UTILITY_PAGES:
        return None
    base = os.path.basename(rel_path)
    if "-level-1.html" in base or rel_path.startswith("digital-skills/level-1/"):
        return "level-1"
    if (
        base.startswith("e3-")
        or base.startswith("entry-level-3-english-")
        or rel_path.startswith("digital-skills/entry-3/")
    ):
        return "entry-3"
    return "level-2"


def is_maths_l2_only(rel_path: str) -> bool:
    base = os.path.basename(rel_path)
    if not base.startswith("functional-skills-"):
        return False
    if "-level-1" in base or "english" in base or "past-papers" in base or "maths-level" in base or "entry-level" in base or "exam" in base:
        return False
    l1_equiv = ROOT / rel_path.replace(".html", "-level-1.html")
    return not l1_equiv.exists()


def main() -> None:
    for av in REQUIRED_AVATARS:
        if not (ROOT / av).exists():
            raise FileNotFoundError(f"Missing required avatar asset: {av}")

    html_files = sorted(
        glob.glob(str(ROOT / "*.html")) + glob.glob(str(ROOT / "digital-skills/*/*.html"))
    )

    stats = {
        "scanned": 0,
        "changed": 0,
        "tuple_fixes": 0,
        "pill_l2_fixes": 0,
        "hero_pills_updated": 0,
        "l1_switch_updated": 0,
        "l2_only_pill_cleaned": 0,
        "l1_steps_upgraded": 0,
        "l1_skill_cards_upgraded": 0,
        "area_fixes": 0,
    }

    tuple_re = re.compile(
        r"""<div style="font-size:0\.94rem;\s*color:#0f766e;"><strong>\('([^']+)',\s*'([^']+)',\s*'([^']+)'\)&rsquo;s Level 1 Exam Tip:</strong>(.*?)</div>""",
        re.S,
    )
    hero_row_re = re.compile(r'(<div class="revision-hero-pill-row">.*?</div>)', re.S)
    css_ver_re = re.compile(r'(mfs-revision\.css\?v=)[^"\']+')
    step_l1_re = re.compile(
        r'<div class="model-step-col-desc" style="font-variant-numeric:tabular-nums;">\s*'
        r'<div>(.*?)</div>\s*'
        r'<div style="margin-top:6px;\s*display:inline-block;\s*background:#e0f2fe;[^"]*">(.*?)</div>\s*</div>',
        re.S,
    )
    skill_l1_re = re.compile(
        r'<div style="background:#f8fafc;\s*border:1\.5px solid #cbd5e1;\s*border-left:4px solid #0284c7;\s*border-radius:8px;\s*padding:14px 18px;\s*margin-bottom:12px;">\s*'
        r'<div style="font-weight:800;\s*color:#0f172a;\s*font-size:1\.05rem;\s*margin-bottom:4px;">(.*?)</div>\s*'
        r'<div style="color:#334155;\s*font-size:1rem;\s*line-height:1\.65;">(.*?)</div>\s*</div>',
        re.S,
    )

    for fp in html_files:
        p = Path(fp)
        rel = p.relative_to(ROOT).as_posix()
        orig = p.read_text(encoding="utf-8", errors="ignore")
        if "mfs-revision.css" not in orig:
            continue

        stats["scanned"] += 1
        tier = classify_tier(rel)
        text = orig

        # 1. Bump mfs-revision.css query string
        text = css_ver_re.sub(r"\g<1>20261120v10", text)

        if tier is None:
            if text != orig:
                p.write_text(text, encoding="utf-8")
                stats["changed"] += 1
            continue

        # 2. Set/update data-level on <html>
        def set_html_level(m: re.Match) -> str:
            tag = m.group(0)
            if "data-level=" in tag:
                return re.sub(r'data-level="[^"]*"', f'data-level="{tier}"', tag)
            return tag[:-1] + f' data-level="{tier}">'

        text = re.sub(r"<html\b[^>]*>", set_html_level, text, count=1)

        # 3. Fix Python tuple leaks across Maths L1
        def replace_tuple(m: re.Match) -> str:
            stats["tuple_fixes"] += 1
            _, avatar_path, name, body = m.groups()
            return (
                f'<div class="mfs-l1-tutor-tip">'
                f'<img src="{avatar_path}" alt="{name} &mdash; MFS Specialist Tutor">'
                f'<div><strong>{name}&rsquo;s Level 1 Exam Tip:</strong>{body}</div>'
                f'</div>'
            )

        text = tuple_re.sub(replace_tuple, text)

        # 4. Fix Level 2 badges wrongly using .mfs-pill-l1
        if tier == "level-2":
            text, n_l2 = re.subn(
                r'<span class="mfs-pill-l1">(\s*Level\s*2[^<]*)</span>',
                r'<span class="mfs-pill-l2">\1</span>',
                text,
                flags=re.I,
            )
            if n_l2:
                stats["pill_l2_fixes"] += n_l2

            # Remove Level 1 footer tags from true Level 2-only Maths pages
            if is_maths_l2_only(rel):
                new_text = re.sub(
                    r'\s*<span class="mfs-pill-l1">(?:FS\s+)?Level 1</span>',
                    "",
                    text,
                )
                if new_text != text:
                    stats["l2_only_pill_cleaned"] += 1
                    text = new_text

        # 5. Standardize hero pill classes & Level 2 copy
        def update_hero_pills(m: re.Match) -> str:
            block = m.group(1)
            new_block = block
            if tier == "level-1":
                new_block = re.sub(
                    r'<span class="badge-pill-gold"[^>]*>',
                    '<span class="badge-pill-l1">',
                    new_block,
                )
            elif tier == "level-2":
                new_block = re.sub(
                    r'<span class="badge-pill-gold"[^>]*>(.*?)</span>',
                    lambda sm: '<span class="badge-pill-l2">'
                    + re.sub(r"LEVEL 1\s*&(?:amp;)?\s*LEVEL 2", "LEVEL 2 REVISION", sm.group(1))
                    + "</span>",
                    new_block,
                    flags=re.S,
                )
            elif tier == "entry-3":
                new_block = re.sub(
                    r'<span class="badge-pill-gold"[^>]*>',
                    '<span class="badge-pill-e3">',
                    new_block,
                )
            if new_block != block:
                stats["hero_pills_updated"] += 1
            return new_block

        text = hero_row_re.sub(update_hero_pills, text, count=1)

        # 6. Level 1 switch bar active badge Emerald Green
        if tier == "level-1":
            new_text = text.replace(
                "background:#eab308; color:#0f172a; font-weight:800;",
                "background:#16a34a; color:#ffffff; font-weight:800;",
            )
            if new_text != text:
                stats["l1_switch_updated"] += 1
                text = new_text

        # 7. Fix specific bugs in functional-skills-area-level-1.html & functional-skills-area.html
        if rel == "functional-skills-area-level-1.html":
            t2 = text.replace('href="#core-examples"', 'href="#skill-1"')
            t2 = t2.replace('>7 Sections<', '>9 Sections<')
            t2 = re.sub(
                r'\s*\.mfs-pill-l1\s*\{[^}]*\}\s*\.mfs-pill-board\s*\{[^}]*\}',
                "\n",
                t2,
                flags=re.S,
            )
            if t2 != text:
                stats["area_fixes"] += 1
                text = t2
        elif rel == "functional-skills-area.html":
            t2 = re.sub(
                r'\s*\.mfs-pill-l1\s*\{[^}]*\}\s*\.mfs-pill-l2\s*\{[^}]*\}\s*\.mfs-pill-board\s*\{[^}]*\}',
                "\n",
                text,
                flags=re.S,
            )
            if t2 != text:
                stats["area_fixes"] += 1
                text = t2

        # 8. Upgrade Maths Level 1 worked-model steps & plain Core Skill cards
        if rel.startswith("functional-skills-") and rel.endswith("-level-1.html"):
            def up_step(m: re.Match) -> str:
                stats["l1_steps_upgraded"] += 1
                return (
                    '<div class="model-step-col-desc">'
                    '<div class="mfs-step-calc-board">'
                    f'<div class="mfs-step-calc-line">{m.group(1)}</div>'
                    f'<span class="mfs-step-result-chip">{m.group(2)}</span>'
                    '</div></div>'
                )

            text = step_l1_re.sub(up_step, text)

            def up_skill(m: re.Match) -> str:
                stats["l1_skill_cards_upgraded"] += 1
                return (
                    '<div class="mfs-pastel-card mfs-pastel-mint" style="margin-bottom:12px;">'
                    f'<div class="mfs-pastel-label">{m.group(1)}</div>'
                    f'<div class="mfs-pastel-math" style="font-size:1.18rem; margin-bottom:0;">{m.group(2)}</div>'
                    '</div>'
                )

            text = skill_l1_re.sub(up_skill, text)

        if text != orig:
            p.write_text(text, encoding="utf-8")
            stats["changed"] += 1

    print("SPRINT6_DESIGN_TIERS_OK:", stats)


if __name__ == "__main__":
    main()
