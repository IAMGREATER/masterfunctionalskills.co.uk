#!/usr/bin/env python3
"""
Catalog SLC & Digital Skills: Speaking, Listening & Communicating and Digital Functional Skills.
"""
from build_topic_dataset import make_english_topic, make_digital_topic

CATALOG_SLC_DIGITAL = [
    # 1. Digital Functional Skills Core
    make_digital_topic(
        slug="digital-functional-skills",
        title="Digital Functional Skills Core",
        spec_codes="DFS Entry 3 & Level 1",
        golden_rule="Digital Functional Skills covers 5 core standards: 1. Using devices & handling information, 2. Creating & editing, 3. Communicating, 4. Transacting, 5. Being safe and responsible online. Always verify file formats, check spreadsheet formula syntax, and identify phishing red flags.",
        q1={
            "title": "Question 1 (Core File Management & Storage)",
            "marks": 2,
            "stem": "An administrative apprentice saves a confidential patient training roster.<br>1. Which file format is most appropriate for a document intended for read-only distribution that cannot be accidentally edited: <strong>.docx, .pdf, or .txt</strong>?<br>2. Give one security reason why storing confidential staff records on an unencrypted USB stick breaches workplace data protection policies.",
            "lines": 3,
            "ans_label": "Format & Security Reason =",
            "choice_box": "Format: ________________ | Reason: ________________",
            "step_rows": [
                ("1. Identify correct format: .pdf (Portable Document Format preserves formatting and prevents accidental alteration)", "[A1]"),
                ("2. State security risk: USB sticks can be easily lost, stolen, or accessed without password protection/encryption, causing GDPR breach", "[A1]")
            ],
            "final_answer": "Format: .pdf; Security Risk: Physical loss/theft leads to unauthorized data access and GDPR violation.",
            "pitfall": "Selecting .docx which allows anyone to alter records.",
            "reverse_check": ".pdf is standard for immutable read-only records."
        },
        q2={
            "title": "Question 2 (Spreadsheet Formula Syntax)",
            "marks": 2,
            "stem": "Look at the spreadsheet excerpt below showing staff training hours:<br>• Cells B2 to B15 contain the hours completed by 14 healthcare assistants.<br><br>Write down the exact spreadsheet formula to calculate:<br>1. The total hours completed by all 14 assistants.<br>2. The average hours completed per assistant.",
            "lines": 3,
            "ans_label": "Formulas =",
            "choice_box": "1 (Total): =________________ | 2 (Average): =________________",
            "step_rows": [
                ("1. Total formula: =SUM(B2:B15)", "[A1]"),
                ("2. Average formula: =AVERAGE(B2:B15)", "[A1]")
            ],
            "final_answer": "1. =SUM(B2:B15);  2. =AVERAGE(B2:B15)",
            "pitfall": "Omitting the '=' sign or writing =TOTAL() or =AVG() instead of =AVERAGE().",
            "reverse_check": "=SUM sums range; =AVERAGE computes arithmetic mean."
        },
        q3={
            "title": "Question 3 (Phishing Email Forensics & Red Flags)",
            "marks": 3,
            "stem": "A clinic receptionist receives an email with the subject: <em>'URGENT: Your NHS Email Account Will Be Terminated in 2 Hours - Verify Password Now'</em>.<br>The sender address is: <code>support@nhs-security-update.co.uk</code>.<br>The email instructs: <em>'Click here immediately and enter your login password to maintain access.'</em><br><br>Identify <strong>three distinct red flags</strong> proving this is a phishing scam.",
            "lines": 4,
            "ans_label": "Three Red Flags =",
            "choice_box": "1: ________________ | 2: ________________ | 3: ________________",
            "step_rows": [
                ("1. Red flag 1: Artificial sense of urgency / panic-inducing deadline ('within 2 hours / account terminated')", "[A1]"),
                ("2. Red flag 2: Suspicious sender domain (<code>@nhs-security-update.co.uk</code> instead of official <code>@nhs.net</code> or <code>@nhs.uk</code>)", "[A1]"),
                ("3. Red flag 3: Unsolicited request for password entry via an unverified hyperlink", "[A1]")
            ],
            "final_answer": "1. Panic/urgency deadline; 2. Fake sender domain (.co.uk instead of .net); 3. Direct request to enter password via link.",
            "pitfall": "Only mentioning that it's an email without highlighting domain or deadline tactics.",
            "reverse_check": "Legitimate IT never asks users to click a link to verify passwords within 2 hours."
        },
        q4={
            "title": "Question 4 (Level 1 Spreadsheet Data Analysis & Sorting)",
            "marks": 3,
            "stem": "An inventory clerk tracks PPE deliveries in Excel. Column A contains Delivery Date (DD/MM/YYYY), Column B contains Supplier Name, Column C contains Quantity, and Column D contains Unit Cost.<br>The clerk wants to find the <strong>largest delivery</strong> received during October.<br><br>Describe the exact digital steps to sort the spreadsheet to display the largest delivery quantity at the very top.",
            "lines": 4,
            "ans_label": "Digital Steps =",
            "choice_box": "Step 1: ____________ | Step 2: ____________ | Step 3: ____________",
            "step_rows": [
                ("1. Select the data table range including header row (A1:D50)", "[P1]"),
                ("2. Navigate to 'Data' tab and select 'Sort' (or Sort & Filter)", "[P1]"),
                ("3. Sort by 'Quantity' (Column C), order from 'Largest to Smallest' (Descending)", "[A1]")
            ],
            "final_answer": "Select table, go to Data > Sort, sort by Column C (Quantity) in Descending order (Largest to Smallest).",
            "pitfall": "Sorting Ascending (which puts the smallest at the top) or sorting Column C without selecting the other columns (corrupting data rows).",
            "reverse_check": "Descending sort order places maximum values in the first row."
        },
        q5={
            "title": "Question 5 (Cybersecurity & Multi-Factor Authentication)",
            "marks": 4,
            "stem": "A community healthcare provider introduces mandatory Multi-Factor Authentication (MFA) for all remote staff logging into patient records.<br>1. Explain what Multi-Factor Authentication (MFA) means using the concepts of <em>'something you know'</em> and <em>'something you have'</em>.<br>2. Give a specific example of each factor.<br>3. Explain why MFA protects patient data even if a cybercriminal successfully steals an employee's password.",
            "lines": 5,
            "ans_label": "MFA Explanation & Protection =",
            "choice_box": "Definition: ________________ | Protection: ________________",
            "step_rows": [
                ("1. Definition: MFA requires two or more independent authentication factors before granting system access", "[P1]"),
                ("2. Examples: 'Something you know' = Password / PIN; 'Something you have' = Authenticator app on registered smartphone / physical security token / SMS OTP", "[M1]"),
                ("3. Protection: If password is compromised, the attacker cannot log in because they do not possess the secondary physical device/token to generate the one-time code", "[A1]"),
                ("4. Clear, technically precise summary with zero ambiguity", "[A1]")
            ],
            "final_answer": "MFA requires 2+ credentials. Password ('something you know') + Mobile token ('something you have'). Even with stolen password, attacker lacks the second factor.",
            "pitfall": "Describing MFA as simply 'entering two different passwords'.",
            "reverse_check": "Two distinct authentication categories: knowledge + possession."
        },
        q6={
            "title": "Question 6 (Cloud Sharing Permission Audit Justification)",
            "marks": 4,
            "stem": "An office apprentice uploads an internal audit spreadsheet containing staff home addresses and National Insurance numbers to Microsoft OneDrive.<br>The apprentice generates a sharing link with the permission set to: <em>'Anyone with the link can view'</em> and posts the link in a company-wide Microsoft Teams public channel.<br><br>The data protection officer flags a critical security breach.<br>Explain why this sharing setting breaches GDPR, state which permission setting should have been used instead, and describe two immediate actions required to contain the data leak.",
            "lines": 5,
            "ans_label": "GDPR Breach & Remediation =",
            "choice_box": "Breach reason: ________________ | Remediation: ________________",
            "step_rows": [
                ("1. Explain breach: 'Anyone with the link' allows public, unauthenticated access; anyone can forward the link externally without logging in, exposing sensitive personal data (GDPR violation)", "[M1]"),
                ("2. Correct permission: Should be restricted to 'Specific people' (named auditors only) with authenticated login required", "[P1]"),
                ("3. Containment Action 1: Delete or revoke the sharing link immediately in OneDrive to terminate external access", "[P1]"),
                ("4. Containment Action 2: Remove the post from the Teams channel and report the incident to the Information Governance Lead / Data Protection Officer", "[A1]")
            ],
            "final_answer": "Breach: Unrestricted public access to sensitive PII. Correct setting: 'Specific people'. Containment: Revoke sharing link immediately and report incident to DPO.",
            "pitfall": "Suggesting changing permission to 'Can edit' or assuming password-protected intranet prevents forwarding.",
            "reverse_check": "'Anyone with the link' bypasses organizational authentication controls."
        }
    ),
    # 2. Speaking, Listening & Communicating (SLC)
    make_english_topic(
        slug="slc-key-slc-skills",
        title="Key SLC Skills & Discussion Strategies",
        category="slc",
        spec_codes="Pearson Edexcel: SLC Level 1 & Level 2",
        golden_rule="In Functional Skills SLC, candidates must demonstrate effective verbal communication: 1. Making clear, relevant contributions, 2. Listening attentively and building on others' points, 3. Asking clarifying open questions, 4. Adapting language for formal settings, 5. Reaching collaborative conclusions.",
        q1={
            "title": "Question 1 (Open vs Closed Questions in Consultation)",
            "marks": 2,
            "stem": "In a clinical feedback meeting, a supervisor wants to understand why staff feel rushed during morning handovers.<br>1. Convert this closed question into an open question: <em>'Do you find the morning handover too short?'</em><br>2. Explain why open questions are more effective in workplace discussions.",
            "lines": 3,
            "ans_label": "Open Question & Explanation =",
            "choice_box": "Open question: ________________ | Explanation: ________________",
            "step_rows": [
                ("1. Convert to open: 'How could we improve the morning handover process?' OR 'What factors make the morning handover feel rushed?'", "[A1]"),
                ("2. Explanation: Open questions prompt detailed, reflective answers and constructive insights, whereas closed questions limit responses to a single word ('yes'/'no')", "[A1]")
            ],
            "final_answer": "Open: 'What challenges do you experience during morning handover?'; Explanation: Prompts qualitative insight rather than a yes/no answer.",
            "pitfall": "Rewriting as another closed question (e.g. 'Is the handover 15 minutes long?').",
            "reverse_check": "Open questions begin with How, What, Why; closed questions prompt Yes/No."
        },
        q2={
            "title": "Question 2 (Active Listening & Non-Verbal Communication)",
            "marks": 2,
            "stem": "During a formal committee discussion, describe <strong>two positive non-verbal cues</strong> that demonstrate active listening without interrupting the speaker.",
            "lines": 3,
            "ans_label": "Two Non-Verbal Cues =",
            "choice_box": "Cue 1: ________________ | Cue 2: ________________",
            "step_rows": [
                ("1. Cue 1: Maintaining steady, respectful eye contact and nodding to signal comprehension", "[A1]"),
                ("2. Cue 2: Leaning slightly forward with open posture (arms uncrossed) and taking brief notes", "[A1]")
            ],
            "final_answer": "1. Eye contact and nodding; 2. Open posture and taking relevant notes.",
            "pitfall": "Describing verbal interruptions like saying 'I agree' repeatedly.",
            "reverse_check": "Both cues show engagement through body language without speaking."
        },
        q3={
            "title": "Question 3 (Constructive Disagreement in a Team Meeting)",
            "marks": 3,
            "stem": "A colleague proposes: <em>'We should cancel all staff training days this quarter to cover sick leave.'</em><br>You strongly disagree with this proposal.<br><br>Write down a professional, diplomatic response that expresses disagreement respectfully while suggesting an alternative solution.",
            "lines": 4,
            "ans_label": "Diplomatic Response =",
            "choice_box": "Write your response in the workspace provided.",
            "step_rows": [
                ("1. Acknowledge colleague's concern courteously ('I understand we are under acute staffing pressure...')", "[P1]"),
                ("2. State disagreement professionally without personal attack ('However, cancelling training will harm long-term compliance and staff retention...')", "[M1]"),
                ("3. Propose constructive alternative ('Could we instead look at short modular e-learning sessions or staggered bank staff cover?')", "[A1]")
            ],
            "final_answer": "Model: 'I understand staffing levels are critical right now; however, cancelling mandatory training could compromise patient safety and compliance. Could we instead deliver the training in shorter, 30-minute modules or utilize bank staff to cover key hours?'",
            "pitfall": "Aggressive language ('That is a terrible idea and will never work').",
            "reverse_check": "Acknowledges concern + provides evidence-based objection + offers alternative."
        },
        q4={
            "title": "Question 4 (Adapting Register for Varied Audiences)",
            "marks": 3,
            "stem": "An apprentice healthcare assistant explains infection control procedures to two different audiences:<br>• Audience A: A team of consultant surgeons and clinical leads.<br>• Audience B: An anxious elderly patient and their family.<br><br>Describe how your vocabulary, sentence structure, and tone must adapt between Audience A and Audience B.",
            "lines": 4,
            "ans_label": "Adaptation Analysis =",
            "choice_box": "Audience A: ________________ | Audience B: ________________",
            "step_rows": [
                ("1. Audience A: Formal clinical register, specialist medical terminology (aseptic technique, pathogen transmission), concise evidence-based data", "[M1]"),
                ("2. Audience B: Warm, empathetic, accessible plain English; avoiding frightening jargon; checking for understanding with reassuring body language", "[M1]"),
                ("3. Contrast clearly articulated", "[A1]")
            ],
            "final_answer": "Audience A uses formal clinical terminology and data; Audience B uses compassionate plain English, reassuring tone, and checks for comfort.",
            "pitfall": "Using patronizing or overly simplistic language with professionals, or jargon-heavy terms with patients.",
            "reverse_check": "Adapts complexity and empathy to match audience needs."
        },
        q5={
            "title": "Question 5 (Synthesizing Arguments to Reach Consensus)",
            "marks": 4,
            "stem": "In a 15-minute group discussion, four team members debate whether to introduce 12-hour shifts or keep 8-hour shifts.<br>• Member A argues 12-hour shifts give more consecutive days off.<br>• Member B argues 12-hour shifts cause extreme clinical fatigue in the final 3 hours.<br>• Member C worries about childcare pickup times.<br><br>As meeting facilitator, write down a concluding summary statement that synthesizes all three viewpoints and proposes a collaborative compromise.",
            "lines": 5,
            "ans_label": "Facilitator Synthesis Statement =",
            "choice_box": "Write your synthesis statement in the workspace.",
            "step_rows": [
                ("1. Summarize key advantages highlighted (consecutive rest days from Member A)", "[P1]"),
                ("2. Acknowledge safety and wellbeing risks (fatigue from Member B, childcare from Member C)", "[P1]"),
                ("3. Propose concrete compromise / trial period (e.g. 3-month pilot of hybrid rota with fatigue audits and flexible start options)", "[M1]"),
                ("4. Invite consensus confirmation from all participants", "[A1]")
            ],
            "final_answer": "Model: 'We have heard compelling points today: while 12-hour shifts provide valuable consecutive rest days, we cannot ignore the valid concerns regarding end-of-shift clinical fatigue and childcare logistics. Would the team agree to a 3-month pilot allowing staff to choose between 8-hour and 12-hour schedules, backed by monthly fatigue reviews?'",
            "pitfall": "Picking one side and ignoring the other participants' contributions.",
            "reverse_check": "Incorporates all 3 participants' points into a fair collaborative solution."
        },
        q6={
            "title": "Question 6 (SLC Assessment Criteria & Self-Evaluation)",
            "marks": 4,
            "stem": "An apprentice prepares for their Pearson Edexcel Level 2 SLC formal presentation on <em>'Improving Environmental Sustainability in Health Clinics'</em>.<br>Review the four Pearson Edexcel SLC grading criteria below:<br>1. Structure & Logical Sequencing<br>2. Language Register & Vocabulary<br>3. Effective Use of Presentation Aids<br>4. Handling Audience Questions<br><br>Describe one specific action the apprentice must take during their preparation or delivery to achieve top marks in each of the four criteria.",
            "lines": 5,
            "ans_label": "Four Actions for Top Marks =",
            "choice_box": "1: ________ | 2: ________ | 3: ________ | 4: ________",
            "step_rows": [
                ("1. Structure: Use clear signposting (introduction with agenda, 3 logical subtopics, concise conclusion with call to action)", "[A1]"),
                ("2. Register: Maintain formal professional vocabulary, clear diction, and appropriate pace without slang", "[A1]"),
                ("3. Visual Aids: Use clean, uncluttered visual slides or handouts with relevant charts/statistics, referencing them directly during speech", "[A1]"),
                ("4. Questions: Listen attentively to audience questions, thank the questioner, clarify if needed, and provide evidence-backed answers", "[A1]")
            ],
            "final_answer": "1. Clear signposting; 2. Formal professional diction; 3. Well-referenced visual charts; 4. Active listening and evidence-based Q&A replies.",
            "pitfall": "Vague answers like 'do well' or 'speak loudly'.",
            "reverse_check": "Directly maps to the official Pearson Edexcel SLC Level 2 assessment grid."
        }
    )
]

print(f"Loaded {len(CATALOG_SLC_DIGITAL)} topics in catalog_slc_digital.py")
