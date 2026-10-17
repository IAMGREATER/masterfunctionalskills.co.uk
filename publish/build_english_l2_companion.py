#!/usr/bin/env python3
"""
build_english_l2_companion.py
Compiles the complete 88-page Master Companion Workbook:
MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf

Mapped strictly to Pearson Edexcel & Ofqual Functional Skills English Level 2 Writing standards.
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

SRC_COMPANION = "/home/subi/Nextcloud/NVMe469GB/Work/Pearson Writing Guide/Level 2/Version 7/pearson_edexcel_level2_writing_companion_booklet.html"

def generate_l2_companion_html():
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
    # Remove any page-break-before: always that might create blank pages
    clean_css = clean_css.replace("page-break-before: always;", "page-break-before: auto;")
    clean_css = clean_css.replace("break-before: page;", "break-before: auto;")

    built_pages = []

    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page first-page" style="padding:0; background:#003366; justify-content:center; align-items:center;">
  <div style="width:180mm; border:3px solid #facc15; border-radius:12px; padding:32px 28px; text-align:center; background:#002244; color:#ffffff; box-shadow:0 10px 25px rgba(0,0,0,0.4);">
    <div style="background:#facc15; color:#002244; font-family:'Montserrat',sans-serif; font-size:11pt; font-weight:900; padding:6px 20px; border-radius:20px; display:inline-block; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:18px;">
      Pearson Edexcel Functional Skills &bull; English Level 2
    </div>
    <div style="font-size:14pt; color:#93c5fd; font-weight:700; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;">
      88-Page Master Companion Workbook
    </div>
    <h1 style="color:#ffffff; font-size:26pt; font-weight:900; line-height:1.2; margin:0 0 12px 0;">
      Writing Practice Companion &amp; Mock Exam Pack
    </h1>
    <p style="font-size:12pt; color:#e2e8f0; line-height:1.45; margin:0 auto 20px auto; max-width:160mm;">
      22 Exam Format Practice Drills &bull; Dedicated Ruled Workspaces &bull; 4 Complete Practice Mock Papers &bull; Pearson Band 1&ndash;4 Criteria Rubrics &bull; Comprehensive Benchmark Exemplars
    </p>

    <div style="background:#0f172a; border-left:6px solid #facc15; border-radius:6px; padding:14px 18px; text-align:left; margin:16px auto; font-size:9pt; line-height:1.45;">
      <strong style="color:#facc15; font-size:10pt;">📌 Comprehensive 88-Page Workbook Features:</strong>
      <ul style="margin:6px 0 0 16px; padding:0; color:#cbd5e1;">
        <li><strong>Part 1: 11 Core Formats (Pages 4&ndash;47):</strong> 22 authentic exam-standard prompts with ruled writing spaces.</li>
        <li><strong>Part 2: Format Self-Audit &amp; Model Key (Pages 48&ndash;56):</strong> Band 1&ndash;4 marking rubrics &amp; benchmark answers.</li>
        <li><strong>Part 3: 4 Full Mock Examination Papers (Pages 57&ndash;84):</strong> Official 30-mark exam papers with planning scaffolds.</li>
        <li><strong>Part 4: Benchmark Solutions &amp; Pass Criteria (Pages 85&ndash;88):</strong> Examiner breakdown &amp; tutor sign-off.</li>
      </ul>
    </div>

    <div style="margin-top:20px; border-top:1px solid #1e3a8a; padding-top:12px; display:flex; justify-content:space-between; font-size:8.5pt; color:#94a3b8; text-align:left;">
      <div>
        <strong>Curriculum Lead:</strong> Subi (Tutor Subi)<br>
        Functional Skills English Specialist &bull; masterfunctionalskills.co.uk
      </div>
      <div style="text-align:right;">
        <strong>Qualification Code:</strong> 603/4289/8<br>
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
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; English Level 2</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Candidate Workbook Blueprint</div>
  </div>

  <h2 style="color:#003366; margin:0 0 6px 0; font-size:14pt;">Writing Practice Companion &mdash; Learner Blueprint</h2>
  <p style="margin:0 0 8px 0; font-size:8.8pt;">This dedicated workbook is designed to be used alongside your <em>Level 2 Writing Core Guide</em>. It provides deliberate, repetitive practice across all 11 examination writing formats and 4 complete official-style mock examination papers.</p>

  <div class="card-concept" style="background:#f0f7ff; border:1px solid #bfdbfe; border-left:4.5px solid #003366; padding:10px 12px; border-radius:5px; margin-bottom:8px;">
    <h3 style="color:#003366; margin:0 0 4px 0; font-size:9.5pt;">The Pearson Edexcel Band 1 to Band 4 Marking System</h3>
    <p style="margin:0; font-size:8.3pt; line-height:1.45;">
      In Functional Skills English Level 2 Writing, every piece of writing is marked out of <strong>15 marks</strong> (Task 1: 15 marks, Task 2: 15 marks, Total: 30 marks):<br>
      &bull; <strong>Composition &amp; Purpose (9 Marks):</strong> Audience, register, formatting conventions, paragraph cohesion, persuasive/explanatory devices.<br>
      &bull; <strong>Spelling, Punctuation &amp; Grammar (6 Marks):</strong> Sentence boundaries, complex punctuation (colons, semicolons), and spelling accuracy.
    </p>
  </div>

  <div class="grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:8px;">
    <div class="card-method" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4.5px solid #16a34a; padding:9px 12px; border-radius:5px; font-size:8.2pt;">
      <h3 style="color:#16a34a; margin:0 0 4px 0; font-size:9pt;">How to Use the Ruled Workspaces</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.4;">
        <li>Use a black ballpoint pen to simulate live exam conditions.</li>
        <li>Follow the word count guide indicator (~200&ndash;250 words per task).</li>
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
    Master Functional Skills &bull; Level 2 Writing Practice Companion &bull; Page 2
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: CONTENTS & 88-PAGE AUDIT MAP
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; English Level 2</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Curriculum Progress Matrix</div>
  </div>

  <h2 style="color:#003366; margin:0 0 4px 0; font-size:13pt;">88-Page Master Workbook Map &amp; Audit</h2>
  <p style="font-size:8pt; margin:0 0 6px 0;">Track your completed practice tasks and mock examination scores below:</p>

  <table style="width:100%; border-collapse:collapse; font-size:7.2pt; margin-bottom:6px;">
    <tr style="background:#003366; color:#ffffff; font-weight:700;">
      <th style="padding:4px 6px; text-align:left;">Section</th>
      <th style="padding:4px 6px; text-align:left;">Task / Module Name</th>
      <th style="padding:4px 6px; text-align:center;">Pages</th>
      <th style="padding:4px 6px; text-align:center;">Word Target</th>
      <th style="padding:4px 6px; text-align:center;">Self-Score</th>
    </tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 1</strong></td><td style="border-bottom:1px solid #e2e8f0;">Articles (Community Park &bull; Youth Training)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 4&ndash;7</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;250</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 2</strong></td><td style="border-bottom:1px solid #e2e8f0;">Workplace Emails (Rota Change &bull; Client Project)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 8&ndash;11</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 3</strong></td><td style="border-bottom:1px solid #e2e8f0;">Formal Letters (Council Complaint &bull; Job Grievance)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 12&ndash;15</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;250</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 4</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reports (IT Infrastructure &bull; Health &amp; Safety Audit)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 16&ndash;19</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">220&ndash;260</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 5</strong></td><td style="border-bottom:1px solid #e2e8f0;">Incident Reports (Warehouse Hazard &bull; Slip/Trip Log)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 20&ndash;23</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 6</strong></td><td style="border-bottom:1px solid #e2e8f0;">Public Advice Leaflets (Shift Health &bull; Fire Protocol)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 24&ndash;27</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;250</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 7</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reviews (Corporate Hotel &bull; Equipment Evaluation)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 28&ndash;31</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;240</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 8</strong></td><td style="border-bottom:1px solid #e2e8f0;">Online Feedback (Service Centre &bull; Transit Portal)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 32&ndash;35</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">160&ndash;200</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 9</strong></td><td style="border-bottom:1px solid #e2e8f0;">Online Forum / Blog (Apprenticeship Debate &bull; Tech)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 36&ndash;39</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;240</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 10</strong></td><td style="border-bottom:1px solid #e2e8f0;">Newsletters (Staff Internal &bull; Community Action)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 40&ndash;43</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">200&ndash;250</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Format 11</strong></td><td style="border-bottom:1px solid #e2e8f0;">Reflective Logs (Induction Log &bull; Conflict Reflection)</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 44&ndash;47</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">180&ndash;220</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /15 ]</td></tr>
    <tr style="background:#fef2f2;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Criteria</strong></td><td style="border-bottom:1px solid #e2e8f0;">Self-Audit Rubrics, Glossary &amp; 22 Format Benchmark Keys</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 48&ndash;56</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Benchmark</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Verified</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 1</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 1: Incident Report &bull; Persuasive Article</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 57&ndash;63</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 2</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 2: Formal Letter &bull; Public Safety Leaflet</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 64&ndash;70</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 3</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 3: Technical Report &bull; Professional Review</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 71&ndash;77</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#f0fdf4;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Mock 4</strong></td><td style="border-bottom:1px solid #e2e8f0;">Official Mock 4: Strategy Email &bull; Persuasive Speech</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 78&ndash;84</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">30 Marks</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">[ &nbsp; /30 ]</td></tr>
    <tr style="background:#eff6ff;"><td style="padding:3px 6px; border-bottom:1px solid #e2e8f0;"><strong>Solutions</strong></td><td style="border-bottom:1px solid #e2e8f0;">Mock Benchmark Exemplars &amp; Final Readiness Sign-Off</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Pages 85&ndash;88</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Full Key</td><td style="text-align:center; border-bottom:1px solid #e2e8f0;">Signed</td></tr>
  </table>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:6px;">
    Master Functional Skills &bull; Level 2 Writing Practice Companion &bull; Page 3
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGES 4 TO 47: 11 FORMATS (44 Pages: orig_pages[2] to orig_pages[45])
    # -------------------------------------------------------------
    # In orig_pages: orig_pages[0] was cover, [1] was page 2.
    # orig_pages[2] to orig_pages[45] are the 44 format pages!
    for p_idx, p_content in enumerate(orig_pages[2:46], 4):
        # Update page background to warm cream
        p_clean = re.sub(r'(\.page\s*\{[^}]*background:\s*)#ffffff;', r'\1#FDFBF7;', p_content)
        p_clean = re.sub(r'style="([^"]*background:\s*)#ffffff', r'style="\1#FDFBF7', p_clean)
        # Update page number pill
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
         # Task 1: Incident Report
         ("Task 1: Workplace Incident & Safety Investigation Report (15 Marks)",
          "You are the Senior Logistics Team Leader at Apex Express Distribution Hub in Leeds. On Tuesday 14 October at 10:15 am, a serious near-miss and equipment collision occurred in Loading Bay C: a forklift truck (FLT-04) operated by an agency driver reversed into an unbolted racking bay, causing several pallets of consumer electronics to topple across the main transit walkway. A warehouse operative had to jump clear and sustained a sprained wrist.",
          "Write an official Workplace Incident & Safety Investigation Report to the Regional Operations Director, Ms Victoria Sterling.",
          ["A complete chronological timeline of what occurred before, during, and after the collision.",
           "An objective analysis of root causes (inadequate signage, blind spot, uncertified driver, unbolted racking).",
           "Details of immediate emergency first aid and floor clearance actions taken.",
           "At least four realistic corrective recommendations to prevent recurrence."]),
         # Task 2: Persuasive Article
         ("Task 2: Persuasive Article for Regional Business Journal (15 Marks)",
          "The Yorkshire Business Review is publishing a special feature on the future of vocational education. Many employers continue to complain about recruitment shortages, yet some business leaders argue that hiring apprentices is too expensive, time-consuming, and disruptive to short-term productivity.",
          "Write a persuasive, engaging article titled: 'Why Investing in Modern Apprenticeships is the Lifeline British Businesses Need'.",
          ["Challenge the misconception that apprenticeships are an unprofitable burden on employers.",
           "Highlight concrete commercial benefits (higher retention, tailored skillsets, government co-funding).",
           "Provide a compelling case study or practical examples of apprentices driving operational innovation.",
           "Conclude with a powerful call to action urging local businesses to commit to youth apprentice pledges."])),

        # Mock 2
        ("Mock Examination 2",
         # Task 1: Formal Letter
         ("Task 1: Formal Letter of Grievance & Demanded Rectification (15 Marks)",
          "You are the Chairperson of the Highfield Residents and Tenants Association in Birmingham. Over the past three months, residents in Highfield Towers (a 12-storey block with elderly and disabled residents) have experienced persistent failures by Sovereign Facilities Management: the main passenger elevator has been out of service for 18 days, the electronic security access gates are broken, and communal recycling bins have not been emptied for two consecutive weeks.",
          "Write a formal letter of grievance to the Managing Director of Sovereign Facilities Management, Mr Jonathan Vance.",
          ["Outline the specific maintenance failures with precise dates and severe impact on residents.",
           "Explain the safety, security, and fire hazard risks caused by the neglected repairs.",
           "Demand a binding, written schedule for immediate repairs and restoration of elevator access within 5 days.",
           "Request a formal apology and a proportionate rebate on communal service charges for affected residents."]),
         # Task 2: Public Safety Leaflet
         ("Task 2: Workplace Health & Wellbeing Information Leaflet (15 Marks)",
          "You are a Health and Safety Representative at St Jude's NHS Trust. Following an internal survey revealing high levels of physical fatigue and psychological burnout among rotational shift workers, management has asked you to produce an authoritative guidance leaflet to be distributed across all staff breakrooms.",
          "Draft the text for an information leaflet titled: 'Protecting Your Health & Energy: The Shift Worker's Essential Guide'.",
          ["An empathetic opening explaining why shift fatigue is a serious health and safety matter.",
           "Practical, actionable advice on sleep hygiene, circadian rhythm adjustment, and black-out rest routines.",
           "Guidance on healthy workplace nutrition, hydration, and avoiding excessive energy drinks.",
           "Details of occupational health support, confidential counseling, and quiet rest area facilities."])),

        # Mock 3
        ("Mock Examination 3",
         # Task 1: Technical Report
         ("Task 1: Technical Investigation & IT Feasibility Report (15 Marks)",
          "You are a Project Officer at Greenfield Financial Services. The company is planning to transition 120 client advisors to a permanent hybrid working model (2 days in the office, 3 days remote). However, an initial technical audit revealed that 40% of home workers experience unreliable broadband, personal laptops lack secure disk encryption, and client confidentiality protocols are vulnerable.",
          "Write an IT Feasibility and Compliance Report to the Chief Information Officer, Dr Marcus Thorne.",
          ["Analyze current technology and cybersecurity vulnerabilities identified in home setups.",
           "Evaluate the risks of non-compliance with UK GDPR and Data Protection regulations.",
           "Propose standard company-issued hardware packages (encrypted laptops, VPN tokens, headsets).",
           "Detail cost estimates, staff security training modules, and an implementation rollout schedule."]),
         # Task 2: Professional Review
         ("Task 2: Evaluative Professional Review for Hospitality Journal (15 Marks)",
          "You are an events management consultant writing for Commercial Venue Monthly. You recently attended a two-day national conference hosted at the newly opened 'Summit International Convention Centre' in Manchester. The venue boasts state-of-the-art facilities, but several delegates complained of sound bleed between seminar rooms and disorganized catering queues.",
          "Write an evaluative, balanced professional review of the Summit International Convention Centre.",
          ["A catchy headline and clear overall rating (e.g. 3.5 or 4 out of 5 stars).",
           "Detailed appraisal of conference facilities (audiovisual technology, seating, presentation stages).",
           "Critical analysis of weaknesses (acoustic issues, catering delays, elevator bottlenecks).",
           "A definitive verdict on what types of corporate events the venue is best suited for."])),

        # Mock 4
        ("Mock Examination 4",
         # Task 1: Strategic Email
         ("Task 1: Strategic Workplace Email to Executive Board (15 Marks)",
          "You are the Sustainability Lead at Meridian Retail Logistics. The executive board has invited staff proposals for the company's 'Net Zero 2030' strategy. Operating 45 diesel delivery vans and generating over 8 tons of single-use plastic packaging waste every month, the company faces growing criticism from corporate clients and rising fuel costs.",
          "Compose a formal workplace proposal email to Chief Executive Officer, Ms Elena Rostova.",
          ["A persuasive opening explaining why urgent sustainability action is commercially and ethically essential.",
           "Proposals for transitioning the delivery fleet to electric vehicles (EVs) with solar charging hubs.",
           "A concrete plan for replacing plastic wrap with biodegradable, reusable packaging materials.",
           "An overview of projected financial savings, tax incentives, and positive brand recognition."]),
         # Task 2: Persuasive Speech
         ("Task 2: Inspiring Persuasive Speech for Careers Assembly (15 Marks)",
          "You have been invited as a guest speaker at the West Midlands Adult Skills & Apprenticeship Fair. The audience consists of school leavers, career changers, and long-term jobseekers who feel anxious, underqualified, or discouraged by previous negative experiences in formal education.",
          "Write the complete script for an inspiring 5-minute persuasive speech titled: 'Unlocking Your Potential: Why Functional Skills & Continuous Learning Change Lives'.",
          ["An engaging opening using personal reflection or a powerful rhetorical question to connect with the audience.",
           "Emphasize that intelligence is not defined by past academic failures or standardized tests.",
           "Highlight real-life success stories of adults who mastered literacy and numeracy to achieve promotions.",
           "An inspiring, memorable call to action urging every attendee to take control of their future today."]))
    ]

    for m_idx, (m_title, (t1_name, t1_scenario, t1_task, t1_bullets), (t2_name, t2_scenario, t2_task, t2_bullets)) in enumerate(mock_specs, 1):
        m_start_pg = 57 + (m_idx - 1) * 7

        # PAGE 1: TASK 1 PROMPT & PLANNING SCAFFOLD
        bullets_t1_html = "".join([f"<li style='margin-bottom:3px;'>{b}</li>" for b in t1_bullets])
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Stimulus &amp; Planning</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <h2 style="color:#003366; margin:0; font-size:12.5pt;">{t1_name}</h2>
    <span style="background:#003366; color:#ffffff; padding:2px 8px; border-radius:4px; font-weight:700; font-size:7.5pt;">15 MARKS &bull; 30 MINS</span>
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 12px; border-radius:5px; margin-bottom:8px; font-size:8.3pt; line-height:1.42;">
    <strong>Scenario Stimulus:</strong> {t1_scenario}
    <p style="margin:5px 0 3px 0; font-weight:700; color:#003366;">{t1_task}</p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:8pt;">
      {bullets_t1_html}
    </ul>
  </div>

  <h3 style="color:#003366; margin:4px 0 2px 0; font-size:9pt;">Mandatory 5-Minute Planning Scaffold (4 Quadrants):</h3>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:6px;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[1] Audience &amp; Formal Tone:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[2] Structural Conventions Required:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[3] Key Factual Details &amp; Evidence:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[4] Advanced SPaG Target (Colons / Passive):</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
  </div>

  <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4px solid #d97706; padding:5px 8px; font-size:7.5pt;">
    <strong>Tutor Advice:</strong> Turn to <strong>Pages {m_start_pg+1} and {m_start_pg+2}</strong> to write your official candidate response. Aim for 200&ndash;250 words across the two ruled pages.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg}
  </div>
</div>
""")

        # PAGE 2: TASK 1 CANDIDATE RESPONSE SHEET (PART 1)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Candidate Response (Page 1 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#003366; font-size:9pt;">Task 1: Official Candidate Writing Space</strong>
    <span style="font-size:7.5pt; color:#64748b;">Target: ~120 words on this page</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:225mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+1}
  </div>
</div>
""")

        # PAGE 3: TASK 1 CANDIDATE RESPONSE SHEET (PART 2)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 1 Candidate Response (Page 2 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#003366; font-size:9pt;">Task 1: Conclusion &amp; Final Proofread</strong>
    <span style="font-size:7.5pt; color:#64748b;">Cumulative Word Count: ~220&ndash;250 words</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:190mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:6px 10px; margin-top:8px; font-size:7.5pt; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Task 1 Verification:</strong> [ &nbsp; ] All 4 prompts addressed &nbsp;&bull;&nbsp; [ &nbsp; ] Paragraph breaks clear &nbsp;&bull;&nbsp; [ &nbsp; ] Colons/semicolons verified</div>
    <div><strong>Word Count:</strong> ______</div>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+2}
  </div>
</div>
""")

        # PAGE 4: TASK 2 PROMPT & PLANNING SCAFFOLD
        bullets_t2_html = "".join([f"<li style='margin-bottom:3px;'>{b}</li>" for b in t2_bullets])
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Stimulus &amp; Planning</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <h2 style="color:#003366; margin:0; font-size:12.5pt;">{t2_name}</h2>
    <span style="background:#003366; color:#ffffff; padding:2px 8px; border-radius:4px; font-weight:700; font-size:7.5pt;">15 MARKS &bull; 30 MINS</span>
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 12px; border-radius:5px; margin-bottom:8px; font-size:8.3pt; line-height:1.42;">
    <strong>Scenario Stimulus:</strong> {t2_scenario}
    <p style="margin:5px 0 3px 0; font-weight:700; color:#003366;">{t2_task}</p>
    <ul style="margin:0 0 0 16px; padding:0; font-size:8pt;">
      {bullets_t2_html}
    </ul>
  </div>

  <h3 style="color:#003366; margin:4px 0 2px 0; font-size:9pt;">Mandatory 5-Minute Planning Scaffold (4 Quadrants):</h3>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:6px;">
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[1] Target Reader &amp; Purpose:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[2] Headline &amp; Subheading Plan:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[3] DAFOREST Devices to Include:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:6px 8px; font-size:7.5pt;">
      <strong style="color:#003366;">[4] Concluding Call to Action:</strong>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px; margin-top:2px;"></div>
      <div style="border-bottom:1px dashed #cbd5e1; height:18px;"></div>
    </div>
  </div>

  <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4px solid #d97706; padding:5px 8px; font-size:7.5pt;">
    <strong>Tutor Advice:</strong> Turn to <strong>Pages {m_start_pg+4} and {m_start_pg+5}</strong> to write your official candidate response. Ensure you demonstrate a persuasive, authoritative register.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+3}
  </div>
</div>
""")

        # PAGE 5: TASK 2 CANDIDATE RESPONSE SHEET (PART 1)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Candidate Response (Page 1 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#003366; font-size:9pt;">Task 2: Official Candidate Writing Space</strong>
    <span style="font-size:7.5pt; color:#64748b;">Target: ~120 words on this page</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:225mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+4}
  </div>
</div>
""")

        # PAGE 6: TASK 2 CANDIDATE RESPONSE SHEET (PART 2)
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Task 2 Candidate Response (Page 2 of 2)</div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
    <strong style="color:#003366; font-size:9pt;">Task 2: Climax, Action Call &amp; Proofread</strong>
    <span style="font-size:7.5pt; color:#64748b;">Cumulative Word Count: ~220&ndash;250 words</span>
  </div>

  <div style="background:repeating-linear-gradient(transparent, transparent 21px, #cbd5e1 21px, #cbd5e1 22px); border:1px solid #94a3b8; border-radius:5px; padding:10px 14px; min-height:190mm; line-height:22px; font-size:9pt;">
  </div>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:6px 10px; margin-top:8px; font-size:7.5pt; display:flex; justify-content:space-between; align-items:center;">
    <div><strong>Task 2 Verification:</strong> [ &nbsp; ] All bullet points met &nbsp;&bull;&nbsp; [ &nbsp; ] DAFOREST devices used &nbsp;&bull;&nbsp; [ &nbsp; ] Call to action included</div>
    <div><strong>Word Count:</strong> ______</div>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+5}
  </div>
</div>
""")

        # PAGE 7: PEER-AUDIT CHECKLIST & EXAMINER MARK SCHEME
        built_pages.append(f"""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; {m_title}</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Pearson Band 1&ndash;4 Examiner Audit</div>
  </div>

  <h2 style="color:#003366; margin:0 0 6px 0; font-size:13pt;">{m_title} &mdash; Candidate Peer-Audit &amp; Marking Rubric</h2>
  <p style="font-size:8pt; margin:0 0 8px 0;">Use this official Pearson-aligned diagnostic rubric to mark both tasks:</p>

  <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-bottom:8px;">
    <tr style="background:#003366; color:#ffffff;">
      <th style="padding:4px 6px; text-align:left; width:18%;">Mark Band</th>
      <th style="padding:4px 6px; text-align:left; width:52%;">Composition &amp; Purpose Descriptors (9 Marks)</th>
      <th style="padding:4px 6px; text-align:left; width:30%;">SPaG Standards (6 Marks)</th>
    </tr>
    <tr style="background:#f0fdf4;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 4 (Distinction)<br>Task Total: 13&ndash;15m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Highly persuasive or authoritative; exceptional audience adaptation; seamless paragraph cohesion; all prompts comprehensively developed; perfect layout.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Flawless sentence syntax; accurate colons/semicolons; ambitious vocabulary; near-zero spelling errors.</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 3 (Strong Pass)<br>Task Total: 9&ndash;12m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Clear register and purpose maintained throughout; logical paragraph flow; all prompts addressed with good supporting detail; appropriate format markers.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Correct sentence boundaries; commas and apostrophes used well; common workplace vocabulary correctly spelled.</td>
    </tr>
    <tr style="background:#fffbeb;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 2 (Borderline)<br>Task Total: 5&ndash;8m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">General awareness of purpose; some lapses in tone or formatting; paragraphs brief or uneven; 1&ndash;2 prompts omitted or superficial.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Comma splices or run-ons present; repeated spelling mistakes in irregular or multisyllabic words.</td>
    </tr>
    <tr style="background:#fef2f2;">
      <td style="padding:4px 6px; border:1px solid #cbd5e1;"><strong>Band 1 (Unclassified)<br>Task Total: 1&ndash;4m</strong></td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Little awareness of audience; inappropriate tone; lacks paragraphing or formatting; insufficient detail.</td>
      <td style="padding:4px 6px; border:1px solid #cbd5e1;">Frequent basic sentence boundary errors; simple punctuation missing; significant spelling breakdown.</td>
    </tr>
  </table>

  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:5px; padding:8px 12px; margin-bottom:8px;">
    <strong style="color:#003366; font-size:8.5pt;">Candidate Exam Score Summary:</strong>
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
    Functional Skills English Level 2 &bull; {m_title} &bull; Page {m_start_pg+6}
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGES 85 TO 87: BENCHMARK SOLUTIONS & MARK SCHEMES (3 Pages)
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; English Level 2</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Examiner Solutions &bull; Mocks 1 &amp; 2</div>
  </div>

  <h2 style="color:#003366; margin:0 0 6px 0; font-size:13pt;">Mock Exams 1 &amp; 2 &mdash; Band 4 Benchmark Solutions</h2>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 1 Task 1: Incident Report Benchmark (15/15)</strong><br>
    <strong>To:</strong> Victoria Sterling, Operations Director &bull; <strong>From:</strong> Senior Logistics Team Leader &bull; <strong>Date:</strong> 15 October 2026<br>
    <strong>Subject:</strong> Investigation Report: Forklift Collision &amp; Pallet Collapse in Loading Bay C<br>
    <strong>1. Executive Summary:</strong> On Tuesday 14 October at 10:15 am, FLT-04 collided with an unbolted racking upright, resulting in three collapsed pallets of electronics and a minor wrist injury to operative Mark Davies.<br>
    <strong>2. Root Cause Analysis:</strong> Investigation revealed three critical failures: first, the blind spot mirror at Bay C was misaligned; second, the agency driver had not completed site-specific induction; third, upright rack column anchors had been removed during electrical re-wiring last month and never re-bolted.<br>
    <strong>3. Immediate Actions:</strong> Area cordoned off; first aid applied; racking unloaded by certified senior operative.<br>
    <strong>4. Mandatory Corrective Recommendations:</strong> [1] Mandate site induction checks before FLT keys are issued; [2] Install optical collision sensors; [3] Complete immediate structural bolt audit across all bays; [4] Repaint high-visibility pedestrian boundaries.
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 1 Task 2: Persuasive Article Benchmark (15/15)</strong><br>
    <strong style="font-size:8pt;">Why Investing in Modern Apprenticeships is the Lifeline British Businesses Need</strong><br>
    In today's cut-throat commercial landscape, business leaders frequently lament an acute skills deficit. Yet, ironically, many still view hiring apprentices as an inconvenient cost center rather than a growth engine. It is time to dismantle this obsolete myth once and for all.<br>
    Far from being an unproductive drain, modern apprenticeships represent one of the highest-yielding investments available to UK enterprise. According to government data, 78% of employers report significant productivity surges after onboarding apprentices, while 74% observe improved staff retention. By shaping talent from the ground up, businesses instill company values and cultivate loyalty that external recruitment agencies simply cannot match.<br>
    Consider Apex Logistics in Leeds: by establishing an in-house supply chain academy, operational error rates plummeted by 32% within nine months. With substantial apprenticeship levy funding covering training costs, the economic argument is undeniable. British business stands at a pivotal crossroads: continue complaining about talent deficits, or invest in our youth and reap the commercial dividends.
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 2 Task 1: Formal Grievance Letter Benchmark (15/15)</strong><br>
    Standard address layout, 'Dear Mr Vance', 'Re: Urgent Safety &amp; Service Failures at Highfield Towers'. Chronological breakdown of 18 days elevator outage, security gate failure, and uncollected waste. Strict legal reference to landlord and tenant obligations, demanding restoration within 5 working days and service fee compensation. Signed 'Yours sincerely'.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; Examiner Solutions &bull; Page 85
  </div>
</div>
""")

    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; English Level 2</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Examiner Solutions &bull; Mocks 3 &amp; 4</div>
  </div>

  <h2 style="color:#003366; margin:0 0 6px 0; font-size:13pt;">Mock Exams 3 &amp; 4 &mdash; Band 4 Benchmark Solutions</h2>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 3 Task 1: IT Feasibility Report Benchmark (15/15)</strong><br>
    <strong>Title:</strong> Feasibility &amp; Compliance Audit: Hybrid Workplace IT Infrastructure &bull; <strong>To:</strong> Dr Marcus Thorne, CIO<br>
    <strong>Findings:</strong> 40% broadband latency, unencrypted personal devices violating GDPR, absence of multi-factor authentication (MFA).<br>
    <strong>Recommendations:</strong> Phased rollout of standardized Lenovo encrypted laptops; mandatory hardware VPN tokens; monthly cyber-hygiene webinars. Projected capital expenditure (£68,000) offset by 35% reduction in office overheads.
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 3 Task 2: Commercial Review Benchmark (15/15)</strong><br>
    <strong>Headline:</strong> "Summit Convention Centre: Cutting-Edge Tech Marred by Acoustic Oversights" (Rating: 3.5 / 5 Stars)<br>
    Pours praise on 4K digital projection, ergonomic seating, and high-speed Wi-Fi in the main auditorium. Critiques partition wall soundproofing and 25-minute luncheon queues. Concludes: ideal for tech product reveals, but unsuitable for multi-track simultaneous seminars until sound insulation is upgraded.
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; margin-bottom:8px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 4 Task 1: Strategic Sustainability Proposal Email (15/15)</strong><br>
    Professional greeting, 'Dear Ms Rostova', compelling carbon audit figures, 3-phase EV fleet transition proposal, replacement of plastic film with biodegradable starch polymers, payback period calculated at 2.4 years through fuel duty savings. Signed 'Kind regards, Sustainability Lead'.
  </div>

  <div class="card-exam" style="background:#faf5ff; border:1px solid #e9d5ff; border-left:4.5px solid #7c3aed; padding:8px 10px; border-radius:5px; font-size:7.5pt; line-height:1.4;">
    <strong style="color:#7c3aed; font-size:8pt;">Mock 4 Task 2: Inspiring Speech Benchmark (15/15)</strong><br>
    Engaging hook: <em>'How many times have you been told that your past defines your future?'</em> Emotive personal narrative of overcoming educational disadvantage; rhetorical triples (<em>'We are capable, we are resilient, we are unstoppable'</em>); persuasive facts on adult earnings; climactic standing ovation call to enroll today.
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; Examiner Solutions &bull; Page 86
  </div>
</div>
""")

    built_pages.append("""
<div class="page">
  <div class="page-header" style="border-bottom:2px solid #003366; padding-bottom:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
    <div style="font-weight:800; font-size:8pt; color:#003366; text-transform:uppercase;">Master Functional Skills &bull; English Level 2</div>
    <div style="font-size:7.5pt; color:#64748b; font-weight:700;">Final Readiness Verification</div>
  </div>

  <h2 style="color:#003366; margin:0 0 6px 0; font-size:13pt;">Master Level 2 Writing Readiness Verification</h2>
  <p style="font-size:8pt; margin:0 0 8px 0;">Review your comprehensive preparation before sitting your official Pearson exam:</p>

  <div class="grid-2" style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:8px;">
    <div class="card-method" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:4.5px solid #16a34a; padding:8px 12px; border-radius:5px; font-size:8pt;">
      <h3 style="color:#16a34a; margin:0 0 4px 0; font-size:9pt;">Skills Mastered Audit:</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.45;">
        <li>[ &nbsp; ] All 11 Writing Formats practiced</li>
        <li>[ &nbsp; ] 4 Practice Mock Papers completed</li>
        <li>[ &nbsp; ] 4-Quadrant planning used on every task</li>
        <li>[ &nbsp; ] Colons and semicolons used accurately</li>
        <li>[ &nbsp; ] Top 50 spelling words memorized</li>
        <li>[ &nbsp; ] 5-minute proofreading routine embedded</li>
      </ul>
    </div>

    <div class="card-tip" style="background:#fefce8; border:1px solid #fde68a; border-left:4.5px solid #d97706; padding:8px 12px; border-radius:5px; font-size:8pt;">
      <h3 style="color:#d97706; margin:0 0 4px 0; font-size:9pt;">Exam Day Golden Rules:</h3>
      <ul style="margin:0 0 0 14px; padding:0; line-height:1.45;">
        <li>Divide time evenly: 30 mins Task 1, 30 mins Task 2.</li>
        <li>Always write in the specified format (email headers, letter addresses, article titles).</li>
        <li>Do not write too little! Aim for 200&ndash;250 words per task.</li>
        <li>Keep your handwriting clear, legible, and dark.</li>
      </ul>
    </div>
  </div>

  <div class="card-practice" style="background:#ffffff; border:1.5px solid #003366; padding:10px 14px; border-radius:6px; margin-top:8px;">
    <h3 style="color:#003366; margin:0 0 6px 0; font-size:9.5pt;">Tutor Endorsement &amp; Exam Authorization</h3>
    <table style="width:100%; border-collapse:collapse; font-size:8pt; margin-top:4px;">
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1; width:35%;"><strong>Tutor / Assessor Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Assessor Signature:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Final Mock Exam Average:</strong></td><td style="border-bottom:1px solid #cbd5e1;">____ / 30 Marks</td></tr>
      <tr><td style="padding:4px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Exam Readiness:</strong></td><td style="border-bottom:1px solid #cbd5e1;">[ &nbsp; ] FULLY READY &nbsp;&bull;&nbsp; [ &nbsp; ] ADDITIONAL REVISION NEEDED</td></tr>
    </table>
  </div>

  <div style="margin-top:auto; font-size:7.5pt; color:#64748b; text-align:center; border-top:1px solid #e2e8f0; padding-top:4px;">
    Functional Skills English Level 2 &bull; Readiness Sign-Off &bull; Page 87
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 88: BACK COVER (FULL BLEED)
    # -------------------------------------------------------------
    built_pages.append("""
<div class="page cover-full-page" style="padding:0; background:#003366; justify-content:center; align-items:center;">
  <div style="width:180mm; border:3px solid #facc15; border-radius:12px; padding:32px 28px; text-align:center; background:#002244; color:#ffffff; box-shadow:0 10px 25px rgba(0,0,0,0.4);">
    <div style="font-size:12pt; color:#93c5fd; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;">
      Master Functional Skills &bull; Curriculum Edition
    </div>
    <h2 style="color:#ffffff; font-size:22pt; font-weight:900; line-height:1.25; margin:0 0 10px 0;">
      Everything You Need to Pass Functional Skills English Level 2 Writing
    </h2>
    <p style="font-size:10pt; color:#e2e8f0; line-height:1.45; margin:0 auto 16px auto; max-width:160mm;">
      Published by DarkNight Educational Press in partnership with the Master Functional Skills Learning Network. Designed strictly in accordance with Ofqual subject content regulations and British Dyslexia Association accessibility standards.
    </p>

    <div style="background:#0f172a; border-radius:6px; padding:12px 16px; margin:14px auto; font-size:8.5pt; color:#cbd5e1; text-align:left; line-height:1.5;">
      <strong>Why Learners &amp; Colleges Choose Our Workbooks:</strong>
      <ul style="margin:4px 0 0 16px; padding:0;">
        <li><strong>Zero Visual Fatigue:</strong> Accessible warm cream canvas (#FDFBF7) with Lexend typography.</li>
        <li><strong>Comprehensive Practice:</strong> 22 realistic writing drills covering all 11 examination formats.</li>
        <li><strong>Authentic Mock Exams:</strong> 4 full 30-mark practice papers with official Pearson marking rubrics.</li>
        <li><strong>Guaranteed Band 4 Progress:</strong> Full benchmark model answers with step-by-step examiner analysis.</li>
      </ul>
    </div>

    <div style="margin-top:18px; border-top:1px solid #1e3a8a; padding-top:10px; display:flex; justify-content:space-between; align-items:center; font-size:8pt; color:#94a3b8;">
      <div>
        <strong>Master Functional Skills</strong><br>
        masterfunctionalskills.co.uk
      </div>
      <div style="text-align:right;">
        <strong>ISBN:</strong> 978-1-912345-72-2<br>
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
<title>Pearson Edexcel Level 2 Functional Skills English - Writing Practice Companion (Master 88-Page Edition)</title>
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
    background: #003366 !important;
  }}
</style>
</head>
<body>
{''.join(built_pages)}
</body>
</html>"""

    return full_html, len(built_pages)

def build_english_l2_companion():
    html, page_divs = generate_l2_companion_html()
    print(f"[*] Generated HTML with {page_divs} page divs.")
    pdf_filename = "MasterFunctionalSkills_English_Writing_Level_2_Companion_Workbook.pdf"
    pages = render_book_to_pdf(html, pdf_filename)
    return pages

if __name__ == "__main__":
    build_english_l2_companion()
