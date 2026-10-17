#!/usr/bin/env python3
"""
Authentic Fluency Workouts: English Writing Batch 3
10 Curriculum Topics:
1. english-level-2-writing-blog
2. writing-assessing-audience
3. writing-communicating
4. writing-context
5. writing-fantastic-finalising
6. writing-form-presentational-and-language-features
7. writing-organisational-markers
8. writing-planning-your-answer
9. writing-the-exam
10. writing-why-are-you-writing
"""

ENGLISH_WRITING_BATCH3_WORKOUTS = {
    # 1. WRITING BLOG
    "english-level-2-writing-blog": {
        "title": "Online Blog & Web Article Writing",
        "slug": "english-level-2-writing-blog",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L2.19 • L2.20 • L2.25",
        "level": "Level 2",
        "method_card": {
            "title": "Conventions of Effective Blog Writing",
            "points": [
                "Catchy, engaging headline that hooks reader interest (e.g. using alliteration, a question, or a bold claim).",
                "Personal yet professional voice: 1st/2nd person address ('I', 'we', 'you') with relatable opening hook.",
                "Visual web structure: Short, punchy paragraphs, subheadings, bullet points, and call-out quotes.",
                "Interactive call-to-action (CTA) at the close: Invite reader comments, shares, or feedback.",
                "Consistent register: Informal or semi-formal, avoiding text-speak or inappropriate slang."
            ],
            "calc_tip": "Always conclude with a discussion prompt: 'What are your thoughts on this? Leave a comment below!'"
        },
        "workout_blocks": [
            {
                "title": "Crafting High-Converting Blog Headlines",
                "instruction": "Identify whether each headline is Dull, Too Clickbaity, or Strong/Engaging:",
                "items": [
                    ("a", "'Recycling in the Workplace'", "Dull (lacks engagement)"),
                    ("b", "'5 Simple Workplace Swaps for a Greener Office Today'", "Strong/Engaging (numbered, actionable)"),
                    ("c", "'YOU WILL NEVER BELIEVE WHAT OUR BOSS SAID ABOUT BINS!!!'", "Too Clickbaity (excessive punctuation/caps)"),
                    ("d", "'Why Flexible Working Boosts Productivity: A Carer's View'", "Strong/Engaging (clear perspective & benefit)"),
                    ("e", "'Health and Safety Information Update'", "Dull (reads like an internal memo)")
                ]
            },
            {
                "title": "Blog Structural Features & Calls-to-Action",
                "instruction": "Match the element with its intended blogging purpose:",
                "items": [
                    ("a", "Short 2-3 sentence paragraphs", "Enhances readability on mobile screens"),
                    ("b", "Subheadings every 100-150 words", "Allows readers to skim and navigate key themes"),
                    ("c", "Bullet point lists", "Breaks down complex guidance into actionable steps"),
                    ("d", "'Share your thoughts in the comment section below!'", "Call-to-action (CTA) encouraging community interaction")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Workplace Wellbeing Blog Post",
                "stem": "You are writing a blog post for your healthcare facility's staff intranet on the topic: <strong>'Overcoming Burnout: Small Daily Habits for Busy Healthcare Workers'</strong>.<br><br>(a) Write a catchy headline and a 2-sentence opening hook.<br>(b) Draft two bullet points offering practical, achievable workplace tips.<br>(c) Write an engaging closing sentence inviting colleagues to leave a comment.",
                "marks": 4,
                "prefix": "",
                "steps": [
                    ("Headline & hook: Punchy title + relatable opening acknowledging busy shift demands", "[W1]"),
                    ("Body bullets: Clear, realistic actions (e.g. hydration reminders, 5-minute outdoor micro-breaks)", "[W1]"),
                    ("Call to action: Direct invitation to share personal tips in the comment thread below", "[W1]"),
                    ("Tone & register: Professional, empathetic, grammatically accurate", "[W1]")
                ],
                "final_answer": "Headline: 'From Surviving to Thriving: 3 Micro-Habits for Busy Shifts'. Hook acknowledges pressure, provides 2 practical tips, and ends with an interactive comment prompt.",
                "reverse_check": "Includes headline, hook, bulleted tips, and CTA.",
                "pitfall": "Writing an essay without blog layout features (subheadings, bullets, or call to action)."
            }
        ]
    },

    # 2. ASSESSING AUDIENCE
    "writing-assessing-audience": {
        "title": "Adapting Writing for Your Audience",
        "slug": "writing-assessing-audience",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.19 • L2.20",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Audience Profiling & Tone Matching",
            "points": [
                "Identify who will read the text: Senior manager, local council, colleague, client, or general public.",
                "Determine the appropriate register: Formal, Semi-formal, or Informal.",
                "Formal audience (Director, Council): Use passive voice, no contractions (do not, cannot), sophisticated vocabulary, polite sign-offs.",
                "General public / Peers: Clear, direct, empathetic tone, active verbs, contractions acceptable if semi-formal.",
                "Avoid inappropriate colloquialisms (e.g. don't write 'Cheers mate' to a committee chair)."
            ],
            "calc_tip": "Before writing a single word, note down: 'Audience = ...', 'Tone = ...', 'Form = ...'."
        },
        "workout_blocks": [
            {
                "title": "Identifying Appropriate Register",
                "instruction": "State whether each audience requires Formal, Semi-Formal, or Informal register:",
                "items": [
                    ("a", "A formal letter of complaint to a regional transport regulator", "Formal"),
                    ("b", "A staff noticeboard message about a charity bake sale", "Semi-formal"),
                    ("c", "A job application covering letter to a human resources director", "Formal"),
                    ("d", "A WhatsApp message to a close colleague about lunch cover", "Informal"),
                    ("e", "An article for a community health clinic patient newsletter", "Semi-formal (friendly yet professional)"),
                    ("f", "A witness statement following an incident in a warehouse", "Formal")
                ]
            },
            {
                "title": "Vocabulary Upgrades for Formal Audiences",
                "instruction": "Replace the informal phrase with a professional formal equivalent:",
                "items": [
                    ("a", "Replace 'I want to say sorry' in a letter", "'I am writing to offer my sincere apologies'"),
                    ("b", "Replace 'The machine is bust' in a maintenance log", "'The diagnostic machine is currently defective / out of service'"),
                    ("c", "Replace 'Get in touch ASAP' in a formal email", "'Please contact me at your earliest convenience'"),
                    ("d", "Replace 'Lots of stuff went wrong' in a report", "'Multiple procedural irregularities occurred'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Facility Manager Correspondence",
                "stem": "A trainee care assistant drafted this opening sentence in an official incident letter to the Clinical Operations Lead:<br><em>'Hey David, just letting you know the lift was completely broken today and loads of patients were really annoyed.'</em><br><br>Rewrite this sentence to demonstrate an appropriate formal register suitable for a senior operations lead.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Remove informal salutation and colloquial vocabulary ('Hey David', 'completely broken', 'loads of', 'really annoyed')", "[W1]"),
                    ("Substitute with formal phrasing ('Dear Mr Davis / Operations Lead', 'out of order / malfunctioning', 'numerous patients experienced distress/delay')", "[W1]"),
                    ("Ensure objective, professional Standard English throughout", "[A1]")
                ],
                "final_answer": "'Dear Mr Davis, I am writing to formally report that the main passenger elevator was out of service today, causing substantial disruption and concern among several patients.'",
                "reverse_check": "Professional, formal tone, error-free syntax.",
                "pitfall": "Keeping colloquial expressions like 'loads of' or 'annoyed' in a formal report."
            }
        ]
    },

    # 3. COMMUNICATING
    "writing-communicating": {
        "title": "Clarity & Precision in Written Communication",
        "slug": "writing-communicating",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.20 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Clear, Coherent & Concise Writing",
            "points": [
                "Clarity: Express one main idea per sentence; avoid convoluted, runaway sentences.",
                "Precision: Use exact numbers, dates, locations, and names rather than vague terms ('at 14:15 in Room 4', not 'earlier today').",
                "Active Voice: Make the subject perform the action ('The team completed the audit', rather than 'The audit was completed by the team').",
                "Coherence: Ensure sentences connect logically with transitional words (furthermore, consequently, however).",
                "Eliminate wordiness: Cut unnecessary filler words (e.g. 'due to the fact that' → 'because')."
            ],
            "calc_tip": "If a sentence is more than 3 lines long, find where to split it into two concise sentences."
        },
        "workout_blocks": [
            {
                "title": "Cutting Wordy Filler Phrases",
                "instruction": "Replace each wordy phrase with a single concise word:",
                "items": [
                    ("a", "'Due to the fact that'", "Because"),
                    ("b", "'At this moment in time'", "Currently / Now"),
                    ("c", "'In the near future'", "Soon / Shortly"),
                    ("d", "'In order to'", "To"),
                    ("e", "'Has the ability to'", "Can"),
                    ("f", "'Despite the fact that'", "Although")
                ]
            },
            {
                "title": "Active vs Passive Voice",
                "instruction": "Identify whether each sentence is Active or Passive voice:",
                "items": [
                    ("a", "The nurse administered the medication.", "Active (nurse performs action)"),
                    ("b", "The medication was administered by the nurse.", "Passive"),
                    ("c", "The committee approved the budget proposal.", "Active"),
                    ("d", "The fire alarm was tested by the safety officer.", "Passive"),
                    ("e", "Security inspected all visitor badges at reception.", "Active")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Safety Briefing Memo",
                "stem": "Read this poorly structured sentence from a workplace maintenance briefing:<br><em>'It has come to our attention that people are leaving doors open because of the fact that they don't know the code, which creates a huge security problem for the whole building at this moment in time.'</em><br><br>Rewrite this message so that it is concise, authoritative, and professionally phrased in two clear sentences.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Cut filler phrases ('because of the fact that', 'at this moment in time')", "[W1]"),
                    ("Split into two distinct, punchy sentences: Issue statement + Action/Risk statement", "[W1]"),
                    ("Maintain professional authority and clarity", "[A1]")
                ],
                "final_answer": "'Security fire doors are frequently being left propped open due to staff unfamiliarity with the access codes. This practice poses a serious security hazard and must cease immediately.'",
                "reverse_check": "Concise, eliminates redundancy, clear instruction.",
                "pitfall": "Leaving the sentence as one long, breathless clause."
            }
        ]
    },

    # 4. CONTEXT
    "writing-context": {
        "title": "Contextual Awareness & Purpose in Writing",
        "slug": "writing-context",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.19 • L2.19",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Analyzing Writing Prompts: PAF (Purpose, Audience, Form)",
            "points": [
                "Purpose: Why are you writing? (To persuade, inform, advise, complain, or explain).",
                "Audience: Who will read your writing? (Determines register, formality, and vocabulary choices).",
                "Form: What format are you writing in? (Letter, email, article, report, review, blog).",
                "Contextual details: Pick up on clues in the prompt (dates, budgets, deadlines, locations) to make your response authentic.",
                "Never write a generic response: weave the specific vocational context throughout every paragraph."
            ],
            "calc_tip": "Write 'P - A - F' at the top of your planning sheet and fill it in before writing."
        },
        "workout_blocks": [
            {
                "title": "Identifying Primary Purpose",
                "instruction": "State the primary purpose (Persuade, Inform, Complain, Advise, or Review):",
                "items": [
                    ("a", "A letter to a supplier demanding a refund for damaged goods", "Complain"),
                    ("b", "A staff guide detailing the steps for hazardous waste disposal", "Inform / Instruct"),
                    ("c", "A speech encouraging team members to volunteer for overtime shifts", "Persuade"),
                    ("d", "An evaluation of a new scheduling software tool testing ease of use", "Review"),
                    ("e", "A patient leaflet explaining how to prepare for an ultrasound", "Advise / Inform")
                ]
            },
            {
                "title": "Context Clues Extraction",
                "instruction": "Identify what details must be included based on the prompt:",
                "items": [
                    ("a", "Prompt: 'Write a letter to your estates lead proposing solar panels on Clinic Block B...'", "Address to Estates Lead, Block B location, benefits of solar, cost/energy savings"),
                    ("b", "Prompt: 'Write an article for a college website about balanced shift nutrition...'", "Student/worker audience, practical meal ideas, budget considerations, engaging title")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Vocational Facility Relocation Notice",
                "stem": "You are the administrative lead at a healthcare diagnostic centre.<br>The blood testing phlebotomy suite is moving from <strong>Ground Floor Room 3</strong> to <strong>Second Floor Room 24</strong> on <strong>Monday 3rd November</strong>.<br>Patients need to know how to access the new location using the rear lifts.<br>Draft a 3-bullet point patient notice informing them of the move, date, and access guidance.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Bullet 1: State the exact change of room and effective date clearly", "[W1]"),
                    ("Bullet 2: Provide clear navigation instructions (use rear lifts to 2nd Floor)", "[W1]"),
                    ("Bullet 3: Provide reassurance and assistance contact info for mobility support", "[A1]")
                ],
                "final_answer": "• Relocation: Effective Monday 3rd November, all blood tests will take place in Room 24 (Second Floor).\n• Access: Please use the rear elevators located next to the main pharmacy.\n• Assistance: Step-free wheelchair access is available; please alert reception if you require escort assistance.",
                "reverse_check": "Covers date, rooms, navigation, and accessibility.",
                "pitfall": "Omitting the effective date or failing to give directions to the second floor."
            }
        ]
    },

    # 5. FANTASTIC FINALISING (PROOFREADING)
    "writing-fantastic-finalising": {
        "title": "Proofreading, Editing & Finalising",
        "slug": "writing-fantastic-finalising",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.21 • L1.22 • L2.23 • L2.24",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The 5-Point Proofreading Checklist",
            "points": [
                "1. Capital Letters: Check beginnings of sentences, proper nouns (days, months, names, places), and the personal pronoun 'I'.",
                "2. Punctuation: Check every sentence ends with a full stop, question mark, or exclamation mark; eliminate comma splices.",
                "3. Homophones: Check commonly confused words (their / there / they're; your / you're; its / it's; to / too / two).",
                "4. Subject-Verb Agreement: Ensure singular subjects have singular verbs and plurals match.",
                "5. Paragraphing: Verify text is divided into distinct, cohesive paragraphs with clear topic sentences."
            ],
            "calc_tip": "Read your final draft backwards sentence by sentence to spot spelling and punctuation errors objectively!"
        },
        "workout_blocks": [
            {
                "title": "Spotting Common Homophone Errors",
                "instruction": "Choose the correct word in brackets:",
                "items": [
                    ("a", "The doctors collected (their / there / they're) stethoscopes.", "their (belonging)"),
                    ("b", "Please place the confidential files over (their / there / they're).", "there (location)"),
                    ("c", "The clinic updated (it's / its) opening hours.", "its (possessive)"),
                    ("d", "Make sure (your / you're) wearing safety goggles.", "you're (you are)"),
                    ("e", "The dose was (to / too / two) high.", "too (excessive)"),
                    ("f", "The change of diet had a positive (affect / effect).", "effect (noun)")
                ]
            },
            {
                "title": "Error Detection Drills",
                "instruction": "Find and correct the single error in each sentence:",
                "items": [
                    ("a", "'On wednesday morning, we attended a mandatory seminar.'", "wednesday → Wednesday (capital letter)"),
                    ("b", "'The manager and myself conducted the inspection.'", "myself → I / me ('The manager and I...')"),
                    ("c", "'Neither of the printers are working.'", "are → is (singular 'neither')"),
                    ("d", "'She should of checked the prescription label.'", "should of → should have"),
                    ("e", "'We was delighted with the audit outcome.'", "We was → We were")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Governance Incident Proofreading",
                "stem": "Read this paragraph written by a student nurse containing <strong>four deliberate errors</strong>:<br><em>'On friday, the pharmacy delivered three boxes of bandages. Me and Sarah checked the inventory, but their was two missing packs. We should of reported it immediately.'</em><br><br>Identify all four errors and provide the corrected version of the paragraph.",
                "marks": 4,
                "prefix": "",
                "steps": [
                    ("Error 1: 'friday' needs capital letter → 'Friday'", "[W1]"),
                    ("Error 2: 'Me and Sarah' subject pronoun error → 'Sarah and I'", "[W1]"),
                    ("Error 3: Homophone error 'their' → 'there were' (and plural agreement 'was' → 'were')", "[W1]"),
                    ("Error 4: 'should of' → 'should have'", "[W1]")
                ],
                "final_answer": "'On Friday, the pharmacy delivered three boxes of bandages. Sarah and I checked the inventory, but there were two missing packs. We should have reported it immediately.'",
                "reverse_check": "Corrects capitalisation, pronouns, homophones, and modal verbs.",
                "pitfall": "Missing the 'should of' error or leaving 'their' unchanged."
            }
        ]
    },

    # 6. FORM, PRESENTATIONAL AND LANGUAGE FEATURES
    "writing-form-presentational-and-language-features": {
        "title": "Text Forms & Layout Conventions",
        "slug": "writing-form-presentational-and-language-features",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.20 • L2.21",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Mandatory Structural Features by Text Form",
            "points": [
                "Formal Letter: Sender address (top-right), Date, Recipient name & address (top-left), Salutation ('Dear Mr X,'), Subject line, Body paragraphs, Sign-off ('Yours sincerely' if named, 'Yours faithfully' if 'Dear Sir/Madam').",
                "Formal Email: 'To:', 'From:', 'Date:', 'Subject:' line (clear and descriptive), Professional opening and closing.",
                "Newspaper/Web Article: Headline, Subheading/strap-line, Byline ('By [Name]'), Introductory summary, Columns or subheadings, Closing conclusion.",
                "Formal Report: Title, 'To / From / Date', Section subheadings (Introduction, Findings, Recommendations), Bullet points.",
                "Review: Title, Star rating, Overview, Pros & Cons, Final verdict/recommendation."
            ],
            "calc_tip": "Memorize: 'Sincerely' when you know their name; 'Faithfully' when you are faithful to a stranger."
        },
        "workout_blocks": [
            {
                "title": "Matching Sign-offs with Salutations",
                "instruction": "State the correct formal sign-off:",
                "items": [
                    ("a", "Dear Mr Henderson,", "Yours sincerely,"),
                    ("b", "Dear Sir or Madam,", "Yours faithfully,"),
                    ("c", "Dear Dr Patel,", "Yours sincerely,"),
                    ("d", "Dear Hiring Manager,", "Yours faithfully,"),
                    ("e", "Dear Colleagues (internal email),", "Kind regards, / Best regards,")
                ]
            },
            {
                "title": "Identifying Essential Form Features",
                "instruction": "State which text form requires the listed feature:",
                "items": [
                    ("a", "Subject line, To:, From:", "Email"),
                    ("b", "Headline, Byline, Subheadings", "Article / Blog"),
                    ("c", "Executive Summary, Findings, Recommendations", "Report"),
                    ("d", "Sender and Recipient addresses with date", "Formal Letter"),
                    ("e", "Rating, Pros/Cons, Verdict", "Review")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Safety Committee Formal Report",
                "stem": "You are writing a short workplace report for your health and safety committee titled: <strong>'Review of Slip and Trip Hazards in Main Entrance Foyer'</strong>.<br><br>Set out the professional layout of this report, including:<br>• The standard header block (To, From, Date, Subject)<br>• Three formal section subheadings<br>• One bulleted recommendation.",
                "marks": 4,
                "prefix": "",
                "steps": [
                    ("Include standard report header: To: Safety Committee, From: Facilities Officer, Date: [Date], Subject: Slip/Trip Hazard Audit", "[W1]"),
                    ("Three structured subheadings: 1. Introduction & Background, 2. Key Findings & Hazard Inspection, 3. Proposed Safety Recommendations", "[W1]"),
                    ("Provide a clear, actionable bulleted recommendation (e.g. install high-traction safety floor matting)", "[W1]"),
                    ("Ensure formal, objective tone throughout", "[A1]")
                ],
                "final_answer": "Complete report template displaying header block, three distinct numbered subheadings, and a concrete recommendation with estimated implementation timeframe.",
                "reverse_check": "Contains all required report conventions.",
                "pitfall": "Writing a letter or essay layout instead of using report headers and subheadings."
            }
        ]
    },

    # 7. ORGANISATIONAL MARKERS
    "writing-organisational-markers": {
        "title": "Organisational Markers & Cohesive Devices",
        "slug": "writing-organisational-markers",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.20 • L2.22",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Signposting & Paragraph Linking Words",
            "points": [
                "Adding information: Furthermore, In addition, Moreover, Additionally.",
                "Showing contrast: However, On the other hand, Conversely, Nevertheless, In contrast.",
                "Showing cause and effect: Consequently, As a result, Therefore, Thus, Accordingly.",
                "Sequencing: Firstly, Secondly, Subsequently, Finally.",
                "Always place a comma after an introductory organisational marker (e.g. 'Furthermore, staff received...')."
            ],
            "calc_tip": "Use organisational markers at the start of body paragraphs to create seamless transitions between ideas."
        },
        "workout_blocks": [
            {
                "title": "Categorising Discourse Markers",
                "instruction": "State whether the word shows Addition, Contrast, Cause/Effect, or Sequencing:",
                "items": [
                    ("a", "'Consequently'", "Cause / Effect"),
                    ("b", "'Furthermore'", "Addition"),
                    ("c", "'However'", "Contrast"),
                    ("d", "'Subsequently'", "Sequencing"),
                    ("e", "'On the other hand'", "Contrast"),
                    ("f", "'Therefore'", "Cause / Effect")
                ]
            },
            {
                "title": "Selecting the Right Transitional Word",
                "instruction": "Choose the most appropriate connective to join the ideas:",
                "items": [
                    ("a", "'The budget was cut by 10%. (However / Furthermore), we maintained all staff posts.'", "However (shows contrast)"),
                    ("b", "'Staff attended the training day. (Consequently / In addition), error rates decreased.'", "Consequently (cause and effect)"),
                    ("c", "'The new ward has 30 beds. (Moreover / Alternatively), it features two triage suites.'", "Moreover (addition)"),
                    ("d", "'The first shift cleaned the equipment. (Subsequently / Conversely), the second shift ran calibrations.'", "Subsequently (time sequence)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Policy Justification Statement",
                "stem": "Read these two disconnected statements from a care home manager's report:<br><em>'Statement 1: Our baseline energy bills increased by 25% over the winter months.'</em><br><em>'Statement 2: We must implement scheduled LED lighting shutdowns across all non-clinical administrative offices.'</em><br><br>Join these two ideas into a single sophisticated sentence using an appropriate organisational marker of <strong>cause and effect</strong>, with correct punctuation.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Select cause-and-effect connective: 'Consequently', 'Therefore', or 'As a result'", "[W1]"),
                    ("Punctuate correctly with a semicolon/full stop before and comma after, or use a subordinating conjunction", "[A1]")
                ],
                "final_answer": "'Our baseline energy bills increased by 25% over the winter months; consequently, we must implement scheduled LED lighting shutdowns across all non-clinical administrative offices.'",
                "reverse_check": "Smooth logical flow, appropriate semicolon and comma.",
                "pitfall": "Creating a comma splice by using only a comma before 'therefore'."
            }
        ]
    },

    # 8. PLANNING YOUR ANSWER
    "writing-planning-your-answer": {
        "title": "Planning Strategies & Brainstorming",
        "slug": "writing-planning-your-answer",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.19 • L2.19",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The 10-Minute Exam Planning Routine",
            "points": [
                "Step 1: Read the prompt twice and highlight the 3-4 mandatory bullet points you must address.",
                "Step 2: Note down PAF (Purpose, Audience, Form).",
                "Step 3: Spider diagram or bullet outline: Assign 1 paragraph to each bullet point in the prompt.",
                "Step 4: Jot down key vocabulary, connectives, and statistics you intend to weave into each paragraph.",
                "Step 5: Allocate word count: Functional Skills writing tasks typically require 200-300 words for Level 1, and 250-350 words for Level 2."
            ],
            "calc_tip": "Spend 5-8 minutes planning for a 45-minute writing task. A strong plan prevents getting stuck halfway through!"
        },
        "workout_blocks": [
            {
                "title": "Structuring a 4-Paragraph Response",
                "instruction": "Outline the role of each paragraph in an exam response:",
                "items": [
                    ("a", "Paragraph 1 (Introduction)", "State reason for writing, establish tone, acknowledge context"),
                    ("b", "Paragraph 2 (Main Argument 1)", "Address prompt bullet 1 with supporting evidence and explanation"),
                    ("c", "Paragraph 3 (Main Argument 2 / Counter)", "Address prompt bullet 2 with detailed examples or solutions"),
                    ("d", "Paragraph 4 (Conclusion & Action)", "Summarize main points, request action or state next steps")
                ]
            },
            {
                "title": "Time Management in the Writing Exam",
                "instruction": "Calculate time allocations for a 1-hour writing paper (two tasks: 40% and 60%):",
                "items": [
                    ("a", "Task 1 (15 marks): Recommended writing time?", "20 to 25 minutes"),
                    ("b", "Task 2 (21 marks): Recommended writing time?", "35 to 40 minutes"),
                    ("c", "How much time should be reserved at the end for proofreading?", "5 minutes per task")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pearson Edexcel Writing Task Planning Scaffold",
                "stem": "Exam Task Prompt: <em>'Write a letter to your regional facilities director proposing the creation of a staff quiet room for rest breaks during intense shifts. You should explain the current problem, suggest a suitable location, and outline the benefits for staff wellbeing.'</em><br><br>Produce a concise 4-part paragraph plan covering all three bullet points from the prompt.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Introduction plan: Purpose of letter + identify current issue (lack of restorative space during 12-hour shifts)", "[W1]"),
                    ("Body Paragraph 1 & 2 plan: Suggest underutilized disused office on 2nd floor + outline specific wellbeing benefits (reduced stress, fewer fatigue errors)", "[W1]"),
                    ("Conclusion plan: Propose next steps, site walkaround visit, polite professional sign-off", "[A1]")
                ],
                "final_answer": "Para 1: Intro & shift fatigue issues | Para 2: Proposal for Room 14 conversion & low-cost furniture | Para 3: Measurable benefits on retention & safety | Para 4: Call to action for site meeting & sign-off.",
                "reverse_check": "Directly maps to all bullet points in the prompt.",
                "pitfall": "Planning only 1 paragraph and forgetting to address the location or benefits."
            }
        ]
    },

    # 9. THE EXAM
    "writing-the-exam": {
        "title": "Exam Technique & Mark Scheme Mastery",
        "slug": "writing-the-exam",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1 & L2 Mark Schemes",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Writing Mark Scheme Breakdown: Composition vs SPaG",
            "points": [
                "Composition (Content & Organisation): Accounts for ~55-60% of marks. Assesses clarity, paragraphing, vocabulary, and addressing all prompt bullets.",
                "SPaG (Spelling, Punctuation & Grammar): Accounts for ~40-45% of marks. Assesses full stops, capital letters, apostrophes, commas, and sentence accuracy.",
                "You cannot pass on ideas alone: accurate punctuation is essential to secure Level 1 and Level 2 passes.",
                "Length rule: Do not write too little! An under-length response (under 150 words) cannot demonstrate range of sentence structures."
            ],
            "calc_tip": "If running out of time, finish your sentence, write a crisp 1-sentence conclusion, and check your punctuation!"
        },
        "workout_blocks": [
            {
                "title": "Exam Dos and Don'ts",
                "instruction": "State whether each practice is Recommended or Avoid:",
                "items": [
                    ("a", "Using bullet points in a formal report", "Recommended"),
                    ("b", "Using slang or text abbreviations like 'u' or 'thx'", "Avoid (severely penalised)"),
                    ("c", "Writing one single giant paragraph without breaks", "Avoid (fails organisation criteria)"),
                    ("d", "Using a range of simple, compound, and complex sentences", "Recommended"),
                    ("e", "Leaving the last 5 minutes to check full stops and capitals", "Recommended")
                ]
            },
            {
                "title": "Word Count and Timing Targets",
                "instruction": "State the standard target for Level 2 Functional Skills English writing:",
                "items": [
                    ("a", "Target word count for Level 2 Task 1", "200 to 250 words"),
                    ("b", "Target word count for Level 2 Task 2", "250 to 350 words"),
                    ("c", "Number of distinct punctuation marks to demonstrate at Level 2", "At least 4-5 (., !, ?, commas, apostrophes, semicolons/colons)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pearson Edexcel SPaG Self-Audit",
                "stem": "In Pearson Edexcel Level 2 Writing, examiners award marks across three distinct SPaG criteria:<br>1. Spelling accuracy of specialist and everyday vocabulary<br>2. Punctuation range and precision<br>3. Grammatical syntax and subject-verb agreement<br><br>Describe three specific strategies you will use during the final 5 minutes of your exam to maximise your SPaG score.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Strategy 1: Scan every sentence ending for missing full stops and verify the following word starts with a capital letter", "[W1]"),
                    ("Strategy 2: Check homophones (there/their/they're, your/you're, its/it's) and common double consonants (e.g. accommodate, necessary)", "[W1]"),
                    ("Strategy 3: Check subject-verb agreement on collective nouns and ensure no comma splices exist", "[A1]")
                ],
                "final_answer": "1. Verify sentence boundary punctuation (full stops & capital letters). 2. Targeted homophone and silent letter spelling check. 3. Check for comma splices and subject-verb agreement.",
                "reverse_check": "Actionable, exam-ready review strategies.",
                "pitfall": "Merely saying 'I will re-read it' without specific targeted error checks."
            }
        ]
    },

    # 10. WHY ARE YOU WRITING?
    "writing-why-are-you-writing": {
        "title": "Determining Purpose & Persuasive Devices",
        "slug": "writing-why-are-you-writing",
        "subject": "English Writing",
        "spec_codes": "Pearson Edexcel English: Writing L1.19 • L2.19",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Persuasive Techniques (DAREST / AFOREST)",
            "points": [
                "D - Direct Address: Engaging the reader directly using 'you', 'your', 'we'.",
                "A - Alliteration / Anecdote: Memorable phrasing or a brief real-life story.",
                "R - Rhetorical Questions & Repetition: Encourages reader reflection and reinforces key themes.",
                "E - Emotive Language & Expert Opinion: Words that provoke feeling ('vital', 'critical', 'devastating') paired with authority.",
                "S - Statistics & Facts: Concrete numbers lend credibility ('85% of healthcare staff reported...').",
                "T - Rule of Three: Grouping three words or ideas together for rhythm and impact."
            ],
            "calc_tip": "Do not overload every sentence with techniques; choose 2-3 appropriate devices per paragraph."
        },
        "workout_blocks": [
            {
                "title": "Identifying Persuasive Devices",
                "instruction": "Name the technique used in each sentence:",
                "items": [
                    ("a", "'Can we really afford to ignore the wellbeing of our frontline team?'", "Rhetorical Question"),
                    ("b", "'Over 78% of staff surveyed expressed severe fatigue.'", "Statistic / Fact"),
                    ("c", "'This vital service provides safe, supportive, and specialist care.'", "Rule of Three"),
                    ("d", "'Failing to upgrade equipment will lead to catastrophic breakdowns.'", "Emotive Language"),
                    ("e", "'Together, you and I can transform patient recovery.'", "Direct Address")
                ]
            },
            {
                "title": "Applying the Rule of Three",
                "instruction": "Complete the rule of three with a third powerful word:",
                "items": [
                    ("a", "Our service must be efficient, reliable, and ___.", "compassionate / professional"),
                    ("b", "We need training that is accessible, practical, and ___.", "engaging / affordable"),
                    ("c", "The working environment should be clean, secure, and ___.", "welcoming / safe")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Workplace Campaign Article",
                "stem": "You are writing a persuasive article for your organisation's monthly newsletter campaigning for <strong>improved cycle-to-work facilities (secure bike lockers and showers)</strong>.<br><br>Draft a short persuasive paragraph (3-4 sentences) that includes:<br>• A direct address or rhetorical question<br>• A statistic or fact<br>• A rule of three.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Incorporate direct address or rhetorical question ('Have you ever arrived at work soaked...?')", "[W1]"),
                    ("Integrate a realistic workplace statistic ('Over 65% of staff live within cycling distance...')", "[W1]"),
                    ("Conclude with a rhythmic rule of three ('...making cycling healthier, cheaper, and greener.')", "[A1]")
                ],
                "final_answer": "'Have you ever considered cycling to work, only to be deterred by the lack of secure lockers and showers? Over 65% of our staff live within three miles of the clinic, yet less than 5% commute by bicycle. Investing in modern cycle storage would make our daily commute healthier, cheaper, and greener for everyone.'",
                "reverse_check": "Contains rhetorical question, statistic, and rule of three.",
                "pitfall": "Writing a dry informational statement without persuasive devices."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(ENGLISH_WRITING_BATCH3_WORKOUTS)} topics in authentic_workouts_english_writing_batch3.py")
