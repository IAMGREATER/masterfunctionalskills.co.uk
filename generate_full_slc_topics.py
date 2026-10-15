#!/usr/bin/env python3
import sys

# Load batch 1
import build_slc_module
all_slc = list(build_slc_module.SLC_TOPICS)

# Define batch 2
batch_2 = [
    {
        "filename": "slc-line-of-argument-and-narratives.html",
        "clean_topic": "Structuring Arguments & Formal Presentations",
        "intro_lead": "Plan and deliver a well-structured, 3-to-5 minute formal presentation featuring a captivating opening, coherent signposted arguments, and a memorable concluding summary.",
        "next_file": "slc-using-evidence.html",
        "next_name": "Using Evidence & Persuasive Points in Speech",
        "spec_points": [
            ("L2.1", "Identify relevant information and lines of argument in explanations or presentations."),
            ("L2.5", "Follow and analyse lines of argument, using speech and other techniques to clarify and develop points.")
        ],
        "golden_rules": [
            {
                "icon": "fa-signs-post",
                "title": "Golden Rule 1: The Three-Part Signposting Structure",
                "desc": "Tell your audience what you are going to tell them (Introduction), tell them (Body paragraphs with evidence), and tell them what you told them (Conclusion & Action).",
                "badge": "Introductory Roadmap → 3 Core Arguments → Concluding Action"
            },
            {
                "icon": "fa-list-ol",
                "title": "Golden Rule 2: Limit Spoken Body Arguments to Three",
                "desc": "Audiences cannot retain seven disconnected points in a spoken presentation. Pick three compelling, evidence-backed arguments and explore them in depth.",
                "badge": "Rule of Three: 3 Main Arguments + 1 Concrete Recommendation"
            }
        ],
        "skills": [
            {
                "title": "The 5-Part Formal Presentation Architecture",
                "summary": "Step-by-step structural blueprint for Level 2 Functional English presentations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>The Hook &amp; Welcome (0:00–0:30):</strong> Welcome the audience, state your professional title, and hook attention with a striking statistic or vocational problem statement.</li>
                    <li><strong>The Overview / Roadmap (0:30–0:45):</strong> <em>"Today I will cover three areas: our current challenge, the proposed solution, and the anticipated cost benefits."</em></li>
                    <li><strong>Argument 1 &amp; Evidence (0:45–2:00):</strong> Present primary finding supported by real-world data or official standards.</li>
                    <li><strong>Argument 2 &amp; Counter-Perspective (2:00–3:15):</strong> Present operational mechanics and address potential feasibility hurdles.</li>
                    <li><strong>Conclusion &amp; Call to Action (3:15–4:00):</strong> Summarize core findings, offer a clear next step, and invite audience questions.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "4-Minute Presentation Plan: Implementing Mental Health First Aiders in NHS Trusts",
                "marks": "Full Criteria Level 2 (L2.1, L2.5)",
                "context": "Healthcare Staff Wellbeing & Retention",
                "question": "Structure a 4-minute presentation advocating for accredited Mental Health First Aid training for senior healthcare assistants.",
                "steps": [
                    ("Step 1", "Introduction & Hook", "'Good morning colleagues. Did you know that work-related stress accounted for 54% of all working days lost in the NHS last year? My name is Alex, and today I propose introducing certified Mental Health First Aiders across our acute wards.'", "Hook with national statistic, establish authority"),
                    ("Step 2", "Signposted Main Arguments", "'First, early intervention prevents staff burnout before it escalates to long-term sickness. Second, peer support creates a confidential culture where carers feel supported. Third, reducing agency cover costs will offset training fees within six months.'", "Logical 3-part argument with explicit signposts"),
                    ("Step 3", "Impactful Conclusion & Invitation", "'In conclusion, supporting our carers enables them to provide safer care for our patients. Thank you for your time; I now welcome any questions on our proposed roll-out schedule.'", "Clear summary and seamless transition to Q&A")
                ],
                "final_answer": "Complete presentation structure adhering strictly to the 4-minute guideline with clear signposts, credible evidence, and professional Q&A invitation.",
                "tutor_tip": "Notice how each transition word ('First', 'Second', 'Third', 'In conclusion') acts as a mental signpost for the assessor."
            }
        ],
        "examiner_traps": [
            {
                "title": "Reading from an A4 Script Verbatim",
                "desc": "Reading full written paragraphs makes your delivery flat, destroys eye contact, and results in failing criteria for spoken communication.",
                "fix": "Use index cue cards containing only 3–5 bullet points and key statistics per card."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "Draft an introductory hook (30 words) and a concluding summary (30 words) for a 3-minute presentation on why your care home should adopt an electronic medication administration record (eMAR) system.",
                "solution_steps": "Hook: 'Good morning team. Last quarter, manual paper charting errors cost our care home 120 admin hours. Today I will demonstrate how eMAR eliminates transcription mistakes and safeguards residents.'<br>Conclusion: 'To conclude, eMAR ensures 100% medication compliance, frees up staff time for direct resident care, and protects our CQC rating. I welcome any questions.'",
                "correct_answer": "Features clear problem hook and structured concluding recommendation.",
                "tutor_tip": "Connecting the topic to CQC or regulatory standards demonstrates high-level vocational understanding."
            }
        ]
    },
    {
        "filename": "slc-using-evidence.html",
        "clean_topic": "Using Evidence & Persuasive Data in Speech",
        "intro_lead": "Elevate spoken arguments by embedding quantitative data, regulatory citations, and real-world case studies to build indisputable vocational business cases.",
        "next_file": "slc-extracting-information.html",
        "next_name": "Listening & Extracting Key Information",
        "spec_points": [
            ("L2.4", "Express opinions and arguments and support them with relevant and persuasive evidence."),
            ("L2.1", "Identify and evaluate relevant evidence and supporting data in spoken discourse.")
        ],
        "golden_rules": [
            {
                "icon": "fa-chart-pie",
                "title": "Golden Rule 1: The Claim-Evidence-Impact Formula",
                "desc": "Never state a claim in isolation. Pair every assertion with tangible evidence and explain its human or financial impact.",
                "badge": "Claim ('We need new hoists') → Evidence ('Breakdowns rose 40%') → Impact ('Delays patient transfers')"
            },
            {
                "icon": "fa-certificate",
                "title": "Golden Rule 2: Cite Authoritative Standards Verbally",
                "desc": "Strengthen credibility by referencing respected professional bodies: HSE guidelines, CQC fundamental standards, NICE clinical guidelines, or company audits.",
                "badge": "Phrasing: 'In accordance with CQC Regulation 12...', 'As published in the 2025 HSE report...'"
            }
        ],
        "skills": [
            {
                "title": "Three Categories of Spoken Evidence",
                "summary": "How to deploy diverse evidence types during discussions and presentations.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>1. Statistical / Quantitative Evidence:</strong> Percentages, financial figures, time metrics. <em>"Adopting LED lighting across our 3 warehouses will reduce annual energy expenditure by £22,000."</em></li>
                    <li><strong>2. Regulatory &amp; Legal Standards:</strong> Statutory codes of practice. <em>"Under the Health and Safety at Work Act 1974, employers must provide adequate training for all manual handling operations."</em></li>
                    <li><strong>3. Concrete Case Studies &amp; Anecdotes:</strong> Specific real-world examples. <em>"When Ward 3 piloted this staggered visiting policy in August, visitor congestion fell by 35% with zero safety incidents."</em></li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Defending a Capital Funding Request for Electric Pallet Trucks",
                "marks": "Full Criteria Level 2 (L2.4)",
                "context": "Warehouse Distribution Logistics",
                "question": "A finance director questions why the depot needs £18,000 for three electric pallet trucks when manual pump trucks cost only £300 each. Deliver an evidenced spoken defense.",
                "steps": [
                    ("Step 1", "State the core claim with ergonomics focus", "'While manual trucks have a lower upfront cost, electric pallet trucks deliver substantial long-term operational and health savings.'", "Clear assertion aligned with business priorities"),
                    ("Step 2", "Introduce statistical and medical evidence", "'According to our HSE accident log, manual handling strain injuries caused 64 lost working days last year, costing the company £9,200 in temporary agency cover.'", "Evidences claim with internal audit records"),
                    ("Step 3", "Project ROI and operational efficiency impact", "'Furthermore, trials showed loading turnaround times dropped from 45 minutes to 22 minutes per lorry. The investment pays for itself within 14 months while protecting staff wellbeing.'", "Proves measurable productivity and financial return")
                ],
                "final_answer": "Compelling spoken defense combining internal safety audit figures, HSE compliance, and measurable loading efficiency gains.",
                "tutor_tip": "Notice how the candidate compared the hidden cost of injury leave (£9,200) against the machine cost, creating a bulletproof business case."
            }
        ],
        "examiner_traps": [
            {
                "title": "Unsubstantiated Sweeping Generalizations",
                "desc": "Saying 'Everyone knows electric trucks are better' or 'It's obvious this will work' earns zero evidence marks.",
                "fix": "Always attach a number, a percentage, a named department, or an official standard to your claim."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "You are presenting an argument for introducing water dispensers on hospital wards for staff hydration. Incorporate one physiological fact and one operational benefit into a 40-word spoken statement.",
                "solution_steps": "Spoken argument: 'Clinical studies by the Royal College of Nursing show that even a 2% drop in hydration impairs cognitive focus by 15%. Providing accessible chilled water stations directly reduces charting errors and combats mid-shift fatigue.'",
                "correct_answer": "Integrates authoritative medical reference (RCN 2% hydration statistic) with operational outcome (charting errors).",
                "tutor_tip": "Citing recognized professional bodies like RCN or HSE immediately validates your points."
            }
        ]
    },
    {
        "filename": "slc-extracting-information.html",
        "clean_topic": "Listening & Extracting Key Information",
        "intro_lead": "Hone advanced active listening strategies: capture essential facts under time pressure, identify underlying speaker bias, and filter critical operational data from conversational filler.",
        "next_file": "slc-language-in-context.html",
        "next_name": "Language in Professional Contexts",
        "spec_points": [
            ("L1.1 / L2.1", "Identify relevant information and lines of argument in explanations or presentations."),
            ("L2.5", "Follow and analyse lines of argument, using listening skills to synthesize spoken information.")
        ],
        "golden_rules": [
            {
                "icon": "fa-pen-to-square",
                "title": "Golden Rule 1: The 2-Column Listening Grid",
                "desc": "When listening to a peer presentation, fold your notes into two columns: 'Key Facts & Figures' on the left, and 'Questions to Ask' on the right.",
                "badge": "Column 1: Data & Policies | Column 2: Follow-up Questions"
            },
            {
                "icon": "fa-ear-deaf",
                "title": "Golden Rule 2: Listen for Verbal Stress Markers",
                "desc": "Speakers naturally emphasize key facts with vocal inflection, slower pacing, or verbal signposts ('Crucially', 'Our main priority is', 'The mandatory date is').",
                "badge": "Listen for: Signposts • Pitch Shifts • Deliberate Pauses"
            }
        ],
        "skills": [
            {
                "title": "Filtering Signal from Noise in Workplace Briefings",
                "summary": "Techniques for extracting actionable directives from lengthy spoken updates.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Spoken Statement Extract</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#64748b;">Contextual Filler (Ignore)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Actionable Key Information (Extract)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Well, as you know the weather's been terrible, but anyway, from November 3rd, all medication trolleys must be double-locked between 13:00 and 14:00."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Weather comments, introductory filler.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Mandatory Rule:</strong> Double-lock medication trolleys between 13:00–14:00, effective Nov 3.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I personally think the new uniforms look rather smart, but the supplier confirmed delivery of size medium is delayed until next Friday."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Personal subjective opinion on appearance.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Operational Constraint:</strong> Size M uniforms delayed until next Friday.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Extracting Action Items from a Senior Sister's Ward Briefing",
                "marks": "Full Criteria Level 2 (L2.1)",
                "context": "NHS Acute Ward Management",
                "question": "Listen to the transcript of the ward manager's 2-minute briefing:<br><em>'Good morning everyone. First, thank you for your hard work over the weekend. A quick reminder that the CQC inspection window opens next Monday, the 17th. Environmental cleaning audits must be uploaded to the portal by 16:00 daily without exception. Also, the pharmacy technician reported that three controlled drug registers had missing countersignatures last Thursday. Anyone administering Schedule 2 drugs must ensure two signatures are logged immediately at the bedside. Finally, the staff barbecue has been rescheduled to July 8th.'</em><br>Extract the two critical clinical compliance directives.",
                "steps": [
                    ("Step 1", "Filter out social notices and pleasantries", "Ignore staff barbecue date and general thank-you remarks; these are non-regulatory pleasantries.", "Filters background noise"),
                    ("Step 2", "Extract Compliance Directive 1", "Upload environmental cleaning audits to the online portal daily by 16:00 (ahead of CQC window opening Nov 17).", "Identifies deadline and specific task"),
                    ("Step 3", "Extract Compliance Directive 2", "Controlled drug (Schedule 2) administrations must be countersigned by two practitioners immediately at the bedside.", "Identifies mandatory patient safety protocol")
                ],
                "final_answer": "Directive 1: Daily environmental cleaning audits uploaded by 16:00 | Directive 2: Mandatory immediate bedside dual countersignatures for Schedule 2 drugs.",
                "tutor_tip": "In listening tests and real workplace briefings, separate social announcements from mandatory regulatory directives."
            }
        ],
        "examiner_traps": [
            {
                "title": "Transcribing Word-for-Word Instead of Synthesizing",
                "desc": "Trying to write down every word causes candidates to miss subsequent information.",
                "fix": "Use shorthand keywords: 'CQC Mon 17', 'Audit upload 16:00', 'CD dual sign bedside'."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "A warehouse supervisor announces: <em>'We've had three near-misses in Loading Bay 4 this morning due to oil spills. All operators must wear high-visibility vests and steel-toecap boots at all times, and Bay 4 is closed for maintenance until 14:00.'</em> Identify the primary safety action and the operational restriction.",
                "solution_steps": "Safety action: Mandatory wearing of hi-vis vests and steel-toecap boots at all times.<br>Operational restriction: Loading Bay 4 is closed for maintenance until 14:00.",
                "correct_answer": "Safety action: Hi-vis & steel toecap boots | Restriction: Bay 4 closed until 14:00.",
                "tutor_tip": "Be exact with times and locations when recording operational restrictions."
            }
        ]
    },
    {
        "filename": "slc-language-in-context.html",
        "clean_topic": "Language in Professional Contexts",
        "intro_lead": "Eliminate casual slang, eliminate crutch words, and communicate with assertive, respectful vocabulary tailored to high-stakes vocational environments.",
        "next_file": "slc-your-turn.html",
        "next_name": "Role-Play, Scenarios & Discussion Practice",
        "spec_points": [
            ("L1.2 / L2.6", "Use appropriate language and register suitable for purpose, subject, and audience."),
            ("L2.3", "Communicate clearly and effectively in a professional working environment.")
        ],
        "golden_rules": [
            {
                "icon": "fa-user-check",
                "title": "Golden Rule 1: Adopt Assertive Communication Over Passive or Aggressive",
                "desc": "Assertive communication is calm, factual, and direct. It respects both your perspective and that of your listener without retreating passively or lashing out aggressively.",
                "badge": "Passive: 'It doesn't matter' | Aggressive: 'You ruined it' | Assertive: 'Here is what occurred'"
            },
            {
                "icon": "fa-trash-can",
                "title": "Golden Rule 2: Purge Casual Fillers from Your Spoken Vocabulary",
                "desc": "Eliminate crutches: 'sort of', 'innit', 'basically', 'like', 'you know what I mean'. Replace them with deliberate silence or measured professional transitions.",
                "badge": "Pause > 'Um' / 'Like' / 'Basically'"
            }
        ],
        "skills": [
            {
                "title": "Transforming Informal Speech into Professional Register",
                "summary": "Practical conversion guide for healthcare and commercial settings.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#dc2626;">Informal / Colloquial Slang</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Professional Functional English</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Vocational Rationale</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I had a chat with the bloke and he was fuming."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"I consulted with the client, who expressed significant dissatisfaction."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Replaces colloquialisms with objective emotional reporting.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The printer's totally knackered again."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The main office printer has malfunctioned and requires maintenance."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Clear, factual equipment status.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We need to sort this mess out ASAP."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We must prioritize resolving this procedural backlog today."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Action-oriented, professional urgency.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Communicating a Treatment Delay to an Anxious Outpatient",
                "marks": "Full Criteria Level 2 (L2.3, L2.6)",
                "context": "NHS Outpatients Clinic Customer Service",
                "question": "A patient in the surgical waiting room has been waiting 90 minutes past their appointment time. Deliver a professional, empathetic spoken communication explaining the delay.",
                "steps": [
                    ("Step 1", "Respectful greeting & acknowledgment of delay", "'Good afternoon Mr Henderson. I apologize that you have been kept waiting past your two o'clock appointment slot.'", "Addresses patient by surname, validates time lost"),
                    ("Step 2", "Factual explanation without clinical breaches", "'Mr Evans, our consultant surgeon, was called into an emergency procedure in Theatre 2. Emergency cases take precedence, but he is completing the procedure now.'", "Transparent explanation preserving patient confidentiality"),
                    ("Step 3", "Realistic updated timeframe & comfort offer", "'He anticipates seeing you at approximately 15:45. In the meantime, can I offer you a glass of water, and would you like me to notify your transport driver?'", "Proactive assistance and practical support")
                ],
                "final_answer": "Communicates clinical delay empathetically and transparently while maintaining professional boundaries and patient comfort.",
                "tutor_tip": "Notice how the speaker didn't over-promise ('He will see you in 2 minutes') but gave a realistic, measured timeframe."
            }
        ],
        "examiner_traps": [
            {
                "title": "Blaming Other Departments or Colleagues",
                "desc": "Saying 'The lab messed up' or 'The night shift was lazy' reflects poorly on your professional standard.",
                "fix": "Frame issues objectively around process and solutions: 'The laboratory encountered an unexpected batch delay, which we are expediting.'"
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "Rewrite the following informal colleague statement into professional standard English suitable for an official clinical handover: <em>'The guy in bed 3 went mad cos his tea was cold.'</em>",
                "solution_steps": "Professional version: 'The patient in Bay 3 expressed frustration regarding the temperature of his hot beverage.'",
                "correct_answer": "Replaces slang ('guy', 'went mad', 'tea') with respectful clinical terminology ('patient in Bay 3', 'expressed frustration', 'hot beverage').",
                "tutor_tip": "Always maintain dignified language when referring to patients or service users."
            }
        ]
    },
    {
        "filename": "slc-your-turn.html",
        "clean_topic": "Discussion Simulations, Scenarios & Practical Drills",
        "intro_lead": "Put Speaking, Listening, and Communicating theory into action through realistic vocational simulation briefs, peer assessment drills, and timed group discussion scenarios.",
        "next_file": "slc-the-exam.html",
        "next_name": "SLC Assessment Strategy & Exam Guide",
        "spec_points": [
            ("L1 & L2 SLC Standards", "Participate effectively in formal presentations and interactive workplace discussions."),
            ("L2.1–L2.7", "Demonstrate all seven Level 2 Speaking and Listening regulatory criteria in realistic simulation tasks.")
        ],
        "golden_rules": [
            {
                "icon": "fa-stopwatch-20",
                "title": "Golden Rule 1: Allocate 5 Minutes to Pre-Discussion Bulleting",
                "desc": "Before the group discussion begins, use your planning time to note 3 distinct points, 1 piece of supporting evidence, and 2 questions you want to ask your peers.",
                "badge": "Pre-flight Checklist: 3 Points • 1 Statistic • 2 Questions"
            },
            {
                "icon": "fa-list-check",
                "title": "Golden Rule 2: Complete the Assessor Checklist in Real Time",
                "desc": "Keep mental track of your contributions: Have I presented evidence? Have I invited a peer? Have I summarized an agreement? Check off all three during the talk.",
                "badge": "Self-Audit: Evidence Given? Peer Invited? Consensus Summarized?"
            }
        ],
        "skills": [
            {
                "title": "Three Regulated Workplace Discussion Simulation Briefs",
                "summary": "Authentic exam-standard simulation scenarios to practice with peers or your tutor.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <div style="display:flex; flex-direction:column; gap:16px;">
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#0369a1; margin-bottom:6px;"><i class="fa-solid fa-hospital"></i> Simulation 1: Healthcare Shift Rota Reorganisation</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Your residential care home is debating switching from three 8-hour shifts to two 12-hour shifts. Consider staff fatigue, handover quality, resident continuity of care, and weekend family visits. Reach a unanimous recommendation in 12 minutes.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#166534; margin-bottom:6px;"><i class="fa-solid fa-truck"></i> Simulation 2: Logistics Depot Environmental Sustainability</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Your delivery hub must reduce cardboard waste and carbon emissions by 20% over the next 12 months. Discuss reusable plastic tote boxes, electric fleet charging schedules, and driver route optimization. Propose an action plan with milestones.</p>
                    </div>
                    <div style="background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:14px;">
                      <h4 style="color:#ea580c; margin-bottom:6px;"><i class="fa-solid fa-graduation-cap"></i> Simulation 3: Apprenticeship Mentorship Programme</h4>
                      <p style="font-size:0.95rem; color:#334155; line-height:1.6;"><strong>Scenario:</strong> Early leaver rates among new apprentices have reached 25%. Discuss establishing a formal 1-to-1 buddy system, allocating protected study time, and conducting bi-weekly progress reviews. Agree on three compulsory implementation steps.</p>
                    </div>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Annotated Group Discussion Transcript (Meeting Simulation 1)",
                "marks": "Distinction Level Performance Benchmark",
                "context": "Residential Care Home Shift Policy Review",
                "question": "Read the transcript extract demonstrating candidate excellence in turn-taking, evidence citation, and consensus building.",
                "steps": [
                    ("Candidate A (Lead)", "'To open our discussion on the proposed 12-hour rota, I've reviewed the staff survey where 60% of care assistants favored 3-day working weeks. However, we must examine resident medication handover safety.'", "Opens discussion, introduces quantitative data, outlines safety theme"),
                    ("Candidate B (Build)", "'Building on Candidate A's point, a study by Skills for Care noted that fatigue peaks during the 11th hour of clinical shifts. Could we incorporate mandatory 30-minute breaks every four hours?'", "Verbal bridge, cites regulatory body, introduces solution"),
                    ("Candidate C (Synthesize)", "'That addresses Candidate A's concern. If we agree on the 12-hour model with guaranteed 4-hour break rotations, can we agree to recommend a 3-month trial on Elm Wing?'", "Synthesizes points, drives group to concrete pilot agreement")
                ],
                "final_answer": "All three candidates hit regulatory criteria: turn-taking, citing external standards, and agreeing on an actionable pilot.",
                "tutor_tip": "Notice how no one argued emotionally; every comment was rooted in staff data, clinical safety, and phased trials."
            }
        ],
        "examiner_traps": [
            {
                "title": "Going Silent Once You Have Made One Point",
                "desc": "Functional Skills criteria require continuous evidence throughout the entire 10–15 minute discussion.",
                "fix": "Aim to make a substantive contribution or ask a probing question every 2 to 3 minutes."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "Select Simulation 2 (Logistics Depot Waste Reduction). Write your opening 35-word contribution outlining your position and introducing a specific operational initiative.",
                "solution_steps": "Contribution: 'Good morning everyone. In examining our depot packaging waste, replacing single-use cardboard with RFID-tracked reusable plastic tote boxes could eliminate 4,000 boxes monthly. Liam, what are the initial capital costs for those containers?'",
                "correct_answer": "States clear stance, cites waste reduction metric, and hands over to a peer with a specific operational question.",
                "tutor_tip": "Ending your opening turn with a direct question ensures smooth turn-taking."
            }
        ]
    },
    {
        "filename": "slc-the-exam.html",
        "clean_topic": "Speaking, Listening & Communicating Exam Strategy & Grading Criteria",
        "intro_lead": "A comprehensive guide to the Pearson Edexcel Functional Skills English SLC assessment: grading rubrics, assessor witness testimonies, exam day rules, and how to pass on your first sitting.",
        "next_file": "functional-skills-english-level-2.html",
        "next_name": "Functional Skills English Level 2 Directory",
        "spec_points": [
            ("L1 / L2 Assessment Regulations", "Pearson Edexcel / City & Guilds Speaking, Listening and Communicating regulated examination requirements."),
            ("Witness Testimony Standards", "Assessor observation records, video recording regulations, and standardisation evidence.")
        ],
        "golden_rules": [
            {
                "icon": "fa-award",
                "title": "Golden Rule 1: Every Criterion Must Be Evidenced",
                "desc": "Unlike Reading and Writing where marks are averaged, in SLC you must achieve a 'Pass' across ALL regulated criteria. Failing a single criterion (such as turn-taking) requires a reassessment.",
                "badge": "All-or-Nothing Mastery: 100% of Criteria Must Be Evidenced"
            },
            {
                "icon": "fa-video",
                "title": "Golden Rule 2: Speak Directly to Your Group, Not the Assessor",
                "desc": "The assessor is a neutral observer taking notes or monitoring the recording. Address your peers, colleagues, and audience directly with natural eye contact.",
                "badge": "Do not look at the examiner; maintain eye contact with your peer group."
            }
        ],
        "skills": [
            {
                "title": "The Assessor Witness Record Deconstructed",
                "summary": "What examiners look for and document on the official Pearson Edexcel witness sheet.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Criteria Code</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Standard Requirement</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Evidence the Assessor Records</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.1</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Identify relevant info and lines of argument</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Candidate took notes and accurately summarized peer's argument regarding ward staffing.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.3</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Communicate ideas clearly and effectively</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Presentation had logical introduction, clear signposts, and articulate conclusion.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.4</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Support arguments with persuasive evidence</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Cited CQC inspection findings and 2025 NHS Staff Survey figures.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.6</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Appropriate language and register</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Consistent formal workplace tone maintained; zero inappropriate slang or filler words.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">L2.7</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Respect turn-taking conventions</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Used verbal bridges, did not interrupt, invited quiet member to speak.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Pre-Exam 10-Minute Preparation Strategy",
                "marks": "Full Exam Readiness Protocol",
                "context": "SLC Exam Day Countdown",
                "question": "How should a candidate utilize the 10 minutes immediately prior to entering the formal assessment room?",
                "steps": [
                    ("Step 1", "Review Cue Cards (Minutes 1–4)", "Scan your 3 presentation cue cards. Check that bullet points are legible and numbers/percentages are highlighted in yellow.", "Locks in presentation signposts"),
                    ("Step 2", "Breathing & Vocal Warm-up (Minutes 5–7)", "Perform three deep diaphragmatic breaths (4 seconds in, 6 seconds out). Hydrate with water to prevent dry mouth.", "Calms nervous system and centers pitch"),
                    ("Step 3", "Connect with Group Peers (Minutes 8–10)", "Introduce yourself warmly to fellow group participants. Confirm names so you can address them naturally by name during discussion.", "Prepares for seamless turn-taking and verbal bridging")
                ],
                "final_answer": "Systematic 10-minute routine addressing mental preparation, physiological vocal control, and interpersonal group rapport.",
                "tutor_tip": "Knowing your group members' names before entering the room gives you an immediate advantage when using verbal bridges."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming Speaking and Listening Doesn't Count",
                "desc": "Some learners put all their energy into Reading and Writing, treating SLC as an afterthought. You cannot receive your Functional Skills certificate without passing SLC.",
                "fix": "Treat your presentation and discussion with the same professional rigor as an NHS or corporate job interview."
            }
        ],
        "practice_questions": [
            {
                "marks": "Pass Benchmark",
                "question": "State the three actions you must complete during the group discussion to ensure criteria L2.7 (respecting turn-taking) is achieved on the assessor's witness sheet.",
                "solution_steps": "1. Allow peers to finish speaking without interrupting.<br>2. Use a verbal bridge that references a peer's point before stating your own.<br>3. Actively invite a quieter participant into the discussion by name with an open question.",
                "correct_answer": "No interrupting, verbal bridging, and inviting a quiet peer by name.",
                "tutor_tip": "Memorize these three actions as your non-negotiable discussion checklist."
            }
        ]
    }
]

all_slc.extend(batch_2)

# Write out to english_slc_topics.py
out_file = "/home/subi/Projects/masterfunctionalskills.co.uk/english_slc_topics.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""\nEnglish Speaking, Listening and Communicating (SLC) Topics (12 Topics)\n')
    f.write('Master Functional Skills Curriculum Suite\n')
    f.write('"""\n\n')
    f.write("SLC_TOPICS = " + repr(all_slc) + "\n")

print(f"Successfully generated english_slc_topics.py with {len(all_slc)} topics!")
