"""
spag_data_l2.py - Comprehensive Level 2 Educational Content Dataset
Includes:
- Diagnostic Assessment (10 questions + scoring matrix)
- 11 Murphy 2-Page Units (Units 1 to 11)
- Master Spelling Rules & Vocabulary (2 pages)
- Mixed Exam Proofreading Mock (2 pages)
- Complete Answer Key (4 pages)
"""

L2_DIAGNOSTIC = {
    "title": "Baseline Diagnostic Assessment: Level 2 SPaG Audit",
    "subtitle": "Complete this 10-minute diagnostic to identify your grammar, punctuation, and proofreading priority areas.",
    "questions": [
        {
            "num": 1,
            "topic": "Unit 1: Sentence Boundaries",
            "prompt": "Identify the sentence that correctly resolves the comma splice:",
            "options": [
                "A) The audit was completed early, the report was submitted on time.",
                "B) The audit was completed early; the report was submitted on time.",
                "C) The audit was completed early the report was submitted on time.",
                "D) The audit was completed early, however the report was submitted on time."
            ],
            "correct": "B"
        },
        {
            "num": 2,
            "topic": "Unit 2: Commas for Complex Sentences",
            "prompt": "Which sentence correctly punctuates the fronted adverbial clause?",
            "options": [
                "A) Although the fire alarm sounded three times none of the staff evacuated.",
                "B) Although the fire alarm sounded three times, none of the staff evacuated.",
                "C) Although, the fire alarm sounded three times none of the staff evacuated.",
                "D) Although the fire alarm sounded three times none of the staff, evacuated."
            ],
            "correct": "B"
        },
        {
            "num": 3,
            "topic": "Unit 3: Colons & Semicolons",
            "prompt": "Select the sentence with correct colon punctuation introducing a list:",
            "options": [
                "A) The new safety policy requires: steel-capped boots, high-vis vests, and hard hats.",
                "B) All site operatives must wear the following items: steel-capped boots, high-vis vests, and hard hats.",
                "C) All site operatives must wear: steel-capped boots, high-vis vests, and hard hats.",
                "D) The required items are: steel-capped boots, high-vis vests, and hard hats."
            ],
            "correct": "B"
        },
        {
            "num": 4,
            "topic": "Unit 4: Apostrophes",
            "prompt": "Choose the sentence with 100% accurate apostrophe usage:",
            "options": [
                "A) The company updated it's policy regarding the directors' company vehicles.",
                "B) The company updated its policy regarding the director's company vehicles.",
                "C) The company updated its' policy regarding the directors' company vehicles.",
                "D) The company updated its policy regarding the directors' company vehicles."
            ],
            "correct": "D"
        },
        {
            "num": 5,
            "topic": "Unit 5: Speech Marks & Quotations",
            "prompt": "Which sentence accurately quotes the health inspector's exact words in formal British style?",
            "options": [
                "A) The inspector stated, \"All hygiene records must be updated immediately.\"",
                "B) The inspector stated \"All hygiene records must be updated immediately\".",
                "C) The inspector stated, 'All hygiene records must be updated immediately'.",
                "D) The inspector stated, \"All hygiene records must be updated immediately\"."
            ],
            "correct": "A"
        },
        {
            "num": 6,
            "topic": "Unit 6: Subject-Verb Agreement",
            "prompt": "Identify the grammatically standard subject-verb agreement:",
            "options": [
                "A) Neither the clinical team nor the lead surgeon were aware of the missing steriliser.",
                "B) A detailed range of modern healthcare solutions were presented to the trust.",
                "C) Neither the clinical team nor the lead surgeon was aware of the missing steriliser.",
                "D) The committee have decided to dismiss the contractor immediately."
            ],
            "correct": "C"
        },
        {
            "num": 7,
            "topic": "Unit 7: Tense Consistency",
            "prompt": "Which sentence maintains logical, consistent chronological verb tenses?",
            "options": [
                "A) When the customer complained, the supervisor steps in and offered a refund.",
                "B) When the customer complained, the supervisor stepped in and offered a refund.",
                "C) When the customer complains, the supervisor stepped in and offered a refund.",
                "D) When the customer had complained, the supervisor steps in and offers a refund."
            ],
            "correct": "B"
        },
        {
            "num": 8,
            "topic": "Unit 8: Pronoun Precision",
            "prompt": "Select the sentence with unambiguous pronoun agreement:",
            "options": [
                "A) The manager told the technician that he had made a configuration error.",
                "B) After consulting with Dr Ellis, Sarah confirmed that the doctor would sign the discharge letter.",
                "C) When the laptop fell from the desk, it shattered into pieces.",
                "D) Between you and I, the promotion criteria should be reviewed."
            ],
            "correct": "B"
        },
        {
            "num": 9,
            "topic": "Unit 9: Formal Register & Tone",
            "prompt": "Which sentence achieves the most appropriate formal vocational register for a client report?",
            "options": [
                "A) We got super fed up with the delays and had a huge row with the delivery folks.",
                "B) We were bitterly disappointed and are gonna demand a full refund pronto.",
                "C) Following repeated consignment delays, formal representations were made to the carrier.",
                "D) You lot need to fix this massive mess before we get totally outraged."
            ],
            "correct": "C"
        },
        {
            "num": 10,
            "topic": "Unit 11: Advanced Homophones",
            "prompt": "Select the sentence that uses both homophones correctly:",
            "options": [
                "A) The new working hours will not effect our daily legal practise.",
                "B) The new working hours will not affect our daily legal practice.",
                "C) The new working hours will not effect our daily legal practice.",
                "D) The new working hours will not affect our daily legal practise."
            ],
            "correct": "B"
        }
    ],
    "scoring": [
        {"range": "8 – 10 Marks", "status": "Advanced SPaG Mastery", "advice": "Focus on high-speed proofreading accuracy and nuanced exam questions (Units 3, 8 & 11)."},
        {"range": "5 – 7 Marks", "status": "Intermediate Competence", "advice": "Review Units 1, 2, 4, 6 and 9 carefully to eliminate recurring workplace writing errors."},
        {"range": "0 – 4 Marks", "status": "Foundation Priority", "advice": "Work through all 11 units systematically in the Murphy 2-page spread sequence."}
    ]
}

L2_UNITS = [
    # UNIT 1
    {
        "unit_num": 1,
        "title": "Sentence Boundaries & Conquering Comma Splices",
        "strand": "Punctuation & Syntax (Ofqual L2.19)",
        "outcome": "Punctuate sentences correctly using full stops, semicolons, or conjunctions to prevent comma splices and run-ons.",
        # Left Page
        "anchor_title": "NHS Acute Ward Clinical Handover Note",
        "anchor_context": "HEALTHCARE / WARD MANAGEMENT",
        "anchor_text": "During an emergency handover, Staff Nurse Tariq wrote: <em>'Patient in Bed 4 experienced acute tachycardia, saline was administered immediately.'</em> The junior doctor misread this as one combined instruction. Two distinct medical events were illegally joined with only a comma, creating clinical ambiguity.",
        "formula_title": "The Sentence Boundary Architecture",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Independent Clause 1 (Complete Thought)"},
            {"cls": "fpill-punct", "text": "Full Stop [.] OR Semicolon [;] OR Comma + FANBOYS [, and]"},
            {"cls": "fpill-subj", "text": "Independent Clause 2 (Complete Thought)"}
        ],
        "formula_desc": "An independent clause contains a subject and a conjugated finite verb and expresses a complete thought. You cannot connect two independent clauses with a comma alone.",
        "compare_bad": "The laboratory results arrived at noon, the consultant immediately reviewed them.",
        "compare_bad_tag": "COMMA SPLICE (2 Independent Clauses glued with a comma)",
        "compare_good": "The laboratory results arrived at noon; the consultant immediately reviewed them.",
        "compare_good_tag": "STANDARD (Joined with Semicolon OR Full Stop OR Coordinating Conjunction)",
        "compare_why": "A comma represents a brief rhythm pause; it possesses zero grammatical strength to bond two independent thoughts. Use a semicolon to signal close thematic relation, or split with a full stop.",
        "golden_rule": "The Standalone Test: Read what comes before the comma. If it could stand alone as a sentence, and what comes after could also stand alone, REPLACE the comma with a full stop, semicolon, or ', and'.",
        "golden_mnemonic": "SPLICE CHECK: Never let a comma do a full stop's heavy lifting.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which sentence contains a comma splice?", "options": ["A) The server rebooted; users logged in.", "B) The server rebooted, users logged in.", "C) The server rebooted, so users logged in."], "ans": "B"},
            {"prompt": "2. Identify the correctly punctuated sentence:", "options": ["A) She finished the audit, however, she left.", "B) She finished the audit; however, she left.", "C) She finished the audit however she left."], "ans": "B"},
            {"prompt": "3. What is needed between 'Staff attended the briefing' and 'they signed the register'?", "options": ["A) A comma alone", "B) A semicolon or ', and'", "C) No punctuation"], "ans": "B"},
            {"prompt": "4. Select the valid compound sentence:", "options": ["A) Stock arrived early, we unloaded the pallets.", "B) Stock arrived early, and we unloaded the pallets.", "C) Stock arrived early we unloaded pallets."], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Correct this comma splice using a semicolon: 'The fire drill began at 10:00, staff assembled in Zone A.'", "hint": "Replace comma with ;", "ans": "The fire drill began at 10:00; staff assembled in Zone A."},
            {"prompt": "2. Correct this comma splice using a coordinating conjunction: 'Budget cuts were announced, the project continued.'", "hint": "Use ', but'", "ans": "Budget cuts were announced, but the project continued."},
            {"prompt": "3. Transform into two distinct sentences: 'The client rejected the proposal, they requested alterations.'", "hint": "Use a full stop", "ans": "The client rejected the proposal. They requested alterations."},
            {"prompt": "4. Punctuate with a transition adverb: 'Deliveries were halted [consequently] suppliers were notified.'", "hint": "Use ; consequently,", "ans": "Deliveries were halted; consequently, suppliers were notified."}
        ],
        "ex3": {
            "doc_type": "INTERNAL SHIFT HANDOVER MEMORANDUM",
            "from_to": "FROM: Shift Supervisor Evans | TO: Facilities Manager Davies | DATE: 14 Oct 2026",
            "body": "The night shift reported three separate power surges in Substation B, the primary transformer overheated rapidly. Maintenance dispatched an engineer at 03:15, he isolated the damaged circuit breakers. Production line 4 remained halted for two hours, customer orders were delayed until the morning shift arrived. Please review the equipment warranty, we must decide whether to replace the regulator today.",
            "error_count": 4,
            "error_types": "Comma Splices / Run-on Sentences"
        },
        "ex4": {
            "prompt": "You are a health and safety officer writing a 50-word incident summary following a chemical spill drill. You must write exactly 3 sentences describing what occurred, what action was taken, and what prevention step is required. Ensure you use NO comma splices; use at least one semicolon and one coordinating conjunction.",
            "criteria": ["3 complete sentences", "At least 1 semicolon", "At least 1 coordinating conjunction (, and / , but)", "Zero comma splices"]
        }
    },

    # UNIT 2
    {
        "unit_num": 2,
        "title": "Commas for Complex Sentences & Fronted Adverbials",
        "strand": "Punctuation & Complex Syntax (Ofqual L2.19)",
        "outcome": "Deploy commas accurately to isolate fronted adverbials, subordinate clauses, and parenthetical non-defining information.",
        # Left Page
        "anchor_title": "Logistics Depot Daily Operations Briefing",
        "anchor_context": "WAREHOUSING & SUPPLY CHAIN",
        "anchor_text": "A depot controller typed: <em>'While the forklift was loading the truck driver slept in the rest bay.'</em> Without a comma after the fronted subordinate clause, readers initially believe the forklift was loading the truck driver!",
        "formula_title": "Complex Sentence & Fronted Adverbial Architecture",
        "formula_pills": [
            {"cls": "fpill-conn", "text": "Subordinate Conjunction (Although / While / Because / When)"},
            {"cls": "fpill-clause", "text": "Subordinate Clause"},
            {"cls": "fpill-punct", "text": "COMMA [, ]"},
            {"cls": "fpill-subj", "text": "Main Independent Clause"}
        ],
        "formula_desc": "When a dependent or adverbial clause precedes the main sentence, a comma must mark the boundary. When the main clause comes first, no comma is typically needed.",
        "compare_bad": "Although the consignment was signed for by reception nobody alerted the site manager.",
        "compare_bad_tag": "MISSING FRONTED ADVERBIAL COMMA",
        "compare_good": "Although the consignment was signed for by reception, nobody alerted the site manager.",
        "compare_good_tag": "CORRECT SUBORDINATE CLAUSE COMMA BOUNDARY",
        "compare_why": "The introductory clause sets the condition. The comma alerts the reader that the dependent condition has concluded and the main executive message is beginning.",
        "golden_rule": "The Elevator Drop Rule: If an introductory phrase answers When, Where, Why, or Under What Condition, drop a comma immediately after it before entering your main clause.",
        "golden_mnemonic": "FRONTED CLAUSE FIRST? Comma in the middle. MAIN CLAUSE FIRST? Leave the comma out.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which sentence requires a comma?", "options": ["A) Before operating heavy machinery you must wear goggles.", "B) You must wear goggles before operating heavy machinery.", "C) Machinery requires goggles."], "ans": "A"},
            {"prompt": "2. Identify the correctly punctuated non-defining clause:", "options": ["A) Mr Patel who joined last month has won the safety award.", "B) Mr Patel, who joined last month, has won the safety award.", "C) Mr Patel who joined last month, has won the safety award."], "ans": "B"},
            {"prompt": "3. Where does the comma belong: 'Despite severe weather conditions the express courier arrived on time'?", "options": ["A) After 'Despite'", "B) After 'conditions'", "C) After 'courier'"], "ans": "B"},
            {"prompt": "4. Does this sentence require a comma: 'The audit failed because paperwork was lost'?", "options": ["A) Yes, before 'because'", "B) No, main clause comes first", "C) Yes, after 'paperwork'"], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Insert the missing comma: 'To ensure maximum compliance all employees must complete the GDPR module.'", "hint": "Find the end of the infinitive opener", "ans": "To ensure maximum compliance, all employees must complete the GDPR module."},
            {"prompt": "2. Insert parenthetical commas: 'The new regional depot which cost £2.4 million will open in November.'", "hint": "Enclose non-essential relative clause", "ans": "The new regional depot, which cost £2.4 million, will open in November."},
            {"prompt": "3. Add commas around the transitional word: 'The director however refused to authorise the expenditure.'", "hint": "Two commas around 'however'", "ans": "The director, however, refused to authorise the expenditure."},
            {"prompt": "4. Insert fronted clause comma: 'When the fire alarm sounds operatives must assemble in Car Park B.'", "hint": "Comma after sounds", "ans": "When the fire alarm sounds, operatives must assemble in Car Park B."}
        ],
        "ex3": {
            "doc_type": "DEPOT HEALTH & SAFETY COMPLIANCE NOTICE",
            "from_to": "FROM: Safety Auditor Thorne | TO: Logistics Personnel | DATE: 22 Oct 2026",
            "body": "Before entering the cold-storage facility operatives must inspect thermal protective suits for tears. In accordance with Section 4 of the safety manual forklift operators must sound horns at every intersection. Mr Higgins who inspects vehicle hoists found three hydraulic leaks yesterday morning. Consequently all affected loading bays have been closed until repairs finish. If an emergency occurs press the red isolator button immediately.",
            "error_count": 5,
            "error_types": "Missing Commas (Fronted Adverbials, Non-defining Clause, Transitional Adverb)"
        },
        "ex4": {
            "prompt": "Write a 50-word formal update to your transport director regarding unexpected road closures affecting delivery schedules. You must include at least two fronted adverbial clauses (e.g., 'Due to motorway resurfacing...', 'Although alternate routes were mapped...') and ensure each is followed by a comma.",
            "criteria": ["Formal workplace register", "At least 2 fronted adverbial clauses", "Accurate comma placement", "Clear practical delivery solution"]
        }
    },

    # UNIT 3
    {
        "unit_num": 3,
        "title": "Colons & Semicolons: High-Impact Punctuation",
        "strand": "Advanced Punctuation & Complex Syntax (Ofqual L2.19)",
        "outcome": "Master colons to introduce lists or explanations, and semicolons to link closely related independent clauses or complex lists.",
        # Left Page
        "anchor_title": "Council Planning Executive Formal Briefing",
        "anchor_context": "LOCAL GOVERNMENT / CIVIC PLANNING",
        "anchor_text": "In a formal budget submission, a planning officer wrote: <em>'The capital projects are: leisure centre expansion, library renovation, and cycle lanes.'</em> The examiner marked this as incorrect because a colon must NEVER separate a verb ('are') from its direct object.",
        "formula_title": "The Colon & Semicolon Precision Rules",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "COMPLETE INDEPENDENT SENTENCE"},
            {"cls": "fpill-punct", "text": "COLON [ : ]"},
            {"cls": "fpill-clause", "text": "Direct Explanation, Consequence, OR Structured List"}
        ],
        "formula_desc": "Rule 1 (Colon): What precedes a colon MUST be a complete grammatical sentence. Rule 2 (Semicolon): Use a semicolon to connect two complete sentences that share an intimate conceptual link without a conjunction.",
        "compare_bad": "The candidate lacks three vital skills; punctuality, formal writing, and digital literacy.",
        "compare_bad_tag": "SEMICOLON MISUSED AS LIST INTRODUCER",
        "compare_good": "The candidate lacks three vital skills: punctuality, formal writing, and digital literacy.",
        "compare_good_tag": "ACCURATE COLON INTRODUCING SPECIFIED LIST",
        "compare_why": "A colon points forward like an arrow towards amplification or a list. A semicolon acts as an equal balance scales between two independent statements.",
        "golden_rule": "The Independent Anchor Rule: Cover everything after the colon. Does the first part stand alone as a 100% complete sentence? If yes, the colon is legal. If no, remove it.",
        "golden_mnemonic": "COLON = Announcement or Expansion. SEMICOLON = Balance of two equal thoughts.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which sentence uses a colon correctly?", "options": ["A) We require: paper, pens, and toner.", "B) The depot stocks three items: paper, pens, and toner.", "C) Our items include: paper, pens, and toner."], "ans": "B"},
            {"prompt": "2. Choose the correct semicolon between independent clauses:", "options": ["A) The budget is exhausted; therefore, all hiring is frozen.", "B) The budget is exhausted, therefore; all hiring is frozen.", "C) The budget is exhausted; and hiring is frozen."], "ans": "A"},
            {"prompt": "3. Which punctuation belongs in the blank: 'The reason for delay is clear [ ] the supplier declared bankruptcy.'?", "options": ["A) Comma", "B) Colon", "C) Hyphen"], "ans": "B"},
            {"prompt": "4. In a complex list containing internal commas, which mark separates items?", "options": ["A) Commas", "B) Semicolons", "C) Slashes"], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Insert the colon in the correct position: 'The inspection team identified one critical hazard exposed live electrical wiring.'", "hint": "Colon after hazard", "ans": "The inspection team identified one critical hazard: exposed live electrical wiring."},
            {"prompt": "2. Combine using a semicolon: 'The morning seminar was postponed. The afternoon workshop proceeded as planned.'", "hint": "Replace full stop with ;", "ans": "The morning seminar was postponed; the afternoon workshop proceeded as planned."},
            {"prompt": "3. Separate items in this complex list: 'Offices are located in Leeds, Yorkshire Glasgow, Scotland and Cardiff, Wales.'", "hint": "Use semicolons between cities/regions", "ans": "Offices are located in Leeds, Yorkshire; Glasgow, Scotland; and Cardiff, Wales."},
            {"prompt": "4. Correct the colon misuse: 'The essential requirements are: enthusiasm, reliability, and numeracy.'", "hint": "Remove colon or add 'the following'", "ans": "The essential requirements are enthusiasm, reliability, and numeracy. (OR: The position requires the following qualities: enthusiasm, reliability, and numeracy.)"}
        ],
        "ex3": {
            "doc_type": "COUNCIL PLANNING COMMITTEE EXECUTIVE BRIEFING",
            "from_to": "FROM: Head of Strategic Planning | TO: Ward Councillors | DATE: 28 Oct 2026",
            "body": "The committee examined three strategic priorities; affordable housing quotas, renewable energy infrastructure, and flood defences. Progress on housing has accelerated, nevertheless, ground surveys remain incomplete. The development team represents three distinct organisations: Homes England, Bristol City Council, and Wessex Water. One fundamental issue persists the planning inspectorate has not yet approved our environmental impact assessment.",
            "error_count": 4,
            "error_types": "Misused Semicolons & Missing Colons"
        },
        "ex4": {
            "prompt": "You are drafting a 50-word proposal to your department head outlining a new flexible working policy. You must use exactly ONE colon to introduce a list of 3 benefits, and exactly ONE semicolon to join two closely related independent clauses regarding staff productivity and wellbeing.",
            "criteria": ["Formal vocational tone", "1 correct colon introducing list after complete sentence", "1 correct semicolon linking independent clauses", "Accurate spelling and grammar"]
        }
    },

    # UNIT 4
    {
        "unit_num": 4,
        "title": "Apostrophes for Possession & Contraction Mastery",
        "strand": "Punctuation Precision (Ofqual L2.19)",
        "outcome": "Deploy apostrophes faultlessly for singular possession, regular and irregular plural possession, and avoid the notorious 'its vs it's' trap.",
        # Left Page
        "anchor_title": "Human Resources Employee Benefits Policy Guide",
        "anchor_context": "HUMAN RESOURCES / EMPLOYMENT LAW",
        "anchor_text": "An HR intranet update stated: <em>'The company updated it's leave entitlements for all employee's.'</em> In employment law and formal writing, misuse of apostrophes undermines professional credibility and damages exam SPaG scores.",
        "formula_title": "The Possessive & Contraction Matrix",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Singular: The worker's tool (1 worker)"},
            {"cls": "fpill-clause", "text": "Plural in -s: The workers' tools (2+ workers)"},
            {"cls": "fpill-verb", "text": "Irregular Plural: Children's / Women's"},
            {"cls": "fpill-punct", "text": "IT'S = It is / It has | ITS = Possessive"}
        ],
        "formula_desc": "Golden Distinction: 'It's' ONLY ever replaces 'it is' or 'it has'. 'Its' shows possession (just like his, hers, yours). Never use an apostrophe to form a simple plural noun!",
        "compare_bad": "The organisation renewed it's lease, ensuring all client's records were secure.",
        "compare_bad_tag": "INCORRECT 'IT'S' AND PLURAL NOUN APOSTROPHE",
        "compare_good": "The organisation renewed its lease, ensuring all clients' records were secure.",
        "compare_good_tag": "POSSESSIVE PRONOUN (ITS) & PLURAL POSSESSIVE (CLIENTS')",
        "compare_why": "Pronouns showing possession (its, hers, his, theirs, ours) never use apostrophes. Regular plural nouns take an apostrophe AFTER the 's' when showing shared ownership.",
        "golden_rule": "The Substitution Test for 'It's': Whenever you write 'it's', say 'it is' out loud. If 'it is' sounds ridiculous in your sentence, ERASE the apostrophe immediately.",
        "golden_mnemonic": "ITS = Belonging to it. IT'S = IT IS. Simple plural? No apostrophe needed!",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Choose the correct form: 'The committee published [its / it's] findings.'", "options": ["A) its", "B) it's", "C) its'"], "ans": "A"},
            {"prompt": "2. Select the correct plural possessive for all the nurses in the hospital:", "options": ["A) The nurse's station", "B) The nurses' station", "C) The nurses station's"], "ans": "B"},
            {"prompt": "3. Which sentence has no apostrophe errors?", "options": ["A) The womens' locker room was renovated.", "B) The women's locker room was renovated.", "C) The womens locker room's was renovated."], "ans": "B"},
            {"prompt": "4. Identify the correct sentence:", "options": ["A) Two supervisor's attended the conference.", "B) Two supervisors attended the conference.", "C) Two supervisors' attended the conference."], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Rewrite using an apostrophe: 'The vehicles belonging to the paramedics.'", "hint": "Plural paramedics", "ans": "The paramedics' vehicles."},
            {"prompt": "2. Rewrite using an apostrophe: 'The office belonging to James.'", "hint": "James's or James'", "ans": "James's office (or James' office)."},
            {"prompt": "3. Correct the error: 'The clinic lost it's accreditation last November.'", "hint": "Possessive its", "ans": "The clinic lost its accreditation last November."},
            {"prompt": "4. Correct the plural error: 'All trainee's must register before Friday.'", "hint": "Remove apostrophe", "ans": "All trainees must register before Friday."}
        ],
        "ex3": {
            "doc_type": "HUMAN RESOURCES STAFF POLICY BULLETIN",
            "from_to": "FROM: Head of People & Culture | TO: Departmental Leads | DATE: 03 Nov 2026",
            "body": "The company has reviewed it's annual leave policy following feedback from the union's representatives. Under the revised guidelines, all employee's entitlements will accrue on a monthly basis. The directors' decision will take effect next quarter, allowing managers to plan their team's rosters effectively. Please ensure that every apprentice's portfolio is submitted to the assessors' office prior to the Christmas recess.",
            "error_count": 4,
            "error_types": "Apostrophe Misuse (It's/Its, Greengrocer Plural, Misplaced Possession)"
        },
        "ex4": {
            "prompt": "Write a 50-word workplace memorandum clarifying security locker etiquette for employees. You must accurately incorporate: 1) a singular possessive (e.g. employee's padlock), 2) a plural possessive (e.g. supervisors' inspection), and 3) the possessive pronoun 'its' (referring to the facility or locker).",
            "criteria": ["Singular possessive correctly placed", "Plural possessive correctly placed", "Possessive 'its' without apostrophe", "Professional administrative tone"]
        }
    },

    # UNIT 5
    {
        "unit_num": 5,
        "title": "Speech Marks, Direct Quotes & Reported Speech in Reports",
        "strand": "Punctuation & Reporting Conventions (Ofqual L2.19 & L2.20)",
        "outcome": "Punctuate direct witness quotations accurately in professional incident reports and transform them into precise reported speech.",
        # Left Page
        "anchor_title": "Ombudsman Customer Complaint Investigation",
        "anchor_context": "LEGAL & REGULATORY COMPLIANCE",
        "anchor_text": "In a formal incident dossier, an investigator wrote: <em>'The tenant exclaimed, \"the heating has been broken for three weeks\"!'</em> In formal legal and vocational reporting, incorrect placement of quotation marks and internal punctuation discredits evidence.",
        "formula_title": "The Professional Direct Quotation Formula",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Reporting Clause (The witness stated, )"},
            {"cls": "fpill-punct", "text": "Opening Speech Marks [ \" / ' ]"},
            {"cls": "fpill-clause", "text": "Capitalised Direct Statement"},
            {"cls": "fpill-punct", "text": "Internal Punctuation [, . ! ?] + Closing Speech Marks"}
        ],
        "formula_desc": "When quoting direct speech: introduce with a comma, capitalise the first quoted word, and place terminal punctuation INSIDE the closing quotation mark. In reported speech, shift pronouns and backshift tenses.",
        "compare_bad": "The client argued \"we did not agree to this contract\".",
        "compare_bad_tag": "MISSING INTRODUCTORY COMMA & TERMINAL PUNCTUATION OUTSIDE",
        "compare_good": "The client argued, \"We did not agree to this contract.\"",
        "compare_good_tag": "FORMAL REPORTING STANDARD (Comma + Capital + Full Stop Inside)",
        "compare_why": "Quotation marks represent a speech capsule. In standard British functional examination English, the sentence's terminal punctuation sits inside the speech capsule.",
        "golden_rule": "Direct vs Reported Rule: Direct speech needs quotation marks and original spoken words. Reported speech NEVER uses quotation marks and uses 'that' (e.g. The client stated that they had not agreed).",
        "golden_mnemonic": "INSIDE THE BOX: Full stops and commas stay inside quotation marks.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which sentence punctuates direct speech accurately?", "options": ["A) The manager said \"Stock is low\".", "B) The manager said, \"Stock is low.\"", "C) The manager said, \"stock is low\"."], "ans": "B"},
            {"prompt": "2. Identify the correct reported speech equivalent of: 'I will attend the meeting,' said Sarah.", "options": ["A) Sarah said that she would attend the meeting.", "B) Sarah said that \"she will attend the meeting\".", "C) Sarah said that she will attend the meeting."], "ans": "A"},
            {"prompt": "3. Where does the question mark belong: The supervisor asked, \"Are all extinguishers inspected [ ]\"?", "options": ["A) Inside the speech marks", "B) Outside the speech marks", "C) Both inside and outside"], "ans": "A"},
            {"prompt": "4. Does reported speech require speech marks?", "options": ["A) Yes, always", "B) Only for important words", "C) No, never"], "ans": "C"}
        ],
        "ex2": [
            {"prompt": "1. Punctuate this direct quote: The paramedic reported the patient regained consciousness after oxygen was administered.", "hint": "Add comma, quotes, capital letter, full stop inside", "ans": "The paramedic reported, \"The patient regained consciousness after oxygen was administered.\""},
            {"prompt": "2. Convert to reported speech: Officer Reed stated, \"I arrived at the scene at 08:30.\"", "hint": "Shift pronoun and verb to past perfect", "ans": "Officer Reed stated that he had arrived at the scene at 08:30."},
            {"prompt": "3. Convert to direct speech: The customer insisted that she had paid the invoice twice.", "hint": "The customer insisted, \"...\"", "ans": "The customer insisted, \"I paid the invoice twice.\""},
            {"prompt": "4. Correct the punctuation error: \"We are ready to proceed\", the contractor confirmed.", "hint": "Comma goes inside speech marks", "ans": "\"We are ready to proceed,\" the contractor confirmed."}
        ],
        "ex3": {
            "doc_type": "FORMAL INCIDENT INVESTIGATION INTERVIEW TRANSCRIPT",
            "from_to": "CASE: INV-8821 | WITNESS: Security Officer K. Vance | DATE: 10 Nov 2026",
            "body": "When questioned regarding the perimeter breach, Officer Vance responded \"I observed two individuals tampering with the north gate.\" He further stated that, 'the CCTV cameras in Zone 3 were non-functional at the time'. When asked why the emergency siren was not triggered, Vance explained, \"The alarm console indicated a false positive\", so I opted to conduct a manual patrol. Finally, the site supervisor confirmed that \"all gate locks will be replaced immediately\".",
            "error_count": 4,
            "error_types": "Quotation Punctuation & Quotation Marks in Reported Speech"
        },
        "ex4": {
            "prompt": "You are writing a 50-word formal workplace grievance report regarding a dispute between two retail colleagues. You must include exactly ONE direct quote from the store supervisor (punctuated with speech marks and terminal punctuation inside) and ONE sentence of professional reported speech summarizing the customer's perspective.",
            "criteria": ["One direct quote with flawless punctuation", "One reported speech sentence without speech marks", "Objective professional register", "Accurate syntax"]
        }
    },

    # UNIT 6
    {
        "unit_num": 6,
        "title": "Subject-Verb Agreement with Complex & Compound Subjects",
        "strand": "Grammar & Syntactical Concord (Ofqual L2.20)",
        "outcome": "Ensure complete agreement between subjects and verbs when separated by prepositional phrases, collective nouns, or compound correlative structures.",
        # Left Page
        "anchor_title": "Financial Audit & Corporate Governance Advisory",
        "anchor_context": "FINANCIAL SERVICES & COMPLIANCE",
        "anchor_text": "An internal audit lead wrote: <em>'A comprehensive portfolio of capital investment schemes have been deferred.'</em> The auditor mistakenly matched the verb 'have' to the plural noun 'schemes' instead of the true singular subject 'portfolio'.",
        "formula_title": "The Subject-Verb Agreement Concordance Rules",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "True Singular Subject [A portfolio]"},
            {"cls": "fpill-clause", "text": "(of capital schemes) <- IGNORE PREPOSITIONAL PHRASE"},
            {"cls": "fpill-verb", "text": "Singular Verb [has been deferred]"}
        ],
        "formula_desc": "Correlative Rule: With 'either... or' and 'neither... nor', the verb agrees with the subject CLOSEST to it. Collective Nouns (committee, team, board) take singular verbs in formal Functional Skills writing.",
        "compare_bad": "Neither the managing director nor the departmental heads was willing to compromise.",
        "compare_bad_tag": "FAULTY CORRELATIVE AGREEMENT (Verb must agree with closest plural subject)",
        "compare_good": "Neither the managing director nor the departmental heads were willing to compromise.",
        "compare_good_tag": "CORRECT PROXIMITY AGREEMENT ('heads' is plural)",
        "compare_why": "With 'neither/nor', look at the noun right next to the verb. 'Departmental heads' is plural, so the verb must be 'were'. If it were reversed ('Neither the heads nor the director...'), the verb would be 'was'.",
        "golden_rule": "The Bracket Elimination Trick: Cross out any words sitting between commas or prepositions ('along with...', 'as well as...', 'of the files'). Then read the true subject and verb together.",
        "golden_mnemonic": "THE PROXIMITY TEST: Find the true commander of the sentence and ignore the passengers.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Choose the correct verb: 'A delivery of medical supplies [has / have] arrived.'", "options": ["A) has", "B) have"], "ans": "A"},
            {"prompt": "2. Select the correct form: 'Neither the manager nor the assistants [was / were] notified.'", "options": ["A) was", "B) were"], "ans": "B"},
            {"prompt": "3. Which sentence is grammatically correct?", "options": ["A) The team of auditors are presenting their report.", "B) The team of auditors is presenting its report.", "C) The team of auditors were presenting."], "ans": "B"},
            {"prompt": "4. Select the matching verb: 'The technician, together with two apprentices, [is / are] inspecting the boiler.'", "options": ["A) is", "B) are"], "ans": "A"}
        ],
        "ex2": [
            {"prompt": "1. Correct the verb: 'The list of candidate qualifications are enclosed with the application.'", "hint": "Subject is 'The list'", "ans": "The list of candidate qualifications is enclosed with the application."},
            {"prompt": "2. Correct the verb: 'Either the lead consultant or the client have signed the deed.'", "hint": "Client is singular", "ans": "Either the lead consultant or the client has signed the deed."},
            {"prompt": "3. Complete with 'is' or 'are': 'Every one of the fire extinguishers ______ inspected annually.'", "hint": "'Every one' is singular", "ans": "Every one of the fire extinguishers is inspected annually."},
            {"prompt": "4. Complete with 'was' or 'were': 'The quality of the refurbished components ______ satisfactory.'", "hint": "'Quality' is singular", "ans": "The quality of the refurbished components was satisfactory."}
        ],
        "ex3": {
            "doc_type": "INTERNAL COMPLIANCE AUDIT MEMORANDUM",
            "from_to": "FROM: Chief Compliance Officer | TO: Executive Board | DATE: 17 Nov 2026",
            "body": "A thorough evaluation of clinical procedures indicate that significant training deficits remain in Oncology. Neither the head of nursing nor the clinical practice facilitators was aware of the new triage software update. Furthermore, the committee have determined that emergency protocols requires immediate restructuring. A series of remedial workshops, along with an updated digital handbook, is scheduled to launch next Monday.",
            "error_count": 4,
            "error_types": "Subject-Verb Agreement Errors (Intervening phrases, Correlative, Collective nouns)"
        },
        "ex4": {
            "prompt": "You are writing a 50-word formal email update to your operations manager detailing stock discrepancies. You must construct at least two sentences featuring complex subjects: one using a singular subject with an intervening prepositional phrase ('A container of spare parts...'), and one using 'Neither [singular] nor [plural]...'.",
            "criteria": ["Singular subject agreement with intervening phrase", "Correlative 'neither... nor' agreement", "Professional workplace register", "Accurate spelling and syntax"]
        }
    },

    # UNIT 7
    {
        "unit_num": 7,
        "title": "Tense Consistency & Chronological Sequencing",
        "strand": "Grammar & Temporal Cohesion (Ofqual L2.20)",
        "outcome": "Maintain unbroken tense consistency across paragraphs and utilise past perfect, past simple, and present tenses with chronological precision.",
        # Left Page
        "anchor_title": "Residential Care Home Clinical Incident Review",
        "anchor_context": "HEALTH & SOCIAL CARE",
        "anchor_text": "In a medication review, a senior care worker wrote: <em>'The resident fell in the corridor, so the nurse immediately attends to her and called the doctor.'</em> Slipping randomly between past ('fell', 'called') and present ('attends') disorients readers and fails exam criteria.",
        "formula_title": "The Chronological Tense Continuum",
        "formula_pills": [
            {"cls": "fpill-punct", "text": "1. Past Perfect (had occurred) - Earliest Event"},
            {"cls": "fpill-clause", "text": "2. Past Simple (occurred / intervened) - Main Incident"},
            {"cls": "fpill-subj", "text": "3. Present Simple (remains / reports) - Current Status"}
        ],
        "formula_desc": "Maintain the governing tense established in your opening sentence. Only shift tenses when signaling a genuine change in chronological time.",
        "compare_bad": "When the supervisor arrived at the loading bay, he notices that three crates were broken.",
        "compare_bad_tag": "ILLEGITIMATE TENSE SHIFT (arrived [past] -> notices [present])",
        "compare_good": "When the supervisor arrived at the loading bay, he noticed that three crates were broken.",
        "compare_good_tag": "CONSISTENT HISTORICAL PAST TENSE",
        "compare_why": "Both events occurred simultaneously in the past. Slipping into the present tense creates jarring narrative friction and costs valuable SPaG marks.",
        "golden_rule": "The Time Anchor Check: Identify your anchor verb in sentence 1. Underline every subsequent verb. If an action happened in the same timeframe, its verb tense MUST match your anchor verb.",
        "golden_mnemonic": "STAY IN TIME: If the story started yesterday, do not speak as if it is happening now.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which sentence contains an unjustified tense shift?", "options": ["A) The technician opened the casing and examined the circuit.", "B) The technician opened the casing and examines the circuit.", "C) The technician opens the casing and examines the circuit."], "ans": "B"},
            {"prompt": "2. Select the sentence that uses past perfect correctly for the earlier action:", "options": ["A) By the time police arrived, the suspects fled.", "B) By the time police arrived, the suspects had fled.", "C) By the time police arrive, the suspects had fled."], "ans": "B"},
            {"prompt": "3. Identify the correct verb form: 'Last year we expanded our fleet; today we [operate / operated] 50 vans.'", "options": ["A) operate", "B) operated"], "ans": "A"},
            {"prompt": "4. Complete consistently: 'The customer paid the bill and [leaves / left] the counter.'", "options": ["A) leaves", "B) left"], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Eliminate the tense shift: 'The nurse took the blood pressure reading and inputs the figures into the database.'", "hint": "Change inputs to past tense", "ans": "The nurse took the blood pressure reading and inputted (or entered) the figures into the database."},
            {"prompt": "2. Correct the timeline: 'Before the inspection began, the team already prepared the safety dossiers.'", "hint": "Earlier action requires past perfect 'had prepared'", "ans": "Before the inspection began, the team had already prepared the safety dossiers."},
            {"prompt": "3. Make consistent in the present tense: 'The company provides training and supported all new apprentices.'", "hint": "Change supported to supports", "ans": "The company provides training and supports all new apprentices."},
            {"prompt": "4. Align the tenses: 'She unlocked the laboratory, turns on the ventilation, and checked the temperature.'", "hint": "Change turns to turned", "ans": "She unlocked the laboratory, turned on the ventilation, and checked the temperature."}
        ],
        "ex3": {
            "doc_type": "CARE FACILITY SHIFT HANDOVER REPORT",
            "from_to": "FACILITY: Meadowbrook Care Home | WARD: Pine Unit | DATE: 24 Nov 2026",
            "body": "At 06:30, Care Assistant Miller visited Room 12 and finds Resident Arthur experiencing mild shortness of breath. Miller immediately alerted the duty sister, who administers supplementary oxygen. By the time the GP arrived at 07:15, the resident's oxygen saturation levels stabilised significantly. The resident now rests comfortably in bed and had requested a light breakfast.",
            "error_count": 4,
            "error_types": "Inconsistent Past/Present Tense Shifts & Past Perfect Misalignment"
        },
        "ex4": {
            "prompt": "You are writing a 50-word formal incident log describing a water pipe burst in a commercial kitchen yesterday morning. You must write strictly in the past tense to describe what happened, what action staff took, and conclude with one present-tense sentence describing the kitchen's current condition.",
            "criteria": ["Flawless past tense for past events", "Accurate past perfect for earlier cause", "Legitimate present tense shift for current status", "Professional incident tone"]
        }
    },

    # UNIT 8
    {
        "unit_num": 8,
        "title": "Pronoun Precision, Relative Clauses & Eliminating Ambiguity",
        "strand": "Grammar, Pronoun Reference & Cohesion (Ofqual L2.20)",
        "outcome": "Deploy subject and object pronouns accurately, distinguish 'who vs whom', and eliminate ambiguous antecedents that obscure meaning.",
        # Left Page
        "anchor_title": "IT Cyber Security & Incident Protocol Advisory",
        "anchor_context": "INFORMATION TECHNOLOGY / DATA COMPLIANCE",
        "anchor_text": "An IT technician reported: <em>'When the user plugged the external hard drive into the workstation, it crashed.'</em> What crashed—the hard drive or the workstation? Ambiguous pronoun reference creates confusion in technical documentation.",
        "formula_title": "The Pronoun Case & Antecedent Architecture",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Subject: I, he, she, they, WHO (Does the action)"},
            {"cls": "fpill-punct", "text": "vs"},
            {"cls": "fpill-verb", "text": "Object: me, him, her, them, WHOM (Receives action)"},
            {"cls": "fpill-clause", "text": "Preposition + Object: Between you and ME (not I)"}
        ],
        "formula_desc": "Rule 1: Every pronoun must link unmistakably to ONE antecedent noun. Rule 2: Use 'who' where you could substitute 'he/she/they'; use 'whom' where you could substitute 'him/her/them'.",
        "compare_bad": "Confidential details were shared between Mr Henderson and I during the audit.",
        "compare_bad_tag": "INCORRECT SUBJECT PRONOUN AFTER PREPOSITION ('BETWEEN')",
        "compare_good": "Confidential details were shared between Mr Henderson and me during the audit.",
        "compare_good_tag": "ACCURATE OBJECT PRONOUN ('BETWEEN ... AND ME')",
        "compare_why": "'Between' is a preposition. Prepositions govern object pronouns (me, him, her, us, them). Saying 'between you and I' is a common hypercorrection that examiners penalise.",
        "golden_rule": "The He/Him Shortcut for Who/Whom: Ask: 'Does HE do it, or did someone do it to HIM?' If HE = WHO. If HIM = WHOM (notice both end with M: hiM = whoM).",
        "golden_mnemonic": "CLEAR ANTECEDENT: If 'it' could mean two different nouns, name the noun directly.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which pronoun is correct: 'The employee [who / whom] submitted the claim has resigned.'?", "options": ["A) who", "B) whom"], "ans": "A"},
            {"prompt": "2. Choose the correct form: 'To [who / whom] should the invoice be forwarded?'", "options": ["A) who", "B) whom"], "ans": "B"},
            {"prompt": "3. Select the correct pronoun: 'The committee awarded the bursary to Priya and [I / me].'", "options": ["A) I", "B) me"], "ans": "B"},
            {"prompt": "4. Identify the sentence free of ambiguous pronouns:", "options": ["A) As the lorry struck the bollard, it broke.", "B) The bollard broke when the lorry struck it.", "C) The lorry struck the bollard, and it was damaged."], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Resolve the ambiguity: 'The supervisor informed the apprentice that he had passed the safety test.'", "hint": "Clarify who passed", "ans": "The supervisor informed the apprentice: \"You have passed the safety test.\" (OR: The supervisor confirmed that the apprentice had passed the safety test.)"},
            {"prompt": "2. Correct the pronoun: 'Between you and I, the proposed merger will face regulatory challenges.'", "hint": "Use object pronoun me", "ans": "Between you and me, the proposed merger will face regulatory challenges."},
            {"prompt": "3. Correct who/whom: 'The contractor who we hired last month has exceeded performance targets.'", "hint": "We hired him -> whom", "ans": "The contractor whom we hired last month has exceeded performance targets."},
            {"prompt": "4. Complete with 'who' or 'whom': 'Candidates ______ meet the minimum criteria will be shortlisted.'", "hint": "They meet the criteria -> who", "ans": "Candidates who meet the minimum criteria will be shortlisted."}
        ],
        "ex3": {
            "doc_type": "CYBER SECURITY DATA BREACH NOTIFICATION",
            "from_to": "FROM: Data Protection Officer | TO: IT Security Steering Committee | DATE: 01 Dec 2026",
            "body": "On Thursday afternoon, a system administrator discovered unauthorized login attempts targeting customer databases. The administrator alerted the Chief Technology Officer whom immediately severed the external firewall connection. Disciplinary proceedings have commenced regarding the employee which neglected two-factor authentication protocols. Between you and I, the forensic analysts whom inspected the audit logs believe customer records were compromised before they could isolate the server.",
            "error_count": 4,
            "error_types": "Misused Relative Pronouns (Who/Whom/Which) & Ambiguous Pronoun Reference"
        },
        "ex4": {
            "prompt": "Write a 50-word formal workplace email to human resources recommending an administrative colleague for a specialist training course. You must use 'whom' correctly (e.g., 'a colleague whom I hold in high regard') and use 'between [Name] and me' accurately without any pronoun ambiguity.",
            "criteria": ["Accurate use of 'whom'", "Accurate use of '... and me' as object", "Zero ambiguous pronouns", "Professional vocational recommendation"]
        }
    },

    # UNIT 9
    {
        "unit_num": 9,
        "title": "Formal Register, Professional Vocabulary & Tone",
        "strand": "Register, Audience & Tone (Ofqual L2.21 & L2.22)",
        "outcome": "Write with an authoritative, measured, and objective formal register, eliminating colloquialisms, emotive slang, and inappropriate contractions.",
        # Left Page
        "anchor_title": "Corporate Grievance & Client Appeal Response",
        "anchor_context": "COMMERCIAL DISPUTE RESOLUTION",
        "anchor_text": "An operations manager responded to a formal customer complaint: <em>'We're really gutted about the massive mess-up with your goods and will sort it ASAP.'</em> Emotive slang, colloquial phrasing, and informal contractions destroy commercial credibility in Level 2 writing.",
        "formula_title": "The Formal Register Lexical Transformation Matrix",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Informal / Slang: 'sort it out' -> 'resolve the matter'"},
            {"cls": "fpill-verb", "text": "Emotive: 'gutted / outraged' -> 'regret / dispute'"},
            {"cls": "fpill-punct", "text": "Contractions: 'can't / won't' -> 'cannot / will not'"},
            {"cls": "fpill-clause", "text": "Nominalisation: 'decide' -> 'reach a determination'"}
        ],
        "formula_desc": "Formal vocational writing is characterised by objective statements, precise vocabulary, passive or impersonal constructions where appropriate, and the absence of conversational shortcuts.",
        "compare_bad": "The boss told us to chuck away the old files coz they're rubbish.",
        "compare_bad_tag": "INAPPROPRIATE COLLOQUIAL SLANG & CONTRACTIONS",
        "compare_good": "The managing director instructed staff to archive obsolete files in line with retention policy.",
        "compare_good_tag": "OBJECTIVE, AUTHORITATIVE VOCATIONAL VOCABULARY",
        "compare_why": "Functional Level 2 examiners assess whether your tone matches the intended audience. In workplace reports, emails to directors, and formal articles, standard English is non-negotiable.",
        "golden_rule": "The Chief Executive Test: Imagine your document being read aloud in an employment tribunal or board meeting. If any phrase sounds like casual street conversation, replace it with formal terminology.",
        "golden_mnemonic": "EXPAND & ELEVATE: Expand contractions (do not) and elevate everyday verbs to professional equivalents.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which option provides the formal equivalent of 'look into the problem'?", "options": ["A) check out the mess", "B) investigate the matter", "C) sort out the hassle"], "ans": "B"},
            {"prompt": "2. Select the sentence with an appropriately formal register:", "options": ["A) The team delivered a sub-par performance and dropped the ball.", "B) The department failed to achieve its targeted performance milestones.", "C) We messed up big time on the sales targets."], "ans": "B"},
            {"prompt": "3. Which word should replace 'kids' in a formal nursery inspection report?", "options": ["A) youngsters", "B) children / infants", "C) little ones"], "ans": "B"},
            {"prompt": "4. Are contractions (don't, can't, it's) appropriate in formal Functional Skills Level 2 letters of complaint?", "options": ["A) Yes, always", "B) No, write them out in full", "C) Only in the introduction"], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Elevate to formal register: 'We're writing to tell you that the event is off coz of bad weather.'", "hint": "Use 'We are writing to notify you...', 'cancelled due to adverse conditions'", "ans": "We are writing to inform you that the event has been cancelled due to adverse weather conditions."},
            {"prompt": "2. Replace colloquial words: 'The firm got a lot of cash from the council.'", "hint": "Acquired / secured substantial funding", "ans": "The firm secured substantial grant funding from the municipal council."},
            {"prompt": "3. Remove conversational tone: 'You guys need to get your act together about safety.'", "hint": "All personnel must adhere strictly to safety protocols", "ans": "All personnel must adhere strictly to established safety protocols."},
            {"prompt": "4. Eliminate contractions and slang: 'Management won't put up with staff slacking off.'", "hint": "Management will not tolerate unauthorised absenteeism", "ans": "Management will not tolerate non-compliance or poor productivity."}
        ],
        "ex3": {
            "doc_type": "FORMAL CLIENT RESOLUTION CORRESPONDENCE",
            "from_to": "REF: COMP-7712 | RE: CATERING CONTRACT DISPUTE | DATE: 08 Dec 2026",
            "body": "Dear Mr Thorne, We're getting in touch about the recent mess-up at your annual banquet. We were totally gutted to hear that the hot food was stone cold and that our waiting staff acted like total amateurs. Management has had a huge row with the kitchen supplier to sort out why the ovens broke down. We're gonna give you a massive refund to make up for the hassle. Yours sincerely, Apex Corporate Hospitality.",
            "error_count": 5,
            "error_types": "Informal Slang, Contractions & Unprofessional Emotive Register"
        },
        "ex4": {
            "prompt": "You are writing a 50-word formal letter on behalf of an estate management firm to a commercial tenant whose lease has expired. You must use an elevated, professional register with zero contractions, outlining that the premises must be vacated and inspected before deposit return.",
            "criteria": ["Zero contractions", "Elevated professional vocabulary", "Authoritative, courteous tone", "Flawless sentence boundaries"]
        }
    },

    # UNIT 10
    {
        "unit_num": 10,
        "title": "Cohesive Discourse Markers & Advanced Formatting",
        "strand": "Organisational Markers & Cohesion (Ofqual L2.21 & L2.23)",
        "outcome": "Use sophisticated transitional discourse markers, bulleted hierarchies, and structural signposts to guide readers logically through complex arguments.",
        # Left Page
        "anchor_title": "Facility Management Sustainable Energy Reduction Strategy",
        "anchor_context": "ENVIRONMENTAL MANAGEMENT & OPERATIONS",
        "anchor_text": "In a boardroom proposal, a sustainability coordinator wrote: <em>'Solar panels will reduce daytime consumption. And also we can install LED bulbs. Plus staff should turn monitors off.'</em> Childish connectives ('And also', 'Plus') fail to build a convincing executive business case.",
        "formula_title": "The Logical Discourse Hierarchy",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "Addition: Furthermore, / Additionally, / In addition,"},
            {"cls": "fpill-punct", "text": "Contrast: Conversely, / However, / Nevertheless,"},
            {"cls": "fpill-verb", "text": "Causation: Consequently, / Therefore, / Accordingly,"},
            {"cls": "fpill-clause", "text": "PUNCTUATION: Discourse Marker + COMMA + Main Clause"}
        ],
        "formula_desc": "Transitional adverbs link ideas across sentence boundaries. They must be punctuated with a comma when opening a sentence, or enclosed in semicolons and commas when bridging clauses.",
        "compare_bad": "The capital outlay is substantial however the long-term energy savings will offset costs.",
        "compare_bad_tag": "MISSING PUNCTUATION AROUND CONJUNCTIVE ADVERB",
        "compare_good": "The capital outlay is substantial; however, the long-term energy savings will offset costs.",
        "compare_good_tag": "ACCURATELY BRIDGED WITH SEMICOLON AND COMMA",
        "compare_why": "'However' is an adverb, not a conjunction. To connect two sentences with 'however', you need a semicolon before it and a comma after it, or start a new sentence.",
        "golden_rule": "The Variety Rule: Do not repeat 'Furthermore' or 'However' three times in the same document. Deploy varied discourse markers to signal distinct logical relationships (concession, addition, result).",
        "golden_mnemonic": "SIGNPOST YOUR LOGIC: Tell the reader whether you are adding, contrasting, or concluding.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which discourse marker correctly introduces a contrasting counter-argument?", "options": ["A) Furthermore,", "B) Conversely,", "C) Additionally,"], "ans": "B"},
            {"prompt": "2. Choose the correct punctuation for 'therefore':", "options": ["A) Costs rose, therefore, prices increased.", "B) Costs rose; therefore, prices increased.", "C) Costs rose therefore; prices increased."], "ans": "B"},
            {"prompt": "3. Which marker indicates a causal consequence?", "options": ["A) Subsequently,", "B) Consequently,", "C) Alternatively,"], "ans": "B"},
            {"prompt": "4. Is a comma required after 'In conclusion' when introducing a closing sentence?", "options": ["A) Yes, always", "B) No, never", "C) Only in informal texts"], "ans": "A"}
        ],
        "ex2": [
            {"prompt": "1. Connect these contrasting sentences using '; however,': 'Staff turnover increased. Customer satisfaction remained high.'", "hint": "Use semicolon and comma", "ans": "Staff turnover increased; however, customer satisfaction remained high."},
            {"prompt": "2. Insert a formal connective of addition: 'The new machinery boosts output. [______], it lowers noise pollution.'", "hint": "Furthermore, / Additionally,", "ans": "The new machinery boosts output. Furthermore, it lowers noise pollution."},
            {"prompt": "3. Connect with a marker of result: 'The audit identified multiple non-compliance issues. [______], the accreditation was suspended.'", "hint": "Consequently, / As a result,", "ans": "The audit identified multiple non-compliance issues. Consequently, the accreditation was suspended."},
            {"prompt": "4. Punctuate properly: 'Moreover the facility failed its statutory legionella test.'", "hint": "Add comma after moreover", "ans": "Moreover, the facility failed its statutory legionella test."}
        ],
        "ex3": {
            "doc_type": "SUSTAINABILITY COMMITTEE STRATEGIC POLICY PAPER",
            "from_to": "FROM: Green Transition Officer | TO: Executive Leadership | DATE: 15 Dec 2026",
            "body": "The installation of automated LED sensor lighting across all warehouse bays has yielded impressive results. Energy consumption fell by 22% during Q3, however initial maintenance costs exceeded projections. Plus several sensors suffered calibration faults during high-temperature periods. Consequently technical teams will conduct weekly inspections. In addition to this all site personnel will receive revised energy conservation briefings next month.",
            "error_count": 4,
            "error_types": "Misused Connectives ('Plus'), Missing Commas & Semicolons with Transitional Adverbs"
        },
        "ex4": {
            "prompt": "You are writing a 50-word proposal to your company's senior leadership arguing for the introduction of electric delivery vans. You must use at least THREE distinct discourse markers (one of contrast, one of addition, and one of result) punctuated with flawless commas.",
            "criteria": ["1 contrast marker (e.g. However, / Conversely,)", "1 addition marker (e.g. Furthermore, / In addition,)", "1 result marker (e.g. Consequently, / Therefore,)", "Professional executive style"]
        }
    },

    # UNIT 11
    {
        "unit_num": 11,
        "title": "Advanced Homophones, Confusable Words & Proofreading Traps",
        "strand": "Spelling, Lexical Precision & Proofreading (Ofqual L2.20 & L2.24)",
        "outcome": "Differentiate and spell advanced workplace homophones faultlessly (affect/effect, practice/practise, principal/principle, complement/compliment).",
        # Left Page
        "anchor_title": "Legal Contracts & Commercial Procurement Audit",
        "anchor_context": "COMMERCIAL CONTRACTS & LAW",
        "anchor_text": "A procurement manager drafted a supplier agreement: <em>'The new regulatory changes will drastically effect our company's daily legal practise.'</em> Confusing 'effect' with 'affect', and 'practise' with 'practice', creates embarrassing legal and exam errors.",
        "formula_title": "The Golden Homophone Demystifier",
        "formula_pills": [
            {"cls": "fpill-subj", "text": "AFFECT = Verb (to influence) | EFFECT = Noun (the result)"},
            {"cls": "fpill-verb", "text": "-CE = Noun (Practice, Advice, Device, Licence)"},
            {"cls": "fpill-punct", "text": "-SE = Verb (Practise, Advise, Devise, License)"},
            {"cls": "fpill-clause", "text": "PRINCIPLE = Rule/Value | PRINCIPAL = Head/Main/Capital"}
        ],
        "formula_desc": "The 'RAVEN' Rule: Remember: Affect is Verb, Effect is Noun. The 'Ice/Is' Rule: Nouns have 'ice' (advice, practice); verbs have 'ise' (advise, practise).",
        "compare_bad": "We complement the team on adhering to strict ethical principals.",
        "compare_bad_tag": "CONFUSED COMPLIMENT/COMPLEMENT & PRINCIPLE/PRINCIPAL",
        "compare_good": "We compliment the team on adhering to strict ethical principles.",
        "compare_good_tag": "PRAISE (COMPLIMENT) & MORAL RULES (PRINCIPLES)",
        "compare_why": "'Compliment' with an 'i' means praise ('I like your work'). 'Complement' with an 'e' means to complete or match well. 'Principles' are core values; a 'principal' is the school head or primary sum.",
        "golden_rule": "The Replacement Test: When stuck between 'affect' and 'effect', replace the word with 'influence' or 'result'. If 'influence' fits, choose AFFECT. If 'result' fits, choose EFFECT.",
        "golden_mnemonic": "RAVEN: R-Affect-Verb-Effect-Noun. ICE is a NOUN: AdvICE, PractICE, DevICE.",
        # Right Page Drills
        "ex1": [
            {"prompt": "1. Which word completes: 'The new taxation policy will greatly [affect / effect] small businesses.'?", "options": ["A) affect", "B) effect"], "ans": "A"},
            {"prompt": "2. Choose the correct noun: 'All dental staff must follow standard infection control [practice / practise].'", "options": ["A) practice", "B) practise"], "ans": "A"},
            {"prompt": "3. Which word means core moral rule: 'He refused on [principal / principle]'?", "options": ["A) principal", "B) principle"], "ans": "B"},
            {"prompt": "4. Complete: 'Wine and cheese [compliment / complement] each other.'", "options": ["A) compliment", "B) complement"], "ans": "B"}
        ],
        "ex2": [
            {"prompt": "1. Select affect or effect: 'The economic downturn had an immediate ______ on sales.'", "hint": "Preceded by 'an' -> noun", "ans": "effect"},
            {"prompt": "2. Select advice or advise: 'Legal counsel will ______ the board tomorrow morning.'", "hint": "Doing an action -> verb", "ans": "advise"},
            {"prompt": "3. Select site, sight, or cite: 'The engineer inspected the construction ______ at dawn.'", "hint": "Physical location", "ans": "site"},
            {"prompt": "4. Select stationery or stationary: 'The delivery vehicle remained ______ while in queue.'", "hint": "Stationary = not moving", "ans": "stationary"}
        ],
        "ex3": {
            "doc_type": "COMMERCIAL SUPPLIER AGREEMENT MEMORANDUM",
            "from_to": "FROM: Senior Procurement Officer | TO: Corporate Finance Director | DATE: 20 Dec 2026",
            "body": "Following our recent tender review, we advise that the selected contractor will complementary our existing facilities team. The principal principle guiding our choice was value for money. Although supply chain disruptions may temporarily effect delivery timescales, we do not anticipate any adverse affect on statutory operations. All staff must now put the new safety practises into daily practice.",
            "error_count": 6,
            "error_types": "Confused Homophones (Complement/Compliment, Principal/Principle, Affect/Effect, Practise/Practice)"
        },
        "ex4": {
            "prompt": "Write a 50-word formal procurement recommendation email endorsing a chosen software vendor. You must correctly incorporate: 1) 'affect' (as a verb), 2) 'effect' (as a noun), 3) 'practice' (as a noun), and 4) 'principles' (as ethical standards).",
            "criteria": ["Accurate use of affect (verb)", "Accurate use of effect (noun)", "Accurate use of practice (noun)", "Accurate use of principles (noun)", "Flawless sentence syntax"]
        }
    }
]

L2_SPELLING_PAGE_1 = {
    "title": "Master Spelling Rules & High-Yield Word Architecture",
    "subtitle": "Essential morphological rules and orthographic conventions for Level 2 Functional English examinations.",
    "rules": [
        {
            "num": 1,
            "name": "The 'I before E except after C' Rule & Its Exceptions",
            "explanation": "Use 'i' before 'e' when sounding like /ee/ (believe, relief, yield), except after the letter 'c' (receive, ceiling, receipt, deceit).",
            "exceptions": "Key Exam Exceptions: weird, seize, forfeit, leisure, protein, caffeine, science, conscience.",
            "examples": "Correct: achieve, believe, receive, deceit. Trap: *recieve (WRONG), *beleive (WRONG)."
        },
        {
            "num": 2,
            "name": "The Consonant Doubling Rule (1-1-1 Pattern)",
            "explanation": "Double the final consonant before a vowel suffix (-ed, -ing, -er) if the word has 1 syllable, ends in 1 consonant preceded by 1 single vowel (stop -> stopped, plan -> planned). In multi-syllable words, only double if the stress is on the final syllable (refer -> referred, occur -> occurred, BUT benefit -> benefited).",
            "exceptions": "British English doubles 'l' after a short vowel regardless of stress: travel -> travelled, cancel -> cancelled.",
            "examples": "Correct: beginning, occurring, submitted. Trap: *prefered (WRONG - must be preferred)."
        },
        {
            "num": 3,
            "name": "Dropping or Keeping the Silent 'E'",
            "explanation": "Drop the final silent 'e' when adding a suffix beginning with a vowel (hope -> hoping, write -> writing, sense -> sensible). Keep the 'e' when adding a suffix beginning with a consonant (hope -> hopeful, manage -> management).",
            "exceptions": "Keep 'e' after soft 'c' or 'g' to preserve soft sound before -able/-ous: noticeable, manageable, courageous.",
            "examples": "Correct: truly (drops 'e' from true), definitely, argument (drops 'e' from argue)."
        },
        {
            "num": 4,
            "name": "Changing 'Y' to 'I'",
            "explanation": "If a word ends in a consonant + 'y', change 'y' to 'i' before any suffix except -ing (apply -> applies / applied / application; rely -> reliable). If preceded by a vowel, keep the 'y' (play -> played).",
            "exceptions": "Keep 'y' before -ing to prevent double 'i': hurry -> hurrying, cry -> crying.",
            "examples": "Correct: business (from busy), necessary, thoroughly, unaccompanied."
        }
    ]
}

L2_SPELLING_PAGE_2 = {
    "title": "High-Yield Vocational Exam Vocabulary & Spelling Drills",
    "subtitle": "40 Essential words frequently penalised by Pearson Edexcel, City & Guilds, and NCFE examiners.",
    "word_bank": [
        {"word": "Accommodate", "trap": "Double 'c' and double 'm'", "tip": "Needs two cots and two mattresses"},
        {"word": "Recommendation", "trap": "Single 'c', double 'm'", "tip": "One coffee, two muffins"},
        {"word": "Necessary", "trap": "One 'c', double 's'", "tip": "One collar, two sleeves"},
        {"word": "Disciplinary", "trap": "Single 's', ends in -ary", "tip": "Linked to disciple"},
        {"word": "Privilege", "trap": "Ends in -ege, no 'd'", "tip": "Never write *priviledge"},
        {"word": "Definite", "trap": "Contains 'finite' (no 'a')", "tip": "Never write *definate"},
        {"word": "Separate", "trap": "Contains 'a rat'", "tip": "There is a rat in sep-a-rate"},
        {"word": "Liaison", "trap": "Two 'i's: l-i-a-i-s-o-n", "tip": "Keep the double 'i' on both sides of 'a'"},
        {"word": "Embarrassment", "trap": "Double 'r', double 's'", "tip": "Two red faces, two shy grins"},
        {"word": "Maintenance", "trap": "Main-TEN-ance (not maintain)", "tip": "Spelled with 'ten' in the middle"},
        {"word": "Independent", "trap": "Ends in -ent (not -ant)", "tip": "All 'e's after the 'p'"},
        {"word": "Environment", "trap": "Do not omit silent 'n'", "tip": "En-vi-ron-ment"}
    ],
    "drill_text": "The managing directer made a recomendation to accomodate all fourty contractors at the conference. It was nescessary to seperate the disciplinary records to maintain full confidentiallity. The operational envirnment requires definate commitments from all personnel to ensure privelege and safety standards are up held.",
    "drill_errors_count": 8
}

L2_MOCK_TASK_1 = {
    "title": "Mixed Exam Proofreading Mock: Task 1 (6 Marks)",
    "subtitle": "Realistic Pearson / City & Guilds Calibrated Functional Workplace Scenario",
    "scenario_title": "ESTATE SERVICES STATUTORY HEALTH & SAFETY INSPECTION REPORT",
    "context": "You are an assistant facilities inspector reviewing an urgent compliance briefing. The draft below contains exactly 6 deliberate SPaG errors (2 punctuation errors, 2 spelling errors, and 2 grammatical agreement/tense errors). Identify and correct all 6 errors in the correction table provided.",
    "doc_meta": "REPORT REF: H&S-L2-2026 | INSPECTOR: Marcus Vance | SITE: Central Logistics Depot",
    "text": "During the statutory inspection of Loading Bay 3, the facilities team identified several urgent hazards, the emergency exit door was obstructed by discarded pallets. A comprehensive range of chemical spill kits were missing from their designated storage stations. Maintenance personnel had begun structural repairs yesterday however, they failed to cordon off the perimeter. Consequently all warehouse operatives was exposed to trip hazards. It is vital that the company updates it's emergency response procedures immediately. Management must seperate hazardous waste containers before statutory re-inspection on Monday.",
    "marks": 6
}

L2_MOCK_TASK_2 = {
    "title": "Mixed Exam Proofreading Mock: Task 2 (6 Marks)",
    "subtitle": "Formal Client Resolution & Policy Document Rewrite",
    "scenario_title": "EXECUTIVE APOLOGY & DISPUTE RESOLUTION CORRESPONDENCE",
    "context": "The draft client letter below contains exactly 6 deliberate SPaG errors (spelling, comma splice, pronoun case, apostrophe, tense, and homophone). Identify the errors and produce a fully corrected, publication-grade rewrite in the lines below.",
    "doc_meta": "CORRESPONDENCE: Formal Letter | TO: Dr Aris Thorne | RE: Contract Non-Compliance",
    "text": "Dear Dr Thorne, We are writing to formally apologise for the delay in completing your clinic's refurbishment. Between you and I, the initial survey was deficient, the project manager failed to identify asbestos in the ceiling tiles. Although the specialist contractors arrived promptly last Tuesday they was unable to proceed without secondary certification. This had an adverse affect on the completion timeline. The company will accomodate your staff in temporary consulting suites and compensate all direct losses. Yours sincerely, Premier Build Solutions.",
    "marks": 6
}

L2_ANSWERS = {
    "page_31": {
        "title": "Complete Answer Key: Diagnostic Assessment & Units 1 to 3",
        "diagnostic": [
            "1. B (Semicolon joins independent clauses)",
            "2. B (Comma after fronted subordinate clause)",
            "3. B (Colon follows complete independent clause)",
            "4. D (Possessive 'its' has no apostrophe; 'directors'' is plural possessive)",
            "5. A (Direct quote introduced with comma, capital letter, full stop inside)",
            "6. C (Verb agrees with singular subject 'lead surgeon')",
            "7. B (Consistent past simple: complained, stepped, offered)",
            "8. B (Eliminates pronoun ambiguity by naming the doctor)",
            "9. C (Objective, formal register without slang or contractions)",
            "10. B (Affect = verb; practice = noun)"
        ],
        "unit_1": {
            "ex1": "1: B (Comma splice) | 2: B (Semicolon + transition) | 3: B (Semicolon or , and) | 4: B (, and)",
            "ex2": "1. The fire drill began at 10:00; staff assembled in Zone A. | 2. Budget cuts were announced, but the project continued. | 3. The client rejected the proposal. They requested alterations. | 4. Deliveries were halted; consequently, suppliers were notified.",
            "ex3": "Errors found (4 Comma Splices corrected): 1) Substation B; the primary... (or . The) | 2) at 03:15; he isolated... (or . He) | 3) for two hours; customer orders... (or , and customer) | 4) equipment warranty; we must decide... (or . We)",
            "ex4_model": "Yesterday afternoon, a chemical spill drill was conducted in the main laboratory; all safety officers evacuated within three minutes. Emergency showers were activated immediately, and decontamination teams isolated the simulated acid safely. To prevent future incidents, chemical containers must always be secured in secondary containment bunds."
        },
        "unit_2": {
            "ex1": "1: A (Fronted infinitive) | 2: B (Non-defining relative clause enclosed in commas) | 3: B (After 'conditions') | 4: B (Main clause first)",
            "ex2": "1. To ensure maximum compliance, all employees must complete the GDPR module. | 2. The new regional depot, which cost £2.4 million, will open in November. | 3. The director, however, refused to authorise the expenditure. | 4. When the fire alarm sounds, operatives must assemble in Car Park B.",
            "ex3": "Errors found (5 missing commas): 1) ...cold-storage facility, operatives... | 2) ...safety manual, forklift operators... | 3) Mr Higgins, who inspects vehicle hoists, found... (2 commas) | 4) Consequently, all affected loading bays... | 5) If an emergency occurs, press...",
            "ex4_model": "Due to unexpected motorway resurfacing on the M62, several scheduled delivery consignments experienced severe transit delays this morning. Although drivers identified alternative arterial routes, heavy congestion persisted across the industrial sector. Transport dispatchers have contacted affected clients, and all pending orders will arrive by 17:00."
        },
        "unit_3": {
            "ex1": "1: B (Full sentence before colon) | 2: A (Semicolon before 'therefore,') | 3: B (Colon introducing explanation) | 4: B (Semicolons separate complex items)",
            "ex2": "1. The inspection team identified one critical hazard: exposed live electrical wiring. | 2. The morning seminar was postponed; the afternoon workshop proceeded as planned. | 3. Offices are located in Leeds, Yorkshire; Glasgow, Scotland; and Cardiff, Wales. | 4. The essential requirements are enthusiasm, reliability, and numeracy. (OR: The position requires the following qualities: enthusiasm, reliability, and numeracy.)",
            "ex3": "Errors found (4 punctuation corrections): 1) ...strategic priorities: affordable... (colon, not semicolon) | 2) ...accelerated; nevertheless, ground... (semicolon before nevertheless) | 3) ...distinct organisations: Homes England... (correct as is) | 4) One fundamental issue persists: the planning inspectorate... (colon needed)",
            "ex4_model": "The department proposes introducing a formal flexible working framework: core collaborative office hours, remote project days, and compressed working weeks. Staff productivity has increased markedly during trial periods; employee wellbeing metrics have demonstrated equal improvement across all operational teams."
        }
    },
    "page_32": {
        "title": "Complete Answer Key: Units 4 to 7",
        "unit_4": {
            "ex1": "1: A (its) | 2: B (nurses' station) | 3: B (women's) | 4: B (supervisors)",
            "ex2": "1. The paramedics' vehicles. | 2. James's office (or James' office). | 3. The clinic lost its accreditation last November. | 4. All trainees must register before Friday.",
            "ex3": "Errors found (4 apostrophe corrections): 1) ...reviewed its annual leave... (remove apostrophe) | 2) ...all employees' (or employees) entitlements... | 3) ...the union's (or unions') representatives... | 4) ...their teams' (or team's) rosters... (ensure correct singular vs plural)",
            "ex4_model": "Staff are reminded to safeguard every employee's personal belongings by securing locker doors. All team members must comply with the supervisors' inspection guidelines issued this morning. The facility cannot accept liability for any damage to its locker mechanisms caused by unauthorised padlocks."
        },
        "unit_5": {
            "ex1": "1: B (Comma + Capital + Full stop inside) | 2: A (Backshifted tense + she) | 3: A (Inside speech marks) | 4: C (No speech marks in reported speech)",
            "ex2": "1. The paramedic reported, \"The patient regained consciousness after oxygen was administered.\" | 2. Officer Reed stated that he had arrived at the scene at 08:30. | 3. The customer insisted, \"I paid the invoice twice.\" | 4. \"We are ready to proceed,\" the contractor confirmed.",
            "ex3": "Errors found (4 quotation corrections): 1) ...Vance responded, \"I observed... (comma required before speech) | 2) ...stated that the CCTV cameras in Zone 3 had been... (remove quotation marks in reported speech) | 3) ...\"The alarm console indicated a false positive,\" so I... (comma inside quotes) | 4) ...confirmed that all gate locks would be replaced... (remove quotes from reported clause)",
            "ex4_model": "During the investigation, the store supervisor affirmed, \"Both employees maintained professional conduct during the initial exchange.\" However, the customer subsequently reported that she had received conflicting pricing guidance and felt ignored at the checkout counter."
        },
        "unit_6": {
            "ex1": "1: A (has arrived) | 2: B (were notified) | 3: B (is presenting its report) | 4: A (is inspecting)",
            "ex2": "1. The list of candidate qualifications is enclosed with the application. | 2. Either the lead consultant or the client has signed the deed. | 3. Every one of the fire extinguishers is inspected annually. | 4. The quality of the refurbished components was satisfactory.",
            "ex3": "Errors found (4 subject-verb corrections): 1) ...evaluation of clinical procedures indicates... (evaluation is singular) | 2) ...nor the clinical practice facilitators were aware... (facilitators is plural) | 3) ...the committee has determined... (collective noun is singular) | 4) ...emergency protocols require... (protocols is plural)",
            "ex4_model": "A shipment of precision tools is currently missing from Bay 4. Neither the warehouse supervisor nor the inventory clerks were informed of the consignment's early dispatch. A secondary manifest of replacement components has been requested from the supplier to rectify stock imbalances."
        },
        "unit_7": {
            "ex1": "1: B (opened [past] -> examines [present]) | 2: B (had fled) | 3: A (operate) | 4: B (left)",
            "ex2": "1. The nurse took the blood pressure reading and inputted (or entered) the figures into the database. | 2. Before the inspection began, the team had already prepared the safety dossiers. | 3. The company provides training and supports all new apprentices. | 4. She unlocked the laboratory, turned on the ventilation, and checked the temperature.",
            "ex3": "Errors found (4 tense corrections): 1) ...visited Room 12 and found... (found, not finds) | 2) ...duty sister, who administered... (administered, not administers) | 3) ...levels had stabilised... (had stabilised prior to arrival) | 4) ...rests comfortably in bed and has requested... (has requested, not had requested)",
            "ex4_model": "At 07:00 yesterday, a major pipe burst in the prep kitchen, flooding the main food storage area. Staff had isolated the mains valve before structural damage occurred, and catering technicians replaced the split copper pipe by midday. The kitchen is now fully operational and meets all statutory hygiene standards."
        }
    },
    "page_33": {
        "title": "Complete Answer Key: Units 8 to 11",
        "unit_8": {
            "ex1": "1: A (who) | 2: B (whom) | 3: B (me) | 4: B (The bollard broke when the lorry struck it)",
            "ex2": "1. The supervisor confirmed that the apprentice had passed the safety test. | 2. Between you and me, the proposed merger will face regulatory challenges. | 3. The contractor whom we hired last month has exceeded performance targets. | 4. Candidates who meet the minimum criteria will be shortlisted.",
            "ex3": "Errors found (4 pronoun corrections): 1) ...Technology Officer, who immediately... (who, not whom - subject of severed) | 2) ...employee who neglected... (who, not which - referring to a person) | 3) Between you and me... (me, not I) | 4) ...forensic analysts who inspected... (who, not whom - subject of inspected)",
            "ex4_model": "I am writing to recommend Jordan Smith, whom I have supervised for over two years, for the upcoming Senior Compliance Diploma. Between Jordan and me, all departmental audits were submitted ahead of schedule. He demonstrates exemplary analytical diligence and requires no oversight when resolving technical reporting queries."
        },
        "unit_9": {
            "ex1": "1: B (investigate the matter) | 2: B (department failed to achieve...) | 3: B (children / infants) | 4: B (Write them out in full in formal texts)",
            "ex2": "1. We are writing to inform you that the event has been cancelled due to adverse weather conditions. | 2. The firm secured substantial grant funding from the municipal council. | 3. All personnel must adhere strictly to established safety protocols. | 4. Management will not tolerate unauthorised absenteeism or substandard productivity.",
            "ex3": "Errors found (5 register/tone corrections): 1) We're getting in touch -> We are writing to you regarding... | 2) mess-up -> unacceptable disruption / failing | 3) totally gutted -> deeply regret | 4) acted like total amateurs -> exhibited unprofessional conduct | 5) We're gonna give you a massive refund -> We will issue a full reimbursement",
            "ex4_model": "Dear Commercial Tenant, We write to remind you that your commercial lease for Suite 4B expires on 31 January 2027. All furniture must be removed and premises returned in good repair. Following our formal inspection, your tenancy deposit will be transferred in accordance with contractual terms. Yours sincerely, Property Management."
        },
        "unit_10": {
            "ex1": "1: B (Conversely,) | 2: B (; therefore,) | 3: B (Consequently,) | 4: A (Yes, always)",
            "ex2": "1. Staff turnover increased; however, customer satisfaction remained high. | 2. The new machinery boosts output. Furthermore (or Additionally), it lowers noise pollution. | 3. The audit identified multiple non-compliance issues. Consequently, the accreditation was suspended. | 4. Moreover, the facility failed its statutory legionella test.",
            "ex3": "Errors found (4 cohesive/punctuation corrections): 1) ...during Q3; however, initial maintenance... (semicolon before however, comma after) | 2) Plus several -> Furthermore, several... (replace childish 'Plus') | 3) Consequently, technical teams... (comma after consequently) | 4) In addition to this, all site personnel... (comma after introductory phrase)",
            "ex4_model": "Transitioning our fleet to electric vehicles will substantially lower greenhouse gas emissions; however, the upfront procurement capital remains considerable. Furthermore, government clean-air subsidies offset charging infrastructure costs. Consequently, adopting this strategy enhances corporate sustainability while securing long-term operational cost reductions across all delivery routes."
        },
        "unit_11": {
            "ex1": "1: A (affect) | 2: A (practice) | 3: B (principle) | 4: B (complement)",
            "ex2": "1. effect | 2. advise | 3. site | 4. stationary",
            "ex3": "Errors found (6 homophone corrections): 1) ...will complement our existing... (not complementary) | 2) The principal principle -> The principal principle... (first is principal [main], second is principle [rule]) | 3) ...temporarily affect delivery timescales... (affect, not effect) | 4) ...no adverse effect on... (effect, not affect) | 5) ...safety practices into... (practices [noun], not practises) | 6) ...daily practice (correct noun)",
            "ex4_model": "We recommend appointing Apex Logistics as our primary distribution partner. This decision will positively affect our fulfillment timelines and yield an immediate cost-saving effect. Their operational practice complies fully with statutory safety standards, and their management team upholds rigorous commercial principles."
        }
    },
    "page_34": {
        "title": "Complete Answer Key: Master Spelling & Mixed Exam Mocks",
        "spelling": {
            "drill_corrections": [
                "1. directer -> director (spelled with -or)",
                "2. recomendation -> recommendation (single c, double m)",
                "3. accomodate -> accommodate (double c, double m)",
                "4. fourty -> forty (no 'u')",
                "5. nescessary -> necessary (one c, double s)",
                "6. seperate -> separate (sep-a-rate with an 'a')",
                "7. confidentiallity -> confidentiality (single 'l')",
                "8. envirnment -> environment (remember silent 'n')",
                "9. definate -> definite (finite with 'i')",
                "10. privelege -> privilege (ends in -ege, no 'd')"
            ]
        },
        "mock_1": {
            "title": "Task 1 Correction Grid & Examiner Guidance (6 Marks)",
            "corrections": [
                {"original": "Loading Bay 3, the facilities", "correction": "Loading Bay 3; the facilities (or . The)", "type": "Punctuation (Comma Splice)", "mark": "1 Mark"},
                {"original": "spill kits were missing", "correction": "spill kits was missing", "type": "Grammar (Subject-Verb: range is singular)", "mark": "1 Mark"},
                {"original": "yesterday however, they", "correction": "yesterday; however, they (or . However,)", "type": "Punctuation (Conjunctive Adverb)", "mark": "1 Mark"},
                {"original": "operatives was exposed", "correction": "operatives were exposed", "type": "Grammar (Subject-Verb: operatives is plural)", "mark": "1 Mark"},
                {"original": "updates it's emergency", "correction": "updates its emergency", "type": "Punctuation (Possessive pronoun its)", "mark": "1 Mark"},
                {"original": "must seperate hazardous", "correction": "must separate hazardous", "type": "Spelling (separate contains 'a rat')", "mark": "1 Mark"}
            ],
            "examiner_notes": "Award 1 mark per accurately identified and corrected error. Total: 6 Marks. Candidates must demonstrate precise spelling and standard grammar concord."
        },
        "mock_2": {
            "title": "Task 2 Model Rewrite & Mark Scheme (6 Marks)",
            "model_rewrite": "Dear Dr Thorne,\n\nWe are writing to formally apologise for the delay in completing your clinic's refurbishment. Between you and me, the initial survey was deficient; the project manager failed to identify asbestos in the ceiling tiles. Although the specialist contractors arrived promptly last Tuesday, they were unable to proceed without secondary certification. This had an adverse effect on the completion timeline. The company will accommodate your staff in temporary consulting suites and compensate all direct losses.\n\nYours sincerely,\nPremier Build Solutions",
            "error_breakdown": [
                "1. Between you and I -> Between you and me (Object pronoun)",
                "2. was deficient, the project -> was deficient; the project (Comma splice)",
                "3. last Tuesday they was -> last Tuesday, they were (Comma after fronted adverbial + verb concord)",
                "4. adverse affect -> adverse effect (Noun required)",
                "5. accomodate -> accommodate (Double 'c' and double 'm')",
                "6. clinics' -> clinic's (Singular possessive)"
            ]
        }
    }
}
