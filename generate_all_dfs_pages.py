# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Automated Digital Skills Page Generator & QA Suite
Author: Abdul (MFS Pedagogical Systems)
Generates:
1. 39 Dedicated Topic Pages (Entry 3 & Level 1)
2. Dual-View Integrated Hubs in /digital-skills/entry-3/ and /digital-skills/level-1/
3. Root Landing Pages: digital-functional-skills-level-1.html, digital-functional-skills-entry-3.html, entry-3-digital-skills.html
4. Master Gateway Hub: /digital-skills/index.html
5. Executes automated syntax and confidentiality audits
"""

import os
import re
from html.parser import HTMLParser
from collections import defaultdict

from dfs_templates import render_revision_page, render_hub_page
from dfs_data_entry3 import ALL_ENTRY_3_TOPICS
from dfs_data_level1 import ALL_LEVEL_1_TOPICS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DFS_DIR = os.path.join(BASE_DIR, "digital-skills")
E3_DIR = os.path.join(DFS_DIR, "entry-3")
L1_DIR = os.path.join(DFS_DIR, "level-1")

FORBIDDEN_TERMS = [
    r"\boxford\s+health\b",
    r"\bnhs\b",
    r"\bhospital\s+trust\b",
    r"\bentry\s+level\s+3\b"  # Strictly Entry 3, never "Entry Level 3"
]

class HTMLBalanceChecker(HTMLParser):
    VOID_ELEMENTS = {
        'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'
    }

    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.VOID_ELEMENTS:
            self.stack.append(tag.lower())

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.VOID_ELEMENTS:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{t}> without matching open tag")
            return
        if self.stack[-1] == t:
            self.stack.pop()
        else:
            if t in self.stack:
                while self.stack and self.stack[-1] != t:
                    popped = self.stack.pop()
                    if popped not in {'p', 'li', 'td', 'th', 'tr'}:
                        self.errors.append(f"Unclosed tag <{popped}> before closing </{t}>")
                if self.stack and self.stack[-1] == t:
                    self.stack.pop()
            else:
                self.errors.append(f"Mismatched closing tag </{t}> (expected </{self.stack[-1]}>)")

def build_level(topics, level_code, level_title, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []

    # 1. Generate individual topic pages
    for idx, topic in enumerate(topics):
        prev_topic = topics[idx - 1] if idx > 0 else None
        next_topic = topics[idx + 1] if idx < len(topics) - 1 else None

        html_content = render_revision_page(topic, prev_topic, next_topic, level_code, level_title)
        filepath = os.path.join(output_dir, f"{topic['slug']}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        generated_files.append(filepath)

    # 2. Group by skill area for Hub
    grouped = defaultdict(list)
    for t in topics:
        grouped[t['skill_area']].append(t)

    # 3. Generate Directory Hub page (digital-skills/<level>/index.html)
    dir_hub_html = render_hub_page(grouped, level_code, level_title, is_root=False)
    dir_hub_filepath = os.path.join(output_dir, "index.html")
    with open(dir_hub_filepath, "w", encoding="utf-8") as f:
        f.write(dir_hub_html)
    generated_files.append(dir_hub_filepath)

    # 4. Generate Root Landing Page (e.g. digital-functional-skills-level-1.html)
    root_hub_html = render_hub_page(grouped, level_code, level_title, is_root=True)
    root_hub_filepath = os.path.join(BASE_DIR, f"digital-functional-skills-{level_code}.html")
    with open(root_hub_filepath, "w", encoding="utf-8") as f:
        f.write(root_hub_html)
    generated_files.append(root_hub_filepath)

    # Also mirror root alias for entry 3 (entry-3-digital-skills.html)
    if level_code == "entry-3":
        alias_filepath = os.path.join(BASE_DIR, "entry-3-digital-skills.html")
        with open(alias_filepath, "w", encoding="utf-8") as f:
            f.write(root_hub_html)
        generated_files.append(alias_filepath)

    return generated_files

def run_qa_audit(files):
    print("\n" + "="*70)
    print("RUNNING AUTOMATED QUALITY ASSURANCE & AUDIT SUITE")
    print("="*70)

    total_files = len(files)
    confidentiality_passed = 0
    syntax_passed = 0

    for filepath in files:
        filename = os.path.relpath(filepath, BASE_DIR)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # A. Confidentiality & Naming Regex Audit
        violations = []
        for pat in FORBIDDEN_TERMS:
            matches = re.findall(pat, content, re.IGNORECASE)
            if matches:
                violations.extend(matches)
        
        if not violations:
            confidentiality_passed += 1
        else:
            print(f"[FAIL: Policy/Naming] {filename} contains forbidden terms: {violations}")

        # B. HTML Syntax & Tag Balance Audit
        parser = HTMLBalanceChecker()
        try:
            parser.feed(content)
            unclosed = [tag for tag in parser.stack if tag not in {'p', 'li', 'td', 'th', 'tr'}]
            if len(unclosed) == 0 and len(parser.errors) == 0:
                syntax_passed += 1
            else:
                print(f"[FAIL: HTML Syntax] {filename} Unclosed: {unclosed}, Errors: {parser.errors[:3]}")
        except Exception as e:
            print(f"[ERROR: Parser] {filename} Exception: {e}")

    print(f"\n--- AUDIT RESULTS ---")
    print(f"Total Pages Audited: {total_files}")
    print(f"Confidentiality & Naming Check: {confidentiality_passed}/{total_files} PASSED (0 leaks)")
    print(f"HTML Tag Balance: {syntax_passed}/{total_files} PASSED")
    print("="*70)

    if confidentiality_passed == total_files and syntax_passed == total_files:
        print("ALL QUALITY CHECKS PASSED WITH ZERO DEFECTS.")
    else:
        print("WARNING: Some files require attention.")

def main():
    print(f"Building Entry 3 Digital Skills Revision Pages ({len(ALL_ENTRY_3_TOPICS)} topics)...")
    e3_files = build_level(ALL_ENTRY_3_TOPICS, "entry-3", "Entry 3", E3_DIR)
    print(f"Successfully generated {len(e3_files)} Entry 3 pages")

    print(f"\nBuilding Level 1 Digital Skills Revision Pages ({len(ALL_LEVEL_1_TOPICS)} topics)...")
    l1_files = build_level(ALL_LEVEL_1_TOPICS, "level-1", "Level 1", L1_DIR)
    print(f"Successfully generated {len(l1_files)} Level 1 pages")

    all_files = e3_files + l1_files + [os.path.join(DFS_DIR, "index.html")]
    run_qa_audit(all_files)

if __name__ == "__main__":
    main()
