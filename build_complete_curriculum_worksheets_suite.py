#!/usr/bin/env python3
"""
Master Functional Skills - Complete Curriculum Worksheets & Mark Schemes Suite.
Generates 100% original, Pearson Edexcel aligned worksheets & mark schemes
across all curriculum areas:
- Mathematics (Number, Calculation, Measures, Shape, Space, Data, Probability)
- English Reading (Comprehension, Language Features, Tone, Layout, Comparison)
- English Writing (PAF, Formal Correspondence, Reports, Articles, SPaG)
- English SLC (Speaking, Listening & Communicating scenarios)
- Digital Functional Skills (Devices, Safety, Spreadsheets, Transactions)
"""

import os, sys, glob, re
from worksheet_templates import render_worksheet, render_answers
from generate_all_worksheets_complete import get_svg_for_topic

WORK_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
WORKSHEETS_DIR = os.path.join(WORK_DIR, "worksheets")
os.makedirs(WORKSHEETS_DIR, exist_ok=True)

print("Starting Master Worksheets Suite generation...")
