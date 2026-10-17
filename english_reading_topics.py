#!/usr/bin/env python3
"""
English Reading Topics (13 Topics)
Master Functional Skills Curriculum Suite — Deep Pedagogical Overhaul
"""

READING_TOPICS = [
    # 1. Fact or Opinion
    {
        "filename": "reading-fact-or-opinion.html",
        "clean_topic": "Fact or Opinion",
        "intro_lead": "Distinguish between verifiable objective facts and subjective opinions, recognize subtle author bias and opinions disguised as facts, and formulate evidence-based answers for Pearson Edexcel and City & Guilds assessments.",
        "next_file": "reading-meaning.html",
        "next_name": "Words in Context & Meaning",
        "spec_points": [
            ("L1.13 / L2.11", "Identify and distinguish between fact and opinion in workplace, instructional, and informative texts."),
            ("L2.14", "Recognise bias, detect opinions disguised as facts, and determine whether statements represent verifiable truth or subjective evaluation.")
        ],
        "golden_rules": [
            {
                "icon": "fa-magnifying-glass",
                "title": "Golden Rule 1: Facts Can Be Objectively Verified by Evidence",
                "desc": "A fact is verifiable using data, records, dates, measurements, or official statistics. If a statement can be checked against independent records and proven true or false, it is a fact — even if it sounds surprising.",
                "badge": "Test: Can an independent auditor, database, or measurement prove this true or false?"
            },
            {
                "icon": "fa-comment-dots",
                "title": "Golden Rule 2: Opinions Contain Subjective Value Judgments",
                "desc": "Opinions reflect personal feelings, beliefs, predictions, or recommendations. Look out for evaluative adjectives ('superb', 'appalling', 'vital', 'unfair') and modal verbs ('should', 'ought to').",
                "badge": "Test: Could two reasonable people disagree on this word (e.g. 'reasonable', 'delicious')?"
            }
        ],
        "skills": [
            {
                "title": "Spotting the Linguistic Clues for Facts vs Opinions",
                "summary": "Key linguistic signals and verification tests used in vocational reading.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Feature</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Objective Fact</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">Subjective Opinion</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Proof Basis</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Dates, statistics, medical readings, test scores, legal statutes, timestamps.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Personal perspectives, aesthetic impressions, moral judgments, unverified predictions.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Typical Vocabulary</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"recorded at 37.8°C", "exceeded 500 units", "founded in 1948", "contains 12g protein"</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"invaluable", "disappointing", "undoubtedly the finest", "unacceptable", "should be banned"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Agreement Test</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Universal once checked against official records.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Varies from person to person depending on personal taste or priorities.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Separating Mixed Sentences (Fact + Opinion in One Sentence)",
                "summary": "How Level 2 examiners hide a factual clause and an opinion clause inside the same sentence.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">In Level 2 exams, writers rarely put facts and opinions in neat, separate sentences. Instead, they blend a verifiable statistic with an evaluative adjective in the same sentence. You must <strong>slice the sentence in half</strong> and quote only the relevant clause:</p>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-top:0; color:#0f172a;"><strong>Mixed Sentence Example:</strong></p>
                  <p style="line-height:1.8; color:#334155; background:#fff; padding:14px; border-radius:6px; border:1px solid #e2e8f0;">
                    <span style="background:#dbeafe; padding:2px 6px; border-radius:4px;">[FACT CLAUSE] "The council spent £1.4 million resurfacing High Street in March,</span>
                    <span style="background:#ffedd5; padding:2px 6px; border-radius:4px;">[OPINION CLAUSE] which was a reckless waste of local taxpayers' money."</span>
                  </p>
                  <p style="margin-bottom:0; color:#475569; font-size:0.95rem;"><strong>Exam Rule:</strong> If asked for a fact, quote <em>"The council spent £1.4 million resurfacing High Street in March."</em> Do NOT copy the second half of the sentence, or you will lose the mark for including an opinion!</p>
                </div>
                """
            },
            {
                "title": "Unmasking Opinions Disguised as Facts (Level 2 Critical Skill)",
                "summary": "Recognize assertive introductory phrases and future predictions that masquerade as facts.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Persuasive writers often disguise their personal opinions using confident opener phrases or future claims:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>False Fact Openers:</strong> Phrases like <em>"It is an undeniable fact that..."</em>, <em>"Everyone knows that..."</em>, or <em>"Clearly, nobody can deny..."</em> followed by a value judgment (e.g. <em>"...remote working ruins team spirit"</em>) are still <strong>100% opinions</strong>.</li>
                  <li><strong>Unverified Future Predictions:</strong> A statement about the future (e.g., <em>"Opening the new bypass will completely solve town centre traffic by next summer"</em>) cannot be proven true right now, making it an <strong>opinion/claim</strong> rather than an established fact.</li>
                  <li><strong>Reported Survey Facts vs Direct Opinions:</strong> Note that <em>"72% of surveyed patients rated the food as excellent"</em> is a <strong>verifiable fact</strong> about what the survey recorded, whereas <em>"The hospital food is excellent"</em> is an <strong>opinion</strong>.</li>
                </ul>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Distinguishing Fact and Opinion in a Gym Flyer (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Community Leisure Centre Promotion",
                "question": "Read the extract from the leisure centre leaflet:<br><em>'Riverside Gym opens at 6:00 a.m. seven days a week and features 40 cardiovascular machines. Our friendly personal trainers deliver the most inspiring fitness classes in the region.'</em><br>(a) Extract <strong>one fact</strong> from the leaflet. [1 Mark]<br>(b) Extract <strong>one opinion</strong> from the leaflet. [1 Mark]",
                "steps": [
                    ("Step 1", "Extract a verifiable factual statement", "'Riverside Gym opens at 6:00 a.m. seven days a week' (or 'features 40 cardiovascular machines'). Both can be checked and proven.", "1 Mark [A1 Fact]"),
                    ("Step 2", "Extract the subjective opinion statement", "'Our friendly personal trainers deliver the most inspiring fitness classes in the region.' ('friendly' and 'most inspiring' are personal judgments).", "1 Mark [A1 Opinion]")
                ],
                "final_answer": "(a) Fact: 'Riverside Gym opens at 6:00 a.m. seven days a week' (or has 40 machines). | (b) Opinion: 'Our friendly personal trainers deliver the most inspiring fitness classes in the region.'",
                "tutor_tip": "At Level 1, copy the exact sentence or clause cleanly without changing the words."
            },
            {
                "title": "Hospital Ward Inspection Report Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "NHS Healthcare Compliance",
                "question": "Read the extract from the hospital audit report:<br><em>'Ward 4 admitted 142 patients in October. The nursing staff provided exceptional, heartwarming care throughout the winter surge. Patient discharge waiting times exceeded 3 hours.'</em><br>(a) Identify <strong>one fact</strong>. [1 Mark]<br>(b) Identify <strong>one opinion</strong>. [1 Mark]<br>(c) Explain why the opinion cannot be verified as an objective fact. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify the verifiable factual statement", "Option A: 'Ward 4 admitted 142 patients in October' OR Option B: 'Patient discharge waiting times exceeded 3 hours.' Both can be verified from hospital admission logs.", "1 Mark [A1 Fact]"),
                    ("Step 2", "Identify the subjective opinion", "'The nursing staff provided exceptional, heartwarming care throughout the winter surge.'", "1 Mark [A1 Opinion]"),
                    ("Step 3", "Explain why the opinion is unverifiable", "'Exceptional' and 'heartwarming' are evaluative value judgments based on subjective personal feelings rather than clinical numerical metrics.", "1 Mark [A1 Justification]")
                ],
                "final_answer": "Fact: 'Ward 4 admitted 142 patients in October' | Opinion: 'The nursing staff provided exceptional, heartwarming care' | Reason: It uses evaluative adjectives reflecting personal perception rather than measurable data.",
                "tutor_tip": "In Pearson Edexcel exams, always copy the exact quotation for the fact and opinion, and make sure your explanation clearly mentions subjective language or lack of measurable proof."
            }
        ],
        "examiner_traps": [
            {
                "title": "Treating Expert Quotes as Automatic Facts",
                "desc": "Just because a senior doctor or chief executive says 'This is the best ward management app available', that does not make the claim itself a fact. It remains an informed professional opinion.",
                "fix": "Ask: Is the statement an empirical measurement, or is it an expert's qualitative value judgment?"
            },
            {
                "title": "Copying a Whole Mixed Sentence for a Fact Question",
                "desc": "If a sentence contains both a statistic and an emotive adjective ('The £50 ticket is a total rip-off') and you copy the entire sentence as a fact, you score 0 because 'total rip-off' is an opinion.",
                "fix": "Trim your quotation so it includes only the factual clause."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics fleet report states: <em>'The electric delivery vans cut depot fuel expenditure by £14,500 between January and June. They are undeniably the most stylish commercial vehicles on British roads today.'</em><br>Extract <strong>one fact</strong> and <strong>one opinion</strong> from this statement.",
                "solution_steps": "1. Fact: 'The electric delivery vans cut depot fuel expenditure by £14,500 between January and June.' (verifiable in accounting records) [1 Mark].<br>2. Opinion: 'They are undeniably the most stylish commercial vehicles on British roads today.' (subjective aesthetic judgment) [1 Mark].",
                "correct_answer": "Fact: Reduced fuel expenditure by £14,500 between January and June. | Opinion: Most stylish commercial vehicles on British roads today.",
                "tutor_tip": "Do not be fooled by the word 'undeniably' — 'most stylish' is still a subjective opinion about appearance."
            },
            {
                "marks": "2 Marks",
                "question": "Read this mixed sentence from a restaurant review:<br><em>'The bistro charges £18.50 for its two-course lunch menu, which is an outrageous price for such tiny portions.'</em><br>Separate this single sentence into <strong>one fact</strong> and <strong>one opinion</strong>.",
                "solution_steps": "1. Fact clause: 'The bistro charges £18.50 for its two-course lunch menu' (can be verified on the printed menu) [1 Mark].<br>2. Opinion clause: 'which is an outrageous price for such tiny portions' ('outrageous' and 'tiny' are subjective value judgments) [1 Mark].",
                "correct_answer": "Fact: The bistro charges £18.50 for its two-course lunch menu. | Opinion: It is an outrageous price for tiny portions.",
                "tutor_tip": "Slice the mixed sentence cleanly at the comma so your fact contains zero evaluative adjectives."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a campaign leaflet:<br><em>'It is a proven fact that the council's new 20 mph speed limit is a ridiculous inconvenience that will ruin every delivery driver's schedule.'</em><br>Explain why this statement is actually an <strong>opinion</strong> despite starting with <em>'It is a proven fact that...'</em>, and quote <strong>two subjective words or phrases</strong> as evidence. [3 Marks]",
                "solution_steps": "1. Explanation: Starting a sentence with 'It is a proven fact' is a rhetorical assertion that does not make the claim verifiable; it also makes an unproven prediction about the future [1 Mark].<br>2. Subjective Quote 1: 'ridiculous inconvenience' (evaluative judgment) [1 Mark].<br>3. Subjective Quote 2: 'will ruin every delivery driver's schedule' (exaggerated future prediction) [1 Mark].",
                "correct_answer": "The phrase 'It is a proven fact' is used persuasively to disguise a personal viewpoint. The quotes 'ridiculous inconvenience' and 'will ruin every delivery driver's schedule' are subjective judgments and unproven predictions.",
                "tutor_tip": "Always ignore assertive openers like 'It is a fact that...' and test the actual words that follow!"
            }
        ]
    },
    # 2. Meaning / Words in Context
    {
        "filename": "reading-meaning.html",
        "clean_topic": "Words in Context & Meaning",
        "intro_lead": "Decode unfamiliar vocabulary in context, distinguish literal versus implicit and figurative meanings, and provide exact synonyms that pass the Pearson Edexcel substitution test.",
        "next_file": "reading-specialist-words.html",
        "next_name": "Specialist Vocabulary",
        "spec_points": [
            ("L1.10 / L2.10", "Understand vocabulary and determine how meaning is conveyed through word choice in context."),
            ("L1.9 / L2.11", "Identify and explain implicit (suggested) and explicit (stated) meanings across extended workplace texts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-compass",
                "title": "Golden Rule 1: The Synonym Substitution & Grammar Test",
                "desc": "When asked to give a word or phrase that can 'replace' a target word in the text, your answer MUST match the exact part of speech and verb tense (e.g., if the target word ends in '-ed' or '-ing', your replacement must also fit grammatically into the original sentence).",
                "badge": "Test: Plug your word back into the original sentence. Does it read grammatically?"
            },
            {
                "icon": "fa-arrows-split-up-and-left",
                "title": "Golden Rule 2: Distinguish Explicit from Implicit Meaning",
                "desc": "Explicit meaning is stated directly on the page. Implicit meaning is hinted at between the lines — you must deduce it from clues, tone, and actions.",
                "badge": "Explicit = Directly stated | Implicit = Suggested / Inferred from clues"
            }
        ],
        "skills": [
            {
                "title": "Four-Step Contextual Clue Decoding Strategy",
                "summary": "How to decipher unfamiliar vocabulary under exam pressure without a dictionary.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>Identify the Part of Speech:</strong> Check whether the target word is a noun (thing), verb (action), adjective (describing a noun), or adverb (ending in <em>-ly</em>).</li>
                    <li><strong>Look for Surrounding Synonym or Contrast Clues:</strong> Read the clause before and after. Words like <em>"or"</em>, <em>"such as"</em>, and <em>"unlike"</em> often reveal the meaning (e.g., <em>"Unlike the <u>gregarious</u> sales team, the night auditor preferred working alone"</em> &rarr; <em>gregarious</em> means outgoing/sociable).</li>
                    <li><strong>Check Positive vs Negative Connotation:</strong> Does the sentence describe a hazard/problem (negative word) or a benefit/achievement (positive word)?</li>
                    <li><strong>Run the Substitution Check:</strong> Swap your chosen synonym into the sentence to verify both meaning and grammatical fit.</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Polysemous Words: Choosing the Right Meaning for the Context",
                "summary": "Why common English words change meaning completely depending on the workplace setting.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Examiners love testing words that have multiple dictionary definitions (polysemy). You only score the mark if you give the definition that fits the specific passage:</p>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Target Word</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#be123c;">Wrong Meaning (Wrong Context)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Correct Contextual Meaning</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Critical"</em><br>(in a hospital report: <em>"critical equipment"</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Finding fault or criticising someone unfairly.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Essential, vital, or life-saving.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Reservation"</em><br>(in a policy meeting: <em>"expressed reservations"</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Booking a table at a restaurant or hotel room.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Doubts, concerns, or hesitations about a plan.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Measure"</em><br>(in a council memo: <em>"introduced new measures"</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Checking length with a tape or ruler.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Actions, steps, or policies taken to achieve a goal.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Inferring Implicit Meaning & Subtext (Level 2)",
                "summary": "How to read between the lines when an author hints at an outcome without stating it outright.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">In Level 2 exams, questions asking <em>"What is implied by..."</em> or <em>"What does the writer suggest when..."</em> test <strong>inference</strong>. Look at this example:</p>
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>Excerpt:</strong> <em>"When the health inspector opened the kitchen cold-room door, he immediately reached for his red prohibition notice pad."</em><br><strong>Explicit Meaning:</strong> The inspector opened the door and took out his red pad.<br><strong>Implicit (Inferred) Meaning:</strong> The cold room was in such a dangerously unhygienic state that the inspector decided to shut the kitchen down on the spot.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Word Replacement in a Workplace Notice (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Office Facilities Refurbishment",
                "question": "Read the sentence from the office manager's email:<br><em>'The air-conditioning repairs are <strong>mandatory</strong> and will cause <strong>minimal</strong> disruption to reception staff.'</em><br>(a) Give one word or phrase that can replace <strong>'mandatory'</strong> in this sentence. [1 Mark]<br>(b) Give one word or phrase that can replace <strong>'minimal'</strong> in this sentence. [1 Mark]",
                "steps": [
                    ("Step 1", "Decode 'mandatory' in the context of safety repairs", "'Mandatory' means required by rule or compulsory. Substituting 'compulsory' or 'essential' fits grammatically.", "1 Mark [A1 Meaning 1]"),
                    ("Step 2", "Decode 'minimal' in the context of disruption", "'Minimal' means very little, slight, or the smallest possible amount.", "1 Mark [A1 Meaning 2]")
                ],
                "final_answer": "(a) Mandatory: compulsory / required / obligatory. | (b) Minimal: very little / slight / negligible.",
                "tutor_tip": "Test your word in the sentence: 'The repairs are compulsory and will cause very little disruption' — it makes complete grammatical sense!"
            },
            {
                "title": "Care Home Policy Handbook Vocabulary & Inference (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Social Care Quality Assurance",
                "question": "An extract from the residential home guidelines states:<br><em>'Night staff must remain <strong>vigilant</strong> regarding subtle <strong>fluctuations</strong> in a resident's baseline vital signs, as elderly patients rarely voice discomfort until a condition has deteriorated.'</em><br>(a) In this context, what is the meaning of the word <strong>'vigilant'</strong>? [1 Mark]<br>(b) What is meant by <strong>'fluctuations'</strong>? [1 Mark]<br>(c) What does the final clause imply about relying solely on patients asking for help? [1 Mark]",
                "steps": [
                    ("Step 1", "Define 'vigilant' using the clinical supervision context", "'Vigilant' means being alert, watchful, observant, or carefully attentive to potential risks.", "1 Mark [A1 Meaning]"),
                    ("Step 2", "Define 'fluctuations' in relation to vital signs", "'Fluctuations' means irregular changes, rises and falls, or variations in measurements over time.", "1 Mark [A1 Meaning]"),
                    ("Step 3", "Explain the implicit warning in the final clause", "It implies that waiting for elderly residents to complain is unsafe because by the time they speak up, their illness is already severe.", "1 Mark [A1 Inference]")
                ],
                "final_answer": "(a) Vigilant: Alert, watchful, or attentively monitoring. | (b) Fluctuations: Irregular changes, rises and falls, or variations. | (c) Implies that waiting for residents to report pain is dangerous because their health will already have worsened significantly.",
                "tutor_tip": "Never use the target word itself (or a root variation like 'fluctuating') in your definition!"
            }
        ],
        "examiner_traps": [
            {
                "title": "Giving a General Dictionary Definition Instead of Contextual Meaning",
                "desc": "A word like 'reservations' can mean 'restaurant bookings' or 'doubts/concerns'. Giving 'bookings' when the text says 'The union had reservations about the contract' scores 0.",
                "fix": "Always re-read the sentence with your chosen definition substituted in place of the original word."
            },
            {
                "title": "Mismatching Verb Tense or Word Class on 'Replace' Questions",
                "desc": "If the question asks for a word to replace 'accelerated' (past tense verb) and you write 'speed up' (present tense) or 'fast' (adjective), it fails the grammatical substitution check.",
                "fix": "Match past tense with past tense ('accelerated' -> 'sped up' or 'increased')."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A workshop safety notice reads: <em>'Failure to <strong>isolate</strong> electrical machinery prior to maintenance poses <strong>imminent</strong> danger to technicians.'</em><br>Explain what is meant by <strong>'isolate'</strong> and <strong>'imminent'</strong> in this context.",
                "solution_steps": "1. Isolate: Disconnect, switch off, or separate completely from the electrical power supply [1 Mark].<br>2. Imminent: About to happen immediately, instant, or looming right away [1 Mark].",
                "correct_answer": "Isolate = Disconnect / cut off from the power supply. | Imminent = About to happen immediately / instant.",
                "tutor_tip": "Notice how 'isolate' in an electrical context specifically means disconnecting from power, not social isolation."
            },
            {
                "marks": "2 Marks",
                "question": "Read this sentence from a council housing report:<br><em>'The committee expressed grave <strong>reservations</strong> about building on the flood plain and voted to <strong>defer</strong> the decision until November.'</em><br>Give one word or phrase to replace (a) <strong>'reservations'</strong> and (b) <strong>'defer'</strong>.",
                "solution_steps": "1. 'reservations' in a committee debate means doubts, concerns, or misgivings [1 Mark].<br>2. 'defer' means to postpone, delay, or put off until a later date [1 Mark].",
                "correct_answer": "(a) Reservations: doubts / concerns / hesitations. | (b) Defer: postpone / delay / put off.",
                "tutor_tip": "Check the time clue 'until November' — that confirms 'defer' means postpone/delay!"
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a retail manager's appraisal note:<br><em>'Although Marcus is punctual and polite at the till, he consistently disappears into the stockroom whenever a delivery lorry arrives for unloading.'</em><br>What is the manager <strong>implying</strong> about Marcus in the second half of the sentence?",
                "solution_steps": "1. Identify the implied behaviour: Marcus deliberately avoids heavy physical work / unloading duties [1 Mark].<br>2. Link to the textual clue: The word 'consistently' shows it is a deliberate habit rather than a coincidence whenever a lorry arrives [1 Mark].",
                "correct_answer": "The manager is implying that Marcus deliberately avoids the heavy physical work of unloading delivery lorries.",
                "tutor_tip": "Implicit questions ask you to explain the unstated motive behind the action described."
            }
        ]
    },
    # 3. Specialist & Technical Vocabulary
    {
        "filename": "reading-specialist-words.html",
        "clean_topic": "Specialist & Technical Vocabulary",
        "intro_lead": "Master workplace jargon, regulatory acronyms, and industry-specific terminology across healthcare, construction, logistics, finance, and digital environments.",
        "next_file": "reading-presentational-features.html",
        "next_name": "Presentational Features",
        "spec_points": [
            ("L1.11 / L2.10", "Understand and explain specialist and technical vocabulary in vocational and regulatory texts."),
            ("L2.16", "Recognise how glossaries, parenthetical definitions, and prefixes/suffixes clarify technical terms for different audiences.")
        ],
        "golden_rules": [
            {
                "icon": "fa-book-medical",
                "title": "Golden Rule 1: Hunt for In-Text Brackets, Dashes & Glossaries First",
                "desc": "Informational texts frequently define technical acronyms or specialist terms immediately upon first mention using brackets, dashes, or appositive commas (e.g., 'tachycardia — an abnormally rapid heart rate — must be logged'). Always check adjacent punctuation!",
                "badge": "Check brackets ( ), dashes — —, footnotes (*), and glossary boxes first."
            },
            {
                "icon": "fa-network-wired",
                "title": "Golden Rule 2: Break Down Prefixes, Roots, and Suffixes",
                "desc": "When no glossary is given, split compound specialist words into familiar building blocks (e.g., 'anti-' = against, 'co-' = together, 'mal-' = bad/faulty, 'cardio-' = heart, 'therm-' = heat, 'musculo-skeletal' = muscles and bones).",
                "badge": "Prefix + Root + Suffix + Sentence Context = Accurate Technical Definition"
            }
        ],
        "skills": [
            {
                "title": "Common Specialist Terms Across Functional Vocations",
                "summary": "Core industry terminology frequently examined in Level 1 & Level 2 Reading papers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Sector</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Specialist Terms &amp; Acronyms</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Plain-English Definition</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Healthcare &amp; Social Care</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>Contraindicated, Prognosis, Safeguarding, Triage, PPE</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Unsafe to give a patient; expected recovery outcome; protecting vulnerable people; sorting by urgency; Personal Protective Equipment.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Health, Safety &amp; Estates</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>COSHH, RIDDOR, Ergonomic, Carcinogen, Mitigate</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Hazardous substances rules; injury reporting law; designed for safe posture; cancer-causing agent; reduce risk severity.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Business, Finance &amp; Logistics</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>Procurement, Inventory, Deficit, Remittance, Lead Time</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Purchasing supplies; stock on hand; financial shortfall; payment sent; waiting time between order and delivery.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Prefix & Root Decoding Toolkit for Unseen Technical Words",
                "summary": "Decode complex medical, scientific, and administrative words by recognising their Latin/Greek prefixes.",
                "content_html": """
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:14px; margin:16px 0;">
                  <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:14px; border-radius:6px;">
                    <strong style="color:#0369a1;">Medical &amp; Science Prefixes:</strong>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:6px 0 0 0;">
                      <li><strong>Hyper- / Hypo-:</strong> Too high (<em>hypertension</em>) / Too low (<em>hypothermia</em>)</li>
                      <li><strong>Anti- / Contra-:</strong> Against (<em>antiseptic, contraindicated</em>)</li>
                      <li><strong>Bio- / Eco-:</strong> Life / Environment (<em>biodegradable</em>)</li>
                    </ul>
                  </div>
                  <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px; border-radius:6px;">
                    <strong style="color:#166534;">Workplace &amp; Admin Prefixes:</strong>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:6px 0 0 0;">
                      <li><strong>Inter- / Intra-:</strong> Between groups / Within one organisation (<em>intranet</em>)</li>
                      <li><strong>Mal- / Mis-:</strong> Faulty or wrong (<em>malfunction, misconduct</em>)</li>
                      <li><strong>Sub- / Super-:</strong> Under (<em>subcontractor</em>) / Over (<em>supervisor</em>)</li>
                    </ul>
                  </div>
                </div>
                """
            },
            {
                "title": "Why Writers Use Specialist Jargon (Effect on Audience)",
                "summary": "How to answer Level 2 questions asking WHY an author included technical terminology.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">In Level 2 exams, you may be asked: <em>"Why does the writer use specialist terms like 'photovoltaic inverter' and 'kilowatt-hour yield' in this report?"</em> Use these three model reasons:</p>
                <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                  <li><strong>Establishes Professional Authority &amp; Credibility:</strong> Proves the writer is a qualified expert who understands the industry deeply.</li>
                  <li><strong>Delivers Exact Technical Precision:</strong> Avoids ambiguity when giving legal, medical, or engineering specifications where vague everyday words could cause errors.</li>
                  <li><strong>Matches a Specialist Target Audience:</strong> Signals that the document is written for trained peers (e.g. electricians, nurses) rather than the general public.</li>
                </ol>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Using In-Text Clues to Define Workplace Jargon (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Catering Kitchen Induction Manual",
                "question": "Read the extract from the food hygiene manual:<br><em>'All raw poultry must be stored on the bottom shelf of the walk-in chiller to prevent <strong>pathogens</strong> (harmful bacteria that cause food poisoning) from dripping onto ready-to-eat foods and causing <strong>cross-contamination</strong>.'</em><br>(a) According to the text, what are <strong>'pathogens'</strong>? [1 Mark]<br>(b) In your own words, explain what <strong>'cross-contamination'</strong> means in this sentence. [1 Mark]",
                "steps": [
                    ("Step 1", "Locate the bracketed in-text definition for 'pathogens'", "The brackets immediately after 'pathogens' define them as 'harmful bacteria that cause food poisoning'.", "1 Mark [A1 In-Text Definition]"),
                    ("Step 2", "Deduce 'cross-contamination' from the surrounding action", "It means the transfer/spreading of harmful bacteria from raw food (poultry) onto clean, ready-to-eat food.", "1 Mark [A1 Contextual Meaning]")
                ],
                "final_answer": "(a) Pathogens: Harmful bacteria that cause food poisoning. | (b) Cross-contamination: When bacteria from raw food drip onto or spread to ready-to-eat food.",
                "tutor_tip": "Always check right next to a bold or unfamiliar word for brackets ( ) or dashes — examiners often hide the exact definition right there!"
            },
            {
                "title": "Warehouse Safety Protocol & Effect of Technical Register (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Occupational Health & Safety Audit",
                "question": "A warehouse safety manual states:<br><em>'Operatives must adhere to <strong>ergonomic</strong> guidelines when handling palletised freight to <strong>mitigate</strong> chronic <strong>musculoskeletal</strong> strain.'</em><br>(a) What is meant by <strong>'ergonomic guidelines'</strong> and <strong>'musculoskeletal strain'</strong>? [2 Marks]<br>(b) Why has the writer chosen formal technical vocabulary in this manual? [1 Mark]",
                "steps": [
                    ("Step 1", "Define 'ergonomic guidelines' and 'musculoskeletal strain'", "'Ergonomic guidelines' are rules designed to fit the human body safely and efficiently during physical work; 'musculoskeletal strain' means injury or damage to muscles, bones, and joints.", "2 Marks [A1 Technical Definitions]"),
                    ("Step 2", "Explain the purpose of using specialist terminology", "It establishes authoritative occupational health precision and ensures compliance with official workplace safety standards.", "1 Mark [A1 Register Effect]")
                ],
                "final_answer": "(a) Ergonomic guidelines: Safe lifting and posture rules designed to protect the body; Musculoskeletal strain: Injury to muscles and bones/joints. | (b) Conveys professional authority and precise health-and-safety compliance.",
                "tutor_tip": "Look at the word 'musculoskeletal' — splitting it into 'musculo' (muscles) and 'skeletal' (skeleton/bones) gives you the exact definition immediately."
            }
        ],
        "examiner_traps": [
            {
                "title": "Guessing Acronyms Instead of Checking the Text",
                "desc": "Candidates sometimes guess what an acronym like 'MAR' or 'PPE' stands for using everyday slang instead of scanning the text or footer glossary where the full expansion ('Medication Administration Record') is printed.",
                "fix": "Always scan the first mention of an acronym or the bottom of the text box for its expanded name."
            },
            {
                "title": "Repeating the Root Word Inside Your Definition",
                "desc": "Defining 'biodegradable packaging' as 'packaging that degrades biologically' is too circular to guarantee the mark.",
                "fix": "Translate into plain everyday words: 'packaging that breaks down naturally in the environment without causing pollution'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A pharmacy dispensing notice states: <em>'This oral suspension is <strong>contraindicated</strong> for patients with severe <strong>renal impairment</strong>.'</em><br>Explain what is meant by (a) <strong>'contraindicated'</strong> and (b) <strong>'renal impairment'</strong>.",
                "solution_steps": "1. (a) Contraindicated: Not advisable, unsafe, or must not be given to the patient due to risk of harm [1 Mark].<br>2. (b) Renal impairment: Kidney damage, kidney disease, or reduced kidney function [1 Mark].",
                "correct_answer": "(a) Contraindicated: Unsafe / should not be given to the patient. | (b) Renal impairment: Poor kidney function or kidney damage.",
                "tutor_tip": "Remember: 'contra-' means against, so 'contraindicated' means advised against."
            },
            {
                "marks": "2 Marks",
                "question": "An IT security memo states: <em>'Staff must only access patient records via the Trust <strong>intranet</strong> and must never click links in suspected <strong>phishing</strong> emails.'</em><br>Explain the meaning of (a) <strong>'intranet'</strong> and (b) <strong>'phishing'</strong>.",
                "solution_steps": "1. (a) Intranet: A private, internal computer network accessible only to staff within that organisation [1 Mark].<br>2. (b) Phishing: Fraudulent/scam emails designed to trick staff into revealing passwords or sensitive data [1 Mark].",
                "correct_answer": "(a) Intranet: A private internal network used only inside the organisation. | (b) Phishing: Scam emails sent to steal passwords or confidential information.",
                "tutor_tip": "Do not confuse 'intranet' (internal private network) with 'internet' (public global network)!"
            },
            {
                "marks": "2 Marks",
                "question": "A building surveyor's report states: <em>'The garage roof contains damaged <strong>asbestos</strong> lagging, which is a known <strong>carcinogen</strong> requiring licensed removal.'</em><br>What does the specialist word <strong>'carcinogen'</strong> mean, and why did the surveyor use this technical term?",
                "solution_steps": "1. Meaning: A substance capable of causing cancer in living tissue [1 Mark].<br>2. Reason for use: Conveys the severe, life-threatening medical and legal hazard precisely so the property owner uses licensed specialists [1 Mark].",
                "correct_answer": "Meaning: A substance that causes cancer. | Reason: Highlights the serious medical danger with professional authority so safe licensed removal is arranged.",
                "tutor_tip": "Linking technical terms to safety compliance and authority always scores well in Level 2."
            }
        ]
    },
    # 4. Presentational Features
    {
        "filename": "reading-presentational-features.html",
        "clean_topic": "Presentational Features",
        "intro_lead": "Analyze headings, subheadings, bold/italic typography, bullet points, numbered lists, pull-out quotes, and colour callout boxes to explain how visual formatting enhances meaning and guides reader attention.",
        "next_file": "reading-investigating-layout.html",
        "next_name": "Layout Devices",
        "spec_points": [
            ("L1.14 / L2.16", "Recognise and explain how presentational and organisational features aid understanding and convey information."),
            ("L2.17", "Analyse how formatting, typographic emphasis, and visual signposts support the writer's overall purpose.")
        ],
        "golden_rules": [
            {
                "icon": "fa-table-columns",
                "title": "Golden Rule 1: Link Every Feature to Specific Content & Reader Effect",
                "desc": "You only get half the marks for naming a feature (e.g. 'bullet points' or 'bold heading'). To score full marks, state WHAT specific information the feature highlights in that text and HOW it helps the reader.",
                "badge": "Formula: [Presentational Feature] + [Specific Content Shown] + [How It Helps the Reader]"
            },
            {
                "icon": "fa-eye",
                "title": "Golden Rule 2: Never Confuse Presentational Features with Language Features",
                "desc": "Presentational features are visual formatting elements you can see without reading the words (bold, bullet points, subheadings, boxes, photos). Language features are word choices (metaphors, rhetorical questions, rule of three).",
                "badge": "Visual Formatting = Presentational | Word Choice & Figures of Speech = Language"
            }
        ],
        "skills": [
            {
                "title": "Catalogue of Core Presentational Devices & Their Exact Effects",
                "summary": "The standard typographical and visual features tested in Functional Skills Reading papers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Presentational Feature</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">How to Recognise It</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Accredited Exam Explanation (Effect)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Main Heading / Headline</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Largest bold title at the very top of the page.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Immediately announces the core topic (e.g. <em>'New Fire Drill Rules'</em>) and grabs the target audience's attention.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Subheadings</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Smaller bold titles dividing sections of the body text.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Breaks a long document into thematic sections so readers can scan straight to relevant information (e.g. <em>'Ticket Prices'</em>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Bullet Points</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Indented list items marked with dots (•).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Separates key facts or kit items into bite-sized points that are easy to digest at a glance without reading dense prose.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Numbered List</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Items marked 1, 2, 3 in order.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Sets out a clear chronological sequence of steps that the reader must follow in exact order.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Bold / Capitalised Text</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Darker, thicker letters or ALL CAPS within a sentence.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Creates visual contrast to emphasise vital warnings, deadlines, or key terms (e.g. <em>'<strong>DO NOT</strong> enter'</em>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Shaded Box / Callout Panel</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Text enclosed in a coloured or bordered rectangle.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Isolates high-priority details (such as emergency phone numbers or discount codes) from the surrounding paragraphs.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Digital & Webpage Presentational Features",
                "summary": "Recognize hyperlinks, navigation bars, search boxes, and dropdown menus in online source texts.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Many Functional Skills source texts are mock webpages, staff intranets, or discussion forums. When asked for presentational/organisational features of an online text, look for:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Hyperlinks (Underlined / Blue Text):</strong> Allows the user to click directly to related pages, booking forms, or external policies for deeper detail.</li>
                  <li><strong>Top Navigation Bar / Menu Tabs:</strong> Lets users switch rapidly between site categories (e.g. <em>Home | Services | Book Appointment | Contact Us</em>).</li>
                  <li><strong>Search Bar &amp; Filter Buttons:</strong> Enables users to type keywords and jump straight to specific articles without scrolling.</li>
                  <li><strong>Star Ratings / Timestamped Avatars:</strong> In review or forum texts, visually shows user satisfaction scores at a glance and indicates when each comment was posted.</li>
                </ul>
                """
            },
            {
                "title": "Level 1 Identification vs Level 2 Contextual Evaluation",
                "summary": "How to tailor your answer to the mark tariff.",
                "content_html": """
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>At Level 1 (e.g. "List two organisational features used in Text A"):</strong> Simply naming the features accurately (<em>"1. Subheadings. 2. Bullet points."</em>) secures full marks.<br><strong>At Level 2 (e.g. "Explain how two presentational features help the writer achieve their purpose"):</strong> You MUST link each feature to the specific content of the text (<em>"The bold red subheading 'URGENT PRODUCT RECALL' immediately alerts customers to the safety risk, while the bulleted list of serial numbers allows shoppers to check their kettle model quickly."</em>).</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Presentational Features in a Clinic Appointment Card (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "NHS Outpatient Appointment Letter",
                "question": "An outpatient letter includes the following formatted section:<br><strong>WHAT TO BRING TO YOUR SCAN:</strong><br>• Your appointment reference letter<br>• A list of your current prescribed tablets<br><em><strong>IMPORTANT: Do not eat any solid food for 6 hours before your scan.</strong></em><br>Identify <strong>two presentational features</strong> used in this extract and state what information each one highlights. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify Feature 1 and link to content", "Bullet points — used to list the two items the patient needs to bring to the scan clearly.", "1 Mark [A1 Feature 1]"),
                    ("Step 2", "Identify Feature 2 and link to content", "Bold/capitalised text (and italics) — used on the heading 'WHAT TO BRING TO YOUR SCAN' and to emphasise the urgent fasting rule ('IMPORTANT: Do not eat...').", "1 Mark [A1 Feature 2]")
                ],
                "final_answer": "1. Bullet points: Clearly list the items the patient must bring. | 2. Bold and capital letters: Emphasise the section title and the crucial rule not to eat for 6 hours before the scan.",
                "tutor_tip": "Always mention what information the bullet points or bold text actually show!"
            },
            {
                "title": "Fire Evacuation Workplace Notice Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Facility Management & Safety",
                "question": "A workplace emergency evacuation poster features:<br>• A large bold red banner heading: <strong>FIRE ACTION: IF YOU DISCOVER A FIRE</strong><br>• A <strong>numbered list (1 to 4)</strong> setting out the alarm and exit steps<br>• A <strong>green shaded box</strong> at the bottom reading: <em>'Assembly Point: Car Park Zone C'</em>.<br>(a) Identify two different presentational features used in the poster. [1 Mark]<br>(b) Explain how two of these features help staff during a real emergency. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify two distinct presentational features", "Feature 1: Bold capitalised red banner heading. Feature 2: Numbered list (1 to 4) / Green shaded callout box.", "1 Mark [A1 Features]"),
                    ("Step 2", "Explain the practical effect of the numbered list", "The numbered list (1 to 4) presents the evacuation sequence in strict chronological order so panicked employees can follow the exact escape steps rapidly without reading dense paragraphs.", "1 Mark [A1 Effect 1]"),
                    ("Step 3", "Explain the practical effect of the green shaded box", "The green shaded box visually separates the final meeting location ('Assembly Point: Car Park Zone C') so fleeing staff can spot where to gather at a glance.", "1 Mark [A1 Effect 2]")
                ],
                "final_answer": "(a) Bold red banner heading, numbered list, and green shaded box. | (b) 1. The numbered list allows panicked staff to follow the escape steps in exact chronological order. 2. The green shaded box makes the Car Park Zone C assembly point stand out instantly.",
                "tutor_tip": "Never give vague answers like 'it makes it look pretty'. Always explain how the formatting helps a busy or panicked reader process the information faster."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Language Features with Presentational Features",
                "desc": "Alliteration, rhetorical questions, and metaphors are language techniques. Bold fonts, tables, bullet points, subheadings, and shaded boxes are presentational features.",
                "fix": "Ask: 'Is this a visual design/formatting choice on the page?' If yes, it is a presentational feature."
            },
            {
                "title": "Saying 'It Makes the Page Look Less Boring'",
                "desc": "Examiners award 0 marks for saying bullet points or subheadings 'make the text look nice/less boring'.",
                "fix": "Use functional verbs: 'breaks complex information into scannable points', 'guides the reader's eye to urgent warnings', or 'enables rapid navigation'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "An NHS appointment booking webpage features a prominent yellow shaded box at the top stating: <em>'<strong>URGENT:</strong> Please arrive 15 minutes before your scheduled MRI scan.'</em><br>Identify <strong>two presentational features</strong> used here and explain their purpose.",
                "solution_steps": "1. Features: Yellow shaded callout box AND bold capital letters on 'URGENT:' [1 Mark].<br>2. Purpose: Draws immediate visual attention to the time-sensitive arrival requirement (15 minutes early) so patients do not miss their MRI slot [1 Mark].",
                "correct_answer": "Features: Shaded yellow box and bold capital letters ('URGENT'). | Purpose: Immediately alerts patients to the requirement to arrive 15 minutes early before they read the rest of the page.",
                "tutor_tip": "Identify both the container (shaded box) and the typography (bold capitals), then link them to the 15-minute arrival rule."
            },
            {
                "marks": "2 Marks",
                "question": "A staff intranet guide on claiming travel expenses includes underlined blue text reading: <em>'<u>Click here to download the Mileage Claim Form (PDF)</u>'</em>.<br>Name this presentational feature and explain how it helps employees.",
                "solution_steps": "1. Feature: Hyperlink (clickable link) [1 Mark].<br>2. Effect: Allows employees to open and download the required Mileage Claim Form directly with one click without having to search the intranet manually [1 Mark].",
                "correct_answer": "Feature: Hyperlink. | Effect: Gives staff instant one-click access to download the Mileage Claim Form without searching for it.",
                "tutor_tip": "Whenever you see underlined blue clickable text in an online source, name it specifically as a 'hyperlink'."
            },
            {
                "marks": "3 Marks",
                "question": "A magazine article reviewing electric vans includes a large, bordered box in the middle of the page printing a quote in oversized italics: <em>'\"Switching our bakery vans to electric saved us £3,400 in diesel in just six months!\" — Sarah Lin, Owner'</em>.<br>Name this presentational feature [1 Mark] and give <strong>two reasons</strong> why the editor included it [2 Marks].",
                "solution_steps": "1. Feature: Pull quote / callout quote box (with oversized italics) [1 Mark].<br>2. Reason 1: Breaks up dense columns of text and hooks skimming readers' attention [1 Mark].<br>3. Reason 2: Highlights the most persuasive real-life financial saving (£3,400 saved in six months) to convince other business owners [1 Mark].",
                "correct_answer": "Feature: Pull quote / boxed quotation in italics. | Reasons: 1. Breaks up the article layout to grab skimming readers' attention. 2. Emphasises the impressive £3,400 fuel saving to persuade business readers.",
                "tutor_tip": "A quotation lifted from an article and printed in large font inside a box is called a 'pull quote' or 'callout quote'."
            }
        ]
    },
    # 5. Investigating Layout
    {
        "filename": "reading-investigating-layout.html",
        "clean_topic": "Layout Devices & Visual Signposting",
        "intro_lead": "Evaluate how page architecture, multi-column grids, tables, sidebars, white space, and structural signposting guide the reader's eye and establish information hierarchy.",
        "next_file": "reading-investigating-image.html",
        "next_name": "Images & Visual Effects",
        "spec_points": [
            ("L1.14 / L2.16", "Understand how layout and organisational devices structure complex information for rapid retrieval."),
            ("L2.17", "Analyse the relationship between textual hierarchy, columns, tables, sidebars, and reader navigation.")
        ],
        "golden_rules": [
            {
                "icon": "fa-layer-group",
                "title": "Golden Rule 1: Visual Hierarchy Directs Reading Order",
                "desc": "Page layout is engineered so the primary message occupies top prominence (banner headline), secondary themes are divided into columns or sub-sections, and reference details sit in sidebars or footers.",
                "badge": "Top-to-bottom, large-to-small: track how visual weight dictates reader attention."
            },
            {
                "icon": "fa-border-all",
                "title": "Golden Rule 2: Tables & Sidebars Isolate Practical Lookup Data",
                "desc": "Whenever a writer puts times, prices, dosages, or contact numbers into a table or sidebar instead of a paragraph, their goal is to enable instant cross-referencing without scanning walls of prose.",
                "badge": "Tables = Fast row/column lookup | Sidebars = Separated quick-reference facts"
            }
        ],
        "skills": [
            {
                "title": "Deconstructing Page Architecture in Professional Documents",
                "summary": "How columns, tables, sidebars, and headers/footers work together.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Layout Element</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Where It Appears</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Why Designers Use It</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Multi-Column Grid</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Newspaper articles, staff newsletters, three-fold leaflets.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Keeps line lengths short so the eye can read rapidly down narrow columns without losing its place.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Dedicated Sidebar</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Vertical panel running down the left or right edge.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Separates practical summary info (e.g. <em>Opening Hours, Helpline Numbers, Checklist</em>) from the main article.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Data Table / Grid</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Timetables, price lists, dosage charts, shift rosters.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Aligns variables in rows and columns so readers can compare figures accurately in seconds.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">White Space &amp; Dividers</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Margins, padding around boxes, horizontal rule lines.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Prevents visual overload and clearly marks where one topic ends and the next begins.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Navigating Complex Multi-Section Texts Using Signposts",
                "summary": "How indexes, contents boxes, Q&A layouts, and flowcharts speed up comprehension.",
                "content_html": """
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>FAQ (Question-and-Answer) Layout:</strong> Uses bold common questions as subheadings (e.g., <em>"How do I apply for paternity leave?"</em>) followed by direct answers, allowing readers with a specific query to skip straight to their exact question.</li>
                  <li><strong>Step-by-Step Flowchart / Arrows:</strong> Uses boxes connected by directional arrows (<code>Step 1 &rarr; Step 2 &rarr; Step 3</code>) to visually guide the reader through a decision tree or troubleshooting process (e.g. <em>"Is the patient breathing? Yes / No"</em>).</li>
                  <li><strong>Header &amp; Footer Bands:</strong> Stores document version numbers, security classifications (<em>"CONFIDENTIAL"</em>), and page numbers (<em>"Page 2 of 4"</em>) so staff know the document is current and complete.</li>
                </ul>
                """
            },
            {
                "title": "Comparing Layout Choices Across Two Texts (Level 2)",
                "summary": "How to contrast a dense prose article with a structured leaflet or webpage.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">When a Level 2 question asks you to compare how Text A and Text B are structured or laid out:</p>
                <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>Model Comparison Sentence:</strong> <em>"Text A uses a highly structured FAQ layout with bold question subheadings and a two-column tariff table so busy commuters can find ticket prices instantly. In contrast, Text B is laid out in continuous single-column narrative paragraphs suitable for an in-depth opinion column."</em></p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Navigating an FAQ Staff Intranet Page (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "HR Annual Leave Policy Guide",
                "question": "A staff handbook page is laid out with three bold question headings:<br><strong>Q1: How many days of annual leave do I get?</strong><br><strong>Q2: How do I carry over unused holiday into next year?</strong><br><strong>Q3: Who approves emergency compassionate leave?</strong><br>(a) Which heading should an employee read if they have 3 days of holiday left in December that they want to use in January? [1 Mark]<br>(b) Why is this Question-and-Answer layout helpful for busy staff? [1 Mark]",
                "steps": [
                    ("Step 1", "Match the employee's query to the exact heading", "Heading Q2 ('How do I carry over unused holiday into next year?') directly addresses moving unused holiday into the new year.", "1 Mark [A1 Navigation]"),
                    ("Step 2", "Explain the benefit of the Q&A layout", "It allows staff to scan the bold questions and jump straight to the exact answer they need without reading the whole policy document.", "1 Mark [A1 Layout Purpose]")
                ],
                "final_answer": "(a) Q2: How do I carry over unused holiday into next year? | (b) It lets staff quickly scan for their exact question and find the answer immediately without reading every paragraph.",
                "tutor_tip": "In navigation questions, always copy the heading label ('Q2') and its title accurately."
            },
            {
                "title": "Community Clinic Health Leaflet Layout Evaluation (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Public Health Communications",
                "question": "A vaccination guide uses a three-column leaflet layout with a separate shaded sidebar on the right edge titled: <strong>'Walk-In Clinic Opening Times &amp; Postcodes'</strong>, while the main columns explain how the flu vaccine works.<br>(a) Why did the designer place clinic opening times and postcodes in a dedicated sidebar? [1 Mark]<br>(b) Explain two ways this overall layout benefits a busy working parent needing a flu jab. [2 Marks]",
                "steps": [
                    ("Step 1", "Explain the architectural purpose of the sidebar", "The shaded sidebar physically separates practical logistical details (times and postcodes) from the scientific explanation in the main columns.", "1 Mark [A1 Sidebar Purpose]"),
                    ("Step 2", "Explain Benefit 1 for the target reader", "A busy parent can locate clinic opening hours and postcodes instantly at a glance without having to scan through paragraphs of medical background.", "1 Mark [A1 Reader Benefit 1]"),
                    ("Step 3", "Explain Benefit 2 for the target reader", "The narrow three-column format breaks the medical explanation into short, digestible sections that are quick and easy to read on the go.", "1 Mark [A1 Reader Benefit 2]")
                ],
                "final_answer": "(a) It separates practical appointment logistics (times and postcodes) from the medical explanation. | (b) 1. Enables busy parents to find clinic times and locations instantly. 2. Narrow columns break the vaccine information into short, readable chunks.",
                "tutor_tip": "Focus on the practical time-saving convenience delivered by the layout for the specific target reader."
            }
        ],
        "examiner_traps": [
            {
                "title": "Describing What the Text Says Instead of How It Is Laid Out",
                "desc": "If asked about layout, summarizing the medical facts or repeating the opening hours scores 0. You must discuss columns, sidebars, tables, spacing, and visual hierarchy.",
                "fix": "Focus exclusively on visual arrangement, structural containers, and how they speed up navigation."
            },
            {
                "title": "Forgetting to Explain WHY a Table Beats a Paragraph",
                "desc": "Simply writing 'There is a table' is an observation, not an explanation.",
                "fix": "Always explain that a table aligns matching data in rows and columns for instant comparison and error-free lookup."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A staff intranet page presents monthly payroll submission cut-off dates and payday dates in a centred two-column table rather than continuous prose. Explain <strong>two advantages</strong> of this table layout for staff.",
                "solution_steps": "1. Advantage 1: Aligns each month's submission cut-off date directly alongside its corresponding payday in clear rows [1 Mark].<br>2. Advantage 2: Enables staff to look up a specific month's deadline in seconds without misreading dates buried in a paragraph [1 Mark].",
                "correct_answer": "1. Aligns cut-off dates directly next to paydays in clear rows. | 2. Allows staff to scan and find a specific month's deadline quickly without misreading.",
                "tutor_tip": "Mention 'rows and columns' and 'rapid/error-free lookup' whenever explaining the effect of a table."
            },
            {
                "marks": "2 Marks",
                "question": "A first-aid poster for choking uses three boxes connected by large downward arrows: <strong>Box 1: Encourage Coughing &rarr; Box 2: Give 5 Back Blows &rarr; Box 3: Give 5 Abdominal Thrusts</strong>.<br>Identify this layout device and explain why it is effective in a medical emergency.",
                "solution_steps": "1. Device: Flowchart / sequential diagram with directional arrows [1 Mark].<br>2. Effectiveness: Visually guides a panicked bystander through the exact step-by-step order of life-saving actions without having to read long sentences [1 Mark].",
                "correct_answer": "Device: Flowchart / arrow sequence diagram. | Effectiveness: Visually shows the exact chronological order of first-aid actions so a bystander can act immediately in an emergency.",
                "tutor_tip": "Boxes linked by arrows are called a 'flowchart' or 'process diagram'."
            },
            {
                "marks": "2 Marks",
                "question": "A council recycling guide prints a horizontal dashed line with a pair of scissors icon (&#9986;) above a bottom slip titled <strong>'Cut Out &amp; Pin to Your Fridge: Collection Days Calendar'</strong>.<br>Explain how this layout feature helps residents follow the recycling rules.",
                "solution_steps": "1. Feature identification: Tear-off / cut-out slip separated by a dashed line [1 Mark].<br>2. Practical benefit: Allows residents to detach the calendar and display it on their kitchen fridge as a permanent visual reminder of bin collection days [1 Mark].",
                "correct_answer": "The dashed cut-out slip allows residents to detach the collection calendar and keep it visible on their fridge so they never miss bin day.",
                "tutor_tip": "Always connect layout design to how the reader physically uses the document in everyday life."
            }
        ]
    },
    # 6. Investigating Images
    {
        "filename": "reading-investigating-image.html",
        "clean_topic": "Images, Diagrams, Charts & Captions",
        "intro_lead": "Analyze how photographs, technical diagrams, infographics, warning icons, and captions reinforce written arguments, evoke emotional responses, and clarify complex procedures.",
        "next_file": "reading-language-features.html",
        "next_name": "Language Devices",
        "spec_points": [
            ("L1.14 / L2.16", "Analyse how images, diagrams, and graphical representations support or extend written content."),
            ("L2.17", "Evaluate the persuasive, emotional, and informational impact of visual imagery and captions in functional texts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-image",
                "title": "Golden Rule 1: Connect Specific Image Details to the Text's Core Message",
                "desc": "Images are never merely decorative in Functional Skills exams. Describe the specific visual detail shown in the image (e.g. a smiling apprentice in a hard hat, or a flooded high street) and explain how it proves or reinforces the writer's point.",
                "badge": "Formula: [Specific Visual Detail] + [Emotion or Fact Conveyed] + [Link to Text Purpose]"
            },
            {
                "icon": "fa-comment",
                "title": "Golden Rule 2: Always Read the Caption and Chart Labels First",
                "desc": "Captions, axis labels, and legends anchor the meaning of an image or graph. Examiners often hide a 1-mark retrieval fact inside an image caption or chart key that does not appear anywhere in the main body paragraphs!",
                "badge": "Never skip captions! They frequently contain unique exam-scoring facts."
            }
        ],
        "skills": [
            {
                "title": "Four Categories of Visual Media in Functional Skills Papers",
                "summary": "How photographs, diagrams, charts, and icons function differently.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Visual Type</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Typical Exam Context</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Primary Function &amp; Effect on Reader</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Emotive Photograph</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Charity appeals, environmental campaigns, community petitions.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Humanises statistics and triggers empathy, sympathy, or outrage by showing real people/animals affected.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Instructional Diagram</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">First-aid guides, flat-pack assembly, lifting posture manuals.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Demonstrates exact physical positioning (e.g. straight back, bent knees) far more clearly than words alone.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Bar Chart / Pie Chart</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Financial reports, climate audits, staff survey summaries.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Converts complex percentages and trends into instant visual proportions so readers spot peaks and drops immediately.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Hazard / Warning Symbols</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">COSHH chemical labels, workshop signs, road safety notices.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Communicates danger universally across language barriers at a single glance (e.g. skull and crossbones, high voltage).</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "How Captions Anchor and Extend Image Meaning",
                "summary": "Why the text directly underneath a photo is critical for comprehension.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">A photograph on its own can be ambiguous. The <strong>caption</strong> (the short text printed directly beneath or beside an image) performs three vital jobs:</p>
                <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                  <li><strong>Identifies Who, Where, and When:</strong> Names the specific person, location, and date (e.g., <em>"Apprentice electrician Maya Patel testing solar panels at Kettering Depot, May 2026"</em>).</li>
                  <li><strong>Links the Image to the Argument:</strong> Explains how the photo proves the article's claim (e.g., <em>"The new panels cut depot electricity bills by 38%"</em>).</li>
                  <li><strong>Provides Extra Retrieval Facts:</strong> In Pearson Edexcel exams, always check captions when a retrieval question asks for a date, name, or cost that you cannot find in the main paragraphs!</li>
                </ol>
                """
            },
            {
                "title": "Evaluating Whether an Image Is Effective (Level 2)",
                "summary": "How to structure a 2-mark or 3-mark evaluation of an image's suitability.",
                "content_html": """
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>Question Pattern:</strong> <em>"Explain how the image and caption support the writer's purpose in Text B. [2 Marks]"</em><br><strong>Step 1 (Visual Impact):</strong> Describe what the image shows and the feeling/impression it creates (<em>"The photograph of overflowing litter bins next to a children's swingset creates disgust and concern for child safety..."</em>).<br><strong>Step 2 (Link to Purpose):</strong> Connect it to the writer's goal (<em>"...which reinforces the writer's campaign to persuade the council to fund twice-weekly park collections."</em>).</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Interpreting a Manual Handling Diagram & Caption (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Warehouse Lifting Safety Guide",
                "question": "A safety leaflet includes a diagram showing a worker lifting a heavy box with a straight back and bent knees, accompanied by a green tick icon and the caption: <em>'Figure 1: Hold the load close to your waist (maximum solo lift: 20 kg).'</em><br>(a) According to the caption, what is the heaviest weight one worker should lift alone? [1 Mark]<br>(b) Why has the writer included this diagram alongside the written rules? [1 Mark]",
                "steps": [
                    ("Step 1", "Retrieve the exact weight limit from the caption", "The caption states 'maximum solo lift: 20 kg'.", "1 Mark [A1 Caption Retrieval]"),
                    ("Step 2", "Explain the functional purpose of the diagram", "The diagram visually shows staff the exact safe body posture (straight back, bent knees, load close to waist) so they can copy it easily and avoid back injury.", "1 Mark [A1 Diagram Purpose]")
                ],
                "final_answer": "(a) 20 kg. | (b) Visually demonstrates the correct lifting posture (bent knees, straight back) so workers can easily see and copy the safe technique.",
                "tutor_tip": "Notice how the 20 kg figure was inside the caption — always read every word around a diagram!"
            },
            {
                "title": "Air Ambulance Charity Campaign Image Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Charitable Healthcare Fundraising",
                "question": "Text A (a fundraising appeal for the County Air Ambulance) includes a photograph of a paramedic kneeling beside a red helicopter trauma pack, smiling warmly alongside a young boy who survived a road accident.<br>(a) What emotional response does this photograph evoke in potential donors? [1 Mark]<br>(b) Explain how this specific image supports the text's headline: <em>'Every Second Counts, Every Pound Saves Lives'</em>. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify the emotional response evoked", "Evokes warmth, relief, hope, gratitude, and empathy for the recovered child.", "1 Mark [A1 Emotion]"),
                    ("Step 2", "Link the helicopter/trauma pack to 'Every Second Counts'", "The emergency helicopter and trauma pack highlight the rapid, time-critical medical response ('Every Second Counts').", "1 Mark [A1 Visual Detail 1]"),
                    ("Step 3", "Link the smiling child to 'Every Pound Saves Lives'", "The smiling, healthy boy provides tangible photographic proof that public donations directly save real children's lives, persuading readers to donate.", "1 Mark [A1 Visual Detail 2]")
                ],
                "final_answer": "(a) Evokes warmth, hope, relief, and empathy. | (b) The helicopter and trauma kit illustrate the speed of emergency care ('Every Second Counts'), while the smiling recovered boy gives tangible visual proof that donations save real lives ('Every Pound Saves Lives').",
                "tutor_tip": "Always link the specific visual details in the photograph directly to the exact words in the headline or text purpose."
            }
        ],
        "examiner_traps": [
            {
                "title": "Stating the Obvious Without Analysing Significance",
                "desc": "Writing 'The picture shows a nurse so you know the text is about nurses' scores 0 at Level 2. You must explain WHY that specific depiction was chosen (e.g. to project frontline professionalism, reassurance, or urgency).",
                "fix": "Always state what the image proves, clarifies, or makes the reader feel."
            },
            {
                "title": "Saying 'It Helps People Who Cannot Read'",
                "desc": "Writing 'The picture is there for people who cannot read English' is a generic guess that examiners reject unless the text is specifically about international safety symbols.",
                "fix": "Explain how the image complements the written text for the target audience."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A marine conservation poster includes a close-up photograph of a sea turtle entangled in a discarded plastic six-pack ring, alongside the caption: <em>'Over 100,000 marine animals die from plastic entanglement every year.'</em><br>Explain why the author used this photograph and caption together rather than just printing waste statistics.",
                "solution_steps": "1. Effect of photograph: Provokes immediate shock, sympathy, and guilt by showing an innocent animal physically trapped in everyday litter [1 Mark].<br>2. Combined effect with caption: Combines emotional impact with the stark 100,000 annual death toll to prove it is a widespread crisis and persuade readers to cut plastic use [1 Mark].",
                "correct_answer": "The photo provokes shock and sympathy by showing a real turtle trapped in plastic, while the caption's 100,000 statistic proves the massive scale of the crisis to persuade readers to stop littering.",
                "tutor_tip": "Mention both the emotional impact of the photo and the factual scale added by the caption."
            },
            {
                "marks": "2 Marks",
                "question": "An engineering apprenticeship brochure features a photograph of a young female technician wearing safety goggles and operating a CNC laser cutter in a bright, modern workshop.<br>Give <strong>two reasons</strong> why the college selected this specific photograph for the brochure.",
                "solution_steps": "1. Reason 1: Challenges gender stereotypes by showing that engineering apprenticeships are welcoming and accessible to women [1 Mark].<br>2. Reason 2: Portrays the workshop as modern, high-tech, and safety-conscious (safety goggles, CNC laser), making the course look attractive and professional [1 Mark].",
                "correct_answer": "1. Encourages female applicants by showing women succeeding in engineering. | 2. Makes the course look modern, hands-on, and safe (high-tech laser cutter and safety goggles).",
                "tutor_tip": "Look closely at who is in the photo and what equipment they are using to deduce how it appeals to the target audience."
            },
            {
                "marks": "2 Marks",
                "question": "A company energy report includes a bar chart titled <strong>'Quarterly Gas Consumption (kWh)'</strong> showing a tall red bar for Winter (45,000 kWh) and a short green bar for Summer (8,000 kWh).<br>Explain how this bar chart helps managers reading the report.",
                "solution_steps": "1. Visual comparison: Allows managers to see the dramatic contrast between winter peak usage (45,000 kWh) and summer usage (8,000 kWh) instantly through bar height and colour coding [1 Mark].<br>2. Decision support: Makes seasonal energy trends clear at a glance without having to calculate figures from a paragraph [1 Mark].",
                "correct_answer": "Visually contrasts the sharp winter spike (45,000 kWh in red) against low summer usage (8,000 kWh in green) so managers can spot seasonal energy trends at a glance.",
                "tutor_tip": "Refer to the visual contrast (tall red bar vs short green bar) and the exact figures shown."
            }
        ]
    },
    # 7. Language Features
    {
        "filename": "reading-language-features.html",
        "clean_topic": "Language Devices & Rhetorical Techniques",
        "intro_lead": "Identify and analyze persuasive language devices including alliteration, rule of three, rhetorical questions, metaphors, similes, direct address, imperative verbs, emotive language, and hyperbole.",
        "next_file": "reading-point-of-view-and-line-of-argument.html",
        "next_name": "Point of View & Bias",
        "spec_points": [
            ("L1.12 / L2.13", "Identify language techniques and explain how they convey meaning and influence the reader."),
            ("L2.14 / L2.15", "Analyse rhetorical devices used to persuade, inform, critique, or advocate across multiple texts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-wand-magic-sparkles",
                "title": "Golden Rule 1: Name the Device, Quote the Example, Explain the Impact",
                "desc": "To score full marks on language questions in Pearson Edexcel, follow the 3-step formula: 1. Technique Name -> 2. Direct Quote -> 3. Specific impact on reader thoughts/feelings.",
                "badge": "Technique Name + Accurate Short Quote + Specific Reader Impact = Full Marks."
            },
            {
                "icon": "fa-bullhorn",
                "title": "Golden Rule 2: Rule of Three, Direct Address & Emotive Language Drive Persuasion",
                "desc": "The 'Rule of Three' creates rhythm and completeness; 'Direct Address' ('you') places personal responsibility on the reader; 'Emotive Language' triggers strong feelings like guilt, pride, or urgency.",
                "badge": "Look first for: Rule of Three, Rhetorical Questions, Direct Address ('you'), and Statistics."
            }
        ],
        "skills": [
            {
                "title": "Mastery Matrix: Core Language Devices and Their Real Effects",
                "summary": "The essential rhetorical devices examined in Functional Skills English.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1;">Technique</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Vocational Example</th>
                        <th style="padding:10px; border:1px solid #cbd5e1;">Specific Effect on Reader</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rhetorical Question</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Can our NHS afford another year of staffing shortfalls?"</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Forces the reader to mentally agree with the author's implied answer ('No') and highlights urgency.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rule of Three (Triad)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Compassionate, resilient, and dedicated care."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Delivers a rhythmic, memorable triplet that makes the claim sound comprehensive and convincing.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Hyperbole (Exaggeration)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We are drowning in mountains of pointless paperwork."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Dramatizes staff frustration and emphasizes the overwhelming scale of administrative burden.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Direct Address &amp; Pronouns</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"You hold the key to your team's safety."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Speaks directly to the individual reader, making them feel personally accountable.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Alliteration</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Cut carbon costs with clever carpooling."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Creates a punchy, memorable acoustic rhythm that reinforces the campaign slogan.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Logical & Authoritative Language Devices (Statistics, Expert Quotes, Case Studies)",
                "summary": "Not all language devices are emotional — learn to spot evidence-based persuasive techniques.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">In formal reports and informative articles, writers persuade using <strong>logos (logic and evidence)</strong> rather than emotion. Examiners credit all of the following as language features:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Statistics &amp; Numerical Data:</strong> (e.g., <em>"Reduced workplace slips by 64% across 12 depots"</em>) &rarr; Provides concrete, verifiable proof that builds trust and convinces sceptical readers.</li>
                  <li><strong>Expert / Authority Endorsement:</strong> (e.g., <em>"Dr. Helen Vance, Chief Clinical Toxicologist, warns that..."</em>) &rarr; Lends weight, professional credibility, and trustworthiness to the writer's claim.</li>
                  <li><strong>First-Hand Case Study / Anecdote:</strong> (e.g., <em>"When 19-year-old apprentice Liam joined our welding scheme..."</em>) &rarr; Provides relatable, real-life human proof that the programme works in practice.</li>
                </ul>
                """
            },
            {
                "title": "How to Structure a 3-Mark Language Analysis Response",
                "summary": "The sentence template that guarantees 3/3 marks on Level 2 papers.",
                "content_html": """
                <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>3-Mark Sentence Template:</strong><br><em>"The writer uses <strong>[Technique Name]</strong> in the phrase <strong>'[Exact Short Quote]'</strong>, which encourages/persuades the reader by <strong>[Specific Emotional or Logical Impact linked to the topic]</strong>."</em><br><strong>Example:</strong> <em>"The writer uses <strong>emotive language and hyperbole</strong> in the phrase <strong>'abandoned in freezing waiting rooms for eternity'</strong>, which provokes outrage and sympathy for vulnerable patients so readers sign the hospital petition."</em></p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Spotting Persuasive Language in a Cycling Campaign Flyer (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Sustainable Commuting Initiative",
                "question": "Read the extract from a staff cycling flyer:<br><em>'Pedal to work for a healthier heart, a happier mood, and a heavier wallet! Over 78% of staff who switched to our Cycle-to-Work scheme saved at least £600 on fuel last year.'</em><br>Identify <strong>two language features</strong> used in this extract and copy the example for each. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify Feature 1 and quote", "Rule of three (and alliteration of 'h' / 'w'): 'a healthier heart, a happier mood, and a heavier wallet!'", "1 Mark [A1 Feature 1]"),
                    ("Step 2", "Identify Feature 2 and quote", "Statistics / numerical facts: '78% of staff' and 'saved at least £600 on fuel'.", "1 Mark [A1 Feature 2]")
                ],
                "final_answer": "1. Rule of three (or alliteration): 'a healthier heart, a happier mood, and a heavier wallet'. | 2. Statistics: '78% of staff' / 'saved at least £600'.",
                "tutor_tip": "Statistics and percentages are one of the easiest and safest language features to spot in any exam!"
            },
            {
                "title": "Healthcare Recruitment Drive Article Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "NHS Clinical Recruitment",
                "question": "Read the extract:<br><em>'Are you ready to make an indelible mark on patients' lives? Nursing offers a career of purpose, passion, and pride. Do not let this once-in-a-lifetime calling slip through your fingers.'</em><br>(a) Identify and quote one <strong>rhetorical question</strong>. [1 Mark]<br>(b) Identify and quote one example of the <strong>rule of three</strong> (or alliteration). [1 Mark]<br>(c) Explain the persuasive effect of the metaphor <em>'slip through your fingers'</em>. [1 Mark]",
                "steps": [
                    ("Step 1", "Quote the rhetorical question exactly", "'Are you ready to make an indelible mark on patients' lives?'", "1 Mark [A1 Quote]"),
                    ("Step 2", "Quote the rule of three / alliterative triplet", "'purpose, passion, and pride'", "1 Mark [A1 Quote]"),
                    ("Step 3", "Explain the metaphorical effect", "The metaphor 'slip through your fingers' portrays the nursing career as a precious physical treasure that can be easily lost, creating urgency and fear of missing out so candidates apply immediately.", "1 Mark [A1 Effect]")
                ],
                "final_answer": "(a) 'Are you ready to make an indelible mark on patients' lives?' | (b) 'purpose, passion, and pride' | (c) Creates a sense of urgency and fear of losing a precious career opportunity, prompting readers to apply now.",
                "tutor_tip": "Copy quotations word-for-word inside quotation marks. When explaining impact, use active verbs like 'compels', 'dramatizes', or 'creates urgency'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Vague Impact Statements like 'It makes you read on'",
                "desc": "Writing 'it catches the reader's eye and makes them read on' is the #1 reason candidates lose the effect mark on language questions.",
                "fix": "Always explain the exact emotion (guilt, pride, urgency) or logical conclusion the reader experiences."
            },
            {
                "title": "Naming Punctuation or Font Styles as Language Features",
                "desc": "Writing 'bold letters' or 'bullet points' on a language question scores 0.",
                "fix": "Stick strictly to the PERSUADE mnemonic (Pronouns, Emotive words, Rhetorical questions, Statistics, Urgent imperatives, Alliteration, Metaphors/Similes, Exaggeration/Rule of three)."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A union safety flyer states: <em>'Exhausted nurses make dangerous mistakes. Safe ward staffing is a matter of life and death.'</em><br>Identify <strong>one language technique</strong> used in this extract and explain its intended effect on the reader.",
                "solution_steps": "1. Technique: Emotive language ('Exhausted', 'dangerous', 'matter of life and death') or contrast/antithesis ('life and death') [1 Mark].<br>2. Effect: Elevates ward staffing levels from a routine scheduling issue into an urgent moral crisis, alarming the reader so they support safer staffing ratios [1 Mark].",
                "correct_answer": "Technique: Emotive language / contrast ('matter of life and death'). | Effect: Emphasizes the fatal consequences of understaffing to create urgency and compel support.",
                "tutor_tip": "Connecting the emotive phrase to the life-saving gravity of the topic secures full marks."
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a local charity advert:<br><em>'For the price of your morning coffee (£3.50), you can provide a hot meal and a warm blanket for a homeless veteran tonight.'</em><br>Identify <strong>two language features</strong> used to persuade the reader to donate.",
                "solution_steps": "1. Feature 1: Direct address ('your morning coffee', 'you can provide') — speaks directly to the individual donor [1 Mark].<br>2. Feature 2: Relatable financial comparison / contrast (£3.50 coffee vs a hot meal and warm blanket) or emotive language ('homeless veteran') [1 Mark].",
                "correct_answer": "1. Direct address ('your', 'you'). | 2. Relatable cost comparison (£3.50 coffee vs hot meal and warm blanket) / emotive appeal ('homeless veteran').",
                "tutor_tip": "Comparing a small everyday luxury (£3.50 coffee) with a life-changing donation makes giving money feel effortless."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a cybersecurity training alert:<br><em>'Cyber-criminals are lurking in your inbox like digital pickpockets! Never share your two-factor passcode, or a single careless click could paralyse our entire hospital network.'</em><br>Identify <strong>two figurative or rhetorical techniques</strong> with quotes [2 Marks] and explain their effect on staff [1 Mark].",
                "solution_steps": "1. Technique 1 & Quote: Simile ('lurking in your inbox like digital pickpockets!') [1 Mark].<br>2. Technique 2 & Quote: Imperative command ('Never share...') or alliteration/hyperbole ('careless click could paralyse our entire hospital network') [1 Mark].<br>3. Effect: Makes invisible online hackers feel like an immediate physical threat and warns staff that one mistake could shut down critical patient care [1 Mark].",
                "correct_answer": "1. Simile ('like digital pickpockets'). 2. Imperative command / hyperbole ('Never share...' / 'paralyse our entire hospital network'). Effect: Makes the cyber threat feel immediate and personal so staff guard their passcodes carefully.",
                "tutor_tip": "Any comparison using 'like' or 'as' ('like digital pickpockets') is a simile!"
            }
        ]
    },
    # 8. Point of View and Line of Argument
    {
        "filename": "reading-point-of-view-and-line-of-argument.html",
        "clean_topic": "Point of View, Bias & Line of Argument",
        "intro_lead": "Critique an author's underlying perspective, trace how a line of argument builds from premise to conclusion, detect one-sided bias, and evaluate the credibility of supporting evidence.",
        "next_file": "reading-styles-of-writing-and-voice.html",
        "next_name": "Tone, Style & Voice",
        "spec_points": [
            ("L1.9 / L2.11", "Identify the writer's main point of view, attitude, and line of argument across extended texts."),
            ("L2.14", "Recognise bias and determine whether arguments are balanced or one-sided, evaluating the strength of supporting evidence.")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-balanced",
                "title": "Golden Rule 1: Trace the Line of Argument (Claim -> Evidence -> Conclusion)",
                "desc": "A line of argument is the logical chain a writer builds: 1. Opening Claim (what they believe is wrong/right), 2. Supporting Reasons & Evidence (why they believe it), and 3. Final Call to Action (what must happen next).",
                "badge": "Line of Argument = Opening Stance -> Supporting Reasons -> Final Conclusion"
            },
            {
                "icon": "fa-coins",
                "title": "Golden Rule 2: Balanced Arguments Acknowledge Counter-Arguments",
                "desc": "A balanced text considers both advantages and disadvantages before reaching a measured verdict. A biased text suppresses counter-arguments, uses loaded language, or stems from a vested financial/personal interest.",
                "badge": "Balanced = Weighs Pros & Cons | Biased = One-sided + Loaded Vocabulary + Vested Interest"
            }
        ],
        "skills": [
            {
                "title": "Checklist for Detecting Bias vs Balance in Workplace Texts",
                "summary": "Key diagnostic questions to evaluate argument objectivity in Level 2 exams.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Diagnostic Test</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Balanced / Objective Argument</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#be123c;">Biased / One-Sided Argument</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Counter-Arguments</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Explicitly acknowledges opposing views (<em>"While critics point out the £2m cost, supporters note..."</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Completely ignores any drawbacks or dismisses critics with insults (<em>"Only fools oppose this..."</em>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Word Choice (Diction)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Measured, neutral, analytical verbs and adjectives.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Emotionally loaded pejoratives or extreme superlatives (<em>"disastrous", "greedy", "miraculous"</em>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Author Identity</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Independent auditor, public regulator, or neutral journalist.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Company CEO selling a product, lobbyist, or angry individual with a personal grudge.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Tracking Discourse Markers in a Line of Argument",
                "summary": "How connectives reveal the direction of the writer's reasoning.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">When asked to trace a writer's line of argument, follow their structural signposts from paragraph to paragraph:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Building the Case (Cumulative Signposts):</strong> <em>"Firstly...", "Furthermore...", "In addition to financial savings...", "More importantly..."</em> &rarr; Adds weight to the author's primary stance.</li>
                  <li><strong>Addressing the Counter-Argument (Concession Signposts):</strong> <em>"Admittedly...", "While some residents worry that...", "Although initial training takes two days..."</em> &rarr; Shows the writer considering an objection before knocking it down.</li>
                  <li><strong>Reaching the Verdict (Causal Signposts):</strong> <em>"Consequently...", "Therefore...", "For these reasons, the board must..."</em> &rarr; Signals the writer's ultimate conclusion and recommendation.</li>
                </ul>
                """
            },
            {
                "title": "Distinguishing the Author's View from Quoted Views",
                "summary": "Avoid the classic trap of confusing a critic's quote with the writer's own opinion.",
                "content_html": """
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>Watch Out for Reported Speech!</strong> An article might write: <em>"Some landlords claim that licensing fees will force them to raise rents. However, council data proves that 91% of landlords easily absorb the £80 annual fee."</em><br>If asked for the <strong>writer's point of view</strong>, do NOT say the writer thinks fees will raise rents! That is the landlords' claim, which the writer immediately disproves after the word <strong>"However"</strong>.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Point of View and Supporting Reasons (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Local Library Consultation Letter",
                "question": "Read this extract from a resident's letter to the council:<br><em>'Closing Oakwood Library on Saturdays is a terrible mistake. Saturday is the only day working parents can bring their children to borrow books, and elderly residents rely on the Saturday computer club to pay their bills online.'</em><br>(a) What is the writer's point of view on closing the library on Saturdays? [1 Mark]<br>(b) Give <strong>two reasons</strong> the writer uses to support their argument. [1 Mark]",
                "steps": [
                    ("Step 1", "State the writer's stance clearly", "The writer is strongly against closing Oakwood Library on Saturdays (calls it 'a terrible mistake').", "1 Mark [A1 Point of View]"),
                    ("Step 2", "Extract the two supporting reasons", "1. Working parents can only bring their children to borrow books on Saturdays. 2. Elderly residents rely on the Saturday computer club to pay bills online.", "1 Mark [A1 Supporting Reasons]")
                ],
                "final_answer": "(a) Strongly opposes closing Oakwood Library on Saturdays. | (b) 1. Working parents can only take children on Saturdays. 2. Elderly residents need the Saturday computer club to pay bills.",
                "tutor_tip": "Always state clearly whether the writer is 'in favour of' (supports) or 'against' (opposes) the proposal."
            },
            {
                "title": "Private Telehealth App Editorial Bias Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Digital Healthcare Procurement",
                "question": "Read the editorial written by the CEO of 'InstantDoctor Ltd':<br><em>'Traditional GP surgeries are inefficient relics of the past. Our revolutionary InstantDoctor app guarantees video consultations in 3 minutes, solving Britain's healthcare crisis overnight.'</em><br>(a) Identify the author's point of view and main line of argument. [1 Mark]<br>(b) Give <strong>two pieces of evidence</strong> showing that this text is biased. [2 Marks]",
                "steps": [
                    ("Step 1", "State the author's point of view and argument", "The author argues that traditional GP surgeries are outdated and should be replaced by their 3-minute digital consultation app.", "1 Mark [A1 Viewpoint]"),
                    ("Step 2", "Identify Evidence 1 of bias (Loaded Language & Hyperbole)", "Uses dismissive, loaded language to insult GP surgeries ('inefficient relics of the past') and unverified hyperbole ('solving Britain's healthcare crisis overnight').", "1 Mark [A1 Language Evidence]"),
                    ("Step 3", "Identify Evidence 2 of bias (Vested Interest & One-Sidedness)", "Written by the CEO of InstantDoctor Ltd, who profits financially from app sales and omits any limitations (such as patients needing physical examinations).", "1 Mark [A1 Vested Interest]")
                ],
                "final_answer": "(a) Argues that digital telehealth apps are far superior to traditional GP clinics and should replace them. | (b) Bias evidence: 1. Dismisses GP surgeries with loaded language ('inefficient relics of the past') and exaggerated claims ('solving Britain's healthcare crisis overnight'). 2. Written by the company CEO who has a commercial motive and ignores patients needing physical check-ups.",
                "tutor_tip": "In Level 2 papers, identifying both the loaded vocabulary AND the author's commercial vested interest guarantees full marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing a Counter-Argument Quote with the Writer's Own Stance",
                "desc": "When a writer mentions an opposing view in order to argue against it ('While some claim X, the reality is Y'), candidates sometimes mistakenly report X as the writer's opinion.",
                "fix": "Look for pivot words like 'However', 'In reality', or 'Despite these claims' — the writer's true stance always follows the pivot!"
            },
            {
                "title": "Confusing Personal Passion with Objective Proof",
                "desc": "Just because an author writes with strong conviction and dramatic adjectives does not mean their line of argument is factually proven.",
                "fix": "Ask: Where is the independent third-party evidence, sample size, and balanced consideration of drawbacks?"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A trade union newsletter argues: <em>'The proposed shift roster overhaul is an unmitigated disaster designed solely to exploit loyal warehouse staff.'</em><br>Identify the author's stance and explain why the phrasing demonstrates <strong>bias</strong>.",
                "solution_steps": "1. Stance: Strongly opposed to the proposed shift roster overhaul [1 Mark].<br>2. Bias Reason: Uses extreme, emotionally loaded language ('unmitigated disaster', 'exploit') and assumes bad motives without presenting any of management's operational reasons [1 Mark].",
                "correct_answer": "Stance: Strongly opposes the new shift roster. | Bias: Uses loaded emotional words ('unmitigated disaster', 'exploit') and presents a one-sided view without management's perspective.",
                "tutor_tip": "Quote the exact loaded phrase ('unmitigated disaster') to substantiate your bias finding."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a town planning report:<br><em>'Some high-street retailers fear that pedestrianising Market Street will reduce passing car trade. However, evidence from 14 comparable UK market towns demonstrates that pedestrian zones increase footfall by 28% and reduce empty shop units by half. Therefore, the council should approve the pedestrian zone immediately.'</em><br>Trace the writer's <strong>line of argument</strong> across the three sentences. [3 Marks]",
                "solution_steps": "1. Sentence 1 (Counter-argument): Acknowledges the opposing concern from retailers that banning cars might reduce passing trade [1 Mark].<br>2. Sentence 2 (Rebuttal with Evidence): Rebuts that fear using statistical evidence from 14 UK towns showing a 28% rise in footfall and 50% fewer empty shops [1 Mark].<br>3. Sentence 3 (Conclusion): Concludes that the council should approve the pedestrianisation scheme immediately [1 Mark].",
                "correct_answer": "1. Acknowledges retailers' fear of losing car trade. 2. Counters this with data from 14 UK towns showing a 28% footfall increase. 3. Concludes that the council should approve pedestrianisation immediately.",
                "tutor_tip": "Notice the classic three-part argument structure: Counter-claim -> Statistical Rebuttal ('However...') -> Final Recommendation ('Therefore...')."
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a nutrition blog written by the founder of 'KetoShake Supplements':<br><em>'Standard breakfast cereals are toxic bowls of pure poison. Drinking two KetoShake pouches every morning is the only way to stay healthy.'</em><br>Give <strong>two reasons</strong> why a reader should treat this argument with caution.",
                "solution_steps": "1. Reason 1 (Vested commercial interest): The writer is the founder of KetoShake Supplements and is trying to sell their own product [1 Mark].<br>2. Reason 2 (Extreme hyperbole / lack of scientific proof): Uses unverified, alarmist exaggeration ('toxic bowls of pure poison', 'the only way to stay healthy') without independent nutritional evidence [1 Mark].",
                "correct_answer": "1. The author owns KetoShake Supplements and has a financial motive to boost sales. | 2. Uses extreme, unscientific exaggeration ('toxic bowls of pure poison', 'the only way').",
                "tutor_tip": "Always check the author introduction above the excerpt for commercial conflicts of interest."
            }
        ]
    },
    # 9. Styles of Writing and Voice
    {
        "filename": "reading-styles-of-writing-and-voice.html",
        "clean_topic": "Tone, Style & Writer's Voice",
        "intro_lead": "Identify nuances of tone (urgent, critical, reassuring, formal, humorous, apologetic, authoritative) and analyze how register, vocabulary, and sentence structure shape the writer's voice.",
        "next_file": "reading-text-types.html",
        "next_name": "Text Types & Purpose",
        "spec_points": [
            ("L1.15 / L2.15", "Identify the tone and style of texts and explain how register, vocabulary, and grammar communicate attitude."),
            ("L2.16", "Evaluate how the writer's voice establishes credibility, empathy, urgency, or professional detachment.")
        ],
        "golden_rules": [
            {
                "icon": "fa-sliders",
                "title": "Golden Rule 1: Tone is the Writer's Attitude & Emotion",
                "desc": "Tone is not WHAT is said, but HOW it sounds if spoken aloud: reassuring, urgent, apologetic, sarcastic, enthusiastic, cautionary, or matter-of-fact. Always use a precise adjective to name the tone.",
                "badge": "Ban vague words like 'good/bad tone'. Use: Urgent, Reassuring, Apologetic, Critical, Formal."
            },
            {
                "icon": "fa-user-tie",
                "title": "Golden Rule 2: Style & Register Reflect Relationship with the Reader",
                "desc": "Formal style uses passive voice, complex sentences, and specialist vocabulary to project authority. Conversational/informal style uses contractions, questions, and friendly idioms to build warmth and rapport.",
                "badge": "Formal Voice = Authoritative & Detached | Conversational Voice = Friendly & Approachable"
            }
        ],
        "skills": [
            {
                "title": "The Tone Vocabulary Matrix for Exam Candidates",
                "summary": "Precise adjectives to describe tone accurately in Level 1 & Level 2 Reading answers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Precise Tone Label</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Linguistic Clues in the Text</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Typical Workplace Context</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Authoritative / Direct</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Imperative verbs (<em>"Ensure", "Do not"</em>), modal verbs (<em>"must"</em>), statutory citations.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Health &amp; safety notices, standard operating procedures, legal memos.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Reassuring / Empathetic</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Supportive adjectives (<em>"gentle", "confidential"</em>), calming assurances (<em>"don't worry, our team is here"</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Patient information leaflets, mental health helplines, induction guides.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Apologetic / Conciliatory</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Expressions of regret (<em>"sincerely apologise", "deeply regret"</em>), offers of compensation.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Customer complaint responses, service disruption updates.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Outraged / Critical</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Negative emotive words (<em>"shambolic", "unacceptable"</em>), exclamation marks, rhetorical questions.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Letters of complaint, critical newspaper editorials, union petitions.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Enthusiastic / Promotional</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Positive superlatives (<em>"thrilled", "unbeatable", "fantastic"</em>), inviting commands.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Tourism brochures, job recruitment adverts, product launches.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Active Voice vs Passive Voice (How Grammar Shapes Style)",
                "summary": "Understand why formal reports use the passive voice while campaigns use the active voice.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Sentence grammar directly controls how personal or detached a writer's voice sounds:</p>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                    <h4 style="color:#0369a1; margin-top:0; margin-bottom:8px;">Active Voice (Direct &amp; Dynamic)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;">The subject performs the action:<br><em>"Our maintenance team repaired the boiler in two hours."</em><br><strong>Effect:</strong> Sounds energetic, accountable, and direct.</p>
                  </div>
                  <div style="background:#f8fafc; border-left:4px solid #64748b; padding:16px; border-radius:6px;">
                    <h4 style="color:#334155; margin-top:0; margin-bottom:8px;">Passive Voice (Formal &amp; Detached)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;">The action is done to the subject:<br><em>"The boiler was repaired within two hours."</em><br><strong>Effect:</strong> Sounds objective, clinical, and impersonal (common in scientific and audit reports).</p>
                  </div>
                </div>
                """
            },
            {
                "title": "How Sentence Length Controls Pace and Urgency",
                "summary": "Why writers switch between short punchy sentences and complex multi-clause sentences.",
                "content_html": """
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Short Simple / Minor Sentences:</strong> (e.g., <em>"Act now. Every minute matters. Check your smoke alarm tonight."</em>) &rarr; Creates a rapid, urgent, punchy pace that demands immediate reader attention.</li>
                  <li><strong>Long Complex Sentences:</strong> (e.g., <em>"Following a comprehensive six-month consultation with ward matrons, estates engineers, and patient representatives, the Trust has approved a phased refurbishment."</em>) &rarr; Creates a measured, formal, deliberate pace that conveys thoroughness and authority.</li>
                </ul>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Tone and Style in a Patient Leaflet (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "NHS First Blood Donation Guide",
                "question": "Read this extract from a leaflet for first-time blood donors:<br><em>'Feeling a little nervous about your first donation? That is completely normal! Our warm, friendly nurses will chat with you every step of the way, and the needle pinch lasts less than a second.'</em><br>(a) Describe the <strong>tone</strong> of this extract. [1 Mark]<br>(b) Quote <strong>one phrase</strong> that helps create this tone. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify the writer's attitude toward nervous donors", "The tone is reassuring, comforting, friendly, and supportive.", "1 Mark [A1 Tone Label]"),
                    ("Step 2", "Quote a specific reassuring phrase", "'That is completely normal!' or 'Our warm, friendly nurses will chat with you every step of the way'.", "1 Mark [A1 Supporting Quote]")
                ],
                "final_answer": "(a) Tone: Reassuring, friendly, and comforting. | (b) Quote: 'That is completely normal!' (or 'Our warm, friendly nurses will chat with you every step of the way').",
                "tutor_tip": "'Reassuring' is one of the highest-scoring tone words whenever a healthcare or customer leaflet calms a reader's worries."
            },
            {
                "title": "Hospital Complaint Response Letter Tone Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Patient Relations",
                "question": "Read the opening paragraph of a letter from the Hospital Director:<br><em>'We have thoroughly investigated your grievance regarding your mother's care on Ward 2. We sincerely regret the unacceptable distress caused by the communication delay, and we have instituted immediate corrective safeguards.'</em><br>(a) Describe the tone and style of this extract. [1 Mark]<br>(b) Quote <strong>two words or phrases</strong> that establish this tone. [1 Mark]<br>(c) Explain why this tone and style are appropriate for the audience and situation. [1 Mark]",
                "steps": [
                    ("Step 1", "Describe the tone and style accurately", "The tone is formal, apologetic, empathetic, and accountable.", "1 Mark [A1 Tone]"),
                    ("Step 2", "Quote two supporting words/phrases", "Quote 1: 'sincerely regret' | Quote 2: 'unacceptable distress' (or 'immediate corrective safeguards').", "1 Mark [A1 Quotes]"),
                    ("Step 3", "Explain contextual appropriateness", "It validates the family's upset with genuine empathy while using formal, professional language to reassure them that the hospital takes the error seriously and has fixed the system.", "1 Mark [A1 Appropriateness]")
                ],
                "final_answer": "(a) Formal, apologetic, and empathetic. | (b) 'sincerely regret' and 'unacceptable distress'. | (c) Acknowledges the family's upset respectfully while reassuring them that professional corrective action has been taken.",
                "tutor_tip": "Avoid generic words like 'good' or 'nice'. Pair precise tone descriptors like 'apologetic' and 'formal' with exact quotations."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Tone with the Overall Subject Matter",
                "desc": "A text about a serious road accident might be written in a detached, factual, clinical tone (e.g. a police log) rather than an emotional one.",
                "fix": "Focus on HOW the writer expresses the information (their word choice and attitude), not the raw topic itself."
            },
            {
                "title": "Using Vague Words Like 'Positive Tone' or 'Negative Tone'",
                "desc": "At Level 2, writing 'the tone is negative' is too broad to secure full marks.",
                "fix": "Specify what KIND of positive or negative tone it is: 'enthusiastic and welcoming' vs 'critical, frustrated, and urgent'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A dental hygiene flyer asks: <em>'Hate flossing? We get it — it feels like a total chore at bedtime! But just two minutes a night will keep your gums healthy and save you painful bills.'</em><br>Describe the <strong>style/tone</strong> of this extract and quote <strong>one colloquial (informal) phrase</strong>.",
                "solution_steps": "1. Style/Tone: Informal, conversational, friendly, and relatable [1 Mark].<br>2. Colloquial Quote: 'We get it' or 'feels like a total chore' [1 Mark].",
                "correct_answer": "Tone: Conversational, friendly, and informal. | Quote: 'We get it' (or 'feels like a total chore').",
                "tutor_tip": "Both parts (an accurate tone adjective and an exact quoted informal phrase) are required for 2 marks."
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a laboratory safety protocol:<br><em>'Protective eye shields must be worn at all times. Unauthorised personnel are strictly prohibited from entering the centrifuge room.'</em><br>Describe the <strong>tone and style</strong> of this extract and identify <strong>one grammatical feature</strong> that creates it.",
                "solution_steps": "1. Tone/Style: Formal, authoritative, strict, and impersonal [1 Mark].<br>2. Grammatical feature: Passive voice ('must be worn', 'are strictly prohibited') or strong modal/adverbial emphasis ('must', 'strictly prohibited') [1 Mark].",
                "correct_answer": "Tone/Style: Formal, strict, and authoritative. | Feature: Passive voice ('must be worn') and strong modal/adverbial phrasing ('strictly prohibited').",
                "tutor_tip": "Notice how passive voice ('must be worn') makes the rule sound like an objective, unbreakable law."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a commuter's letter to a train company:<br><em>'Paying £4,200 a year to stand wedged like sardines in an unheated carriage while your company boasts about \"record punctuality\" is an absolute insult to hardworking passengers!'</em><br>Identify the writer's <strong>tone</strong> [1 Mark] and explain how <strong>two language or punctuation choices</strong> convey this tone [2 Marks].",
                "solution_steps": "1. Tone: Outraged, angry, bitter, or sarcastic [1 Mark].<br>2. Choice 1: The simile 'wedged like sardines' and emotive noun 'absolute insult' highlight physical discomfort and disrespect [1 Mark].<br>3. Choice 2: Scare quotes around '\"record punctuality\"' and the final exclamation mark (!) convey bitter sarcasm and anger [1 Mark].",
                "correct_answer": "Tone: Outraged, bitter, and sarcastic. | Choices: 1. Simile ('wedged like sardines') and emotive phrase ('absolute insult') emphasise mistreatment. 2. Inverted commas around '\"record punctuality\"' and the exclamation mark show sarcasm and anger.",
                "tutor_tip": "Quotation marks used around a phrase like '\"record punctuality\"' to mock a claim are a classic sign of a sarcastic/ironic tone!"
            }
        ]
    },
    # 10. Text Types
    {
        "filename": "reading-text-types.html",
        "clean_topic": "Text Types, Genre Conventions & Audience",
        "intro_lead": "Identify distinctive functional text genres (articles, formal reports, emails, leaflets, blogs, discussion forums, instructional manuals, and formal letters) and map their structural conventions to purpose and audience.",
        "next_file": "reading-comparing-texts.html",
        "next_name": "Comparing Texts",
        "spec_points": [
            ("L1.16 / L2.17", "Identify different text types, purposes, and audiences across informational, instructional, and transactional materials."),
            ("L2.16", "Recognise structural and formatting conventions distinguishing reports, articles, forums, manuals, and formal correspondence.")
        ],
        "golden_rules": [
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 1: Identify Genre from Structural Conventions + Purpose",
                "desc": "Every text type has a visual fingerprint: Letters have addresses, date, and 'Dear.../Yours...'; Reports have numbered sections (1.0 Introduction, 2.0 Findings, 3.0 Recommendations); Forums have usernames, timestamps, and 'Reply' buttons.",
                "badge": "Visual Conventions (Format) + Communicative Goal (Purpose) = Text Type"
            },
            {
                "icon": "fa-envelope-open-text",
                "title": "Golden Rule 2: Always Define Target Audience Specifically",
                "desc": "Never write 'anyone' or 'the general public' for an audience question if the text is aimed at a specific group (e.g. 'parents of primary school children', 'HGV drivers at the depot', or 'first-time homebuyers').",
                "badge": "Be specific: Who needs this exact information, and what role or interest do they have?"
            }
        ],
        "skills": [
            {
                "title": "The Complete Functional Skills Text Type Fingerprint Table",
                "summary": "How to recognize and describe every document genre tested in Level 1 and Level 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Text Genre</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Structural Conventions</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Primary Purpose &amp; Register</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Formal Business Letter</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Sender/recipient addresses, date, Reference line, <em>Dear... / Yours sincerely/faithfully</em>.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Transactional: to complain, apply, request, or notify officially in a formal register.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Formal Report</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Title, <em>To/From/Date</em>, numbered subheadings (<em>Findings, Conclusion, Recommendations</em>), data tables.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To investigate an issue objectively, present audit facts, and propose action points.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Magazine / Newspaper Article</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Catchy headline, strapline, author byline, columns, pull quotes, captioned photo.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To engage, inform, persuade, or debate a topical issue with a lively voice.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Information Leaflet / Guide</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Q&amp;A subheadings, bullet points, shaded advice boxes, helpline contact details.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To inform, advise, and guide readers clearly on health, community, or workplace services.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Online Discussion Forum</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Thread title, multiple user handles/avatars, timestamps, <em>Like / Reply</em> buttons.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To share multiple contrasting personal opinions, tips, and lived experiences informally.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Instruction Manual / SOP</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Equipment list, warning symbols, numbered sequential steps starting with imperative verbs.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To instruct the reader step-by-step on how to perform a procedure safely and accurately.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Distinguishing Dual-Purpose Texts (Level 2)",
                "summary": "Why many real-world texts combine two purposes at once (e.g. to inform AND persuade).",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">At Level 1, a text usually has one clear purpose. At Level 2, examiners regularly select texts with a <strong>dual purpose</strong>:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>To Inform AND Persuade:</strong> A council leaflet that gives factual dates and maps for a new park-and-ride bus service (<em>informing</em>) while urging commuters to ditch their cars to cut town pollution (<em>persuading</em>).</li>
                  <li><strong>To Review/Evaluate AND Advise:</strong> A workplace software review that evaluates the pros and cons of two payroll systems (<em>evaluating</em>) and recommends which one small businesses should buy (<em>advising</em>).</li>
                </ul>
                """
            },
            {
                "title": "Pinpointing the Exact Target Audience from Text Clues",
                "summary": "How to deduce who a text was written for using pronouns, jargon, and topic focus.",
                "content_html": """
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>3 Clues That Reveal Target Audience:</strong><br>1. <strong>Direct Address Context:</strong> <em>"If your child is starting Year 7 this September..."</em> &rarr; Target Audience: Parents/guardians of Year 6 children moving up to secondary school.<br>2. <strong>Level of Jargon:</strong> Unexplained clinical terms (<em>"administer 5mg IV bolus"</em>) &rarr; Qualified medical staff, NOT patients.<br>3. <strong>Publication Source:</strong> Printed in <em>'Logistics Manager Monthly'</em> &rarr; Fleet managers and warehouse directors.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Text Type and Purpose of a Safety SOP (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Hospital Clinical Waste Protocol",
                "question": "Read this extract from a workplace wall chart:<br><strong>SAFE DISPOSAL OF SHARPS (NEEDLES &amp; SYRINGES)</strong><br><em>1. Never re-sheath a used needle by hand.<br>2. Place the needle and syringe immediately into the yellow UN-approved sharps bin.<br>3. Lock the bin lid permanently once contents reach the black fill line.</em><br>(a) Identify the <strong>type of text</strong>. [1 Mark]<br>(b) State its <strong>main purpose</strong>. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify the genre from numbered imperative steps", "Instructional notice / Standard Operating Procedure (SOP) / safety instruction guide.", "1 Mark [A1 Text Type]"),
                    ("Step 2", "State the primary purpose using an action verb", "To instruct healthcare staff step-by-step on how to dispose of used needles and syringes safely without injury.", "1 Mark [A1 Purpose]")
                ],
                "final_answer": "(a) Safety instruction notice / Standard Operating Procedure (SOP). | (b) To instruct healthcare staff on the safe step-by-step disposal of sharp medical instruments.",
                "tutor_tip": "Always include the topic ('how to dispose of used needles safely') when stating the purpose — never just write 'to instruct'!"
            },
            {
                "title": "Care Quality Commission Inspection Summary Evaluation (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Health and Social Care Regulatory Reporting",
                "question": "You are presented with a document headed: <em>'CQC Provider Audit: Cedar Grove Residential Home — Ref 884-B'</em> featuring numbered subheadings (<em>1.0 Inspection Summary, 2.0 Medication Safety Findings, 3.0 Mandatory Compliance Actions</em>) and rating tables.<br>(a) Identify the <strong>text type</strong> and give one structural feature that confirms it. [1 Mark]<br>(b) State the <strong>primary purpose</strong> of this document. [1 Mark]<br>(c) Identify two specific groups who form the <strong>target audience</strong>. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify text type and structural convention", "Formal inspection/audit report, confirmed by numbered section headings ('1.0 Inspection Summary', '3.0 Mandatory Compliance Actions') and reference code.", "1 Mark [A1 Text Type & Feature]"),
                    ("Step 2", "Determine the primary purpose", "To evaluate and report on the care home's regulatory compliance standards and set out mandatory improvements.", "1 Mark [A1 Purpose]"),
                    ("Step 3", "Identify specific target audience groups", "Care home management/directors, social care regulators, and families of current or prospective residents.", "1 Mark [A1 Audience]")
                ],
                "final_answer": "(a) Formal audit/inspection report (uses numbered section subheadings and compliance tables). | (b) To evaluate care standards at Cedar Grove Residential Home and mandate safety improvements. | (c) Care home managers/owners and families of residents.",
                "tutor_tip": "Audience answers must be specific. Rather than writing 'people', state 'care home managers and residents' families'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing a Single Word Like 'To Inform' Without Topic Context",
                "desc": "In Pearson Edexcel Level 2 exams, writing 'To inform' or 'To persuade' on its own scores 0 marks! The mark scheme requires you to state WHAT the text is informing or persuading the reader about.",
                "fix": "Always use the full formula: 'To [inform/persuade/instruct] the reader about [specific topic of the text].'"
            },
            {
                "title": "Confusing an Online Forum with an Article or Email",
                "desc": "If a text shows 3 or 4 different usernames (e.g. '@Dave_Builds', '@Sarah_N') posting separate replies under a question thread, it is an online discussion forum, not a single-author article.",
                "fix": "Check for multiple user handles, avatars, and 'Reply' timestamps."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A webpage displays a thread titled <em>'Best waterproof work boots for winter site work?'</em> followed by posts from <strong>@BricklayerDan (Posted 10 mins ago)</strong> and <strong>@SparkyJen (Posted 4 mins ago)</strong>.<br>Identify the <strong>text type</strong> and explain why someone would read it.",
                "solution_steps": "1. Text type: Online discussion forum / message board thread [1 Mark].<br>2. Reason for reading: To read real-world recommendations, personal opinions, and reviews from fellow tradespeople about durable winter work boots [1 Mark].",
                "correct_answer": "Text type: Online discussion forum thread. | Purpose for reader: To gather firsthand tips and reviews from other tradespeople on the best waterproof work boots.",
                "tutor_tip": "Multiple user handles ('@BricklayerDan', '@SparkyJen') and timestamps ('Posted 4 mins ago') always signal an online forum."
            },
            {
                "marks": "2 Marks",
                "question": "Read the header of this workplace document:<br><strong>MEMORANDUM | To: All Outpatient Receptionists | From: Practice Manager | Date: 12 October | Subject: Updated NHS Prescription Exemption Checks</strong><br>Identify the <strong>target audience</strong> and the <strong>main purpose</strong> of this document.",
                "solution_steps": "1. Target audience: Outpatient receptionists at the medical practice [1 Mark].<br>2. Main purpose: To inform and instruct reception staff on the updated procedures for checking patient NHS prescription exemptions [1 Mark].",
                "correct_answer": "Target Audience: Outpatient receptionists. | Main Purpose: To inform/instruct staff on the updated procedure for checking NHS prescription exemptions.",
                "tutor_tip": "In memos and emails, the 'To:' line gives you the exact target audience and the 'Subject:' line gives you the exact topic!"
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a leaflet distributed in university halls:<br><em>'Struggling to stretch your student loan till December? Download the FreeBudget App today! You'll get instant spending alerts, plus 20% student discounts at 50 local takeaways and supermarkets.'</em><br>State the <strong>specific target audience</strong> [1 Mark] and explain how the text has a <strong>dual purpose</strong> [2 Marks].",
                "solution_steps": "1. Target audience: University students living in halls / managing a student loan [1 Mark].<br>2. Purpose 1 (Inform): Informs students about the features of the FreeBudget App (spending alerts and 20% local discounts) [1 Mark].<br>3. Purpose 2 (Persuade): Persuades/urges them to download and use the app ('Download the FreeBudget App today!') [1 Mark].",
                "correct_answer": "Target Audience: University students managing a student loan. | Dual Purpose: 1. To inform students about the app's budgeting alerts and 20% discounts. 2. To persuade them to download the FreeBudget App immediately.",
                "tutor_tip": "Naming both 'to inform about...' and 'to persuade to...' secures full marks on Level 2 purpose questions."
            }
        ]
    },
    # 11. Comparing Texts
    {
        "filename": "reading-comparing-texts.html",
        "clean_topic": "Comparing Texts & Contrasting Perspectives",
        "intro_lead": "Synthesize information across two or three distinct texts (Text A, Text B, Text C), extract complementary facts, analyze conflicting viewpoints, and construct high-scoring comparative responses.",
        "next_file": "reading-why-do-writers-write.html",
        "next_name": "The Writer's Purpose",
        "spec_points": [
            ("L1.10 / L2.12", "Compare information, ideas, and perspectives across multiple extended texts on the same topic."),
            ("L2.15 / L2.18", "Synthesize evidence from multiple sources, comparing how writers use language and tone to convey agreement or disagreement.")
        ],
        "golden_rules": [
            {
                "icon": "fa-code-compare",
                "title": "Golden Rule 1: Use Comparative Connectives to Link Texts Directly",
                "desc": "Never write about Text A in one isolated paragraph and Text B in another. Weave them together in the same sentence using comparative discourse markers: 'Similarly', 'Both texts agree that', 'Whereas', 'In sharp contrast', 'On the other hand'.",
                "badge": "Point-by-point integration: [Text A states X + Quote], [whereas Text B argues Y + Quote]."
            },
            {
                "icon": "fa-puzzle-piece",
                "title": "Golden Rule 2: Compare Ideas, Attitudes & Language Methods",
                "desc": "High-scoring Level 2 comparative answers contrast not only factual claims, but also the authors' underlying attitudes (optimistic vs sceptical) and how they use language (statistics vs emotive hyperbole).",
                "badge": "Contrast: 1. Factual Claims + Quotes | 2. Writer's Attitude/Tone | 3. Language Devices"
            }
        ],
        "skills": [
            {
                "title": "Comparative Synthesis Structure for Level 2 Reading",
                "summary": "How to secure full marks on 3-mark to 6-mark comparison questions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>Identify the Shared Theme:</strong> Confirm the exact sub-topic both writers are discussing (e.g. cost of electric vans, impact of working from home on productivity).</li>
                    <li><strong>Spot Similarities (Points of Agreement):</strong> Use <em>"Both Text A and Text B agree that..."</em> or <em>"Similarly, Text B also notes..."</em> supported by a short quote from each text.</li>
                    <li><strong>Spot Differences (Points of Disagreement):</strong> Use <em>"Whereas Text A claims..., Text B argues..."</em> supported by a short quote from each text.</li>
                    <li><strong>Compare Tone &amp; Language (Level 2 Bonus):</strong> Contrast how each writer expresses their view (e.g., <em>"Text A uses formal statistics ('40% reduction'), whereas Text B uses emotive language ('catastrophic mistake')."</em>).</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Side-by-Side Comparison: Band 1 (Capped) vs Band 3 (Full Marks)",
                "summary": "See why isolated summaries lose marks and integrated comparisons win full marks.",
                "content_html": """
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#fef2f2; border-left:4px solid #ef4444; padding:16px; border-radius:6px;">
                    <h4 style="color:#b91c1c; margin-top:0; margin-bottom:8px;">Band 1: Isolated Summaries (1/4 Marks)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;"><em>"Text A is about electric ambulances and says they cut emissions by 40%. Text B is an interview with a paramedic who talks about rural charging stations."</em><br><strong>Why it fails:</strong> No comparative connectives, no direct contrast of viewpoints, and no language comparison.</p>
                  </div>
                  <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                    <h4 style="color:#166534; margin-top:0; margin-bottom:8px;">Band 3: Integrated Synthesis (4/4 Marks)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;"><em>"<strong>Whereas</strong> Text A takes an enthusiastic view of electric ambulances, using statistics to show they <strong>'slash emissions by 40%'</strong>, Text B takes a cautious, critical view, warning in an urgent tone that lacking rural chargers leaves crews <strong>'vulnerable during surges'</strong>."</em></p>
                  </div>
                </div>
                """
            },
            {
                "title": "Cross-Referencing Three Texts (Synthesising Evidence)",
                "summary": "How to handle questions that ask you to gather evidence across Text A, Text B, and Text C.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">Some questions ask: <em>"Using information from Text A, Text B, and Text C, give three reasons why..."</em></p>
                <p style="color:#334155; line-height:1.7; margin:0;"><strong>Crucial Rule:</strong> You MUST take at least <strong>one piece of evidence from each of the named texts</strong> and label them clearly (e.g., <em>"From Text A: ... | From Text B: ... | From Text C: ..."</em>). If you take all three points from Text A and ignore Text B and C, you can only score 1 mark out of 3!</p>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Comparing Two Staff Reviews of a New Cashless Till System (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Retail Store Technology Feedback",
                "question": "Read the two staff comments:<br><strong>Text A (Supervisor):</strong> <em>'The new card-only self-service tills have cut lunchtime queue times in half and eliminated end-of-day cash counting errors.'</em><br><strong>Text B (Cashier):</strong> <em>'Although queues move faster at lunchtime, elderly customers who budget with cash feel excluded and frustrated by the card-only rule.'</em><br>(a) Identify <strong>one similarity</strong> between Text A and Text B. [1 Mark]<br>(b) Identify <strong>one difference</strong> between their views. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify shared agreement", "Both Text A and Text B agree that the new tills have made lunchtime queues faster.", "1 Mark [A1 Similarity]"),
                    ("Step 2", "Contrast their overall attitude toward going cashless", "Text A views the card-only tills purely positively (eliminating cash counting errors), whereas Text B points out that elderly customers who rely on cash feel excluded and frustrated.", "1 Mark [A1 Difference]")
                ],
                "final_answer": "(a) Similarity: Both agree that lunchtime queues move faster. | (b) Difference: Text A praises the card-only rule for stopping cash errors, whereas Text B criticises it for excluding elderly customers who pay with cash.",
                "tutor_tip": "Look for concession clauses starting with 'Although' — writers often agree with the other text in that opening clause before stating their disagreement!"
            },
            {
                "title": "Electric Ambulances Fleet Transition (Text A vs Text B — Level 2)",
                "marks": "4 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Emergency Services Fleet Modernization",
                "question": "Read the two extracts:<br><strong>Text A (Government Press Release):</strong> <em>'Our green fleet revolution will slash urban ambulance emissions by 40% and save £1.8m in diesel costs, with rapid hubs charging batteries in just 20 minutes.'</em><br><strong>Text B (Paramedic Union Interview):</strong> <em>'While everyone wants cleaner air, rushing into electric ambulances is a reckless gamble. Rapid chargers are nonexistent in rural hills — what happens when a battery dies mid-emergency?'</em><br>Compare how the two writers convey their perspectives on electric ambulances. [4 Marks]",
                "steps": [
                    ("Step 1", "Contrast overall stance and priorities with quotes", "Both texts acknowledge the benefit of cleaner air; however, Text A enthusiastically supports electric ambulances to 'slash urban ambulance emissions by 40%', whereas Text B opposes a rushed rollout, calling it a 'reckless gamble' that threatens patient safety.", "2 Marks [A1 Viewpoint & Quote Contrast]"),
                    ("Step 2", "Contrast views on charging reliability and language used", "Text A uses confident statistics ('save £1.8m', 'charging batteries in just 20 minutes') in a promotional tone. In contrast, Text B highlights rural infrastructure gaps ('nonexistent in rural hills') and uses emotive language and a rhetorical question ('what happens when a battery dies mid-emergency?') to provoke alarm.", "2 Marks [A1 Language & Tone Contrast]")
                ],
                "final_answer": "While both writers support reducing emissions, Text A takes an optimistic, promotional view backed by statistics ('slash urban ambulance emissions by 40%', 'charging batteries in just 20 minutes'). Conversely, Text B adopts an urgent, critical stance, warning that rural chargers are 'nonexistent' and using emotive phrasing ('reckless gamble') and a rhetorical question ('what happens when a battery dies mid-emergency?') to highlight patient risk.",
                "tutor_tip": "Notice the use of 'while', 'however', and 'conversely' alongside direct quotations from both texts. This structure guarantees 4/4 marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Two Separate Summaries with No Comparison",
                "desc": "Summarizing Text A in one block and Text B in a separate block without linking connectives caps your score heavily.",
                "fix": "Use comparative linking words ('whereas', 'in contrast', 'similarly') in every single point of your response."
            },
            {
                "title": "Forgetting to Quote from BOTH Texts",
                "desc": "If a Level 2 question asks you to compare how two texts convey their views and you only include quotations from Text A, you cannot achieve top-band marks.",
                "fix": "Pair every Text A quotation with a matching Text B quotation in the same sentence."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Read the two extracts on remote GP appointments:<br><strong>Text A (Health App Brochure):</strong> <em>'Video consultations empower busy workers by eliminating travel time and cutting waiting room infection risks by 50%.'</em><br><strong>Text B (Age Charity Report):</strong> <em>'Replacing face-to-face appointments with smartphone apps alienates elderly patients who lack digital skills or fast broadband.'</em><br>Compare the viewpoints and language of Text A and Text B. [3 Marks]",
                "solution_steps": "1. Viewpoint contrast: Text A views video consultations positively as convenient and safe for busy workers ('eliminating travel time'), whereas Text B views them negatively as excluding older people ('alienates elderly patients') [2 Marks].<br>2. Language contrast: Text A uses positive verbs ('empower') and a statistic ('50%'), whereas Text B uses emotive vocabulary ('alienates') to highlight digital exclusion [1 Mark].",
                "correct_answer": "Text A presents video appointments positively as convenient and hygienic, using the verb 'empower' and a '50%' statistic. In contrast, Text B criticises them for excluding older people without broadband, using the emotive verb 'alienates'.",
                "tutor_tip": "Directly balance the two viewpoints and quote key words ('empower' vs 'alienates') in a single coherent answer."
            },
            {
                "marks": "3 Marks",
                "question": "Read the two extracts on a proposed four-day working week (32 hours for 100% pay):<br><strong>Text A (HR Trial Summary):</strong> <em>'During our six-month four-day week trial, staff sick leave dropped by 62% and overall company revenue rose by 8%.'</em><br><strong>Text B (Retail Franchise Owner):</strong> <em>'Four-day weeks may work for desk jobs, but small shops open seven days a week would be forced to hire extra part-time staff and go bankrupt!'</em><br>Compare how the two writers present the four-day working week.",
                "solution_steps": "1. Stance comparison: Text A supports the four-day week as a proven success for wellbeing and profits, whereas Text B opposes it as financially impossible for small seven-day retail shops [2 Marks].<br>2. Evidence/Tone comparison: Text A relies on measured trial statistics ('sick leave dropped by 62%', 'revenue rose by 8%'), whereas Text B uses dramatic, emotive hyperbole ('go bankrupt!') [1 Mark].",
                "correct_answer": "Text A supports the four-day week using positive trial statistics ('sick leave dropped by 62%', 'revenue rose by 8%'). Conversely, Text B argues it only suits desk jobs and uses emotive exaggeration ('go bankrupt!') to warn that small shops cannot afford extra staffing costs.",
                "tutor_tip": "Contrast the statistical evidence in Text A against the emotional warning in Text B."
            },
            {
                "marks": "3 Marks",
                "question": "Using information from all three extracts below, give <strong>three reasons</strong> why employees are leaving city-centre offices:<br><strong>Text A:</strong> <em>'Annual rail season tickets rose by 6.5% in March, costing commuters over £3,800.'</em><br><strong>Text B:</strong> <em>'Parents save 90 minutes a day on school-run travel when working from home.'</em><br><strong>Text C:</strong> <em>'City-centre air quality breached safe nitrogen dioxide limits on 42 days last year.'</em>",
                "solution_steps": "1. From Text A: High commuting costs (rail season tickets rose by 6.5% to over £3,800) [1 Mark].<br>2. From Text B: Better work-life balance / saving 90 minutes a day on school-run travel by working from home [1 Mark].<br>3. From Text C: Poor city-centre air quality / pollution (breached safe nitrogen dioxide limits on 42 days) [1 Mark].",
                "correct_answer": "1. (Text A) Expensive rail fares (£3,800 / up 6.5%). | 2. (Text B) Saving 90 minutes daily on school-run travel. | 3. (Text C) High city-centre air pollution (breached safe limits 42 times).",
                "tutor_tip": "When a question names three texts, make sure you extract one distinct point from each text!"
            }
        ]
    },
    # 12. Why Do Writers Write (Writer's Purpose)
    {
        "filename": "reading-why-do-writers-write.html",
        "clean_topic": "The Writer's Purpose & Target Audience",
        "intro_lead": "Identify why writers produce texts (to persuade, inform, explain, instruct, advise, review, or entertain), recognize sub-purposes, and analyze how authors tailor tone and content to their target audience.",
        "next_file": "reading-the-exam.html",
        "next_name": "Reading Exam Strategy",
        "spec_points": [
            ("L1.16 / L2.17", "Identify the writer's main purpose and sub-purposes and determine why texts were produced."),
            ("L2.18", "Analyse how purpose and target audience shape vocabulary choice, tone, layout, and calls to action.")
        ],
        "golden_rules": [
            {
                "icon": "fa-user-check",
                "title": "Golden Rule 1: Always Pair the Purpose Verb with the Specific Topic",
                "desc": "Never write 'To inform' or 'To persuade' on its own! Pearson Edexcel mark schemes require the full formula: 'To [Purpose Verb] the reader about [Specific Topic and Action]'.",
                "badge": "Formula: To [persuade / inform / instruct / advise] [audience] about [specific topic]."
            },
            {
                "icon": "fa-people-group",
                "title": "Golden Rule 2: Look at the Final Sentence (Call to Action) to Confirm Purpose",
                "desc": "A text may spend three paragraphs giving factual statistics, but if the final sentence says 'Sign our petition before Friday' or 'Book your free eye test today', its overarching main purpose is to persuade/promote!",
                "badge": "Informative body + Urgent Call to Action at the end = Persuasive / Promotional Purpose"
            }
        ],
        "skills": [
            {
                "title": "The Six Core Writer's Purposes in Functional Skills",
                "summary": "How to distinguish between Inform, Persuade, Instruct, Advise, Explain, and Review.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Purpose Verb</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Key Linguistic Clues</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Full-Mark Exam Answer Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">To Persuade / Campaign</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Rhetorical questions, emotive language, rule of three, call to action (<em>"Donate now!"</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To persuade local residents to sign the petition against closing the town post office."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">To Inform</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Neutral tone, dates, times, prices, facts without trying to sell an opinion.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To inform hospital staff about the new car park barrier operating hours and permit fees."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">To Instruct</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Numbered steps (1, 2, 3), imperative command verbs (<em>"Switch off", "Attach"</em>), warnings.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To instruct laboratory technicians on how to calibrate the centrifuge safely."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">To Advise / Guide</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Modal verbs (<em>"you should", "try to", "it is a good idea to"</em>), supportive tone.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To advise first-year apprentices on how to manage exam stress and sleep well."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">To Review / Evaluate</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Weighs pros and cons, star ratings, evaluative adjectives, final verdict.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To review the strengths and weaknesses of the EcoWash dishwasher for family kitchens."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Distinguishing Instruct vs Advise (High-Frequency Distinction)",
                "summary": "Learn the simple modal verb test that separates mandatory instructions from helpful advice.",
                "content_html": """
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#fef2f2; border-left:4px solid #e11d48; padding:16px; border-radius:6px;">
                    <h4 style="color:#be123c; margin-top:0; margin-bottom:8px;">To Instruct (Mandatory Rules)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;">Leaves <strong>zero choice</strong>. Uses imperative commands and <em>"must / do not"</em>:<br><em>"1. Isolate the mains switch. 2. Lock the fuse box with your safety padlock."</em></p>
                  </div>
                  <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                    <h4 style="color:#166534; margin-top:0; margin-bottom:8px;">To Advise (Optional Recommendations)</h4>
                    <p style="margin:0; color:#1e293b; line-height:1.7;">Offers <strong>helpful suggestions</strong> the reader can choose to follow. Uses <em>"could / should / consider"</em>:<br><em>"You might find it helpful to prepare your interview outfit the evening before."</em></p>
                  </div>
                </div>
                """
            },
            {
                "title": "How Writers Adapt Language to Suit Their Target Audience",
                "summary": "Explaining why a text's vocabulary and examples fit a specific demographic.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">When asked <em>"How has the writer adapted this text to suit its target audience?"</em>, look at three elements:</p>
                <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                  <li><strong>Register &amp; Slang:</strong> Uses casual, upbeat language for teenagers/students vs formal clinical language for senior managers.</li>
                  <li><strong>Relatable Examples &amp; Scenarios:</strong> Mentions student loans and campus halls for university students, or pension tax relief and mortgage rates for older professionals.</li>
                  <li><strong>Visual &amp; Layout Aids:</strong> Uses step-by-step diagrams and plain-English glossaries for beginners vs dense data tables for experienced analysts.</li>
                </ol>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Purpose and Audience of a Workplace Guide (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Apprentice Induction Advice Sheet",
                "question": "Read this extract from a college booklet:<br><em>'Starting your first carpentry apprenticeship can feel overwhelming! To make a great impression in week one, you should pack two sharp pencils, arrive 10 minutes before your site supervisor, and never hesitate to ask questions if a power tool feels unfamiliar.'</em><br>(a) What is the <strong>main purpose</strong> of this extract? [1 Mark]<br>(b) Who is the specific <strong>target audience</strong>? [1 Mark]",
                "steps": [
                    ("Step 1", "Identify the purpose verb + specific topic", "The text uses supportive suggestions ('you should', 'never hesitate to') to advise and reassure new apprentices on how to succeed in their first week on site.", "1 Mark [A1 Purpose + Topic]"),
                    ("Step 2", "Identify the specific target audience", "New carpentry apprentices (or trainees starting their first construction apprenticeship).", "1 Mark [A1 Specific Audience]")
                ],
                "final_answer": "(a) To advise and reassure new carpentry apprentices on how to prepare and succeed during their first week at work. | (b) First-year carpentry apprentices.",
                "tutor_tip": "Notice how the answer states 'To advise new carpentry apprentices on how to succeed in their first week' — including the topic secures the mark!"
            },
            {
                "title": "NHS Blood Donation Appeal Purpose & Sub-Purpose Analysis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Transfusion Service Public Campaign",
                "question": "An NHS campaign text opens with a moving story of a six-year-old child surviving leukaemia thanks to platelet donors, followed by a box stating <em>'Donating takes just 45 minutes and requires no medical check-up beforehand'</em>, and ends with: <em>'Register as a donor today — 45 minutes of your time is someone's lifetime.'</em><br>(a) State the <strong>overall main purpose</strong> of this text. [1 Mark]<br>(b) Explain why the writer included the child's recovery story. [1 Mark]<br>(c) Explain why the writer included the factual box about the 45-minute appointment time. [1 Mark]",
                "steps": [
                    ("Step 1", "State the overarching purpose with topic context", "To persuade members of the public to register and donate blood/platelets for the NHS.", "1 Mark [A1 Main Purpose]"),
                    ("Step 2", "Explain the persuasive purpose of the case study", "The child's recovery story creates an emotional connection (empathy and warmth) and proves that donations save real children's lives.", "1 Mark [A1 Story Purpose]"),
                    ("Step 3", "Explain the purpose of the factual reassurance box", "Informing readers that donating takes only 45 minutes with no prior check-up removes practical excuses or fears about the process being too slow or complicated.", "1 Mark [A1 Sub-Purpose]")
                ],
                "final_answer": "(a) To persuade the public to register and donate blood/platelets. | (b) Evokes empathy and provides emotional proof that donations save children's lives. | (c) Reassures busy or nervous readers that donating is quick (45 minutes) and straightforward.",
                "tutor_tip": "Persuasive texts often include informative boxes to remove practical barriers (like time or fear) so the reader takes action."
            }
        ],
        "examiner_traps": [
            {
                "title": "Treating Persuasive Texts as Solely Informative",
                "desc": "A text may contain plenty of facts and statistics, but if those facts are selected to convince you to buy a product, donate money, or sign a petition, its main purpose is to persuade.",
                "fix": "Always check the conclusion and final call-to-action before deciding the main purpose."
            },
            {
                "title": "Giving a One-Word Answer ('To Inform')",
                "desc": "Writing 'To inform' without explaining what the text informs the reader about scores 0 marks on Pearson Edexcel Level 1 and Level 2 papers.",
                "fix": "Always write a full sentence: 'To inform [audience] about [specific topic].'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A hospice director publishes a newspaper article titled: <em>'Dignity at the End: Why Community Palliative Care Deserves Equal NHS Funding.'</em><br>State the writer's <strong>main purpose</strong> and <strong>target audience</strong>.",
                "solution_steps": "1. Main purpose: To persuade/campaign for equal NHS funding for community palliative care services by highlighting patient dignity [1 Mark].<br>2. Target audience: Newspaper readers, voters, and healthcare policymakers/commissioners [1 Mark].",
                "correct_answer": "Main Purpose: To persuade the public and policymakers that community palliative care deserves equal NHS funding. | Target Audience: Adult newspaper readers and healthcare decision-makers.",
                "tutor_tip": "Look at the word 'Why... Deserves' in the headline — that confirms the writer is arguing/persuading for a cause."
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a home energy guide:<br><em>'If you want to cut £150 off your winter heating bill without spending a penny, try bleeding your radiators in October and moving sofas at least 30 cm away from wall heaters.'</em><br>Is the main purpose of this extract to <strong>instruct</strong> or to <strong>advise</strong>? Explain your answer.",
                "solution_steps": "1. Identification: To advise [1 Mark].<br>2. Explanation: It offers optional, money-saving suggestions ('If you want to...', 'try bleeding...') to help householders lower their bills, rather than mandatory safety commands [1 Mark].",
                "correct_answer": "To advise — it offers helpful, optional money-saving tips ('If you want to...', 'try bleeding...') rather than compulsory rules.",
                "tutor_tip": "Words like 'try' and 'if you want to' always signal advice rather than strict instruction."
            },
            {
                "marks": "2 Marks",
                "question": "A leaflet distributed at a GP surgery is titled: <strong>'Understanding Type 2 Diabetes: Symptoms, Blood Sugar Checks, and Local Support Groups'</strong>.<br>Explain the <strong>main purpose</strong> of this leaflet and identify who it is written for.",
                "solution_steps": "1. Main purpose: To inform and educate readers about Type 2 diabetes symptoms, blood sugar monitoring, and where to access local support [1 Mark].<br>2. Target audience: Newly diagnosed Type 2 diabetes patients, their families, or GP patients worried about symptoms [1 Mark].",
                "correct_answer": "Main Purpose: To inform and guide readers about Type 2 diabetes symptoms, monitoring, and local support groups. | Target Audience: GP patients diagnosed with or at risk of Type 2 diabetes and their families.",
                "tutor_tip": "Include all key elements from the title when stating what the leaflet informs patients about."
            }
        ]
    },
    # 13. The Exam (Reading Exam Strategy & Timing)
    {
        "filename": "reading-the-exam.html",
        "clean_topic": "Reading Exam Strategy, Command Words & Timing",
        "intro_lead": "Master exam hall time management, command-word decoding, quotation precision, and mark scheme criteria across Pearson Edexcel, City & Guilds, and NCFE Reading papers.",
        "next_file": "writing-planning-your-answer.html",
        "next_name": "Planning Written Responses",
        "spec_points": [
            ("L1 / L2 Exam Strategy", "Manage 60-minute reading exam papers effectively across three unseen source texts (Text A, Text B, Text C)."),
            ("Mark Scheme Mastery", "Decode command verbs (Identify, Explain, Replace, Compare) and match answer depth to 1, 2, 3, and 4-mark allocations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-clock",
                "title": "Golden Rule 1: The 'Two Minutes Per Mark' Pacing Rule",
                "desc": "Pearson Edexcel Reading exams last 60 minutes for 30 marks across three texts. Spend roughly 1.5 to 2 minutes per mark: answer 1-mark retrieval questions in 60 seconds so you bank extra time for the multi-mark Level 2 comparison and evaluation questions.",
                "badge": "60 Mins / 30 Marks: Never spend 10 minutes stuck on a 1-mark question!"
            },
            {
                "icon": "fa-crosshairs",
                "title": "Golden Rule 2: Read the Question & Target Text Label FIRST",
                "desc": "Always check WHICH text the question specifies ('Using Text A...', 'Look at Text B...'). If you give a factually true answer from Text B when the question asked about Text A, you automatically score 0 marks!",
                "badge": "Check: 1. Which Text? | 2. How many points? | 3. Do I need a quote?"
            }
        ],
        "skills": [
            {
                "title": "Decoding Exam Command Verbs & Mark Allocations",
                "summary": "Know exactly what the examiner expects for every command phrase.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Exam Command Phrase</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Typical Marks</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Exact Mark Scheme Requirement</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Identify / State / Give two..."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1–2 Marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Direct information retrieval. Lift the exact fact, figure, or short phrase from the named text. No lengthy explanation needed.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Give one word or phrase to replace..."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1–2 Marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Write a single synonym or short phrase that matches the exact contextual meaning AND fits grammatically into the original sentence.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Explain how two language / organisational features..."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">2–4 Marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1. Name the feature. 2. Give the exact quote/example. 3. Explain the specific effect on the reader in this context.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;"><em>"Compare how Text A and Text B..."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">3–6 Marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Synthesise both texts using comparative connectives (<em>whereas, similarly</em>) and include direct quotes from BOTH texts.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Watching Out for Negative & Qualifier Traps in Questions",
                "summary": "How words like 'NOT', 'EXCEPT', 'MINIMUM', and 'APART FROM' trip up rushed candidates.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Examiners test close reading accuracy by inserting qualifier words into both the question stem and the source text:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>"Apart from X, give two reasons..."</strong> &rarr; The question has already given you 'X' as an example. If you write 'X' in your answer space, it scores 0! Find two <em>other</em> reasons in the text.</li>
                  <li><strong>"Which one of the following statements is FALSE / NOT true?"</strong> &rarr; Three options are true facts from the text; you must tick the one statement that contradicts the text.</li>
                  <li><strong>Numerical Qualifiers (<em>"at least", "up to", "under", "more than"</em>):</strong> If the text says <em>"Grants are available for businesses with <strong>fewer than 50</strong> staff"</em>, a business with 50 staff does <em>not</em> qualify!</li>
                </ul>
                """
            },
            {
                "title": "Quotation Precision: How Much to Copy",
                "summary": "Why copying too little or too much costs marks on quotation questions.",
                "content_html": """
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>The Goldilocks Quotation Rule:</strong><br>• <strong>Too Short (0 Marks):</strong> Writing <em>"£15"</em> when asked for a quote showing the parking fine increased &rarr; doesn't make sense on its own.<br>• <strong>Too Long (0 Marks):</strong> Copying a 40-word paragraph containing 3 facts and 2 opinions when asked for one quote.<br>• <strong>Just Right (Full Marks):</strong> Copying the exact 4–10 word clause that proves the point: <em>"'parking fines rose by £15 in April'"</em>.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Avoiding the 'Apart From' Qualifier Trap (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Workplace Induction Checklist Retrieval",
                "question": "Read this extract from Text A:<br><em>'Before starting your first warehouse shift, you must bring your signed contract, a valid passport or driving licence, steel-toe safety boots, and your National Insurance number.'</em><br>Exam Question: <strong>Apart from steel-toe safety boots, identify two things you must bring before starting your first shift. [2 Marks]</strong><br>Explain why writing <em>'1. Steel-toe boots 2. Signed contract'</em> only scores 1 mark, and write a full 2-mark answer.",
                "steps": [
                    ("Step 1", "Identify the 'Apart from' exclusion rule", "The question explicitly says 'Apart from steel-toe safety boots', which excludes safety boots from receiving credit.", "1 Mark [Rule Analysis]"),
                    ("Step 2", "Extract two valid remaining items from the text", "1. Signed contract. 2. Valid passport or driving licence (or National Insurance number).", "1 Mark [Full 2-Mark Retrieval]")
                ],
                "final_answer": "'Apart from' means excluding that item. Correct 2-mark answer: 1. Signed contract. 2. Valid passport or driving licence (or National Insurance number).",
                "tutor_tip": "Always underline 'Apart from...' or 'Other than...' in the question stem so you never repeat the excluded item!"
            },
            {
                "title": "Executing a 3-Mark Evidence & Justification Question (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Evaluating a Colleague's Claim Against Text Evidence",
                "question": "Read this extract from Text B (Council Solar Grant Rules):<br><em>'Small businesses in the borough can claim a £4,000 grant towards rooftop solar panels, provided the building was constructed before 2015, employs fewer than 25 full-time staff, and submits two independent installer quotes by 30 November.'</em><br>Your colleague says: <em>'Our bakery was built in 2010 and we have 18 full-time staff, so we are guaranteed to get the £4,000 grant whenever we apply next year!'</em><br>Using Text B, explain whether your colleague is correct, giving <strong>three pieces of evidence</strong> to justify your answer. [3 Marks]",
                "steps": [
                    ("Step 1", "Check criteria met (Building age & Staff count)", "The colleague is right that the bakery meets the pre-2015 building rule (built in 2010) and the under-25 staff limit (18 full-time staff).", "1 Mark [A1 Criteria Met]"),
                    ("Step 2", "Spot the deadline violation ('next year')", "However, the colleague is wrong to say they can apply 'next year' because applications must be submitted 'by 30 November'.", "1 Mark [A1 Deadline Condition]"),
                    ("Step 3", "Spot the missing requirement (two installer quotes)", "Furthermore, the grant is not guaranteed until they also submit 'two independent installer quotes'.", "1 Mark [A1 Quote Condition]")
                ],
                "final_answer": "The colleague is only partly correct (overall incorrect): while the bakery qualifies on building age (built in 2010, which is before 2015) and staff size (18 is fewer than 25), they cannot apply 'next year' because the deadline is 30 November, and they must also submit two independent installer quotes.",
                "tutor_tip": "In 'Is X correct?' evaluation questions, check every single condition in the source text (age, numbers, dates, and required documents)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Answering from Personal Experience Instead of Text Evidence",
                "desc": "Even if you are an experienced nurse, electrician, or manager, you score 0 if you write real-world advice that is not printed in the source text.",
                "fix": "Anchor every single answer strictly to the words and facts printed on the exam paper."
            },
            {
                "title": "Looking at the Wrong Source Text (Text A vs Text B)",
                "desc": "Under exam pressure, candidates frequently pull quotes from Text B when the question starts with 'Using Text A...'.",
                "fix": "Physically point your finger at the requested Text header ('Text A') before writing your answer."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Read this extract from Text A:<br><em>'Staff parking permits cost £15 per month for petrol cars, £10 per month for hybrid vehicles, and are completely free for fully electric cars and bicycles.'</em><br>Question: <strong>Apart from bicycles, identify two types of transport that receive free or discounted parking permits compared to petrol cars.</strong>",
                "solution_steps": "1. Exclude 'bicycles' because of 'Apart from bicycles'.<br>2. Transport 1: Fully electric cars (receive free permits) [1 Mark].<br>3. Transport 2: Hybrid vehicles (receive discounted £10 permits compared to £15 for petrol) [1 Mark].",
                "correct_answer": "1. Fully electric cars (free). | 2. Hybrid vehicles (£10 per month vs £15 for petrol).",
                "tutor_tip": "Carefully excluding bicycles and naming both electric cars and hybrid vehicles secures both marks."
            },
            {
                "marks": "2 Marks",
                "question": "Read this sentence:<br><em>'The new warehouse scanner is <strong>indispensable</strong> for tracking chilled medical deliveries.'</em><br>An exam question asks: <strong>'Give one word or phrase to replace indispensable that keeps the meaning of the sentence. [1 Mark]'</strong><br>(a) Explain why the answer <em>'essential'</em> scores 1 mark.<br>(b) Explain why the answer <em>'you cannot do without it'</em> scores 0 marks.",
                "solution_steps": "1. Why 'essential' scores 1 mark: It is an adjective that means the exact same thing and fits grammatically ('The new warehouse scanner is essential for tracking...') [1 Mark].<br>2. Why 'you cannot do without it' scores 0 marks: It is a full clause that breaks the grammar of the sentence if substituted ('The new warehouse scanner is you cannot do without it for tracking...') [1 Mark].",
                "correct_answer": "(a) 'Essential' is an adjective that fits seamlessly into the sentence grammar. | (b) 'You cannot do without it' does not fit grammatically when plugged into the sentence.",
                "tutor_tip": "Always plug your replacement word back into the original sentence to check that it reads smoothly!"
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a training centre brochure:<br><em>'Our Forklift Licence Course costs £380 and runs every Saturday from 08:30 to 16:30. Trainees must be aged 18 or over, hold a provisional or full UK driving licence, and bring their own high-visibility vest.'</em><br>Sam is 17 years old, has a provisional UK driving licence, and owns a high-visibility vest. Can Sam join the course this Saturday? Explain your answer using evidence from the text. [3 Marks]",
                "solution_steps": "1. Clear verdict: No, Sam cannot join the course this Saturday [1 Mark].<br>2. Criteria met: Sam meets the requirements of holding a provisional UK driving licence and owning a high-visibility vest [1 Mark].<br>3. Criterion failed: However, the text states trainees 'must be aged 18 or over', and Sam is only 17 [1 Mark].",
                "correct_answer": "No — although Sam has a provisional UK driving licence and a high-visibility vest, trainees 'must be aged 18 or over' and Sam is only 17.",
                "tutor_tip": "State 'No' clearly at the start, then reference both the rules Sam meets and the specific age rule (18 or over) Sam fails."
            }
        ]
    }
]
