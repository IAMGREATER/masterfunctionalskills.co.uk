#!/usr/bin/env python3
"""
Master Functional Skills - Master Curriculum Worksheet & Answer Suite Generator.
Compiles 100% original, Pearson Edexcel aligned worksheets & mark schemes for all curriculum areas.
"""

import os, sys, glob, re
from worksheet_templates import render_worksheet, render_answers
from generate_all_worksheets_complete import get_svg_for_topic
from topics_maths_number import TOPICS_MATHS_NUMBER
from data_maths_core import MATHS_CORE_TOPICS
from topics_data_maths import MATHS_TOPIC_DEFS

BASE_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk"
WORKSHEETS_DIR = os.path.join(BASE_DIR, "worksheets")
os.makedirs(WORKSHEETS_DIR, exist_ok=True)

# Combine loaded topics so far
COMBINED_TOPICS = {}

for t in TOPICS_MATHS_NUMBER:
    COMBINED_TOPICS[t['slug']] = t

for t in MATHS_CORE_TOPICS:
    COMBINED_TOPICS[t['slug']] = t

for t in MATHS_TOPIC_DEFS:
    COMBINED_TOPICS[t['slug']] = t

print(f"Loaded {len(COMBINED_TOPICS)} high-yield core topics so far: {list(COMBINED_TOPICS.keys())}")
