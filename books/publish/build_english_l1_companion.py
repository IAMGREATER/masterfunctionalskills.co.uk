#!/usr/bin/env python3
"""
build_english_l1_companion.py
Compiles the complete 88-page Master Companion Workbook:
MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf

Mapped strictly to Pearson Edexcel & Ofqual Functional Skills English Level 1 Writing standards.
Full CGP-grade visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7),
Open Sans / Lexend typography, 11 writing formats (22 practice questions),
dedicated ruled candidate response sheets, peer-audit checklists against Pearson Band 1-4 criteria,
4 complete realistic mock exam papers, benchmark solutions, and explanatory mark schemes.
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

SRC_COMPANION = "/home/subi/Nextcloud/NVMe469GB/Work/Pearson Writing Guide/Level 1/Version 5/pearson_edexcel_level1_writing_companion_booklet.html"

def generate_l1_companion_html():
    with open(SRC_COMPANION, "r", encoding="utf-8") as f:
        src_html = f.read()

    # Extract only head/styles from src_html
    head_end = src_html.find("</head>")
    css_header = src_html[:head_end + 7]
    body_content = src_html[head_end + 7:]

    # Split body into original page divs
    orig_pages = re.split(r'(?=<div class=[\"\']page(?:[\"\']|\s+[^>]*[\"\']))', body_content)[1:]

    # Clean CSS in header: enforce Warm Cream canvas #FDFBF7, Lexend typography, exact A4 page budgeting
    clean_css = css_header.replace(
        "font-family: 'Open Sans', Arial, sans-serif;",
        "font-family: 'Open Sans', 'Lexend', Arial, sans-serif;"
    )
    clean_css = re.sub(r'(\.page\s*\{[^}]*background:\s*)#ffffff;', r'\1#FDFBF7;', clean_css)
    clean_css = re.sub(r'(body\s*\{[^}]*background:\s*)#ffffff;', r'\1#FDFBF7;', clean_css)
    clean_css = clean_css.replace("page-break-before: always;", "page-break-before: auto;")
    clean_css = clean_css.replace("break-before: page;", "break-before: auto;")

    built_pages = []

    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page first-page" style="padding:0; background:#0f766e; justify-content:center; align-items:center;">
  <div style="width:180mm; border:3px solid #fde047; border-radius:12px; padding:32px 28px; text-align:center; background:#115e59; color:#ffffff; box-shadow:0 10px 25px rgba(0,0,0,0.4);">
    <div style="background:#fde047; color:#115e59; font-family:'Montserrat',sans-serif; font-size:11pt; font-weight:900; padding:6px 20px; border-radius:20px; display:inline-block; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:18px;">
      Pearson Edexcel Functional Skills &bull; English Level 1
    </div>
    <div style="font-size:14pt; color:#99f6e4; font-weight:700; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;">
      88-Page Master Companion Workbook
    </div>
    <h1 style="color:#ffffff; font-size:26pt; font-weight:900; line-height:1.2; margin:0 0 12px 0;">
      Writing Practice Companion &amp; Mock Exam Pack
    </h1>
    <p style="font-size:12pt; color:#f0fdfa; line-height:1.45; margin:0 auto 20px auto; max-width:160mm;">
      22 Exam Format Practice Drills &bull; Dedicated Ruled Workspaces &bull; 4 Complete Practice Mock Papers &bull; Pearson Band 1&ndash;4 Criteria Rubrics &bull; Comprehensive Benchmark Exemplars
    </p>

    <div style="background:#042f2e; border-left:6px solid #fde047; border-radius:6px; padding:14px 18px; text-align:left; margin:16px auto; font-size:9pt; line-height:1.45;">
      <strong style="color:#fde047; font-size:10pt;">📌 Comprehensive 88-Page Workbook Features:</strong>
      <ul style="margin:6px 0 0 16px; padding:0; color:#ccfbf1;">
        <li><strong>Part 1: 11 Core Formats (Pages 4&ndash;47):</strong> 22 authentic exam-standard prompts with ruled writing spaces.</li>
        <li><strong>Part 2: Format Self-Audit &amp; Model Key (Pages 48&ndash;56):</strong> Band 1&ndash;4 marking rubrics &amp; benchmark answers.</li>
        <li><strong>Part 3: 4 Full Mock Examination Papers (Pages 57&ndash;84):</strong> Official 30-mark exam papers with planning scaffolds.</li>
        <li><strong>Part 4: Benchmark Solutions &amp; Pass Criteria (Pages 85&ndash;88):</strong> Examiner breakdown &amp; tutor sign-off.</li>
      </ul>
    </div>

    <div style="margin-top:20px; border-top:1px solid #14b8a6; padding-top:12px; display:flex; justify-content:space-between; font-size:8.5pt; color:#99f6e4; text-align:left;">
      <div>
        <strong>Curriculum Lead:</strong> Subi (Tutor Subi)<br>
        Functional Skills English Specialist &bull; masterfunctionalskills.co.uk
      </div>
      <div style="text-align:right;">
        <strong>Qualification Code:</strong> 603/4288/6<br>
        100% Dyslexia-Friendly Cream Architecture (#FDFBF7)
      </div>
    </div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 2: INSIDE COVER & CANDIDATE BLUEPRINT
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; English Level 1</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Candidate Workbook Blueprint</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 6px 0; font-size:14pt;">Writing Practice Companion &mdash; Learner Blueprint</h2>
  <p style="margin:0 0 8px 0; font-size:8.8pt;">This dedicated workbook is designed to be used alongside your <em>Level 1 Writing Core Guide</em>. It provides deliberate, repetitive practice across all 11 examination writing formats and 4 complete official-style mock examination papers.</p>

  <div class="card-concept" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:10px 12px; border-radius:5px; margin-bottom:8px;">
    <h3 style="color:#0f766e; margin:0 0 4px 0; font-size:9.5pt;">The Pearson Edexcel Band 1 to Band 4 Marking System</h3>
    <p style="margin:0; font-size:8.3pt; line-height:1.45;">
      In Functional Skills English Level 1 Writing, every piece of writing is marked out of <strong>15 marks</strong> (Task 1: 15 marks, Task 2: 15 marks, Total: 30 marks):<br>
      &bull; <strong>Composition &amp; Purpose (9 Marks):</strong> Audience awareness, appropriate tone, clear formatting, logical sequencing, and supporting details.<br>
      &bull; <strong>Spelling, Punctuation &amp; Grammar (6 Marks):</strong> Capital letters, full stops, question marks, commas in lists, simple apostrophes, and accurate spelling of common everyday words.
    </p>
  </div>

  <div class="grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:8px;">
    <div class="card-method" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4.5px solid #16a34a; padding:9px 12px; border-radius:5px; font-size:8.2pt;">
      <h3 style="color:#16a34a; margin:0 0 4px 0; font-size:9pt;">How to Use the Ruled Workspaces</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.4;">
        <li>Use a black ballpoint pen to simulate live exam conditions.</li>
        <li>Follow the word count guide indicator (~180&ndash;220 words per task).</li>
        <li>Spend 5 minutes planning using the quadrant box before writing.</li>
        <li>Leave 3&ndash;5 minutes at the end for the proofreading check.</li>
      </ul>
    </div>

    <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4.5px solid #d97706; padding:9px 12px; border-radius:5px; font-size:8.2pt;">
      <h3 style="color:#d97706; margin:0 0 4px 0; font-size:9pt;">Candidate Registration Details</h3>
      <table style="width:100%; border-collapse:collapse; font-size:7.8pt;">
        <tr><td style="padding:3px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:3px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Number:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:3px; border-bottom:1px solid #cbd5e1;"><strong>Centre Name / Number:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:3px; border-bottom:1px solid #cbd5e1;"><strong>Target Exam Date:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      </table>
    </div>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:6px;">
    Master Functional Skills &bull; Level 1 Writing Practice Companion &bull; Page 2
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: CONTENTS & 88-PAGE AUDIT MAP
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; English Level 1</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Curriculum Progress Matrix</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 4px 0; font-size:13pt;">88-Page Master Workbook Map &amp; Audit</h2>
  <p style="font-size:8pt; margin:0 0 6px 0;">Track your completed practice tasks and mock examination scores below:</p>

  <table style="width:100%; border-collapse:collapse; font-size:7.2pt; margin-bottom:6px;">
    <tr style="background:#0f766e; color:#ffffff; font-weight:700;">
      <th style="padding:4px 6px; text-align:left;">Section</th>
      <th style="padding:4px 6px; text-align:left;">Task / Module Name</th>
      <th style="padding:4px 6px; text-align:center;">Pages</th>
      <th style="padding:4px 6px; text-align:center;">Word Target</th>
      <th style="padding:4px 6px; text-align:center;">Self-Score</th>
    </tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 1</strong></td><td style="border-bottom:1px solid #e2e8f0;">Articles (Greenwood Park &bull; Youth Centre)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 4&ndash;7</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 2</strong></td><td style="border-bottom:1px solid #e2e8f0;">Workplace Emails (Shift Rota &bull; Training Request)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 8&ndash;11</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">160&ndash;200</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 3</strong></td><td style="border-bottom:1px solid #e2e8f0;">Formal Letters (Council Road Safety &bull; Course Letter)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 12&ndash;15</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 4</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reports (Library Computers &bull; Staff Facilities)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 16&ndash;19</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 5</strong></td><td style="border-bottom:1px solid #e2e8f0;">Incident Reports (Warehouse Slip &bull; Equipment Fault)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 20&ndash;23</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">160&ndash;200</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 6</strong></td><td style="border-bottom:1px solid #e2e8f0;">Public Advice Leaflets (Healthy Living &bull; Fire Safety)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 24&ndash;27</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 7</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reviews (Corner Bakery &bull; Leisure Centre)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 28&ndash;31</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">160&ndash;200</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 8</strong></td><td style="border-bottom:1px solid #e2e8f0;">Online Feedback (Shopping Centre &bull; Bus Service)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 32&ndash;35</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">140&ndash;180</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 9</strong></td><td style="border-bottom:1px solid #e2e8f0;">Online Forum / Blog (Rescue Dog &bull; Cycling to Work)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 36&ndash;39</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">160&ndash;200</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 10</strong></td><td style="border-bottom:1px solid #e2e8f0;">Newsletters (Community Centre &bull; Workplace News)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 40&ndash;43</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 11</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reflective Logs (Induction Log &bull; Weekly Diary)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 44&ndash;47</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">150&ndash;190</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr style="background:#fef2f2;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Criteria</strong></td><td style="border-bottom:1px solid #e2e8f0;">Self-Audit Rubrics, Glossary &amp; 22 Format Benchmark Keys</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 48&ndash;56</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Benchmark</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Verified</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 1</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 1: Formal Letter &bull; Healthy Eating Leaflet</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 57&ndash;63</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 2</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 2: Incident Report &bull; Community Article</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 64&ndash;70</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 3</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 3: Workplace Email &bull; Facility Review</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 71&ndash;77</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 4</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 4: Housing Letter &bull; Animal Rescue Blog</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 78&ndash;84</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#eff6ff;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Solutions</strong></td><td style="border-bottom:1px solid #e2e8f0;">Mock Benchmark Exemplars &amp; Final Readiness Sign-Off</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 85&ndash;88</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Full Key</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Signed</td></tr>
  </table>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:6px;">
    Master Functional Skills &bull; Level 1 Writing Practice Companion &bull; Page 3
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGES 4 TO 47: 11 FORMATS (44 Pages: orig_pages[2] to orig_pages[45])
    # -------------------------------------------------------------
    for p_idx, p_content in enumerate(orig_pages[2:46], 4):
        p_clean = re.sub(r'(\.page\s*\{[^}]*background:\s*)#ffffff;', r'\1#FDFBF7;', p_content)
        p_clean = re.sub(r'style="([^"]*background:\s*)#ffffff', r'style="\1#FDFBF7', p_clean)
        p_clean = re.sub(r'<span class="page-num-pill">Page \d+</span>', f'<span class="page-num-pill">Page {p_idx}</span>', p_clean)
        built_pages.append(p_clean)

    # -------------------------------------------------------------
    # PAGES 48 TO 56: SELF-AUDIT, GLOSSARY, FORMAT ANSWERS (9 Pages)
    # orig_pages[46] to orig_pages[54]
    # -------------------------------------------------------------
    for p_idx, p_content in enumerate(orig_pages[46:55], 48):
        if p_idx == 56 and '<div class="cover-page">' in p_content:
            p_content = p_content.split('<div class="cover-page">')[0]
        p_clean = re.sub(r'(\.page\s*\{[^}]*background:\s*)#ffffff;', r'\1#FDFBF7;', p_content)
        p_clean = re.sub(r'<span class="page-num-pill">Page \d+</span>', f'<span class="page-num-pill">Page {p_idx}</span>', p_clean)
        built_pages.append(p_clean)

    # -------------------------------------------------------------
    # PAGES 57 TO 84: 4 FULL PRACTICE MOCK EXAMS (28 Pages = 7 Pages Each)
    # -------------------------------------------------------------
    mock_specs = [
        # Mock 1
        ("Mock Examination 1",
         # Task 1: Formal Letter
         ("Task 1: Formal Letter to College Principal (15 Marks)",
          "You are interested in improving your qualifications to gain a promotion at work. You wish to enrol on an evening computer course at Oakwood Community College. However, the current college website does not list course start times, fees, or whether free childcare is available during evening lessons.",
          "Write a formal letter to the College Principal, Dr Martin Hayes.",
          ["State clearly why you are writing and which evening course you wish to join.",
           "Explain how gaining this digital qualification will help you in your current job.",
           "Ask for details regarding term dates, weekly lesson times, course fees, and childcare.",
           "Use appropriate formal letter layout (addresses, date, greeting, and sign-off)."]),
         # Task 2: Advice Leaflet
         ("Task 2: Informational Health & Wellbeing Leaflet (15 Marks)",
          "You work at a large supermarket distribution centre. The staff wellbeing committee wants to encourage employees to make healthier lifestyle choices, improve their nutrition, and stay active during breaks.",
          "Write the text for an information leaflet titled: 'Eating Well & Staying Active at Work: A Quick Guide for Staff'.",
          ["An attractive title and friendly introductory section explaining the benefits of healthy eating.",
           "Practical tips for packing healthy lunches and choosing nutritious snacks during shifts.",
           "Advice on staying hydrated and taking short, active walking breaks throughout the working day.",
           "Contact information for the staff wellness officer and local gym discount schemes."])),

        # Mock 2
        ("Mock Examination 2",
         # Task 1: Incident Report
         ("Task 1: Workplace Incident & Safety Report (15 Marks)",
          "You work in the kitchen at The Grand Hotel. On Friday 17 October at 12:45 pm, the commercial dishwasher began leaking soapy water onto the kitchen floor. A commis chef slipped on the wet tiles and dropped a tray of clean plates, cutting their thumb.",
          "Write a factual incident report to the Head Chef, Mr Carlos Mendez.",
          ["State the exact date, time, and kitchen location of the accident.",
           "Describe clearly what happened and how the chef was injured.",
           "Explain the immediate first aid and safety actions taken to clean the spill.",
           "Suggest two ways to prevent similar water leak accidents from happening again."]),
         # Task 2: Article
         ("Task 2: Article for Local Community Magazine (15 Marks)",
          "Your local neighbourhood council is creating a new community allotment and wildlife garden. They need volunteers of all ages to help clear the land, plant vegetables, and build raised garden beds.",
          "Write an enthusiastic, persuasive article for the Greenwood Community Chronicle titled: 'Help Grow Our Future: Join the Community Garden Project'.",
          ["Explain what the community garden project is and why it is important for the local area.",
           "Describe the different volunteer activities available (gardening, building, painting, tea making).",
           "Highlight the personal benefits of volunteering (meeting neighbours, learning new skills, fresh air).",
           "Give clear details on how residents can sign up and when the first planting day will take place."])),

        # Mock 3
        ("Mock Examination 3",
         # Task 1: Workplace Email
         ("Task 1: Workplace Email to Store Manager (15 Marks)",
          "You work as a customer service assistant at City Electricals. Your store manager, Mrs Angela Wright, has published the weekend shift rota for the busy Christmas shopping period. You notice that you have been scheduled to work on Saturday 20 December, a day you had booked off three months ago to attend your brother's wedding.",
          "Write a polite, professional email to Mrs Angela Wright (manager@cityelectricals.co.uk).",
          ["Explain clearly the issue with the current rota and the date you cannot work.",
           "Remind Mrs Wright of your previous leave approval and explain the reason for your absence.",
           "Offer a practical solution (such as swapping your shift with a colleague who has agreed).",
           "Ask for confirmation that the revised rota has been updated."]),
         # Task 2: Review
         ("Task 2: Evaluative Review of New Community Sports Centre (15 Marks)",
          "You recently visited the newly opened Riverdale Leisure Centre with your family. You used the swimming pool, fitness gym, and cafeteria. While the swimming facilities were modern and clean, the cafeteria was short-staffed and ran out of fresh food.",
          "Write an honest, balanced review for a local leisure website titled: 'Riverdale Leisure Centre: Great Pool but Cafeteria Needs Work'.",
          ["Give a star rating (e.g. 3 or 4 out of 5 stars) and a catchy headline.",
           "Describe what you liked about the swimming pool, changing rooms, and gym equipment.",
           "Explain politely what needs improvement in the cafeteria (wait times, food choices).",
           "Conclude with a clear recommendation on who should visit."])),

        # Mock 4
        ("Mock Examination 4",
         # Task 1: Formal Letter
         ("Task 1: Formal Letter to Housing Office (15 Marks)",
          "You are a resident of Victoria Court. Over the past month, the communal front entrance door has been broken and will not lock securely, allowing non-residents to enter the hallway. In addition, the hallway lights have failed, leaving the stairwell dark and dangerous at night.",
          "Write a formal letter to your Housing Officer, Ms Rachel Adams, at Metro Housing Association.",
          ["Explain the two specific problems (broken lock and failed lights) with dates and locations.",
           "Describe the safety and security risks these issues cause for residents, especially children and elderly tenants.",
           "Request urgent repairs to be completed within seven days.",
           "Use correct formal letter layout with addresses, date, and professional sign-off."]),
         # Task 2: Persuasive Blog Post
         ("Task 2: Persuasive Blog Post for Animal Shelter (15 Marks)",
          "You volunteer at the Hope Animal Rescue Centre. The shelter is currently full of rescue dogs and cats looking for loving, permanent homes. You want to persuade local families to adopt a rescue pet rather than buying puppies from online sellers.",
          "Write an engaging blog post for the shelter website titled: 'Adopt, Don't Shop: Why Rescue Pets Make the Best Companions'.",
          ["An eye-catching opening explaining why rescue pets are so special.",
           "Explain the benefits of adopting from a registered rescue shelter (health checks, vaccinations, advice).",
           "Describe what potential owners should consider before adopting (time, space, exercise).",
           "End with an encouraging call to action inviting readers to visit the adoption open day."]))
    ]

    for m_idx, (m_title, (t1_name, t1_scenario, t1_task, t1_bullets), (t2_name, t2_scenario, t2_task, t2_bullets)) in enumerate(mock_specs, 1):
        m_start_pg = 57 + (m_idx - 1) * 7

        # PAGE 1: TASK 1 PROMPT & PLANNING SCAFFOLD
        bullets_t1_html = "".join([f"<li style='margin-bottom:3px;'>{b}</li>" for b in t1_bullets])
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Stimulus &amp; Planning</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <h2 style="color:#0f766e; margin:0; font-size:12.5pt;">{t1_name}</h2>
    <span style="background:#0f766e; color:#ffffff; padding:2px 8px; border-radius:4px; font-weight:700; font-size:7.5pt;">15 MARKS &bull; 30 MINS</span>
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 12px; border-radius:5px; margin-bottom:8px; font-size:8.3pt; line-height:1.42;">
    <strong>Scenario Stimulus:</strong> {t1_scenario}
    <p style="margin:5px 0 3px 0; font-weight:700; color:#0f766e;">{t1_task}</p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:8pt;">
      {bullets_t1_html}
    </ul>
  </div>

  <h3 style="color:#0f766e; margin:4px 0 2px 0; font-size:9pt;">Mandatory 5-Minute Planning Scaffold (4 Quadrants):</h3>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:6px;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[1] Audience &amp; Formal Tone:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[2] Structural Conventions Required:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[3] Key Factual Details &amp; Points:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[4] SPaG Target (Capitals &amp; Commas):</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
  </div>

  <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4px solid #d97706; padding:5px 8px; font-size:7.5pt;">
    <strong>Tutor Advice:</strong> Turn to <strong>Pages {m_start_pg+1} and {m_start_pg+2}</strong> to write your official candidate response. Aim for 180&ndash;220 words across the two ruled pages.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg}
  </div>
</div>
""")

        # PAGE 2: TASK 1 CANDIDATE RESPONSE SHEET (PART 1)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Candidate Response (Page 1 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#0f766e; font-size:9pt;">Task 1: Official Candidate Writing Space</strong>
    <span style="font-size:7.5pt; color:#64748b;">Target: ~100 words on this page</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:225mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+1}
  </div>
</div>
""")

        # PAGE 3: TASK 1 CANDIDATE RESPONSE SHEET (PART 2)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Candidate Response (Page 2 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#0f766e; font-size:9pt;">Task 1: Conclusion &amp; Final Proofread</strong>
    <span style="font-size:7.5pt; color:#64748b;">Cumulative Word Count: ~180&ndash;220 words</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:190mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:6px 10px; margin-top:8px; font-size:7.5pt; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Task 1 Verification:</strong> [ &nbsp; ] All bullet points met &nbsp;&bull;&nbsp; [ &nbsp; ] Capital letters verified &nbsp;&bull;&nbsp; [ &nbsp; ] Full stops used</div>
    <div><strong>Word Count:</strong> ______</div>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+2}
  </div>
</div>
""")

        # PAGE 4: TASK 2 PROMPT & PLANNING SCAFFOLD
        bullets_t2_html = "".join([f"<li style='margin-bottom:3px;'>{b}</li>" for b in t2_bullets])
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Stimulus &amp; Planning</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <h2 style="color:#0f766e; margin:0; font-size:12.5pt;">{t2_name}</h2>
    <span style="background:#0f766e; color:#ffffff; padding:2px 8px; border-radius:4px; font-weight:700; font-size:7.5pt;">15 MARKS &bull; 30 MINS</span>
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 12px; border-radius:5px; margin-bottom:8px; font-size:8.3pt; line-height:1.42;">
    <strong>Scenario Stimulus:</strong> {t2_scenario}
    <p style="margin:5px 0 3px 0; font-weight:700; color:#0f766e;">{t2_task}</p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:8pt;">
      {bullets_t2_html}
    </ul>
  </div>

  <h3 style="color:#0f766e; margin:4px 0 2px 0; font-size:9pt;">Mandatory 5-Minute Planning Scaffold (4 Quadrants):</h3>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:6px;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[1] Target Audience &amp; Main Purpose:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[2] Title &amp; Heading Structure:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[3] Key Information &amp; Advice Points:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#0f766e;">[4] Positive Call to Action / Next Step:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
  </div>

  <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4px solid #d97706; padding:5px 8px; font-size:7.5pt;">
    <strong>Tutor Advice:</strong> Turn to <strong>Pages {m_start_pg+4} and {m_start_pg+5}</strong> to write your official candidate response. Use clear paragraphs with bullet points if helpful.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+3}
  </div>
</div>
""")

        # PAGE 5: TASK 2 CANDIDATE RESPONSE SHEET (PART 1)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Candidate Response (Page 1 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#0f766e; font-size:9pt;">Task 2: Official Candidate Writing Space</strong>
    <span style="font-size:7.5pt; color:#64748b;">Target: ~100 words on this page</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:225mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+4}
  </div>
</div>
""")

        # PAGE 6: TASK 2 CANDIDATE RESPONSE SHEET (PART 2)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Candidate Response (Page 2 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#0f766e; font-size:9pt;">Task 2: Conclusion, Contact Details &amp; Proofread</strong>
    <span style="font-size:7.5pt; color:#64748b;">Cumulative Word Count: ~180&ndash;220 words</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:190mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:6px 10px; margin-top:8px; font-size:7.5pt; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Task 2 Verification:</strong> [ &nbsp; ] All prompts covered &nbsp;&bull;&nbsp; [ &nbsp; ] Clear paragraphs &nbsp;&bull;&nbsp; [ &nbsp; ] Contact info included</div>
    <div><strong>Word Count:</strong> ______</div>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+5}
  </div>
</div>
""")

        # PAGE 7: PEER-AUDIT CHECKLIST & EXAMINER MARK SCHEME
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Pearson Band 1&ndash;4 Examiner Audit</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 6px 0; font-size:13pt;">{m_title} &mdash; Candidate Peer-Audit &amp; Marking Rubric</h2>
  <p style="font-size:8pt; margin:0 0 8px 0;">Use this official Pearson Level 1 marking rubric to evaluate your practice tasks:</p>

  <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-bottom:8px;">
    <tr style="background:#0f766e; color:#ffffff;">
      <th style="padding:4px 6px; text-align:left; width:18%;">Mark Band</th>
      <th style="padding:4px 6px; text-align:left; width:52%;">Composition &amp; Purpose Descriptors (9 Marks)</th>
      <th style="padding:4px 6px; text-align:left; width:30%;">SPaG Standards (6 Marks)</th>
    </tr>
    <tr style="background:#f0fdf4;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 4 (Distinction)<br>Task Total: 13&ndash;15m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Clear, polite, and effective tone; all prompts from the scenario fully developed; excellent paragraph organization; correct letter/email/report formatting.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Consistent capital letters and full stops; accurate commas in lists; compound sentences with conjunctions; high spelling accuracy.</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 3 (Strong Pass)<br>Task Total: 9&ndash;12m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Appropriate purpose and audience awareness; all main prompts addressed; ideas grouped into basic paragraphs; recognizable layout.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Mostly accurate sentence boundaries; capital letters used for names/days; common workplace words spelled correctly.</td>
    </tr>
    <tr style="background:#fffbeb;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 2 (Borderline)<br>Task Total: 5&ndash;8m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Some awareness of task; tone may be slightly informal; brief sentences; 1&ndash;2 bullet points missed; limited paragraph breaks.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Frequent missing capital letters or full stops; some run-on sentences; spelling errors in regular past tense or plurals.</td>
    </tr>
    <tr style="background:#fef2f2;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 1 (Unclassified)<br>Task Total: 1&ndash;4m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Minimal response; lacks required formatting; bullet points not answered; unclear meaning.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Significant breakdown in basic punctuation and spelling; very short disconnected fragments.</td>
    </tr>
  </table>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:5px; padding:8px 12px; margin-bottom:8px;">
    <strong style="color:#0f766e; font-size:8.5pt;">Candidate Exam Score Summary:</strong>
    <div style="display:flex; justify-content:space-around; margin-top:6px; font-size:8.5pt;">
      <div><strong>Task 1:</strong> [ &nbsp; /15 ]</div>
      <div><strong>Task 2:</strong> [ &nbsp; /15 ]</div>
      <div><strong>Total Exam Score:</strong> [ &nbsp; /30 ]</div>
      <div><strong>Verdict:</strong> [ &nbsp; ] PASS &nbsp; [ &nbsp; ] RETAKE</div>
    </div>
  </div>

  <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4px solid #d97706; padding:6px 10px; font-size:7.5pt;">
    <strong>Tutor Feedback &amp; Action Target:</strong><br>
    ________________________________________________________________________________________________________________________<br>
    ________________________________________________________________________________________________________________________
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; {m_title} &bull; Page {m_start_pg+6}
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGES 85 TO 87: BENCHMARK SOLUTIONS & MARK SCHEMES (3 Pages)
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; English Level 1</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Examiner Solutions &bull; Mocks 1 &amp; 2</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 6px 0; font-size:13pt;">Mock Exams 1 &amp; 2 &mdash; Band 4 Benchmark Solutions</h2>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 1 Task 1: Formal Letter to Principal Benchmark (15/15)</strong><br>
    Standard layout (candidate address top right, date, Dr Hayes address top left). 'Dear Dr Hayes', 'Re: Evening Digital Skills Course Inquiry'. Clearly explains desire to qualify for promotion at work, asks about course fees, start times, and confirms whether evening childcare is provided. Closes with 'Yours sincerely' and printed name.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 1 Task 2: Health &amp; Wellbeing Leaflet Benchmark (15/15)</strong><br>
    <strong>Title:</strong> Eating Well &amp; Staying Active at Work: A Quick Guide for Staff.<br>
    Welcoming opening highlighting energy benefits; subheadings for 'Packing a Healthy Lunch', 'Hydration &amp; Water', and 'Active Breaks'; bulleted suggestions; contact email for wellness officer. Clear, positive instructional tone throughout.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 2 Task 1: Kitchen Incident Report Benchmark (15/15)</strong><br>
    Clear heading, date (Friday 17 October), time (12:45 pm), location (Main Kitchen). Describes dishwasher leak, commis chef slipping, and broken plates causing cut thumb. First aid applied and floor dried. Recommends urgent plumber repair and rubber anti-slip mats.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 2 Task 2: Community Garden Article Benchmark (15/15)</strong><br>
    Catchy headline; explains allotment project; lists volunteer roles (digging, planting, painting); emphasizes social and health benefits; provides contact phone and date of first planting session.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; Examiner Solutions &bull; Page 85
  </div>
</div>
""")

    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; English Level 1</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Examiner Solutions &bull; Mocks 3 &amp; 4</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 6px 0; font-size:13pt;">Mock Exams 3 &amp; 4 &mdash; Band 4 Benchmark Solutions</h2>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 3 Task 1: Rota Issue Email Benchmark (15/15)</strong><br>
    To: manager@cityelectricals.co.uk &bull; Subject: Shift Rota Inquiry &mdash; Saturday 20 December.<br>
    Polite greeting ('Dear Mrs Wright'); explains pre-booked leave for brother's wedding; states that colleague Jack has agreed to cover; asks for confirmation. Closes with 'Kind regards' and candidate name.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 3 Task 2: Sports Centre Review Benchmark (15/15)</strong><br>
    Headline: "Riverdale Leisure Centre: Great Pool but Cafeteria Needs Work" (Rating: 4 / 5 Stars).<br>
    Praises clean changing rooms, warm pool water, and modern gym machines. Politely points out slow cafeteria service and shortage of hot food. Recommends centre for families.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 4 Task 1: Housing Maintenance Letter Benchmark (15/15)</strong><br>
    Standard formal letter format. 'Dear Ms Adams', 'Re: Urgent Communal Repairs at Victoria Court'. Details broken lock and stairwell light outage; explains security concerns for elderly tenants; requests repairs within seven days. Closes with 'Yours sincerely'.
  </div>

  <div class="card-exam" style="background:#f0fdfa; border:1px solid #99f6e4; border-left:4.5px solid #0f766e; padding:8px 10px; border-radius:5px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#0f766e; font-size:8pt;">Mock 4 Task 2: Animal Adoption Blog Benchmark (15/15)</strong><br>
    Catchy title: "Adopt, Don't Shop: Why Rescue Pets Make the Best Companions". Friendly opening; explains benefits of veterinary checks and rescue support; advises on pet care responsibilities; warmly invites readers to Saturday's open day.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; Examiner Solutions &bull; Page 86
  </div>
</div>
""")

    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #0f766e; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#0f766e; text-transform:uppercase;">Master Functional Skills &bull; English Level 1</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Final Readiness Verification</div>
  </div>

  <h2 style="color:#0f766e; margin:0 0 6px 0; font-size:13pt;">Master Level 1 Writing Readiness Verification</h2>
  <p style="font-size:8pt; margin:0 0 8px 0;">Review your comprehensive preparation before sitting your official Pearson Level 1 exam:</p>

  <div class="grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:8px;">
    <div class="card-method" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4.5px solid #16a34a; padding:8px 12px; border-radius:5px; font-size:8pt;">
      <h3 style="color:#16a34a; margin:0 0 4px 0; font-size:9pt;">Skills Mastered Audit:</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.45;">
        <li>[ &nbsp; ] All 11 Writing Formats practiced</li>
        <li>[ &nbsp; ] 4 Practice Mock Papers completed</li>
        <li>[ &nbsp; ] 4-Quadrant planning used on every task</li>
        <li>[ &nbsp; ] Capital letters (MINTS) verified</li>
        <li>[ &nbsp; ] Full stops and question marks accurate</li>
        <li>[ &nbsp; ] 5-minute proofreading routine embedded</li>
      </ul>
    </div>

    <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4.5px solid #d97706; padding:8px 12px; border-radius:5px; font-size:8pt;">
      <h3 style="color:#d97706; margin:0 0 4px 0; font-size:9pt;">Exam Day Golden Rules:</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.45;">
        <li>Divide time evenly: 30 mins Task 1, 30 mins Task 2.</li>
        <li>Always write in the specified format (email headers, letter addresses, article titles).</li>
        <li>Aim for 180&ndash;220 words per task.</li>
        <li>Keep your handwriting clear, legible, and dark.</li>
      </ul>
    </div>
  </div>

  <div class="card-practice" style="background:#ffffff; border:1.5px solid #0f766e; padding:10px 14px; border-radius:6px; margin-top:8px;">
    <h3 style="color:#0f766e; margin:0 0 6px 0; font-size:9.5pt;">Tutor Endorsement &amp; Exam Authorization</h3>
    <table style="width:100%; border-collapse:collapse; font-size:8pt; margin-top:4px;">
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1; width:35%;"><strong>Tutor / Assessor Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Assessor Signature:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Final Mock Exam Average:</strong></td><td style="border-bottom:1px solid #cbd5e1;">____ / 30 Marks</td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Exam Readiness:</strong></td><td style="border-bottom:1px solid #cbd5e1;">[ &nbsp; ] FULLY READY &nbsp;&bull;&nbsp; [ &nbsp; ] ADDITIONAL REVISION NEEDED</td></tr>
    </table>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 1 &bull; Readiness Sign-Off &bull; Page 87
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 88: BACK COVER (FULL BLEED)
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page cover-full-page" style="padding:0; background:#0f766e; justify-content:center; align-items:center;">
  <div style="width:180mm; border:3px solid #fde047; border-radius:12px; padding:32px 28px; text-align:center; background:#115e59; color:#ffffff; box-shadow:0 10px 25px rgba(0,0,0,0.4);">
    <div style="font-size:12pt; color:#99f6e4; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;">
      Master Functional Skills &bull; Curriculum Edition
    </div>
    <h2 style="color:#ffffff; font-size:22pt; font-weight:900; line-height:1.25; margin:0 0 10px 0;">
      Everything You Need to Pass Functional Skills English Level 1 Writing
    </h2>
    <p style="font-size:10pt; color:#f0fdfa; line-height:1.45; margin:0 auto 16px auto; max-width:160mm;">
      Published by DarkNight Educational Press in partnership with the Master Functional Skills Learning Network. Designed strictly in accordance with Ofqual subject content regulations and British Dyslexia Association accessibility standards.
    </p>

    <div style="background:#042f2e; border-radius:6px; padding:12px 16px; margin:14px auto; font-size:8.5pt; color:#ccfbf1; text-align:left; line-height:1.5;">
      <strong>Why Learners &amp; Colleges Choose Our Workbooks:</strong>
      <ul style="margin:4px 0 0 16px; padding:0;">
        <li><strong>Zero Visual Fatigue:</strong> Accessible warm cream canvas (#FDFBF7) with Lexend typography.</li>
        <li><strong>Comprehensive Practice:</strong> 22 realistic writing drills covering all 11 examination formats.</li>
        <li><strong>Authentic Mock Exams:</strong> 4 full 30-mark practice papers with official Pearson marking rubrics.</li>
        <li><strong>Guaranteed Progress:</strong> Step-by-step scaffolded writing frames and full benchmark answers.</li>
      </ul>
    </div>

    <div style="margin-top:18px; border-top:1px solid #14b8a6; padding-top:10px; display:flex; justify-content:space-between; align-items:center; font-size:8pt; color:#99f6e4;">
      <div>
        <strong>Master Functional Skills</strong><br>
        masterfunctionalskills.co.uk
      </div>
      <div style="text-align:right;">
        <strong>ISBN:</strong> 978-1-912345-71-5<br>
        Standard A4 &bull; 88 Pages Complete
      </div>
    </div>
  </div>
</div>
""")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pearson Edexcel Level 1 Functional Skills English - Writing Practice Companion (Master 88-Page Edition)</title>
{clean_css}
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}
  body {{
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', 'Lexend', Arial, sans-serif !important;
    background: #FDFBF7 !important;
    color: #1a202c;
  }}
  .page {{
    width: 210mm !important;
    height: 297mm !important;
    min-height: 297mm !important;
    max-height: 297mm !important;
    page-break-after: always !important;
    break-after: page !important;
    position: relative !important;
    overflow: hidden !important;
    padding: 12mm 15mm 13mm 15mm !important;
    background: #FDFBF7 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
  }}
  .cover-full-page {{
    padding: 0 !important;
    background: #0f766e !important;
  }}
</style>
</head>
<body>
{''.join(built_pages)}
</body>
</html>"""

    return full_html, len(built_pages)

def build_english_l1_companion():
    html, page_divs = generate_l1_companion_html()
    print(f"[*] Generated HTML with {page_divs} page divs.")
    pdf_filename = "MasterFunctionalSkills_English_Writing_Level_1_Companion_Workbook.pdf"
    pages = render_book_to_pdf(html, pdf_filename)
    return pages

if __name__ == "__main__":
    build_english_l1_companion()
