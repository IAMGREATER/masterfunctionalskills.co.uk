#!/usr/bin/env python3
"""
Authentic Fluency Workouts: English Speaking, Listening & Communication (SLC) Batch 3
10 Curriculum Topics:
1. slc-key-slc-skills
2. slc-adapting
3. slc-communicating
4. slc-extracting-information
5. slc-language-in-context
6. slc-line-of-argument-and-narratives
7. slc-responding
8. slc-the-exam
9. slc-using-evidence
10. slc-your-turn
"""

ENGLISH_SLC_BATCH3_WORKOUTS = {
    # 1. KEY SLC SKILLS
    "slc-key-slc-skills": {
        "title": "Core Speaking, Listening & Communication Skills",
        "slug": "slc-key-slc-skills",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.1 • L1.2 • L2.1 • L2.2",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The Pillars of Effective Spoken Communication",
            "points": [
                "Active Listening: Nodding, maintaining eye contact, taking brief notes, and asking relevant follow-up questions.",
                "Turn-taking: Respecting conversational boundaries without speaking over others or interrupting.",
                "Non-verbal communication: Open posture, appropriate facial expressions, and natural hand gestures.",
                "Clarity & Projection: Speaking at a measured pace with clear articulation and audible volume.",
                "Encouraging others: Inviting quieter participants to share their views ('What are your thoughts on this, James?')."
            ],
            "calc_tip": "In an SLC discussion, aim to speak 3-4 times with substantial contributions rather than dominating the conversation."
        },
        "workout_blocks": [
            {
                "title": "Identifying Active vs Passive Listening",
                "instruction": "State whether the behavior demonstrates Active Listening, Passive Listening, or Disruptive Behavior:",
                "items": [
                    ("a", "Nodding and summarizing: 'So if I understand correctly, your main concern is night shift staffing?'", "Active Listening"),
                    ("b", "Looking down at a mobile phone while a colleague presents budget proposals", "Disruptive / Disengaged"),
                    ("c", "Interrupting mid-sentence: 'No you're wrong, let me speak!'", "Disruptive"),
                    ("d", "Maintaining eye contact and asking: 'Could you give an example of how that software works?'", "Active Listening"),
                    ("e", "Sitting silently without making notes or asking questions for 30 minutes", "Passive Listening")
                ]
            },
            {
                "title": "Turn-Taking and Facilitation Phrases",
                "instruction": "Select the phrase best suited for the conversational goal:",
                "items": [
                    ("a", "Bringing a quieter team member into the discussion", "'Sarah, you've had extensive experience with this equipment – how do you see it?'"),
                    ("b", "Politely disagreeing with a colleague", "'I see your point about cost, however, have we considered the long-term safety implications?'"),
                    ("c", "Steering a derailed conversation back to the agenda", "'That's an interesting point, but could we return to our main agenda item regarding the clinic rota?'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinical Shift Handover Discussion",
                "stem": "During a multidisciplinary shift handover, two team members begin arguing over weekend on-call coverage, talking over each other and raising their voices.<br><br>Describe three specific verbal and non-verbal techniques you would use as shift lead to de-escalate the tension, restore professional turn-taking, and ensure all viewpoints are heard.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Technique 1 (Verbal intervention): Use a calm, measured tone to intervene and re-establish meeting ground rules ('Let's pause for a moment so we can hear both perspectives clearly')", "[S1]"),
                    ("Technique 2 (Structured turn-taking): Allocate dedicated time to each speaker in turn ('Marcus, please finish your point, then we will hear Maria's response without interruptions')", "[S1]"),
                    ("Technique 3 (Active summarising): Summarize common ground and focus on collaborative solutions", "[A1]")
                ],
                "final_answer": "1. Intervene calmly with neutral boundary-setting language. 2. Establish structured turn-taking giving each speaker equal uninterrupted time. 3. Summarise key concerns on both sides to refocus on patient safety and fair rota distribution.",
                "reverse_check": "Realistic, constructive communication management.",
                "pitfall": "Taking sides or shouting over the participants."
            }
        ]
    },

    # 2. ADAPTING
    "slc-adapting": {
        "title": "Adapting Spoken Language to Audience & Context",
        "slug": "slc-adapting",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.3 • L2.3",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Code-Switching & Spoken Registers",
            "points": [
                "Code-Switching: Adapting vocabulary, pace, and sentence complexity depending on who you are speaking to.",
                "Speaking to senior managers/inspectors: Formal Standard English, professional terminology, polite framing, objective tone.",
                "Speaking to patients/service users: Plain English, empathetic tone, avoiding confusing medical jargon, reassuring manner.",
                "Speaking to close peers/colleagues: Collaborative semi-formal register, direct and supportive.",
                "Non-verbal adaptation: Respect personal space, adapt eye contact to cultural sensitivity, use open posture."
            ],
            "calc_tip": "If explaining a medical or technical term to a member of the public, always follow up with a plain-English analogy."
        },
        "workout_blocks": [
            {
                "title": "Selecting the Appropriate Spoken Register",
                "instruction": "Choose the most appropriate phrasing for the given audience:",
                "items": [
                    ("a", "Explaining an injection to an anxious patient", "'This is a small injection in your upper arm that helps protect your lungs; you might feel a brief scratch.' (reassuring, plain English)"),
                    ("b", "Reporting an equipment fault to a senior biomedical engineer", "'The primary transducer on unit 4 is giving intermittent pressure readings outside calibrated tolerance.' (precise technical register)"),
                    ("c", "Asking a manager for leave approval", "'Could we discuss the possibility of taking two days annual leave next month?' (polite, professional)")
                ]
            },
            {
                "title": "Jargon Busting for Patients",
                "instruction": "Translate the clinical jargon into clear, accessible plain English:",
                "items": [
                    ("a", "'NPO / Nil by mouth'", "'Please do not eat or drink anything before your procedure'"),
                    ("b", "'Hypertension'", "'High blood pressure'"),
                    ("c", "'Analgesic'", "'Painkiller / pain relief medication'"),
                    ("d", "'Edema'", "'Swelling caused by fluid build-up'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Patient Consultation Communication",
                "stem": "A junior healthcare assistant says to an elderly, anxious patient awaiting minor surgery:<br><em>'You're scheduled for a subcutaneous excision under local anesthesia, so we need to ensure haemostasis and check your baseline vitals before ambulatory discharge.'</em><br><br>Explain why this communication is ineffective, and rewrite the explanation in clear, reassuring plain English suitable for the patient.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify why ineffective: Overloaded with dense clinical jargon ('subcutaneous excision', 'haemostasis', 'ambulatory discharge') that causes unnecessary anxiety and confusion", "[S1]"),
                    ("Draft plain English rewrite: Translate procedures into everyday terms (minor procedure, numbing medicine, checking blood pressure, going home today)", "[S1]"),
                    ("Ensure warm, reassuring, empathetic tone", "[A1]")
                ],
                "final_answer": "The original phrasing causes fear through alienating clinical jargon. Plain English rewrite: 'Today the doctor will carry out a minor procedure to remove the small lump on your arm. We will numb the area completely so you won't feel pain. Before you head home later today, we'll check your blood pressure and ensure you're resting comfortably.'",
                "reverse_check": "Eliminates jargon, maintains accurate medical facts, reassures patient.",
                "pitfall": "Leaving medical terms like 'ambulatory discharge' unexplained."
            }
        ]
    },

    # 3. COMMUNICATING (SLC)
    "slc-communicating": {
        "title": "Verbal Precision, Pitch, Pace & Modulation",
        "slug": "slc-communicating",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.4 • L2.4",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Vocal Delivery: Pitch, Pace, Pauses & Tone",
            "points": [
                "Pace: Speak at 130-150 words per minute; rushing conveys nervousness or dismissiveness, while speaking too slowly loses attention.",
                "Pauses: Use strategic 1-2 second pauses before key points or after asking a question to allow listeners to process information.",
                "Pitch & Intonation: Avoid monotone delivery; modulate pitch naturally to emphasize crucial points and convey genuine interest.",
                "Volume & Projection: Breathe from the diaphragm to project clearly across the room without shouting.",
                "Eliminate vocal fillers: Replace repeated 'um', 'er', 'like', 'you know' with silent, deliberate pauses."
            ],
            "calc_tip": "When you feel the urge to say 'um', simply close your lips and take a silent breath instead."
        },
        "workout_blocks": [
            {
                "title": "Vocal Mechanics Diagnostics",
                "instruction": "State the delivery technique needed to resolve the communication issue:",
                "items": [
                    ("a", "The speaker talks so fast that listeners cannot take notes", "Slow down pace and introduce pauses between key facts"),
                    ("b", "The speaker speaks in an unvarying, flat robotic voice", "Modulate intonation and pitch to emphasize key words"),
                    ("c", "The speaker's voice fades away at the end of sentences", "Maintain breath support and project through to sentence endings"),
                    ("d", "The speaker fills every silence with 'um, like, yeah'", "Use purposeful silent pauses instead of verbal fillers")
                ]
            },
            {
                "title": "Emphasizing Key Words (Intonation Shifts)",
                "instruction": "Explain how shifting stress changes the meaning of: 'I didn't say she stole the medicine':",
                "items": [
                    ("a", "Stress on '<u>I</u>'", "Someone else said it, not me"),
                    ("b", "Stress on '<u>she</u>'", "Someone stole it, but not that specific woman"),
                    ("c", "Stress on '<u>stole</u>'", "She took it, but maybe borrowed it or had permission")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Emergency Ward Tannoy Announcement",
                "stem": "A facilities security officer must broadcast an urgent public announcement over a busy clinic's public address (PA) system regarding a temporary evacuation of the ground floor due to a minor electrical hazard.<br><br>Describe three vocal delivery techniques the officer should apply to ensure the message is understood immediately without inciting panic.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Pace and pauses: Speak at a calm, deliberate pace, pausing between sentences so acoustics don't echo or blur words", "[S1]"),
                    ("Tone and pitch: Maintain a steady, reassuring, authoritative tone (avoiding high-pitched frantic inflection)", "[S1]"),
                    ("Clarity and repetition: Articulate consonants clearly and repeat key instructions (exit door, assembly point)", "[A1]")
                ],
                "final_answer": "1. Calm, measured pace with distinct pauses to prevent acoustic reverb. 2. Steady, authoritative intonation projecting control and preventing alarm. 3. Clear articulation with verbatim repetition of the specific exit and assembly location.",
                "reverse_check": "Combines pace, tone, and projection for high-stakes communication.",
                "pitfall": "Focusing only on the words and ignoring vocal delivery (speed, volume, tone)."
            }
        ]
    },

    # 4. EXTRACTING INFORMATION
    "slc-extracting-information": {
        "title": "Listening for Detail & Note-Taking in Discussions",
        "slug": "slc-extracting-information",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.1 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Strategic Listening & Note-Taking Methods",
            "points": [
                "Listen for signpost words: 'The critical priority is...', 'In summary...', 'Firstly, secondly...', 'However...'",
                "Extract facts over fluff: Record names, figures, deadlines, assigned tasks, and agreed action points.",
                "Shorthand & Bullet notes: Don't write full sentences; use abbreviations (e.g. w/o = without, approx = approximately, min = minutes).",
                "Confirm understanding: Paraphrase key takeaways back to the speaker ('Just to confirm, we are aiming to finish the audit by Friday 4pm?')."
            ],
            "calc_tip": "Divide your note sheet into two columns: Left = Key Ideas / Facts, Right = My Questions / Follow-ups."
        },
        "workout_blocks": [
            {
                "title": "Spotting Signpost Words in Speech",
                "instruction": "State what the spoken signpost indicates (Key priority, Contrast, or Conclusion):",
                "items": [
                    ("a", "'Above all else, patient safety must come first...'", "Key priority / core emphasis"),
                    ("b", "'On the other hand, we must remember our budget constraints...'", "Contrast / counter-argument"),
                    ("c", "'To wrap up our findings today...'", "Conclusion / summary"),
                    ("d", "'The crucial takeaway from this audit is...'", "Key priority")
                ]
            },
            {
                "title": "Extracting Action Items from Spoken Dialogue",
                "instruction": "Extract the specific action, person responsible, and deadline from: 'Marcus, could you ensure the medicine cabinets are audited and re-stocked before the Friday 17:00 handover?'",
                "items": [
                    ("a", "Person responsible", "Marcus"),
                    ("b", "Action required", "Audit and re-stock medicine cabinets"),
                    ("c", "Deadline", "Friday by 17:00 (5:00pm) handover")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Multidisciplinary Team Meeting Minutes",
                "stem": "Listen to this spoken briefing from a clinical lead:<br><em>'Team, our main goal for Q4 is reducing medication dispensing errors. Dr Evans will review the digital prescribing software by November 15th, while Sister Kelly will deliver refresher numeracy training for all band 5 staff across three workshops in early December. We will review progress at our January meeting.'</em><br><br>Produce a concise 3-bullet point action summary capturing all delegated tasks, leads, and deadlines.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Task 1 extraction: Dr Evans – Review digital prescribing software by November 15th", "[S1]"),
                    ("Task 2 extraction: Sister Kelly – Conduct Band 5 numeracy refresher workshops (3 sessions) in early December", "[S1]"),
                    ("Task 3 extraction: Whole Team – Progress review at January meeting (overall goal: reduce dispensing errors)", "[A1]")
                ],
                "final_answer": "• Dr Evans: Complete digital prescribing software review by November 15th.\n• Sister Kelly: Deliver 3 Band 5 numeracy refresher training workshops in early December.\n• Team Review: Full progress evaluation scheduled for January team meeting.",
                "reverse_check": "Accurately captures all 3 actions, people, and deadlines.",
                "pitfall": "Missing the deadlines or confusing Dr Evans' and Sister Kelly's responsibilities."
            }
        ]
    },

    # 5. LANGUAGE IN CONTEXT
    "slc-language-in-context": {
        "title": "Spoken Formality, Colloquialisms & Professional Tone",
        "slug": "slc-language-in-context",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.3 • L2.3",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Professionalism vs Slang in Spoken Interactions",
            "points": [
                "Standard English in exams: Avoid fillers ('innit', 'like', 'you get me', 'gonna', 'wanna') during official presentations and formal discussions.",
                "Colloquialisms vs Technical precision: Say 'experienced breathing difficulty' rather than 'was out of puff'.",
                "Polite questioning: Use modal verbs for courteous inquiry ('Could you clarify...', 'Would you mind explaining...').",
                "Constructive criticism: Focus on the issue, not the person ('The current process seems inefficient' rather than 'You are being lazy')."
            ],
            "calc_tip": "In the SLC exam, the assessor specifically marks your ability to maintain consistent Standard English."
        },
        "workout_blocks": [
            {
                "title": "Upgrading Informal Spoken Phrases",
                "instruction": "Replace the informal colloquialism with a professional equivalent:",
                "items": [
                    ("a", "'He was totally stressing out'", "'He was experiencing significant anxiety / distress'"),
                    ("b", "'The machine packed in'", "'The diagnostic equipment malfunctioned / failed'"),
                    ("c", "'I reckon that's rubbish'", "'I hold a different perspective on that issue'"),
                    ("d", "'Give us a hand with this'", "'Could you assist me with this task, please?'")
                ]
            },
            {
                "title": "Constructive Professional Phrasing",
                "instruction": "Select the professional, non-confrontational response:",
                "items": [
                    ("a", "Challenging an unfeasible project deadline", "'Given our current staffing levels, that deadline may compromise safety; could we consider phased delivery?'"),
                    ("b", "Addressing missed documentation", "'I noticed the triage log wasn't completed for room 3; shall we complete it together now?'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Multidisciplinary Case Conference Feedback",
                "stem": "During a formal multi-agency case conference with social workers and clinical consultants, a trainee remarks:<br><em>'Look, the family are just kicking off because they reckon we don't care, which is totally unfair innit.'</em><br><br>Rewrite this spoken contribution in fluent, professional Standard English suitable for a formal multi-agency panel.",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Remove colloquial slang ('kicking off', 'reckon', 'totally unfair', 'innit')", "[S1]"),
                    ("Substitute with respectful, objective professional phrasing addressing the family's distress", "[A1]")
                ],
                "final_answer": "'In my view, the family's heightened frustration stems from a feeling that their concerns have not been fully addressed, which does not reflect the dedicated care our team has provided.'",
                "reverse_check": "Reframes emotional situation with empathy and professional decorum.",
                "pitfall": "Retaining informal expressions like 'kicking off'."
            }
        ]
    },

    # 6. LINE OF ARGUMENT AND NARRATIVES
    "slc-line-of-argument-and-narratives": {
        "title": "Structuring Spoken Presentations & Arguments",
        "slug": "slc-line-of-argument-and-narratives",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.2 • L2.2",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The 3-Act Structure for Spoken Presentations",
            "points": [
                "Act 1 (Introduction): Hook the audience, state your thesis, and outline the 3 main points you will cover.",
                "Act 2 (Body - 3 Points): Present each point logically with a clear topic sentence, supporting data/evidence, and real-world example.",
                "Act 3 (Conclusion): Summarize your core arguments, deliver a memorable closing thought, and invite audience questions.",
                "Spoken transitions: Use clear signposting phrases ('Moving on to my second point...', 'To illustrate this...')."
            ],
            "calc_tip": "Functional Skills Level 2 presentations typically run for 3-5 minutes, followed by 3-5 minutes of questions."
        },
        "workout_blocks": [
            {
                "title": "Signposting Transitions in Presentations",
                "instruction": "Match the signpost phrase to its presentation stage (Opening, Transition, Evidence, or Conclusion):",
                "items": [
                    ("a", "'Good morning everyone, today I will examine three key benefits of...' ", "Opening / Introduction"),
                    ("b", "'Having looked at the financial costs, let us now turn to staff wellbeing...'", "Transition between points"),
                    ("c", "'To demonstrate the scale of this problem, consider recent audit data...'", "Introducing Evidence"),
                    ("d", "'In conclusion, investing in modern equipment saves time, money, and stress...'", "Conclusion / Summary"),
                    ("e", "'Thank you for listening. I would now welcome any questions you may have.'", "Closing / Q&A Invitation")
                ]
            },
            {
                "title": "Structuring Argument Flow",
                "instruction": "Order the steps of a persuasive spoken presentation into logical sequence (1 to 4):",
                "items": [
                    ("a", "Step 1", "Engaging hook & clear thesis statement"),
                    ("b", "Step 2", "First main argument backed by statistics and case study"),
                    ("c", "Step 3", "Second argument addressing counter-claims and offering solutions"),
                    ("d", "Step 4", "Summary of key takeaways and call to action / questions")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pearson Edexcel L2 Spoken Presentation Scaffold",
                "stem": "You must deliver a 4-minute presentation to your team on the topic: <strong>'Improving Waste Recycling in Our Workplace'</strong>.<br><br>Produce a presentation cue-card outline containing:<br>• A 2-sentence opening hook and roadmap<br>• Two distinct main point headings with supporting evidence bullets<br>• A concluding summary sentence and Q&A prompt.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Opening: Hook establishing environmental/financial problem + roadmap of points", "[S1]"),
                    ("Body: Point 1 (Cost of contaminated waste bins) + Point 2 (Clear color-coded bin signage system)", "[S1]"),
                    ("Conclusion: Reiterate collective responsibility + invite audience questions", "[A1]")
                ],
                "final_answer": "Opening: 'Every week, our facility throws away over £400 by misallocating recyclable card into incineration bins. Today, I will outline why this happens and propose two practical changes to fix it.' Body: 1. Financial impact & audit facts. 2. Implementation of color-coded bin hubs. Conclusion: 'Small sorting habits save thousands; thank you, and I look forward to your questions.'",
                "reverse_check": "Structured outline covering opening, 2 points, and Q&A.",
                "pitfall": "Writing a full script rather than a bulleted cue-card outline."
            }
        ]
    },

    # 7. RESPONDING
    "slc-responding": {
        "title": "Responding to Questions & Handling Challenges",
        "slug": "slc-responding",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1.1 • L2.1",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "The STAR & Clarification Strategy for Q&A",
            "points": [
                "Acknowledge the question: 'Thank you, that is an insightful question...'",
                "Clarify if unsure: 'Could you clarify whether you are referring to the initial capital cost or running costs?'",
                "If you don't know the answer: Be honest and professional ('I don't have that specific data to hand, but I will check with finance and update you by tomorrow').",
                "Handling disagreement: Validate their perspective before presenting counter-evidence ('I understand your concern regarding shift length, however...').",
                "Keep responses focused: Don't ramble; deliver a 30-45 second structured response."
            ],
            "calc_tip": "Always look directly at the person who asked the question, but sweep your gaze to include the whole room while answering."
        },
        "workout_blocks": [
            {
                "title": "Professional Q&A Opening Phrases",
                "instruction": "Select the most professional response opening:",
                "items": [
                    ("a", "When asked a complex question requiring thought", "'That's an important point. Let me address the two key aspects you raised...'"),
                    ("b", "When asked a question you do not know the exact figure for", "'I don't have the exact figure with me today, but I will confirm that with our audit team and email you this afternoon.'"),
                    ("c", "When a questioner misunderstands your presentation", "'Thank you. Perhaps I wasn't entirely clear on that point; what I intended to highlight was...'")
                ]
            },
            {
                "title": "Constructive Responses to Skepticism",
                "instruction": "State how to respond constructively to: 'Your proposed rota will never work because nobody wants to work weekends.'",
                "items": [
                    ("a", "Poor response", "'Yes it will, you're just being negative.'"),
                    ("b", "Constructive model response", "'I recognize that weekend working is unpopular, which is why the proposal includes enhanced premium rates and guaranteed consecutive weekdays off in return.'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Clinical Presentation Q&A Challenge",
                "stem": "After delivering a presentation advocating for electronic tablet patient charting, an attendee challenges you:<br><em>'Digital tablets are a waste of money because older staff will struggle with the technology and paper is much faster.'</em><br><br>Draft a professional, respectful 3-sentence spoken response that acknowledges the concern, provides reassurance regarding staff training, and highlights the patient safety benefits of digital records.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Sentence 1 (Validate): Acknowledge the legitimate concern regarding staff confidence with new technology", "[S1]"),
                    ("Sentence 2 (Address with solution): Highlight comprehensive peer-to-peer mentoring and intuitive app design", "[S1]"),
                    ("Sentence 3 (Reiterate core benefit): Emphasize legible prescriptions and instant allergy alerts that protect patient safety", "[A1]")
                ],
                "final_answer": "'That is a very understandable concern, and supporting all staff through technological changes is vital. To address this, our rollout includes dedicated one-to-one mentoring and hands-on practice sessions until everyone feels confident. Ultimately, the electronic system prevents handwriting misinterpretations and provides instant allergy warnings that significantly improve patient safety.'",
                "reverse_check": "Validates, provides solution, re-establishes safety benefit.",
                "pitfall": "Dismissing the questioner or becoming defensive."
            }
        ]
    },

    # 8. THE EXAM (SLC)
    "slc-the-exam": {
        "title": "SLC Assessment Criteria & Exam Protocols",
        "slug": "slc-the-exam",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC Component Assessment Criteria",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Pearson Edexcel SLC Exam Architecture",
            "points": [
                "Two mandatory components: Task 1 = Formal Discussion (in a group of 3-5 candidates); Task 2 = Spoken Presentation and Q&A.",
                "All candidates are filmed/recorded for external awarding body moderation.",
                "Assessment Criteria Level 2: Express information clearly, use persuasive/analytical language, adapt register, make relevant contributions, challenge others politely, and respond perceptively to complex questions.",
                "Pass/Fail criteria: Every single assessment criterion (AC) must be achieved. A candidate who speaks brilliantly in Task 1 but fails to ask a question in Task 2 will fail the entire component!",
                "Ground rules: Do not dominate, do not remain silent, and always support arguments with evidence."
            ],
            "calc_tip": "Keep a mental tally: 'Have I: 1. Made a main point? 2. Supported someone? 3. Asked a question? 4. Responded to a challenge?'"
        },
        "workout_blocks": [
            {
                "title": "Assessment Criteria True or False",
                "instruction": "State whether each statement is True or False regarding Pearson Edexcel SLC exams:",
                "items": [
                    ("a", "You must prepare a 10-page PowerPoint slide deck for the presentation.", "False (cue cards or brief notes are sufficient; slides are optional)"),
                    ("b", "You can pass even if you never ask any questions during discussions.", "False (asking relevant questions is a mandatory criterion)"),
                    ("c", "Discussions must be carried out in a formal, respectful register.", "True (Standard English and professional register required)"),
                    ("d", "You are permitted to glance at bullet-pointed cue cards while presenting.", "True (cue cards are encouraged; reading a verbatim script is penalised)")
                ]
            },
            {
                "title": "Mandatory Role Checklists",
                "instruction": "State which task each requirement belongs to (Task 1: Discussion, Task 2: Presentation, or Both):",
                "items": [
                    ("a", "Deliver a continuous 3-5 minute spoken talk", "Task 2 (Presentation)"),
                    ("b", "Negotiate consensus and invite others to contribute", "Task 1 (Discussion)"),
                    ("c", "Answer questions from peers and assessor", "Task 2 (Presentation Q&A)"),
                    ("d", "Use appropriate non-verbal body language and maintain eye contact", "Both")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Pearson Edexcel SLC Candidate Performance Audit",
                "stem": "During an SLC Task 1 formal discussion on workplace training, candidate Jamal speaks passionately for 6 uninterrupted minutes, citing numerous personal stories. When other candidates attempt to speak, Jamal talks over them. He asks no questions of others.<br><br>(a) Identify two specific Pearson Edexcel assessment criteria Jamal failed to demonstrate.<br>(b) State two concrete pieces of advice you would give Jamal before his reassessment.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Criteria failed: 1. Respecting turn-taking / not dominating discussion. 2. Listening actively and asking relevant questions of others", "[S1]"),
                    ("Advice 1: Pause after making a 1-minute point and explicitly invite a peer to share their perspective", "[S1]"),
                    ("Advice 2: Prepare 2-3 open questions in advance to demonstrate active listening and inquiry", "[A1]")
                ],
                "final_answer": "(a) Failed criteria: 1. Facilitating turn-taking without interrupting/dominating. 2. Asking relevant questions to extend discussion. (b) Advice: 1. Keep individual contributions under 90 seconds, then pass the floor to others. 2. Actively ask open questions ('How does your department handle this, Sarah?').",
                "reverse_check": "Identifies assessment criteria failures and provides actionable coaching advice.",
                "pitfall": "Praising Jamal for speaking for 6 minutes (dominating is a major failure)."
            }
        ]
    },

    # 9. USING EVIDENCE
    "slc-using-evidence": {
        "title": "Using Evidence, Facts & Data in Spoken Arguments",
        "slug": "slc-using-evidence",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L2.2 • L2.4",
        "level": "Level 2",
        "method_card": {
            "title": "Evidence Types in Spoken Discourse",
            "points": [
                "Empirical Data: Percentages, survey counts, audit statistics ('A survey of 120 staff revealed that 74%...').",
                "Expert Opinion / Authority: Citing professional standards or recognized guidelines ('Under Health & Safety Executive guidance...').",
                "Real-World Examples / Case Studies: Concrete workplace anecdotes that illustrate a point in practice.",
                "Framing evidence aloud: 'Research demonstrates that...', 'According to recent facility audits...', 'In our experience on Ward 2...'",
                "Avoid unsupported assertions: Never say 'Everyone knows that...' or 'It's obvious that...'"
            ],
            "calc_tip": "Round complex statistics aloud for ease of listening (e.g. say 'roughly three-quarters' or 'just over 70%' rather than '73.842%')."
        },
        "workout_blocks": [
            {
                "title": "Weak Assertions vs Evidence-Based Statements",
                "instruction": "State whether each statement is an Unsupported Assertion or an Evidence-Based Argument:",
                "items": [
                    ("a", "'Staff are obviously lazy because attendance on Mondays is terrible.'", "Unsupported Assertion (generalized opinion)"),
                    ("b", "'Our absence audit indicates Monday sick leave is 18% higher than midweek days, primarily due to weekend shift fatigue.'", "Evidence-Based Argument (cites audit data and rationale)"),
                    ("c", "'Everyone agrees that our current uniforms are completely useless.'", "Unsupported Assertion"),
                    ("d", "'According to a survey of 85 healthcare assistants, 68% reported that the poly-cotton uniforms cause overheating during summer shifts.'", "Evidence-Based Argument")
                ]
            },
            {
                "title": "Verbalizing Statistics Smoothly",
                "instruction": "Convert the raw statistic into a conversational spoken phrase:",
                "items": [
                    ("a", "74.8% of respondents", "'Nearly three-quarters of respondents'"),
                    ("b", "49 out of 100 participants", "'Approximately half of the participants'"),
                    ("c", "£1,985 in unexpected repair fees", "'Just under two thousand pounds in unexpected repair costs'")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Estates Committee Resource Proposal",
                "stem": "You are arguing in a meeting that your healthcare facility should install <strong>two dedicated water filtration stations</strong> in the staff rest rooms.<br><br>Draft a 3-sentence spoken argument that incorporates:<br>• A concrete statistic or survey finding<br>• An environmental or health benefit<br>• A reference to reputable workplace standards.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Sentence 1: State proposal and cite survey statistic (e.g. 82% of staff currently buy single-use plastic bottles)", "[S1]"),
                    ("Sentence 2: Link to environmental/financial benefits (eliminating 10,000 plastic bottles per year)", "[S1]"),
                    ("Sentence 3: Quote workplace standard/guideline recommending accessible chilled hydration", "[A1]")
                ],
                "final_answer": "'In our recent staff consultation, over 80% of colleagues reported purchasing single-use bottled water daily due to poor tap water quality. Installing dedicated filtered hydration stations would eliminate an estimated 12,000 plastic bottles annually from our waste stream. Furthermore, the Health and Safety Executive specifically emphasizes that easily accessible, clean drinking water significantly reduces fatigue during long clinical shifts.'",
                "reverse_check": "Includes statistic, environmental outcome, and official workplace standard.",
                "pitfall": "Expressing only personal preference without citing data or standards."
            }
        ]
    },

    # 10. YOUR TURN
    "slc-your-turn": {
        "title": "Independent Discussion & Facilitation Practice",
        "slug": "slc-your-turn",
        "subject": "English Speaking & Listening",
        "spec_codes": "Pearson Edexcel English: SLC L1 & L2 Comprehensive Practice",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Chairing and Facilitating a Discussion",
            "points": [
                "Opening the discussion: Introduce the topic clearly and state the objective (e.g. 'Our goal today is to choose two recommendations to submit to management').",
                "Timekeeping: Keep an eye on the clock and signal transitions ('We have about 3 minutes left, so let's move toward a consensus').",
                "Synthesising ideas: Pull together disparate viewpoints into a shared agreement.",
                "Concluding: Summarize the decision reached and thank all participants."
            ],
            "calc_tip": "If the group falls into an awkward silence, do not panic! Summarize what has been said so far and ask an open question."
        },
        "workout_blocks": [
            {
                "title": "Facilitation Tool-Kit Phrases",
                "instruction": "Match the facilitator phrase to the appropriate situation:",
                "items": [
                    ("a", "Breaking an awkward silence in the group", "'We've heard some great points on cost; what do people feel about the impact on staff time?'"),
                    ("b", "Bringing a runaway debate to a close", "'We've had a vigorous debate on both sides; let's take a quick vote so we can agree our recommendation.'"),
                    ("c", "Handling two speakers talking simultaneously", "'Hold on a second, Marcus, let's let Priya finish her thought and then we'll come right back to you.'")
                ]
            },
            {
                "title": "Reaching Consensus",
                "instruction": "State whether the outcome represents Consensus, Deadlock, or Imposed Decision:",
                "items": [
                    ("a", "All members agree on a compromise combining Option A's schedule with Option B's budget", "Consensus (collaborative agreement)"),
                    ("b", "Two members refuse to budge and the meeting ends with no agreed action", "Deadlock"),
                    ("c", "The manager says 'I don't care what you think, we are doing Option C'", "Imposed Decision")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Multidisciplinary Consensus Simulation",
                "stem": "Your group has <strong>2 minutes remaining</strong> in an SLC formal discussion on: <em>'Should clinical staff rotas move to a flexible 4-day compressed week?'</em><br>Two members strongly favor the change, while one member has raised serious concerns about evening child-care arrangements.<br><br>As facilitator, write a 3-sentence spoken contribution that acknowledges both sides, proposes a practical trial compromise, and concludes the discussion on time.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Sentence 1: Summarize the two perspectives fairly (productivity/rest benefits vs childcare concerns)", "[S1]"),
                    ("Sentence 2: Propose a constructive compromise (e.g. a voluntary 3-month pilot with flexible opting-in)", "[S1]"),
                    ("Sentence 3: Secure group consensus and formally conclude the discussion", "[A1]")
                ],
                "final_answer": "'We have heard compelling arguments today regarding the rest benefits of a 4-day week, as well as crucial practical concerns regarding evening childcare commitments. As a workable compromise, I propose we recommend a voluntary 3-month pilot where interested staff can trial the compressed rota while others remain on standard shifts. Does everyone agree that this gives us the evidence we need without disadvantaging anyone?'",
                "reverse_check": "Acknowledges both sides, offers compromise, seeks agreement, closes on time.",
                "pitfall": "Ignoring the childcare concern and forcing a one-sided vote."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(ENGLISH_SLC_BATCH3_WORKOUTS)} topics in authentic_workouts_english_slc_batch3.py")
