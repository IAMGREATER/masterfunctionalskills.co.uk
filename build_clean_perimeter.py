import os, sys, re, lxml.html
from lxml import etree

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
INPUT_FILE = os.path.join(PROJECT_DIR, "functional-skills-perimeter.html")

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    raw_html = f.read()

tree = lxml.html.fromstring(raw_html)

# Extract home-content
home_content = tree.get_element_by_id("home-content")

# Clean mathml duplicates across home_content
for m in home_content.xpath('.//*[contains(@class, "katex-mathml")]'):
    m.drop_tree()

# Clean script/style
for bad in home_content.xpath('.//script | .//style | .//noscript'):
    bad.drop_tree()

# Fix images
for img in home_content.xpath('.//img'):
    src = img.get('src', '')
    if '%20' in src:
        src = src.split('%20')[0].strip()
    src = src.split(' ')[0].strip()
    img.set('src', src)
    for attr in ['width', 'height', 'data-lazy-src', 'data-lazy-srcset', 'data-lazy-sizes', 'loading']:
        if img.get(attr):
            del img.attrib[attr]
    img.set('class', 'img-fluid')

# Extract sections
sections = [s for s in home_content if isinstance(s, lxml.html.HtmlElement)]

# Intro section is section 0
intro_el = sections[0]
intro_p = [p.text_content().strip() for p in intro_el.xpath('.//p') if p.text_content().strip()]
intro_text = " ".join(intro_p)

# Skill 1 is section 4
skill1_el = sections[4]
# Skill 2 is section 7
skill2_el = sections[7]
# Harder example is section 10
harder_el = sections[10]
# Questions is section 11
questions_el = sections[11]
# Spec is section 13
spec_el = sections[13]
# Worksheet is section 14
worksheet_el = sections[14]

print(f"Extracted: Intro, Skill 1, Skill 2, Harder Example, Questions, Spec, Worksheet")
