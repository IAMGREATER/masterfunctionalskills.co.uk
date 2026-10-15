#!/usr/bin/env python3
"""
books/a4/build_reading_suite_a4.py
=============================================================================
Compiles the 2 dedicated Master Functional Skills English Reading Core Guides:
1. MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf (104 Pages)
2. MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf (104 Pages)

Outputs to:
- assets/downloads/
- ~/Documents/
=============================================================================
"""

import os
import sys
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROJECT_DIR))

import a4_kit as K
import english_reading_topics as ert
import visual_curriculum_catalog as vcc

DOWNLOADS = PROJECT_DIR / "assets" / "downloads"
DOCUMENTS = Path("/home/subi/Documents")
COV = K.COVER_DIR


def get_photo(keywords, theme="classroom_studying_adults", exclude=None):
    return K.photo(keywords, theme, exclude or set())


def escape_html(text):
    if not text:
        return ""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))


# =============================================================================
# Level 1 Reading Core Guide (104 Pages)
# =============================================================================
def build_reading_l1_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "English Reading Level 1 Core Guide"
    front_cov = COV / "reading_l1_core_cover_page-1.png"
    back_cov = COV / "reading_l1_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw, title=""):
        if title:
            rel, caption, char, q, svg = vcc.get_topic_visual(title)
            cat_path = K.PHOTO_DIR / rel
            if cat_path.exists():
                return str(cat_path)
        p = (get_photo(kw, "classroom_studying_adults", used_photos) or
             get_photo(kw, "workplace_office", used_photos) or
             get_photo(kw, "everyday_objects", used_photos))
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover / Contents (strictly across single lines)
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Reading",
        "Level 1 &bull; Complete Study &amp; Comprehension Mastery Manual",
        "English Reading Level 1",
        [
            ("1&ndash;12", "All 12 Core Reading Topics &amp; Comprehension Drills (48 pages)", "5"),
            ("EXAM", "Pearson Edexcel Level 1 Reading Strategy &amp; Question Types (6 pages)", "53"),
            ("M1&ndash;M2", "2 Complete Official Pearson Reading Mock Exam Papers (16 pages)", "59"),
            ("RUB", "Official Pearson Edexcel Reading Mark Schemes &amp; Assessment Grids (6 pages)", "75"),
            ("REF", "Complete Step-by-Step Solutions, Reading Glossary &amp; Index", "81"),
            ("REV", "Candidate Pre-Exam Readiness Commitments &amp; Progress Matrix", "85"),
        ],
        footer=BOOK
    ))

    # p3: Specification Overview
    p3_body = (
        K.page_title("Pearson Edexcel Level 1 Reading &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; DfE Subject Content L1.9 to L1.17", badge="SPEC")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 1 Reading paper is an externally assessed, <b>60-minute</b> examination worth <b>30 marks</b>.</p>"
            "<p>Candidates must read and comprehend <b>two to three non-fiction texts</b> drawn from real-world contexts (such as workplace safety notices, community leaflets, operational emails, news articles, and web pages).</p>"
            "<ul>"
            "<li><b>Question Types:</b> Multiple-choice questions, straightforward retrieval, explaining vocabulary in context, identifying organizational features, and distinguishing fact from opinion.</li>"
            "<li><b>Timing Strategy:</b> Aim for approximately <b>2 minutes per mark</b>. Spend 10–12 minutes reading the source texts carefully before tackling the questions.</li>"
            "<li><b>No Dictionaries:</b> Dictionaries and spellcheckers are not permitted during the examination.</li>"
            "</ul>"
            "</div>",
            title="Pearson Edexcel Level 1 Reading Assessment Format"
        )
        + K.tip_pair(
            "Always re-read the specific paragraph referenced in the question before selecting your answer.",
            "Never rely on personal background knowledge — every answer must be evidenced directly from the text.",
            golden_title="Golden Reading Rule", watch_title="Examiner Warning"
        )
        + K.fill_notes("Personal Target Score &amp; Reading Strategy Priorities", min_mm=30)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Candidate Diagnostic Self-Audit Matrix
    p4_body = (
        K.page_title("Level 1 Candidate Diagnostic Matrix", kicker="Baseline Skills Audit", badge="AUDIT")
        + K.box_html(
            "<p>Evaluate your confidence across the core Level 1 Reading standards before starting:</p>"
            + K.bullets([
                "Can you quickly separate objective facts from personal opinions in a workplace article?",
                "Can you work out the meaning of unfamiliar words by reading the surrounding sentences?",
                "Can you identify why a writer has used bullet points, subheadings, or bold text?",
                "Can you find specific information in an email, memo, or website in under 60 seconds?",
                "Can you explain the main purpose of a text (to inform, instruct, explain, or persuade)?"
            ]),
            title="Core Functional Skills Level 1 Reading Competencies"
        )
        + K.fill_notes("Reading Skills I Need to Practise Most", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Audit"), footer=BOOK, page_no=4))

    # p5 to p52: 12 Reading Topics x 4 pages = 48 pages
    p_curr = 5
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        clean_title = topic["clean_topic"]
        lead = topic["intro_lead"]
        spec_pts = topic["spec_points"]
        rules = topic["golden_rules"]
        skills = topic.get("skills", [])
        models = topic.get("worked_models", [])
        traps = topic.get("examiner_traps", [])
        practice = topic.get("practice_questions", [])

        # Page 1: Topic Blueprint & Reading Theory
        spec_text = "<br>".join(f"&bull; <b>{code}:</b> {desc}" for code, desc in spec_pts)
        rule_desc = rules[0]["desc"] if rules else "Read texts actively and cross-reference details."
        p1_body = (
            K.page_title(f"Reading Topic {t_idx}: {clean_title}", kicker=f"Topic Blueprint &bull; Level 1 Reading", badge=f"R{t_idx}")
            + K.hero_image(P(clean_title, title=clean_title), f"Study context for {clean_title}.", 52, fill=True)
            + K.rule_box("DfE Criteria &amp; Core Concept",
                         f"<div style='font-size:12.5pt;line-height:1.5;'>"
                         f"<p><b>Curriculum Standard:</b><br>{spec_text}</p>"
                         f"<p><b>Key Concept:</b> {rule_desc}</p>"
                         f"</div>")
            + K.tip_pair(
                rules[1]["desc"] if len(rules) > 1 else "Always underline keywords in the question.",
                traps[0]["desc"] if traps else "Do not assume something is a fact just because it is written down.",
                golden_title="Golden Rule", watch_title="Examiner Trap"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Topic {t_idx} &bull; Theory"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Workplace Text & Strategy Walkthrough
        first_model = models[0] if models else {}
        context_name = first_model.get("context", "Workplace Communication")
        q_prompt = first_model.get("question", "Read the text carefully and answer the questions.")
        steps = first_model.get("steps", [])
        steps_html = "".join(f"<li><b>{s[0]} ({s[1]}):</b> {s[2]} <span style='color:var(--primary);font-weight:700;'>[{s[3]}]</span></li>" for s in steps) if steps else "<li>Read carefully and extract key points.</li>"
        
        p2_body = (
            K.page_title(f"{clean_title} &bull; Text Analysis", kicker=f"Authentic Workplace Context &bull; {context_name}", badge="PASSAGE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;margin-bottom:3mm;'>"
                f"<strong style='color:var(--primary);font-size:12pt;'>Extract &bull; {first_model.get('title', clean_title)}:</strong><br><br>"
                f"{q_prompt}"
                f"</div>",
                title=f"Source Text &bull; {context_name}"
            )
            + K.box_html(
                f"<ol style='margin:0;padding-left:5mm;font-size:11pt;line-height:1.45;'>{steps_html}</ol>",
                title="Tutor Step-by-Step Analysis Strategy"
            )
            + K.fill_notes("Key Clues &amp; Vocabulary Notes", min_mm=28)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Topic {t_idx} &bull; Analysis"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Worked Full-Marks Benchmark Model
        final_ans = first_model.get("final_answer", "Full model answer.")
        tutor_tip = first_model.get("tutor_tip", "Answer clearly with direct evidence.")
        p3_body = (
            K.page_title(f"{clean_title} &bull; Benchmark Model Answer", kicker="Examiner Full Marks Exemplar", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:3.5mm;border:1.5px solid #cbd5e1;border-radius:6px;font-size:11.5pt;line-height:1.5;'>"
                f"<strong style='color:var(--primary);'>Model Candidate Answer:</strong><br><br>"
                f"{final_ans}"
                f"</div>",
                title=f"Full Marks Benchmark &bull; {first_model.get('marks', '3 Marks')}"
            )
            + K.tip_pair(
                tutor_tip,
                "Examiners award marks for exact quotes or accurate paraphrasing that directly answers what was asked.",
                golden_title="Examiner Guidance", watch_title="Mark Scheme Criterion"
            )
            + K.fill_notes("What Makes This Answer Successful", min_mm=32)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Topic {t_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Candidate Comprehension Practice & Ruled Response Lines
        first_pr = practice[0] if practice else {}
        pr_q = first_pr.get("question", f"Read an everyday workplace text and explain how {clean_title.lower()} is used.")
        pr_marks = first_pr.get("marks", "2 Marks")
        p4_body = (
            K.page_title(f"{clean_title} &bull; Candidate Practice", kicker=f"Exam Practice &bull; {pr_marks}", badge="DRILL")
            + K.box_html(
                f"<p style='font-size:11.5pt;margin:0 0 2mm 0;'><b>Comprehension Task:</b></p>"
                f"<div style='background:#f8fafc;padding:3mm;border:1px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>"
                f"{pr_q}"
                f"</div>",
                title=f"Independent Practice Task &bull; {pr_marks}"
            )
            + K.fill_lines(f"Write your response below ({pr_marks}):", min_mm=170, gap_mm=9.5)
        )
        pages.append(K.page(p4_body, header=(BOOK, f"Topic {t_idx} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p53 to p58: Reading Exam Strategy Masterclass (6 pages)
    exam_masterclasses = [
        ("Managing Your Time: The 1-Minute-Per-Mark Rule",
         "In a 60-minute exam for 30 marks, you have exactly 2 minutes per mark. Allocate your time systematically: 10 mins reading texts, 40 mins answering questions, 10 mins checking.",
         "Read questions first so you read with a purpose.", "Never get stuck on a 1-mark question for more than 2 minutes."),
        ("Retrieval Questions &amp; Locating Facts",
         "Retrieval questions ask you to find a specific piece of information (who, what, where, when, how much). Scan for capital letters, numbers, and key verbs.",
         "Keep answers short and factual.", "Don't copy entire paragraphs when only one phrase is needed."),
        ("Working Out the Meaning of Unfamiliar Words",
         "When encountering specialist or difficult words, read the sentence before and the sentence after. The surrounding context almost always provides a synonym or explanation.",
         "Check if a glossary, bracket, or footnote explains the word.", "Substitute a simpler word to test if the sentence still makes sense."),
        ("Understanding Organizational &amp; Layout Features",
         "Writers use headings to introduce topics, subheadings to organize sub-topics, bullet points to list items concisely, and bold text for visual emphasis.",
         "Always explain HOW the feature helps the reader (e.g. 'makes it easy to scan').", "Do not just say 'it looks nice' or 'it grabs attention'."),
        ("Distinguishing Fact, Opinion &amp; Bias",
         "A fact can be proved true with evidence, statistics, or records. An opinion expresses personal belief, feelings, or value judgments ('best', 'terrible', 'undoubtedly').",
         "Facts can be proven; opinions reflect feelings.", "Watch out for opinions hidden inside quotes from employees or experts."),
        ("Final Checking &amp; Proofreading Strategy",
         "Use your final 10 minutes to verify every answer. Ensure you haven't left any multiple-choice boxes blank and that your written answers are clear and legible.",
         "Even a guessed multiple-choice answer gives you a 25% chance of a mark.", "Check that you have copied dates, names, and phone numbers accurately.")
    ]

    for em_idx, (em_title, em_desc, em_gold, em_trap) in enumerate(exam_masterclasses, 1):
        em_body = (
            K.page_title(f"Exam Masterclass {em_idx}: {em_title}", kicker="Pearson Edexcel Reading Strategy", badge=f"EX{em_idx}")
            + K.box_html(f"<p style='font-size:12.5pt;line-height:1.55;'>{em_desc}</p>", title="Core Examination Technique")
            + K.tip_pair(em_gold, em_trap, golden_title="Top Scoring Strategy", watch_title="Common Exam Pitfall")
            + K.fill_notes(f"My Exam Strategy Notes &amp; Personal Rules (Masterclass {em_idx})", min_mm=60)
        )
        pages.append(K.page(em_body, header=(BOOK, f"Masterclass {em_idx}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59 to p74: 2 Full Official Reading Mock Exams (16 pages: 8 pages per mock)
    # Mock 1 (8 pages)
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Level 1 &bull; 60 Minutes &bull; 30 Marks", badge="MOCK 1")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 reading texts (Text A, Text B, and Text C).",
                "Answer all questions in the candidate spaces provided.",
                "Total time allowed: 60 minutes. Total marks: 30 marks.",
                "You may not use a dictionary or spellchecker."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Spend 10 minutes reading all texts thoroughly before beginning the questions.",
                     "Check the marks allocated to each question. A 2-mark question requires 2 distinct points.",
                     golden_title="Pacing Rule", watch_title="Mark Allocation")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 1 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 1 Texts & Questions (7 pages)
    mock1_sections = [
        ("Text A: Greendale Community Health &amp; Wellbeing Centre",
         "The Greendale Health &amp; Wellbeing Centre opens Monday to Friday from 08:00 to 19:30. We provide free confidential health checks, NHS smoking cessation clinics, and diabetes prevention workshops. To book an appointment, telephone 01865 774200 or visit our reception desk in Zone 2. Patients attending morning clinics may use the visitor car park free of charge for up to two hours.",
         [{"q": "<b>Question 1:</b> According to Text A, what time does the Wellbeing Centre close on weekdays? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two free health services offered by the centre. (2 marks)", "lines": 3}]),
        ("Text A Continued &amp; Questions",
         "Please note that evening workshops require advance booking at least 48 hours in advance. If you cannot attend your scheduled appointment, you must notify staff so another patient can be offered your time slot. Missed appointments cost the centre over &pound;12,000 each year.",
         [{"q": "<b>Question 3:</b> How much notice is required to book an evening workshop? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Explain one consequence mentioned in the text if a patient misses an appointment. (1 mark)", "lines": 2},
          {"q": "<b>Question 5:</b> What is the main purpose of Text A? (1 mark)", "options": ["To complain about NHS funding", "To inform the public about services and opening hours", "To advertise private gym memberships", "To instruct readers how to become a doctor"]}]),
        ("Text B: Customer Feedback &amp; Public Reviews",
         "Review by David T. (5 Stars &bull; Verified Visitor):<br><em>'I visited the Greendale Wellbeing Centre yesterday for a blood pressure check. The nurse, Sister Sarah, was exceptionally kind and reassuring. The modern waiting area was spotlessly clean and spacious. The automated check-in screen was effortless to use. Without a doubt, this is the finest healthcare facility in Oxfordshire!'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from David's review. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from David's review. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how David uses adjectives to describe the staff and facilities. (2 marks)", "lines": 3}]),
        ("Text B Questions &amp; Text C Introduction",
         "Text C &bull; Staff Operational Memo:<br>From: Clinic Operations Manager<br>To: All Nursing &amp; Administrative Staff<br>Date: 12 October 2026<br>Subject: Annual Flu Vaccination Clinic Logistics<br><br>All staff must complete their mandatory infection control refresher training by Friday 24 October. Flu vaccination clinics commence Monday 3 November in Seminar Room B.",
         [{"q": "<b>Question 9:</b> In David's review in Text B, what does the word 'reassuring' suggest about Sister Sarah? (1 mark)", "lines": 2},
          {"q": "<b>Question 10:</b> Identify the date by which staff must complete their refresher training. (1 mark)", "lines": 2}]),
        ("Text C: Operational Memo Details",
         "To maintain efficient patient flow, please adhere strictly to the 10-minute appointment slots. Laminated patient pathway flowcharts are displayed in the staff breakroom. Any adverse vaccine reactions must be logged in the yellow clinical incident binder within 30 minutes of occurrence.",
         [{"q": "<b>Question 11:</b> Where can staff find the laminated patient pathway flowcharts? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> Where must adverse vaccine reactions be recorded? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Within what timeframe must an adverse reaction be logged? (1 mark)", "lines": 2}]),
        ("Text C Layout &amp; Comparison Questions",
         "The memo uses bold subheadings and bullet points so that operational instructions are clear during busy clinic hours. All staff receive a complimentary hot beverage voucher from the cafeteria.",
         [{"q": "<b>Question 14:</b> Identify two layout features used in Text C and explain how they help the reader. (2 marks)", "lines": 4},
          {"q": "<b>Question 15:</b> Both Text A and Text C discuss healthcare clinics. Compare one difference in audience between Text A and Text C. (2 marks)", "lines": 4}]),
        ("Mock 1 &bull; Candidate Self-Audit Matrix",
         "Complete your review of Paper 1 before marking your score against the official solutions on p81.",
         [{"q": "<b>Question 16:</b> Summarize two key pieces of advice you would give to someone visiting the Greendale Centre for the first time. (2 marks)", "lines": 4}])
    ]

    for p_title, p_extract, p_qs in mock1_sections:
        p_body = (
            K.page_title(f"Mock 1 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 1", badge="M1")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 1 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Mock 2 (8 pages)
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Level 1 &bull; 60 Minutes &bull; 30 Marks", badge="MOCK 2")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 reading texts on workplace apprenticeship training and health and safety.",
                "Answer all questions in the spaces provided.",
                "Time allowed: 60 minutes. Total marks: 30 marks.",
                "Check your answers against the official mark scheme on p86."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Keep your answers precise and directly quote the passage where appropriate.",
                     "Watch out for words like 'except' or 'not' in multiple-choice questions.",
                     golden_title="Top Scoring Tip", watch_title="Question Phrasing")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 2 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    # Mock 2 Texts & Questions (7 pages)
    mock2_sections = [
        ("Text A: Oxfordshire Council Apprenticeship Guide",
         "The Oxfordshire Council Apprenticeship Programme offers paid apprenticeships across digital skills, business administration, and horticulture. Apprentices receive a starting salary of &pound;19,500 per annum, 25 days of paid annual leave, and fully funded qualifications up to Level 3. Applicants must be aged 16 or over and hold GCSEs in English and Maths at Grade 3 or Functional Skills Level 1.",
         [{"q": "<b>Question 1:</b> According to Text A, what is the starting salary for an apprentice? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> State two qualification fields offered on the apprenticeship programme. (2 marks)", "lines": 3}]),
        ("Text A Continued &amp; Questions",
         "All applications must be submitted via the online portal by Friday 28 November 2026. Successful candidates will be invited for assessment days during the second week of December. If you need reasonable adjustments for the interview, contact the disability support coordinator at hr@oxfordshire.gov.uk.",
         [{"q": "<b>Question 3:</b> What is the final deadline date for submitting an application? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Who should applicants contact if they require reasonable adjustments? (1 mark)", "lines": 2},
          {"q": "<b>Question 5:</b> What text type is Text A? (1 mark)", "options": ["An informal personal diary", "An informative official recruitment guide", "A critical newspaper review", "A recipe instruction card"]}]),
        ("Text B: Apprentice Case Study &bull; Marcus",
         "Marcus Davies, Digital Support Apprentice:<br><em>'Joining the council digital team was the best decision of my career! I was nervous on my first day, but my mentor Abdul guided me through every software deployment. The workplace culture is wonderfully welcoming and positive. Last month, I configured 85 new laptops for field healthcare workers.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Marcus's case study. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Marcus's case study. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> How does Marcus describe the workplace culture? (1 mark)", "lines": 2}]),
        ("Text B Questions &amp; Text C Introduction",
         "Text C &bull; Depot Health &amp; Safety Policy Notice:<br>All warehouse and IT depot employees must wear high-visibility vests and steel toe-capped safety boots at all times in the logistics bay. Forklift operating lanes are marked with yellow cross-hatch lines. Pedestrians must strictly use the green painted walkways.",
         [{"q": "<b>Question 9:</b> In Marcus's account, how did mentor Abdul support him? (1 mark)", "lines": 2},
          {"q": "<b>Question 10:</b> According to Text C, what two items of PPE are compulsory in the logistics bay? (2 marks)", "lines": 3}]),
        ("Text C: Depot Safety Rules",
         "Mobile phones are strictly prohibited while walking through the loading bays. Earphones must never be worn as they prevent staff from hearing forklift reverse warning alarms. In the event of a spillage, immediately erect the yellow 'Caution: Wet Floor' warning cones.",
         [{"q": "<b>Question 11:</b> Why are earphones prohibited in the loading bays? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> What action must an employee take immediately if a liquid spillage occurs? (1 mark)", "lines": 2}]),
        ("Text C Layout &amp; Comparison Questions",
         "Text C uses bold uppercase lettering and warning symbols to emphasize urgent safety protocols. Failure to observe safety notices may result in formal disciplinary action under section 4 of the Employment Contract.",
         [{"q": "<b>Question 13:</b> Explain why the writer of Text C used bold uppercase lettering for key safety rules. (1 mark)", "lines": 2},
          {"q": "<b>Question 14:</b> Both Text A and Text C are written for council employees. Identify one difference in purpose between Text A and Text C. (2 marks)", "lines": 4}]),
        ("Mock 2 &bull; Candidate Self-Audit Matrix",
         "Check your answers against the official mark scheme before recording your final score.",
         [{"q": "<b>Question 15:</b> What advice does Text C give regarding mobile phone usage? (1 mark)", "lines": 2},
          {"q": "<b>Question 16:</b> Summarize two benefits of doing an apprenticeship as described across Text A and Text B. (2 marks)", "lines": 4}])
    ]

    for p_title, p_extract, p_qs in mock2_sections:
        p_body = (
            K.page_title(f"Mock 2 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 2", badge="M2")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 2 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p75 to p80: Official Pearson Edexcel Reading Mark Schemes (6 pages)
    rubrics = [
        ("Retrieval &amp; Identification Mark Schemes (L1.9–L1.11)",
         "Pearson Edexcel Level 1 Reading awards marks for accurate factual extraction. Accept direct quotes or unambiguous paraphrasing that answers the question precisely."),
        ("Layout &amp; Organizational Devices Mark Scheme (L1.12)",
         "To achieve full marks on layout questions, candidates must identify the specific device (e.g. bullet points, headings, columns) AND explain its functional benefit for the reader."),
        ("Fact vs. Opinion Assessment Criteria (L1.9)",
         "Award 1 mark for verifiable factual statement supported by records or metrics. Award 1 mark for subjective opinion containing evaluative vocabulary."),
        ("Vocabulary in Context Mark Scheme (L1.10–L1.11)",
         "Candidates must demonstrate understanding of words in their specific sentence context rather than offering unrelated dictionary definitions."),
        ("Text Purpose &amp; Audience Assessment Grids (L1.16–L1.17)",
         "Candidates must accurately link purpose verbs (persuade, inform, explain, instruct) to evidence in the text."),
        ("Comparison of Two Texts Mark Scheme (L1.17)",
         "Award marks for direct comparative links between Text A and Text B identifying similarities or differences in ideas, audience, or purpose.")
    ]

    for r_idx, (r_title, r_desc) in enumerate(rubrics, 1):
        r_body = (
            K.page_title(f"Official Mark Scheme &bull; Part {r_idx} of 6", kicker=r_title, badge=f"MS{r_idx}")
            + K.box_html(
                f"<div style='font-size:12.5pt;line-height:1.55;'>"
                f"<p><b>Examiner Assessment Guidance:</b><br>{r_desc}</p>"
                f"<p><b>Standard Marking Rules:</b></p>"
                f"<ul>"
                f"<li>Do not penalize spelling, punctuation, or grammar errors in the Reading paper provided meaning is clear.</li>"
                f"<li>Where a question asks for TWO points, do not award marks for two variations of the same idea.</li>"
                f"<li>Answers copied verbatim from the text are acceptable if they answer the specific question asked.</li>"
                f"</ul>"
                f"</div>",
                title="Mark Scheme Standards &amp; Criteria"
            )
            + K.fill_notes(f"Personal Marking Notes &amp; Checkpoints (Part {r_idx})", min_mm=45)
        )
        pages.append(K.page(r_body, header=(BOOK, f"Mark Scheme Part {r_idx}/6"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p81 to p102: Complete Step-by-Step Solutions, Glossary & Index (22 pages)
    ref_blocks = []

    # Topic Practice Solutions (Topics 1 to 12)
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        first_pr = topic.get("practice_questions", [{}])[0]
        sol_text = first_pr.get("solution_steps", "Full worked steps.")
        ans_text = first_pr.get("correct_answer", "Correct benchmark answer.")
        ref_blocks.append(K.ref_block(
            f"Topic {t_idx}: {topic['clean_topic']} Solutions",
            K.ref_qa(f"R{t_idx}", f"<b>Steps:</b> {sol_text}<br><b>Answer:</b> {ans_text}", marks=first_pr.get("marks", "2m"))
        ))

    # Mock 1 Full Solutions
    m1_ans = [
        ("Q1", "19:30 (7:30 pm)", "1m", "Direct retrieval from Text A paragraph 1."),
        ("Q2", "Health checks / Smoking cessation clinics / Diabetes prevention workshops (any two)", "2m", "1 mark for each service listed."),
        ("Q3", "48 hours in advance", "1m", "Direct retrieval."),
        ("Q4", "Costs the centre over £12,000 / denies another patient a time slot", "1m", "Accept either consequence."),
        ("Q5", "B: To inform the public about services and opening hours", "1m", "Multiple choice correct key."),
        ("Q6", "Visited yesterday / Nurse was Sister Sarah / Had blood pressure check", "1m", "Verifiable fact."),
        ("Q7", "Sister Sarah was exceptionally kind / Finest healthcare facility in Oxfordshire", "1m", "Subjective opinion."),
        ("Q8", "Kind, reassuring, clean, spacious — creates an encouraging and positive impression", "2m", "1 mark for quote, 1 mark for effect."),
        ("Q9", "She made the patient feel calm, relaxed, and safe during the test", "1m", "Vocabulary inference."),
        ("Q10", "Friday 24 October", "1m", "Direct retrieval."),
        ("Q11", "In the staff breakroom", "1m", "Direct retrieval."),
        ("Q12", "Yellow clinical incident binder", "1m", "Direct retrieval."),
        ("Q13", "Within 30 minutes of occurrence", "1m", "Direct retrieval."),
        ("Q14", "Bold headings organize topics; bullet points present rules clearly for quick reading", "2m", "1m for features, 1m for effect."),
        ("Q15", "Text A is for general public/patients; Text C is for internal clinical/administrative staff", "2m", "1m for Text A audience, 1m for Text C."),
        ("Q16", "Book appointments in advance; utilize free 2-hour parking in morning clinics", "2m", "1m for each valid recommendation.")
    ]
    m1_html = "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_ans)
    ref_blocks.append(K.ref_block("Official Reading Mock Examination 1 &bull; Full Mark Scheme &amp; Solutions (30 Marks)", m1_html))

    # Mock 2 Full Solutions
    m2_ans = [
        ("Q1", "£19,500 per annum", "1m", "Direct retrieval from Text A."),
        ("Q2", "Digital skills / Business administration / Horticulture (any two)", "2m", "1m each."),
        ("Q3", "Friday 28 November 2026", "1m", "Direct retrieval."),
        ("Q4", "Disability support coordinator (hr@oxfordshire.gov.uk)", "1m", "Direct retrieval."),
        ("Q5", "B: An informative official recruitment guide", "1m", "Multiple choice key."),
        ("Q6", "Configured 85 new laptops / Mentor was Abdul", "1m", "Verifiable fact."),
        ("Q7", "Best decision of my career / Wonderfully welcoming workplace culture", "1m", "Subjective opinion."),
        ("Q8", "Wonderfully welcoming and positive", "1m", "Direct quote."),
        ("Q9", "Abdul guided him through software deployments and helped him overcome nervousness", "1m", "Explanation."),
        ("Q10", "High-visibility vests AND steel toe-capped safety boots", "2m", "1m for each PPE item."),
        ("Q11", "They prevent workers from hearing forklift reverse warning alarms", "1m", "Safety justification."),
        ("Q12", "Erect yellow 'Caution: Wet Floor' warning cones immediately", "1m", "Action required."),
        ("Q13", "To emphasize urgent mandatory health and safety rules so they are immediately noticed", "1m", "Layout effect."),
        ("Q14", "Text A aims to recruit and inform applicants; Text C aims to enforce strict safety rules", "2m", "Purpose comparison."),
        ("Q15", "Mobile phones are strictly prohibited while walking through loading bays", "1m", "Rule retrieval."),
        ("Q16", "Earn a salary while training (£19,500); receive mentorship and gain qualifications", "2m", "Synthesis across texts.")
    ]
    m2_html = "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_ans)
    ref_blocks.append(K.ref_block("Official Reading Mock Examination 2 &bull; Full Mark Scheme &amp; Solutions (30 Marks)", m2_html))

    # Reading Glossary
    glossary_items = [
        ("Audience", "The specific group of readers a text is written for (e.g. staff, patients, general public)."),
        ("Bias", "A one-sided viewpoint that favors one perspective over another, often lacking balance."),
        ("Caption", "A brief text explanation placed beneath an image or diagram."),
        ("Context", "The surrounding words, sentences, or background situation that gives a word or text its meaning."),
        ("Fact", "A verifiable piece of information that can be proven true by records, measurements, or evidence."),
        ("Headline / Heading", "The main title of an article or document designed to state the subject clearly."),
        ("Implicit Meaning", "Information that is suggested or hinted at rather than directly stated."),
        ("Informative Text", "A text whose main purpose is to give clear, factual information to the reader."),
        ("Layout Feature", "A visual or structural element (columns, bullet points, boxes) that organizes content."),
        ("Opinion", "A personal belief, attitude, or feeling that cannot be verified as an objective fact."),
        ("Persuasive Text", "A text designed to convince the reader to take action or agree with a specific viewpoint."),
        ("Purpose", "The main reason why the author wrote the text (to inform, instruct, explain, or persuade)."),
        ("Retrieval", "Finding and extracting specific facts, figures, or dates directly from a text."),
        ("Subheading", "A smaller heading that divides an article or document into clear sections."),
        ("Tone", "The mood, feeling, or attitude conveyed by the writer's choice of words.")
    ]
    gl_html = "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in glossary_items)
    ref_blocks.append(K.ref_block("Essential Glossary of Reading &amp; Comprehension Terminology", gl_html))

    # Alphabetical Index
    index_items = [
        ("A", [("Audience Identification", "10, 12, 53"), ("The Writer's Purpose", "12, 53")]),
        ("B", [("Bias Detection", "8, 54"), ("Bullet Points Effect", "4, 5, 55")]),
        ("C", [("Captions &amp; Images", "6"), ("Comparing Texts", "11, 56"), ("Context Meaning", "2")]),
        ("E", [("Examiner Traps", "5, 9, 13"), ("Explicit Meaning", "2")]),
        ("F", [("Fact vs. Opinion", "1, 54"), ("Fonts &amp; Headings", "4, 5")]),
        ("G", [("Glossary of Terms", "98"), ("Golden Reading Rules", "5, 9, 13, 17")]),
        ("I", [("Implicit Meaning", "2"), ("Informative Purpose", "10, 12")]),
        ("L", [("Layout Devices", "5, 55"), ("Locating Facts", "53")]),
        ("M", [("Mock Exam 1", "59"), ("Mock Exam 2", "67"), ("Multiple Choice Strategy", "53")]),
        ("O", [("Opinions Identification", "1, 54"), ("Organizational Devices", "4, 5")]),
        ("P", [("Persuasive Techniques", "7, 10"), ("Purpose of Texts", "10, 12")]),
        ("R", [("Retrieval Skills", "53"), ("Rhetorical Devices", "7")]),
        ("S", [("Specialist Vocabulary", "3"), ("Subheadings Effect", "4, 5")]),
        ("T", [("Text Types", "10"), ("Timing Strategy (1 min/mark)", "3, 53"), ("Tone &amp; Style", "9")])
    ]
    ix_html = ""
    for letter, entries in index_items:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        ix_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Level 1 Reading Alphabetical Subject Index", ix_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Reading Notes")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # p103: Pre-Exam Readiness Commitments & Progress Matrix
    p103_body = (
        K.page_title("Level 1 Reading &bull; Exam Day Commitments", kicker="Final Revision &bull; Exam Readiness", badge="READY")
        + K.box_html(
            "<p>Before entering your Pearson Edexcel Level 1 Reading examination, commit to these 5 essentials:</p>"
            + K.bullets([
                "<b>1. Read Questions First:</b> Always read the questions before the source texts so you read with focus.",
                "<b>2. Strict Pacing:</b> Spend 10 minutes reading texts, 40 minutes on questions, and 10 minutes checking.",
                "<b>3. Quote Directly:</b> For retrieval questions, quote exact words or statistics from the source passage.",
                "<b>4. Explain Layout:</b> When asked about layout features, always state how they help the reader.",
                "<b>5. Answer Every Question:</b> Never leave a multiple-choice question blank — eliminate wrong answers."
            ]),
            title="Golden Exam Rules for Reading Success"
        )
        + K.fill_notes("Personal Commitments &amp; Tutor Sign-off", min_mm=45)
    )
    pages.append(K.page(p103_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_extra = (
            K.page_title("Candidate Final Verification Protocol", kicker="Pearson Edexcel Reading Standards", badge="AUDIT")
            + K.box_html(
                "<p>Final review checklist for the exam room:</p>"
                + K.bullets([
                    "Did you verify whether statements were facts or opinions?",
                    "Did you explain the specific purpose of the writer (inform, persuade, instruct)?",
                    "Did you double check all dates, phone numbers, and numbers copied from the passages?"
                ]),
                title="Final Verification"
            )
            + K.fill_notes("Last-Minute Exam Reminders", min_mm=40)
        )
        pages.append(K.page(p_extra, header=(BOOK, "Verification Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Reading_Level_1_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Reading Level 1 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


# =============================================================================
# Level 2 Reading Core Guide (104 Pages)
# =============================================================================
def build_reading_l2_core():
    print("\n" + "="*70)
    print("BUILDING: MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf (A4 104p)")
    print("="*70)

    BOOK = "English Reading Level 2 Core Guide"
    front_cov = COV / "reading_l2_core_cover_page-1.png"
    back_cov = COV / "reading_l2_core_cover_page-2.png"

    pages = []
    used_photos = set()

    def P(kw, title=""):
        if title:
            rel, caption, char, q, svg = vcc.get_topic_visual(title)
            cat_path = K.PHOTO_DIR / rel
            if cat_path.exists():
                return str(cat_path)
        p = (get_photo(kw, "workplace_office", used_photos) or
             get_photo(kw, "classroom_studying_adults", used_photos) or
             get_photo(kw, "everyday_objects", used_photos))
        if p:
            used_photos.add(p)
        return p

    # p1: Front Cover
    pages.append(K.front_cover(front_cov))

    # p2: Inside Cover / Contents (strictly across single lines)
    pages.append(K.inside_cover(
        "Functional Skills English &bull; Reading",
        "Level 2 &bull; Comprehensive Textual Analysis &amp; Comparison Manual",
        "English Reading Level 2",
        [
            ("1&ndash;12", "All 12 Core Reading Topics &amp; Textual Analysis Drills (48 pages)", "5"),
            ("EXAM", "Pearson Edexcel Level 2 Strategy &amp; Comparison Mastery (6 pages)", "53"),
            ("M1&ndash;M2", "2 Complete Official Pearson Reading Mock Exam Papers (16 pages)", "59"),
            ("RUB", "Official Pearson Edexcel Reading Assessment Grids &amp; Rubrics (6 pages)", "75"),
            ("REF", "Complete Step-by-Step Solutions, Critical Glossary &amp; Index", "81"),
            ("REV", "Candidate Pre-Exam Readiness Commitments &amp; Progress Matrix", "85"),
        ],
        footer=BOOK
    ))

    # p3: Specification Overview
    p3_body = (
        K.page_title("Pearson Edexcel Level 2 Reading &bull; Specification Overview",
                     kicker="Curriculum Architecture &bull; DfE Subject Content L2.9 to L2.18", badge="SPEC")
        + K.box_html(
            "<div style='font-size:12.5pt;line-height:1.55;'>"
            "<p><b>Examination Structure:</b> The Pearson Edexcel Functional Skills English Level 2 Reading paper is an externally assessed, <b>75-minute</b> examination worth <b>35 marks</b>.</p>"
            "<p>Candidates must analyse and synthesize evidence across <b>three extended non-fiction texts</b> on a shared theme (e.g. workplace automation, healthcare ethics, environmental policy, or community regeneration).</p>"
            "<ul>"
            "<li><b>Core Challenge Areas:</b> Advanced implicit meaning, tone and register analysis, detecting subtle bias and propaganda, evaluating rhetorical and presentational devices, and synthesis across multiple sources.</li>"
            "<li><b>The 11-Mark Comparison Question:</b> The flagship question requiring candidates to compare ideas, arguments, and perspectives across two texts using direct comparative connectives and an evidence grid.</li>"
            "<li><b>Timing:</b> Approximately <b>2 minutes per mark</b>. Spend 15 minutes reading all three source passages thoroughly.</li>"
            "</ul>"
            "</div>",
            title="Pearson Edexcel Level 2 Reading Assessment Architecture"
        )
        + K.tip_pair(
            "For the 11-mark comparison question, ensure you provide balanced points from BOTH texts with direct comparative links.",
            "Do not confuse tone with purpose. Purpose is what the writer wants to achieve; tone is their attitude and voice.",
            golden_title="Band 4 Comparison Rule", watch_title="Critical Audit Trap"
        )
        + K.fill_notes("Personal Target Score &amp; High-Yield Topic Priorities", min_mm=30)
    )
    pages.append(K.page(p3_body, header=(BOOK, "Specification Overview"), footer=BOOK, page_no=3))

    # p4: Candidate Diagnostic Self-Audit Matrix
    p4_body = (
        K.page_title("Candidate Diagnostic Self-Audit Matrix", kicker="Baseline Skills Audit &bull; Level 2 Reading", badge="AUDIT")
        + K.box_html(
            "<p>Assess your confidence across the advanced Level 2 Reading competencies before beginning:</p>"
            + K.bullets([
                "Can you identify subtle bias in texts that appear neutral on the surface?",
                "Can you unpack implicit meanings, subtext, and irony in extended professional prose?",
                "Can you evaluate how rhetorical devices (rule of three, hyperbole, rhetorical questions) sway reader opinion?",
                "Can you systematically construct a side-by-side comparison of two authors' contrasting viewpoints?",
                "Can you explain exactly how layout and typography direct reader attention and convey authority?"
            ]),
            title="Core Functional Skills Level 2 Reading Competencies"
        )
        + K.fill_notes("Target Areas for Maximum Mark Gains", min_mm=35)
    )
    pages.append(K.page(p4_body, header=(BOOK, "Diagnostic Self-Audit"), footer=BOOK, page_no=4))

    # p5 to p52: 12 Reading Topics x 4 pages = 48 pages
    p_curr = 5
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        clean_title = topic["clean_topic"]
        lead = topic["intro_lead"]
        spec_pts = topic["spec_points"]
        rules = topic["golden_rules"]
        skills = topic.get("skills", [])
        models = topic.get("worked_models", [])
        traps = topic.get("examiner_traps", [])
        practice = topic.get("practice_questions", [])

        # Page 1: Topic Blueprint & Theory
        spec_text = "<br>".join(f"&bull; <b>{code}:</b> {desc}" for code, desc in spec_pts)
        rule_desc = rules[0]["desc"] if rules else "Read texts critically and evaluate evidence."
        p1_body = (
            K.page_title(f"Reading Topic {t_idx}: {clean_title}", kicker=f"Topic Blueprint &bull; Level 2 Reading", badge=f"R{t_idx}")
            + K.hero_image(P(clean_title, title=clean_title), f"Professional context for {clean_title}.", 52, fill=True)
            + K.rule_box("DfE Statutory Criteria &amp; Theoretical Architecture",
                         f"<div style='font-size:12.5pt;line-height:1.5;'>"
                         f"<p><b>Curriculum Standard:</b><br>{spec_text}</p>"
                         f"<p><b>Critical Principle:</b> {rule_desc}</p>"
                         f"</div>")
            + K.tip_pair(
                rules[1]["desc"] if len(rules) > 1 else "Always evaluate evidence and the writer's bias.",
                traps[0]["desc"] if traps else "Never assume quotes from experts are objective facts.",
                golden_title="Golden Method", watch_title="Examiner Audit Trap"
            )
        )
        pages.append(K.page(p1_body, header=(BOOK, f"Topic {t_idx} &bull; Blueprint"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 2: Advanced Text Analysis & Strategy Walkthrough
        first_model = models[0] if models else {}
        context_name = first_model.get("context", "Workplace Governance")
        q_prompt = first_model.get("question", "Read the extract and answer the analytical questions.")
        steps = first_model.get("steps", [])
        steps_html = "".join(f"<li><b>{s[0]} ({s[1]}):</b> {s[2]} <span style='color:var(--primary);font-weight:700;'>[{s[3]}]</span></li>" for s in steps) if steps else "<li>Evaluate arguments and textual evidence.</li>"

        p2_body = (
            K.page_title(f"{clean_title} &bull; Text Analysis", kicker=f"Extended Extract &bull; {context_name}", badge="PASSAGE")
            + K.box_html(
                f"<div style='background:#f8fafc;padding:3.5mm;border:1.5px solid var(--soft);border-radius:6px;font-size:11.5pt;line-height:1.5;margin-bottom:3mm;'>"
                f"<strong style='color:var(--primary);font-size:12pt;'>Extract &bull; {first_model.get('title', clean_title)}:</strong><br><br>"
                f"{q_prompt}"
                f"</div>",
                title=f"Source Passage &bull; {context_name}"
            )
            + K.box_html(
                f"<ol style='margin:0;padding-left:5mm;font-size:11pt;line-height:1.45;'>{steps_html}</ol>",
                title="Examiner Step-by-Step Analytical Protocol"
            )
            + K.fill_notes("Rhetorical Markers &amp; Subtext Notes", min_mm=28)
        )
        pages.append(K.page(p2_body, header=(BOOK, f"Topic {t_idx} &bull; Analysis"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 3: Band 4 Full-Marks Benchmark Model
        final_ans = first_model.get("final_answer", "Full benchmark response.")
        tutor_tip = first_model.get("tutor_tip", "Quote evidence and explain the writer's impact.")
        p3_body = (
            K.page_title(f"{clean_title} &bull; Band 4 Benchmark Exemplar", kicker="Examiner Full Marks Benchmark", badge="MODEL")
            + K.box_html(
                f"<div style='background:#ffffff;padding:3.5mm;border:1.5px solid #cbd5e1;border-radius:6px;font-size:11.5pt;line-height:1.5;'>"
                f"<strong style='color:var(--primary);'>Band 4 Model Answer:</strong><br><br>"
                f"{final_ans}"
                f"</div>",
                title=f"Official Benchmark Exemplar &bull; {first_model.get('marks', '3 Marks')}"
            )
            + K.tip_pair(
                tutor_tip,
                "Band 4 responses at Level 2 provide precise textual quotes paired with insightful explanations of the writer's deliberate effect on the reader.",
                golden_title="Band 4 Criteria", watch_title="Examiner Insight"
            )
            + K.fill_notes("Why This Answer Achieves Band 4 Distinction", min_mm=32)
        )
        pages.append(K.page(p3_body, header=(BOOK, f"Topic {t_idx} &bull; Model"), footer=BOOK, page_no=p_curr))
        p_curr += 1

        # Page 4: Candidate Comprehension Practice & Ruled Response Lines
        first_pr = practice[0] if practice else {}
        pr_q = first_pr.get("question", f"Read an extended workplace document and critically analyse how {clean_title.lower()} is used.")
        pr_marks = first_pr.get("marks", "3 Marks")
        p4_body = (
            K.page_title(f"{clean_title} &bull; Independent Practice", kicker=f"Analytical Challenge &bull; {pr_marks}", badge="DRILL")
            + K.box_html(
                f"<p style='font-size:11.5pt;margin:0 0 2mm 0;'><b>Comprehension &amp; Analysis Task:</b></p>"
                f"<div style='background:#f8fafc;padding:3mm;border:1px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>"
                f"{pr_q}"
                f"</div>",
                title=f"Examination Task Brief &bull; {pr_marks}"
            )
            + K.fill_lines(f"Write your analytical response below ({pr_marks}):", min_mm=170, gap_mm=9.5)
        )
        pages.append(K.page(p4_body, header=(BOOK, f"Topic {t_idx} &bull; Practice"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p53 to p58: Level 2 Reading Strategy & Comparison Masterclass (6 pages)
    l2_masterclasses = [
        ("The 75-Minute Examination Clock Strategy",
         "Pacing is critical on Level 2 Reading. Allocate 15 mins for thorough initial reading, 35 mins for Questions 1–10 (retrieval, language, layout, bias), and 25 mins for the synthesis & comparison tasks.",
         "Read the questions before reading the passages to prime your memory.", "Never start writing without reading all 3 texts — later questions compare multiple texts."),
        ("Deconstructing Implicit Meaning &amp; Subtext",
         "Level 2 examiners frequently test what is implied rather than stated. Look for euphemisms, sarcastic undertones, ironic contrasts, and what the writer deliberately omitted.",
         "Ask: 'What does the writer want me to feel without directly saying it?'", "Do not mistake speculation for valid inference — inference must be grounded in textual clues."),
        ("Detecting Sophisticated Bias &amp; Commercial Agenda",
         "Authors with a vested commercial or political interest often write in an authoritative, neutral tone while selectively presenting only supporting data.",
         "Check the author credentials and funding source.", "Notice which opposing viewpoints are missing from the argument."),
        ("Analyzing Rhetorical Devices in Persuasive Writing",
         "Identify rule of three, emotive vocabulary, hyperbole, rhetorical questions, and statistics. Explain how each device manipulates reader empathy or logic.",
         "Name the technique, quote the exact words, and explain the psychological effect.", "Do not just write 'it makes the reader think' — specify WHAT it makes them think."),
        ("Mastering the 11-Mark Comparison Question",
         "The comparison question is the highest-value question on the paper. Use an explicit 3-stage method: (1) Point of comparison, (2) Text A quote and interpretation, (3) Comparative connective (whereas, in contrast, similarly) and Text B quote.",
         "Ensure balanced weight: cite evidence equally from Text A and Text B.", "Never analyze Text A and Text B in separate isolated paragraphs — integrate them continuously."),
        ("Synthesis &amp; Cross-Referencing Evidence",
         "Questions asking you to synthesize information require combining facts from Text A and Text B into a unified conclusion or actionable recommendation.",
         "Combine data from both sources to create a complete answer.", "Clearly attribute which fact originates from Text A and which from Text B.")
    ]

    for em_idx, (em_title, em_desc, em_gold, em_trap) in enumerate(l2_masterclasses, 1):
        em_body = (
            K.page_title(f"Masterclass {em_idx}: {em_title}", kicker="Level 2 Analytical Strategy", badge=f"EX{em_idx}")
            + K.box_html(f"<p style='font-size:12.5pt;line-height:1.55;'>{em_desc}</p>", title="Core Examination Technique")
            + K.tip_pair(em_gold, em_trap, golden_title="Band 4 Strategy", watch_title="Common Exam Pitfall")
            + K.fill_notes(f"Personal Strategic Takeaways &amp; Checkpoints (Masterclass {em_idx})", min_mm=60)
        )
        pages.append(K.page(em_body, header=(BOOK, f"Masterclass {em_idx}"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p59 to p74: 2 Full Official Reading Mock Exams (16 pages: 8 pages per mock)
    # Mock 1 (8 pages)
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 1", kicker="Pearson Edexcel Level 2 &bull; 75 Minutes &bull; 35 Marks", badge="MOCK 1")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 extended reading extracts on the theme of 'Workplace Artificial Intelligence &amp; NHS Automation'.",
                "Answer all questions in the spaces provided.",
                "Total time: 75 minutes. Total marks: 35 marks.",
                "Dictionaries are strictly prohibited."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Spend 15 minutes reading all three source passages thoroughly.",
                     "For Question 14 (the comparison question), write in continuous integrated paragraphs.",
                     golden_title="Pacing Rule", watch_title="Comparison Strategy")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 1 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    mock1_l2_sections = [
        ("Text A: The Clinical Revolution &bull; Medical AI",
         "The deployment of automated diagnostic imaging software across NHS radiology departments has reduced scan interpretation backlogs by 42%. Dr Marcus Vance, Chief Medical Technology Officer, argues: 'Machine learning tools detect malignant micro-tumours with 96.8% precision, dramatically outperforming exhausted human clinicians working overnight shifts. Automation does not replace doctors; it rescues them from catastrophic burnout.'",
         [{"q": "<b>Question 1:</b> According to Text A, by what percentage have scan backlogs been reduced? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two advantages of automated diagnostic software claimed by Dr Vance. (2 marks)", "lines": 3}]),
        ("Text A Language &amp; Purpose Analysis",
         "Dr Vance acknowledges that algorithmic diagnostics require continuous oversight: 'Unsupervised automation invites algorithmic bias, especially across diverse patient demographic groups. We must retain robust clinical guardrails.'",
         [{"q": "<b>Question 3:</b> What does Dr Vance mean by the phrase 'algorithmic bias'? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Analyse how the writer of Text A uses emotive vocabulary to present human clinicians ('exhausted', 'catastrophic burnout'). (2 marks)", "lines": 3},
          {"q": "<b>Question 5:</b> What is the primary purpose of Text A? (1 mark)", "options": ["To demand the immediate sacking of human radiologists", "To advocate for the measured adoption of clinical AI tools", "To sell commercial software licenses to private hospitals", "To explain how to write Python code for medical algorithms"]}]),
        ("Text B: The Human Cost &bull; Trade Union Perspective",
         "Article by Sarah Jenkins, Healthcare Workers' Union:<br><em>'Beneath the glossy tech jargon lies an aggressive cost-cutting drive. Remote diagnostic hubs dehumanize medicine, isolating vulnerable patients behind cold glowing screens. When algorithms misread atypical symptoms, who bears legal accountability? Certainly not the Silicon Valley venture capitalists profiting from NHS procurement contracts.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how Sarah Jenkins uses rhetorical questions and emotive language to influence the reader. (2 marks)", "lines": 4}]),
        ("Text B Tone &amp; Text C Introduction",
         "Text C &bull; NHS England National Implementation Guidelines:<br>All Trusts adopting AI tools must complete a Data Protection Impact Assessment (DPIA) and ensure secondary validation by a senior consultant radiologist for any high-risk diagnostic classifications.",
         [{"q": "<b>Question 9:</b> How would you describe the overall tone of Text B? Support your answer with a quote. (2 marks)", "lines": 3},
          {"q": "<b>Question 10:</b> Identify the statutory assessment that NHS Trusts must complete according to Text C. (1 mark)", "lines": 2}]),
        ("Text C: Guidelines &amp; Governance Rules",
         "Trusts must provide mandatory 20-hour technical training for all healthcare practitioners interfacing with clinical decision-support systems. Bi-annual audits must be submitted to the Healthcare Governance Committee.",
         [{"q": "<b>Question 11:</b> How many hours of technical training are mandatory for staff? (1 mark)", "lines": 2},
          {"q": "<b>Question 12:</b> How frequently must clinical AI audits be submitted? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Identify two presentational features in Text C that convey official regulatory authority. (2 marks)", "lines": 3}]),
        ("The Flagship Comparison Question (Texts A &amp; B)",
         "Both Text A and Text B discuss the introduction of artificial intelligence in healthcare. Compare how the writers present differing perspectives on the impact of automation on staff and patient care.",
         [{"q": "<b>Question 14 (The 11-Mark Comparison Question):</b> In your response, compare: &bull; The differing viewpoints on technology &bull; How evidence and quotes are used &bull; The tone and persuasive techniques in each text. Use comparative connectives and integrate quotes from both texts. (11 marks)", "lines": 14}]),
        ("Synthesis &amp; Final Evaluation",
         "Synthesize findings from all three texts to evaluate how the NHS can achieve safety while modernizing clinical operations.",
         [{"q": "<b>Question 15:</b> Synthesizing ideas from Text A, Text B, and Text C, explain three essential safeguards needed when introducing clinical AI tools into hospital wards. (3 marks)", "lines": 6}])
    ]

    for p_title, p_extract, p_qs in mock1_l2_sections:
        p_body = (
            K.page_title(f"Mock 1 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 1", badge="M1")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 1 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Mock 2 (8 pages)
    pages.append(K.page(
        K.page_title("Official Reading Mock Examination &bull; Paper 2", kicker="Pearson Edexcel Level 2 &bull; 75 Minutes &bull; 35 Marks", badge="MOCK 2")
        + K.box_html(
            "<p><b>Instructions for Candidates:</b></p>"
            + K.bullets([
                "This paper contains 3 extended reading extracts on 'Remote Working, Urban Decline &amp; The Future of Cities'.",
                "Answer all questions in the spaces provided.",
                "Time allowed: 75 minutes. Total marks: 35 marks.",
                "Check your answers against the official mark scheme on p86."
            ]),
            title="Examination Protocol"
        )
        + K.tip_pair("Keep your comparison structured with direct comparative connectives (in contrast, conversely).",
                     "Ensure every claim is supported with a quotation from the source text.",
                     golden_title="Top Scoring Advice", watch_title="Evidence Requirement")
        + K.fill_notes("Personal Target Score &amp; Time Checkpoints", min_mm=38),
        header=(BOOK, "Mock 2 &bull; Instructions"), footer=BOOK, page_no=p_curr
    ))
    p_curr += 1

    mock2_l2_sections = [
        ("Text A: The Freedom Economy &bull; Work from Home",
         "The shift toward flexible remote working has liberated millions of British workers from soul-destroying daily commutes. Economist Priya Sharma reports: 'Remote employees save an average of &pound;2,800 annually in rail fares and 380 hours in travel time. Productivity metrics across professional services have risen by 14%, disproving the antiquated myth that staff only work when surveilled in open-plan offices.'",
         [{"q": "<b>Question 1:</b> According to Text A, how much money do remote workers save on rail fares annually? (1 mark)", "lines": 2},
          {"q": "<b>Question 2:</b> Identify two benefits of remote working stated by Priya Sharma. (2 marks)", "lines": 3}]),
        ("Text A Language &amp; Argumentation",
         "Sharma notes that decentralized work stimulates regional market towns: 'Spending that once flowed exclusively into Central London now invigorates local bakeries, high streets, and community enterprises across the Home Counties.'",
         [{"q": "<b>Question 3:</b> What does Sharma mean by 'decentralized work'? (1 mark)", "lines": 2},
          {"q": "<b>Question 4:</b> Analyse how the writer of Text A uses emotive phrasing ('soul-destroying', 'liberated', 'antiquated myth') to persuade the reader. (2 marks)", "lines": 3},
          {"q": "<b>Question 5:</b> Identify the primary purpose of Text A. (1 mark)", "options": ["To persuade readers that remote working benefits individuals and regional economies", "To advise people how to buy cheap rail season tickets", "To criticize employees who spend money in local bakeries", "To announce the closure of all train lines into London"]}]),
        ("Text B: The Hollowed High Street &bull; Chamber of Commerce",
         "Statement by Arthur Pendelton, City Centre Retail Coalition:<br><em>'Our city centres are becoming ghost towns. Footfall across commercial districts has plunged by 35%, driving hundreds of independent sandwich bars, dry cleaners, and family-owned cafes into bankruptcy. Corporate landlords and remote workers abandon the civic ecosystem that sustained British commerce for generations. Without urgent return-to-office mandates, urban culture faces irreversible extinction.'</em>",
         [{"q": "<b>Question 6:</b> Extract one fact from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 7:</b> Extract one opinion from Text B. (1 mark)", "lines": 2},
          {"q": "<b>Question 8:</b> Explain how Pendelton uses catastrophic imagery ('ghost towns', 'bankruptcy', 'extinction') to convey urgency. (2 marks)", "lines": 4}]),
        ("Text B Tone &amp; Text C Introduction",
         "Text C &bull; Parliamentary Commission on Future Urban Planning:<br>Recommendation 1: Local authorities must grant expedited planning permission for converting vacant commercial office premises into affordable residential apartments and creative co-working spaces.",
         [{"q": "<b>Question 9:</b> How would you describe the tone of Text B? Support your answer with a quotation. (2 marks)", "lines": 3},
          {"q": "<b>Question 10:</b> According to Text C, what planning permission should local authorities grant? (1 mark)", "lines": 2}]),
        ("Text C: Urban Regeneration Policy",
         "Recommendation 2: Establish 'Enterprise Hubs' in municipal town halls providing subsidised gigabit broadband, hot-desking, and childcare facilities. Funding will be allocated from the National Infrastructure Levelling Fund.",
         [{"q": "<b>Question 11:</b> Name two facilities provided in Enterprise Hubs according to Text C. (2 marks)", "lines": 3},
          {"q": "<b>Question 12:</b> Which national fund will finance the Enterprise Hubs? (1 mark)", "lines": 2},
          {"q": "<b>Question 13:</b> Explain how the layout of Text C (numbered recommendations) helps policy makers. (1 mark)", "lines": 2}]),
        ("The Flagship Comparison Question (Texts A &amp; B)",
         "Both Text A and Text B explore the consequences of the rise in remote working. Compare how the writers present contrasting arguments regarding the social and economic impact on communities.",
         [{"q": "<b>Question 14 (The 11-Mark Comparison Question):</b> In your answer, compare: &bull; The opposing views on where economic value is created &bull; How each writer characterizes remote workers &bull; The contrasting tone, language, and stylistic devices. Include quotes from both texts. (11 marks)", "lines": 14}]),
        ("Synthesis &amp; Future Recommendations",
         "Synthesize ideas from all three texts to suggest a balanced model for future working arrangements.",
         [{"q": "<b>Question 15:</b> Synthesizing insights from Text A, Text B, and Text C, propose three strategies for balancing remote employee flexibility with the survival of urban town centres. (3 marks)", "lines": 6}])
    ]

    for p_title, p_extract, p_qs in mock2_l2_sections:
        p_body = (
            K.page_title(f"Mock 2 &bull; {p_title}", kicker="Official Examination Booklet &bull; Reading Paper 2", badge="M2")
            + K.box_html(f"<div style='background:#f8fafc;padding:3mm;border:1.5px solid var(--soft);border-radius:4px;font-size:11pt;line-height:1.45;'>{p_extract}</div>", title="Reading Passage")
            + K.exercise_list(p_qs, lines=3)
        )
        pages.append(K.page(p_body, header=(BOOK, "Mock 2 &bull; Reading"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p75 to p80: Official Pearson Edexcel Level 2 Reading Assessment Grids & Rubrics (6 pages)
    l2_rubrics = [
        ("The 11-Mark Comparison Question Band Descriptors",
         "Band 4 (9–11 marks): Perceptive, detailed comparison across both texts; continuous direct comparative connectives; insightful analysis of perspectives and stylistic devices; balanced, well-chosen quotations.<br>"
         "Band 3 (6–8 marks): Clear comparison with sound identification of similarities and differences; appropriate quotes from both texts; mostly balanced structure.<br>"
         "Band 2 (3–5 marks): Basic comparison with superficial links; relies heavily on paraphrase; unbalanced coverage favoring one text.<br>"
         "Band 1 (1–2 marks): Isolated comments on one or both texts with no meaningful comparative synthesis."),
        ("Tone, Voice &amp; Register Assessment Criteria (L2.15)",
         "Full marks awarded for identifying the specific adjective defining tone (e.g. indignant, urgent, impassioned, clinical, detached) paired with accurate lexical evidence and explanation of reader impact."),
        ("Implicit Meaning &amp; Subtext Marking Guidance (L2.11)",
         "Candidates must demonstrate insight into the writer's subtext, irony, or underlying assumptions rather than merely repeating literal surface statements."),
        ("Rhetorical &amp; Language Devices Assessment (L2.14)",
         "Examiners award marks for identifying the rhetorical device (hyperbole, rule of three, rhetorical question) AND explaining its exact psychological or persuasive influence on the target audience."),
        ("Evaluating Bias &amp; Argumentation Criteria (L2.16)",
         "Full marks require candidates to distinguish verifiable factual claims from subjective vested interests, identifying omissions or unbalanced evidence."),
        ("Synthesis &amp; Cross-Referencing Standards (L2.18)",
         "Marks awarded for correctly extracting and synthesizing disparate pieces of information from two or three separate source texts to draw a valid comprehensive conclusion.")
    ]

    for r_idx, (r_title, r_desc) in enumerate(l2_rubrics, 1):
        r_body = (
            K.page_title(f"Level 2 Assessment Criteria &bull; Part {r_idx} of 6", kicker=r_title, badge=f"RUB{r_idx}")
            + K.box_html(
                f"<div style='font-size:12pt;line-height:1.55;'>{r_desc}</div>",
                title="Official Pearson Edexcel Level 2 Marking Protocol"
            )
            + K.fill_notes(f"Personal Band 4 Action Plan &amp; Audit Notes (Part {r_idx})", min_mm=45)
        )
        pages.append(K.page(r_body, header=(BOOK, f"Assessment Criteria Part {r_idx}/6"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # p81 to p102: Complete Solutions, Critical Glossary & Index (22 pages)
    ref_blocks = []

    # Topic Practice Solutions (Topics 1 to 12)
    for t_idx, topic in enumerate(ert.READING_TOPICS[:12], 1):
        first_pr = topic.get("practice_questions", [{}])[0]
        sol_text = first_pr.get("solution_steps", "Full worked steps.")
        ans_text = first_pr.get("correct_answer", "Correct benchmark answer.")
        ref_blocks.append(K.ref_block(
            f"Topic {t_idx}: {topic['clean_topic']} Solutions",
            K.ref_qa(f"R{t_idx}", f"<b>Analysis:</b> {sol_text}<br><b>Benchmark Answer:</b> {ans_text}", marks=first_pr.get("marks", "3m"))
        ))

    # Mock 1 Full Solutions
    m1_l2_ans = [
        ("Q1", "42%", "1m", "Direct retrieval from Text A paragraph 1."),
        ("Q2", "Detects malignant micro-tumours with 96.8% precision / Rescues clinicians from catastrophic burnout", "2m", "1m for each valid point."),
        ("Q3", "Systematic errors in computer algorithms that unfairly disadvantage specific demographic groups", "1m", "Conceptual vocabulary definition."),
        ("Q4", "Words like 'catastrophic burnout' elicit deep empathy, framing automation as a compassionate saviour rather than a managerial replacement", "2m", "1m for quote/analysis, 1m for impact."),
        ("Q5", "B: To advocate for the measured adoption of clinical AI tools", "1m", "Multiple choice key."),
        ("Q6", "Remote diagnostic hubs are being deployed / Tech companies hold NHS procurement contracts", "1m", "Verifiable fact."),
        ("Q7", "Remote hubs dehumanize medicine / Software venture capitalists profit excessively", "1m", "Subjective value judgment."),
        ("Q8", "Rhetorical question ('who bears legal accountability?') casts doubt on corporate safety, positioning patients as exploited victims", "2m", "1m for device/quote, 1m for impact."),
        ("Q9", "Impassioned, indignant, and skeptical ('cold glowing screens', 'irreversible extinction')", "2m", "1m for tone label, 1m for quote."),
        ("Q10", "Data Protection Impact Assessment (DPIA)", "1m", "Direct statutory retrieval."),
        ("Q11", "20 hours", "1m", "Direct retrieval."),
        ("Q12", "Bi-annually (twice a year)", "1m", "Direct retrieval."),
        ("Q13", "Numbered legal clauses and formal regulatory headings convey strict statutory compliance", "2m", "1m for feature, 1m for effect."),
        ("Q14", "<b>Band 4 Model Answer (11 Marks):</b><br>"
                "Text A presents a progressive, technological perspective, portraying AI as a vital clinical asset that 'rescues' exhausted doctors from burnout. In sharp contrast, Text B adopts an indignant trade-union stance, contending that technology 'dehumanizes medicine' and serves corporate profit.<br><br>"
                "Furthermore, whereas Text A validates its argument using quantitative medical statistics ('96.8% precision', '42% backlog reduction') to project scientific authority, Text B relies on evocative rhetorical questions and emotive metaphors ('cold glowing screens') to arouse ethical apprehension.<br><br>"
                "However, both writers concede that human supervision remains essential: Text A explicitly cautions that 'unsupervised automation invites algorithmic bias', which aligns directly with Text B's demand for clear legal accountability and Text C's mandatory secondary validation protocol.", "11m", "Comprehensive Band 4 comparative synthesis."),
        ("Q15", "(1) Mandatory secondary validation by human consultants; (2) Comprehensive 20-hour staff training; (3) Rigorous bi-annual ethical audits", "3m", "1m for each safeguard synthesized.")
    ]
    m1_l2_html = "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m1_l2_ans)
    ref_blocks.append(K.ref_block("Official Reading Mock Examination 1 &bull; Full Mark Scheme &amp; Solutions (35 Marks)", m1_l2_html))

    # Mock 2 Full Solutions
    m2_l2_ans = [
        ("Q1", "£2,800 annually", "1m", "Direct retrieval from Text A."),
        ("Q2", "Saves 380 travel hours / Increases professional productivity by 14%", "2m", "1m for each point."),
        ("Q3", "Working away from a centralized central office, typically from home or local co-working spaces", "1m", "Conceptual definition."),
        ("Q4", "Phrases like 'soul-destroying' and 'antiquated myth' delegitimize traditional office attendance, portraying remote work as enlightened progress", "2m", "1m for quote, 1m for persuasive effect."),
        ("Q5", "A: To persuade readers that remote working benefits individuals and regional economies", "1m", "Multiple choice key."),
        ("Q6", "Footfall across commercial districts has plunged by 35%", "1m", "Verifiable statistic."),
        ("Q7", "Our city centres are becoming ghost towns / Urban culture faces irreversible extinction", "1m", "Subjective hyperbolic opinion."),
        ("Q8", "Catastrophic language creates an existential crisis, pressurizing policymakers to mandate office returns", "2m", "1m for quote, 1m for impact."),
        ("Q9", "Alarmist, urgent, and despairing ('bankruptcy', 'abandoned', 'extinction')", "2m", "1m for tone label, 1m for quote."),
        ("Q10", "Expedited planning permission for converting vacant offices into residential apartments and co-working hubs", "1m", "Direct policy retrieval."),
        ("Q11", "Subsidised gigabit broadband / hot-desking / childcare facilities (any two)", "2m", "1m each."),
        ("Q12", "National Infrastructure Levelling Fund", "1m", "Direct retrieval."),
        ("Q13", "Numbered recommendations provide an unambiguous sequential roadmap for local council executives", "1m", "Layout functionality."),
        ("Q14", "<b>Band 4 Model Answer (11 Marks):</b><br>"
                "Text A celebrates remote working as a triumph of individual autonomy and regional redistribution, arguing that saving '£2,800' and '380 hours' stimulates suburban high streets. Conversely, Text B laments this development as an economic catastrophe, warning that a 35% footfall collapse threatens urban commercial centres with 'irreversible extinction'.<br><br>"
                "Stylistically, Text A employs an optimistic, professional register grounded in productivity research, whereas Text B leverages dramatic, apocalyptic imagery ('ghost towns', 'abandon the civic ecosystem') to lobby for corporate office mandates.<br><br>"
                "While Text A champions the worker's personal sovereignty, Text B prioritizes the collective civic community. Ultimately, Text C bridges this ideological divide by proposing the pragmatic conversion of vacant urban offices into hybrid co-working hubs and residential dwellings.", "11m", "Comprehensive Band 4 comparative synthesis."),
        ("Q15", "(1) Convert obsolete commercial offices into affordable housing; (2) Create subsidized municipal co-working hubs; (3) Adopt hybrid working schedules combining office collaboration with remote focus days", "3m", "1m for each synthesized policy.")
    ]
    m2_l2_html = "".join(K.ref_qa(q, a, marks=m, working=w) for q, a, m, w in m2_l2_ans)
    ref_blocks.append(K.ref_block("Official Reading Mock Examination 2 &bull; Full Mark Scheme &amp; Solutions (35 Marks)", m2_l2_html))

    # Level 2 Critical Reading Glossary
    glossary_l2 = [
        ("Algorithmic Bias", "Systematic unfairness embedded in automated systems reflecting unrepresentative source data."),
        ("Comparative Connectives", "Conjunctions that establish explicit contrasts or parallels between texts (whereas, conversely, in contrast, similarly)."),
        ("Connotation", "The emotional or cultural association evoked by a word beyond its literal dictionary definition."),
        ("Counter-Argument", "An argument formulated to oppose or disprove an existing perspective."),
        ("Euphemism", "A mild or indirect word substituted for one considered harsh or blunt."),
        ("Hyperbole", "Deliberate exaggeration used for dramatic rhetorical emphasis."),
        ("Implicit Meaning", "Ideas suggested, hinted at, or embedded within the subtext of a passage."),
        ("Irony", "Expressing meaning by using language that normally signifies the opposite, typically for humorous or critical effect."),
        ("Objectivity", "Judgments based purely on observable, verifiable facts free from personal bias."),
        ("Register", "The variety and formality of language used in a specific professional or social context."),
        ("Rhetorical Question", "A question posed to provoke thought or persuade rather than elicit an answer."),
        ("Subjectivity", "Statements based on personal opinions, interpretations, feelings, or points of view."),
        ("Synthesis", "Combining diverse facts and perspectives from multiple sources into a coherent whole."),
        ("Tone", "The author's underlying attitude or perspective communicated through vocabulary and syntax."),
        ("Vested Interest", "A personal or commercial stake in an issue that influences objectivity.")
    ]
    gl_l2_html = "".join(f"<p><b>{w}:</b> {d}</p>" for w, d in glossary_l2)
    ref_blocks.append(K.ref_block("Critical Lexicon of Advanced Literary &amp; Textual Analysis", gl_l2_html))

    # Level 2 Subject Index
    index_l2_items = [
        ("A", [("Algorithmic Bias", "2, 8, 81"), ("Argumentation Lines", "8, 54"), ("The Writer's Voice", "9, 54")]),
        ("B", [("Band 4 Comparison Criteria", "75"), ("Bias Detection", "8, 54")]),
        ("C", [("Comparison Question (11 Marks)", "11, 55, 65, 73"), ("Connotation", "2, 7")]),
        ("D", [("Deconstructing Subtext", "53"), ("Diagnostic Matrix", "4")]),
        ("E", [("Emotive Language", "7, 54"), ("Evaluating Evidence", "8, 54")]),
        ("G", [("Glossary of Terms", "98"), ("Golden Comparison Rules", "55")]),
        ("H", [("Hyperbole Analysis", "7, 54")]),
        ("I", [("Implicit Meaning", "2, 53"), ("Irony &amp; Sarcasm", "9, 53")]),
        ("L", [("Layout Authority", "4, 5, 55")]),
        ("M", [("Mock Exam 1 (Medical AI)", "59"), ("Mock Exam 2 (Remote Work)", "67")]),
        ("O", [("Objectivity vs. Subjectivity", "1, 8")]),
        ("P", [("Pacing Strategy (75 Mins)", "3, 53"), ("Persuasive Devices", "7, 54")]),
        ("R", [("Rhetorical Questions", "7, 54")]),
        ("S", [("Synthesis Methods", "11, 56, 66, 74")]),
        ("T", [("Timing (2 Mins/Mark)", "3, 53"), ("Tone &amp; Register", "9, 54")]),
        ("V", [("Vested Interests", "8, 54")])
    ]
    ix_l2_html = ""
    for letter, entries in index_l2_items:
        items = "".join(f"<div class='ix'><span>{escape_html(t)}</span><span>{escape_html(p)}</span></div>" for t, p in entries)
        ix_l2_html += f"<div class='ix-letter'>{letter}</div>{items}"
    ref_blocks.append(K.ref_block("Level 2 Reading Alphabetical Subject Index", ix_l2_html))

    cover_theme = K.theme_from_cover(front_cov)
    ref_page_list = K.ref_pages("Reference Section: Solutions, Glossary &amp; Index", ref_blocks,
                                BOOK, start_page=p_curr, subtitle="Complete Worked Solutions, Lexicon &amp; Alphabetical Index",
                                cols=2, theme=cover_theme, notes_title="Candidate Analytical Notes")
    pages.extend(ref_page_list)
    p_curr += len(ref_page_list)

    # p103: Pre-Exam Readiness Commitments & Progress Matrix
    p103_body = (
        K.page_title("Level 2 Reading &bull; Exam Day Commitments", kicker="Final Revision &bull; Band 4 Mastery", badge="READY")
        + K.box_html(
            "<p>Before sitting your Pearson Edexcel Level 2 Reading examination, commit to these 5 Band 4 imperatives:</p>"
            + K.bullets([
                "<b>1. Allocate Time for All 3 Texts:</b> Spend the first 15 minutes actively reading all extracts before writing.",
                "<b>2. Integrate Your Comparison:</b> In Question 14, link Text A and Text B continuously with comparative connectives.",
                "<b>3. Quote and Analyse:</b> Always pair direct textual quotations with explanations of the writer's deliberate effect.",
                "<b>4. Distinguish Fact from Bias:</b> Question the writer's motives and identify vested commercial or political interests.",
                "<b>5. Protect Your Synthesis:</b> In multi-text questions, combine evidence from across the sources rather than relying on one."
            ]),
            title="Golden Exam Rules for Level 2 Reading Success"
        )
        + K.fill_notes("Personal Pre-Exam Commitments &amp; Tutor Endorsement", min_mm=45)
    )
    pages.append(K.page(p103_body, header=(BOOK, "Exam Readiness"), footer=BOOK, page_no=p_curr))
    p_curr += 1

    # Duplex balance check before back cover
    if (len(pages) + 1) % 2 != 0:
        p_extra = (
            K.page_title("Candidate Final Verification Protocol", kicker="Pearson Edexcel Band 4 Reading Standards", badge="AUDIT")
            + K.box_html(
                "<p>Final pre-submission audit checklist:</p>"
                + K.bullets([
                    "Did you integrate comparative connectives in the 11-mark comparison question?",
                    "Did you clearly name specific language and layout techniques with direct quotes?",
                    "Did you review your answers against the author's overall tone and purpose?"
                ]),
                title="Final Verification"
            )
            + K.fill_notes("Final Examination Reflections", min_mm=40)
        )
        pages.append(K.page(p_extra, header=(BOOK, "Verification Protocol"), footer=BOOK, page_no=p_curr))
        p_curr += 1

    # Back Cover
    pages.append(K.back_cover(back_cov))

    print(f"Total Pages Assembled: {len(pages)}")
    out_pdf = DOWNLOADS / "MasterFunctionalSkills_English_Reading_Level_2_Core_Guide.pdf"
    res = K.render_pdf(pages, out_pdf, theme=cover_theme, entry3=False, title="Master Functional Skills - English Reading Level 2 Core Guide")
    shutil.copy(out_pdf, DOCUMENTS / out_pdf.name)
    print(f"Verified & Saved: {out_pdf} -> {DOCUMENTS / out_pdf.name}")
    return res


def main():
    build_reading_l1_core()
    build_reading_l2_core()
    print("\nALL READING SUITE BUILDS COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
