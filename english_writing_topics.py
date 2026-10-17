#!/usr/bin/env python3
"""
English Writing Topics (15 Topics)
Master Functional Skills Curriculum Suite — Deep PFS-Beating Edition
Every topic features:
- 3 Core Skills with rich HTML tables, before/after upgrades, and L1 vs L2 rules
- 2 Step-by-Step Worked Exam Models (Level 1 & Level 2)
- 2 Critical Examiner Traps
- 3 Scenario/Draft-Rich Exam Practice Questions with complete model answers
"""

WRITING_TOPICS = [
    # 1. Planning Written Responses
    {
        "filename": "writing-planning-your-answer.html",
        "clean_topic": "Planning Written Responses",
        "intro_lead": "Construct structured, logical written responses using the 5-minute planning blueprint, PAF (Purpose, Audience, Format) deconstruction, paragraph mapping, and target word-count allocation.",
        "next_file": "writing-communicating.html",
        "next_name": "Communicating Clearly",
        "spec_points": [
            ("L1.19 / L2.19", "Plan and organise written work coherently, selecting appropriate formats and layouts for the target audience."),
            ("L1.22 / L2.20", "Use planning strategies to sequence arguments logically, integrate all prompt bullets, and meet target word counts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-pen-to-square",
                "title": "Golden Rule 1: Spend 5 Minutes Planning Before You Write a Word",
                "desc": "In Pearson Edexcel and City & Guilds writing exams, candidates who spend 5 minutes jotting down a bullet-pointed paragraph plan score up to 30% higher on organisation, coherence, and task completion.",
                "badge": "Plan: PAF Check → Paragraph 1 (Intro) → Paragraph 2 & 3 (Core Bullets) → Paragraph 4 (Action/Close)"
            },
            {
                "icon": "fa-list-check",
                "title": "Golden Rule 2: Tick Off Every Prompt Bullet Point in the Exam Question",
                "desc": "Exam questions always provide 3 or 4 bullet points that you MUST address. Number them 1 to 4 on your question paper and cross each one off as you map it into a specific paragraph.",
                "badge": "Every omitted bullet point results in an automatic penalty to your Content & Organisation mark."
            }
        ],
        "skills": [
            {
                "title": "The Vocational 5-Minute PAF & Paragraph Blueprint",
                "summary": "How to deconstruct the exam prompt and map your response under timed exam pressure.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Minute 1 — Decode PAF (Purpose, Audience &amp; Format):</strong> Highlight who you are writing to (e.g. Hospital Estates Director), why (e.g. persuade them to improve staff parking), and in what form (e.g. Formal Letter).</li>
                    <li><strong>Minute 2 — Map the Prompt Bullets:</strong> Assign each bullet point from the exam prompt to a dedicated body paragraph so nothing is left out.</li>
                    <li><strong>Minute 3 — Brainstorm Evidence &amp; Details:</strong> Add 1 realistic statistic, example, or workplace consequence next to each paragraph note (e.g. <em>"25-minute delay at shift handover"</em>).</li>
                    <li><strong>Minute 4 — Select Discourse Markers &amp; Punctuation Targets:</strong> Jot down 3 linking words (<em>Furthermore, Consequently, Nevertheless</em>) and remind yourself to use a semicolon and colon.</li>
                    <li><strong>Minute 5 — Confirm Format Frame:</strong> Note the exact greeting and sign-off required (e.g. <em>Dear Mr Evans → Yours sincerely</em>).</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Level 1 vs Level 2 Planning & Structural Expectations",
                "summary": "Key differences in detail, length, and paragraph sophistication between Level 1 and Level 2 writing tasks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Planning Dimension</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Level 1 Benchmark</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Level 2 Benchmark</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Target Word Count</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Task 1: 150–200 words | Task 2: 100–150 words</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Task 1: 250–300 words | Task 2: 200–250 words</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Paragraph Structure</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">3–4 clear paragraphs with logical sequence (Intro, Main Points, Conclusion).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">4–5 cohesive paragraphs including counter-argument or evaluation and subheadings where appropriate.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Evidence &amp; Elaboration</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Direct expansion of every bullet point in the prompt using clear examples.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Sustained persuasive or analytical development backed by realistic operational data, costs, or regulatory standards.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Before & After: Unplanned Rambling vs Planned Paragraph Structure",
                "summary": "See how a 4-minute plan transforms disorganised thoughts into a high-scoring Level 2 opening.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:10px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Unplanned Draft (Repetitive, Jumbled Ideas — Band 1):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"I am writing about the staff canteen because the food is too expensive and also the microwaves are broken so night shift staff can't heat up their meals and we need healthy options too because everyone is eating crisps from the vending machine which is bad for health."</em>
                  </div>
                  <p style="margin-bottom:10px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Planned Draft (Clear Topic Sentence &amp; Sequenced Focus — Band 3):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"I am writing on behalf of the nursing team to propose three urgent improvements to the hospital staff canteen. Currently, night-shift staff have no access to hot nutritious meals after 20:00, and two of the three breakroom microwaves have been out of order for a fortnight."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Task Plan & Opening: Community Centre Hall Hire Email",
                "marks": "Level 1 Planning & Execution Benchmark (15 Marks)",
                "context": "Local Community Event Organisation",
                "question": "You are organising a charity first-aid workshop and want to hire a room at Oakwood Community Centre on Saturday 14 November.<br>Write an email to the manager, Mr Samuels, to:<br>• Explain what the event is and how many people will attend<br>• Ask about room availability and projector equipment<br>• Enquire about weekend hire costs and parking.",
                "steps": [
                    ("Step 1", "Decode PAF & Email Headers", "<strong>Format:</strong> Formal/Semi-formal Email.<br><strong>To:</strong> m.samuels@oakwoodcentre.org.uk | <strong>Subject:</strong> Room Hire Enquiry – Charity First-Aid Workshop (14 November)<br><strong>Salutation:</strong> Dear Mr Samuels,", "Format & Audience (L1.22)"),
                    ("Step 2", "Map 3 Short Body Paragraphs to the 3 Prompt Bullets", "<strong>Para 1 (Event & Numbers):</strong> St John Ambulance community first-aid session, 25 local residents attending, 10:00 to 14:00.<br><strong>Para 2 (Room & Equipment):</strong> Need ground-floor hall with a digital projector, screen, and 30 chairs.<br><strong>Para 3 (Costs & Parking):</strong> Request charity discount rate and confirm if free parking is available for 15 cars.", "Covers All 3 Prompt Bullets (L1.19)"),
                    ("Step 3", "Draft Complete Model Response", "Write out the email cleanly using the 3-paragraph plan and sign off with <em>Kind regards</em> or <em>Yours sincerely</em>.", "Coherent Structure & SPaG")
                ],
                "final_answer": "To: m.samuels@oakwoodcentre.org.uk<br>Subject: Room Hire Enquiry – Charity First-Aid Workshop (14 November)<br><br>Dear Mr Samuels,<br><br>I am writing to enquire about hiring a training room at Oakwood Community Centre on Saturday 14 November from 10:00 to 14:00. We are holding a free community first-aid workshop for approximately 25 local residents.<br><br>Could you please confirm whether the Main Ground-Floor Hall is available on this date? For our practical demonstrations, we require a room equipped with a digital projector, a display screen, and seating for 30 people.<br><br>Finally, please could you send me your weekend hire rates, including any discounts for registered charities, and confirm whether delegates can use the centre car park free of charge?<br><br>Yours sincerely,<br>Alex Taylor",
                "tutor_tip": "Notice how each bullet point from the question becomes one clear, self-contained paragraph. The examiner can tick off all three content requirements in seconds."
            },
            {
                "title": "Level 2 Extended Plan & Model: NHS Electronic Shift Handover Proposal",
                "marks": "Level 2 Full Planning & Writing Benchmark (18 Marks)",
                "context": "Clinical Ward Operations & Digital Transformation",
                "question": "You are asked to write a 250-word proposal to your Clinical Lead recommending an electronic handover app.<br>Create a structured paragraph plan and draft the executive summary and recommendations addressing:<br>• Flaws in current paper notes<br>• Benefits of digital handover<br>• Proposed staff training timeline.",
                "steps": [
                    ("Step 1", "Plan Heading and Strategic Objective", "<strong>Title:</strong> Proposal: Implementation of Electronic Ward Handover System<br><strong>PAF:</strong> Formal Internal Proposal to Clinical Lead — analytical, persuasive, evidence-led.", "PAF & Layout Conventions (L2.23)"),
                    ("Step 2", "Map Body Paragraphs 1 & 2 (Problem & Digital Solution)", "<strong>Section 1 (Paper Flaws):</strong> Illegible handwriting and misplaced paper sheets delay shift handovers by 25 minutes daily.<br><strong>Section 2 (Digital Benefits):</strong> Real-time bedside tablet updates, automated vital-sign alerts, and full GDPR encryption.", "Logical Sequencing & Detail (L2.20)"),
                    ("Step 3", "Map Body Paragraph 3 (Phased Training Rollout)", "<strong>Section 3 (Timeline):</strong> Two-week pilot on Ward 4 starting next month; 30-minute lunchtime workshops led by two ward 'super-users'.", "Feasible Action Plan & SPaG (L2.24)")
                ],
                "final_answer": "<strong>PROPOSAL: IMPLEMENTATION OF ELECTRONIC SHIFT HANDOVER APP</strong><br><strong>To:</strong> Clinical Lead | <strong>From:</strong> Senior Ward Coordinator | <strong>Date:</strong> 14 October 2026<br><br><strong>1. Current Paper Handover Deficiencies</strong><br>Currently, ward handovers rely on handwritten paper sheets that are frequently illegible or incomplete; consequently, incoming nursing teams lose an average of 25 minutes per shift clarifying medication changes.<br><br><strong>2. Operational &amp; Safety Benefits of Digital Handover</strong><br>Transitioning to a secure tablet-based handover app will synchronise patient observations in real time, flag overdue medications automatically, and ensure full GDPR compliance.<br><br><strong>3. Proposed Rollout &amp; Training Timeline</strong><br>• <strong>Weeks 1–2:</strong> Train two senior nurses as digital super-users during 30-minute lunchtime modules.<br>• <strong>Weeks 3–4:</strong> Pilot the electronic app on Ward 4 alongside paper backups before trust-wide deployment.",
                "tutor_tip": "A tight 4-minute plan prevents mid-essay rambling and guarantees you include high-scoring Level 2 features such as numbered subheadings, bulleted timelines, and a semicolon."
            }
        ],
        "examiner_traps": [
            {
                "title": "Starting to Write Immediately Without a Plan",
                "desc": "Candidates who skip planning inevitably repeat themselves in Paragraphs 2 and 3, lose control of sentence structure, and run out of time before writing a proper conclusion.",
                "fix": "Always spend 4 to 5 minutes sketching a 4-box paragraph outline in your planning space before typing your response."
            },
            {
                "title": "Writing Your Entire Essay Inside the Planning Box",
                "desc": "Some candidates write full sentences in the planning box and then run out of time to copy them into the final answer box. Examiners primarily mark the final response area.",
                "fix": "Keep your plan strictly to short 3-to-5 word bullet notes (e.g. 'Para 2: Cost savings — £400/month')."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Read this exam prompt: <em>'Write a formal letter to your local council complaining about dangerous potholes on Highfield Road, explaining the risks to cyclists and suggesting repairs.'</em><br>Create a structured 4-paragraph plan showing the exact focus of each paragraph and the correct letter sign-off.",
                "solution_steps": "1. Identify PAF: Formal complaint letter to Local Council Highways Department (Dear Sir/Madam → Yours faithfully).<br>2. Map Paragraph 1 (Purpose & Location) and Paragraph 2 (Specific risks to cyclists/vehicles).<br>3. Map Paragraph 3 (Requested resurfacing action & timeline) and Paragraph 4 (Formal closing call to action).",
                "correct_answer": "Paragraph 1: Purpose of letter and exact location of potholes on Highfield Road. | Paragraph 2: Safety hazards to cyclists (swerving into traffic, punctured tyres) and recent near-misses. | Paragraph 3: Request urgent inspection and full resurfacing within 14 days. | Paragraph 4: Request written confirmation of repair schedule + 'Yours faithfully,' sign-off.",
                "tutor_tip": "Keep each paragraph focused on a single distinct stage: Situation → Impact/Risk → Solution → Formal Close."
            },
            {
                "marks": "3 Marks",
                "question": "A candidate wrote this disorganised draft paragraph containing three mixed-up topics:<br><em>'Our warehouse needs electric charging points in the car park. Also the canteen vending machine is broken and staff want more salad options. Seven delivery drivers have bought electric cars this year and have nowhere to charge them during shifts.'</em><br>Edit and restructure this draft so it maintains a single coherent paragraph topic suitable for an estates proposal.",
                "solution_steps": "1. Delete the irrelevant sentence about the canteen vending machine and salad options (off-topic drift).<br>2. Combine the remaining two points logically: state the proposal first, then follow with the supporting staff evidence.<br>3. Add a cohesive linking word ('Furthermore' or 'Consequently') and a concluding benefit.",
                "correct_answer": "'Our warehouse urgently requires the installation of electric vehicle (EV) charging points in the main staff car park. Seven delivery drivers have purchased electric cars this year; however, they currently have nowhere to charge their vehicles during shift hours. Installing four fast-charging bays will support staff retention and reduce our depot's carbon footprint.'",
                "tutor_tip": "One paragraph = one core topic. If a sentence belongs to a different topic (like the canteen), delete it or move it to its own paragraph."
            },
            {
                "marks": "4 Marks",
                "question": "You have 30 minutes to complete a Level 2 report (250–300 words) for your Care Home Manager on improving visitor check-in security.<br>1. Break down how you should allocate your 30 minutes across planning, writing, and proofreading.<br>2. Write the exact Title and three numbered subheadings you would put in your plan.",
                "solution_steps": "1. Time allocation: 5 minutes planning, 20 minutes drafting the report, 5 minutes proofreading SPaG.<br>2. Title: Formal report heading stating the exact topic.<br>3. Subheadings: 1.0 Current Security Vulnerabilities, 2.0 Proposed Digital Sign-In System, 3.0 Cost & Implementation Recommendations.",
                "correct_answer": "1. Time Split: 5 mins Planning | 20 mins Writing | 5 mins Proofreading.<br>2. Report Structure:<br>Title: Report on Upgrading Visitor Check-In Security at Elmwood Care Home<br>• 1.0 Introduction & Current Sign-In Risks<br>• 2.0 Benefits of Electronic Visitor Badges & Lanyards<br>• 3.0 Recommendations & Rollout Costs",
                "tutor_tip": "Writing down your report subheadings during the 5-minute planning phase gives you an instant scaffold to fill in during your 20-minute writing phase."
            }
        ]
    },

    # 2. Communicating Clearly & Coherently
    {
        "filename": "writing-communicating.html",
        "clean_topic": "Communicating Clearly & Coherently",
        "intro_lead": "Express complex ideas with precision, maintain logical continuity, replace vague colloquialisms with exact workplace terminology, and eliminate ambiguity across professional communications.",
        "next_file": "writing-context.html",
        "next_name": "Vocational Context & Purpose",
        "spec_points": [
            ("L1.20 / L2.20", "Communicate information, ideas, and opinions clearly, coherently, and effectively."),
            ("L2.21", "Write with sustained clarity and appropriate detail, ensuring logical progression and precise vocabulary.")
        ],
        "golden_rules": [
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 1: One Core Idea Per Sentence (Eliminate Rambling Run-Ons)",
                "desc": "Avoid breathless 50-word sentences strung together with 'and then... and so...'. Break ideas down into crisp clauses connected by precise conjunctions so your reader understands the exact sequence on the first read.",
                "badge": "Clear Subject → Strong Active Verb → Exact Operational Consequence"
            },
            {
                "icon": "fa-road",
                "title": "Golden Rule 2: Progress Logically from Situation to Impact to Action",
                "desc": "Guide your reader step-by-step. State clearly what happened (Situation), explain why it matters (Impact on safety, cost, or service), and conclude with what must happen next (Remedial Action).",
                "badge": "Sequence: Situation → Operational Impact → Remedial Action"
            }
        ],
        "skills": [
            {
                "title": "Three Techniques for Crystal-Clear Professional Prose",
                "summary": "Eliminating wordiness, vague pronouns, and passive ambiguity in workplace writing.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Prefer Active Voice for Accountability:</strong> Write <em>"Senior Nurse Taylor completed the controlled drug audit at 18:00"</em> rather than <em>"The audit was done by someone later on."</em></li>
                    <li><strong>Trim Bloated Wordiness:</strong> Replace <em>"Due to the fact that"</em> with <em>"Because"</em>; replace <em>"At this present moment in time"</em> with <em>"Currently"</em>; replace <em>"In the event that"</em> with <em>"If"</em>.</li>
                    <li><strong>Anchor Every Pronoun ('This', 'It', 'They'):</strong> Never write <em>"They didn't fix it, which caused a problem."</em> Specify the exact nouns: <em>"The external contractors failed to repair the boiler valve, which left Ward 3 without hot water."</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Before & After: Upgrading Vague Sentences into Precise Level 2 Prose",
                "summary": "Side-by-side comparison showing how specific nouns, times, and verbs earn Band 3 Content marks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Vague / Ambiguous Draft (Band 1)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Clear, Precise Professional Upgrade (Band 3)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Why It Scores Higher</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Some stuff was left in the corridor and somebody nearly tripped over it earlier."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Three unpacked cardboard delivery boxes were left obstructing Fire Exit B at 11:30, causing a visiting outpatient to trip."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Replaces 'some stuff' and 'earlier' with exact quantities, location, time, and hazard.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We need better computers because the ones we have are really slow and annoying."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Upgrading the reception desktop terminals will reduce patient check-in times from five minutes to under sixty seconds."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Replaces emotional complaint ('annoying') with measurable operational benefit.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"People aren't washing their hands properly so germs are spreading."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Recent infection-control audits revealed a 15% drop in hand-hygiene compliance prior to patient contact."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Uses authoritative workplace register and concrete audit evidence.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Level 1 vs Level 2 Clarity & Detail Standards",
                "summary": "How examiners judge 'sufficient detail' and 'effective communication' across both levels.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Level 1 Standard (L1.20):</strong> Statements must be unambiguous and directly relevant to the task. Dates, times, prices, and locations must be stated clearly so the recipient knows exactly what to do.</li>
                    <li><strong>Level 2 Standard (L2.21):</strong> Ideas must be developed with persuasive or analytical depth. Instead of merely stating a rule, explain the <strong>rationale</strong> behind the rule and the <strong>consequence</strong> of non-compliance.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Clear Staff Notice for Office Refurbishment",
                "marks": "Level 1 Clarity & Detail Benchmark (3 Marks)",
                "context": "Business Administration & Facilities Management",
                "question": "Rewrite this confusing staff notice so that the instructions, dates, and actions are 100% clear:<br><em>'The painters are coming in next week to do the second floor offices so you need to pack up your desk things in crates by Friday afternoon and work in the downstairs meeting room until Wednesday.'</em>",
                "steps": [
                    ("Step 1", "Break the rambling run-on sentence into clear logical statements", "Separate the refurbishment schedule, the Friday preparation task, and the temporary workspace arrangement.", "Sentence Control (L1.20)"),
                    ("Step 2", "Add specific times and unambiguous action verbs", "Specify 17:00 on Friday for packing desks and Ground Floor Conference Room for Monday–Wednesday.", "Precision & Detail"),
                    ("Step 3", "Draft polished, easy-to-read notice", "Present as a crisp 3-sentence workplace notice.", "Final Execution")
                ],
                "final_answer": "<strong>Notice: Second-Floor Office Refurbishment (Monday 19 – Wednesday 21 October)</strong><br>External decorators will be repainting all second-floor offices from Monday 19 October until Wednesday 21 October. Please pack all personal desk items and keyboards into the plastic storage crates provided before 17:00 this Friday. During the three days of painting, all second-floor staff will work from the Ground-Floor Conference Room.",
                "tutor_tip": "Breaking a 38-word run-on sentence into three distinct sentences (What is happening → What you must do by Friday → Where to go on Monday) eliminates confusion immediately."
            },
            {
                "title": "Level 2 Model: Clinical Near-Miss Incident Notification Rewrite",
                "marks": "Level 2 Precision & Register Benchmark (4 Marks)",
                "context": "Healthcare Incident Reporting",
                "question": "Rewrite this confusing, colloquial incident note for a formal clinical governance log:<br><em>'There was medication which was left out because someone didn't put it back when they finished their shift and then someone else almost gave it to the wrong patient on bed 4.'</em>",
                "steps": [
                    ("Step 1", "Identify key factual components and remove vague pronouns", "Replace 'someone' and 'they' with specific clinical roles and exact handover timing.", "Eliminates Ambiguity (L2.21)"),
                    ("Step 2", "Apply formal clinical incident terminology", "Use precise terms: 'unsecured medication', 'shift changeover', 'near-miss administration', 'remedial lock-check'.", "Vocational Register (L2.23)"),
                    ("Step 3", "Structure as Situation → Risk → Immediate Containment", "Draft three clear sentences stating the security breach, the near-miss event, and the corrective action taken.", "Coherent Progression")
                ],
                "final_answer": "'During the 19:00 shift changeover, a blister pack of prescribed analgesia was inadvertently left unsecured on the nursing station counter. Consequently, a near-miss occurred when the medication was almost administered to the resident in Bed 4. The medication was immediately returned to the locked controlled-drugs cabinet, and all staff were briefed on mandatory end-of-shift counter checks.'",
                "tutor_tip": "Converting colloquial chatter ('someone didn't put it back') into crisp, objective incident prose demonstrates top-band Level 2 mastery."
            }
        ],
        "examiner_traps": [
            {
                "title": "Using Vague Pronouns like 'It', 'This', and 'They'",
                "desc": "Writing 'They told them about it, which caused delays' leaves the examiner guessing who spoke, who listened, and what was delayed.",
                "fix": "Always name the exact role and object: 'The Warehouse Supervisor informed the delivery drivers of the road closure.'"
            },
            {
                "title": "Contradictory Statements Within the Same Response",
                "desc": "Saying in Paragraph 1 that a training course is 'completely free for staff' and in Paragraph 3 that 'staff only pay £25 each' destroys coherence.",
                "fix": "Check that figures, dates, and policies remain 100% consistent from your opening sentence to your conclusion."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Rewrite this vague workplace sentence so it communicates clearly and professionally:<br><em>'The machines are broken so workers are sitting around and delivery times are going down the drain.'</em>",
                "solution_steps": "1. Replace colloquialisms ('sitting around', 'going down the drain') with formal operational terms.<br>2. State cause and effect clearly in a well-punctuated sentence.",
                "correct_answer": "'Due to an unexpected conveyor belt malfunction on Line 2, packing operations have halted and customer delivery schedules are experiencing significant delays.'",
                "tutor_tip": "Always replace idioms like 'down the drain' with concrete workplace impacts like 'experiencing significant delays'."
            },
            {
                "marks": "3 Marks",
                "question": "Eliminate the wordy filler phrases and vague pronouns in this draft email sentence:<br><em>'At this moment in time, due to the fact that they haven't sent the stuff we ordered last week, we are basically unable to finish doing their kitchen job on time.'</em>",
                "solution_steps": "1. Replace 'At this moment in time' with 'Currently' and 'due to the fact that' with 'because'.<br>2. Replace 'they', 'the stuff', and 'their kitchen job' with specific nouns (e.g. the supplier, the ceramic wall tiles, the kitchen installation).",
                "correct_answer": "'Currently, because our supplier has not yet delivered the ceramic wall tiles ordered last week, we are unable to complete the kitchen installation on schedule.'",
                "tutor_tip": "Cutting bloated phrases makes your writing sharper, faster to read, and far more authoritative."
            },
            {
                "marks": "4 Marks",
                "question": "You are a Care Home Team Leader. Write a clear, 3-sentence handover note for the night shift explaining that Resident Mr Arthur Evans (Room 12) had his blood pressure medication adjusted by Dr Patel at 15:00 today, requires his blood pressure checked at 21:00, and must be monitored for dizziness when standing.",
                "solution_steps": "1. Sentence 1 (Situation): State resident name, room number, and exact medication change by Dr Patel at 15:00.<br>2. Sentence 2 (Required Action): Instruct night staff to record his blood pressure at 21:00.<br>3. Sentence 3 (Safety Monitoring): Specify observation for postural dizziness during mobility transfers.",
                "correct_answer": "'At 15:00 today, Dr Patel adjusted the blood pressure medication for Mr Arthur Evans in Room 12. Night-shift staff must check and record Mr Evans's blood pressure on his observation chart at 21:00. Additionally, please supervise him closely when standing or transferring, as the revised dosage may cause temporary dizziness.'",
                "tutor_tip": "Notice how every clinical detail (Who, Where, When, What action, Why) is stated with zero ambiguity."
            }
        ]
    },

    # 3. Vocational Context & Purpose
    {
        "filename": "writing-context.html",
        "clean_topic": "Vocational Context & Purpose",
        "intro_lead": "Align your writing with real-world workplace scenarios, regulatory frameworks, organisational priorities, and stakeholder expectations across healthcare, logistics, business, and public services.",
        "next_file": "writing-assessing-audience.html",
        "next_name": "Audience, Tone & Register",
        "spec_points": [
            ("L1.21 / L2.21", "Write for specific vocational contexts and purposes, selecting appropriate level of detail and specialist vocabulary."),
            ("L2.22", "Adapt writing strategies to meet specific commercial, public sector, and statutory operational contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-briefcase",
                "title": "Golden Rule 1: Step Fully Into the Scenario Persona",
                "desc": "If the exam prompt casts you as a Senior Care Assistant, Site Safety Officer, or Customer Relations Manager, adopt the exact responsibilities, concerns, and vocabulary of that role from sentence one.",
                "badge": "Adopt the exact professional persona and authority level specified in the exam scenario."
            },
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 2: Anchor Every Argument to Core Organisational Priorities",
                "desc": "Managers and councils make decisions based on five factors: Health & Safety, Budget/Cost-Efficiency, Legal/Regulatory Compliance, Service User Wellbeing, and Staff Retention. Tie your points to these drivers.",
                "badge": "Justify proposals using Safety, Cost Savings, Compliance (CQC/HSE/GDPR), or Client Care."
            }
        ],
        "skills": [
            {
                "title": "Sector-Specific Vocabulary & Priorities Matrix",
                "summary": "High-scoring terminology and regulatory anchors across the four most common exam settings.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Vocational Sector</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Key Regulatory / Organisational Drivers</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">High-Scoring Specialist Vocabulary</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Health &amp; Social Care</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">CQC inspection ratings, patient dignity, safeguarding, infection control, continuity of care.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>multidisciplinary team, clinical governance, person-centred care, domiciliary, holistic wellbeing</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Construction &amp; Logistics</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">HSE compliance, accident reduction, PPE enforcement, turnaround times, supply-chain reliability.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>risk mitigation, mandatory PPE, pedestrian segregation, preventative maintenance, throughput</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Business &amp; Administration</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">GDPR data protection, return on investment (ROI), staff productivity, overhead reduction.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>capital expenditure, operational overheads, data encryption, stakeholder engagement, audit trail</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Local Council &amp; Community</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Public safety, accessibility, environmental sustainability, value for taxpayers, social inclusion.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>civic amenities, traffic calming, sustainable infrastructure, community cohesion, public consultation</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Before & After: Turning Personal Complaints into Vocational Business Cases",
                "summary": "Why framing arguments around organisational benefit wins top marks in Level 2 tasks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Weak Personal Angle (Low Context Awareness):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"We want you to buy new office chairs because our backs hurt by 3pm and it isn't fair that we have to sit on old chairs all day."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Strong Vocational Angle (Aligned with H&amp;S and Productivity):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"Investing in ergonomic lumbar-support seating will ensure full compliance with Display Screen Equipment (DSE) regulations while reducing musculoskeletal sickness absence across the administration team."</em>
                  </div>
                </div>
                """
            },
            {
                "title": "Level 1 vs Level 2 Contextual Detail Requirements",
                "summary": "How to pitch realistic facts, figures, and workplace solutions without inventing absurd statistics.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Use Plausible, Grounded Details:</strong> You are encouraged to invent realistic supporting details (e.g. <em>"a 15% reduction in energy bills"</em> or <em>"a £500 grant from the local council"</em>), provided they fit the scenario believably.</li>
                    <li><strong>Avoid Unrealistic Exaggeration:</strong> Never write <em>"100% of staff will quit tomorrow if we don't get a new coffee machine."</em> Exaggeration undermines your professional credibility.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Warehouse PPE Replacement Request Email",
                "marks": "Level 1 Vocational Context Benchmark (3 Marks)",
                "context": "Warehouse Operations & Health and Safety",
                "question": "You are a warehouse team leader. Write a short email to the Depot Manager, Mr Khan, requesting 15 new high-visibility thermal jackets for the loading bay team ahead of winter.",
                "steps": [
                    ("Step 1", "Set up email headers and state the specific request", "<strong>To:</strong> r.khan@metrologistics.co.uk | <strong>Subject:</strong> Urgent Order Request – 15 Thermal High-Visibility Jackets", "Clear Vocational Format (L1.21)"),
                    ("Step 2", "Connect request to workplace safety and winter weather conditions", "Explain that loading bay doors remain open during early morning dispatches and current jackets have faded reflective strips.", "Contextual Justification"),
                    ("Step 3", "Provide supplier cost detail and call to action", "State unit cost (£22 per jacket, total £330) and ask for purchase approval by Friday.", "Practical Workplace Detail")
                ],
                "final_answer": "To: r.khan@metrologistics.co.uk<br>Subject: Urgent Order Request – 15 Thermal High-Visibility Jackets<br><br>Dear Mr Khan,<br><br>I am writing to request authorisation to order 15 replacement thermal high-visibility jackets for our Loading Bay 2 team before winter shift schedules begin next month.<br><br>Several existing jackets have worn reflective strips that no longer meet site safety standards around moving forklifts. Furthermore, because the loading bay shutters remain open during 05:00 dispatches, thermal insulation is essential to prevent cold-related illness.<br><br>Our approved PPE supplier can deliver 15 jackets for £330 in total (£22 each). Please could you approve this purchase order by Friday?<br><br>Kind regards,<br>Jordan Smith, Loading Bay Team Leader",
                "tutor_tip": "Notice how linking the jackets to forklift visibility and 05:00 winter temperatures makes the request realistic and compelling."
            },
            {
                "title": "Level 2 Model: Care Home Sensory Garden Capital Funding Proposal",
                "marks": "Level 2 Vocational Context Benchmark (4 Marks)",
                "context": "Dementia Care & CQC Inspection Readiness",
                "question": "Write the opening two paragraphs of an internal funding request to the Care Home Finance Director for £800 to create a sensory garden for residents living with dementia.",
                "steps": [
                    ("Step 1", "State the capital expenditure proposal clearly", "Formal request for £800 capital funding to convert the unused South Lawn courtyard into a secure sensory garden.", "Clear Proposal Opening (L2.21)"),
                    ("Step 2", "Anchor proposal to clinical outcomes and CQC inspection criteria", "Link sensory horticulture to reduced resident agitation, non-pharmacological therapy, and the upcoming CQC 'Responsive' and 'Well-Led' inspection domains.", "Strategic Alignment (L2.22)"),
                    ("Step 3", "Emphasise cost-effectiveness and community co-funding", "Highlight that local garden centres have donated plants and staff volunteers will complete the planting over one weekend.", "Financial Persuasion")
                ],
                "final_answer": "'I am writing to submit a capital expenditure proposal for £800 to construct a secure therapeutic sensory garden on the South Lawn courtyard. Clinical research demonstrates that outdoor sensory stimulation significantly reduces sundowning agitation among residents living with moderate-to-severe dementia, while directly strengthening our evidence portfolio for our upcoming CQC inspection.<br><br>To minimise costs to the Trust, local suppliers have already donated raised timber planters and sensory herbs free of charge; consequently, the £800 budget is required solely for non-slip pathway surfacing and a wheelchair-accessible bench.'",
                "tutor_tip": "Citing clinical benefits, CQC inspection standards, and cost mitigation proves to the examiner that you understand how real workplace proposals succeed."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing a Generic School Essay Instead of a Workplace Document",
                "desc": "If asked to write an internal workplace memo or incident report, writing a detached academic essay ('In this essay I will discuss...') loses format and context marks.",
                "fix": "Always adopt the exact document format (Memo, Email, Letter, Report) and speak directly from your assigned workplace role."
            },
            {
                "title": "Ignoring Financial or Practical Constraints",
                "desc": "Proposing that a small local charity should 'build a brand-new £5 million swimming pool next week' shows poor vocational realism.",
                "fix": "Keep your recommendations practical, phased, and cost-conscious (e.g. a 4-week pilot, staff rota adjustments, or applying for a local council grant)."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "You are a warehouse supervisor writing to senior management requesting anti-fatigue rubber floor mats for staff working on the packing line. Write two sentences that justify this request using workplace health and productivity priorities.",
                "solution_steps": "1. Sentence 1 (Health & Safety): Link standing on concrete floors for 8 hours to joint strain and sickness absence.<br>2. Sentence 2 (Productivity & Cost): Explain how anti-fatigue mats improve packing speed and pay for themselves through reduced agency cover costs.",
                "correct_answer": "'Installing ergonomic anti-fatigue floor mats along Packing Lines 1 to 4 will significantly reduce lower-back and joint strain for operatives standing on concrete floors throughout eight-hour shifts. Furthermore, reducing musculoskeletal sickness absence by just three shifts per quarter will fully offset the £450 equipment cost while maintaining peak dispatch throughput.'",
                "tutor_tip": "Always connect employee wellbeing directly to reduced absenteeism and operational performance."
            },
            {
                "marks": "3 Marks",
                "question": "Rewrite this weak student draft so it fits the vocational context of a Dental Practice Manager writing to patients about a new SMS appointment reminder system:<br><em>'We are starting text reminders next month because loads of patients keep forgetting to turn up and it wastes the dentist's time and costs us money.'</em>",
                "solution_steps": "1. Remove blaming/hostile tone ('loads of patients keep forgetting', 'wastes time').<br>2. Frame the SMS system positively around patient convenience and making urgent emergency slots available for others.<br>3. Explain clearly how patients can reply to confirm or reschedule.",
                "correct_answer": "'From 1 November, Oakridge Dental Practice is introducing a free automated SMS reminder service to help you manage your routine check-ups conveniently. You will receive a text message 48 hours before your appointment, allowing you to confirm your attendance or reschedule with a single reply so that unused clinical slots can be offered to patients requiring urgent dental care.'",
                "tutor_tip": "When writing to customers or patients, frame policy changes around improved service and convenience rather than scolding them."
            },
            {
                "marks": "4 Marks",
                "question": "You are an Apprentice Coordinator at an engineering firm. Draft a 3-paragraph email to Department Heads proposing a 'Buddy Mentorship Scheme' where experienced technicians mentor first-year apprentices for one hour a week.",
                "solution_steps": "1. Paragraph 1: State purpose of email and current challenge (first-year apprentice workshop errors and confidence).<br>2. Paragraph 2: Explain how the 1-hour weekly buddy check-in improves safety compliance and speeds up skill acquisition.<br>3. Paragraph 3: Request each Department Head to nominate two senior technicians by Friday.",
                "correct_answer": "To: Department Heads<br>Subject: Proposal – First-Year Apprentice Buddy Mentorship Scheme<br><br>Dear Colleagues,<br><br>I am writing to propose launching a structured Buddy Mentorship Scheme pairing each of our eight first-year engineering apprentices with an experienced workshop technician for one hour per week.<br><br>Providing dedicated on-the-job guidance during the first six months will reinforce machinery safety protocols, reduce component wastage, and accelerate apprentice progression toward independent work.<br><br>Please could each Department Head nominate two experienced technicians from your team by Friday 23 October so we can schedule a brief 20-minute mentor briefing next week?<br><br>Kind regards,<br>Samira Patel, Apprentice Coordinator",
                "tutor_tip": "Notice how the email addresses what Department Heads care about: workshop safety, reduced material wastage, and minimal time disruption."
            }
        ]
    },

    # 4. Audience, Tone & Register
    {
        "filename": "writing-assessing-audience.html",
        "clean_topic": "Audience, Tone & Register",
        "intro_lead": "Calibrate your writing tone, register, sentence structure, and vocabulary to match your exact readership: senior executives, external regulators, workplace peers, or members of the public.",
        "next_file": "writing-form-presentational-and-language-features.html",
        "next_name": "Format & Conventions",
        "spec_points": [
            ("L1.22 / L2.22", "Write with a clear awareness of audience, adapting tone, register, and vocabulary appropriately."),
            ("L2.23", "Select sophisticated vocabulary and syntactic structures tailored to formal, semi-formal, and public audiences.")
        ],
        "golden_rules": [
            {
                "icon": "fa-users-gear",
                "title": "Golden Rule 1: Establish the Exact Register in Sentence One and Never Slip",
                "desc": "Never mix registers midway through a task. A formal letter to a Council Director or Hospital CEO must maintain courteous, objective Standard English from the opening salutation to the final full stop.",
                "badge": "Formal = Objective, courteous, zero slang. Semi-formal = Collaborative, engaging, respectful."
            },
            {
                "icon": "fa-ban",
                "title": "Golden Rule 2: Eliminate Contractions in Formal Letters and Reports",
                "desc": "In formal letters, job applications, and official reports, always write verbs in full: 'do not' instead of 'don't', 'cannot' instead of 'can't', 'it is' instead of 'it's', 'will not' instead of 'won't'.",
                "badge": "Zero contractions in formal documents = immediate boost to register & SPaG marks."
            }
        ],
        "skills": [
            {
                "title": "The 3-Tier Audience Register Calibration Matrix",
                "summary": "How to adapt your greeting, vocabulary, and tone across the three main exam readerships.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Target Audience</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Required Register &amp; Tone</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Model Phrasing Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Senior Management / Council / Regulator</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Highly Formal:</strong> Courteous, objective, evidence-driven, zero contractions, no exclamation marks.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I am writing to formally request an urgent review of traffic safety measures outside St Luke's Primary School."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Workplace Colleagues / Team Members</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Semi-Formal Professional:</strong> Cooperative, clear, constructive, direct address (<em>we, our team</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Please ensure all portable electrical equipment is unplugged and stored in Bay 2 before 17:30 on Friday."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. General Public / Patients / Community Blog</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Accessible &amp; Engaging:</strong> Warm, empathetic, jargon-free, persuasive, inclusive.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Whether you are a complete beginner or a seasoned runner, our Saturday Park Walk offers a welcoming morning for the whole family."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Assertive vs Aggressive Tone in Formal Complaints",
                "summary": "How to complain firmly and persuasively in an exam task without sounding rude or abusive.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Aggressive / Emotional Rant (Penalised by Examiners):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"Your delivery driver was totally useless and rude!! He dumped my £400 washing machine in the rain and drove off! You lot are a disgrace and I want my money back right now!!"</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Assertive, Dignified Formal Complaint (Full Marks):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"I am writing to express my extreme dissatisfaction regarding the delivery of my washing machine (Order Ref: WM-409) on 12 October. Despite paying £25 for indoor installation, the courier left the unpackaged appliance outside in heavy rain without ringing the doorbell. Consequently, I request a full refund of the £25 delivery fee and an inspection of the water-damaged packaging."</em>
                  </div>
                </div>
                """
            },
            {
                "title": "High-Value Vocabulary Upgrades for Formal Tasks",
                "summary": "Replace everyday conversational words with formal Standard English equivalents.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Instead of <em>"ask for"</em> → write <strong>"request"</strong> or <strong>"enquire about"</strong>.</li>
                    <li>Instead of <em>"tell you about"</em> → write <strong>"inform you of"</strong> or <strong>"bring to your attention"</strong>.</li>
                    <li>Instead of <em>"fix the problem"</em> → write <strong>"rectify the issue"</strong> or <strong>"resolve this matter"</strong>.</li>
                    <li>Instead of <em>"really bad"</em> → write <strong>"unacceptable"</strong>, <strong>"detrimental"</strong>, or <strong>"substandard"</strong>.</li>
                    <li>Instead of <em>"help out"</em> → write <strong>"assist"</strong>, <strong>"facilitate"</strong>, or <strong>"support"</strong>.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Courteous Email to Colleagues About Shared Kitchen Hygiene",
                "marks": "Level 1 Audience & Tone Benchmark (3 Marks)",
                "context": "Office Administration & Team Etiquette",
                "question": "Rewrite this rude note left on the staffroom fridge as a polite, semi-formal email to all office staff:<br><em>'Whoever keeps leaving dirty mugs in the sink and mouldy milk in the fridge needs to grow up! Clean up your own mess or the manager will ban us from using the kitchen!'</em>",
                "steps": [
                    ("Step 1", "Replace hostile accusations with a collaborative team greeting", "Use a constructive subject line and address colleagues collectively without pointing fingers.", "Appropriate Semi-Formal Tone (L1.22)"),
                    ("Step 2", "State the two hygiene rules clearly and politely", "Ask staff to place used mugs directly into the dishwasher and dispose of expired milk every Friday.", "Clear Actionable Requests"),
                    ("Step 3", "Explain the shared benefit for the team", "Keeping the breakroom clean ensures a pleasant environment for everyone during lunch breaks.", "Positive Closing Register")
                ],
                "final_answer": "To: All Office Staff<br>Subject: Keeping Our Shared Staff Kitchen Clean and Tidy<br><br>Dear Everyone,<br><br>As our staff kitchen is busy during lunch breaks, please could we all work together to keep the area clean and hygienic?<br><br>Please rinse your mugs and place them straight into the dishwasher after use rather than leaving them in the sink. Additionally, our cleaning team will empty the refrigerator every Friday at 16:30, so please label your food containers and remove any expired milk before the weekend.<br><br>Thank you for your cooperation in keeping our breakroom pleasant for the whole team.<br><br>Best regards,<br>Office Facilities Team",
                "tutor_tip": "Notice how using inclusive pronouns ('our kitchen', 'work together') achieves full compliance without alienating colleagues."
            },
            {
                "title": "Level 2 Model: Council Environmental Health Formal Complaint",
                "marks": "Level 2 Formal Register Benchmark (4 Marks)",
                "context": "Public Environmental Health & Statutory Nuisance",
                "question": "Draft the opening two paragraphs of a formal complaint letter to Ms Henderson, Head of Environmental Services, regarding commercial fly-tipping behind a residential care centre.",
                "steps": [
                    ("Step 1", "Select formal salutation and state immediate grievance", "Use formal greeting ('Dear Ms Henderson,') and authoritative opening sentence stating exact location.", "Formal Salutation & Purpose (L2.22)"),
                    ("Step 2", "Maintain dignified, objective complaint register", "Describe the hazard factually using precise vocabulary ('obstructing emergency access', 'attracting vermin') without slang or exclamation marks.", "Sustained Formal Register (L2.23)"),
                    ("Step 3", "Specify requested statutory action and timeframe", "Request an Environmental Health enforcement officer visit and clearance within 48 hours.", "Assertive Call to Action")
                ],
                "final_answer": "Dear Ms Henderson,<br><br>I am writing in my capacity as Facilities Manager at St Mary’s Residential Care Centre to register an urgent formal complaint regarding persistent commercial fly-tipping in the service lane adjacent to our rear fire exits.<br><br>Over the past fortnight, unknown contractors have deposited broken plasterboard, rusted metal sheeting, and unsealed paint canisters across the access driveway. Not only does this hazardous waste attract vermin within metres of our kitchen store, but it also severely obstructs emergency ambulance access for our frail residents. I therefore urge your department to dispatch an enforcement crew to clear the lane within 48 hours and install CCTV signage to deter further offences.<br><br>Yours sincerely,<br>David Clarke, Facilities Manager",
                "tutor_tip": "Notice how the tone is firm, urgent, and authoritative without ever becoming rude. Examiners reward precise vocabulary ('in my capacity as', 'obstructs emergency ambulance access')."
            }
        ],
        "examiner_traps": [
            {
                "title": "Inconsistent Tone Shifts Midway Through a Response",
                "desc": "Starting formally with 'Dear Sir or Madam, I am writing to complain...' and then slipping into 'Anyway, it's a total rip-off and you need to sort it ASAP' in Paragraph 3 ruins register consistency.",
                "fix": "During your final 5-minute proofread, check that your last paragraph is just as formal and controlled as your first."
            },
            {
                "title": "Using Text-Speak or Multiple Exclamation Marks (!!!)",
                "desc": "Writing 'u', 'asap', 'cos', or ending sentences with '!!' in a Functional Skills exam immediately caps your SPaG and register marks.",
                "fix": "Write every word out in full Standard English and use a single full stop at the end of declarative sentences."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Explain why writing: <em>'Hey guys, grab your big coats cos the ward heating is busted today lol'</em> is inappropriate for an official hospital staff email memo, and rewrite it in an appropriate professional register.",
                "solution_steps": "1. Critique: Identify the casual slang ('Hey guys', 'cos', 'busted', 'lol') which is unprofessional for clinical workplace records.<br>2. Rewrite: Provide a clear, polite semi-formal staff advisory.",
                "correct_answer": "Critique: Uses informal slang ('cos', 'busted', 'lol') and casual greeting ('Hey guys') which undermine professional communication.<br>Professional Rewrite: 'Please be advised that the Ward 4 heating system is currently undergoing emergency repair; staff are permitted to wear plain navy thermal fleeces during today's shift.'",
                "tutor_tip": "Always provide both the brief explanation of why the original fails and the complete rewritten sentence."
            },
            {
                "marks": "3 Marks",
                "question": "Rewrite this overly aggressive complaint paragraph into an assertive, formal Level 2 register suitable for a letter to a Training Provider Director:<br><em>'Your tutor didn't bother turning up for our first-aid exam on Tuesday and nobody even phoned us! Seven of my staff wasted a whole morning sitting in an empty room! You better give us our £700 back today!'</em>",
                "solution_steps": "1. Replace emotional accusations ('didn't bother turning up', 'wasted a whole morning') with objective facts.<br>2. Eliminate exclamation marks and aggressive demands ('You better give us').<br>3. State the financial impact and formal request for a full £700 refund or rescheduled sitting.",
                "correct_answer": "'Regrettably, your assigned assessor failed to attend our scheduled First-Aid at Work examination on Tuesday 10 October, and no prior cancellation notice was communicated to our office. Consequently, seven members of our care team were removed from clinical duties for an entire morning without achieving their certification. I therefore request an immediate full refund of the £700 booking fee or a priority rescheduled assessment at our premises within seven days.'",
                "tutor_tip": "Words like 'Regrettably' and 'Consequently' allow you to express strong dissatisfaction while remaining 100% professional."
            },
            {
                "marks": "3 Marks",
                "question": "Adapt this technical clinical instruction so it is warm, accessible, and easy to understand for an anxious patient reading a hospital pre-admission leaflet:<br><em>'Patients scheduled for general anaesthesia must maintain nil-by-mouth status from 00:00 prior to admission; non-compliance will result in immediate cancellation of the surgical procedure.'</em>",
                "solution_steps": "1. Translate technical jargon ('general anaesthesia', 'nil-by-mouth status', 'non-compliance') into plain, reassuring English.<br>2. Explain clearly that patients must not eat food or drink liquids after midnight.<br>3. Explain gently why this rule keeps them safe during their operation.",
                "correct_answer": "'To keep you completely safe during your operation, it is essential that your stomach is empty before you are given your anaesthetic. Please do not eat any food or drink any liquids (including water, tea, or chewing gum) after midnight on the night before your surgery. If you accidentally eat or drink after midnight, we may need to rearrange your operation for another day for your own safety.'",
                "tutor_tip": "Explaining the safety reason ('so your stomach is empty') makes public leaflets reassuring rather than intimidating."
            }
        ]
    },

    # 5. Format & Conventions: Letters, Emails, Articles & Reports
    {
        "filename": "writing-form-presentational-and-language-features.html",
        "clean_topic": "Format & Conventions: Letters, Emails, Articles & Reports",
        "intro_lead": "Execute the exact layout, salutations, complimentary closes, subject lines, headlines, and subheadings required for formal letters, emails, articles, and workplace reports.",
        "next_file": "writing-organisational-markers.html",
        "next_name": "Organisational Markers",
        "spec_points": [
            ("L1.23 / L2.23", "Write in a variety of forms, utilising appropriate format conventions, layouts, and structural features."),
            ("L2.24", "Demonstrate full mastery of professional conventions across formal letters, emails, articles, blogs, and reports.")
        ],
        "golden_rules": [
            {
                "icon": "fa-stamp",
                "title": "Golden Rule 1: Master the Non-Negotiable Letter Sign-Off Rule",
                "desc": "If you address a named person (e.g. 'Dear Mr Phillips' or 'Dear Mrs Patel'), you MUST sign off 'Yours sincerely,'. If you do not know the recipient's name (e.g. 'Dear Sir or Madam,' or 'Dear Editor,'), you MUST sign off 'Yours faithfully,'.",
                "badge": "Named Recipient = Yours sincerely | Sir or Madam = Yours faithfully (Remember: never two S's together!)"
            },
            {
                "icon": "fa-heading",
                "title": "Golden Rule 2: Articles Need Headlines; Reports Need Numbered Sections; Emails Need Subject Lines",
                "desc": "Examiners deduct format marks immediately if an article lacks a headline, a report lacks subheadings, or an email lacks To/Subject lines.",
                "badge": "Article = Headline + Subheadings | Report = Title + Numbered Headings | Email = To + Subject + Sign-off"
            }
        ],
        "skills": [
            {
                "title": "Master Layout Blueprint: All 5 Functional Skills Exam Formats",
                "summary": "Memorise the exact structural checklist for every document type that can appear in Task 1 or Task 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Document Format</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Top Header Requirements</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Body &amp; Sign-Off Conventions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Formal Letter</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1. Your address (top right)<br>2. Date beneath your address<br>3. Recipient name/title &amp; address (left)<br>4. Salutation (<em>Dear Mr... / Dear Sir or Madam,</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">3–4 formal paragraphs.<br>Close: <em>Yours sincerely,</em> (named) or <em>Yours faithfully,</em> (unnamed) + Your Full Name.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Workplace Email</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>To:</strong> recipient@organisation.co.uk<br><strong>Subject:</strong> Clear, specific summary of email topic<br>Salutation (<em>Dear Sarah, / Dear Mr Davies,</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Focused paragraphs (plus bullet points if listing items).<br>Close: <em>Kind regards,</em> or <em>Best wishes,</em> + Name &amp; Job Title.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Formal Report</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Title:</strong> REPORT ON [TOPIC]<br><strong>To:</strong> | <strong>From:</strong> | <strong>Date:</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Numbered subheadings: <em>1.0 Introduction, 2.0 Key Findings, 3.0 Recommendations</em> (with bulleted action points).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. Magazine / Website Article</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Catchy Headline</strong> (bold/underlined)<br>Optional Byline: <em>By [Your Name]</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Engaging hook opening, 2–3 thematic subheadings, rhetorical questions, motivating final call to action.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">5. Witness Statement / Account</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Title:</strong> Formal Incident / Witness Statement<br><strong>Name:</strong> | <strong>Role:</strong> | <strong>Date of Incident:</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Chronological past-tense paragraphs detailing exact times and observations.<br>Close: <em>Signed: [Name] | Date: [Date]</em>.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Visual Template: How to Lay Out a Formal Letter in the Exam Box",
                "summary": "Exact line-by-line placement of addresses, dates, and salutations.",
                "content_html": """
                <div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:8px; padding:20px; margin:16px 0; font-family:monospace; font-size:0.93rem; line-height:1.6; color:#1e293b;">
                  <div style="text-align:right; margin-bottom:12px;">
                    14 Oakfield Avenue<br>
                    Headington<br>
                    Oxford<br>
                    OX3 9BP<br><br>
                    14 October 2026
                  </div>
                  <div style="text-align:left; margin-bottom:14px;">
                    Ms Samantha Davies<br>
                    Director of Estates<br>
                    Master Healthcare Trust<br>
                    Headley Way, Oxford<br>
                    OX3 9DU
                  </div>
                  <div style="margin-bottom:12px;">
                    <strong>Dear Ms Davies,</strong>
                  </div>
                  <div style="margin-bottom:12px;">
                    <strong>Re: Proposal for Secure Staff Cycle Storage at Churchill Wing</strong><br><br>
                    [Paragraph 1: State clear purpose of the letter...]<br>
                    [Paragraph 2: Detailed evidence and operational impact...]<br>
                    [Paragraph 3: Practical recommendations and next steps...]
                  </div>
                  <div>
                    <strong>Yours sincerely,</strong><br>
                    Subi Rahman<br>
                    Senior Physiotherapy Assistant
                  </div>
                </div>
                """
            },
            {
                "title": "Language Features Matched to Format Types",
                "summary": "Choosing the right rhetorical and grammatical tools for articles vs reports.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Articles &amp; Blogs:</strong> Use direct address (<em>"Have you ever wondered...?"</em>), inclusive pronouns (<em>"our neighbourhood"</em>), short punchy subheadings, and a lively, motivating tone.</li>
                    <li><strong>Formal Reports:</strong> Avoid personal emotion or rhetorical questions. Use objective third-person phrasing (<em>"The audit revealed that 68% of respondents..."</em>) and numbered recommendations.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Complete Formal Letter Layout & Opening",
                "marks": "Level 1 Format Conventions Benchmark (4 Marks)",
                "context": "Consumer Refund Complaint Letter",
                "question": "You bought a laptop from TechMart Store (45 High Street, Leeds, LS1 4BR) last Saturday, but the battery does not hold a charge. Set out the full formal letter header (using your address: 12 Park Lane, Leeds, LS2 9AA), date, salutation to the Store Manager (unnamed), opening paragraph, and sign-off.",
                "steps": [
                    ("Step 1", "Position sender address and date on the top right", "Write 12 Park Lane, Leeds, LS2 9AA followed by today's date (14 October 2026).", "Sender Address & Date (L1.23)"),
                    ("Step 2", "Position recipient address on the left and select salutation", "Write The Store Manager, TechMart Store, 45 High Street, Leeds, LS1 4BR, followed by 'Dear Sir or Madam,'.", "Recipient Address & Salutation"),
                    ("Step 3", "Draft opening paragraph and match sign-off", "State purchase details and fault, then close with 'Yours faithfully,' because the manager's name is unknown.", "Matching Sign-Off Rule")
                ],
                "final_answer": "<div style='text-align:right;'>12 Park Lane<br>Leeds<br>LS2 9AA<br><br>14 October 2026</div><br>The Store Manager<br>TechMart Store<br>45 High Street<br>Leeds<br>LS1 4BR<br><br>Dear Sir or Madam,<br><br>I am writing to formally complain about a faulty Lenovo IdeaPad laptop (Receipt No. TM-8821) that I purchased from your Leeds High Street branch on Saturday 10 October for £429. Despite charging the device overnight, the battery drains completely within fifteen minutes of unplugging the power cable. Under the Consumer Rights Act, I would like to request a full refund or an immediate replacement laptop.<br><br>Yours faithfully,<br>Jamie Clarke",
                "tutor_tip": "Never skip addresses in a formal letter! Even in an onscreen exam where alignment is tricky, typing your address, a blank line, the date, a blank line, and the recipient's address earns automatic format marks."
            },
            {
                "title": "Level 2 Model: NHS Staff Wellbeing Article with Headline & Subheadings",
                "marks": "Level 2 Article Format & Conventions Benchmark (5 Marks)",
                "context": "Internal NHS Trust Magazine",
                "question": "Draft the headline, sub-deck, opening paragraph, and first subheaded section of an article for an NHS staff newsletter promoting trained Mental Health First Aiders across clinical wards.",
                "steps": [
                    ("Step 1", "Craft an engaging headline and sub-deck", "<strong>Headline:</strong> Caring for the Carers: Why Mental Health First Aiders Matter on Every Ward<br><strong>Sub-deck:</strong> <em>How trained peer champions are transforming frontline clinical support.</em>", "Article Headline & Hook (L2.23)"),
                    ("Step 2", "Draft a compelling hook opening paragraph", "Open with a direct rhetorical question acknowledging the emotional pressures of frontline healthcare.", "Audience Engagement"),
                    ("Step 3", "Introduce a bold thematic subheading and evidence paragraph", "<strong>Subheading:</strong> Confidential Support Without Waiting Lists<br>Explain how peer champions provide immediate signposting during shifts.", "Structural Subheadings (L2.24)")
                ],
                "final_answer": "<strong>Caring for the Carers: Why Mental Health First Aiders Matter on Every Ward</strong><br><em>How trained peer champions are transforming frontline clinical support — By Nadia Hassan</em><br><br>Every day across our acute wards, dedicated nurses and healthcare assistants deliver extraordinary compassion under intense pressure. Yet who listens when the caregivers themselves feel overwhelmed after a traumatic shift? This month, our Trust is proud to launch a network of forty accredited Mental Health First Aiders.<br><br><strong>Confidential Support Right on Your Ward</strong><br>Unlike external counselling services that require formal referrals, our peer champions wear a distinctive green lanyard and are available for a confidential ten-minute conversation during your shift; furthermore, they can signpost you directly to occupational wellbeing resources.",
                "tutor_tip": "Formatting your article with a bold headline, a byline, a rhetorical hook, and distinct subheadings immediately secures full layout marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting the Subject Line in Email Tasks",
                "desc": "Writing an email response without 'To:' and 'Subject:' lines at the top automatically forfeits format marks in Pearson Edexcel and City & Guilds exams.",
                "fix": "Even if the onscreen exam box doesn't have pre-printed To/Subject boxes, always type 'To:' and 'Subject:' on the first two lines of your email."
            },
            {
                "title": "Signing Off an Article or Report with 'Yours sincerely'",
                "desc": "Ending a magazine article or a workplace report with 'Yours sincerely, John' shows the examiner you have confused letter conventions with article/report conventions.",
                "fix": "Only letters and formal emails use 'Yours sincerely / faithfully'. Articles end with a call to action; reports end with 'Report compiled by: [Name, Role]'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "State the exact salutation and complimentary close (sign-off) required for each formal letter below:<br>1. A letter addressed to <strong>Ms Samantha Davies, Operations Director</strong>.<br>2. A letter addressed to <strong>The Customer Services Manager</strong> (name unknown).",
                "solution_steps": "1. Named recipient (Ms Davies) takes 'Dear Ms Davies,' and 'Yours sincerely,'.<br>2. Unnamed recipient takes 'Dear Sir or Madam,' and 'Yours faithfully,'.",
                "correct_answer": "1. Salutation: Dear Ms Davies, | Sign-off: Yours sincerely,<br>2. Salutation: Dear Sir or Madam, | Sign-off: Yours faithfully,",
                "tutor_tip": "Memory rule: Never put two S's together (Sir/Madam never pairs with Sincerely!)."
            },
            {
                "marks": "3 Marks",
                "question": "You are asked to write an email to all warehouse staff reminding them that the annual fire drill takes place tomorrow at 10:30 am and that everyone must assemble at Point B. Write the exact email header block (To, Subject, Salutation) and the opening sentence.",
                "solution_steps": "1. Write 'To: All Warehouse Staff (staff@warehouselogistics.co.uk)'.<br>2. Write a specific, informative 'Subject:' line including the time.<br>3. Include a professional greeting and clear opening sentence.",
                "correct_answer": "To: allstaff@warehouselogistics.co.uk<br>Subject: Mandatory Annual Fire Drill – Tomorrow at 10:30 am (Assembly Point B)<br><br>Dear Colleagues,<br><br>Please be reminded that our mandatory annual warehouse fire evacuation drill will take place tomorrow morning at 10:30 am prompt, and all staff must evacuate immediately to Assembly Point B in the north car park.",
                "tutor_tip": "A strong Subject line summarizes the entire purpose of the email in 6 to 10 words."
            },
            {
                "marks": "4 Marks",
                "question": "A student wrote a workplace report on canteen energy waste as one giant paragraph starting with <em>'Dear Manager, I walked around the kitchen and saw the ovens left on...'</em>.<br>Rewrite the opening of this report using correct formal report conventions (Report Title, To/From/Date block, and Section 1.0 Introduction).",
                "solution_steps": "1. Remove the letter greeting ('Dear Manager') and casual first-person storytelling.<br>2. Add a formal Report Title and To/From/Date metadata block.<br>3. Add numbered subheading '1.0 Introduction' and write an objective opening statement.",
                "correct_answer": "<strong>REPORT ON REDUCING ENERGY WASTE IN THE STAFF CANTEEN</strong><br><strong>To:</strong> Facilities Director<br><strong>From:</strong> Environmental Compliance Officer<br><strong>Date:</strong> 14 October 2026<br><br><strong>1.0 Introduction &amp; Audit Scope</strong><br>This report presents the findings of a five-day energy audit conducted in the main staff canteen kitchen between 5 and 9 October 2026, identifying significant electricity wastage caused by commercial ovens and chillers remaining switched on outside operating hours.",
                "tutor_tip": "Reports never start with 'Dear...'. Always use a bold Title, To/From/Date lines, and numbered section headings."
            }
        ]
    },

    # 6. Organisational Markers & Headings
    {
        "filename": "writing-organisational-markers.html",
        "clean_topic": "Organisational Markers & Headings",
        "intro_lead": "Deploy clear headings, numbered subheadings, bulleted lists, bold lead-ins, and callout boxes to structure long-form workplace reports, instructional guides, and policy documents.",
        "next_file": "writing-linking-up-your-answer.html",
        "next_name": "Paragraphing & Cohesion",
        "spec_points": [
            ("L1.24 / L2.24", "Use organisational markers and structural features to signpost information clearly for the reader."),
            ("L2.25", "Structure complex technical reports and procedural guides using systematic numerical and thematic headings.")
        ],
        "golden_rules": [
            {
                "icon": "fa-signs-post",
                "title": "Golden Rule 1: Organisational Markers Are Visual Signposts for Busy Readers",
                "desc": "A busy ward manager, safety inspector, or examiner should be able to grasp the entire architecture of your report or guide in 5 seconds just by scanning your bold subheadings and bullet lead-ins.",
                "badge": "Use informative subheadings (e.g. '2.0 Cost Savings of LED Lighting', not just 'Part 2')."
            },
            {
                "icon": "fa-list-ol",
                "title": "Golden Rule 2: Numbered Lists for Chronological Steps; Bullet Points for Unordered Lists",
                "desc": "If steps MUST happen in strict time order (e.g. fire evacuation, medication administration), use numbers (1, 2, 3). If items are an unordered set of points or features (e.g. required PPE items), use bullet points (•).",
                "badge": "1, 2, 3 = Mandatory chronological sequence | • Bullets = Unordered features or recommendations"
            }
        ],
        "skills": [
            {
                "title": "The Professional Report Heading Hierarchy",
                "summary": "How to structure Level 2 business, safety, and audit reports using numbered sections.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Main Document Title:</strong> Capitalised or bold at the very top (e.g. <em>REPORT: WAREHOUSE FORKLIFT SAFETY AUDIT</em>).</li>
                    <li><strong>1.0 Executive Summary / Purpose:</strong> 2–3 sentences stating why the investigation was conducted.</li>
                    <li><strong>2.0 Key Operational Findings:</strong> Divided into clear thematic points (e.g. <em>2.1 Pedestrian Walkway Signage, 2.2 Lighting Levels</em>).</li>
                    <li><strong>3.0 Risk &amp; Cost Evaluation:</strong> Analyses the impact of leaving the issue unresolved.</li>
                    <li><strong>4.0 Actionable Recommendations:</strong> A bulleted or numbered list specifying <strong>who</strong> must do <strong>what</strong> by <strong>when</strong>.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Writing Grammatically Parallel Bullet Points with Bold Lead-Ins",
                "summary": "How to use bullet lists in Functional Skills exams without losing SPaG marks for sentence fragments.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Weak Shopping-List Bullets (Loses SPaG Marks for Fragments):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    • new locks on doors<br>
                    • staff need training on Tuesdays<br>
                    • buying 4 CCTV cameras
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> High-Scoring Parallel Bullets with Bold Lead-Ins (Full SPaG &amp; Format Marks):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    To upgrade depot security immediately, the estates team should implement three measures:<br>
                    • <strong>Keypad Door Locks:</strong> Install digital combination locks on all external stockroom doors by 30 November.<br>
                    • <strong>Mandatory Staff Briefings:</strong> Deliver a 20-minute security refresher during Tuesday morning shift handovers.<br>
                    • <strong>Perimeter CCTV Coverage:</strong> Mount four motion-activated infrared cameras overlooking Loading Bay 1.
                  </div>
                </div>
                """
            },
            {
                "title": "Where to Use Organisational Markers (And Where NOT To)",
                "summary": "Matching organisational features to the right exam text format.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Format</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Recommended Organisational Markers</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">What to Avoid</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Formal Report / Info Sheet</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Main Title, numbered subheadings (1.0, 2.0), bulleted recommendations, bold key terms.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Writing unbroken walls of prose without headings.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Article / Blog Post</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Catchy Headline, 2–3 thematic subheadings, optional short bullet box of top tips.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Robotic numbered headings like '1.0 Introduction'.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Formal Letter</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Subject line (<em>Re: ...</em>) after salutation, clear indented or spaced paragraphs.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Do not put article subheadings inside a short formal letter.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Sequenced Fire Evacuation Instruction Notice",
                "marks": "Level 1 Organisational Markers Benchmark (3 Marks)",
                "context": "Workplace Health & Safety Noticeboard",
                "question": "Convert these disorganised notes into a clearly structured staff instruction notice using a bold title, a numbered sequence for the evacuation steps, and a final warning note:<br><em>'When you hear the continuous siren leave the building right away by the green fire exits. Don't stop to pick up bags or coats and never use the lift. Walk to Car Park A and wait for the Fire Warden to call your name.'</em>",
                "steps": [
                    ("Step 1", "Create a clear, authoritative main heading", "<strong>EMERGENCY FIRE EVACUATION PROCEDURE</strong>", "Clear Heading (L1.24)"),
                    ("Step 2", "Use a numbered list (1 to 3) for the chronological evacuation steps", "Because the actions must happen in strict order (Hear alarm → Exit via stairs → Register at assembly point), use numbers 1, 2, 3.", "Sequential Numbering"),
                    ("Step 3", "Place the prohibitions in a bold warning callout at the bottom", "Highlight the 'Do not use lifts or collect personal belongings' rule clearly.", "Visual Signposting")
                ],
                "final_answer": "<strong>EMERGENCY FIRE EVACUATION PROCEDURE</strong><br>If the continuous fire siren sounds, all staff and visitors must follow these three steps immediately:<br>1. Stop work at once and leave the building calmly via the nearest illuminated green fire exit.<br>2. Walk directly to Assembly Point A in the main front car park.<br>3. Remain in your department group until the Fire Warden has completed the roll call.<br><br><strong>IMPORTANT SAFETY WARNING:</strong> Never use the passenger lifts during an alarm, and do not return to your desk to collect coats or personal bags.",
                "tutor_tip": "Using numbered steps (1, 2, 3) for chronological actions and a bold warning box for prohibitions makes safety instructions instant to follow."
            },
            {
                "title": "Level 2 Model: Hospital Clinical Waste Segregation SOP",
                "marks": "Level 2 Organisational Markers Benchmark (4 Marks)",
                "context": "NHS Infection Control Standard Operating Procedure",
                "question": "Format a guidance section for hospital domestic and auxiliary staff detailing the 3-tier waste bag colour-coding system (Yellow, Orange, Black) and sharps disposal rule using professional organisational markers.",
                "steps": [
                    ("Step 1", "Create an authoritative section heading and introductory colon clause", "<strong>Section 2.0: Clinical Waste Segregation Protocols</strong> followed by a complete lead-in sentence ending with a colon.", "Section Heading & Colon (L2.24)"),
                    ("Step 2", "Use bulleted bold lead-ins with complete sentences for the 3 bag colours", "Detail Yellow (infectious incineration), Orange (clinical autoclaving), and Black (domestic general waste).", "Parallel Bulleted Prose (L2.25)"),
                    ("Step 3", "Insert a high-visibility mandatory compliance callout", "Add a boxed or bold directive regarding rigid yellow sharps bins.", "Compliance Callout")
                ],
                "final_answer": "<strong>2.0 Clinical Waste Segregation Protocols</strong><br>To maintain strict CQC infection-control compliance, all ward staff must segregate waste according to the three colour-coded categories below:<br>• <strong>Yellow Bags (Highly Infectious Waste):</strong> Use exclusively for dressings, swabs, and PPE contaminated with infectious bodily fluids requiring high-temperature incineration.<br>• <strong>Orange Bags (Standard Clinical Waste):</strong> Use for non-infectious clinical items such as disposable aprons, wipes, and incontinence pads treated via autoclaving.<br>• <strong>Black Bags (Domestic General Refuse):</strong> Use strictly for non-clinical waste including paper towels, food packaging, and clean cardboard.<br><br><strong>[CRITICAL SAFETY DIRECTIVE]:</strong> Needles, lancets, and scalpel blades must be deposited immediately into rigid yellow BS-approved sharps bins; never place sharps inside plastic waste bags.",
                "tutor_tip": "Notice how every bullet point starts with a bold category label followed by a colon and a complete grammatical sentence. This earns top marks for both layout and SPaG."
            }
        ],
        "examiner_traps": [
            {
                "title": "Turning Your Entire Exam Answer into Bullet Point Fragments",
                "desc": "If 80% of your response consists of 3-word bullet points without full sentences or paragraphs, examiners cannot award Level 2 grammar or cohesion marks.",
                "fix": "Limit bullet points to one specific section (such as Recommendations), and always write full, grammatically complete sentences inside each bullet."
            },
            {
                "title": "Using Subheadings That Don't Match the Paragraph Content",
                "desc": "Writing the subheading 'Cost Savings' and then spending the paragraph talking about staff parking permits confuses the reader and loses organisation marks.",
                "fix": "Ensure every sentence beneath a subheading directly addresses the topic promised in that heading."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Rewrite these unformatted notes into a structured workplace safety section with a bold heading and two grammatically complete bullet points:<br><em>'Workers need steel toe cap boots on the warehouse floor and also high-vis jackets must be worn at all times near forklift trucks.'</em>",
                "solution_steps": "1. Create a clear heading (e.g. Mandatory Warehouse PPE Regulations).<br>2. Write an introductory lead-in clause followed by two parallel, complete-sentence bullet points.",
                "correct_answer": "<strong>Mandatory Warehouse PPE Regulations</strong><br>All operatives entering the main distribution floor must comply with the following personal protective equipment rules:<br>• <strong>Safety Footwear:</strong> Steel toe-cap boots must be worn at all times across all warehouse storage and packing zones.<br>• <strong>High-Visibility Clothing:</strong> Fastened high-visibility vests or jackets are mandatory whenever working near active forklift transit lanes.",
                "tutor_tip": "Adding bold lead-ins ('Safety Footwear:', 'High-Visibility Clothing:') makes bullet points look like an authentic workplace policy document."
            },
            {
                "marks": "3 Marks",
                "question": "Explain whether you should use a <strong>numbered list (1, 2, 3)</strong> or <strong>unordered bullet points (•)</strong> for each workplace document below, and give the reason why:<br>Document A: The four stages of sterilising surgical instruments in an autoclave.<br>Document B: The four employee benefits offered in a company recruitment leaflet.",
                "solution_steps": "1. Analyse Document A: Sterilising instruments must follow a strict chronological sequence to be safe → Numbered list.<br>2. Analyse Document B: Employee benefits are a collection of features with no required time order → Bullet points.",
                "correct_answer": "Document A: Use a numbered list (1, 2, 3, 4) because sterilisation steps must be performed in a strict chronological sequence.<br>Document B: Use unordered bullet points (•) because employee benefits are separate features that do not happen in a sequence.",
                "tutor_tip": "Numbers = strict sequence where order matters; Bullets = non-sequential collection."
            },
            {
                "marks": "4 Marks",
                "question": "You are compiling the final section of a Level 2 Report titled <em>'Reducing Patient Waiting Times at Oakfield GP Surgery'</em>. Draft <strong>Section 3.0: Recommendations</strong> containing a brief lead-in sentence and three bulleted, actionable recommendations with bold lead-ins.",
                "solution_steps": "1. Write heading: '3.0 Strategic Recommendations'.<br>2. Write a formal introductory sentence ending with a colon.<br>3. Draft three full-sentence bullet points covering online triage, evening nurse clinics, and SMS cancellations.",
                "correct_answer": "<strong>3.0 Strategic Recommendations</strong><br>To reduce average appointment waiting times by 30% over the next quarter, the Practice Partnership should implement the following three measures:<br>• <strong>Digital Triage Portal:</strong> Launch an online symptom-checker form from 1 November so routine prescription renewals do not block morning telephone lines.<br>• <strong>Extended Nurse Practitioner Hours:</strong> Introduce two evening minor-illness clinics on Tuesdays and Thursdays until 19:30 for working patients.<br>• <strong>Automated SMS Cancellation Links:</strong> Send automated text reminders 24 hours prior to appointments, allowing patients to cancel unused slots with a single reply.",
                "tutor_tip": "Notice how each recommendation states the specific initiative, how it works, and the operational benefit."
            }
        ]
    },

    # 7. Paragraphing, Transitions & Cohesion
    {
        "filename": "writing-linking-up-your-answer.html",
        "clean_topic": "Paragraphing, Transitions & Cohesion",
        "intro_lead": "Unify extended texts using the PEEL paragraph architecture, sophisticated transitional discourse markers, and thematic bridges to achieve seamless flow from introduction to conclusion.",
        "next_file": "writing-grammar.html",
        "next_name": "Grammar & Sentence Structures",
        "spec_points": [
            ("L1.25 / L2.25", "Organise writing into logical paragraphs, establishing clear transitions and cohesive devices."),
            ("L2.26", "Master complex discourse markers to contrast, elaborate, Sequence, and conclude professional arguments.")
        ],
        "golden_rules": [
            {
                "icon": "fa-link",
                "title": "Golden Rule 1: Build Every Body Paragraph Using the PEEL Formula",
                "desc": "Every body paragraph should contain 3 to 4 sentences following PEEL: Point (clear topic sentence) → Evidence (realistic statistic, cost, or example) → Explain (impact on the workplace/community) → Link (bridge to the overall goal).",
                "badge": "Point (Topic Sentence) → Evidence (Fact/Example) → Explain (Impact) → Link"
            },
            {
                "icon": "fa-arrow-right-arrow-left",
                "title": "Golden Rule 2: Upgrade 'Also', 'And', and 'But' to Level 2 Discourse Markers",
                "desc": "Examiners look specifically for advanced cohesive transitions: use 'Furthermore' or 'Moreover' to add points, 'Conversely' or 'Nevertheless' to contrast, and 'Consequently' or 'Therefore' to show results.",
                "badge": "Addition: Furthermore / Moreover | Contrast: Conversely / However | Cause/Effect: Consequently / Therefore"
            }
        ],
        "skills": [
            {
                "title": "The Level 2 Discourse Marker Toolkit (Categorised by Function)",
                "summary": "Memorise two transitions from each category and weave them into every Writing exam response.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Cohesive Function</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">High-Scoring Transitions</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Punctuation Rule &amp; Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Adding &amp; Reinforcing</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>Furthermore, Moreover, In addition, Equally important</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Follow with a comma: <em>"<strong>Furthermore,</strong> recent staff surveys confirm that..."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Contrasting &amp; Qualifying</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>However, Conversely, Nevertheless, Whilst, On the other hand</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Use after a full stop or semicolon: <em>"...costs £600<strong>; however,</strong> it saves £2,000 annually."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Cause &amp; Consequence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>Consequently, Therefore, As a direct result, Accordingly</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Follow with a comma: <em>"<strong>Consequently,</strong> waiting times dropped by 40%."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Concluding &amp; Summarising</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>In conclusion, Ultimately, In light of these findings</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Opens final paragraph: <em>"<strong>In light of these findings,</strong> I recommend..."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "The TiP ToP Rule: When to Start a New Paragraph",
                "summary": "Never write a wall of text—start a new paragraph every time you shift Time, Place, Topic, or Person.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Ti — Time Change:</strong> Moving from past background (<em>"Last winter, our heating failed..."</em>) to future proposals (<em>"From next month, we propose..."</em>).</li>
                    <li><strong>P — Place Change:</strong> Moving from discussing the reception desk to discussing the staff car park.</li>
                    <li><strong>To — Topic / Bullet Point Change:</strong> Moving from Prompt Bullet 1 (health benefits) to Prompt Bullet 2 (financial costs).</li>
                    <li><strong>P — Person / Perspective Change:</strong> Moving from the management view to addressing staff concerns or counter-arguments.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Before & After: Transforming Choppy Sentences into Cohesive PEEL Prose",
                "summary": "See how discourse markers and pronoun referencing glue disconnected sentences together.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Disconnected, Choppy Sentences (Repetitive &amp; Basic):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"The library roof is leaking. Rain comes in when it storms. Ten computers got ruined last month. We need to fix the roof soon. People cannot use the study room."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Cohesive PEEL Paragraph with Discourse Markers (Level 2 Standard):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"Urgent structural repairs are required on the library roof to prevent further damage to public IT equipment. During last month's heavy storms, rainwater penetrated the ceiling panels and destroyed ten desktop computers worth £4,500. <strong>Consequently,</strong> the entire adult study suite has been closed to residents for three weeks. <strong>Therefore,</strong> authorising emergency roofing maintenance this month will protect council assets and restore vital community learning access."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Inserting Paragraph Breaks & Linking Words in a Letter",
                "marks": "Level 1 Paragraphing & Cohesion Benchmark (3 Marks)",
                "context": "Customer Service Feedback Letter",
                "question": "This draft extract is written as one unbroken block of short sentences. Divide it into <strong>two logical paragraphs</strong> and insert appropriate linking words (<em>However, Furthermore, Therefore</em>):<br><em>'I visited your leisure centre on Tuesday evening for the beginner swimming class. The receptionist was very welcoming and showed me to the changing rooms. The changing room floors were covered in muddy footprints. Two of the three hairdryers were broken and had exposed wires. You need to inspect the changing rooms daily.'</em>",
                "steps": [
                    ("Step 1", "Identify the topic shift from positive reception to changing room hazards", "Start Paragraph 1 with the visit and positive reception; start Paragraph 2 where the complaint about the changing rooms begins.", "Logical Paragraph Split (L1.25)"),
                    ("Step 2", "Insert a contrasting marker ('However,') at the start of Paragraph 2", "Use 'However,' to pivot from the polite receptionist to the unhygienic changing rooms.", "Cohesive Transition"),
                    ("Step 3", "Insert 'Furthermore,' and 'Therefore,' to link the electrical hazard and action", "Connect the muddy floor to the dangerous hairdryers and final recommendation.", "Smooth Narrative Flow")
                ],
                "final_answer": "I visited your leisure centre on Tuesday evening to attend the beginner adult swimming class. Upon arrival, the front-desk receptionist was extremely welcoming and kindly directed me to the poolside facilities.<br><br><strong>However,</strong> I was disappointed to find that the changing room floors were covered in muddy footprints. <strong>Furthermore,</strong> two of the three wall-mounted hairdryers were out of order with exposed electrical wiring, presenting a serious safety hazard. <strong>Therefore,</strong> I ask that centre management conduct daily hygiene and electrical safety inspections.",
                "tutor_tip": "Starting Paragraph 2 with 'However,' creates a smooth bridge between your praise in Paragraph 1 and your complaint in Paragraph 2."
            },
            {
                "title": "Level 2 Model: Community Health Hub Expansion PEEL Paragraph",
                "marks": "Level 2 PEEL & Discourse Markers Benchmark (4 Marks)",
                "context": "Primary Care Infrastructure Proposal",
                "question": "Write one fully cohesive body paragraph arguing why extending GP clinic opening hours until 20:00 will alleviate evening A&E overcrowding, using the PEEL method and at least two Level 2 discourse markers.",
                "steps": [
                    ("Step 1", "Draft Topic Sentence (Point)", "State clearly that extending primary care hours until 20:00 directly relieves emergency hospital congestion.", "Clear Topic Sentence (L2.25)"),
                    ("Step 2", "Incorporate Evidence & Explanation with 'Furthermore,'", "Use 'Furthermore,' to introduce audit data (38% of evening A&E visits are minor ailments) and explain how nurse practitioners can treat them.", "Evidence & Elaboration"),
                    ("Step 3", "Link back to overarching clinical strategy with 'Consequently,'", "Use 'Consequently,' to connect local evening access with reduced hospital waiting times and NHS savings.", "Cohesive Conclusion (L2.26)")
                ],
                "final_answer": "'Extending our community clinic opening hours until 20:00 on weekdays will directly alleviate severe congestion at the neighbouring hospital Emergency Department. <strong>Furthermore,</strong> recent regional audit data reveals that 38% of non-urgent evening A&E attendances involve minor infections or sprains that could be treated rapidly by our primary care nurse practitioners. <strong>Consequently,</strong> providing local evening appointments not only prevents vulnerable patients from enduring six-hour hospital waits, but also frees acute trauma teams to focus on life-threatening emergencies.'",
                "tutor_tip": "Notice how 'Furthermore,' introduces supporting data and 'Consequently,' drives the logical conclusion home. This is textbook Level 2 cohesion."
            }
        ],
        "examiner_traps": [
            {
                "title": "Starting Every Paragraph Mechanically with 'Firstly', 'Secondly', 'Thirdly'",
                "desc": "While better than no markers at all, starting every paragraph with 'Firstly... Secondly... Thirdly...' feels robotic at Level 2.",
                "fix": "Link paragraphs conceptually using thematic bridges: 'In addition to these clinical safety benefits, the financial implications must also be considered.'"
            },
            {
                "title": "Using a Discourse Marker That Contradicts the Meaning",
                "desc": "Writing 'The course was cheap. However, everyone enjoyed it' makes no sense because 'cheap' and 'enjoyed it' are both positive points, not a contrast!",
                "fix": "Only use 'However' or 'Conversely' when the second idea genuinely opposes or contrasts with the first."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Combine these two choppy sentences into one cohesive Level 2 sentence using a semicolon and an appropriate contrasting discourse marker (e.g. <em>nevertheless, however</em>):<br><em>'The night-shift care team experienced two unexpected staff sickness absences. They completed all resident medication rounds safely and on schedule.'</em>",
                "solution_steps": "1. Place a semicolon after the first independent clause ('...sickness absences;').<br>2. Insert 'nevertheless,' or 'however,' followed by a comma and the second clause.",
                "correct_answer": "'The night-shift care team experienced two unexpected staff sickness absences; nevertheless, they completed all resident medication rounds safely and on schedule.'",
                "tutor_tip": "Using 'semicolon + discourse marker + comma' (; nevertheless, / ; however, / ; consequently,) is one of the highest-scoring punctuation structures in Level 2 English."
            },
            {
                "marks": "3 Marks",
                "question": "Choose the most logical discourse marker from the list (<strong>Consequently / Conversely / Furthermore</strong>) to fill each gap below:<br>1. Replacing halogen bulbs with LED panels will cut electricity usage by 45%. __________, the new panels have a ten-year lifespan that reduces maintenance callouts.<br>2. The north car park lighting timer failed at 17:00 yesterday. __________, staff leaving the evening shift had to walk to their vehicles in complete darkness.<br>3. Online training modules allow staff to study flexibly at home. __________, practical manual-handling skills can only be assessed safely in person.",
                "solution_steps": "1. Sentence 1 adds a second positive benefit → Furthermore.<br>2. Sentence 2 shows the direct result/effect of the timer failing → Consequently.<br>3. Sentence 3 contrasts online study with in-person assessment → Conversely.",
                "correct_answer": "1. Furthermore | 2. Consequently | 3. Conversely",
                "tutor_tip": "Test the relationship between the two sentences first: Addition = Furthermore; Result = Consequently; Contrast = Conversely."
            },
            {
                "marks": "4 Marks",
                "question": "Write a complete 4-sentence PEEL body paragraph for a formal letter to your College Principal arguing why the college library should remain open until 20:00 on Tuesdays and Thursdays for adult evening-class learners.",
                "solution_steps": "1. Point: Topic sentence stating that extending library hours until 20:00 is essential for adult learners.<br>2. Evidence: Cite that over 120 adult apprentices work full-time daytime shifts and have no quiet study space or Wi-Fi at home.<br>3. Explain (with 'Furthermore'): Explain how access to textbooks and computers after work improves exam pass rates.<br>4. Link (with 'Consequently'): Conclude that keeping one librarian on duty for two extra hours will significantly boost student retention.",
                "correct_answer": "'Extending college library opening hours until 20:00 on Tuesdays and Thursdays is essential to support our adult evening-class learners. Currently, the library closes at 17:00, which means over 120 adult apprentices who work full-time daytime shifts are completely locked out of textbook and computer resources. Furthermore, many learners live in shared accommodation without quiet study spaces or reliable broadband to complete their coursework. Consequently, funding just six additional hours of library staffing per week will directly improve functional skills pass rates and student retention.'",
                "tutor_tip": "Every sentence in this paragraph has a clear job: Point → Evidence → Explanation → Link."
            }
        ]
    },

    # 8. Grammar, Sentence Variety & Syntax
    {
        "filename": "writing-grammar.html",
        "clean_topic": "Grammar, Sentence Variety & Syntax",
        "intro_lead": "Master simple, compound, and complex sentence structures, enforce strict subject-verb agreement with collective and singular nouns, and eliminate comma splices and fragments.",
        "next_file": "writing-tenses.html",
        "next_name": "Consistency of Tense",
        "spec_points": [
            ("L1.26 / L2.26", "Write grammatically correct sentences, ensuring accurate subject-verb agreement and syntactic variety."),
            ("L2.27", "Use complex sentence structures, fronted subordinate clauses, relative clauses, and modal verbs with sustained accuracy.")
        ],
        "golden_rules": [
            {
                "icon": "fa-shapes",
                "title": "Golden Rule 1: Deliberately Mix Simple, Compound, and Complex Sentences",
                "desc": "Examiners award top grammar marks for deliberate syntactic variety: use punchy simple sentences for clear directives, compound sentences (FANBOYS) for balanced ideas, and complex sentences (Although, Because, Whilst) for cause-and-effect analysis.",
                "badge": "Simple (1 clause) + Compound (and/but/so) + Complex (Although/Because + comma) = Top Band Grammar"
            },
            {
                "icon": "fa-triangle-exclamation",
                "title": "Golden Rule 2: Never Join Two Complete Sentences with Just a Comma (Comma Splice)",
                "desc": "A comma cannot hold two independent sentences together. Fix every comma splice using either a full stop, a semicolon (;), or a coordinating conjunction (, and / , but / , so).",
                "badge": "Wrong: 'The delivery arrived late, the stock was warm.' → Right: 'The delivery arrived late, so the stock was warm.'"
            }
        ],
        "skills": [
            {
                "title": "The 3 Sentence Architectures Every Candidate Must Demonstrate",
                "summary": "Formula and punctuation rules for Simple, Compound, and Complex sentences.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Sentence Type</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Grammatical Formula</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Workplace Model Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Simple Sentence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">One independent clause (Subject + Main Verb) expressing a single complete thought.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"All visitors must sign the security register at reception."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Compound Sentence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Two independent clauses joined by a comma + coordinating conjunction (<strong>F</strong>or, <strong>A</strong>nd, <strong>N</strong>or, <strong>B</strong>ut, <strong>O</strong>r, <strong>Y</strong>et, <strong>S</strong>o).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The clinic heating failed at 08:00<strong>, so</strong> portable radiators were deployed to every waiting room."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Complex Sentence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Main clause + subordinate clause starting with <em>Although, Because, Since, Whilst, Unless, If</em>.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"<strong>Although</strong> the initial installation costs £1,200<strong>,</strong> the solar panels will reduce annual bills by 30%."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Mastering Tricky Subject-Verb Agreement Traps",
                "summary": "How to match singular subjects with singular verbs even when plural nouns sit in the middle.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>The Prepositional Phrase Trap:</strong> Match the verb to the true head noun, NOT the plural noun before the verb:<br>
                    Wrong: <em>"The box of surgical gloves <strong>are</strong> empty."</em> → Right: <em>"The <strong>box</strong> of surgical gloves <strong>is</strong> empty."</em></li>
                    <li><strong>Indefinite Singular Pronouns (Each, Everyone, Neither, Either):</strong> These always take a singular verb:<br>
                    Wrong: <em>"Each of the drivers <strong>have</strong> a permit."</em> → Right: <em>"<strong>Each</strong> of the drivers <strong>has</strong> a permit."</em><br>
                    Wrong: <em>"Neither the manager nor the supervisor <strong>were</strong> informed."</em> → Right: <em>"<strong>Neither</strong> the manager nor the supervisor <strong>was</strong> informed."</em></li>
                    <li><strong>Standard English 'Was' vs 'Were':</strong> Never write <em>"We was waiting"</em> or <em>"You was told"</em>. Always write <em>"We <strong>were</strong> waiting"</em> and <em>"They <strong>were</strong> informed"</em>.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Embedded Relative Clauses ('Who', 'Which', 'Whose')",
                "summary": "How to drop an extra layer of detail into the middle of a sentence using paired commas.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To impress Level 2 examiners, insert a non-defining relative clause framed by two bracketing commas:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    • <strong>People (who):</strong> <em>"Sister Evans<strong>, who has led the maternity unit since 2019,</strong> will coordinate the training programme."</em><br>
                    • <strong>Things (which):</strong> <em>"The main goods lift<strong>, which was installed over twenty years ago,</strong> requires urgent cable replacement."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Subject-Verb Agreement & Comma Splice Repair",
                "marks": "Level 1 Grammar Accuracy Benchmark (3 Marks)",
                "context": "Retail Stockroom Handover Note",
                "question": "Correct the <strong>two grammatical errors</strong> (one subject-verb agreement error and one comma splice) in this stockroom note:<br><em>'The delivery of winter coats have arrived in Bay 2, the afternoon team needs to hang them on the shop floor before 16:00.'</em>",
                "steps": [
                    ("Step 1", "Fix the subject-verb agreement error", "The true subject is 'The delivery' (singular), not 'coats'. Change 'have arrived' to 'has arrived'.", "Subject-Verb Agreement (L1.26)"),
                    ("Step 2", "Fix the comma splice between the two independent clauses", "Replace the comma after 'Bay 2' with ', so' or ', and' (or use a semicolon/full stop).", "Eliminates Comma Splice"),
                    ("Step 3", "Write out the complete corrected sentence", "Verify that both clauses read smoothly and accurately.", "Final Sentence Check")
                ],
                "final_answer": "'The delivery of winter coats <strong>has</strong> arrived in Bay 2, <strong>so</strong> the afternoon team needs to hang them on the shop floor before 16:00.'",
                "tutor_tip": "Cross out 'of winter coats' in your head: you would never say 'The delivery have arrived'—you say 'The delivery has arrived'!"
            },
            {
                "title": "Level 2 Model: Synthesising Three Simple Sentences into One Complex Sentence",
                "marks": "Level 2 Syntactic Variety Benchmark (3 Marks)",
                "context": "Clinical Discharge Coordinator Report",
                "question": "Combine these three simple sentences into a single, grammatically sophisticated complex sentence using a fronted subordinate clause and an embedded relative clause:<br>1. Mrs Green completed her six-week course of outpatient physiotherapy.<br>2. Mrs Green underwent hip replacement surgery in August.<br>3. The consultant approved her return to independent living.",
                "steps": [
                    ("Step 1", "Embed Sentence 2 as a relative clause inside the subject", "'Mrs Green, who underwent hip replacement surgery in August,' (framed with paired commas).", "Embedded Relative Clause (L2.27)"),
                    ("Step 2", "Front Sentence 1 using a subordinating conjunction ('Because' or 'After')", "'After Mrs Green, who underwent hip replacement surgery in August, completed her six-week course of outpatient physiotherapy,'", "Fronted Subordinate Clause"),
                    ("Step 3", "Attach the main clause (Sentence 3) after the separating comma", "'...the consultant approved her return to independent living.'", "Complex Sentence Synthesis")
                ],
                "final_answer": "'After Mrs Green, who underwent hip replacement surgery in August, completed her six-week course of outpatient physiotherapy, the consultant approved her return to independent living.'",
                "tutor_tip": "Combining a fronted subordinate clause ('After...') with a bracketed relative clause (', who...,') showcases top-tier Level 2 grammatical control."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing 'Could Of', 'Should Of', or 'Would Of'",
                "desc": "In spoken English, 'could've' sounds like 'could of'. Writing 'We could of prevented the accident' in an exam is a serious grammatical error.",
                "fix": "Always write the auxiliary verb 'have': 'could have', 'should have', 'would have'."
            },
            {
                "title": "Leaving Subordinate Clauses Hanging as Incomplete Fragments",
                "desc": "Writing 'Although the staff worked extremely hard all weekend.' with a full stop at the end is a sentence fragment because there is no main clause!",
                "fix": "If you start a sentence with 'Although', 'Because', or 'Whereas', make sure you follow the comma with a complete main clause."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Fix the comma splice in this sentence using two different grammatical methods (Method 1: using a coordinating conjunction; Method 2: using a semicolon):<br><em>'The fire alarm sounded at 14:00, all staff evacuated to Car Park B within three minutes.'</em>",
                "solution_steps": "1. Method 1: Insert ', and' after '14:00'.<br>2. Method 2: Replace the comma after '14:00' with a semicolon (;).",
                "correct_answer": "Method 1: 'The fire alarm sounded at 14:00, and all staff evacuated to Car Park B within three minutes.'<br>Method 2: 'The fire alarm sounded at 14:00; all staff evacuated to Car Park B within three minutes.'",
                "tutor_tip": "Both clauses could stand alone as complete sentences, so a bare comma between them is always wrong."
            },
            {
                "marks": "3 Marks",
                "question": "Identify and correct the <strong>three grammatical errors</strong> in this workplace paragraph:<br><em>'Neither the supervisor nor the operatives was aware that the forklift brakes was faulty. The manager should of inspected the vehicle logbook before the shift started.'</em>",
                "solution_steps": "1. Error 1 ('neither... nor...'): With 'neither/nor', the verb agrees with the closer plural noun 'operatives' → change 'was aware' to 'were aware'.<br>2. Error 2 (plural subject 'brakes'): Change 'brakes was faulty' to 'brakes were faulty'.<br>3. Error 3 ('should of'): Change 'should of inspected' to 'should have inspected'.",
                "correct_answer": "1. 'was aware' → 'were aware' | 2. 'brakes was' → 'brakes were' | 3. 'should of' → 'should have'.<br>Corrected text: 'Neither the supervisor nor the operatives were aware that the forklift brakes were faulty. The manager should have inspected the vehicle logbook before the shift started.'",
                "tutor_tip": "Watch out for 'was/were' agreement with plural nouns like 'brakes' and never write 'should of'."
            },
            {
                "marks": "3 Marks",
                "question": "Rewrite the two simple sentences below as a single complex sentence starting with the subordinating conjunction <strong>'Whilst'</strong>:<br>Sentence 1: <em>Installing solar panels on the community centre roof requires an upfront investment of £6,000.</em><br>Sentence 2: <em>The scheme will reduce annual electricity bills by £1,500 every year.</em>",
                "solution_steps": "1. Start the dependent clause with 'Whilst installing solar panels on the community centre roof requires an upfront investment of £6,000,'.<br>2. Place a mandatory comma after '£6,000'.<br>3. Follow with the main clause.",
                "correct_answer": "'Whilst installing solar panels on the community centre roof requires an upfront investment of £6,000, the scheme will reduce annual electricity bills by £1,500 every year.'",
                "tutor_tip": "Starting a persuasive paragraph with 'Whilst [counter-argument], [your main benefit]' is the cleanest way to knock down objections in Level 2 writing."
            }
        ]
    },

    # 9. Consistency of Tense
    {
        "filename": "writing-tenses.html",
        "clean_topic": "Consistency of Tense",
        "intro_lead": "Maintain consistent grammatical tense across extended writing, master past continuous, past perfect, and present perfect forms in workplace reporting, and eliminate jarring tense shifts.",
        "next_file": "writing-perfecting-your-punctuation.html",
        "next_name": "Punctuation Mastery",
        "spec_points": [
            ("L1.27 / L2.27", "Use correct and consistent tense across extended narratives, letters, and formal reports."),
            ("L2.28", "Accurately apply present perfect, past continuous, past perfect, and modal conditional constructions in workplace documentation.")
        ],
        "golden_rules": [
            {
                "icon": "fa-timeline",
                "title": "Golden Rule 1: Choose Your Anchor Tense for Each Paragraph and Stick to It",
                "desc": "An incident report or witness statement is anchored in the PAST tense ('The alarm sounded, staff evacuated, and the manager arrived'). Never slip mid-sentence into the present tense ('then the manager arrives and says').",
                "badge": "Past Events = Past Tense | Current Policy = Present Tense | Recommendations = Future / Modal Verbs"
            },
            {
                "icon": "fa-hourglass-half",
                "title": "Golden Rule 2: Use Present Perfect ('Have/Has + Past Participle') to Link Past Actions to Now",
                "desc": "When describing recent workplace improvements or ongoing problems that started in the past and still affect today, use the present perfect: 'We have installed four cameras' or 'Waiting times have increased by 20% since May'.",
                "badge": "Simple Past = 'We updated the rota on Monday.' | Present Perfect = 'We have updated the rota to improve cover.'"
            }
        ],
        "skills": [
            {
                "title": "The Workplace Tense Selection Matrix",
                "summary": "Which verb tenses to deploy for each section of a Functional Skills writing response.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Workplace Purpose</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Target Tense Form</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Model Sentence Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Recounting an Incident / History</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Past Simple &amp; Past Continuous:</strong> (<em>walked, was inspecting</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"While the technician <strong>was inspecting</strong> the boiler, the pressure valve <strong>failed</strong>."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Describing Current Rules / Facts</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Present Simple:</strong> (<em>requires, operates, ensures</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Our current clinic policy <strong>requires</strong> two nurses to verify controlled dosages."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Recent Changes Affecting Now</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Present Perfect:</strong> (<em>has/have + past participle</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Over the past six months, staff turnover <strong>has fallen</strong> by 18%."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Proposing Future Solutions</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Future &amp; Modal Conditional:</strong> (<em>will reduce, would enable</em>)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Introducing staggered breaks <strong>will eliminate</strong> lunchtime queue bottlenecks."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Irregular Past Participles & Standard English Verb Forms",
                "summary": "Eliminate non-standard spoken verb errors ('I seen', 'I done', 'it had broke') that cost SPaG marks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>See / Saw / Have Seen:</strong> Never write <em>"I seen the spill"</em>. Write <em>"I <strong>saw</strong> the spill"</em> (past simple) or <em>"I <strong>have seen</strong> several incidents"</em> (present perfect).</li>
                    <li><strong>Do / Did / Have Done:</strong> Never write <em>"The team done the audit"</em>. Write <em>"The team <strong>completed / did</strong> the audit"</em> or <em>"The team <strong>has done</strong> the audit"</em>.</li>
                    <li><strong>Break / Broke / Had Broken:</strong> Never write <em>"The lock was broke"</em>. Write <em>"The lock was <strong>broken</strong>"</em>.</li>
                    <li><strong>Come / Came / Have Come:</strong> Never write <em>"The parcel come yesterday"</em>. Write <em>"The parcel <strong>came / arrived</strong> yesterday"</em>.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "How to Shift Tenses Legitimately Across a 4-Paragraph Letter",
                "summary": "Signposting time changes clearly using temporal adverbials.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">You CAN change tense between paragraphs—provided you signal the time shift with a clear time marker:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    • <strong>Paragraph 2 (Past Event):</strong> <em>"<strong>Last Tuesday at 14:30,</strong> a delivery lorry struck the car park barrier and damaged the sensor."</em><br>
                    • <strong>Paragraph 3 (Present Impact):</strong> <em>"<strong>Currently,</strong> the barrier remains stuck in the open position, allowing unauthorised commuters to park on site."</em><br>
                    • <strong>Paragraph 4 (Future Action):</strong> <em>"<strong>Next week,</strong> our estates contractor will install a reinforced automatic gate."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Paramedic Callout Log Tense Repair",
                "marks": "Level 1 Tense Consistency Benchmark (3 Marks)",
                "context": "Emergency Medical Documentation",
                "question": "Identify and correct the <strong>three tense errors</strong> in this paramedic incident log:<br><em>'We arrived at the residential address at 03:15 and find the patient conscious on the hallway floor. The lead paramedic administers oxygen while the technician checked the ECG monitor, and then we takes the patient to St Jude’s Hospital.'</em>",
                "steps": [
                    ("Step 1", "Identify the anchor tense of the incident log", "The callout happened in the past ('arrived at 03:15', 'checked'). All main action verbs must be in the PAST tense.", "Anchor Tense Identified (L1.27)"),
                    ("Step 2", "Locate the three present-tense slips", "1. 'find' → 'found'<br>2. 'administers' → 'administered'<br>3. 'takes' → 'took' (or 'transferred').", "Verb Corrections"),
                    ("Step 3", "Write out the fully consistent past-tense log", "Ensure smooth past-tense narration throughout.", "Final Verification")
                ],
                "final_answer": "'We arrived at the residential address at 03:15 and <strong>found</strong> the patient conscious on the hallway floor. The lead paramedic <strong>administered</strong> oxygen while the technician checked the ECG monitor, and then we <strong>transferred</strong> the patient to St Jude’s Hospital.'",
                "tutor_tip": "Read your incident log aloud in your head: shifting from 'arrived' to 'find' and 'administers' immediately sounds jarring."
            },
            {
                "title": "Level 2 Model: Multi-Tense Audit Report (Past Perfect, Present Perfect & Future)",
                "marks": "Level 2 Advanced Tense Control Benchmark (4 Marks)",
                "context": "Warehouse Health & Safety Audit Report",
                "question": "Write a 3-sentence executive summary for a safety report that:<br>1. Uses the <strong>past perfect</strong> (<em>had + past participle</em>) to state what had gone wrong prior to last month's inspection.<br>2. Uses the <strong>present perfect</strong> (<em>have/has + past participle</em>) to state what remedial steps have been completed since then.<br>3. Uses a <strong>future modal verb</strong> to state the projected outcome for next quarter.",
                "steps": [
                    ("Step 1", "Sentence 1: Past Perfect for pre-inspection background", "Use 'had deteriorated' and 'had not received' to show conditions before the October audit.", "Past Perfect Mastery (L2.28)"),
                    ("Step 2", "Sentence 2: Present Perfect for recent completed actions", "Use 'has repainted' and 'have completed' to connect recent fixes to the current state.", "Present Perfect Mastery"),
                    ("Step 3", "Sentence 3: Future Modal for projected safety outcome", "Use 'will eliminate' and 'should ensure' to project next quarter's compliance.", "Future Modal Projection")
                ],
                "final_answer": "'Prior to our internal audit on 1 October, pedestrian walkway markings in Bay 3 <strong>had faded</strong> severely and twelve temporary operatives <strong>had not completed</strong> their forklift awareness induction. Over the past fortnight, the facilities team <strong>has repainted</strong> all high-visibility floor lanes and all agency staff <strong>have passed</strong> mandatory safety assessments. Consequently, these interventions <strong>will reduce</strong> vehicle-pedestrian near-misses to zero during the upcoming peak winter quarter.'",
                "tutor_tip": "Moving logically from Past Perfect ('had faded') → Present Perfect ('has repainted') → Future ('will reduce') demonstrates effortless Level 2 grammatical command."
            }
        ],
        "examiner_traps": [
            {
                "title": "Slipping into the Conversational Present When Recounting Past Events",
                "desc": "In casual speech, people often say: 'So I walked up to the counter and the manager says to me...' In Functional Skills writing, mixing 'walked' and 'says' is penalised as a tense error.",
                "fix": "Always keep past narratives strictly in the past tense: 'I walked up to the counter and the manager said to me...'"
            },
            {
                "title": "Confusing Past Simple with Past Participles ('I Seen' / 'I Done')",
                "desc": "Writing 'I seen the broken window' or 'We done the risk assessment' is non-standard grammar and loses immediate SPaG marks.",
                "fix": "Use 'I saw' / 'We did' for simple past, or add 'have/had': 'I have seen' / 'We have done'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Correct the two tense errors in this sentence from an audit report:<br><em>'Yesterday morning, the pharmacy auditor inspected the controlled drugs cabinet and finds that two signature entries are missing from Tuesday's log.'</em>",
                "solution_steps": "1. The time marker 'Yesterday morning' and verb 'inspected' establish the past tense.<br>2. Change 'finds' to 'found' and 'are missing' to 'were missing'.",
                "correct_answer": "'Yesterday morning, the pharmacy auditor inspected the controlled drugs cabinet and found that two signature entries were missing from Tuesday's log.'",
                "tutor_tip": "When a sentence begins with a past time marker like 'Yesterday morning' or 'Last week', every verb that follows in that recount must stay in the past tense."
            },
            {
                "marks": "3 Marks",
                "question": "Replace the three non-standard verb forms in this witness statement with correct Standard English past-tense or past-participle verbs:<br><em>'When I come onto the ward at 07:00, I seen that the medication fridge door had broke during the night.'</em>",
                "solution_steps": "1. Change 'come' (present) to 'came' (or 'arrived').<br>2. Change 'I seen' to 'I saw' (or 'I noticed').<br>3. Change 'had broke' to 'had broken'.",
                "correct_answer": "'When I came onto the ward at 07:00, I saw that the medication fridge door had broken during the night.'",
                "tutor_tip": "After 'had', 'have', or 'has', always use the past participle ('broken', 'taken', 'written', 'seen'), never the simple past ('broke', 'took', 'wrote')."
            },
            {
                "marks": "3 Marks",
                "question": "Rewrite this paragraph so that it maintains consistent <strong>present tense</strong> appropriate for a permanent Staff Standard Operating Procedure (SOP) manual:<br><em>'All laboratory technicians must wear safety goggles before entering Room 4. You checked the fume cupboard airflow gauge, and then you will record the pressure reading in the yellow logbook.'</em>",
                "solution_steps": "1. Identify the anchor tense for an SOP manual: Present tense (or imperative instruction).<br>2. Change past tense 'checked' and future tense 'will record' into present simple verbs ('check' and 'record') to match the routine procedure.",
                "correct_answer": "'All laboratory technicians must wear safety goggles before entering Room 4. Technicians check the fume cupboard airflow gauge and then record the pressure reading in the yellow logbook.'",
                "tutor_tip": "Standard Operating Procedures describe permanent rules, so keep all verbs in the present simple tense."
            }
        ]
    },

    # 10. Punctuation Mastery: Apostrophes, Colons & Commas
    {
        "filename": "writing-perfecting-your-punctuation.html",
        "clean_topic": "Punctuation Mastery: Apostrophes, Colons & Commas",
        "intro_lead": "Command full stops, introductory and list commas, singular and plural possessive apostrophes, semicolons, colons, and parenthetical dashes with zero ambiguity.",
        "next_file": "writing-spelling.html",
        "next_name": "Spelling Rules & Strategies",
        "spec_points": [
            ("L1.28 / L2.28", "Use a wide range of punctuation accurately, including capital letters, full stops, question marks, commas, and apostrophes."),
            ("L2.29", "Deploy colons, semicolons, inverted commas, brackets, and dashes accurately to enhance clarity in complex professional documents.")
        ],
        "golden_rules": [
            {
                "icon": "fa-quote-right",
                "title": "Golden Rule 1: The Singular vs Plural Possessive Apostrophe Rule",
                "desc": "Ask yourself: WHO owns the item? If ONE person/thing owns it, add 's (the nurse's locker). If MULTIPLE people ending in s own it, place the apostrophe AFTER the s (the nurses' staffroom). If an irregular plural owns it (children, men, women, people), add 's (the children's ward).",
                "badge": "1 Owner = nurse's | 2+ Owners ending in s = nurses' | Irregular Plural = children's / people's"
            },
            {
                "icon": "fa-grip-lines-vertical",
                "title": "Golden Rule 2: Colons Introduce Lists or Explanations; Semicolons Link Equal Clauses",
                "desc": "Place a COLON (:) after a complete clause to introduce a list, explanation, or verdict. Place a SEMICOLON (;) between two complete, closely related sentences without using 'and' or 'but'.",
                "badge": "Colon (:) = 'Here is what you need: ...' | Semicolon (;) = 'Clause 1 is true; Clause 2 is closely linked.'"
            }
        ],
        "skills": [
            {
                "title": "The Complete Level 2 Punctuation Arsenal",
                "summary": "How and where to use all 6 high-value punctuation marks in your Writing exam.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Punctuation Mark</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Exact Grammatical Rule</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">High-Scoring Exam Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Introductory Comma (,)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Placed immediately after a fronted adverbial, discourse marker, or subordinate clause.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Following last week's safety audit<strong>,</strong> all ladders were replaced."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Possessive Apostrophe (')</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Shows ownership. Never use in ordinary plurals (<em>cameras</em>) or possessive pronoun <em>its</em>.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The <strong>manager's</strong> office is next to the <strong>drivers'</strong> rest area."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Colon (:)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Follows a complete main clause to introduce a list, key reason, or quotation.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The audit identified three priorities<strong>:</strong> lighting, heating, and security."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Semicolon (;)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Joins two related independent clauses OR separates complex items in a detailed list.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The main car park is full<strong>;</strong> however, overflow spaces remain open."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Brackets ( ) / Dashes (–)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Encloses extra parenthetical statistics, dates, or clarifications mid-sentence.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Staff turnover <strong>(currently 24% per annum)</strong> must be reduced."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Conquering the #1 Exam Trap: It's vs Its",
                "summary": "Why possessive 'its' NEVER takes an apostrophe.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>It's (with an apostrophe) = "It is" or "It has":</strong> Only use an apostrophe if you can expand the word to <em>"it is"</em>. (Note: in formal letters and reports, write <em>"it is"</em> in full anyway!).</li>
                    <li><strong>Its (NO apostrophe) = "belonging to it":</strong> Just like possessive <em>his</em> and <em>hers</em> don't have apostrophes, possessive <em>its</em> never has an apostrophe:<br>
                    Correct: <em>"The hospital celebrated <strong>its</strong> 50th anniversary, and the charity published <strong>its</strong> annual accounts."</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Using Semicolons in Complex Multi-Word Lists",
                "summary": "When list items already contain commas, use semicolons to separate the items cleanly.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Look how a colon and semicolons organise a complex workplace list with 100% clarity:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    <em>"The safety committee comprises three regional leads<strong>:</strong> Sarah Jenkins, Head of Nursing<strong>;</strong> David Patel, Facilities Engineer<strong>;</strong> and Marcus Vance, Health and Safety Representative."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Capital Letters, Commas & Apostrophes in a Clinic Notice",
                "marks": "Level 1 Punctuation Benchmark (3 Marks)",
                "context": "GP Surgery Reception Notice",
                "question": "Rewrite this unpunctuated reception notice, inserting all missing capital letters, commas, apostrophes, and full stops:<br><em>'on monday 2 november dr patels morning clinic will start at 09:30 before booking an appointment please check that the receptionists computer has your current mobile number address and postcode'</em>",
                "steps": [
                    ("Step 1", "Restore proper noun capitals and sentence boundaries", "Capitalise 'On Monday 2 November', 'Dr Patel', and split into two sentences after '09:30.' with a capital 'Before'.", "Capitals & Full Stops (L1.28)"),
                    ("Step 2", "Insert introductory commas and list commas", "Place a comma after 'On Monday 2 November,', after 'Before booking an appointment,', and between list items ('mobile number, address, and postcode').", "Commas in Lists & Clauses"),
                    ("Step 3", "Insert singular possessive apostrophes", "'Dr Patel's morning clinic' and 'the receptionist's computer'.", "Possessive Apostrophes")
                ],
                "final_answer": "'On Monday 2 November, Dr Patel's morning clinic will start at 09:30. Before booking an appointment, please check that the receptionist's computer has your current mobile number, address, and postcode.'",
                "tutor_tip": "Check days of the week (Monday), months (November), and titles/surnames (Dr Patel)—missing a capital letter on a proper noun is an avoidable SPaG slip."
            },
            {
                "title": "Level 2 Model: Advanced Punctuation Overhaul (Colon, Semicolon & Apostrophes)",
                "marks": "Level 2 Advanced Punctuation Benchmark (4 Marks)",
                "context": "Clinical Governance Directive",
                "question": "Insert all missing punctuation (including two possessive apostrophes, a colon, a semicolon, and commas) into this clinical directive:<br><em>'All nurses must check each patients wristband before administering medication specifically verify the full name date of birth and allergy status the wards electronic scanner must also be used'</em>",
                "steps": [
                    ("Step 1", "Insert singular possessive apostrophes", "'each patient's wristband' and 'the ward's electronic scanner'.", "Possessive Accuracy (L2.28)"),
                    ("Step 2", "Insert colon and list commas", "Place a colon after 'medication:' to introduce the specific checks, and commas between 'full name, date of birth, and allergy status'.", "Colon & List Commas (L2.29)"),
                    ("Step 3", "Insert semicolon before the final independent clause", "Place a semicolon after 'allergy status;' to link the final mandatory scanner rule.", "Semicolon Control")
                ],
                "final_answer": "'All nurses must check each patient's wristband before administering medication: specifically, verify the full name, date of birth, and allergy status; the ward's electronic scanner must also be used.'",
                "tutor_tip": "Deliberately including one colon and one semicolon in each of your two Writing exam tasks guarantees you hit the Level 2 punctuation range criteria."
            }
        ],
        "examiner_traps": [
            {
                "title": "The 'Greengrocer's Apostrophe' in Ordinary Plurals",
                "desc": "Putting apostrophes into simple plural nouns (e.g. 'Two nurse's were on duty', 'We bought new laptop's', 'CCTV camera's') is penalised heavily.",
                "fix": "Never use an apostrophe just because a word ends in 's'. Only use an apostrophe for ownership or contraction."
            },
            {
                "title": "Placing a Colon After an Incomplete Verb Phrase",
                "desc": "Writing 'The three main problems are: cost, time, and staffing' is technically incorrect because 'The three main problems are' is not a complete sentence.",
                "fix": "Make the clause before the colon complete: 'The audit identified three main problems: cost, time, and staffing.'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Insert the apostrophe in the exact correct position for each phrase below:<br>1. <em>the childrens play area</em> (belonging to the children)<br>2. <em>the six delivery drivers vans</em> (belonging to six drivers)<br>3. <em>the company updated its / it's health policy</em> (select the correct form)",
                "solution_steps": "1. 'children' is already an irregular plural, so add 's → children's.<br>2. 'drivers' is a regular plural ending in s, so place the apostrophe after the s → drivers'.<br>3. Possessive pronoun never takes an apostrophe → its.",
                "correct_answer": "1. the children's play area | 2. the six delivery drivers' vans | 3. its (no apostrophe)",
                "tutor_tip": "Test irregular plurals carefully: children's, women's, men's, and people's always put the apostrophe BEFORE the s."
            },
            {
                "marks": "3 Marks",
                "question": "Punctuate this sentence accurately using <strong>one colon</strong>, <strong>commas</strong>, and <strong>one semicolon</strong>:<br><em>'The leisure centre refurbishment includes three major upgrades a heated indoor pool a 40-station fitness suite and a healthy cafe membership prices will remain frozen until January.'</em>",
                "solution_steps": "1. Place a colon after 'three major upgrades:' to introduce the list.<br>2. Place commas between the list items ('a heated indoor pool, a 40-station fitness suite, and a healthy cafe').<br>3. Place a semicolon after 'cafe;' to join the final independent clause.",
                "correct_answer": "'The leisure centre refurbishment includes three major upgrades: a heated indoor pool, a 40-station fitness suite, and a healthy cafe; membership prices will remain frozen until January.'",
                "tutor_tip": "Read the clause before your colon ('The leisure centre refurbishment includes three major upgrades')—because it makes complete sense on its own, the colon is 100% grammatical."
            },
            {
                "marks": "3 Marks",
                "question": "Explain how adding bracketing commas changes the meaning of Sentence A compared to Sentence B:<br>Sentence A: <em>The care assistants who completed the dementia course received a £100 bonus.</em><br>Sentence B: <em>The care assistants, who completed the dementia course, received a £100 bonus.</em>",
                "solution_steps": "1. Analyse Sentence A (no commas = defining relative clause): Only those specific care assistants who completed the course got the bonus (others did not).<br>2. Analyse Sentence B (paired commas = non-defining parenthetical clause): ALL the care assistants completed the course and ALL of them received the £100 bonus.",
                "correct_answer": "Sentence A (no commas) means ONLY the subset of care assistants who completed the course received the £100 bonus. Sentence B (with bracketing commas) means ALL care assistants completed the course and received the bonus.",
                "tutor_tip": "Bracketing commas act like handles: if you lift out the words between the two commas, the main sentence still applies to the whole group."
            }
        ]
    },

    # 11. Spelling Rules, Homophones & Specialist Words
    {
        "filename": "writing-spelling.html",
        "clean_topic": "Spelling Rules, Homophones & Specialist Words",
        "intro_lead": "Eliminate high-frequency spelling errors, master British English noun-vs-verb pairs (practice/practise, advice/advise), conquer homophone trios, and spell multi-syllabic workplace vocabulary accurately.",
        "next_file": "writing-fantastic-finalising.html",
        "next_name": "Proofreading & Editing",
        "spec_points": [
            ("L1.29 / L2.29", "Spell words used most often in work, study, and daily life accurately, including specialist words."),
            ("L2.30", "Distinguish accurately between homophones and spell complex polysyllabic vocational vocabulary.")
        ],
        "golden_rules": [
            {
                "icon": "fa-spell-check",
                "title": "Golden Rule 1: The UK English 'C = Noun / S = Verb' Rule (Practice vs Practise)",
                "desc": "In British English exams, the NOUN is always spelled with a 'C' ('a medical practice', 'some helpful advice', 'a driving licence'), whereas the VERB is spelled with an 'S' ('to practise first aid', 'I advise you to book', 'licensed to operate').",
                "badge": "Memory Hook: 'ICE' is a Noun (Pract-ICE, Adv-ICE, Licen-CE) | 'ISE' is a Verb (Pract-ISE, Adv-ISE)"
            },
            {
                "icon": "fa-shuffle",
                "title": "Golden Rule 2: Audit Every Homophone Trio Using the Substitution Test",
                "desc": "Spellcheckers (even if available) never catch homophones because the wrong word is still a real word! Test 'they're' by expanding to 'they are'; test 'there' by swapping with 'here'; test 'too' by swapping with 'excessively' or 'also'.",
                "badge": "Their = ownership | There = place/existence | They're = they are | Were = past verb | Where = location"
            }
        ],
        "skills": [
            {
                "title": "The Top 12 Most Tested Functional Skills Spelling Words",
                "summary": "Memorise the syllable breakdowns and visual memory hooks for these classic exam words.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Correct Spelling</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Common Exam Trap</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Syllable Breakdown &amp; Memory Hook</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Accommodate / Accommodation</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Acommodate / Accomodate</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Large enough to hold <strong>2 C</strong>ats and <strong>2 M</strong>ice (<strong>cc</strong> + <strong>mm</strong>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Necessary</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Neccessary / Necesary</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">A shirt has <strong>1 C</strong>ollar and <strong>2 S</strong>leeves (one <strong>c</strong>, double <strong>ss</strong>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Separate</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Seperate</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">There is <strong>A RAT</strong> in <em>sep-<strong>a-rat</strong>-e</em>.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Definitely</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Definately / Defiantly</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Built on the root word <strong>finite</strong>: <em>de-<strong>finite</strong>-ly</em> (never an 'a').</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Environment / Government</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Enviroment / Goverment</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Keep the silent <strong>N</strong> before <em>-ment</em>: <em>enviro<strong>n</strong>-ment</em>, <em>gover<strong>n</strong>-ment</em>.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Recommend</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Reccomend / Recomend</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Prefix <strong>re-</strong> + root word <strong>commend</strong> (<strong>1 c</strong>, <strong>2 m</strong>'s).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Maintenance</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Maintainance</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Spelled <em>main-<strong>ten</strong>-ance</em> (think of <strong>ten</strong> engineers).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Opportunity</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Oppertunity / Oportunity</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Ships wait in <strong>port</strong>: <em>op-<strong>port</strong>-unity</em> (double <strong>pp</strong>, <strong>o-r-t</strong>).</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Deceptive Workplace Homophones & Near-Homophones",
                "summary": "Distinguish between pairs that sound identical or similar in fast speech.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Affect (Verb = to influence) vs Effect (Noun = the result):</strong><br>
                    <em>"The cold weather will <strong>affect</strong> road safety, producing a negative <strong>effect</strong> on delivery times."</em> (Memory hook: <strong>RAVEN</strong> — <strong>R</strong>emember <strong>A</strong>ffect <strong>V</strong>erb, <strong>E</strong>ffect <strong>N</strong>oun).</li>
                    <li><strong>Accept (Verb = to receive/agree) vs Except (Preposition = excluding):</strong><br>
                    <em>"All staff <strong>except</strong> night security must <strong>accept</strong> the updated shift rota."</em></li>
                    <li><strong>Stationary (Not moving — 'a' for 'at rest' / 'car') vs Stationery (Paper &amp; pens — 'e' for 'envelopes'):</strong><br>
                    <em>"Wait until the forklift is completely <strong>stationary</strong> before signing the <strong>stationery</strong> order."</em></li>
                    <li><strong>Ensure (Guarantee) vs Insure (Financial policy):</strong><br>
                    <em>"Please <strong>ensure</strong> all doors are locked so the broker can <strong>insure</strong> the building."</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Core Prefix & Suffix Spelling Rules",
                "summary": "Why 'disappear' has one 's' while 'dissatisfied' has two.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Prefix Rule (Never drop or double letters unless the root starts with that letter):</strong><br>
                    <em>dis + appear = <strong>disappear</strong></em> (1 s, 2 p's) | <em>dis + satisfied = <strong>dissatisfied</strong></em> (2 s's because root is <em>satisfied</em>) | <em>un + necessary = <strong>unnecessary</strong></em> (2 n's).</li>
                    <li><strong>I Before E Except After C (When the sound is 'EE'):</strong><br>
                    <em>ach<strong>ie</strong>ve, bel<strong>ie</strong>ve, h<strong>ygie</strong>ne, p<strong>ie</strong>ce</em> — but after C: <em>rec<strong>ei</strong>ve, rec<strong>ei</strong>pt, ceiling, dec<strong>ei</strong>ve</em>.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Pharmacy Stock-Take Spelling & Homophone Audit",
                "marks": "Level 1 Spelling Accuracy Benchmark (3 Marks)",
                "context": "Clinical Pharmacy Records",
                "question": "Identify and correct the <strong>three spelling/homophone errors</strong> in this dispensary notice:<br><em>'It is neccessary to seperate all expired medication bottles and return them to there original manufacturer by Friday.'</em>",
                "steps": [
                    ("Step 1", "Correct 'neccessary'", "Apply the '1 Collar, 2 Sleeves' rule: one 'c' and double 'ss' → <strong>necessary</strong>.", "High-Frequency Word (L1.29)"),
                    ("Step 2", "Correct 'seperate'", "Apply the 'a rat' memory hook: <em>sep-a-rat-e</em> → <strong>separate</strong>.", "Vowel Accuracy"),
                    ("Step 3", "Correct the homophone 'there'", "The sentence requires the possessive determiner belonging to the bottles → <strong>their</strong>.", "Homophone Mastery")
                ],
                "final_answer": "1. neccessary → <strong>necessary</strong> | 2. seperate → <strong>separate</strong> | 3. there → <strong>their</strong>.<br>Corrected sentence: 'It is necessary to separate all expired medication bottles and return them to their original manufacturer by Friday.'",
                "tutor_tip": "Keep a personal flashcard of these exact three words—they appear in almost every Functional Skills mock and live exam!"
            },
            {
                "title": "Level 2 Model: Specialist Vocational Spelling & C/S Verb Distinction",
                "marks": "Level 2 Specialist Spelling Benchmark (4 Marks)",
                "context": "Healthcare Estates & Training Report",
                "question": "Identify and correct the <strong>four spelling errors</strong> in this Level 2 report extract:<br><em>'Following the recent enviromental audit, we reccomend that the GP practise upgrades its heating maintainance schedule and advises staff accordingly.'</em>",
                "steps": [
                    ("Step 1", "Correct 'enviromental'", "Insert the silent 'n' before the suffix '-mental' → <strong>environmental</strong>.", "Suffix & Root Accuracy (L2.30)"),
                    ("Step 2", "Correct 'reccomend'", "Prefix 're-' + 'commend' = one 'c', double 'mm' → <strong>recommend</strong>.", "Double Consonant Rule"),
                    ("Step 3", "Correct 'GP practise'", "Here 'GP practice' is a NOUN (the medical surgery), so it must use a 'c' → <strong>practice</strong>.", "UK Noun vs Verb Rule"),
                    ("Step 4", "Correct 'maintainance'", "Root shifts to '-ten-' → <strong>maintenance</strong>.", "Vocational Terminology")
                ],
                "final_answer": "1. enviromental → <strong>environmental</strong> | 2. reccomend → <strong>recommend</strong> | 3. GP practise → <strong>GP practice</strong> | 4. maintainance → <strong>maintenance</strong>.<br>Corrected sentence: 'Following the recent environmental audit, we recommend that the GP practice upgrades its heating maintenance schedule and advises staff accordingly.'",
                "tutor_tip": "Notice how 'GP practice' (noun = C) and 'advises staff' (verb = S) sit in the same sentence—getting both right proves total command of British English spelling."
            }
        ],
        "examiner_traps": [
            {
                "title": "Misspelling Words That Are Printed Right in the Exam Prompt!",
                "desc": "Examiners report that thousands of candidates lose marks by misspelling words like 'community', 'accommodation', or 'questionnaire' when those exact words are printed in the exam question above!",
                "fix": "Always check your spelling of key topic words against the exam prompt paper."
            },
            {
                "title": "Confusing 'Loose' and 'Lose'",
                "desc": "Writing 'We will loose customers' instead of 'We will lose customers' is a classic phonetic slip ('loose' with double o means not tight; 'lose' with one o means to forfeit).",
                "fix": "Remember: If you LOSE something, it has lost one of its O's!"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Select the correct spelling from each bracket in this clinical sentence:<br><em>'The senior consultant gave the apprentice helpful [advice / advise] and encouraged her to [practice / practise] taking blood pressure readings on the training mannequin.'</em>",
                "solution_steps": "1. 'helpful [advice]' is a noun ('a piece of ice') → advice (with a c).<br>2. 'to [practise]' is an infinitive verb ('to do something') → practise (with an s).",
                "correct_answer": "1. advice (noun) | 2. practise (verb)",
                "tutor_tip": "Substitute 'guidance' (noun) vs 'train' (verb): 'helpful guidance' = advice (C); 'to train' = to practise (S)."
            },
            {
                "marks": "3 Marks",
                "question": "Select the correct homophone or near-homophone in each workplace sentence below:<br>1. <em>All delivery vans must remain completely [stationary / stationery] while the loading bay barrier is raised.</em><br>2. <em>The new shift pattern will positively [affect / effect] staff morale across the depot.</em><br>3. <em>The college can [accommodate / acommodate] up to thirty learners in the new IT suite.</em>",
                "solution_steps": "1. Not moving ('parked car') = stationary (with an 'a').<br>2. Action verb ('will influence') = affect (RAVEN: Affect = Verb).<br>3. Double 'cc' and double 'mm' = accommodate.",
                "correct_answer": "1. stationary | 2. affect | 3. accommodate",
                "tutor_tip": "Stationary with 'ar' = parked car; Stationery with 'er' = writing paper."
            },
            {
                "marks": "4 Marks",
                "question": "Proofread this customer service email extract and correct all <strong>four spelling errors</strong>:<br><em>'We sincerely apologise that you did not recieve your furniture delivery on Wednesday. Unfortunatly, our courier experienced an unexpected vehicle breakdown, and we would like to offer you a full refund on your delivery reciept at your earliest conveniance.'</em>",
                "solution_steps": "1. 'recieve' → 'receive' (i before e except after c).<br>2. 'Unfortunatly' → 'Unfortunately' (keep the 'e' in fortunate + ly).<br>3. 'reciept' → 'receipt' (after c use ei + silent p).<br>4. 'conveniance' → 'convenience' (-ience ending).",
                "correct_answer": "1. recieve → receive | 2. Unfortunatly → Unfortunately | 3. reciept → receipt | 4. conveniance → convenience.",
                "tutor_tip": "When adding '-ly' to words ending in '-te' (fortunate, immediate, definite, separate), never drop the 'e': fortunately, immediately, definitely, separately."
            }
        ]
    },

    # 12. Proofreading, Editing & Error Hunting
    {
        "filename": "writing-fantastic-finalising.html",
        "clean_topic": "Proofreading, Editing & Error Hunting",
        "intro_lead": "Conduct systematic 4-pass proofreading audits in the final 5 minutes of the exam to eliminate slips in SPaG, verify format conventions, and protect your 42% technical accuracy mark allocation.",
        "next_file": "writing-why-are-you-writing.html",
        "next_name": "Purpose in Writing",
        "spec_points": [
            ("L1.30 / L2.30", "Proofread and revise written work systematically, identifying and correcting errors in spelling, punctuation, and grammar."),
            ("L2.31", "Critically edit extended responses to improve register consistency, syntactic variety, and adherence to exam criteria.")
        ],
        "golden_rules": [
            {
                "icon": "fa-magnifying-glass-arrow-right",
                "title": "Golden Rule 1: Reserve 5 Minutes After Each Task Strictly for Proofreading",
                "desc": "Never write right up to the final second. Candidates who stop writing 5 minutes before the end of each task and run a structured 4-pass audit catch an average of 5 to 7 SPaG errors—often the exact difference between a narrow Fail and a clear Pass.",
                "badge": "25 mins Plan & Write + 5 mins Dedicated Error Hunt = Protected SPaG Marks"
            },
            {
                "icon": "fa-backward",
                "title": "Golden Rule 2: Separate Your Content Read-Through from Your Spelling Scan",
                "desc": "When you read normally, your brain auto-corrects typos because it focuses on meaning. Do one pass reading sentences aloud in your head for grammar/punctuation, and a second pass scanning individual long words and homophones visually.",
                "badge": "Pass 1: Format & Prompt Check | Pass 2: Sentence Boundaries | Pass 3: Homophones & Spelling"
            }
        ],
        "skills": [
            {
                "title": "The 4-Pass 5-Minute Exam Proofreading Protocol",
                "summary": "Follow this exact sequence in the final 5 minutes of Task 1 and Task 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Pass 1 — Format &amp; Bullet Audit (60 seconds):</strong> Check your top headers and sign-off (e.g. <em>Dear Mr... → Yours sincerely</em>; Report Title + Subheadings; Email <em>To/Subject</em>). Count that all 3 or 4 prompt bullets are covered.</li>
                    <li><strong>Pass 2 — Comma Splice &amp; Sentence Boundary Check (90 seconds):</strong> Look at every comma in your draft. If there is a complete sentence before the comma AND a complete sentence after the comma without <em>and/but/so</em>, change that comma to a semicolon (;) or full stop!</li>
                    <li><strong>Pass 3 — Capital Letters &amp; Apostrophes (90 seconds):</strong> Check that every sentence starts with a capital, every proper noun (days, months, names, street names, 'I') is capitalised, and every possessive noun has its apostrophe (while <em>its</em> has none).</li>
                    <li><strong>Pass 4 — High-Risk Spelling &amp; Homophone Scan (60 seconds):</strong> Check every instance of <em>their/there/they're</em>, <em>to/too</em>, <em>practice/practise</em>, and check long words against the exam paper.</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Before & After: Annotated Proofreading Pass on a Student Draft",
                "summary": "Watch how catching 6 small slips upgrades a Band 1 SPaG draft to Band 3.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Unchecked Student Draft (6 Hidden SPaG Errors):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"On tuesday morning i visited oakwood clinic for my blood test, the waiting room was freezing cold. Neither of the receptionists were helpful when Staff asked for there coats."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Post-Proofread Final Version (All 6 Errors Fixed):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"On <strong>Tuesday</strong> morning<strong>, I</strong> visited <strong>Oakwood Clinic</strong> for my blood test<strong>;</strong> the waiting room was freezing cold. Neither of the receptionists <strong>was</strong> helpful when <strong>staff</strong> asked for <strong>their</strong> coats."</em>
                  </div>
                </div>
                """
            },
            {
                "title": "Editing for Conciseness & Word Count Control",
                "summary": "How to trim a bloated draft or expand a thin paragraph during your review.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>If Your Draft Is Too Short (&lt;200 words at L2):</strong> Add a specific real-world example or statistic to Paragraph 2 or 3 (e.g. <em>"For instance, a recent staff survey revealed that 72% of evening workers..."</em>).</li>
                    <li><strong>If Your Draft Is Repetitive:</strong> Delete duplicate adjectives (e.g. replace <em>"very unique and completely essential"</em> with <em>"essential"</em>) and cut repeated points.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Proofreading a Retail Customer Apology Email",
                "marks": "Level 1 Proofreading Benchmark (3 Marks)",
                "context": "Customer Service Email Audit",
                "question": "Proofread this short customer email and correct the <strong>three errors</strong> (1 capital letter error, 1 homophone error, and 1 missing question mark):<br><em>'Dear Mrs Carter, I am sorry that your order did not arrive on wednesday. Our courier left the parcel at there local depot by mistake. Would you prefer us to redeliver the item tomorrow morning.'</em>",
                "steps": [
                    ("Step 1", "Fix the missing proper noun capital letter", "Days of the week are proper nouns: change 'wednesday' to 'Wednesday'.", "Capitalisation (L1.30)"),
                    ("Step 2", "Fix the homophone error", "'at there local depot' requires the possessive pronoun 'their'.", "Homophone Correction"),
                    ("Step 3", "Fix the terminal punctuation on the closing question", "'Would you prefer...' is a direct question requiring a question mark (?) instead of a full stop.", "Question Mark Accuracy")
                ],
                "final_answer": "1. wednesday → <strong>Wednesday</strong> | 2. there → <strong>their</strong> | 3. tomorrow morning. → <strong>tomorrow morning?</strong><br>Corrected email: 'Dear Mrs Carter, I am sorry that your order did not arrive on Wednesday. Our courier left the parcel at their local depot by mistake. Would you prefer us to redeliver the item tomorrow morning?'",
                "tutor_tip": "Direct questions starting with 'Would you', 'Could you', or 'How can we' frequently lose marks because candidates forget the question mark at the end!"
            },
            {
                "title": "Level 2 Model: 4-Category Audit of an Internal HR Compliance Memo",
                "marks": "Level 2 Proofreading & Editing Benchmark (4 Marks)",
                "context": "Human Resources & Safeguarding Compliance",
                "question": "Proofread this draft internal email and identify and fix <strong>four distinct errors</strong> (1 format error, 1 punctuation error, 1 spelling/homophone error, 1 grammar error):<br><br><em>From: hr@communityhealth.org<br>Date: 14 October 2026<br><br>Dear All Staff,<br>All clinical staff must complete there annual safeguarding refresher by Friday, failure to do so will result in temporary suspension from ward duties. Each of the ward supervisors are responsible for logging team certificates.<br>Yours faithfully,<br>Karen White, HR Director</em>",
                "steps": [
                    ("Step 1", "Format Error", "The email is missing a mandatory <strong>To:</strong> and <strong>Subject:</strong> line, and uses 'Yours faithfully' instead of 'Kind regards' or 'Yours sincerely'.", "Format Audit (L2.31)"),
                    ("Step 2", "Punctuation Error (Comma Splice)", "Comma splice between 'by Friday,' and 'failure to do so'. Replace the comma with a semicolon (;) or full stop.", "Punctuation Audit (L2.30)"),
                    ("Step 3", "Spelling / Homophone Error", "'complete there annual safeguarding' uses location 'there' instead of possessive 'their'.", "Spelling Audit"),
                    ("Step 4", "Grammar Error (Subject-Verb Agreement)", "'Each of the ward supervisors are' must be 'Each of the ward supervisors <strong>is</strong>' because 'Each' is singular.", "Grammar Audit")
                ],
                "final_answer": "1. <strong>Format:</strong> Add 'Subject: Mandatory Annual Safeguarding Refresher' and change sign-off to 'Kind regards,'.<br>2. <strong>Punctuation:</strong> Fix comma splice after 'Friday' with a semicolon (<em>'...by Friday; failure to do so...'</em>).<br>3. <strong>Spelling:</strong> Change 'there' to 'their'.<br>4. <strong>Grammar:</strong> Change 'Each of the ward supervisors are' to 'Each of the ward supervisors is'.",
                "tutor_tip": "Practising this 4-category scan (Format → Punctuation → Spelling → Grammar) trains your eye to spot every single examiner deduction before you click Submit."
            }
        ],
        "examiner_traps": [
            {
                "title": "Relying on Onscreen Exam Software to Auto-Capitalise or Spellcheck",
                "desc": "Unlike Microsoft Word or smartphone keyboards, Pearson Edexcel and City & Guilds onscreen exam portals do NOT auto-capitalise 'i' to 'I' or underline spelling errors in red!",
                "fix": "Manually press Shift for every capital 'I', every sentence start, and every proper noun."
            },
            {
                "title": "Leaving Missing Words Out When Typing Fast",
                "desc": "Under exam pressure, your thoughts move faster than your fingers, leading to skipped words like 'I am writing [to] complain about [the] service'.",
                "fix": "Point at each word on the screen with your cursor during your final read-through so you don't skip missing prepositions or articles."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Proofread this sentence and correct both errors:<br><em>'The doctors surgery closed it's doors early yesterday because of severe flooding.'</em>",
                "solution_steps": "1. Error 1: 'doctors surgery' is missing the possessive apostrophe → doctor's surgery (or doctors' surgery).<br>2. Error 2: 'it's doors' uses the contraction apostrophe instead of possessive pronoun 'its'.",
                "correct_answer": "'The doctor's surgery closed its doors early yesterday because of severe flooding.'",
                "tutor_tip": "Whenever you see two apostrophe words in the same sentence, check each one carefully: nouns need 's for possession, whereas 'its' never takes an apostrophe for possession."
            },
            {
                "marks": "3 Marks",
                "question": "Find and correct the <strong>three errors</strong> in this sentence from a job application letter:<br><em>'Having worked in retail for three years i have developed strong customer service skills, furthermore I am always punctual and realiable.'</em>",
                "solution_steps": "1. Missing introductory comma and lowercase pronoun 'i': change 'years i' to 'years, I'.<br>2. Comma splice before 'furthermore': change ', furthermore' to '; furthermore,' (or '. Furthermore,').<br>3. Spelling error: change 'realiable' to 'reliable'.",
                "correct_answer": "'Having worked in retail for three years, I have developed strong customer service skills; furthermore, I am always punctual and reliable.'",
                "tutor_tip": "Never leave a lowercase 'i' anywhere in your exam response—it is one of the first things examiners penalise."
            },
            {
                "marks": "4 Marks",
                "question": "A candidate wrote this closing paragraph to a named recipient (<strong>Dear Mr Thornton</strong>) at the end of a formal complaint letter:<br><em>'I hope you can sort this mess out soon cos we are fed up of waiting, i look forward to hearing from you.<br>Yours faithfully,<br>Sam'</em><br><br>Rewrite this closing paragraph and sign-off so that it achieves full marks for formal register, punctuation, and letter conventions.",
                "solution_steps": "1. Replace informal slang ('sort this mess out', 'cos', 'fed up of waiting') with formal business language.<br>2. Fix the comma splice and lowercase 'i' ('...waiting, i look...').<br>3. Change 'Yours faithfully' to 'Yours sincerely' (to match named recipient Mr Thornton) and provide a full name.",
                "correct_answer": "'I trust that you will investigate and resolve this matter promptly, as this ongoing delay is causing significant inconvenience. I look forward to receiving your written response within seven days.<br><br>Yours sincerely,<br>Samira Begum'",
                "tutor_tip": "Always sign off formal letters with both your first name and surname, and ensure 'Dear Mr Thornton' pairs with 'Yours sincerely'."
            }
        ]
    },

    # 13. Purpose in Writing: Persuade, Inform, Explain, Advise
    {
        "filename": "writing-why-are-you-writing.html",
        "clean_topic": "Purpose in Writing: Persuade, Inform, Explain, Advise",
        "intro_lead": "Identify the primary functional purpose of every exam prompt and deploy the exact rhetorical, analytical, informational, or advisory techniques required to achieve full Content marks.",
        "next_file": "writing-the-exam.html",
        "next_name": "Writing Exam Strategy",
        "spec_points": [
            ("L1.31 / L2.31", "Write with a clear understanding of purpose, adapting language and structure to persuade, inform, explain, or advise."),
            ("L2.32", "Deploy rhetorical devices, counter-arguments, and advisory modal verbs to achieve specific communicative outcomes.")
        ],
        "golden_rules": [
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 1: Match Your Toolkit to the Command Verb in the Prompt",
                "desc": "Highlight the command verb in the exam question: 'Persuade' requires rhetorical questions, statistics, and counter-arguments; 'Inform/Explain' requires clear facts, dates, and cause-and-effect; 'Advise' requires supportive modal verbs ('you should', 'we recommend').",
                "badge": "Persuade = DAFOREST & ROI | Inform = Objective Facts | Explain = Cause & Why | Advise = Supportive Guidance"
            },
            {
                "icon": "fa-flag-checkered",
                "title": "Golden Rule 2: Close With a Purpose-Aligned Call to Action",
                "desc": "Your final paragraph must seal your purpose: a persuasive proposal ends by urging approval of a trial; an informational notice ends with contact details for queries; a complaint ends with the specific remedy requested.",
                "badge": "Every final sentence must directly fulfil the core purpose of the prompt."
            }
        ],
        "skills": [
            {
                "title": "The 4 Functional Writing Purposes & Linguistic Toolkit",
                "summary": "How to adapt your sentence starters and techniques to each of the four exam purposes.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Primary Purpose</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Key Linguistic Features</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">High-Scoring Exam Sentence</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. To Persuade / Argue</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Direct address, Rhetorical questions, Rule of Three, credible statistics, knocking down counter-arguments.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Can we truly afford to ignore a measure that is safe, affordable, and proven to cut emissions by 35%?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. To Inform</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Precise dates, times, locations, neutral tone, subheadings, bulleted facts (Who, What, When, Where).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The staff car park resurfacing will commence at 07:00 on Monday 16 November and conclude on Friday 20 November."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. To Explain</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Causal conjunctions (<em>because, consequently, therefore, in order to</em>), step-by-step rationale.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The new two-factor login is required because external cyber-attacks on healthcare databases rose by 40% last year."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. To Advise / Guide</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Supportive modal verbs (<em>should, ought to, could</em>), empathetic reassurance, practical tips.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To avoid peak commuter traffic, delegates are strongly advised to use the Park &amp; Ride shuttle bus from Junction 4."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Persuasive Writing at Level 2: The Counter-Argument Rebuttal Technique",
                "summary": "Why anticipating and defeating an objection is the fastest way to reach Band 3 Content.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">In Level 2 persuasive letters, speeches, and articles, include a 2-sentence counter-argument rebuttal in Paragraph 3:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    <strong>Formula:</strong> <em>"Some critics may argue that [Objection]; however, [Evidence that proves them wrong]."</em><br><br>
                    <strong>Model Example:</strong> <em>"Some committee members may argue that installing water coolers on every floor is an unnecessary expense; however, the £400 annual rental cost is less than a single day's agency cover for dehydration-related sickness."</em>
                  </div>
                </div>
                """
            },
            {
                "title": "Balancing Dual-Purpose Tasks (e.g. 'Inform and Persuade')",
                "summary": "Many exam prompts combine two purposes—learn how to satisfy both.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Example Prompt:</strong> <em>"Write an email to staff informing them of the charity fun run and persuading them to sign up."</em></li>
                    <li><strong>How to Structure It:</strong> Use Paragraph 1 &amp; 2 to <strong>Inform</strong> (exact date, 5km route, start time, registration link), and Paragraph 3 to <strong>Persuade</strong> (team spirit, free medal, raising £2,000 for the local children's hospice).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Advisory Email to a New Apprentice Starting Next Week",
                "marks": "Level 1 Purpose (Advise & Inform) Benchmark (3 Marks)",
                "context": "Workplace Onboarding & Mentoring",
                "question": "Write a supportive 3-paragraph email to a new administrative apprentice, Leo, advising him on what to bring on his first day (Monday 9 November at 09:00), dress code, and lunch arrangements.",
                "steps": [
                    ("Step 1", "Warm welcome and clear arrival information (Inform)", "State start time (09:00 on Monday 9 November) and who to ask for at reception.", "Informative Clarity (L1.31)"),
                    ("Step 2", "Practical advice on dress code and ID documents (Advise)", "Use supportive modal verbs ('you should wear', 'please remember to bring') for smart-casual attire and passport/ID.", "Advisory Tone"),
                    ("Step 3", "Reassuring guidance on lunch and first-day buddy support", "Explain kitchen facilities and reassure Leo that his mentor will guide him through the day.", "Encouraging Close")
                ],
                "final_answer": "To: leo.davies@email.co.uk<br>Subject: Welcome to Oakfield Medical Practice – First Day Advice (Monday 9 November)<br><br>Dear Leo,<br><br>We are delighted that you are joining our administration team next Monday, 9 November. Please arrive at the main reception desk at 09:00, where I will meet you and issue your security pass.<br><br>For your first day, we advise wearing smart-casual office clothing, such as tailored trousers and a collared shirt. You should also bring your passport or driving licence so that HR can complete your identification check.<br><br>Finally, our staff kitchen has a fridge and microwave if you wish to bring a packed lunch, or we can visit the café across the road together during your break. Please reply if you have any questions at all!<br><br>Best wishes,<br>Hannah Reed, Senior Administrator",
                "tutor_tip": "Notice how the tone is warm, practical, and reassuring—perfectly matching the 'Advise and Inform' purpose."
            },
            {
                "title": "Level 2 Model: NHS Smoking Cessation Campaign Leaflet (Advise & Persuade)",
                "marks": "Level 2 Dual-Purpose Benchmark (4 Marks)",
                "context": "Public Health Promotion Campaign",
                "question": "Write the concluding two paragraphs of a public health leaflet intended to ADVISE and PERSUADE long-term smokers to enrol in a free local NHS stop-smoking clinic.",
                "steps": [
                    ("Step 1", "Combine empathetic advisory guidance with clinical evidence", "Acknowledge how challenging quitting is alone, then cite the 400% higher success rate with specialist support.", "Dual Purpose Alignment (L2.31)"),
                    ("Step 2", "Deploy Rule of Three and financial/health incentives", "Highlight saving £2,000 a year and improving breathing within 72 hours.", "Persuasive Rhetoric (L2.32)"),
                    ("Step 3", "Deliver a clear, motivating call to action", "Provide the free helpline number and drop-in clinic hours.", "Actionable Close")
                ],
                "final_answer": "'Quitting smoking is undeniably challenging, but you do not have to face cravings through willpower alone. We strongly recommend booking a free 15-minute consultation with our friendly NHS Stop Smoking advisers, who can prescribe tailored nicotine replacement patches and gum free of charge. Clinical studies prove that combining one-to-one support with dual nicotine therapy makes you four times more likely to quit permanently.<br><br>Within just 72 hours of your final cigarette, your lung capacity begins to recover—and quitting a twenty-a-day habit puts over £3,500 back into your pocket every year. Take the first step toward a healthier, wealthier, and smoke-free future by calling our confidential helpline on 0800 012 345 today.'",
                "tutor_tip": "Blending supportive advice ('we strongly recommend') with hard persuasive figures ('four times more likely', '£3,500 a year') hits every Level 2 marking descriptor."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing an Aggressive Sales Pitch When Asked to 'Inform' or 'Advise'",
                "desc": "If a prompt asks you to write an informational guide explaining a new recycling system, filling it with emotional exaggeration and exclamation marks misjudges the purpose.",
                "fix": "Match your emotional temperature to the prompt verb: 'Inform' and 'Explain' require calm, factual authority."
            },
            {
                "title": "Using Made-Up Surveys That Sound Ridiculous ('99.9% of People Agree')",
                "desc": "Writing 'According to a survey, 99.9% of people hate buses' sounds childish and unconvincing.",
                "fix": "Use realistic, believable figures in persuasive writing (e.g. 'According to our recent staff survey, 68% of commuters...')."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Identify the primary purpose (<strong>To Persuade / To Inform / To Instruct</strong>) of each sentence below:<br>1. <em>'Isolate the mains electricity switch before removing the inspection cover.'</em><br>2. <em>'Can our community afford to lose its only youth sports field to another luxury housing development?'</em>",
                "solution_steps": "1. Sentence 1 uses an imperative command verb ('Isolate') for a safety step → To Instruct.<br>2. Sentence 2 uses an emotive rhetorical question to rally opposition → To Persuade.",
                "correct_answer": "1. To Instruct | 2. To Persuade",
                "tutor_tip": "Imperative verbs ('Isolate', 'Wash', 'Press') always signal instructional writing; rhetorical questions signal persuasive writing."
            },
            {
                "marks": "3 Marks",
                "question": "Write a 2-sentence <strong>counter-argument and rebuttal</strong> for a persuasive letter to your manager asking to allow administrative staff to work from home one day a week.",
                "solution_steps": "1. Sentence 1 (Acknowledge the manager's likely objection): Mention concern about telephone cover or productivity.<br>2. Sentence 2 (Rebut with evidence): Explain how cloud phone forwarding and rotating rota days maintain 100% office cover while boosting output.",
                "correct_answer": "'Some managers may be concerned that allowing remote working one day per week could leave the main reception telephone lines understaffed; however, rotating home-working days across the five-person team ensures four administrators remain on site at all times. Furthermore, our cloud telephone system routes calls seamlessly to staff laptops, guaranteeing uninterrupted client service.'",
                "tutor_tip": "Using 'Some may be concerned that...; however,...' shows the examiner you can evaluate multiple viewpoints at Level 2."
            },
            {
                "marks": "4 Marks",
                "question": "A prompt instructs: <em>'Write an article for your college website explaining why apprenticeships offer a valuable alternative to university and advising school leavers on how to apply.'</em><br>Draft a 4-sentence paragraph that fulfils both the <strong>Explain</strong> and <strong>Advise</strong> purposes.",
                "solution_steps": "1. Sentences 1–2 (Explain): Explain why apprenticeships are valuable (earning a salary while gaining an accredited qualification without £40,000 of student debt).<br>2. Sentences 3–4 (Advise): Advise school leavers on practical application steps (registering on the government apprenticeship portal and tailoring their CV).",
                "correct_answer": "'Higher and degree apprenticeships offer a compelling alternative to traditional university degrees because learners earn a full-time salary while gaining practical industry experience and a recognized qualification, graduating with zero student loan debt. Consequently, over 85% of apprentices secure permanent employment immediately upon completing their programme. If you are considering this route, we strongly advise registering on the official Find an Apprenticeship portal before the spring recruitment window opens. Additionally, you should ask your college careers adviser to review your CV and arrange a mock interview.'",
                "tutor_tip": "Notice how 'because' and 'consequently' drive the explanation, while 'we strongly advise' and 'you should' deliver the advice."
            }
        ]
    },

    # 14. Writing Exam Strategy, Allocation & Word Counts
    {
        "filename": "writing-the-exam.html",
        "clean_topic": "Writing Exam Strategy, Allocation & Word Counts",
        "intro_lead": "Execute winning strategies for the 60-minute Functional Skills Writing exam: strict 30/30 time allocation across Task 1 and Task 2, hitting the word-count sweet spot, and defending the 42% SPaG allocation.",
        "next_file": "functional-skills-english-level-2-writing-blog.html",
        "next_name": "Level 2 Writing Examples & Models",
        "spec_points": [
            ("L1 / L2 Writing Exam Protocol", "Complete two distinct extended writing tasks within 60 minutes under regulated exam conditions."),
            ("Content vs SPaG Mark Split", "Maximise marks across both assessment grids: Content & Organisation (~58%) and SPaG (~42%).")
        ],
        "golden_rules": [
            {
                "icon": "fa-clock",
                "title": "Golden Rule 1: Follow the Strict 30/30 Minute Split Across Both Tasks",
                "desc": "The 60-minute exam contains two tasks. Never spend 45 minutes perfecting Task 1 and leave only 15 minutes for Task 2! Allocate 30 minutes per task (or 35 minutes on the longer task and 25 minutes on the shorter task).",
                "badge": "Task 1 (30 mins): 5m Plan + 20m Write + 5m Check | Task 2 (30 mins): 5m Plan + 20m Write + 5m Check"
            },
            {
                "icon": "fa-text-width",
                "title": "Golden Rule 2: Hit the 220–280 Word Sweet Spot (Quality Beats Quantity)",
                "desc": "At Level 2, writing only 90 words caps your Content & Grammar marks at Band 1. Conversely, writing 550 words wastes time and multiplies your risk of spelling and comma-splice errors. Aim for 250–300 polished words on the main task and 200–250 words on the second task.",
                "badge": "Level 1 Sweet Spot: 150–200 words | Level 2 Sweet Spot: 230–300 words"
            }
        ],
        "skills": [
            {
                "title": "Inside the Pearson Edexcel Level 2 Writing Mark Scheme (36 Total Marks)",
                "summary": "Understand exactly where every mark comes from so you can target all examiner tick-boxes.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Assessment Category</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Mark Weighting</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">What You Must Do to Score Top Band</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Content, Audience &amp; Format</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">~35% of total marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Address 100% of prompt bullets in convincing detail; use exact format layout (addresses/headings); maintain consistent tone.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Organisation &amp; Cohesion</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">~23% of total marks</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Sequence into 4–5 clear paragraphs with blank lines between them; link ideas smoothly using discourse markers (<em>Furthermore, Consequently</em>).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Spelling, Punctuation &amp; Grammar (SPaG)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">~42% of total marks (9 marks per task!)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Mix simple, compound, and complex sentences; use apostrophes, colons, and semicolons accurately; zero comma splices; accurate spelling of specialist vocabulary.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "The 5-Point 'Examiner Tick-List' to Include in Every Response",
                "summary": "Write this 5-item checklist at the top of your scratch paper in every exam.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>[ ] 1. Format Header &amp; Sign-Off:</strong> Addresses + Date + Salutation (Letter) OR Title + Subheadings (Report/Article) OR To + Subject (Email).</li>
                    <li><strong>[ ] 2. Four Clear Paragraphs:</strong> Separated by a full blank line so paragraphing is visually unmistakable.</li>
                    <li><strong>[ ] 3. Three Discourse Markers:</strong> e.g. <em>Furthermore, However, Consequently</em> (each followed by a comma).</li>
                    <li><strong>[ ] 4. One Fronted Complex Sentence:</strong> Starting with <em>Although..., Whilst...,</em> or <em>Because...</em> with a comma after the first clause.</li>
                    <li><strong>[ ] 5. One Colon (:) and One Semicolon (;):</strong> Used accurately to introduce a list/explanation and link two related clauses.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Onscreen Exam Typing & Formatting Tips",
                "summary": "How to make your response look clean inside the basic Pearson / City & Guilds onscreen text box.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Always Press Enter Twice Between Paragraphs:</strong> In plain text boxes, single line breaks look squashed. Leave a clear blank line between every paragraph, address block, and subheading.</li>
                    <li><strong>Use Asterisks or Hyphens for Bullet Points:</strong> If the onscreen toolbar lacks a bullet icon, simply type a hyphen (<code>- </code>) on a new line for each bullet point.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Level 1 Model: Deconstructing an Exam Prompt into a 30-Minute Game Plan",
                "marks": "Level 1 Exam Strategy Benchmark",
                "context": "Timed Exam Deconstruction",
                "question": "Read this Level 1 exam prompt:<br><em>'Your local park has become littered and the children's swings are damaged. Write an email (150–200 words) to Councillor Green explaining the problems, how they affect local families, and what the council should do.'</em><br>Show the exact 5-step exam execution plan.",
                "steps": [
                    ("Step 1", "Extract PAF & Headers (Minute 1)", "<strong>Format:</strong> Formal Email | <strong>To:</strong> c.green@council.gov.uk | <strong>Subject:</strong> Urgent Repairs & Litter Clearance Needed at Victoria Park | <strong>Salutation:</strong> Dear Councillor Green,", "PAF Locked In"),
                    ("Step 2", "Map 3 Paragraphs to the 3 Prompt Bullets (Minutes 2–5)", "Para 1: Overflowing bins and rusted broken chains on toddler swings.<br>Para 2: Families avoiding the park; broken glass hazard for children and dogs.<br>Para 3: Repair swings, install two larger recycling bins, and add weekly ranger patrol.", "100% Bullet Coverage"),
                    ("Step 3", "Draft & Proofread (Minutes 6–30)", "Write 175 words across 3 clear paragraphs, close with 'Yours sincerely,' and spend the final 4 minutes checking capital letters and full stops.", "Timed Completion")
                ],
                "final_answer": "Complete 30-minute strategy: 5m PAF & 3-paragraph bullet map → 20m drafting (~175 words with To/Subject headers and 'Yours sincerely') → 5m SPaG check.",
                "tutor_tip": "Notice how turning the three prompt requirements directly into Paragraphs 1, 2, and 3 makes running out of ideas impossible."
            },
            {
                "title": "Level 2 Model: Upgrading a Borderline Fail Draft into a Band 3 Pass",
                "marks": "Level 2 Marking Criteria Comparison (9 SPaG + 12 Content Marks)",
                "context": "Examiner Marking Analysis",
                "question": "Compare why Draft A scores only 8/21 (Fail) while Draft B scores 19/21 (Distinction-level Pass) on the same Level 2 report task about staff car park congestion.",
                "steps": [
                    ("Step 1", "Analyse Draft A (8/21 — Borderline Fail)", "<em>'The car park is always full in the morning, people park on the grass and block ambulances, we should give out permits and let people cycle.'</em><br><strong>Why it fails:</strong> No report title or subheadings, only 25 words, two comma splices, vague detail.", "Band 1 Content & SPaG"),
                    ("Step 2", "Analyse Draft B (19/21 — Top Band Pass)", "Includes bold Report Title, To/From/Date, numbered subheadings (<em>1.0 Current Congestion Hazards, 2.0 Permit & Car-Share Proposals</em>), complex sentences, semicolon, and realistic figures.", "Band 3 Content & SPaG"),
                    ("Step 3", "Key Examiner Takeaway", "Adding structural headings, expanding each bullet to 70–80 words with concrete examples, and eliminating comma splices doubles the score.", "Strategic Upgrade")
                ],
                "final_answer": "Draft B achieves 19/21 by combining full report formatting (Title + numbered subheadings), sustained operational detail (260 words), and varied Level 2 punctuation (colon, semicolon, and zero comma splices).",
                "tutor_tip": "You don't need to be a novelist to pass Level 2 Writing—you just need clear formatting, 4 structured paragraphs, and clean sentence punctuation."
            }
        ],
        "examiner_traps": [
            {
                "title": "Submitting a Single Unbroken 250-Word Block of Text",
                "desc": "Even if your vocabulary and spelling are good, forgetting to divide your response into paragraphs automatically caps your Organisation mark at Band 1.",
                "fix": "If you realise at the end of the exam that you forgot paragraph breaks, press Enter twice before each major topic shift to create clear paragraphs."
            },
            {
                "title": "Spending 45 Minutes on Task 1 and Leaving Task 2 Half-Finished",
                "desc": "An unfinished 60-word response on Task 2 loses up to 10 marks—far more than you could ever gain by polishing Task 1 for an extra 15 minutes.",
                "fix": "Watch the onscreen clock strictly: when 30 minutes have elapsed, move immediately to Task 2."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "In a 60-minute Writing exam where Task 1 is worth 21 marks (250–300 words) and Task 2 is worth 15 marks (200–250 words), how should you divide your 60 minutes, and why?",
                "solution_steps": "1. Allocate approximately 33–35 minutes to Task 1 (more marks and higher word count) and 25–27 minutes to Task 2.<br>2. Ensure both tasks include 4–5 minutes of planning and 4–5 minutes of proofreading.",
                "correct_answer": "Allocate 35 minutes to Task 1 (5m plan, 25m write, 5m check) and 25 minutes to Task 2 (4m plan, 17m write, 4m check) to reflect the mark weighting while guaranteeing both tasks are completed in full.",
                "tutor_tip": "Never give any task less than 25 minutes—both tasks carry heavy SPaG marks."
            },
            {
                "marks": "3 Marks",
                "question": "A student wrote a 260-word formal letter that covered all the prompt bullets well, but lost 6 out of 9 SPaG marks because they joined almost every pair of sentences with a comma (comma splices).<br>Repair the three comma splices in their paragraph below:<br><em>'The community library is a vital hub for elderly residents, it provides free internet access and warm reading rooms, however the council plans to cut its funding by half, this will force the library to close on Saturdays.'</em>",
                "solution_steps": "1. Fix splice 1 ('...elderly residents, it provides...') with a semicolon or 'as it provides'.<br>2. Fix splice 2 ('...reading rooms, however...') by starting a new sentence: '. However,'.<br>3. Fix splice 3 ('...by half, this will...') by using ', which will force...'.",
                "correct_answer": "'The community library is a vital hub for elderly residents, as it provides free internet access and warm reading rooms. However, the council plans to cut its funding by half, which will force the library to close on Saturdays.'",
                "tutor_tip": "Never put ', however,' between two complete sentences—always use '; however,' or '. However,'!"
            },
            {
                "marks": "4 Marks",
                "question": "Read this exam prompt: <em>'Write a report (250–300 words) for your Retail Store Manager on ways to reduce single-use plastic packaging in the store.'</em><br>Write out the <strong>5-item Examiner Tick-List</strong> showing the exact Format headers, Discourse markers, Complex sentence starter, Colon, and Semicolon you will include in this report.",
                "solution_steps": "1. Format headers: Title + To/From/Date + 3 numbered subheadings.<br>2. Three discourse markers: Furthermore, Consequently, However.<br>3. Fronted complex sentence: 'Whilst biodegradable bags cost 4p more per unit, customers strongly support...'<br>4. Colon and Semicolon examples tailored to plastic reduction.",
                "correct_answer": "1. Format: Title ('Report on Reducing Single-Use Plastic Packaging'), To/From/Date header, and numbered subheadings (1.0 Introduction, 2.0 Packaging Findings, 3.0 Recommendations).<br>2. Discourse Markers: Furthermore, Consequently, Nevertheless.<br>3. Complex Sentence: 'Whilst loose produce paper bags cost slightly more to procure, they eliminate over 10,000 plastic wrappers monthly.'<br>4. Colon & Semicolon: 'We recommend three immediate changes: ...' (colon) and 'Plastic carrier bag sales have dropped by 40%; however, bakery film waste remains high.' (semicolon).",
                "tutor_tip": "Planning your exact colon and semicolon sentences before you start writing ensures you never forget them under exam stress."
            }
        ]
    },

    # 15. English Level 2 Writing Examples & Model Responses (Blog / Hub Page)
    {
        "filename": "functional-skills-english-level-2-writing-blog.html",
        "clean_topic": "English Level 2 Writing Examples & Model Responses",
        "intro_lead": "Master full-mark Functional Skills English Level 2 writing responses across all four assessed formats — formal letters, workplace emails, persuasive articles/blogs, and structured reports — calibrated to Pearson Edexcel & City & Guilds marking criteria.",
        "next_file": "writing-planning-your-answer.html",
        "next_name": "Planning Written Responses",
        "spec_points": [
            ("L2.21 / L1.22", "Communicate information, ideas, and opinions clearly, coherently, and effectively across extended written documents."),
            ("L2.22 / L2.23", "Write text of an appropriate level of detail and length (250–350 words) using format, structure, and vocabulary suited to purpose and audience."),
            ("L2.24 / L2.25", "Organise writing into logical paragraphs using cohesive discourse markers and accurate grammar, punctuation, and spelling (SPaG).")
        ],
        "golden_rules": [
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 1: Lock In Your Format Conventions Before Writing Paragraph 1",
                "desc": "Examiners check format layout in the first 10 seconds. Formal letters require sender and recipient addresses, the date, a formal salutation, and matching sign-off (Dear Sir/Madam → Yours faithfully; Dear Mr Patel → Yours sincerely). Articles and blogs require a compelling headline and subheadings; reports require a title, subheadings (Introduction, Findings, Recommendations), and bullet points; emails require To, Subject, and a professional greeting.",
                "badge": "Letter: 2 Addresses + Date + Sign-Off | Article/Blog: Headline + Subheadings | Report: Title + Findings + Bullets"
            },
            {
                "icon": "fa-spell-check",
                "title": "Golden Rule 2: Protect the 42% SPaG Allocation by Eliminating Comma Splices",
                "desc": "In Pearson Edexcel and City & Guilds Level 2 Writing, roughly 40–45% of total marks are awarded purely for Spelling, Punctuation, and Grammar (SPaG). Never join two standalone sentences with a comma — use a full stop, semicolon, or subordinating conjunction (although, whereas, consequently).",
                "badge": "Use Complex Sentences + Semicolons + Zero Comma Splices = Maximum SPaG Band"
            }
        ],
        "skills": [
            {
                "title": "The 4 Core Level 2 Writing Formats Compared",
                "summary": "Side-by-side structural and register blueprint for every document type tested in Functional Skills English Level 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Format Type</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Mandatory Layout Features</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Tone, Register &amp; Key Devices</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Formal Letter</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Sender address (top right), Date, Recipient address (left), <em>Dear Sir/Madam</em> or <em>Dear Ms...</em>, 3–4 paragraphs, <em>Yours faithfully / sincerely</em> + full name.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Formal, courteous, objective, zero contractions (write <em>do not</em>, <em>cannot</em>). State purpose in sentence 1.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Article / Community Blog</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Engaging Headline, Byline / Topic intro, 2–3 thematic subheadings, concluding call-to-action or reader comment prompt.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Semi-formal, lively, persuasive; uses rhetorical questions, direct address (<em>you</em>, <em>our community</em>), and Rule of Three.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Workplace Report</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Report Title, To/From/Date header, numbered or bold subheadings (<em>1. Introduction, 2. Key Findings, 3. Recommendations</em>), bulleted action points.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Impersonal, analytical, evidence-led; uses passive constructions and statistical evidence.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. Workplace / Formal Email</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>To:</strong> [Email], <strong>Subject:</strong> [Clear concise summary], Salutation, clear paragraphs, professional sign-off (<em>Kind regards</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Direct, structured, professional; adapts formality to recipient (colleague vs external director).</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "High-Scoring Level 2 Sentence Starters & Discourse Markers",
                "summary": "Upgrade simple Band 1 sentences into cohesive Band 3 Level 2 prose using sophisticated transitions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.85; color:#334155;">
                    <li><strong>Opening Purpose (Formal Letter / Email):</strong> <em>"I am writing to express my serious concern regarding..."</em> | <em>"Further to our recent departmental audit, I am writing to outline..."</em></li>
                    <li><strong>Developing &amp; Adding Evidence:</strong> <em>"Furthermore, recent staff feedback indicates that..."</em> | <em>"In addition to the financial benefits, this initiative will..."</em></li>
                    <li><strong>Contrasting &amp; Evaluating Perspectives:</strong> <em>"Whilst the initial capital outlay appears substantial, the long-term savings..."</em> | <em>"Conversely, failing to upgrade these facilities risks..."</em></li>
                    <li><strong>Concluding &amp; Recommending Action:</strong> <em>"In light of these findings, I strongly recommend that..."</em> | <em>"I look forward to receiving your prompt confirmation regarding these proposals."</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "How to Structure a High-Scoring Community or Workplace Blog Post",
                "summary": "Specific conventions that distinguish an interactive blog post from a standard print article.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Blog Header / Metadata:</strong> Include a catchy <strong>Blog Title</strong> and a short date/author line (e.g. <em>Posted by Maya Lin | 14 October 2026 | Community Green Hub</em>).</li>
                    <li><strong>Conversational yet Articulate Hook:</strong> Address readers directly (<em>"Have you noticed how..."</em>) and establish an inclusive, motivating voice.</li>
                    <li><strong>Scannable Subheadings &amp; Bullet Tips:</strong> Break up online text with 2 bold subheadings and a short 3-bullet takeaway list.</li>
                    <li><strong>Interactive Sign-Off:</strong> End by inviting reader comments or shares (e.g. <em>"What changes would you like to see in our town centre? Share your thoughts in the comments box below!"</em>).</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1: Community Wellbeing Blog / Article — Launching a Workplace Cycle-to-Work Scheme",
                "marks": "21 Marks (Pearson Edexcel Level 2 Writing Task — Content 12 + SPaG 9)",
                "context": "NHS Trust Staff Intranet Blog & Wellbeing Portal",
                "question": "Your hospital trust is launching a new Cycle-to-Work and secure bike storage scheme. Write a blog post (250–300 words) for the staff intranet persuading employees to join the scheme, explaining the health and financial benefits, and addressing safety concerns.",
                "steps": [
                    ("Step 1", "Headline, Byline & Engaging Opening Hook", "<strong>Headline:</strong> Ditch the Traffic Jam: Why Our New Cycle-to-Work Scheme Is a Win for Your Wallet and Wellbeing<br><em>Posted by Samira Khan, Staff Wellbeing Coordinator | 14 October 2026</em><br><strong>Opening:</strong> Are you tired of sitting in gridlocked hospital car park queues every morning while paying rising fuel prices? Next month, our Trust is launching an upgraded Cycle-to-Work programme designed for every staff member.", "Format & Audience Hook (Content Band 3)"),
                    ("Step 2", "Subheading 1: Financial & Physical Health Benefits", "<strong>Save Up to 40% While Boosting Your Energy</strong><br>Through salary sacrifice, staff can save up to 40% on a brand-new commuter bike or electric bicycle, spreading the cost interest-free over twelve months. Furthermore, cycling just twenty minutes each way burns calories, reduces cardiovascular risk, and ensures you arrive on the ward feeling energised rather than stressed.", "Addresses Prompt Bullets + Complex Sentences"),
                    ("Step 3", "Subheading 2: Addressing Safety & Storage + Interactive Call to Action", "<strong>Safe, Lit Routes and Card-Access Bike Hubs</strong><br>We know that bike security and wet weather have previously deterred staff; consequently, the Estates team has installed heated shower rooms and CCTV-monitored cycle pods outside the Main Wing.<br><strong>Ready to Ride?</strong> Click the Staff Benefits tab today to claim your voucher, or drop your questions in the comments box below!", "Semicolon + Cohesive Conclusion + Blog Sign-off")
                ],
                "final_answer": "Full-mark Level 2 blog response featuring a bold headline, date/author byline, two thematic subheadings, rhetorical question hook, semicolon connecting independent clauses, statistical detail (40% savings), and interactive blog comment call-to-action.",
                "tutor_tip": "Notice how a blog post differs from a formal report: it uses direct address ('you', 'our Trust'), an engaging conversational yet polished tone, subheadings, and invites reader comments at the end."
            },
            {
                "title": "Model 2: Formal Complaint & Proposal Letter to Local Council Highways Department",
                "marks": "21 Marks (Pearson Edexcel Level 2 Formal Letter Benchmark)",
                "context": "Road Safety & Pedestrian Infrastructure",
                "question": "Write a formal letter (250–300 words) to Mr David Vance, Head of Highways at Westshire Council, complaining about dangerous speeding outside Oakfield Primary School and proposing specific traffic-calming measures.",
                "steps": [
                    ("Step 1", "Full Letter Address Block, Date & Named Salutation", "Sender address + Date (top right); Mr David Vance, Head of Highways, Westshire Council (left); Salutation: <em>Dear Mr Vance,</em> + Subject line: <em>Re: Urgent Request for Traffic-Calming Measures on Oakfield Lane</em>.", "Full Letter Layout (L2.23)"),
                    ("Step 2", "Body Paragraphs (Evidence + Counter-Argument + Solutions)", "Detail morning peak speeding (vehicles exceeding 40 mph in a 20 mph zone) and last week's near-miss on the zebra crossing. Propose three measures: digital speed-indicator signs, raised speed cushions, and peak-hour school crossing patrols.", "Sustained Persuasive Detail (L2.21)"),
                    ("Step 3", "Formal Close & Matching Sign-Off", "Urge a site inspection before winter dark mornings arrive and close with <em>Yours sincerely,</em> + full name.", "Register & Sign-Off Accuracy")
                ],
                "final_answer": "<div style='text-align:right;'>28 Oakfield Lane, Westshire, WS4 2LP<br>14 October 2026</div><br>Mr David Vance, Head of Highways<br>Westshire County Council, Civic Way, WS1 1AA<br><br>Dear Mr Vance,<br><br><strong>Re: Urgent Request for Traffic-Calming Measures Outside Oakfield Primary School</strong><br><br>I am writing on behalf of the Oakfield Residents' Association to express our grave concern regarding persistent vehicle speeding along Oakfield Lane between 08:15 and 09:00.<br><br>Although Oakfield Lane is designated as a 20 mph school zone, commuter vehicles routinely use the street as a shortcut, frequently exceeding 40 mph. Last Thursday morning, a delivery van failed to stop at the pedestrian crossing, narrowly missing two seven-year-old pupils; consequently, parents now fear a fatal collision is inevitable unless physical deterrents are installed.<br><br>Whilst we recognise that council highways budgets are tightly constrained this financial year, the cost of preventative safety infrastructure is minimal compared to the human cost of a serious accident. We therefore urge your department to implement three urgent measures: installing solar-powered digital speed-indicator signs, constructing raised speed cushions on the approach to the school gates, and funding a dedicated school crossing patrol officer.<br><br>I invite a highways engineer to observe morning drop-off traffic next week and look forward to your prompt written response.<br><br>Yours sincerely,<br>Rebecca Sterling<br>Chair, Oakfield Residents' Association",
                "tutor_tip": "Study how this letter hits every single Level 2 top-band requirement: two addresses, date, 'Re:' line, fronted 'Although' clause, semicolon before 'consequently', counter-argument starting with 'Whilst', colon introducing a 3-item list, and 'Yours sincerely'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting Subheadings in Articles, Blogs, and Reports",
                "desc": "Candidates frequently write an article or blog post as plain continuous paragraphs without a headline or subheadings, losing essential format and organisational marks.",
                "fix": "Always write a clear, bold Headline at the top of every article/blog, and include at least two short subheadings to divide your main sections."
            },
            {
                "title": "Using Informal Contractions and Slang in Formal Letters and Reports",
                "desc": "Writing 'don't', 'can't', 'it's', or 'kids' in a formal letter to a Council Director undermines your register mark.",
                "fix": "In formal tasks, write 'do not', 'cannot', 'it is', and 'pupils/children'."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "You are asked to write a formal letter to the Director of Estates, Mrs Helen Vance, proposing improvements to the staff canteen. Write: (a) the correct salutation, (b) an appropriate formal opening sentence, and (c) the correct complimentary close.",
                "solution_steps": "1. Salutation: 'Dear Mrs Vance,' (named recipient).<br>2. Opening sentence: 'I am writing on behalf of the clinical staff team to propose three practical improvements to the hospital canteen facilities.'<br>3. Complimentary close: 'Yours sincerely,' followed by your full name.",
                "correct_answer": "(a) Dear Mrs Vance, | (b) I am writing on behalf of the clinical staff team to propose three practical improvements to the hospital canteen facilities. | (c) Yours sincerely, [Full Name]",
                "tutor_tip": "Because the recipient's name (Mrs Vance) is given in the prompt, you must use 'Yours sincerely', never 'Yours faithfully'."
            },
            {
                "marks": "3 Marks",
                "question": "Write an engaging <strong>Headline</strong>, <strong>Byline</strong>, and <strong>2-sentence opening hook</strong> (including a rhetorical question) for a community blog post encouraging local residents to volunteer at a weekend riverbank clean-up.",
                "solution_steps": "1. Write a catchy, action-oriented headline.<br>2. Add a blog byline (Author + Date).<br>3. Open with a rhetorical question about the local river and invite residents to Saturday's clean-up.",
                "correct_answer": "<strong>Headline:</strong> Let’s Restore Our Riverbank: Join Saturday’s Two-Hour Community Clean-Up!<br><em>Posted by Liam O'Connor | 14 October 2026 | Riverside Neighbourhood Blog</em><br><br>Have you walked along the River Cherwell footpath recently and felt disheartened by the plastic bottles and discarded shopping trolleys choking our wildlife habitats? This Saturday from 10:00 to 12:00, fifty local volunteers are teaming up to transform our riverbank—and we need your help to make a lasting difference.",
                "tutor_tip": "Combining a direct rhetorical question with a dash ('—and we need your help') creates an authentic, lively blog voice."
            },
            {
                "marks": "4 Marks",
                "question": "Upgrade this weak Band 1 report conclusion into a formal, high-scoring Band 3 Level 2 report <strong>Recommendations</strong> section:<br><em>'So basically I think the office should buy recycling bins for paper and plastic and tell staff to turn off their computers at night so we save money.'</em>",
                "solution_steps": "1. Add a numbered subheading ('3.0 Strategic Recommendations').<br>2. Replace casual phrasing ('So basically I think') with an authoritative formal lead-in ending with a colon.<br>3. Format the two recommendations as parallel bullet points with bold lead-ins and measurable impacts.",
                "correct_answer": "<strong>3.0 Strategic Recommendations</strong><br>In light of the audit findings, senior management should implement the following two sustainability measures immediately:<br>• <strong>Dual-Stream Recycling Stations:</strong> Install colour-coded paper and plastic recycling bins next to every printer hub to divert 70% of office waste from landfill.<br>• <strong>Mandatory Overnight Shutdown Policy:</strong> Instruct all staff to power down desktop terminals and monitors at 17:30 daily, reducing annual electricity expenditure by approximately £1,400.",
                "tutor_tip": "Replacing 'So basically I think' with 'In light of the audit findings, senior management should implement...' transforms the authority of your writing."
            }
        ]
    }
]
