#!/usr/bin/env python3
"""
Appends DIGITAL_SKILLS_DATA and BKSB_REMEDIATION_DATA to books/a4/specialist_suite_content.py.
"""
import sys

data_code = '''
# =============================================================================
# Digital Skills (EDSQ National Standards) Units & Mocks Data
# =============================================================================

DIGITAL_SKILLS_UNITS = [
    # Domain 1: Using Devices & Handling Information
    {
        "unit": 1,
        "title": "Operating Systems, File Hierarchy & Cloud Storage",
        "domain": "Domain 1: Using Devices & Handling Information",
        "badge": "D1.1",
        "kw": "laptop computer keyboard modern workspace typing",
        "theory": (
            "<p><b>Operating Systems &amp; File Systems:</b> Modern workplace devices operate on Windows, macOS, ChromeOS, or mobile OS (iOS/Android). "
            "A structured hierarchical file architecture organises data into logical nested folders (e.g. <code>/Documents/Clients/2025/Invoices/</code>). "
            "Standard file naming conventions use ISO dates and clear descriptors (e.g. <code>2025-05-14_Invoice_SmithLtd_v2.pdf</code>) to avoid version confusion.</p>"
            "<p><b>Cloud Storage &amp; Synchronisation:</b> Cloud platforms (OneDrive, Google Drive, Nextcloud) synchronize local files to secure remote servers. "
            "This enables multi-device access, automated version history, and real-time multi-author collaboration with granular viewing/editing permissions.</p>"
        ),
        "steps": [
            "Create a root project folder with the standardized format: <code>YYYY-MM_ProjectName</code>.",
            "Establish logical subfolders: <code>01_Briefs</code>, <code>02_Working_Drafts</code>, <code>03_Assets</code>, <code>04_Final_Approved</code>.",
            "Apply read-only permissions to final distribution PDFs and full edit access to designated team members.",
            "Verify cloud synchronization status icons (green checkmark = synced locally, cloud icon = online only)."
        ],
        "drill": "Scenario: You are organizing the digital assets for a regional charity campaign. Outline a nested 3-tier folder structure, specify standard naming for 3 distinct files, and explain why saving directly to the Desktop causes governance risks.",
        "trap": "Examiner Trap: Saving multiple files named 'Draft1.docx', 'Draft_final.docx', 'Draft_real_final.docx' loses marks. Always use ISO dates and version numbers (v1.0, v1.1)!"
    },
    {
        "unit": 2,
        "title": "Advanced Search Syntax & Information Verification",
        "domain": "Domain 1: Using Devices & Handling Information",
        "badge": "D1.2",
        "kw": "search engine browser research internet",
        "theory": (
            "<p><b>Search Syntax &amp; Precision Filtering:</b> Professional workplace research requires targeted Boolean operators and search filters: "
            "quotes <code>\"exact phrase\"</code> for verbatim matching, <code>site:.gov.uk</code> to restrict results to verified government domains, "
            "<code>filetype:pdf</code> for official reports, and the minus operator <code>-keyword</code> to exclude irrelevant commercial results.</p>"
            "<p><b>CRAAP Evaluation Framework:</b> Not all online data is reliable. Candidates must evaluate information using the CRAAP test: "
            "<b>C</b>urrency (publication date), <b>R</b>elevance (matches research scope), <b>A</b>uthority (author credentials and domain reputation), "
            "<b>A</b>ccuracy (backed by cited evidence), and <b>P</b>urpose (identifying commercial bias vs objective research).</p>"
        ),
        "steps": [
            "Construct a targeted Boolean query: e.g. <code>\"apprenticeship minimum wage\" site:.gov.uk filetype:pdf</code>.",
            "Inspect the top 3 results for author credentials, publication date, and cited research references.",
            "Cross-reference key numerical claims against at least two independent primary statistical sources.",
            "Record the full URL, retrieval date, and author name for transparent professional citation."
        ],
        "drill": "Scenario: Your manager asks you to verify whether a viral social media post claiming a new statutory UK minimum wage rate is accurate. Formulate two search queries, identify the primary authority domain to check, and explain how to spot misinformation.",
        "trap": "Examiner Trap: Citing sponsored blog posts or commercial sales pages (.com) as official legislation evidence. Always cross-check against official (.gov.uk or .org.uk) repositories!"
    },

    # Domain 2: Creating & Editing
    {
        "unit": 3,
        "title": "Professional Word Processing & Structured Documents",
        "domain": "Domain 2: Creating & Editing",
        "badge": "D2.1",
        "kw": "typing document office word processing",
        "theory": (
            "<p><b>Document Hierarchy &amp; Styles:</b> Professional word processing (MS Word, Google Docs) relies on semantic paragraph styles "
            "(<code>Heading 1</code>, <code>Heading 2</code>, <code>Body Text</code>) rather than manual font resizing. "
            "Styles guarantee consistent typography, automatically generate clickable Tables of Contents, and maintain screen reader accessibility.</p>"
            "<p><b>Tables, Headers &amp; Page Architecture:</b> Long documents require structured headers and footers with automated page numbering "
            "(<code>Page X of Y</code>), balanced margins (minimum 20 mm), accessible data tables with dedicated header rows, and embedded high-resolution graphics with descriptive Alt-Text.</p>"
        ),
        "steps": [
            "Apply Heading 1 to primary chapters and Heading 2 to sub-sections to establish a logical outline.",
            "Insert an automated Table of Contents linked directly to heading styles.",
            "Format data into an accessible table: specify a repeating header row and zebra-stripe alternating shading for readability.",
            "Add descriptive alternative text (Alt-Text) to all photographic images to comply with WCAG accessibility standards."
        ],
        "drill": "Scenario: Format a 4-page health and safety executive briefing document. Specify font hierarchy (title, headings, body), explain the benefit of using Styles instead of manual bolding, and describe how to make a 5-column incident log table fully accessible.",
        "trap": "Examiner Trap: Hitting 'Enter' repeatedly to force text onto a new page. Always use a proper Page Break (Ctrl+Enter) or Section Break!"
    },
    {
        "unit": 4,
        "title": "Spreadsheet Architecture, Formulas & Data Visualisation",
        "domain": "Domain 2: Creating & Editing",
        "badge": "D2.2",
        "kw": "spreadsheet excel analytics chart data",
        "theory": (
            "<p><b>Spreadsheet Principles:</b> Spreadsheets (MS Excel, Google Sheets) manage numerical and tabular records across columns and rows. "
            "Formulas always begin with an equals sign (<code>=</code>) and use relative cell referencing (<code>=B2*C2</code>) or absolute cell referencing (<code>=$B$1*C2</code>) "
            "to automate calculations without manual data re-entry.</p>"
            "<p><b>Essential Formulas &amp; Functions:</b> Statutory Level 1 &amp; Level 2 standards require mastery of: "
            "<code>=SUM(range)</code> for totals, <code>=AVERAGE(range)</code> for arithmetic means, <code>=COUNT(range)</code> / <code>=COUNTA(range)</code>, "
            "<code>=MIN(range)</code> and <code>=MAX(range)</code>, and logical conditional expressions <code>=IF(logical_test, value_if_true, value_if_false)</code>.</p>"
        ),
        "steps": [
            "Enter clear column headers in Row 1: Item, Unit Cost, Quantity, Line Total, Reorder Status.",
            "Apply formula <code>=B2*C2</code> to calculate line total, then double-click the fill handle to auto-populate the column.",
            "Calculate summary metrics in the bottom row using <code>=SUM(D2:D50)</code> and <code>=AVERAGE(B2:B50)</code>.",
            "Apply an IF function to column E: <code>=IF(C2<10, \"REORDER\", \"OK\")</code>.",
            "Select the data range and generate a clean Column or Bar Chart with labeled axes and a descriptive chart title."
        ],
        "drill": "Scenario: Create an inventory management sheet for 20 warehouse product lines. Show the exact formulas for Line Total, Overall Spend, Average Unit Cost, and an automated 'Low Stock' alert for any item with under 15 units remaining.",
        "trap": "Examiner Trap: Typing hardcoded numbers into a formula (e.g. '=B2*12.50') instead of referencing cells. Always keep variable rates in separate parameter cells!"
    },
    {
        "unit": 5,
        "title": "Presentation Design, Multimedia & Digital Accessibility",
        "domain": "Domain 2: Creating & Editing",
        "badge": "D2.3",
        "kw": "presentation slide deck meeting projector",
        "theory": (
            "<p><b>Visual Storytelling &amp; Cognitive Load:</b> Effective slide presentations (PowerPoint, Google Slides) communicate complex ideas succinctly. "
            "Avoid wall-of-text slides; adhere to the 6x6 guideline (maximum 6 bullet points, maximum 6 words per bullet). "
            "Use high-contrast color palettes (dark text on white/cream backgrounds) and legible sans-serif typography (Arial, Calibri, Montserrat) at 24pt+ for readability.</p>"
            "<p><b>Multimedia Integration &amp; Accessibility:</b> Audio and video clips must be compressed and formatted with closed captions. "
            "Ensure all visual graphics have Alt-Text descriptions. Never use colour as the sole visual indicator of status (e.g. combine green/red icons with text labels 'Pass' / 'Fail').</p>"
        ),
        "steps": [
            "Select a clean, accessible presentation template with high contrast and consistent slide masters.",
            "Summarise source data into 3 key bullet takeaways accompanied by a clear, high-resolution infographic.",
            "Embed audio/video files and verify that automatic playback and subtitling are enabled.",
            "Run the built-in Accessibility Checker to detect missing alternative text or low-contrast warnings."
        ],
        "drill": "Scenario: Design a 5-slide induction deck for new healthcare apprentices. Outline slide titles, bullet point content for Slide 2, and explain 3 design choices made to ensure the presentation is accessible to visually impaired learners.",
        "trap": "Examiner Trap: Using distracting animations and transition effects that detract from readability. Keep transitions simple, subtle, and consistent!"
    },

    # Domain 3: Communicating
    {
        "unit": 6,
        "title": "Professional Email Etiquette, Attachments & Scheduling",
        "domain": "Domain 3: Communicating",
        "badge": "D3.1",
        "kw": "email laptop office communication sending message",
        "theory": (
            "<p><b>Workplace Email Protocols:</b> Business email requires precise communication conventions: a concise, informative subject line "
            "(e.g. <code>Action Required: Q3 Budget Review Meeting – 14 June</code>), professional salutations (<code>Dear Mr Davies,</code> / <code>Good morning Sarah,</code>), "
            "and appropriate closing sign-offs. Understand recipient fields: <b>To</b> for primary action owners, <b>Cc</b> (Carbon Copy) for informational awareness, "
            "and <b>Bcc</b> (Blind Carbon Copy) for mass distributions to preserve recipient data privacy under UK GDPR.</p>"
            "<p><b>Calendar Scheduling &amp; Secure Attachments:</b> Scheduling meetings via digital calendars (Outlook, Google Calendar) requires checking attendee availability "
            "via scheduling assistants, including agenda points, and attaching meeting links. Before attaching files, compress large folders into .zip archives and verify that "
            "sensitive documents are password-encrypted.</p>"
        ),
        "steps": [
            "Compose a clear subject line indicating priority and topic.",
            "Draft message using concise paragraphs, bullet points for action items, and professional register.",
            "Use Bcc when sending newsletters or group announcements to protect individual email addresses from public exposure.",
            "Verify file size of attachments (under 10MB) and ensure file names are professional and descriptive."
        ],
        "drill": "Scenario: You need to send a confidential staffing rota to 30 care home operatives. Draft the email, explain why Bcc must be used instead of To/Cc, and detail how you will securely password-protect the spreadsheet attachment.",
        "trap": "Examiner Trap: Hitting 'Reply All' on company-wide announcements. Only reply to the sender unless everyone genuinely needs the update!"
    },
    {
        "unit": 7,
        "title": "Video Conferencing, Collaboration Tools & Netiquette",
        "domain": "Domain 3: Communicating",
        "badge": "D3.2",
        "kw": "video conference call remote meeting screen headset",
        "theory": (
            "<p><b>Virtual Meeting Platforms:</b> Platforms like MS Teams, Zoom, and Google Meet are integral to remote teamwork. "
            "Professional meeting management involves setting meeting roles (Presenter vs Attendee), testing microphone/camera peripherals prior to commencement, "
            "and using background blur or neutral virtual backgrounds to preserve home privacy.</p>"
            "<p><b>Collaboration Netiquette:</b> Maintain virtual etiquette by keeping microphones muted when not speaking to eliminate background ambient noise, "
            "using the 'Raise Hand' feature to avoid interrupting speakers, and utilizing chat channels for resource links and constructive feedback. "
            "Respect digital boundaries by recording sessions only with explicit participant consent.</p>"
        ),
        "steps": [
            "Perform audio/video check 5 minutes before scheduled call start time.",
            "Enable background blur to ensure a professional, distraction-free appearance.",
            "Mute microphone upon entering and unmute only when addressing the meeting.",
            "Share screen selectively (share individual application window rather than entire desktop to prevent accidental personal data display)."
        ],
        "drill": "Scenario: You are co-hosting a virtual workshop for 25 external clients. List the 4 key setup steps you must perform before admitting attendees from the lobby, and explain how to handle an unexpected participant disruption.",
        "trap": "Examiner Trap: Sharing your entire desktop screen containing private browser tabs, emails, or personal photos. Always share only the specific presentation window!"
    },

    # Domain 4: Transacting
    {
        "unit": 8,
        "title": "E-Commerce, Online Invoicing & Secure Payment Verification",
        "domain": "Domain 4: Transacting",
        "badge": "D4.1",
        "kw": "credit card payment online shopping pos terminal",
        "theory": (
            "<p><b>Digital Commercial Transactions:</b> Purchasing products and services online requires robust security verification. "
            "Ensure the website URL begins with <code>https://</code> (Hypertext Transfer Protocol Secure) and displays a locked padlock icon in the browser address bar, "
            "confirming that data transmitted between browser and web server is encrypted using TLS/SSL protocols.</p>"
            "<p><b>Payment Security &amp; Fraud Prevention:</b> When entering payment card details, verify that the transaction requires Strong Customer Authentication (SCA) "
            "via 3D Secure (e.g. one-time passcode SMS or banking app biometric approval). Never store commercial card details on shared devices, and reconcile digital invoices "
            "against merchant receipts before approving payments.</p>"
        ),
        "steps": [
            "Verify website credentials: check for <code>https://</code>, valid SSL security certificate, and company registration details.",
            "Review transaction basket: confirm quantities, VAT charges, and delivery fee calculations before proceeding.",
            "Complete checkout using a secure payment gateway or protected digital wallet (Apple Pay, Google Pay, PayPal).",
            "Save and archive the generated digital PDF receipt and order confirmation reference number."
        ],
        "drill": "Scenario: Your office manager asks you to purchase &pound;450 of office supplies from a new online supplier. Explain 4 distinct security checks you must perform before entering company credit card details.",
        "trap": "Examiner Trap: Assuming a padlock icon proves a website is 100% legitimate. Padlocks prove the connection is encrypted, but you must still check the domain name carefully to spot spoofed fake websites!"
    },
    {
        "unit": 9,
        "title": "Digital Public Services & Official Online Accounts",
        "domain": "Domain 4: Transacting",
        "badge": "D4.2",
        "kw": "government office passport document citizen services",
        "theory": (
            "<p><b>Accessing Public Services Online:</b> Government and public health services in the UK are centralised through Gov.uk and NHS App portals. "
            "Accessing services (e.g. Universal Credit, DVLA vehicle tax, Council Tax billing, NHS prescriptions) requires verified digital identity accounts "
            "utilising multi-factor authentication (MFA) and National Insurance number verification.</p>"
            "<p><b>Online Form Completion &amp; Document Uploads:</b> Completing digital public service applications requires entering accurate biographical details, "
            "uploading proof-of-address documents (.pdf or .jpg formats, typically under 5MB), and verifying that all input fields pass client-side data validation checks "
            "(e.g. valid postcode format, correctly formatted telephone numbers).</p>"
        ),
        "steps": [
            "Log in via official portal gateway: verify the domain ends strictly in <code>.gov.uk</code> or <code>.nhs.uk</code>.",
            "Authenticate account using SMS one-time passcode or authenticator app token.",
            "Complete form sections sequentially, checking progress indicators and error validation highlights.",
            "Upload compressed, clear PDF copies of required utility bill or driving licence verification documents.",
            "Submit application and record the unique statutory reference tracking code."
        ],
        "drill": "Scenario: An adult learner needs to renew their driving licence and apply for an NHS prescription online. Detail the steps required to access the genuine Gov.uk portal, verify identity, and avoid predatory copycat charging websites.",
        "trap": "Examiner Trap: Using unofficial third-party websites that charge &pound;40–&pound;80 handling fees for free Gov.uk services. Always check that the URL domain ends in .gov.uk!"
    },

    # Domain 5: Being Safe & Responsible Online
    {
        "unit": 10,
        "title": "Cybersecurity Hygiene, Phishing Detection & UK GDPR",
        "domain": "Domain 5: Being Safe & Responsible Online",
        "badge": "D5.1",
        "kw": "cyber security lock digital privacy shield hacker",
        "theory": (
            "<p><b>Cyber Threats &amp; Social Engineering:</b> The vast majority of cyber breaches stem from human deception rather than technical flaws. "
            "<b>Phishing:</b> Fraudulent emails imitating banks, delivery couriers, or HMRC attempting to harvest login credentials. "
            "Key red flags include urgent threatening language (<i>'Your account will be suspended within 24 hours'</i>), generic greetings (<i>'Dear Customer'</i>), "
            "and spoofed sender email addresses (e.g. <code>support@paypal-security-alert.co.uk</code> instead of <code>@paypal.com</code>).</p>"
            "<p><b>Password Security &amp; 2FA:</b> Create strong, memorable passphrases using three random words combined with numbers and symbols (e.g. <code>Castle$Pebble97Breeze!</code>). "
            "Enable Two-Factor Authentication (2FA) across all professional accounts. "
            "<b>UK GDPR &amp; Data Protection:</b> Handle personal identifiable data (PID) strictly according to the 7 UK GDPR principles: lawfulness, purpose limitation, "
            "data minimisation, accuracy, storage limitation, integrity/confidentiality, and accountability.</p>"
        ),
        "steps": [
            "Hover mouse over hyperlinks in emails to reveal the actual destination URL before clicking.",
            "Verify sender header email address carefully to detect domain spoofing.",
            "Implement multi-factor authentication (MFA) across email, banking, and cloud storage systems.",
            "Never share passwords via unencrypted messaging apps or write them on sticky notes.",
            "Immediately report suspected security incidents or accidental data disclosures to the Data Protection Officer (DPO)."
        ],
        "drill": "Scenario: You receive an urgent email purporting to be from the IT Support team requesting you to verify your employee email password via an external link. Identify 3 warning signs of phishing and outline your exact response protocol.",
        "trap": "Examiner Trap: Believing that anti-virus software alone provides complete protection. Human vigilance and skepticism are the ultimate line of defence against social engineering!"
    }
]

DIGITAL_SKILLS_MOCKS = [
    # Mock 1: Administrative Officer Cloud & File Management
    {
        "title": "Practical Mock 1: Administrative Operations & Document Processing",
        "scenario": "You are working as an Administrative Officer for a regional vocational training academy. "
                    "The centre manager has tasked you with auditing and restructuring the new apprentice onboarding digital toolkit.",
        "tasks": [
            "Task 1: Establish a standardized hierarchical folder structure for 30 new apprentices across 3 vocational sectors (Healthcare, Engineering, Digital).",
            "Task 2: Format an Apprentice Induction Handbook in Word using styles (Title, Heading 1, Heading 2), inserting an automated Table of Contents and an accessible table of key dates.",
            "Task 3: Conduct research to identify statutory minimum wage rates for apprentices, citing two verified .gov.uk sources using proper search operators.",
            "Task 4: Draft a professional welcome email to apprentices using appropriate To, Cc, and Bcc fields to distribute the handbook while protecting private personal email addresses."
        ]
    },
    # Mock 2: Retail Inventory Spreadsheet & Commercial Invoicing
    {
        "title": "Practical Mock 2: Retail Inventory Spreadsheet & Commercial Accounting",
        "scenario": "You are the Operations Assistant for a growing eco-friendly home goods retailer. "
                    "The business needs a dynamic, automated inventory tracking and customer billing spreadsheet.",
        "tasks": [
            "Task 1: Construct an inventory management spreadsheet with 15 stock lines, applying formulas for Line Total (=Unit Cost * Quantity), VAT at 20%, and Gross Retail Value.",
            "Task 2: Use summary formulas =SUM, =AVERAGE, =MIN, and =MAX to extract key operational metrics across the stock inventory.",
            "Task 3: Apply an automated =IF function to Column G to flag 'RESTOCK REQUIRED' for any item falling below 12 units.",
            "Task 4: Generate a high-contrast Clustered Bar Chart illustrating stock value by product category, complete with labeled axes and data labels."
        ]
    },
    # Mock 3: Customer Care Digital Helpdesk & Data Privacy
    {
        "title": "Practical Mock 3: Digital Customer Care & Secure Communications",
        "scenario": "You are a Customer Experience Coordinator for a community health trust. "
                    "You must handle digital communications, appointment scheduling, and patient data requests with strict adherence to privacy.",
        "tasks": [
            "Task 1: Schedule a series of virtual consultation meetings in MS Teams, configuring presenter permissions, lobby security, and calendar invites.",
            "Task 2: Respond to a patient inquiry via email, maintaining empathetic professional register and attaching a guidance document encrypted with password protection.",
            "Task 3: Identify a suspicious incoming email claiming to represent NHS procurement, documenting 4 clear phishing indicators in an incident log.",
            "Task 4: Outline the procedure for handling a Subject Access Request (SAR) under UK GDPR, specifying the statutory response deadline (1 calendar month)."
        ]
    },
    # Mock 4: Corporate Data Security Audit & Cloud Governance
    {
        "title": "Practical Mock 4: Corporate Data Security Audit & Technology Governance",
        "scenario": "You are supporting the Information Governance lead in preparing an organization for Cyber Essentials certification and statutory data compliance.",
        "tasks": [
            "Task 1: Conduct a password hygiene and 2FA compliance audit across 40 user accounts, identifying 5 critical security vulnerabilities.",
            "Task 2: Formulate an acceptable cloud storage policy restricting the storage of sensitive personal data on unencrypted personal mobile devices.",
            "Task 3: Evaluate 3 online payment gateway solutions for the corporate website, verifying SSL/TLS certificates and PCI-DSS compliance.",
            "Task 4: Create a 6-slide staff training presentation on social engineering awareness, applying WCAG 2.1 accessibility standards and Alt-Text graphics."
        ]
    }
]

print("DIGITAL_SKILLS_UNITS (10) and DIGITAL_SKILLS_MOCKS (4) defined successfully!")
'''

with open('books/a4/specialist_suite_content.py', 'a') as f:
    f.write(data_code)

print("Appended DIGITAL_SKILLS_DATA to specialist_suite_content.py!")
