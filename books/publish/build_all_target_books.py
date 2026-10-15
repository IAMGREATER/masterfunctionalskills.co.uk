#!/usr/bin/env python3
"""
build_all_target_books.py
Master runner script that compiles and verifies all 6 publication books:
1. MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf (48 pages)
2. MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf (48 pages)
3. MasterFunctionalSkills_Digital_Skills_Handbook.pdf (48 pages)
4. MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf (48 pages)
5. MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf (48 pages)
6. MasterFunctionalSkills_Mock_Pack_English_L2.pdf (48 pages)

Saves to both:
- /home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/downloads/
- /home/subi/Documents/
"""

import os
import sys
import subprocess
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from build_maths_e3 import build_maths_e3_book
from build_english_e3 import build_english_e3_book
from build_digital_skills import build_digital_skills_book
from build_bksb_remediation import build_bksb_remediation_book
from build_mock_maths_l2 import build_mock_maths_l2_book
from build_mock_english_l2 import build_mock_english_l2_book

BOOKS = [
    ("Maths Entry Level 3 Core Guide", "MasterFunctionalSkills_Maths_Entry_Level_3_Core_Guide.pdf", build_maths_e3_book),
    ("English Entry Level 3 Core Guide", "MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf", build_english_e3_book),
    ("Essential Digital Skills Handbook", "MasterFunctionalSkills_Digital_Skills_Handbook.pdf", build_digital_skills_book),
    ("BKSB Remediation Workbook", "MasterFunctionalSkills_BKSB_Remediation_Workbook.pdf", build_bksb_remediation_book),
    ("Maths Level 2 Mock Exam Pack", "MasterFunctionalSkills_Mock_Pack_Maths_L2.pdf", build_mock_maths_l2_book),
    ("English Level 2 Mock Exam Pack", "MasterFunctionalSkills_Mock_Pack_English_L2.pdf", build_mock_english_l2_book),
]

def main():
    print("=" * 80)
    print("MASTER FUNCTIONAL SKILLS: COMPILING ALL PUBLICATIONS")
    print("=" * 80)
    t0 = time.time()
    
    results = []
    for title, filename, builder_func in BOOKS:
        print(f"\n>>> Compiling: {title} ({filename})...")
        pages = builder_func()
        results.append((title, filename, pages))
        
    duration = time.time() - t0
    print("\n" + "=" * 80)
    print("ALL 6 PUBLICATIONS COMPILED SUCCESSFULLY!")
    print(f"Total time elapsed: {duration:.2f} seconds")
    print("=" * 80)
    print(f"{'Publication Title':<38} | {'Filename':<55} | {'Pages':<6}")
    print("-" * 105)
    for title, filename, pages in results:
        print(f"{title:<38} | {filename:<55} | {pages:<6}")
    print("=" * 80)

if __name__ == "__main__":
    main()
