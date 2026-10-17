#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Digital Functional Skills Batch 3
2 Curriculum Topics:
1. digital-functional-skills-level-1-revision
2. entry-level-3-digital-skills
"""

DIGITAL_BATCH3_WORKOUTS = {
    # 1. DIGITAL FUNCTIONAL SKILLS LEVEL 1 REVISION
    "digital-functional-skills-level-1-revision": {
        "title": "Digital Level 1 Comprehensive Revision",
        "slug": "digital-functional-skills-level-1-revision",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel / Ofqual Digital Functional Skills: Level 1 (All 5 Skill Areas)",
        "level": "Level 1",
        "method_card": {
            "title": "The 5 Digital Functional Skills Domains",
            "points": [
                "Domain 1 (Using Devices & Handling Information): File paths, file management (move, rename, delete), storage units (KB < MB < GB < TB), cloud vs local storage.",
                "Domain 2 (Creating & Editing): Word processing formatting, table design, spreadsheet formulas (=SUM, =AVERAGE, =COUNT), charts.",
                "Domain 3 (Communicating): Professional email etiquette, subject lines, attachments, CC vs BCC, messaging platforms.",
                "Domain 4 (Transacting): Online shopping, booking appointments, online banking, digital forms, identity verification.",
                "Domain 5 (Being Safe & Responsible): Strong passwords, two-factor authentication (2FA), recognizing phishing emails, privacy settings, UK GDPR compliance."
            ],
            "calc_tip": "Remember: BCC (Blind Carbon Copy) hides recipient email addresses from other recipients, ensuring GDPR privacy compliance."
        },
        "workout_blocks": [
            {
                "title": "Data Storage and File Extensions",
                "instruction": "State the standard file type or evaluate the storage size:",
                "items": [
                    ("a", "Which file extension represents a spreadsheet workbook?", ".xlsx (or .csv)"),
                    ("b", "Which file extension represents a portable document format for printing?", ".pdf"),
                    ("c", "Order by storage capacity from smallest to largest: 1 GB, 500 MB, 2 TB, 800 KB", "800 KB < 500 MB < 1 GB < 2 TB"),
                    ("d", "How many Megabytes (MB) are approximately in 1 Gigabyte (GB)?", "1,000 MB (1,024 MB)"),
                    ("e", "Where is data stored when using Microsoft OneDrive or Google Drive?", "Cloud storage (remote secure servers)")
                ]
            },
            {
                "title": "Spreadsheet Formulas & Email Security",
                "instruction": "State the exact spreadsheet formula or security action required:",
                "items": [
                    ("a", "Formula to calculate the total sum of cells B2 to B12", "=SUM(B2:B12)"),
                    ("b", "Formula to find the average value of cells C4 to C20", "=AVERAGE(C4:C20)"),
                    ("c", "Which email field should be used to email 50 patients without exposing their email addresses to each other?", "BCC (Blind Carbon Copy)"),
                    ("d", "What should you do if an email urges you to 'Click here immediately to verify your account or be suspended'?", "Do not click links; report as suspected phishing to IT security")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Administrative Email & Data Security",
                "stem": "A medical receptionist needs to email an updated clinical appointment schedule to <strong>45 independent community patients</strong>.<br>The email includes an attached PDF document containing appointment dates.<br>(a) Which email field (To, CC, or BCC) must the receptionist place the 45 patient email addresses in, and explain why under UK GDPR data protection rules.<br>(b) State two essential checks the receptionist should carry out on the attachment before clicking 'Send'.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify email field: BCC (Blind Carbon Copy)", "[D1]"),
                    ("Explain GDPR rationale: Prevents sharing patients' personal identifiable contact details with other recipients, ensuring confidentiality", "[D1]"),
                    ("Attachment checks: 1. Verify correct document is attached (no confidential data belonging to other individuals). 2. Check file format is accessible (.pdf) and file size is under email limit", "[A1]")
                ],
                "final_answer": "(a) BCC: Under UK GDPR, patient email addresses are personal data; using BCC prevents exposing private email addresses to strangers. (b) 1. Check correct file is attached (prevent data breach). 2. Confirm document opens and contains no unauthorized patient records.",
                "reverse_check": "Complies strictly with UK data protection and cyber security best practice.",
                "pitfall": "Suggesting 'CC' or 'To' for group patient communication."
            }
        ]
    },

    # 2. ENTRY LEVEL 3 DIGITAL SKILLS
    "entry-level-3-digital-skills": {
        "title": "Entry Level 3 Digital Skills",
        "slug": "entry-level-3-digital-skills",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel / Ofqual Digital Functional Skills: Entry Level 3",
        "level": "Entry Level 3",
        "method_card": {
            "title": "Core Digital Competencies for Entry Level 3",
            "points": [
                "Hardware Basics: Keyboard, mouse, touchscreen, monitor, power button, USB port.",
                "Basic Navigation: Turning a computer on/off, opening an application from desktop or start menu, scrolling.",
                "Entering Information: Typing text with capital letters (Shift key), punctuation, backspace, and spacebar.",
                "Internet Basics: Typing a web address (URL) into an address bar, using a search engine, clicking hyperlinks.",
                "Digital Safety: Creating a private password, never sharing passwords with strangers, logging off shared public computers."
            ],
            "calc_tip": "Remember: Always click the address bar at the very top of the browser to enter a website address, not the search box."
        },
        "workout_blocks": [
            {
                "title": "Hardware and Desktop Basics",
                "instruction": "State the hardware part or keyboard key used for the task:",
                "items": [
                    ("a", "Key pressed to create a capital letter or symbol", "Shift key (or Caps Lock)"),
                    ("b", "Key pressed to erase a mistake to the left of the cursor", "Backspace key"),
                    ("c", "Key pressed to move down onto a new line in a document", "Enter / Return key"),
                    ("d", "Device used to point, click, and drag items on a desktop screen", "Mouse (or touchpad)"),
                    ("e", "Port used to plug in a memory stick or external mouse", "USB port")
                ]
            },
            {
                "title": "Digital Safety and Passwords",
                "instruction": "State whether each practice is Safe or Unsafe:",
                "items": [
                    ("a", "Using 'password123' for your online banking account", "Unsafe (too weak and easily guessed)"),
                    ("b", "Creating a password with letters, numbers, and symbols (e.g. BlueSky#84!)", "Safe (strong combination)"),
                    ("c", "Writing your password on a sticky note attached to your computer monitor", "Unsafe"),
                    ("d", "Logging out of your account on a public library computer when finished", "Safe (prevents unauthorised access)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Community Clinic Public Kiosk Navigation",
                "stem": "A patient uses a digital check-in touch screen kiosk at a community health clinic.<br>The screen asks the patient to:<br>1. Tap the screen to begin<br>2. Type in their date of birth using an on-screen numerical keypad<br>3. Confirm their appointment time<br><br>(a) If the patient makes a typing mistake on the numerical keypad, what button should they press to erase the last number?<br>(b) Why should the patient tap 'Done / Log out' on the screen after checking in before walking away?",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Identify correction button: Backspace / Clear / Erase button", "[D1]"),
                    ("Explain privacy reason: Prevents the next person in line from seeing personal identifying health details on the screen", "[A1]")
                ],
                "final_answer": "(a) Backspace / Delete / Clear button | (b) To protect their personal privacy and confidentiality so the next person in the queue cannot see their medical details.",
                "reverse_check": "Realistic patient kiosk digital skill application.",
                "pitfall": "Telling the patient to turn off the power button instead of pressing clear/backspace."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Loaded {len(DIGITAL_BATCH3_WORKOUTS)} topics in authentic_workouts_digital_batch3.py")
