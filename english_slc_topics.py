#!/usr/bin/env python3
"""
English Speaking, Listening and Communicating (SLC) Topics (12 Topics)
Master Functional Skills Curriculum Suite — Deep PFS-Beating Edition
Every topic features:
- 3 Core Skills with rich HTML tables, before/after spoken upgrades, and L1 vs L2 rules
- 2 Step-by-Step Worked Exam Models (Level 1 & Level 2)
- 2 Critical Examiner Traps
- 3 Scenario/Transcript-Rich Exam Practice Questions with complete model spoken answers
"""

SLC_TOPICS = [
    # 1. Key Speaking, Listening & Communicating Skills
    {
        "filename": "slc-key-slc-skills.html",
        "clean_topic": "Key Speaking, Listening & Communicating Skills",
        "intro_lead": "Master the core assessment standards, active listening techniques, P-E-E-R spoken structure, and verbal articulation strategies required to achieve a first-time Pass in Pearson Edexcel Level 1 and Level 2 Functional Skills English.",
        "next_file": "slc-communicating.html",
        "next_name": "Communicating Clearly & Purposefully",
        "spec_points": [
            ("L1.1 / L2.1", "Identify relevant information and lines of argument in spoken explanations and presentations."),
            ("L1.2 / L2.2", "Make requests and ask detailed probing questions using appropriate register and language."),
            ("L1.3 / L2.3", "Communicate information, ideas, and opinions clearly and effectively, providing further elaboration."),
            ("L1.5 / L2.7", "Respect the turn-taking rights of others during discussions, using appropriate spoken conventions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-ear-listen",
                "title": "Golden Rule 1: Active Listening Constitutes Half Your Grade",
                "desc": "Assessors grade you not just when you speak, but on how effectively you listen. Nodding, taking brief keyword notes, referencing a peer's point by name, and asking clarifying questions prove observable active engagement.",
                "badge": "Examiner Focus: Do you build on what others say, or merely wait for your turn to talk?"
            },
            {
                "icon": "fa-diagram-project",
                "title": "Golden Rule 2: Use the P-E-E-R Spoken Structure in Every Contribution",
                "desc": "Whenever contributing to a group discussion, state your Point, provide Evidence/Example, Explain the vocational impact, and Redirect to the team ('Point → Evidence → Explanation → Redirect').",
                "badge": "Structure: Point → Evidence → Explanation → Redirect Question"
            }
        ],
        "skills": [
            {
                "title": "The Two Compulsory SLC Exam Components (Level 1 vs Level 2)",
                "summary": "Understanding the exact format, duration, and assessor requirements of the Pearson Edexcel Speaking and Listening assessment.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Assessment Component</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Level 1 Format</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Level 2 Format</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Task 1: Formal Presentation / Talk</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>3–4 minutes</strong> short talk/explanation on a familiar topic + audience Q&amp;A.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>4–5 minutes</strong> extended formal presentation on a researched topic + challenging Q&amp;A.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Task 2: Formal Group Discussion</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>10 minutes</strong> formal discussion (3–5 peers) reaching shared agreement.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>12–15 minutes</strong> unscripted group discussion evaluating complex options and reaching consensus.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Active Listening vs Passive Hearing on the Witness Sheet",
                "summary": "How to demonstrate observable listening behaviours that assessors can tick off on camera.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Verbal Signposts of Listening:</strong> Explicitly name the previous speaker: <em>"Following on from Marcus's point regarding staffing levels..."</em> or <em>"To add to what Priya mentioned about infection control..."</em></li>
                    <li><strong>Non-Verbal Attentiveness:</strong> Maintain steady eye contact with whoever is speaking, orient your posture toward them, and jot down 2–3 keyword notes on your pad.</li>
                    <li><strong>Clarification Prompts:</strong> Ask targeted follow-up questions: <em>"Could you explain how that change would affect the weekend shift handover?"</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Before & After: Upgrading One-Word Answers into Full P-E-E-R Contributions",
                "summary": "See why short conversational replies fail while structured P-E-E-R contributions pass effortlessly.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Weak Contribution (Fails Elaboration &amp; Evidence Criteria):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"Yeah, I agree with Sarah. I think having a staff gym is a really good idea and everyone would like it."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Strong P-E-E-R Contribution (Passes L2.3, L2.4, and L2.7):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"Building on Sarah's suggestion, converting the unused basement room into a staff fitness area would significantly boost employee wellbeing. In last month's staff survey, 65% of warehouse operatives cited back strain as their primary health concern. Providing stretching mats and resistance machines on site would reduce sickness absence. David, from a budget perspective, could our wellbeing fund cover the initial equipment?"</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Team Discussion on Organising a Staff Charity Fundraiser",
                "marks": "Level 1 Pass Benchmark (L1.2, L1.3, L1.5)",
                "context": "Retail Store Team Meeting",
                "question": "During a Level 1 group discussion about raising £500 for a local food bank, a colleague says:<br><em>'We could do a sponsored silence in the shop on Saturday.'</em><br>Deliver a polite spoken response that explains why that idea is impractical for retail staff, suggests a better alternative, and asks a peer for their view.",
                "steps": [
                    ("Step 1", "Acknowledge the colleague politely", "'That is a creative idea, Chloe, and it shows great enthusiasm for the food bank appeal.'", "Respectful Turn-Taking (L1.5)"),
                    ("Step 2", "Explain the practical issue and offer an alternative", "'However, because Saturday is our busiest trading day, staff need to speak with customers at the tills. Instead, we could hold a charity bake sale and raffle at the store entrance.'", "Clear Point & Explanation (L1.3)"),
                    ("Step 3", "Redirect with an open question", "'Ben, what prizes do you think we could donate for a Saturday customer raffle?'", "Asking Questions (L1.2)")
                ],
                "final_answer": "'That is a creative idea, Chloe. However, because Saturday is our busiest trading day, till staff must be able to speak clearly with customers. Instead, we could host a charity bake sale and raffle by the main entrance, which raised £380 last December. Ben, what prizes do you think our store could donate for the raffle?'",
                "tutor_tip": "Notice how the candidate never says 'That is a silly idea'—they validate the speaker first, explain the operational constraint, and propose a practical alternative."
            },
            {
                "title": "Model 2 (Level 2): Multidisciplinary Ward Handover Meeting",
                "marks": "Level 2 Pass Criteria (L2.3, L2.4, L2.7)",
                "context": "NHS Healthcare Shift Handover",
                "question": "Observe the dialogue during a morning hospital ward meeting:<br><em>Colleague A (Marcus): 'We had three fall incidents in Bay 2 last week. Call bells were ignored because the agency nurses didn't know the buzzer panel layout.'</em><br>Deliver a model response demonstrating L2.3, L2.4, and L2.7.",
                "steps": [
                    ("Step 1", "Acknowledge and validate the colleague's observation", "'Thank you for raising that, Marcus. Patient safety in Bay 2 is an urgent operational priority.'", "Active Listening & Bridge (L2.7)"),
                    ("Step 2", "Provide constructive analysis and supporting evidence", "'According to our clinical audit last month, 40% of agency staff receive less than ten minutes of ward orientation before starting their shift.'", "Supporting Evidence (L2.4)"),
                    ("Step 3", "Propose a structured vocational solution and invite feedback", "'I propose we attach a laminated colour-coded buzzer map next to every nursing terminal and include a mandatory two-minute call-bell check at handover. Elena, from an occupational therapy perspective, would that resolve the response delay?'", "Elaboration & Peer Invitation (L2.3, L2.7)")
                ],
                "final_answer": "'Thank you for raising that, Marcus; patient safety in Bay 2 is an urgent operational priority. According to our audit last month, 40% of agency staff receive less than ten minutes of ward orientation. I propose we place a laminated colour-coded buzzer guide at every nursing station and run a two-minute induction check at handover. Elena, from an occupational therapy view, would that resolve the delay?'",
                "tutor_tip": "Assessors look for candidates who synthesise points and invite quieter members in. Bridging Marcus's observation to Elena's expertise ticks three witness criteria in 25 seconds."
            }
        ],
        "examiner_traps": [
            {
                "title": "The Silent Participant Trap",
                "desc": "Some candidates believe that sitting quietly and nodding is enough to pass the listening component. Assessors cannot award marks for unobservable internal listening.",
                "fix": "You must verbally reference other participants' contributions and ask at least two relevant follow-up questions during each discussion."
            },
            {
                "title": "Dominating the Airtime and Interrupting",
                "desc": "Speaking for 75% of the meeting or cutting off quieter peers causes you to fail criterion L2.7 (respecting turn-taking rights) even if your ideas are strong.",
                "fix": "Keep each speaking turn to 30–45 seconds, then deliberately hand over the floor with an open question."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "You are participating in a workplace meeting discussing whether your department should adopt a 4-day working week (four 9.5-hour shifts). A colleague argues:<br><em>'It will leave our customer service helpdesk unstaffed on Fridays.'</em><br>Write a 45-word spoken response that acknowledges their concern, introduces counter-evidence, and invites another colleague (David) to contribute.",
                "solution_steps": "1. Acknowledge: Validate the concern regarding Friday customer service coverage.<br>2. Counter-evidence: Explain how staggered Monday–Thursday and Tuesday–Friday rotas maintained 100% cover at another branch.<br>3. Redirect: Ask David how the logistics team manages rotating shifts.",
                "correct_answer": "'That is a very valid operational concern regarding Friday helpdesk coverage. However, when our Manchester branch trialled a four-day week last quarter, staggering staff across Monday-to-Thursday and Tuesday-to-Friday rotas maintained 100% telephone cover every weekday. David, how does the logistics team currently manage rotating Friday cover?'",
                "tutor_tip": "Always pair your rebuttal with a concrete example ('when our Manchester branch trialled...') and finish with a named handover question."
            },
            {
                "marks": "3 Marks",
                "question": "Upgrade this weak, 8-word spoken comment into a full Level 2 P-E-E-R contribution for a council meeting on youth crime:<br><em>'I think we should open the youth club on Friday nights.'</em>",
                "solution_steps": "1. Point: State the proposal to reopen Oakfield Youth Centre on Friday and Saturday evenings.<br>2. Evidence: Cite that local antisocial behaviour callouts peak between 19:00 and 22:00 on Fridays.<br>3. Explain & Redirect: Explain how structured sports and music workshops divert teenagers positively, and ask a peer about volunteer staffing.",
                "correct_answer": "'I strongly believe we should reopen Oakfield Youth Centre on Friday evenings between 18:00 and 21:30. Neighbourhood policing figures show that 60% of local antisocial behaviour reports occur on Friday nights when teenagers have nowhere safe to socialise. Providing structured boxing and music workshops would channel their energy positively. Samira, could local sports coaches help staff those Friday sessions?'",
                "tutor_tip": "Adding a time window ('18:00 to 21:30') and a realistic statistic ('60% of reports') transforms a basic opinion into a Level 2 argument."
            },
            {
                "marks": "4 Marks",
                "question": "During a group discussion, Participant A has spoken for two minutes non-stop while Participant C (Maya) has not spoken at all. Write the exact spoken intervention you would use to politely bring Participant A to a close and invite Maya into the discussion.",
                "solution_steps": "1. Wait for Participant A to take a breath and briefly summarise their core point so they feel heard.<br>2. Use a polite transition to shift the floor.<br>3. Invite Maya by name with an accessible open question linked to the topic.",
                "correct_answer": "'Thank you, Liam—your point about the upfront software cost is really important for our budget summary. Before we finalise that section, we haven't heard from Maya yet. Maya, from your experience on the reception desk, how easy would this booking software be for staff to use daily?'",
                "tutor_tip": "Summarizing a dominant speaker's point ('Thank you, Liam—your point about X is really important') is the most diplomatic way to close their turn without offending them."
            }
        ]
    },

    # 2. Communicating Clearly, Coherently & Purposefully
    {
        "filename": "slc-communicating.html",
        "clean_topic": "Communicating Clearly, Coherently & Purposefully",
        "intro_lead": "Develop vocal projection, pace control, tone modulation, and professional poise to communicate complex instructions and vocational data with confidence and authority.",
        "next_file": "slc-adapting.html",
        "next_name": "Adapting Talk to Audience and Situation",
        "spec_points": [
            ("L1.1 / L2.3", "Communicate information, ideas, and opinions clearly and coherently in workplace contexts."),
            ("L2.5", "Use spoken techniques such as pitch, pace, tone, and pause to clarify and develop points effectively.")
        ],
        "golden_rules": [
            {
                "icon": "fa-gauge-high",
                "title": "Golden Rule 1: Master the Power of the Controlled 2-Second Pause",
                "desc": "Rushing speech indicates nervousness and obscures technical instructions. Pause for 2 full seconds before stating major statistics or transitions; this commands authority and lets listeners process your point.",
                "badge": "Rule: 130–150 words per minute is the optimal professional speaking cadence."
            },
            {
                "icon": "fa-bullseye",
                "title": "Golden Rule 2: Apply the 4 Cs of Professional Spoken Delivery",
                "desc": "Every spoken briefing must be Clear (unambiguous words), Concise (free from rambling tangents), Coherent (logical chronological order), and Courteous (respectful, composed tone).",
                "badge": "Clear • Concise • Coherent • Courteous"
            }
        ],
        "skills": [
            {
                "title": "Four Physical Dimensions of Vocal & Non-Verbal Delivery",
                "summary": "How assessors evaluate your physical delivery during formal presentations and briefings.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px;">
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#0284c7;"><i class="fa-solid fa-volume-high"></i> Projection &amp; Clarity</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Project from the diaphragm and enunciate word endings clearly so listeners at the back hear effortlessly without you shouting.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#16a34a;"><i class="fa-solid fa-stopwatch"></i> Pacing &amp; Tempo</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Maintain a steady 140 wpm. Slow down deliberately when delivering numbers, medication dosages, or safety deadlines.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#ea580c;"><i class="fa-solid fa-wave-square"></i> Pitch &amp; Emphasis</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Avoid a flat monotone. Use downward vocal inflection at the end of statements to project confidence and certainty.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:12px;">
                      <strong style="color:#7c3aed;"><i class="fa-solid fa-person"></i> Non-Verbal Poise</strong>
                      <p style="margin-top:6px; font-size:0.92rem; color:#475569;">Keep an open chest posture, uncrossed arms, purposeful hand gestures, and shared eye contact across all group members.</p>
                    </div>
                  </div>
                </div>
                """
            },
            {
                "title": "The SBAR Framework for High-Stakes Spoken Handovers",
                "summary": "Use Situation → Background → Assessment → Recommendation to structure any workplace update in 45 seconds.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">SBAR Stage</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Purpose</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Spoken Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">S — Situation</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">State immediately what the issue is and where.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I am calling regarding a walk-in chiller failure in the main kitchen."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">B — Background</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Provide brief context (when it started, what was checked).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The temperature alarm sounded at 07:30, and the digital gauge currently reads 9°C instead of 4°C."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">A — Assessment</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">State the risk or operational impact.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We have £600 of fresh dairy and meat stock that will spoil if left above 8°C for two hours."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">R — Recommendation</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">State the exact action taken and what you need now.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We have moved all high-risk stock to Chiller 2; please dispatch an emergency refrigeration engineer before noon."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Eliminating Verbal Fillers & Crutch Words",
                "summary": "How to replace 'um', 'like', 'basically', and 'you know' with composed silence.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Filler-Heavy Delivery (Sounds Unprepared &amp; Hesitant):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"Um, basically what I wanted to say is, like, the car park is sort of dangerous at night, you know, because the lights don't really work properly."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Composed, Purposeful Delivery (Clear &amp; Authoritative):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"Our primary safety concern is the staff car park after 17:00. [2-second pause] Currently, three of the four overhead floodlights are out of order, leaving evening-shift staff walking in complete darkness."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Care Assistant Shift Handover Briefing",
                "marks": "Level 1 Clarity & Coherence Benchmark (L1.1, L1.3)",
                "context": "Residential Care Home Shift Changeover",
                "question": "Deliver a clear 45-second spoken handover informing the incoming afternoon care assistant that Resident Mrs Patel (Room 14) had a minor uninjured fall yesterday, requires a two-person walking transfer until 15:00, and has an updated chart on the tablet.",
                "steps": [
                    ("Step 1", "Identify the resident, room number, and background clearly", "'Before we start the afternoon round, please note an important update for Mrs Patel in Room 14, who had a minor uninjured slip yesterday evening.'", "Clear Context (L1.1)"),
                    ("Step 2", "State the exact mandatory safety instruction", "'Until the physiotherapist reviews her at 15:00 today, Mrs Patel requires two care assistants to support her whenever she transfers from her chair to her walking frame.'", "Unambiguous Instruction (L1.3)"),
                    ("Step 3", "Confirm documentation location", "'I have logged her morning observations on the ward tablet under Room 14. Do you have any questions before we begin?'", "Coherent Close")
                ],
                "final_answer": "'Before we start the afternoon round, please note an important update for Mrs Patel in Room 14, who had a minor uninjured slip yesterday evening. Until the physiotherapist reviews her at 15:00 today, she requires two care assistants to support her whenever she transfers to her walking frame. I have updated her mobility chart on the ward tablet.'",
                "tutor_tip": "In healthcare handovers, stating Who (Mrs Patel, Room 14), Why (minor fall yesterday), and What action (2-person assist until 15:00) in chronological order prevents errors."
            },
            {
                "title": "Model 2 (Level 2): Delivering a Health & Safety Depot Toolbox Briefing",
                "marks": "Level 2 Delivery & Vocal Technique Benchmark (L2.3, L2.5)",
                "context": "Logistics & Warehousing Operations",
                "question": "Deliver a 60-second verbal briefing to forklift operators regarding newly designated pedestrian safety walkways in Bay 3, indicating where vocal emphasis and pauses should be used.",
                "steps": [
                    ("Step 1", "Opening Hook & Clear Purpose", "'Good morning team. Please give me your full attention for sixty seconds on a critical safety update regarding Loading Bay 3.'", "Establishes Immediate Authority (L2.3)"),
                    ("Step 2", "Key Factual Directive with Vocal Stress & Pause", "'As of 06:00 today, the yellow cross-hatched lanes are strictly <strong>pedestrian-only</strong>. [Pause for 2 seconds] Forklift trucks must not cross or park on these lines under any circumstances.'", "Pace, Stress & Pause Control (L2.5)"),
                    ("Step 3", "Actionable Consequence & Sign-Off", "'Breaching this walkway zone triggers an automatic HSE incident review. Please sign the briefing register on the clipboard before collecting your vehicle keys. Thank you.'", "Concise & Purposeful Close")
                ],
                "final_answer": "'Good morning team. Please give me your full attention for sixty seconds on a critical safety update regarding Loading Bay 3. As of 06:00 today, the yellow cross-hatched lanes are strictly pedestrian-only. [2-second pause] Forklift trucks must not cross or park on these lines under any circumstances. Breaching this policy triggers an automatic HSE incident review. Please sign the briefing register before collecting your keys.'",
                "tutor_tip": "Notice how pausing for 2 seconds right after 'strictly pedestrian-only' makes the safety rule sink in immediately."
            }
        ],
        "examiner_traps": [
            {
                "title": "Verbal Tics and Crutch Words ('Um', 'Like', 'Basically', 'Sort Of')",
                "desc": "Repeating 'like' or 'basically' every five words weakens your authority and distracts the assessor from the substance of your argument.",
                "fix": "Slow your speaking pace by 15%. Whenever you need to think of your next word, close your mouth and take a calm breath instead of saying 'um'."
            },
            {
                "title": "Trailing Off at the End of Sentences",
                "desc": "Ending statements with '...so yeah, that's basically it' or letting your voice drop to a mumble makes your conclusion sound weak.",
                "fix": "Finish every speaking turn with a complete, crisp sentence or a direct handover question."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Rewrite this rambling, filler-heavy spoken announcement so it is clear, concise, and professional for a GP surgery waiting room:<br><em>'Um, excuse me everyone, basically Dr Evans is running like half an hour late this morning because there was an emergency callout, so yeah, sorry about that, if you can't wait just tell the desk.'</em>",
                "solution_steps": "1. Remove all filler words ('Um', 'basically', 'like', 'so yeah').<br>2. Structure clearly: Polite greeting → Factual reason & 30-minute delay → Actionable option at reception.",
                "correct_answer": "'Good morning everyone, may I have your attention please. Due to an urgent medical callout, Dr Evans's morning clinic is currently running approximately thirty minutes behind schedule. We sincerely apologise for the delay; if you are unable to wait, please speak to our reception team to rebook your appointment for a convenient time.'",
                "tutor_tip": "Always state the exact delay time ('thirty minutes') and give listeners a clear next step."
            },
            {
                "marks": "3 Marks",
                "question": "Use the <strong>4-step SBAR framework</strong> (Situation, Background, Assessment, Recommendation) to write a 50-word spoken telephone report to your IT Helpdesk explaining that the main reception card-payment terminal has frozen.",
                "solution_steps": "1. Situation: Identify yourself and state that the main reception PDQ card machine has frozen.<br>2. Background: Explain that it displayed 'Error 404' at 09:15 and restarting the router did not fix it.<br>3. Assessment: Customers cannot pay by card and queues are building.<br>4. Recommendation: Request an urgent replacement handset from IT stores.",
                "correct_answer": "'Hello IT Support, this is Sam at Main Reception. Our primary card-payment terminal has frozen completely. It displayed Error 404 at 09:15 this morning, and rebooting the terminal has not resolved the fault. Consequently, we cannot process customer card payments and a queue is building. Could a technician bring out the spare replacement terminal within the next fifteen minutes please?'",
                "tutor_tip": "SBAR works in every industry—it gives your listener all the facts they need in four logical sentences."
            },
            {
                "marks": "3 Marks",
                "question": "Look at this sentence from a formal presentation:<br><em>'Last year, avoidable packaging waste cost our distribution centre forty-two thousand pounds—enough to fund two full-time apprenticeships.'</em><br>Explain <strong>two specific vocal techniques</strong> (pace, pause, volume, or emphasis) you would use when speaking this sentence aloud to maximise its impact on the audience.",
                "solution_steps": "1. Technique 1 (Vocal Emphasis & Slowed Pace): Slow down and stress the words 'forty-two thousand pounds' to highlight the scale of the financial loss.<br>2. Technique 2 (Deliberate Pause): Pause for two full seconds at the dash before delivering 'enough to fund two full-time apprenticeships'.",
                "correct_answer": "1. Slow the speaking pace and place strong vocal stress on each word of 'forty-two thousand pounds' so the financial figure stands out clearly.<br>2. Insert a deliberate two-second pause at the dash before delivering the comparison ('enough to fund two full-time apprenticeships') to let the audience absorb the human impact.",
                "tutor_tip": "Numbers and statistics always land harder when you slow down and pause right after stating them."
            }
        ]
    },

    # 3. Adapting Talk to Audience and Situation
    {
        "filename": "slc-adapting.html",
        "clean_topic": "Adapting Talk to Audience and Situation",
        "intro_lead": "Calibrate your spoken vocabulary, tone, register, and level of technical detail when moving between team handovers, anxious patients or customers, and formal executive panels.",
        "next_file": "slc-asking.html",
        "next_name": "Asking Questions Effectively",
        "spec_points": [
            ("L1.6 / L2.6", "Use appropriate language and register suitable for purpose, subject, and audience in formal and informal situations."),
            ("L2.3", "Adapt verbal communication effectively to suit varying levels of technical understanding and emotional need.")
        ],
        "golden_rules": [
            {
                "icon": "fa-sliders",
                "title": "Golden Rule 1: Calibrate Formality Along the Workplace Register Continuum",
                "desc": "Match your spoken vocabulary to the room. Casual street slang ('mate', 'wrecked', 'innit') is unacceptable in an assessed SLC task, while cold technical jargon alienates worried customers or patients.",
                "badge": "Supportive & Accessible (Public/Patients) ↔ Collaborative & Clear (Peers) ↔ Formal & Evidenced (Boardroom)"
            },
            {
                "icon": "fa-language",
                "title": "Golden Rule 2: Translate Specialist Jargon Immediately into Plain English",
                "desc": "When speaking to non-specialists (patients, parents, customers, or new apprentices), always pair any technical term or acronym with a clear plain-English explanation.",
                "badge": "Formula: Technical Term + 'which means...' (e.g. 'hypertension—which means high blood pressure')"
            }
        ],
        "skills": [
            {
                "title": "The Register Adaptation Matrix Across 3 Workplace Settings",
                "summary": "Compare how the exact same operational issue is communicated to three different audiences.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Situation</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Inappropriate / Too Casual</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Adapted Functional English</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Requesting Leave (To Manager)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I need Friday off cos my mates are going away."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I would like to request annual leave for this Friday; I have already arranged shift cover with Michael."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Explaining Delay (To Customer)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Our IT server is totally wrecked so we can't check your order."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We are experiencing a temporary system update this morning; I will take your telephone number and call you back by 11:00 with your tracking details."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Challenging a Proposal (In Committee)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"That idea makes zero sense and costs way too much."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"While I appreciate the rationale behind the proposal, have we evaluated the impact on our quarterly training budget?"</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "De-Escalating Frustrated Customers or Anxious Patients (The LAST Method)",
                "summary": "How to adapt your tone when speaking to someone who is upset or stressed.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>L — Listen Without Interrupting:</strong> Let the client finish explaining their problem while maintaining calm, empathetic eye contact.</li>
                    <li><strong>A — Apologise &amp; Acknowledge Empathy:</strong> <em>"I completely understand how frustrating it is to wait in all morning for a missed delivery, and I sincerely apologise."</em></li>
                    <li><strong>S — Solve with a Concrete Action Plan:</strong> State exactly what you will do right now and give a realistic timeframe.</li>
                    <li><strong>T — Thank &amp; Check Satisfaction:</strong> <em>"Thank you for your patience, Mr Davies—does that Saturday morning slot work for you?"</em></li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Specialist Technical Register vs Public Plain-English Register",
                "summary": "How to switch smoothly between professional peers and members of the public.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Speaking to a Mechanic Colleague (Technical Peer):</strong> <em>"The diagnostic scan flagged a faulty DPF pressure sensor and worn front brake callipers."</em></li>
                    <li><strong>Speaking to the Car Owner (Public Customer):</strong> <em>"Our diagnostic check showed a faulty exhaust filter sensor and worn front brake parts. Replacing both today will cost £185 and ensure your car passes its MOT safely."</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Explaining a Vehicle Repair Delay to a Customer",
                "marks": "Level 1 Audience Adaptation Benchmark (L1.6)",
                "context": "Automotive Service Reception",
                "question": "A mechanic tells you: <em>'Tell Mr Robinson his van won't be ready today because the supplier sent the wrong alternator bracket.'</em><br>Deliver a polite, 3-sentence spoken message to Mr Robinson that apologises, explains the delay clearly without blaming people, and confirms tomorrow's collection time.",
                "steps": [
                    ("Step 1", "Courteous greeting & sincere apology", "'Good afternoon Mr Robinson, I am calling from Metro Garage with an update on your transit van, and I want to apologise for a slight delay.'", "Polite Customer Register (L1.6)"),
                    ("Step 2", "Clear explanation & new completion time", "'Unfortunately, the replacement alternator bracket delivered this morning did not match your engine model, so we have ordered an express replacement arriving at 08:30 tomorrow.'", "Clear Factual Explanation"),
                    ("Step 3", "Reassurance & customer check", "'Our senior technician will fit and road-test it first thing, meaning your van will be ready for collection by 11:00 tomorrow morning—does that arrangement work for you?'", "Solution-Focused Close")
                ],
                "final_answer": "'Good afternoon Mr Robinson, I am calling from Metro Garage with an update on your van, and I sincerely apologise for a slight delay. Unfortunately, the alternator bracket delivered this morning did not match your engine model, so we have arranged an express replacement arriving at 08:30 tomorrow. Our technician will fit and test it immediately, so your van will be ready for collection by 11:00 tomorrow morning.'",
                "tutor_tip": "Always pair bad news (a delay) with a definite solution and an exact updated time ('ready by 11:00 tomorrow')."
            },
            {
                "title": "Model 2 (Level 2): Communicating a Discharge Plan to an Elderly Patient and Family",
                "marks": "Level 2 Register & Sensitivity Benchmark (L2.3, L2.6)",
                "context": "Health and Social Care Discharge Consultation",
                "question": "A clinical handover note reads: <em>'Patient ambulates with Zimmer frame. Requires BID domiciliary care package post-discharge and PRN analgesia.'</em><br>How should the care coordinator communicate this verbally to the elderly patient (Mrs Davies) and her daughter (Claire)?",
                "steps": [
                    ("Step 1", "Establish warm, respectful rapport with both listeners", "'Good afternoon Mrs Davies, hello Claire. I would like to talk through the support package we have arranged so you feel safe and comfortable returning home tomorrow.'", "Empathetic Tone (L2.6)"),
                    ("Step 2", "Translate clinical terminology into accessible plain English", "'To help you walk steadily around your bungalow, our physiotherapist has provided this lightweight walking frame. We have also arranged for friendly home-care assistants to visit twice a day—once at 08:30 to help you get washed and dressed, and once at 19:00.'", "Translates 'ambulates' & 'BID domiciliary' (L2.3)"),
                    ("Step 3", "Explain medication clearly and invite questions", "'Finally, the pharmacy has packed your pain-relief tablets, which you can take whenever your knee feels sore, up to four times a day. What questions do you both have about the visiting times?'", "Translates 'PRN analgesia' & Checks Understanding")
                ],
                "final_answer": "'Good afternoon Mrs Davies, hello Claire. I would like to run through the support we have arranged for your return home tomorrow. To help you walk steadily indoors, you will have this lightweight walking frame. We have also arranged for home carers to visit twice a day—at 08:30 and 19:00—and packed pain-relief tablets that you can take whenever your knee aches. What questions do you both have about the routine?'",
                "tutor_tip": "Functional Skills examiners award high marks when candidates replace clinical acronyms ('BID domiciliary', 'PRN analgesia') with warm, transparent explanations."
            }
        ],
        "examiner_traps": [
            {
                "title": "Using Unexplained Acronyms or Jargon with Lay Audiences",
                "desc": "Throwing around terms like 'SOP', 'KPI', 'DSE', or 'dyspnoea' when speaking to customers or patients creates confusion and fails audience adaptation criteria.",
                "fix": "Either use plain English from the start or immediately define the term."
            },
            {
                "title": "Over-Formality That Sounds Robotic or Patronising",
                "desc": "Reciting memorised dictionary words that you wouldn't naturally use makes your delivery sound stiff and insincere.",
                "fix": "Aim for natural, composed professional Standard English—clear, courteous, and direct."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Rewrite this casual spoken remark so it is appropriate for a formal presentation to your College Board of Governors:<br><em>'Loads of students are quitting the evening maths class cos the buses stop running at 8pm and they can't get home.'</em>",
                "solution_steps": "1. Replace informal slang ('Loads of', 'quitting', 'cos') with formal educational register.<br>2. State the transport issue clearly and professionally.",
                "correct_answer": "'A significant number of adult learners have withdrawn from the evening Mathematics programme because local public bus services cease operating at 20:00, leaving students without reliable transport home.'",
                "tutor_tip": "Replacing 'Loads of students are quitting cos...' with 'A significant number of adult learners have withdrawn because...' instantly elevates your spoken register."
            },
            {
                "marks": "3 Marks",
                "question": "An IT technician needs to tell a non-technical receptionist: <em>'Don't click links in phishing emails because malware will encrypt the local LAN server.'</em><br>Rewrite this spoken advice in 2–3 clear, jargon-free sentences that explain what to look out for and why it matters.",
                "solution_steps": "1. Explain 'phishing emails' in plain terms (suspicious emails pretending to be from banks or couriers).<br>2. Explain 'malware encrypting the LAN server' in plain terms (harmful software locking all our patient appointment files).",
                "correct_answer": "'Please be extra cautious if you receive unexpected emails asking you to click a link or enter your password, even if they look official. Clicking a fake link can install harmful software that locks everyone out of our shared patient booking computer system. If an email ever looks unusual, please forward it straight to the IT desk before clicking anything.'",
                "tutor_tip": "Explaining the practical consequence ('locks everyone out of our booking system') helps non-technical colleagues understand why the rule matters."
            },
            {
                "marks": "4 Marks",
                "question": "A parent arrives at a nursery reception desk upset because their child's favourite jacket has gone missing from the cloakroom. Using the <strong>LAST method</strong> (Listen/Acknowledge, Apologise, Solve, Thank/Check), write a calm, empathetic 4-sentence spoken response.",
                "solution_steps": "1. Acknowledge & Apologise: Validate the parent's frustration warmly.<br>2. Solve (Immediate Action): Offer to check the classroom lost-property box and garden area immediately.<br>3. Solve (Follow-up): Promise to put a notice on the parents' app if not found within 10 minutes.<br>4. Check satisfaction.",
                "correct_answer": "'I completely understand how upsetting it is to find Leo's jacket missing at pickup time, Mrs Green, and I am really sorry for the worry this has caused. I am going to check the Blue Room lost-property basket and the outdoor play area with his key worker right now. If we do not locate it within the next five minutes, I will send an urgent photo alert to all parents on the nursery app so anyone who picked it up by mistake can return it tomorrow morning. Does that sound helpful while you wait in reception?'",
                "tutor_tip": "Staying calm, using the child's name, and taking immediate practical action de-escalates upset parents or customers every time."
            }
        ]
    },

    # 4. Asking Questions Effectively
    {
        "filename": "slc-asking.html",
        "clean_topic": "Asking Questions Effectively",
        "intro_lead": "Formulate open, probing, clarifying, and collaborative questions to extract vital operational facts, stimulate group discussion, and fulfil mandatory Q&A assessment criteria.",
        "next_file": "slc-responding.html",
        "next_name": "Responding to Questions & Feedback",
        "spec_points": [
            ("L1.2 / L2.2", "Make requests and ask detailed questions using appropriate language in a wide range of contexts."),
            ("L2.1 / L2.7", "Use strategic questioning to clarify lines of argument, probe evidence, and draw peers into group discussions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-circle-question",
                "title": "Golden Rule 1: Ask Open Questions ('How', 'Why', 'What Impact') to Unlock Detail",
                "desc": "Closed questions ('Do you agree?', 'Is it expensive?') produce one-word 'Yes/No' answers that kill discussion momentum. Start your questions with 'How will...', 'What evidence...', or 'In what ways could...' to prompt rich answers.",
                "badge": "Closed: 'Will this save money?' (1 word) → Open: 'How much will this save over 12 months?' (Detailed)"
            },
            {
                "icon": "fa-filter",
                "title": "Golden Rule 2: Ask At Least Two Probing Questions During Peer Presentations",
                "desc": "In Task 1 (Presentations), you are assessed not only on your own talk, but also as an audience member asking questions after your peers' talks! Prepare two open probing questions for every speaker.",
                "badge": "Audience Rule: Listen actively → Note 2 gaps or impacts → Ask 1 Clarifying + 1 Probing Question"
            }
        ],
        "skills": [
            {
                "title": "The 4-Type Questioning Taxonomy for Functional Skills Exams",
                "summary": "Deploy all four question types across your group discussion and presentation Q&A.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Question Type</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Functional Purpose</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">High-Scoring Exam Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Open Exploratory</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Opens up a new topic or invites broad views.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"What are the main challenges our team faces during the Friday evening rush?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Clarifying Fact-Check</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Pins down exact numbers, dates, or definitions.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Could you clarify whether that £1,500 quote includes annual maintenance?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Probing / Analytical</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Tests feasibility, risks, or deeper evidence (Level 2).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"How will we maintain customer service standards if we reduce reception staffing by 20%?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. Collaborative / Inviting</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Brings a quiet peer into the conversation by name.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Priya, having worked on the night shift, how realistic does this timetable seem to you?"</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Converting Weak Closed Questions into High-Scoring Open Probes",
                "summary": "Practise upgrading single-word Yes/No questions into analytical Level 2 questions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Closed:</strong> <em>"Is the new software hard to learn?"</em><br>
                    <strong>Open Upgrade:</strong> <em>"What training support will staff need to master the new software confidently?"</em></li>
                    <li><strong>Closed:</strong> <em>"Did the trial work well?"</em><br>
                    <strong>Open Upgrade:</strong> <em>"What measurable improvements did you see during the four-week pilot scheme?"</em></li>
                    <li><strong>Closed:</strong> <em>"Do you think we should ban cars from the town centre?"</em><br>
                    <strong>Open Upgrade:</strong> <em>"How might pedestrianising the High Street affect elderly residents and disabled badge holders?"</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Polite Indirect Requests & Diplomatic Question Framing",
                "summary": "How to ask challenging questions without sounding hostile or interrogative.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Instead of firing blunt questions (<em>"Why didn't you check the cost?"</em>), soften and elevate your question using a polite lead-in:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    • <em>"Thank you for a very clear presentation, Alex. <strong>Could you expand a little on</strong> how the scheme will be funded in Year 2?"</em><br>
                    • <em>"That is an interesting proposal. <strong>Have we considered what safeguards</strong> would be needed if a supplier delivery is delayed?"</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Asking Questions After a Peer's Presentation on Cycling to Work",
                "marks": "Level 1 Questioning Benchmark (L1.2)",
                "context": "Post-Presentation Q&A Session",
                "question": "A fellow candidate has just finished a 3-minute talk encouraging college students to cycle to campus instead of taking the bus. Formulate <strong>one clarifying question</strong> and <strong>one open question</strong> to ask them during the Q&A.",
                "steps": [
                    ("Step 1", "Acknowledge the speaker's talk politely", "'Thank you for that interesting talk, Sam.'", "Courteous Framing (L1.2)"),
                    ("Step 2", "Ask a specific Clarifying Question about campus facilities", "'Could you clarify where the locked bike sheds are located on the main campus and whether students need to pay for a key fob?'", "Extracts Practical Detail"),
                    ("Step 3", "Ask an Open Question about wet weather / winter safety", "'What advice would you give to beginners who feel nervous about cycling in heavy rain or dark winter evenings?'", "Stimulates Detailed Response")
                ],
                "final_answer": "Question 1 (Clarifying): 'Thank you for your talk, Sam. Could you clarify where the secure cycle shelters are located on campus and how students apply for a key fob?'<br>Question 2 (Open): 'What practical advice would you give to students who feel nervous about cycling on busy roads during dark winter afternoons?'",
                "tutor_tip": "Asking a question that starts with 'What practical advice would you give...' gives the presenter a great chance to elaborate, earning marks for both of you!"
            },
            {
                "title": "Model 2 (Level 2): Quality Assurance Audit Inquiry Sequence",
                "marks": "Level 2 Strategic Questioning Benchmark (L2.1, L2.2)",
                "context": "Pharmaceutical Logistics Quality Assurance Meeting",
                "question": "During a stock integrity meeting, the depot supervisor announces: <em>'Cold-chain temperature deviations occurred four times in our refrigerated vans last month.'</em><br>Formulate three progressive questions (Clarifying → Probing Root Cause → Collaborative Action) to interrogate this issue thoroughly.",
                "steps": [
                    ("Step 1", "Clarifying Question (Pinpointing Scope & Data)", "'Could you specify which delivery routes and which refrigerated vehicles accounted for those four temperature breaches?'", "Extracts Exact Facts (L2.1)"),
                    ("Step 2", "Probing Question (Root-Cause Analysis)", "'What did the vehicle data-loggers reveal about whether the breaches were caused by faulty chiller compressors or doors being left open during multi-drop unloading?'", "Probes Underlying Cause (L2.2)"),
                    ("Step 3", "Action-Oriented Collaborative Question (Prevention)", "'While engineering inspects those vans, how can we adjust our loading procedure tomorrow morning to guarantee zero stock spoilage?'", "Drives Collaborative Solution")
                ],
                "final_answer": "1. Clarifying: 'Could you specify which vehicles and routes experienced those four temperature deviations?'<br>2. Probing: 'What did the telemetry logs show regarding whether the cause was compressor failure or prolonged door openings during deliveries?'<br>3. Action: 'How can we modify our loading protocol tomorrow morning to protect temperature-sensitive stock while those units are inspected?'",
                "tutor_tip": "Moving systematically from What happened → Why did it happen → How do we fix it tomorrow is the hallmark of Level 2 questioning."
            }
        ],
        "examiner_traps": [
            {
                "title": "Asking Hostile or Loaded Questions ('Don't You Think That's Stupid?')",
                "desc": "Questions framed as attacks ('Why would anyone waste money on that?') make speakers defensive and fail criteria for collaborative professional register.",
                "fix": "Frame challenging questions neutrally around risk and feasibility: 'How might we overcome the upfront cost of that option?'"
            },
            {
                "title": "Sitting Silently During Other Candidates' Q&A Sessions",
                "desc": "To pass Criterion L1.2 / L2.2, the assessor must record evidence of you asking detailed questions. If you never raise your hand in Q&A, you risk failing that criterion.",
                "fix": "Make it a rule to ask at least one well-formed question after EVERY peer presentation in your group."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Convert both of these closed Yes/No questions into detailed <strong>open probing questions</strong>:<br>1. <em>'Do you think moving the staffroom upstairs is a good idea?'</em><br>2. <em>'Will the new computer system save time?'</em>",
                "solution_steps": "1. Rewrite Question 1 starting with 'How might...' or 'What impact...' to explore accessibility and break time.<br>2. Rewrite Question 2 starting with 'In what ways will...' or 'How much time...'.",
                "correct_answer": "1. 'How might relocating the staffroom to the second floor affect staff who only have a fifteen-minute break or colleagues with mobility needs?'<br>2. 'In what specific ways will the upgraded booking software reduce administrative processing times each day?'",
                "tutor_tip": "Starting questions with 'How might...' or 'In what specific ways...' makes a one-word answer impossible."
            },
            {
                "marks": "3 Marks",
                "question": "A colleague proposes: <em>'We should replace all annual staff appraisals with monthly 15-minute informal check-ins.'</em><br>Write <strong>two open probing questions</strong> to test the practical feasibility of this proposal in a busy workplace.",
                "solution_steps": "1. Probe 1 (Time/Workload): Ask how line managers will schedule 12 meetings per employee alongside daily operational duties.<br>2. Probe 2 (Record-Keeping): Ask how long-term training and promotion targets will be documented consistently.",
                "correct_answer": "1. 'With line managers supervising up to fifteen staff each, how will they find capacity to conduct fifteen separate check-ins every month during busy clinical shifts?'<br>2. 'What standardised form will we use during these informal chats to ensure staff training requests and pay-progression targets are still formally documented for HR?'",
                "tutor_tip": "Good probing questions always test the two main workplace pressures: Time capacity and Documentation/Cost."
            },
            {
                "marks": "3 Marks",
                "question": "You have just listened to a peer's presentation proposing that your local council should dim all residential streetlights by 50% after midnight to save electricity. Write a polite 2-sentence question that acknowledges their environmental point and probes the impact on shift workers and public safety.",
                "solution_steps": "1. Sentence 1: Acknowledge the energy-saving and carbon-reduction benefits outlined in their talk.<br>2. Sentence 2: Ask an open probing question about pedestrian safety for night-shift workers and elderly residents.",
                "correct_answer": "'Thank you for a very well-researched presentation—the projected £40,000 saving on council electricity bills is certainly impressive. However, how would the council protect the personal safety of night-shift nurses and factory workers walking home after midnight on dimly lit residential streets?'",
                "tutor_tip": "Complimenting a specific statistic from the speaker's talk before asking your question proves to the assessor that you were listening closely."
            }
        ]
    },

    # 5. Responding to Questions & Feedback
    {
        "filename": "slc-responding.html",
        "clean_topic": "Responding to Questions & Feedback",
        "intro_lead": "Formulate composed, structured, and evidenced responses using the PREP method when answering audience questions, handling unexpected challenges, and addressing counter-arguments.",
        "next_file": "slc-contributing.html",
        "next_name": "Contributing to Group Discussions",
        "spec_points": [
            ("L1.4 / L2.3", "Respond to questions and feedback clearly and effectively, giving detailed explanations and elaboration."),
            ("L2.5", "Follow and analyse lines of argument, using speech to clarify, defend, and develop points under questioning.")
        ],
        "golden_rules": [
            {
                "icon": "fa-shield-halved",
                "title": "Golden Rule 1: Use the PREP Formula to Answer Any Question Under Pressure",
                "desc": "Never panic or ramble when asked a tough question after your presentation. Structure your answer in 4 steps: Point (direct answer) → Reason (why) → Example (real-world evidence) → Point (reaffirm conclusion).",
                "badge": "Point → Reason → Example → Point (PREP)"
            },
            {
                "icon": "fa-handshake",
                "title": "Golden Rule 2: Validate the Questioner's Concern Before Pivoting with Evidence",
                "desc": "When someone challenges your proposal, never react defensively or say 'No, you're wrong'. Acknowledge their point ('That is an understandable concern regarding budget...'), then pivot calmly ('...however, the pilot data shows...').",
                "badge": "Acknowledge Courtesy → Validate Concern → Pivot with Factual Evidence"
            }
        ],
        "skills": [
            {
                "title": "Three Professional Strategies for Handling Tough or Unexpected Questions",
                "summary": "How to stay composed when an audience member asks a difficult or multi-part question.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Buy 3 Seconds of Thinking Time with a Courteous Opening:</strong> <em>"Thank you for raising that—staffing cover is a crucial operational aspect of this proposal."</em> This gives your brain 3 seconds to organise your PREP answer while sounding confident.</li>
                    <li><strong>Unpack Two-Part Questions Explicitly:</strong> <em>"There are two important parts to your question: first the upfront cost, and second the training time. Taking the cost first..."</em></li>
                    <li><strong>Handle Unknown Figures with Professional Honesty:</strong> Never invent absurd numbers on the spot. Say: <em>"I do not have the exact Q4 breakdown in front of me today; however, our last audit showed a 15% saving, and I would be happy to email the full cost table after this meeting."</em></li>
                  </ol>
                </div>
                """
            },
            {
                "title": "The PREP Response Architecture in Action",
                "summary": "See how the 4-sentence PREP model turns a challenging question into a Distinction-level answer.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">PREP Stage</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">What It Does</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Spoken Example (Question: 'Won't reusable cups create more washing-up work?')</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">P — Point</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Acknowledge and give a clear direct answer.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"That is a fair question, but switching to reusable mugs will not add extra workload for our catering staff."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; border-radius:0; font-weight:700;">R — Reason</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Explain the operational mechanism why.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Because our existing commercial dishwasher runs a high-temperature cycle in just ninety seconds per rack."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">E — Example</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Provide a concrete trial statistic or comparison.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"For example, when the Bristol office made this switch, staff simply placed their own mugs straight into the dishwasher racks at the end of breaks."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">P — Point</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Seal the conclusion and check if answered.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Therefore, we eliminate 4,000 disposable cups a month with zero extra catering hours. Does that address your concern?"</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Receiving Constructive Criticism & Modifying Your Proposal",
                "summary": "Why showing flexibility when a peer spots a flaw scores top marks at Level 2.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">You do not have to stubbornly defend every detail! If a questioner points out a genuine gap (e.g. disabled access or night-shift cover), incorporating their feedback proves advanced collaborative listening:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    <em>"Thank you for pointing that out, Farah—I had focused on daytime staff and had not factored in night-shift security. We should definitely amend the proposal to keep three floodlit spaces directly outside the main entrance reserved for night workers."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Answering a Question After a Talk on Healthy Canteen Meals",
                "marks": "Level 1 Responding to Questions Benchmark (L1.4)",
                "context": "Workplace Canteen Improvement Talk",
                "question": "After your short talk proposing healthier salad and soup options in the staff canteen, a peer asks:<br><em>'Healthy food is usually much more expensive—won't staff end up paying £7 or £8 for lunch?'</em><br>Deliver a clear 3-sentence response.",
                "steps": [
                    ("Step 1", "Acknowledge the concern about lunch prices", "'Thank you, Ben—keeping meals affordable for everyone is definitely a top priority.'", "Polite Acknowledgment (L1.4)"),
                    ("Step 2", "Explain how costs will be kept low", "'By buying seasonal vegetables in bulk from our local market supplier, the canteen can prepare fresh soup and salad bowls for under £3.50 per portion.'", "Clear Explanation & Figure"),
                    ("Step 3", "Reaffirm the benefit and check satisfaction", "'That means the healthy meal deal will actually cost 50p less than the current fried meal deal. Does that answer your question?'", "Positive Reassurance")
                ],
                "final_answer": "'Thank you, Ben—keeping lunch affordable for all staff is definitely a priority. By buying seasonal vegetables in bulk from our local supplier, the kitchen can serve fresh soup and a roll or a large salad bowl for £3.50. That means the healthy option will actually cost 50p less than the current burger meal deal.'",
                "tutor_tip": "Giving a specific, realistic price comparison ('£3.50 vs the current burger deal') makes your answer immediately convincing."
            },
            {
                "title": "Model 2 (Level 2): Defending a Presentation on Digital Patient Records (PREP Method)",
                "marks": "Level 2 Extended Q&A Response Benchmark (L2.3, L2.5)",
                "context": "Healthcare Informatics Implementation",
                "question": "Following your 4-minute presentation advocating for electronic tablets on hospital rounds, an assessor asks:<br><em>'Senior ward staff are already overwhelmed. Won't introducing new software simply increase their stress and cause charting errors?'</em><br>Deliver a model PREP response.",
                "steps": [
                    ("Step 1", "Point (Validate & Give Direct Thesis)", "'While any system transition carries an initial learning curve, introducing bedside tablets will significantly reduce overall nursing workload once implemented.'", "Validates Premise & States Thesis (L2.3)"),
                    ("Step 2", "Reason (Explain Functional Mechanism)", "'This is because automated drop-down menus and barcode wristband scanning eliminate repetitive handwritten transcription across three different paper folders.'", "Logical Operational Rationale"),
                    ("Step 3", "Example (Cite Measurable Pilot Evidence)", "'For instance, during the six-week pilot on Ward 6, pairing two floor super-users with nursing staff cut medication charting time by 35 minutes per shift and reduced transcription errors by 28%.'", "Persuasive Evidence (L2.4)"),
                    ("Step 4", "Point (Reaffirm Conclusion)", "'Therefore, with phased super-user mentoring during the first fortnight, the digital system relieves clinical pressure rather than adding to it.'", "Composed Concluding Synthesis (L2.5)")
                ],
                "final_answer": "'While any system change carries an initial learning curve, digital bedside tablets will actually reduce overall nursing workload once implemented. Automated drop-down menus and barcode scanning eliminate repetitive paper charting, saving an average of 35 minutes per shift. For instance, during the pilot on Ward 6, dedicated super-user floor support ensured charting errors dropped by 28% within the first fortnight. Therefore, with proper hands-on mentoring, the system relieves clinical pressure rather than adding to it.'",
                "tutor_tip": "Notice how the candidate did not deny that learning new software takes effort ('While any system change carries an initial learning curve...') before proving with Ward 6 data why the long-term benefit wins."
            }
        ],
        "examiner_traps": [
            {
                "title": "Giving One-Sentence Dismissive Replies ('No, It Will Be Fine')",
                "desc": "Brushing off an audience question with 'No, I don't think that will be a problem' fails Criterion L1.4 / L2.3, which requires detailed explanations.",
                "fix": "Always give at least 3 full sentences (Point + Reason + Example) when answering any question in your Q&A."
            },
            {
                "title": "Getting Flustered or Arguing Back Defensively",
                "desc": "If a peer challenges your idea, snapping back ('Well you clearly didn't listen to my slide!') ruins your professional register mark.",
                "fix": "Smile, thank the questioner for raising an important angle, and respond with calm facts."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "During a team discussion on installing recycling bins in a warehouse depot, a colleague remarks:<br><em>'No one will bother sorting rubbish; staff will just throw everything into the nearest bin.'</em><br>Write a 45-word spoken response using the <strong>PREP method</strong>.",
                "solution_steps": "1. Point & Reason: Acknowledge that poorly labelled bins cause confusion, but clear visual signage solves this.<br>2. Example: Cite that the Leeds depot achieved 85% sorting accuracy by placing colour-coded picture posters above each bin.<br>3. Point: Conclude that clear signage and a 5-minute briefing will make compliance easy.",
                "correct_answer": "'Compliance is certainly a valid concern if bins are poorly labelled; however, clear visual design makes sorting effortless. For example, when our Leeds depot installed colour-coded bins with large pictorial posters above each station, recycling accuracy reached 85% within two weeks. Therefore, combining clear signage with a brief morning toolbox talk will ensure our team adapts quickly.'",
                "tutor_tip": "Citing a successful trial at a sister branch or neighbouring ward is the easiest way to supply the 'E' (Example) in PREP."
            },
            {
                "marks": "3 Marks",
                "question": "At the end of your presentation on upgrading office lighting, an audience member asks:<br><em>'What is the exact kilowatt-hour rating of the proposed Philips LED tubes?'</em><br>You do not know that technical figure. Write a professional 2-sentence spoken response that handles the unknown detail with authority while offering relevant information you DO know.",
                "solution_steps": "1. State honestly and professionally that you do not have the exact wattage figure to hand, and offer to confirm it after the meeting.<br>2. Pivot to a related energy fact you do know (e.g. the 45% overall reduction in electricity bills).",
                "correct_answer": "'That is a great technical question—I do not have the exact kilowatt-hour specification per tube in front of me today, so I will check the manufacturer's datasheet and email that figure to the group this afternoon. What I can confirm from the estates quote is that the LED units consume 45% less electricity overall than our current fluorescent tubes.'",
                "tutor_tip": "Pivoting from a tiny technical detail you don't know to a headline statistic you DO know shows impressive workplace poise."
            },
            {
                "marks": "4 Marks",
                "question": "After your presentation proposing that a community library should replace half of its book shelves with computer desks, an elderly resident asks:<br><em>'Many older residents rely on large-print books and do not use computers—won't your plan push us out of our own library?'</em><br>Write a compassionate, constructive 4-sentence spoken response that validates their concern and adapts your proposal to protect large-print book stocks.",
                "solution_steps": "1. Validate the resident's concern with empathy and respect.<br>2. Reassure them that the library must remain inclusive for all age groups.<br>3. Adapt your proposal on the spot (e.g. keep 100% of the large-print and ground-floor reading collections, and place the new computer desks on the mezzanine floor).<br>4. Check if that reassurance helps.",
                "correct_answer": "'Thank you so much for raising that point, and I completely understand why protecting our book collection is vital for older residents. Our library must remain a welcoming space for every generation in the community. To ensure no readers lose out, we will ring-fence 100% of our large-print books and comfortable ground-floor armchairs, and instead install the new computer study desks purely in the upstairs reference room. Would keeping the entire ground floor dedicated to traditional reading address your concern?'",
                "tutor_tip": "Adapting your proposal to protect vulnerable service users shows high emotional intelligence and collaborative problem-solving."
            }
        ]
    },

    # 6. Contributing to Group Discussions
    {
        "filename": "slc-contributing.html",
        "clean_topic": "Contributing to Group Discussions",
        "intro_lead": "Master turn-taking conventions, verbal bridges, diplomatic disagreement, and group facilitation techniques to guide collaborative workplace meetings toward actionable consensus.",
        "next_file": "slc-line-of-argument-and-narratives.html",
        "next_name": "Line of Argument & Structured Presentations",
        "spec_points": [
            ("L1.5 / L2.7", "Respect the turn-taking rights of others during discussions, using appropriate conventions for turn-taking and moving discussions forward."),
            ("L2.4", "Express opinions and arguments and support them with relevant and persuasive evidence."),
            ("L2.5", "Follow and analyse lines of argument, synthesising diverse viewpoints to reach shared conclusions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-users",
                "title": "Golden Rule 1: Demonstrate All Three Discussion Roles (Facilitator, Builder, Synthesiser)",
                "desc": "To secure a clear Pass, demonstrate all three collaborative roles across the 12–15 minute discussion: The Builder (adds evidence to a peer's idea), The Facilitator (invites quiet peers and watches the clock), and The Synthesiser (summarises shared agreement at the end).",
                "badge": "Builder (Adds Evidence) • Facilitator (Invites Peers) • Synthesiser (Summarises Consensus)"
            },
            {
                "icon": "fa-bridge",
                "title": "Golden Rule 2: Always Build a Verbal Bridge Before Making Your Point",
                "desc": "Never start speaking as if the previous person said nothing. Link your contribution to the speaker before you: 'Building on Amara's point about...', 'While I understand Tom's concern regarding...'",
                "badge": "Verbal Bridge Formula: Peer's Name + Their Point + Your New Addition"
            }
        ],
        "skills": [
            {
                "title": "High-Scoring Turn-Taking & Facilitation Phrasebank",
                "summary": "Memorise these exact Standard English phrases to manage group dynamics gracefully.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Discussion Function</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">High-Scoring Spoken Phrasing</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Building on a Peer's Point</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Building on what Sarah just mentioned about parking, a staff car-share scheme would also cut commuter costs."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Inviting a Quiet Participant</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Marcus, you work closely with the night transport team—what are your thoughts on this handover schedule?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Diplomatic Disagreement</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I appreciate that perspective, Liam, although we also need to consider the staffing constraints during school holidays."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. Refocusing an Off-Topic Drift</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Those are interesting points, but conscious that we have five minutes remaining, shall we agree on our top three priorities?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">5. Summarising Final Consensus</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"To sum up our discussion, we all agree to trial the digital booking system for four weeks alongside a staff training workshop."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "How to Resolve a Deadlock Between Two Disagreeing Peers",
                "summary": "Use the 'Synthesis & Compromise' technique to unlock top Level 2 facilitation marks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Validate Both Sides Neutrally:</strong> Show that both speakers have raised legitimate workplace priorities (e.g. cost vs safety).</li>
                    <li><strong>Propose a Phased Pilot or Hybrid Compromise:</strong> Suggest combining the best elements of both ideas or running a 4-week trial on one department first.</li>
                    <li><strong>Check for Group Agreement:</strong> Ask: <em>"Would a four-week trial on Ward 2 satisfy both the budget concern and the safety requirement?"</em></li>
                  </ol>
                </div>
                """
            },
            {
                "title": "Non-Verbal Turn-Taking Signals (How to Enter Without Interrupting)",
                "summary": "How to signal that you are ready to speak without cutting across a peer mid-sentence.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Wait for a Clause Boundary:</strong> Never speak while someone is mid-sentence. Lean forward slightly, make eye contact, and slightly raise an open palm or pen as they finish their point.</li>
                    <li><strong>If Two People Start Speaking Simultaneously:</strong> Yield graciously once during the discussion (<em>"Please go ahead, Priya—I will come in right after your point"</em>). Assessors love recording this as direct evidence of Criterion L2.7!</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Refocusing a Drifting Group Discussion",
                "marks": "Level 1 Turn-Taking & Focus Benchmark (L1.5)",
                "context": "Workplace Staffroom Improvement Meeting",
                "question": "Your group is supposed to agree on how to spend a £500 grant to improve the staff breakroom, but two colleagues have spent three minutes arguing about football results. Deliver a polite spoken intervention that steers the group back to the task and invites a decision.",
                "steps": [
                    ("Step 1", "Polite interjection at a natural pause", "'Sorry to step in, everyone—it sounds like it was a great match on Saturday!'", "Friendly, Non-Confrontational Entry (L1.5)"),
                    ("Step 2", "Remind the group of the remaining time and core task", "'Conscious that we only have five minutes left to allocate our £500 breakroom grant, could we refocus on the equipment list?'", "Time & Agenda Awareness"),
                    ("Step 3", "Propose a concrete item and invite a peer's vote", "'We have £300 left after the new microwave—shall we spend that on comfortable armchairs or a filtered water cooler? Jade, what would you prefer?'", "Moves Discussion Forward")
                ],
                "final_answer": "'Sorry to step in, everyone—it sounds like a great match! Conscious that we only have five minutes left to allocate our £500 breakroom grant, could we refocus on our final items? After buying the commercial microwave for £200, we have £300 remaining. Jade, do you think we should spend that on new armchairs or a chilled water dispenser?'",
                "tutor_tip": "Citing the clock ('Conscious that we only have five minutes left...') is the most natural, polite excuse to bring an off-topic group back on track."
            },
            {
                "title": "Model 2 (Level 2): Hospital Waste Reduction Committee Consensus Facilitation",
                "marks": "Level 2 Synthesis & Consensus Benchmark (L2.4, L2.7)",
                "context": "NHS Sustainability Working Group",
                "question": "Four candidates are discussing how to reduce single-use plastic cups across hospital wards. The conversation has stalled after Liam argued reusable mugs pose a hot-drink scald risk to confused patients, while Sophie argued the hospital wastes 5,000 plastic cups a month. Intervene to resolve the impasse and guide the group to consensus.",
                "steps": [
                    ("Step 1", "Synthesise both competing concerns fairly", "'I think both points are vital: Liam is completely right that patient scald prevention on clinical bays comes first, while Sophie has shown our plastic waste exceeds 5,000 cups every month.'", "Validates Competing Views (L2.5)"),
                    ("Step 2", "Propose a targeted, phased compromise", "'Could we bridge both concerns by introducing reusable ceramic mugs strictly in staff breakrooms and administrative offices first—which accounts for 60% of cup usage—while keeping lidded biodegradable paper cups on patient bays?'", "Evidence-Led Compromise (L2.4)"),
                    ("Step 3", "Invite consensus confirmation and assign next step", "'Liam and Sophie, would that split approach protect patient safety while still cutting over 3,000 plastic cups a month?'", "Drives Collaborative Consensus (L2.7)")
                ],
                "final_answer": "'I think both points are vital: Liam is right that patient scald prevention on clinical wards comes first, while Sophie has shown our plastic waste exceeds 5,000 cups monthly. Could we bridge both concerns by introducing reusable mugs across all staff breakrooms and offices first—eliminating 3,000 plastic cups a month—while retaining safe lidded biodegradable cups for patient bays? Would everyone agree to recommend that two-tier policy?'",
                "tutor_tip": "Assessor witness sheets contain specific tick-boxes for 'helps move discussion forward' and 'synthesises viewpoints to reach consensus'."
            }
        ],
        "examiner_traps": [
            {
                "title": "Interrupting or Talking Over Peers Mid-Sentence",
                "desc": "Cutting across a speaker while they are still developing their point directly violates Criterion L1.5 / L2.7 and can force a full group resit.",
                "fix": "Wait until the speaker finishes their sentence before using a verbal bridge ('Building on that point...')."
            },
            {
                "title": "Letting the 15-Minute Discussion End Without a Final Decision",
                "desc": "Many groups chat for 15 minutes and stop when the timer rings without ever agreeing on the final recommendations requested in the brief.",
                "fix": "When 2 minutes remain, step in as the Synthesiser: 'In our final two minutes, let's confirm the three recommendations we all agree on...'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Write a 2-sentence <strong>verbal bridge</strong> that connects Colleague A's point (<em>'We need more car park security lights'</em>) to your own point about installing CCTV cameras at the bicycle shed.",
                "solution_steps": "1. Sentence 1: Reference Colleague A by name and validate their point about car park lighting.<br>2. Sentence 2: Link lighting to your complementary proposal for motion-activated CCTV over the cycle shelter.",
                "correct_answer": "'I completely agree with Hassan's point that upgrading the car park floodlights is essential for staff safety during winter evenings. Building on that security improvement, we should also install a motion-activated CCTV camera overlooking the staff bicycle shelter so that cyclists and drivers are equally protected.'",
                "tutor_tip": "Use the phrase 'Building on [Name]'s point about X, we should also...' at least twice in your exam discussion."
            },
            {
                "marks": "3 Marks",
                "question": "During a group discussion on improving staff induction, two participants start interrupting each other heatedly about whether induction should last one day or one week. Write a diplomatic 40-word intervention that calms the exchange, summarises both points, and proposes a middle ground.",
                "solution_steps": "1. Step in calmly and validate both perspectives (getting staff onto the floor quickly vs thorough safety training).<br>2. Propose a hybrid solution (2 days intensive core induction + 3 days shadowed floor buddy shifts).<br>3. Ask for agreement.",
                "correct_answer": "'Both of you are raising really important points: we need new starters productive on the shop floor quickly, yet we cannot rush mandatory safety training. Could we compromise on a two-day classroom induction covering core safety, followed by three days of paid floor shadowing with a senior buddy? Does that balance both priorities?'",
                "tutor_tip": "Stepping in to de-escalate two arguing peers and offering a practical compromise guarantees top facilitation marks."
            },
            {
                "marks": "4 Marks",
                "question": "There are 90 seconds left in your 15-minute Level 2 group discussion on reducing staff sickness absence. Write a 50-word <strong>concluding synthesis statement</strong> that summarises the group's three agreed measures (ergonomic chairs, flu vaccination vouchers, and flexible return-to-work interviews) and checks for unanimous agreement.",
                "solution_steps": "1. Signal that the meeting is concluding ('As we are in our final minute, let me summarise our agreed action plan...').<br>2. List the three agreed points clearly.<br>3. Ask the group to confirm unanimous agreement.",
                "correct_answer": "'As we are in our final ninety seconds, let me summarise the three recommendations we have agreed on today: first, replacing broken office chairs with ergonomic lumbar seating; second, offering free winter flu vaccination vouchers to all staff; and third, introducing supportive return-to-work wellbeing check-ins. Are we all happy to put those three measures forward as our final group decision?'",
                "tutor_tip": "Delivering the final 60-second summary statement is the single smartest move you can make in a Functional Skills group discussion."
            }
        ]
    },

    # 7. Structuring Arguments & Formal Presentations
    {
        "filename": "slc-line-of-argument-and-narratives.html",
        "clean_topic": "Structuring Arguments & Formal Presentations",
        "intro_lead": "Plan and deliver a compelling 3-to-5 minute formal presentation featuring an attention-grabbing opening hook, three signposted evidence-backed arguments, and a memorable concluding call to action.",
        "next_file": "slc-using-evidence.html",
        "next_name": "Using Evidence & Persuasive Points in Speech",
        "spec_points": [
            ("L1.3 / L2.1", "Identify and structure clear lines of argument and narratives in spoken explanations and formal presentations."),
            ("L2.3 / L2.5", "Follow and develop complex lines of argument, using spoken signposting to guide the audience and transition smoothly to Q&A.")
        ],
        "golden_rules": [
            {
                "icon": "fa-signs-post",
                "title": "Golden Rule 1: The Three-Part Spoken Signposting Architecture",
                "desc": "Unlike readers who can re-read a paragraph, listeners rely entirely on your verbal signposts. Tell your audience what you are going to cover (Roadmap), guide them through 3 numbered points ('First...', 'Moving to my second point...'), and summarise your conclusion.",
                "badge": "Hook & Roadmap (45s) → 3 Signposted Arguments (3m) → Conclusion & Q&A Invite (30s)"
            },
            {
                "icon": "fa-list-ol",
                "title": "Golden Rule 2: Speak From Bullet-Point Cue Cards—Never Read an A4 Essay Verbatim",
                "desc": "Reading word-for-word from a sheet of paper flattens your voice, destroys eye contact, and violates spoken communication criteria. Write 3 or 4 bold keywords per index card and speak naturally to the room.",
                "badge": "4 Cue Cards (1. Intro/Hook | 2. Point 1 & 2 | 3. Point 3 & Counter | 4. Conclusion)"
            }
        ],
        "skills": [
            {
                "title": "Minute-by-Minute Blueprint for a 4-Minute Level 2 Presentation",
                "summary": "How to pace your presentation so you hit every marking criterion without running over time.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Time Segment</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Structural Stage</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Exact Spoken Signpost Phrase</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">0:00 – 0:45</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Welcome, Hook &amp; Roadmap</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Good morning everyone. Did you know that...? Today I will examine three areas: first..., second..., and finally..."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">0:45 – 1:45</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Argument 1: The Core Problem</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Starting with my first point, let's look at the current impact on..."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1:45 – 2:45</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Argument 2: Proposed Solution &amp; Evidence</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Turning now to my second point, the evidence from our pilot scheme shows..."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2:45 – 3:30</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Argument 3: Counter-Argument &amp; Cost</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Finally, while some may question the upfront cost, the return on investment..."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3:30 – 4:00</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Summary &amp; Q&amp;A Handover</strong></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"In conclusion, implementing these three steps will... Thank you for listening; I welcome any questions."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Using Visual Aids & PowerPoint Slides Effectively",
                "summary": "How to use 3–4 simple slides or a handout to boost your presentation without hiding behind the screen.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>The 6x6 Slide Rule:</strong> Put no more than 6 bullet points per slide and no more than 6 words per bullet. Your slides are visual prompts for the audience, NOT your script!</li>
                    <li><strong>Face the Audience, Not the Whiteboard:</strong> Never turn your back on your peers to read off the projector wall. Glance at your laptop or cue card and maintain eye contact with your listeners.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Structuring Spoken Narratives & Workplace Case Accounts (STAR Method)",
                "summary": "When recounting an incident or case study in speech, use Situation → Task → Action → Result.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To keep spoken anecdotes focused and chronological, use <strong>STAR</strong>:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    • <strong>Situation &amp; Task:</strong> <em>"Last winter, our pharmacy dispensary faced a 40-minute backlog during peak afternoon discharges."</em><br>
                    • <strong>Action:</strong> <em>"We introduced a dedicated express tray for single-item prescriptions."</em><br>
                    • <strong>Result:</strong> <em>"Within two weeks, average patient waiting times fell from forty minutes to under twelve minutes."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): 3-Minute Talk Structure — Benefits of First-Aid Training in Schools",
                "marks": "Level 1 Presentation Structure Benchmark (L1.1, L1.3)",
                "context": "Community Health & Education Talk",
                "question": "Create a 3-part spoken talk outline (Introduction, 3 Main Points, Conclusion) explaining why all secondary school pupils should learn basic first aid and CPR.",
                "steps": [
                    ("Step 1", "Opening Hook & Purpose", "'Good morning everyone. If someone collapsed with a cardiac arrest in front of you today, would you know how to perform CPR? My talk today explains why every secondary school pupil should receive two hours of mandatory first-aid training each year.'", "Engaging Hook & Clear Topic (L1.3)"),
                    ("Step 2", "Three Sequenced Main Points", "'First, immediate CPR in the first three minutes doubles a person's chance of survival before anambulance arrives. Second, teenagers often look after younger siblings and can treat choking or burns safely. Third, St John Ambulance provides free school training kits, so the cost to schools is minimal.'", "Clear 3-Point Sequence"),
                    ("Step 3", "Concluding Summary & Q&A Invite", "'To sum up, teaching CPR in schools is simple, low-cost, and saves hundreds of lives every year. Thank you for listening—what questions do you have?'", "Strong Conclusion & Q&A Transition")
                ],
                "final_answer": "Complete 3-minute talk structure featuring a rhetorical question hook, three clearly signposted arguments (survival rates, home safety, low cost), and a confident invitation for audience questions.",
                "tutor_tip": "Opening your talk with a direct question ('If someone collapsed in front of you today, would you know what to do?') grabs every listener's attention in the first 10 seconds."
            },
            {
                "title": "Model 2 (Level 2): 4-Minute Presentation — Implementing Mental Health First Aiders in NHS Trusts",
                "marks": "Level 2 Extended Presentation Benchmark (L2.1, L2.3, L2.5)",
                "context": "Healthcare Staff Wellbeing & Retention Proposal",
                "question": "Deliver the structured opening, signposted argument transitions, and conclusion of a 4-minute Level 2 presentation advocating for accredited Mental Health First Aiders across acute hospital wards.",
                "steps": [
                    ("Step 1", "Hook, Authority & 3-Part Roadmap", "'Good morning colleagues. Did you know that anxiety and work-related stress accounted for 54% of all working days lost across the NHS last year? My name is Alex, and today I will present the business case for training one accredited Mental Health First Aider on every ward, covering three areas: early burnout prevention, confidential peer signposting, and the financial return on investment.'", "Statistic Hook & Roadmap (L2.1)"),
                    ("Step 2", "Signposted Arguments & Counter-Argument", "'Starting with early intervention, ward staff frequently hide emotional exhaustion until they reach crisis point... Turning to my second point, peer champions wear a green lanyard so colleagues can access confidential listening support on shift... Finally, while training forty champions costs £8,000, preventing just twenty agency-covered sick days recovers that entire cost within six months.'", "Coherent Line of Argument (L2.5)"),
                    ("Step 3", "Memorable Conclusion & Seamless Q&A Handover", "'In conclusion, caring for our staff is the foundation of safe patient care. By approving this £8,000 pilot today, we protect both our workforce and our ward budgets. Thank you for your attention; I now welcome any questions on our proposed rollout schedule.'", "Authoritative Close & Q&A")
                ],
                "final_answer": "Full 4-minute presentation blueprint combining a striking 54% NHS sickness statistic hook, explicit verbal signposting ('Starting with...', 'Turning to...', 'Finally...'), ROI cost rebuttal, and a composed handover to audience Q&A.",
                "tutor_tip": "Notice how the speaker gives the audience a clear 3-point roadmap in the first 30 seconds and then uses verbal signposts to tick off each stage."
            }
        ],
        "examiner_traps": [
            {
                "title": "Reading Verbatim from an A4 Sheet of Paper",
                "desc": "Staring down at a typed essay and reading it aloud monotone will fail the spoken delivery criteria even if the written essay is well written.",
                "fix": "Write your talk onto 4 small cue cards using large bullet-point keywords only."
            },
            {
                "title": "Stopping Abruptly With 'Yeah, That's Everything'",
                "desc": "Ending a formal presentation by muttering 'So yeah, that's all I've got' leaves the audience hanging and ruins your final impression.",
                "fix": "Always memorise your final two sentences: 'In conclusion, [1-sentence summary]. Thank you for listening, and I welcome any questions.'"
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Draft an attention-grabbing <strong>opening hook and roadmap</strong> (35–45 words) for a 4-minute Level 2 presentation proposing that your company should replace its diesel delivery vans with electric vehicles.",
                "solution_steps": "1. Open with a striking statistic or question about diesel fuel costs and urban clean-air charges.<br>2. State your proposal clearly.<br>3. Give a 3-point roadmap (fuel savings, clean-air zone compliance, and overnight depot charging).",
                "correct_answer": "'Good morning everyone. Last year alone, rising diesel prices and city Clean Air Zone penalties cost our delivery fleet over £38,000. Today, I will demonstrate why transitioning to electric delivery vans is essential, covering three key areas: annual fuel savings, zero-emission zone compliance, and overnight depot charging.'",
                "tutor_tip": "Hook Stat (£38,000 cost) + Clear Thesis + 3-Part Roadmap = the perfect 30-second presentation opening."
            },
            {
                "marks": "3 Marks",
                "question": "Convert this long, written paragraph into <strong>4 concise Cue Card bullet points</strong> (maximum 6 words per bullet) so a candidate can speak naturally without reading:<br><em>'If we introduce a four-day working week at the call centre, staff morale will improve dramatically and fewer people will resign. Last year we spent £15,000 recruiting and training replacement call handlers because staff were burned out. By rotating Friday and Monday rest days, we can keep phone lines open five days a week while giving staff a three-day weekend.'</em>",
                "solution_steps": "1. Extract Keyword Bullet 1: Morale & staff retention.<br>2. Extract Keyword Bullet 2: £15,000 recruitment cost last year.<br>3. Extract Keyword Bullet 3: Rotate Monday/Friday rest days.<br>4. Extract Keyword Bullet 4: 100% 5-day phone cover maintained.",
                "correct_answer": "Cue Card 2 — Staff Retention & Cover:<br>• Boosts morale & stops burnout<br>• Saves £15,000 annual recruitment cost<br>• Rotate Monday / Friday rest days<br>• Maintains 100% 5-day phone cover",
                "tutor_tip": "Each bullet contains just the trigger statistic or concept—allowing you to look up at your audience and form the sentences naturally."
            },
            {
                "marks": "3 Marks",
                "question": "Write a 35-word <strong>concluding summary and Q&A invitation</strong> for a presentation on why your care home should adopt an electronic medication administration record (eMAR) tablet system.",
                "solution_steps": "1. Start with a clear concluding signpost ('In conclusion,' or 'To sum up,').<br>2. Summarise the three core benefits (eliminates paper transcription errors, saves nursing time, and strengthens CQC safety ratings).<br>3. Thank the audience and invite questions.",
                "correct_answer": "'In conclusion, adopting the eMAR tablet system eliminates handwritten medication errors, saves nurses forty minutes per shift for direct resident care, and strengthens our CQC safety rating. Thank you for listening—I now welcome your questions.'",
                "tutor_tip": "Using the Rule of Three in your final summary sentence makes your presentation end on a crisp, memorable note."
            }
        ]
    },

    # 8. Using Evidence & Persuasive Data in Speech
    {
        "filename": "slc-using-evidence.html",
        "clean_topic": "Using Evidence & Persuasive Data in Speech",
        "intro_lead": "Elevate spoken arguments from personal opinions into indisputable business cases by embedding quantitative statistics, regulatory citations, and workplace pilot evidence.",
        "next_file": "slc-extracting-information.html",
        "next_name": "Listening & Extracting Key Information",
        "spec_points": [
            ("L2.4", "Express opinions and arguments and support them with relevant and persuasive evidence."),
            ("L1.1 / L2.1", "Identify and evaluate relevant supporting data and evidence in spoken discussions and presentations.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-pie",
                "title": "Golden Rule 1: Follow the Claim → Evidence → Impact Formula",
                "desc": "Never state a naked opinion ('We need new hoists'). Pair every claim with concrete evidence ('Breakdowns rose 40% last quarter') and explain the human or financial impact ('Delaying patient transfers by 20 minutes').",
                "badge": "Claim (What we need) → Evidence (Statistic/Audit) → Impact (Why it matters)"
            },
            {
                "icon": "fa-certificate",
                "title": "Golden Rule 2: Cite Authoritative Bodies & Workplace Audits Verbally",
                "desc": "Anchor your spoken points using authoritative sources: HSE safety guidelines, CQC regulations, NHS staff surveys, Citizens Advice reports, or internal company audit figures.",
                "badge": "Phrasing: 'According to our Q3 safety audit...', 'In line with HSE manual handling guidelines...'"
            }
        ],
        "skills": [
            {
                "title": "The Three Pillars of Persuasive Spoken Evidence",
                "summary": "Combine numbers, rules, and real-world examples to make any spoken argument bulletproof.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Evidence Pillar</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Why It Persuades</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Spoken Model Phrasing</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Quantitative Data &amp; Costs</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Proves financial scale and return on investment (ROI).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Replacing halogen floodlights across our three depots will cut annual electricity expenditure by £14,500."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Regulatory &amp; Legal Standards</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Shows mandatory compliance (HSE, CQC, GDPR).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Under the Health and Safety at Work Act, we are legally required to provide adequate ventilation in the workshop."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Comparative Pilot / Case Study</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Proves the solution already works in practice.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"When Ward 3 piloted staggered visiting hours in August, corridor congestion fell by 35% with zero complaints."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Before & After: Upgrading Vague Assertions into Evidenced Level 2 Arguments",
                "summary": "See how adding one realistic statistic and source satisfies Criterion L2.4 immediately.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-bottom:8px; color:#dc2626; font-weight:700;"><i class="fa-solid fa-xmark"></i> Unsubstantiated Opinion (Earns Zero Evidence Credit):</p>
                  <div style="background:#fef2f2; border-left:4px solid #dc2626; padding:12px; margin-bottom:14px; color:#334155;">
                    <em>"Everyone knows that the staff canteen food is way too expensive and nobody eats there anymore."</em>
                  </div>
                  <p style="margin-bottom:8px; color:#166534; font-weight:700;"><i class="fa-solid fa-check"></i> Evidenced Level 2 Argument (Ticks Criterion L2.4):</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; color:#334155;">
                    <em>"According to last month's staff wellbeing survey, 74% of employees stopped buying hot meals in the canteen after the price of a main meal rose to £6.80, leading to £400 of daily food waste."</em>
                  </div>
                </div>
                """
            },
            {
                "title": "How to Prepare 3 'Pocket Statistics' During Your Pre-Exam Research",
                "summary": "Never walk into an SLC assessment without 3 memorable figures on your notepad.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>1 Percentage Stat:</strong> e.g. <em>"68% of respondents in the national survey..."</em></li>
                    <li><strong>1 Financial / Cost Figure:</strong> e.g. <em>"An initial outlay of £1,200 that saves £3,500 per year..."</em></li>
                    <li><strong>1 Named Organisation / Report:</strong> e.g. <em>"Research published by the Royal College of Nursing / HSE / Local Government Association..."</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Supporting an Opinion with Practical Examples",
                "marks": "Level 1 Supporting Opinions Benchmark (L1.3)",
                "context": "Local Town Council Parking Discussion",
                "question": "In a group discussion about boosting Saturday trade for local High Street shops, support the idea of offering '2 Hours Free Parking' in council car parks using a clear reason and a real-world example.",
                "steps": [
                    ("Step 1", "State the core opinion clearly", "'I believe introducing two hours of free Saturday parking in the town centre car park is the best way to help independent shops.'", "Clear Opinion (L1.3)"),
                    ("Step 2", "Give the financial reason why shoppers currently avoid the High Street", "'Currently, families have to pay £4.50 just to park for ninety minutes, so many drive to the out-of-town retail park where parking is free.'", "Logical Reason & Price Detail"),
                    ("Step 3", "Provide a concrete neighbouring town example", "'When our neighbouring town, Market Drayton, introduced two hours of free Saturday parking last summer, High Street footfall increased by a quarter.'", "Concrete Supporting Example")
                ],
                "final_answer": "'I believe introducing two hours of free Saturday parking in the town centre is the best way to boost local trade. Currently, drivers pay £4.50 for ninety minutes, which pushes families toward out-of-town retail parks with free parking. When our neighbouring town trialled two hours of free Saturday parking last summer, High Street visitor numbers rose by 25%.'",
                "tutor_tip": "Comparing current costs (£4.50) with a successful trial in a neighbouring town makes your point grounded and persuasive."
            },
            {
                "title": "Model 2 (Level 2): Defending a Capital Funding Request for Electric Pallet Trucks",
                "marks": "Level 2 Persuasive Evidence Benchmark (L2.4)",
                "context": "Warehouse Distribution Logistics",
                "question": "A finance director questions why the depot needs £18,000 for three electric pallet trucks when manual pump trucks cost only £300 each. Deliver an evidenced spoken business case.",
                "steps": [
                    ("Step 1", "State the core claim focusing on long-term return on investment", "'While manual pump trucks have a low upfront price, investing £18,000 in three powered pallet trucks delivers substantial health and productivity savings.'", "Strategic Business Claim (L2.3)"),
                    ("Step 2", "Introduce internal HSE accident and agency cost data", "'According to our HSE accident log, manual-handling back strains caused 64 lost working days last year, costing the depot £9,200 in temporary agency cover alone.'", "Quantitative Audit Evidence (L2.4)"),
                    ("Step 3", "Project turnaround efficiency and payback period", "'Furthermore, trials in Bay 1 showed powered trucks cut lorry unloading times from 45 minutes to 22 minutes. Consequently, the £18,000 investment pays for itself within fourteen months while protecting our operatives from injury.'", "Measurable ROI & Impact")
                ],
                "final_answer": "'While manual trucks have a lower upfront cost, electric pallet trucks deliver substantial long-term savings. According to our HSE accident log, manual-handling strain injuries caused 64 lost working days last year, costing £9,200 in temporary agency cover. Furthermore, trials showed lorry turnaround times dropped from 45 minutes to 22 minutes. The investment pays for itself within 14 months while protecting staff wellbeing.'",
                "tutor_tip": "Comparing the hidden cost of staff injury leave (£9,200/year) against the equipment price creates an unarguable Level 2 business case."
            }
        ],
        "examiner_traps": [
            {
                "title": "Making Sweeping Generalisations ('Everyone Thinks...', 'It's Obvious...')",
                "desc": "Saying 'Everyone hates the new uniform' or 'It is obvious this will save millions' does not count as persuasive evidence under Criterion L2.4.",
                "fix": "Replace 'everyone' with a specific percentage or survey source: 'In last week's poll, 78% of ward staff reported...'"
            },
            {
                "title": "Dumping Raw Numbers Without Explaining Their Human Impact",
                "desc": "Reciting a string of numbers without explaining what they mean for patients, staff, or customers leaves listeners cold.",
                "fix": "Always follow a statistic with 'which means that...' to translate data into real-world impact."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "You are presenting an argument for installing chilled water dispensers on hospital wards for nursing staff. Combine one physiological fact and one operational benefit into a 40-word spoken statement.",
                "solution_steps": "1. Cite an authoritative source and physiological fact (e.g. Royal College of Nursing research showing a 2% drop in hydration reduces concentration by 15%).<br>2. Connect hydration directly to reduced medication charting errors and lower mid-shift fatigue.",
                "correct_answer": "'Clinical studies cited by the Royal College of Nursing show that even a 2% drop in hydration impairs concentration and cognitive focus by 15%. Installing chilled water dispensers on every ward will directly combat mid-shift fatigue and reduce prescription charting errors.'",
                "tutor_tip": "Citing recognised bodies like the Royal College of Nursing (RCN), HSE, or NICE immediately elevates your spoken authority."
            },
            {
                "marks": "3 Marks",
                "question": "Upgrade this weak, unsubstantiated spoken opinion into a persuasive Level 2 evidenced contribution for a college meeting:<br><em>'We should make all textbooks available online as PDFs because heavy books are annoying to carry and cost too much money.'</em>",
                "solution_steps": "1. Replace 'annoying to carry and cost too much' with concrete financial data (e.g. £140 average textbook cost per student).<br>2. Add accessibility evidence (screen-reader compatibility and zoom functions for learners with dyslexia or visual impairments).<br>3. State the impact on course completion.",
                "correct_answer": "'Providing free digital PDF textbooks on the college portal would remove a major financial barrier for adult learners, who currently spend an average of £140 per term on printed manuals. Furthermore, digital editions allow learners with dyslexia to adjust font sizes and use text-to-speech software on their phones, which increased assignment submission rates by 22% in the Business department last year.'",
                "tutor_tip": "Notice how pairing a financial figure (£140 per term) with an inclusivity benefit (dyslexia software) makes the argument twice as strong."
            },
            {
                "marks": "3 Marks",
                "question": "During a discussion on workplace security, a colleague says: <em>'Replacing our lost visitor paper book with an electronic tablet sign-in costs £600—that's a waste of money.'</em><br>Deliver a 3-sentence counter-argument using <strong>legal/regulatory evidence (GDPR & fire safety)</strong> to prove why the £600 tablet is necessary.",
                "solution_steps": "1. Acknowledge the £600 cost.<br>2. Cite GDPR data protection law (open paper visitor books let anyone read previous visitors' names, phone numbers, and car registrations, which breaches GDPR).<br>3. Cite fire safety compliance (instant cloud evacuation roll-call access on a warden's phone).",
                "correct_answer": "'While £600 is an upfront outlay, our current open paper visitor book leaves every visitor's full name, mobile number, and vehicle registration visible to the public, which directly breaches GDPR privacy regulations. An electronic tablet encrypts visitor details immediately and prints a photo lanyard badge. Furthermore, during a fire alarm, wardens can access the live digital visitor list on their phones at the assembly point in seconds.'",
                "tutor_tip": "Whenever a peer objects on cost, counter with GDPR data protection or Fire Safety compliance—legal requirements always trump minor costs!"
            }
        ]
    },

    # 9. Listening & Extracting Key Information
    {
        "filename": "slc-extracting-information.html",
        "clean_topic": "Listening & Extracting Key Information",
        "intro_lead": "Hone active listening strategies to capture critical facts under time pressure, separate mandatory operational directives from conversational filler, and synthesise multi-speaker viewpoints.",
        "next_file": "slc-language-in-context.html",
        "next_name": "Language in Professional Contexts",
        "spec_points": [
            ("L1.1 / L2.1", "Identify relevant information and lines of argument in spoken explanations, briefings, and presentations."),
            ("L2.5", "Follow and analyse spoken lines of argument, synthesising key facts to formulate relevant questions and responses.")
        ],
        "golden_rules": [
            {
                "icon": "fa-pen-to-square",
                "title": "Golden Rule 1: Use the 2-Column Listening Note Grid During Peer Talks",
                "desc": "Draw a line down the middle of your notepad before your peers start speaking. Label the left column 'Key Facts / Figures' and the right column 'My Follow-Up Question'. Jot down 3 keywords per speaker—never try to write full sentences.",
                "badge": "Left Column: Dates, Costs & Core Claims | Right Column: 1 Clarifying or Probing Question"
            },
            {
                "icon": "fa-ear-deaf",
                "title": "Golden Rule 2: Listen for Verbal Signposts and Stress Markers",
                "desc": "Speakers naturally flag their most important points using verbal signposts: 'Crucially...', 'Our primary recommendation is...', 'The mandatory deadline is...'. Perk up and note whatever follows these phrases.",
                "badge": "Listen for: 'Crucially' • 'The main risk is' • 'By Friday' • 'Three key reasons'"
            }
        ],
        "skills": [
            {
                "title": "Filtering Actionable Signal from Conversational Noise",
                "summary": "How to strip away anecdotes and pleasantries to isolate mandatory workplace instructions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Spoken Briefing Extract</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#64748b;">Conversational Filler (Ignore)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Extracted Key Information (Note Down)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Well, as you know the weather has been awful all week, but anyway, from Monday 3 November, all medication trolleys must be double-locked to the wall bracket between 13:00 and 14:00."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Weather remarks, 'well, as you know', 'but anyway'.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Rule:</strong> Double-lock med trolleys to wall 13:00–14:00 (starts Mon 3 Nov).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I personally think the new navy tunics look very smart, though the supplier phoned to say medium-sized tunics are delayed until Friday 20th."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Personal opinion on how smart navy looks.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Supply Update:</strong> Size Medium tunics delayed until Fri 20th.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Identifying a Speaker's Underlying Line of Argument & Bias",
                "summary": "At Level 2 (Criterion L2.1 & L2.5), you must track not just isolated facts, but the speaker's overall argument.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Ask 3 Listening Questions:</strong><br>
                    1. <em>What is the speaker's main proposal?</em> (e.g. Moving to cashless payments only).<br>
                    2. <em>What evidence are they relying on?</em> (e.g. Faster till queues and zero cash-handling bank fees).<br>
                    3. <em>What perspective have they overlooked?</em> (e.g. Elderly or vulnerable customers who rely on cash budgets).</li>
                    <li>Spotting what a speaker <strong>overlooked</strong> gives you the perfect probing question for the Q&amp;A!</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Shorthand Note-Taking Symbols for Fast Spoken Briefings",
                "summary": "Keep your eyes on the speaker 85% of the time by using quick symbols.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li>Use <strong>↑ / ↓</strong> for increases and decreases (e.g. <em>"Staff turnover ↓ 18%"</em>).</li>
                    <li>Use <strong>→</strong> for cause and effect (e.g. <em>"Broken boiler → Ward 2 moved to Ground Floor"</em>).</li>
                    <li>Use <strong>?</strong> in the margin next to any point you want to ask about in the Q&amp;A.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Extracting Key Details from a Voicemail Transcript",
                "marks": "Level 1 Information Extraction Benchmark (L1.1)",
                "context": "Reception Desk Telephone Message",
                "question": "Listen to / read this voicemail transcript left on the garage answerphone:<br><em>'Hi there, it's Mrs Anita Shah calling about my silver Ford Fiesta, registration BD68 KLP. Sorry I missed your call earlier—I was stuck in the dentist's chair! Anyway, please go ahead and fit the two new front tyres you quoted £140 for, and I will come in to collect the car at 4:30 pm today. My mobile is 07700 900412 if there's any problem.'</em><br>Extract the four essential workshop action details and ignore the filler.",
                "steps": [
                    ("Step 1", "Filter out irrelevant personal anecdote", "Ignore the comment about being stuck in the dentist's chair.", "Filters Noise (L1.1)"),
                    ("Step 2", "Extract Customer, Vehicle & Authorised Work", "Customer: Mrs Anita Shah (07700 900412) | Vehicle: Silver Ford Fiesta (BD68 KLP) | Authorised work: Fit 2 new front tyres at £140.", "Captures Core Facts"),
                    ("Step 3", "Extract Deadline Time", "Ready for customer collection at 16:30 today.", "Captures Deadline")
                ],
                "final_answer": "1. Customer & Contact: Mrs Anita Shah (07700 900412)<br>2. Vehicle: Silver Ford Fiesta (Reg: BD68 KLP)<br>3. Authorised Action: Fit two new front tyres at the agreed quote of £140<br>4. Deadline: Ready for collection by 16:30 today.",
                "tutor_tip": "Always double-check registration numbers, prices (£140), and exact collection times (16:30) when extracting spoken messages."
            },
            {
                "title": "Model 2 (Level 2): Extracting Compliance Directives & Formulating a Probe from a Ward Briefing",
                "marks": "Level 2 Listening & Analysis Benchmark (L2.1, L2.5)",
                "context": "NHS Acute Ward Morning Briefing",
                "question": "Read the transcript of the Ward Manager's briefing:<br><em>'Good morning team. First, thank you for covering the busy weekend shifts. A crucial reminder that our CQC inspection window opens next Monday, 17 November. All environmental cleaning audits must be uploaded to the digital portal by 16:00 daily without exception. Second, pharmacy reported that three controlled-drug entries lacked a second signature last Thursday; therefore, anyone administering Schedule 2 medications must log two practitioner signatures at the bedside immediately. Finally, the staff summer barbecue has been moved to 18 July.'</em><br>1. Extract the two mandatory clinical compliance directives.<br>2. Formulate one relevant follow-up question to clarify implementation.",
                "steps": [
                    ("Step 1", "Filter out social notices and pleasantries", "Ignore weekend thanks and the July barbecue date.", "Isolates Regulatory Content"),
                    ("Step 2", "Extract Compliance Directives 1 & 2 with exact times", "Directive 1: Upload environmental cleaning audits to the digital portal by 16:00 daily (ahead of CQC window on Mon 17 Nov).<br>Directive 2: Log two practitioner countersignatures immediately at the bedside for all Schedule 2 controlled drugs.", "Exact Extraction (L2.1)"),
                    ("Step 3", "Formulate a logical follow-up clarifying question", "Ask what backup procedure applies if the digital audit portal is offline at 16:00 or when only one registered nurse is on the bay during night break rotations.", "Analytical Follow-Up (L2.5)")
                ],
                "final_answer": "<strong>Directive 1:</strong> Upload daily environmental cleaning audits to the portal by 16:00 (effective immediately ahead of 17 Nov CQC window).<br><strong>Directive 2:</strong> Mandatory immediate bedside dual-signature logging for all Schedule 2 controlled drugs.<br><strong>Follow-Up Question:</strong> 'During night-shift break rotations when only one registered nurse is on Bay B, should we call the night coordinator across to witness and countersign Schedule 2 administrations at the bedside?'",
                "tutor_tip": "Notice how the follow-up question directly tests a real practical edge-case of Directive 2—proving both accurate listening and critical thinking."
            }
        ],
        "examiner_traps": [
            {
                "title": "Staring at Your Notepad Trying to Write Full Sentences",
                "desc": "If you try to write down every word a speaker says, you will miss their next two points AND lose marks for lack of eye contact.",
                "fix": "Write max 3–4 words per line (e.g. 'CQC 17 Nov | Audit 16:00 | CD 2 sigs') while keeping your head up."
            },
            {
                "title": "Asking a Question the Speaker Already Answered!",
                "desc": "Asking 'How much will it cost?' when the speaker clearly stated 'The total cost is £800' proves to the assessor that you were NOT listening.",
                "fix": "Refer to the figure they gave and probe deeper: 'You mentioned the total cost is £800—does that include installation?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A warehouse supervisor announces:<br><em>'We've had two near-misses in Loading Bay 4 this morning due to hydraulic oil spills. All operatives must wear steel-toecap boots and high-visibility vests at all times, and Loading Bay 4 is closed for steam cleaning until 14:30.'</em><br>Extract (a) the mandatory PPE rule and (b) the operational restriction.",
                "solution_steps": "1. Identify the mandatory PPE requirement.<br>2. Identify the specific location and time of the closure.",
                "correct_answer": "(a) Mandatory PPE Rule: All operatives must wear steel-toecap boots and high-visibility vests at all times.<br>(b) Operational Restriction: Loading Bay 4 is closed for steam cleaning until 14:30.",
                "tutor_tip": "Be exact with locations ('Loading Bay 4') and times ('until 14:30') when summarising safety briefings."
            },
            {
                "marks": "3 Marks",
                "question": "Read this spoken pitch from a colleague in a meeting:<br><em>'Switching all customer support entirely to an AI chatbot will save our company £30,000 a year in call-centre wages and give instant 24/7 replies.'</em><br>1. Identify the speaker's core line of argument.<br>2. Identify one critical customer-service risk the speaker has ignored.<br>3. Write an open question exposing that risk.",
                "solution_steps": "1. Core argument: Replace human call handlers with an AI chatbot to save £30,000/year and offer 24/7 responses.<br>2. Ignored risk: Complex complaints, elderly/vulnerable customers who struggle with chatbots, and customer frustration.<br>3. Open question probing how complex or distressed customer calls will be handled.",
                "correct_answer": "1. Line of Argument: Automating customer support via an AI chatbot saves £30,000 annually while providing 24/7 instant replies.<br>2. Overlooked Risk: Elderly or vulnerable customers and complex complaints that automated bots cannot resolve.<br>3. Probing Question: 'While the £30,000 saving is attractive, how would an automated chatbot support elderly customers without internet access or handle complex complaints that require human empathy?'",
                "tutor_tip": "Referencing the speaker's exact figure ('While the £30,000 saving is attractive...') before probing the flaw proves Level 2 active listening."
            },
            {
                "marks": "3 Marks",
                "question": "Convert this 55-word spoken briefing extract into <strong>3 concise shorthand notepad lines</strong> (using arrows/symbols) that take less than 10 seconds to jot down:<br><em>'Starting next Monday 9 November, our main staff car park will close for five days so contractors can install six electric vehicle chargers. During next week, all staff must park at the Leisure Centre overflow car park on Mill Road and show their staff ID badge to the barrier attendant.'</em>",
                "solution_steps": "1. Line 1: Date & closure (Mon 9 Nov, 5 days: Main car park CLOSED → 6 EV chargers).<br>2. Line 2: Alternative parking (Park at Leisure Centre overflow, Mill Rd).<br>3. Line 3: Requirement (Show Staff ID badge at barrier).",
                "correct_answer": "• Mon 9 Nov (5 days): Main car park CLOSED → 6 EV chargers installed<br>• Temp parking: Leisure Centre overflow (Mill Rd)<br>• Action: Must show Staff ID badge at barrier",
                "tutor_tip": "Short keyword notes let you capture 100% of the facts while keeping your eyes on the speaker."
            }
        ]
    },

    # 10. Language in Professional Contexts
    {
        "filename": "slc-language-in-context.html",
        "clean_topic": "Language in Professional Contexts",
        "intro_lead": "Eliminate casual slang and aggressive phrasing, master assertive workplace communication, and deploy respectful, dignified vocabulary across high-stakes vocational settings.",
        "next_file": "slc-your-turn.html",
        "next_name": "Role-Play, Scenarios & Discussion Practice",
        "spec_points": [
            ("L1.6 / L2.6", "Use appropriate language, tone, and register suitable for purpose, subject, and audience."),
            ("L2.3", "Communicate clearly, assertively, and effectively in a professional working environment.")
        ],
        "golden_rules": [
            {
                "icon": "fa-user-check",
                "title": "Golden Rule 1: Choose Assertive Communication Over Passive or Aggressive",
                "desc": "Passive speech ('I guess it doesn't matter') fails to solve workplace problems, while aggressive speech ('You ruined the schedule!') causes conflict. Assertive communication is calm, factual, respectful, and solution-focused.",
                "badge": "Passive (Retreats) | Aggressive (Attacks Person) | Assertive (Addresses Issue Calmly & Factually)"
            },
            {
                "icon": "fa-heart-pulse",
                "title": "Golden Rule 2: Always Use Dignified, Person-Centred Language for Clients & Patients",
                "desc": "Never refer to patients, customers, or residents using slang or labels ('the grumpy bloke in bed 3', 'the wheelchair lady'). Always use respectful professional phrasing ('Mr Evans in Bay 3', 'a resident who uses a wheelchair').",
                "badge": "Use Objective, Dignified Standard English at All Times"
            }
        ],
        "skills": [
            {
                "title": "Upgrading Colloquial Slang into Professional Functional English",
                "summary": "Memorise these high-frequency workplace register upgrades before your assessment.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Informal / Colloquial Slang</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Professional Functional English</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Vocational Context</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I had a chat with the bloke and he was fuming."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I spoke with the client, who expressed significant dissatisfaction."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Customer service / Incident handover.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The main printer is totally knackered again."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The main office printer has malfunctioned and requires an engineer callout."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Facilities / IT reporting.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We need to sort this mess out ASAP."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We must prioritise resolving this administrative backlog today."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Team planning meeting.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The lady in room 4 kicked off about her dinner."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The resident in Room 4 became distressed regarding her evening meal."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Health &amp; social care handover.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Passive vs Aggressive vs Assertive Workplace Phrasing",
                "summary": "How to raise problems or say 'no' to unsafe requests without causing confrontation.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Passive (Too Weak):</strong> <em>"Um, I don't really mind if I have to lift those heavy boxes on my own, I suppose I'll try."</em></li>
                    <li><strong>Aggressive (Hostile):</strong> <em>"Are you crazy? I'm not lifting 40kg crates by myself and breaking my back for you!"</em></li>
                    <li><strong>Assertive (Professional &amp; Safe):</strong> <em>"Because those crates exceed the 25kg single-person manual handling limit, I will need a colleague or a pallet truck to move them safely."</em></li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Maintaining Confidentiality & Objective Neutrality",
                "summary": "Never gossip, speculate, or blame other departments in front of clients.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When explaining a delay or error to a service user, keep internal staffing or private medical details confidential:</p>
                  <div style="background:#f0fdf4; border-left:4px solid #166534; padding:12px; margin-top:10px; color:#334155;">
                    • <strong>Wrong (Breaches Confidentiality &amp; Blames):</strong> <em>"Your appointment is late because Nurse Jones called in sick with a migraine and reception forgot to rebook you."</em><br>
                    • <strong>Right (Professional &amp; Solution-Focused):</strong> <em>"Due to unexpected staff absence this morning, our clinic is running twenty minutes behind schedule; however, Sister Patel will see you in Room 2 at 10:20."</em>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Assertively Refusing an Unsafe Workplace Shortcut",
                "marks": "Level 1 Professional Language Benchmark (L1.6)",
                "context": "Construction & Maintenance Safety",
                "question": "A busy colleague says to you: <em>'Don't bother fetching the tall stepladder from the van—just stand on that plastic swivel chair to change the ceiling bulb.'</em><br>Deliver a calm, assertive 2-sentence spoken refusal that explains the safety risk and states the correct action.",
                "steps": [
                    ("Step 1", "Refuse the unsafe shortcut calmly and assertively", "'I know we want to finish this job quickly, Danny, but I cannot stand on a wheeled swivel chair to reach the ceiling fitting.'", "Calm Assertive Refusal (L1.6)"),
                    ("Step 2", "State the safety hazard and immediate safe alternative", "'The chair could easily roll and cause a serious fall, so I will take two minutes to fetch the insulated fibreglass stepladder from the van.'", "Clear Safety Rationale")
                ],
                "final_answer": "'I know we are keen to finish quickly, Danny, but I cannot stand on a wheeled office chair to reach the ceiling light. It could easily tip and cause a serious fall, so I will take two minutes to fetch the insulated stepladder from the van.'",
                "tutor_tip": "Assertive speech focuses on the objective safety rule ('It could easily tip') rather than attacking the colleague."
            },
            {
                "title": "Model 2 (Level 2): Communicating a Treatment Delay to an Anxious Outpatient",
                "marks": "Level 2 Professional Register & Empathy Benchmark (L2.3, L2.6)",
                "context": "NHS Outpatients Clinic Customer Service",
                "question": "A patient (Mr Henderson) in the surgical waiting room has been waiting 60 minutes past his appointment time and says angrily: <em>'Have you lot forgotten about me or is the doctor just having a long lunch?'</em><br>Deliver a composed, empathetic spoken response.",
                "steps": [
                    ("Step 1", "Respectful greeting, validation, and sincere apology", "'Good afternoon Mr Henderson. Please accept my sincere apologies that you have been kept waiting an hour past your two o'clock appointment—I completely understand your frustration.'", "De-escalates & Validates (L2.6)"),
                    ("Step 2", "Transparent explanation preserving clinical confidentiality", "'Mr Evans, our consultant surgeon, was called into an unplanned emergency procedure in Theatre 2, which had to take clinical priority. He has just finished in theatre and is reviewing your notes now.'", "Objective Explanation without Breaching Privacy"),
                    ("Step 3", "Realistic updated timeframe and proactive comfort offer", "'He will call you into Consultation Room 1 within the next fifteen minutes. In the meantime, may I bring you a cup of water, or would you like me to update your parking permit at reception?'", "Proactive Service & Poise (L2.3)")
                ],
                "final_answer": "'Good afternoon Mr Henderson. Please accept my sincere apologies that you have been kept waiting past your two o'clock appointment—I completely understand your frustration. Mr Evans was called into an urgent emergency procedure in Theatre 2, which has just concluded. He will see you within the next fifteen minutes; in the meantime, may I get you a glass of water or extend your car park ticket free of charge?'",
                "tutor_tip": "Notice how the speaker never reacts to the 'long lunch' jibe—they remain warm, dignified, and offer practical help (extending the car park ticket)."
            }
        ],
        "examiner_traps": [
            {
                "title": "Blaming Other Departments or Colleagues ('The Night Shift Was Lazy')",
                "desc": "Saying 'Warehouse messed up again' or 'The agency staff are useless' reflects poorly on your professional standard and fails workplace register criteria.",
                "fix": "Use collective, objective process language: 'There was a communication gap during handover, which we are resolving now.'"
            },
            {
                "title": "Slipping into Casual Slang When You Relax Midway Through the Discussion",
                "desc": "Candidates often start formally for the first 3 minutes and then slip into 'mate', 'dodgy', 'ripped off', or 'mental' once the conversation warms up.",
                "fix": "Remember the video camera is recording the entire 15 minutes—maintain your professional workplace persona until the assessor stops the recording."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Rewrite this informal spoken handover sentence into dignified, professional Standard English suitable for a clinical ward meeting:<br><em>'The old guy in bed 3 went mad this morning cos his tea was cold and he chucked his newspaper on the floor.'</em>",
                "solution_steps": "1. Replace disrespectful slang ('The old guy', 'went mad', 'cos', 'chucked') with dignified clinical phrasing.<br>2. State the observation objectively.",
                "correct_answer": "'Mr Davies in Bay 3 became agitated this morning because his hot beverage had cooled down, and he threw his newspaper onto the floor.'",
                "tutor_tip": "Always refer to patients and service users by name or as 'the patient/resident in Bay 3', never 'the old guy'."
            },
            {
                "marks": "3 Marks",
                "question": "Convert this aggressive spoken complaint from a supervisor into a calm, <strong>assertive</strong> professional request:<br><em>'You are always turning up ten minutes late for the morning shift and leaving the rest of us to do your work! Sort your alarm out or don't bother coming in!'</em>",
                "solution_steps": "1. Remove personal attacks ('always', 'don't bother coming in') and state the factual observation (arriving at 08:10 instead of 08:00 three times this week).<br>2. Explain the operational impact on the morning handover.<br>3. Ask constructively if there is a transport issue and set a clear expectation.",
                "correct_answer": "'Ryan, I need to speak with you privately about morning punctuality, as you have arrived ten minutes after the 08:00 shift start three times this week. When team members arrive after 08:00, it delays our safety briefing and leaves the reception desk uncovered. Is there a transport issue we need to discuss, and can we agree that you will be on the floor ready to start at 08:00 from tomorrow?'",
                "tutor_tip": "Use the 'Fact → Impact → Expectation' formula for assertive workplace feedback."
            },
            {
                "marks": "3 Marks",
                "question": "A customer at a pharmacy counter asks loudly: <em>'Why is Mrs Jenkins from next door taking so long in the consultation room? What is wrong with her?'</em><br>Write a polite, firm 2-sentence spoken response that upholds <strong>patient confidentiality</strong> while assisting the waiting customer.",
                "solution_steps": "1. Politely decline to discuss another patient's medical consultation due to strict patient confidentiality.<br>2. Pivot immediately to helping the customer with their own prescription.",
                "correct_answer": "'To protect patient confidentiality, we never discuss another customer's consultation or health details. However, our second pharmacist will be free in just two minutes, and I can start preparing your prescription right away if you have your slip with you.'",
                "tutor_tip": "Politely stating 'To protect patient confidentiality...' while immediately offering service is the gold standard in health and social care."
            }
        ]
    },

    # 11. Discussion Simulations, Scenarios & Practical Drills
    {
        "filename": "slc-your-turn.html",
        "clean_topic": "Discussion Simulations, Scenarios & Practical Drills",
        "intro_lead": "Put Speaking, Listening, and Communicating theory into action through realistic Pearson Edexcel simulation briefs, 5-minute pre-discussion prep drills, and annotated model transcripts.",
        "next_file": "slc-the-exam.html",
        "next_name": "SLC Assessment Strategy & Exam Guide",
        "spec_points": [
            ("L1 & L2 SLC Standards", "Participate effectively in formal presentations and interactive workplace discussions."),
            ("L2.1–L2.7", "Demonstrate all seven Level 2 Speaking and Listening regulatory criteria across realistic simulation tasks.")
        ],
        "golden_rules": [
            {
                "icon": "fa-stopwatch-20",
                "title": "Golden Rule 1: Use Your 5-Minute Prep Time to Write the '3-1-2' Notepad Grid",
                "desc": "Before any group discussion begins, write down: 3 distinct arguments you will contribute, 1 realistic statistic or regulatory standard you will cite, and 2 open questions you will ask your peers.",
                "badge": "Pre-Discussion Grid: 3 Points • 1 Statistic • 2 Peer Questions"
            },
            {
                "icon": "fa-list-check",
                "title": "Golden Rule 2: Tick Off Your Personal Witness Checklist Live During the Talk",
                "desc": "Keep a tiny 4-box checklist at the corner of your notepad: [ ] Made Evidenced Point, [ ] Used Verbal Bridge, [ ] Asked Open Question, [ ] Summarised Consensus. Tick each box as you complete it!",
                "badge": "Live Self-Audit Guarantees You Never Miss a Criterion"
            }
        ],
        "skills": [
            {
                "title": "Three Regulated Workplace Discussion Simulation Briefs",
                "summary": "Authentic exam-standard scenarios to practise with peers or your tutor before assessment day.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <div style="display:flex; flex-direction:column; gap:16px;">
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#0369a1; margin-bottom:6px;"><i class="fa-solid fa-hospital"></i> Simulation Brief 1: Healthcare Shift Rota Reorganisation</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Your residential care home is debating switching from three 8-hour shifts to two 12-hour shifts. Consider staff fatigue, handover accuracy, resident continuity of care, and childcare impact. Reach a unanimous recommendation in 12 minutes.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#166534; margin-bottom:6px;"><i class="fa-solid fa-truck"></i> Simulation Brief 2: Logistics Depot Carbon &amp; Waste Reduction</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Your delivery hub must reduce packaging waste and carbon emissions by 20% over the next 12 months with a £5,000 budget. Discuss reusable plastic crates, solar roof panels, and route optimisation software. Agree on an action plan.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#ea580c; margin-bottom:6px;"><i class="fa-solid fa-graduation-cap"></i> Simulation Brief 3: Reducing Early Apprentice Drop-Out Rates</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Early leaver rates among first-year apprentices have reached 25%. Discuss establishing a 1-to-1 buddy system, allocating protected Friday study time, and travel subsidies. Agree on three compulsory retention steps.</p>
                    </div>
                  </div>
                </div>
                """
            },
            {
                "title": "How to Open, Middle-Steer, and Close a 12-Minute Group Discussion",
                "summary": "Exact spoken scripts for the three pivotal moments of any group assessment.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Discussion Phase</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Strategic Move</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Ready-to-Use Spoken Script</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Minute 1 (The Opening)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Set the agenda and invite the first view.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Shall we begin by outlining the main challenge? Our goal today is to agree on three practical ways to... Sarah, what would be your top priority?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Minute 6 (The Mid-Point Pivot)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Move the group from problem-talk to budget/solutions.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We have identified the main risks really clearly; now that we are halfway through, how should we allocate the £5,000 budget?"</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Minute 11 (The Final Wrap-Up)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Lock in the 3 agreed recommendations.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Before our time ends, let's confirm our final consensus: we are recommending X, Y, and Z. Does everyone agree with that summary?"</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Solo Practice Drill: The 60-Second Topic Improvisation",
                "summary": "How to build spoken fluency at home before exam day.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Pick any everyday workplace topic (e.g. <em>Why staff breaks matter, Banning mobile phones on wards, Free public transport for apprentices</em>), set a 60-second timer on your phone, and speak aloud using <strong>Point → Evidence → Explanation → Redirect</strong> without stopping or saying <em>"um"</em>.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Pre-Discussion 5-Minute Preparation Card (Simulation Brief 3)",
                "marks": "Level 1 Discussion Preparation Benchmark",
                "context": "Apprenticeship Retention Discussion Prep",
                "question": "You are given 5 minutes to prepare for Simulation Brief 3 (Reducing Early Apprentice Drop-Out Rates). Create a completed '3-1-2' preparation card showing your 3 points, 1 statistic, and 2 questions.",
                "steps": [
                    ("Step 1", "List 3 clear, practical contributions", "1. Pair every new apprentice with a second-year buddy.<br>2. Protect 4 hours every Friday morning strictly for college assignments.<br>3. Provide a £30 monthly bus pass subsidy for 16–19 apprentices.", "3 Core Contributions"),
                    ("Step 2", "Note 1 realistic supporting statistic", "'25% of apprentices drop out in the first 3 months because they fall behind on coursework.'", "1 Supporting Statistic"),
                    ("Step 3", "Write 2 open questions to ask peers", "Q1: 'How can we make sure supervisors don't pull apprentices out of their Friday study time?'<br>Q2: 'What qualities should we look for when choosing workshop mentors?'", "2 Open Questions")
                ],
                "final_answer": "<strong>3 Points:</strong> (1) 1-to-1 Buddy Scheme, (2) Protected Friday morning study block, (3) £30/month travel pass.<br><strong>1 Stat:</strong> 25% drop-out rate linked to coursework stress.<br><strong>2 Questions:</strong> 'How do we protect Friday study hours during busy weeks?' and 'What training do buddies need?'",
                "tutor_tip": "Walking into the discussion with this 6-line card in front of you guarantees you will never freeze or run out of things to say."
            },
            {
                "title": "Model 2 (Level 2): Annotated Multi-Speaker Discussion Transcript (Simulation Brief 1)",
                "marks": "Level 2 Distinction Performance Benchmark (L2.1–L2.7)",
                "context": "Residential Care Home 12-Hour Shift Policy Review",
                "question": "Analyse how Candidates A, B, and C achieve a unanimous Pass across all Level 2 criteria in this 3-turn exchange.",
                "steps": [
                    ("Turn 1 — Candidate A (Opening & Data)", "'To open our review of the proposed 12-hour shift rota, I looked at our recent staff survey where 62% of care assistants favoured working three 12-hour shifts per week to cut commuting costs. However, we need to evaluate how 12-hour shifts affect evening medication safety.'", "Introduces Quantitative Data & Agenda (L2.3, L2.4)"),
                    ("Turn 2 — Candidate B (Verbal Bridge & Regulatory Evidence)", "'Building on Candidate A's point about medication safety, a report by the Royal College of Nursing found that clinical errors double during the eleventh and twelfth hours of a shift unless breaks are enforced. Could we mandate two protected 30-minute rest breaks per 12-hour shift?'", "Verbal Bridge + External Citation + Solution (L2.4, L2.7)"),
                    ("Turn 3 — Candidate C (Synthesis & Peer Invitation)", "'That directly solves the fatigue risk Candidate A raised. What if we pilot an optional hybrid rota on Elm Wing for eight weeks—allowing parents who need 8-hour school-run shifts to keep them, while trialling 12-hour shifts with guaranteed breaks? Amara, how would that work for the night team?'", "Synthesises Compromise + Invites Quiet Peer (L2.5, L2.7)")
                ],
                "final_answer": "All three candidates demonstrate Level 2 mastery: citing survey/RCN data, building directly on the previous speaker's words, resolving conflict via a hybrid pilot, and inviting a quiet colleague by name.",
                "tutor_tip": "Notice how natural and collaborative the exchange is—nobody reads a speech; everyone reacts directly to what was just said."
            }
        ],
        "examiner_traps": [
            {
                "title": "Making One Big Speech at the Start and Staying Silent for the Next 10 Minutes",
                "desc": "Delivering all three of your points in the first 90 seconds and then sitting back silently for the rest of the meeting fails interactive turn-taking criteria.",
                "fix": "Pace your contributions: share Point 1 in the first third, Point 2 in the middle third, and summarise consensus at the end."
            },
            {
                "title": "Ignoring Quiet Group Members Who Are Struggling to Get In",
                "desc": "If a nervous candidate in your group hasn't spoken after 5 minutes, a good team player actively invites them in.",
                "fix": "Turn to the quiet member warmly and ask: 'David, we haven't heard your view yet—what do you think about option B?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Look at <strong>Simulation Brief 2</strong> (Logistics Depot Carbon & Waste Reduction with a £5,000 budget). Write a 40-word <strong>opening contribution</strong> to launch the group discussion, introduce a specific initiative with a figure, and hand over to a peer (Liam).",
                "solution_steps": "1. Open the meeting and state the goal (20% waste/carbon reduction within our £5,000 budget).<br>2. Propose replacing single-use cardboard boxes with reusable plastic tote crates (eliminating 3,000 boxes a month for £2,200).<br>3. Ask Liam for his view.",
                "correct_answer": "'Good morning everyone. To hit our 20% waste reduction target within the £5,000 budget, I propose spending £2,200 on durable, stackable plastic tote boxes, which would eliminate 3,000 single-use cardboard cartons every month. Liam, how well would reusable crates fit onto our existing delivery vans?'",
                "tutor_tip": "Starting the discussion first is a great way to conquer nerves and claim immediate leadership credit."
            },
            {
                "marks": "3 Marks",
                "question": "During <strong>Simulation Brief 2</strong>, a peer proposes spending £45,000 on solar roof panels—even though the scenario brief states the total budget is only £5,000. Write a polite 3-sentence response that points out the budget constraint without embarrassing them and suggests a lower-cost lighting alternative.",
                "solution_steps": "1. Validate the long-term environmental benefit of solar panels.<br>2. Gently remind the group of the £5,000 maximum budget limit in the brief.<br>3. Suggest smart motion-sensor LED warehouse lighting for £1,800 instead.",
                "correct_answer": "'Solar roof panels would certainly deliver huge long-term carbon savings, Priya. However, because our total budget for this quarter is capped at £5,000, a £45,000 installation would need board approval next year. In the meantime, could we spend £1,800 installing motion-sensor LED switches in the warehouse aisles, which cuts lighting electricity by 35% immediately?'",
                "tutor_tip": "Checking proposals against the constraints in the brief (budget, deadline, headcount) proves sharp Level 2 analytical listening."
            },
            {
                "marks": "3 Marks",
                "question": "Create a <strong>'3-1-2' Pre-Discussion Notepad Plan</strong> for a 12-minute discussion on <em>'How to Improve Healthy Eating & Wellbeing for Night-Shift Hospital Staff'</em>.",
                "solution_steps": "1. Write 3 distinct practical proposals (24-hour healthy vending chiller, functioning breakroom microwaves, quiet dark rest pods).<br>2. Write 1 realistic statistic (e.g. 70% of night nurses rely on sugary snacks after 20:00).<br>3. Write 2 open questions to ask peers.",
                "correct_answer": "<strong>3 Points:</strong> (1) Stock a subsidised 24-hour fresh soup/salad smart-fridge, (2) Install two commercial microwaves on every ward breakroom, (3) Create a quiet darkened 20-minute rest room.<br><strong>1 Statistic:</strong> Trust survey showed 70% of night staff have no access to hot healthy food after 20:00.<br><strong>2 Open Questions:</strong> 'How could catering restock the smart-fridge before the 19:30 shift starts?' and 'What impact does night-shift nutrition have on staff sickness rates?'",
                "tutor_tip": "Practise writing a 3-1-2 plan in under 4 minutes for any workplace topic."
            }
        ]
    },

    # 12. Speaking, Listening & Communicating Exam Strategy & Grading Criteria
    {
        "filename": "slc-the-exam.html",
        "clean_topic": "Speaking, Listening & Communicating Exam Strategy & Grading Criteria",
        "intro_lead": "A complete guide to the Pearson Edexcel and City & Guilds Functional Skills English SLC assessment: official witness sheets, video recording rules, L1 vs L2 criteria, and how to guarantee a first-time Pass.",
        "next_file": "functional-skills-english-level-2.html",
        "next_name": "Functional Skills English Level 2 Directory",
        "spec_points": [
            ("L1.1–L1.6 & L2.1–L2.7", "Full mastery of regulated Ofqual Speaking, Listening and Communicating subject content criteria."),
            ("Witness Testimony & Recording", "Assessor observation records, camera positioning rules, and internal quality assurance (IQA) standards.")
        ],
        "golden_rules": [
            {
                "icon": "fa-award",
                "title": "Golden Rule 1: Every Single Criterion Must Be Evidenced (100% Mastery Rule)",
                "desc": "Unlike Reading and Writing where marks are added up to reach a pass boundary, SLC is graded on an 'All Criteria Met' basis. You must demonstrate every single criterion (L2.1 to L2.7) at least once across your tasks to achieve a Pass.",
                "badge": "All-or-Nothing Mastery: Hit Every Tick-Box on the Assessor Witness Sheet"
            },
            {
                "icon": "fa-video",
                "title": "Golden Rule 2: Speak Directly to Your Peers—Ignore the Camera and Assessor",
                "desc": "The video camera is only there so an external moderator can verify the assessor's marking, and the assessor is a silent observer. Look exclusively at your group members with warm, natural eye contact.",
                "badge": "Look at Your Group Peers, Never at the Examiner or Camera Lens"
            }
        ],
        "skills": [
            {
                "title": "The Official Pearson Edexcel Level 2 Assessor Witness Sheet Deconstructed",
                "summary": "See the exact 7 criteria boxes sitting on your examiner's clipboard and how to trigger every tick.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0; overflow-x:auto;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Code</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Official Criterion Descriptor</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Exact Action That Guarantees the Tick</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.1</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Identify relevant information and lines of argument</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Take brief notes during peer talks and refer accurately to a specific figure or argument they made.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.2</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Make requests and ask detailed questions</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Ask at least 2 open probing questions (<em>"How will...?", "What evidence...?"</em>) during Q&amp;A and discussion.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.3</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Communicate ideas clearly and effectively with detail</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Deliver a 4-minute structured presentation and answer Q&amp;A questions using the 4-step PREP method.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.4</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Support arguments with relevant, persuasive evidence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Quote at least 2 statistics, financial figures, or regulatory standards (HSE, CQC, NHS) in your talk and discussion.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.5</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Follow and analyse lines of argument using spoken techniques</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Use clear signposts, vocal emphasis, controlled pauses, and synthesise competing views in the discussion.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.6</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Use appropriate language and register for audience</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Maintain composed professional Standard English throughout; zero slang or aggressive remarks.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.7</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Respect turn-taking rights and move discussion forward</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Never interrupt; use verbal bridges (<em>"Building on..."</em>); invite a quiet peer by name; summarise consensus.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Online Remote Assessment (Teams / Zoom) vs In-Person Room Rules",
                "summary": "How to pass smoothly if your SLC exam is conducted remotely via Microsoft Teams or Zoom.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Camera &amp; Lighting Check:</strong> Position your webcam at eye level with a light source in front of you so the assessor and moderator can clearly see your face and non-verbal listening cues.</li>
                    <li><strong>Handling Online Audio Lag:</strong> On video calls, slight audio delays can cause accidental overlapping speech. Always use the speaker's first name when handing over (<em>"Priya, what do you think?"</em>) so turn-taking is crystal clear.</li>
                    <li><strong>Screen-Sharing Your Slides:</strong> Test screen-sharing 10 minutes before the assessment starts, and keep your physical cue cards in your hand so you never read off a hidden Word document on screen.</li>
                  </ul>
                </div>
                """
            },
            {
                "title": "Conquering Exam Nerves & Vocal Anxiety in 3 Minutes",
                "summary": "Simple physiological techniques used by professional speakers to steady a shaky voice.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Box Breathing (4–4–4):</strong> Inhale quietly through the nose for 4 seconds, hold for 4 seconds, exhale slowly for 4 seconds. This immediately lowers heart rate and stops vocal tremor.</li>
                    <li><strong>Memorise Your First Sentence Word-for-Word:</strong> Nerves peak in the first 15 seconds. Knowing your opening sentence by heart gets you over the starting line smoothly.</li>
                    <li><strong>Keep a Glass of Water Next to Your Notepad:</strong> Taking a small sip of water before the Q&amp;A begins relieves dry mouth and gives you a natural 3-second pause.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Model 1 (Level 1): Pre-Assessment 10-Minute Readiness Routine",
                "marks": "Level 1 Exam Readiness Protocol",
                "context": "SLC Assessment Day Countdown",
                "question": "How should a candidate use the final 10 minutes before entering the SLC assessment room (or joining the video call) to guarantee peak performance?",
                "steps": [
                    ("Step 1", "Audit Cue Cards & Notepad (Minutes 1–4)", "Check that your 3 or 4 presentation cue cards are numbered in order, with key statistics highlighted in yellow, and draw your 2-column listening grid on a blank notepad page.", "Materials Organised"),
                    ("Step 2", "Vocal & Breathing Warm-Up (Minutes 5–7)", "Take three slow diaphragmatic breaths, sip room-temperature water, and quietly rehearse your opening hook sentence.", "Calms Nerves & Steadies Voice"),
                    ("Step 3", "Learn Your Group Members' First Names (Minutes 8–10)", "Introduce yourself warmly to your 3 or 4 fellow candidates and write their first names in seating order at the top of your notepad.", "Enables Natural Verbal Bridging")
                ],
                "final_answer": "1. Number cue cards & draw 2-column listening grid | 2. Slow breathing + rehearse opening sentence | 3. Note down fellow candidates' names in seating order so you can address them by name during the discussion.",
                "tutor_tip": "Writing down your group members' names in seating order at the top of your notepad is a game-changer—it lets you say 'Building on Sarah's point...' effortlessly."
            },
            {
                "title": "Model 2 (Level 2): Self-Auditing a Candidate's Performance Against the Witness Sheet",
                "marks": "Level 2 Assessor Marking Audit (L2.1–L2.7)",
                "context": "Examiner Standardization Review",
                "question": "During a 12-minute Level 2 group discussion, Candidate Jordan spoke four times, cited two statistics, and did not interrupt anyone, yet the assessor flagged a borderline concern on Criterion L2.2. Explain why Jordan was at risk on L2.2 and how to fix it in the final two minutes.",
                "steps": [
                    ("Step 1", "Check the exact requirement of Criterion L2.2", "Criterion L2.2 requires the candidate to 'make requests and ask detailed questions using appropriate language'.", "Identifies Criterion L2.2"),
                    ("Step 2", "Diagnose why Jordan's performance was incomplete", "Although Jordan made strong statements and cited statistics (meeting L2.3, L2.4, and L2.6), Jordan never asked a question to another participant!", "Spots Missing Question Evidence"),
                    ("Step 3", "Deliver the immediate fix before the timer ends", "In the final two minutes, Jordan must ask an open probing or collaborative question to a peer (e.g. 'Elena, how would we measure the success of this trial after three months?').", "Secures 100% Criteria Pass")
                ],
                "final_answer": "Diagnosis: Jordan met L2.3 and L2.4 by making evidenced statements, but failed to ask any detailed questions (L2.2). Fix: Before the discussion ends, Jordan must ask at least two open probing questions to peers or during the presentation Q&A.",
                "tutor_tip": "Never finish a discussion having only made statements! You MUST ask at least two open questions so the assessor can tick box L1.2 / L2.2."
            }
        ],
        "examiner_traps": [
            {
                "title": "Forgetting That You Cannot Pass Overall English Without Passing SLC",
                "desc": "Even if you score 90% in your Reading and Writing exams, Ofqual regulations state that your Functional Skills English certificate cannot be issued until your SLC Pass is logged.",
                "fix": "Prepare your 4-minute presentation cue cards and discussion phrases with the same care as a job interview."
            },
            {
                "title": "Looking at the Assessor for Approval After Every Sentence",
                "desc": "Turning to look at the examiner to see if they are nodding breaks the natural group dynamic and makes you look self-conscious.",
                "fix": "Pretend the assessor is not in the room—keep 100% of your eye contact on your fellow group participants."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "State the <strong>three observable actions</strong> you must complete during the Task 2 Group Discussion to ensure Criterion L2.7 (respecting turn-taking rights and moving discussion forward) is ticked off by your assessor.",
                "solution_steps": "1. Action 1: Never interrupt or talk over a peer while they are speaking.<br>2. Action 2: Use a verbal bridge referencing the previous speaker's name and point.<br>3. Action 3: Actively invite a quieter participant into the conversation with an open question (and help summarise agreement).",
                "correct_answer": "1. Allow peers to finish their sentences without interrupting.<br>2. Use a verbal bridge that references a peer's point by name ('Building on Marcus's point...').<br>3. Actively invite a quieter group member to contribute with an open question and help summarise consensus.",
                "tutor_tip": "Memorise these three actions as your non-negotiable discussion checklist."
            },
            {
                "marks": "3 Marks",
                "question": "A candidate brings a 600-word typed essay into their Level 2 Formal Presentation and reads it aloud word-for-word without looking up. Explain which <strong>two SLC assessment criteria</strong> this candidate is at high risk of failing and how they should prepare their notes instead.",
                "solution_steps": "1. Identify Criterion L2.3 (Communicate clearly and effectively in speech) and L2.5 (Use spoken techniques such as pitch, pace, eye contact, and natural delivery).<br>2. Explain the fix: Convert the essay into 4 small index cue cards with 3–4 bold bullet-point keywords per card.",
                "correct_answer": "At-risk criteria: L2.3 (effective spoken communication) and L2.5 (using spoken techniques and audience engagement), because reading verbatim produces a flat monotone and zero eye contact.<br>Fix: Condense the script onto four numbered index cue cards containing only short bullet-point keywords and statistics.",
                "tutor_tip": "Assessors are grading your SPEAKING skills, not your ability to read an essay aloud!"
            },
            {
                "marks": "3 Marks",
                "question": "Your SLC assessment is taking place online via Microsoft Teams tomorrow morning. List <strong>three practical technical and presentation checks</strong> you should perform 15 minutes before the call begins.",
                "solution_steps": "1. Check 1 (Camera & Lighting): Position camera at eye level in a well-lit, quiet room so your face and non-verbal nodding are clearly visible on the recording.<br>2. Check 2 (Audio & Screen-Share): Test microphone clarity and verify that your 3–4 presentation slides share cleanly.<br>3. Check 3 (Cue Cards & Notepad): Place physical cue cards and a blank notepad + pen next to your keyboard so your eyes stay near the webcam.",
                "correct_answer": "1. Position the webcam at eye level in a quiet, well-lit room so the assessor can see your eye contact and non-verbal listening cues.<br>2. Test microphone audio and practise screen-sharing your presentation slides in advance.<br>3. Place physical bullet-point cue cards and a 2-column listening notepad on your desk so you do not read off the screen.",
                "tutor_tip": "On video calls, sticking your cue card right beside your webcam lens makes it look like you are maintaining direct eye contact with everyone!"
            }
        ]
    }
]
