#!/usr/bin/env python3
"""
Complete Builder for Deck 4: Functional Skills English - Level 1 (42 Cards)
Generates strand_a.py, strand_b.py, strand_c.py and __init__.py.
"""
import os
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS_A = [
    # 1. Main Points and Ideas
    {
        "id": "e-l1-01",
        "number": 1,
        "title": "Main Points and Ideas",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R1",
        "rule_heading": "What is the Big Picture?",
        "rule_body": "The main point is the most important message the author wants you to understand. Read the title, opening sentence, and closing sentence to identify the central message.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.8"/>
            <text x="170" y="28" font-size="13" font-weight="900" fill="#115e59" text-anchor="middle">FINDING THE MAIN POINT</text>
            <text x="30" y="58" font-size="11" font-weight="700" fill="#0f172a">1. Headline / Title: Gives the topic</text>
            <text x="30" y="82" font-size="11" font-weight="700" fill="#0f172a">2. First sentence: Introduces the central point</text>
            <text x="30" y="106" font-size="11" font-weight="800" fill="#0d9488">3. Ask yourself: "What is this text really telling me?"</text>
          </g>"""),
        "golden_rule": "The main point is the overarching message, NOT a small illustrative detail!",
        "watch_out": "Don't confuse an example with the main point.",
        "challenge_prompt": "A text lists opening hours, emergency numbers, and ward rules for a hospital. What is the main point of the text?",
        "answer_text": "To inform visitors about essential hospital visiting rules and contact information."
    },

    # 2. Text Types
    {
        "id": "e-l1-02",
        "number": 2,
        "title": "Text Types: Inform, Persuade, Instruct",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R2",
        "rule_heading": "Identify the Goal",
        "rule_body": "Inform: Gives facts and data (news, timetables). Persuade: Wants you to buy or believe something (adverts, flyers). Instruct: Tells you how to do something step-by-step (recipes, user guides).",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">INFORM</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Facts, stats, dates, notices</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#9d174d" text-anchor="middle">PERSUADE</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Adverts, opinions, reviews</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f0fdf4" stroke="#16a34a"/>
            <text x="60" y="24" font-size="11" font-weight="800" fill="#15803d" text-anchor="middle">INSTRUCT</text>
            <text x="10" y="55" font-size="10" font-weight="700" fill="#475569">Numbered steps, bossy verbs</text>
          </g>"""),
        "golden_rule": "Look for imperative verbs (Chop, Turn, Press) = INSTRUCT!",
        "watch_out": "Adverts inform you about prices, but their PRIMARY goal is to PERSUADE you to buy.",
        "challenge_prompt": "What type of text is a user manual for a washing machine?",
        "answer_text": "An instructional text (it gives step-by-step instructions on operating the appliance)."
    },

    # 3. Headings, Subheadings & Titles
    {
        "id": "e-l1-03",
        "number": 3,
        "title": "Headings &amp; Subheadings",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R3",
        "rule_heading": "Signposts for Quick Navigation",
        "rule_body": "Main Heading: Tells you what the whole document is about. Subheadings: Break the text into topics so you can quickly scan and find specific details without reading every single word.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="900" fill="#0f172a" text-anchor="middle">MAIN TITLE: COMMUNITY CENTRE</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0d9488">Subheading 1: Opening Hours</text>
            <text x="30" y="72" font-size="10" font-weight="700" fill="#64748b">Monday to Friday 9am - 8pm</text>
            <text x="30" y="98" font-size="11" font-weight="800" fill="#0d9488">Subheading 2: Room Hire Fees</text>
            <text x="30" y="115" font-size="10" font-weight="700" fill="#64748b">Main Hall: £25 per hour</text>
          </g>"""),
        "golden_rule": "Read the subheadings first to find where your answer is hiding!",
        "watch_out": "Don't read the whole article line-by-line if a subheading tells you exactly where the topic is.",
        "challenge_prompt": "Under which subheading would you look to find out how much a fitness class costs?",
        "answer_text": "Under 'Prices', 'Fees', or 'Cost'."
    },

    # 4. Bullet Points & Numbered Lists
    {
        "id": "e-l1-04",
        "number": 4,
        "title": "Bullet Points &amp; Lists",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R4",
        "rule_heading": "Clear, Distinct Items",
        "rule_body": "Bullet points: Separate key items in a list so they stand out clearly. Numbered lists: Indicate a strict order of steps that must be done in sequence (1st, 2nd, 3rd).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#115e59" text-anchor="middle">BULLETS vs NUMBERING</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">• Bullets: Order does not matter (checklist, packing list)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">1. Numbered: Sequence MATTERS (recipe, safety fire drill)</text>
            <text x="170" y="110" font-size="10.5" font-weight="800" fill="#0d9488" text-anchor="middle">Makes information fast and easy to digest</text>
          </g>"""),
        "golden_rule": "Use numbered lists when steps MUST be followed in exact sequence!",
        "watch_out": "Keep each bullet point short and grammatically consistent.",
        "challenge_prompt": "Why are fire escape procedures presented as numbered lists rather than paragraphs?",
        "answer_text": "To ensure people follow the emergency steps in the correct chronological order without panic."
    },

    # 5. Images, Diagrams & Captions
    {
        "id": "e-l1-05",
        "number": 5,
        "title": "Images, Diagrams &amp; Captions",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R5",
        "rule_heading": "Visual Evidence &amp; Explanations",
        "rule_body": "Images and diagrams reinforce the written text. Captions are the short descriptive sentences directly below an image explaining what it shows.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="30" y="10" width="120" height="75" fill="#e2e8f0" stroke="#94a3b8" rx="4"/>
            <circle cx="90" cy="45" r="20" fill="#38bdf8"/>
            <text x="90" y="105" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">Figure 1: Solar panel installation</text>
            <g transform="translate(180, 20)">
              <rect x="0" y="0" width="150" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
              <text x="75" y="24" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">The Caption:</text>
              <text x="75" y="46" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Explains the image</text>
              <text x="75" y="60" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">and links to text</text>
            </g>
          </g>"""),
        "golden_rule": "Always read the small print in the caption — it often contains exam answers!",
        "watch_out": "Don't ignore the pictures — exam questions often ask how the graphic supports the article.",
        "challenge_prompt": "What is the purpose of a caption underneath a photograph in a news article?",
        "answer_text": "To describe what is happening in the photograph and provide context for the reader."
    },

    # 6. Fact vs Opinion (Core Test)
    {
        "id": "e-l1-06",
        "number": 6,
        "title": "Fact vs Opinion (Core Test)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R6",
        "rule_heading": "True / False vs Personal Belief",
        "rule_body": "Fact: Can be proven true with dates, measurements, or official records ('The shop opens at 8 am'). Opinion: What someone thinks or feels ('The shop is wonderful').",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">FACT (Proven)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"The library has 12 computers."</text>
            <rect x="15" y="85" width="150" height="24" rx="4" fill="#3b82f6"/>
            <text x="90" y="101" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Can be counted &amp; verified</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">OPINION (Feeling)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">"It is the best place to study."</text>
            <rect x="15" y="85" width="150" height="24" rx="4" fill="#ec4899"/>
            <text x="90" y="101" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Personal point of view</text>
          </g>"""),
        "golden_rule": "If it uses words like 'best', 'delicious', or 'terrible', it is an OPINION!",
        "watch_out": "Numbers and dates are almost always facts.",
        "challenge_prompt": "Is this a fact or an opinion: 'The train ticket costs £14.50'?",
        "answer_text": "Fact (it is a verifiable price that can be proven true)."
    },

    # 7. Skimming for Overall Gist
    {
        "id": "e-l1-07",
        "number": 7,
        "title": "Skimming for Overall Gist",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R7",
        "rule_heading": "Rapid 30-Second Glance",
        "rule_body": "Skimming is fast reading to get the general idea: 1. Read the title and subheadings. 2. Glance at the first and last sentence of each paragraph. 3. Look at any pictures. Do NOT read every word.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">SKIMMING TECHNIQUE</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#0d9488">✓ Read titles, subheadings &amp; bold words</text>
            <text x="0" y="45" font-size="11.5" font-weight="700" fill="#0d9488">✓ Read the first sentence of each paragraph</text>
            <text x="0" y="68" font-size="11.5" font-weight="800" fill="#2563eb">Result: Understand the general topic in 30 seconds!</text>
          </g>"""),
        "golden_rule": "Skimming gives you the big picture without getting bogged down!",
        "watch_out": "Don't read word-by-word when skimming — keep your eyes moving quickly down the page.",
        "challenge_prompt": "What is the difference between skimming and scanning?",
        "answer_text": "Skimming is fast reading for the general overview; scanning is searching for a specific piece of information (like a number or name)."
    },

    # 8. Scanning for Key Facts & Numbers
    {
        "id": "e-l1-08",
        "number": 8,
        "title": "Scanning for Facts &amp; Numbers",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R8",
        "rule_heading": "Search like a Metal Detector",
        "rule_body": "Scanning is searching for specific targets: Look for capital letters (names, places), numbers (dates, times, prices), or symbols (£, %, @). Ignore everything else until you spot your target.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="900" fill="#1e40af" text-anchor="middle">SCANNING TARGET CLUES</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">• Looking for a price? Scan for: '£' and decimal points</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">• Looking for a person/place? Scan for: CAPITAL LETTERS</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">• Looking for a time? Scan for: 'am', 'pm', or colon (14:30)</text>
          </g>"""),
        "golden_rule": "Lock your target in your mind before your eyes touch the page!",
        "watch_out": "Don't start reading the whole text from the beginning when answering 'What time...' questions.",
        "challenge_prompt": "If a question asks: 'Who is the event coordinator?', what visual clue will you scan for?",
        "answer_text": "Scan for Capital Letters indicating a person's name or title (e.g. 'Coordinator' or 'Sarah Jenkins')."
    },

    # 9. Simple Inference ("Reading Clues")
    {
        "id": "e-l1-09",
        "number": 9,
        "title": "Simple Inference (Reading Clues)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R9",
        "rule_heading": "Detective Reading",
        "rule_body": "Inference means working out meaning from hints in the text: If someone is wearing a heavy winter coat, gloves, and shivering, you infer that the weather is freezing.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">INFERENCE DETECTIVE CLUES</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#2563eb">Text: "She slammed her locker door and stomped away."</text>
            <rect x="0" y="35" width="320" height="30" rx="4" fill="#dbeafe"/>
            <text x="160" y="55" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">Inference: She is feeling very angry or upset.</text>
          </g>"""),
        "golden_rule": "Inference is finding the hidden clue in the writer's description!",
        "watch_out": "Make sure your answer is directly supported by words in the text.",
        "challenge_prompt": "Text: 'Liam yawned and kept rubbing his eyes during the lecture.' What can you infer about Liam?",
        "answer_text": "You can infer that Liam is tired or bored."
    },

    # 10. Vocabulary: Using Context Clues
    {
        "id": "e-l1-10",
        "number": 10,
        "title": "Vocabulary: Using Context Clues",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R10",
        "rule_heading": "Guess the Word from the Sentence",
        "rule_body": "If you don't know a word: 1. Read the words before and after it. 2. Look for examples or explanations in the sentence. 3. Try replacing it with a word you do know that makes sense.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">CONTEXT CLUE STRATEGY</text>
            <text x="25" y="55" font-size="11" font-weight="700" fill="#0f172a">"The recipe requires several condiments, like ketchup and mustard."</text>
            <text x="25" y="80" font-size="11" font-weight="700" fill="#475569">Clue: Ketchup and mustard are sauces/relishes added to food.</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#15803d">Meaning: 'Condiments' means seasonings or sauces.</text>
          </g>"""),
        "golden_rule": "Read the whole sentence before deciding an unknown word is impossible!",
        "watch_out": "Don't panic when you see long words — look for root words you already recognise.",
        "challenge_prompt": "What does 'hazardous' mean in: 'Wear gloves when handling hazardous chemicals that burn the skin'?",
        "answer_text": "'Hazardous' means dangerous or harmful."
    },

    # 11. Alphabetical Order & Directory Searching
    {
        "id": "e-l1-11",
        "number": 11,
        "title": "Alphabetical Order &amp; Directories",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R11",
        "rule_heading": "Dictionaries &amp; Index Pages",
        "rule_body": "A to Z alphabetical order: Look at the 1st letter. If 1st letters are the same, look at the 2nd letter (Apple, Apricot). If 2nd letters match, look at the 3rd letter.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">ALPHABETICAL ORDERING</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#475569">Put in order: Brown, Baker, Bailey</text>
            <text x="30" y="78" font-size="11" font-weight="700" fill="#2563eb">1. All start with 'B'</text>
            <text x="30" y="98" font-size="11" font-weight="700" fill="#2563eb">2. Compare second letters: Ba... before Br...</text>
            <text x="30" y="118" font-size="11" font-weight="800" fill="#059669">3. Correct order: Bailey, Baker, Brown</text>
          </g>"""),
        "golden_rule": "Look at the 3rd and 4th letter if the first two letters are identical!",
        "watch_out": "Surnames in directories are listed Last Name first: 'Smith, John'.",
        "challenge_prompt": "Put in alphabetical order: Nurse, Needle, Next, Night.",
        "answer_text": "Needle, Next, Night, Nurse."
    },

    # 12. Instructions & Guides
    {
        "id": "e-l1-12",
        "number": 12,
        "title": "Instructions &amp; Step-by-Step",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R12",
        "rule_heading": "Chronological Sequence &amp; Imperatives",
        "rule_body": "Instructions must be followed in order. Look for sequence words: First, Next, Then, After that, Finally. Action verbs (bossy verbs) start each instruction ('Turn off power').",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">FOLLOWING INSTRUCTIONS</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">Step 1: First, wash hands thoroughly</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">Step 2: Next, open sterile packaging</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#0f172a">Step 3: Finally, apply bandage securely</text>
          </g>"""),
        "golden_rule": "Instructions always use imperative 'bossy' verbs at the start of sentences!",
        "watch_out": "Never skip a step when answering questions about instructional texts.",
        "challenge_prompt": "Identify the imperative verb in: 'Carefully insert the key and turn clockwise.'",
        "answer_text": "'insert' and 'turn'."
    },

    # 13. Formal vs Informal Language
    {
        "id": "e-l1-13",
        "number": 13,
        "title": "Formal vs Informal Language",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R13",
        "rule_heading": "Professional vs Casual Speech",
        "rule_body": "Formal: Used with managers, council, doctors ('I am writing to enquire', no slang, full words). Informal: Used with friends, family ('Hi mate', contractions, emojis, casual phrases).",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">FORMAL</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• "Dear Sir or Madam"</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• "I am writing to..."</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• "Yours sincerely"</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">INFORMAL</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• "Hi Alex"</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• "Can't wait to see you!"</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• "Cheers / Bye"</text>
          </g>"""),
        "golden_rule": "Avoid contractions (don't, can't) when writing formal letters or reports!",
        "watch_out": "Don't use informal slang like 'gonna' or 'cool' in workplace emails.",
        "challenge_prompt": "Rewrite this informally for a friend: 'I should be delighted to accompany you to the cinema.'",
        "answer_text": "'I'd love to come to the cinema with you!' (or 'I'd love to go to the cinema!')."
    },

    # 14. Comparing Two Simple Texts
    {
        "id": "e-l1-14",
        "number": 14,
        "title": "Comparing Two Simple Texts",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R14",
        "rule_heading": "What is the Same? What is Different?",
        "rule_body": "To compare two texts at Level 1: 1. State one piece of information that BOTH texts agree on. 2. State one difference between the two texts (e.g. price, opening time, or opinion).",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">LEVEL 1 TEXT COMPARISON</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="700" fill="#059669">Agreement: "Both texts state that the gym has a swimming pool."</text>
            <text x="0" y="45" font-size="11.5" font-weight="700" fill="#dc2626">Difference: "However, Text A says it costs £30 while Text B says £35."</text>
          </g>"""),
        "golden_rule": "Always answer both parts: one similarity AND one difference!",
        "watch_out": "Make sure you name both Text A and Text B in your answer.",
        "challenge_prompt": "Text 1 says a cafe is open 7 days a week. Text 2 says it is open Monday to Saturday only. What is the difference?",
        "answer_text": "Text 1 says the cafe opens on Sundays (7 days), while Text 2 says it is closed on Sundays (6 days)."
    },

    # 15. Target Audience (Who is it for?)
    {
        "id": "e-l1-15",
        "number": 15,
        "title": "Target Audience (Who is it for?)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Reading Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.R15",
        "rule_heading": "Spotting Who the Text is Written For",
        "rule_body": "To find the audience, look at who benefits from the information: Parents (school notices), Motorists (parking leaflet), Dog owners, Job seekers, Patients.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#5b21b6" text-anchor="middle">IDENTIFYING TARGET AUDIENCE</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">• Look at vocabulary and images</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">• Notice who is directly addressed ('Dear Residents')</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#7c3aed">• Be specific: 'New parents', not just 'people'</text>
          </g>"""),
        "golden_rule": "Be specific when naming the audience (e.g. 'Gym members', NOT just 'adults')!",
        "watch_out": "Don't just say 'everyone' — almost every text has a specific intended reader.",
        "challenge_prompt": "A leaflet gives advice on preparing babies for weaning onto solid food. Who is the target audience?",
        "answer_text": "Parents and caregivers of young babies."
    }
]

CARDS_B = [
    # 16. Informal Email to a Friend
    {
        "id": "e-l1-16",
        "number": 16,
        "title": "Informal Email to a Friend",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W16",
        "rule_heading": "Friendly Greeting &amp; Clear Points",
        "rule_body": "Format: 1. Subject line. 2. Friendly greeting (Hi Sam / Dear Chloe). 3. Polite friendly opener ('Hope you are well'). 4. Clear details in 2 paragraphs. 5. Warm sign-off (Best wishes / See you soon).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="25" y="24" font-size="10" font-weight="800" fill="#0f172a">Subject: Catching up / Weekend plans</text>
            <line x1="15" y1="34" x2="325" y2="34" stroke="#cbd5e1"/>
            <text x="25" y="55" font-size="10.5" font-weight="700" fill="#2563eb">Hi Marcus,</text>
            <text x="25" y="75" font-size="10" font-weight="700" fill="#475569">Hope you are having a good week. Would you like to meet...</text>
            <text x="25" y="105" font-size="10" font-weight="800" fill="#059669">See you soon, / Best wishes,</text>
          </g>"""),
        "golden_rule": "Always include a relevant Subject Line, even for friendly emails!",
        "watch_out": "Even informal emails must have capital letters and full stops in exams.",
        "challenge_prompt": "What are two appropriate sign-offs for an informal email to a friend?",
        "answer_text": "'Best wishes,' or 'See you soon,'."
    },

    # 17. Formal Email (Enquiry or Absence)
    {
        "id": "e-l1-17",
        "number": 17,
        "title": "Formal Email (Enquiry/Absence)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W17",
        "rule_heading": "Polite Workplace Message",
        "rule_body": "Format: 1. Clear subject line ('Absence Notification - 12 Oct'). 2. Polite greeting (Dear Mr Davies). 3. Factual reason for email. 4. Request for confirmation or action. 5. Formal sign-off (Kind regards).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="25" y="24" font-size="10" font-weight="800" fill="#1e40af">Subject: Absence Notification: [Your Name]</text>
            <line x1="15" y1="34" x2="325" y2="34" stroke="#cbd5e1"/>
            <text x="25" y="55" font-size="10.5" font-weight="800" fill="#0f172a">Dear Ms Taylor,</text>
            <text x="25" y="75" font-size="10" font-weight="700" fill="#475569">I am writing to inform you that I am unwell today and cannot attend work...</text>
            <text x="25" y="105" font-size="10" font-weight="800" fill="#059669">Kind regards,</text>
          </g>"""),
        "golden_rule": "Keep workplace emails concise, polite, and professional!",
        "watch_out": "Don't write text-speak (e.g. 'u', 'thx', 'c u') in any exam email.",
        "challenge_prompt": "Write a professional closing sign-off for a formal email to your tutor.",
        "answer_text": "'Kind regards,' or 'Best regards,' followed by your full name."
    },

    # 18. Formal Letter of Complaint
    {
        "id": "e-l1-18",
        "number": 18,
        "title": "Letter of Complaint (L1)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W18",
        "rule_heading": "Addresses • Clear Issue • Expected Remedy",
        "rule_body": "Layout: Addresses and date at top. Opening: 'I am writing to complain about...'. Body: Factual details (date, receipt number, defect). Closing: What you want done ('I expect a full refund or replacement').",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="25" y="24" font-size="10" font-weight="800" fill="#0f172a">Dear Customer Services,</text>
            <text x="25" y="48" font-size="10" font-weight="700" fill="#475569">1. Reason: I am writing to complain about my recent order...</text>
            <text x="25" y="72" font-size="10" font-weight="700" fill="#475569">2. Problem: The item arrived damaged on 14th May...</text>
            <text x="25" y="96" font-size="10" font-weight="700" fill="#2563eb">3. Solution: I request a replacement or full refund...</text>
            <text x="25" y="118" font-size="10" font-weight="800" fill="#0f172a">Yours faithfully,</text>
          </g>"""),
        "golden_rule": "Be polite and factual — never use rude or abusive language when complaining!",
        "watch_out": "Always state what resolution you expect (refund, apology, repair).",
        "challenge_prompt": "What should always be stated in the final paragraph of a complaint letter?",
        "answer_text": "The action or remedy you expect the company to take (e.g. a refund or replacement)."
    },

    # 19. Simple Article for Newsletter
    {
        "id": "e-l1-19",
        "number": 19,
        "title": "Community Newsletter Article",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W19",
        "rule_heading": "Catchy Title • Positive News • Details",
        "rule_body": "Features: 1. Interesting Title. 2. Introduction: What, where, and when. 3. Body: Highlights, quotes, and benefits for residents. 4. Call to join or participate.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">NEWSLETTER ARTICLE</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#0f172a">Title: New Community Garden Opens!</text>
            <text x="25" y="78" font-size="10" font-weight="700" fill="#475569">On Saturday, local volunteers transformed the park...</text>
            <text x="25" y="105" font-size="10.5" font-weight="800" fill="#16a34a">Come along this Saturday at 10 am to help plant seeds!</text>
          </g>"""),
        "golden_rule": "Articles must have a headline at the top!",
        "watch_out": "Organise into at least two or three paragraphs rather than one solid block of text.",
        "challenge_prompt": "Write an engaging title for an article about a local fun run.",
        "answer_text": "Example: 'Lace Up Your Trainers for the Annual Riverside Fun Run!'"
    },

    # 20. Event Leaflet / Flyer
    {
        "id": "e-l1-20",
        "number": 20,
        "title": "Writing an Event Flyer / Leaflet",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W20",
        "rule_heading": "Who • What • Where • When • Cost",
        "rule_body": "A flyer must include the 5 W's: What the event is. When (date &amp; time). Where (venue). Cost (ticket price / free). Who to contact (email / telephone / website).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="170" y="24" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">COMMUNITY BAKE SALE</text>
            <text x="30" y="50" font-size="10.5" font-weight="700" fill="#0f172a">📅 Date: Saturday 18th November  |  ⏰ Time: 10am - 2pm</text>
            <text x="30" y="72" font-size="10.5" font-weight="700" fill="#0f172a">📍 Venue: St Mark's Community Hall</text>
            <text x="30" y="94" font-size="10.5" font-weight="700" fill="#0f172a">🎟️ Entry: FREE (All proceeds to charity)</text>
            <text x="30" y="115" font-size="10" font-weight="800" fill="#be185d">📞 Contact: bakesale@email.com / 01865 123456</text>
          </g>"""),
        "golden_rule": "Make dates, times, and venue stand out with bullet points!",
        "watch_out": "Don't forget contact details — visitors need to know how to book or ask questions.",
        "challenge_prompt": "What five essential details must every event flyer include?",
        "answer_text": "1. Event name (what). 2. Date and time (when). 3. Location (where). 4. Price/ticket cost. 5. Contact information."
    },

    # 21. Writing a Review
    {
        "id": "e-l1-21",
        "number": 21,
        "title": "Writing a Review (L1)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W21",
        "rule_heading": "What You Liked &amp; What Could Improve",
        "rule_body": "Review structure: 1. Star rating (e.g. 4/5). 2. What you bought or experienced. 3. Positive features. 4. One thing that could be improved. 5. Overall recommendation.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#b45309" text-anchor="middle">CAFE REVIEW ★★★★☆</text>
            <text x="25" y="55" font-size="10.5" font-weight="700" fill="#059669">✓ Positives: Delicious food and friendly staff.</text>
            <text x="25" y="80" font-size="10.5" font-weight="700" fill="#dc2626">✗ Drawback: The service was slightly slow at lunch.</text>
            <text x="25" y="105" font-size="10.5" font-weight="800" fill="#0f172a">Recommendation: I would definitely return!</text>
          </g>"""),
        "golden_rule": "Give specific reasons for your opinion rather than just saying 'it was good'!",
        "watch_out": "Mention both pros and at least one small con to show balanced judgment.",
        "challenge_prompt": "Write a sentence recommending a book or film you enjoyed.",
        "answer_text": "'I would highly recommend this film because the storyline was exciting and kept me guessing until the very end.'"
    },

    # 22. Incident / Accident Report
    {
        "id": "e-l1-22",
        "number": 22,
        "title": "Incident &amp; Accident Report",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W22",
        "rule_heading": "Strictly Factual &amp; Clear",
        "rule_body": "Workplace report format: 1. Date, time, and location of incident. 2. Persons involved and witnesses. 3. Factual description of what occurred (no guessing). 4. First aid given or action taken.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="24" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">ACCIDENT REPORT FORM</text>
            <text x="25" y="48" font-size="10" font-weight="700" fill="#0f172a">Date: 12 October  |  Time: 14:15  |  Location: Warehouse Bay 3</text>
            <text x="25" y="70" font-size="10" font-weight="700" fill="#475569">Details: Employee slipped on spilled water near the sink.</text>
            <text x="25" y="92" font-size="10" font-weight="700" fill="#475569">Action Taken: First aid ice pack applied; area cordoned off.</text>
            <text x="25" y="114" font-size="10" font-weight="800" fill="#059669">Reported by: [Staff Name]</text>
          </g>"""),
        "golden_rule": "Incident reports must be 100% factual — state only what happened!",
        "watch_out": "Don't assign blame or write emotional rants in an incident report.",
        "challenge_prompt": "Why should personal opinions be excluded from an workplace accident report?",
        "answer_text": "Accident reports must be objective legal records based entirely on verified facts."
    },

    # 23. Basic Paragraphing
    {
        "id": "e-l1-23",
        "number": 23,
        "title": "Basic Paragraphing (TiP ToP)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W23",
        "rule_heading": "New Idea = New Paragraph",
        "rule_body": "Start a new paragraph whenever there is a change in: Time (later that day), Place (back at the office), Topic (turning to the cost), or Person (a new speaker). Leave a blank line between paragraphs.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">WHEN TO START A NEW PARAGRAPH</text>
            <text x="40" y="55" font-size="11" font-weight="800" fill="#2563eb">Ti - Time (Next morning, Later)</text>
            <text x="40" y="75" font-size="11" font-weight="800" fill="#059669">P - Place (In the hospital, At home)</text>
            <text x="40" y="95" font-size="11" font-weight="800" fill="#d97706">To - Topic (Discussing the cost, Looking at safety)</text>
            <text x="40" y="115" font-size="11" font-weight="800" fill="#7c3aed">P - Person (A different speaker or character)</text>
          </g>"""),
        "golden_rule": "Leave a clear blank line between paragraphs in your exam!",
        "watch_out": "One giant unspaced block of writing loses marks for organisation.",
        "challenge_prompt": "What does the 'TiP ToP' paragraph rule stand for?",
        "answer_text": "Ti = Time, P = Place, To = Topic, P = Person (start a new paragraph when any of these change)."
    },

    # 24. Using Linking Words (Connectives)
    {
        "id": "e-l1-24",
        "number": 24,
        "title": "Using Linking Connectives",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W24",
        "rule_heading": "Joining Sentences Smoothly",
        "rule_body": "Use connectives to connect ideas: Adding (and, also, as well as). Contrasting (but, however, although). Explaining cause (because, so, therefore). Sequencing (then, after that, finally).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">ESSENTIAL CONNECTIVES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">Cause: "I was late BECAUSE the bus broke down."</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">Contrast: "The car was old, HOWEVER it ran well."</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#0f172a">Addition: "We need bread AND we also need milk."</text>
          </g>"""),
        "golden_rule": "Linking words turn short choppy sentences into flowing prose!",
        "watch_out": "Don't start every sentence with 'And' or 'Because'.",
        "challenge_prompt": "Join these two sentences with a suitable connective: 'It was raining heavily. We decided to walk to work.'",
        "answer_text": "'Although it was raining heavily, we decided to walk to work' (or 'It was raining heavily, but we decided to walk to work')."
    },

    # 25. Writing Instructions (Bossy Verbs)
    {
        "id": "e-l1-25",
        "number": 25,
        "title": "Writing Instructions (Bossy Verbs)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W25",
        "rule_heading": "Start with Imperative Verbs",
        "rule_body": "When writing instructions, start each point with a clear command verb (imperative): 'Chop', 'Wash', 'Turn', 'Press', 'Check'. Keep sentences direct, short, and numbered.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">IMPERATIVE COMMAND VERBS</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#2563eb">1. Wash hands with warm soap and water.</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#2563eb">2. Remove the plastic safety cap.</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#2563eb">3. Press the red button to power on.</text>
          </g>"""),
        "golden_rule": "Put the action verb first: 'Press button', not 'You should press button'!",
        "watch_out": "Avoid polite padding like 'If you wouldn't mind pressing...' in user instructions.",
        "challenge_prompt": "Rewrite as a clear command instruction: 'You need to make sure the door is locked before leaving.'",
        "answer_text": "'Lock the door securely before leaving.'"
    },

    # 26. Varying Sentence Lengths
    {
        "id": "e-l1-26",
        "number": 26,
        "title": "Varying Sentence Lengths",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W26",
        "rule_heading": "Mix Short and Long Sentences",
        "rule_body": "Use a mix: Short sentences create impact, suspense, or clarity ('Stop immediately.'). Longer compound sentences explain reasons and add detail smoothly.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">SENTENCE VARIETY</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#dc2626">Short: "Help arrived just in time." (Impact)</text>
            <text x="25" y="85" font-size="11" font-weight="700" fill="#0f172a">Long: "The team worked together through the night,</text>
            <text x="25" y="105" font-size="11" font-weight="700" fill="#0f172a">and they successfully restored full electrical power."</text>
          </g>"""),
        "golden_rule": "A short sentence at the end of a paragraph creates drama and punch!",
        "watch_out": "Don't write endless rambling sentences joined by 'and... and... and...'.",
        "challenge_prompt": "Why should you avoid having all sentences the same length?",
        "answer_text": "Writing with varied sentence lengths sounds natural, engaging, and prevents the text from becoming repetitive."
    },

    # 27. Tone: Polite & Constructive
    {
        "id": "e-l1-27",
        "number": 27,
        "title": "Tone: Polite and Constructive",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W27",
        "rule_heading": "Professional Courtesy",
        "rule_body": "Always maintain a polite, respectful tone even when making a complaint: Use 'Please could you look into this matter' rather than 'You need to sort this out now'.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">CONSTRUCTIVE POLITE TONE</text>
            <text x="25" y="55" font-size="10.5" font-weight="700" fill="#dc2626">Rude: "Your staff are useless and I want my money back."</text>
            <line x1="25" y1="68" x2="315" y2="68" stroke="#cbd5e1"/>
            <text x="25" y="90" font-size="10.5" font-weight="800" fill="#15803d">Polite: "I was disappointed with the service received,</text>
            <text x="25" y="110" font-size="10.5" font-weight="800" fill="#15803d">and would appreciate a full refund at your convenience."</text>
          </g>"""),
        "golden_rule": "Polite firmness achieves faster results than angry hostility!",
        "watch_out": "Never write in ALL CAPITALS in an email — it looks like shouting.",
        "challenge_prompt": "Make this sentence more polite: 'Give me the report by 3 pm.'",
        "answer_text": "'Please could you provide the report by 3 pm?'"
    },

    # 28. Checking Your Writing Checklist
    {
        "id": "e-l1-28",
        "number": 28,
        "title": "Proofreading Checklist",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "Writing Skills",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W28",
        "rule_heading": "Final 3-Minute Sweep",
        "rule_body": "Before submitting: 1. Capitals on names and 'I'. 2. Full stop at every sentence end. 3. Correct homophones (there/their/they're). 4. Clear paragraphs. 5. Does every sentence make sense?",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">5-POINT PROOFREADING SWEEP</text>
            <text x="30" y="52" font-size="10.5" font-weight="700" fill="#0f172a">[✓] 1. Every sentence starts with a CAPITAL letter</text>
            <text x="30" y="72" font-size="10.5" font-weight="700" fill="#0f172a">[✓] 2. Every sentence ends with . or ?</text>
            <text x="30" y="92" font-size="10.5" font-weight="700" fill="#0f172a">[✓] 3. The pronoun 'I' is always capitalized</text>
            <text x="30" y="112" font-size="10.5" font-weight="800" fill="#059669">[✓] 4. Clear paragraph breaks</text>
          </g>"""),
        "golden_rule": "Read your work slowly in your head to check for missing words!",
        "watch_out": "Don't rush to finish early — use the last minutes to collect easy SPaG marks.",
        "challenge_prompt": "What punctuation mark is missing from: 'How much does a weekly train ticket cost'",
        "answer_text": "A question mark (? at the end of the sentence)."
    }
]

CARDS_C = [
    # 29. Capital Letters: The 5 Golden Rules
    {
        "id": "e-l1-29",
        "number": 29,
        "title": "Capital Letters: 5 Golden Rules",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W29",
        "rule_heading": "M.I.N.T.S Rules",
        "rule_body": "Always use a capital letter for: M - Months &amp; Days (Monday, July). I - The word 'I'. N - Names of people &amp; places (Sarah, London). T - Titles of books/films. S - Start of every sentence.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">M.I.N.T.S FOR CAPITAL LETTERS</text>
            <text x="30" y="52" font-size="10.5" font-weight="800" fill="#0f172a">M - Months &amp; Days: Friday, October</text>
            <text x="30" y="72" font-size="10.5" font-weight="800" fill="#0f172a">I - The pronoun: 'I' (NEVER lower case 'i')</text>
            <text x="30" y="92" font-size="10.5" font-weight="800" fill="#0f172a">N - Names: David, Manchester, NHS</text>
            <text x="30" y="112" font-size="10.5" font-weight="800" fill="#059669">S - Start of every new sentence</text>
          </g>"""),
        "golden_rule": "The word 'I' is ALWAYS a capital letter, no matter where it is in a sentence!",
        "watch_out": "Days and months must have capitals: 'wednesday' and 'august' are WRONG.",
        "challenge_prompt": "Correct the capital letters: 'last monday, i went to birmingham with my sister anna.'",
        "answer_text": "'Last Monday, I went to Birmingham with my sister Anna.'"
    },

    # 30. Full Stops & Question Marks
    {
        "id": "e-l1-30",
        "number": 30,
        "title": "Full Stops &amp; Question Marks",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W30",
        "rule_heading": "Sentence Endings",
        "rule_body": "Every complete sentence must end with an end mark: Full stop (.) for statements. Question mark (?) for direct questions starting with Who, What, Where, When, Why, How, or Can.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">SENTENCE ENDINGS</text>
            <text x="30" y="60" font-size="11.5" font-weight="800" fill="#2563eb">Statement (.): "The meeting begins at 10 am."</text>
            <text x="30" y="95" font-size="11.5" font-weight="800" fill="#dc2626">Question (?): "What time does the meeting start?"</text>
          </g>"""),
        "golden_rule": "Direct questions always demand a question mark (?)!",
        "watch_out": "Never use multiple question marks (???) or full stops (...!) in exam writing.",
        "challenge_prompt": "Add the correct punctuation mark: 'Could you please confirm your email address'",
        "answer_text": "'Could you please confirm your email address?'"
    },

    # 31. Exclamation Marks
    {
        "id": "e-l1-31",
        "number": 31,
        "title": "Exclamation Marks (!)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W31",
        "rule_heading": "Urgency, Surprise &amp; Warning",
        "rule_body": "Use exclamation marks (!) sparingly to show strong emotion, surprise, danger, or urgency ('Watch out!', 'What wonderful news!'). Avoid in formal letters and reports.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
            <text x="170" y="26" font-size="13" font-weight="900" fill="#dc2626" text-anchor="middle">EXCLAMATION MARK RULES</text>
            <text x="30" y="58" font-size="11" font-weight="700" fill="#0f172a">✓ Use for emergency warnings: 'Fire! Evacuate now!'</text>
            <text x="30" y="82" font-size="11" font-weight="700" fill="#0f172a">✓ Use in friendly flyers: 'Join our summer gala!'</text>
            <text x="30" y="106" font-size="11" font-weight="800" fill="#dc2626">✗ DO NOT use in formal reports or complaint letters!</text>
          </g>"""),
        "golden_rule": "One exclamation mark is enough — never write '!!' or '!!!'!",
        "watch_out": "Overusing exclamation marks makes writing look childish.",
        "challenge_prompt": "Is an exclamation mark appropriate in a formal letter to your local council about council tax?",
        "answer_text": "No, formal letters should maintain a calm, professional tone using full stops."
    },

    # 32. Commas in Lists
    {
        "id": "e-l1-32",
        "number": 32,
        "title": "Commas in Lists",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W32",
        "rule_heading": "Separating 3 or More Items",
        "rule_body": "Use commas to separate items in a list of three or more things. Do NOT put a comma before the word 'and' at the end of a simple list.",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">COMMA LIST RULE</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="12" font-weight="800" fill="#2563eb">"We bought milk, eggs, bread and butter."</text>
            <text x="0" y="45" font-size="11" font-weight="700" fill="#475569">Commas between first items; 'and' before the last item.</text>
          </g>"""),
        "golden_rule": "Comma between items, 'and' before the final item!",
        "watch_out": "Don't put a comma after the final item in the list.",
        "challenge_prompt": "Punctuate with commas: 'The stall sold cakes pies pastries and fresh bread.'",
        "answer_text": "'The stall sold cakes, pies, pastries and fresh bread.'"
    },

    # 33. Apostrophes for Contractions
    {
        "id": "e-l1-33",
        "number": 33,
        "title": "Apostrophes for Contractions",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W33",
        "rule_heading": "Replacing Missing Letters",
        "rule_body": "An apostrophe replaces missing letters when two words are joined into one: do not → don't (o is missing). cannot → can't (no is missing). it is → it's (i is missing).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">CONTRACTION APOSTROPHES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">do not  →  don't (replaces 'o')</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">could not  →  couldn't (replaces 'o')</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#0f172a">they have  →  they've (replaces 'ha')</text>
          </g>"""),
        "golden_rule": "The apostrophe sits exactly where the missing letter used to be!",
        "watch_out": "Don't write 'dont' or 'cant' without an apostrophe — examiners mark these as spelling errors.",
        "challenge_prompt": "Write the contracted form with an apostrophe for: 'have not'.",
        "answer_text": "'haven't'."
    },

    # 34. Apostrophes for Possession
    {
        "id": "e-l1-34",
        "number": 34,
        "title": "Apostrophes for Possession",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W34",
        "rule_heading": "Showing Who Owns What",
        "rule_body": "Singular owner: Add 's after the owner's name (the boy's bike = bike belongs to one boy). Plural owners: If word already ends in s, just add apostrophe after the s (the boys' bikes = bikes belong to many boys).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">POSSESSIVE APOSTROPHE</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#0f172a">Singular: John's bag  (1 person owns it)</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#0f172a">Plural: The teachers' lounge  (many teachers)</text>
            <text x="30" y="105" font-size="10.5" font-weight="700" fill="#dc2626">⚠️ Never use an apostrophe for simple plurals ('two cats')!</text>
          </g>"""),
        "golden_rule": "Ask: 'Who does it belong to?' Then put the apostrophe after the owner!",
        "watch_out": "'CDs' and '1990s' do NOT have apostrophes (they are simple plurals).",
        "challenge_prompt": "Add the possessive apostrophe: 'The nurse coat was hanging on the door.'",
        "answer_text": "'The nurse's coat was hanging on the door.'"
    },

    # 35. Plural Rules (-s, -es, -ies, -ves)
    {
        "id": "e-l1-35",
        "number": 35,
        "title": "Plural Spelling Rules",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W35",
        "rule_heading": "-s, -es, -ies, -ves",
        "rule_body": "Standard: Add -s (book → books). Ending in ch, sh, s, x: Add -es (box → boxes, watch → watches). Ending in consonant + y: Drop y, add -ies (baby → babies). Ending in f/fe: Change to -ves (leaf → leaves).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">PLURAL SPELLING RULES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#2563eb">box → boxes  (ends in x, s, ch, sh → add -es)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#059669">city → cities  (consonant + y → change to -ies)</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#d97706">knife → knives  (ends in f/fe → change to -ves)</text>
          </g>"""),
        "golden_rule": "If there's a vowel before 'y' (boy, day), just add 's' (boys, days)!",
        "watch_out": "Don't write 'babys' or 'boxs' — apply the rules.",
        "challenge_prompt": "What is the correct plural form of 'match'?",
        "answer_text": "'matches' (ends in 'ch', so add '-es')."
    },

    # 36. Irregular Plurals
    {
        "id": "e-l1-36",
        "number": 36,
        "title": "Irregular Plurals",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W36",
        "rule_heading": "Words That Change Internally",
        "rule_body": "Some words change their internal vowels instead of adding 's': man → men, woman → women, child → children, person → people, tooth → teeth, foot → feet, mouse → mice. Sheep and fish stay the same.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">IRREGULAR PLURALS</text>
            <text x="40" y="55" font-size="11" font-weight="800" fill="#0f172a">child → children  (NOT childs)</text>
            <text x="40" y="78" font-size="11" font-weight="800" fill="#0f172a">person → people  (NOT persons)</text>
            <text x="40" y="101" font-size="11" font-weight="800" fill="#0f172a">tooth → teeth  •  foot → feet</text>
          </g>"""),
        "golden_rule": "Never add an 's' to irregular plurals: 'childrens' is WRONG!",
        "watch_out": "'Women' is pronounced 'wim-in' (plural); 'woman' is singular.",
        "challenge_prompt": "Correct the error: 'Several childs were playing in the park.'",
        "answer_text": "'Several children were playing in the park.'"
    },

    # 37. Subject-Verb Agreement (Basic)
    {
        "id": "e-l1-37",
        "number": 37,
        "title": "Subject-Verb Agreement (L1)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W37",
        "rule_heading": "Singular vs Plural Matching",
        "rule_body": "I go / He goes. We are / She is. They were / He was. You do / She does. The verb must agree with who is doing the action.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">AGREEMENT MATCHING</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">He WAS (singular)  |  They WERE (plural)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">She DOES (singular)  |  They DO (plural)</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#dc2626">WRONG: "We was going..." → CORRECT: "We were going..."</text>
          </g>"""),
        "golden_rule": "'We was' is always marked wrong — it must be 'We were'!",
        "watch_out": "Watch out for slang habits in speaking that creep into written work.",
        "challenge_prompt": "Choose the correct verb: 'The nurses (was / were) very supportive.'",
        "answer_text": "'were' ('nurses' is plural, so it takes 'were')."
    },

    # 38. Past Tense Regular Verbs (-ed)
    {
        "id": "e-l1-38",
        "number": 38,
        "title": "Past Tense (-ed Rules)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W38",
        "rule_heading": "Regular Past Tense Suffixes",
        "rule_body": "Most regular verbs add -ed (walk → walked). If verb ends in 'e', just add 'd' (like → liked). If short vowel + consonant, double consonant (stop → stopped, plan → planned).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">REGULAR PAST TENSE (-ED)</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">walk + ed = walked</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">hope + d = hoped  (drop redundant e)</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#15803d">stop → stopped  (double the 'p')</text>
          </g>"""),
        "golden_rule": "Double the consonant if the vowel before it is short (hop → hopped)!",
        "watch_out": "'Hoped' (from hope) has one 'p'; 'hopped' (from hop) has two 'p's.",
        "challenge_prompt": "Write the past tense of the verb 'drop'.",
        "answer_text": "'dropped' (double the final consonant). "
    },

    # 39. Irregular Past Tense Verbs
    {
        "id": "e-l1-39",
        "number": 39,
        "title": "Irregular Past Tense Verbs",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W39",
        "rule_heading": "Saw • Went • Bought • Came",
        "rule_body": "Irregular verbs do NOT add -ed in the past tense: See → saw (NOT seened or sawed). Go → went (NOT goed). Buy → bought (NOT buyed). Come → came (NOT comed). Write → wrote.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">IRREGULAR VERBS IN PAST TENSE</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#059669">see → SAW  |  go → WENT</text>
            <text x="30" y="80" font-size="11" font-weight="800" fill="#059669">buy → BOUGHT  |  catch → CAUGHT</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#dc2626">⚠️ "I seen it" is WRONG → "I SAW it"</text>
          </g>"""),
        "golden_rule": "'I saw it' is correct; 'I seen it' is incorrect without 'have'!",
        "watch_out": "Don't add -ed to words that already changed: 'went', not 'wented'.",
        "challenge_prompt": "Correct the past tense verb: 'Yesterday, she goed to the supermarket and buyed milk.'",
        "answer_text": "'Yesterday, she went to the supermarket and bought milk.'"
    },

    # 40. Common Confusables (To, Too, Two)
    {
        "id": "e-l1-40",
        "number": 40,
        "title": "Confusables: To / Too / Two",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W40",
        "rule_heading": "Direction • Also/Excessive • Number",
        "rule_body": "TO: Direction or verb ('Going to school', 'to sleep'). TOO: Means 'also' or 'too much' ('Can I come too?', 'too hot'). TWO: The number 2 ('two tickets').",
        "svg_html": wrap_svg("""
          <g transform="translate(30, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">TO</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#475569">Direction / Action</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#0f172a">"Go to work"</text>
          </g>
          <g transform="translate(170, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#9d174d" text-anchor="middle">TOO</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#475569">Also / Excessive</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#0f172a">"Too expensive"</text>
          </g>
          <g transform="translate(310, 20)">
            <rect x="0" y="0" width="120" height="120" rx="6" fill="#f0fdf4" stroke="#16a34a"/>
            <text x="60" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">TWO</text>
            <text x="10" y="55" font-size="10.5" font-weight="700" fill="#475569">Number 2</text>
            <text x="10" y="80" font-size="10" font-weight="700" fill="#0f172a">"Two cups"</text>
          </g>"""),
        "golden_rule": "'Too' has an extra 'o' because it has too much of something!",
        "watch_out": "'I want to go to' is WRONG — it must be 'I want to go too'.",
        "challenge_prompt": "Fill the blanks: 'We bought (to / too / two) tickets (to / too / two) London.'",
        "answer_text": "'We bought two tickets to London.'"
    },

    # 41. Common Confusables (There, Their, They're)
    {
        "id": "e-l1-41",
        "number": 41,
        "title": "There / Their / They're (L1)",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W41",
        "rule_heading": "Location • Belonging • They Are",
        "rule_body": "THERE has 'here' in it = place ('over there'). THEIR has 'heir' in it = ownership ('their coats'). THEY'RE has an apostrophe = 'they are' ('they're coming').",
        "svg_html": wrap_svg("""
          <rect x="30" y="20" width="400" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
          <text x="230" y="42" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">HOMOPHONE MEMORY TRICK</text>
          <g transform="translate(60, 60)">
            <text x="0" y="20" font-size="11.5" font-weight="800" fill="#2563eb">tHERE = Has the word 'HERE' (place)</text>
            <text x="0" y="45" font-size="11.5" font-weight="800" fill="#059669">tHEIR = Belongs to them</text>
            <text x="0" y="70" font-size="11.5" font-weight="800" fill="#dc2626">THEY'RE = Short for 'THEY ARE'</text>
          </g>"""),
        "golden_rule": "Test with 'they are' — if it fits, use 'they're'!",
        "watch_out": "This is tested in almost every Functional Skills English exam.",
        "challenge_prompt": "Which word completes the sentence: 'The team forgot to submit ______ timesheets.'",
        "answer_text": "'their' (possession/belonging to the team)."
    },

    # 42. High-Frequency Essential Spellings
    {
        "id": "e-l1-42",
        "number": 42,
        "title": "Essential Level 1 Spellings",
        "subject": "english",
        "level": "l1",
        "subject_label": "English",
        "level_label": "Level 1",
        "strand_name": "SPaG Essentials",
        "strand_theme": "teal",
        "dfe_code": "DfE L1.W42",
        "rule_heading": "The 10 Golden Words",
        "rule_body": "1. Because (Big Elephants Can Always Upset Small Elephants). 2. Beautiful. 3. Believe (never be-LIE-ve a lie). 4. Friend (ends in end). 5. Tomorrow (1 'm', 2 'r's). 6. Wednesday. 7. People.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">ESSENTIAL SPELLING MNEMONICS</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#0f172a">• FriEND: A true friend stays to the END</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#0f172a">• Wed-nes-day: Say it as 'Wed-Nes-Day'</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#15803d">• Tomorrow: 1 Morning, 2 Roses (1 m, 2 r's)</text>
          </g>"""),
        "golden_rule": "Spell 'friend' with 'i' before 'e', ending in 'end'!",
        "watch_out": "'Becos' and 'tommorow' are immediate red pen errors.",
        "challenge_prompt": "Spell the day of the week that comes after Tuesday.",
        "answer_text": "'Wednesday'."
    }
]

def main():
    base_dir = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/decks/english_l1"
    os.makedirs(base_dir, exist_ok=True)

    with open(os.path.join(base_dir, "strand_a.py"), "w") as f:
        f.write('\"\"\"English L1 Strand A: Reading Fundamentals (Cards 1-15)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_A, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_b.py"), "w") as f:
        f.write('\"\"\"English L1 Strand B: Writing Formats & Composition (Cards 16-28)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_B, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "strand_c.py"), "w") as f:
        f.write('\"\"\"English L1 Strand C: Essential SPaG & Punctuation (Cards 29-42)\"\"\"\n')
        f.write('CARDS = ' + pprint.pformat(CARDS_C, indent=2, width=120) + '\n')

    with open(os.path.join(base_dir, "__init__.py"), "w") as f:
        f.write('from .strand_a import CARDS as STRAND_A\n')
        f.write('from .strand_b import CARDS as STRAND_B\n')
        f.write('from .strand_c import CARDS as STRAND_C\n\n')
        f.write('CARDS = STRAND_A + STRAND_B + STRAND_C\n')

    print(f"✓ English Level 1 Complete: {len(CARDS_A) + len(CARDS_B) + len(CARDS_C)} cards generated!")

if __name__ == "__main__":
    main()
