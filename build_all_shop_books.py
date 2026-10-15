#!/usr/bin/env python3
"""
build_all_shop_books.py
Generates official publication-grade Front Covers, Back Covers, and 3D Book Mockups
for ALL books in the Master Functional Skills shop.

Strictly adheres to the Level-Based & Subject Color Scheme:
• Entry Level 3: Rich Crimson & Cherry Red (#991b1b / #881337)
• Level 1 English: Deep Forest Teal Green (#0c4e45)
• Level 1 Maths: Distinct Vibrant Emerald / Jade Green (#047857)
• Level 2 English: Classic Oxford Royal Blue (#003366)
• Level 2 Maths: Distinct Deep Midnight Sapphire Navy (#002046 / #002855) with Sky Blue (#38bdf8)
• Digital Skills (EDSQ): High-Tech Cyber Midnight (#090d16) with Electric Neon Cyan (#00e5ff)
• SPaG Specialist: Imperial Royal Violet (#581c87) with Warm Gold
• BKSB Remediation: Electric Cobalt (#1d4ed8) & Safety Amber (#f59e0b)
• Mock Exam Packs: Official Exam Slate (#18181b)
"""

import os
import subprocess
from PIL import Image, ImageFilter, ImageDraw

PROJECT_DIR = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
BOOKS_IMG_DIR = os.path.join(PROJECT_DIR, "assets", "img", "books")
os.makedirs(BOOKS_IMG_DIR, exist_ok=True)

TEXTURE_WRITING = "/home/subi/Nextcloud/NVMe469GB/Work/Pearson Writing Guide/Cover Mockups/cover_writing_hands.jpg"
TEXTURE_MATHS = os.path.join(BOOKS_IMG_DIR, "cover_maths_calculations.jpg")
TEXTURE_DIGITAL = os.path.join(BOOKS_IMG_DIR, "cover_digital_tech.jpg")
TEXTURE_BKSB = os.path.join(BOOKS_IMG_DIR, "cover_bksb_diagnostic.jpg")

def get_book_texture(book):
    book_id = book.get("id", "").lower()
    if "maths" in book_id or "math" in book_id or "numeracy" in book_id:
        return TEXTURE_MATHS
    elif "digital" in book_id or "edsq" in book_id or "ict" in book_id:
        return TEXTURE_DIGITAL
    elif "bksb" in book_id or "remediation" in book_id or "diagnostic" in book_id:
        return TEXTURE_BKSB
    else:
        return TEXTURE_WRITING

BOOK_SPECS = [
    # =========================================================================
    # ENTRY LEVEL 3: RED / CRIMSON THEME (#991b1b / #881337)
    # =========================================================================
    {
        "id": "maths_e3_core",
        "level_num": "E3",
        "level_label": "ENTRY 3",
        "is_white": False,
        "bg_color": "#991b1b",          # Rich Crimson Red for Entry 3
        "accent_color": "#fbbf24",      # Warm Honey Gold
        "gold_accent": "#fde047",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS MATHEMATICS",
        "knockout_word": "FOUNDATIONS",
        "main_title_1": "MATHEMATICS",
        "main_title_2": "ENTRY LEVEL 3",
        "subtitle": "Step-by-step visual numeracy foundations for Entry Level 3 candidates",
        "edition_badge": "ENTRY LEVEL 3 CORE GUIDE • VISUAL STEPS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • ENTRY LEVEL 3",
        "badge_pills": ["Entry 3 Spec", "Step-by-Step", "Number & Money", "Visual Models"],
        "back_heading": "Build solid numeracy foundations and achieve Entry Level 3",
        "back_desc": "Engineered for adult learners, apprentices, and ESOL candidates building foundational math skills. Takes you step-by-step through whole numbers up to 1000, addition, subtraction, multiplication grids, division remainders, decimal money, and basic clock time.",
        "key_features": [
            ("Dyslexia-Friendly Layout", "High-contrast visual models, chunked explanations, and generous font spacing."),
            ("Whole Numbers & Place Value", "Clear visual place value charts (Hundreds, Tens, Units) and number line jumps."),
            ("Everyday Practical Arithmetic", "Real-world calculations: shopping change, bus timetables, and measuring recipes."),
            ("Illustrated Step-by-Step Models", "Step-by-step breakdowns showing learners exactly how to complete each calculation."),
            ("Confidence-Building Checkpoints", "Self-check progress grids at the end of each unit to verify mastery.")
        ],
        "isbn": "978-1-912345-78-4",
        "companion_note_title": "Progress to Functional Skills Level 1:",
        "companion_note_text": "Once Entry Level 3 is mastered, learners transition directly to the <em>Functional Skills Maths Level 1 Core Study Guide</em> for accredited Level 1 qualification."
    },
    {
        "id": "english_e3_core",
        "level_num": "E3",
        "level_label": "ENTRY 3",
        "is_white": False,
        "bg_color": "#881337",          # Deep Rosewood / Crimson Red for Entry 3
        "accent_color": "#fde047",      # Bright Sunshine Gold
        "gold_accent": "#fbbf24",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH",
        "knockout_word": "LITERACY",
        "main_title_1": "ENGLISH SKILLS",
        "main_title_2": "ENTRY LEVEL 3",
        "subtitle": "Clear sentence building, workplace reading, and basic writing guide",
        "edition_badge": "ENTRY LEVEL 3 CORE GUIDE • STEP-BY-STEP",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • ENTRY LEVEL 3",
        "badge_pills": ["Entry 3 Spec", "Sentence Building", "Workplace Notes", "Spelling Rules"],
        "back_heading": "Master fundamental reading and writing with complete confidence",
        "back_desc": "The supportive step-by-step guide for Entry Level 3 English candidates. Covers compound sentence formation with connectives (and, but, because), fundamental punctuation, high-frequency spelling lists, and simple workplace emails, notes, and forms.",
        "key_features": [
            ("Scaffolded Sentence Construction", "Guided frameworks to write clear, grammatically accurate sentences."),
            ("Practical Everyday Formats", "Short emails to colleagues, community messages, filling out application forms."),
            ("Essential Punctuation", "Capital letters, full stops, question marks, and commas in lists made simple."),
            ("High-Frequency Spelling Banks", "Master the 100 most common words tested in Entry Level 3 exams."),
            ("Reading Comprehension Strategies", "Extracting key facts from notices, signs, schedules, and instructions.")
        ],
        "isbn": "978-1-912345-79-1",
        "companion_note_title": "Gateway to Level 1 English:",
        "companion_note_text": "Prepares candidates with the core literacy foundation required before embarking on the <em>Functional Skills English Level 1 Writing Core Guide</em>."
    },

    # =========================================================================
    # LEVEL 1: GREEN THEME (Deep Teal Green for English, Emerald Jade for Maths)
    # =========================================================================
    {
        "id": "maths_l1_core",
        "level_num": "1",
        "level_label": "LEVEL 1",
        "is_white": False,
        "bg_color": "#047857",          # Distinct Vibrant Emerald / Jade Green for Maths L1
        "accent_color": "#facc15",      # Warm Golden Yellow
        "gold_accent": "#fde047",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS MATHEMATICS",
        "knockout_word": "NUMERACY",
        "main_title_1": "MATHEMATICS",
        "main_title_2": "FOUNDATIONS",
        "subtitle": "A step-by-step visual guide to building confidence and passing Level 1 Maths",
        "edition_badge": "CORE REVISION GUIDE • VISUAL METHODS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 1",
        "badge_pills": ["Level 1 Spec", "Emerald Series", "Non-Calc Skills", "Real-Life Scenarios"],
        "back_heading": "Build solid numerical confidence and pass Level 1 Maths",
        "back_desc": "Tailored specifically for Level 1 candidates. Breaks down daunting arithmetic into friendly, visual steps: place value, times tables, decimals, fractions of amounts, simple percentages, metric unit conversions, perimeter, area, and bar charts.",
        "key_features": [
            ("Visual, Dyslexia-Friendly Layout", "Clear diagrams, color-coded arithmetic steps, and simplified chunked explanations."),
            ("Non-Calculator Mental Strategies", "Multiplication grids, division remainders, and fraction models that demystify Section A."),
            ("Everyday Practical Contexts", "Real-world problems: budgeting wages, train timetables, shopping deals, tiling and fencing."),
            ("Clear Step-by-Step Exemplars", "Over 50 illustrated model answers demonstrating how to lay out workings cleanly."),
            ("Key Formulas & Conversions", "Quick recall conversion charts for length (mm/cm/m/km), weight (g/kg), and time.")
        ],
        "isbn": "978-1-912345-82-1",
        "companion_note_title": "Pair with the Level 1 Practice Companion:",
        "companion_note_text": "Strengthen your numeracy skills by combining this Core Guide with the <em>Functional Skills Maths Level 1 Companion Practice Workbook</em> for structured, stepped exercises."
    },
    {
        "id": "maths_l1_companion",
        "level_num": "1",
        "level_label": "LEVEL 1",
        "is_white": True,
        "bg_color": "#ffffff",
        "accent_color": "#047857",      # Matching Emerald Green accent
        "comp_accent": "#059669",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS MATHEMATICS",
        "knockout_word": "PRACTICE",
        "main_title_1": "PRACTICE",
        "main_title_2": "COMPANION",
        "subtitle": "Guided calculation frames & real-life workplace maths scenarios",
        "edition_badge": "COMPANION PRACTICE WORKBOOK • STEPPED DRILLS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 1",
        "badge_pills": ["Scaffolded Grids", "Real Scenarios", "Step-by-Step", "Answer Key Included"],
        "back_heading": "The supportive independent practice workbook for Level 1 Maths",
        "back_desc": "Designed to build learner confidence through scaffolded calculations. Eliminates math anxiety with guided working frames, intermediate checkpoints, and realistic workplace calculations.",
        "key_features": [
            ("Scaffolded Calculation Frames", "Step-by-step boxes that guide you through every calculation without feeling overwhelmed."),
            ("Real-Life Workplace Tasks", "Practical scenarios: calculating hours and pay, stock-taking, decorating measurements, and bills."),
            ("Essential Number Workouts", "Targeted drills for addition, subtraction, multiplication, and non-calculator fractions."),
            ("Clear Visual Charts & Tables", "Hands-on practice reading timetables, tally charts, pictograms, and simple graphs."),
            ("Complete Worked Answers Included", "Full answers provided in the back for self-checking or tutor feedback.")
        ],
        "isbn": "978-1-912345-83-8",
        "companion_note_title": "Use Alongside the Level 1 Core Guide:",
        "companion_note_text": "Study the methods in the <em>Functional Skills Maths Level 1 Core Study Guide</em> first, then practice independently in this companion workbook."
    },
    {
        "id": "level1_core",
        "level_num": "1",
        "level_label": "LEVEL 1",
        "is_white": False,
        "bg_color": "#0c4e45",          # Classic Deep Forest Teal Green for English L1
        "accent_color": "#ffe500",      # Sunshine Yellow
        "gold_accent": "#facc15",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH",
        "knockout_word": "WRITING",
        "main_title_1": "WRITING",
        "main_title_2": "SKILLS",
        "subtitle": "A step-by-step guide to a high Level 1 writing score",
        "edition_badge": "CORE REVISION GUIDE • MODEL ANSWERS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 1",
        "badge_pills": ["All Formats", "Model Answers", "SPaG Rules", "Assessment Criteria"],
        "back_heading": "Everything you need to master Functional Skills English Level 1 Writing",
        "back_desc": "Designed specifically for candidates preparing for Functional Skills English Level 1 examination. Takes you step-by-step through every required writing format with exam-standard tasks and fully annotated high-scoring model answers.",
        "key_features": [
            ("Core Writing Formats", "Formal letters, emails, community articles, reviews, information leaflets."),
            ("11 Full Exemplar Model Answers", "Step-by-step deconstructions of top-scoring student responses."),
            ("Targeted SPaG & Vocabulary Lists", "Essential Level 1 spelling lists, punctuation rules, and vocabulary banks."),
            ("Official Assessment Criteria", "Detailed mark scheme breakdowns: Composition (15 marks) + SPaG (10 marks).")
        ],
        "isbn": "978-1-912345-67-8",
        "companion_note_title": "Pair with the Practice Companion Booklet:",
        "companion_note_text": "For complete exam readiness, pair this Core Study Guide with the <em>Level 1 Writing Practice Companion Booklet</em>, offering 22 additional independent exam tasks with zero model answers."
    },
    {
        "id": "level1_companion",
        "level_num": "1",
        "level_label": "LEVEL 1",
        "is_white": True,
        "bg_color": "#ffffff",
        "accent_color": "#0c4e45",      # Forest Teal accent
        "comp_accent": "#0c4e45",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH",
        "knockout_word": "PRACTICE",
        "main_title_1": "PRACTICE",
        "main_title_2": "COMPANION",
        "subtitle": "22 independent exam tasks for complete mock assessment",
        "edition_badge": "PRACTICE COMPANION BOOKLET • ZERO MODEL ANSWERS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 1",
        "badge_pills": ["22 Tasks", "Zero Models", "Exam Layout", "Mark Rubrics"],
        "back_heading": "The essential independent practice companion for Level 1 Writing",
        "back_desc": "The official companion to the Core Revision Guide. Provides 22 brand-new, unseen exam-standard writing tasks across all assessment formats with zero model answers — designed specifically for homework and mock examinations.",
        "key_features": [
            ("22 Unseen Exam Practice Tasks", "Two complete, authentic writing tasks for every one of the Functional Skills formats."),
            ("Zero Model Answers Provided", "Engineered specifically for timed exam conditions and diagnostic progress tracking."),
            ("Full Mark Scheme Rubrics", "Complete assessment grids for Composition (15 Marks) and SPaG (10 Marks)."),
            ("Task Planning & Self-Check Grids", "Pre-writing planning spaces and proofreading checklists tailored to every format.")
        ],
        "isbn": "978-1-912345-68-5",
        "companion_note_title": "Use Alongside the Core Revision Guide:",
        "companion_note_text": "Study the exemplar models first in the Core Revision Guide, then test your skills independently with these 22 tasks."
    },

    # =========================================================================
    # LEVEL 2: BLUE THEME (Classic Oxford Royal Blue for English, Deep Midnight Sapphire for Maths)
    # =========================================================================
    {
        "id": "maths_l2_core",
        "level_num": "2",
        "level_label": "LEVEL 2",
        "is_white": False,
        "bg_color": "#002046",          # Distinct Deep Midnight Sapphire Navy for Maths L2
        "accent_color": "#38bdf8",      # Electric Sky Blue
        "gold_accent": "#f59e0b",       # Warm Amber Gold
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS MATHEMATICS",
        "knockout_word": "MATHEMATICS",
        "main_title_1": "MATHEMATICS",
        "main_title_2": "CORE STUDY GUIDE",
        "subtitle": "Complete 39-standard curriculum guide with Section A & Section B model solutions",
        "edition_badge": "CORE REVISION GUIDE • MODEL ANSWERS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 2",
        "badge_pills": ["39 Standards", "Sec A Non-Calc", "Sec B Calculator", "Worked Solutions"],
        "back_heading": "Everything you need to pass Functional Skills Maths Level 2",
        "back_desc": "The definitive preparation manual for candidates aiming for a pass at Level 2 (GCSE 4/C Equivalent). Master non-calculator mental arithmetic, multi-step compound calculations, fractions, decimals, percentages, perimeter, area, volume, scatter graphs, and probability.",
        "key_features": [
            ("All 39 Curriculum Standards", "Exhaustive coverage of Number, Measure & Shape, and Handling Data mapped to Pearson Edexcel and City & Guilds."),
            ("Section A Non-Calculator Strategy", "Fast-track mental arithmetic, grid multiplication, long division, and fraction manipulations."),
            ("Section B Multi-Step Problems", "Stepped breakdowns of 4-to-6 mark complex workplace scenarios showing exact method mark allocation."),
            ("Official Examiner Trap Alerts", "Highlighting frequent calculation blunders, unit omission errors, and rounding pitfalls."),
            ("Complete Worked Model Answers", "Every question includes full intermediate workings so you know exactly how marks are earned.")
        ],
        "isbn": "978-1-912345-80-7",
        "companion_note_title": "Pair with the Companion Practice Workbook:",
        "companion_note_text": "For extensive hands-on calculation practice, pair this Core Study Guide with the <em>Functional Skills Maths Level 2 Companion Practice Workbook</em> containing 120+ stepped drills and blank method workspaces."
    },
    {
        "id": "maths_l2_companion",
        "level_num": "2",
        "level_label": "LEVEL 2",
        "is_white": True,
        "bg_color": "#ffffff",
        "accent_color": "#002046",      # Sapphire Navy border
        "comp_accent": "#0284c7",      # Sky Blue accent
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS MATHEMATICS",
        "knockout_word": "PRACTICE",
        "main_title_1": "PRACTICE",
        "main_title_2": "COMPANION",
        "subtitle": "120+ stepped exam drills & full method mark workspaces",
        "edition_badge": "COMPANION PRACTICE WORKBOOK • STEPPED DRILLS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 2",
        "badge_pills": ["120+ Drills", "Method Workspaces", "Non-Calc & Calc", "Worked Solutions"],
        "back_heading": "The essential calculation practice companion for Maths Level 2",
        "back_desc": "Designed to accompany the Core Study Guide. Provides targeted problem-solving frames and dedicated calculation workspaces for every syllabus topic, training learners to secure every single method mark on exam day.",
        "key_features": [
            ("120+ Stepped Exam Drills", "Authentic workplace and life problem-solving questions calibrated to Level 2 exam standards."),
            ("Dedicated Method Working Boxes", "Structured calculation frames ensuring learners write down every intermediate step."),
            ("Targeted Weak-Spot Drills", "Specialist practice sections for percentages, ratio, compound interest, volume, and density."),
            ("Full Step-by-Step Mark Schemes", "Complete answer keys detailing precisely where method (M) and accuracy (A) marks are scored."),
            ("Self-Assessment Checklists", "Progress review grids to track topic mastery before sitting the official exam.")
        ],
        "isbn": "978-1-912345-81-4",
        "companion_note_title": "Use Alongside the Core Study Guide:",
        "companion_note_text": "This companion workbook is designed to be used alongside the <em>Functional Skills Maths Level 2 Core Study Guide</em>. Master the formulas and methods first, then complete these stepped workouts independently."
    },
    {
        "id": "level2_core",
        "level_num": "2",
        "level_label": "LEVEL 2",
        "is_white": False,
        "bg_color": "#003366",          # Classic Oxford Royal Blue for English L2
        "accent_color": "#fbbf24",      # Warm Academic Gold
        "gold_accent": "#f59e0b",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH",
        "knockout_word": "WRITING",
        "main_title_1": "WRITING",
        "main_title_2": "SKILLS",
        "subtitle": "A step-by-step guide to a high Level 2 writing score",
        "edition_badge": "CORE REVISION GUIDE • MODEL ANSWERS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 2",
        "badge_pills": ["All 11 Formats", "Model Answers", "Rhetoric & SPaG", "Exemplar Mark Schemes"],
        "back_heading": "Everything you need to master Functional Skills English Level 2 Writing",
        "back_desc": "The definitive preparation manual for candidates aiming for a pass at Level 2 (GCSE 4/C Equivalent). Master advanced organizational markers, persuasive rhetoric, sophisticated register, and complex sentence structures across all 11 exam formats.",
        "key_features": [
            ("All 11 Level 2 Formats", "Letters, Emails, Articles, Reports, Speeches, Reviews, Leaflets, Blogs, Contributions."),
            ("22 High-Challenge Exam Tasks", "Realistic workplace, civic, and academic scenarios calibrated to the Level 2 standard."),
            ("11 Full Exemplar Model Answers", "Comprehensive model answers demonstrating sophisticated vocabulary and varied syntax."),
            ("Full Mark Scheme Breakdown", "Exhaustive criteria for Composition & Effect (21 Marks) and SPaG (15 Marks).")
        ],
        "isbn": "978-1-912345-71-5",
        "companion_note_title": "Pair with the Practice Companion Booklet:",
        "companion_note_text": "For maximum exam confidence, use this Core Revision Guide alongside the <em>Level 2 Writing Practice Companion Booklet</em>."
    },
    {
        "id": "level2_companion",
        "level_num": "2",
        "level_label": "LEVEL 2",
        "is_white": True,
        "bg_color": "#ffffff",
        "accent_color": "#003366",      # Oxford Royal Blue accent
        "comp_accent": "#003366",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH",
        "knockout_word": "PRACTICE",
        "main_title_1": "PRACTICE",
        "main_title_2": "COMPANION",
        "subtitle": "22 independent exam tasks for complete mock assessment",
        "edition_badge": "PRACTICE COMPANION BOOKLET • ZERO MODEL ANSWERS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVEL 2",
        "badge_pills": ["22 Exam Tasks", "Zero Models", "Planning Boxes", "Full Rubrics"],
        "back_heading": "The essential independent practice companion for Level 2 Writing",
        "back_desc": "The dedicated mock testing resource for Level 2 candidates. Contains 22 brand-new, unseen exam tasks covering the entire specification with zero model answers — allowing students to simulate genuine exam conditions.",
        "key_features": [
            ("22 Rigorous Level 2 Exam Tasks", "Two challenging, independent writing prompts for every format."),
            ("Zero Model Answers for Clean Assessment", "Ideal for homework, timed classroom mock examinations, and self-evaluation."),
            ("Full 36-Mark Assessment Rubrics", "Authentic marking criteria covering Composition (21 Marks) and SPaG (15 Marks)."),
            ("Audience & Purpose Planning Boxes", "Dedicated structural planning templates for establishing tone and paragraphs.")
        ],
        "isbn": "978-1-912345-72-2",
        "companion_note_title": "Use Alongside the Core Revision Guide:",
        "companion_note_text": "Study the full exemplar models and examiner notes first in the Core Revision Guide, then practice independently."
    },

    # =========================================================================
    # DIGITAL SKILLS: HIGH-TECH CYBER MIDNIGHT & ELECTRIC CYAN (#090d16 / #00e5ff)
    # =========================================================================
    {
        "id": "digital_skills",
        "level_num": "EDSQ",
        "level_label": "EDSQ L1 / E3",
        "is_white": False,
        "bg_color": "#090d16",          # High-Tech Cyber Slate Midnight
        "accent_color": "#00e5ff",      # Electric Neon Cyan
        "gold_accent": "#38bdf8",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "ESSENTIAL DIGITAL SKILLS QUALIFICATIONS",
        "knockout_word": "DIGITAL",
        "main_title_1": "DIGITAL SKILLS",
        "main_title_2": "PRACTICAL HANDBOOK",
        "subtitle": "Complete practical handbook for Entry 3 & Level 1 EDSQ across all 5 National Standards",
        "edition_badge": "PRACTICAL STUDY HANDBOOK • 5 NATIONAL STANDARDS",
        "spec_text": "NATIONAL DIGITAL STANDARDS • ENTRY 3 & LEVEL 1",
        "badge_pills": ["5 Standards", "Cloud & Security", "Workplace Tools", "Exam Tasks"],
        "back_heading": "Master essential digital skills for work, study, and daily life",
        "back_desc": "Mapped directly to the Department for Education (DfE) National Standards for Essential Digital Skills. Features visual, screenshot-guided instructions for navigating devices, operating cloud systems, communicating professionally, and staying secure online.",
        "key_features": [
            ("All 5 National Digital Standards", "Using Devices & Handling Information, Creating & Editing, Communicating, Transacting, and Being Safe Online."),
            ("Hands-On Workplace Practicality", "File management, spreadsheets, formatting documents, email attachments, and online collaboration tools."),
            ("Cybersecurity & Online Safety", "Recognizing phishing emails, password hygiene, two-factor authentication, and data privacy rights."),
            ("Digital Transaction Protocols", "Booking appointments, online banking safely, evaluating credible web sources, and public services."),
            ("Authentic Practical Assessment Tasks", "Simulated exam scenarios calibrated to Gateway, Pearson, and NCFE EDSQ standards.")
        ],
        "isbn": "978-1-912345-86-9",
        "companion_note_title": "Official EDSQ Curriculum Alignment:",
        "companion_note_text": "Aligned with the statutory National Standards for Essential Digital Skills at Entry Level 3 and Level 1. Ideal for college courses, adult education, and corporate digital literacy programs."
    },

    # =========================================================================
    # SPECIALIST & DIAGNOSTIC: VIOLET & COBALT/AMBER
    # =========================================================================
    {
        "id": "spag_mastery",
        "level_num": "1 & 2",
        "level_label": "LEVELS 1 & 2",
        "is_white": False,
        "bg_color": "#581c87",          # Imperial Royal Violet
        "accent_color": "#fbbf24",      # Warm Academic Gold
        "gold_accent": "#fde047",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "FUNCTIONAL SKILLS ENGLISH SPECIALIST",
        "knockout_word": "GRAMMAR",
        "main_title_1": "SPaG HANDBOOK",
        "main_title_2": "& DRILLS",
        "subtitle": "Eliminate errors, master punctuation, and write with professional precision",
        "edition_badge": "SPECIALIST HANDBOOK • 25 TARGETED UNITS & DRILLS",
        "spec_text": "OFQUAL REGULATED SPECIFICATION • LEVELS 1 & 2",
        "badge_pills": ["25 Core Units", "150+ Drills", "Colon & Semicolon", "Workplace Vocab"],
        "back_heading": "Conquer Spelling, Punctuation and Grammar once and for all",
        "back_desc": "Up to 42% of marks in Functional Skills English Writing depend on SPaG accuracy. This definitive handbook breaks down every essential rule into digestible, memorable formulas with high-impact before-and-after corrections.",
        "key_features": [
            ("25 Targeted SPaG Units", "Comma splices, run-on sentences, subject-verb agreement, apostrophes, homophones, and tense consistency."),
            ("Master High-Level Punctuation", "Foolproof rules for colons, semicolons, dashes, and parenthetical commas that examiners reward."),
            ("150+ Rapid Correction Sentences", "Immediate hands-on drills to identify and fix errors in authentic student writing."),
            ("Workplace & Academic Vocabulary", "Subject-specific glossaries and sophisticated linking adverbs to elevate register."),
            ("Pre-Exam Proofreading Checklist", "A fast, 5-minute pre-submission inspection routine to prevent losing easy marks.")
        ],
        "isbn": "978-1-912345-85-2",
        "companion_note_title": "Essential for Both Level 1 and Level 2:",
        "companion_note_text": "Designed as the universal grammar partner for both Level 1 and Level 2 writing guides. Suitable for apprentices, adult learners, and ESOL candidates."
    },
    {
        "id": "bksb_remediation",
        "level_num": "L1 & L2",
        "level_label": "DIAGNOSTIC",
        "is_white": False,
        "bg_color": "#1d4ed8",          # Electric Cobalt Blue
        "accent_color": "#f59e0b",      # Safety Amber Gold
        "gold_accent": "#fbbf24",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "DIAGNOSTIC MASTERY & GAP REMEDIATION",
        "knockout_word": "REMEDIATION",
        "main_title_1": "DIAGNOSTIC GAP",
        "main_title_2": "REMEDIATION WORKBOOK",
        "subtitle": "The two-stage bridge workbook to conquer BKSB & OneAdvanced assessments",
        "edition_badge": "DIAGNOSTIC MASTERY WORKBOOK • TWO-STAGE METHOD",
        "spec_text": "BKSB & ONEADVANCED ALIGNED • 2026/2027 EDITION",
        "badge_pills": ["Two-Stage Method", "Error Repair", "Maths & English", "Exit Milestones"],
        "back_heading": "Bridge diagnostic skill gaps and unlock Level 2 qualification success",
        "back_desc": "Compiled specifically for apprentices and healthcare learners who have taken BKSB or OneAdvanced assessments and need to repair flagged weaknesses. Implements our proven Two-Stage Remediation System to build competence and retention.",
        "key_features": [
            ("Targeted Weak-Spot Diagnostics", "Covers the most frequently failed question archetypes across BKSB and OneAdvanced platforms."),
            ("Stage 1: Independent Retry Sheets", "Retry questions without worked answers to test understanding under simulated assessment conditions."),
            ("Stage 2: Tutor Step-by-Step Solutions", "Exhaustive tutor diagnostic explanations, underlying rules, and method proofs."),
            ("Both Maths & English Covered", "Addresses numerical calculations and reading/writing formatting criteria in one cohesive volume."),
            ("Exit Milestone Verification", "Milestone practice assessments to ensure learners are ready to sit their gateway exam.")
        ],
        "isbn": "978-1-912345-87-6",
        "companion_note_title": "Proven Two-Stage Remediation Routine:",
        "companion_note_text": "Specifically structured to bridge the gap from Entry Level to Level 2. Used by NHS apprentices and training providers nationwide."
    },

    # =========================================================================
    # PRINTED MOCK PACKS: OFFICIAL EXAM SLATE (#18181b)
    # =========================================================================
    {
        "id": "mock_pack_maths_l2",
        "level_num": "2",
        "level_label": "MOCK PACK",
        "is_white": False,
        "bg_color": "#18181b",          # Official Examination Slate
        "accent_color": "#38bdf8",      # Cyan Blue Accent
        "gold_accent": "#fbbf24",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "OFFICIAL EXAM SIMULATION SERIES",
        "knockout_word": "MOCK EXAMS",
        "main_title_1": "5 FULL EXAM PAPERS",
        "main_title_2": "MATHS LEVEL 2",
        "subtitle": "Authentic Section A (Non-Calc) & Section B (Calc) booklets with complete mark schemes",
        "edition_badge": "OFFICIAL SIMULATION PACK • 5 COMPLETE TESTS",
        "spec_text": "PEARSON EDEXCEL & CITY & GUILDS ALIGNED • 2026/2027",
        "badge_pills": ["5 Full Papers", "Section A & B", "Mark Schemes", "Method Criteria"],
        "back_heading": "Realistic exam simulation for guaranteed first-time pass",
        "back_desc": "Contains 5 complete, authentic Functional Skills Maths Level 2 mock exam papers. Formatted identically to official examination booklets, allowing candidates to practice under realistic timed conditions.",
        "key_features": [
            ("5 Complete Mock Examinations", "5 x Section A (Non-Calculator, 25 mins) + 5 x Section B (Calculator, 1 hr 30 mins)."),
            ("Authentic Exam Booklet Layout", "Real question structures, multi-step problem spaces, and official answer lines."),
            ("Comprehensive Mark Schemes", "Clear breakdown of Method (M), Accuracy (A), and Process (P) marks for every question."),
            ("Grade Boundary Thresholds", "Realistic pass mark boundaries to accurately evaluate exam readiness."),
            ("Examiner Notes & Tips", "Guidance on how examiners award marks and common errors to avoid.")
        ],
        "isbn": "978-1-912345-88-3",
        "companion_note_title": "The Ultimate Exam Readiness Benchmark:",
        "companion_note_text": "Complete these 5 full-length papers under timed exam conditions to ensure total confidence before exam day."
    },
    {
        "id": "mock_pack_english_l2",
        "level_num": "2",
        "level_label": "MOCK PACK",
        "is_white": False,
        "bg_color": "#18181b",          # Official Examination Slate
        "accent_color": "#c084fc",      # Indigo Violet Accent
        "gold_accent": "#facc15",
        "series_title": "MASTER FUNCTIONAL SKILLS",
        "series_sub": "OFFICIAL EXAM SIMULATION SERIES",
        "knockout_word": "MOCK EXAMS",
        "main_title_1": "5 FULL EXAM PAPERS",
        "main_title_2": "ENGLISH LEVEL 2",
        "subtitle": "Authentic Reading source booklets & Writing answer booklets with examiner rubrics",
        "edition_badge": "OFFICIAL SIMULATION PACK • 5 COMPLETE TESTS",
        "spec_text": "PEARSON EDEXCEL & CITY & GUILDS ALIGNED • 2026/2027",
        "badge_pills": ["5 Reading Tests", "5 Writing Tests", "Multi-Text Inserts", "Model Benchmarks"],
        "back_heading": "Master both Reading and Writing under genuine exam conditions",
        "back_desc": "Contains 5 complete Reading and Writing examination papers formatted to official exam board standards. Features authentic multi-text source inserts and ruled writing booklets.",
        "key_features": [
            ("5 Complete Reading Papers", "Authentic multi-text source inserts with questions assessing comprehension, comparison, and organizational features."),
            ("5 Complete Writing Papers", "Authentic 2-task writing papers covering letters, emails, articles, speeches, and reports."),
            ("Exemplar Benchmark Responses", "Model answers showing Level 2 pass standard for every writing task."),
            ("Official Marking Criteria Rubrics", "Detailed criteria for Composition & Effect (21 Marks) and SPaG (15 Marks)."),
            ("Timed Condition Practice", "Calibrated to 1 hour for Reading and 1 hour 20 minutes for Writing.")
        ],
        "isbn": "978-1-912345-89-0",
        "companion_note_title": "Simulate Real Exam Day Experience:",
        "companion_note_text": "Use these 5 full test papers to practice time management, text analysis, and sustained writing under realistic exam constraints."
    }
]

def generate_svg_barcode(isbn):
    return f'''
    <svg width="150" height="42" viewBox="0 0 150 42" xmlns="http://www.w3.org/2000/svg">
      <rect width="150" height="42" fill="#ffffff" rx="3"/>
      <rect x="10" y="3" width="2.5" height="27" fill="#1e293b"/>
      <rect x="14" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="18" y="3" width="3" height="27" fill="#1e293b"/>
      <rect x="23" y="3" width="1" height="27" fill="#1e293b"/>
      <rect x="26" y="3" width="4" height="27" fill="#1e293b"/>
      <rect x="32" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="36" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="41" y="3" width="3" height="27" fill="#1e293b"/>
      <rect x="46" y="3" width="1" height="27" fill="#1e293b"/>
      <rect x="50" y="3" width="3.5" height="27" fill="#1e293b"/>
      <rect x="56" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="60" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="65" y="3" width="3" height="27" fill="#1e293b"/>
      <rect x="70" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="74" y="3" width="4" height="27" fill="#1e293b"/>
      <rect x="80" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="84" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="88" y="3" width="3" height="27" fill="#1e293b"/>
      <rect x="94" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="98" y="3" width="4" height="27" fill="#1e293b"/>
      <rect x="104" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="108" y="3" width="1" height="27" fill="#1e293b"/>
      <rect x="112" y="3" width="3" height="27" fill="#1e293b"/>
      <rect x="117" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="122" y="3" width="3.5" height="27" fill="#1e293b"/>
      <rect x="128" y="3" width="1.5" height="27" fill="#1e293b"/>
      <rect x="132" y="3" width="2" height="27" fill="#1e293b"/>
      <rect x="136" y="3" width="3" height="27" fill="#1e293b"/>
      <text x="75" y="37" font-family="'Open Sans', Arial, sans-serif" font-size="7" font-weight="600" fill="#334155" text-anchor="middle">{isbn}</text>
    </svg>
    '''

def hex_to_rgba(hex_str, alpha):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) == 3:
        hex_str = "".join([c*2 for c in hex_str])
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"

def build_cover_html(book):
    is_white = book["is_white"]
    bg_color = book["bg_color"]
    accent = book["accent_color"]
    comp_accent = book.get("comp_accent", accent)
    
    if not is_white:
        body_text_color = "#ffffff"
        brand_color = accent
        level_badge_bg = accent
        level_badge_text = bg_color if bg_color not in ["#18181b", "#090d16"] else "#070d1e"
        edition_pill_border = accent
        edition_pill_text = accent
        edition_pill_bg = "rgba(0,0,0,0.3)"
        main_title_color = accent
        subtitle_color = "#ffffff"
        badge_pill_bg = "rgba(255, 255, 255, 0.12)"
        badge_pill_border = "rgba(255, 255, 255, 0.25)"
        badge_pill_text = "#ffffff"
        footer_border = "rgba(255, 255, 255, 0.2)"
        footer_text = "rgba(255, 255, 255, 0.8)"
        
        # Back cover
        back_bg = bg_color
        back_badge_color = accent
        back_headline_color = accent
        back_desc_color = "rgba(255, 255, 255, 0.92)"
        features_bg = "rgba(0, 0, 0, 0.22)"
        features_border = "rgba(255, 255, 255, 0.14)"
        features_title_color = accent
        feature_bullet_color = accent
        feature_text_color = "rgba(255, 255, 255, 0.92)"
        callout_bg = "rgba(255, 255, 255, 0.08)"
        callout_border = accent
        callout_title = accent
        callout_text = "rgba(255, 255, 255, 0.85)"
        back_footer_border = "rgba(255, 255, 255, 0.18)"
        publisher_text = "rgba(255, 255, 255, 0.7)"
        barcode_shadow = "0 6px 16px rgba(0, 0, 0, 0.4)"
        barcode_border = "none"
    else:
        body_text_color = "#1e293b"
        brand_color = comp_accent
        level_badge_bg = comp_accent
        level_badge_text = "#ffffff"
        edition_pill_border = comp_accent
        edition_pill_text = comp_accent
        edition_pill_bg = hex_to_rgba(comp_accent, 0.08)
        main_title_color = comp_accent
        subtitle_color = "#334155"
        badge_pill_bg = hex_to_rgba(comp_accent, 0.08)
        badge_pill_border = comp_accent
        badge_pill_text = comp_accent
        footer_border = "#cbd5e1"
        footer_text = "#64748b"
        
        # Back cover
        back_bg = "#ffffff"
        back_badge_color = comp_accent
        back_headline_color = comp_accent
        back_desc_color = "#334155"
        features_bg = "#f8fafc"
        features_border = "#e2e8f0"
        features_title_color = comp_accent
        feature_bullet_color = comp_accent
        feature_text_color = "#334155"
        callout_bg = hex_to_rgba(comp_accent, 0.07)
        callout_border = comp_accent
        callout_title = comp_accent
        callout_text = "#334155"
        back_footer_border = "#cbd5e1"
        publisher_text = "#64748b"
        barcode_shadow = "0 4px 12px rgba(0, 0, 0, 0.1)"
        barcode_border = "1px solid #cbd5e1"

    badge_pills_html = "".join([f'<div class="pill-badge">{p}</div>' for p in book["badge_pills"]])
    
    key_features_html = "".join([
        f'''<div class="feature-item">
          <div class="feature-bullet">&#10004;</div>
          <div class="feature-text"><strong>{title}:</strong> {desc}</div>
        </div>''' for title, desc in book["key_features"]
    ])

    texture_img = get_book_texture(book)
    if is_white:
        knockout_html = f'''
        <div class="knockout-container" style="filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.12));">
          <svg class="knockout-svg" viewBox="0 0 1000 170" preserveAspectRatio="none">
            <defs>
              <pattern id="kw_pat_{book['id']}" patternUnits="userSpaceOnUse" width="1000" height="170">
                <image href="file://{texture_img}" x="0" y="-85" width="1000" height="340" preserveAspectRatio="xMidYMid slice"/>
              </pattern>
            </defs>
            <text x="0" y="152" font-family="'Oswald', sans-serif" font-weight="700" font-size="200" textLength="1000" lengthAdjust="spacingAndGlyphs" fill="none" stroke="#000000" stroke-width="3" stroke-linejoin="round">{book["knockout_word"]}</text>
            <text x="0" y="152" font-family="'Oswald', sans-serif" font-weight="700" font-size="200" textLength="1000" lengthAdjust="spacingAndGlyphs" fill="url(#kw_pat_{book['id']})">{book["knockout_word"]}</text>
          </svg>
        </div>
        '''
    else:
        knockout_html = f'''
        <div class="knockout-container" style="filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.6));">
          <svg class="knockout-svg" viewBox="0 0 1000 170" preserveAspectRatio="none">
            <defs>
              <pattern id="kw_pat_{book['id']}" patternUnits="userSpaceOnUse" width="1000" height="170">
                <image href="file://{texture_img}" x="0" y="-85" width="1000" height="340" preserveAspectRatio="xMidYMid slice"/>
              </pattern>
            </defs>
            <text x="0" y="152" font-family="'Oswald', sans-serif" font-weight="700" font-size="205" textLength="1000" lengthAdjust="spacingAndGlyphs" fill="url(#kw_pat_{book['id']})">{book["knockout_word"]}</text>
          </svg>
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{book["series_title"]} - {book["main_title_1"]} {book["main_title_2"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Montserrat:wght@400;600;700;800;900&family=Open+Sans:wght@400;500;600;700&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', Arial, sans-serif;
    background: {bg_color};
    color: {body_text_color};
    -webkit-font-smoothing: antialiased;
  }}
  .cover-page {{
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    background-color: {bg_color};
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 18mm 18mm 16mm 18mm;
    overflow: hidden;
  }}
  .cover-page::before {{
    content: "";
    position: absolute;
    top: -120px;
    right: -120px;
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, {hex_to_rgba(accent, 0.15)} 0%, transparent 70%);
    pointer-events: none;
  }}
  .front-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}
  .brand-block {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}
  .series-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 15pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: {brand_color};
  }}
  .series-sub {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 8.5pt;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: {body_text_color};
    opacity: 0.9;
  }}
  .level-badge {{
    background: {level_badge_bg};
    color: {level_badge_text};
    padding: 6px 18px;
    border-radius: 20px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 9.5pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
  }}
  .front-top {{
    position: relative;
    z-index: 2;
    padding-top: 2mm;
  }}
  .edition-pill {{
    display: inline-block;
    margin: 8px 0 0 0;
    padding: 4px 14px;
    border-radius: 4px;
    border: 1px solid {edition_pill_border};
    background: {edition_pill_bg};
    color: {edition_pill_text};
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    text-align: left;
  }}
  .knockout-container {{
    width: 100%;
    margin: 4mm 0 2mm 0;
    position: relative;
    z-index: 2;
  }}
  .knockout-svg {{
    width: 100%;
    height: 48mm;
    display: block;
    overflow: visible;
  }}
  .front-mid {{
    position: relative;
    z-index: 2;
    margin-bottom: 4mm;
  }}
  .title-group {{
    margin: 0;
    text-align: left;
  }}
  .main-title-1 {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 44pt;
    line-height: 0.95;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: {main_title_color};
    margin: 0;
    text-align: left;
  }}
  .main-title-2 {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 38pt;
    line-height: 1.0;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: {body_text_color};
    margin: 4px 0 0 0;
    text-align: left;
  }}
  .subtitle {{
    font-family: 'Open Sans', Arial, sans-serif;
    font-size: 13.5pt;
    font-weight: 600;
    color: {subtitle_color};
    margin: 14px 0 0 0;
    line-height: 1.4;
    max-width: 480px;
    text-align: left;
  }}
  .badge-pills-row {{
    display: flex;
    gap: 8px;
    margin-top: 16px;
    flex-wrap: wrap;
    justify-content: flex-start;
  }}
  .pill-badge {{
    background: {badge_pill_bg};
    border: 1px solid {badge_pill_border};
    color: {badge_pill_text};
    padding: 6px 14px;
    border-radius: 6px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 8pt;
    letter-spacing: 0.5px;
  }}
  .front-footer {{
    border-top: 1px solid {footer_border};
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .footer-spec {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.5pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: {footer_text};
  }}
  .footer-edition {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.5pt;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: {brand_color};
  }}

  /* BACK COVER STYLES */
  .back-cover {{
    background-color: {back_bg};
    color: {body_text_color};
  }}
  .back-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid {features_border};
    padding-bottom: 12px;
  }}
  .back-badge {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 8.5pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: {back_badge_color};
  }}
  .back-headline {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 17pt;
    line-height: 1.25;
    color: {back_headline_color};
    margin: 16px 0 10px 0;
  }}
  .back-desc {{
    font-size: 9.5pt;
    line-height: 1.55;
    color: {back_desc_color};
    margin-bottom: 18px;
  }}
  .features-card {{
    background: {features_bg};
    border: 1px solid {features_border};
    border-radius: 12px;
    padding: 16px 18px;
    margin-bottom: 18px;
  }}
  .features-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 10pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: {features_title_color};
    margin-bottom: 12px;
  }}
  .feature-item {{
    display: flex;
    gap: 10px;
    margin-bottom: 9px;
    font-size: 8.8pt;
    line-height: 1.45;
    color: {feature_text_color};
  }}
  .feature-item:last-child {{
    margin-bottom: 0;
  }}
  .feature-bullet {{
    color: {feature_bullet_color};
    font-weight: 900;
  }}
  .companion-callout {{
    background: {callout_bg};
    border-left: 3.5px solid {callout_border};
    padding: 12px 14px;
    border-radius: 4px;
    margin-bottom: 16px;
  }}
  .companion-callout-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 8.8pt;
    color: {callout_title};
    margin-bottom: 4px;
  }}
  .companion-callout-text {{
    font-size: 8.2pt;
    line-height: 1.45;
    color: {callout_text};
  }}
  .back-footer {{
    border-top: 1px solid {back_footer_border};
    padding-top: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .publisher-block {{
    font-size: 7.8pt;
    color: {publisher_text};
    line-height: 1.4;
  }}
  .barcode-wrapper {{
    box-shadow: {barcode_shadow};
    border: {barcode_border};
    border-radius: 4px;
    overflow: hidden;
  }}
</style>
</head>
<body>

<!-- FRONT COVER -->
<div class="cover-page">
  <div class="front-top">
    <div class="front-header">
      <div class="brand-block">
        <div class="series-title">{book["series_title"]}</div>
        <div class="series-sub">{book["series_sub"]}</div>
      </div>
      <div class="level-badge">{book["level_label"]}</div>
    </div>
    <div class="edition-pill">{book["edition_badge"]}</div>
  </div>

  {knockout_html}

  <div class="front-mid">
    <div class="title-group">
      <h1 class="main-title-1">{book["main_title_1"]}</h1>
      <h2 class="main-title-2">{book["main_title_2"]}</h2>
    </div>
    <p class="subtitle">{book["subtitle"]}</p>
    <div class="badge-pills-row">
      {badge_pills_html}
    </div>
  </div>

  <div class="front-footer">
    <div class="footer-spec">{book["spec_text"]}</div>
    <div class="footer-edition">OFFICIAL STUDY MANUAL</div>
  </div>
</div>

<!-- BACK COVER -->
<div class="cover-page back-cover">
  <div class="back-top">
    <div class="back-header">
      <div class="back-badge">{book["series_title"]} &bull; {book["level_label"]}</div>
      <div class="back-badge">OFFICIAL PUBLICATION</div>
    </div>
    <h3 class="back-headline">{book["back_heading"]}</h3>
    <p class="back-desc">{book["back_desc"]}</p>
  </div>

  <div class="features-card">
    <div class="features-title">Inside This Publication</div>
    {key_features_html}
  </div>

  <div class="companion-callout">
    <div class="companion-callout-title">{book["companion_note_title"]}</div>
    <div class="companion-callout-text">{book["companion_note_text"]}</div>
  </div>

  <div class="back-footer">
    <div class="publisher-block">
      <strong>Master Functional Skills Publishing</strong><br>
      Approved Assessment Support Materials &bull; Great Britain<br>
      Registered Office: Oxford &bull; London &bull; United Kingdom
    </div>
    <div class="barcode-wrapper">
      {generate_svg_barcode(book["isbn"])}
    </div>
  </div>
</div>

</body>
</html>
'''
    return html

def create_3d_mockup(front_cover_png_path, output_3d_png_path, is_white=False):
    """
    Creates a photorealistic 3D angled standing book mockup with spine depth,
    page ridges, cast ambient shadow, and glossy highlight.
    """
    if not os.path.exists(front_cover_png_path):
        print(f"Error: {front_cover_png_path} not found for 3D mockup")
        return

    front = Image.open(front_cover_png_path).convert("RGBA")
    
    canvas_w = 800
    canvas_h = 960
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))

    book_w = 520
    book_h = int(book_w * (front.height / front.width))
    front_scaled = front.resize((book_w, book_h), Image.Resampling.LANCZOS)

    spine_w = 42
    
    # 1. Cast Floor & Ambient Shadow
    shadow_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    s_draw.ellipse([80, canvas_h - 130, canvas_w - 60, canvas_h - 40], fill=(7, 13, 30, 160))
    s_draw.polygon([
        (130, canvas_h - 140),
        (canvas_w - 70, canvas_h - 140),
        (canvas_w - 30, canvas_h - 60),
        (170, canvas_h - 60)
    ], fill=(7, 13, 30, 130))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(24))
    canvas.paste(shadow_layer, (0, 0), shadow_layer)

    # 2. Book Spine Layer
    spine_x = 135
    spine_y = 110
    
    spine_img = Image.new("RGBA", (spine_w, book_h), (0, 0, 0, 0))
    sp_draw = ImageDraw.Draw(spine_img)
    
    edge_sample = front_scaled.crop((0, 0, 10, book_h)).resize((1, 1)).getpixel((0, 0))
    base_r, base_g, base_b = edge_sample[:3]
    
    for x in range(spine_w):
        factor = 0.45 + 0.55 * (x / spine_w)
        r = int(base_r * factor)
        g = int(base_g * factor)
        b = int(base_b * factor)
        sp_draw.line([(x, 0), (x, book_h)], fill=(r, g, b, 255))
    
    sp_draw.line([(spine_w - 1, 0), (spine_w - 1, book_h)], fill=(255, 255, 255, 50))
    sp_draw.line([(0, 0), (0, book_h)], fill=(0, 0, 0, 100))

    canvas.paste(spine_img, (spine_x, spine_y), spine_img)

    # 3. Front Cover Layer with Sheen
    front_x = spine_x + spine_w
    front_y = spine_y
    
    front_with_sheen = front_scaled.copy()
    f_draw = ImageDraw.Draw(front_with_sheen)
    f_draw.line([(0, 0), (0, book_h)], fill=(0, 0, 0, 110), width=2)
    f_draw.line([(3, 0), (3, book_h)], fill=(255, 255, 255, 80), width=1)
    f_draw.line([(8, 0), (8, book_h)], fill=(0, 0, 0, 45), width=2)

    canvas.paste(front_with_sheen, (front_x, front_y), front_with_sheen)

    # 4. Top Page Edge
    top_edge = Image.new("RGBA", (book_w + spine_w, 20), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(top_edge)
    t_draw.polygon([
        (0, 18),
        (spine_w, 4),
        (spine_w + book_w - 10, 4),
        (spine_w + book_w, 18)
    ], fill=(235, 235, 235, 240), outline=(180, 180, 180, 180))
    canvas.paste(top_edge, (spine_x, spine_y - 14), top_edge)

    # 5. Right Page Trim Ridge
    right_edge = Image.new("RGBA", (14, book_h), (0, 0, 0, 0))
    r_draw = ImageDraw.Draw(right_edge)
    for y in range(0, book_h, 3):
        r_draw.line([(0, y), (12, y)], fill=(220, 220, 220, 200))
    canvas.paste(right_edge, (front_x + book_w - 2, front_y + 4), right_edge)

    canvas.save(output_3d_png_path, "PNG", optimize=True)
    print(f"Generated 3D Mockup -> {output_3d_png_path}")

def create_bundle_mockup(book_mockup_paths, output_path):
    """Creates a stacked 3D multi-book bundle mockup image."""
    valid_paths = [p for p in book_mockup_paths if os.path.exists(p)]
    if not valid_paths:
        return
    canvas_w, canvas_h = 1000, 750
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    num = len(valid_paths)
    spacing = 160 if num == 3 else 120
    start_x = 80
    
    for i, path in enumerate(valid_paths):
        img = Image.open(path).convert("RGBA")
        target_h = 580
        target_w = int(img.width * (target_h / img.height))
        img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        pos_x = start_x + (i * spacing)
        pos_y = 70 + (i * 12)
        canvas.paste(img_resized, (pos_x, pos_y), img_resized)
        
    canvas.save(output_path, "PNG", optimize=True)
    print(f"Generated Bundle Mockup -> {output_path}")

def main():
    print("=== Master Functional Skills Level-Based Color Harmonization ===")
    
    temp_dir = os.path.join(PROJECT_DIR, "scratch", "book_build_v2")
    os.makedirs(temp_dir, exist_ok=True)
    
    for book in BOOK_SPECS:
        b_id = book["id"]
        print(f"\nProcessing book: {b_id} ({book['main_title_1']} {book['main_title_2']}) [{book['level_label']}]...")
        
        html_content = build_cover_html(book)
        html_file = os.path.join(temp_dir, f"{b_id}_cover.html")
        pdf_file = os.path.join(temp_dir, f"{b_id}_cover.pdf")
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        cmd_pdf = [
            "/usr/lib/chromium/chromium",
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--user-data-dir=/tmp/chromium_color_gen_{b_id}",
            f"--print-to-pdf={pdf_file}",
            html_file
        ]
        subprocess.run(cmd_pdf, check=True)
        
        png_prefix = os.path.join(BOOKS_IMG_DIR, f"{b_id}_cover_page")
        cmd_png = [
            "/usr/bin/pdftoppm",
            "-png",
            "-r", "150",
            pdf_file,
            png_prefix
        ]
        subprocess.run(cmd_png, check=True)
        
        front_png = f"{png_prefix}-1.png"
        back_png = f"{png_prefix}-2.png"
        print(f"Rendered Front Cover: {front_png}")
        print(f"Rendered Back Cover:  {back_png}")
        
        mockup_3d_png = os.path.join(BOOKS_IMG_DIR, f"3d_{b_id}.png")
        create_3d_mockup(front_png, mockup_3d_png, is_white=book["is_white"])

    # Generate multi-volume bundle mockups
    create_bundle_mockup(
        [
            os.path.join(BOOKS_IMG_DIR, "3d_level2_core.png"),
            os.path.join(BOOKS_IMG_DIR, "3d_level2_companion.png"),
            os.path.join(BOOKS_IMG_DIR, "3d_spag_mastery.png")
        ],
        os.path.join(BOOKS_IMG_DIR, "3d_bundle_writing_l2.png")
    )
    create_bundle_mockup(
        [
            os.path.join(BOOKS_IMG_DIR, "3d_maths_l2_core.png"),
            os.path.join(BOOKS_IMG_DIR, "3d_maths_l2_companion.png"),
            os.path.join(BOOKS_IMG_DIR, "3d_level2_core.png"),
            os.path.join(BOOKS_IMG_DIR, "3d_level2_companion.png")
        ],
        os.path.join(BOOKS_IMG_DIR, "3d_bundle_ultimate_l2.png")
    )

    print("\nALL HARMONIZED BOOKS AND 3D MOCKUPS SUCCESSFULLY COMPILED!")

if __name__ == "__main__":
    main()
