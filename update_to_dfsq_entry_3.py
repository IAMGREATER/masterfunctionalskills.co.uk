#!/usr/bin/env python3
"""
Updates DFS Entry 3 -> DFSQ Entry 3 across all HTML pages, scripts, and worksheets.
"""

import glob
import os

html_files = sorted(glob.glob("*.html"))
ws_files = sorted(glob.glob("worksheets/*digital*.html"))
py_files = ["generate_modern_digital_skills.py", "update_dfs_naming.py"]

all_files = html_files + ws_files + py_files

updated_files = 0

for fpath in all_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content

    # Replace DFS Entry 3 with DFSQ Entry 3
    # Be careful not to produce DFSQQ if DFSQ Entry 3 already exists
    content = content.replace("DFSQ Entry 3", "___DFSQ_ENTRY_3___")
    content = content.replace("DFS Entry 3", "DFSQ Entry 3")
    content = content.replace("___DFSQ_ENTRY_3___", "DFSQ Entry 3")

    # Clean any double "DFS DFSQ" if any
    content = content.replace("DFS DFSQ", "DFSQ")

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files += 1

print(f"Successfully updated {updated_files} files with DFSQ Entry 3.")
