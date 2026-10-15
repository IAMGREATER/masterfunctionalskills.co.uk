#!/usr/bin/env python3
"""
Complete Builder for Deck 3: Functional Skills English - Level 2 (48 Cards)
Generates strand_a.py, strand_b.py, strand_c.py and __init__.py.
"""
import os
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

# Import Strand A
from build_english_l2 import CARDS_A

CARDS_B = [
    # 19. Formal Letter Writing
    {
        "id": "e-l2-19",
        "number": 19,
        "title": "Formal Letter Layout &amp; Salutations",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W19",
        "rule_heading": "Addresses, Date &amp; Salutation Rules",
        "rule_body": "Sender address top right. Recipient address top left below date. Rule: Dear Sir/Madam ends with 'Yours faithfully'. Named person (Dear Mr Smith) ends with 'Yours sincerely'.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="280" y="24" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Your Address (Top Right)</text>
            <text x="280" y="38" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Date</text>
            <text x="60" y="55" font-size="9" font-weight="700" fill="#64748b">Their Address (Top Left)</text>
            <text x="60" y="78" font-size="11" font-weight="800" fill="#1e40af">Dear Sir/Madam  →  Yours faithfully</text>
            <text x="60" y="100" font-size="11" font-weight="800" fill="#059669">Dear Mr Jones  →  Yours sincerely</text>
          </g>"""),
        "golden_rule": "Sir/Madam = Faithfully (strangers) • Named = Sincerely (someone you name)!",
        "watch_out": "Never mix them up: 'Dear Sir' paired with 'Yours sincerely' loses format marks.",
        "challenge_prompt": "You are writing a formal complaint to customer services and do not know the recipient's name. How should you open and close the letter?",
        "answer_text": "Open with: 'Dear Sir or Madam,' and close with: 'Yours faithfully,' followed by your full printed name."
    },

    # 20. Formal Report Structure
    {
        "id": "e-l2-20",
        "number": 20,
        "title": "Formal Report Structure",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W20",
        "rule_heading": "Title • Background • Findings • Recommendations",
        "rule_body": "A professional report requires 5 distinct sections: 1. Title. 2. Introduction / Purpose. 3. Current Findings / Key Issues (with subheadings). 4. Conclusion. 5. Actionable Recommendations.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="24" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">REPORT FORMAT BLUEPRINT</text>
            <text x="30" y="50" font-size="10.5" font-weight="800" fill="#0f172a">1. Title: Report into Staff Parking Facilities</text>
            <text x="30" y="70" font-size="10.5" font-weight="700" fill="#475569">2. Introduction &amp; Purpose</text>
            <text x="30" y="90" font-size="10.5" font-weight="700" fill="#475569">3. Key Findings (Subheading 1 &amp; 2)</text>
            <text x="30" y="112" font-size="10.5" font-weight="800" fill="#059669">4. Conclusion &amp; Actionable Recommendations</text>
          </g>"""),
        "golden_rule": "Reports must be impersonal, objective, and finish with bulleted recommendations!",
        "watch_out": "Don't write a narrative story — use professional passive tone and clear subheadings.",
        "challenge_prompt": "What final section is mandatory at the end of every workplace formal report?",
        "answer_text": "The Recommendations section (proposing clear, actionable next steps based on the findings)."
    },

    # 21. Newspaper / Magazine Article
    {
        "id": "e-l2-21",
        "number": 21,
        "title": "Article Writing (Newspaper/Magazine)",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W21",
        "rule_heading": "Headline • Strapline • Byline • Hook",
        "rule_body": "Articles must feature: 1. Punchy Headline (alliteration/pun). 2. Byline ('By [Name]'). 3. Engaging hook opening paragraph. 4. Balanced body exploring perspectives. 5. Concluding thought-provoking call to action.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="900" fill="#0f172a" text-anchor="middle">HEADLINE: CATCHY &amp; BOLD</text>
            <text x="170" y="45" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">Byline: By Alex Morgan, Health Correspondent</text>
            <line x1="30" y1="55" x2="310" y2="55" stroke="#cbd5e1"/>
            <text x="40" y="75" font-size="10.5" font-weight="700" fill="#2563eb">Hook opening: Introduce the debate with a question</text>
            <text x="40" y="98" font-size="10.5" font-weight="700" fill="#475569">Balanced body paragraphs exploring both viewpoints</text>
            <text x="40" y="118" font-size="10.5" font-weight="800" fill="#059669">Final call to action for the reader</text>
          </g>"""),
        "golden_rule": "Every article must start with a captivating Headline and a Byline!",
        "watch_out": "Don't draw mock newspaper columns or pictures — just write the text with headers.",
        "challenge_prompt": "Create an engaging alliterative headline for an article about the dangers of smartphone addiction.",
        "answer_text": "Example: 'Screen Slavery: The Silent Struggle of Smartphone Addicts'."
    },

    # 22. Persuasive Speech / Presentation Script
    {
        "id": "e-l2-22",
        "number": 22,
        "title": "Speech &amp; Presentation Writing",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W22",
        "rule_heading": "Welcome • Passion • Rhetoric • Final Appeal",
        "rule_body": "Speeches are written to be spoken aloud: 1. Greet audience ('Good morning fellow council members'). 2. State clear conviction. 3. Use rhetorical devices (rule of 3, pause cues). 4. Close with a memorable final rallying call.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">SPEECH STRUCTURE</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">1. Direct Greeting: "Ladies and gentlemen..."</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">2. Rhetorical Triples: "We can, we must, we will."</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#be185d">3. Thank the audience: "Thank you for your time."</text>
          </g>"""),
        "golden_rule": "Write in a spoken voice with direct address ('you', 'we', 'our community')!",
        "watch_out": "Remember to thank the audience at the very end of the speech.",
        "challenge_prompt": "Write the opening two sentences of a speech to high school students advocating for mental health days.",
        "answer_text": "'Good morning students and staff. Have you ever felt so overwhelmed by exam pressure that you simply could not face another day?'"
    },

    # 23. Formal Workplace Email
    {
        "id": "e-l2-23",
        "number": 23,
        "title": "Formal Workplace Email",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W23",
        "rule_heading": "Subject Line • Professional Body • Sign-off",
        "rule_body": "Email format: 1. Informative Subject line (concise, clear). 2. Professional salutation (Dear Mr Davis / Dear Team). 3. Purpose stated in opening sentence. 4. Clear bulleted action points. 5. Formal sign-off (Kind regards).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="25" y="24" font-size="10" font-weight="800" fill="#0f172a">To: sarah.jenkins@healthtrust.nhs.uk</text>
            <text x="25" y="42" font-size="10" font-weight="800" fill="#2563eb">Subject: Urgent: Quarterly Clinical Audit Review - 14 Oct</text>
            <line x1="15" y1="52" x2="325" y2="52" stroke="#cbd5e1"/>
            <text x="25" y="70" font-size="10.5" font-weight="700" fill="#0f172a">Dear Ms Jenkins,</text>
            <text x="25" y="90" font-size="10" font-weight="700" fill="#475569">I am writing to confirm the schedule for Thursday's review...</text>
            <text x="25" y="115" font-size="10" font-weight="800" fill="#059669">Kind regards, / Best regards,</text>
          </g>"""),
        "golden_rule": "Subject line must be specific: 'Urgent Budget Query', NOT just 'Hi' or 'Meeting'!",
        "watch_out": "Don't use casual sign-offs like 'Cheers' or 'Thanks a lot' in a formal work email.",
        "challenge_prompt": "Write an appropriate subject line for an email requesting two days of annual leave.",
        "answer_text": "Subject: Annual Leave Request: 14th–15th November - [Your Name]."
    },

    # 24. Online Review
    {
        "id": "e-l2-24",
        "number": 24,
        "title": "Writing an Online Review",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W24",
        "rule_heading": "Balanced Evaluation &amp; Verdict",
        "rule_body": "Reviews must be balanced and credible: 1. Star rating or headline score. 2. What was experienced / purchased. 3. Positive features (pros). 4. Shortcomings or areas for improvement (cons). 5. Final verdict &amp; recommendation.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="900" fill="#b45309" text-anchor="middle">★★★★☆ (4/5 Stars) - Balanced Review</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#059669">✓ Strengths: Excellent battery life &amp; crisp screen</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#dc2626">✗ Weaknesses: Charging cable feels flimsy</text>
            <text x="30" y="108" font-size="11" font-weight="800" fill="#0f172a">Final Verdict: Highly recommended for students.</text>
          </g>"""),
        "golden_rule": "A top-level review must be balanced — mention at least one drawback even if you loved it!",
        "watch_out": "Don't just rant emotionally; give specific evidence and examples.",
        "challenge_prompt": "Why is a review that includes both positive and negative aspects more persuasive than one with only praise?",
        "answer_text": "A balanced review appears objective, credible, and authentic, whereas uncritical praise looks like sponsored advertising."
    },

    # 25. Informative Leaflet / Guide
    {
        "id": "e-l2-25",
        "number": 25,
        "title": "Informative Leaflet / Guide",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W25",
        "rule_heading": "Signposting • Chunks • Contact Box",
        "rule_body": "Leaflet layout: 1. Engaging title with benefit for reader. 2. Brief introductory overview. 3. Section subheadings with bulleted practical tips. 4. Contact details / Where to find further help box.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">LEAFLET FORMAT</text>
            <text x="25" y="52" font-size="10.5" font-weight="800" fill="#0f172a">Title: Healthy Eating on a Budget</text>
            <text x="25" y="74" font-size="10.5" font-weight="700" fill="#475569">Subheading: Top Tips for Smarter Shopping</text>
            <text x="25" y="94" font-size="10.5" font-weight="700" fill="#475569">• Plan meals weekly  • Buy frozen produce</text>
            <text x="25" y="115" font-size="10.5" font-weight="800" fill="#059669">Contact: Visit www.nhs.uk/budget-meals</text>
          </g>"""),
        "golden_rule": "Always include contact details, website links, or hotline numbers at the end of a leaflet!",
        "watch_out": "Keep sentences concise — leaflets are designed for quick scanning, not essay reading.",
        "challenge_prompt": "State two layout features that make a healthcare leaflet easy for patients to navigate.",
        "answer_text": "1. Informative subheadings dividing topics. 2. Bullet points highlighting key advice clearly."
    },

    # 26. Online Blog / Opinion Editorial
    {
        "id": "e-l2-26",
        "number": 26,
        "title": "Blog Post &amp; Opinion Editorial",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W26",
        "rule_heading": "Personal Voice &amp; Reader Interaction",
        "rule_body": "Blog features: 1. Catchy conversational title. 2. Date and author handle. 3. Strong first-person personal voice ('I couldn't believe it when...'). 4. Conversational tone with witty anecdotes. 5. Call for comments at the end.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">BLOG POST FORMAT</text>
            <text x="25" y="52" font-size="10.5" font-weight="800" fill="#0f172a">Title: Confessions of a Commuter</text>
            <text x="25" y="74" font-size="10" font-weight="700" fill="#475569">Personal tone: "Like many of you, I dread the 7:15 train..."</text>
            <rect x="25" y="90" width="290" height="26" rx="4" fill="#ec4899"/>
            <text x="170" y="108" font-size="10.5" font-weight="800" fill="#ffffff" text-anchor="middle">Call to comments: "What do you think? Leave a reply!"</text>
          </g>"""),
        "golden_rule": "Always invite reader comments or debate at the end of an online blog!",
        "watch_out": "While conversational, your grammar and spelling must still be 100% accurate.",
        "challenge_prompt": "Write a closing sentence for a blog post discussing cycle lanes in cities.",
        "answer_text": "'Do cycle lanes make your journey safer or cause traffic chaos? Share your thoughts in the comments below!'"
    },

    # 27. Paragraphing: The PEEL Technique
    {
        "id": "e-l2-27",
        "number": 27,
        "title": "PEEL / TEEL Paragraphs",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W27",
        "rule_heading": "Point • Evidence • Explanation • Link",
        "rule_body": "Every body paragraph should follow PEEL: Point (topic sentence statement). Evidence (fact, statistic, or quote). Explanation (analyse the impact in detail). Link (tie back to overall argument/question).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="170" y="24" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">PEEL PARAGRAPH TOWER</text>
            <text x="30" y="48" font-size="11" font-weight="800" fill="#0f172a">P - Point: State your main argument</text>
            <text x="30" y="70" font-size="11" font-weight="700" fill="#2563eb">E - Evidence: Support with data or examples</text>
            <text x="30" y="92" font-size="11" font-weight="700" fill="#059669">E - Explain: Deeply analyse the significance</text>
            <text x="30" y="114" font-size="11" font-weight="800" fill="#d97706">L - Link: Connect directly back to the thesis</text>
          </g>"""),
        "golden_rule": "The 'Explain' step is where the highest marks are earned — explain the 'why' and 'how'!",
        "watch_out": "Don't jump straight from point to point without providing evidence and explanation.",
        "challenge_prompt": "What does each letter in the PEEL acronym represent?",
        "answer_text": "P = Point, E = Evidence, E = Explanation, L = Link."
    },

    # 28. Introduction Techniques
    {
        "id": "e-l2-28",
        "number": 28,
        "title": "Introduction: The 3-Sentence Hook",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W28",
        "rule_heading": "Hook • Context • Thesis Statement",
        "rule_body": "Craft a powerful opening in 3 sentences: 1. The Hook (surprising fact, rhetorical question, or provocative statement). 2. The Context (why this issue matters today). 3. The Thesis (your definitive stance/roadmap).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">THE 3-SENTENCE INTRODUCTION</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#0f172a">1. Hook: "Did you know that 8 million tonnes..."</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#475569">2. Context: "Plastic pollution is now choking our oceans..."</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#2563eb">3. Thesis: "This article will demonstrate why a ban is vital."</text>
          </g>"""),
        "golden_rule": "Avoid starting with 'In this essay I will write about...' — grab attention immediately!",
        "watch_out": "Don't write a two-page introduction — keep it under 60 words so you have time for body paragraphs.",
        "challenge_prompt": "What is the role of a thesis statement in an introduction?",
        "answer_text": "A thesis statement clearly declares the writer's central argument or stance on the topic."
    },

    # 29. Conclusion Techniques
    {
        "id": "e-l2-29",
        "number": 29,
        "title": "Conclusion: Memorable Endings",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W29",
        "rule_heading": "Re-state • Synthesise • Final Call",
        "rule_body": "Never introduce brand new arguments in a conclusion! 1. Restate your main stance in fresh words. 2. Synthesise your strongest arguments. 3. End with a memorable final call to action or warning.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">EFFECTIVE CONCLUSION BLUEPRINT</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#475569">1. Re-affirm stance with authority</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#475569">2. Summarise top two compelling reasons</text>
            <rect x="25" y="92" width="290" height="26" rx="4" fill="#059669"/>
            <text x="170" y="110" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">3. Lasting final thought or call to action</text>
          </g>"""),
        "golden_rule": "Leave the examiner with a punchy, lingering final sentence!",
        "watch_out": "Never bring up brand-new evidence in the conclusion — it looks unplanned.",
        "challenge_prompt": "What is the primary mistake students make when writing conclusions?",
        "answer_text": "Introducing new arguments or points that were never mentioned or explained in the main body."
    },

    # 30. Cohesive Devices & Transition Words
    {
        "id": "e-l2-30",
        "number": 30,
        "title": "Cohesive Devices &amp; Connectives",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W30",
        "rule_heading": "Linking Ideas Across Paragraphs",
        "rule_body": "Use mature connective discourse markers to guide the reader: Adding (Furthermore, In addition). Contrasting (Conversely, Nevertheless, On the contrary). Cause/Result (Consequently, Therefore).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#5b21b6" text-anchor="middle">TRANSITION WORD BANK</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#2563eb">Addition: Furthermore, Moreover, Additionally</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#dc2626">Contrast: Conversely, However, Nevertheless</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#059669">Result: Consequently, Therefore, As a result</text>
          </g>"""),
        "golden_rule": "Put a comma immediately after fronted connective words (e.g. 'Furthermore, ...')!",
        "watch_out": "Don't overuse 'Also', 'And', or 'But' to start every sentence.",
        "challenge_prompt": "Replace 'also' with a higher-level transition word in: 'Also, local businesses will benefit.'",
        "answer_text": "'Furthermore, local businesses will benefit' (or 'Moreover' / 'In addition')."
    },

    # 31. Varying Sentence Openers
    {
        "id": "e-l2-31",
        "number": 31,
        "title": "Varying Sentence Openers",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W31",
        "rule_heading": "ISPACED Opener Variety",
        "rule_body": "Avoid repeatedly starting sentences with 'The' or 'I': I - -Ing verb (Rushing to the ward...). S - Simile. P - Preposition (Under the table...). A - Adverb (Frantically,...). C - Conjunction (Although...). ED - Past participle (Exhausted,...).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">VARY YOUR OPENERS (ISPACED)</text>
            <text x="25" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Adverb: 'Alarmingly, the waiting times doubled.'</text>
            <text x="25" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• -Ing Word: 'Facing budget cuts, the clinic closed.'</text>
            <text x="25" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• Conjunction: 'Although funding increased, staff left.'</text>
          </g>"""),
        "golden_rule": "Follow fronted openers with a comma to separate the clause!",
        "watch_out": "A piece where every sentence begins with 'The' or 'We' feels monotonous and loses grammar marks.",
        "challenge_prompt": "Rewrite this sentence starting with an -ed participle: 'The nurses were exhausted by the night shift and took a break.'",
        "answer_text": "'Exhausted by the night shift, the nurses took a break.'"
    },

    # 32. Vocabulary Enhancement (Up-levelling)
    {
        "id": "e-l2-32",
        "number": 32,
        "title": "Up-Levelling Vocabulary",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W32",
        "rule_heading": "Swap Weak Words for Sophisticated Diction",
        "rule_body": "Replace overused, simple words with mature academic language: 'Bad' → Detrimental / Inadequate. 'Good' → Beneficial / Exemplary. 'A lot of' → Substantial / Numerous. 'Think' → Contend / Assert.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">UP-LEVELLING DICTION</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#dc2626">Simple: "This is a very bad idea that will cause big problems."</text>
            <line x1="25" y1="68" x2="355" y2="68" stroke="#cbd5e1"/>
            <text x="25" y="90" font-size="11" font-weight="800" fill="#059669">Level 2: "This proposal is highly detrimental and will</text>
            <text x="25" y="110" font-size="11" font-weight="800" fill="#059669">precipitate substantial operational challenges."</text>
          </g>"""),
        "golden_rule": "Use sophisticated words accurately; don't force complex words if unsure of meaning!",
        "watch_out": "Avoid colloquial slang: 'stuff', 'kids', 'gonna', 'loads of'.",
        "challenge_prompt": "Up-level the word 'show' in: 'The figures show that attendance dropped.'",
        "answer_text": "'The figures demonstrate / illustrate / indicate that attendance dropped.'"
    },

    # 33. Planning & Proofreading Workflow
    {
        "id": "e-l2-33",
        "number": 33,
        "title": "Planning &amp; Proofreading Strategy",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Writing & Formats",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W33",
        "rule_heading": "5-Minute Plan • Write • 5-Minute Sweep",
        "rule_body": "Time allocation strategy: 5 mins: Spidergram plan (format, 4 key points, PAF). 35 mins: Sustained writing following PEEL. 5 mins: Proofreading sweep for capital letters, sentence boundaries, and homophones.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">EXAM WRITING WORKFLOW (45 MINS)</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">1. Plan (5 mins): Check PAF, jot 4 paragraph bullets</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#2563eb">2. Write (35 mins): Keep focus on paragraphing &amp; tone</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#dc2626">3. Check (5 mins): Sweep for capitals, full stops &amp; commas</text>
          </g>"""),
        "golden_rule": "A 5-minute proofread regularly saves 3 to 5 SPaG marks that would otherwise be lost!",
        "watch_out": "Never write without planning — unplanned essays wander off-topic and repeat points.",
        "challenge_prompt": "What three things should you check for during your final 5-minute proofreading sweep?",
        "answer_text": "1. Capital letters (names, 'I', start of sentences). 2. Sentence boundary punctuation (avoiding comma splices). 3. Common homophones (there/their/they're)."
    }
]

CARDS_C = [
    # 34. Sentence Boundaries & Comma Splices
    {
        "id": "e-l2-34",
        "number": 34,
        "title": "Sentence Boundaries &amp; Splices",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W34",
        "rule_heading": "Never Join Sentences with a Comma Alone",
        "rule_body": "A comma splice occurs when two independent sentences are joined with only a comma. Fix it with: 1. A full stop. 2. A semicolon (;). 3. A coordinating conjunction (FANBOYS: for, and, nor, but, or, yet, so).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">COMMA SPLICE ERROR</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#dc2626">WRONG: "The weather was awful, we stayed indoors."</text>
            <line x1="25" y1="68" x2="355" y2="68" stroke="#cbd5e1"/>
            <text x="25" y="90" font-size="11" font-weight="800" fill="#15803d">FIX 1: "The weather was awful. We stayed indoors."</text>
            <text x="25" y="110" font-size="11" font-weight="800" fill="#15803d">FIX 2: "The weather was awful; we stayed indoors."</text>
          </g>"""),
        "golden_rule": "A comma is a brief pause, NEVER a full stop!",
        "watch_out": "Comma splices are the #1 penalized grammar error at Level 2.",
        "challenge_prompt": "Correct the comma splice: 'The report is complete, it will be emailed tomorrow.'",
        "answer_text": "'The report is complete; it will be emailed tomorrow.' (or with a full stop: 'The report is complete. It will be emailed tomorrow.')"
    },

    # 35. The Comma Rulebook
    {
        "id": "e-l2-35",
        "number": 35,
        "title": "The Comma Rulebook",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W35",
        "rule_heading": "Lists • Adverbials • Parenthetical Clauses",
        "rule_body": "Use commas for: 1. Separating items in a list. 2. After introductory adverbials ('Suddenly, ...'). 3. Around non-essential parenthetical information ('Dr Smith, who retired last year, attended').",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">3 ESSENTIAL COMMA RULES</text>
            <text x="25" y="55" font-size="10.5" font-weight="700" fill="#2563eb">1. List: 'Apples, oranges, and pears.'</text>
            <text x="25" y="78" font-size="10.5" font-weight="700" fill="#059669">2. Opener: 'Despite the delay, the flight landed safely.'</text>
            <text x="25" y="101" font-size="10.5" font-weight="700" fill="#7c3aed">3. Parenthesis: 'Mr Patel, our head of finance, approved it.'</text>
          </g>"""),
        "golden_rule": "If you can remove the bracketed information between the commas and the sentence still makes sense, the commas are correct!",
        "watch_out": "Don't place a comma between a subject and its verb (e.g. 'The tall man in the coat, walked away' is INCORRECT).",
        "challenge_prompt": "Add commas to this sentence: 'Although it rained heavily the marathon runners who had trained for months completed the course.'",
        "answer_text": "'Although it rained heavily, the marathon runners, who had trained for months, completed the course.'"
    },

    # 36. Apostrophes: Omission vs Possession
    {
        "id": "e-l2-36",
        "number": 36,
        "title": "Apostrophes: Omission vs Possession",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W36",
        "rule_heading": "Missing Letters vs Ownership",
        "rule_body": "Omission: Replaces missing letters in contractions (don't = do not, it's = it is). Singular possession: 's (the nurse's badge). Plural ending in s: s' (the nurses' station). Irregular plural: 's (children's ward).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">IT'S vs ITS</text>
            <text x="15" y="55" font-size="11" font-weight="800" fill="#0f172a">It's = It is (Contraction)</text>
            <text x="15" y="75" font-size="10.5" font-weight="700" fill="#475569">"It's raining outside."</text>
            <text x="15" y="98" font-size="11" font-weight="800" fill="#059669">Its = Possessive pronoun</text>
            <text x="15" y="115" font-size="10.5" font-weight="700" fill="#475569">"The cat licked its paws."</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">PLURAL POSSESSION</text>
            <text x="15" y="55" font-size="11" font-weight="800" fill="#0f172a">One doctor: doctor's</text>
            <text x="15" y="75" font-size="10.5" font-weight="700" fill="#475569">"The doctor's car"</text>
            <text x="15" y="98" font-size="11" font-weight="800" fill="#15803d">Many doctors: doctors'</text>
            <text x="15" y="115" font-size="10.5" font-weight="700" fill="#475569">"The doctors' room"</text>
          </g>"""),
        "golden_rule": "'Its' for possession NEVER has an apostrophe (like hers, his, ours)!",
        "watch_out": "Never use an apostrophe to make a word plural! (e.g. 'Apple's for sale' is WRONG).",
        "challenge_prompt": "Choose the correct word: 'The company reviewed (it's / its) annual policy.'",
        "answer_text": "'its' (possessive pronoun showing ownership; 'it is annual policy' makes no sense)."
    },

    # 37. Colons & Semicolons
    {
        "id": "e-l2-37",
        "number": 37,
        "title": "Colons &amp; Semicolons",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W37",
        "rule_heading": "Colon (Introduces) • Semicolon (Bridges)",
        "rule_body": "Colon (:): Introduces a list, explanation, or direct quotation following a full independent clause. Semicolon (;): Connects two closely linked independent sentences without a conjunction.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">COLON (:)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Introduces a list or conclusion</text>
            <text x="15" y="80" font-size="10" font-weight="700" fill="#475569">"Please bring three items: a pen, a ruler, and paper."</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#5b21b6" text-anchor="middle">SEMICOLON (;)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Links two complete sentences</text>
            <text x="15" y="80" font-size="10" font-weight="700" fill="#475569">"She loves surgery; he prefers general practice."</text>
          </g>"""),
        "golden_rule": "The clause before a colon MUST be a complete standalone sentence!",
        "watch_out": "Don't put a colon after a verb like 'including' or 'are' (e.g. 'Items are: pen...' is INCORRECT).",
        "challenge_prompt": "Insert a semicolon into this sentence: 'Call me tomorrow I will give you my final decision then.'",
        "answer_text": "'Call me tomorrow; I will give you my final decision then.'"
    },

    # 38. Speech Marks & Dialogue Punctuation
    {
        "id": "e-l2-38",
        "number": 38,
        "title": "Speech Marks &amp; Quotations",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W38",
        "rule_heading": "Punctuation Inside the Quotes",
        "rule_body": "1. Put quotation marks around the spoken words only. 2. Punctuation (comma, full stop, exclamation mark) goes INSIDE the speech marks. 3. New speaker = start a new paragraph line.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">DIRECT SPEECH PUNCTUATION</text>
          <g transform="translate(50, 60)">
            <text x="0" y="20" font-size="12" font-weight="800" fill="#2563eb">"We must act immediately," warned the director.</text>
            <text x="0" y="45" font-size="12" font-weight="800" fill="#059669">The nurse replied, "The ward is fully prepared."</text>
            <text x="0" y="68" font-size="11" font-weight="700" fill="#dc2626">⚠️ Comma goes BEFORE the closing quote mark!</text>
          </g>"""),
        "golden_rule": "Punctuation belongs INSIDE the speech marks!",
        "watch_out": "Capitalise the first word inside the opening speech mark when starting dialogue.",
        "challenge_prompt": "Correct the punctuation: The manager said 'we will achieve our targets.'",
        "answer_text": "The manager said, \"We will achieve our targets.\""
    },

    # 39. Hyphens & Dashes
    {
        "id": "e-l2-39",
        "number": 39,
        "title": "Hyphens &amp; Parenthetical Dashes",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W39",
        "rule_heading": "Hyphen (Joins) vs Dash (Separates)",
        "rule_body": "Hyphen (-): Short line joining words to form compound adjectives before nouns (well-known actor, part-time job). Dash (—): Longer pause used in pairs for dramatic emphasis or parenthetical side-thoughts.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">HYPHEN (-)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Joins compound words:</text>
            <text x="15" y="78" font-size="11" font-weight="800" fill="#2563eb">• state-of-the-art facility</text>
            <text x="15" y="101" font-size="11" font-weight="800" fill="#2563eb">• thirty-five patients</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">DASH (—)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Dramatic pause/aside:</text>
            <text x="15" y="80" font-size="10.5" font-weight="700" fill="#be185d">"The outcome — though unexpected — was positive."</text>
          </g>"""),
        "golden_rule": "Hyphens glue words together; dashes push thoughts apart!",
        "watch_out": "Notice the difference: 'twenty five-pound notes' (20 notes) vs 'twenty-five pound notes' (£25 notes).",
        "challenge_prompt": "Insert a hyphen where required: 'He submitted a well written application.'",
        "answer_text": "'He submitted a well-written application.' ('well-written' is a compound adjective preceding 'application')."
    },

    # 40. Subject-Verb Agreement
    {
        "id": "e-l2-40",
        "number": 40,
        "title": "Subject-Verb Agreement",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W40",
        "rule_heading": "Singular Subjects take Singular Verbs",
        "rule_body": "Singular subject = singular verb (The student IS writing). Plural subject = plural verb (The students ARE writing). Trap: Ignore prepositional phrases (e.g. 'The box of chocolates IS on the desk').",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">PREPOSITIONAL PHRASE TRAP</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#dc2626">TRAP: "The list of employees (is / are) on the desk."</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#475569">The subject is 'The list' (singular), NOT 'employees'.</text>
            <rect x="25" y="92" width="330" height="26" rx="4" fill="#16a34a"/>
            <text x="190" y="110" font-size="11.5" font-weight="800" fill="#ffffff" text-anchor="middle">CORRECT: "The list of employees IS on the desk."</text>
          </g>"""),
        "golden_rule": "Find the true core subject by crossing out phrases starting with 'of', 'in', or 'with'!",
        "watch_out": "Words like 'everyone', 'each', and 'someone' are grammatically SINGULAR ('Everyone is ready').",
        "challenge_prompt": "Choose the correct verb: 'Neither of the applicants (was / were) shortlisted.'",
        "answer_text": "'was' ('Neither' is a singular indefinite pronoun taking a singular verb)."
    },

    # 41. Consistent Verb Tenses
    {
        "id": "e-l2-41",
        "number": 41,
        "title": "Consistent Verb Tenses",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W41",
        "rule_heading": "Maintain Tense Throughout",
        "rule_body": "Do not drift accidentally between past and present tense within the same sentence or paragraph: Reports and recount narratives must stay strictly in the past tense.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">TENSE DRIFT ERROR</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#dc2626">WRONG: "She walked into the room and picks up the file."</text>
            <line x1="25" y1="68" x2="355" y2="68" stroke="#cbd5e1"/>
            <text x="25" y="90" font-size="11" font-weight="800" fill="#15803d">CORRECT: "She walked into the room and picked up the file."</text>
            <text x="25" y="110" font-size="10.5" font-weight="700" fill="#475569">Keep both verbs in the simple past tense.</text>
          </g>"""),
        "golden_rule": "Check all your verbs during proofreading to ensure they match in tense!",
        "watch_out": "Accidental tense drift into present tense is common when writing recount stories.",
        "challenge_prompt": "Correct the tense in: 'The customer complained loudly and leaves the store.'",
        "answer_text": "'The customer complained loudly and left the store.' (keeping both verbs in past tense)."
    },

    # 42. Active vs Passive Voice
    {
        "id": "e-l2-42",
        "number": 42,
        "title": "Active vs Passive Voice",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W42",
        "rule_heading": "Active (Direct) vs Passive (Formal &amp; Objective)",
        "rule_body": "Active: Subject performs action ('The doctor administered the vaccine'). Direct and energetic. Passive: Action happens to subject ('The vaccine was administered'). Formal, impersonal, ideal for reports.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">ACTIVE VOICE</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"The committee approved the budget."</text>
            <text x="15" y="95" font-size="10" font-weight="800" fill="#2563eb">Subject does action</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">PASSIVE VOICE</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"The budget was approved by the committee."</text>
            <text x="15" y="95" font-size="10" font-weight="800" fill="#059669">Formal &amp; Objective</text>
          </g>"""),
        "golden_rule": "Use passive voice in incident reports and scientific write-ups to sound impartial!",
        "watch_out": "Overusing passive voice in persuasive letters can sound lifeless and bureaucratic.",
        "challenge_prompt": "Convert to passive voice: 'The inspector reviewed the fire doors.'",
        "answer_text": "'The fire doors were reviewed by the inspector.'"
    },

    # 43. Complex & Compound Sentences
    {
        "id": "e-l2-43",
        "number": 43,
        "title": "Complex &amp; Compound Sentences",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W43",
        "rule_heading": "Main Clauses &amp; Subordinate Clauses",
        "rule_body": "Compound: Joins two independent clauses with FANBOYS conjunction (and, but, so). Complex: Contains a main clause + subordinate clause joined with subordinating conjunction (although, because, while, since).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">COMPLEX SENTENCE STRUCTURE</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#2563eb">Subordinate Clause: 'Although funding was cut,' (cannot stand alone)</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#059669">+ Main Clause: 'the project finished on time.' (stands alone)</text>
            <rect x="25" y="92" width="330" height="26" rx="4" fill="#3b82f6"/>
            <text x="190" y="110" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Examiners look for a variety of simple, compound &amp; complex!</text>
          </g>"""),
        "golden_rule": "When a subordinate clause comes first, always put a comma after it!",
        "watch_out": "A subordinate clause alone is a fragment, NOT a complete sentence.",
        "challenge_prompt": "Identify the subordinate clause in: 'Because traffic was congested, we arrived twenty minutes late.'",
        "answer_text": "'Because traffic was congested' (it depends on the main clause to make sense)."
    },

    # 44. Common Confusables (Part 1)
    {
        "id": "e-l2-44",
        "number": 44,
        "title": "Homophones: There / Their / They're",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W44",
        "rule_heading": "Location • Ownership • Contraction",
        "rule_body": "THERE: Place or fact ('Put it over there', 'There is a problem'). THEIR: Ownership / belonging ('Their coats'). THEY'RE: Short for 'they are' ('They're leaving now').",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">THERE</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Place (contains 'here')</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#475569">"Over there"</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f0fdf4" stroke="#16a34a"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">THEIR</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#0f172a">Possession (their car)</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#475569">"Their home"</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">THEY'RE</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#0f172a">They are (has apostrophe)</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#475569">"They're late"</text>
          </g>"""),
        "golden_rule": "If you can replace it with 'they are', use 'they're'!",
        "watch_out": "Affect vs Effect: Affect is a Verb (Action), Effect is a Noun (End result).",
        "challenge_prompt": "Fill the blanks: '(They're / Their) coats are hanging over (there / their).'",
        "answer_text": "'Their coats are hanging over there.'"
    },

    # 45. Tricky Pairs: Practice vs Practise
    {
        "id": "e-l2-45",
        "number": 45,
        "title": "Confusable Pairs: Practice vs Practise",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W45",
        "rule_heading": "Noun (C) vs Verb (S)",
        "rule_body": "In British English: Nouns end in 'ce' (Practice, Advice, Device, Licence). Verbs end in 'se' (Practise, Advise, Devise, License). Tip: Think of 'Ice is a noun' (-ice = noun).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">NOUN (-CE)</text>
            <text x="15" y="55" font-size="11" font-weight="800" fill="#0f172a">• Practice (a doctor's surgery)</text>
            <text x="15" y="80" font-size="11" font-weight="800" fill="#0f172a">• Advice (useful advice)</text>
            <text x="15" y="105" font-size="11" font-weight="800" fill="#0f172a">• Licence (driving licence)</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">VERB (-SE)</text>
            <text x="15" y="55" font-size="11" font-weight="800" fill="#15803d">• Practise (to practise guitar)</text>
            <text x="15" y="80" font-size="11" font-weight="800" fill="#15803d">• Advise (I advise you...)</text>
            <text x="15" y="105" font-size="11" font-weight="800" fill="#15803d">• License (licensed to sell)</text>
          </g>"""),
        "golden_rule": "Test with 'Advice/Advise': You give advice (noun), you advise someone (verb)!",
        "watch_out": "Loose vs Lose: 'Loose' rhymes with goose (untied shoelace). 'Lose' has one 'o' (to misplace something).",
        "challenge_prompt": "Choose the correct spelling: 'Doctors must (practice / practise) medicine ethically.'",
        "answer_text": "'practise' (it is the doing verb)."
    },

    # 46. Suffix Rules (-ible vs -able)
    {
        "id": "e-l2-46",
        "number": 46,
        "title": "Suffix Rules (-able vs -ible)",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W46",
        "rule_heading": "Root Word Test",
        "rule_body": "-able: Used when the base word is a complete standalone word (depend → dependable, enjoy → enjoyable). -ible: Used when the base word is not a complete English word (horr → horrible, vis → visible).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">-ABLE (Whole Word)</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">comfort + able = comfortable</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">rely + able = reliable</text>
            <text x="15" y="105" font-size="11" font-weight="700" fill="#0f172a">accept + able = acceptable</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#a16207" text-anchor="middle">-IBLE (Incomplete Root)</text>
            <text x="15" y="55" font-size="11" font-weight="700" fill="#0f172a">poss + ible = possible</text>
            <text x="15" y="80" font-size="11" font-weight="700" fill="#0f172a">elig + ible = eligible</text>
            <text x="15" y="105" font-size="11" font-weight="700" fill="#0f172a">respons + ible = responsible</text>
          </g>"""),
        "golden_rule": "If you take away the suffix and have a complete word left, use -able!",
        "watch_out": "-tion vs -sion: Use -sion when base word ends in d/s (extend → extension; divide → division).",
        "challenge_prompt": "Add the correct suffix to form the adjective: 'aud___' (able to be heard).",
        "answer_text": "'audible' ('aud' is not a standalone English word, so it takes -ible)."
    },

    # 47. Silent Letters & Tricky Exam Spellings
    {
        "id": "e-l2-47",
        "number": 47,
        "title": "High-Frequency Exam Spellings",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W47",
        "rule_heading": "The 10 Most Common Exam Misspellings",
        "rule_body": "1. Accommodate (2 c's, 2 m's). 2. Definitely (de-finite-ly, NO 'a'). 3. Necessary (1 collar, 2 socks: 1 c, 2 s's). 4. Government (has 'n'). 5. Environment (has 'n'). 6. Colleague. 7. Separate.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">SPELLING MNEMONICS</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#2563eb">• Necessary: 1 Coffee (c) and 2 Sugars (ss)</text>
            <text x="25" y="78" font-size="11" font-weight="800" fill="#059669">• Definitely: Has the word 'FINITE' inside it (NO 'a')</text>
            <text x="25" y="101" font-size="11" font-weight="800" fill="#d97706">• Separate: There is 'A RAT' in separate</text>
          </g>"""),
        "golden_rule": "Break tricky words into syllables or mnemonics!",
        "watch_out": "'Definately' is always marked wrong — remember 'definitely'.",
        "challenge_prompt": "Spell the word that means two people working together that begins with 'coll...'",
        "answer_text": "'colleague'."
    },

    # 48. Prefix Rules & Negative Antonyms
    {
        "id": "e-l2-48",
        "number": 48,
        "title": "Prefixes &amp; Negative Antonyms",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "SPaG & Grammar",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.W48",
        "rule_heading": "Un-, In-, Im-, Dis-, Mis-, Ir-",
        "rule_body": "Prefixes change word meaning without altering base word spelling: 'im-' before 'p/m' (patient → impatient). 'ir-' before 'r' (responsible → irresponsible). 'il-' before 'l' (legal → illegal). Root spelling is PRESERVED.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">PREFIX PATTERNS</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#0f172a">• Words starting with P take IM-: im + perfect = imperfect</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#0f172a">• Words starting with R take IR-: ir + regular = irregular</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#0f172a">• Words starting with L take IL-: il + legible = illegible</text>
          </g>"""),
        "golden_rule": "Don't drop letters when adding prefixes: un + necessary = unnecessary (keep both n's)!",
        "watch_out": "'Disappointed' has ONE 's' and TWO 'p's (dis + appoint + ed).",
        "challenge_prompt": "Add the negative prefix to the word 'rational'.",
        "answer_text": "'irrational' (prefix 'ir-' before 'r')."
    }
]

def main():
    base_dir = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/decks/english_l2"
    os.makedirs(base_dir, exist_ok=True)

    with open(os.path.join(base_dir, "strand_a.py"), "w") as f:
        f.write('\"\"\"English L2 Strand A: Reading Comprehension & Text Analysis (Cards 1-18)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_A, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_b.py"), "w") as f:
        f.write('\"\"\"English L2 Strand B: Writing Formats, Structure & Composition (Cards 19-33)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_B, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_c.py"), "w") as f:
        f.write('\"\"\"English L2 Strand C: Spelling, Punctuation and Grammar (Cards 34-48)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_C, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "__init__.py"), "w") as f:
        f.write('from .strand_a import CARDS as STRAND_A\n')
        f.write('from .strand_b import CARDS as STRAND_B\n')
        f.write('from .strand_c import CARDS as STRAND_C\n\n')
        f.write('CARDS = STRAND_A + STRAND_B + STRAND_C\n')

    print(f"✓ English Level 2 Complete: {len(CARDS_A) + len(CARDS_B) + len(CARDS_C)} cards generated!")

if __name__ == "__main__":
    main()
