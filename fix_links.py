import glob, re, os

# 1. Create root aliases / symlinks
aliases = [
    ('book-functional-skills-exam.html', 'exams.html'),
    ('topics/functional-skills-courses.html', '../functional-skills-courses.html'),
    ('topics/book-functional-skills-exam.html', '../exams.html'),
    ('topics/digital-functional-skills.html', '../digital-functional-skills.html'),
    ('topics/past-papers.html', '../past-papers.html'),
    ('topics/study.html', '../study.html'),
    ('topics/tutors.html', '../tutors.html'),
]

for link_name, target in aliases:
    if os.path.islink(link_name) or os.path.exists(link_name):
        try: os.remove(link_name)
        except: pass
    os.symlink(target, link_name)
    print(f"Created symlink: {link_name} -> {target}")

# 2. Fix stray ../ in root HTML files
root_htmls = glob.glob('*.html')
fixed_root_links = 0
for fn in root_htmls:
    with open(fn, 'r', errors='ignore') as f:
        content = f.read()
    
    # Replace href="../filename.html" with href="filename.html" if filename.html exists in root
    def replace_dotdot(match):
        global fixed_root_links
        target_fn = match.group(1)
        if os.path.exists(target_fn):
            fixed_root_links += 1
            return f'href="{target_fn}"'
        return match.group(0)

    new_content = re.sub(r'href=[\"\']\.\./([a-zA-Z0-9_-]+\.html)[\"\']', replace_dotdot, content)
    if new_content != content:
        with open(fn, 'w') as f:
            f.write(new_content)

print(f"Fixed {fixed_root_links} stray ../ links in root HTML files.")

# 3. Replace 'Pass Functional Skills' with 'Master Functional Skills' in visible user text
brand_fixed_files = 0
for fn in glob.glob('*.html') + glob.glob('topics/*.html') + glob.glob('worksheets/*.html'):
    with open(fn, 'r', errors='ignore') as f:
        c = f.read()
    
    # We want to replace "Pass Functional Skills" in text nodes, but keep URLs pointing to passfunctionalskills.co.uk if they are external assets
    # Regex lookaround to avoid replacing inside http://passfunctionalskills...
    new_c = re.sub(r'(?<!https://)(?<!http://)(?<!/)Pass Functional Skills', 'Master Functional Skills', c)
    new_c = re.sub(r'(?<!https://)(?<!http://)(?<!/)pass functional skills', 'master functional skills', new_c)
    new_c = re.sub(r'Pass FS', 'Master FS', new_c)
    
    if new_c != c:
        with open(fn, 'w') as f:
            f.write(new_c)
        brand_fixed_files += 1

print(f"Updated branding in {brand_fixed_files} files.")
