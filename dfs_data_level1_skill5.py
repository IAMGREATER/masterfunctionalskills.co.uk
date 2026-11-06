# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Level 1 Digital Skills (Skill Area 5)
Author: Abdul (MFS Pedagogical Systems)
"""

LEVEL_1_SKILL_5 = [
    {
        "slug": "l1-cybersecurity-malware-defence",
        "code": "L1.5.1",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "Cybersecurity, Malware and Antivirus Defence",
        "time": "15 Mins",
        "lead": "Defend systems against online threats: understand malware types (viruses, ransomware, spyware, trojans), configure automated antivirus software updates, and understand the role of firewalls.",
        "objectives": [
            "Define common malware categories: viruses, ransomware, spyware, and trojans",
            "Explain how firewalls block unauthorised incoming network traffic",
            "Maintain automated operating system and antivirus definition updates"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Malware Types & Antivirus Defence",
        "steps": [
            {
                "title": "Understanding Malware Types",
                "body": "<p><strong>Malware</strong> (Malicious Software) is any software intentionally designed to cause damage to a computer, server, client, or computer network:</p><ul><li><strong>Virus:</strong> Malicious program that replicates itself by modifying other programs and inserting its own code, corrupting files and slowing performance.</li><li><strong>Ransomware:</strong> Deadly malware that secretly <strong>encrypts all your files</strong> so you cannot open them, demanding a cryptocurrency ransom payment to unlock them.</li><li><strong>Spyware:</strong> Secretly records your keystrokes (keylogger), webcam, and web browsing history to steal passwords and financial data.</li><li><strong>Trojan:</strong> Disguised as legitimate, helpful software (e.g. a free game or PDF reader) but secretly installs a backdoor for hackers.</li></ul>"
            },
            {
                "title": "The Role of Firewalls and Antivirus Software",
                "body": "<p>Digital security relies on layers of defence:</p><ul><li><strong>Firewall:</strong> Acts like a digital security guard at your front gate. It inspects all incoming and outgoing network traffic, blocking unauthorized access attempts from external hackers.</li><li><strong>Antivirus / Anti-malware:</strong> Scans files, downloads, and USB drives against a database of known threats. It quarantines and destroys detected infections.</li></ul>",
                "ui_sim": {
                    "title": "Windows Security Dashboard",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:12px; border-radius:4px; font-size:0.85rem;'><div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;'><span style='color:#0f172a; font-weight:700;'><i class='fa-solid fa-shield-virus' style='color:#10b981;'></i> Virus &amp; Threat Protection</span><span style='background:#d1fae5; color:#065f46; padding:2px 8px; border-radius:4px; font-weight:700;'>Protected</span></div><div style='color:#475569; font-size:0.78rem;'>Last quick scan: Today, 08:30 &bull; Security intelligence up to date</div><button style='background:#0284c7; color:#ffffff; border:none; padding:4px 12px; border-radius:4px; font-weight:700; margin-top:6px;'>Quick Scan Now</button></div>"
                }
            },
            {
                "title": "Keeping Software Updated (Patching)",
                "body": "<p>Software updates are not just for new features — they include critical <strong>security patches</strong> that fix newly discovered vulnerabilities. Always leave <strong>Automatic Updates</strong> switched ON for your operating system and web browsers.</p>"
            }
        ],
        "exam_model": {
            "scenario": "A medical centre administrator receives an alert saying: 'All your files have been encrypted. Pay £500 within 48 hours to receive the decryption key.' Name the specific type of malware responsible, and state two measures the centre should have had in place to prevent this.",
            "steps": [
                {
                    "action": "Name the malware",
                    "solution": "Ransomware",
                    "mark": "[B1]",
                    "rationale": "Correctly classifies extortion malware that encrypts files."
                },
                {
                    "action": "State two preventive measures",
                    "solution": "1. Keep regular offline / cloud backups of all data to restore files without paying.\n2. Keep antivirus software and operating systems updated, and train staff not to click suspicious email links.",
                    "mark": "[B1]",
                    "rationale": "Identifies standard disaster recovery (backups) and prevention (updates/antivirus)."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever an alert demands money to unlock files, the answer is always 'Ransomware', and the best defence is 'Offline Backups'."
        },
        "drills": [
            {
                "question": "Which type of malware locks and encrypts a user's files and demands a ransom payment to unlock them?",
                "options": [
                    {"text": "Ransomware", "correct": True},
                    {"text": "Spyware", "correct": False},
                    {"text": "Adware", "correct": False},
                    {"text": "Task Manager", "correct": False}
                ],
                "explanation": "Ransomware holds victim files hostage through encryption until a ransom is paid."
            },
            {
                "question": "What is the primary function of a network FIREWALL?",
                "options": [
                    {"text": "To monitor and block unauthorised network traffic entering or leaving your computer", "correct": True},
                    {"text": "To extinguish fires inside the computer case", "correct": False},
                    {"text": "To print colour documents faster", "correct": False},
                    {"text": "To increase screen brightness", "correct": False}
                ],
                "explanation": "Firewalls filter network packets based on security rules to block unauthorised access."
            },
            {
                "question": "Why is it dangerous to ignore operating system updates on workplace computers?",
                "options": [
                    {"text": "Updates include critical security patches that fix vulnerabilities exploited by cybercriminals", "correct": True},
                    {"text": "The computer monitor will change colour to purple", "correct": False},
                    {"text": "Your keyboard will stop typing vowels", "correct": False},
                    {"text": "Printers will stop working permanently", "correct": False}
                ],
                "explanation": "Unpatched systems possess known vulnerabilities that automated malware exploits."
            }
        ],
        "practice": {
            "task": "A company is reviewing its digital security policies. Explain the difference between Spyware and a Trojan, and describe the role of Antivirus software in protecting workplace computers.",
            "scaffold_starter": "Spyware vs Trojan: \nRole of Antivirus software: ",
            "model_answer": "Spyware: Secretly monitors and records user actions (such as keystrokes and passwords) without their consent.\nTrojan: Pretends to be a safe, legitimate application but secretly introduces malware onto the system.\nAntivirus Role: Continuously scans files and memory against a library of known threats, quarantines or destroys infections, and protects against new malware.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Accurate definitions of Spyware (monitoring) and Trojan (disguised software)."},
                {"tag": "[1 Mark]", "desc": "Explaining the scanning, detection, and removal role of antivirus software."}
            ]
        },
        "revision_links": [
            {"label": "Phishing & Social Engineering", "href": "l1-phishing-social-engineering.html"},
            {"label": "Data Backups & Cloud Sync", "href": "l1-backups-cloud-sync.html"},
            {"label": "Multi-Factor Authentication", "href": "l1-multi-factor-authentication-banking.html"}
        ]
    },
    {
        "slug": "l1-phishing-social-engineering",
        "code": "L1.5.2",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "Identifying Phishing and Social Engineering",
        "time": "15 Mins",
        "lead": "Recognise sophisticated social engineering attacks: analyse spoofed email headers, inspect hyperlinked URLs without clicking, identify SMS scams (smishing) and telephone impersonation (vishing), and follow reporting procedures.",
        "objectives": [
            "Inspect sender domain names and hover over hyperlinks to reveal destination URLs",
            "Differentiate between Phishing (email), Smishing (SMS text), and Vishing (phone voice)",
            "Follow official workplace incident reporting protocols when suspicious communications arrive"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Spotting Phishing & Fake Links",
        "steps": [
            {
                "title": "How Social Engineering Works",
                "body": "<p><strong>Social Engineering</strong> manipulates human emotions (fear, urgency, greed, or curiosity) rather than hacking hardware directly. Criminals know that tricking a human into clicking a link is often easier than breaking computer encryption.</p><p>Key variations include:</p><ul><li><strong>Phishing (Email):</strong> Fake emails appearing to come from banks, delivery couriers, or senior managers.</li><li><strong>Smishing (SMS / Text Messages):</strong> Scam texts about missed parcel deliveries or banking blocks containing shortened links.</li><li><strong>Vishing (Voice / Phone Calls):</strong> Scammers impersonating the police, Microsoft technical support, or your bank fraud team on the telephone.</li></ul>"
            },
            {
                "title": "Inspecting Sender Domains and Hyperlinks",
                "body": "<p>Never trust the display name alone! Anyone can set their display name to <em>'Healthcare IT Support'</em> or <em>'HM Revenue &amp; Customs'</em>.</p><ol><li><strong>Check the actual email address:</strong> Look at the characters after the <code>@</code> symbol. If it says <code>support@hmrc-tax-gov-service99.net</code>, it is fake. Official HMRC emails end in <code>@hmrc.gov.uk</code>.</li><li><strong>Hover to Reveal (URL Snooping):</strong> Hover your mouse cursor over any hyperlink <strong>without clicking</strong>. A small preview box will appear showing the real web address. If the text says <em>'www.bank.co.uk'</em> but the hover link points to <em>'www.scam-login-portal.ru'</em>, it is fraudulent!</li></ol>",
                "ui_sim": {
                    "title": "Hyperlink Hover Preview Simulation",
                    "content": "<div style='background:#fef2f2; border:1px solid #f87171; padding:12px; border-radius:4px; font-size:0.85rem;'><div style='color:#991b1b; font-weight:700; margin-bottom:4px;'><i class='fa-solid fa-triangle-exclamation'></i> Fake IT Support Notification</div><p style='color:#334155; margin-bottom:8px;'>Your cloud storage is full. <span style='color:#0284c7; text-decoration:underline; cursor:pointer;'>Click here to upgrade your storage</span></p><div style='background:#ffffff; border:1px solid #94a3b8; padding:4px 8px; border-radius:4px; display:inline-block; font-family:monospace; font-size:0.75rem; color:#dc2626;'><i class='fa-solid fa-arrow-pointer'></i> Real URL: http://phish-login-steal.xyz/account</div></div>"
                }
            },
            {
                "title": "Workplace Incident Reporting",
                "body": "<p>If you receive a phishing email at work:</p><ul><li>Do NOT click any links, do NOT open any attachments, and do NOT reply.</li><li>Click the <strong>Report Phishing</strong> button in Outlook, or forward the email as an attachment to your organisation's official IT security helpdesk.</li><li>Delete the message from your Deleted Items folder.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A clinic worker receives an email that appears to come from 'Payroll Department' with the subject 'URGENT: Payroll Verification Required'. The email states that wages will be stopped unless the employee clicks a link and enters their bank login details. State two clues that indicate this is a social engineering attack, and describe the action the employee should take.",
            "steps": [
                {
                    "action": "Identify two phishing clues",
                    "solution": "1. Uses high psychological pressure / urgency (threatening to stop wages).\n2. Requests private banking login credentials via an emailed link (legitimate payroll departments never ask for bank passwords).",
                    "mark": "[B1]",
                    "rationale": "Identifies psychological manipulation and credential harvesting."
                },
                {
                    "action": "Describe correct workplace action",
                    "solution": "Do not click the link; report the email immediately to the internal IT security department and delete it.",
                    "mark": "[B1]",
                    "rationale": "Correctly follows organisational reporting and remediation protocol."
                }
            ],
            "tutor_rule": "In Level 1 exams, never say 'Reply to ask if it's real'. The accredited action is ALWAYS: 'Do not click links; report to IT and delete'."
        },
        "drills": [
            {
                "question": "How can you check where a link in an email really leads BEFORE clicking on it?",
                "options": [
                    {"text": "Hover your mouse cursor over the link to preview the destination URL", "correct": True},
                    {"text": "Click on it as fast as possible", "correct": False},
                    {"text": "Print the email onto paper", "correct": False},
                    {"text": "Turn off your computer monitor", "correct": False}
                ],
                "explanation": "Hovering reveals the target destination address without executing code or visiting the site."
            },
            {
                "question": "What is 'Smishing'?",
                "options": [
                    {"text": "A phishing attack delivered via SMS text message to a mobile phone", "correct": True},
                    {"text": "A physical robbery at an office", "correct": False},
                    {"text": "A tool for compressing video files", "correct": False},
                    {"text": "A type of printer ink", "correct": False}
                ],
                "explanation": "Smishing combines SMS and Phishing to trick mobile phone users via text message."
            },
            {
                "question": "What should you do if you receive a suspicious email in your workplace inbox?",
                "options": [
                    {"text": "Do not click links or open attachments; report it to your IT department and delete it", "correct": True},
                    {"text": "Reply with your password to verify your identity", "correct": False},
                    {"text": "Forward it to all your personal social media accounts", "correct": False},
                    {"text": "Download all attachments to your desktop", "correct": False}
                ],
                "explanation": "Never engage with phishing emails; reporting them allows IT teams to block the sender across the network."
            }
        ],
        "practice": {
            "task": "A staff member accidentally clicked a link in a phishing email and entered their workplace network password before realising it was a scam. List the immediate three steps the employee must take to protect the organisation.",
            "scaffold_starter": "Step 1 (Password): \nStep 2 (Report): \nStep 3 (IT Action): ",
            "model_answer": "Step 1: Change their network password immediately from a clean device.\nStep 2: Disconnect the computer from the network (unplug network cable / turn off Wi-Fi) to stop malware spreading.\nStep 3: Contact the workplace IT security team immediately to report the compromise so they can reset sessions and check account logs.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Immediately changing the compromised password."},
                {"tag": "[1 Mark]", "desc": "Reporting to IT security and isolating device from the network."}
            ]
        },
        "revision_links": [
            {"label": "Cybersecurity & Malware", "href": "l1-cybersecurity-malware-defence.html"},
            {"label": "Multi-Factor Authentication", "href": "l1-multi-factor-authentication-banking.html"},
            {"label": "UK GDPR & Privacy", "href": "l1-uk-gdpr-data-protection-privacy.html"}
        ]
    },
    {
        "slug": "l1-uk-gdpr-data-protection-privacy",
        "code": "L1.5.3",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "UK GDPR, Privacy and Digital Footprints",
        "time": "15 Mins",
        "lead": "Understand legal compliance and privacy rights: apply the UK Data Protection Act 2018 and UK GDPR principles, manage browser cookies and tracking, and manage your professional digital footprint.",
        "objectives": [
            "Explain core UK GDPR principles (lawfulness, purpose limitation, data minimisation, accuracy, storage limitation)",
            "Identify individual data rights (Right to Access / Subject Access Request, Right to Erasure)",
            "Manage website cookie consent banners (Essential vs Marketing cookies) and browser privacy modes"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - UK GDPR & Data Protection",
        "steps": [
            {
                "title": "The UK Data Protection Act 2018 & UK GDPR",
                "body": "<p>In the UK, the <strong>Data Protection Act 2018</strong> (incorporating <strong>UK GDPR</strong>) governs how businesses and public bodies handle personal data. Organisations must obey six core principles:</p><ol><li><strong>Lawful, Fair &amp; Transparent:</strong> Data must be collected honestly with clear notice to individuals.</li><li><strong>Purpose Limitation:</strong> Data collected for one reason (e.g. appointment booking) cannot be secretly used for another (e.g. marketing).</li><li><strong>Data Minimisation:</strong> Only collect what is strictly necessary — do not ask for irrelevant personal history.</li><li><strong>Accuracy:</strong> Keep records up to date and correct mistakes promptly.</li><li><strong>Storage Limitation:</strong> Do not keep personal data longer than needed. Delete securely when no longer required.</li><li><strong>Integrity &amp; Confidentiality:</strong> Keep data secure from theft or loss using strong passwords and encryption.</li></ol>"
            },
            {
                "title": "Individual Rights Under UK GDPR",
                "body": "<p>Every person (data subject) has statutory legal rights:</p><ul><li><strong>Right to be Informed:</strong> Plain-English privacy policies explaining how data is used.</li><li><strong>Right of Access (Subject Access Request - SAR):</strong> You can request a free copy of all personal records an organisation holds about you.</li><li><strong>Right to Erasure ('Right to be Forgotten'):</strong> Request deletion of your data when there is no longer a legal reason to hold it.</li></ul>",
                "callout": {
                    "type": "vocational",
                    "title": "Workplace Confidentiality Mandate",
                    "text": "Never discuss patients or clients on public social media, and never take photos of medical records. Disclosing personal data without consent is a serious criminal offence under UK law."
                }
            },
            {
                "title": "Cookies and Browser Privacy Modes",
                "body": "<p>When visiting websites:</p><ul><li><strong>Cookies:</strong> Small text files saved on your computer by websites to remember login states or track browsing behavior. <strong>Essential cookies</strong> are required for sites to function; <strong>marketing cookies</strong> track you across other sites for adverts. You can decline marketing cookies on consent banners.</li><li><strong>Incognito / InPrivate Browsing:</strong> Opens a temporary browser window that deletes your search history, cookies, and temporary cache as soon as you close it. (Note: It does NOT hide your activity from your employer or internet provider!).</li></ul>",
                "ui_sim": {
                    "title": "Website Cookie Consent Banner",
                    "content": "<div style='background:#f1f5f9; border:1px solid #cbd5e1; padding:12px; border-radius:6px; font-size:0.85rem;'><div style='font-weight:700; color:#0f172a; margin-bottom:4px;'><i class='fa-solid fa-cookie-bite' style='color:#d97706;'></i> We value your privacy</div><p style='color:#475569; font-size:0.78rem; margin-bottom:8px;'>We use essential cookies to make our site work, and optional analytics cookies to improve our services.</p><div style='display:flex; gap:8px;'><button style='background:#0f172a; color:#ffffff; border:none; padding:4px 12px; border-radius:4px; font-weight:700;'>Accept Essential Only</button><button style='background:#0284c7; color:#ffffff; border:none; padding:4px 12px; border-radius:4px; font-weight:700;'>Accept All</button></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A patient moves to a different city and contacts their local health clinic requesting that all their non-essential medical marketing survey data be deleted from the clinic mailing system. State the specific UK GDPR right the patient is exercising, and state one key responsibility the clinic has under the Data Protection Act.",
            "steps": [
                {
                    "action": "Identify the GDPR right",
                    "solution": "The Right to Erasure (or 'Right to be Forgotten' / Right to Object).",
                    "mark": "[B1]",
                    "rationale": "Correctly names the statutory individual right."
                },
                {
                    "action": "State clinic responsibility",
                    "solution": "The clinic must comply without undue delay (within one month) and delete the data, provided there is no conflicting legal obligation to retain it.",
                    "mark": "[B1]",
                    "rationale": "Demonstrates understanding of statutory response deadlines."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever questions ask about data protection legislation in the UK, the legislation is the 'Data Protection Act 2018' (incorporating UK GDPR)."
        },
        "drills": [
            {
                "question": "What UK legislation protects individual privacy and regulates how personal data is processed by organisations?",
                "options": [
                    {"text": "Data Protection Act 2018 (UK GDPR)", "correct": True},
                    {"text": "Computer Games Act 2005", "correct": False},
                    {"text": "Broadband Speed Regulation 2012", "correct": False},
                    {"text": "Printer Maintenance Code 1999", "correct": False}
                ],
                "explanation": "The Data Protection Act 2018 sets out UK data protection and GDPR standards."
            },
            {
                "question": "What is the 'Right of Access' (Subject Access Request) under UK GDPR?",
                "options": [
                    {"text": "An individual's legal right to ask an organisation for a free copy of the personal data held about them", "correct": True},
                    {"text": "The right to use anyone's Wi-Fi without permission", "correct": False},
                    {"text": "The right to borrow computers from the library", "correct": False},
                    {"text": "The right to change your date of birth legally online", "correct": False}
                ],
                "explanation": "Subject Access Requests allow people to see what personal data organisations store about them."
            },
            {
                "question": "What happens when you close an 'InPrivate' or 'Incognito' browser window?",
                "options": [
                    {"text": "Your browsing history, cookies, and temporary form data from that session are deleted from that device", "correct": True},
                    {"text": "Your computer automatically shuts down", "correct": False},
                    {"text": "All your bookmarks are permanently lost", "correct": False},
                    {"text": "Your internet subscription is cancelled", "correct": False}
                ],
                "explanation": "Private browsing cleans local traces (cookies, history, cache) upon window closure."
            }
        ],
        "practice": {
            "task": "A company is reviewing its compliance with the Data Protection Act 2018. Describe two key principles of UK GDPR that the company must follow when collecting customer names and addresses.",
            "scaffold_starter": "Principle 1 (Data Minimisation/Purpose): \nPrinciple 2 (Security/Storage): ",
            "model_answer": "Principle 1: Purpose Limitation and Data Minimisation: The company must only collect customer data that is strictly necessary for the transaction, and must not use it for unrelated marketing without consent.\nPrinciple 2: Storage Limitation and Security: Data must be kept securely using encryption and strong access controls, and must not be retained longer than legally necessary.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Explaining Purpose Limitation or Data Minimisation."},
                {"tag": "[1 Mark]", "desc": "Explaining Storage Limitation, Accuracy, or Security / Confidentiality."}
            ]
        },
        "revision_links": [
            {"label": "Workplace Email Etiquette & BCC", "href": "l1-workplace-email-etiquette.html"},
            {"label": "Cybersecurity & Malware Defence", "href": "l1-cybersecurity-malware-defence.html"},
            {"label": "Copyright, Plagiarism & DSE", "href": "l1-copyright-plagiarism-dse.html"}
        ]
    },
    {
        "slug": "l1-copyright-plagiarism-dse",
        "code": "L1.5.4",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "Copyright, Fair Use, DSE and Ergonomics",
        "time": "15 Mins",
        "lead": "Master legal intellectual property rights and workplace health standards: understand copyright and Creative Commons licensing, prevent plagiarism by citing sources, comply with Display Screen Equipment (DSE) regulations, and dispose of electronic waste (WEEE) responsibly.",
        "objectives": [
            "Explain copyright law and Creative Commons licenses when reusing online text and images",
            "Define plagiarism and correctly cite external research sources and references",
            "Apply DSE (Display Screen Equipment) ergonomic regulations and environmentally responsible WEEE recycling"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Copyright & DSE Ergonomics",
        "steps": [
            {
                "title": "Copyright Law and Creative Commons",
                "body": "<p>Just because an image or article appears on Google does <strong>NOT</strong> mean it is free to use!</p><ul><li><strong>Copyright:</strong> Under the <strong>Copyright, Designs and Patents Act 1988</strong>, the original creator automatically owns the legal rights to their text, images, videos, and software. Copying, publishing, or selling someone else's work without permission or a licence is copyright infringement.</li><li><strong>Public Domain:</strong> Material whose copyright has expired or has been donated for free public use.</li><li><strong>Creative Commons (CC):</strong> Licences that permit public reuse under specific conditions (e.g. <strong>CC-BY</strong> requires giving credit/attribution to the author; <strong>CC-NC</strong> forbids commercial use).</li></ul>"
            },
            {
                "title": "Plagiarism & Citing Online Sources",
                "body": "<p><strong>Plagiarism</strong> is the practice of taking someone else's work, ideas, or words and passing them off as your own.</p><ul><li>To avoid plagiarism: Always use quotation marks when quoting word-for-word, and provide a clear <strong>citation</strong> (Author Name, Title, Year, and Website URL).</li><li>In workplace reports, referencing reputable sources enhances your credibility and professional integrity.</li></ul>"
            },
            {
                "title": "Display Screen Equipment (DSE) & Environmental Responsibility",
                "body": "<p>UK law protects your physical health and the environment:</p><ul><li><strong>DSE Regulations:</strong> Employers must provide workstation risk assessments, adjustable chairs with lumbar support, anti-glare screen filters, and free regular eye tests for screen workers.</li><li><strong>Repetitive Strain Injury (RSI):</strong> Prevent wrist pain by using ergonomic mouse mats and keeping forearms horizontal.</li><li><strong>WEEE (Waste Electrical and Electronic Equipment):</strong> Old laptops, monitors, and printer cartridges contain hazardous toxic chemicals (lead, mercury). Never throw electronic hardware into household general rubbish — dispose of them through certified WEEE recycling schemes!</li></ul>",
                "ui_sim": {
                    "title": "DSE Health & Safety Checklist",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='display:flex; justify-content:space-between; margin-bottom:4px;'><span style='color:#0f172a;'><i class='fa-solid fa-check' style='color:#10b981;'></i> Adjustable chair with lower back support</span><span style='color:#10b981; font-weight:700;'>Compliant</span></div><div style='display:flex; justify-content:space-between; margin-bottom:4px;'><span style='color:#0f172a;'><i class='fa-solid fa-check' style='color:#10b981;'></i> Screen at eye level (arm's length)</span><span style='color:#10b981; font-weight:700;'>Compliant</span></div><div style='display:flex; justify-content:space-between;'><span style='color:#0f172a;'><i class='fa-solid fa-recycle' style='color:#0284c7;'></i> Dispose via certified WEEE recycling</span><span style='color:#0284c7; font-weight:700;'>Eco-Friendly</span></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A medical training coordinator is preparing a printed trainee handbook. They download medical diagrams from a commercial medical website and paste them into the handbook without contacting the creator. Explain whether this is permitted, and state one legal way the coordinator could find images they are allowed to use.",
            "steps": [
                {
                    "action": "Explain copyright violation",
                    "solution": "It is NOT permitted; it is a breach of copyright law to copy and distribute someone else's intellectual property without permission or a licence.",
                    "mark": "[B1]",
                    "rationale": "Correctly applies copyright restrictions to online media."
                },
                {
                    "action": "Provide legal alternative",
                    "solution": "Search for images under Creative Commons licences (or public domain / royalty-free stock libraries) that permit reuse with attribution.",
                    "mark": "[B1]",
                    "rationale": "Identifies Creative Commons as a legitimate licensing solution."
                }
            ],
            "tutor_rule": "In Level 1 exams, never assume images online are free. Always mention 'Copyright permission' or 'Creative Commons licences'."
        },
        "drills": [
            {
                "question": "What is the name of the licensing system that allows creators to permit public reuse of their images or articles with attribution?",
                "options": [
                    {"text": "Creative Commons (CC)", "correct": True},
                    {"text": "Recycle Bin", "correct": False},
                    {"text": "Operating System", "correct": False},
                    {"text": "Task Manager", "correct": False}
                ],
                "explanation": "Creative Commons licences provide standardised legal permissions for sharing and adapting creative works."
            },
            {
                "question": "Under UK Display Screen Equipment (DSE) regulations, what must an employer provide to employees who work on screens daily?",
                "options": [
                    {"text": "Workstation ergonomic risk assessments, adjustable seating, and regular eye tests", "correct": True},
                    {"text": "Free video game consoles", "correct": False},
                    {"text": "Free coffee every twenty minutes", "correct": False},
                    {"text": "A new smartphone every month", "correct": False}
                ],
                "explanation": "Health and Safety (DSE) regulations mandate ergonomic assessments, adjustable chairs, and eye examinations."
            },
            {
                "question": "Why must old computers, batteries, and monitors be disposed of via certified WEEE recycling facilities rather than ordinary household rubbish bins?",
                "options": [
                    {"text": "Electronics contain toxic chemicals and heavy metals (lead, mercury) that contaminate landfills and groundwater", "correct": True},
                    {"text": "Rubbish bins are too small to hold computers", "correct": False},
                    {"text": "Old computers explode if thrown in a wheelie bin", "correct": False},
                    {"text": "Bin lorries only collect paper", "correct": False}
                ],
                "explanation": "WEEE regulations ensure hazardous substances are safely handled and valuable materials are recycled."
            }
        ],
        "practice": {
            "task": "An office worker is experiencing persistent wrist and finger pain after typing for long hours each day. Name the condition they may be developing, and describe two ergonomic adjustments that can prevent this workplace health issue.",
            "scaffold_starter": "Condition: \nAdjustment 1: \nAdjustment 2: ",
            "model_answer": "Condition: Repetitive Strain Injury (RSI).\nAdjustment 1: Use an ergonomic keyboard and gel wrist rest to keep wrists straight while typing.\nAdjustment 2: Ensure forearms are horizontal with elbows at a 90-degree angle, and take frequent micro-breaks from typing to stretch fingers and wrists.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Naming Repetitive Strain Injury (RSI)."},
                {"tag": "[1 Mark]", "desc": "Describing wrist rests, forearm angles, or typing micro-breaks."}
            ]
        },
        "revision_links": [
            {"label": "UK GDPR & Data Protection", "href": "l1-uk-gdpr-data-protection-privacy.html"},
            {"label": "Cybersecurity & Malware Defence", "href": "l1-cybersecurity-malware-defence.html"},
            {"label": "Professional Word Formatting", "href": "l1-word-processing-professional.html"}
        ]
    }
]
