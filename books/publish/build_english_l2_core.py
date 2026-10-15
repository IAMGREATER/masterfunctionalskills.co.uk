#!/usr/bin/env python3
"""
build_english_l2_core.py
Builds the expanded 84-page Master Edition of:
MasterFunctionalSkills_English_Writing_Level_2_Core_Guide.pdf

Mapped strictly to Pearson Edexcel & Ofqual Functional Skills English Level 2 Writing standards.
Full CGP-grade visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7),
Open Sans / Lexend typography, wireframe layouts, 11 benchmark model answers,
guided planning scaffolds, SPaG masterclass, and complete mock exam papers.
"""

import os
import sys
import re
import subprocess
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import render_book_to_pdf

PROTOTYPE_PATH = "/home/subi/Nextcloud/NVMe469GB/Work/Pearson Writing Guide/Level 2/Version 7/pearson_edexcel_level2_writing_booklet_84pg_prototype.html"

def build_english_l2_core():
    with open(PROTOTYPE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Apply Dyslexia-friendly Warm Cream background (#FDFBF7) and typography
    # Ensure font family includes Lexend alongside Open Sans
    html = html.replace(
        "font-family: 'Open Sans', Arial, sans-serif;",
        "font-family: 'Open Sans', 'Lexend', Arial, sans-serif;"
    )
    
    # Update page background to warm cream #FDFBF7
    html = re.sub(
        r'(\.page\s*\{[^}]*background:\s*)#ffffff;',
        r'\1#FDFBF7;',
        html
    )
    html = re.sub(
        r'(body\s*\{[^}]*background:\s*)#ffffff;',
        r'\1#FDFBF7;',
        html
    )

    pdf_filename = "MasterFunctionalSkills_English_Writing_Level_2_Core_Guide.pdf"
    pages = render_book_to_pdf(html, pdf_filename)
    return pages

if __name__ == "__main__":
    build_english_l2_core()
