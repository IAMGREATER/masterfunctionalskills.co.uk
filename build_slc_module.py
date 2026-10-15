#!/usr/bin/env python3
import json

SLC_TOPICS = [
    {
        "filename": "slc-key-slc-skills.html",
        "clean_topic": "Key Speaking, Listening & Communicating Skills",
        "intro_lead": "Master the core assessment standards, active listening techniques, and verbal articulation strategies required to achieve full certification in Pearson Edexcel Level 1 and Level 2 Functional Skills English.",
        "next_file": "slc-communicating.html",
        "next_name": "Communicating Clearly & Purposefully",
        "spec_points": [
            ("L1.1 / L2.1", "Identify relevant information and lines of argument in spoken explanations and presentations."),
            ("L1.2 / L2.2", "Make requests and ask detailed questions using appropriate register and language."),
            ("L1.3 / L2.3", "Communicate information, ideas, and opinions clearly and effectively, providing further elaboration."),
            ("L2.7", "Respect the turn-taking rights of others during discussions, using appropriate spoken conventions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-ear-listen",
                "title": "Golden Rule 1: Active Listening Constitutes Half Your Grade",
                "desc": "Assessors grade you not just when you speak, but on how effectively you listen. Nodding, taking brief notes, referencing a peer's point, and asking clarifying questions prove active engagement.",
                "badge": "Examiner Focus: Do you build on what others say, or merely wait for your turn to talk?"
            },
            {
                "icon": "fa-diagram-project",
                "title": "Golden Rule 2: Use the P-E-E-R Spoken Structure",
                "desc": "Whenever contributing, state your Point, provide Evidence/Example, Explain the vocational impact, and Redirect to the team ('Point, Evidence, Explanation, Redirect').",
                "badge": "Structure: Point → Evidence → Explanation → Redirect"
            }
        ],
        "skills": [
            {
                "title": "The Two Compulsory SLC Exam Components",
                "summary": "Understanding the structure of the Pearson Edexcel Speaking and Listening assessment.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Assessment Component</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Format &amp; Duration</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Core Assessed Skills</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Task 1: Formal Presentation</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">L1: 2–3 mins + Q&amp;A<br>L2: 3–5 mins + Q&amp;A</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Structured argument, visual or factual support, professional tone, responding to audience questions.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Task 2: Formal Group Discussion</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">10–15 mins (group of 3–5 candidates)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Collaborative problem solving, turn-taking conventions, challenging diplomatically, inviting quieter participants.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Active Listening vs Passive Hearing",
                "summary": "Demonstrating observable listening behaviors required on the assessor witness sheet.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Verbal Signposts of Listening:</strong> <em>"Following on from Marcus's point regarding staffing levels...", "To add to what Priya mentioned about infection control..."</em></li>
                    <li><strong>Non-Verbal Attentiveness:</strong> Maintain steady eye contact with the speaker, orient your posture toward them, and take short bullet notes.</li>
                    <li><strong>Clarification Prompts:</strong> <em>"Could you explain how that change would affect the weekend shift handover?"</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Multidisciplinary Team Ward Handover Meeting",
                "marks": "Pass Criteria (Pearson Edexcel Level 2 SLC)",
                "context": "NHS Healthcare Shift Handover",
                "question": "Observe the dialogue during a morning hospital ward meeting:<br><em>Colleague A: 'We had three fall incidents in Bay 2 last week. Call bells were ignored because the agency nurses didn't know the buzzer system.'<br>Candidate Response needed to demonstrate L2.3, L2.4, and L2.7.</em>",
                "steps": [
                    ("Step 1", "Acknowledge and validate the colleague's observation", "Say: 'Thank you for raising that, Marcus. Patient safety in Bay 2 is an urgent operational priority.'", "Turn-taking & active listening demonstrated"),
                    ("Step 2", "Provide constructive analysis and supporting evidence", "Say: 'According to our audit last month, 40% of agency staff receive less than ten minutes of ward induction.'", "L2.4: Supporting argument with persuasive evidence"),
                    ("Step 3", "Propose a structured vocational solution and invite feedback", "Say: 'I propose we implement a 5-minute laminated quick-start guide by every terminal. Elena, from an occupational therapy view, would that resolve the delay?'", "L2.7: Inviting others and guiding collaborative consensus")
                ],
                "final_answer": "Complete spoken contribution combines active listening acknowledgment, statistical evidence, practical solution, and inviting a quiet colleague into the discussion.",
                "tutor_tip": "Assessors look for candidates who synthesize points and invite others. Notice how the model response bridges Marcus's point to Elena's expertise."
            }
        ],
        "examiner_traps": [
            {
                "title": "The Silent Participant Trap",
                "desc": "Some candidates believe that simply sitting quietly and nodding is enough to pass the listening component. Assessors cannot award marks for unobservable listening.",
                "fix": "You must verbally reference other participants' contributions and ask at least two relevant follow-up questions during the discussion."
            },
            {
                "title": "Dominating the Airtime",
                "desc": "Speaking for 80% of the meeting will cause you to fail criteria L2.7 (respecting turn-taking rights) even if your points are brilliant.",
                "fix": "Keep individual speaking turns between 30 and 60 seconds, then deliberately hand over the floor with an open question."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "You are participating in a workplace meeting discussing whether your department should adopt a 4-day working week. A colleague argues: <em>'It will leave our customer service desk unstaffed on Fridays.'</em><br>Draft a 40-word spoken response that acknowledges their concern, introduces a counter-evidence point, and invites another colleague to contribute.",
                "solution_steps": "1. Acknowledge: 'That is a valid operational concern regarding Friday cover.'<br>2. Counter-evidence: 'However, trials at our sister depot showed staggered rotas maintained 100% phone coverage.'<br>3. Invite peer: 'David, how does the logistics team manage rotating rotas during peak periods?'",
                "correct_answer": "Demonstrates acknowledgment, data-driven rebuttal, and peer invitation.",
                "tutor_tip": "Keep the tone collaborative rather than combative. Never say 'You are wrong'; say 'That is an important concern, however...'"
            }
        ]
    },
    {
        "filename": "slc-communicating.html",
        "clean_topic": "Communicating Clearly, Coherently & Purposefully",
        "intro_lead": "Develop vocal projection, pace control, tone modulation, and professional poise to communicate complex instructions and vocational data with confidence and authority.",
        "next_file": "slc-adapting.html",
        "next_name": "Adapting Talk to Audience and Situation",
        "spec_points": [
            ("L1.1 / L2.3", "Communicate information, ideas, and opinions clearly and coherently in workplace contexts."),
            ("L2.5", "Use spoken techniques such as pitch, pace, and pause to clarify and develop points.")
        ],
        "golden_rules": [
            {
                "icon": "fa-gauge-high",
                "title": "Golden Rule 1: Master the Power of the Controlled Pause",
                "desc": "Rushing speech indicates nervousness and obscures technical instructions. Pause for 2 full seconds before major statistics or transitions; this commands authority and lets listeners process.",
                "badge": "Rule: 130–150 words per minute is optimal professional speaking cadence."
            },
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 2: The 4 Cs of Professional Speech",
                "desc": "Every spoken message must be Clear (unambiguous words), Concise (direct to the point), Coherent (logical chronological order), and Courteous (respectful tone).",
                "badge": "Clear • Concise • Coherent • Courteous"
            }
        ],
        "skills": [
            {
                "title": "Vocal Delivery Metrics",
                "summary": "Four physical dimensions of vocal technique assessed in formal SLC presentations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px;">
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#0284c7;"><i class="fa-solid fa-volume-high"></i> Projection &amp; Volume</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Project from the diaphragm so listeners in the furthest row hear effortlessly without you straining or shouting.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#16a34a;"><i class="fa-solid fa-stopwatch"></i> Pacing &amp; Tempo</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Maintain steady 140 wpm. Slow down slightly when delivering numbers, medication doses, or technical acronyms.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#ea580c;"><i class="fa-solid fa-wave-square"></i> Pitch &amp; Modulation</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Avoid flat monotone. Vary pitch to highlight key achievements, warnings, and calls to action.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#7c3aed;"><i class="fa-solid fa-person"></i> Non-Verbal Poise</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Open chest posture, uncrossed arms, purposeful hand gestures, and distributed eye contact across all listeners.</p>
                    </div>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Delivering a Health & Safety Depot Toolbox Briefing",
                "marks": "Full Criteria Level 2 (L2.3, L2.5)",
                "context": "Logistics & Warehousing Operations",
                "question": "Deliver a 60-second verbal briefing to forklift operators regarding newly designated pedestrian safety walkways in Bay 3.",
                "steps": [
                    ("Step 1", "Opening Hook & Clear Purpose", "'Good morning team. Please give me your full attention for 60 seconds on a critical safety update regarding Bay 3.'", "Establishes immediate clarity and seriousness"),
                    ("Step 2", "Key Factual Information with Vocal Emphasis", "'As of 06:00 today, the yellow cross-hatched lanes are strictly pedestrian-only. Forklifts must not cross these lines under any circumstances.' [Pause for 2 seconds]", "Pacing and pause emphasize the mandatory rule"),
                    ("Step 3", "Actionable Consequence & Sign-off", "'Breaching this policy triggers an automatic HSE incident review. Please sign the briefing sheet before collecting your vehicle keys. Thank you.'", "Concise, coherent, and professional")
                ],
                "final_answer": "Briefing is delivered under 60 seconds with clear vocational directives, deliberate pausing on safety boundaries, and clear sign-off.",
                "tutor_tip": "Notice how the speaker didn't ramble. Clear directives with explicit times and consequences make spoken instructions unmistakable."
            }
        ],
        "examiner_traps": [
            {
                "title": "Verbal Tics and Fillers ('Um', 'Like', 'You Know')",
                "desc": "Fillers weaken candidate authority and distract the assessor from the substance of your message.",
                "fix": "Replace fillers with silence. When gathering your thoughts, pause and close your mouth rather than saying 'like' or 'um'."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Standard",
                "question": "Outline a 45-second spoken handover message informing the incoming care assistant that Resident Mrs Patel requires assistance with mobility following a fall yesterday.",
                "solution_steps": "1. Resident identification & status: 'Mrs Patel in Room 14 had an uninjured minor fall yesterday.'<br>2. Specific instructions: 'She requires a two-person transfer assist for all mobility until the physiotherapist reviews her at 11:00.'<br>3. Documentation check: 'Her mobility chart has been updated on the tablet.'",
                "correct_answer": "Presents essential clinical information logically, specifying care requirements and documentation location.",
                "tutor_tip": "In healthcare handovers, clarity and precision prevent clinical errors. Keep information ordered chronologically."
            }
        ]
    },
    {
        "filename": "slc-adapting.html",
        "clean_topic": "Adapting Talk to Audience and Situation",
        "intro_lead": "Learn how to calibrate language, tone, register, and technical detail when moving between informal team discussions, client consultations, and formal executive presentations.",
        "next_file": "slc-asking.html",
        "next_name": "Asking Questions Effectively",
        "spec_points": [
            ("L1.2 / L2.6", "Use appropriate language and register suitable for purpose, subject, and audience in formal and informal situations."),
            ("L2.3", "Adapt verbal communication to suit varying levels of technical understanding.")
        ],
        "golden_rules": [
            {
                "icon": "fa-sliders",
                "title": "Golden Rule 1: Calibrate Formality Along the Register Continuum",
                "desc": "Match your vocabulary to the audience. Informal slang is unacceptable in an assessed presentation, while overly academic jargon alienates frontline clients.",
                "badge": "Informal Colleague → Professional Peer → Formal Boardroom"
            },
            {
                "icon": "fa-language",
                "title": "Golden Rule 2: Translate Specialist Terminology into Plain English",
                "desc": "When speaking to non-specialists (e.g. patients, customers, apprentices), immediately follow technical acronyms or jargon with an accessible explanation.",
                "badge": "Example: 'She is presenting with dyspnoea — that means shortness of breath.'"
            }
        ],
        "skills": [
            {
                "title": "The Register Adaptation Spectrum",
                "summary": "Comparing verbal phrasing across three workplace communication settings.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Scenario</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Inappropriate / Too Casual</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Professional Functional English</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Requesting Leave</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I need Friday off cos me mates are going away."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I would like to request annual leave for this Friday. I have arranged shift cover with Michael."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Explaining Delay</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The IT system went down, it's totally wrecked."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We experienced an unexpected server outage this morning, which delayed processing by two hours."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Challenging a Peer</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"That idea makes no sense whatsoever."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I see your rationale, but have we considered the cost implications for our quarterly budget?"</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Communicating a Discharge Plan to an Elderly Patient and Family",
                "marks": "Level 2 Assessment Benchmark (L2.6)",
                "context": "Health and Social Care Communication",
                "question": "A clinical note reads: <em>'Patient ambulates with zimmer frame. Requires BID domiciliary care package post-discharge.'</em> How should the care coordinator communicate this verbally to the patient and their daughter?",
                "steps": [
                    ("Step 1", "Establish warm, empathetic rapport", "'Good afternoon Mrs Davies, hello Claire. I would like to run through the support we have arranged for your return home.'", "Sets respectful, reassuring tone"),
                    ("Step 2", "Translate clinical terminology into clear plain English", "'To help you move around safely, you will have a walking frame. We have also arranged home carers to visit twice a day — once in the morning and once in the evening.'", "Replaces 'ambulates' and 'BID domiciliary' with accessible explanations"),
                    ("Step 3", "Check for understanding with open question", "'How does that sound to both of you, and what questions do you have about the visiting times?'", "Invites dialogue without putting patient on the spot")
                ],
                "final_answer": "Replaces technical jargon with compassionate, transparent terms while maintaining professional rigor and inviting family participation.",
                "tutor_tip": "Functional Skills examiners award high marks for candidates who demonstrate empathy and sensitivity to diverse audiences."
            }
        ],
        "examiner_traps": [
            {
                "title": "Over-Formality and Stilted Speech",
                "desc": "Trying to sound overly complex or reciting memorized thesaurus words often leads to confusion and unnatural phrasing.",
                "fix": "Aim for professional clarity: straightforward sentences, standard English vocabulary, and polite framing."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "You need to explain to a customer why their vehicle repair is taking 24 hours longer than estimated due to a backordered alternator. Frame your verbal explanation in 3 sentences using an adapted, professional customer service register.",
                "solution_steps": "1. Apology & cause: 'I apologize for the delay, Mr Robinson; the replacement alternator had to be sourced directly from the manufacturer.'<br>2. Updated timescale: 'The component arrives tomorrow at 09:00, and our technician will fit and test it by 14:00.'<br>3. Assurance: 'We will telephone you as soon as the final road test is completed.'",
                "correct_answer": "Expresses courteous apology, clear factual explanation, and concrete next steps.",
                "tutor_tip": "Always pair bad news with a definite solution and estimated time of completion."
            }
        ]
    },
    {
        "filename": "slc-asking.html",
        "clean_topic": "Asking Questions Effectively",
        "intro_lead": "Formulate open, probing, and clarifying questions to extract vital operational facts, stimulate collaborative discussion, and resolve ambiguities in professional settings.",
        "next_file": "slc-responding.html",
        "next_name": "Responding to Questions & Feedback",
        "spec_points": [
            ("L1.2 / L2.2", "Make requests and ask detailed questions using appropriate language in a range of contexts."),
            ("L2.1", "Identify relevant information and lines of argument through strategic inquiry.")
        ],
        "golden_rules": [
            {
                "icon": "fa-circle-question",
                "title": "Golden Rule 1: Use Open Questions to Stimulate Dialogue",
                "desc": "Closed questions that yield a single 'Yes' or 'No' kill discussion momentum. Use open interrogatives: How, Why, In what ways, Could you elaborate on... to invite substantive answers.",
                "badge": "Open: 'What steps are we taking to prevent delays?' vs Closed: 'Are we delayed?'"
            },
            {
                "icon": "fa-filter",
                "title": "Golden Rule 2: The Question Funnel Technique",
                "desc": "Start broad with an open question, narrow down with a probing question for specific evidence, and close with a clarifying question to lock in agreement.",
                "badge": "Broad Open → Detailed Probing → Closed Confirmation"
            }
        ],
        "skills": [
            {
                "title": "Questioning Taxonomy for Functional English",
                "summary": "Three types of questions assessed by Pearson Edexcel examiners.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>1. Clarifying Questions (Checking Facts):</strong> Used when details are vague. <em>"Could you specify which ward reported the shortage?"</em> or <em>"Am I right in thinking this takes effect from next Monday?"</em></li>
                    <li><strong>2. Probing Questions (Exploring Depth):</strong> Used to uncover rationale and evidence. <em>"What evidence supports the switch to 12-hour shifts?"</em> or <em>"How will this measure impact staff retention?"</em></li>
                    <li><strong>3. Collaborative / Inviting Questions (Facilitating Group):</strong> Used to bring peers into the conversation. <em>"Sita, having managed the stock audit last term, how feasible is this timeline from your perspective?"</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Quality Audit Review Meeting",
                "marks": "Full Criteria Level 2 (L2.2)",
                "context": "Pharmaceutical Logistics Quality Assurance",
                "question": "During a stock integrity review, the depot supervisor announces: <em>'Cold-chain temperature deviations occurred four times during transit last month.'</em> Formulate three progressive questions to interrogate this issue thoroughly.",
                "steps": [
                    ("Step 1", "Clarifying Question (Facts & Parameters)", "'Which delivery routes and refrigerated vehicles were involved in these four temperature breaches?'", "Pinpoints specific operational data"),
                    ("Step 2", "Probing Question (Root Cause Analysis)", "'What initial findings did the vehicle telemetry show regarding compressor performance or driver door opening durations?'", "Explores deeper causal evidence"),
                    ("Step 3", "Action-Oriented Collaborative Question (Future Prevention)", "'How quickly can maintenance inspect the telemetry sensors, and what backup storage protocols are in place for tomorrow's deliveries?'", "Drives toward concrete preventive solutions")
                ],
                "final_answer": "Three sequential questions moving systematically from factual identification to root-cause probing and preventive operational action.",
                "tutor_tip": "In the Level 2 SLC discussion, asking intelligent probing questions is one of the quickest ways to secure top band marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Leading or Aggressive Questions",
                "desc": "Questions like 'Don't you think that is a terrible idea?' sound confrontational and shut down collaborative discussion.",
                "fix": "Rephrase neutrally: 'What potential drawbacks might we encounter if we take that approach?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "A colleague proposes moving all staff appraisals from annual meetings to monthly 15-minute informal check-ins. Draft two open probing questions to explore the practical feasibility of this proposal.",
                "solution_steps": "1. Time management probe: 'How will line managers find time to schedule twelve monthly check-ins per staff member alongside daily operational duties?'<br>2. Documentation probe: 'What method will we use to record measurable progression goals without creating excessive admin paperwork?'",
                "correct_answer": "Two open probing questions targeting workload feasibility and documentation rigor.",
                "tutor_tip": "Start questions with 'How will...' or 'What method...' to ensure detailed answers."
            }
        ]
    },
    {
        "filename": "slc-responding.html",
        "clean_topic": "Responding to Questions & Feedback",
        "intro_lead": "Formulate composed, structured, and evidenced responses when answering questions from assessors, handling challenging inquiries, and addressing counter-arguments.",
        "next_file": "slc-contributing.html",
        "next_name": "Contributing to Group Discussions",
        "spec_points": [
            ("L1.4 / L2.3", "Respond to questions and feedback clearly, giving detailed explanations."),
            ("L2.5", "Follow and analyse lines of argument, using speech to clarify and develop points.")
        ],
        "golden_rules": [
            {
                "icon": "fa-shield-halved",
                "title": "Golden Rule 1: Use the PREP Spoken Response Formula",
                "desc": "Structure answers instantly under pressure: Point (direct answer), Reason (why), Example (real-world vocational case), Point (reaffirm conclusion).",
                "badge": "Point → Reason → Example → Point (PREP)"
            },
            {
                "icon": "fa-handshake",
                "title": "Golden Rule 2: Validate Before Rebutting",
                "desc": "When someone challenges your idea, never react defensively. Acknowledge their concern first ('That is an understandable concern...'), then pivot with evidence ('...however, data shows...').",
                "badge": "Acknowledge → Validate → Pivot with Evidence"
            }
        ],
        "skills": [
            {
                "title": "Handling Difficult or Unexpected Questions",
                "summary": "Three professional strategies when asked challenging questions during presentations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Buy Thinking Time with a Professional Acknowledgment:</strong> <em>"Thank you, that raises a crucial operational aspect regarding budget allocation."</em> This gives you 3–5 seconds to organize your response.</li>
                    <li><strong>Deconstruct Complex Multi-Part Questions:</strong> <em>"There are two key elements to your question: first the staffing impact, and second the timeline. Addressing staffing first..."</em></li>
                    <li><strong>Handling the Unknown with Integrity:</strong> If you don't know the exact figure, say: <em>"I do not have the exact Q3 percentage to hand, but our interim report indicated a 15% reduction. I will verify that figure and email it after this meeting."</em></li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Defending a Presentation on Digital Patient Records",
                "marks": "Full Criteria Level 2 (L2.3, L2.5)",
                "context": "Healthcare Informatics Implementation",
                "question": "Following your 4-minute presentation advocating for electronic tablets on hospital rounds, an assessor asks:<br><em>'Senior ward staff are already overwhelmed. Won't introducing new software simply increase their stress and cause charting errors?'</em><br>Deliver a model PREP response.",
                "steps": [
                    ("Step 1", "Point (Direct Answer)", "'While any system change carries an initial learning curve, digital records will actually reduce overall workload once implemented.'", "Clear direct thesis"),
                    ("Step 2", "Reason (Logical Explanation)", "'Because automated drop-down menus and voice-to-text eliminate repetitive paper charting, saving an average of 45 minutes per shift.'", "Provides compelling functional rationale"),
                    ("Step 3", "Example (Vocational Evidence)", "'For instance, during the trial in Ward 6, dedicated super-user floor support ensured charting errors dropped by 28% within the first fortnight.'", "Backs claim with measurable case evidence"),
                    ("Step 4", "Point (Reaffirmed Conclusion)", "'Therefore, with proper hands-on mentoring, the system relieves clinical pressure rather than adding to it.'", "Strong, reassuring wrap-up")
                ],
                "final_answer": "Structured PREP response addresses assessor concern directly, explains reasoning, cites trial data, and reaffirms the proposal.",
                "tutor_tip": "Notice how the candidate did not deny the colleague's premise ('There is an initial learning curve') before pivoting with facts."
            }
        ],
        "examiner_traps": [
            {
                "title": "The Defensive or Dismissive Reaction",
                "desc": "Saying 'No, you're wrong' or rolling eyes immediately loses marks for professional conduct and communication.",
                "fix": "Always treat challenges as valuable opportunities to elaborate on your reasoning."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "During a team discussion on installing recycling stations in a warehouse depot, a colleague remarks: <em>'No one will bother sorting rubbish; they will just throw everything into the nearest bin.'</em> Draft a 50-word response using the PREP method.",
                "solution_steps": "1. Point & Reason: 'Compliance is indeed a valid concern if bins are poorly labeled.'<br>2. Example: 'However, at the Leeds depot, clear color-coded pictorial signage increased sorting accuracy to 85%.'<br>3. Summary: 'With clear visual aids and staff briefings, our team will adapt quickly.'",
                "correct_answer": "Validates concern, provides counter-example from another site, and concludes constructively.",
                "tutor_tip": "Using peer depot comparisons demonstrates realistic vocational problem-solving."
            }
        ]
    },
    {
        "filename": "slc-contributing.html",
        "clean_topic": "Contributing to Group Discussions",
        "intro_lead": "Learn turn-taking conventions, diplomatic disagreement techniques, and group facilitation strategies to guide collaborative meetings toward actionable consensus.",
        "next_file": "slc-line-of-argument-and-narratives.html",
        "next_name": "Line of Argument & Structured Presentations",
        "spec_points": [
            ("L1.5 / L2.7", "Respect the turn-taking rights of others during discussions, using appropriate conventions for turn-taking."),
            ("L2.4", "Express opinions and arguments and support them with relevant and persuasive evidence."),
            ("L2.5", "Follow and analyse lines of argument, using speech to clarify and develop points.")
        ],
        "golden_rules": [
            {
                "icon": "fa-users",
                "title": "Golden Rule 1: Master the Three Core Discussion Roles",
                "desc": "To achieve top marks, demonstrate all three roles across the 15-minute discussion: The Facilitator (keeps time, invites peers), The Builder (adds evidence to others' ideas), and The Synthesizer (summarizes agreement).",
                "badge": "Facilitator • Builder • Synthesizer"
            },
            {
                "icon": "fa-bridge",
                "title": "Golden Rule 2: Build Verbal Bridges Before Speaking",
                "desc": "Never start speaking as if no one else has spoken. Always link your utterance to the preceding remark: 'Building on what Amara said...', 'While I see Tom's concern...'",
                "badge": "Linguistic Bridge: Name + Preceding Idea + Your Addition"
            }
        ],
        "skills": [
            {
                "title": "Turn-Taking & Discussion Facilitation Phrases",
                "summary": "High-scoring functional expressions to navigate group dynamics gracefully.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Purpose</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Standard English Phrasing</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Inviting a Quiet Peer</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Marcus, you work closely with night transport — what are your thoughts on this handover schedule?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Diplomatic Disagreement</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I appreciate that perspective, but have we taken into account the staffing constraints during peak holiday periods?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Refocusing an Off-Topic Group</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Those are interesting points, but conscious of our 15-minute timeframe, should we return to deciding the main training date?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Summarizing Consensus</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"It seems we all agree that digital check-ins are beneficial, provided we offer a two-week shadowing period first."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Waste Reduction Committee Discussion",
                "marks": "Full Criteria Level 2 (L2.4, L2.7)",
                "context": "NHS Sustainability Working Group",
                "question": "Four candidates are discussing how to reduce single-use plastic cups across hospital wards. The conversation has stalled after two members disagreed over hot drink spill risks. Intervene to resolve the impasse and advance the agenda.",
                "steps": [
                    ("Step 1", "Synthesize the competing concerns", "'I think both points are crucial: Liam is right that patient safety and scald prevention come first, while Sophie has shown our current plastic waste exceeds 5,000 cups monthly.'", "Validates both sides without taking a polarized stance"),
                    ("Step 2", "Propose a compromise solution", "'Could we pilot silicone-sleeved reusable mugs with secure lids in staff breakrooms first, where spill risks are minimal, before touching clinical areas?'", "Introduces feasible, phased compromise"),
                    ("Step 3", "Invite consensus and assign action", "'If we agree on that compromise, should we ask facilities to calculate the procurement cost for 100 sample mugs by Friday?'", "Guides group to concrete resolution and next step")
                ],
                "final_answer": "Candidate demonstrates expert facilitation: validates conflicting viewpoints, introduces an actionable compromise, and steers group to consensus.",
                "tutor_tip": "Assessor witness sheets contain specific tick-boxes for 'helps move discussion forward' and 'synthesizes viewpoints'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Interrupting or Talking Over Peers",
                "desc": "Cutting across a speaker while they are developing a thought directly violates L2.7 and will result in a resit.",
                "fix": "Wait until the speaker finishes their sentence or pauses before indicating verbally or with a slight hand gesture that you wish to contribute."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "Two colleagues in your SLC group have spent three minutes debating the brand of coffee machine to buy for the staffroom, ignoring the main topic (arranging weekend cover). Write a 30-word diplomatic intervention to steer the group back to the core task.",
                "solution_steps": "Intervention: 'While staffroom amenities are certainly important, we have only five minutes remaining to finalize the weekend emergency cover rota. Could we agree on the staffing numbers first?'",
                "correct_answer": "Polite, time-conscious, and refocuses the meeting on the primary objective.",
                "tutor_tip": "Citing the remaining time ('we have five minutes remaining') is the most professional way to refocus a drifting meeting."
            }
        ]
    }
]

print(f"SLC topics batch 1 defined: {len(SLC_TOPICS)} topics.")
