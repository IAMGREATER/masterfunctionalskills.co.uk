"""
book_framework.py
Shared framework, CSS styling tokens, and PDF compiler for Master Functional Skills
40-50+ page publication books.
"""

import os
import sys
import subprocess
import time

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
DOWNLOADS_DIR = os.path.join(PROJECT_DIR, "assets", "downloads")
DOCUMENTS_DIR = "/home/subi/Documents"
BOOKS_IMG_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
SCRATCH_DIR = os.path.join(PROJECT_DIR, "scratch", "book_publish")
CHROME_BIN = "/usr/lib/chromium/chromium"

os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

SHARED_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Lexend:wght@400;500;600;700;800;900&family=Montserrat:wght@700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');

  @page {
    size: A4 portrait;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  body {
    margin: 0;
    padding: 0;
    font-family: 'Lexend', 'Open Sans', 'Atkinson Hyperlegible', sans-serif;
    color: #1F2937;
    background: #ffffff;
    font-size: 8.5pt;
    line-height: 1.48;
    letter-spacing: 0.02em;
    text-align: left;
  }

  .page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    min-height: 297mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    overflow: hidden;
    padding: 12mm 15mm 13mm 15mm;
    background: #FDFBF7;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  /* Full Bleed Covers */
  .cover-full-page {
    padding: 0 !important;
    background: #0f172a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .cover-full-img {
    width: 210mm;
    height: 297mm;
    display: block;
    object-fit: cover;
  }

  /* Header & Footer */
  .page-header {
    border-bottom: 2px solid var(--theme, #991b1b);
    padding-bottom: 5px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
  }
  .page-header-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--theme, #991b1b);
  }
  .page-header-strand {
    font-size: 7.8pt;
    font-weight: 700;
    color: #64748b;
  }
  .page-footer {
    position: absolute;
    bottom: 8mm;
    left: 15mm;
    right: 15mm;
    border-top: 1px solid #e2e8f0;
    padding-top: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #64748b;
  }
  .page-num {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme, #991b1b);
    font-size: 7.8pt;
  }

  /* Typography */
  h1 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    color: var(--theme, #991b1b);
    font-size: 16pt;
    margin: 0 0 6px 0;
    line-height: 1.15;
  }
  h2 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--theme, #991b1b);
    font-size: 12pt;
    margin: 0 0 6px 0;
    line-height: 1.2;
  }
  h3 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #0f172a;
    font-size: 9.5pt;
    margin: 6px 0 3px 0;
  }
  p {
    margin: 0 0 6px 0;
    line-height: 1.45;
  }

  /* Pedagogical Cards (CGP / Murphy Schema) */
  .card-concept {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-left: 4.5px solid #0284c7;
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }
  .card-method {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4.5px solid #16a34a;
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }
  .card-trap {
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-left: 4.5px solid #dc2626;
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }
  .card-tip {
    background: #fefce8;
    border: 1px solid #fde68a;
    border-left: 4.5px solid #d97706;
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }
  .card-practice {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-left: 4.5px solid var(--theme, #991b1b);
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }
  .card-exam {
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-left: 4.5px solid #7c3aed;
    padding: 8px 11px;
    border-radius: 5px;
    margin-bottom: 7px;
    font-size: 8.3pt;
  }

  /* Mark Badges & Tags */
  .mark-badge {
    background: var(--theme, #991b1b);
    color: #ffffff;
    padding: 1.5px 6px;
    border-radius: 4px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 7pt;
    display: inline-block;
    vertical-align: middle;
  }
  .tag-pill {
    display: inline-block;
    padding: 1.5px 7px;
    border-radius: 4px;
    font-size: 7pt;
    font-weight: 700;
    text-transform: uppercase;
    margin-right: 4px;
  }
  .tag-blue { background: #dbeafe; color: #1e40af; }
  .tag-green { background: #d1fae5; color: #065f46; }
  .tag-amber { background: #fef3c7; color: #92400e; }
  .tag-purple { background: #f3e8ff; color: #6b21a8; }
  .tag-red { background: #fee2e2; color: #991b1b; }

  /* Workspaces */
  .workspace-ruled {
    background: repeating-linear-gradient(
      transparent,
      transparent 21px,
      #e2e8f0 21px,
      #e2e8f0 22px
    );
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 8px 12px;
    min-height: 88px;
    margin: 5px 0;
    font-size: 8pt;
    color: #94a3b8;
    font-style: italic;
  }
  .workspace-grid {
    background-image: 
      linear-gradient(to right, #f1f5f9 1px, transparent 1px),
      linear-gradient(to bottom, #f1f5f9 1px, transparent 1px);
    background-size: 6mm 6mm;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    min-height: 85px;
    margin: 5px 0;
    padding: 6px;
    font-size: 7.5pt;
    color: #94a3b8;
  }

  /* Tables */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8pt;
  }
  table.data-table th, table.data-table td {
    padding: 5px 8px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }
  table.data-table th {
    background: var(--theme, #991b1b);
    color: #ffffff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.5pt;
    text-transform: uppercase;
  }
  table.data-table tr:nth-child(even) {
    background: #f8fafc;
  }

  /* Grid Layouts */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 7px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 6px;
  }

  /* Arithmetic Steps */
  .step-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3px 0;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 8.2pt;
  }
  .step-num {
    font-weight: 800;
    color: var(--theme, #991b1b);
    font-size: 8pt;
    width: 18px;
  }

  /* UI Mockups for EDSQ */
  .ui-window {
    background: #ffffff;
    border: 1.5px solid #94a3b8;
    border-radius: 6px;
    overflow: hidden;
    margin: 6px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }
  .ui-titlebar {
    background: #e2e8f0;
    padding: 4px 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 7.2pt;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #334155;
    border-bottom: 1px solid #cbd5e1;
  }
  .ui-controls {
    display: flex;
    gap: 4px;
  }
  .ui-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  .ui-body {
    padding: 7px 10px;
    font-size: 8pt;
  }

  /* Animated Drawing / Cartoon Style Character Vignettes (Raymond Murphy style) */
  .tutor-vignette {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin: 6px 0;
    padding: 6px 10px;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
  }
  .tutor-avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--theme, #991b1b);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 13pt;
    flex-shrink: 0;
    border: 2px solid #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.12);
  }
  .speech-bubble {
    position: relative;
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 6px 10px;
    font-size: 8pt;
    line-height: 1.4;
    flex-grow: 1;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .speech-bubble::before {
    content: '';
    position: absolute;
    top: 12px;
    left: -7px;
    width: 0;
    height: 0;
    border-top: 6px solid transparent;
    border-bottom: 6px solid transparent;
    border-right: 7px solid #cbd5e1;
  }
  .speech-bubble::after {
    content: '';
    position: absolute;
    top: 13px;
    left: -5px;
    width: 0;
    height: 0;
    border-top: 5px solid transparent;
    border-bottom: 5px solid transparent;
    border-right: 6px solid #ffffff;
  }
  .speech-bubble-speaker {
    font-weight: 800;
    font-size: 7.2pt;
    text-transform: uppercase;
    color: var(--theme, #991b1b);
    margin-bottom: 2px;
  }

  /* Workplace Artifacts */
  .workplace-memo {
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-top: 4px solid var(--theme, #991b1b);
    padding: 8px 12px;
    border-radius: 4px;
    margin: 6px 0;
    font-size: 7.8pt;
    box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  }
</style>
"""

def render_book_to_pdf(html_str, filename):
    """
    Renders HTML string to PDF using Chromium headless and saves to:
    1. DOWNLOADS_DIR
    2. DOCUMENTS_DIR
    Verifies page count with pdfinfo.
    """
    out_downloads = os.path.join(DOWNLOADS_DIR, filename)
    out_documents = os.path.join(DOCUMENTS_DIR, filename)
    temp_html = os.path.join(SCRATCH_DIR, f"temp_{int(time.time()*1000)}.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_str)
    
    print(f"[*] Rendering {filename} via Chromium...")
    t0 = time.time()
    
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-background-networking",
        "--disable-sync",
        "--no-first-run",
        f"--user-data-dir=/tmp/chr_render_{int(time.time()*1000)}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_downloads}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    
    # Copy to Documents
    import shutil
    shutil.copy2(out_downloads, out_documents)
    
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    duration = time.time() - t0
    
    # Check page count
    res = subprocess.run(["pdfinfo", out_downloads], capture_output=True, text=True, check=True)
    page_count = 0
    for line in res.stdout.splitlines():
        if "Pages:" in line:
            page_count = int(line.split()[1])
            
    file_size_mb = os.path.getsize(out_downloads) / (1024 * 1024)
    print(f"[+] SUCCESS: {filename}")
    print(f"    Pages: {page_count}")
    print(f"    Size: {file_size_mb:.2f} MB")
    print(f"    Time: {duration:.1f}s")
    print(f"    Saved to: {out_downloads}")
    print(f"    Saved to: {out_documents}\n")
    return page_count
