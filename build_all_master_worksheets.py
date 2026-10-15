#!/usr/bin/env python3
"""
Master Functional Skills - Comprehensive Worksheet & Answer Key Engine.
Generates 100% original, Pearson Edexcel aligned worksheets & mark schemes
across all curriculum areas:
- Maths (Numbers, Calculations, Measures, Shape, Space, Data, Probability)
- English (Reading comprehension, text analysis, writing forms, SPaG)
- Speaking, Listening & Communicating (SLC scenarios, discussions, presentation frameworks)
- Digital Functional Skills (devices, spreadsheets, email security, digital safety)
"""

import os, sys
from worksheet_templates import render_worksheet, render_answers

OUTPUT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/worksheets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# We will populate our master dictionary TOPIC_REGISTRY
TOPIC_REGISTRY = {}

def register_topic(topic_dict):
    TOPIC_REGISTRY[topic_dict['slug']] = topic_dict

