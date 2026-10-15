import glob, re, os

PROJECT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
files = sorted(glob.glob(os.path.join(PROJECT_DIR, "*.html")))

class_mapping = {
    'pfs-card-title': 'mfs-topic-title',
    'pfs-card-head': 'mfs-topic-head',
    'pfs-card-stem': 'mfs-topic-stem',
    'pfs-card-body': 'mfs-topic-body',
    'pfs-card-footer': 'mfs-topic-footer',
    'pfs-card': 'mfs-topic-card',
    'pfs-prefix': 'mfs-topic-prefix',
    'pfs-math-col': 'mfs-math-col',
    'pfs-marks-row': 'mfs-marks-row',
    'pfs-formula-display': 'mfs-formula-display',
    'pfs-formula-label': 'mfs-formula-label',
    'pfs-formula-value': 'mfs-formula-value',
    'pfs-answer-banner': 'mfs-answer-banner',
    'pfs-diagram-col': 'mfs-diagram-col',
    'pfs-steps-box': 'mfs-steps-box',
    'pfs-step-row': 'mfs-step-row',
    'pfs-step-tag': 'mfs-step-tag',
    'pfs-step-content': 'mfs-step-content',
    'pfs-pill-l1': 'mfs-pill-l1',
    'pfs-pill-l2': 'mfs-pill-l2',
    'pfs-pill-board': 'mfs-pill-board',
    'pfs-math-text': 'mfs-math-text',
    'pfs-loading': 'mfs-loading',
    'pfs-circle-preloader': 'mfs-circle-preloader',
    'pfs-nav-dropdown-styles': 'mfs-nav-dropdown-styles',
    'pfs-logo-hoz': 'mfs-logo-hoz',
    'pfs-icon-27': 'mfs-icon-27'
}

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    orig = c

    # 1. Strip <source> tags pointing to passfunctionalskills
    c = re.sub(r'<source[^>]*passfunctionalskills[^>]*>', '', c, flags=re.I)

    # 2. Strip srcset/data-lazy-srcset pointing to passfunctionalskills
    c = re.sub(r'(data-lazy-)?srcset=[\"\'][^\"\']*passfunctionalskills[^\"\']*[\"\']', '', c, flags=re.I)

    # 3. Clean any image tags that might only have competitor src
    c = re.sub(r'https?://(?:www\.)?passfunctionalskills\.co\.uk/app/uploads/([^\"\'\s>]+)', r'assets/img/pfs/\1', c, flags=re.I)
    c = re.sub(r'https?://(?:www\.)?passfunctionalskills\.co\.uk/wp-content/uploads/([^\"\'\s>]+)', r'assets/img/pfs/\1', c, flags=re.I)

    # 4. Replace text mentions of Pass Functional Skills with Master Functional Skills
    c = re.sub(r'Pass\s+Functional\s+Skills', 'Master Functional Skills', c, flags=re.I)

    # 5. Replace card and component classes
    for k, v in class_mapping.items():
        c = re.sub(r'\b' + k + r'\b', v, c, flags=re.I)

    # 6. Generic replacement for remaining pfs- or PFS-
    c = re.sub(r'\bPFS-([a-zA-Z0-9_-]+)', r'MFS-\1', c)
    c = re.sub(r'\bpfs-([a-zA-Z0-9_-]+)', r'mfs-\1', c)

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        count += 1

print(f"Sanitized {count} HTML files successfully.")
