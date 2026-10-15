# spag_data_e3_84p.py
# ==============================================================================
# Master Functional Skills English: Entry Level 3 SPaG Complete Curriculum
# Mapped strictly to Ofqual Entry Level 3 Functional Skills English Subject Content
# Follows the Raymond Murphy 'Grammar in Use' Two-Page Facing Spread Schema
#
# Complete data foundation for 82-page publication:
# - Diagnostic Assessment: 24 Questions mapped 1:1 to Units 1 to 24
# - 24 Two-Page Units (48 pages)
# - Phonics Spelling Rules & Master High-Frequency Word Banks (8 pages)
# - Mixed Proofreading & Sentence Building Workouts (6 pages)
# - Practical Workplace Writing Tasks with Lined Working Frames (6 pages)
# - Complete Explanatory Answer Key (6 pages)
# - Candidate Self-Audit Checklist (1 page)
# ==============================================================================

THEME_E3 = {
    "code": "E3",
    "title": "Entry Level 3 Mastery",
    "full_name": "Functional Skills English Entry Level 3",
    "subtitle": "Complete 82-Page SPaG Core Foundations & Building Blocks Handbook",
    "primary": "#881337",       # Deep Crimson
    "secondary": "#be123c",     # Ruby Red
    "accent": "#e11d48",        # Bright Crimson Rose
    "amber": "#fbbf24",         # Accent Amber
    "amber_dark": "#b45309",    # High contrast amber text
    "tint": "#fff1f2",          # Warm Rose tint
    "border_color": "#fecdd3",
    "badge_bg": "#be123c",
    "badge_text": "#ffffff",
    "cover_grad_start": "#3b0413",
    "cover_grad_mid": "#881337",
    "cover_grad_end": "#4c0519",
    "ofqual_code": "Entry Level 3 Writing (FS-ENG-E3)",
    "file_stem": "MasterFunctionalSkills_SPaG_Entry_Level_3_Mastery",
}

# ==============================================================================
# BASELINE DIAGNOSTIC ASSESSMENT: 24 QUESTIONS MAPPED 1:1 TO UNITS 1 TO 24
# ==============================================================================

DIAGNOSTIC_QUESTIONS = [
    # SECTION A: Questions 1 to 8 (Page 3)
    {
        "q_num": 1,
        "unit": 1,
        "topic": "Capital Letters: 'I' & Names",
        "question": "Which sentence correctly capitalises the personal pronoun 'I' and personal names?",
        "options": [
            "A) When mr ahmed arrived, i welcomed him to the office.",
            "B) When Mr Ahmed arrived, I welcomed him to the office.",
            "C) When Mr Ahmed arrived, i welcomed him to the office."
        ],
        "answer": "B",
        "reason": "The personal pronoun 'I' and both parts of a formal name ('Mr Ahmed') must always be capitalised."
    },
    {
        "q_num": 2,
        "unit": 2,
        "topic": "Capitals: Places, Days & Months",
        "question": "Which sentence uses capital letters correctly for days, months, and towns?",
        "options": [
            "A) The training starts on monday in leeds and finishes in march.",
            "B) The training starts on Monday in Leeds and finishes in march.",
            "C) The training starts on Monday in Leeds and finishes in March."
        ],
        "answer": "C",
        "reason": "Days ('Monday'), towns ('Leeds'), and months ('March') all require capital letters."
    },
    {
        "q_num": 3,
        "unit": 3,
        "topic": "Capitals: Brands, Streets & Postcodes",
        "question": "Which address label has capital letters in all the correct places?",
        "options": [
            "A) Tesco Express, 14 High Street, Manchester, M4 5BD",
            "B) Tesco Express, 14 high street, Manchester, m4 5bd",
            "C) tesco express, 14 High Street, manchester, M4 5BD"
        ],
        "answer": "A",
        "reason": "Brand names ('Tesco Express'), street names ('High Street'), cities ('Manchester'), and postcodes ('M4 5BD') must have capitals."
    },
    {
        "q_num": 4,
        "unit": 4,
        "topic": "Full Stops: Sentence Boundaries",
        "question": "Which option is correctly punctuated with a full stop ending a complete thought?",
        "options": [
            "A) David cleaned the staff kitchen he locked the door at five.",
            "B) David cleaned the staff kitchen. He locked the door at five.",
            "C) David cleaned the staff kitchen he locked. The door at five."
        ],
        "answer": "B",
        "reason": "Two separate complete thoughts require a full stop and a new capital letter: '...kitchen. He locked...'"
    },
    {
        "q_num": 5,
        "unit": 5,
        "topic": "Question Marks: Asking for Info",
        "question": "Which sentence correctly uses a question mark for an enquiry?",
        "options": [
            "A) Could you show me how to log into the computer system?",
            "B) Could you show me how to log into the computer system.",
            "C) I asked my manager how to log into the computer system?"
        ],
        "answer": "A",
        "reason": "'Could you show me...' is a direct request/question and must end with a question mark."
    },
    {
        "q_num": 6,
        "unit": 6,
        "topic": "Exclamation Marks: Safety & Urgent Warnings",
        "question": "Which safety warning is punctuated correctly with a single exclamation mark?",
        "options": [
            "A) Danger, keep away from the forklift truck?",
            "B) Danger! Keep clear of the moving forklift truck.",
            "C) Danger keep clear of the moving forklift truck!!!"
        ],
        "answer": "B",
        "reason": "An urgent safety alert uses a single exclamation mark to draw immediate attention: 'Danger!'"
    },
    {
        "q_num": 7,
        "unit": 7,
        "topic": "Simple Sentences (SVO)",
        "question": "Which sentence is a complete simple sentence with a Subject, Verb, and Object?",
        "options": [
            "A) The new delivery boxes in the storeroom.",
            "B) The warehouse assistant stacked the delivery boxes.",
            "C) Stacked the heavy delivery boxes carefully."
        ],
        "answer": "B",
        "reason": "'The warehouse assistant' (Subject) + 'stacked' (Verb) + 'the delivery boxes' (Object)."
    },
    {
        "q_num": 8,
        "unit": 8,
        "topic": "Joining Sentences with 'And'",
        "question": "Which option correctly joins two related pieces of information using 'and'?",
        "options": [
            "A) Sarah printed the shift rota and she posted it on the noticeboard.",
            "B) Sarah printed the shift rota and and she posted it on the noticeboard.",
            "C) Sarah printed the shift rota, and, she posted it on the noticeboard."
        ],
        "answer": "A",
        "reason": "'And' joins the two actions smoothly without double words or misplaced commas."
    },

    # SECTION B: Questions 9 to 16 (Page 4)
    {
        "q_num": 9,
        "unit": 9,
        "topic": "Joining Sentences with 'But'",
        "question": "Which sentence correctly contrasts two statements using 'but'?",
        "options": [
            "A) We ordered twenty safety helmets, but only twelve arrived.",
            "B) We ordered twenty safety helmets and only twelve arrived.",
            "C) We ordered twenty safety helmets but, only twelve arrived."
        ],
        "answer": "A",
        "reason": "'But' correctly signals an unexpected contrast between what was ordered and what arrived."
    },
    {
        "q_num": 10,
        "unit": 10,
        "topic": "Giving Reasons with 'Because'",
        "question": "Which sentence correctly gives a reason using 'because'?",
        "options": [
            "A) The store closed early because the power supply failed.",
            "B) The store closed early. Because the power supply failed.",
            "C) Because the store closed early so the power supply failed."
        ],
        "answer": "A",
        "reason": "'Because' connects the main clause directly to the explanation without splitting it into a fragment."
    },
    {
        "q_num": 11,
        "unit": 11,
        "topic": "Cause & Effect with 'So'",
        "question": "Which sentence correctly uses 'so' to show a result or consequence?",
        "options": [
            "A) The floor was wet because I put up a yellow caution sign.",
            "B) The floor was wet, so I put up a yellow caution sign.",
            "C) The floor was wet so because I put up a caution sign."
        ],
        "answer": "B",
        "reason": "'So' shows the action taken as a direct consequence of the wet floor."
    },
    {
        "q_num": 12,
        "unit": 12,
        "topic": "Commas in Simple Lists",
        "question": "Which sentence uses commas correctly to separate items in an equipment list?",
        "options": [
            "A) Please order pens, notebooks, paperclips and folders.",
            "B) Please order pens, notebooks, paperclips, and, folders.",
            "C) Please order pens notebooks paperclips, and folders."
        ],
        "answer": "A",
        "reason": "Commas separate the list items, and 'and' joins the final pair without extra commas."
    },
    {
        "q_num": 13,
        "unit": 13,
        "topic": "Present Tense: Everyday Routines",
        "question": "Which sentence correctly uses the present tense for a daily workplace routine?",
        "options": [
            "A) Every morning, I check the stock and log the deliveries.",
            "B) Every morning, I checked the stock and log the deliveries.",
            "C) Every morning, I checking the stock and log the deliveries."
        ],
        "answer": "A",
        "reason": "Daily routine actions with 'I' take the base form of the present tense ('check' and 'log')."
    },
    {
        "q_num": 14,
        "unit": 14,
        "topic": "Present Tense: He, She, It (+s/-es)",
        "question": "Which sentence uses the correct verb form for 'He' or 'She' in the present tense?",
        "options": [
            "A) Marcus lock the main entrance and set the alarm.",
            "B) Marcus locks the main entrance and sets the alarm.",
            "C) Marcus locking the main entrance and sets the alarm."
        ],
        "answer": "B",
        "reason": "Singular third-person subjects ('Marcus' / 'He') require an '-s' ending ('locks', 'sets')."
    },
    {
        "q_num": 15,
        "unit": 15,
        "topic": "Past Tense: Regular Verbs with -ed",
        "question": "Which sentence correctly spells the past tense regular verbs with '-ed'?",
        "options": [
            "A) Yesterday, the supervisor inspected the equipment and called the technician.",
            "B) Yesterday, the supervisor inspect the equipment and call the technician.",
            "C) Yesterday, the supervisor inspectid the equipment and callt the technician."
        ],
        "answer": "A",
        "reason": "Regular past tense adds '-ed' to the base verbs ('inspected', 'called')."
    },
    {
        "q_num": 16,
        "unit": 16,
        "topic": "Past Tense: Doubling Consonants",
        "question": "Which sentence correctly doubles the consonant before adding '-ed'?",
        "options": [
            "A) The driver stoped at the gate and planed his route.",
            "B) The driver stopped at the gate and planned his route.",
            "C) The driver stopd at the gate and pland his route."
        ],
        "answer": "B",
        "reason": "Short vowel + single consonant verbs double the final letter: 'stop' -> 'stopped', 'plan' -> 'planned'."
    },

    # SECTION C: Questions 17 to 24 (Page 5)
    {
        "q_num": 17,
        "unit": 17,
        "topic": "Irregular Past Verbs (Part 1)",
        "question": "Which sentence uses the correct irregular past tense verbs (was, were, had, went, saw)?",
        "options": [
            "A) The managers was in the meeting and I seen the visitor.",
            "B) The managers were in the meeting and I saw the visitor.",
            "C) The managers were in the meeting and I seed the visitor."
        ],
        "answer": "B",
        "reason": "Plural subject takes 'were' ('managers were'), and the past tense of 'see' is 'saw'."
    },
    {
        "q_num": 18,
        "unit": 18,
        "topic": "Irregular Past Verbs (Part 2)",
        "question": "Which sentence uses the correct irregular past verbs (came, did, said, took, gave)?",
        "options": [
            "A) The courier came at noon, took the parcel, and gave a receipt.",
            "B) The courier comed at noon, taked the parcel, and gived a receipt.",
            "C) The courier come at noon, took the parcel, and gived a receipt."
        ],
        "answer": "A",
        "reason": "The standard irregular past forms are 'came' (not comed), 'took' (not taked), and 'gave' (not gived)."
    },
    {
        "q_num": 19,
        "unit": 19,
        "topic": "Subject-Verb Agreement: Singular",
        "question": "Which sentence shows correct singular subject-verb agreement?",
        "options": [
            "A) The new apprentice has finished his training and is ready to work.",
            "B) The new apprentice have finished his training and are ready to work.",
            "C) The new apprentice has finished his training and were ready to work."
        ],
        "answer": "A",
        "reason": "Singular subject ('apprentice') agrees with singular verbs 'has' and 'is'."
    },
    {
        "q_num": 20,
        "unit": 20,
        "topic": "Subject-Verb Agreement: Plural",
        "question": "Which sentence shows correct plural subject-verb agreement?",
        "options": [
            "A) Both warehouse doors was open and the keys was missing.",
            "B) Both warehouse doors were open and the keys were missing.",
            "C) Both warehouse doors were open and the keys was missing."
        ],
        "answer": "B",
        "reason": "Plural subjects ('doors', 'keys') agree with plural verbs 'were'."
    },
    {
        "q_num": 21,
        "unit": 21,
        "topic": "Plural Nouns: Adding -s and -es",
        "question": "Which sentence spells all plural nouns correctly (boxes, dishes, matches)?",
        "options": [
            "A) Please pack the glass cups into the boxs and clear the dishs.",
            "B) Please pack the glass cups into the boxes and clear the dishes.",
            "C) Please pack the glass cups into the boxies and clear the dishies."
        ],
        "answer": "B",
        "reason": "Nouns ending in -x ('box') and -sh ('dish') take '-es' in the plural ('boxes', 'dishes')."
    },
    {
        "q_num": 22,
        "unit": 22,
        "topic": "Plural Nouns: Changing -y to -ies",
        "question": "Which sentence correctly changes 'y' to '-ies' for plural nouns?",
        "options": [
            "A) Our company operates factories in three different cities.",
            "B) Our company operates factorys in three different citys.",
            "C) Our company operates factories in three different cityes."
        ],
        "answer": "A",
        "reason": "Consonant + y changes to '-ies' in the plural: 'factory' -> 'factories', 'city' -> 'cities'."
    },
    {
        "q_num": 23,
        "unit": 23,
        "topic": "Homophones: To/Two/Too, There/Their, Hear/Here",
        "question": "Which sentence uses all homophones correctly?",
        "options": [
            "A) The two drivers parked their vans over there.",
            "B) The to drivers parked there vans over their.",
            "C) The too drivers parked they're vans over there."
        ],
        "answer": "A",
        "reason": "'Two' (number 2), 'their' (belonging to them), and 'there' (in that place)."
    },
    {
        "q_num": 24,
        "unit": 24,
        "topic": "Application Forms: Capitals & Punctuation",
        "question": "Which application form profile section is completed with perfect capitals and punctuation?",
        "options": [
            "A) I am applying for the care assistant role. I have two years of experience in Leeds.",
            "B) i am applying for the care assistant role i have two years of experience in leeds.",
            "C) I am applying for the care assistant role, I have two years of experience in leeds."
        ],
        "answer": "A",
        "reason": "Full capitalisation of 'I' and 'Leeds', with proper full stops separating the complete thoughts."
    }
]

DIAGNOSTIC_SCORING_BANDS = [
    {
        "range": "21 – 24 Marks",
        "band": "Mastery Foundation",
        "color": "#16a34a",
        "bg": "#f0fdf4",
        "border": "#86efac",
        "summary": "Outstanding SPaG foundation. You demonstrate secure control of capitalisation, punctuation, tenses, and plural spelling rules.",
        "action": "Proceed directly to Unit exercises for fast review, and challenge yourself with the Mixed Proofreading Workouts (pp. 63–68) and Practical Writing Tasks (pp. 69–74)."
    },
    {
        "range": "14 – 20 Marks",
        "band": "Developing Competency",
        "color": "#d97706",
        "bg": "#fffbeb",
        "border": "#fde68a",
        "summary": "Good practical knowledge with specific priority areas. A few rules such as consonant doubling, irregular verbs, or list commas need consolidation.",
        "action": "Use the Visual Study Selector on Page 6 to identify any incorrect question numbers. Revise those exact units thoroughly before attempting the mixed workouts."
    },
    {
        "range": "0 – 13 Marks",
        "band": "Priority Core Revision",
        "color": "#dc2626",
        "bg": "#fef2f2",
        "border": "#fecaca",
        "summary": "Core foundational skills require step-by-step reinforcement. Sentence boundaries, verb agreement, and capital letters must be secured.",
        "action": "Work through all 24 units sequentially. Study the left-hand theory spreads carefully, complete all right-hand drills, and self-check using the Explanatory Answer Key."
    }
]
