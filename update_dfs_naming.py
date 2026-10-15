#!/usr/bin/env python3
"""
Updates Digital Functional Skills nomenclature across all HTML pages and worksheets:
- "Entry Level 3" -> "DFSQ Entry 3"
- "Digital Skills Level 1" -> "DFS Level 1"
- Clarifies that DFS operates strictly at Entry 3 and Level 1 (no Level 2).
"""

import glob
import re
import os

html_files = sorted(glob.glob("*.html"))
ws_files = sorted(glob.glob("worksheets/*digital*.html"))
all_files = html_files + ws_files

print(f"Total HTML files to process: {len(all_files)}")

# 1. Update navigation dropdowns and footers across all site HTML files
nav_replacements = [
    # Dropdown in Exams
    (r"Digital Functional Skills \(Entry 3 & Level 1\)", "Digital Functional Skills (DFSQ Entry 3 & DFS Level 1)"),
    (r"Digital Functional Skills \(Entry Level 3 & Level 1\)", "Digital Functional Skills (DFSQ Entry 3 & DFS Level 1)"),
    
    # Dropdown in Courses
    (r"Digital Skills Level 1 Course", "DFS Level 1 Course"),
    
    # Dropdown in Revision
    (r"Digital Skills Hub \(Entry 3 & Level 1\) →", "Digital Skills Hub (DFSQ Entry 3 & DFS Level 1) →"),
    (r"Digital Skills Hub \(Entry Level 3 & Level 1\) →", "Digital Skills Hub (DFSQ Entry 3 & DFS Level 1) →"),
    (r'<a href="digital-functional-skills\.html" class="mfs-dropdown-item">Digital Skills Entry Level 3</a>',
     '<a href="digital-functional-skills.html" class="mfs-dropdown-item">DFSQ Entry 3</a>'),
    (r'<a href="digital-functional-skills-level-1\.html" class="mfs-dropdown-item">Digital Skills Level 1</a>',
     '<a href="digital-functional-skills-level-1.html" class="mfs-dropdown-item">DFS Level 1</a>'),
    
    # Footer links
    (r"Digital Skills Hub \(L1 & E3\)", "DFS Hub (DFS Level 1 & DFSQ Entry 3)"),
    (r"Digital Skills Level 1 Course", "DFS Level 1 Course"),
]

updated_count = 0

for fpath in all_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    
    # Apply nav replacements
    for pattern, repl in nav_replacements:
        content = re.sub(pattern, repl, content)
        
    # Specific updates for digital-functional-skills.html
    if os.path.basename(fpath) == "digital-functional-skills.html":
        content = content.replace("Digital Functional Skills Qualifications (Entry Level 3 & Level 1)",
                                  "Digital Functional Skills Qualifications (DFSQ Entry 3 & DFS Level 1)")
        content = content.replace("for Entry Level 3 & Level 1.", "for DFSQ Entry 3 & DFS Level 1.")
        content = content.replace("Available at Entry Level 3 & Level 1", "Available at DFSQ Entry 3 & DFS Level 1")
        content = content.replace("<h3 style=\"font-size:1.3rem; margin:0;\">Digital Skills Entry Level 3</h3>",
                                  "<h3 style=\"font-size:1.3rem; margin:0;\">DFSQ Entry 3</h3>")
        content = content.replace("Inquire About Entry 3 Digital", "Inquire About DFSQ Entry 3")
        content = content.replace("<h3 style=\"font-size:1.3rem; margin:0;\">Digital Skills Level 1</h3>",
                                  "<h3 style=\"font-size:1.3rem; margin:0;\">DFS Level 1</h3>")
        content = content.replace("DFSQ Entry Level 3 vs Level 1 Comparison", "DFSQ Entry 3 vs DFS Level 1 Comparison")
        content = content.replace("<th style=\"padding:16px 20px;\">Digital Functional Skills Entry Level 3</th>",
                                  "<th style=\"padding:16px 20px;\">DFSQ Entry 3 (Digital Functional Skills Entry 3)</th>")
        content = content.replace("<th style=\"padding:16px 20px;\">Digital Functional Skills Level 1</th>",
                                  "<th style=\"padding:16px 20px;\">DFS Level 1 (Digital Functional Skills Level 1)</th>")
        content = content.replace("Both Entry Level 3 and Level 1 are structured around",
                                  "Both DFSQ Entry 3 and DFS Level 1 are structured around")
        content = content.replace(">Entry Level 3</span>", ">DFSQ Entry 3</span>")
        content = content.replace("DFSQ Entry Level 3 Sample Assessment Material", "DFSQ Entry 3 Sample Assessment Material")

    # Specific updates for digital-functional-skills-level-1.html
    if os.path.basename(fpath) == "digital-functional-skills-level-1.html":
        content = content.replace("Digital Functional Skills Level 1 Online Course & Exam",
                                  "DFS Level 1 Online Course & Exam | Digital Functional Skills")
        content = content.replace("Complete Digital Functional Skills Level 1 online course",
                                  "Complete DFS Level 1 (Digital Functional Skills Level 1) online course")

    # Specific updates for revise.html
    if os.path.basename(fpath) == "revise.html":
        content = content.replace("Digital Skills Entry Level 3 (Essential Foundation)",
                                  "DFSQ Entry 3 (Essential Foundation)")
        content = content.replace("Digital Skills Level 1 (Workplace & Apprenticeships)",
                                  "DFS Level 1 (Workplace & Apprenticeships)")
        content = content.replace("Entry 3 Hub →", "DFSQ Entry 3 Hub →")
        content = content.replace("Level 1 Course →", "DFS Level 1 Course →")

    # Specific updates for worksheets
    if "digital-functional-skills-worksheet.html" in fpath:
        content = content.replace("Digital Functional Skills Core Worksheet (Level 1 & Level 2)",
                                  "DFSQ Entry 3 Worksheet (Digital Functional Skills Entry 3)")
        content = content.replace("Digital Functional Skills Core", "DFSQ Entry 3")
        content = content.replace("Level 1 & Level 2", "DFSQ Entry 3")
    elif "digital-functional-skills-answers.html" in fpath:
        content = content.replace("Digital Functional Skills Core Answer Key & Mark Scheme (Level 1 & Level 2)",
                                  "DFSQ Entry 3 Worked Mark Scheme (Digital Functional Skills Entry 3)")
        content = content.replace("Digital Functional Skills Core", "DFSQ Entry 3")
        content = content.replace("Level 1 & Level 2", "DFSQ Entry 3")
    elif "digital-functional-skills-level-1-worksheet.html" in fpath:
        content = content.replace("Digital Level 1 Worksheet (Level 1 & Level 2)",
                                  "DFS Level 1 Worksheet (Digital Functional Skills Level 1)")
        content = content.replace("Digital Level 1", "DFS Level 1")
        content = content.replace("Level 1 & Level 2", "DFS Level 1")
    elif "digital-functional-skills-level-1-answers.html" in fpath:
        content = content.replace("Digital Level 1 Answer Key & Mark Scheme (Level 1 & Level 2)",
                                  "DFS Level 1 Worked Mark Scheme (Digital Functional Skills Level 1)")
        content = content.replace("Digital Level 1", "DFS Level 1")
        content = content.replace("Level 1 & Level 2", "DFS Level 1")
    elif "digital-functional-skills-revision-worksheet.html" in fpath:
        content = content.replace("Digital Revision Worksheet (Level 1 & Level 2)",
                                  "DFS Revision Worksheet (DFSQ Entry 3 & DFS Level 1)")
        content = content.replace("Level 1 & Level 2", "DFSQ Entry 3 & DFS Level 1")
    elif "digital-functional-skills-revision-answers.html" in fpath:
        content = content.replace("Digital Revision Answer Key & Mark Scheme (Level 1 & Level 2)",
                                  "DFS Revision Worked Mark Scheme (DFSQ Entry 3 & DFS Level 1)")
        content = content.replace("Level 1 & Level 2", "DFSQ Entry 3 & DFS Level 1")

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"Successfully updated {updated_count} files with DFSQ Entry 3 & DFS Level 1 naming.")
