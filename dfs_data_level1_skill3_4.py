# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Level 1 Digital Skills (Skill Areas 3 & 4)
Author: Abdul (MFS Pedagogical Systems)
"""

LEVEL_1_SKILL_3_4 = [
    # -------------------------------------------------------------------------
    # Skill Area 3: Communicating
    # -------------------------------------------------------------------------
    {
        "slug": "l1-workplace-email-etiquette",
        "code": "L1.3.1",
        "skill_area": "3. Communicating",
        "title": "Professional Workplace Email, CC and BCC",
        "time": "15 Mins",
        "lead": "Master corporate email communication: understand the vital distinction between To, CC (Carbon Copy), and BCC (Blind Carbon Copy), set high importance flags, create automated email signatures, and maintain UK GDPR compliance.",
        "objectives": [
            "Use To, CC (Carbon Copy), and BCC (Blind Carbon Copy) appropriately",
            "Explain the privacy and UK GDPR benefits of using BCC for group emails",
            "Set High Importance flags and configure automated workplace email signatures"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Workplace Email CC vs BCC",
        "steps": [
            {
                "title": "Understanding To, CC, and BCC",
                "body": "<p>In professional environments, using the wrong recipient field can result in serious data breaches:</p><ul><li><strong>To:</strong> The primary recipients who need to read the email and <strong>take action</strong>.</li><li><strong>CC (Carbon Copy):</strong> Secondary recipients who are kept <strong>informed for visibility</strong> (e.g. keeping your supervisor in the loop). Everyone can see who is in the CC list.</li><li><strong>BCC (Blind Carbon Copy):</strong> Recipients whose email addresses are <strong>hidden from everyone else</strong> on the email. None of the recipients can see who is on the BCC list!</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "UK GDPR & Privacy Alert",
                    "text": "When sending an email to a large group of external patients, clients, or customers, you <strong>MUST put them in BCC</strong>! Putting external contacts in 'To' or 'CC' exposes their private email addresses to strangers, causing a major GDPR data breach."
                }
            },
            {
                "title": "Setting Importance Flags and Automated Signatures",
                "body": "<p>To manage professional correspondence:</p><ul><li><strong>High Importance Flag (<i class='fa-solid fa-exclamation' style='color:#dc2626;'></i>):</strong> Marks urgent, time-sensitive emails with a red exclamation point in the recipient's inbox. Use sparingly!</li><li><strong>Email Signatures:</strong> Configure an automated sign-off in <em>Settings &gt; Signatures</em> containing your Full Name, Job Role, Department, and Contact Number. This guarantees professional consistency across all communications.</li></ul>",
                "ui_sim": {
                    "title": "Workplace Email Recipient Fields & High Importance",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='margin-bottom:6px;'><strong>To:</strong> <span style='background:#e0f2fe; padding:2px 8px; border-radius:12px; color:#0369a1;'>david.miller@clinic.org</span></div><div style='margin-bottom:6px;'><strong>CC:</strong> <span style='background:#f1f5f9; padding:2px 8px; border-radius:12px; color:#475569;'>team_manager@clinic.org</span></div><div style='margin-bottom:6px;'><strong>BCC:</strong> <span style='background:#fef3c7; padding:2px 8px; border-radius:12px; color:#92400e;'><i class='fa-solid fa-eye-slash'></i> patient_group_50_recipients</span></div><div style='display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:6px;'><span><strong>Subject:</strong> Clinic Update Notice</span><span style='background:#fee2e2; color:#dc2626; padding:2px 8px; border-radius:4px; font-weight:700;'><i class='fa-solid fa-exclamation'></i> High Importance</span></div></div>"
                }
            },
            {
                "title": "Professional Tone & Netiquette",
                "body": "<p>Always maintain a courteous tone: avoid text-speak (e.g. 'u', 'thx'), do not type in ALL CAPS, and proofread carefully before hitting Send.</p>"
            }
        ],
        "exam_model": {
            "scenario": "A medical centre administrator is emailing 80 patients to notify them of flu vaccination slots. Explain which email field (To, CC, or BCC) the administrator must use for the patients' email addresses, and explain why this is necessary under data protection law.",
            "steps": [
                {
                    "action": "Identify recipient field",
                    "solution": "BCC (Blind Carbon Copy)",
                    "mark": "[B1]",
                    "rationale": "Correct recipient field for mass public mailings."
                },
                {
                    "action": "Explain data protection justification",
                    "solution": "BCC conceals all recipients' email addresses from one another, preventing a breach of personal privacy and complying with UK GDPR.",
                    "mark": "[B1]",
                    "rationale": "Demonstrates understanding of personal data privacy."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever an email is sent to multiple external clients or customers, the answer is ALWAYS 'BCC to protect personal data and privacy'."
        },
        "drills": [
            {
                "question": "What is the key difference between CC and BCC when addressing an email?",
                "options": [
                    {"text": "Recipients in CC are visible to everyone; recipients in BCC are hidden and private", "correct": True},
                    {"text": "BCC emails take three days to deliver", "correct": False},
                    {"text": "CC deletes the email after reading", "correct": False},
                    {"text": "BCC only works on Apple computers", "correct": False}
                ],
                "explanation": "BCC conceals recipient email addresses from all other people receiving the email."
            },
            {
                "question": "Why should you use the 'High Importance' flag sparingly on workplace emails?",
                "options": [
                    {"text": "If you mark every routine email as high importance, colleagues will ignore the flag when a genuine emergency arises", "correct": True},
                    {"text": "It costs £5 per email to send high importance messages", "correct": False},
                    {"text": "It prevents recipients from opening attachments", "correct": False},
                    {"text": "It automatically forwards the email to the police", "correct": False}
                ],
                "explanation": "Overusing priority flags causes fatigue and reduces responsiveness to real emergencies."
            },
            {
                "question": "What information should typically be included in an automated professional email signature?",
                "options": [
                    {"text": "Full Name, Job Title, Department, Organisation Name, and Workplace Contact Details", "correct": True},
                    {"text": "Your personal bank account PIN and home address", "correct": False},
                    {"text": "Your favourite video game high scores", "correct": False},
                    {"text": "A list of all your passwords", "correct": False}
                ],
                "explanation": "A professional signature provides essential workplace contact identity details."
            }
        ],
        "practice": {
            "task": "A department manager asks you to email a project briefing to team member 'Alex', copy in supervisor 'Chloe' for monitoring, and send a hidden copy to external consultant 'Farhan'. State where each person's email address should be placed in the email header.",
            "scaffold_starter": "Alex: \nChloe: \nFarhan: ",
            "model_answer": "Alex: 'To' field (primary action recipient).\nChloe: 'CC' field (Carbon Copy for monitoring).\nFarhan: 'BCC' field (Blind Carbon Copy to keep his address private).",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Placing Alex in 'To' and Chloe in 'CC'."},
                {"tag": "[1 Mark]", "desc": "Placing Farhan in 'BCC'."}
            ]
        },
        "revision_links": [
            {"label": "Calendar & Meeting Scheduling", "href": "l1-calendar-meeting-scheduling.html"},
            {"label": "Collaborative Cloud Sharing", "href": "l1-collaborative-tools-cloud-sharing.html"},
            {"label": "UK GDPR & Data Protection", "href": "l1-uk-gdpr-data-protection-privacy.html"}
        ]
    },
    {
        "slug": "l1-calendar-meeting-scheduling",
        "code": "L1.3.2",
        "skill_area": "3. Communicating",
        "title": "Calendar Management and Meeting Scheduling",
        "time": "15 Mins",
        "lead": "Organise schedules and collaborative events using digital calendars like Outlook and Google Calendar: create new calendar appointments, invite attendees, set recurring events, configure reminders, and manage RSVPs.",
        "objectives": [
            "Create calendar events with date, start/end time, and location (physical or virtual)",
            "Invite colleagues to meetings and track accepted/declined responses",
            "Configure recurring appointments and automated advance reminders"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Calendar Invites & Scheduling",
        "steps": [
            {
                "title": "Creating a Calendar Event / Meeting",
                "body": "<p>A digital calendar replaces wall planners and paper diaries, synchronising across your computer, phone, and tablet:</p><ol><li>Open your Calendar app and click <strong>New Event</strong> (or double-click the required time slot).</li><li><strong>Title:</strong> Give it a specific, clear name (e.g. <em>'Quarterly Health &amp; Safety Review'</em>).</li><li><strong>Date &amp; Time:</strong> Set the exact date, start time, and duration (e.g. 10:00 - 11:00 AM).</li><li><strong>Location:</strong> Enter the physical room (e.g. <em>'Room 2B'</em>) or toggle <strong>Teams / Online Meeting</strong> to generate a virtual video link automatically.</li></ol>",
                "shortcuts": [
                    {"label": "New Appointment", "key": "Ctrl + Shift + A"},
                    {"label": "New Meeting Request", "key": "Ctrl + Shift + Q"}
                ]
            },
            {
                "title": "Inviting Attendees and Tracking Responses",
                "body": "<p>Type colleagues' names or email addresses into the <strong>Required Attendees</strong> box:</p><ul><li>When you click <strong>Send</strong>, an invitation is delivered to their inbox.</li><li>Attendees can click <strong>Accept</strong> (adds event to their calendar), <strong>Tentative</strong>, or <strong>Decline</strong>.</li><li>The meeting organiser can open the event anytime to view the <strong>Tracking tab</strong> to see who is attending.</li></ul>",
                "ui_sim": {
                    "title": "Calendar Meeting Invite Window",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; padding:12px; border-radius:4px; font-size:0.85rem;'><div style='margin-bottom:6px;'><strong>Title:</strong> Clinical Governance Meeting</div><div style='margin-bottom:6px;'><strong>Attendees:</strong> <span style='background:#e0f2fe; padding:2px 8px; border-radius:12px;'>dr.patel@clinic.org</span>, <span style='background:#e0f2fe; padding:2px 8px; border-radius:12px;'>nurse.sarah@clinic.org</span></div><div style='display:flex; gap:16px; margin-bottom:6px; color:#475569;'><span><i class='fa-regular fa-calendar'></i> 24 Nov 2026</span><span><i class='fa-regular fa-clock'></i> 14:00 - 15:30</span></div><div style='display:flex; justify-content:space-between; align-items:center; border-top:1px solid #e2e8f0; padding-top:8px;'><span><i class='fa-solid fa-bell' style='color:#f59e0b;'></i> Reminder: 15 minutes before</span><button style='background:#0284c7; color:#ffffff; border:none; padding:4px 14px; border-radius:4px; font-weight:700;'>Send Invite</button></div></div>"
                }
            },
            {
                "title": "Recurring Events and Reminders",
                "body": "<p>For ongoing tasks:</p><ul><li><strong>Recurrence:</strong> Set events to repeat <strong>Weekly</strong> (e.g. team catch-up every Monday), <strong>Monthly</strong>, or <strong>Annually</strong>.</li><li><strong>Reminders:</strong> Set an alert pop-up (e.g. 15 minutes or 1 day before) so you and your attendees never miss a deadline.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A clinic manager needs to arrange a monthly staff training session that occurs on the first Monday of every month from 09:00 to 10:30 in Conference Room A. Explain three settings the manager must configure when creating this calendar appointment.",
            "steps": [
                {
                    "action": "Set Recurrence",
                    "solution": "Set the recurrence pattern to 'Monthly on the first Monday'.",
                    "mark": "[B1]",
                    "rationale": "Automates repeat scheduling across future months."
                },
                {
                    "action": "Set Duration & Location",
                    "solution": "Set start time to 09:00, end time to 10:30, and location to 'Conference Room A'.",
                    "mark": "[B1]",
                    "rationale": "Specifies time boundaries and venue."
                },
                {
                    "action": "Add Attendees & Reminder",
                    "solution": "Add staff email addresses to Required Attendees and set a 15-minute advance reminder alert.",
                    "mark": "[B1]",
                    "rationale": "Dispatches invitations and ensures automated notification."
                }
            ],
            "tutor_rule": "In Level 1 exams, calendar questions check: Date/Time, Location, Recurrence, and Reminders."
        },
        "drills": [
            {
                "question": "What feature should you use when scheduling a team meeting that takes place every single Wednesday morning?",
                "options": [
                    {"text": "Set the event Recurrence to Weekly", "correct": True},
                    {"text": "Create 52 separate appointments one by one", "correct": False},
                    {"text": "Send a text message every Tuesday midnight", "correct": False},
                    {"text": "Delete your calendar", "correct": False}
                ],
                "explanation": "Setting recurrence to weekly repeats the event automatically across the calendar."
            },
            {
                "question": "What happens when an invited attendee clicks 'Accept' on an email meeting invitation?",
                "options": [
                    {"text": "The event is automatically added to their digital calendar and an acceptance notice is sent to the organiser", "correct": True},
                    {"text": "Their computer restarts immediately", "correct": False},
                    {"text": "The meeting is cancelled for everyone", "correct": False},
                    {"text": "The email is moved into the Spam folder", "correct": False}
                ],
                "explanation": "Accepting synchronises the appointment into the attendee's personal calendar."
            },
            {
                "question": "Why is it helpful to set a calendar reminder 15 minutes before an appointment?",
                "options": [
                    {"text": "It provides a visual or audible notification so you can wrap up current work and prepare for the meeting", "correct": True},
                    {"text": "It prints the meeting minutes automatically", "correct": False},
                    {"text": "It locks the meeting room door", "correct": False},
                    {"text": "It mutes your phone forever", "correct": False}
                ],
                "explanation": "Reminders alert participants in advance so they can arrive punctually."
            }
        ],
        "practice": {
            "task": "You are scheduling an emergency team briefing for tomorrow at 11:30 AM via Microsoft Teams. State four pieces of information you must enter into the digital calendar meeting form.",
            "scaffold_starter": "1. Title: \n2. Time: \n3. Platform/Location: \n4. People: ",
            "model_answer": "1. Title: Emergency Team Briefing.\n2. Date and Time: Tomorrow's date, 11:30 AM to 12:00 PM.\n3. Location / Channel: Online Microsoft Teams Meeting (link generated).\n4. Attendees: Email addresses of all required team members, with an alert reminder set for 15 minutes prior.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Clear title, correct date, and start/end time."},
                {"tag": "[1 Mark]", "desc": "Virtual location (Teams) and attendee email addresses with reminder."}
            ]
        },
        "revision_links": [
            {"label": "Workplace Email Etiquette", "href": "l1-workplace-email-etiquette.html"},
            {"label": "Collaborative Cloud Sharing", "href": "l1-collaborative-tools-cloud-sharing.html"},
            {"label": "Online Support & Portals", "href": "l1-portal-uploads-customer-support.html"}
        ]
    },
    {
        "slug": "l1-collaborative-tools-cloud-sharing",
        "code": "L1.3.3",
        "skill_area": "3. Communicating",
        "title": "Cloud Sharing, Permissions and Collaboration",
        "time": "15 Mins",
        "lead": "Collaborate in real time on shared cloud documents (Word Online, Google Docs, SharePoint): set sharing permissions (View Only vs Can Edit), track revision changes, add comments, and tag colleagues.",
        "objectives": [
            "Share cloud documents via secure email links with specific permissions (View vs Edit)",
            "Collaborate simultaneously on documents with multiple authors (co-authoring)",
            "Insert, reply to, and resolve comments and track document revisions"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Cloud Sharing & Co-Authoring",
        "steps": [
            {
                "title": "Sharing Links & Setting Access Permissions",
                "body": "<p>Instead of emailing large document attachments back and forth (which results in five conflicting versions), share a single live cloud document:</p><ol><li>Click the blue <strong>Share</strong> button in the top right corner.</li><li>Choose access permissions:<ul><li><strong>Can Edit:</strong> The recipient can type, format, delete, and add content. Use for active co-workers.</li><li><strong>Can View (View Only):</strong> The recipient can read and download the file, but <strong>cannot make any edits</strong>. Ideal for final drafts or external clients.</li></ul></li><li>Enter their specific email address and click <strong>Send</strong>.</li></ol>",
                "ui_sim": {
                    "title": "Cloud Share Permissions Dialogue",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; padding:12px; border-radius:4px; font-size:0.85rem;'><div style='font-weight:700; color:#0f172a; margin-bottom:8px;'><i class='fa-solid fa-share-nodes' style='color:#0284c7;'></i> Share 'Annual_Audit_2026.docx'</div><input type='text' value='nurse_supervisor@clinic.org' style='width:95%; padding:4px 8px; border:1px solid #94a3b8; border-radius:4px; margin-bottom:8px;'><div style='display:flex; justify-content:space-between; align-items:center;'><select style='padding:4px 8px; border:1px solid #94a3b8; border-radius:4px;'><option>Can edit</option><option selected>Can view (Read-only)</option></select><button style='background:#0284c7; color:#ffffff; border:none; padding:6px 14px; border-radius:4px; font-weight:700;'>Send Link</button></div></div>"
                }
            },
            {
                "title": "Real-Time Co-Authoring",
                "body": "<p>When multiple people open the same cloud document, you can see their initials or avatar in the top ribbon:</p><ul><li>A coloured cursor shows where your colleague is currently typing.</li><li>Changes save automatically in real time without conflicting copies.</li></ul>"
            },
            {
                "title": "Using Comments and Resolving Feedback",
                "body": "<p>To give feedback without changing the author's words:</p><ol><li>Highlight the sentence and click <strong>New Comment</strong> (<kbd class='dfs-kbd'>Ctrl + Alt + M</kbd>).</li><li>Type your question or suggestion (e.g. <em>'@Sarah please verify these medication numbers'</em>).</li><li>Once the feedback is addressed, click <strong>Resolve</strong>. The comment thread is tucked away neatly without cluttering the page.</li></ol>"
            }
        ],
        "exam_model": {
            "scenario": "A training coordinator writes an exam timetable and wants a colleague to proofread it. The coordinator wants the colleague to read the timetable and suggest notes without having permission to accidentally delete or change any exam dates. Explain how the coordinator should configure the sharing permissions.",
            "steps": [
                {
                    "action": "Set sharing permission",
                    "solution": "Set the link permission to 'Can View' (or 'View Only' / 'Review Only').",
                    "mark": "[B1]",
                    "rationale": "Prevents unauthorized or accidental direct modification of document text."
                },
                {
                    "action": "Explain feedback mechanism",
                    "solution": "Allow the colleague to use the 'Comments' tool to suggest revisions.",
                    "mark": "[B1]",
                    "rationale": "Enables constructive feedback while preserving source document integrity."
                }
            ],
            "tutor_rule": "In Level 1 exams, always distinguish between 'Can Edit' and 'Can View (View Only)'. View Only is the answer whenever accidental changes must be prevented."
        },
        "drills": [
            {
                "question": "Which sharing permission should you choose when sending a report to an external inspector so they can read it but cannot alter any text?",
                "options": [
                    {"text": "View Only (Can View)", "correct": True},
                    {"text": "Full Admin Access", "correct": False},
                    {"text": "Can Edit", "correct": False},
                    {"text": "Owner", "correct": False}
                ],
                "explanation": "View Only allows reading and downloading without permitting edits to text or formatting."
            },
            {
                "question": "What is the primary benefit of co-authoring a cloud document compared to emailing document attachments?",
                "options": [
                    {"text": "Everyone works on a single live document in real time, avoiding multiple confusing versions", "correct": True},
                    {"text": "It turns the document into a YouTube video", "correct": False},
                    {"text": "It automatically prints out 100 copies", "correct": False},
                    {"text": "It deletes previous drafts permanently", "correct": False}
                ],
                "explanation": "Live co-authoring ensures all collaborators see and edit the single up-to-date version."
            },
            {
                "question": "What tool in word processing allows you to suggest a correction to a colleague without altering their original typed words?",
                "options": [
                    {"text": "Insert Comment", "correct": True},
                    {"text": "Delete All", "correct": False},
                    {"text": "Backspace", "correct": False},
                    {"text": "High Contrast Mode", "correct": False}
                ],
                "explanation": "Comments attach side notes to text for discussion without modifying the document body."
            }
        ],
        "practice": {
            "task": "You are collaborating on a staff training presentation with three colleagues. Describe how you would share the presentation link with them, ensure they can edit slides, and use comments to assign a task to one colleague.",
            "scaffold_starter": "1. Share link & permission: \n2. Assigning task via comment: ",
            "model_answer": "1. Click Share, enter colleagues' email addresses, select 'Can Edit' permission, and send the link.\n2. In the document, highlight the relevant slide, click New Comment, type '@colleague_name please add the slide 4 safety diagram', and post the comment.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Sharing link with 'Can Edit' permissions."},
                {"tag": "[1 Mark]", "desc": "Using comments / tagging colleagues to assign tasks."}
            ]
        },
        "revision_links": [
            {"label": "Workplace Email Etiquette", "href": "l1-workplace-email-etiquette.html"},
            {"label": "Calendar Management", "href": "l1-calendar-meeting-scheduling.html"},
            {"label": "Cloud Backups & Sync", "href": "l1-backups-cloud-sync.html"}
        ]
    },

    # -------------------------------------------------------------------------
    # Skill Area 4: Transacting
    # -------------------------------------------------------------------------
    {
        "slug": "l1-evaluating-online-services",
        "code": "L1.4.1",
        "skill_area": "4. Transacting",
        "title": "Evaluating Online Services and Information",
        "time": "15 Mins",
        "lead": "Assess the reliability, credibility, and security of online suppliers and information sources: evaluate customer reviews, check terms & conditions, verify return policies, and check consumer rights.",
        "objectives": [
            "Evaluate website credibility using domain extensions, contact details, and independent reviews",
            "Identify customer rights: Consumer Rights Act, refund policies, and cancellation periods",
            "Spot deceptive online practices (hidden subscription fees, fake review patterns)"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Evaluating Online Websites & Reviews",
        "steps": [
            {
                "title": "Checking Website Authenticity & Credibility",
                "body": "<p>Not every website that appears on Google is legitimate. Check these four credibility factors:</p><ol><li><strong>Domain Extension:</strong> Trusted UK public bodies end in <code>.gov.uk</code> (government) or <code>.ac.uk</code> (universities). Be sceptical of obscure domains like <code>.xyz</code>, <code>.top</code>, or <code>.biz</code>.</li><li><strong>Physical Address &amp; Landline Phone:</strong> Legitimate UK businesses provide a registered Companies House number, full postal address, and working contact details.</li><li><strong>SSL Certificate (Padlock &amp; HTTPS):</strong> Encrypts communications.</li><li><strong>Professional Design &amp; Spelling:</strong> Numerous typos, poor grammar, and blurry logos are warning signs of scam copycat sites.</li></ol>"
            },
            {
                "title": "Spotting Fake Reviews",
                "body": "<p>Many fraudulent sellers post fake 5-star reviews to deceive shoppers. Look out for:</p><ul><li>Dozens of 5-star reviews posted on the exact same date.</li><li>Vague, generic praise with no specific mention of the product features.</li><li>Check independent third-party review sites (like Trustpilot) rather than relying only on testimonials hosted on the seller's own homepage.</li></ul>",
                "ui_sim": {
                    "title": "Website Credibility Checklist",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='display:flex; justify-content:space-between; margin-bottom:4px;'><span style='color:#0f172a;'><i class='fa-solid fa-check' style='color:#10b981;'></i> Working UK Phone &amp; Postal Address</span><span style='color:#10b981; font-weight:700;'>Verified</span></div><div style='display:flex; justify-content:space-between; margin-bottom:4px;'><span style='color:#0f172a;'><i class='fa-solid fa-check' style='color:#10b981;'></i> Clear 14-day refund &amp; returns policy</span><span style='color:#10b981; font-weight:700;'>Compliant</span></div><div style='display:flex; justify-content:space-between;'><span style='color:#0f172a;'><i class='fa-solid fa-triangle-exclamation' style='color:#dc2626;'></i> Independent Trustpilot rating below 2.0</span><span style='color:#dc2626; font-weight:700;'>High Risk</span></div></div>"
                }
            },
            {
                "title": "Terms, Conditions, and Consumer Rights",
                "body": "<p>Under the UK <strong>Consumer Contracts Regulations</strong>, online shoppers have a statutory <strong>14-day cooling-off period</strong> to cancel most orders and receive a full refund. Always check who pays for return postage before completing a transaction.</p>"
            }
        ],
        "exam_model": {
            "scenario": "A clinic worker is tasked with ordering ergonomic desk chairs from an unfamiliar online office supplier offering 70% discounts. State two checks the worker must carry out before making payment to confirm that the supplier is reputable and legitimate.",
            "steps": [
                {
                    "action": "First verification check",
                    "solution": "Check independent customer reviews on third-party platforms (such as Trustpilot) to see other buyers' experiences.",
                    "mark": "[B1]",
                    "rationale": "Independent third-party validation reveals real service quality."
                },
                {
                    "action": "Second verification check",
                    "solution": "Verify the website's physical contact details (postal address, registered company number, landline telephone) and clear returns policy.",
                    "mark": "[B1]",
                    "rationale": "Confirms physical corporate accountability and statutory consumer compliance."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever evaluating a new supplier, look for: 1. Independent reviews; 2. Physical contact details and returns policy."
        },
        "drills": [
            {
                "question": "What is the best way to verify whether an unfamiliar shopping website is trustworthy?",
                "options": [
                    {"text": "Check independent third-party review websites (like Trustpilot) and verify their physical contact details", "correct": True},
                    {"text": "Assume it is trustworthy because it has pretty colours", "correct": False},
                    {"text": "Only read the reviews written on the seller's own homepage", "correct": False},
                    {"text": "Ask if they accept payments in gift cards", "correct": False}
                ],
                "explanation": "Independent review platforms provide unedited buyer feedback and fraud warnings."
            },
            {
                "question": "Under UK consumer regulations, what standard right do consumers have when buying goods online?",
                "options": [
                    {"text": "A statutory 14-day cooling-off cancellation period to return goods for a refund", "correct": True},
                    {"text": "Goods are completely free if delivered on a Sunday", "correct": False},
                    {"text": "You can never return items bought on the internet", "correct": False},
                    {"text": "You must pay a 50% fee to cancel any order", "correct": False}
                ],
                "explanation": "UK Consumer Contracts Regulations guarantee a 14-day cancellation window for online orders."
            },
            {
                "question": "Which domain extension indicates an official UK government department or agency?",
                "options": [
                    {"text": ".gov.uk", "correct": True},
                    {"text": ".com", "correct": False},
                    {"text": ".biz", "correct": False},
                    {"text": ".co", "correct": False}
                ],
                "explanation": ".gov.uk is strictly reserved for authenticated UK government departments and local authorities."
            }
        ],
        "practice": {
            "task": "You are purchasing clinical training equipment online. You find a site offering prices half of retail value, but there is no telephone number, only an email address, and all customer reviews are 5-star reviews posted on the same day. Explain whether you should buy from this site and give reasons.",
            "scaffold_starter": "Decision: \nReason 1: \nReason 2: ",
            "model_answer": "Decision: Do not purchase from this website; it is highly likely to be fraudulent.\nReason 1: Lack of a physical address or telephone number means you cannot contact the business if items never arrive.\nReason 2: Clustered 5-star reviews posted on the same day are a classic sign of fabricated/fake reviews.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Clear decision not to buy / flagging fraud risk."},
                {"tag": "[1 Mark]", "desc": "Citing missing contact details and suspicious fake review patterns."}
            ]
        },
        "revision_links": [
            {"label": "Multi-Factor Authentication", "href": "l1-multi-factor-authentication-banking.html"},
            {"label": "Document Uploads & Portals", "href": "l1-portal-uploads-customer-support.html"},
            {"label": "Phishing & Social Engineering", "href": "l1-phishing-social-engineering.html"}
        ]
    },
    {
        "slug": "l1-multi-factor-authentication-banking",
        "code": "L1.4.2",
        "skill_area": "4. Transacting",
        "title": "Multi-Factor Authentication (MFA) and Online Banking",
        "time": "15 Mins",
        "lead": "Protect financial and workplace accounts with Multi-Factor Authentication (MFA / 2FA): understand knowledge, possession, and inherence factors, use authenticator apps, and spot banking transaction fraud.",
        "objectives": [
            "Explain how Multi-Factor Authentication (MFA) protects accounts against stolen passwords",
            "Identify the three authentication factors: Something you know, Something you have, Something you are",
            "Safely authorise workplace transactions and spot banking fraud red flags"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Multi-Factor Authentication (MFA)",
        "steps": [
            {
                "title": "Why Passwords Alone Are No Longer Enough",
                "body": "<p>Billions of usernames and passwords are leaked on the dark web every year. If you use the same password on multiple websites, a data breach at one company puts all your accounts at risk.</p><p><strong>Multi-Factor Authentication (MFA / 2FA)</strong> adds an extra layer of security. Even if a criminal steals your password, they CANNOT log in without your second authentication factor!</p>"
            },
            {
                "title": "The Three Factors of Authentication",
                "body": "<p>MFA combines at least two different categories:</p><ol><li><strong>Something you KNOW:</strong> Password, PIN, or memorable security question.</li><li><strong>Something you HAVE:</strong> Physical smartphone receiving an SMS code, authenticator app (e.g. Microsoft Authenticator), or a physical hardware security key (YubiKey).</li><li><strong>Something you ARE (Biometrics):</strong> Fingerprint scan, facial recognition (Face ID), or retina scan.</li></ol>",
                "ui_sim": {
                    "title": "Two-Factor Verification Prompt",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; padding:12px; border-radius:4px; text-align:center; font-size:0.85rem;'><i class='fa-solid fa-mobile-screen-button' style='font-size:1.8rem; color:#0284c7; margin-bottom:6px;'></i><div style='font-weight:700; color:#0f172a;'>Check your phone</div><div style='color:#64748b; margin-bottom:8px;'>We sent a 6-digit code to ***-***-7890</div><div style='display:flex; justify-content:center; gap:6px; margin-bottom:8px;'><input type='text' value='4' style='width:24px; text-align:center;'><input type='text' value='8' style='width:24px; text-align:center;'><input type='text' value='2' style='width:24px; text-align:center;'><input type='text' value='9' style='width:24px; text-align:center;'><input type='text' value='1' style='width:24px; text-align:center;'><input type='text' value='5' style='width:24px; text-align:center;'></div><button style='background:#0284c7; color:#ffffff; border:none; padding:4px 14px; border-radius:4px; font-weight:700;'>Verify Code</button></div>"
                }
            },
            {
                "title": "Online Banking Security Rules",
                "body": "<p>When managing business or personal finances online:</p><ul><li>Always log out completely when finished.</li><li>Check statements weekly for unauthorised micro-charges.</li><li><strong>Never approve an MFA prompt on your phone unless you are actively logging in yourself!</strong> Criminals who steal passwords trigger MFA prompts hoping you will click 'Approve' without thinking (MFA fatigue attack).</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A dental practice introduces Multi-Factor Authentication (MFA) for its staff patient database. Staff must now type their password AND enter a 6-digit code sent to their mobile phone. Explain how this prevents unauthorised access if a worker's password is stolen in a phishing attack.",
            "steps": [
                {
                    "action": "Explain the protection mechanism",
                    "solution": "The criminal only has the password (something you know), but they do not possess the worker's physical mobile phone (something you have) to receive the 6-digit code.",
                    "mark": "[B1]",
                    "rationale": "Identifies the requirement for two independent factors."
                },
                {
                    "action": "State outcome",
                    "solution": "Without the second factor, the login attempt is blocked and patient records remain protected.",
                    "mark": "[B1]",
                    "rationale": "Confirms system denies unauthorized access."
                }
            ],
            "tutor_rule": "In Level 1 exams, questions on MFA test whether you know the three factors: something you know (password), something you have (phone/token), something you are (fingerprint)."
        },
        "drills": [
            {
                "question": "Which of the following is an example of 'Something you ARE' in biometric authentication?",
                "options": [
                    {"text": "Fingerprint scan or facial recognition", "correct": True},
                    {"text": "A 4-digit card PIN", "correct": False},
                    {"text": "Your mother's maiden name", "correct": False},
                    {"text": "A USB memory stick", "correct": False}
                ],
                "explanation": "Biometrics evaluate unique physical human characteristics like fingerprints, retina, or facial geometry."
            },
            {
                "question": "What should you do if an authenticator app notification pops up on your phone asking you to 'Approve Login' when you are not currently logging in?",
                "options": [
                    {"text": "Click 'Deny' immediately and change your account password", "correct": True},
                    {"text": "Click 'Approve' just in case", "correct": False},
                    {"text": "Turn off your phone battery", "correct": False},
                    {"text": "Ignore it and tell no one", "correct": False}
                ],
                "explanation": "An unexpected MFA prompt means someone has entered your password and is trying to access your account."
            },
            {
                "question": "Why is an SMS or Authenticator App code considered 'Something you HAVE'?",
                "options": [
                    {"text": "Because it requires physical possession of your registered mobile device", "correct": True},
                    {"text": "Because you have to memorise it forever", "correct": False},
                    {"text": "Because you own the internet", "correct": False},
                    {"text": "Because it is stored in your computer RAM", "correct": False}
                ],
                "explanation": "Possession factors require holding the physical hardware device that generates or receives the dynamic code."
            }
        ],
        "practice": {
            "task": "A company wants to strengthen security for remote employees logging into their financial system. Explain what Multi-Factor Authentication is, and give one example of each of the two different factors the company could use.",
            "scaffold_starter": "MFA Definition: \nFactor 1 (Something you know): \nFactor 2 (Something you have/are): ",
            "model_answer": "Definition: Multi-Factor Authentication is a security process requiring users to provide two or more different forms of identification before gaining access.\nFactor 1 (Something you know): A strong private password or secret PIN.\nFactor 2 (Something you have/are): A one-time passcode generated on a registered authenticator app / phone, or a biometric fingerprint scan.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Accurate definition of MFA requiring 2+ distinct verification steps."},
                {"tag": "[1 Mark]", "desc": "Providing valid examples of two different authentication categories."}
            ]
        },
        "revision_links": [
            {"label": "Cybersecurity & Malware Defence", "href": "l1-cybersecurity-malware-defence.html"},
            {"label": "Phishing & Social Engineering", "href": "l1-phishing-social-engineering.html"},
            {"label": "Evaluating Online Services", "href": "l1-evaluating-online-services.html"}
        ]
    },
    {
        "slug": "l1-portal-uploads-customer-support",
        "code": "L1.4.3",
        "skill_area": "4. Transacting",
        "title": "Document Uploads and Digital Support Portals",
        "time": "15 Mins",
        "lead": "Interact successfully with customer and public service portals: verify file type and size restrictions when uploading documents (ID, CVs, certificates), use online live chat and ticketing systems, and cancel unwanted subscriptions.",
        "objectives": [
            "Verify file format (.pdf, .jpg) and file size limits before uploading to online portals",
            "Use live chat, helpdesk ticketing, and digital support channels effectively",
            "Manage and cancel recurring digital subscriptions and direct debits safely"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Uploading Files & Digital Portals",
        "steps": [
            {
                "title": "Uploading Documents to Web Portals",
                "body": "<p>Workplaces, universities, and government bodies (e.g. DBS checks, HMRC, healthcare clinic portals) require you to upload proof of identity and certificates. <strong>Check portal rules before uploading:</strong></p><ul><li><strong>File Format:</strong> Many portals only accept <code>.PDF</code> or <code>.JPG</code>. If you try to upload a <code>.docx</code> or <code>.pages</code> file, the system will reject it.</li><li><strong>File Size Limit:</strong> Portals often enforce limits (e.g. <em>'Max file size 4 MB'</em>). If your scan is 12 MB, you must compress or resize it before uploading.</li><li><strong>Confirmation Message:</strong> Always wait for the progress bar to reach 100% and look for a green checkmark or confirmation reference number (e.g. <code>REF-98432</code>).</li></ul>",
                "ui_sim": {
                    "title": "Portal Document Upload Interface",
                    "content": "<div style='background:#f8fafc; border:2px dashed #94a3b8; padding:16px; border-radius:6px; text-align:center; font-size:0.85rem;'><i class='fa-solid fa-cloud-arrow-up' style='font-size:2rem; color:#0284c7; margin-bottom:6px;'></i><div style='font-weight:700; color:#0f172a;'>Drag &amp; drop Proof of ID here, or browse</div><div style='color:#64748b; font-size:0.75rem; margin-top:4px;'>Accepted formats: PDF, JPG, PNG (Max 5 MB)</div><div style='margin-top:10px; display:inline-flex; align-items:center; gap:8px; background:#e0f2fe; padding:4px 10px; border-radius:12px; color:#0369a1;'><i class='fa-solid fa-check'></i> Passport_Scan.pdf (1.8 MB) - Uploaded</div></div>"
                }
            },
            {
                "title": "Using Online Customer Support & Live Chat",
                "body": "<p>When technical or billing problems arise:</p><ul><li><strong>Live Chat / Chatbots:</strong> Provide your account reference and state the issue clearly in your first message.</li><li><strong>Ticketing Systems:</strong> Receive a support ticket number. Keep this reference for following up.</li></ul>"
            },
            {
                "title": "Managing & Cancelling Online Subscriptions",
                "body": "<p>Many digital services offer 'free 30-day trials' that automatically convert into paid monthly direct debits:</p><ul><li>Set a calendar reminder 3 days before the trial ends.</li><li>To cancel: Navigate to <em>Account Settings &gt; Subscriptions / Billing &gt; Cancel Subscription</em>.</li><li>Always save the cancellation confirmation email as proof of termination.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A candidate is uploading their CV to a job portal. The website states: 'Accepted format: PDF only. Maximum file size: 2 MB.' The candidate tries to upload 'My_CV.docx' which is 3.5 MB in size. The upload fails. State two changes the candidate must make to successfully submit their CV.",
            "steps": [
                {
                    "action": "Change file format",
                    "solution": "Convert / Export the Word document (.docx) as a PDF file (.pdf).",
                    "mark": "[B1]",
                    "rationale": "Satisfies the format requirement."
                },
                {
                    "action": "Reduce file size",
                    "solution": "Compress images or reduce document quality so the file size is under the 2 MB limit.",
                    "mark": "[B1]",
                    "rationale": "Satisfies the storage size constraint."
                }
            ],
            "tutor_rule": "In Level 1 exams, upload failure questions always test: 1. Wrong file extension; 2. File size exceeding maximum MB limit."
        },
        "drills": [
            {
                "question": "Why might an online government portal refuse to accept an uploaded photo of your passport?",
                "options": [
                    {"text": "The file size exceeds the maximum limit or the file format is not accepted (e.g. docx instead of pdf/jpg)", "correct": True},
                    {"text": "The government website is sleeping", "correct": False},
                    {"text": "Passports cannot be stored on computers", "correct": False},
                    {"text": "The internet is only for text, not photos", "correct": False}
                ],
                "explanation": "Portals reject files that violate strict format (.pdf, .jpg) or file size (MB) constraints."
            },
            {
                "question": "What should you always retain as evidence after submitting an official document or cancelling a subscription online?",
                "options": [
                    {"text": "The confirmation reference number or confirmation email", "correct": True},
                    {"text": "A photograph of your computer keyboard", "correct": False},
                    {"text": "Your computer power cable", "correct": False},
                    {"text": "The cardboard box your laptop arrived in", "correct": False}
                ],
                "explanation": "Confirmation emails and reference numbers act as legal proof of transaction."
            },
            {
                "question": "How can you prevent a 30-day free software trial from charging your bank card automatically?",
                "options": [
                    {"text": "Set a calendar reminder and cancel the subscription in account settings before the trial period expires", "correct": True},
                    {"text": "Throw away your computer monitor", "correct": False},
                    {"text": "Uninstall your web browser", "correct": False},
                    {"text": "Change your desktop colour to black", "correct": False}
                ],
                "explanation": "Cancelling prior to the renewal date terminates the recurring billing instruction."
            }
        ],
        "practice": {
            "task": "You need to upload training certificates to a professional registry portal. The portal allows only PDF files up to 5 MB. Your certificates are currently 4 separate JPEG photo files totaling 14 MB. Describe the steps you would take to prepare and upload these documents successfully.",
            "scaffold_starter": "1. Format & Size adjustment: \n2. Upload process: ",
            "model_answer": "1. Insert the 4 photos into a Word document or PDF editor, resize/compress the images to reduce file size, and export the document as a single PDF file under 5 MB.\n2. Open the portal, click Upload Document, select the new PDF file, wait for 100% completion, and record the submission confirmation reference.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Converting photos into a single PDF and compressing under 5 MB."},
                {"tag": "[1 Mark]", "desc": "Uploading and recording submission confirmation reference."}
            ]
        },
        "revision_links": [
            {"label": "Evaluating Online Services", "href": "l1-evaluating-online-services.html"},
            {"label": "File Management & Sizes", "href": "l1-file-management-hierarchies.html"},
            {"label": "Multi-Factor Authentication", "href": "l1-multi-factor-authentication-banking.html"}
        ]
    }
]
