#!/usr/bin/env python3
"""
Master Functional Skills - Core Suite Generator.
Generates worksheets and answer schemes across all curriculum areas.
"""

import os, sys, glob, re
from worksheet_templates import render_worksheet, render_answers
from generate_all_worksheets_complete import get_svg_for_topic
from build_topic_dataset import make_maths_topic, make_english_topic, make_digital_topic

OUTPUT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/worksheets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

