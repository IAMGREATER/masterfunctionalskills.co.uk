import os, glob, re, urllib.parse

site_dir = '/home/subi/Projects/masterfunctionalskills.co.uk'
all_html_files = []
for root, dirs, files in os.walk(site_dir):
    # skip .git or node_modules if any
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            all_html_files.append(os.path.join(root, f))

print(f"Total HTML files found: {len(all_html_files)}")

# 1. Check for broken internal links
broken_links = []
external_links = []
pfs_mentions = []
missing_assets = []

for file_path in all_html_files:
    rel_source = os.path.relpath(file_path, site_dir)
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
    
    # Check for "pass functional skills" brand leakage in user-facing content (exclude external URLs)
    # Exclude passfunctionalskills.co.uk URLs since some download links reference legacy CDN
    text_without_urls = re.sub(r'https?://[^\s<>"\']+', '', content)
    matches_pfs = re.findall(r'(?i)\bpass functional skills\b', text_without_urls)
    if matches_pfs:
        pfs_mentions.append((rel_source, len(matches_pfs)))

    # Find all href and src
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for l in links:
        l = l.strip()
        if not l or l.startswith('#') or l.startswith('javascript:') or l.startswith('mailto:') or l.startswith('tel:'):
            continue
        if l.startswith('http://') or l.startswith('https://'):
            external_links.append((rel_source, l))
            continue
        
        # Internal link or asset
        parsed = urllib.parse.urlparse(l)
        clean_path = parsed.path
        if not clean_path:
            continue
        
        # Resolve target
        source_dir = os.path.dirname(file_path)
        target_path = os.path.normpath(os.path.join(source_dir, clean_path))
        
        if not os.path.exists(target_path):
            broken_links.append((rel_source, l, target_path))

print(f"\n--- AUDIT RESULTS ---")
print(f"Broken internal links/assets count: {len(broken_links)}")
for src, l, tgt in broken_links[:25]:
    print(f"  [404] In {src} -> '{l}' (Target not found: {tgt})")

print(f"\nLegacy 'Pass Functional Skills' text mentions in {len(pfs_mentions)} files:")
for src, count in pfs_mentions[:20]:
    print(f"  - {src}: {count} occurrences")
