#!/usr/bin/env python3
"""
build_english_e3.py
Compiles the complete 84-page Master Publication:
MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf

Mapped strictly to Ofqual Functional Skills English Entry Level 3 Subject Content.
Full CGP-style visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7),
Open Sans / Lexend typography, scaffolded writing frames, sentence starters,
vocabulary word banks, real workplace communication forms, Band 4 exemplars,
3 complete official-style mock exam papers, and comprehensive answer keys.
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import (
    SHARED_CSS, render_book_to_pdf, BOOKS_IMG_DIR
)

def build_english_e3_book():
    front_img = os.path.join(BOOKS_IMG_DIR, "english_e3_core_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "english_e3_core_cover_page-2.png")
    
    pages = []
    
    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>
""")

    # -------------------------------------------------------------
    # PAGE 2: INSIDE COVER & BLUEPRINT
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Candidate Blueprint &amp; Accessibility</div>
  </div>

  <h2>Welcome to Entry Level 3 Functional English (Master 84-Page Edition)</h2>
  <p>This comprehensive study handbook provides the step-by-step literacy foundations essential for everyday work, modern digital communication, and passing your accredited Entry Level 3 qualification. Every lesson is aligned strictly to Ofqual standards.</p>

  <div class="card-concept" style="border-left-color:#881337; background:#fff1f2;">
    <h3 style="color:#881337; margin-top:0;">Dyslexia-Friendly Architecture</h3>
    <p>We believe learning must be accessible and stress-free. This publication incorporates the British Dyslexia Association design recommendations:</p>
    <ul style="margin:4px 0 0 16px; padding:0;">
      <li><strong>Gentle Cream Canvas (#FDFBF7):</strong> Prevents visual glare and ocular fatigue common with bright bleached white paper.</li>
      <li><strong>Accessible Lexend &amp; Open Sans Typography:</strong> Specifically engineered to reduce visual distortion and increase character recognition.</li>
      <li><strong>Left-Aligned Ragged-Right Text:</strong> Never justified, ensuring predictable letter spacing without distracting white 'rivers'.</li>
      <li><strong>Visual Card Chunking:</strong> High-impact left-bordered cards highlight Rules, Models, Common Traps, and Golden Tips.</li>
    </ul>
  </div>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-method">
      <h3 style="color:#16a34a; margin-top:0;">The Two-Page Mastery Spread</h3>
      <p><strong>Left-Hand Study Page:</strong></p>
      <ul style="margin:2px 0 0 14px; padding:0; font-size:8pt;">
        <li>[A] Workplace Context &amp; Purpose</li>
        <li>[B] Visual Structural Formula &amp; Syntax</li>
        <li>[C] Correct vs Incorrect Worked Model</li>
        <li>[D] Watch Out Alert &amp; Memory Hook</li>
      </ul>
      <p style="margin-top:4px;"><strong>Right-Hand Practice Page:</strong> Graded multiple-choice recognition drills, sentence completion, and workplace writing practice.</p>
    </div>
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Candidate Registration</h3>
      <table style="width:100%; border-collapse:collapse; font-size:8pt; margin-top:4px;">
        <tr><td style="padding:5px; border-bottom:1px solid #cbd5e1;"><strong>Learner Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:5px; border-bottom:1px solid #cbd5e1;"><strong>Exam Centre:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:5px; border-bottom:1px solid #cbd5e1;"><strong>Target Date:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:5px; border-bottom:1px solid #cbd5e1;"><strong>Tutor Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
      </table>
      <div style="margin-top:8px; font-size:7.2pt; color:#64748b;">
        Master Functional Skills &bull; masterfunctionalskills.co.uk<br>
        Curriculum Edition &bull; Regulated by Ofqual
      </div>
    </div>
  </div>

  <div class="card-practice" style="margin-top:6px;">
    <h3 style="margin-top:0;">Entry Level 3 English Examination Scheme</h3>
    <div class="grid-2" style="margin-top:4px;">
      <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:6px 8px; border-radius:4px;">
        <strong>Component 1: Reading (45-60 Mins)</strong><br>
        Extracting facts from emails, letters, instructions, notices, and understanding organizational features.
      </div>
      <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:6px 8px; border-radius:4px;">
        <strong>Component 2: Writing (45-60 Mins)</strong><br>
        Task 1: Workplace note, incident log, or form.<br>
        Task 2: Structured email or letter (approx. 70–100 words).
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: CONTENTS & PROGRESS TRACKER
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Master Curriculum Map (84 Pages)</div>
  </div>

  <h2>Curriculum Contents &amp; Skills Audit</h2>
  <p>Follow the complete 84-page syllabus map below to build total literacy and exam mastery.</p>

  <table class="data-table" style="font-size:7pt; margin-top:2px;">
    <tr>
      <th style="width:14%;">Module</th>
      <th style="width:52%;">Curriculum Strand &amp; Topic Name</th>
      <th style="width:18%;">Page Range</th>
      <th style="width:16%;">Status</th>
    </tr>
    <tr><td><strong>Part 1</strong></td><td>Course Blueprint, Dyslexia Architecture &amp; Registration</td><td>Pages 1–3</td><td>Complete</td></tr>
    <tr><td><strong>Units 1–6</strong></td><td>Reading Foundation: Purpose, Features, Signs, Instructions, Alphabetical &amp; Facts</td><td>Pages 4–15</td><td>Core Study</td></tr>
    <tr><td><strong>Units 7–10</strong></td><td>Grammar &amp; Punctuation: Sentence Basics, MINTS Capitals, End Marks &amp; Commas</td><td>Pages 16–23</td><td>Core Study</td></tr>
    <tr><td><strong>Units 11–14</strong></td><td>Sentence Mastery: Compound Sentences, Complex Clauses, Verb Tenses &amp; Agreement</td><td>Pages 24–31</td><td>Core Study</td></tr>
    <tr><td><strong>Units 15–17</strong></td><td>Spelling &amp; Word Mechanics: Prefixes/Suffixes, Plurals, Homophones &amp; Top 100 Words</td><td>Pages 32–37</td><td>Core Study</td></tr>
    <tr><td><strong>Units 18–20</strong></td><td>Applied Workplace Literacy: Form Filling, Shift Logs &amp; Professional Emails</td><td>Pages 38–43</td><td>Core Study</td></tr>
    <tr style="background:#fef2f2;"><td><strong>Workshops 1–4</strong></td><td>Scaffolded Writing: Incident Form, Shift Handover, Leave Request, Customer Form</td><td>Pages 44–51</td><td>Applied Writing</td></tr>
    <tr style="background:#fef2f2;"><td><strong>Workshops 5–8</strong></td><td>Scaffolded Writing: Safety Notice, Formal Letter, Staff Leaflet, Service Review</td><td>Pages 52–59</td><td>Applied Writing</td></tr>
    <tr style="background:#f0fdf4;"><td><strong>Exemplars</strong></td><td>Band 4 Benchmark Exemplars &amp; Detailed Examiner Marking Commentary</td><td>Pages 60–63</td><td>Benchmarks</td></tr>
    <tr style="background:#fffbeb;"><td><strong>Reference</strong></td><td>Workplace Word Banks, Irregular Verb Tables &amp; Discourse Connectives</td><td>Pages 64–67</td><td>Master Banks</td></tr>
    <tr style="background:#f3e8ff;"><td><strong>Mock Exam 1</strong></td><td>Full Official Mock Paper 1 (Reading &amp; Writing Booklets)</td><td>Pages 68–71</td><td>Assessment</td></tr>
    <tr style="background:#f3e8ff;"><td><strong>Mock Exam 2</strong></td><td>Full Official Mock Paper 2 (Reading &amp; Writing Booklets)</td><td>Pages 72–75</td><td>Assessment</td></tr>
    <tr style="background:#f3e8ff;"><td><strong>Mock Exam 3</strong></td><td>Full Official Mock Paper 3 (Reading &amp; Writing Booklets)</td><td>Pages 76–79</td><td>Assessment</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Answer Keys</strong></td><td>Complete Step-by-Step Explanatory Answer Keys for All Units &amp; Mocks</td><td>Pages 80–83</td><td>Self-Check</td></tr>
    <tr><td><strong>Part 8</strong></td><td>Publisher Information &amp; Final Readiness Sign-Off</td><td>Page 84</td><td>Target Met</td></tr>
  </table>

  <div class="card-tip" style="margin-top:4px; font-size:7.8pt;">
    <strong>Tutor Study Tip:</strong> Practice writing with a black or dark blue pen on the lined worksheets. Remember that SPaG (Spelling, Punctuation, and Grammar) accounts for approximately 40% of marks in your writing paper.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
""")

    english_units_data = [
        # Unit 1
        ("Unit 1: Purpose of Texts (Instruct, Inform, Persuade)", "Reading: Understanding Text Types",
         """Every text is written with a specific intention. In Entry 3 reading tests, you must identify the main purpose:
         <ul style="margin:4px 0 0 16px;">
           <li><strong>To Inform:</strong> Gives neutral facts, details, and information (e.g. news reports, company memos, timetables).</li>
           <li><strong>To Instruct:</strong> Tells the reader how to do something step-by-step (e.g. fire escape instructions, recipes, user manuals).</li>
           <li><strong>To Persuade:</strong> Tries to convince you to buy, join, or agree with something (e.g. sales advertisements, charity appeals).</li>
           <li><strong>To Describe:</strong> Paints a picture in words using descriptive details.</li>
         </ul>""",
         """Look at the language cues:
         <ul style="margin:4px 0 0 16px;">
           <li>Imperative 'bossy' verbs (<em>Press, Turn, Exit, Wear</em>) &rarr; <strong>To Instruct</strong>.</li>
           <li>Dates, times, facts, contact emails &rarr; <strong>To Inform</strong>.</li>
           <li>Positive adjectives, offers, exclamation marks (<em>Best, Bargain, Hurry!</em>) &rarr; <strong>To Persuade</strong>.</li>
         </ul>""",
         "A notice on a warehouse staff room door reads: <em>'All staff must wear high-visibility vests and steel-toed boots when entering the loading bay. Anyone found without PPE will receive a warning.'</em> What is the primary purpose of this text?",
         """1. The notice uses direct rules ('must wear', 'entering', 'will receive a warning').<br>2. It gives clear workplace health and safety rules and instructions.<br><strong>Primary Purpose:</strong> To instruct staff on safety rules (or to inform them of safety regulations).""",
         "Don't confuse instructing with persuading. An advert persuades you to buy; a safety notice instructs you on rules.",
         "Look at the first few verbs. If they tell you what to do (imperative), the text is instructional.",
         [
           ("A poster says: <em>'50% off all winter jackets this weekend only! Don't miss out on London's best fashion deals.'</em> What is the main purpose of this text?<br>A) To instruct &nbsp;&nbsp; B) To persuade &nbsp;&nbsp; C) To complain", "[1 Mark]"),
           ("A leaflet title reads: <em>'How to assemble your new office desk in 5 easy steps.'</em> State the purpose of the text.", "[1 Mark]"),
           ("An email from HR confirms: <em>'The office will be closed on Bank Holiday Monday, 25 May. Normal hours resume Tuesday.'</em> What is the purpose of this email?", "[1 Mark]"),
           ("Explain how you can tell an advertisement is trying to persuade the reader.", "[2 Marks]")
         ]),

        # Unit 2
        ("Unit 2: Organisational & Presentation Features", "Reading: Text Features",
         """Organisational features are visual formatting elements that make texts simple to navigate and understand.""",
         """<strong>Key Features to Identify:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Headings &amp; Titles:</strong> Tell the reader what the entire text or document is about.</li>
           <li><strong>Subheadings:</strong> Divide the text into smaller, clear topic sections.</li>
           <li><strong>Bullet Points &amp; Numbered Lists:</strong> Break up complex instructions so steps can be followed easily.</li>
           <li><strong>Bold Text &amp; Italics:</strong> Highlight vital keywords, warnings, or dates.</li>
           <li><strong>Images, Diagrams &amp; Captions:</strong> Illustrate concepts and provide quick visual reference.</li>
         </ul>""",
         "Why has the author used <strong>bullet points</strong> in a fire safety policy notice?",
         """1. Bullet points break long chunks of text into individual, distinct items.<br>2. They allow employees to read emergency actions quickly without searching through dense paragraphs.<br><strong>Answer:</strong> To make key steps clear, distinct, and quick to follow during an emergency.""",
         "When asked why a feature is used, don't just say 'it looks nice'. Explain how it helps the READER (e.g. 'makes it easy to find information').",
         "Always connect the feature to the specific text: a bold date helps the reader remember an appointment deadline.",
         [
           ("Name two presentation features used to organise information on a webpage.", "[2 Marks]"),
           ("Why do authors use <strong>subheadings</strong> in informational leaflets?", "[1 Mark]"),
           ("A poster has the sentence: <em>'<strong>WARNING: DO NOT TOUCH SWITCHES WITH WET HANDS</strong>'</em> in bold capital letters. Why is bold text used here?", "[1 Mark]"),
           ("What is the purpose of an image caption underneath a photograph?", "[1 Mark]")
         ]),

        # Unit 3
        ("Unit 3: Reading Workplace Notices & Signs", "Reading: Everyday Workplace Texts",
         """Notices and signs convey essential instructions, hazards, and company updates in offices, hospitals, and construction sites.""",
         """<strong>How to Read a Notice Forensically:</strong>
         <ol style="margin:4px 0 0 16px;">
           <li>Read the <strong>main title</strong> to determine the subject matter.</li>
           <li>Scan for <strong>dates, times, and deadlines</strong>.</li>
           <li>Identify <strong>who</strong> the notice applies to (all staff, visitors, drivers).</li>
           <li>Note any <strong>action required</strong> (sign form, contact HR, change parking space).</li>
         </ol>""",
         """Read this staff notice:<br>
         <em>'Attention All Drivers: Resurfacing work will take place in Car Park B from Monday 12 October to Wednesday 14 October. Please park in Car Park C during this period. Normal parking resumes on Thursday.'</em><br>
         Where must drivers park on Tuesday 13 October?""",
         """1. Locate Tuesday 13 October in the dates: It falls between Mon 12 and Wed 14 October.<br>2. Read the action required during this period: 'Please park in Car Park C'.<br><strong>Answer: Car Park C</strong>.""",
         "Scan for exact keywords (e.g. Tuesday 13 October) rather than reading from word one. It saves time during exams.",
         "Make sure your answer directly quotes or reflects the exact detail from the text.",
         [
           ("A sign says: <em>'Visitors must sign in at Reception and wear a visitor pass at all times.'</em> What two things must visitors do?", "[2 Marks]"),
           ("A notice announces: <em>'First Aid training takes place in Room 4 on Friday at 2:00 pm. To book, email nurse@health.co.uk before 5 pm Wednesday.'</em> What is the booking deadline?", "[1 Mark]"),
           ("Which room will host the First Aid training?", "[1 Mark]"),
           ("Who should you contact to book a place?", "[1 Mark]")
         ]),

        # Unit 4
        ("Unit 4: Following Workplace Instructions", "Reading: Procedural Texts",
         """Instructions must be followed in strict sequential order. Missing a step can lead to safety hazards or operational errors.""",
         """<strong>Sequential Markers:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Chronological Words:</strong> <em>First, Next, Then, After that, Finally</em>.</li>
           <li><strong>Numbered Steps:</strong> Step 1, Step 2, Step 3 indicate the exact order of actions.</li>
           <li><strong>Conditional Warnings:</strong> Words like <em>Before, Make sure, Ensure, Never</em> tell you prerequisite conditions.</li>
         </ul>""",
         """Look at these sanitising instructions:<br>
         <em>'1. Rinse surface with warm water.<br>2. Spray antibacterial cleaner evenly.<br>3. Leave spray on surface for 60 seconds.<br>4. Wipe clean with a dry microfibre cloth.'</em><br>
         What must you do immediately before wiping the surface dry?""",
         """1. Locate the action: 'Wipe clean with a dry microfibre cloth' (Step 4).<br>2. Identify the step immediately BEFORE Step 4: Step 3.<br>3. Step 3 states: 'Leave spray on surface for 60 seconds.'<br><strong>Answer: Leave the antibacterial spray on the surface for 60 seconds</strong>.""",
         "Read carefully: questions asking what to do 'BEFORE' or 'AFTER' are common exam traps. Double check which direction in time you are looking.",
         "Underline time words like 'before', 'prior to', and 'subsequently'.",
         [
           ("In a printer manual, Step 1 is: <em>'Turn off power'</em>. Step 2 is: <em>'Open tray and clear jammed paper'</em>. Step 3 is: <em>'Close tray and restart power'</em>. What should you do before opening the paper tray?", "[1 Mark]"),
           ("Why are instructions presented in numbered steps instead of one large paragraph?", "[1 Mark]"),
           ("A recipe says: <em>'Preheat oven to 180°C before mixing the ingredients.'</em> When should the oven be switched on?", "[1 Mark]"),
           ("Write two imperative (bossy) verbs commonly found in workplace instructions.", "[2 Marks]")
         ]),

        # Unit 5
        ("Unit 5: Alphabetical Order & Dictionary Skills", "Reading: Vocabulary and Referencing",
         """Alphabetical order is essential for finding contact names in directories, filing client folders, and looking up words in dictionaries and glossaries.""",
         """<strong>Rules for Alphabetical Ordering:</strong>
         <ol style="margin:4px 0 0 16px;">
           <li>Look at the <strong>first letter</strong> of each word (e.g. <strong>A</strong>pple, <strong>B</strong>anana, <strong>C</strong>herry).</li>
           <li>If the first letters are identical, look at the <strong>second letter</strong> (e.g. B<strong>a</strong>ker, B<strong>e</strong>rry, B<strong>o</strong>at).</li>
           <li>If the second letters are also the same, look at the <strong>third letter</strong> (e.g. Ca<strong>b</strong>le, Ca<strong>m</strong>p, Ca<strong>r</strong>t).</li>
           <li><strong>Dictionary Guide Words:</strong> The words at the top of a dictionary page show the first and last word on that page.</li>
         </ol>""",
         "Put these four employee surnames in alphabetical order: <strong>Davies, Daniels, Dixon, Dawson</strong>.",
         """1. All four start with 'D'. Compare second letters: a, a, i, a.<br>2. Three start with 'Da': Davies, Daniels, Dawson.<br>3. Compare third letters for 'Da':<br>&nbsp;&nbsp;&bull; Dani... ('n' is 14th letter)<br>&nbsp;&nbsp;&bull; Davi... ('v' is 22nd letter)<br>&nbsp;&nbsp;&bull; Daws... ('w' is 23rd letter)<br>4. Therefore: Daniels, Davies, Dawson.<br>5. Dixon has 'i' as second letter, which comes after 'a'.<br><strong>Final Alphabetical Order:</strong> Daniels, Davies, Dawson, Dixon.""",
         "Sing the alphabet in your head if you get stuck on letter positions: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.",
         "Double-check identical prefixes carefully: 'Clark' comes before 'Clarke'.",
         [
           ("Put these four job titles in alphabetical order: a) Electrician &nbsp;&nbsp; b) Carpenter &nbsp;&nbsp; c) Plumber &nbsp;&nbsp; d) Builder", "[2 Marks]"),
           ("Put these towns in alphabetical order: Bolton, Bristol, Bath, Birmingham.", "[2 Marks]"),
           ("A dictionary page has guide words <strong>Market &ndash; Metal</strong>. Which word would appear on this page: a) Map &nbsp;&nbsp; b) Match &nbsp;&nbsp; c) Modern?", "[1 Mark]"),
           ("What is the purpose of a glossary at the back of a training textbook?", "[1 Mark]")
         ]),

        # Unit 6
        ("Unit 6: Extracting Facts & Comparing Two Texts", "Reading: Comparative Analysis",
         """In Entry Level 3 reading exams, you will be given two short texts on the same topic (e.g. two gym adverts, or an email and an announcement) and asked to extract facts and compare them.""",
         """<strong>Comparative Reading Technique:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Fact vs Opinion:</strong> A fact can be proven true or false with evidence (e.g. 'The course lasts 6 weeks'). An opinion is a personal belief or feeling (e.g. 'It is a wonderful course').</li>
           <li><strong>Finding Similarities:</strong> Look for information that appears in BOTH texts (e.g. both offer free parking).</li>
           <li><strong>Finding Differences:</strong> Look for contrasting details (e.g. Text A opens at 8 am, but Text B opens at 7 am).</li>
         </ul>""",
         """Text A says: <em>'Peak Fitness is open 7 days a week from 6 am to 10 pm. Membership is £25 per month.'</em><br>
         Text B says: <em>'City Gym charges £20 a month and is open Monday to Friday from 7 am to 9 pm.'</em><br>
         Give one way the two gyms are different regarding opening hours.""",
         """1. Text A opening: Open 7 days a week (weekends included), 6 am to 10 pm.<br>2. Text B opening: Open only Monday to Friday (5 days), 7 am to 9 pm.<br><strong>Answer:</strong> Peak Fitness is open at weekends and opens earlier/closes later than City Gym.""",
         "Always name WHICH text you are talking about in your comparative answers (e.g. 'Text A is £25 whereas Text B is £20').",
         "Make sure you answer the exact aspect asked: if asked about opening times, do not write about prices.",
         [
           ("Identify whether each statement is a Fact or an Opinion:<br>a) 'The store opened in 2018.'<br>b) 'The store has the friendliest staff in the city.'", "[2 Marks]"),
           ("Using the gym texts in the example above, which gym is cheaper per month?", "[1 Mark]"),
           ("Give one piece of information about opening times that is different between the two gyms.", "[1 Mark]"),
           ("Why is it important to check facts from more than one source?", "[1 Mark]")
         ]),

        # Unit 7
        ("Unit 7: Sentence Basics: Subject, Verb & Object", "Writing: Sentence Mechanics",
         """A complete sentence must make complete sense on its own. Every standard English sentence requires a <strong>Subject</strong> (who or what does the action) and a <strong>Verb</strong> (the action or state).""",
         """<strong>The Core Sentence Formula:</strong>
         <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:6px 10px; border-radius:4px; margin:4px 0; font-family:'JetBrains Mono',monospace; font-size:8pt;">
           [Subject] + [Verb] + [Object / Complement]<br>
           e.g. [The manager] + [inspected] + [the warehouse].
         </div>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Subject:</strong> The person, place, or thing performing the action.</li>
           <li><strong>Verb:</strong> The action or state of being (<em>walked, operates, is, has</em>).</li>
           <li><strong>Sentence Fragment Trap:</strong> A group of words lacking a subject or main verb (e.g. <em>'Working on the engine.'</em> &mdash; who is working?).</li>
         </ul>""",
         "Identify the Subject, Verb, and Object in the sentence: <em>'Sarah repaired the broken printer.'</em>",
         """1. Who did the action? <strong>Sarah</strong> &rarr; Subject.<br>2. What action did she do? <strong>repaired</strong> &rarr; Verb.<br>3. What received the action? <strong>the broken printer</strong> &rarr; Object.<br><strong>Answer:</strong> Subject: Sarah | Verb: repaired | Object: the broken printer.""",
         "Never leave a sentence fragment alone in formal writing. Make sure every sentence has a clear subject and a finite verb.",
         "Read your sentence aloud in your head. If it feels unfinished, it is probably a fragment missing a verb.",
         [
           ("Identify the verb in each sentence:<br>a) The mechanic tested the brakes.<br>b) We ordered new stationery yesterday.", "[2 Marks]"),
           ("Which of these is a complete sentence?<br>A) Waiting outside the office for the bus.<br>B) The manager called a team meeting.<br>C) Because the weather was cold.", "[1 Mark]"),
           ("Add a subject to complete this sentence: <em>'__________ inspected the fire alarms this morning.'</em>", "[1 Mark]"),
           ("Write a complete sentence about your workplace or college containing a subject, verb, and object.", "[2 Marks]")
         ]),

        # Unit 8
        ("Unit 8: Capital Letters: The MINTS Rule", "Writing: Punctuation Mastery",
         """Capital letters mark sentence boundaries and identify proper nouns (specific names). Missing capital letters is the single most common error penalized in Entry 3 exams.""",
         """<strong>The MINTS Memory Rule for Capital Letters:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>M &rarr; Months &amp; Days:</strong> <em>January, August, Monday, Friday</em>. (Note: seasons like summer are lower case).</li>
           <li><strong>I &rarr; Personal Pronoun 'I':</strong> Always a capital letter when referring to yourself (<em>'Yesterday I visited...'</em>).</li>
           <li><strong>N &rarr; Names of People &amp; Places:</strong> <em>David, Maria, Leeds, Manchester, Thames</em>.</li>
           <li><strong>T &rarr; Titles &amp; Brands:</strong> <em>Mr, Mrs, Dr, Queen Street, Tesco, Apple, Microsoft</em>.</li>
           <li><strong>S &rarr; Start of every sentence:</strong> The very first letter after a full stop or question mark.</li>
         </ul>""",
         "Correct all capital letter errors in: <em>'on friday i travelled to manchester with mr ahmed.'</em>",
         """1. 'on' &rarr; <strong>On</strong> (Start of sentence).<br>2. 'friday' &rarr; <strong>Friday</strong> (Day of the week).<br>3. 'i' &rarr; <strong>I</strong> (Pronoun).<br>4. 'manchester' &rarr; <strong>Manchester</strong> (Place name).<br>5. 'mr ahmed' &rarr; <strong>Mr Ahmed</strong> (Title and surname).<br><strong>Corrected:</strong> <em>'On Friday, I travelled to Manchester with Mr Ahmed.'</em>""",
         "Never write the pronoun 'i' as a lowercase letter in English! It is ALWAYS capital 'I'.",
         "Job titles like 'manager' or 'nurse' are lowercase unless part of an official name (e.g. Manager John).",
         [
           ("Rewrite these sentences with correct capital letters:<br>a) in september i will start my apprenticeship in leeds.<br>b) mrs green met amir on thursday morning.", "[4 Marks]"),
           ("Which word in this sentence requires a capital letter?<br><em>'We will travel to london by train next week.'</em>", "[1 Mark]"),
           ("List the 7 days of the week, ensuring each begins with a capital letter.", "[2 Marks]"),
           ("Explain what the letter 'N' stands for in the MINTS memory rule.", "[1 Mark]")
         ]),

        # Unit 9
        ("Unit 9: Full Stops, Question Marks & Exclamations", "Writing: Punctuation Mastery",
         """Every sentence must finish with an appropriate terminal punctuation mark. The choice of mark determines how the reader interprets the tone and function of your writing.""",
         """<strong>The 3 Terminal Punctuation Marks:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Full Stop (.) :</strong> Used at the end of a statement that conveys information or fact (e.g. <em>'The shift starts at 8 am.'</em>).</li>
           <li><strong>Question Mark (?) :</strong> Used at the end of a direct inquiry asking for information (e.g. <em>'Where is the First Aid kit?'</em>).</li>
           <li><strong>Exclamation Mark (!) :</strong> Used to show urgency, danger, strong emotion, or surprise (e.g. <em>'Stop immediately!'</em>). Use sparingly in formal writing.</li>
         </ul>""",
         "Add the correct punctuation mark to the end of each sentence:<br>a) Can you work overtime this Saturday<br>b) The store delivers groceries between 9 am and 1 pm<br>c) Watch out for that wet floor",
         """a) This is a direct inquiry &rarr; <strong>Question Mark (?)</strong>: <em>'Can you work overtime this Saturday?'</em><br>b) This is a factual statement &rarr; <strong>Full Stop (.)</strong>: <em>'The store delivers groceries between 9 am and 1 pm.'</em><br>c) This is an urgent safety warning &rarr; <strong>Exclamation Mark (!)</strong>: <em>'Watch out for that wet floor!'</em>""",
         "Don't put a question mark on indirect questions! <em>'He asked if I could work.'</em> is a statement and ends with a full stop.",
         "Avoid multiple exclamation marks (!!!) in functional writing. One mark is sufficient.",
         [
           ("Insert the correct punctuation mark at the end of each sentence:<br>a) When does the morning delivery arrive<br>b) The invoice was paid yesterday<br>c) What time does your train depart", "[3 Marks]"),
           ("Rewrite this short workplace note with full stops and capital letters in the correct places:<br><em>'the meeting finished late amir called his supervisor to explain the delay'</em>", "[2 Marks]"),
           ("Why is an exclamation mark suitable for a hazard warning sign?", "[1 Mark]"),
           ("Write one question asking your tutor about an upcoming assessment.", "[1 Mark]")
         ]),

        # Unit 10
        ("Unit 10: Commas in Lists & Introductory Words", "Writing: Punctuation Mastery",
         """Commas provide brief pauses within a sentence, preventing words from running together and clarifying meaning.""",
         """<strong>Two Essential Uses at Entry Level 3:</strong>
         <ol style="margin:4px 0 0 16px;">
           <li><strong>Commas in Lists:</strong> Separate three or more items in a series. Use a comma between items, and use <strong>'and'</strong> before the final item. (e.g. <em>'Please bring a notebook, a pen, a calculator and your ID badge.'</em>).</li>
           <li><strong>Commas After Time / Introductory Openers:</strong> Placed after introductory words at the start of a sentence (e.g. <em>'Yesterday, we completed the audit.'</em> &bull; <em>'However, the server was down.'</em>).</li>
         </ol>""",
         "Insert commas where needed in this sentence: <em>'At the depot we handle parcels letters packages and freight.'</em>",
         """1. Introductory time/place phrase: 'At the depot,' needs a comma.<br>2. List items: 'parcels, letters, packages and freight'.<br><strong>Corrected sentence:</strong> <em>'At the depot, we handle parcels, letters, packages and freight.'</em>""",
         "Do not put a comma before the first item in a list, or after the word 'and' in a simple list.",
         "Rule: Item 1, Item 2, Item 3 and Item 4. Never put a comma after the final item.",
         [
           ("Insert commas in the list: <em>'The technician brought screwdrivers pliers a drill and spare batteries.'</em>", "[2 Marks]"),
           ("Add a comma after the introductory word/phrase in each sentence:<br>a) Last Friday we held a fire drill.<br>b) Fortunately the client signed the contract.", "[2 Marks]"),
           ("Explain why commas are needed when listing several ingredients in a recipe.", "[1 Mark]"),
           ("Write a sentence listing four items you use regularly at work or college.", "[2 Marks]")
         ]),

        # Unit 11
        ("Unit 11: Compound Sentences (and, but, or, so)", "Writing: Sentence Building",
         """A compound sentence joins two independent clauses (complete thoughts that could each stand alone as a sentence) using a coordinating conjunction: <strong>FANBOYS</strong> (most commonly: <em>and, but, or, so</em>).""",
         """<strong>The Conjunction Toolkit:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>and:</strong> Adds similar information (e.g. <em>'I finished the report, and I emailed it to the director.'</em>).</li>
           <li><strong>but:</strong> Shows contrast or unexpected difference (e.g. <em>'I applied for the role, but I have not heard back yet.'</em>).</li>
           <li><strong>or:</strong> Presents an alternative or choice (e.g. <em>'You can pay by card, or you can pay with cash.'</em>).</li>
           <li><strong>so:</strong> Shows a result or consequence (e.g. <em>'The road was flooded, so we took a detour.'</em>).</li>
         </ul>""",
         "Join these two simple sentences using <strong>'so'</strong>: <em>'The printer was out of paper. We could not print the delivery notes.'</em>",
         """1. Identify the cause: The printer was out of paper.<br>2. Identify the result: We could not print the delivery notes.<br>3. Connect with 'so': <em>'The printer was out of paper, <strong>so</strong> we could not print the delivery notes.'</em>""",
         "Don't start every sentence with 'And' or 'But' in formal writing. Use them to link related clauses.",
         "Check both halves of your sentence: each side of 'and', 'but', or 'so' should make sense by itself.",
         [
           ("Join these simple sentences using <strong>'but'</strong>:<br><em>'Mark wanted to attend the training course. He was scheduled on shift.'</em>", "[2 Marks]"),
           ("Choose the correct conjunction (and / but / or / so):<br>a) The office was cold, _____ we switched on the heater.<br>b) Would you prefer tea, _____ would you like coffee?", "[2 Marks]"),
           ("Combine into a compound sentence using <strong>'and'</strong>:<br><em>'Sophie answered customer calls. She logged complaints on the database.'</em>", "[2 Marks]"),
           ("Explain the difference between using 'and' and using 'but'.", "[1 Mark]")
         ]),

        # Unit 12
        ("Unit 12: Complex Sentences (because, although, if)", "Writing: Sentence Building",
         """A complex sentence connects an independent clause (main clause) with a subordinate clause (dependent clause) that cannot stand alone, using subordinating conjunctions like <strong>because, although, if, when, while</strong>.""",
         """<strong>Subordinating Conjunction Functions:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>because:</strong> Gives the reason or explanation (e.g. <em>'The train was delayed <strong>because</strong> there was ice on the track.'</em>).</li>
           <li><strong>although:</strong> Concedes a contrasting fact (e.g. <em>'We completed the audit on time, <strong>although</strong> we were short-staffed.'</em>).</li>
           <li><strong>if:</strong> States a condition (e.g. <em>'<strong>If</strong> you need assistance, please ring the reception bell.'</em>).</li>
           <li><strong>when:</strong> Establishes a time relationship (e.g. <em>'<strong>When</strong> the alarm sounds, exit via the nearest staircase.'</em>).</li>
         </ul>""",
         "Combine these clauses using <strong>'because'</strong>: <em>'The team celebrated. They achieved their monthly sales target.'</em>",
         """1. The second clause provides the reason for the celebration.<br>2. Link with 'because': <em>'The team celebrated <strong>because</strong> they achieved their monthly sales target.'</em><br>(Note: When the conjunction is in the middle, a comma is usually not needed).""",
         "If you start a sentence with 'Although' or 'Because', you MUST put a comma between the subordinate clause and the main clause.",
         "Never write 'Because of the delay.' as a sentence by itself &mdash; it must connect to a main clause.",
         [
           ("Join these sentences using <strong>'because'</strong>:<br><em>'The customer requested a refund. The item was damaged during transit.'</em>", "[2 Marks]"),
           ("Complete the sentence with an appropriate ending:<br><em>'If you cannot attend tomorrow's appointment, ____________________.'</em>", "[2 Marks]"),
           ("Which conjunction best connects these clauses: (Although / Because / If)?<br><em>'__________ it was raining heavily, the construction team continued working.'</em>", "[1 Mark]"),
           ("Write one complex sentence explaining why you want to achieve your Functional Skills qualification.", "[2 Marks]")
         ]),

        # Unit 13
        ("Unit 13: Verb Tenses: Present vs Past Simple", "Writing: Grammar and Tenses",
         """Verb tense tells the reader WHEN an action happened. Writing must remain consistent in tense: do not jump between past and present without reason.""",
         """<strong>Regular vs Irregular Past Tense Verbs:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Present Simple (Happening now or regularly):</strong> <em>work, inspect, write, deliver, see</em>.</li>
           <li><strong>Regular Past (Add -ed or -d):</strong> <em>worked, inspected, delivered, checked, printed</em>.</li>
           <li><strong>Irregular Past (Changes spelling completely):</strong>
             <br>&bull; <em>write &rarr; wrote</em> &nbsp;&bull; <em>see &rarr; saw</em> &nbsp;&bull; <em>go &rarr; went</em> &nbsp;&bull; <em>take &rarr; took</em> &nbsp;&bull; <em>buy &rarr; bought</em>
           </li>
         </ul>""",
         "Correct the verb tense error in this workplace log: <em>'Yesterday morning, I arrive at the warehouse and inspected the delivery pallets.'</em>",
         """1. The time marker 'Yesterday morning' specifies the past.<br>2. 'inspected' is already in past tense.<br>3. 'arrive' is present tense and must be changed to past tense ('arrived').<br><strong>Corrected:</strong> <em>'Yesterday morning, I <strong>arrived</strong> at the warehouse and inspected the delivery pallets.'</em>""",
         "Watch out for irregular past verbs! Never write 'goed' (went), 'writed' (wrote), or 'buyed' (bought).",
         "Maintain consistent tense across paragraphs in emails and incident reports.",
         [
           ("Write the past tense form of these regular verbs: a) check &nbsp;&nbsp; b) repair &nbsp;&nbsp; c) clean", "[3 Marks]"),
           ("Write the past tense form of these irregular verbs: a) speak &nbsp;&nbsp; b) write &nbsp;&nbsp; c) give", "[3 Marks]"),
           ("Identify and correct the tense error in this sentence: <em>'Last week the technician fix the broken photocopier.'</em>", "[2 Marks]"),
           ("Rewrite in the past tense: <em>'I send the email to the manager.'</em>", "[1 Mark]")
         ]),

        # Unit 14
        ("Unit 14: Subject-Verb Agreement", "Writing: Grammar and Tenses",
         """A singular subject requires a singular verb; a plural subject requires a plural verb. Errors in subject-verb agreement make writing look unprofessional and are strictly checked by examiners.""",
         """<strong>Agreement Rules to Remember:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Singular (He, She, It, The worker):</strong>
             <br>&bull; <em>The worker <strong>is</strong>...</em> &bull; <em>The worker <strong>was</strong>...</em> &bull; <em>The worker <strong>has</strong>...</em> &bull; <em>The worker <strong>operates</strong>...</em>
           </li>
           <li><strong>Plural (They, We, The workers):</strong>
             <br>&bull; <em>The workers <strong>are</strong>...</em> &bull; <em>The workers <strong>were</strong>...</em> &bull; <em>The workers <strong>have</strong>...</em> &bull; <em>The workers <strong>operate</strong>...</em>
           </li>
           <li><strong>The Pronoun 'You':</strong> Always takes plural verb forms (<em>'You are', 'You were'</em> &mdash; NEVER <em>'You was'</em>).</li>
         </ul>""",
         "Choose the correct verb in brackets: <em>'The parcels (was / were) loaded onto the delivery van.'</em>",
         """1. Identify the subject: 'The parcels'.<br>2. 'The parcels' is plural (more than one parcel).<br>3. Plural subject takes the plural verb 'were'.<br><strong>Correct sentence:</strong> <em>'The parcels <strong>were</strong> loaded onto the delivery van.'</em>""",
         "Common dialect trap: <em>'We was happy'</em> or <em>'You was there'</em>. In standard English, always write <strong>'We were'</strong> and <strong>'You were'</strong>.",
         "Check the subject carefully when words come between it and the verb: <em>'The box of spare parts is (not are) heavy.'</em>",
         [
           ("Select the correct verb for each sentence:<br>a) The new apprentices (is / are) eager to learn.<br>b) My supervisor (has / have) approved my holiday request.<br>c) We (was / were) working late yesterday.", "[3 Marks]"),
           ("Correct the error in this sentence: <em>'The manager and the receptionist was discussing the rota.'</em>", "[2 Marks]"),
           ("Write a sentence about your colleagues using the verb 'were'.", "[1 Mark]"),
           ("Explain why <em>'She don't know the answer'</em> is non-standard English.", "[1 Mark]")
         ]),

        # Unit 15
        ("Unit 15: Prefixes & Suffixes", "Writing: Spelling and Word Roots",
         """A <strong>prefix</strong> is added to the beginning of a root word to alter its meaning (often creating an opposite). A <strong>suffix</strong> is added to the end to change its tense or word class.""",
         """<strong>Key Prefixes &amp; Suffixes at Entry 3:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Prefixes (Opposites):</strong>
             <br>&bull; <strong>un-</strong> (<em>unhappy, unfair, unplug</em>)
             <br>&bull; <strong>dis-</strong> (<em>disagree, disconnect, disappear</em>)
             <br>&bull; <strong>re-</strong> (means again: <em>restart, rebuild, resend</em>)
           </li>
           <li><strong>Suffixes:</strong>
             <br>&bull; <strong>-ful</strong> (full of: <em>helpful, careful</em> &mdash; note: single 'l')
             <br>&bull; <strong>-less</strong> (without: <em>careless, helpless</em>)
             <br>&bull; <strong>-ly</strong> (turns adjectives to adverbs: <em>quick &rarr; quickly, clear &rarr; clearly</em>)
             <br>&bull; <strong>-ing / -ed</strong> (verb endings: <em>training, trained</em>)
           </li>
         </ul>""",
         "Add the correct prefix or suffix to complete the sentences:<br>a) The technician had to (build) _______ the broken shelving.<br>b) Please drive (care) _______ in the icy conditions.",
         """a) Doing the action again &rarr; Prefix <strong>re-</strong>: <em>rebuild</em>.<br>b) Doing the action with care &rarr; Suffixes <strong>-ful</strong> + <strong>-ly</strong>: <em>carefully</em>.<br><strong>Answers:</strong> a) rebuild &nbsp;&nbsp; b) carefully.""",
         "The suffix '-ful' only has ONE 'l'! Write <em>careful</em>, <em>grateful</em>, <em>peaceful</em>. Never write 'carefull'.",
         "When adding '-ly' to an adjective ending in 'y' (e.g. happy), change the 'y' to 'i': <em>happily</em>.",
         [
           ("Add the prefix 'un-' or 'dis-' to create opposites: a) agree &nbsp;&nbsp; b) certain &nbsp;&nbsp; c) connect", "[3 Marks]"),
           ("Add '-ful' or '-less' to the root word: a) help (with plenty of assistance) &nbsp;&nbsp; b) hope (without hope)", "[2 Marks]"),
           ("Turn these adjectives into adverbs by adding '-ly': a) slow &nbsp;&nbsp; b) safe &nbsp;&nbsp; c) easy", "[3 Marks]"),
           ("Correct the spelling error: <em>'The staff were very successfull in meeting the deadline.'</em>", "[1 Mark]")
         ]),

        # Unit 16
        ("Unit 16: Plural Rules & Tricky Homophones", "Writing: Spelling and Word Roots",
         """Plural words indicate more than one. Homophones are words that sound identical when spoken but have different spellings and meanings.""",
         """<strong>Plural Spelling Rules:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Most words:</strong> Add <strong>-s</strong> (<em>tool &rarr; tools, desk &rarr; desks</em>).</li>
           <li><strong>Words ending in -s, -ss, -sh, -ch, -x:</strong> Add <strong>-es</strong> (<em>box &rarr; boxes, watch &rarr; watches</em>).</li>
           <li><strong>Words ending in consonant + y:</strong> Change 'y' to <strong>-ies</strong> (<em>lorry &rarr; lorries, company &rarr; companies</em>).</li>
         </ul>
         <strong>Tricky Homophones:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>There / Their / They're:</strong> <em>There</em> = place (over there). <em>Their</em> = belonging to them (their tools). <em>They're</em> = contraction of they are.</li>
           <li><strong>To / Too / Two:</strong> <em>To</em> = direction (go to work). <em>Too</em> = also / excessively (too hot). <em>Two</em> = number 2.</li>
         </ul>""",
         "Fill in the correct homophones (there / their / they're):<br><em>'The engineers left _______ tools over _______ because _______ leaving early.'</em>",
         """1. First blank: belonging to the engineers &rarr; <strong>their</strong>.<br>2. Second blank: location / place &rarr; <strong>there</strong>.<br>3. Third blank: short for 'they are' &rarr; <strong>they're</strong>.<br><strong>Answer:</strong> <em>'The engineers left <strong>their</strong> tools over <strong>there</strong> because <strong>they're</strong> leaving early.'</em>""",
         "Never write 'there' when you mean 'their' belonging! Remember: t-HEIR has 'heir' (person who owns property).",
         "For plurals of words ending in a vowel + y (e.g. boy, day), just add 's': <em>boys, days</em>. Don't change to 'ies'.",
         [
           ("Write the plural form of each noun: a) church &nbsp;&nbsp; b) factory &nbsp;&nbsp; c) parcel", "[3 Marks]"),
           ("Choose the correct homophone in brackets:<br>a) Please send the invoice (to / too / two) the finance office.<br>b) The room was (to / too / two) noisy for the meeting.<br>c) We ordered (to / too / two) new monitors.", "[3 Marks]"),
           ("Correct the homophone error in: <em>'The drivers checked there mirrors before reversing.'</em>", "[1 Mark]"),
           ("Explain the difference between 'here' and 'hear'.", "[1 Mark]")
         ]),

        # Unit 17
        ("Unit 17: Top 100 Workplace Spelling Words", "Writing: Spelling Mastery",
         """Ofqual Entry Level 3 Functional English requires accurate spelling of high-frequency everyday workplace words.""",
         """<strong>The Look-Say-Cover-Write-Check Technique:</strong>
         <ol style="margin:4px 0 0 16px;">
           <li><strong>LOOK:</strong> Study the word's letter patterns and tricky spots (e.g. double letters in <em>co<strong>mm</strong>u<strong>ni</strong>cation</em>).</li>
           <li><strong>SAY:</strong> Pronounce each syllable clearly (<em>ap-point-ment</em>).</li>
           <li><strong>COVER:</strong> Hide the word completely from sight.</li>
           <li><strong>WRITE:</strong> Write the word from memory.</li>
           <li><strong>CHECK:</strong> Compare letter by letter. Repeat if an error occurred.</li>
         </ol>""",
         "Identify the misspelled word and provide the correct spelling: <em>'Please confirm your attendence at tomorrow's health and safety breifing.'</em>",
         """1. 'attendence' &rarr; Incorrect ending. The correct suffix is <strong>-ance</strong> &rarr; <strong>attendance</strong>.<br>2. 'breifing' &rarr; Violates the 'i before e except after c' rule &rarr; <strong>briefing</strong>.<br><strong>Corrected words:</strong> attendance | briefing.""",
         "Watch silent letters in workplace words: <strong>w</strong>rite, <strong>k</strong>now, com<strong>b</strong>, dou<strong>b</strong>t, lis<strong>t</strong>en.",
         "Break long words into chunks (syllables) when spelling: <em>re-spon-si-bi-li-ty</em>.",
         [
           ("Correct the spelling of these 4 workplace words:<br>a) recieve &nbsp;&nbsp; b) buisness &nbsp;&nbsp; c) neccessary &nbsp;&nbsp; d) tomorow", "[4 Marks]"),
           ("Which spelling is correct: a) accomodation &nbsp;&nbsp; b) accommodation &nbsp;&nbsp; c) acommodation?", "[1 Mark]"),
           ("Write the correct spelling for the day that comes after Tuesday.", "[1 Mark]"),
           ("Use the word 'opportunity' in a full workplace sentence.", "[2 Marks]")
         ]),

        # Unit 18
        ("Unit 18: Applied Writing: Filling in Forms", "Writing: Workplace Documents",
         """Form filling is one of the two core writing tasks tested in Entry Level 3. Forms require accurate personal details, concise descriptions, and correct capitalisation.""",
         """<strong>Form Filling Conventions:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Title:</strong> Mr / Mrs / Miss / Ms / Dr (always capitalised).</li>
           <li><strong>Name &amp; Address:</strong> House number, street name, town/city, postcode in BLOCK CAPITALS (e.g. M1 4BT).</li>
           <li><strong>Dates:</strong> Write in specified format (DD/MM/YYYY or 14 October 2026).</li>
           <li><strong>Reason / Notes Section:</strong> Write in full, grammatically complete sentences. Do not use single bullet words when sentences are requested!</li>
         </ul>""",
         "A gym membership form asks: <em>'Please state in 1-2 complete sentences why you wish to join the health club.'</em> Write a suitable response.",
         """<em>'I wish to join the health club to improve my fitness and prepare for a charity 5k run. I also want to use the swimming pool in the evenings after work.'</em><br>
         &bull; 2 complete sentences &bull; Accurate punctuation &bull; Clear reasons provided.""",
         "Never leave mandatory form fields blank! If something does not apply to you, write 'N/A' (Not Applicable).",
         "Check postcode format: Postcodes have a space before the last 3 characters (e.g. SW1A 1AA).",
         [
           ("Write your full name, home town, and today's date formatted for an official training enrolment form.", "[2 Marks]"),
           ("On a form that asks for 'Occupation', what information should you write?", "[1 Mark]"),
           ("Complete this form section in two sentences: <em>'Explain any training courses you have completed previously.'</em>", "[2 Marks]"),
           ("Why must postcodes and passport numbers be written clearly in block capitals?", "[1 Mark]")
         ]),

        # Unit 19
        ("Unit 19: Applied Writing: Memos & Incident Logs", "Writing: Workplace Documents",
         """Workplace notes, handover memos, and incident logs communicate vital facts to supervisors, colleagues on the next shift, and safety auditors.""",
         """<strong>Structure of an Effective Workplace Note:</strong>
         <ol style="margin:4px 0 0 16px;">
           <li><strong>Heading / Addressee:</strong> State clearly who the note is for (e.g. <em>'To: Morning Shift Team'</em>).</li>
           <li><strong>The What, When &amp; Where:</strong> Provide factual details in chronological order without personal bias.</li>
           <li><strong>Action Taken:</strong> What did you do to address the situation? (e.g. <em>'I contacted maintenance.'</em>).</li>
           <li><strong>Next Steps / Sign-Off:</strong> What must the reader do next? Sign your name and write the date and time.</li>
         </ol>""",
         """Write a 3-sentence incident log for a spillage in the staff kitchen.<br>
         Facts: Juice spilled on tile floor at 11:15 am &bull; Cleaned up &bull; Wet floor hazard cone placed.""",
         """<em>'At 11:15 am, a bottle of juice was spilled on the kitchen tile floor. I wiped up the liquid with paper towels and sanitised the area. I placed a yellow wet floor hazard cone by the entrance until the floor is completely dry.'</em>""",
         "Keep notes factual and objective. Avoid emotional complaints like 'Someone was careless again'.",
         "Always include the exact date, time, and your name on workplace incident records.",
         [
           ("Write a 2-sentence handover note to your colleague explaining that a customer left their glasses at Reception.", "[2 Marks]"),
           ("List three details that must always appear on a formal workplace message or log.", "[3 Marks]"),
           ("Why is accurate timing crucial when recording accidents in a workplace First Aid log?", "[1 Mark]"),
           ("Identify two spelling or grammar errors in: <em>'the parcel was droped at 3pm but nobody wasnt there.'</em>", "[2 Marks]")
         ]),

        # Unit 20
        ("Unit 20: Applied Writing: Workplace Emails", "Writing: Workplace Documents",
         """Emails are the standard medium for business communication. In your Entry 3 writing exam, Task 2 typically asks you to write an email of 70–100 words.""",
         """<strong>The 4-Part Professional Email Framework:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>1. Subject Line:</strong> Concise summary of the email's purpose (e.g. <em>'Subject: Request for Annual Leave &ndash; 15-18 June'</em>).</li>
           <li><strong>2. Professional Salutation:</strong> <em>'Dear Mr Davies,'</em> or <em>'Dear Sarah,'</em> (avoid casual 'Hey').</li>
           <li><strong>3. Body Paragraphs (2-3 short paragraphs):</strong>
             <br>&bull; Paragraph 1: Why you are writing.
             <br>&bull; Paragraph 2: Key details, dates, or questions.
             <br>&bull; Paragraph 3: Action requested or expected response.
           </li>
           <li><strong>4. Sign-Off:</strong> <em>'Kind regards,'</em> or <em>'Best wishes,'</em> followed by your full name.</li>
         </ul>""",
         "Write the opening paragraph of an email to your college tutor requesting an extension on an assignment due on Friday.",
         """<em>'Dear Mr Harrison,<br><br>I am writing to politely request a short extension on my health and safety assignment, which is currently due this Friday, 20 November.'</em>""",
         "Never send an email without a subject line! In the exam, omitting the subject line costs formatting marks.",
         "Keep the tone formal and respectful when writing to managers, tutors, and customers.",
         [
           ("Write an appropriate subject line for an email reporting a broken air conditioning unit in Room 12.", "[1 Mark]"),
           ("Write two suitable professional email sign-offs.", "[2 Marks]"),
           ("Draft the middle paragraph of an email informing your team about a meeting rescheduled to 3:00 pm.", "[2 Marks]"),
           ("Explain why using all capital letters in an email (e.g. 'PLEASE READ THIS') is considered poor etiquette.", "[1 Mark]")
         ])
    ]

    for idx, (title, strand, concept_text, method_text, worked_q, worked_ans, trap_text, tip_text, practice_qs) in enumerate(english_units_data, 1):
        left_page_num = 2 + (idx * 2)      # 4, 6, 8...
        right_page_num = left_page_num + 1  # 5, 7, 9...

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry 3</div>
    <div class="page-header-strand">{strand}</div>
  </div>

  <h2>{title}</h2>

  <div class="card-concept">
    <strong style="color:#0369a1; font-size:9pt;">[A] Literacy Standard &amp; Purpose:</strong><br>
    {concept_text}
  </div>

  <div class="card-method">
    <strong style="color:#15803d; font-size:9pt;">[B] Visual Structural Rules:</strong><br>
    {method_text}
  </div>

  <div class="card-practice" style="border-left-color:#881337;">
    <strong style="color:#881337; font-size:9pt;">[C] High-Scoring Workplace Model:</strong><br>
    <p style="margin:4px 0;"><strong>Scenario:</strong> {worked_q}</p>
    <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:6px 10px; border-radius:4px; margin-top:4px;">
      <strong>Model Analysis &amp; Solution:</strong><br>
      {worked_ans}
    </div>
  </div>

  <div class="grid-2">
    <div class="card-trap">
      <strong style="color:#b91c1c; font-size:8.5pt;">[D] Watch Out For:</strong><br>
      {trap_text}
    </div>
    <div class="card-tip">
      <strong style="color:#b45309; font-size:8.5pt;">[E] Tutor Golden Rule:</strong><br>
      {tip_text}
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {left_page_num}</div>
  </div>
</div>
""")

        practice_html = ""
        for q_idx, (q_text, marks) in enumerate(practice_qs, 1):
            practice_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <strong>Exercise {q_idx}:</strong> <span class="mark-badge" style="background:#881337;">{marks}</span>
  </div>
  <p style="margin:2px 0 4px 0;">{q_text}</p>
  <div class="workspace-ruled" style="min-height:55px;">Write your response here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry 3</div>
    <div class="page-header-strand">Unit {idx} Graded Practice Drills</div>
  </div>

  <h2>Practice Drills: {title.split(':')[1].strip()}</h2>
  <p style="margin-bottom:8px;">Complete the following exam-style exercises. Ensure all spelling, punctuation, and capital letters are accurate.</p>

  {practice_html}

  <div class="card-tip" style="margin-top:auto;">
    <strong>Progress Check:</strong> Compare your answers with the model answers on Pages 46–47. Pay close attention to capital letters and punctuation accuracy.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {right_page_num}</div>
  </div>
</div>
""")



    # -------------------------------------------------------------
    # PAGES 44-59: 8 SCAFFOLDED APPLIED WRITING WORKSHOPS (16 Pages)
    # -------------------------------------------------------------
    workshops_data = [
        ("Workshop 1: Workplace Incident & Hazard Log Form", "Applied Writing: Health & Safety Documentation",
         "In any workplace—whether retail, healthcare, hospitality, or warehousing—accidents and hazards must be logged immediately. An incident form requires factual, concise statements explaining who, what, when, where, and what action was taken.",
         "Incident Date & Time, Specific Location, Person Affected, Description of What Happened, Immediate Action Taken, Further Preventive Action Needed.",
         ["At approximately 09:30 am, I noticed...", "A member of staff reported that...", "I immediately placed a warning cone and...", "To prevent further risk, we informed..."],
         ["hazard", "slip", "wet surface", "warning cone", "paramedic", "first aider", "supervisor", "cleaned", "cordoned off", "reported"],
         "Complete the Workplace Incident & Hazard Log below regarding a liquid detergent spill in the staff breakroom that caused an employee to slip.",
         [("Date of Incident", "Time of Incident", "Location / Department"),
          ("Name of Reporting Person", "Job Title", "Witnesses (if any)"),
          ("Detailed Description of What Happened (Full Sentences)", 4),
          ("Immediate Corrective Actions Taken", 3),
          ("Supervisor Notification & Sign-Off", 2)]),

        ("Workshop 2: Shift Handover & Maintenance Request Note", "Applied Writing: Workplace Communication",
         "Shift handovers ensure seamless continuity of care, safety, and productivity. When machinery or facilities fail, a formal maintenance note provides maintenance engineers with essential fault symptoms.",
         "Date & Shift (Day/Night), Machine/Room ID, Nature of Issue/Fault, Action Already Attempted, Urgency Level (Routine/Urgent), Contact Details.",
         ["During the handover, please note that...", "The primary printer on Floor 2 has developed a...", "We attempted to restart the system, but...", "Engineers must inspect this before..."],
         ["maintenance", "breakdown", "defective", "temperature", "jammed", "unserviceable", "urgent", "replaced", "inspected", "handover"],
         "Write a Shift Handover & Maintenance Request note to the incoming facilities supervisor reporting that the walk-in refrigerator in the staff canteen is making a loud buzzing noise and reading 11°C (above the 5°C legal limit).",
         [("Date & Time of Handover", "Equipment Name & Serial ID", "Room / Zone"),
          ("Reporting Technician / Carer", "Incoming Supervisor", "Priority Level"),
          ("Detailed Symptoms & Temperature Readings", 4),
          ("Interim Safety Precautions Taken (Food Moved)", 3),
          ("Required Engineer Action & Next Steps", 2)]),

        ("Workshop 3: Workplace Absence & Holiday Request Email", "Applied Writing: Professional Digital Communication",
         "Workplace emails requesting annual leave or reporting sickness absence require formal register, respectful tone, clear dates, and proposed coverage of your duties.",
         "Subject Line with Name & Purpose, Professional Salutation, Specific Dates Requested, Work Cover Arrangements, Polite Request for Confirmation, Formal Sign-Off.",
         ["I am writing to formally request...", "I would like to take leave from [Date] to [Date]...", "My colleague Sarah has agreed to cover my...", "Thank you in advance for considering my..."],
         ["annual leave", "absence", "colleague", "handover", "duties", "approved", "confirm", "available", "regards", "request"],
         "Compose a professional email to your department manager, Mr Robert Evans, requesting three days of annual leave (Wednesday 14 May to Friday 16 May) to attend a family wedding. Confirm that your shift duties have been covered by your colleague.",
         [("To:", "Subject:", "Date:"),
          ("Salutation & Opening Statement", 2),
          ("Reason for Request & Exact Dates", 3),
          ("Shift Coverage & Duty Arrangements", 3),
          ("Closing Request & Professional Sign-off", 2)]),

        ("Workshop 4: Customer Feedback & Return Form", "Applied Writing: Customer Service Documentation",
         "Customer service professionals regularly document customer returns, complaints, and warranty requests. Clear factual notes protect both the customer and the business.",
         "Customer Name & Account/Receipt Number, Purchase Date, Item SKU/Description, Reason for Return/Fault, Desired Resolution (Refund/Replacement/Repair), Staff Action.",
         ["The customer visited the store today to...", "Upon visual inspection, the item showed...", "The receipt confirms the purchase date of...", "I have authorized an exchange for..."],
         ["receipt", "refund", "exchange", "defective", "warranty", "customer service", "policy", "satisfaction", "replacement", "condition"],
         "Complete the Customer Feedback & Return Record for Mrs Fatima Khan, who bought an electric kettle that stopped boiling after three days. She brought the original receipt and box and requested a replacement.",
         [("Customer Name", "Contact Telephone", "Transaction / Receipt No."),
          ("Product Description", "Date of Purchase", "Purchase Price"),
          ("Customer Explanation of Fault / Concern", 4),
          ("Inspection Findings by Staff", 3),
          ("Final Resolution Granted & Customer Signature", 2)]),

        ("Workshop 5: Workplace Health & Safety Notice & Sign", "Applied Writing: Public Safety Notices",
         "Workplace notices must catch the reader's eye immediately using bold headings, concise bullet points, and imperative (command) verbs to guarantee compliance.",
         "High-Impact Main Heading, Scope / Target Audience (Who must obey), Mandatory Rules (Must / Do Not), Consequences of Non-Compliance, Contact for Questions.",
         ["All staff and visitors must...", "Do not operate machinery without...", "In the event of an emergency, immediately...", "Safety equipment is mandatory at all times in..."],
         ["mandatory", "protective equipment", "prohibited", "emergency exit", "assembly point", "regulations", "compliance", "authorized personnel"],
         "Design an eye-catching Workplace Health & Safety Notice for a warehouse loading bay informing forklift drivers and pedestrians of new high-visibility vest requirements and 5 mph speed limits.",
         [("Document Title & Target Area", 1),
          ("Why This Policy is Important (Safety Rationale)", 3),
          ("4 Mandatory Safety Rules (Use Bullet Points & Imperatives)", 5),
          ("Reporting Hazards & Emergency Contact Information", 3)]),

        ("Workshop 6: Formal Letter to College / Employer", "Applied Writing: Formal Correspondence",
         "Formal letters follow strict conventions: sender's address (top right), recipient's name and address (top left), date, formal greeting ('Dear Sir or Madam' or 'Dear Ms Jenkins'), and standard closing ('Yours sincerely' or 'Yours faithfully').",
         "Sender Address & Date, Recipient Address, Formal Salutation, Clear Purpose of Writing, Supporting Paragraphs with Evidence, Call to Action, Formal Close & Signature.",
         ["I am writing to express my interest in...", "I believe this course will significantly enhance my...", "I have attached my certificate of...", "I look forward to hearing from you soon."],
         ["qualification", "application", "enrolment", "programme", "experience", "beneficial", "opportunity", "sincerely", "faithfully", "applicant"],
         "Write a formal letter to the Admissions Tutor at Oakwood College applying for a place on the Level 1 Essential Digital Skills course. Explain your motivation, your current skills, and your availability.",
         [("Sender Details & Date", "Recipient Address", "Salutation"),
          ("Opening Paragraph (State What You Are Applying For)", 3),
          ("Body Paragraph 1 (Current Skills & Background)", 3),
          ("Body Paragraph 2 (Why This Course Helps Your Career)", 3),
          ("Formal Sign-off & Printed Name", 2)]),

        ("Workshop 7: Informational Staff / Visitor Leaflet", "Applied Writing: Informational Publications",
         "Leaflets use clear subheadings, short bite-sized paragraphs, bulleted advice, and welcoming language to inform staff, students, or visitors about policies and facilities.",
         "Catchy Title, Welcoming Introduction, Subheading 1: Key Services/Facilities, Subheading 2: Opening Hours & Access, Subheading 3: Rules & Expectations, Contact Info.",
         ["Welcome to our new...", "We are proud to offer...", "Please ensure you adhere to...", "For any further questions, please speak to..."],
         ["facilities", "accessible", "resources", "guidelines", "assistance", "canteen", "reception", "hours", "community", "welcome"],
         "Draft an Informational Welcome Leaflet for new employees joining your company. Detail the canteen location, working hours, ID badge policy, and IT support desk contact.",
         [("Leaflet Title & Welcome Headline", 1),
          ("Working Hours & Building Access (ID Badges)", 3),
          ("Staff Amenities (Canteen, Lockers, Quiet Room)", 3),
          ("IT & Equipment Support (Helpdesk Contacts)", 3),
          ("Key Contacts & First Aid Locations", 2)]),

        ("Workshop 8: Short Product / Service Review & Rating", "Applied Writing: Evaluative Writing",
         "Online reviews allow consumers and employees to share evaluations. A balanced review includes positive features, minor drawbacks, a star rating, and a clear recommendation.",
         "Catchy Review Title, Star Rating (1 to 5 Stars), What Was Tested/Used, Positive Strengths (Specific Details), Constructive Areas for Improvement, Final Recommendation.",
         ["I recently visited / purchased...", "The most impressive aspect was...", "However, one area that could be improved is...", "Overall, I would strongly recommend this to..."],
         ["recommend", "excellent", "service", "efficient", "quality", "disappointed", "satisfactory", "improvement", "value for money", "overall"],
         "Write a balanced, 4-star review of a newly opened community café or workplace cafeteria evaluating the food quality, speed of service, prices, and staff friendliness.",
         [("Review Headline & Star Rating (e.g. 4/5 Stars)", 1),
          ("Introduction (What You Ordered & When You Visited)", 2),
          ("Positive Highlights (Food Quality, Cleanliness, Atmosphere)", 4),
          ("Constructive Feedback (Wait Times, Seating)", 3),
          ("Final Verdict & Who You Recommend It To", 2)])
    ]

    for w_idx, (w_title, w_strand, context, layout_rules, sentence_starters, word_bank, task_prompt, form_sections) in enumerate(workshops_data, 1):
        left_pnum = 44 + (w_idx - 1) * 2
        right_pnum = left_pnum + 1

        starters_html = "".join(["<li><em>'" + s + "'</em></li>" for s in sentence_starters])
        words_html = "".join(["<span class='tag-pill tag-blue' style='margin-bottom:3px;'>" + w + "</span> " for w in word_bank])

        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{w_strand}</div>
  </div>

  <h2>{w_title} &mdash; Scaffolding &amp; Strategy</h2>
  
  <div class="card-concept" style="border-left-color:#881337;">
    <h3 style="color:#881337; margin-top:0;">Workplace Real-World Context</h3>
    <p style="margin:0;">{context}</p>
  </div>

  <div class="card-method">
    <h3 style="color:#16a34a; margin-top:0;">Structure &amp; Formatting Blueprint</h3>
    <p style="margin:0;"><strong>Mandatory Structural Features:</strong> {layout_rules}</p>
  </div>

  <div class="grid-2" style="margin-top:4px;">
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Sentence Starters Bank</h3>
      <ul style="margin:2px 0 0 14px; padding:0; font-size:8pt; line-height:1.4;">
        {starters_html}
      </ul>
    </div>
    <div class="card-exam" style="border-left-color:#7c3aed;">
      <h3 style="color:#7c3aed; margin-top:0;">Target Vocabulary Bank</h3>
      <div style="margin-top:4px; line-height:1.6;">
        {words_html}
      </div>
      <div style="margin-top:6px; font-size:7.5pt; color:#64748b;">
        Spell every chosen word accurately to secure full SPaG marks.
      </div>
    </div>
  </div>

  <div class="card-practice" style="margin-top:6px;">
    <h3 style="margin-top:0;">Candidate Writing Task Brief</h3>
    <p style="margin:0; font-size:8.3pt; font-weight:600; color:#1e293b;">{task_prompt}</p>
    <div style="margin-top:4px; font-size:7.5pt; color:#64748b;">
      Turn to <strong>Page {right_pnum}</strong> to complete the official scaffolded response form. Ensure you use MINTS capital letters and full stops.
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {left_pnum}</div>
  </div>
</div>
''')

        form_html = ""
        for sec in form_sections:
            if isinstance(sec, tuple) and len(sec) == 3 and isinstance(sec[0], str) and isinstance(sec[1], str) and isinstance(sec[2], str):
                form_html += f'''
<div class="grid-3" style="margin-bottom:6px;">
  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:4px 6px;">
    <div style="font-size:7pt; font-weight:700; color:#475569; text-transform:uppercase;">{sec[0]}</div>
    <div style="border-bottom:1px solid #94a3b8; height:18px; margin-top:2px;"></div>
  </div>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:4px 6px;">
    <div style="font-size:7pt; font-weight:700; color:#475569; text-transform:uppercase;">{sec[1]}</div>
    <div style="border-bottom:1px solid #94a3b8; height:18px; margin-top:2px;"></div>
  </div>
  <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:4px; padding:4px 6px;">
    <div style="font-size:7pt; font-weight:700; color:#475569; text-transform:uppercase;">{sec[2]}</div>
    <div style="border-bottom:1px solid #94a3b8; height:18px; margin-top:2px;"></div>
  </div>
</div>'''
            elif isinstance(sec, tuple) and len(sec) == 2 and isinstance(sec[0], str) and isinstance(sec[1], int):
                lines_count = sec[1]
                lines_h = "".join(["<div style='border-bottom:1px solid #e2e8f0; height:20px;'></div>" for _ in range(lines_count)])
                form_html += f'''
<div style="margin-bottom:6px;">
  <div style="font-size:7.5pt; font-weight:700; color:#1e293b; margin-bottom:2px;">{sec[0]}:</div>
  <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; padding:4px 8px;">
    {lines_h}
  </div>
</div>'''

        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{w_strand} &bull; Practice Sheet</div>
  </div>

  <h2>{w_title} &mdash; Official Candidate Writing Frame</h2>
  <p style="font-size:8pt; margin:0 0 6px 0;">Complete all sections using clear black ink, capital letters where required, and full sentences.</p>

  <div style="border:1.5px solid #881337; border-radius:6px; padding:8px 10px; background:#fffafb; margin-bottom:6px;">
    {form_html}
  </div>

  <div class="card-concept" style="margin-top:auto; padding:6px 10px; background:#f0fdf4; border-left-color:#16a34a;">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <strong style="color:#16a34a; font-size:7.5pt;">Candidate Self-Audit Checklist:</strong>
      <span style="font-size:7pt; color:#64748b;">Tick when verified</span>
    </div>
    <div class="grid-4" style="margin-top:4px; font-size:7pt;">
      <div>[ &nbsp; ] All sections completed</div>
      <div>[ &nbsp; ] MINTS capitals verified</div>
      <div>[ &nbsp; ] Full stops on all sentences</div>
      <div>[ &nbsp; ] Words spelled accurately</div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {right_pnum}</div>
  </div>
</div>
''')

    # -------------------------------------------------------------
    # PAGES 60-63: FULL BAND 4 BENCHMARK EXEMPLARS (4 Pages)
    # -------------------------------------------------------------
    exemplars_data = [
        ("Exemplar 1: Workplace Incident & Hazard Form (Band 4 Distinction)",
         "Task Stimulus: Liquid spill causing staff slip in breakroom at 09:30 am.",
         '''<table class="data-table" style="font-size:7.8pt;">
           <tr><td style="width:25%;"><strong>Date &amp; Time:</strong></td><td>Tuesday 14 October, 09:30 am</td></tr>
           <tr><td><strong>Location:</strong></td><td>Staff Breakroom, Ground Floor, Unit 4</td></tr>
           <tr><td><strong>Person Affected:</strong></td><td>Mark Stevens (Warehouse Operative)</td></tr>
           <tr><td><strong>Description of Event:</strong></td><td>At approximately 09:30 am, Mark Stevens slipped on a puddle of liquid dishwashing soap near the kitchen sink. He fell onto his left knee. I was present and immediately assisted him to a chair. Fortunately, he did not sustain any open cuts, but his knee was bruised.</td></tr>
           <tr><td><strong>Immediate Action:</strong></td><td>I retrieved the yellow warning cone and placed it beside the spill. I fetched a dry mop and cleaned the floor thoroughly until dry. Mark applied an ice pack from the first aid kit.</td></tr>
           <tr><td><strong>Prevention:</strong></td><td>I reported the loose soap bottle to our team leader, Brenda Cole, and requested a wall-mounted dispenser.</td></tr>
         </table>''',
         "Why This Achieves Full Marks (Band 4):",
         [("Factual Detail [4m]", "Clear timeline (09:30 am), specific names, exact room location, and full medical/safety sequence."),
          ("SPaG Precision [4m]", "Consistent past simple tense ('slipped', 'assisted', 'placed', 'cleaned'), correct capital letters for names and days, zero run-ons."),
          ("Professional Tone [2m]", "Objective, polite, responsible safety mindset appropriate for UK health and safety audits.")]),

        ("Exemplar 2: Professional Absence & Annual Leave Email (Band 4 Distinction)",
         "Task Stimulus: Formal email to line manager requesting 3 days leave for a family wedding.",
         '''<div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:10px; font-size:8pt; line-height:1.45;">
           <strong>To:</strong> Robert.Evans@apexlogistics.co.uk<br>
           <strong>From:</strong> J.Miller@apexlogistics.co.uk<br>
           <strong>Date:</strong> Monday 5 May 2026<br>
           <strong>Subject:</strong> Annual Leave Request &mdash; Wednesday 14 May to Friday 16 May<br>
           <hr style="border:none; border-top:1px solid #e2e8f0; margin:6px 0;">
           Dear Mr Evans,<br><br>
           I am writing to formally request three days of annual leave from Wednesday 14 May to Friday 16 May. I will return to normal duties on Monday 19 May.<br><br>
           I need to take this leave to attend my sister's wedding in Manchester. Before submitting this request, I spoke with Sarah Jenkins, and she has kindly agreed to cover my warehouse picking shifts on Wednesday and Thursday.<br><br>
           All of my inventory logs for this week are completely up to date. I would be grateful if you could confirm whether this leave is approved.<br><br>
           Kind regards,<br>
           <strong>Jack Miller</strong><br>
           Warehouse Operative (Badge #482)
         </div>''',
         "Why This Achieves Full Marks (Band 4):",
         [("Structure & Format [3m]", "Clear subject line with date and name, professional greeting, paragraph breaks, and courteous closing."),
          ("Task Fulfillment [5m]", "Covers all required prompts: exact dates, purpose of leave, shift coverage arrangements, and confirmation request."),
          ("SPaG Standards [4m]", "Correct MINTS capitalization (Monday, May, Manchester, Sarah, Jack), varied sentence conjunctions (and, because), accurate spelling.")]),

        ("Exemplar 3: Formal Letter to College Admissions (Band 4 Distinction)",
         "Task Stimulus: Application letter for Essential Digital Skills Entry 3 course.",
         '''<div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:10px; font-size:7.8pt; line-height:1.4;">
           <div style="text-align:right;">
             14 High Street<br>Bolton, BL1 4QR<br>18 September 2026
           </div>
           <div>
             Admissions Department<br>Oakwood College<br>Manchester Road<br>Bolton, BL2 1EE
           </div>
           <p style="margin:4px 0 2px 0;">Dear Admissions Team,</p>
           <p style="margin:2px 0;"><strong>Re: Application for Essential Digital Skills Entry Level 3</strong></p>
           <p style="margin:2px 0;">I am writing to apply for the Essential Digital Skills course starting in October. I would like to attend the evening classes on Tuesday and Thursday.</p>
           <p style="margin:2px 0;">At present, I work as a healthcare assistant. I can use a smartphone, but I need to learn how to create spreadsheets, send professional workplace emails, and store files safely online. Gaining this qualification will help me record patient care notes accurately at work.</p>
           <p style="margin:2px 0;">I have attached a copy of my photo ID and proof of address. Please let me know the enrolment dates and course induction times.</p>
           <p style="margin:2px 0;">Yours sincerely,</p>
           <p style="margin:2px 0;"><strong>Amina Begum</strong></p>
         </div>''',
         "Why This Achieves Full Marks (Band 4):",
         [("Layout Conventions [3m]", "Sender address top right, recipient address left, standard date, formal salutation, Re: header, formal close."),
          ("Content Development [5m]", "Explains current job role, reasons for taking the course, specific digital skills wanted, and requests next steps."),
          ("Grammar & Mechanics [4m]", "Clear compound sentences using 'but' and 'and', full control of capital letters and apostrophes.")]),

        ("Exemplar 4: Workplace Health & Safety Information Notice (Band 4 Distinction)",
         "Task Stimulus: High-visibility vest and speed limit policy notice for loading bay.",
         '''<div style="background:#ffffff; border:2px solid #881337; border-radius:5px; padding:10px; font-size:7.8pt; line-height:1.4;">
           <div style="text-align:center; background:#881337; color:#ffffff; padding:4px; font-weight:800; text-transform:uppercase; letter-spacing:1px; margin:-10px -10px 8px -10px;">
             HEALTH &amp; SAFETY NOTICE &bull; LOADING BAY SAFETY
           </div>
           <p style="margin:0 0 4px 0;"><strong>Target Area:</strong> All Warehouse Operatives, Delivery Drivers &amp; Visitors</p>
           <p style="margin:0 0 4px 0;">Safety in our loading bays is our highest priority. Due to recent near-miss incidents, all personnel must follow the safety regulations below with immediate effect:</p>
           <ul style="margin:2px 0 4px 14px; padding:0;">
             <li><strong>Wear High-Visibility Vests:</strong> Yellow or orange reflective vests must be worn at all times in Bay 1 and Bay 2.</li>
             <li><strong>Observe 5 MPH Speed Limit:</strong> All forklift truck drivers must strictly obey the 5 mph speed restriction.</li>
             <li><strong>Use Designated Walkways:</strong> Pedestrians must keep inside the green painted floor paths. Do not take shortcuts across lorry bays.</li>
             <li><strong>Sound Horns at Corners:</strong> Forklift drivers must sound their horn when turning blind corners.</li>
           </ul>
           <p style="margin:2px 0;">Failure to comply with these rules will lead to a safety disciplinary review. If you see a hazard, report it immediately to your shift supervisor on extension 204.</p>
         </div>''',
         "Why This Achieves Full Marks (Band 4):",
         [("Visual Formatting [3m]", "Clear bold header banner, target area label, numbered/bulleted imperative rules, high readability."),
          ("Command Language [5m]", "Uses imperative 'bossy' verbs ('Wear', 'Observe', 'Use', 'Sound', 'Report') suited to health & safety notices."),
          ("SPaG Accuracy [4m]", "Flawless punctuation, correct technical terminology, zero spelling errors.")])
    ]

    for e_idx, (e_title, e_stim, e_body, crit_title, crit_points) in enumerate(exemplars_data, 1):
        pnum = 60 + (e_idx - 1)
        crit_html = "".join(["<li style='margin-bottom:4px;'><strong>" + cp[0] + ":</strong> " + cp[1] + "</li>" for cp in crit_points])
        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Examiner Benchmarks &bull; Band 4 Exemplar</div>
  </div>

  <h2>{e_title}</h2>
  <div class="card-concept" style="padding:6px 10px; margin-bottom:6px;">
    <strong>Prompt Stimulus:</strong> {e_stim}
  </div>

  {e_body}

  <div class="card-method" style="margin-top:8px;">
    <h3 style="color:#16a34a; margin-top:0;">{crit_title}</h3>
    <ul style="margin:2px 0 0 14px; padding:0; font-size:8pt; line-height:1.45;">
      {crit_html}
    </ul>
  </div>

  <div class="card-tip" style="margin-top:6px; font-size:7.5pt;">
    <strong>Examiner Advice:</strong> Compare your own practice writing against this Band 4 model. Notice how every sentence has a capital letter and full stop, and all prompts from the scenario are answered clearly.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {pnum}</div>
  </div>
</div>
''')

    # -------------------------------------------------------------
    # PAGES 64-67: ENTRY 3 REFERENCE & TOOLKIT (4 Pages)
    # -------------------------------------------------------------
    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Reference Toolkit &bull; Top 100 Spelling Words</div>
  </div>

  <h2>Top 100 Entry Level 3 Workplace Spelling Words</h2>
  <p>Pearson and Ofqual test spelling of everyday words and workplace terms. Learn these words grouped by spelling pattern:</p>

  <div class="grid-2" style="font-size:7.5pt;">
    <div class="card-practice">
      <strong style="color:#881337;">Silent Letters &amp; Tricky Patterns</strong>
      <div class="grid-2" style="margin-top:4px;">
        <div>&bull; write / wrong<br>&bull; know / knee<br>&bull; could / would<br>&bull; should / climb<br>&bull; half / talk</div>
        <div>&bull; sign / signpost<br>&bull; doubt / debt<br>&bull; island / answer<br>&bull; listen / fasten<br>&bull; honest / hour</div>
      </div>
    </div>
    <div class="card-practice">
      <strong style="color:#881337;">Double Consonant Words</strong>
      <div class="grid-2" style="margin-top:4px;">
        <div>&bull; address / arrive<br>&bull; appoint / attend<br>&bull; borrow / collect<br>&bull; difficult / happen<br>&bull; letter / lesson</div>
        <div>&bull; message / middle<br>&bull; notice / offer<br>&bull; office / passenger<br>&bull; possible / summer<br>&bull; traffic / yellow</div>
      </div>
    </div>
  </div>

  <div class="grid-2" style="font-size:7.5pt; margin-top:6px;">
    <div class="card-practice">
      <strong style="color:#881337;">Common Suffix Endings (-ful, -tion, -ly)</strong>
      <div class="grid-2" style="margin-top:4px;">
        <div>&bull; careful / helpful<br>&bull; useful / painful<br>&bull; slowly / quickly<br>&bull; clearly / finally<br>&bull; safely / really</div>
        <div>&bull; station / action<br>&bull; section / direction<br>&bull; question / operation<br>&bull; attention / position<br>&bull; education / instruction</div>
      </div>
    </div>
    <div class="card-practice">
      <strong style="color:#881337;">Everyday Workplace &amp; Social Words</strong>
      <div class="grid-2" style="margin-top:4px;">
        <div>&bull; Tuesday / Wednesday<br>&bull; February / August<br>&bull; friend / people<br>&bull; because / thought<br>&bull; through / enough</div>
        <div>&bull; manager / colleague<br>&bull; customer / service<br>&bull; kitchen / vehicle<br>&bull; clothes / shoes<br>&bull; weather / calendar</div>
      </div>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px; font-size:7.8pt;">
    <strong>Look, Say, Cover, Write, Check:</strong> Test yourself on 5 words each day. Cover the word, write it on paper, and check each letter.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 64</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Reference Toolkit &bull; Irregular Verbs Table</div>
  </div>

  <h2>Mastering Past &amp; Present Verbs (Irregular Verbs)</h2>
  <p>In Functional Skills exams, writing about past events (like an incident report) requires accurate past tense verbs. Regular verbs add <strong>-ed</strong> (walk &rarr; walked), but irregular verbs change their spelling completely.</p>

  <table class="data-table" style="font-size:7.2pt; margin-top:4px;">
    <tr>
      <th style="width:20%;">Infinitive (Present)</th>
      <th style="width:25%;">Past Simple</th>
      <th style="width:55%;">Workplace Example Sentence</th>
    </tr>
    <tr><td><strong>be (is / are)</strong></td><td>was / were</td><td>The breakroom floor <strong>was</strong> wet after cleaning.</td></tr>
    <tr><td><strong>buy</strong></td><td>bought</td><td>The manager <strong>bought</strong> new safety goggles yesterday.</td></tr>
    <tr><td><strong>bring</strong></td><td>brought</td><td>The courier <strong>brought</strong> five boxes to reception.</td></tr>
    <tr><td><strong>catch</strong></td><td>caught</td><td>He <strong>caught</strong> the 08:15 train to the training centre.</td></tr>
    <tr><td><strong>come</strong></td><td>came</td><td>The paramedic <strong>came</strong> quickly to assist the patient.</td></tr>
    <tr><td><strong>do</strong></td><td>did</td><td>We <strong>did</strong> our daily stock check before 10:00 am.</td></tr>
    <tr><td><strong>fall</strong></td><td>fell</td><td>The plastic container <strong>fell</strong> off the shelf.</td></tr>
    <tr><td><strong>find</strong></td><td>found</td><td>The supervisor <strong>found</strong> the missing safety keys.</td></tr>
    <tr><td><strong>get</strong></td><td>got</td><td>She <strong>got</strong> an email confirming her new rota.</td></tr>
    <tr><td><strong>give</strong></td><td>gave</td><td>Mr Evans <strong>gave</strong> me permission to leave early.</td></tr>
    <tr><td><strong>go</strong></td><td>went</td><td>I <strong>went</strong> to the store cupboard to fetch a dry mop.</td></tr>
    <tr><td><strong>have</strong></td><td>had</td><td>We <strong>had</strong> a team briefing at the start of the shift.</td></tr>
    <tr><td><strong>hear</strong></td><td>heard</td><td>The staff <strong>heard</strong> the fire alarm sound at 2:00 pm.</td></tr>
    <tr><td><strong>make</strong></td><td>made</td><td>He <strong>made</strong> a telephone call to report the fault.</td></tr>
    <tr><td><strong>see</strong></td><td>saw</td><td>I <strong>saw</strong> the water leaking from the pipe.</td></tr>
    <tr><td><strong>take</strong></td><td>took</td><td>The carer <strong>took</strong> the resident's temperature.</td></tr>
    <tr><td><strong>tell</strong></td><td>told</td><td>I <strong>told</strong> my supervisor about the hazard immediately.</td></tr>
    <tr><td><strong>write</strong></td><td>wrote</td><td>She <strong>wrote</strong> the details in the shift handover log.</td></tr>
  </table>

  <div class="card-tip" style="margin-top:4px; font-size:7.5pt;">
    <strong>Common Error to Avoid:</strong> Never write <em>'I seen the leak'</em> or <em>'We done the work'</em> in a formal exam. Always write: <strong>'I saw the leak'</strong> and <strong>'We did the work'</strong>.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 65</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Reference Toolkit &bull; Sector Word Banks</div>
  </div>

  <h2>Specialist Workplace Vocabulary Banks</h2>
  <p>Examiners award marks when you choose precise, workplace-appropriate vocabulary. Use these sector-specific word banks:</p>

  <div class="grid-2" style="font-size:7.5pt;">
    <div class="card-practice">
      <h3 style="color:#0284c7; margin-top:0;">🏥 Health &amp; Social Care</h3>
      <p style="margin:0 0 4px 0;">Use these words when writing care notes or shift logs:</p>
      <div class="grid-2">
        <div>&bull; appointment<br>&bull; medication<br>&bull; temperature<br>&bull; wheelchair<br>&bull; breakfast / lunch</div>
        <div>&bull; assistance<br>&bull; comfortable<br>&bull; doctor / nurse<br>&bull; emergency<br>&bull; handover notes</div>
      </div>
    </div>
    <div class="card-practice">
      <h3 style="color:#16a34a; margin-top:0;">📦 Warehousing &amp; Logistics</h3>
      <p style="margin:0 0 4px 0;">Use these words for stock sheets, deliveries, and incident logs:</p>
      <div class="grid-2">
        <div>&bull; consignment<br>&bull; delivery note<br>&bull; pallet / forklift<br>&bull; high-visibility vest<br>&bull; inventory</div>
        <div>&bull; barcode scanner<br>&bull; loading bay<br>&bull; dispatch / transit<br>&bull; packaging<br>&bull; supervisor</div>
      </div>
    </div>
  </div>

  <div class="grid-2" style="font-size:7.5pt; margin-top:6px;">
    <div class="card-practice">
      <h3 style="color:#d97706; margin-top:0;">🛍️ Retail &amp; Customer Service</h3>
      <p style="margin:0 0 4px 0;">Use these words for returns, customer feedback, and orders:</p>
      <div class="grid-2">
        <div>&bull; customer<br>&bull; receipt / invoice<br>&bull; refund / exchange<br>&bull; defective item<br>&bull; warranty</div>
        <div>&bull; polite / helpful<br>&bull; payment / cash<br>&bull; discount / offer<br>&bull; aisle / shelf<br>&bull; satisfaction</div>
      </div>
    </div>
    <div class="card-practice">
      <h3 style="color:#7c3aed; margin-top:0;">🏢 Office &amp; Business Admin</h3>
      <p style="margin:0 0 4px 0;">Use these words for formal emails, letters, and memos:</p>
      <div class="grid-2">
        <div>&bull; colleague / manager<br>&bull; meeting / agenda<br>&bull; spreadsheet<br>&bull; attachment<br>&bull; calendar</div>
        <div>&bull; attendance<br>&bull; confirmation<br>&bull; stationery<br>&bull; photocopier<br>&bull; professional</div>
      </div>
    </div>
  </div>

  <div class="card-method" style="margin-top:6px; font-size:7.8pt;">
    <strong>Tutor Tip:</strong> In your exam, check that you have included at least 3-4 topic-specific words from the scenario prompt.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 66</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Reference Toolkit &bull; Connectives &amp; Transitions</div>
  </div>

  <h2>Master Connectives &amp; Transitions Bank</h2>
  <p>Connectives link words and clauses together. Using a variety of connectives turns short, choppy sentences into flowing, mature text.</p>

  <table class="data-table" style="font-size:7.5pt; margin-top:4px;">
    <tr>
      <th style="width:25%;">Connective Function</th>
      <th style="width:30%;">Key Words &amp; Phrases</th>
      <th style="width:45%;">Worked Model Sentence</th>
    </tr>
    <tr>
      <td><strong>Adding Information</strong></td>
      <td>and, also, as well as, in addition</td>
      <td>I cleaned the kitchen <strong>and</strong> I wiped down the counter.</td>
    </tr>
    <tr>
      <td><strong>Contrasting Ideas</strong></td>
      <td>but, although, however</td>
      <td>I wanted to finish the report, <strong>but</strong> the computer froze.</td>
    </tr>
    <tr>
      <td><strong>Giving Reasons (Cause)</strong></td>
      <td>because, so, since, as</td>
      <td>The fire alarm sounded <strong>because</strong> toast had burned.</td>
    </tr>
    <tr>
      <td><strong>Showing Time &amp; Order</strong></td>
      <td>first, next, then, after, finally</td>
      <td><strong>First</strong>, put on gloves. <strong>Next</strong>, inspect the machinery.</td>
    </tr>
    <tr>
      <td><strong>Stating Conditions</strong></td>
      <td>if, when, unless</td>
      <td><strong>If</strong> you see a spill, notify the supervisor immediately.</td>
    </tr>
  </table>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-trap" style="font-size:7.8pt;">
      <strong style="color:#dc2626;">The 'And' Trap:</strong>
      <p style="margin:2px 0 0 0;">Do not link four ideas together with 'and' in one massive sentence: <em>'I came to work and I saw the spill and I told Bob and he mopped it.'</em> Break it into two sentences!</p>
    </div>
    <div class="card-tip" style="font-size:7.8pt;">
      <strong style="color:#d97706;">The Comma Rule with 'Although' &amp; 'If':</strong>
      <p style="margin:2px 0 0 0;">When starting a sentence with 'Although' or 'If', put a comma in the middle: <em>'<strong>Although</strong> it was raining, we completed the delivery on time.'</em></p>
    </div>
  </div>

  <div class="card-practice" style="margin-top:6px; font-size:7.8pt;">
    <strong>Quick Practice Drill:</strong> Join these two sentences using 'because':<br>
    <em>'The shop was closed.'</em> + <em>'It was a public holiday.'</em><br>
    <strong>Model Answer:</strong> The shop was closed because it was a public holiday.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 67</div>
  </div>
</div>
''')

    # -------------------------------------------------------------
    # PAGES 68-79: THREE FULL MOCK EXAM PAPERS (12 Pages = 4 Pages Each)
    # -------------------------------------------------------------
    mocks_data = [
        ("Mock Examination 1", "Westgate Training & Community Centre",
         '''<h3>Text A: Westgate College Open Evening Notice</h3>
            <p><strong>Discover New Opportunities at Westgate College!</strong></p>
            <p>Are you looking to improve your career prospects or gain new confidence? Westgate College is hosting our Autumn Open Evening on <strong>Thursday 22 October, from 5:00 pm to 8:00 pm</strong> at our City Centre Campus.</p>
            <p>We offer fully funded courses accredited by leading exam boards:</p>
            <ul>
              <li><strong>Functional Skills English &amp; Maths:</strong> Entry 1 to Level 2.</li>
              <li><strong>Essential Digital Skills (EDSQ):</strong> Beginner to Level 1.</li>
              <li><strong>Vocational Pathways:</strong> Health &amp; Social Care, Logistics, Business Administration.</li>
            </ul>
            <p>All attendees will have the opportunity to meet course tutors, complete initial assessments, and speak with our dedicated careers advisors. Light refreshments will be provided in the cafeteria.</p>
            <p><strong>Location:</strong> Westgate College, 45 Victoria Road, Birmingham, B1 2AA.<br>
            <strong>Website:</strong> www.westgatecollege.ac.uk | <strong>Phone:</strong> 0121 496 0120.</p>''',
         [("What is the main purpose of Text A?<br>A) To complain &nbsp; B) To inform and invite &nbsp; C) To instruct on rules", "[1 Mark]"),
          ("State the date and opening times of the Open Evening.", "[2 Marks]"),
          ("List two vocational pathways offered by Westgate College.", "[2 Marks]"),
          ("Why has the author used bold bullet points in the middle of Text A?", "[1 Mark]"),
          ("Identify two ways an applicant can contact Westgate College.", "[2 Marks]"),
          ("According to the text, what will be available in the cafeteria?", "[1 Mark]"),
          ("Explain what you should do if you want to speak with a careers advisor.", "[1 Mark]")]),

        ("Mock Examination 2", "Greenline Logistics Safety & Staff Update",
         '''<h3>Text B: Greenline Distribution Warehouse Policy Memo</h3>
            <p><strong>To:</strong> All Warehouse Operatives and Shift Supervisors<br>
            <strong>From:</strong> Sandra Higgins (Head of Health &amp; Safety)<br>
            <strong>Date:</strong> Monday 10 November 2026<br>
            <strong>Subject:</strong> Winter Safety Protocols &amp; Heating Maintenance</p>
            <p>As winter temperatures drop, please take note of important changes across our distribution bays:</p>
            <ul>
              <li><strong>Thermal Workwear:</strong> Winter fleece jackets and insulated gloves are now available from the equipment store.</li>
              <li><strong>Pedestrian Gritting:</strong> Salt and grit bins outside Loading Bays 1 to 4 are refilled every morning at 06:00 am.</li>
              <li><strong>Heater Servicing:</strong> The overhead radiant heaters in Zone B will undergo maintenance on Wednesday 12 November between 12:00 pm and 2:00 pm.</li>
            </ul>
            <p>If you observe ice accumulation on walkways or notice a malfunctioning heater, please notify your team leader immediately or call extension 312.</p>''',
         [("What is the primary purpose of Text B?<br>A) To advertise jackets &nbsp; B) To inform staff of safety updates &nbsp; C) To review a cafeteria", "[1 Mark]"),
          ("Who wrote this safety memo, and what is her job title?", "[2 Marks]"),
          ("At what time are the salt and grit bins refilled each morning?", "[1 Mark]"),
          ("When will overhead heaters in Zone B be serviced?", "[2 Marks]"),
          ("What two items of thermal workwear can staff collect from the store?", "[2 Marks]"),
          ("Why does the memo use a bulleted list?", "[1 Mark]"),
          ("What telephone extension should staff call to report a malfunctioning heater?", "[1 Mark]")]),

        ("Mock Examination 3", "St Jude Healthcare Trust Community Clinic",
         '''<h3>Text C: St Jude Healthcare Drop-In Health Clinic</h3>
            <p><strong>Protect Your Health This Season &mdash; Free Winter Vaccines</strong></p>
            <p>St Jude Community Health Hub is holding a free winter wellness clinic for local residents and key workers. No prior appointment is required.</p>
            <p><strong>Clinic Details:</strong></p>
            <ul>
              <li><strong>Dates:</strong> Saturday 5 December and Sunday 6 December.</li>
              <li><strong>Opening Hours:</strong> 09:00 am to 4:00 pm daily.</li>
              <li><strong>Services:</strong> Free flu immunisations, blood pressure checks, and free dietary advice.</li>
            </ul>
            <p>Please bring proof of address and your NHS number if available. Free parking is available in the visitors' car park at the rear of the building. Wheelchair access is provided via the main ramp entrance.</p>
            <p><strong>Contact:</strong> clinic@stjudehealth.nhs.uk | <strong>Tel:</strong> 0161 883 0450.</p>''',
         [("What is the main purpose of Text C?", "[1 Mark]"),
          ("On which two dates is the drop-in clinic open?", "[2 Marks]"),
          ("Name two free services available at the clinic.", "[2 Marks]"),
          ("What two pieces of information should visitors bring with them?", "[2 Marks]"),
          ("Where is free parking located for clinic visitors?", "[1 Mark]"),
          ("How can wheelchair users enter the building?", "[1 Mark]"),
          ("State the email address given for contact inquiries.", "[1 Mark]")])
    ]

    for m_idx, (m_title, m_context, reading_text, questions) in enumerate(mocks_data, 1):
        m_start = 68 + (m_idx - 1) * 4

        q_p1 = "".join(["<div style='margin-bottom:6px; font-size:7.8pt;'><strong>Q" + str(i+1) + ":</strong> " + q[0] + " <span class='mark-badge' style='float:right;'>" + q[1] + "</span><div style='border-bottom:1px solid #cbd5e1; height:18px; margin-top:2px;'></div></div>" for i, q in enumerate(questions[:4])])
        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{m_title} &bull; Component 1: Reading (Part 1)</div>
  </div>

  <h2>{m_title} &mdash; Component 1: Reading</h2>
  <div class="card-exam" style="padding:6px 10px; margin-bottom:6px; font-size:7.8pt;">
    <strong>Time Allowed:</strong> 45 Minutes &bull; <strong>Total Marks:</strong> 15 Marks &bull; Answer all questions using Text below.
  </div>

  <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:8px 12px; font-size:8pt; line-height:1.4; margin-bottom:8px;">
    {reading_text}
  </div>

  <div class="card-practice" style="padding:6px 10px;">
    <h3 style="margin:0 0 6px 0; font-size:8.5pt;">Comprehension Questions (1 to 4):</h3>
    {q_p1}
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {m_start}</div>
  </div>
</div>
''')

        q_p2 = "".join(["<div style='margin-bottom:6px; font-size:7.8pt;'><strong>Q" + str(i+5) + ":</strong> " + q[0] + " <span class='mark-badge' style='float:right;'>" + q[1] + "</span><div style='border-bottom:1px solid #cbd5e1; height:18px; margin-top:2px;'></div></div>" for i, q in enumerate(questions[4:])])
        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{m_title} &bull; Component 1: Reading (Part 2)</div>
  </div>

  <h2>{m_title} &mdash; Reading Questions &amp; Writing Overview</h2>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:8px;">
    <h3 style="margin:0 0 6px 0; font-size:8.5pt;">Comprehension Questions (5 to 7):</h3>
    {q_p2}
  </div>

  <div class="card-concept" style="border-left-color:#881337;">
    <h3 style="color:#881337; margin-top:0;">Component 2: Writing Examination Instructions</h3>
    <p style="margin:0; font-size:8pt;">Component 2 assesses your written English across two practical tasks:</p>
    <ul style="margin:4px 0 0 14px; padding:0; font-size:8pt;">
      <li><strong>Task 1 (8 Marks):</strong> Short workplace incident note or shift log form.</li>
      <li><strong>Task 2 (12 Marks):</strong> Structured professional email or formal letter (70–100 words).</li>
    </ul>
    <p style="margin:4px 0 0 0; font-size:7.5pt; color:#64748b;">Turn to <strong>Pages {m_start+2} and {m_start+3}</strong> to plan and write your responses.</p>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {m_start+1}</div>
  </div>
</div>
''')

        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{m_title} &bull; Component 2: Writing (Task 1)</div>
  </div>

  <h2>Task 1: Workplace Incident Log Note (8 Marks)</h2>
  
  <div class="card-exam" style="padding:6px 10px; margin-bottom:6px;">
    <strong>Scenario:</strong> You work at {m_context}. At 10:15 am, you discovered a faulty electrical socket in the staff office that was sparking. You switched off the socket at the main wall switch, placed a warning sticker on it, and reported it to your supervisor, David Clark.
    <p style="margin:4px 0 0 0; font-weight:700;">Write a factual log note to record this incident. You must include:</p>
    <ul style="margin:2px 0 0 14px; padding:0; font-size:8pt;">
      <li>The date, time, and exact location of the issue.</li>
      <li>A clear description of what happened.</li>
      <li>The immediate actions you took to keep staff safe.</li>
    </ul>
  </div>

  <div style="background:#ffffff; border:1.5px solid #881337; border-radius:5px; padding:10px; margin-bottom:6px;">
    <div style="font-weight:700; font-size:8pt; color:#881337; margin-bottom:4px; text-transform:uppercase;">Official Workplace Incident Log:</div>
    <div class="grid-2" style="margin-bottom:6px;">
      <div style="font-size:7.5pt;"><strong>Date:</strong> _____________________</div>
      <div style="font-size:7.5pt;"><strong>Time:</strong> _____________________</div>
    </div>
    <div style="font-size:7.5pt; margin-bottom:6px;"><strong>Location / Department:</strong> _______________________________________________</div>
    <div style="font-size:7.5pt; margin-bottom:4px;"><strong>Incident Description &amp; Actions Taken (Full Sentences):</strong></div>
    <div class="workspace-ruled" style="min-height:160px; margin:4px 0;"></div>
    <div class="grid-2" style="margin-top:6px; font-size:7.5pt;">
      <div><strong>Reporting Staff Name:</strong> ___________________</div>
      <div><strong>Signature:</strong> ___________________</div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {m_start+2}</div>
  </div>
</div>
''')

        pages.append(f'''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">{m_title} &bull; Component 2: Writing (Task 2)</div>
  </div>

  <h2>Task 2: Professional Email (12 Marks)</h2>

  <div class="card-exam" style="padding:6px 10px; margin-bottom:6px;">
    <strong>Scenario:</strong> Write a professional email to your training manager, Ms Karen Taylor (karen.taylor@apexskills.co.uk), requesting enrolment on an upcoming first aid training workshop on Friday 28 November.
    <p style="margin:4px 0 0 0; font-weight:700;">In your email (approximately 70 to 100 words), you must:</p>
    <ul style="margin:2px 0 0 14px; padding:0; font-size:8pt;">
      <li>Explain why you would like to attend the first aid course.</li>
      <li>State how this training will help you in your current job role.</li>
      <li>Ask for details about start times, parking, and dress code.</li>
    </ul>
  </div>

  <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:5px; padding:8px 10px; margin-bottom:6px;">
    <div style="font-size:7.8pt; line-height:1.6; border-bottom:1px solid #e2e8f0; padding-bottom:4px; margin-bottom:6px;">
      <strong>To:</strong> karen.taylor@apexskills.co.uk<br>
      <strong>Subject:</strong> ___________________________________________________________
    </div>
    <div class="workspace-ruled" style="min-height:220px; margin:4px 0;"></div>
  </div>

  <div class="card-tip" style="padding:4px 8px; font-size:7.5pt;">
    <strong>Final Reminder:</strong> Check that you opened with 'Dear Ms Taylor,' and closed with 'Kind regards,' followed by your full name.
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page {m_start+3}</div>
  </div>
</div>
''')

    # -------------------------------------------------------------
    # PAGES 80-83: COMPREHENSIVE EXPLANATORY ANSWER KEYS (4 Pages)
    # -------------------------------------------------------------
    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Complete Answer Key &bull; Units 1 to 10</div>
  </div>

  <h2>Explanatory Answer Key: Units 1 to 10</h2>
  <div class="grid-2" style="font-size:7.5pt;">
    <div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 1: Purpose of Texts (Page 5)</strong><br>
        1. B) To persuade [1m].<br>
        2. To instruct [1m].<br>
        3. To inform staff about the Bank Holiday closure [1m].<br>
        4. It uses positive adjectives ('best', 'deals') and exclamation marks [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 2: Organisational Features (Page 7)</strong><br>
        1. Any two: Headings, subheadings, bullet points, images [2m].<br>
        2. To break the text into clear sections so info is easy to find [1m].<br>
        3. Bold text highlights crucial danger/warning warnings [1m].<br>
        4. It explains what the photo shows [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 3: Workplace Signs &amp; Notices (Page 9)</strong><br>
        1. C) Mandatory action (must do) [1m].<br>
        2. Loading Bay A [1m].<br>
        3. B) Keep clear [1m].<br>
        4. Report it immediately to the site manager or supervisor [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 4: Following Instructions (Page 11)</strong><br>
        1. Check the water level [1m].<br>
        2. Press the red power button [1m].<br>
        3. Turn counter-clockwise until it clicks [1m].<br>
        4. Chronological order ensures safety and correct operation [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 5: Alphabetical Order &amp; Dictionaries (Page 13)</strong><br>
        1. Apron, Boiler, Delivery, Helmet, Safety [2m].<br>
        2. Packet, Pallet, Paper, Parcel, Plastic [2m].<br>
        3. Guide words tell you the first and last words on that dictionary page [1m].
      </div>
    </div>

    <div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 6: Comparing Two Short Texts (Page 15)</strong><br>
        1. Both offer free parking / Both open at 09:00 am [2m].<br>
        2. Text A charges £15; Text B is free for students [2m].<br>
        3. Text B provides an online booking link [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 7: Sentence Basics (Page 17)</strong><br>
        1. Subject: 'The electrician' [1m]; Verb: 'repaired' [1m].<br>
        2. B is a complete sentence (A is a fragment missing a verb) [1m].<br>
        3. Model: The nurse checked the patient's temperature. [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 8: Capital Letters &amp; MINTS (Page 19)</strong><br>
        1. <strong>M</strong>onth (June), <strong>I</strong> (myself), <strong>N</strong>ame (Sarah), <strong>T</strong>itle (Dr), <strong>S</strong>tart of sentence [2m].<br>
        2. Corrected: On Wednesday, David and I visited Manchester. [3m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 9: End Punctuation (Page 21)</strong><br>
        1. Question mark (?) [1m].<br>
        2. Exclamation mark (!) [1m].<br>
        3. Full stop (.) [1m].<br>
        4. Model: Where is the nearest fire exit? [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 10: Commas in Lists &amp; Time Openers (Page 23)</strong><br>
        1. Corrected: Please bring gloves, goggles, a hard hat, and boots. [2m].<br>
        2. Corrected: Yesterday morning, the delivery truck arrived late. [2m].
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 80</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Complete Answer Key &bull; Units 11 to 20</div>
  </div>

  <h2>Explanatory Answer Key: Units 11 to 20</h2>
  <div class="grid-2" style="font-size:7.5pt;">
    <div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 11: Compound Sentences (Page 25)</strong><br>
        1. Model: The warehouse was cold, but the heating was fixed quickly. [2m].<br>
        2. Conjunction 'so': I missed the bus, so I was late for my shift. [2m].<br>
        3. Conjunction 'or': You can pay by card, or you can pay with cash. [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 12: Complex Sentences (Page 27)</strong><br>
        1. Model: We closed the loading bay because it was snowing heavily. [2m].<br>
        2. Model: Although he was tired, he finished his stock count. [2m].<br>
        3. Model: If you smell gas, turn off the main valve. [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 13: Verb Tenses (Page 29)</strong><br>
        1. saw [1m].<br>
        2. wrote [1m].<br>
        3. went [1m].<br>
        4. Model: She completed her training course last Friday. [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 14: Subject-Verb Agreement (Page 31)</strong><br>
        1. The boxes <strong>are</strong> on the shelf. [1m].<br>
        2. He <strong>was</strong> working late. [1m].<br>
        3. They <strong>have</strong> finished their lunch. [1m].<br>
        4. She <strong>does</strong> her work carefully. [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 15: Prefixes &amp; Suffixes (Page 33)</strong><br>
        1. uncomfortable [1m]; disconnect [1m].<br>
        2. helpful [1m]; careless [1m]; quickly [1m].<br>
        3. Prefix changes the root meaning; suffix changes the word class [2m].
      </div>
    </div>

    <div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 16: Plurals &amp; Homophones (Page 35)</strong><br>
        1. boxes, cities, lorries, keys, knives [2m].<br>
        2. their (belonging to them), there (location), they're (they are) [2m].<br>
        3. hear vs here: I can hear you from over here. [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 17: Top 100 Spelling Words (Page 37)</strong><br>
        1. because, Tuesday, address, colleague, calendar [2m].<br>
        2. through, thought, enough [2m].<br>
        3. Double consonant drill: difficult, happen, lesson [1m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 18: Form Filling (Page 39)</strong><br>
        1. Surname = family name; Forename = first name [1m].<br>
        2. Date format: DD/MM/YYYY [1m].<br>
        3. Block capitals ensure handwriting is easily scanned [1m].<br>
        4. Signature verifies that all statements are true [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 19: Workplace Notes &amp; Logs (Page 41)</strong><br>
        1. Clarity, date/time, exact problem, who was informed [2m].<br>
        2. Full sentences prevent misunderstandings during shifts [2m].
      </div>
      <div class="card-practice" style="margin-bottom:5px;">
        <strong>Unit 20: Professional Workplace Emails (Page 43)</strong><br>
        1. Clear subject line, polite greeting, clear paragraphs, courteous close [3m].<br>
        2. 'Kind regards' or 'Best regards' [1m].
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 81</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Complete Answer Key &bull; Workshops 1 to 8</div>
  </div>

  <h2>Applied Writing Workshops (1 to 8) &mdash; Marking Criteria</h2>
  <div class="grid-2" style="font-size:7.5pt;">
    <div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 1: Incident Log (Page 45)</strong><br>
        &bull; <strong>Format [2m]:</strong> Date, time, room, reporter name filled.<br>
        &bull; <strong>Content [3m]:</strong> Describes soap spill, Mark's bruised knee, warning cone placed, mop used.<br>
        &bull; <strong>SPaG [3m]:</strong> Past tense verbs ('slipped', 'cleaned'), MINTS capitals, full stops.
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 2: Shift Handover &amp; Maintenance (Page 47)</strong><br>
        &bull; <strong>Format [2m]:</strong> Refrigerator ID, temperature reading recorded.<br>
        &bull; <strong>Content [3m]:</strong> Explains 11°C hazard, food relocated to cold room, engineer requested.<br>
        &bull; <strong>SPaG [3m]:</strong> Accurate spelling of 'refrigerator', 'temperature', 'maintenance'.
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 3: Leave Request Email (Page 49)</strong><br>
        &bull; <strong>Format [2m]:</strong> To, subject line, 'Dear Mr Evans', sign-off.<br>
        &bull; <strong>Content [3m]:</strong> Dates (14–16 May), sister's wedding, Sarah covering shifts.<br>
        &bull; <strong>SPaG [3m]:</strong> MINTS (Wednesday, May, Manchester), polite modal verbs ('would like to').
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 4: Customer Return Form (Page 51)</strong><br>
        &bull; <strong>Format [2m]:</strong> Receipt number, customer contact details.<br>
        &bull; <strong>Content [3m]:</strong> Explains faulty electric kettle, inspected, replacement kettle issued.<br>
        &bull; <strong>SPaG [3m]:</strong> Clear factual sentences, accurate spelling.
      </div>
    </div>

    <div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 5: Safety Notice &amp; Poster (Page 53)</strong><br>
        &bull; <strong>Format [2m]:</strong> Bold heading banner, clear target group.<br>
        &bull; <strong>Content [3m]:</strong> High-vis vests, 5 mph limit, green walkways, horn sounding.<br>
        &bull; <strong>SPaG [3m]:</strong> Imperative verbs ('Wear', 'Obey', 'Keep', 'Report').
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 6: Formal Application Letter (Page 55)</strong><br>
        &bull; <strong>Format [2m]:</strong> Two addresses, date, 'Dear Admissions Team', 'Yours sincerely'.<br>
        &bull; <strong>Content [3m]:</strong> Digital skills needed for care job, photo ID attached.<br>
        &bull; <strong>SPaG [3m]:</strong> Complex sentences ('Although', 'Because'), zero run-ons.
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 7: Informational Staff Leaflet (Page 57)</strong><br>
        &bull; <strong>Format [2m]:</strong> Subheadings, bullet points, helpline phone.<br>
        &bull; <strong>Content [3m]:</strong> Hours, ID badge policy, canteen, IT support contact.<br>
        &bull; <strong>SPaG [3m]:</strong> Welcoming, professional instructional register.
      </div>
      <div class="card-practice" style="margin-bottom:6px;">
        <strong>Workshop 8: Service Review &amp; Rating (Page 59)</strong><br>
        &bull; <strong>Format [2m]:</strong> Catchy title, 4-star rating displayed.<br>
        &bull; <strong>Content [3m]:</strong> Food quality praised, minor wait time noted, recommendation.<br>
        &bull; <strong>SPaG [3m]:</strong> Evaluative vocabulary ('delicious', 'friendly', 'recommend').
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 82</div>
  </div>
</div>
''')

    pages.append('''
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Entry Level 3</div>
    <div class="page-header-strand">Complete Mark Schemes &bull; Mock Exams 1, 2 &amp; 3</div>
  </div>

  <h2>Mock Examination Mark Schemes &amp; Pass Criteria</h2>
  <div style="font-size:7.2pt;">
    <div class="card-exam" style="margin-bottom:5px; border-left-color:#881337;">
      <strong>Mock Exam 1 Mark Scheme (Pages 68–71)</strong><br>
      &bull; <strong>Reading (15m):</strong> Q1: B [1m]; Q2: Thursday 22 October, 5:00 pm to 8:00 pm [2m]; Q3: Two: Care, Logistics, Business [2m]; Q4: Makes courses easy to read [1m]; Q5: Website (www.westgatecollege.ac.uk) OR Phone (0121 496 0120) [2m]; Q6: Light refreshments [1m]; Q7: Attend open evening to meet advisors [1m].<br>
      &bull; <strong>Writing Task 1 (8m):</strong> Factual log of sparking socket at 10:15 am, turned off at wall, reported to David Clark [4m Content, 4m SPaG].<br>
      &bull; <strong>Writing Task 2 (12m):</strong> Email to Ms Taylor requesting first aid course on 28 Nov; explains job role benefits; asks start time, parking, dress code [3m Format, 5m Content, 4m SPaG].
    </div>

    <div class="card-exam" style="margin-bottom:5px; border-left-color:#881337;">
      <strong>Mock Exam 2 Mark Scheme (Pages 72–75)</strong><br>
      &bull; <strong>Reading (15m):</strong> Q1: B [1m]; Q2: Sandra Higgins, Head of Health &amp; Safety [2m]; Q3: 06:00 am [1m]; Q4: Wednesday 12 November, 12:00 pm to 2:00 pm [2m]; Q5: Thermal fleece jackets, insulated gloves [2m]; Q6: To make changes clear and easy to follow [1m]; Q7: Extension 312 [1m].<br>
      &bull; <strong>Writing Task 1 (8m):</strong> Incident log of broken pallet/conveyor belt; safety actions; notification of team leader [4m Content, 4m SPaG].<br>
      &bull; <strong>Writing Task 2 (12m):</strong> Email/letter regarding warehouse winter equipment orders; sizes; delivery dates [3m Format, 5m Content, 4m SPaG].
    </div>

    <div class="card-exam" style="margin-bottom:5px; border-left-color:#881337;">
      <strong>Mock Exam 3 Mark Scheme (Pages 76–79)</strong><br>
      &bull; <strong>Reading (15m):</strong> Q1: To inform and invite residents to a free winter clinic [1m]; Q2: Saturday 5 Dec, Sunday 6 Dec [2m]; Q3: Two: Flu vaccines, blood pressure checks, dietary advice [2m]; Q4: Proof of address, NHS number [2m]; Q5: Visitors' car park at rear [1m]; Q6: Main ramp entrance [1m]; Q7: clinic@stjudehealth.nhs.uk [1m].<br>
      &bull; <strong>Writing Task 1 (8m):</strong> Health clinic incident log or visitor feedback log with date, time, actions taken [4m Content, 4m SPaG].<br>
      &bull; <strong>Writing Task 2 (12m):</strong> Professional email to clinic supervisor volunteering for weekend clinic; availability, previous experience, uniform size [3m Format, 5m Content, 4m SPaG].
    </div>

    <div class="card-tip" style="padding:4px 8px; font-size:7.5pt; margin-top:4px;">
      <strong>Pass Threshold:</strong> The official pass standard across Reading (15 marks) and Writing (20 marks) is approximately <strong>65% to 70%</strong> (23 out of 35 marks overall).
    </div>
  </div>

  <div class="page-footer">
    <div>Functional Skills English Entry Level 3 &bull; Core Literacy Guide</div>
    <div class="page-num">Page 83</div>
  </div>
</div>
''')

    # -------------------------------------------------------------
    # PAGE 84: BACK COVER
    # -------------------------------------------------------------
    pages.append(f'''
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>
''')

    full_html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>English Entry Level 3 Core Literacy Guide</title>
{SHARED_CSS}
<style>
  :root {{
    --theme: #881337;
    --accent: #fde047;
  }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>'''

    pdf_filename = "MasterFunctionalSkills_English_Entry_Level_3_Core_Guide.pdf"
    count = render_book_to_pdf(full_html, pdf_filename)
    return count

if __name__ == "__main__":
    build_english_e3_book()
