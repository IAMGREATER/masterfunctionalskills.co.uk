#!/usr/bin/env python3
"""
Authentic Fluency Workouts: English Writing, Reading & SLC
10 Core High-Yield Topics:
- writing-grammar
- writing-perfecting-your-punctuation
- writing-spelling
- writing-tenses
- writing-linking-up-your-answer
- reading-fact-or-opinion
- reading-language-features
- reading-investigating-layout
- slc-asking
- slc-contributing
"""

ENGLISH_WORKOUTS = {
    # 1. GRAMMAR
    "writing-grammar": {
        "title": "Grammar & Sentence Structures",
        "slug": "writing-grammar",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.22 • L2.24",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Subject-Verb Agreement & Sentence Types",
            "points": [
                "Subject-Verb Agreement: Singular subject takes a singular verb (The nurse IS ready); Plural subject takes a plural verb (The nurses ARE ready).",
                "Collective Nouns: 'The team IS meeting' or 'The management HAS decided'.",
                "Sentence Types: Simple (one independent clause), Compound (joined by FANBOYS: for, and, nor, but, or, yet, so), Complex (uses subordinating conjunctions: although, because, since, while).",
                "Avoid Sentence Fragments: Every complete sentence MUST have a subject and a finite verb.",
                "Avoid Comma Splices: Never join two complete sentences with just a comma; use a full stop, semicolon, or conjunction."
            ],
            "calc_tip": "Look out for intervening phrases: 'The box of sterile gloves IS on the shelf' (subject is 'box', singular)."
        },
        "workout_blocks": [
            {
                "title": "Subject-Verb Agreement Drills",
                "instruction": "Choose the correct verb in brackets:",
                "items": [
                    ("a", "The doctor and the nurse (is / are) in surgery.", "are (plural)"),
                    ("b", "Neither of the files (was / were) located.", "was (singular 'neither')"),
                    ("c", "The list of patient names (was / were) printed.", "was (subject is 'list')"),
                    ("d", "Everyone in the waiting rooms (needs / need) a ticket.", "needs (singular 'everyone')"),
                    ("e", "The team of carers (has / have) completed training.", "has (singular collective noun)"),
                    ("f", "Both of the ambulances (has / have) arrived.", "have (plural)")
                ]
            },
            {
                "title": "Fixing Comma Splices & Fragments",
                "instruction": "Identify whether each sentence is Correct, a Comma Splice, or a Fragment:",
                "items": [
                    ("a", "'The shift ended at 8pm, we all went home.'", "Comma splice (fix with '; ' or '. We')"),
                    ("b", "'Because the emergency generator failed during the storm.'", "Fragment (incomplete thought)"),
                    ("c", "'The clinic opens early; appointments start at 8am.'", "Correct (semicolon links related clauses)"),
                    ("d", "'Although it was raining, the courier arrived on time.'", "Correct (complex sentence)"),
                    ("e", "'The printer ran out of paper, however we had spare.'", "Comma splice (needs '; however,')"),
                    ("f", "'Running quickly down the corridor with urgent blood.'", "Fragment (missing subject and main verb)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Incident Report Editing",
                "stem": "Read this poorly drafted sentence from a trainee healthcare assistant's incident log:<br><em>'The delivery of medical oxygen cylinders was late on Tuesday, it caused delays in theatre and the ward sister were very frustrated.'</em><br><br>Identify the <strong>two grammatical errors</strong> in the sentence and rewrite it in flawless, professional Standard English.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Error 1: Comma splice after 'Tuesday' joining two independent clauses with a comma.", "[P1]"),
                    ("Error 2: Subject-verb disagreement: 'the ward sister were' (singular subject 'sister' requires singular verb 'was').", "[P1]"),
                    ("Rewrite: 'The delivery of medical oxygen cylinders was late on Tuesday. This caused delays in theatre, and the ward sister was very frustrated.' (or '...Tuesday; consequently, it caused delays...')", "[A1]")
                ],
                "final_answer": "Fix comma splice with a full stop or semicolon; change 'sister were' to 'sister was'.",
                "reverse_check": "Grammatically sound, appropriate professional tone.",
                "pitfall": "Leaving 'sister were' unchanged or failing to fix the comma splice."
            }
        ]
    },

    # 2. PUNCTUATION
    "writing-perfecting-your-punctuation": {
        "title": "Punctuation Mastery",
        "slug": "writing-perfecting-your-punctuation",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.21 • L2.23",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Apostrophes, Colons & Semicolons",
            "points": [
                "Apostrophe for Omission (contraction): Shows where letters are missing (don't = do not; it's = it is).",
                "Apostrophe for Possession (belonging): Singular: Add 's (The doctor's coat); Plural ending in s: Add apostrophe after s (The doctors' coats).",
                "It's vs Its: It's = 'it is'; Its = possessive (The hospital updated its policy - NO apostrophe!).",
                "Colon (:): Introduces a list, explanation, or direct quotation.",
                "Semicolon (;): Links two closely related independent clauses without a conjunction."
            ],
            "calc_tip": "Remember: NEVER use an apostrophe for simple plurals! E.g. '1990s' or 'apples for sale' (NOT 1990's or apple's)."
        },
        "workout_blocks": [
            {
                "title": "Apostrophes: Possession vs Contraction",
                "instruction": "Insert the apostrophe in the correct position:",
                "items": [
                    ("a", "The nurses station was busy. (one nurse)", "nurse's"),
                    ("b", "The nurses uniforms were blue. (multiple nurses)", "nurses'"),
                    ("c", "The patients appointment is at 10am. (one patient)", "patient's"),
                    ("d", "The patients records were archived. (multiple patients)", "patients'"),
                    ("e", "The childs toy was sanitized.", "child's (irregular plural children's)"),
                    ("f", "Its cold outside today. (contraction of it is)", "It's"),
                    ("g", "The cat drank its milk.", "its (possessive — NO apostrophe)"),
                    ("h", "Theyre arriving tomorrow morning.", "They're (they are)")
                ]
            },
            {
                "title": "Colons, Semicolons & Commas",
                "instruction": "Choose Colon (:) or Semicolon (;) for each blank:",
                "items": [
                    ("a", "Please bring the following items [ ] pen, ID card, and notepad.", "Colon (:) to introduce a list"),
                    ("b", "The morning clinic was cancelled [ ] the doctor was unwell.", "Semicolon (;) linking related clauses"),
                    ("c", "There was only one possible explanation [ ] human error.", "Colon (:) introducing explanation"),
                    ("d", "Some staff chose night shifts [ ] others preferred days.", "Semicolon (;) balancing contrasting clauses"),
                    ("e", "The rule is simple [ ] wash your hands before entering.", "Colon (:) introducing a rule")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Staff Noticeboard Notice",
                "stem": "Correct all punctuation errors in this draft notice for a clinic reception area:<br><em>'All visitor's must report to reception its essential that you sign in before visiting patient's in ward 3.'</em><br><br>Rewrite the sentence with correct apostrophes and appropriate sentence boundaries.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Remove greengrocer's apostrophe from plural 'visitor's' → 'visitors'", "[P1]"),
                    ("Add missing apostrophe in contraction 'its' → 'it's (it is)' and add full stop/semicolon before it", "[M1]"),
                    ("Remove apostrophe from plural 'patient's' → 'patients'", "[A1]")
                ],
                "final_answer": "'All visitors must report to reception. It's essential that you sign in before visiting patients in Ward 3.' (or '...reception; it's essential...')",
                "reverse_check": "No apostrophes on simple plurals (visitors, patients); apostrophe on contraction (it's).",
                "pitfall": "Leaving 'its' unpunctuated or adding apostrophes to plural words."
            }
        ]
    },

    # 3. SPELLING
    "writing-spelling": {
        "title": "Spelling Rules, Homophones & Specialist Words",
        "slug": "writing-spelling",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.20 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Common Exam Spellings & Homophones",
            "points": [
                "There / Their / They're: There = place; Their = belonging to them; They're = they are.",
                "Practice vs Practise: Practice = noun (a doctor's practice); Practise = verb (to practise medicine).",
                "Advice vs Advise: Advice = noun (good advice); Advise = verb (to advise someone).",
                "Silent letters & double consonants: Necessary (1 collar, 2 socks: one 'c', two 's's); Recommend (one 'c', two 'm's); Accommodate (two 'c's, two 'm's).",
                "Definite: Contains 'finite' in the middle (d-e-f-i-n-i-t-e), NEVER 'definitely' with an 'a'!"
            ],
            "calc_tip": "When proofreading your exam writing, read backwards from the last sentence to catch spelling errors your brain skips over."
        },
        "workout_blocks": [
            {
                "title": "Homophone Precision Drills",
                "instruction": "Choose the correct homophone:",
                "items": [
                    ("a", "(There / Their / They're) coats are hanging in the staffroom.", "Their (belonging)"),
                    ("b", "Put the specimen jar over (there / their / they're).", "there (location)"),
                    ("c", "(There / Their / They're) arriving for the meeting now.", "They're (they are)"),
                    ("d", "I would (advice / advise) you to rest.", "advise (verb)"),
                    ("e", "Thank you for your helpful (advice / advise).", "advice (noun)"),
                    ("f", "A dental (practice / practise).", "practice (noun)")
                ]
            },
            {
                "title": "High-Frequency Misspelled Exam Words",
                "instruction": "Identify the correctly spelled word in each pair:",
                "items": [
                    ("a", "neccessary OR necessary", "necessary (one c, two s)"),
                    ("b", "accomodate OR accommodate", "accommodate (two c, two m)"),
                    ("c", "defanately OR definitely", "definitely (contains 'finite')"),
                    ("d", "seperate OR separate", "separate ('a rat' in the middle)"),
                    ("e", "recieve OR receive", "receive ('i' before 'e' except after 'c')"),
                    ("f", "embarass OR embarrass", "embarrass (two r, two s)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Workplace Policy Memo",
                "stem": "Correct the four spelling errors in this staff memo:<br><em>'It is neccessary that staff recieve formal training before they practise on patients. Management will definately provide full accomodation for trainees.'</em>",
                "marks": 4,
                "prefix": "",
                "steps": [
                    ("Error 1: 'neccessary' → necessary", "[A1]"),
                    ("Error 2: 'recieve' → receive", "[A1]"),
                    ("Error 3: 'definately' → definitely", "[A1]"),
                    ("Error 4: 'accomodation' → accommodation", "[A1]")
                ],
                "final_answer": "1. necessary; 2. receive; 3. definitely; 4. accommodation.",
                "reverse_check": "All 4 words conform to standard English spelling rules.",
                "pitfall": "Overlooking 'recieve' (fails the 'i before e except after c' rule)."
            }
        ]
    },

    # 4. TENSES
    "writing-tenses": {
        "title": "Consistency of Tense",
        "slug": "writing-tenses",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.23 • L2.25",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Tense Consistency & Shift Avoidance",
            "points": [
                "Incident Reports & Past Events: Write strictly in the PAST tense (walked, noticed, reported).",
                "Procedures & Manuals: Write in the PRESENT tense (clean, inspect, verify).",
                "Future Proposals & Plans: Write using FUTURE modal verbs (will install, shall implement).",
                "Tense shifting error: Do NOT accidentally slip from past into present in the same narrative (e.g. 'I walked into the room and see the spilled water' → should be 'saw')."
            ],
            "calc_tip": "Check your verbs! If an incident happened yesterday, every single action verb must be in the past tense."
        },
        "workout_blocks": [
            {
                "title": "Past vs Present Tense Matching",
                "instruction": "Convert the present tense verb into the past tense:",
                "items": [
                    ("a", "see", "saw"),
                    ("b", "run", "ran"),
                    ("c", "bring", "brought"),
                    ("d", "speak", "spoke"),
                    ("e", "choose", "chose"),
                    ("f", "write", "wrote"),
                    ("g", "lead", "led"),
                    ("h", "hear", "heard")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Shift Handover Report",
                "stem": "Spot the three tense-shifting errors in this clinical report extract:<br><em>'At 14:00, the patient reported mild chest pain. Dr Hughes examines the ECG results and decided to prescribe medication. The patient takes the tablets and rested comfortably.'</em><br><br>Rewrite the extract maintaining consistent past tense throughout.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify error 1: 'examines' (present tense) should be 'examined' (past tense).", "[P1]"),
                    ("Identify error 2: 'takes' (present tense) should be 'took' (past tense).", "[P1]"),
                    ("Rewrite: 'At 14:00, the patient reported mild chest pain. Dr Hughes examined the ECG results and decided to prescribe medication. The patient took the tablets and rested comfortably.'", "[A1]")
                ],
                "final_answer": "Change 'examines' to 'examined' and 'takes' to 'took'.",
                "reverse_check": "All verbs (reported, examined, decided, took, rested) are consistently in the past tense.",
                "pitfall": "Leaving 'examines' or 'takes' in the present tense."
            }
        ]
    },

    # 5. LINKING UP / TRANSITIONS
    "writing-linking-up-your-answer": {
        "title": "Paragraphing, Transitions & Cohesion",
        "slug": "writing-linking-up-your-answer",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.19 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Discourse Markers & Paragraph Transitions",
            "points": [
                "Adding Ideas: Furthermore, Moreover, In addition, Additionally.",
                "Contrasting Ideas: However, On the other hand, Conversely, In contrast, Nevertheless.",
                "Showing Cause & Effect: Consequently, As a result, Therefore, Thus.",
                "Sequencing: Firstly, Subsequently, Following this, Finally.",
                "TiP ToP Paragraph Rule: Start a new paragraph for changes in Time, Place, Topic, or Person."
            ],
            "calc_tip": "Always follow transition words at the start of a sentence with a comma (e.g. 'Furthermore, ...' or 'However, ...')."
        },
        "workout_blocks": [
            {
                "title": "Selecting Cohesive Connectives",
                "instruction": "Select the best connective (Furthermore, However, Consequently):",
                "items": [
                    ("a", "The budget was cut. [ ], we had to cancel the trip.", "Consequently (cause & effect)"),
                    ("b", "She is a skilled surgeon. [ ], she trains junior doctors.", "Furthermore (adding info)"),
                    ("c", "The weather was awful. [ ], the outdoor market stayed open.", "However (contrast)"),
                    ("d", "Staff numbers increased. [ ], patient wait times dropped.", "Consequently"),
                    ("e", "The course is free. [ ], travel expenses are covered.", "In addition / Furthermore"),
                    ("f", "He applied late. [ ], he was granted an interview.", "Nevertheless / However")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Formal Proposal to Hospital Board",
                "stem": "A healthcare apprentice drafts a proposal for new recycling bins on hospital wards.<br>Link these two disjointed sentences using an appropriate <strong>contrastive transition</strong> and punctuation:<br><em>'Installing recycling bins requires an upfront cost of £1,200. Waste collection disposal fees will be reduced by £3,500 every year.'</em>",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Select contrastive connective: 'However,' or 'Nevertheless,' or 'Although...'", "[M1]"),
                    ("Punctuate correctly: 'Installing recycling bins requires an upfront cost of £1,200; however, waste collection fees will be reduced by £3,500 every year.' (or '...£1,200. However, waste...')", "[A1]")
                ],
                "final_answer": "'Installing recycling bins requires an upfront cost of £1,200. However, waste collection fees will be reduced by £3,500 every year.'",
                "reverse_check": "Shows clear counter-argument resolution.",
                "pitfall": "Using an additive connective like 'Furthermore' which contradicts the financial contrast."
            }
        ]
    },

    # 6. FACT OR OPINION
    "reading-fact-or-opinion": {
        "title": "Fact or Opinion",
        "slug": "reading-fact-or-opinion",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.11 • L2.13",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Distinguishing Verifiable Facts from Subjective Opinions",
            "points": [
                "Fact: An objective statement that can be proven true or false using evidence, measurements, official data, or historical records.",
                "Opinion: A subjective personal belief, value judgment, or feeling that cannot be conclusively proven.",
                "Watch out for opinion indicators: 'best', 'worst', 'should', 'terrible', 'wonderful', 'obviously', 'undoubtedly'.",
                "Facts disguised with numbers: '75% of voters supported the motion' is a FACT (it reports recorded votes), even though the motion itself might be an opinion!"
            ],
            "calc_tip": "Ask yourself: 'Can this statement be tested against objective evidence?' If yes, it is a fact; if it is open to debate or taste, it is an opinion."
        },
        "workout_blocks": [
            {
                "title": "Fact vs Opinion Classification",
                "instruction": "Classify each statement as a Fact or an Opinion:",
                "items": [
                    ("a", "'The hospital has 450 acute inpatient beds.'", "Fact (verifiable data)"),
                    ("b", "'Our doctors provide the most compassionate care in the UK.'", "Opinion ('most compassionate' is subjective)"),
                    ("c", "'Blood pressure above 140/90 mmHg is clinically termed hypertension.'", "Fact (medical definition)"),
                    ("d", "'Night shifts are far more exhausting than day shifts.'", "Opinion (subjective experience)"),
                    ("e", "'Water freezes at 0 degrees Celsius at sea level.'", "Fact (scientific law)"),
                    ("f", "'Electric ambulances look much more stylish than diesel vans.'", "Opinion (aesthetic judgment)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Facility Annual Review Analysis",
                "stem": "Read this excerpt from a hospital chief executive's annual message:<br><em>'Last year, our surgical teams performed 12,450 operations across three sites. It was the most remarkable and inspiring year in our hospital's history, and every single resident in our town should feel immensely proud of our heroic doctors.'</em><br><br>Extract <strong>one verifiable fact</strong> and <strong>one subjective opinion</strong> from the text.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Extract Fact: 'our surgical teams performed 12,450 operations across three sites'", "[A1]"),
                    ("Extract Opinion: 'It was the most remarkable and inspiring year in our hospital's history' (or 'every resident should feel proud' / 'heroic doctors')", "[A1]")
                ],
                "final_answer": "Fact: 'teams performed 12,450 operations across three sites'. Opinion: 'most remarkable and inspiring year in our hospital's history'.",
                "reverse_check": "Fact contains measurable numerical count; opinion contains emotive adjectives.",
                "pitfall": "Quoting the whole paragraph without distinguishing between the two parts."
            }
        ]
    },

    # 7. LANGUAGE FEATURES
    "reading-language-features": {
        "title": "Language Features & Rhetorical Devices",
        "slug": "reading-language-features",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.14 • L2.15",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Key Rhetorical Devices & Effects",
            "points": [
                "Rhetorical Question: A question asked for effect without expecting an answer (engages reader: 'Can we afford to ignore this?').",
                "Rule of Three / Triad: Group of three words or phrases for emphasis ('Reduce, reuse, recycle').",
                "Hyperbole: Deliberate exaggeration for dramatic impact ('We have waited a million years for this').",
                "Emotive Language: Words designed to evoke strong emotional reactions ('innocent', 'heartbreaking', 'devastated').",
                "Imperative: Direct command verb ('Donate today', 'Call immediately')."
            ],
            "calc_tip": "When asked 'What is the effect of this language feature?', do not just name it—explain how it makes the reader think, feel, or act."
        },
        "workout_blocks": [
            {
                "title": "Identifying Rhetorical Devices",
                "instruction": "Name the specific language device used in each excerpt:",
                "items": [
                    ("a", "'Stop. Look. Listen.'", "Rule of three / Imperative"),
                    ("b", "'Are you tired of paying extortionate energy bills?'", "Rhetorical question"),
                    ("c", "'Our waiting times are a million miles away from perfection.'", "Hyperbole (exaggeration)"),
                    ("d", "'Innocent, defenseless animals suffering in freezing conditions.'", "Emotive language"),
                    ("e", "'Donating blood is giving the gift of life.'", "Metaphor"),
                    ("f", "'Call our emergency helpline now to claim your grant.'", "Imperative verb ('Call')")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Hospital Blood Donor Appeal Campaign",
                "stem": "Read this blood donation campaign slogan:<br><em>'Forty-five minutes of your time can save three precious lives. Will you sit back and do nothing while our blood banks run empty?'</em><br><br>(a) Name <strong>two distinct language features</strong> used in the slogan.<br>(b) Explain the intended effect on the reader.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify feature 1: Factual/numerical contrast (45 mins vs 3 lives) or Emotive language ('precious lives').", "[A1]"),
                    ("Identify feature 2: Rhetorical question ('Will you sit back...?').", "[A1]"),
                    ("Explain effect: Challenges the reader morally, evokes guilt/responsibility, and urges immediate action to donate blood.", "[A1]")
                ],
                "final_answer": "(a) Emotive language ('precious lives') and Rhetorical question. (b) Directly challenges the reader to act immediately out of moral duty.",
                "reverse_check": "Identifies device and articulates persuasive psychological impact.",
                "pitfall": "Simply defining what a rhetorical question is rather than explaining its effect in this specific context."
            }
        ]
    },

    # 8. INVESTIGATING LAYOUT
    "reading-investigating-layout": {
        "title": "Layout Devices & Visual Signposting",
        "slug": "reading-investigating-layout",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.13 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Visual Signposting & Layout Devices",
            "points": [
                "Headlines & Headings: State the topic and catch the reader's eye immediately.",
                "Subheadings: Break text into logical sections so readers can find specific information quickly.",
                "Bullet Points: Chunk complex lists into readable items.",
                "Callout / Shaded Boxes: Draw the eye to vital warnings, contact numbers, or summaries.",
                "Bold / Italic Font: Emphasizes crucial keywords or terminology.",
                "Images & Captions: Reinforce textual meaning and provide visual clarification."
            ],
            "calc_tip": "In Reading exams, when asked 'Why did the writer use bullet points?', always mention that it makes information easier and faster to read/digest."
        },
        "workout_blocks": [
            {
                "title": "Purpose of Layout Features",
                "instruction": "Match each layout feature to its primary purpose:",
                "items": [
                    ("a", "Subheadings", "Divides text into sections; aids navigation"),
                    ("b", "Bulleted list", "Breaks information into digestible points"),
                    ("c", "Text in bold", "Draws immediate attention to key terms"),
                    ("d", "Shaded text box", "Highlights crucial contact info or warnings"),
                    ("e", "Captions beneath photos", "Explains context and relevance of image"),
                    ("f", "Table of data", "Compares numbers clearly in rows and columns")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Fire Evacuation Noticeboard",
                "stem": "A hospital fire safety procedure leaflet displays:<br>• A main title in red 24pt bold: <strong>EMERGENCY FIRE ACTION</strong><br>• Four numbered steps (1 to 4) with bold action verbs (Sound, Evacuate, Report, Assemble)<br>• A yellow shaded box at the bottom displaying the <strong>Assembly Point Map</strong>.<br><br>Explain how the layout devices help hospital staff act safely during a fire emergency.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Title: Large red bold title immediately alerts staff to the emergency nature of the leaflet.", "[A1]"),
                    ("Numbered steps: Numbering gives an unambiguous chronological order of actions under panic/stress.", "[A1]"),
                    ("Yellow callout box: Visually separates the evacuation destination so staff know exactly where to gather without reading full paragraphs.", "[A1]")
                ],
                "final_answer": "Red bold title signals urgency; numbered list provides clear step-by-step instructions under stress; shaded box highlights the assembly point immediately.",
                "reverse_check": "Directly addresses how layout aids emergency compliance.",
                "pitfall": "Describing the fire rules instead of explaining how the layout devices assist the reader."
            }
        ]
    },

    # 9. SLC: ASKING QUESTIONS
    "slc-asking": {
        "title": "Asking Questions Effectively in Group Discussions",
        "slug": "slc-asking",
        "subject": "English SLC",
        "spec_codes": "Pearson Edexcel SLC: L1.1 • L2.2",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Closed vs Open Probing Questions",
            "points": [
                "Closed Questions: Prompt a single word or Yes/No answer (e.g. 'Did you like the plan?'). Unsuitable for driving group discussion.",
                "Open Questions: Prompt detailed, thoughtful elaboration (begin with How, Why, What, In what ways).",
                "Probing Questions: Follow up on another speaker's point to dig deeper ('What evidence led you to that conclusion?').",
                "Clarifying Questions: Check understanding politely ('Could you clarify what you meant by flexible hours?')."
            ],
            "calc_tip": "In your assessed discussion, avoid Yes/No questions! Start questions with 'What do you think about...' or 'How would that affect...'."
        },
        "workout_blocks": [
            {
                "title": "Converting Closed Questions to Open Probes",
                "instruction": "Convert the closed question into an open probing question:",
                "items": [
                    ("a", "Closed: 'Is the new shift rota good?'", "Open: 'How will the new shift rota affect staff work-life balance?'"),
                    ("b", "Closed: 'Do you agree with the budget?'", "Open: 'What are your thoughts on how the budget has been allocated?'"),
                    ("c", "Closed: 'Should we buy new computers?'", "Open: 'In what ways would upgrading our computers improve daily productivity?'"),
                    ("d", "Closed: 'Are you worried about parking?'", "Open: 'What concerns do you have regarding the proposed parking changes?'"),
                    ("e", "Closed: 'Is this policy fair?'", "Open: 'How does this policy impact different teams across the company?'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Departmental Staff Consultation",
                "stem": "During an assessed group discussion on reducing hospital food waste, a quiet peer remarks: <em>'I think the canteen portions are too big.'</em><br><br>Write an effective <strong>open probing question</strong> you would ask this colleague to draw out their ideas and invite constructive solutions.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Acknowledge peer's point respectfully.", "[P1]"),
                    ("Ask an open probing question starting with How, What, or Why: 'That's an interesting point, Sarah. How do you think the catering team could adjust portion sizes or offer flexible options to reduce that waste?'", "[A1]")
                ],
                "final_answer": "'That is a great observation, Sarah. How could the catering team adjust portion options so patients don't end up leaving uneaten food?'",
                "reverse_check": "Open question requiring explanation rather than Yes/No.",
                "pitfall": "Asking 'Do you think they should be smaller?' (closed Yes/No question)."
            }
        ]
    },

    # 10. SLC: CONTRIBUTING
    "slc-contributing": {
        "title": "Contributing to Group Discussions & Verbal Bridges",
        "slug": "slc-contributing",
        "subject": "English SLC",
        "spec_codes": "Pearson Edexcel SLC: L1.3 • L2.3 • L2.5",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Verbal Bridges & Respectful Challenge",
            "points": [
                "Verbal Bridge: Explicitly connects your contribution to what the previous speaker said before adding your point.",
                "Building on ideas: 'Building on Liam's point about cost...' or 'Expanding on what Amara said...'",
                "Respectful Challenge: 'I understand your point about speed, but have you considered the safety risks?'",
                "Inviting quiet members: 'David, we haven't heard your view yet—how would this impact your team?'",
                "Summarizing consensus: 'It sounds like we all agree that option A is the most practical...'"
            ],
            "calc_tip": "Never talk over other candidates. Wait for a natural pause, use the speaker's name, and acknowledge their contribution first."
        },
        "workout_blocks": [
            {
                "title": "Phrasing Verbal Bridges & Transitions",
                "instruction": "State the communicative function of each spoken phrase:",
                "items": [
                    ("a", "'Building on what Liam just said regarding staffing levels...'", "Verbal bridge / Building on ideas"),
                    ("b", "'I take your point about cost, however we must also consider safety.'", "Respectful challenge / Counter-perspective"),
                    ("c", "'Amara, you work on night shifts—what is your experience with this?'", "Inviting a quiet peer by name"),
                    ("d", "'So to summarize our main conclusions so far...'", "Synthesizing consensus"),
                    ("e", "'Could you clarify what you mean by flexible hours?'", "Clarifying question")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Facility Transport Committee Discussion",
                "stem": "In an assessed Level 2 discussion regarding staff parking charges, Candidate A states:<br><em>'We should charge doctors £50 a month and lower-paid healthcare assistants only £10 a month.'</em><br><br>Write a two-sentence contribution demonstrating a <strong>respectful challenge</strong> that acknowledges Candidate A's intention but raises a practical payroll or equity concern.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Sentence 1: Acknowledge Candidate A's fairness rationale: 'I appreciate Candidate A's intention to support lower-paid staff with reduced charges.'", "[P1]"),
                    ("Sentence 2: Introduce respectful challenge with practical consideration: 'However, tiered charges based on salary grades could create administrative complexity for payroll, so should we consider subsidized public transport passes as an alternative?'", "[A1]")
                ],
                "final_answer": "'I understand Candidate A's aim to make parking affordable for lower-paid colleagues. However, linking parking permits to salary bands can cause privacy and payroll issues, so could we explore offering free bus passes instead?'",
                "reverse_check": "Acknowledges speaker + offers constructive counter-view.",
                "pitfall": "Bluntly saying 'That's unfair and won't work' (fails professional tone criteria)."
            }
        ]
    }
}
