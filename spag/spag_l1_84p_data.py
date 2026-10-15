# spag_l1_84p_data.py
# Comprehensive Data Sets for Master Functional Skills English Level 1 SPaG Mastery (84-Page Edition)

# =============================================================================
# 1. BASELINE DIAGNOSTIC ASSESSMENT (32 Questions Tagged to Units 1 to 26)
# =============================================================================

L1_DIAGNOSTIC_32 = [
    # Q1 - Unit 1: Sentence Basics
    {
        "num": 1, "unit": 1, "topic": "Unit 1: Capital Letters & Full Stops",
        "prompt": "Which sentence starts with a capital letter and concludes with a valid full stop?",
        "options": ["A) the warehouse shutter opened at dawn.", "B) The warehouse shutter opened at dawn.", "C) The warehouse shutter opened at dawn"],
        "correct": "B"
    },
    # Q2 - Unit 1: Sentence Boundaries
    {
        "num": 2, "unit": 1, "topic": "Unit 1: Sentence Fragments & Run-ons",
        "prompt": "Identify the option that avoids run-ons by separating two thoughts correctly:",
        "options": ["A) The printer jammed we phoned the technical helpdesk.", "B) The printer jammed. We phoned the technical helpdesk.", "C) The printer jammed, we phoned the technical helpdesk."],
        "correct": "B"
    },
    # Q3 - Unit 2: Question Marks
    {
        "num": 3, "unit": 2, "topic": "Unit 2: Question Marks in Customer Service",
        "prompt": "Which customer enquiry requires a terminal question mark?",
        "options": ["A) Could you please confirm your delivery address", "B) I am writing to ask about your weekend return policy.", "C) The customer enquired whether the store was open."],
        "correct": "A"
    },
    # Q4 - Unit 2: Exclamation Marks
    {
        "num": 4, "unit": 2, "topic": "Unit 2: Professional Exclamation Mark Control",
        "prompt": "Which notice demonstrates appropriate, professional exclamation mark usage?",
        "options": ["A) Warning! High voltage equipment inside!", "B) Thanks for your email today!!!!!!", "C) Please contact us right away!!!"],
        "correct": "A"
    },
    # Q5 - Unit 3: Capital Letters (MINTS)
    {
        "num": 5, "unit": 3, "topic": "Unit 3: Proper Nouns & Months",
        "prompt": "Which sentence capitalises days, months, and proper nouns correctly?",
        "options": ["A) The safety audit begins on Tuesday, 14 october at City Hospital.", "B) The safety audit begins on Tuesday, 14 October at City Hospital.", "C) The safety audit begins on tuesday, 14 October at City hospital."],
        "correct": "B"
    },
    # Q6 - Unit 3: Pronoun 'I' and Acronyms
    {
        "num": 6, "unit": 3, "topic": "Unit 3: Pronoun 'I' & Workplace Acronyms",
        "prompt": "Select the sentence where the pronoun 'I' and workplace acronyms are correct:",
        "options": ["A) Yesterday i visited the NHS clinic to inspect PPE supplies.", "B) Yesterday I visited the NHS clinic to inspect PPE supplies.", "C) Yesterday I visited the nhs clinic to inspect ppe supplies."],
        "correct": "B"
    },
    # Q7 - Unit 4: Coordinating Conjunctions
    {
        "num": 7, "unit": 4, "topic": "Unit 4: Coordinating Conjunctions (And, But, Or, So)",
        "prompt": "Choose the best conjunction to show a contrast: 'The parcel arrived on time, [______] the contents were damaged.'",
        "options": ["A) and", "B) but", "C) so"],
        "correct": "B"
    },
    # Q8 - Unit 4: Coordinating Conjunctions (Result)
    {
        "num": 8, "unit": 4, "topic": "Unit 4: Conjunction Showing Result",
        "prompt": "Select the conjunction showing a logical result: 'The battery was dead, [______] the technician replaced it.'",
        "options": ["A) so", "B) but", "C) or"],
        "correct": "A"
    },
    # Q9 - Unit 5: Subordinating Conjunctions (Because)
    {
        "num": 9, "unit": 5, "topic": "Unit 5: Subordinating Conjunctions (Reason)",
        "prompt": "Which sentence links reason to action without creating a sentence fragment?",
        "options": ["A) Because the weather was severe. Deliveries were halted.", "B) Deliveries were halted because the weather was severe.", "C) Deliveries were halted, because the weather was severe."],
        "correct": "B"
    },
    # Q10 - Unit 5: Subordinating Conjunctions (Although)
    {
        "num": 10, "unit": 5, "topic": "Unit 5: Introductory Subordinate Clause Punctuation",
        "prompt": "Which sentence places a comma correctly after an introductory 'Although' clause?",
        "options": ["A) Although the staff worked overtime they did not complete the order.", "B) Although the staff worked overtime, they did not complete the order.", "C) Although, the staff worked overtime they did not complete."],
        "correct": "B"
    },
    # Q11 - Unit 6: Commas in Everyday Lists
    {
        "num": 11, "unit": 6, "topic": "Unit 6: Commas in Everyday Lists",
        "prompt": "Which sentence uses commas correctly to separate items in an office order?",
        "options": ["A) Please order pens paper clips folders and staples.", "B) Please order pens, paper clips, folders and staples.", "C) Please order pens, paper clips, folders, and, staples."],
        "correct": "B"
    },
    # Q12 - Unit 7: Commas after Introductory Phrases
    {
        "num": 12, "unit": 7, "topic": "Unit 7: Commas after Introductory Time Words",
        "prompt": "Choose the sentence with correct punctuation following an introductory time phrase:",
        "options": ["A) Last Monday morning the depot manager inspected all fire exits.", "B) Last Monday morning, the depot manager inspected all fire exits.", "C) Last Monday, morning the depot manager inspected all fire exits."],
        "correct": "B"
    },
    # Q13 - Unit 8: Contractions
    {
        "num": 13, "unit": 8, "topic": "Unit 8: Apostrophes for Contractions",
        "prompt": "Which sentence places the apostrophe of contraction in the correct position?",
        "options": ["A) You should'nt enter if you dont have a pass.", "B) You shouldn't enter if you don't have a pass.", "C) You shouldnt enter if you haven't a pass."],
        "correct": "B"
    },
    # Q14 - Unit 8: Contraction 'It's' vs 'Its'
    {
        "num": 14, "unit": 8, "topic": "Unit 8: Contraction 'It's' (= It is)",
        "prompt": "Select the sentence that uses 'it's' correctly as a contraction for 'it is':",
        "options": ["A) The machine lost it's power during the storm.", "B) It's essential that all staff attend the safety briefing.", "C) The company changed it's logo last month."],
        "correct": "B"
    },
    # Q15 - Unit 9: Singular Possession
    {
        "num": 15, "unit": 9, "topic": "Unit 9: Apostrophes for Singular Possession",
        "prompt": "Which sentence correctly indicates that an invoice belongs to one supplier?",
        "options": ["A) The supplier's invoice was paid yesterday.", "B) The suppliers invoice was paid yesterday.", "C) The suppliers' invoice was paid yesterday."],
        "correct": "A"
    },
    # Q16 - Unit 10: Plural Nouns Regular (-s, -es)
    {
        "num": 16, "unit": 10, "topic": "Unit 10: Regular Plural Suffixes (-es)",
        "prompt": "What is the correct plural form of the noun 'box'?",
        "options": ["A) boxs", "B) boxes", "C) box's"],
        "correct": "B"
    },
    # Q17 - Unit 10: Irregular Plurals
    {
        "num": 17, "unit": 10, "topic": "Unit 10: Irregular Plurals (men, women, children)",
        "prompt": "Select the sentence with correct irregular plural nouns:",
        "options": ["A) Both security mans guided the visitors and their childs.", "B) Both security men guided the visitors and their children.", "C) Both security mens guided the visitors and their childrens."],
        "correct": "B"
    },
    # Q18 - Unit 11: Plurals ending in -y
    {
        "num": 18, "unit": 11, "topic": "Unit 11: Plural Nouns ending in -y",
        "prompt": "What is the correct plural form of 'company' and 'holiday'?",
        "options": ["A) companys / holidaies", "B) companies / holidays", "C) companies / holidies"],
        "correct": "B"
    },
    # Q19 - Unit 12: Plural Possession
    {
        "num": 19, "unit": 12, "topic": "Unit 12: Apostrophes with Regular Plural Nouns",
        "prompt": "Which phrase correctly describes a rest room shared by multiple drivers?",
        "options": ["A) the driver's rest room", "B) the drivers' rest room", "C) the drivers rest room's"],
        "correct": "B"
    },
    # Q20 - Unit 13: Present Simple
    {
        "num": 20, "unit": 13, "topic": "Unit 13: Present Simple Third-Person -s",
        "prompt": "Which sentence uses the correct present simple verb for a daily routine?",
        "options": ["A) The caretaker inspects the fire alarms every Friday.", "B) The caretaker inspect the fire alarms every Friday.", "C) The caretaker inspecting the fire alarms every Friday."],
        "correct": "A"
    },
    # Q21 - Unit 14: Present Continuous
    {
        "num": 21, "unit": 14, "topic": "Unit 14: Present Continuous Auxiliary + -ing",
        "prompt": "Which sentence forms the present continuous tense correctly?",
        "options": ["A) The technician currently repairing the main server.", "B) The technician is currently repairing the main server.", "C) The technician are currently repairing the main server."],
        "correct": "B"
    },
    # Q22 - Unit 15: Past Simple Regular (-ed)
    {
        "num": 22, "unit": 15, "topic": "Unit 15: Past Simple Regular CVC Doubling",
        "prompt": "What is the correct past simple spelling of 'slip' and 'stop'?",
        "options": ["A) sliped / stoped", "B) slipped / stopped", "C) slipt / stopt"],
        "correct": "B"
    },
    # Q23 - Unit 16: Past Simple Irregular Verbs
    {
        "num": 23, "unit": 16, "topic": "Unit 16: Top Irregular Past Verbs (saw, wrote, went)",
        "prompt": "Select the sentence that uses Standard English past tense verbs:",
        "options": ["A) I seen the oil spill and writed a report immediately.", "B) I saw the oil spill and wrote a report immediately.", "C) I seen the oil spill and wrote a report immediately."],
        "correct": "B"
    },
    # Q24 - Unit 17: Future Intentions
    {
        "num": 24, "unit": 17, "topic": "Unit 17: Future Intentions (Going to vs Will)",
        "prompt": "Which sentence expresses a planned future intention with correct grammar?",
        "options": ["A) We going to upgrade the warehouse conveyor in June.", "B) We are going to upgrade the warehouse conveyor in June.", "C) We will to upgrade the warehouse conveyor in June."],
        "correct": "B"
    },
    # Q25 - Unit 18: Subject-Verb Agreement (Singular vs Plural)
    {
        "num": 25, "unit": 18, "topic": "Unit 18: Subject-Verb Agreement (was/were)",
        "prompt": "Choose the sentence with correct subject-verb agreement:",
        "options": ["A) Both apprentices was commended by the site supervisor.", "B) Both apprentices were commended by the site supervisor.", "C) Both apprentices is commended by the site supervisor."],
        "correct": "B"
    },
    # Q26 - Unit 19: There is / There are
    {
        "num": 26, "unit": 19, "topic": "Unit 19: Subject-Verb Agreement with There is / There are",
        "prompt": "Select the correct option to complete: '[______] six replacement valves in the store cupboard.'",
        "options": ["A) There is", "B) There's", "C) There are"],
        "correct": "C"
    },
    # Q27 - Unit 20: Pronoun Consistency
    {
        "num": 27, "unit": 20, "topic": "Unit 20: Pronoun Consistency (Avoiding Shifts)",
        "prompt": "Which sentence maintains consistent pronouns throughout?",
        "options": ["A) When employees arrive, you must sign in at the gate.", "B) When employees arrive, they must sign in at the gate.", "C) When employees arrive, we must sign in at the gate."],
        "correct": "B"
    },
    # Q28 - Unit 21: Standard English vs Slang
    {
        "num": 28, "unit": 21, "topic": "Unit 21: Standard English (Did vs Done, Double Negatives)",
        "prompt": "Identify the sentence written in correct formal Standard English:",
        "options": ["A) The apprentice done all the maintenance checks.", "B) The apprentice did all the maintenance checks.", "C) The apprentice didn't do no maintenance checks."],
        "correct": "B"
    },
    # Q29 - Unit 22: Homophones (Their, There, They're)
    {
        "num": 29, "unit": 22, "topic": "Unit 22: Homophones (Their, There, They're)",
        "prompt": "Choose the correct words: 'The engineers parked [______] vans over [______].'",
        "options": ["A) there / their", "B) their / there", "C) they're / there"],
        "correct": "B"
    },
    # Q30 - Unit 23: Homophones (Two, To, Too)
    {
        "num": 30, "unit": 23, "topic": "Unit 23: Homophones (Two, To, Too)",
        "prompt": "Select the sentence that uses to, too, and two correctly:",
        "options": ["A) The pallet was too heavy for two workers to lift.", "B) The pallet was to heavy for to workers too lift.", "C) The pallet was two heavy for too workers to lift."],
        "correct": "A"
    },
    # Q31 - Unit 24: Homophones (Hear/Here, Wear/Where)
    {
        "num": 31, "unit": 24, "topic": "Unit 24: Sensory & Spatial Homophones",
        "prompt": "Which sentence uses 'hear', 'here', 'wear', and 'where' accurately?",
        "options": ["A) You must wear your safety goggles where signs are posted here.", "B) You must where your safety goggles wear signs are posted hear.", "C) You must wear your safety goggles wear signs are posted here."],
        "correct": "A"
    },
    # Q32 - Units 25 & 26: Prefixes & Suffixes
    {
        "num": 32, "unit": 25, "topic": "Units 25 & 26: Prefixes and Suffixes",
        "prompt": "Which sentence spells both the prefixed word and the suffixed word correctly?",
        "options": ["A) The team disconnected the wire and completed the task carefully.", "B) The team dissconnected the wire and completed the task carefull.", "C) The team disconnected the wire and completed the task carefullly."],
        "correct": "A"
    }
]

# Diagnostic Scoring Rubric & Routing Guide
L1_DIAGNOSTIC_RUBRIC = [
    {
        "score_range": "28 – 32 Marks",
        "band": "Green: Advanced Level 1 SPaG Competency",
        "description": "Demonstrates outstanding punctuation control, consistent verb tenses, and strong orthographic accuracy. Ready for official exam mocks.",
        "recommended_units": "Focus on high-speed exam proofreading (Pages 71–76) and high-level vocabulary collocations (Pages 59–64)."
    },
    {
        "score_range": "18 – 27 Marks",
        "band": "Amber: Developing Functional Skills Competency",
        "description": "Solid understanding of basic sentence boundaries, but shows minor inconsistencies in apostrophes, irregular verb forms, or homophones.",
        "recommended_units": "Prioritise Units 8–12 (Apostrophes & Plurals), Units 15–16 (Past Tenses), and Units 22–24 (Homophones)."
    },
    {
        "score_range": "0 – 17 Marks",
        "band": "Red: Intensive Foundation Required",
        "description": "Significant gaps in core sentence structure, subject-verb concord, and basic punctuation.",
        "recommended_units": "Work methodically through all 26 units from Unit 1 to Unit 26 using the Raymond Murphy two-page self-study spreads."
    }
]

# Routing Map: Diagnostic Question -> Unit Number & Priority Topic
L1_ROUTING_MAP = [
    (1, "Unit 1", "Sentence Basics & Full Stops"),
    (2, "Unit 1", "Run-ons & Fragments"),
    (3, "Unit 2", "Question Marks in Customer Service"),
    (4, "Unit 2", "Exclamation Control"),
    (5, "Unit 3", "Proper Nouns & MINTS"),
    (6, "Unit 3", "Acronyms & Pronoun 'I'"),
    (7, "Unit 4", "Coordinating Conjunctions (But)"),
    (8, "Unit 4", "Coordinating Conjunctions (So)"),
    (9, "Unit 5", "Subordinating Conjunctions (Because)"),
    (10, "Unit 5", "Introductory Clauses & Commas"),
    (11, "Unit 6", "Commas in Lists"),
    (12, "Unit 7", "Commas after Introductory Phrases"),
    (13, "Unit 8", "Contraction Apostrophes"),
    (14, "Unit 8", "It's vs Its"),
    (15, "Unit 9", "Singular Possession Apostrophes"),
    (16, "Unit 10", "Regular Plurals (-s, -es)"),
    (17, "Unit 10", "Irregular Plurals (men, children)"),
    (18, "Unit 11", "Plural Nouns ending in -y"),
    (19, "Unit 12", "Plural Possessive Apostrophes"),
    (20, "Unit 13", "Present Simple Routines & -s"),
    (21, "Unit 14", "Present Continuous ('is working')"),
    (22, "Unit 15", "Past Simple Regular (-ed) Rules"),
    (23, "Unit 16", "Top 40 Irregular Verbs (saw, wrote)"),
    (24, "Unit 17", "Future Intentions (Going to vs Will)"),
    (25, "Unit 18", "Subject-Verb Agreement (was/were)"),
    (26, "Unit 19", "There is vs There are"),
    (27, "Unit 20", "Pronoun Consistency"),
    (28, "Unit 21", "Standard English vs Slang"),
    (29, "Unit 22", "Homophones: Their, There, They're"),
    (30, "Unit 23", "Homophones: Two, To, Too"),
    (31, "Unit 24", "Homophones: Hear/Here, Wear/Where"),
    (32, "Units 25-26", "Prefixes (un-, dis-) & Suffixes (-ful, -ly)")
]


# =============================================================================
# 2. VOCABULARY IN USE MASTER MODULES (PAGES 59–64: 6 PAGES)
# =============================================================================

VOCAB_MODULES = [
    # Page 59: Module 1
    {
        "page": 59,
        "module": 1,
        "title": "Professional Workplace Register & Formal vs Informal Word Choice",
        "subtitle": "McCarthy & Redman 'Vocabulary in Use' Framework: Register Calibration",
        "intro": "In workplace writing, tone establishes your professionalism. Informal spoken idioms (e.g. 'kids', 'boss', 'get in touch') should be upgraded to precise vocational terminology. Using standard formal register ensures clarity and respect.",
        "tables": [
            {
                "heading": "Everyday Slang / Informal Terms vs High-Yield Professional Alternatives",
                "headers": ["Informal / Colloquial", "Standard Workplace Equivalent", "Vocational Example Sentence"],
                "rows": [
                    ["tell off / have a word", "reprimand / address", "The manager addressed the punctuality issue privately."],
                    ["ask for", "request / enquire", "Please request replacement safety boots using Form B."],
                    ["get in touch with", "contact / liaise with", "We will liaise with the regional logistics coordinator."],
                    ["boss / gaffer", "supervisor / line manager", "Submit your annual leave form to your line manager."],
                    ["look into", "investigate / examine", "Quality assurance will investigate the packaging defect."],
                    ["put off", "postpone / reschedule", "The maintenance shutdown has been rescheduled for July."],
                    ["give back", "refund / reimburse", "The accounts department will reimburse your travel expenses."]
                ]
            },
            {
                "heading": "Standard Correspondence Openers & Sign-offs",
                "headers": ["Situation / Context", "Recommended Formal Phrasing", "Pitfall to Avoid"],
                "rows": [
                    ["Opening formal letter (name known)", "Dear Mr Davies, / Dear Ms Clarke,", "Never write 'Hey' or 'Hi Dave'"],
                    ["Opening formal letter (name unknown)", "Dear Sir or Madam,", "Avoid 'To who it concerns'"],
                    ["Closing (named recipient)", "Yours sincerely,", "Avoid 'Cheers' or 'Best regards' in strict formal letters"],
                    ["Closing (unnamed recipient)", "Yours faithfully,", "Do not mix 'faithfully' with a named person"]
                ]
            }
        ],
        "drill": {
            "prompt": "Transform the informal sentence into professional workplace English:",
            "bad": "Hi boss, I'm writing to tell you that I wanna put off our chat because I gotta look into a problem with the delivery van.",
            "model": "Dear Mr Jenkins, I am writing to request that we reschedule our meeting, as I need to investigate an issue with the delivery vehicle."
        }
    },

    # Page 60: Module 2
    {
        "page": 60,
        "module": 2,
        "title": "Essential Health, Safety & Compliance Vocabulary Bank",
        "subtitle": "Statutory Safety Terminology & Risk Assessment Phrasing",
        "intro": "Health and Safety Executive (HSE) compliance requires exact vocabulary. Using vague language like 'dangerous stuff' instead of 'hazardous substances' weakens incident reports and legal documentation.",
        "tables": [
            {
                "heading": "Core Statutory Safety Terms & Exact Functional Definitions",
                "headers": ["Term & Pronunciation", "Exact Definition", "Workplace Application"],
                "rows": [
                    ["Hazard (/ˈhæzəd/)", "A potential source of harm or adverse health effect.", "Trailing electrical cables represent a severe trip hazard."],
                    ["Risk (/rɪsk/)", "The likelihood and severity of harm occurring.", "Conduct a risk assessment before operating the angle grinder."],
                    ["Mandatory (/ˈmændətəri/)", "Compulsory by law or official statutory directive.", "Wearing high-visibility vests is mandatory on the loading dock."],
                    ["Evacuation (/ɪˌvækjuˈeɪʃn/)", "The urgent removal of personnel from a danger zone.", "Follow the marked green directional arrows during a site evacuation."],
                    ["Precaution (/prɪˈkɔːʃn/)", "A preventative measure taken in advance to prevent danger.", "Take the precaution of isolating the mains power before maintenance."],
                    ["Flammable (/ˈflæməbl/)", "Easily set on fire; combustible.", "Store flammable solvents inside the yellow fire-rated cabinet."],
                    ["Authorized (/ˈɔːθəraɪzd/)", "Having official permission or legal approval.", "Only authorized personnel may enter the chemical storage vault."]
                ]
            },
            {
                "heading": "Statutory Health & Safety Acronyms",
                "headers": ["Acronym", "Full Official Title", "Workplace Significance"],
                "rows": [
                    ["PPE", "Personal Protective Equipment", "Helmets, safety goggles, ear defenders, high-vis vests."],
                    ["COSHH", "Control of Substances Hazardous to Health", "Legal framework for safely storing cleaning chemicals and fumes."],
                    ["RIDDOR", "Reporting of Injuries, Diseases & Dangerous Occurrences", "Statutory reporting of workplace fractures and serious incidents."],
                    ["SOP", "Standard Operating Procedure", "Step-by-step instructions for operating industrial machinery."]
                ]
            }
        ],
        "drill": {
            "prompt": "Complete the statutory safety instruction using words from the table:",
            "bad": "Workers must put on their gear because stuff can catch fire.",
            "model": "Wearing full PPE is mandatory in this workshop because all stored chemicals are highly flammable."
        }
    },

    # Page 61: Module 3
    {
        "page": 61,
        "module": 3,
        "title": "Administrative & Office Communication Collocations",
        "subtitle": "Vocational Collocations: Words That Naturally Go Together",
        "intro": "Collocations are pairs or groups of words that naturally co-occur in British business English. Using natural collocations (e.g. 'schedule an appointment', NOT 'make an appointment on calendar') makes administrative documents sound natural and authoritative.",
        "tables": [
            {
                "heading": "Essential Workplace Verb + Noun Collocations",
                "headers": ["Verb + Noun Collocation", "Meaning", "Example Sentence"],
                "rows": [
                    ["schedule an appointment", "Arrange a formal meeting or consultation.", "The receptionist scheduled an appointment for Thursday morning."],
                    ["submit an invoice", "Send a bill for payment to accounts.", "Please submit your monthly invoice by the 25th of the month."],
                    ["confirm attendance", "Verify that you will participate.", "Delegates must confirm their attendance by replying to the email."],
                    ["attach documentation", "Include supporting evidence or forms.", "Remember to attach documentation verifying your identification."],
                    ["resolve a discrepancy", "Find a solution to an error or difference.", "The warehouse manager resolved the inventory discrepancy."],
                    ["meet a deadline", "Finish a task before the required time.", "The design department worked late to meet the printing deadline."],
                    ["implement a policy", "Put a new rule or strategy into practice.", "Our organisation will implement a new safeguarding policy next week."]
                ]
            },
            {
                "heading": "Prepositional Collocations in Business Writing",
                "headers": ["Collocation", "Correct Preposition", "Example in Office Context"],
                "rows": [
                    ["in compliance with", "WITH (not to)", "All fire doors were fitted in compliance with building regulations."],
                    ["responsible for", "FOR (not of)", "The shift supervisor is responsible for securing the facility."],
                    ["on behalf of", "OF (not for)", "I am writing on behalf of the customer service director."],
                    ["in accordance with", "WITH (not by)", "Leave will be granted in accordance with company policy."]
                ]
            }
        ],
        "drill": {
            "prompt": "Rewrite this clumsy sentence using standard office collocations:",
            "bad": "I am sending this letter for my manager to fix the difference in the bill before the end date.",
            "model": "I am writing on behalf of my manager to resolve the discrepancy in the invoice before the deadline."
        }
    },

    # Page 62: Module 4
    {
        "page": 62,
        "module": 4,
        "title": "Customer Service & Hospitality Precision Phrasing",
        "subtitle": "De-escalation Language & Client Care Phrases",
        "intro": "In retail, customer service, and hospitality, words de-escalate tension and protect brand loyalty. Replacing defensive language with empathetic, solution-oriented phrasing resolves complaints smoothly.",
        "tables": [
            {
                "heading": "Defensive Language vs Solution-Oriented Customer Care Phrasing",
                "headers": ["Defensive / Negative Phrasing", "Professional Customer Care Alternative", "Communication Purpose"],
                "rows": [
                    ["That's not my fault / job.", "Allow me to direct you to the team leader who handles this.", "Taking ownership of customer care."],
                    ["You can't do that.", "Under our store policy, we are able to offer an exchange or credit note.", "Explaining options politely."],
                    ["You have to wait.", "Thank you for your patience while I retrieve your account file.", "Showing courteous appreciation."],
                    ["Calm down.", "I understand your frustration, and I am committed to resolving this for you.", "De-escalating customer distress."],
                    ["We don't have none left.", "Regrettably, that item is currently out of stock; I can order it for tomorrow.", "Offering immediate constructive alternatives."],
                    ["You broke the rules.", "To ensure safety compliance, guests are requested to use the marked walkway.", "Explaining safety constructively."]
                ]
            },
            {
                "heading": "Key Customer Care Collocations",
                "headers": ["Collocation", "Meaning", "Example Context"],
                "rows": [
                    ["apologise for any inconvenience", "Express regret for client disruption.", "We apologise for any inconvenience caused by the delivery delay."],
                    ["rectify the situation", "Correct an error immediately.", "Our supervisor will issue a replacement voucher to rectify the situation."],
                    ["exceed customer expectations", "Deliver better service than anticipated.", "Our staff are trained to exceed customer expectations daily."],
                    ["accommodate dietary requirements", "Provide safe food options for allergies.", "The banquet menu accommodates all vegan and gluten-free dietary requirements."]
                ]
            }
        ],
        "drill": {
            "prompt": "Rewrite the blunt customer service reply into courteous, professional correspondence:",
            "bad": "You can't have a refund because you lost the receipt and it's not my problem.",
            "model": "While store policy requires a receipt for cash refunds, I would be delighted to provide you with a store credit voucher to rectify the issue."
        }
    },

    # Page 63: Module 5
    {
        "page": 63,
        "module": 5,
        "title": "Master Spelling Rules & Morphological Patterns",
        "subtitle": "Orthographic Formulas: Doubling, Dropping Silent 'e', and Suffix Rules",
        "intro": "English spelling follows consistent structural patterns. Mastering these five fundamental rules eliminates over 80% of common Functional Skills Level 1 spelling errors.",
        "tables": [
            {
                "heading": "The 5 Master Spelling Rules for Level 1 Writers",
                "headers": ["Rule Name & Formula", "Structural Explanation", "Key Workplace Examples"],
                "rows": [
                    ["1. CVC Consonant Doubling", "When a 1-syllable word ends in Consonant-Vowel-Consonant, double the final consonant before adding a vowel suffix (-ed, -ing, -er).", "slip &rarr; slipped, run &rarr; running, plan &rarr; planned, drop &rarr; dropped, shop &rarr; shopper."],
                    ["2. Drop Silent 'e' Before Vowel", "Drop the final silent 'e' when adding a suffix starting with a vowel (-ing, -ed, -able). Keep it before consonant suffixes (-ful, -ment).", "write &rarr; writing, hope &rarr; hoping, care &rarr; caring. BUT: care &rarr; careful, manage &rarr; management."],
                    ["3. Change 'y' to 'i'", "When a word ends in a consonant + 'y', change 'y' to 'i' before suffixes (-ed, -es, -ly, -ness), UNLESS adding -ing.", "tidy &rarr; tidied, happy &rarr; happily, rely &rarr; relied. BUT: tidy &rarr; tidying, carry &rarr; carrying."],
                    ["4. 'I' Before 'E' Except After 'C'", "Spell 'ie' when the sound is long /ee/, except immediately after the letter 'c'.", "achieve, believe, brief, piece. EXCEPT after 'c': receive, receipt, ceiling, deceit."],
                    ["5. Plural of -f / -fe to -ves", "Nouns ending in -f or -fe change to -ves in the plural.", "shelf &rarr; shelves, knife &rarr; knives, half &rarr; halves, leaf &rarr; leaves, life &rarr; lives."]
                ]
            }
        ],
        "drill": {
            "prompt": "Apply the correct spelling rules to form the derived words:",
            "bad": "rely + ed = ? | drop + ing = ? | receive or recieve? | shelf (plural) = ?",
            "model": "relied | dropping | receive (after 'c'!) | shelves (-f changes to -ves)"
        }
    },

    # Page 64: Module 6
    {
        "page": 64,
        "module": 6,
        "title": "High-Frequency Level 1 Functional Spelling Bank",
        "subtitle": "Top 100 Commonly Misspelt Vocational Words & Phonemic Anchors",
        "intro": "Examiners penalise repetitive spelling errors in high-frequency vocabulary. Memorise these core vocational words divided into practical semantic categories.",
        "tables": [
            {
                "heading": "Essential Vocational Spelling Clusters & Visual Traps",
                "headers": ["Workplace Category", "Words with Tricky Letters Bolded", "Examiner Memory Anchor"],
                "rows": [
                    ["Office Administration", "bu<strong>si</strong>ness, ca<strong>len</strong>dar, ne<strong>ce</strong>ssary, re<strong>cei</strong>pt, com<strong>mit</strong>tee, se<strong>pa</strong>rate", "Remember: 'ne<strong>c</strong>essary' has 1 <strong>C</strong>ollar and 2 <strong>S</strong>leeves! Sep<strong>a</strong>rate has 'a rat' inside."],
                    ["Health & Safety", "ha<strong>zard</strong>ous, e<strong>quip</strong>ment, hy<strong>gie</strong>ne, a<strong>cci</strong>dent, main<strong>ten</strong>ance, am<strong>bu</strong>lance", "'Equipment' NEVER has an 's' on the end. Main<strong>ten</strong>ance contains 'ten'."],
                    ["Customer Service", "apolo<strong>gise</strong>, qua<strong>li</strong>ty, ex<strong>cell</strong>ent, re<strong>spon</strong>sibility, dis<strong>sa</strong>tisfied", "'Dissatisfied' has TWO 's's (dis + satisfied)."],
                    ["Time & Scheduling", "We<strong>dnes</strong>day, Fe<strong>bru</strong>ary, to<strong>mor</strong>row, to<strong>day</strong>, au<strong>tumn</strong>, sched<strong>ule</strong>", "Wed-<strong>nes</strong>-day! To<strong>mor</strong>row has 1 <strong>M</strong>other and 2 <strong>R</strong>oses (one 'm', two 'r's)."],
                    ["Facilities & Logistics", "ware<strong>house</strong>, pa<strong>ckag</strong>ing, col<strong>league</strong>, veh<strong>icle</strong>, dis<strong>patch</strong>", "'Colleague' ends like league in football."],
                    ["General Workplace", "suc<strong>cess</strong>ful, defi<strong>nite</strong>ly, en<strong>viron</strong>ment, op<strong>por</strong>tunity, sin<strong>cere</strong>ly", "'Definitely' comes from 'finite' (never write definately!). Enviro<strong>n</strong>ment has an 'n'."]
                ]
            }
        ],
        "drill": {
            "prompt": "Select and write the correctly spelled words from each pair:",
            "bad": "neccessary / necessary | buisness / business | tomorow / tomorrow | definately / definitely",
            "model": "necessary | business | tomorrow | definitely"
        }
    }
]


# =============================================================================
# 3. MURPHY-STYLE MIXED ADDITIONAL EXERCISES (PAGES 65–70: 6 PAGES)
# =============================================================================

MIXED_WORKOUTS = [
    # Page 65: Workout 1 (Units 1–7)
    {
        "page": 65,
        "workout_num": 1,
        "title": "Mixed Workout 1: Sentence Boundaries, Connectives & Commas",
        "coverage": "Units 1 to 7: Capital Letters, Full Stops, Conjunctions & Commas",
        "intro": "This multi-topic exercise tests your mastery of sentence boundaries, coordinating and subordinating conjunctions, and comma mechanics across authentic workplace contexts.",
        "drills": [
            {
                "section": "[PART A] Binary Boundary Discrimination (4 Marks)",
                "items": [
                    ("Identify the correctly punctuated sentence without fragments or run-ons:",
                     ["A) The clinic opened at eight, there were twelve patients waiting.", "B) The clinic opened at eight. There were twelve patients waiting.", "C) The clinic opened at eight there were twelve patients waiting."], "B"),
                    ("Which sentence uses a conjunction correctly with terminal punctuation?",
                     ["A) The technician checked the motor, but the power cord was damaged.", "B) The technician checked the motor but, the power cord was damaged.", "C) The technician checked the motor, but the power cord was damaged?"], "A"),
                    ("Choose the sentence that correctly punctuates an introductory clause:",
                     ["A) Because the alarm sounded all staff evacuated to Car Park B.", "B) Because the alarm sounded, all staff evacuated to Car Park B.", "C) Because, the alarm sounded all staff evacuated."], "B"),
                    ("Select the sentence with accurate comma separation in a list:",
                     ["A) Order pens, highlighters, folders and clipboards.", "B) Order pens, highlighters, folders, and, clipboards.", "C) Order pens highlighters folders and clipboards."], "A")
                ]
            },
            {
                "section": "[PART B] Controlled Sentence Synthesis (3 Marks)",
                "items": [
                    ("Join these two choppy sentences using 'so'", "The stockroom was flooded. The supervisor closed Aisle 4.", "The stockroom was flooded, so the supervisor closed Aisle 4."),
                    ("Join these sentences using 'although' at the beginning", "The apprentice was nervous. He passed the practical driving test.", "Although the apprentice was nervous, he passed the practical driving test."),
                    ("Add commas to the introductory phrase and list", "Yesterday morning our catering team ordered bread butter eggs and milk", "Yesterday morning, our catering team ordered bread, butter, eggs and milk.")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Review this staff notice posted on a depot canteen noticeboard. There are exactly 5 SPaG errors (missing capital letters, run-ons, missing commas, and comma splices).",
                "text": "welcome to the new staff canteen on station road. The canteen opens at 07:00 every weekday it serves hot breakfast porridge and fresh fruit. Although the seating area is spacious please clear your own trays after eating. on fridays the kitchen closes early, staff must purchase snacks before 14:00.",
                "err_count": 5
            }
        ]
    },

    # Page 66: Workout 2 (Units 8–12)
    {
        "page": 66,
        "workout_num": 2,
        "title": "Mixed Workout 2: Apostrophes, Plurals & Possession",
        "coverage": "Units 8 to 12: Contractions, Singular & Plural Possession, and Plural Nouns",
        "intro": "Synthesise your knowledge of contraction apostrophes, regular and irregular plural nouns, and the critical distinction between singular and plural possessives.",
        "drills": [
            {
                "section": "[PART A] Multiple Choice Discrimination (4 Marks)",
                "items": [
                    ("Which sentence uses contraction apostrophes accurately?",
                     ["A) You shouldn't enter if you haven't received clearance.", "B) You should'nt enter if you have'nt received clearance.", "C) You shouldnt enter if you havent received clearance."], "A"),
                    ("Identify the sentence showing singular possession for one technician:",
                     ["A) The technician's screwdriver was left on the workbench.", "B) The technicians screwdriver was left on the workbench.", "C) The technicians' screwdriver was left on the workbench."], "A"),
                    ("Which sentence shows regular plural possession for multiple managers?",
                     ["A) The manager's meeting began at noon.", "B) The managers' meeting began at noon.", "C) The managers meeting's began at noon."], "B"),
                    ("Select the sentence with zero pluralisation or apostrophe errors:",
                     ["A) The children's nursery received five new wooden boxes.", "B) The childrens' nursery received five new wooden boxs.", "C) The childrens nursery received five new wooden box's."], "A")
                ]
            },
            {
                "section": "[PART B] Sentence Transformation (3 Marks)",
                "items": [
                    ("Contract 'they cannot' and 'it is'", "they cannot attend because it is too late", "They can't attend because it's too late."),
                    ("Make plural possessive: the tools belonging to the plumbers", "the tools of the plumbers", "the plumbers' tools"),
                    ("Correct the irregular plural and possession", "The womens locker room was refurbished last month", "The women's locker room was refurbished last month.")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Proofread this equipment requisition notice from a construction site office. Find exactly 5 apostrophe and plural errors.",
                "text": "Site Notice: All contractor's must store their gear in the workers locker room. The supervisor found one electricans drill left in the main hallway. In addition, three industrial torchs are missing from the security cupboard. If you cant locate your equipment, please inform site reception before 17:00.",
                "err_count": 5
            }
        ]
    },

    # Page 67: Workout 3 (Units 13–17)
    {
        "page": 67,
        "workout_num": 3,
        "title": "Mixed Workout 3: Tenses & Verb Consistency in Reports",
        "coverage": "Units 13 to 17: Present Simple, Present Continuous, Regular & Irregular Past, Future Intentions",
        "intro": "In workplace incident logs and project reports, maintaining tense consistency is essential. Practise distinguishing present routines, ongoing tasks, completed past actions, and future commitments.",
        "drills": [
            {
                "section": "[PART A] Tense Discrimination Drills (4 Marks)",
                "items": [
                    ("Which sentence uses the present simple third-person verb correctly?",
                     ["A) The supervisor checks the fire doors every Monday.", "B) The supervisor check the fire doors every Monday.", "C) The supervisor checking the fire doors every Monday."], "A"),
                    ("Choose the correct present continuous construction:",
                     ["A) Two contractors is repairing the roof right now.", "B) Two contractors are repairing the roof right now.", "C) Two contractors repairing the roof right now."], "B"),
                    ("Which sentence spells the regular past simple verb correctly?",
                     ["A) The forklift driver sliped on the oily floor and stoped.", "B) The forklift driver slipped on the oily floor and stopped.", "C) The forklift driver slipped on the oily floor and stoped."], "B"),
                    ("Select the sentence that uses Standard English irregular past verbs:",
                     ["A) I seen the intruder and writed down the registration.", "B) I saw the intruder and wrote down the registration.", "C) I seen the intruder and wrote down the registration."], "B")
                ]
            },
            {
                "section": "[PART B] Verb Form Conversion (3 Marks)",
                "items": [
                    ("Convert to past simple: 'The delivery driver [bring] the parcel and [leave] it at reception.'", "bring / leave", "The delivery driver brought the parcel and left it at reception."),
                    ("Convert to future planned intention using 'going to'", "Our company [launch] a new recycling initiative next month.", "Our company is going to launch a new recycling initiative next month."),
                    ("Correct the present continuous spelling error", "The IT team is [runing] full system diagnostics.", "The IT team is running full system diagnostics.")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Proofread this excerpt from a security guard's shift report. Identify exactly 5 verb tense and spelling errors.",
                "text": "Shift Report: At 03:00, officer Davies notice a flickering light in the main office. He went to investigate and seen that a ceiling pipe had burst. Water was runing across the server room floor. The officer stoped the main valve immediately and writed an urgent maintenance log for morning shift.",
                "err_count": 5
            }
        ]
    },

    # Page 68: Workout 4 (Units 18–21)
    {
        "page": 68,
        "workout_num": 4,
        "title": "Mixed Workout 4: Agreement, Pronoun Harmony & Standard English",
        "coverage": "Units 18 to 21: Subject-Verb Agreement, There is/are, Pronoun Consistency & Standard English",
        "intro": "Demonstrate your command of grammatical concord, existential 'there', pronoun stability, and formal Standard English register by eliminating colloquialisms and agreement faults.",
        "drills": [
            {
                "section": "[PART A] Agreement & Register Recognition (4 Marks)",
                "items": [
                    ("Select the sentence with correct subject-verb agreement:",
                     ["A) Both apprentices was awarded their health and safety certificates.", "B) Both apprentices were awarded their health and safety certificates.", "C) Both apprentices is awarded their health and safety certificates."], "B"),
                    ("Which sentence agrees with existential 'There are'?",
                     ["A) There are twenty new laptops stored in the cabinet.", "B) There is twenty new laptops stored in the cabinet.", "C) There's twenty new laptops stored in the cabinet."], "A"),
                    ("Identify the sentence maintaining consistent third-person pronouns:",
                     ["A) When employees arrive, you must scan your identity badge.", "B) When employees arrive, they must scan their identity badges.", "C) When employees arrive, we must scan your identity badge."], "B"),
                    ("Which sentence is written in correct Standard English without slang or double negatives?",
                     ["A) We didn't receive no notification from the depot.", "B) The supervisor did the risk assessment yesterday.", "C) The supervisor done the risk assessment yesterday."], "B")
                ]
            },
            {
                "section": "[PART B] Sentence Correction (3 Marks)",
                "items": [
                    ("Correct the subject-verb agreement error", "The crate of spare machine parts were delivered to Bay 3", "The crate of spare machine parts was delivered to Bay 3."),
                    ("Eliminate the double negative", "The warehouse team haven't got no spare safety helmets", "The warehouse team do not have any spare safety helmets."),
                    ("Replace non-standard 'done' and 'seen'", "I done the cleaning and seen that the drains were clear", "I did the cleaning and saw that the drains were clear.")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Review this draft incident debrief written by a warehouse team leader. Identify exactly 5 agreement, pronoun, and non-standard English errors.",
                "text": "Debrief: Yesterday afternoon, the supervisor and the safety representative was inspecting the loading ramp. There was four pallets stacked unevenly near the bay door. When a worker stacks heavy boxes, you must ensure that the base is level. The team leader done an immediate safety review, and the crew didn't receive no complaints.",
                "err_count": 5
            }
        ]
    },

    # Page 69: Workout 5 (Units 22–24)
    {
        "page": 69,
        "workout_num": 5,
        "title": "Mixed Workout 5: Essential Workplace Homophones",
        "coverage": "Units 22 to 24: Their/There/They're, Two/To/Too, Hear/Here, Wear/Where, New/Knew",
        "intro": "Homophones sound identical but carry completely different spellings and definitions. Prove your mastery across all three Level 1 homophone clusters in formal business memos.",
        "drills": [
            {
                "section": "[PART A] Homophone Discrimination Drills (4 Marks)",
                "items": [
                    ("Choose the sentence that uses <em>their, there</em>, and <em>they're</em> correctly:",
                     ["A) They're leaving their tools over there by the workbench.", "B) Their leaving they're tools over there by the workbench.", "C) They're leaving there tools over their by the workbench."], "A"),
                    ("Which sentence uses <em>to, too</em>, and <em>two</em> accurately?",
                     ["A) We sent two drivers to the depot, but the truck was too full.", "B) We sent to drivers too the depot, but the truck was to full.", "C) We sent two drivers too the depot, but the truck was to full."], "A"),
                    ("Select the sentence with correct sensory/spatial homophones:",
                     ["A) Stand here so you can hear where to wear your ear defenders.", "B) Stand hear so you can here wear to where your ear defenders.", "C) Stand here so you can hear wear to wear your ear defenders."], "A"),
                    ("Identify the sentence using <em>knew</em> and <em>new</em> correctly:",
                     ["A) The manager knew that the new machinery had arrived.", "B) The manager new that the knew machinery had arrived.", "C) The manager knew that the knew machinery had arrived."], "A")
                ]
            },
            {
                "section": "[PART B] Homophone Cloze Sentence Completion (3 Marks)",
                "items": [
                    ("Insert there, their, or they're", "All employees must park [______] vehicles over [______]", "their / there"),
                    ("Insert to, too, or two", "The parcel was [______] heavy for [______] people [______] lift", "too / two / to"),
                    ("Insert wear, where, hear, or here", "Please stand [______] and check [______] you must [______] PPE", "here / where / wear")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Check this staff bulletin concerning site safety and personal protective gear. Identify exactly 5 homophone errors.",
                "text": "Safety Reminder: All factory workers must collect there new high-visibility jackets from the storage room over their. If you cannot here the fire evacuation siren, report to reception immediately. Staff must check the board to see wear they should wear their hard hats. It is to noisy in Bay 1 for verbal instructions.",
                "err_count": 5
            }
        ]
    },

    # Page 70: Workout 6 (Units 25–26)
    {
        "page": 70,
        "workout_num": 6,
        "title": "Mixed Workout 6: Prefixes, Suffixes & Word Formation",
        "coverage": "Units 25 & 26: Prefixes (un-, dis-, mis-, re-) and Suffixes (-ful, -less, -ly, -ment)",
        "intro": "Morphology governs how words expand and modify meaning. Test your ability to attach prefixes and suffixes cleanly without letter duplications or drop errors.",
        "drills": [
            {
                "section": "[PART A] Morphology Discrimination Drills (4 Marks)",
                "items": [
                    ("Which word is spelled correctly with the prefix <em>'dis-'</em>?",
                     ["A) dissconnected", "B) disconnected", "C) dis-connected"], "B"),
                    ("What is the correct spelling when attaching the suffix <em>'-ful'</em> to <em>'care'</em>?",
                     ["A) carefull", "B) careful", "C) carefullly"], "B"),
                    ("How is the adverb formed from the adjective <em>'polite'</em>?",
                     ["A) politely", "B) politeley", "C) politly"], "A"),
                    ("Select the noun correctly formed by adding <em>'-ment'</em> to <em>'manage'</em>:",
                     ["A) managment", "B) management", "C) manage-ment"], "B")
                ]
            },
            {
                "section": "[PART B] Suffix & Prefix Formation (3 Marks)",
                "items": [
                    ("Add 'mis-' to 'calculate'", "The clerk made an error when he [mis + calculate] the invoice total.", "miscalculated"),
                    ("Add '-ly' to 'successful'", "The surgical team [successful + ly] completed the operation.", "successfully"),
                    ("Add '-ment' to 'develop'", "The apprentice showed rapid [develop + ment] in bricklaying.", "development")
                ]
            },
            {
                "section": "[PART C] Forensic Multi-Error Proofreading (5 Marks)",
                "scenario": "Proofread this formal appraisal report written by a customer service supervisor. Identify exactly 5 prefix and suffix spelling errors.",
                "text": "Appraisal Summary: Liam has been a carefull and helpfull member of the support desk. When clients were dissappointed with delayed deliveries, he responded politeley and resolved issues promptley. He noticed that an invoice had been misscalculated and corrected it before submission.",
                "err_count": 5
            }
        ]
    }
]


# =============================================================================
# 4. OFFICIAL EXAM PROOFREADING & EXTENDED WRITING MOCKS (PAGES 71–76: 6 PAGES)
# =============================================================================

EXAM_MOCKS = [
    # Mock 1: Pages 71 & 72
    {
        "mock_num": 1,
        "page_proof": 71,
        "page_writing": 72,
        "title": "Official Exam Mock 1: Health & Safety Incident Investigation",
        "subtitle": "Pearson Edexcel / City & Guilds Level 1 Calibrated Writing Paper",
        "format": "Formal Incident Log & Management Report",
        "proof_scenario": {
            "title": "TASK 1: PROOFREADING AN OFFICIAL INCIDENT REPORT (6 MARKS)",
            "context": "You are an assistant safety marshal at Oakridge Distribution Centre. A colleague has submitted an urgent incident report following a warehouse accident. The text contains exactly 6 deliberate SPaG errors (capitalisation, comma splices/run-ons, past verb spelling, homophones, and apostrophes). Identify and correct all 6 errors in the error log table below.",
            "doc_meta": "REPORT REF: HSE-L1-2026-08 | LOCATION: Bay 3 Packing Line | DATE: 24 October 2026",
            "text": "On monday morning, an incident occurred near the central packaging conveyor. An operative sliped on a patch of hydraulic oil that leaked from Forklift 2. The worker bruised his right wrist, he reported to the medical room immediately. The warehouse supervisor inspected the worker's lockers to ensure dry clothing was available. Yellow warning cones was placed around the hazard to prevent further slips. The team must store there tools in the designated locker.",
            "err_count": 6
        },
        "writing_task": {
            "title": "TASK 1 (CONTINUED): EXTENDED FORMAL WRITING (12 MARKS)",
            "marks_breakdown": "6 Marks for SPaG (Punctuation, Agreement, Spelling) &bull; 6 Marks for Format, Cohesion & Clarity",
            "prompt": "Write a formal summary report (approx. 80–110 words) for the Health and Safety Committee explaining the incident and recommending two actions to prevent future accidents. Your report must include: a clear headline, details of what happened, two preventative measures, correct capital letters and full stops, and accurate past tense verbs.",
            "ruled_lines_count": 16
        }
    },

    # Mock 2: Pages 73 & 74
    {
        "mock_num": 2,
        "page_proof": 73,
        "page_writing": 74,
        "title": "Official Exam Mock 2: Customer Service Complaint Resolution",
        "subtitle": "Highfield / NCFE Calibrated Level 1 Practical Writing Assessment",
        "format": "Customer Service Letter of Rectification",
        "proof_scenario": {
            "title": "TASK 2: PROOFREADING A CUSTOMER COMPLAINT RESPONSE (6 MARKS)",
            "context": "You are a customer resolutions coordinator for Sovereign Electronics in Leeds. A trainee advisor drafted this response to an unhappy customer whose refrigerator delivery was delayed and damaged. The draft contains exactly 6 deliberate SPaG errors (punctuation, spelling, verb agreement, and non-standard English). Identify each error in the table provided.",
            "doc_meta": "LETTER REF: CUST-RES-7709 | CUSTOMER: Mrs H. Thornton | DATE: 18 November 2026",
            "text": "Dear Mrs Thornton, Thank you for contacting our customer care department yesterday! We have investigated your complaint regarding order ref EL-994. The courier driver seen the damage but failed to report it to dispatch. There is two replacement appliances reserved in our regional warehouse. We would of contacted you sooner if the tracking system had updated. Our company apologise for the delay and will refund your delivery charge.",
            "err_count": 6
        },
        "writing_task": {
            "title": "TASK 2 (CONTINUED): EXTENDED FORMAL LETTER (12 MARKS)",
            "marks_breakdown": "6 Marks for SPaG &bull; 6 Marks for Professional Tone, Addressing Customer Points & Solution",
            "prompt": "Write a formal letter (approx. 80–110 words) to Mrs Thornton formally confirming the delivery date of the replacement refrigerator and offering compensation. You must include: professional letter layout (addresses, date, greeting, sign-off), clear statement of replacement delivery, an offer of compensation, and 100% Standard English.",
            "ruled_lines_count": 16
        }
    },

    # Mock 3: Pages 75 & 76
    {
        "mock_num": 3,
        "page_proof": 75,
        "page_writing": 76,
        "title": "Official Exam Mock 3: Workplace Policy & Staff Briefing Memo",
        "subtitle": "Ofqual Functional Skills English Level 1 Writing Paper",
        "format": "Internal Company Policy Briefing Memo",
        "proof_scenario": {
            "title": "TASK 3: PROOFREADING AN INTERNAL POLICY DIRECTIVE (6 MARKS)",
            "context": "Review this staff briefing memo prepared by an assistant office manager regarding new security and visitor badge protocols. The memo contains exactly 6 deliberate SPaG errors (sentence boundary run-on, missing commas after introductory time phrases, homophones, prefix spelling, and pronoun shifts). Record all 6 errors in the correction table.",
            "doc_meta": "MEMO REF: POL-SEC-2026 | TO: All Staff | FROM: Facilities Directorate | DATE: 2 December 2026",
            "text": "Please note that from next Monday all employees must wear their photo ID badges at all times. In the event of an emergency security staff must be able to verify your identity. Staff can collect there new electronic keycards from reception before Friday noon. When a visitor arrives you must escort them to Meeting Room 4. If employees notice unapproved guests, you should notify security immediately.",
            "err_count": 6
        },
        "writing_task": {
            "title": "TASK 3 (CONTINUED): EXTENDED STAFF EMAIL (12 MARKS)",
            "marks_breakdown": "6 Marks for SPaG &bull; 6 Marks for Communication, Clear Bullet Points & Purpose",
            "prompt": "Write an internal email (approx. 80–110 words) to your department team explaining the new security badge procedure and reminding them of three vital steps. Include: appropriate subject line and professional greeting, explanation of why security is important, three clear bulleted instructions, and consistent pronouns throughout.",
            "ruled_lines_count": 16
        }
    }
]


# =============================================================================
# 5. COMPREHENSIVE EXPLANATORY ANSWER KEY (PAGES 77–82: 6 PAGES)
# =============================================================================

ANSWER_KEYS_6P = {
    # Page 77: Key 1
    "page_77": {
        "title": "Explanatory Answer Key 1: Diagnostic Assessment & Units 1 to 5",
        "diagnostic_answers": [
            "1. B (Capitalised 'The', ends with full stop '.')",
            "2. B (Full stop splits two distinct independent thoughts into separate sentences)",
            "3. A (Polite enquiry starting with auxiliary 'Could' requires a question mark '?')",
            "4. A (Urgent hazard warning requires single exclamation mark '!')",
            "5. B (Tuesday, October, City Hospital are all proper nouns requiring capitals)",
            "6. B (Pronoun 'I' and initialisms NHS / PPE are always capitalised)",
            "7. B (Shows contrast between arriving on time and being damaged)",
            "8. A ('so' demonstrates direct consequence / logical result)",
            "9. B (Middle 'because' links subordinate clause smoothly without comma)",
            "10. B (Introductory subordinate clause requires a comma before the main clause)",
            "11. B (Commas separate list items; 'and' joins the final item)",
            "12. B (Introductory time phrase 'Last Monday morning,' requires a comma)",
            "13. B (Apostrophes sit between 'n' and 't' to replace 'o': shouldn't, don't)",
            "14. B ('It's' = 'It is' essential)",
            "15. A (Singular possession: one supplier's invoice)",
            "16. B (Hissing sound -x adds -es: boxes)",
            "17. B (Irregular plurals: men and children; no -s added)",
            "18. B (Consonant+y &rarr; companies; vowel+y &rarr; holidays)",
            "19. B (Plural owners ending in -s take terminal apostrophe only: drivers')",
            "20. A (Singular third person subject 'caretaker' requires -s: inspects)",
            "21. B (Present continuous needs auxiliary 'is' + base verb + -ing: is repairing)",
            "22. B (CVC 1-syllable doubling rule: slipped / stopped)",
            "23. B (Standard English past: saw and wrote; not seen/writed)",
            "24. B (Pre-planned intention: are going to upgrade)",
            "25. B (Plural subject 'both apprentices' takes plural past verb 'were')",
            "26. C (Plural noun 'valves' requires plural 'There are')",
            "27. B (Consistent third-person plural: employees &rarr; they / their)",
            "28. B (Standard English past 'did'; avoids double negative)",
            "29. B (their = possession; there = location)",
            "30. A (too = excessive; two = 2; to = preposition)",
            "31. A (wear = clothing/PPE; where = location; here = place)",
            "32. A (dis- + connect = disconnected; careful + ly = carefully)"
        ],
        "units": {
            1: {"ex_a": "1. B | 2. B | 3. C | 4. A", "ex_b": "1. The delivery docket was signed by the depot manager. 2. Safety helmets are mandatory. Visitors must sign in. 3. Before entering the packing line, staff must wash their hands.", "proof": "1. 'all' &rarr; 'All' | 2. 'the night' &rarr; 'The night' | 3. 'delays the main' &rarr; 'delays. The main' | 4. 'bay 2' &rarr; 'bay 2.'"},
            2: {"ex_a": "1. B | 2. A | 3. B | 4. B", "ex_b": "1. ...Thursday? 2. ...today. Have a lovely weekend. 3. Danger! Do not enter while machinery is in operation.", "proof": "1. 'today!' &rarr; 'today.' | 2. 'postcode.' &rarr; 'postcode?' | 3. 'regional hub!' &rarr; 'regional hub.' | 4. 'tomorrow morning.' &rarr; 'tomorrow morning?'"},
            3: {"ex_a": "1. B | 2. C | 3. B | 4. C", "ex_b": "1. The staff training commences on Friday, 4 November. 2. Yesterday I met David Brown at Leeds Central Station. 3. All warehouse visitors must report to HR and wear PPE.", "proof": "1. 'apex health centre' &rarr; 'Apex Health Centre' | 2. 'on thursday' &rarr; 'On Thursday' | 3. 'ms claire taylor' &rarr; 'Ms Claire Taylor' | 4. 'bath college' &rarr; 'Bath College' | 5. 'all delegates' &rarr; 'All delegates'"},
            4: {"ex_a": "1. B | 2. C | 3. A | 4. A", "ex_b": "1. The technician tested the heating unit, but it failed the safety check. 2. The delivery lorry arrived early, so the stock team unloaded the goods. 3. Staff can book annual leave by email, or they can complete a paper form.", "proof": "1. 'at 09:30 and the manager' &rarr; 'at 09:30, so the manager' | 2. 'within twenty minutes so he did not' &rarr; 'within twenty minutes, but he did not' | 3. 'halt work on Bay 4 but the team' &rarr; 'halt work on Bay 4, so the team' | 4. 'for repairs and they could clean' &rarr; 'for repairs, or they could clean'"},
            5: {"ex_a": "1. B | 2. B | 3. A | 4. B", "ex_b": "1. Because the heating system broke down, the clinic postponed appointments. 2. Leon passed his driving test although he was extremely nervous. 3. When the supervisor signs the form, you can collect your safety boots.", "proof": "1. 'ago. He has' &rarr; 'ago, he has' | 2. 'skills he was' &rarr; 'skills, he was' | 3. 'thoroughly, when he' &rarr; 'thoroughly when he' | 4. 'requests Jack' &rarr; 'requests, Jack'"}
        }
    },

    # Page 78: Key 2
    "page_78": {
        "title": "Explanatory Answer Key 2: Units 6 to 11",
        "units": {
            6: {"ex_a": "1. B | 2. A | 3. A | 4. A", "ex_b": "1. The tool chest holds pliers, screwdrivers, wire strippers and a tape measure. 2. Every morning we inspect the forklift and clean the loading bay. 3. He unlocked the door, turned on the lights and checked the safe.", "proof": "1. 'carrots potatoes onions' &rarr; 'carrots, potatoes, onions' | 2. 'olive oil, and plain' &rarr; 'olive oil and plain' | 3. 'inspect the crates verify' &rarr; 'inspect the crates, verify' | 4. 'vegetables, and chop' &rarr; 'vegetables and chop'"},
            7: {"ex_a": "1. B | 2. B | 3. B | 4. A", "ex_b": "1. Last Friday, our team completed the quarterly stocktake. 2. In addition, staff must wear protective eyewear in the machining bay. 3. In the event of a power cut, do not use the passenger lifts.", "proof": "1. 'continuous alarm staff' &rarr; 'continuous alarm, staff' | 2. 'personal coats or bags walk' &rarr; 'personal coats or bags, walk' | 3. 'circumstances should' &rarr; 'circumstances, should' | 4. 'Outside the building report' &rarr; 'Outside the building, report'"},
            8: {"ex_a": "1. B | 2. A | 3. A | 4. B", "ex_b": "1. they haven't received the delivery 2. the driver wasn't able to reverse into bay 3 3. It's essential that all doors remain locked.", "proof": "1. 'isnt' &rarr; 'isn't' | 2. 'could'nt' &rarr; 'couldn't' | 3. 'weve' &rarr; 'we've' | 4. 'should'nt' &rarr; 'shouldn't'"},
            9: {"ex_a": "1. B | 2. A | 3. A | 4. B", "ex_b": "1. the nurse's locker 2. We received the client's signature on yesterday's contract. 3. The delivery van has lost its front registration plate.", "proof": "1. 'visitors wallet' &rarr; 'visitor's wallet' | 2. 'drivers licence' &rarr; 'driver's licence' | 3. 'cleaner mop' &rarr; 'cleaner's mop' | 4. 'guest child' &rarr; 'guest's child'"},
            10: {"ex_a": "1. B | 2. B | 3. A | 4. C", "ex_b": "1. taxes / glasses 2. Several people and their children attended the family open day. 3. Please stack the pallets and wash the trays.", "proof": "1. 'floor's' &rarr; 'floors' | 2. 'basin's' &rarr; 'basins' | 3. 'stalles' &rarr; 'stalls' | 4. 'security mans... supply boxs' &rarr; 'security men... supply boxes'"},
            11: {"ex_a": "1. B | 2. A | 3. A | 4. B", "ex_b": "1. factories / facilities 2. journeys / trays 3. Staff must review all safeguarding policies before taking their annual holidays.", "proof": "1. 'facilitays' &rarr; 'facilities' | 2. 'holidaies' &rarr; 'holidays' | 3. 'delaies' &rarr; 'delays' | 4. 'categorise' &rarr; 'categories'"}
        }
    },

    # Page 79: Key 3
    "page_79": {
        "title": "Explanatory Answer Key 3: Units 12 to 17",
        "units": {
            12: {"ex_a": "1. B | 2. A | 3. B | 4. A", "ex_b": "1. the teachers' changing room 2. the workers' union 3. We painted the women's staff room yesterday.", "proof": "1. 'courier's vehicles' &rarr; 'couriers' vehicles' | 2. 'worker's rest room' &rarr; 'workers' rest room' | 3. 'drivers's kitchen' &rarr; 'drivers' kitchen' | 4. 'childrens' charity' &rarr; 'children's charity'"},
            13: {"ex_a": "1. A | 2. B | 3. B | 4. B", "ex_b": "1. The supervisor inspects the safety log every Friday. 2. The technician washes his hands and goes to the staff room. 3. Every evening, the cleaner empties all the office recycling bins.", "proof": "1. 'worker arrive' &rarr; 'worker arrives' | 2. 'review... dispense' &rarr; 'reviews... dispenses' | 3. 'assistant restock' &rarr; 'assistant restocks' | 4. 'members signs' &rarr; 'members sign'"},
            14: {"ex_a": "1. B | 2. B | 3. B | 4. C", "ex_b": "1. The network administrator is installing security patches at present. 2. The database backup is stopping due to a connection error. 3. Our team is writing a summary incident report for management.", "proof": "1. 'engineers currently investigating' &rarr; 'engineers are currently investigating' | 2. 'configureing' &rarr; 'configuring' | 3. 'technicians is' &rarr; 'technicians are' | 4. 'runing' &rarr; 'running'"},
            15: {"ex_a": "1. B | 2. B | 3. B | 4. A", "ex_b": "1. stopped / dropped 2. tidied / emptied 3. noticed / closed", "proof": "1. 'sliped' &rarr; 'slipped' | 2. 'droped' &rarr; 'dropped' | 3. 'stoped' &rarr; 'stopped' | 4. 'hurryed' &rarr; 'hurried'"},
            16: {"ex_a": "1. B | 2. C | 3. A | 4. A", "ex_b": "1. told / gave 2. saw / spoke 3. The engineer did the repairs and wrote the certificate.", "proof": "1. 'seen that' &rarr; 'saw that' | 2. 'someone broke' &rarr; 'someone broke' (correct; 'taked' &rarr; 'took') | 3. 'taked three' &rarr; 'took three' | 4. 'runned towards' &rarr; 'ran towards'"},
            17: {"ex_a": "1. B | 2. A | 3. B | 4. A", "ex_b": "1. Next Monday, our company is going to upgrade its payment terminals. 2. Apex Solutions will guarantee delivery within forty-eight hours. 3. The supervisor will inspect the work area before signing off.", "proof": "1. 'are please' &rarr; 'are pleased' | 2. 'team going to' &rarr; 'team is going to' | 3. 'will arrived' &rarr; 'will arrive' | 4. 'will ensuring' &rarr; 'will ensure'"}
        }
    },

    # Page 80: Key 4
    "page_80": {
        "title": "Explanatory Answer Key 4: Units 18 to 22",
        "units": {
            18: {"ex_a": "1. A | 2. B | 3. B | 4. B", "ex_b": "1. Both security cameras were disabled during the power surge. 2. The list of approved suppliers is pinned to the staff noticeboard. 3. The apprentice and the technician were commended for their quick response.", "proof": "1. 'representative and the employee was' &rarr; 'were' | 2. 'folder of grievance documents were' &rarr; 'was' | 3. 'Both committee members was' &rarr; 'were' | 4. 'The employee were advised' &rarr; 'was'"},
            19: {"ex_a": "1. B | 2. B | 3. A | 4. B", "ex_b": "1. There are six replacement air filters on Shelf B. 2. There was only one fire extinguisher in the corridor. 3. There are three visitors waiting at the security gate.", "proof": "1. 'there was four discrepancies' &rarr; 'there were' | 2. 'There is two damaged pallets' &rarr; 'There are' | 3. 'there was thirty units' &rarr; 'there were' | 4. 'there are no immediate delay' &rarr; 'there is'"},
            20: {"ex_a": "1. B | 2. B | 3. B | 4. A", "ex_b": "1. When you lift a heavy box, you must bend your knees. 2. If an apprentice needs advice, they should consult their mentor. 3. Our company values our staff and we reward our team's hard work.", "proof": "1. 'an employee... you should' &rarr; 'they should' | 2. 'They should discuss your concerns' &rarr; 'their concerns' | 3. 'If workers need... you can access' &rarr; 'they can access' | 4. 'whenever one needs' &rarr; 'whenever they need'"},
            21: {"ex_a": "1. B | 2. B | 3. B | 4. A", "ex_b": "1. The technician did all the electrical tests this morning. 2. Our team would have completed the order if the power stayed on. 3. The warehouse team has no spare safety helmets.", "proof": "1. 'team done everything' &rarr; 'did everything' | 2. 'We seen the courier' &rarr; 'We saw the courier' | 3. 'should of notified' &rarr; 'should have notified' | 4. 'ain't got no records' &rarr; 'do not have any records'"},
            22: {"ex_a": "1. B | 2. B | 3. A | 4. B", "ex_b": "1. their 2. There 3. they're", "proof": "1. 'over their' &rarr; 'over there' | 2. 'they're personal files' &rarr; 'their personal files' | 3. 'Their are twenty' &rarr; 'There are twenty' | 4. 'collect from reception' (check consistency)"}
        }
    },

    # Page 81: Key 5
    "page_81": {
        "title": "Explanatory Answer Key 5: Units 23 to 26 & Vocabulary Modules 1 to 6",
        "units": {
            23: {"ex_a": "1. C | 2. B | 3. A | 4. B", "ex_b": "1. too 2. to 3. two", "proof": "1. 'pleased too provide' &rarr; 'pleased to provide' | 2. 'allocated to senior' &rarr; 'allocated two senior' | 3. 'is to old' &rarr; 'is too old' | 4. 'supply those to' &rarr; 'supply those too'"},
            24: {"ex_a": "1. B | 2. C | 3. A | 4. A", "ex_b": "1. here / hear 2. where / wear 3. knew / new", "proof": "1. 'located hear' &rarr; 'located here' | 2. 'cannot here verbal' &rarr; 'cannot hear verbal' | 3. 'to see wear' &rarr; 'to see where' | 4. 'required to where' &rarr; 'required to wear'"},
            25: {"ex_a": "1. C | 2. B | 3. B | 4. A", "ex_b": "1. misplace 2. disconnect 3. rebuild", "proof": "1. 'dissconnected' &rarr; 'disconnected' | 2. 'missread' &rarr; 'misread' | 3. 'uncorrect' &rarr; 'incorrect' | 4. 'retest' is correct; verify 4 error adjustments"},
            26: {"ex_a": "1. B | 2. A | 3. B | 4. A", "ex_b": "1. skilful / skillful 2. promptly 3. development", "proof": "1. 'powerfull' &rarr; 'powerful' | 2. 'politeley' &rarr; 'politely' | 3. 'helpfull' &rarr; 'helpful' | 4. 'developement' &rarr; 'development'"}
        },
        "vocab_modules": {
            1: "Informal to formal transformation: 'Dear Mr Jenkins, I am writing to request that we reschedule our meeting, as I need to investigate an issue with the delivery vehicle.'",
            2: "Completed instruction: 'Wearing full PPE is mandatory in this workshop because all stored chemicals are highly flammable.'",
            3: "Collocation rewrite: 'I am writing on behalf of my manager to resolve the discrepancy in the invoice before the deadline.'",
            4: "Customer service rewrite: 'While store policy requires a receipt for cash refunds, I would be delighted to provide you with a store credit voucher to rectify the issue.'",
            5: "Spelling rule applications: relied | dropping | receive | shelves",
            6: "Correct words: necessary | business | tomorrow | definitely"
        }
    },

    # Page 82: Key 6
    "page_82": {
        "title": "Explanatory Answer Key 6: Mixed Workouts 1 to 6 & Exam Mocks 1 to 3",
        "mixed_workouts": {
            1: {"part_a": "1. B | 2. A | 3. B | 4. A", "part_b": "1. ...flooded, so the supervisor... 2. Although the apprentice was nervous, he passed... 3. Yesterday morning, our catering team ordered bread, butter, eggs and milk.", "part_c": "1. 'welcome' &rarr; 'Welcome' | 2. 'weekday it' &rarr; 'weekday. It' | 3. 'spacious please' &rarr; 'spacious, please' | 4. 'on fridays' &rarr; 'On Fridays' | 5. 'early, staff' &rarr; 'early. Staff'"},
            2: {"part_a": "1. A | 2. A | 3. B | 4. A", "part_b": "1. They can't attend because it's too late. 2. the plumbers' tools 3. The women's locker room was refurbished last month.", "part_c": "1. 'contractor's' &rarr; 'contractors' | 2. 'workers locker' &rarr; 'workers' locker' | 3. 'electricans drill' &rarr; 'electrician's drill' | 4. 'torchs' &rarr; 'torches' | 5. 'cant' &rarr; 'can't'"},
            3: {"part_a": "1. A | 2. B | 3. B | 4. B", "part_b": "1. brought / left 2. is going to launch 3. running", "part_c": "1. 'notice' &rarr; 'noticed' | 2. 'seen that' &rarr; 'saw that' | 3. 'runing' &rarr; 'running' | 4. 'stoped' &rarr; 'stopped' | 5. 'writed' &rarr; 'wrote'"},
            4: {"part_a": "1. B | 2. A | 3. B | 4. B", "part_b": "1. ...parts was delivered... 2. ...team has no spare... 3. I did the cleaning and saw...", "part_c": "1. 'representative was' &rarr; 'were' | 2. 'there was four' &rarr; 'there were' | 3. 'worker stacks... you must' &rarr; 'they must' | 4. 'team leader done' &rarr; 'did' | 5. 'didn't receive no' &rarr; 'did not receive any'"},
            5: {"part_a": "1. A | 2. A | 3. A | 4. A", "part_b": "1. their / there 2. too / two / to 3. here / where / wear", "part_c": "1. 'there new' &rarr; 'their new' | 2. 'over their' &rarr; 'over there' | 3. 'here the fire' &rarr; 'hear the fire' | 4. 'see wear' &rarr; 'see where' | 5. 'to noisy' &rarr; 'too noisy'"},
            6: {"part_a": "1. B | 2. B | 3. A | 4. B", "part_b": "1. miscalculated 2. successfully 3. development", "part_c": "1. 'carefull' &rarr; 'careful' | 2. 'helpfull' &rarr; 'helpful' | 3. 'dissappointed' &rarr; 'disappointed' | 4. 'politeley' &rarr; 'politely' | 5. 'promptley' &rarr; 'promptly'"}
        },
        "exam_mocks": {
            1: {
                "proof_answers": [
                    "1. 'monday' &rarr; 'Monday' (Capital letter for day of week)",
                    "2. 'sliped' &rarr; 'slipped' (Double 'p' after single short vowel in CVC verb)",
                    "3. 'wrist, he reported' &rarr; 'wrist. He reported' (Comma splice correction)",
                    "4. 'worker's lockers' &rarr; 'workers' lockers' (Plural possessive for multiple workers)",
                    "5. 'cones was placed' &rarr; 'cones were placed' (Subject-verb agreement: plural subject takes 'were')",
                    "6. 'there tools' &rarr; 'their tools' (Possessive pronoun required)"
                ],
                "writing_rubric": "Band 3 (5–6 Marks SPaG): Flawless sentence boundaries, correct capitalisation of proper nouns, past simple tense consistency (occurred, slipped, inspected, recommended), correct spelling of vocational words (maintenance, precaution, hazard). Band 3 (5–6 Marks Content): Headline present, clear sequence of events, two realistic preventative measures (e.g. non-slip mats, daily forklift leak checks)."
            },
            2: {
                "proof_answers": [
                    "1. 'yesterday!' &rarr; 'yesterday.' (Over-enthusiastic exclamation mark removed for formal letter)",
                    "2. 'seen the damage' &rarr; 'saw the damage' (Standard English simple past)",
                    "3. 'There is two' &rarr; 'There are two' (Existential agreement with plural noun 'appliances')",
                    "4. 'would of' &rarr; 'would have' (Phonetic spelling error corrected)",
                    "5. 'company apologise' &rarr; 'company apologises' (Singular collective noun agreement)",
                    "6. Missing or punctuation adjustments"
                ],
                "writing_rubric": "Band 3 (5–6 Marks SPaG): Full formal letter conventions (Dear Mrs Thornton / Yours sincerely), zero non-standard slang, precise punctuation, complex sentence joining (although, because). Band 3 (5–6 Marks Content): Clear confirmation of replacement delivery date, professional apology, specific goodwill gesture or discount offered."
            },
            3: {
                "proof_answers": [
                    "1. 'Monday all' &rarr; 'Monday, all' (Comma required after introductory time clause)",
                    "2. 'emergency security' &rarr; 'emergency, security' (Comma after introductory prepositional phrase)",
                    "3. 'there new' &rarr; 'their new' (Possessive homophone error)",
                    "4. 'arrives you' &rarr; 'arrives, you' (Comma following dependent 'when' clause)",
                    "5. 'employees notice... you should' &rarr; 'they should' (Pronoun consistency shift)",
                    "6. Sentence boundary / capitalisation adjustment"
                ],
                "writing_rubric": "Band 3 (5–6 Marks SPaG): Crisp bullet point punctuation, consistent second-person instructional pronouns (you/your), modal verbs (must, should). Band 3 (5–6 Marks Content): Clear email subject header, strong rationale for security, three actionable bullet points."
            }
        }
    }
}
