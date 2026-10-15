#!/usr/bin/env python3
"""
generate_audit_page.py
Generates the comprehensive visual image audit document:
/home/subi/Projects/masterfunctionalskills.co.uk/image_audit_catalog.html
Outlines all images used across Maths and English, shows thumbnails, topic connections,
identifies why diagrams/screenshots were flagged, and presents proposed solutions for user approval.
"""

import os, sys
import visual_curriculum_catalog as vcc
from build_all_curriculum_pages import CURRICULUM_MATHS, CURRICULUM_ENGLISH
from collections import Counter

# Audit Maths topics
maths_data = []
maths_photos_list = []

for fn, title in CURRICULUM_MATHS:
    photo, caption, _, _, svg = vcc.get_topic_visual(fn)
    maths_photos_list.append(photo)
    maths_data.append({
        "fn": fn,
        "title": title,
        "photo": photo,
        "caption": caption,
        "has_svg": bool(svg),
        "svg": svg
    })

# Audit English topics
english_data = []
english_photos_list = []

for fn, title in CURRICULUM_ENGLISH:
    photo, caption, _, _, svg = vcc.get_topic_visual(fn)
    english_photos_list.append(photo)
    english_data.append({
        "fn": fn,
        "title": title,
        "photo": photo,
        "caption": caption,
        "has_svg": bool(svg),
        "svg": svg
    })

maths_counts = Counter(maths_photos_list)
english_counts = Counter(english_photos_list)

print(f"Loaded {len(maths_data)} Maths topics and {len(english_data)} English topics.")
