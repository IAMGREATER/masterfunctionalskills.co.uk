#!/usr/bin/env python3
"""
Authentic Fluency Workouts: English Reading Batch 3
17 Curriculum Topics:
1. reading-comparing-texts
2. reading-investigating-image
3. reading-meaning
4. reading-point-of-view-and-line-of-argument
5. reading-presentational-features
6. reading-specialist-words
7. reading-styles-of-writing-and-voice
8. reading-text-types
9. reading-the-exam
10. reading-why-do-writers-write
11. assessing-the-basics
12. common-mistakes
13. detecting-language-techniques
14. formality-and-bias
15. piecing-it-together-comparing-texts
16. piecing-it-together-key-and-detailed-points
17. types-of-and-navigating-sources
"""

ENGLISH_READING_BATCH3_WORKOUTS = {
    # 1. COMPARING TEXTS
    "reading-comparing-texts": {
        "title": "Comparing Texts & Cross-Referencing Ideas",
        "slug": "reading-comparing-texts",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.11 • L2.12",
        "level": "Level 2",
        "method_card": {
            "title": "Synthesising Information Across Two Texts",
            "points": [
                "Identify the common theme or topic shared by Text A and Text B.",
                "Find points of agreement: Identify ideas, facts, or recommendations supported by BOTH texts.",
                "Find points of contrast: Identify differing perspectives, tones, or conflicting evidence.",
                "Quote or paraphrase accurately: Explicitly state 'Text A argues that... whereas Text B suggests...'",
                "Never write about only one text when a question specifies comparison across both sources."
            ],
            "calc_tip": "Draw a quick 2-column table on scrap paper: Column 1 = Text A points, Column 2 = Text B points."
        },
        "workout_blocks": [
            {
                "title": "Identifying Agreement vs Contrast",
                "instruction": "State whether the pair of statements shows Agreement or Contrast:",
                "items": [
                    ("a", "Text A: 'Hybrid working boosts team morale.' | Text B: 'Working from home enhances employee satisfaction.'", "Agreement (both support remote work)"),
                    ("b", "Text A: 'Electric fleet vans save operational costs.' | Text B: 'High battery replacement costs make EVs uneconomical.'", "Contrast (conflicting financial views)"),
                    ("c", "Text A: 'Staff shortages caused delays.' | Text B: 'Delays occurred due to inadequate staffing numbers.'", "Agreement (same root cause)"),
                    ("d", "Text A: 'Online booking is quick and effortless.' | Text B: 'Patients struggle to navigate the online appointment system.'", "Contrast (positive vs negative user experience)")
                ]
            },
            {
                "title": "Formulating Comparative Sentences",
                "instruction": "Complete the sentence with an appropriate comparative connective (similarly, whereas, however, conversely):",
                "items": [
                    ("a", "Text A emphasizes technological solutions, (whereas / similarly) Text B focuses on human empathy.", "whereas (contrast)"),
                    ("b", "Text A warns of safety risks; (similarly / in contrast), Text B highlights rising incident rates.", "similarly (agreement)"),
                    ("c", "Text A maintains an optimistic tone; Text B, (however / likewise), adopts a cautious stance.", "however (contrast)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinic Fleet Transport Comparison",
                "stem": "Text A states: <em>'Adopting electric courier vehicles will reduce our clinic's carbon emissions by 40% and lower annual fuel costs.'</em><br>Text B states: <em>'The high initial purchase price of electric vans and the lack of regional fast-charging hubs represent significant operational hurdles.'</em><br><br>Compare the views expressed in Text A and Text B regarding electric courier vehicles. You must refer to both texts in your answer.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("State Text A's positive focus on environmental and long-term fuel savings", "[R1]"),
                    ("State Text B's critical concern regarding initial capital expense and charging infrastructure", "[R1]"),
                    ("Synthesise into a clear comparative summary using contrasting connective ('whereas' / 'on the other hand')", "[A1]")
                ],
                "final_answer": "Text A presents an optimistic perspective highlighting environmental benefits (40% emission reduction) and fuel savings, whereas Text B expresses skepticism, pointing out high capital costs and inadequate charging infrastructure.",
                "reverse_check": "Quotes/paraphrases evidence from both texts with balanced contrast.",
                "pitfall": "Summarizing Text A only and failing to mention Text B."
            }
        ]
    },

    # 2. INVESTIGATING IMAGE
    "reading-investigating-image": {
        "title": "Visual Literacy: Analyzing Images, Diagrams & Graphics",
        "slug": "reading-investigating-image",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.14 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Linking Images to Written Text",
            "points": [
                "Images in functional texts are never purely decorative; they reinforce, clarify, or extend the written message.",
                "Identify image type: Photograph, diagram, flowchart, map, infographic, or warning icon.",
                "Analyze purpose: Does it instruct (how to wear PPE), persuade (happy patient recovery photo), or inform (step-by-step assembly)?",
                "Explain the relationship between the image and the surrounding text.",
                "Look at captions: Captions provide critical explanatory context."
            ],
            "calc_tip": "When asked why an image was included, answer: 'The image illustrates [detail] which helps the reader to understand [concept] by visually showing [action].'"
        },
        "workout_blocks": [
            {
                "title": "Identifying the Purpose of Visuals",
                "instruction": "State the primary communicative purpose of each visual element:",
                "items": [
                    ("a", "A step-by-step diagram showing correct clinical handwashing technique", "Instructional (guides correct physical action)"),
                    ("b", "A high-contrast photograph of a smiling, active resident in a care home brochure", "Persuasive / Reassuring (builds trust and emotional appeal)"),
                    ("c", "A bold yellow triangle icon with an exclamation mark on a chemical bottle", "Safety Warning (alerts reader to hazardous content)"),
                    ("d", "A pie chart showing patient feedback ratings", "Informative (displays numerical proportions clearly)")
                ]
            },
            {
                "title": "Connecting Visuals with Textual Evidence",
                "instruction": "Select the best explanation for how the image supports the text:",
                "items": [
                    ("a", "Text describes fire escape routes; image shows a green floor plan with arrows.", "Allows readers to quickly trace emergency exit paths"),
                    ("b", "Text warns of slippery floors; image shows a person slipping on wet tiles.", "Provides an immediate visual hazard warning to draw attention")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Sharps Disposal Safety Notice",
                "stem": "A workplace safety poster on clinical waste disposal includes a close-up photograph of a rigid yellow disposal bin with a locking lid, positioned next to the text: <em>'Always seal clinical sharps containers when they reach the fill line.'</em><br><br>Explain two ways the photograph supports the information given in the written text.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Point 1: Visually identifies the specific yellow container to avoid confusion with general waste bins", "[R1]"),
                    ("Point 2: Clearly illustrates the visible fill line and secure lid mechanism described in the text", "[A1]")
                ],
                "final_answer": "1. It helps staff instantly recognize the specific yellow sharps container in a busy clinic. 2. It visually demonstrates the location of the fill line and locking lid, ensuring compliance with disposal safety.",
                "reverse_check": "Provides 2 distinct functional links between text and image.",
                "pitfall": "Giving a vague generic answer like 'It looks nice' or 'It makes people read it'."
            }
        ]
    },

    # 3. READING MEANING
    "reading-meaning": {
        "title": "Explicit & Implicit Meaning: Inference & Deduction",
        "slug": "reading-meaning",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.11 • L2.13",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Reading Between the Lines (Inference)",
            "points": [
                "Explicit Meaning: Information directly stated in black and white on the page (facts, dates, names).",
                "Implicit Meaning: Information suggested or implied without being directly stated (inference/deduction).",
                "How to infer: Look at the author's word choice, tone, and what is omitted.",
                "PEE Method: Point (Your inference) + Evidence (Direct quote from text) + Explanation (How the quote supports your point)."
            ],
            "calc_tip": "If a question asks 'What does the writer suggest about...', they want an INFERENCE, not just a copied quote."
        },
        "workout_blocks": [
            {
                "title": "Explicit vs Implicit Meaning",
                "instruction": "State whether the statement is Explicit (directly stated) or Implicit (inferred):",
                "items": [
                    ("a", "Text: 'The meeting commenced at 09:30 in Boardroom A.' Fact: The meeting started at 9:30am.", "Explicit (directly stated)"),
                    ("b", "Text: 'He checked his watch repeatedly and tapped his foot against the floor.' Deduction: He was impatient or anxious.", "Implicit (inferred from body language)"),
                    ("c", "Text: 'Staff sighed heavily when the third rota revision of the week was pinned to the board.' Deduction: Staff were frustrated and weary of constant schedule changes.", "Implicit (inferred from reaction)"),
                    ("d", "Text: 'The clinic treated 1,420 patients in August.' Fact: 1,420 patients were treated in August.", "Explicit")
                ]
            },
            {
                "title": "Drawing Accurate Inferences",
                "instruction": "State what can be reasonably inferred from the sentence:",
                "items": [
                    ("a", "'Despite four polite reminder notices, the outstanding invoice remained unpaid.'", "The client is deliberately delaying or avoiding payment"),
                    ("b", "'The newly qualified nurse double-checked the dosage chart three times before drawing the vial.'", "The nurse is conscientious, cautious, and keen to avoid medication errors"),
                    ("c", "'The office air conditioning has been 'under maintenance' since early June.'", "The repair has been delayed or neglected for months (skeptical tone)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Ward Inspection Report Inference",
                "stem": "An excerpt from a healthcare quality inspector's log reads:<br><em>'Although staff were welcoming and attentive to patient comfort, several call bells echoed down the eastern corridor for over ten minutes before receiving a response.'</em><br><br>What does this sentence imply about ward operations during the inspection? Give one inference and quote the supporting evidence.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify inference: The ward is likely understaffed or struggling to manage workload despite having caring staff", "[R1]"),
                    ("Support with direct evidence: 'call bells echoed down the eastern corridor for over ten minutes before receiving a response'", "[A1]")
                ],
                "final_answer": "Inference: The ward is experiencing staffing shortages or workload pressure that prevents timely response to patient calls. Evidence: 'several call bells echoed down the eastern corridor for over ten minutes before receiving a response'.",
                "reverse_check": "Combines a valid deduction with verbatim textual evidence.",
                "pitfall": "Repeating the explicit fact ('it implies call bells rang') without making an inference about ward capacity."
            }
        ]
    },

    # 4. POINT OF VIEW AND LINE OF ARGUMENT
    "reading-point-of-view-and-line-of-argument": {
        "title": "Point of View, Bias & Lines of Argument",
        "slug": "reading-point-of-view-and-line-of-argument",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.15 • L2.16",
        "level": "Level 2",
        "method_card": {
            "title": "Analyzing Writer's Stance & Perspective",
            "points": [
                "Point of View (POV): The author's personal stance, opinion, or angle on an issue.",
                "Line of Argument: The logical progression of reasons and evidence used to build a case from introduction to conclusion.",
                "Bias: A one-sided perspective that favors one viewpoint while ignoring or dismissing counter-arguments.",
                "Balanced text: Presents multiple viewpoints with supporting evidence before reaching a reasoned conclusion.",
                "Spotting bias: Look for loaded adjectives ('disastrous', 'revolutionary'), selective data, and dismissive language."
            ],
            "calc_tip": "Ask yourself: 'Who wrote this, what do they want me to believe, and who benefits if I agree?'"
        },
        "workout_blocks": [
            {
                "title": "Identifying Point of View",
                "instruction": "State whether the writer's stance is In Favor, Opposed, or Balanced/Neutral:",
                "items": [
                    ("a", "'Introducing flexible shift rosters will rejuvenate staff retention and reduce absenteeism across all departments.'", "In Favor (strongly supportive)"),
                    ("b", "'While automated triage kiosks reduce queue times, they lack the diagnostic nuance and human empathy of trained nurses.'", "Balanced / Neutral (weighs pros and cons)"),
                    ("c", "'Scrapping public bus subsidies is an ill-conceived and reckless decision that will isolate vulnerable patients.'", "Opposed (critical, emotive)")
                ]
            },
            {
                "title": "Detecting Bias Indicators",
                "instruction": "Identify the word or phrase that reveals writer bias:",
                "items": [
                    ("a", "'The council's so-called consultation was an absolute farce.'", "'so-called' and 'absolute farce' (loaded, dismissive)"),
                    ("b", "'Only foolish managers would resist adopting this cutting-edge software.'", "'Only foolish managers' (ad hominem, biased assertion)"),
                    ("c", "'Clinical trials demonstrated a 15% reduction in symptoms over 12 weeks.'", "No bias (objective empirical statement)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Transport Policy Article",
                "stem": "Read this opening paragraph from a regional newspaper opinion column:<br><em>'The local authority's misguided decision to shut down the community health shuttle bus is an unmitigated disaster for elderly patients. Council bureaucrats claim they are saving taxpayers money, but anyone with an ounce of compassion can see this is a callous attack on vulnerable citizens.'</em><br><br>Explain how the writer uses language to present a biased point of view. Support your answer with two examples from the text.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify writer's point of view: Strongly opposed to the closure of the health shuttle bus", "[R1]"),
                    ("Example 1: Loaded emotive language ('misguided', 'unmitigated disaster', 'callous attack') paints the council negatively", "[R1]"),
                    ("Example 2: Pejorative labeling ('Council bureaucrats', 'anyone with an ounce of compassion') dismisses opposing arguments without objective facts", "[A1]")
                ],
                "final_answer": "The writer presents an intensely biased viewpoint against the closure by employing emotionally charged language ('unmitigated disaster', 'callous attack') and dismissive labeling of officials ('Council bureaucrats'), presenting their opinion as moral truth while ignoring financial constraints.",
                "reverse_check": "Identifies viewpoint, cites 2 textual examples, explains effect.",
                "pitfall": "Stating whether you agree with the writer instead of analyzing how the language creates bias."
            }
        ]
    },

    # 5. PRESENTATIONAL FEATURES
    "reading-presentational-features": {
        "title": "Presentational Features & Document Layout",
        "slug": "reading-presentational-features",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.14 • L2.14",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Layout Elements & Reader Navigation",
            "points": [
                "Headlines & Titles: Grab attention and indicate the overarching topic.",
                "Subheadings: Divide text into logical chunks and guide the reader's eye when scanning.",
                "Bullet Points: Break down complex instructions, lists, or key takeaways for rapid reading.",
                "Bold Text / Italics: Highlight critical warnings, dates, or essential terminology.",
                "Text Boxes / Callouts: Isolate crucial advice, quotes, or contact information."
            ],
            "calc_tip": "When asked how a feature helps the reader, always link FEATURE → FUNCTION → READER BENEFIT."
        },
        "workout_blocks": [
            {
                "title": "Linking Features to Functions",
                "instruction": "State the presentational feature best suited for each purpose:",
                "items": [
                    ("a", "Highlighting an urgent telephone hotline number", "Text box / Bold text"),
                    ("b", "Listing the 5 mandatory items required for a job interview", "Bullet points / Numbered list"),
                    ("c", "Dividing a 1,000-word workplace policy into distinct subjects", "Subheadings"),
                    ("d", "Showing the percentage of staff vaccinated by department", "Table / Bar chart"),
                    ("e", "Summarizing the author's qualification and job title", "Byline / Footnote")
                ]
            },
            {
                "title": "Analyzing Layout Effectiveness",
                "instruction": "Explain why this feature was used rather than a solid block of text:",
                "items": [
                    ("a", "Using numbered steps (1, 2, 3) for an emergency evacuation procedure", "Ensures users follow instructions in exact sequential order under stress"),
                    ("b", "Printing warning phrases in red bold text on medication labels", "Draws immediate visual attention to prevent dangerous errors")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Facility Infection Control Poster",
                "stem": "An infection prevention noticeboard uses:<br>• A large bold headline: <strong>'STOP THE SPREAD: BARE BELOW THE ELBOWS'</strong><br>• Three bulleted rules with checkmark icons<br>• A shaded yellow text box at the bottom containing contact details for the Infection Control Lead.<br><br>Explain how <strong>two</strong> of these presentational features assist the reader in navigating the information.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Feature 1: Large bold headline catches passing staff/visitor attention and immediately clarifies the hygiene rule", "[R1]"),
                    ("Feature 2: Shaded yellow text box isolates contact info so readers can quickly find where to seek advice without searching the main text", "[A1]")
                ],
                "final_answer": "1. Large bold headline: Immediately arrests the reader's attention and summarizes the core instruction before entering clinical wards. 2. Shaded text box: Clearly separates contact details from clinical rules so staff can locate specialist advice in seconds.",
                "reverse_check": "Identifies 2 distinct features and explains their specific reader utility.",
                "pitfall": "Listing features without explaining HOW they help the reader."
            }
        ]
    },

    # 6. SPECIALIST WORDS
    "reading-specialist-words": {
        "title": "Specialist Vocabulary & Technical Jargon",
        "slug": "reading-specialist-words",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.16 • L2.17",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Deciphering Unfamiliar Technical Terms",
            "points": [
                "Context Clues: Look at words and sentences before and after the unfamiliar term to infer meaning.",
                "Root words, prefixes, and suffixes: 'Bio-' (life), 'Micro-' (small), 'Cardio-' (heart), '-logy' (study of).",
                "Glossary & Footnotes: Technical documents often define specialist terminology at the end or in margins.",
                "Synonym substitution: Replace the unknown word with a candidate synonym to test if the sentence still makes sense."
            ],
            "calc_tip": "If asked to define a specialist word in an exam, give its meaning IN THE CONTEXT of the passage."
        },
        "workout_blocks": [
            {
                "title": "Inferring Meaning from Context",
                "instruction": "Deduce the meaning of the underlined technical word from its surrounding context:",
                "items": [
                    ("a", "'The wound was <u>superficial</u>, affecting only the outermost layer of skin and requiring no stitches.'", "Minor / surface-level (not deep)"),
                    ("b", "'The medication provides <u>palliative</u> care, relieving painful symptoms rather than curing the condition.'", "Soothing / symptom-relieving without curing"),
                    ("c", "'Ensure all instruments are thoroughly <u>sterilised</u> to eliminate bacteria and prevent infection.'", "Disinfected / free from living microorganisms"),
                    ("d", "'The audit revealed significant <u>discrepancies</u> between recorded stock and physical items on the shelf.'", "Inconsistencies / differences / mismatches")
                ]
            },
            {
                "title": "Prefixes and Suffixes in Workplace Vocabulary",
                "instruction": "State the meaning added by each prefix or suffix:",
                "items": [
                    ("a", "Prefix 'mis-' (e.g. miscalculate, misinform)", "Wrongly / incorrectly"),
                    ("b", "Prefix 'pre-' (e.g. pre-op, precaution)", "Before / in advance"),
                    ("c", "Prefix 'anti-' (e.g. antibacterial, antiviral)", "Against / counteracting"),
                    ("d", "Suffix '-able' (e.g. recyclable, washable)", "Capable of being")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Pharmacy Storage Protocol",
                "stem": "A pharmaceutical guidelines document states:<br><em>'Insulin is highly <u>thermolabile</u>; exposure to elevated ambient temperatures accelerates molecular degradation and significantly impairs clinical efficacy.'</em><br><br>Using context clues from the sentence, explain what the specialist term <strong>thermolabile</strong> means.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify context clue: 'exposure to elevated ambient temperatures accelerates degradation'", "[R1]"),
                    ("State clear definition: Easily destroyed, broken down, or sensitive to heat", "[A1]")
                ],
                "final_answer": "'Thermolabile' means sensitive to or easily altered/decomposed by heat.",
                "reverse_check": "Sentence context directly supports heat sensitivity.",
                "pitfall": "Copying the words 'elevated ambient temperatures' without defining the core term."
            }
        ]
    },

    # 7. STYLES OF WRITING AND VOICE
    "reading-styles-of-writing-and-voice": {
        "title": "Writing Styles, Tone & Writer's Voice",
        "slug": "reading-styles-of-writing-and-voice",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.15 • L2.16",
        "level": "Level 2",
        "method_card": {
            "title": "Recognizing Tone & Perspective",
            "points": [
                "Tone reflects the writer's attitude: Critical, enthusiastic, authoritative, sarcastic, empathetic, cautionary.",
                "Formality spectrum: Highly formal (academic/legal) to highly informal (chatty/colloquial).",
                "First-person voice ('I', 'we'): Subjective, personal, reflective, direct.",
                "Third-person voice ('he', 'she', 'they', 'the organisation'): Objective, professional, detached.",
                "Humorous or satirical tone: Uses irony, exaggeration (hyperbole), and wit."
            ],
            "calc_tip": "When asked to identify tone, always provide a specific adjective and quote 2 words that create that tone."
        },
        "workout_blocks": [
            {
                "title": "Identifying Tone from Excerpts",
                "instruction": "Select the adjective that best describes the tone (Authoritative, Sarcastic, Empathetic, or Cautionary):",
                "items": [
                    ("a", "'Failure to wear PPE will result in immediate disciplinary suspension under Regulation 4.'", "Authoritative / Stern"),
                    ("b", "'Oh brilliant, another software update that takes two hours and deletes your preferences.'", "Sarcastic / Ironic"),
                    ("c", "'We understand how overwhelming starting a new ward placement can feel, and our mentors are here to support you.'", "Empathetic / Supportive"),
                    ("d", "'High winds are forecast; estates teams must secure all scaffolding and loose roof sheeting immediately.'", "Cautionary / Urgent")
                ]
            },
            {
                "title": "Voice and Perspective",
                "instruction": "State whether the excerpt uses First, Second, or Third Person voice:",
                "items": [
                    ("a", "'I began my nursing career in a busy acute surgical ward in Leeds.'", "First person ('I')"),
                    ("b", "'You should ensure your badge is visible at all times when entering the building.'", "Second person ('You')"),
                    ("c", "'The facilities committee met on Thursday to consider tenders.'", "Third person ('The committee')")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Executive Annual Address",
                "stem": "Read this excerpt from a healthcare chief executive's staff newsletter:<br><em>'Over the past winter, our dedicated clinical and support teams faced unprecedented pressures with tireless resilience. Each of you demonstrated unwavering commitment to patient dignity, and I am profoundly grateful for your dedication.'</em><br><br>(a) Identify the tone of this passage.<br>(b) Quote two words or phrases that help establish this tone.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify tone: Appreciative, praising, warm, empathetic, respectful", "[R1]"),
                    ("Quote 1: 'tireless resilience' or 'unwavering commitment'", "[R1]"),
                    ("Quote 2: 'profoundly grateful' or 'dedicated clinical and support teams'", "[A1]")
                ],
                "final_answer": "(a) Appreciative / praise-filled / empathetic tone | (b) 'tireless resilience' and 'profoundly grateful'.",
                "reverse_check": "Appropriate tone label backed by exact quotations.",
                "pitfall": "Stating 'happy' or 'good' instead of a precise tone adjective like 'appreciative'."
            }
        ]
    },

    # 8. TEXT TYPES
    "reading-text-types": {
        "title": "Text Types: Informative, Instructive, Persuasive & Descriptive",
        "slug": "reading-text-types",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.13 • L2.13",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The Four Main Functional Text Types",
            "points": [
                "Informative Text: Imparts factual knowledge objectively (news reports, textbooks, encyclopedias).",
                "Instructive Text: Directs the reader to complete a task using imperative (bossy) verbs (recipes, manuals, fire notices).",
                "Persuasive Text: Convinces the reader to take action or adopt a belief (advertisements, campaign letters, reviews).",
                "Descriptive Text: Creates a sensory picture in the reader's mind using vivid adjectives and figurative language."
            ],
            "calc_tip": "Look for imperative verbs (e.g. 'Press', 'Turn', 'Insert') – they instantly reveal an INSTRUCTIVE text!"
        },
        "workout_blocks": [
            {
                "title": "Classifying Text Types",
                "instruction": "Classify each text as Informative, Instructive, Persuasive, or Descriptive:",
                "items": [
                    ("a", "A step-by-step user guide for an automated external defibrillator (AED)", "Instructive"),
                    ("b", "A promotional brochure highlighting why a private dental clinic is the best in the city", "Persuasive"),
                    ("c", "An annual report stating clinical staffing numbers and budget expenditure", "Informative"),
                    ("d", "A vivid account of the morning sunrise over a peaceful rehabilitation garden", "Descriptive"),
                    ("e", "A safety leaflet titled 'How to Report a Needlestick Injury in 4 Easy Steps'", "Instructive")
                ]
            },
            {
                "title": "Spotting Key Linguistic Indicators",
                "instruction": "State which text type typically features these linguistic elements:",
                "items": [
                    ("a", "Imperative verbs, numbered steps, chronological sequence", "Instructive"),
                    ("b", "Rhetorical questions, emotive adjectives, statistics, rule of three", "Persuasive"),
                    ("c", "Neutral passive voice, dates, figures, third-person pronouns", "Informative")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Fire Evacuation Guide Analysis",
                "stem": "Read this excerpt from a facilities booklet:<br><em>'In the event of an alarm, immediately cease work. Direct all visitors towards the nearest green illuminated emergency exit. Do not use passenger lifts. Assemble at Point C in the south car park.'</em><br><br>(a) Identify the primary text type of this excerpt.<br>(b) Give two language features characteristic of this text type present in the excerpt.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify text type: Instructive text", "[R1]"),
                    ("Feature 1: Imperative / command verbs ('cease', 'direct', 'assemble')", "[R1]"),
                    ("Feature 2: Negative commands / prohibitions ('Do not use') and chronological action sequence", "[A1]")
                ],
                "final_answer": "(a) Instructive text | (b) 1. Imperative command verbs ('cease', 'direct'). 2. Clear prohibited action command ('Do not use passenger lifts').",
                "reverse_check": "Identifies text type and cites grammatical features.",
                "pitfall": "Calling it 'Informative' when the sentences are direct orders instructing the reader what to do."
            }
        ]
    },

    # 9. THE EXAM (READING)
    "reading-the-exam": {
        "title": "Reading Exam Strategy & Timing Mastery",
        "slug": "reading-the-exam",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1 & L2 Mark Schemes",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Pearson Edexcel Reading Exam Blueprint",
            "points": [
                "Paper format: Usually 2 or 3 unseen source texts with ~12-15 questions totalling 30-35 marks.",
                "Question types: Retrieval/literal (1 mark), Vocabulary in context (1-2 marks), Organisational features (2 marks), Comparison across texts (3-4 marks).",
                "Rule 1: Always check WHICH text the question refers to (e.g. 'In Text A...', 'In Text B...', or 'In both Text A and Text B').",
                "Rule 2: Don't read the whole text slowly first; read the QUESTIONS first, then skim and scan the texts with a purpose!",
                "Rule 3: Match your points to the marks (a 3-mark question requires 3 distinct points or 2 points with detailed elaboration)."
            ],
            "calc_tip": "If a question gives 3 marks, make sure you write down 3 separate, distinct bullet points!"
        },
        "workout_blocks": [
            {
                "title": "Exam Traps & How to Avoid Them",
                "instruction": "Identify the common error described and how to avoid it:",
                "items": [
                    ("a", "Question says 'According to Text B...', but the candidate quotes from Text A.", "Error: Using wrong source text. Fix: Double underline the text letter in the question prompt."),
                    ("b", "Question asks for 2 reasons, but candidate writes 1 long reason.", "Error: Insufficient points. Fix: Number your responses (1. ... 2. ...)."),
                    ("c", "Question asks 'How does the writer use layout...', but candidate quotes language metaphors.", "Error: Confusing layout with language. Fix: Discuss subheadings, bullets, or fonts, not words.")
                ]
            },
            {
                "title": "Timing Management for 1-Hour Reading Paper",
                "instruction": "Work out the ideal time budget for a 60-minute reading exam:",
                "items": [
                    ("a", "Skimming texts & reading questions", "8 to 10 minutes"),
                    ("b", "Answering short 1-2 mark questions", "25 to 30 minutes"),
                    ("c", "Answering extended comparative questions (3-4 marks)", "15 minutes"),
                    ("d", "Reviewing and checking answers against the texts", "5 minutes")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pearson Edexcel Reading Exam Strategy",
                "stem": "A student attempts a 3-mark question: <em>'Explain three reasons why the author of Text B believes apprenticeships are valuable.'</em><br>The student writes: <em>'The author says apprenticeships are great because you earn money while learning on the job.'</em><br><br>(a) How many marks will this answer receive from the examiner?<br>(b) Rewrite the student's answer to score the maximum <strong>3 marks</strong>.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify current mark: 1 or 2 marks maximum (identifies earning while learning, but only 1 combined point)", "[R1]"),
                    ("Formulate 3 distinct points: 1. Financial earnings while training, 2. Hands-on practical workplace experience, 3. Debt-free qualification route", "[R1]"),
                    ("Present as 3 clear, distinct statements", "[A1]")
                ],
                "final_answer": "(a) 1 mark (only 1 valid reason given) | (b) Maximum mark rewrite: 1. Apprentices earn a wage while studying. 2. They gain direct hands-on workplace experience. 3. They avoid student debt associated with university courses.",
                "reverse_check": "Provides 3 distinct, valid reasons matching mark allocation.",
                "pitfall": "Writing one long sentence that merges multiple ideas without separating them into distinct points."
            }
        ]
    },

    # 10. WHY DO WRITERS WRITE?
    "reading-why-do-writers-write": {
        "title": "The Writer's Purpose & Primary Goal",
        "slug": "reading-why-do-writers-write",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.13 • L2.13",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The PIE Framework for Writer Purpose",
            "points": [
                "P - Persuade: The author wants to influence your opinions, encourage donations, or sell a service.",
                "I - Inform: The author wants to give factual, unbiased information or report findings.",
                "E - Entertain / Express: The author wants to amuse, move, or share personal reflections.",
                "Secondary purposes: To advise, to instruct, to warn, to criticise, or to celebrate.",
                "Look at the medium: A charity website persuades; a community clinic patient leaflet informs/instructs; a satirical blog entertains/criticises."
            ],
            "calc_tip": "When asked for the main purpose, choose the overarching goal of the entire text, not just one paragraph."
        },
        "workout_blocks": [
            {
                "title": "Matching Documents to Core Purpose",
                "instruction": "State whether the primary purpose is to Persuade, Inform, Instruct, or Warn:",
                "items": [
                    ("a", "A leaflet titled 'Protecting Yourself Against Seasonal Influenza'", "Inform / Advise"),
                    ("b", "A petition urging the council to reopen a closed community clinic", "Persuade"),
                    ("c", "A user manual explaining how to calibrate an electronic blood pressure monitor", "Instruct"),
                    ("d", "A high-visibility sign on a biohazard door: 'CAUTION: AUTHORISED ACCESS ONLY'", "Warn")
                ]
            },
            {
                "title": "Recognizing Secondary Intentions",
                "instruction": "State the dual purpose of the text:",
                "items": [
                    ("a", "A dental hygiene blog post that explains flossing benefits while advertising their own brand of eco-friendly floss", "To inform and persuade (commercial marketing)"),
                    ("b", "A staff safety video using humor and cartoons to demonstrate lifting techniques", "To instruct and entertain")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Health Care Campaign Leaflet",
                "stem": "A community healthcare foundation publishes a leaflet titled <strong>'Our Volunteers Make Miracles Happen: Join Us Today'</strong>.<br>The text features stories of lonely patients who found companionship through volunteer visitors, quotes about how rewarding volunteering is, and a large button: <em>'Sign up for our 2-hour weekly companionship scheme'</em>.<br><br>State the main purpose of this leaflet and explain two ways the author attempts to achieve this purpose.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("State primary purpose: To persuade readers to sign up as volunteer companions", "[R1]"),
                    ("Method 1: Uses emotional case studies / human stories showing the positive impact on lonely patients", "[R1]"),
                    ("Method 2: Emphasizes the personal emotional reward for volunteers paired with an easy call-to-action button", "[A1]")
                ],
                "final_answer": "Main purpose: To persuade members of the public to volunteer. Methods: 1. Uses emotive real-life anecdotes illustrating the relief brought to isolated patients. 2. Lowers barriers to entry with an accessible call to action ('2-hour weekly scheme').",
                "reverse_check": "Identifies purpose and provides 2 methods of execution.",
                "pitfall": "Saying 'To inform people about volunteers' when the clear goal is recruitment."
            }
        ]
    },

    # 11. ASSESSING THE BASICS
    "assessing-the-basics": {
        "title": "Assessing the Basics: Core Reading Comprehension",
        "slug": "assessing-the-basics",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading E3.8 • L1.11",
        "level": "Level 1",
        "method_card": {
            "title": "Skimming, Scanning & Retrieval Foundations",
            "points": [
                "Skimming: Reading quickly over headlines, subheadings, and first sentences to grasp the general gist.",
                "Scanning: Moving your eyes rapidly across the text looking for specific keywords, names, numbers, or dates.",
                "Keywords: Identify the 2-3 most important words in the question before scanning the passage.",
                "Fact retrieval: Once your eye locates the keyword, read the full sentence carefully to extract the precise fact."
            ],
            "calc_tip": "Run your finger or a pen smoothly down the page while scanning to keep your focus sharp."
        },
        "workout_blocks": [
            {
                "title": "Keyword Scanning Drills",
                "instruction": "Identify the best keyword to scan for in the text:",
                "items": [
                    ("a", "Question: 'What time does the emergency evening clinic close?'", "Scan for: 'close', 'closing', times (e.g. 'pm', '20:00')"),
                    ("b", "Question: 'How much does a replacement staff security pass cost?'", "Scan for: '£', 'cost', 'fee', 'security pass'"),
                    ("c", "Question: 'Who is the lead clinical nurse in charge of Ward 4?'", "Scan for: 'Ward 4', 'Lead nurse', capitalised names"),
                    ("d", "Question: 'On what date was the hygiene audit completed?'", "Scan for: dates, months, 'audit'")
                ]
            },
            {
                "title": "True or False Retrieval",
                "instruction": "State whether the statement is True or False based on: 'Visiting hours are strictly 14:00 to 19:00 daily, with a maximum of two visitors per bed.'",
                "items": [
                    ("a", "Visitors can arrive at 11:00am.", "False (visiting starts at 14:00)"),
                    ("b", "Three visitors can stand together around one bed.", "False (maximum of two)"),
                    ("c", "Visiting is permitted on Sundays.", "True ('daily' includes weekends)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Workplace Health & Safety First Aid Notice",
                "stem": "Text: <em>'The designated first aid coordinator for the ground floor maintenance workshop is Mark Davies (Ext 402). First aid boxes are located beside the fire exit in Workshop 2 and behind the main reception desk. In the event of a serious chemical spill, immediately dial 2222.'</em><br><br>According to the text:<br>(a) Who is the first aid coordinator?<br>(b) Where are the two first aid boxes located?<br>(c) What internal telephone number must be dialed for a chemical spill?",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Scan for coordinator name: Mark Davies", "[R1]"),
                    ("Scan for box locations: Workshop 2 (beside fire exit) AND behind main reception desk", "[R1]"),
                    ("Scan for emergency number: 2222", "[A1]")
                ],
                "final_answer": "(a) Mark Davies | (b) Beside the fire exit in Workshop 2 and behind main reception desk | (c) 2222",
                "reverse_check": "Direct literal retrieval from source text.",
                "pitfall": "Listing only one first aid box location when the text specifies two."
            }
        ]
    },

    # 12. COMMON MISTAKES
    "common-mistakes": {
        "title": "Common Exam Traps & Pitfalls in Reading",
        "slug": "common-mistakes",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1 & L2 Examiner Reports",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The Top 4 Examiner Pitfalls to Avoid",
            "points": [
                "Pitfall 1: Copying huge chunks of text instead of answering the specific question. Keep quotes focused and concise!",
                "Pitfall 2: Relying on personal outside knowledge rather than what is actually written in the source text.",
                "Pitfall 3: Answering from Text A when the question specifies Text B.",
                "Pitfall 4: Confusing Language Features (metaphor, alliteration, adjectives) with Layout Features (bullet points, subheadings, text boxes)."
            ],
            "calc_tip": "If a question asks 'According to Text A...', do NOT write what you know from personal life; write what the author says!"
        },
        "workout_blocks": [
            {
                "title": "Language vs Layout Features",
                "instruction": "State whether each item is a Language Feature or a Layout Feature:",
                "items": [
                    ("a", "Bullet points", "Layout feature"),
                    ("b", "Rhetorical question", "Language feature"),
                    ("c", "Subheading", "Layout feature"),
                    ("d", "Alliteration", "Language feature"),
                    ("e", "Bold font", "Layout feature"),
                    ("f", "Emotive language", "Language feature"),
                    ("g", "Text box / callout", "Layout feature"),
                    ("h", "Rule of three", "Language feature")
                ]
            },
            {
                "title": "Avoiding Outside Knowledge Traps",
                "instruction": "State which answer is valid based on: 'Text says: Eating kiwi fruit before bed helps sleep due to serotonin.'",
                "items": [
                    ("a", "Candidate A: 'Kiwi fruit helps sleep because it contains serotonin.'", "Valid (derived directly from text)"),
                    ("b", "Candidate B: 'Drinking warm milk helps sleep because my grandmother told me so.'", "Invalid (outside personal knowledge)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Examiner Diagnostic Marking Exercise",
                "stem": "Exam Question: <em>'Identify two organisational features used in Text A to present information clearly.'</em><br><br>Candidate Answer: <em>'The author uses powerful adjectives and writes in a formal tone to persuade us.'</em><br><br>Explain why the candidate received <strong>0 marks</strong> for this response and write a correct model answer.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify why 0 marks awarded: Candidate identified language/tone features instead of organisational/layout features", "[R1]"),
                    ("Provide valid organisational features: Subheadings, bullet points, text boxes, tables, bold text", "[A1]")
                ],
                "final_answer": "Reason for 0 marks: The candidate identified language/tone features ('powerful adjectives', 'formal tone') instead of organisational layout features. Correct model answer: '1. Clear subheadings dividing topics. 2. Bullet points presenting instructions.'",
                "reverse_check": "Identifies error diagnostic and provides valid model response.",
                "pitfall": "Repeating language features in the model answer."
            }
        ]
    },

    # 13. DETECTING LANGUAGE TECHNIQUES
    "detecting-language-techniques": {
        "title": "Language Techniques & Rhetorical Devices",
        "slug": "detecting-language-techniques",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.13 • L2.15",
        "level": "Level 2",
        "method_card": {
            "title": "Rhetorical Devices & Figurative Language",
            "points": [
                "Metaphor: Describing something as if it WERE something else (e.g. 'The hospital was a war zone').",
                "Simile: Comparing two things using 'like' or 'as' (e.g. 'He was as sharp as a scalpel').",
                "Hyperbole: Deliberate dramatic exaggeration for emphasis (e.g. 'I've waited a million years for this result').",
                "Alliteration: Repetition of initial consonant sounds (e.g. 'Careful, compassionate care').",
                "Rhetorical Question: A question asked to provoke thought rather than require an answer."
            ],
            "calc_tip": "When explaining a language technique: Name the technique → Quote the words → Explain the effect on the reader."
        },
        "workout_blocks": [
            {
                "title": "Identifying Rhetorical Devices",
                "instruction": "Name the language technique used in each sentence:",
                "items": [
                    ("a", "'The waiting room was a bustling beehive of frantic activity.'", "Metaphor"),
                    ("b", "'The medication worked like magic on the patient's joint inflammation.'", "Simile ('like magic')"),
                    ("c", "'We have reminded staff a thousand times about password security.'", "Hyperbole (exaggeration)"),
                    ("d", "'Safe, swift, and supportive healthcare solutions.'", "Alliteration (repetition of 's')"),
                    ("e", "'Is it acceptable for vulnerable individuals to suffer in silence?'", "Rhetorical question")
                ]
            },
            {
                "title": "Explaining the Effect on the Reader",
                "instruction": "Explain what feeling or thought the phrase creates in the reader:",
                "items": [
                    ("a", "Describing an administrative system as 'creaking at the seams'", "Creates an image of an outdated system on the verge of collapsing under strain"),
                    ("b", "Calling a new community clinic 'a beacon of hope'", "Inspires optimism and trust that the clinic will provide guidance and care")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Foundation Campaign Analysis",
                "stem": "An excerpt from a medical charity campaign reads:<br><em>'Our emergency air ambulance is a lifeline cutting through the clouds to reach rural communities when every second counts.'</em><br><br>(a) Identify the language technique in the phrase <em>'a lifeline cutting through the clouds'</em>.<br>(b) Explain the effect of this phrase on the reader.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify technique: Metaphor (comparing the ambulance service directly to a lifeline)", "[R1]"),
                    ("Explain reader effect: Conveys the vital, life-saving urgency and dramatic speed of the service, evoking admiration and support", "[A1]")
                ],
                "final_answer": "(a) Metaphor | (b) It powerfully emphasizes that the air ambulance is essential for survival in remote areas, evoking appreciation and prompting donations.",
                "reverse_check": "Identifies metaphor and explains emotional/persuasive impact.",
                "pitfall": "Calling it a simile (it does not use 'like' or 'as')."
            }
        ]
    },

    # 14. FORMALITY AND BIAS
    "formality-and-bias": {
        "title": "Register, Formality & Detecting Bias",
        "slug": "formality-and-bias",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.15 • L2.16",
        "level": "Level 2",
        "method_card": {
            "title": "Levels of Formality & Subjectivity",
            "points": [
                "Formal register: Impersonal passive voice, complex sentence structures, no slang/contractions, objective tone.",
                "Informal register: Slang, idioms, contractions (can't, won't), exclamation marks, direct colloquial address.",
                "Detecting bias: Ask whether the author presents only positive aspects of their view while ignoring opposing facts.",
                "Subjective language: Expresses personal feelings, beliefs, or interpretations ('I feel', 'in my opinion', 'shocking').",
                "Objective language: Based on verifiable, measurable facts and evidence without emotional distortion."
            ],
            "calc_tip": "If a text only uses positive adjectives for one option and negative adjectives for the other, it is BIASED!"
        },
        "workout_blocks": [
            {
                "title": "Formal vs Informal Language Pairs",
                "instruction": "Classify each sentence as Formal or Informal:",
                "items": [
                    ("a", "'We are writing to notify you that your clinical consultation has been rescheduled.'", "Formal"),
                    ("b", "'Just a heads-up that your doc appointment got moved to next week!'", "Informal"),
                    ("c", "'All visitors must sanitise their hands upon entering the facility.'", "Formal"),
                    ("d", "'Don't forget to wash your hands or you'll catch something nasty.'", "Informal")
                ]
            },
            {
                "title": "Objective vs Subjective Statements",
                "instruction": "State whether the statement is Objective (fact-based) or Subjective (opinion-based):",
                "items": [
                    ("a", "The hospital operates 42 acute care beds.", "Objective (verifiable fact)"),
                    ("b", "The hospital provides the most wonderful care in the entire country.", "Subjective (opinion / value judgment)"),
                    ("c", "Wait times increased by an average of 14 minutes in December.", "Objective"),
                    ("d", "December was a thoroughly dreadful month for everyone on duty.", "Subjective")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Product Promotion vs Clinical Review",
                "stem": "Text A (Manufacturer Website): <em>'Our revolutionary herbal supplement guarantees 100% stress relief within 24 hours. Don't waste your time with ordinary medicines – choose nature's miracle!'</em><br>Text B (Medical Journal): <em>'A randomized controlled trial of 150 participants found modest stress reduction in 18% of subjects, with researchers noting a strong placebo effect.'</em><br><br>Compare the formality and bias in Text A and Text B.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Text A analysis: Highly informal/promotional register with extreme commercial bias (unsubstantiated claims 'guarantees 100%', emotive loaded words 'miracle')", "[R1]"),
                    ("Text B analysis: Formal academic register, objective and unbiased (reports empirical numbers and notes limitations)", "[R1]"),
                    ("Synthesise direct comparison of tone and reliability", "[A1]")
                ],
                "final_answer": "Text A uses an informal, highly biased promotional register with sensationalist claims ('miracle', 'guarantees 100%') to sell a product. In contrast, Text B is written in a formal, objective, and unbiased register, using empirical statistics and neutral clinical vocabulary.",
                "reverse_check": "Compares formality and bias across both texts with textual evidence.",
                "pitfall": "Stating which text you personally believe without analyzing language, formality, and bias."
            }
        ]
    },

    # 15. PIECING IT TOGETHER - COMPARING TEXTS
    "piecing-it-together-comparing-texts": {
        "title": "Synthesising & Contrasting Multiple Sources",
        "slug": "piecing-it-together-comparing-texts",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.11 • L2.12",
        "level": "Level 2",
        "method_card": {
            "title": "Cross-Text Synthesis Strategy",
            "points": [
                "Find points of similarity: Both writers agree that X is important...",
                "Find points of divergence: However, Writer A suggests Y, whereas Writer B advocates Z...",
                "Compare presentation: Writer A uses a formal report layout with tables, while Writer B uses a personal blog with informal anecdotes.",
                "Use balanced comparative language: 'In comparison', 'Whereas', 'On the contrary', 'Both texts demonstrate...'"
            ],
            "calc_tip": "Structure your comparison paragraph using point-by-point synthesis rather than writing two separate unconnected blocks."
        },
        "workout_blocks": [
            {
                "title": "Comparative Connectives Practice",
                "instruction": "Fill in the connective that best highlights the comparison (Both, Conversely, In contrast, Similarly):",
                "items": [
                    ("a", "(Both / Conversely) authors agree that regular physical exercise improves cardiovascular health.", "Both"),
                    ("b", "Text A supports a mandatory sugar tax. (In contrast / Similarly), Text B argues for voluntary industry reform.", "In contrast"),
                    ("c", "Text 1 warns of cyber threats; (similarly / conversely), Text 2 highlights data protection vulnerabilities.", "similarly"),
                    ("d", "Author X writes from personal experience. Author Y, (conversely / likewise), relies strictly on statistical surveys.", "conversely")
                ]
            },
            {
                "title": "Matching Contrasting Arguments",
                "instruction": "Pair the argument in Text 1 with its direct counter-argument in Text 2:",
                "items": [
                    ("a", "Text 1: 'Automated check-in kiosks save money and reduce reception queues.'", "Text 2: 'Kiosks confuse elderly patients and eliminate valuable personal human contact.'"),
                    ("b", "Text 1: '12-hour shifts give staff longer blocks of consecutive rest days.'", "Text 2: '12-hour shifts lead to acute cognitive fatigue and increased medical errors towards the end of shifts.'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Shift Scheduling Comparison",
                "stem": "Text 1 argues: <em>'A 4-day working week of 10-hour days provides staff with three full rest days, drastically lowering burn-out and childcare costs.'</em><br>Text 2 argues: <em>'Longer daily working hours compromise focus during critical evening handovers, increasing the likelihood of medication errors.'</em><br><br>Summarize one similarity and one difference between the arguments presented in Text 1 and Text 2.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Similarity: Both texts examine the impact of compressed working hours on healthcare staff and shift patterns", "[R1]"),
                    ("Difference: Text 1 focuses on personal benefits (burn-out reduction, childcare savings), whereas Text 2 warns of patient safety risks (fatigue, medication errors)", "[A1]")
                ],
                "final_answer": "Similarity: Both texts evaluate the consequences of longer, compressed daily shifts. Difference: Text 1 emphasizes employee wellbeing and reduced childcare expenses, whereas Text 2 highlights clinical safety risks and increased errors from fatigue.",
                "reverse_check": "Identifies 1 clear similarity and 1 clear difference.",
                "pitfall": "Giving two differences and forgetting to identify a similarity."
            }
        ]
    },

    # 16. PIECING IT TOGETHER - KEY AND DETAILED POINTS
    "piecing-it-together-key-and-detailed-points": {
        "title": "Extracting Key Points & Supporting Details",
        "slug": "piecing-it-together-key-and-detailed-points",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L1.12 • L2.11",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Main Ideas vs Supporting Evidence",
            "points": [
                "Main (Key) Point: The overarching core message or thesis of a paragraph (often stated in the first 'topic sentence').",
                "Supporting Details: Specific examples, statistics, case studies, or anecdotes that prove or elaborate on the main point.",
                "Summarising: Condensing a text by extracting only the key points while discarding minor supporting details.",
                "Don't confuse an example with the main point! E.g. 'Dr Patel treated 4 patients' is an example supporting the main point that 'staffing was tight'."
            ],
            "calc_tip": "Ask: 'If I could only keep ONE sentence from this paragraph, which one carries the central meaning?'"
        },
        "workout_blocks": [
            {
                "title": "Distinguishing Main Ideas from Supporting Details",
                "instruction": "State whether the statement is a Main Idea or a Supporting Detail:",
                "items": [
                    ("a", "'Good hand hygiene is the single most effective way to stop hospital infections.'", "Main Idea"),
                    ("b", "'Studies show washing with soap for 20 seconds eliminates 99% of surface germs.'", "Supporting Detail (statistic/evidence)"),
                    ("c", "'Transitioning to digital patient records improves clinical efficiency.'", "Main Idea"),
                    ("d", "'For instance, Dr Jenkins retrieved blood test results in 12 seconds.'", "Supporting Detail (anecdote/example)")
                ]
            },
            {
                "title": "Writing a 1-Sentence Summary",
                "instruction": "Extract the key point from this paragraph in one sentence: 'Rising energy prices, increased pharmaceutical shipping tariffs, and inflation have forced clinics across the region to audit administrative overheads.'",
                "items": [
                    ("a", "Core summary sentence", "Economic pressures and rising costs are forcing regional clinics to reduce administrative spending.")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Facility Waste Management Report",
                "stem": "Read this paragraph from a hospital environmental audit:<br><em>'Improper waste segregation remains our largest environmental challenge. In October alone, over 400 kg of harmless packaging was mistakenly placed into expensive hazardous incinerator bins, costing the trust an unnecessary £1,800. Furthermore, non-hazardous plastics in clinical bins prevent recycling compliance.'</em><br><br>(a) State the main key point of the paragraph.<br>(b) Identify two supporting details used by the author to back up this point.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Main key point: Improper waste sorting/segregation is causing major environmental and financial problems", "[R1]"),
                    ("Supporting detail 1: 400 kg of harmless packaging placed in hazardous bins in October", "[R1]"),
                    ("Supporting detail 2: £1,800 in unnecessary incineration costs / plastics preventing recycling", "[A1]")
                ],
                "final_answer": "(a) Main point: Poor waste segregation is creating significant environmental and financial issues for the facility. (b) Supporting details: 1. 400 kg of harmless packaging misallocated in October. 2. Resulting in £1,800 in unnecessary disposal expenditure.",
                "reverse_check": "Distinguishes overarching claim from specific empirical evidence.",
                "pitfall": "Quoting the £1,800 cost as the main point rather than a supporting detail."
            }
        ]
    },

    # 17. TYPES OF AND NAVIGATING SOURCES
    "types-of-and-navigating-sources": {
        "title": "Evaluating Sources, Reliability & Navigation",
        "slug": "types-of-and-navigating-sources",
        "subject": "English Reading",
        "spec_codes": "Pearson Edexcel English: Reading L2.17 • L2.18",
        "level": "Level 2",
        "method_card": {
            "title": "The CRAAP Test for Evaluating Sources",
            "points": [
                "Currency: When was the information published or last updated? Is it out of date?",
                "Relevance: Does the information directly relate to your research question?",
                "Authority: Who is the author or publisher? Are they accredited experts or an anonymous forum user?",
                "Accuracy: Is the content backed by evidence, citations, and peer review?",
                "Purpose: Is the goal to inform objectively, or to sell a product / push a partisan agenda?"
            ],
            "calc_tip": "Government (.gov.uk), educational (.ac.uk), and accredited healthcare bodies (statutory registries / medical colleges) are high-authority sources."
        },
        "workout_blocks": [
            {
                "title": "Assessing Source Reliability",
                "instruction": "State whether the source has High, Medium, or Low reliability for medical research:",
                "items": [
                    ("a", "A peer-reviewed study in the British Medical Journal (BMJ)", "High reliability (peer-reviewed, accredited)"),
                    ("b", "An anonymous post on a social media wellness forum", "Low reliability (unverified, potential misinformation)"),
                    ("c", "A blog post by a vitamin company selling dietary supplements", "Low/Medium reliability (commercial bias)"),
                    ("d", "Official clinical guidance published on a national public health portal", "High reliability (accredited public agency)")
                ]
            },
            {
                "title": "Web Navigation Features",
                "instruction": "State which web navigation feature allows the user to perform the task:",
                "items": [
                    ("a", "Find all pages mentioning 'phlebotomy'", "Search bar"),
                    ("b", "Trace back the path from a subpage to the home page (Home > Services > Blood Clinic)", "Breadcrumb trail"),
                    ("c", "Quickly jump to the 'Complaints Policy' from any page", "Footer menu / Global navigation bar"),
                    ("d", "Jump down directly to Section 4 within a long 10-page document", "Table of contents hyperlinks")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Information Sourcing Evaluation",
                "stem": "A trainee care assistant needs to research current statutory regulations on storing controlled medications in a care home.<br>They find two sources online:<br>• <strong>Source 1:</strong> An unreferenced opinion article on a personal blog written in 2017 titled <em>'Why I think medicine cupboards are too restrictive'</em>.<br>• <strong>Source 2:</strong> A 2026 guidance document from the national healthcare regulatory commission titled <em>'Safe Storage of Controlled Drugs in Residential Care'</em>.<br><br>Explain two reasons why Source 2 is more reliable and suitable for workplace use than Source 1.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Reason 1: Authority and accreditation: Source 2 is published by an official regulatory commission, whereas Source 1 is a personal blog", "[R1]"),
                    ("Reason 2: Currency and objectivity: Source 2 is recent (2026) and provides statutory guidance, whereas Source 1 is outdated (2017) and expresses subjective opinion", "[A1]")
                ],
                "final_answer": "1. Authority: Source 2 is produced by the official national regulator responsible for enforcing legal standards, whereas Source 1 is an unverified personal blog. 2. Currency: Source 2 is up to date (2026), ensuring compliance with current law, whereas Source 1 is nearly a decade old.",
                "reverse_check": "Compares authority and currency using CRAAP criteria.",
                "pitfall": "Merely stating 'Source 2 is better' without giving concrete reasons."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(ENGLISH_READING_BATCH3_WORKOUTS)} topics in authentic_workouts_english_reading_batch3.py")
