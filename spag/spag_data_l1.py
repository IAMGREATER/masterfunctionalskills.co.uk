"""
spag_data_l1.py - Complete Level 1 Educational Content Dataset
Includes:
- Full 10-Question Diagnostic Assessment & Scoring Matrix
- Realistic Mock Exam Proofreading Tasks 1 & 2 (Level 1 Exam Calibrated)
- Exhaustive Complete Answer Key (Pages 31 to 34)
"""

L1_DIAGNOSTIC = {
    "title": "Baseline Diagnostic Assessment: Level 1 SPaG Audit",
    "subtitle": "Complete this 10-minute diagnostic to determine your core punctuation, sentence structure, and spelling strengths.",
    "questions": [
        {"num": 1, "topic": "Unit 1: Capital Letters", "prompt": "Which sentence capitalises all proper nouns, days, and the pronoun 'I' correctly?", "options": ["A) Every tuesday, i travel to Leeds with mr Davies.", "B) Every Tuesday, I travel to Leeds with Mr Davies.", "C) Every tuesday, I travel to Leeds with Mr davies."], "correct": "B"},
        {"num": 2, "topic": "Unit 2: Full Stops & Run-ons", "prompt": "Identify the option that forms two complete, correctly punctuated sentences:", "options": ["A) The shop opened early today there were fifty customers waiting.", "B) The shop opened early today. There were fifty customers waiting.", "C) The shop opened early today, there were fifty customers waiting."], "correct": "B"},
        {"num": 3, "topic": "Unit 3: Question Marks & Exclamations", "prompt": "Which sentence requires an exclamation mark to signal urgent danger?", "options": ["A) Can you please check the fire exit door", "B) Warning! Flammable materials stored in this locker!", "C) The fire exit door is located on the second floor"], "correct": "B"},
        {"num": 4, "topic": "Unit 4: Commas in Lists", "prompt": "Select the sentence that uses commas correctly in a list:", "options": ["A) The toolkit contains hammers screwdrivers spanners, and pliers.", "B) The toolkit contains hammers, screwdrivers, spanners and pliers.", "C) The toolkit contains, hammers screwdrivers, spanners and pliers."], "correct": "B"},
        {"num": 5, "topic": "Unit 5: Contraction Apostrophes", "prompt": "Choose the sentence with correct contraction apostrophes:", "options": ["A) You shouldnt enter if you dont have your visitor badge.", "B) You shouldn't enter if you don't have your visitor badge.", "C) You should'nt enter if you do'nt have your visitor badge."], "correct": "B"},
        {"num": 6, "topic": "Unit 6: Possessive Apostrophes", "prompt": "Which sentence correctly shows that the locker belongs to one worker?", "options": ["A) The worker's locker was inspected by the supervisor.", "B) The workers locker was inspected by the supervisor.", "C) The workers's locker was inspected by the supervisor."], "correct": "A"},
        {"num": 7, "topic": "Unit 7: Complete Sentences", "prompt": "Which option is a complete sentence (not a fragment)?", "options": ["A) Because the delivery lorry arrived an hour late.", "B) When sorting the packages into the blue delivery bins.", "C) The driver unloaded all forty parcels onto the ramp."], "correct": "C"},
        {"num": 8, "topic": "Unit 8: Joining Words (Conjunctions)", "prompt": "Choose the best joining word: 'The team worked overtime, [______] the order was finished on time.'", "options": ["A) but", "B) so", "C) because"], "correct": "B"},
        {"num": 9, "topic": "Unit 9: Subject-Verb Agreement", "prompt": "Select the sentence with correct singular/plural verb matching:", "options": ["A) Both apprentices was awarded their certificates.", "B) Both apprentices were awarded their certificates.", "C) Both apprentices is awarded their certificates."], "correct": "B"},
        {"num": 10, "topic": "Unit 11: Everyday Homophones", "prompt": "Choose the correct words: 'Please put [______] jackets over [______].'", "options": ["A) there / their", "B) their / there", "C) they're / there"], "correct": "B"}
    ],
    "scoring": [
        {"range": "8 – 10 Marks", "status": "Strong Level 1 Foundation", "advice": "Focus on proofreading speed, complex punctuation (Units 4, 6 & 10), and exam accuracy."},
        {"range": "5 – 7 Marks", "status": "Developing SPaG Skills", "advice": "Carefully review sentence boundaries, subject-verb matching, and apostrophe rules (Units 2, 5, 6 & 9)."},
        {"range": "0 – 4 Marks", "status": "Priority Core Revision", "advice": "Work through all 11 units systematically using the Murphy 2-page practice spreads."}
    ]
}

L1_MOCK_TASK_1 = {
    "title": "Mixed Exam Proofreading Mock: Task 1 (6 Marks)",
    "subtitle": "Realistic Level 1 Workplace Health & Safety Incident Report",
    "scenario_title": "FACILITY INCIDENT LOG & MAINTENANCE REPORT",
    "context": "You are an assistant stock supervisor reviewing an accident report written by a warehouse colleague. The report contains exactly 6 deliberate SPaG errors (2 capital letter / full stop errors, 2 spelling errors, and 2 grammatical agreement / apostrophe errors). Identify and correct all 6 errors in the table provided.",
    "doc_meta": "REPORT: ACC-L1-2026 | LOCATION: Depot 4 | DATE: 18 October 2026",
    "text": "on monday morning, an incident occurred in the central packing bay. Mrs davies sliped on a patch of spilled cleaning fluid near Aisle 3. She hurt her left wrist, she was given first aid immediately. The warehouse floor were extremely wet because a pipe was leaking. The supervisor inspected the worker's lockers to check for dry uniforms. Yellow warning cones was placed around the hazard to prevent further slips.",
    "marks": 6
}

L1_MOCK_TASK_2 = {
    "title": "Mixed Exam Proofreading Mock: Task 2 (6 Marks)",
    "subtitle": "Formal Community Notice & Public Information Rewrite",
    "scenario_title": "COMMUNITY RECREATION CENTRE NOTICE & EVENT INVITATION",
    "context": "The public announcement below contains exactly 6 deliberate SPaG errors (capitalisation, run-on sentence, homophone, apostrophe, spelling, and verb tense). Identify each error and write out a corrected, publication-standard version in the lined workspace below.",
    "doc_meta": "NOTICE REF: COMM-2026 | AUTHOR: Recreation Coordinator | VENUE: Oak Tree Community Hub",
    "text": "Welcome to our new community garden project on station road. We are planting winter vegetables this saturday it will be great fun for local families. All volunteers must bring there own garden gloves. Its free to join and refreshments will be provided. Last week, our team planed forty fruit trees. Everyone who attended say that they enjoyed the fresh air.",
    "marks": 6
}

L1_ANSWERS = {
    "page_31": {
        "title": "Complete Answer Key: Diagnostic Assessment & Units 1 to 3",
        "diagnostic": [
            "1. B (Capital letters for Tuesday, I, Leeds, Mr Davies)",
            "2. B (Split into two independent sentences with full stop)",
            "3. B (Urgent warning requires exclamation marks: Warning! / !)",
            "4. B (Commas separate list items; and connects final item)",
            "5. B (Apostrophes replace missing 'o': shouldn't, don't)",
            "6. A (Singular possessive: worker's locker)",
            "7. C (Complete subject and verb expressing full thought)",
            "8. B ('so' expresses the logical result of working overtime)",
            "9. B (Plural subject 'Both apprentices' takes plural verb 'were')",
            "10. B ('their' shows possession; 'there' indicates location)"
        ],
        "unit_1": {
            "ex1": "1: B (The class starts at seven, so please arrive early) | 2: B (Every Tuesday, I travel to London with Mr Davies) | 3: A (Regular exercise boosts your energy it also...) | 4: C (Discover Your Hidden Talent at Our Town Workshop!)",
            "ex2": "1. In our neighbourhood, many friendly neighbours organise weekly social events. | 2. Our local leisure centre is very popular because it offers free swimming lessons. | 3. Next Friday, I will visit Leeds. It is a great city. | 4. To start the course, you must bring your passport and national insurance number.",
            "ex3": "Errors found (5 SPaG corrections): 1) why -> Why (headline capital) | 2) gardening -> Gardening (sentence opener) | 3) last month, i -> Last month, I (day/month/pronoun) | 4) exercise it also -> exercise. It also (run-on split) | 5) when you grow... vegetables. you save -> When you grow your own vegetables, you save (joined fragment)",
            "ex4_model": "Joining our local sports club is a fantastic way to stay healthy and make new friends. Every Thursday evening, Coach Martin leads beginner football training at Greenfields Leisure Centre."
        },
        "unit_2": {
            "ex1": "1: B (has completed) | 2: B (committee has approved) | 3: B (Both shift supervisors were happy...) | 4: A (Could you please confirm the delivery date?)",
            "ex2": "1. Both shift supervisors were happy with your progress. | 2. Could you please send me the inventory report today? | 3. The departmental manager is reviewing all annual leave applications. | 4. Either Sarah or Tom is attending the morning briefing.",
            "ex3": "Errors found (5 SPaG corrections): 1) Dear Mr Vance -> Dear Mr Vance, (comma after greeting) | 2) employees wishes -> employees wish (plural verb) | 3) can't -> cannot (formal register) | 4) proposal, it aligns -> proposal. It aligns (or ; it aligns) | 5) Yours Sincerely -> Yours sincerely (lowercase 's')",
            "ex4_model": "Dear Ms Jenkins, Could you please clarify whether the health and safety team has inspected the warehouse fire doors? Both shift leaders are keen to ensure that all emergency routes remain fully compliant. Yours sincerely, Alex Vance."
        },
        "unit_3": {
            "ex1": "1: B (Dear Mr Henderson, ... Yours sincerely,) | 2: A (Dear Sir or Madam, ... Yours faithfully,) | 3: B (comma after salutation) | 4: B (full stop inside quotation marks)",
            "ex2": "1. Dear Sir, ... Yours faithfully, | 2. I received your letter. I will reply tomorrow. | 3. The patient arrived at 09:00; she was examined immediately. | 4. Dear Dr Taylor, I am writing to express my appreciation.",
            "ex3": "Errors found (5 SPaG corrections): 1) Dear Mrs Campbell -> Dear Mrs Campbell, | 2) Drivers swerves -> Drivers swerve | 3) its very dangerous -> it's very dangerous | 4) sliped -> slipped (1-1-1 rule) | 5) Yours faithfully -> Yours sincerely (named recipient)",
            "ex4_model": "Dear Mr Harrison, I am writing to request that the facilities maintenance team repairs the leaking radiator in Room 4. The pooling water presents a slip hazard to staff and visitors. Yours sincerely, Jordan Reed."
        }
    },
    "page_32": {
        "title": "Complete Answer Key: Units 4 to 7",
        "unit_4": {
            "ex1": "1: B (Install... Repair...) | 2: A (Colon introduces bulleted list) | 3: B (Capital letter at start of each bullet) | 4: A (Consistent bullet syntax)",
            "ex2": "1. The equipment checklist includes the following items: torches, batteries, and radios. | 2. Bullet 1: Wear protective headgear at all times. | 3. Bullet 2: Report all near-miss incidents to your team leader. | 4. All operatives must follow these instructions: wash hands, wear aprons, and sanitize surfaces.",
            "ex3": "Errors found (5 SPaG corrections): 1) recommendations; -> recommendations: (colon required) | 2) non slip -> non-slip (hyphenated compound) | 3) exit doors! -> exit doors. (full stop for formal report) | 4) fire extinguishers was -> fire extinguishers were | 5) staff member's -> staff members (simple plural)",
            "ex4_model": "The quarterly safety inspection recommends the following measures:\n• Install high-visibility floor markings across all forklift transit corridors.\n• Replace damaged fire extinguisher brackets in Bay 2.\n• Ensure all employees wear steel-capped boots during loading operations."
        },
        "unit_5": {
            "ex1": "1: B (friendly and professional) | 2: B (balanced assessment) | 3: A (clear subheadings) | 4: B (evidence-based recommendations)",
            "ex2": "1. The restaurant offers prompt service and delicious meals; however, the seating area is rather cramped. | 2. In summary, I strongly recommend this training course to all new apprentices. | 3. The training manual was clear and well-organised. | 4. The customer service team resolved my billing query within twenty-four hours.",
            "ex3": "Errors found (5 SPaG corrections): 1) service was rubbish -> service was unsatisfactory | 2) food took ages -> order experienced substantial delays | 3) waiters was rude -> waiting staff were unhelpful | 4) sort it out -> resolve this grievance | 5) its unacceptable -> it's unacceptable",
            "ex4_model": "The introductory digital skills course provides excellent tuition for adult learners. The tutor explained computer shortcuts clearly, and the practical exercises built my confidence with spreadsheets. However, the classroom computers were occasionally slow to connect to the internet."
        },
        "unit_6": {
            "ex1": "1: A (Catchy title with subheadings) | 2: B (Bullet points for quick scanning) | 3: A (Imperative action verbs) | 4: B (Clear contact details at bottom)",
            "ex2": "1. Protect your home by locking all windows before leaving. | 2. For more information, visit our community website or call our helpline. | 3. Always wear reflective clothing when cycling after dark. | 4. Keep emergency numbers stored in your mobile phone.",
            "ex3": "Errors found (5 SPaG corrections): 1) how to stay healthy -> How to Stay Healthy (title case) | 2) exercise everyday it -> exercise every day. It (run-on) | 3) fruits vegetables and nuts -> fruits, vegetables, and nuts (list commas) | 4) dont forget -> don't forget (apostrophe) | 5) doctor's -> doctors (simple plural)",
            "ex4_model": "Top Tips for Household Recycling:\n• Rinse all plastic containers and tins before placing them in the green bin.\n• Flatten cardboard boxes to maximize bin capacity.\n• Never place household batteries or electrical goods in regular waste bins."
        },
        "unit_7": {
            "ex1": "1: B (Chronological order) | 2: A (First-person past tense) | 3: B (Linking words like then, next, finally) | 4: A (Clear time indicators)",
            "ex2": "1. First, I inspected the loading bay for safety hazards. | 2. Next, we unloaded twenty pallets from the delivery lorry. | 3. After finishing the stock count, I logged the quantities into the database. | 4. Finally, the supervisor signed the consignment clearance manifest.",
            "ex3": "Errors found (5 SPaG corrections): 1) At 11:20 AM, Mrs Davies slip -> slipped (past tense) | 2) She fall heavily -> fell (irregular past) | 3) hurted her wrist -> hurt (irregular past) | 4) first aider -> first-aider (hyphen) | 5) warning cones was -> cones were (subject-verb agreement)",
            "ex4_model": "Yesterday morning, I conducted the opening vehicle checks at the logistics depot. First, I verified tyre pressure and fluid levels across all five delivery vans. Next, I completed the pre-departure checklist and reported a minor headlight fault on Van 3. Finally, all vehicles departed on schedule."
        }
    },
    "page_33": {
        "title": "Complete Answer Key: Units 8 to 11",
        "unit_8": {
            "ex1": "1: A (Engaging rhetorical opening) | 2: B (Clear signposting for listeners) | 3: A (Inclusive pronouns like 'we' and 'our') | 4: B (Memorable conclusion)",
            "ex2": "1. Good morning everyone, and thank you for attending today's briefing. | 2. Today, I want to talk to you about the importance of workplace wellbeing. | 3. In conclusion, every small action contributes to a safer working environment. | 4. We must work together to achieve our environmental targets.",
            "ex3": "Errors found (5 SPaG corrections): 1) good morning colleagues -> Good morning, colleagues, | 2) today i want -> today I want | 3) our safety record are -> our safety record is | 4) listen careful -> listen carefully | 5) thank you all! -> Thank you all.",
            "ex4_model": "Good morning team. Today, I would like to introduce our new recycling initiative across the office. By sorting paper and plastics correctly, we can reduce departmental waste by forty percent. Let us work together to make our workspace cleaner and greener. Thank you."
        },
        "unit_9": {
            "ex1": "1: B (Informative title and date) | 2: A (Conversational yet professional tone) | 3: B (Clear paragraph breaks) | 4: A (Inviting reader interaction)",
            "ex2": "1. Welcome back to my blog about sustainable living in the city. | 2. Have you ever wondered how much food waste your household produces each week? | 3. Feel free to leave your thoughts and practical tips in the comments below. | 4. In my next post, I will share three simple budget recipes.",
            "ex3": "Errors found (5 SPaG corrections): 1) why cycling to work is great -> Why Cycling to Work is Great | 2) last year i bought -> Last year, I bought | 3) my bikes chain -> my bike's chain | 4) rideing -> riding | 5) leave a comment below? -> leave a comment below.",
            "ex4_model": "Welcome to my weekly blog on apprenticeships in healthcare. Balancing practical clinic shifts with online study can seem daunting at first; however, establishing a structured weekly schedule makes all the difference. What revision techniques work best for you? Let me know in the comments below."
        },
        "unit_10": {
            "ex1": "1: B (Clear headline in bold) | 2: A (Urgent instructions and dates) | 3: B (Professional administrative sign-off) | 4: A (Bulleted key requirements)",
            "ex2": "1. Please note that the main car park will be closed for resurfacing on Friday. | 2. All visitors must sign the register at main reception. | 3. Vehicles parked without a valid permit will be clamped. | 4. By order of the Facilities Management Committee.",
            "ex3": "Errors found (5 SPaG corrections): 1) NOTICE: staff car park closure -> NOTICE: Staff Car Park Closure | 2) will be close -> will be closed | 3) Friday 24th october -> Friday 24th October | 4) contractors machinery -> contractors' machinery | 5) park at your own risk! -> park at your own risk.",
            "ex4_model": "IMPORTANT NOTICE: FIRE ALARM TESTING\nPlease be advised that routine testing of the building fire alarm system will occur on Wednesday 28 October between 10:00 and 10:30. The sirens will sound intermittently. Evacuation is not required unless the alarm sounds continuously for more than thirty seconds."
        },
        "unit_11": {
            "ex1": "1: A (Concise overview) | 2: B (Step-by-step numbered instructions) | 3: A (Clear bold warnings) | 4: B (Glossary of technical terms)",
            "ex2": "1. Step 1: Switch off the power supply before removing the protective casing. | 2. Step 2: Use the specialist screwdriver to loosen the mounting brackets. | 3. Step 3: Inspect the internal wiring for signs of thermal damage. | 4. Step 4: Secure the replacement fuse and test the circuit breaker.",
            "ex3": "Errors found (5 SPaG corrections): 1) guide to safe lifting -> Guide to Safe Lifting | 2) bend your knees, do not bend your back -> bend your knees; do not bend your back | 3) heavy boxes should be lifted careful -> lifted carefully | 4) ask a colleague for help! -> ask a colleague for help. | 5) team work -> teamwork",
            "ex4_model": "Quick User Guide: Booking a Meeting Room Online\n1. Log into the staff intranet using your employee ID and password.\n2. Navigate to Facilities, select Room Reservations, and pick your preferred time slot.\n3. Enter the number of attendees and confirm your audiovisual requirements.\n4. Click Submit to receive your instant email confirmation code."
        }
    },
    "page_34": {
        "title": "Complete Answer Key: Master Spelling & Mixed Exam Mocks",
        "spelling": {
            "drill_corrections": [
                "1. collegue -> colleague (remember the 'a')",
                "2. droped -> dropped (double the 'p')",
                "3. their -> their (belonging to them)",
                "4. communitys -> communities (-y changes to -ies)",
                "5. recieve -> receive (after 'c' use 'ei')",
                "6. carefull -> careful (suffix -ful has single 'l')",
                "7. dissappoint -> disappoint (one 's', two 'p's)",
                "8. enviroment -> environment (silent 'n')"
            ]
        },
        "mock_1": {
            "title": "Task 1 Correction Grid & Examiner Guidance (6 Marks)",
            "corrections": [
                {"original": "on monday morning", "correction": "On Monday morning", "type": "Capitalisation (Sentence opener & Day)", "mark": "1 Mark"},
                {"original": "Mrs davies", "correction": "Mrs Davies", "type": "Capitalisation (Proper Noun)", "mark": "1 Mark"},
                {"original": "sliped on a patch", "correction": "slipped on a patch", "type": "Spelling (Consonant doubling 1-1-1 rule)", "mark": "1 Mark"},
                {"original": "wrist, she was given", "correction": "wrist; she was given (or . She)", "type": "Punctuation (Comma Splice)", "mark": "1 Mark"},
                {"original": "warehouse floor were", "correction": "warehouse floor was", "type": "Grammar (Subject-Verb: floor is singular)", "mark": "1 Mark"},
                {"original": "warning cones was placed", "correction": "warning cones were placed", "type": "Grammar (Subject-Verb: cones is plural)", "mark": "1 Mark"}
            ],
            "examiner_notes": "Award 1 mark per correctly identified and amended error. Total: 6 Marks. Candidates must show accurate spelling and basic punctuation control."
        },
        "mock_2": {
            "title": "Task 2 Model Rewrite & Mark Scheme (6 Marks)",
            "model_rewrite": "Welcome to our new community garden project on Station Road. We are planting winter vegetables this Saturday. It will be great fun for local families. All volunteers must bring their own garden gloves. It's free to join and refreshments will be provided. Last week, our team planted forty fruit trees. Everyone who attended said that they enjoyed the fresh air.",
            "error_breakdown": [
                "1. station road -> Station Road (Proper noun capitalisation)",
                "2. this saturday it -> this Saturday. It (Capital day + run-on sentence split)",
                "3. there own -> their own (Possessive homophone)",
                "4. Its free -> It's free (Contraction apostrophe for 'It is')",
                "5. planed forty -> planted (or planned) forty (Verb spelling)",
                "6. attended say that -> attended said that (Consistent past tense)"
            ]
        }
    }
}
