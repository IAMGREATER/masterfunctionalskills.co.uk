#!/usr/bin/env python3
"""
Builder for Deck 3: Functional Skills English - Level 2 (48 Cards)
Full curriculum alignment with UK DfE and Pearson Edexcel / City & Guilds standards.
"""
import os
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS_A = [
    # 1. Text Purpose
    {
        "id": "e-l2-01",
        "number": 1,
        "title": "Identifying Text Purpose",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R1",
        "rule_heading": "P.A.F: Purpose • Audience • Form",
        "rule_body": "Every text has a primary purpose: Persuade (sway opinions), Inform (factual details), Instruct (step-by-step directions), Explain (how/why something works), Advise (recommendations), or Entertain.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="900" fill="#5b21b6" text-anchor="middle">PRIMARY PURPOSE OF TEXT</text>
            <g transform="translate(15, 45)">
              <rect x="0" y="0" width="115" height="30" rx="4" fill="#ddd6fe"/><text x="57" y="20" font-size="11" font-weight="800" fill="#5b21b6" text-anchor="middle">PERSUADE</text>
              <rect x="125" y="0" width="115" height="30" rx="4" fill="#ddd6fe"/><text x="182" y="20" font-size="11" font-weight="800" fill="#5b21b6" text-anchor="middle">INFORM</text>
              <rect x="250" y="0" width="115" height="30" rx="4" fill="#ddd6fe"/><text x="307" y="20" font-size="11" font-weight="800" fill="#5b21b6" text-anchor="middle">INSTRUCT</text>
            </g>
            <text x="200" y="105" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Look at verbs, modal words, rhetorical questions &amp; imperatives</text>
          </g>"""),
        "golden_rule": "Always pair purpose with language evidence: 'The text aims to persuade by using emotive words like...'",
        "watch_out": "A text can have secondary purposes, but exams always ask for the MAIN/PRIMARY intention.",
        "challenge_prompt": "An article uses phrases like 'You must act now before it is too late' and 'Statistics prove our service is superior'. What is its main purpose?",
        "answer_text": "The main purpose is to PERSUADE the reader to take urgent action using emotive language and direct address."
    },

    # 2. Audience & Context
    {
        "id": "e-l2-02",
        "number": 2,
        "title": "Audience &amp; Tone Adaptation",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R2",
        "rule_heading": "Who is the Reader?",
        "rule_body": "Authors adapt their language, register, and layout for specific demographics: Professionals (formal jargon), Teenagers (casual, modern idioms), Parents, Patients, Customers.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">FORMAL / PROFESSIONAL</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Passive voice</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• Complex vocabulary</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• No slang or contractions</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="90" y="24" font-size="11" font-weight="800" fill="#9d174d" text-anchor="middle">INFORMAL / CASUAL</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Contractions (don't, it's)</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• Direct address ('you')</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• Conversational phrases</text>
          </g>"""),
        "golden_rule": "Identify the target audience by examining vocabulary level and formatting cues!",
        "watch_out": "Don't just say 'the general public' if the text specifically addresses car owners, NHS staff, or homeowners.",
        "challenge_prompt": "A leaflet contains the sentence: 'All clinical practitioners must submit quarterly appraisal forms via the intranet.' Who is the intended audience?",
        "answer_text": "The intended audience is clinical medical staff / healthcare employees."
    },

    # 3. Explicit vs Implicit Meaning (Inference)
    {
        "id": "e-l2-03",
        "number": 3,
        "title": "Explicit vs Implicit (Inference)",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R3",
        "rule_heading": "Fact Stated vs Reading Between Lines",
        "rule_body": "Explicit = Directly and openly stated in the text word-for-word. Implicit = Hinted or suggested through clues, tone, and connotations without being said outright.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">EXPLICIT (Stated)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"The door was locked with three heavy bolts."</text>
            <rect x="15" y="90" width="150" height="24" rx="4" fill="#3b82f6"/>
            <text x="90" y="106" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Clear literal fact</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">IMPLICIT (Inferred)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"She checked over her shoulder before knocking."</text>
            <rect x="15" y="90" width="150" height="24" rx="4" fill="#d97706"/>
            <text x="90" y="106" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Infers fear or secrecy</text>
          </g>"""),
        "golden_rule": "Inference = Clues from text + Reader's logical deductions!",
        "watch_out": "Don't guess wild theories — every inference MUST be grounded in textual clues.",
        "challenge_prompt": "Text: 'David stared at the empty petrol gauge and sighed heavily into the steering wheel on the quiet country lane.' What can you infer?",
        "answer_text": "We can infer that David has run out of petrol and is stranded/frustrated in a remote area."
    },

    # 4. Fact vs Opinion vs Bias
    {
        "id": "e-l2-04",
        "number": 4,
        "title": "Fact vs Opinion vs Bias",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R4",
        "rule_heading": "Verifiable Truth vs Subjective Belief",
        "rule_body": "Fact: Can be proven true or false with objective evidence or data. Opinion: A personal view, feeling, or judgment. Bias: A one-sided presentation favouring one perspective.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="60" y="26" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">FACT</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Can be checked and verified with data</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="60" y="26" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">OPINION</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Belief or value (best, worst, beautiful)</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fffbeb" stroke="#f59e0b"/>
            <text x="60" y="26" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">BIAS</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Unbalanced, one-sided view with commercial interest</text>
          </g>"""),
        "golden_rule": "If it contains adjectives like 'finest', 'dreadful', or 'unacceptable', it is an OPINION!",
        "watch_out": "Watch out for opinions disguised as facts: 'Everyone knows London is the best city' is STILL an opinion.",
        "challenge_prompt": "Identify whether this statement is fact or opinion: 'Over 65% of UK households own a pet, which proves pets are the greatest addition to family life.'",
        "answer_text": "'Over 65% own a pet' is a FACT; 'proves pets are the greatest addition' is an OPINION."
    },

    # 5. Organisational Features
    {
        "id": "e-l2-05",
        "number": 5,
        "title": "Organisational Features &amp; Effects",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R5",
        "rule_heading": "Subheadings, Sidebars &amp; Bullet Points",
        "rule_body": "Always explain WHY an organisational feature is used: Subheadings (break text into chunks), Bullet points (isolate key items), Bold text (draws eye to essential warnings), Tables (organise data).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">ORGANISATIONAL FEATURES &amp; EFFECT</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#2563eb">• Subheadings: Help reader navigate and find information quickly</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#059669">• Bullet Points: Break complex steps into digestible chunks</text>
            <text x="25" y="105" font-size="11" font-weight="700" fill="#d97706">• Pull-quotes / Sidebars: Emphasise critical statistics or takeaways</text>
          </g>"""),
        "golden_rule": "Never just name the feature — you MUST explain its visual effect on the reader!",
        "watch_out": "Don't just say 'it looks nice' — say 'it enhances readability and directs the reader's eye.'",
        "challenge_prompt": "Explain how the use of bullet points helps the reader in a workplace safety notice.",
        "answer_text": "Bullet points break the safety rules into clear, distinct steps so employees can absorb critical instructions quickly."
    },

    # 6. Structural Analysis & Signposting
    {
        "id": "e-l2-06",
        "number": 6,
        "title": "Structural Signposting",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R6",
        "rule_heading": "Chronological • Cause-Effect • Problem-Solution",
        "rule_body": "Structure is how the writer organizes their points over time: Problem-Solution, Cause-and-Effect, Chronological narrative, or Thematic. Look for discourse markers (Firstly, Conversely, Therefore).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#5b21b6" text-anchor="middle">CORE TEXT STRUCTURES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">1. Problem-Solution (Identifies crisis → gives remedy)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">2. Cause &amp; Effect (Action → consequence)</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#0f172a">3. Comparative (Pros vs cons / Text A vs Text B)</text>
          </g>"""),
        "golden_rule": "Notice shifts in perspective or tone between the beginning, middle, and end!",
        "watch_out": "Structure is NOT spelling or grammar — structure is the overall flow and ordering of paragraphs.",
        "challenge_prompt": "What structural technique is used when an article starts with an alarming story and concludes by offering three practical solutions?",
        "answer_text": "A problem-and-solution structure (hooking with the crisis and resolving with actionable remedies)."
    },

    # 7. Rhetorical Devices (DAFOREST)
    {
        "id": "e-l2-07",
        "number": 7,
        "title": "Persuasive Devices (DAFOREST)",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R7",
        "rule_heading": "The Master Persuasion Toolkit",
        "rule_body": "D - Direct Address ('you'). A - Alliteration. F - Facts. O - Opinions. R - Rhetorical questions. E - Emotive language. S - Statistics (85%). T - Rule of Three (triples).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="900" fill="#9d174d" text-anchor="middle">DAFOREST PERSUASION TOOLKIT</text>
            <text x="40" y="55" font-size="11" font-weight="800" fill="#be185d">D - Direct address ('You')  •  A - Alliteration</text>
            <text x="40" y="80" font-size="11" font-weight="800" fill="#be185d">F - Facts  •  O - Opinions  •  R - Rhetorical Questions</text>
            <text x="40" y="105" font-size="11" font-weight="800" fill="#be185d">E - Emotive words  •  S - Statistics  •  T - Rule of 3</text>
          </g>"""),
        "golden_rule": "Quote the exact phrase, name the DAFOREST device, and explain how it influences the reader!",
        "watch_out": "Don't just write 'it makes you want to read on' — explain that it creates guilt, urgency, or authority.",
        "challenge_prompt": "Identify two DAFOREST devices in: 'Can you really ignore this heartbreaking crisis? Over 80% of families are struggling.'",
        "answer_text": "1. Rhetorical question ('Can you really ignore...?'). 2. Emotive language ('heartbreaking crisis') / Statistic ('Over 80%')."
    },

    # 8. Figurative Language Devices
    {
        "id": "e-l2-08",
        "number": 8,
        "title": "Figurative Language Devices",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R8",
        "rule_heading": "Metaphor • Simile • Hyperbole",
        "rule_body": "Simile: Compares using 'like' or 'as' ('busy as a bee'). Metaphor: States one thing IS another ('the hospital was a warzone'). Hyperbole: Deliberate dramatic exaggeration.",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="200" y="26" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">FIGURATIVE LANGUAGE</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#2563eb">• Simile: "Her smile was as bright as the sun" (uses like/as)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#059669">• Metaphor: "Time is a thief" (direct equivalence)</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#dc2626">• Hyperbole: "I've waited a million years for this bus" (exaggeration)</text>
          </g>"""),
        "golden_rule": "Metaphors create vivid mental images by transferring qualities from one concept to another!",
        "watch_out": "Don't confuse similes and metaphors: similes use 'like' or 'as'; metaphors do not.",
        "challenge_prompt": "What technique is used in: 'The wind screamed through the broken window'?",
        "answer_text": "Personification (giving human actions like 'screamed' to non-human objects like the wind)."
    },

    # 9. Analysing Tone and Register
    {
        "id": "e-l2-09",
        "number": 9,
        "title": "Analysing Tone and Register",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R9",
        "rule_heading": "The Writer's Attitude &amp; Mood",
        "rule_body": "Tone is the emotion or attitude behind the words: Sarcastic, Urgent, Critical, Humorous, Sympathetic, Objective, or Authoritative. Proved by diction (choice of words).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="800" fill="#5b21b6" text-anchor="middle">EXAM TONE VOCABULARY</text>
            <text x="30" y="58" font-size="11" font-weight="700" fill="#0f172a">• Critical / Indignant (Angry, disapproving)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">• Pragmatic / Objective (Neutral, factual, balanced)</text>
            <text x="30" y="102" font-size="11" font-weight="700" fill="#0f172a">• Urgent / Passionate (Call to immediate action)</text>
          </g>"""),
        "golden_rule": "Use precise tone adjectives instead of basic words like 'happy' or 'angry'!",
        "watch_out": "Tone can change within a text — look at the overall prevailing attitude.",
        "challenge_prompt": "Describe the tone of: 'Oh wonderful, another train cancellation. What exceptional service we pay thousands for!'",
        "answer_text": "The tone is sarcastic / ironic (using mock praise like 'wonderful' and 'exceptional' to express bitter dissatisfaction)."
    },

    # 10. Comparing Purpose & Perspective
    {
        "id": "e-l2-10",
        "number": 10,
        "title": "Comparing Purpose &amp; Perspective",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R10",
        "rule_heading": "Pearson Section B Master Technique",
        "rule_body": "To compare two texts for top marks: 1. Identify where both authors agree or share common ground. 2. Contrast how their viewpoints differ. 3. Use comparative connectives ('In contrast', 'Similarly').",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">TEXT A</text>
            <text x="15" y="55" font-size="10" font-weight="700" fill="#0f172a">Optimistic about AI</text>
            <text x="15" y="80" font-size="10" font-weight="700" fill="#475569">Quotes industry gains</text>
            <rect x="15" y="92" width="150" height="22" rx="4" fill="#3b82f6"/>
            <text x="90" y="107" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Supports adoption</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#991b1b" text-anchor="middle">TEXT B</text>
            <text x="15" y="55" font-size="10" font-weight="700" fill="#0f172a">Cautionary / Skeptical</text>
            <text x="15" y="80" font-size="10" font-weight="700" fill="#475569">Warns of job losses</text>
            <rect x="15" y="92" width="150" height="22" rx="4" fill="#ef4444"/>
            <text x="90" y="107" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Urges regulation</text>
          </g>"""),
        "golden_rule": "Always refer to BOTH Text A and Text B in every comparative paragraph!",
        "watch_out": "Writing two separate summaries without comparing them will cost you half the marks.",
        "challenge_prompt": "Compare how Text A and Text B view remote working if Text A highlights productivity while Text B stresses employee loneliness.",
        "answer_text": "While both texts examine remote working, Text A has a positive perspective focusing on output, whereas Text B expresses concern over worker isolation."
    },

    # 11. Comparing Structure & Layout
    {
        "id": "e-l2-11",
        "number": 11,
        "title": "Comparing Layout Features",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R11",
        "rule_heading": "Visual Presentation Differences",
        "rule_body": "Contrast the presentation: Text A may use formal paragraph blocks and footnotes, whereas Text B uses subheadings, bullet points, callout boxes, and bold text.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Comparing Structural Formats</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#2563eb">Text A: Dense, unbroken prose suited for academic reports.</text>
            <text x="0" y="45" font-size="11.5" font-weight="700" fill="#059669">Text B: Modern web layout with subheadings and numbered steps.</text>
          </g>"""),
        "golden_rule": "Link the layout choice to how it helps the intended reader navigate the text!",
        "watch_out": "Don't just mention font colours unless it specifically relates to emphasis or branding.",
        "challenge_prompt": "Why might a public information website use bullet points instead of long continuous paragraphs?",
        "answer_text": "To make key information instantly scannable and easy to follow for busy mobile readers."
    },

    # 12. Comparing Language Techniques
    {
        "id": "e-l2-12",
        "number": 12,
        "title": "Comparing Language Techniques",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R12",
        "rule_heading": "Side-by-Side Technique Comparison",
        "rule_body": "Examine how each author uses language to persuade: Author A relies on hard statistics and authoritative professional quotes. Author B relies on vivid metaphors and emotive storytelling.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="190" y="26" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">COMPARATIVE LANGUAGE DRILL</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#0f172a">• "Both authors use rhetorical questions to engage the reader..."</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#0f172a">• "However, Text A employs objective statistics (92%)..."</text>
            <text x="25" y="105" font-size="11" font-weight="700" fill="#0f172a">• "...whereas Text B relies on emotive language ('disastrous')."</text>
          </g>"""),
        "golden_rule": "Compare language side-by-side using 'similarly' or 'on the other hand'!",
        "watch_out": "Always provide exact quoted evidence from both texts.",
        "challenge_prompt": "Text A says: 'Studies confirm 40% efficiency gains.' Text B says: 'It is a miraculous breath of fresh air.' Compare their language techniques.",
        "answer_text": "Text A uses factual statistical evidence to present an objective argument, whereas Text B uses a poetic metaphor ('breath of fresh air') and hyperbole to create enthusiasm."
    },

    # 13. Evaluating Reliability & Credibility
    {
        "id": "e-l2-13",
        "number": 13,
        "title": "Evaluating Source Credibility",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R13",
        "rule_heading": "Authority • Date • Vested Interest",
        "rule_body": "To evaluate reliability: 1. Author authority (doctor vs blogger). 2. Publication date (is it outdated?). 3. Commercial bias (is the writer selling a product?). 4. Corroboration (can claims be verified?).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">SOURCE CREDIBILITY CHECKLIST</text>
            <text x="40" y="55" font-size="11" font-weight="700" fill="#2563eb">1. Who wrote it? (Expert credentials vs anonymous)</text>
            <text x="40" y="80" font-size="11" font-weight="700" fill="#059669">2. When was it published? (Recent vs obsolete)</text>
            <text x="40" y="105" font-size="11" font-weight="700" fill="#dc2626">3. Vested interest? (Sponsored ad vs independent study)</text>
          </g>"""),
        "golden_rule": "A source with financial gain or personal involvement has a VESTED INTEREST!",
        "watch_out": "Don't assume official-looking blogs are factual — check if there are citations or peer reviews.",
        "challenge_prompt": "Why might a dental review written by the manufacturer of a new whitening toothpaste be considered biased?",
        "answer_text": "The manufacturer has a commercial vested interest in selling the product, making the claims biased rather than independent."
    },

    # 14. Vocabulary in Context (Specialist & Jargon)
    {
        "id": "e-l2-14",
        "number": 14,
        "title": "Specialist Vocabulary &amp; Jargon",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R14",
        "rule_heading": "Deduce Meaning from Context",
        "rule_body": "When encountering unfamiliar technical terms or jargon: 1. Read the surrounding sentences for clues. 2. Break down prefixes and root words. 3. Substitute a synonym to check if it makes sense.",
        "svg_html": wrap_svg("""
          <rect x="40" y="20" width="380" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#1e40af" text-anchor="middle">Decoding Unfamiliar Jargon</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#0f172a">"The patient's condition deteriorated rapidly..."</text>
            <text x="0" y="45" font-size="11.5" font-weight="700" fill="#475569">Clue: 'deteriorated' is paired with emergency actions.</text>
            <text x="0" y="68" font-size="12" font-weight="800" fill="#059669">Meaning: Became worse / declined in health.</text>
          </g>"""),
        "golden_rule": "Read forward two sentences and back two sentences to discover context clues!",
        "watch_out": "Don't skip unfamiliar words — replace them with a simpler synonym in your head.",
        "challenge_prompt": "What does the word 'mitigate' mean in: 'Measures were put in place to mitigate the risks of flooding'?",
        "answer_text": "'Mitigate' means to reduce, lessen, or make less severe."
    },

    # 15. Main Ideas vs Supporting Details
    {
        "id": "e-l2-15",
        "number": 15,
        "title": "Main Ideas vs Supporting Details",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R15",
        "rule_heading": "Core Claim vs Examples",
        "rule_body": "Main Idea: The central argument or topic sentence of a paragraph. Supporting Details: Statistics, quotes, illustrative anecdotes, and examples that prove the main claim.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="45" rx="6" fill="#1e3a8a"/>
            <text x="170" y="28" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">MAIN IDEA (Core Claim)</text>
            <g transform="translate(0, 55)">
              <rect x="0" y="0" width="105" height="55" rx="4" fill="#eff6ff" stroke="#3b82f6"/><text x="52" y="32" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Evidence/Stats</text>
              <rect x="117" y="0" width="105" height="55" rx="4" fill="#eff6ff" stroke="#3b82f6"/><text x="170" y="32" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Expert Quote</text>
              <rect x="235" y="0" width="105" height="55" rx="4" fill="#eff6ff" stroke="#3b82f6"/><text x="287" y="32" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Real Example</text>
            </g>
          </g>"""),
        "golden_rule": "The topic sentence at the start of a paragraph usually states the main idea!",
        "watch_out": "Don't mistake a single supporting case study for the writer's overarching point.",
        "challenge_prompt": "In a paragraph arguing that public transport reduces emissions, an author mentions that electric buses saved 200 tonnes of CO2 in Leeds. Which is the supporting detail?",
        "answer_text": "The 200 tonnes of CO2 saved in Leeds is a supporting detail (evidence) proving the main idea."
    },

    # 16. Summarising from Multiple Paragraphs
    {
        "id": "e-l2-16",
        "number": 16,
        "title": "Summarising Multiple Paragraphs",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R16",
        "rule_heading": "Synthesise in Your Own Words",
        "rule_body": "To summarise: 1. Extract the key takeaways across paragraphs. 2. Condense into concise bullet points or sentences. 3. Paraphrase using YOUR OWN WORDS — never copy chunks verbatim.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
          <text x="230" y="42" font-size="13" font-weight="900" fill="#15803d" text-anchor="middle">SUMMARISING GOLDEN RULES</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="800" fill="#0f172a">✓ Paraphrase in your own vocabulary</text>
            <text x="0" y="42" font-size="11.5" font-weight="800" fill="#0f172a">✓ Condense to essential core facts</text>
            <text x="0" y="65" font-size="11.5" font-weight="800" fill="#dc2626">✗ DO NOT copy word-for-word chunks!</text>
          </g>"""),
        "golden_rule": "Exams penalise mindless copying — rewording proves you understood the text!",
        "watch_out": "Leave out minor descriptive details, anecdotes, and redundant adjectives.",
        "challenge_prompt": "State two requirements of an effective Level 2 summary.",
        "answer_text": "1. It must cover the main points concisely. 2. It must be written in your own words without copying long quotes."
    },

    # 17. Irony, Satire & Understatement
    {
        "id": "e-l2-17",
        "number": 17,
        "title": "Irony, Satire &amp; Sarcasm",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R17",
        "rule_heading": "Saying the Opposite of What is Meant",
        "rule_body": "Verbal Irony: When an author says the opposite of their true meaning for humorous or critical effect. Understatement: Deliberately minimising seriousness ('it's just a scratch' on a wrecked car).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="190" y="28" font-size="13" font-weight="900" fill="#b45309" text-anchor="middle">RECOGNISING VERBAL IRONY</text>
            <text x="25" y="58" font-size="11" font-weight="700" fill="#0f172a">Example: "Standing in the pouring rain with no coat is delightful."</text>
            <text x="25" y="82" font-size="11" font-weight="700" fill="#475569">The literal word is 'delightful', but the true meaning is miserable.</text>
            <rect x="25" y="95" width="330" height="24" rx="4" fill="#f59e0b"/>
            <text x="190" y="111" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Examiners test whether you detect the sarcasm!</text>
          </g>"""),
        "golden_rule": "Check if praise is sincere or sarcastic by looking at the broader context!",
        "watch_out": "Don't take ironic statements literally — that leads to picking the exact opposite answer.",
        "challenge_prompt": "Explain the irony in: 'The fire station burned down while firefighters were attending a fire safety lecture.'",
        "answer_text": "It is situational irony because an institution dedicated to preventing fires was destroyed by one while learning about safety."
    },

    # 18. Pearson Exam Golden Reading Method
    {
        "id": "e-l2-18",
        "number": 18,
        "title": "Golden Reading Method: Q-E-L",
        "subject": "english",
        "level": "l2",
        "subject_label": "English",
        "level_label": "Level 2",
        "strand_name": "Reading & Analysis",
        "strand_theme": "purple",
        "dfe_code": "DfE L2.R18",
        "rule_heading": "Quote • Explain • Link",
        "rule_body": "To score full marks on 3-mark and 4-mark reading questions: 1. QUOTE exact textual phrase in quotation marks. 2. EXPLAIN the underlying meaning in your own words. 3. LINK directly to the author's purpose or question.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="190" y="26" font-size="13" font-weight="900" fill="#15803d" text-anchor="middle">PEARSON 3-STEP FORMULA (Q - E - L)</text>
            <text x="30" y="55" font-size="11.5" font-weight="800" fill="#0f172a">1. QUOTE: "..." (Pick a precise word or short phrase)</text>
            <text x="30" y="80" font-size="11.5" font-weight="800" fill="#0f172a">2. EXPLAIN: Clarify what the quote shows or suggests</text>
            <text x="30" y="105" font-size="11.5" font-weight="800" fill="#0f172a">3. LINK: Connect directly back to the question's focus</text>
          </g>"""),
        "golden_rule": "Keep quotes short (1 to 5 words) — never copy entire three-line sentences!",
        "watch_out": "A quote without explanation earns 0 or 1 mark; you must explain its impact.",
        "challenge_prompt": "What are the three components of the Q-E-L reading response model?",
        "answer_text": "1. Quote (evidence). 2. Explain (analysis in your own words). 3. Link (tying back to the question/purpose)."
    }
]

print(f"Validated English L2 Strand A: {len(CARDS_A)} cards")
