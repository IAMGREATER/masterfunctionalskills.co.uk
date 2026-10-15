import glob, re

# Get reference navbar
with open('past-papers.html') as f:
    ref = f.read()

start_top = ref.find('<!-- TOP TRUST BAR -->')
end_nav = ref.find('</header>') + len('</header>')
nav_block = ref[start_top:end_nav]

# 34 legacy files
legacy_files = [
  'aqa-functional-skills-english-level-1-past-papers.html',
  'aqa-functional-skills-english-level-2-past-papers.html',
  'aqa-functional-skills-maths-level-1-past-papers.html',
  'aqa-functional-skills-maths-level-2-past-papers.html',
  'city-and-guilds-functional-skills-english-level-1-past-papers.html',
  'city-and-guilds-functional-skills-english-level-2-past-papers.html',
  'city-and-guilds-functional-skills-maths-level-1-past-papers.html',
  'city-and-guilds-functional-skills-maths-level-2-past-papers.html',
  'edexcel-functional-skills-english-level-1-past-papers.html',
  'edexcel-functional-skills-english-level-2-past-papers.html',
  'edexcel-functional-skills-maths-level-1-past-papers.html',
  'edexcel-functional-skills-maths-level-2-past-papers.html',
  'ncfe-functional-skills-english-level-1-past-papers.html',
  'ncfe-functional-skills-english-level-2-past-papers.html',
  'ncfe-functional-skills-maths-level-1-past-papers.html',
  'ncfe-functional-skills-maths-level-2-past-papers.html',
  'nocn-functional-skills-english-level-1-past-papers.html',
  'nocn-functional-skills-english-level-2-past-papers.html',
  'nocn-functional-skills-maths-level-1-past-papers.html',
  'nocn-functional-skills-maths-level-2-past-papers.html',
  'open-awards-functional-skills-english-level-1-past-papers.html',
  'open-awards-functional-skills-english-level-2-past-papers.html',
  'open-awards-functional-skills-maths-level-1-past-papers.html',
  'open-awards-functional-skills-maths-level-2-past-papers.html',
  'tquk-functional-skills-english-level-1-past-papers.html',
  'tquk-functional-skills-english-level-2-past-papers.html',
  'tquk-functional-skills-maths-level-1-past-papers.html',
  'tquk-functional-skills-maths-level-2-past-papers.html',
  'video-solution.html',
  'functional-skills-area.html',
  'functional-skills-ordering-numbers.html'
]

updated_count = 0
for fn in legacy_files:
    try:
        with open(fn, 'r') as f:
            c = f.read()
        
        if 'mfs-navbar' in c:
            continue
        
        # Find where to insert: right after <body>
        body_idx = c.find('<body>')
        if body_idx == -1:
            continue
        body_end = body_idx + len('<body>')
        
        # Remove old promo banner if present
        promo_match = re.search(r'<!-- CLEAN TRUST BANNER.*?</div>\s*</div>\s*</div>', c, re.DOTALL)
        if promo_match:
            c = c[:promo_match.start()] + c[promo_match.end():]
            # re-calculate body_end
            body_end = c.find('<body>') + len('<body>')
        
        new_c = c[:body_end] + '\n\n' + nav_block + '\n\n' + c[body_end:]
        with open(fn, 'w') as f:
            f.write(new_c)
        updated_count += 1
    except Exception as e:
        print(f"Error updating {fn}: {e}")

print(f"Unified navbars inserted into {updated_count} legacy files.")
