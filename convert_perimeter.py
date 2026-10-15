import os, sys, re, lxml.html
from lxml import etree

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
FILE = "functional-skills-perimeter.html"
filepath = os.path.join(PROJECT_DIR, FILE)

with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
    raw = f.read()

tree = lxml.html.fromstring(raw)

# 1. Clean mathml duplicates across the whole tree
for m in tree.xpath('.//*[contains(@class, "katex-mathml")]'):
    m.drop_tree()

# 2. Extract components
home_content = tree.find('.//*[@id="home-content"]')
if home_content is None:
    home_content = tree.find('.//main')

# Fix all images
for img in home_content.xpath('.//img'):
    src = img.get('src', '')
    if '%20' in src:
        src = src.split('%20')[0].strip()
    src = src.split(' ')[0].strip()
    img.set('src', src)
    for a in ['width', 'height', 'data-lazy-src', 'data-lazy-srcset', 'data-lazy-sizes', 'loading']:
        if img.get(a):
            del img.attrib[a]
    img.set('class', 'img-fluid')

# Extract sections
sections = [s for s in home_content if isinstance(s, lxml.html.HtmlElement)]

# Intro
intro_sec = sections[0]
intro_p = [p.text_content().strip() for p in intro_sec.xpath('.//p') if p.text_content().strip()]
intro_text = " ".join(intro_p)

# Skill 1 (section 4)
sec_s1 = sections[4]
s1_h2 = sec_s1.xpath('.//h2')[0].text_content().strip()
s1_p = [etree.tostring(p, encoding='unicode') for p in sec_s1.xpath('.//p') if p.text_content().strip()]
s1_imgs = [etree.tostring(img, encoding='unicode') for img in sec_s1.xpath('.//img')]

# Skill 2 (section 7)
sec_s2 = sections[7]
s2_h2 = sec_s2.xpath('.//h2')[0].text_content().strip()
s2_p = [etree.tostring(p, encoding='unicode') for p in sec_s2.xpath('.//p') if p.text_content().strip()]
s2_imgs = [etree.tostring(img, encoding='unicode') for img in sec_s2.xpath('.//img')]

# Harder Example (section 10)
sec_harder = sections[10]
harder_h2 = sec_harder.xpath('.//h2')[0].text_content().strip()
harder_p = [etree.tostring(p, encoding='unicode') for p in sec_harder.xpath('.//p') if p.text_content().strip()]
harder_imgs = [etree.tostring(img, encoding='unicode') for img in sec_harder.xpath('.//img')]

# Practice Questions (section 11)
sec_q = sections[11]
questions = []
# Each question is a section or div in sec_q
q_blocks = sec_q.xpath('./section | ./div[contains(@class, "example-question")]')
if not q_blocks:
    # Look for question headers
    q_blocks = sec_q.xpath('./*')

q_items = []
for block in q_blocks:
    txt = block.text_content().strip()
    if 'question' in txt.lower():
        # extract stem, marks, image, and solution collapse
        stem_p = []
        for p in block.xpath('.//p'):
            t = p.text_content().strip()
            if t and not 'btn' in p.get('class', ''):
                stem_p.append(etree.tostring(p, encoding='unicode'))
        q_imgs = [etree.tostring(img, encoding='unicode') for img in block.xpath('.//img')]
        
        # Solution
        sol_el = block.xpath('.//div[contains(@class, "collapse")]')
        sol_html = ""
        if sol_el:
            sol_html = etree.tostring(sol_el[0], encoding='unicode')
            # clean collapse class
            sol_html = re.sub(r'class="[^"]*collapse[^"]*"', '', sol_html)
            sol_html = re.sub(r'id="[^"]*"', '', sol_html)
            
        q_items.append({
            'stem': "".join(stem_p),
            'images': "".join(q_imgs),
            'solution': sol_html
        })

print(f"Perimeter extraction complete: {len(q_items)} questions found")
