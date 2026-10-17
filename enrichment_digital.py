# Enrichment blocks for Digital Functional Skills (DFS) topics to guarantee >= 30 questions per worksheet.
# Covers all 7 DFS topics with authentic workplace digital technology tasks and online safety scenarios.

ENRICHMENT_DIGITAL = {
    "digital-functional-skills": [
        {
            "title": "Question 4: Cloud Storage, Backups & Digital File Management",
            "instruction": "Identify the correct digital practice or tool for handling workplace information:",
            "items": [
                ("a", "Which storage solution allows multiple team members to edit a spreadsheet simultaneously in real time?", "Cloud storage (e.g. Microsoft OneDrive, Google Drive, Nextcloud)"),
                ("b", "What is the primary benefit of maintaining an automatic off-site cloud backup of patient records?", "Disaster recovery: protects data if physical on-site computers are damaged by fire, flood, or theft"),
                ("c", "Which folder hierarchy follows professional file management best practices?", "Department > Year > Month > Specific_Project_Name (structured and logical)"),
                ("d", "What is the risk of saving critical clinical files exclusively to a local computer Desktop?", "High risk of permanent data loss if the computer crashes or drive is corrupted"),
                ("e", "Which file extension is best for distributing non-editable, cross-platform official policy documents?", ".pdf (Portable Document Format)"),
                ("f", "Why should file names avoid special characters like * / ? < > : \" | ?", "They are reserved operating system characters and cause file saving or sync errors"),
                ("g", "What does 'version control' (e.g. Handover_Log_v2.1) prevent in a shared workplace drive?", "Prevents team members accidentally overwriting each other's changes or using outdated procedures"),
                ("h", "How should you securely delete confidential patient spreadsheets before discarding an old laptop?", "Use certified cryptographic digital wiping / physical drive destruction, not just emptying recycle bin")
            ]
        },
        {
            "title": "Question 5: Cybersecurity, Phishing & Multi-Factor Authentication",
            "instruction": "Assess the online security scenario and determine the appropriate action:",
            "items": [
                ("a", "You receive an email from 'IT-Helpdesk@hotm-services.com' asking you to click a link to verify your hospital login", "Phishing scam: check sender domain, do not click links, report immediately to IT security"),
                ("b", "What makes a password strong and resistant to brute-force automated cyberattacks?", "Minimum 12-16 characters combining uppercase, lowercase, numbers, and special symbols (or passphrase)"),
                ("c", "How does Multi-Factor Authentication (MFA / 2FA) protect your NHS account if a password is leaked?", "Requires a secondary physical token or authenticator app code that the attacker does not have"),
                ("d", "What should you do before entering corporate credit card details on an online supplier's checkout page?", "Verify HTTPS protocol (padlock icon in browser URL bar) and check domain authenticity"),
                ("e", "Why is connecting to open, unencrypted public Wi-Fi at a train station dangerous for patient data?", "Network traffic can be intercepted by hackers on the same network ('man-in-the-middle' attack)"),
                ("f", "What is ransomware, and how can an organization minimize the disruption it causes?", "Malware that encrypts files and demands ransom; minimized through regular offline immutable backups"),
                ("g", "Why should you never leave your NHS smartcard inserted into a computer terminal when walking away?", "Enables unauthorized individuals to access confidential records under your legal credentials"),
                ("h", "What is the purpose of software updates and security patches released by operating systems?", "Fixes known security vulnerabilities and exploits that hackers use to infiltrate devices")
            ]
        }
    ],

    "digital-functional-skills-level-1": [
        {
            "title": "Question 3: Word Processing & Professional Document Formatting",
            "instruction": "Identify the word processing tool or formatting command for each task:",
            "items": [
                ("a", "Which formatting tool aligns text with both the left and right margins cleanly?", "Justify alignment"),
                ("b", "How do you repeat a hospital logo and confidentiality notice at the top of every page automatically?", "Insert Header"),
                ("c", "Which feature helps locate and replace every instance of an obsolete drug name across a 40-page report?", "Find and Replace (Ctrl + H)"),
                ("d", "Why should line spacing be set to 1.5 rather than 1.0 in accessible workplace policies?", "Improves readability and reduces visual crowding, especially for readers with dyslexia"),
                ("e", "Which tool creates an automated, clickable list of page numbers based on document Heading styles?", "Table of Contents"),
                ("f", "How can you present a list of six steps that must be carried out in exact chronological order?", "Numbered list"),
                ("g", "Which command allows you to copy formatting (font, size, colour) from one sentence directly to another?", "Format Painter"),
                ("h", "Why should you use Page Break (Ctrl + Enter) instead of pressing Enter repeatedly to start a new page?", "Prevents text from shifting downwards when edits are made to preceding pages")
            ]
        },
        {
            "title": "Question 4: Spreadsheet Formulas & Basic Data Calculation",
            "instruction": "Write the exact spreadsheet formula required for each calculation (assuming cell coordinates given):",
            "items": [
                ("a", "Calculate the total sum of sales in cells B2 to B15", "=SUM(B2:B15)"),
                ("b", "Calculate the average patient waiting time in cells C4 to C20", "=AVERAGE(C4:C20)"),
                ("c", "Find the highest temperature recorded in column D from D2 to D30", "=MAX(D2:D30)"),
                ("d", "Find the lowest recorded daily blood pressure in cells E2 to E18", "=MIN(E2:E18)"),
                ("e", "Multiply the hourly rate in cell B3 by the hours worked in cell C3", "=B3*C3"),
                ("f", "Subtract the discount in cell D2 from the subtotal in cell C2", "=C2-D2"),
                ("g", "Calculate 20% VAT on the net total in cell E5", "=E5*0.2 (or =E5*20%)"),
                ("h", "Count the number of numeric entries in cells A1 to A50", "=COUNT(A1:A50)")
            ]
        },
        {
            "title": "Question 5: Digital Communication Channels & Netiquette",
            "instruction": "Select the appropriate communication channel and etiquette rule for each scenario:",
            "items": [
                ("a", "Urgent time-critical patient emergency on Ward 4 requiring immediate crash team response", "Emergency panic alarm / Internal crash bleep (instant audio-visual dispatch)"),
                ("b", "Sending formal contract terms and conditions to an external legal contractor", "Workplace email with attached password-protected PDF"),
                ("c", "Quick non-urgent check with a desk colleague asking if they want a cup of tea", "Instant messaging / Teams chat"),
                ("d", "Why is typing an entire email in CAPITAL LETTERS considered poor digital netiquette?", "Perceived as aggressive shouting and is difficult for visually impaired users to read"),
                ("e", "When should you use 'Bcc' (Blind Carbon Copy) when emailing external clients?", "When sending to multiple external recipients to prevent sharing their email addresses publicly (GDPR compliance)"),
                ("f", "What is the risk of using 'Reply All' when responding to a company-wide announcement?", "Clutters inboxes for hundreds of colleagues with irrelevant personal confirmations"),
                ("g", "Why should you always include a concise descriptive subject line in professional emails?", "Enables recipients to prioritize urgencies and locate past conversations via search"),
                ("h", "What should you set up before taking two weeks of annual leave from work?", "Automatic Out-of-Office auto-responder with return date and alternative contact details")
            ]
        }
    ],

    "digital-functional-skills-level-1-revision": [
        {
            "title": "Question 2: Operating Systems, Peripherals & Hardware Diagnostics",
            "instruction": "Identify the hardware component or diagnostic solution for the computing issue:",
            "items": [
                ("a", "Computer monitor display is completely black, and the power light is off", "Check physical power cable connection to wall socket and ensure power switch is toggled on"),
                ("b", "Wireless mouse cursor is freezing and lagging erratically across the desktop", "Replace mouse batteries or clean optical sensor on underside"),
                ("c", "Which port type is standard for connecting modern monitors, projectors, and televisions?", "HDMI (High-Definition Multimedia Interface) or DisplayPort"),
                ("d", "Which hardware component temporarily holds active applications and data currently in use?", "RAM (Random Access Memory)"),
                ("e", "What is the function of an operating system (e.g. Windows, macOS, Linux)?", "Manages hardware resources, runs application software, and provides user interface"),
                ("f", "Why does a paper jam occur in an office laser printer, and how should it be cleared?", "Paper misfeed or damp sheets; clear by opening cover and gently pulling in direction of paper path"),
                ("g", "What device converts physical paper medical records into digital image files?", "Optical scanner"),
                ("h", "Why should a USB flash drive be 'Safely Removed / Ejected' before unplugging it from a PC?", "Ensures all cached write operations complete to prevent file corruption")
            ]
        },
        {
            "title": "Question 3: Spreadsheets - Formatting, Sorting & Filtering",
            "instruction": "Explain the spreadsheet feature and its practical workplace benefit:",
            "items": [
                ("a", "What does 'Currency formatting' (e.g. £1,250.00) apply to a raw numeric cell containing 1250?", "Adds currency symbol (£), comma thousands separator, and two decimal places"),
                ("b", "How does 'Sort A to Z' help an administrator managing a list of 500 patient records?", "Organizes surnames alphabetically for rapid manual searching and filing"),
                ("c", "What does applying a 'Filter' to a column of invoice statuses allow you to do?", "Display only specific rows (e.g. show only 'Overdue' invoices while hiding 'Paid')"),
                ("d", "Why is 'Wrap Text' used on long column headers in a spreadsheet table?", "Displays text across multiple lines within the cell so columns do not have to be excessively wide"),
                ("e", "What does the '$' symbol do in a formula like =B4*$C$1?", "Creates an Absolute Cell Reference so cell C1 remains fixed when copying the formula down"),
                ("f", "Which chart type is best for showing proportions of a whole hospital budget?", "Pie chart"),
                ("g", "Which chart type is best for showing temperature fluctuations over a 24-hour period?", "Line graph"),
                ("h", "Why should gridlines be enabled when printing a large spreadsheet table?", "Provides visual row and column guidelines so numbers can be tracked accurately across the page")
            ]
        },
        {
            "title": "Question 4: Online Safety, Privacy Settings & Digital Footprints",
            "instruction": "State the correct privacy rule or online safety measure:",
            "items": [
                ("a", "What is a 'digital footprint' and how can it impact vocational employment opportunities?", "The permanent trail of data left by online activity; employers review social posts during hiring"),
                ("b", "Why should you review privacy settings on personal social media accounts to 'Friends Only'?", "Prevents strangers, commercial data brokers, and employers viewing private personal posts"),
                ("c", "What are browser 'cookies', and what is the difference between essential and tracking cookies?", "Small text files stored by sites; essential enable logins/baskets, tracking profile browsing for ads"),
                ("d", "Why should you never share your date of birth, home address, and mother's maiden name publicly online?", "They are common security verification questions used to commit identity fraud"),
                ("e", "What should you do if an unfamiliar pop-up banner screams 'YOUR PC IS INFECTED WITH 5 VIRUSES!'?", "Do not click; close browser tab via Task Manager or window close; it is malicious scareware"),
                ("f", "How does a VPN (Virtual Private Network) protect remote healthcare workers logging in from home?", "Encrypts all internet traffic between the remote laptop and the hospital network"),
                ("g", "What is phishing via SMS text messages commonly called?", "Smishing"),
                ("h", "Why must you log out of shared computers in university or workplace hot-desking spaces?", "Prevents the next user accessing your open email, personal files, and saved passwords")
            ]
        }
    ],

    "digital-functional-skills-mock-exam": [
        {
            "title": "Question 3: Real-World Exam Task Simulation - Creating & Editing Digital Content",
            "instruction": "State the correct digital tool or method to solve the scenario task:",
            "items": [
                ("a", "You must prepare a 5-slide presentation for the hospital trust board. Which software is designed for this?", "Presentation software (e.g. Microsoft PowerPoint, Google Slides, Keynote)"),
                ("b", "How do you ensure all slides share the same hospital branding, fonts, and logo placement?", "Apply a Slide Master template"),
                ("c", "You need to crop an image to remove background clutter before inserting it into a leaflet. Which tool do you use?", "Image Crop tool"),
                ("d", "How do you combine four cells across a table header into one single wide title cell?", "Merge Cells"),
                ("e", "You need to export a digital newsletter so that external recipients cannot accidentally modify the text.", "Export / Save As PDF"),
                ("f", "How do you make text wrap neatly around an inserted photograph in a word processor?", "Set Text Wrapping to 'Square' or 'Tight'"),
                ("g", "Which tool checks your document for spelling typos and grammatical errors before submission?", "Spelling and Grammar Check (F7)"),
                ("h", "How can you compress a folder of 20 high-resolution photos so it can be sent via email?", "Compress / Zip the folder (.zip format)")
            ]
        },
        {
            "title": "Question 4: Transacting Online & Digital Verification",
            "instruction": "Identify the security checks and procedures for online transactions:",
            "items": [
                ("a", "How can you verify that an e-commerce shopping website is legitimate and safe?", "Check for https://, company registration details, physical address, and independent reviews"),
                ("b", "What is a Card Security Code (CVV / CVC) and where is it located on a debit card?", "A 3-digit security verification number printed on the signature strip on the back of the card"),
                ("c", "Why do banks send an OTP (One-Time Passcode) via SMS or banking app during an online purchase?", "Two-factor payment authentication to verify that the registered cardholder authorized the transaction"),
                ("d", "What is the benefit of paying for expensive equipment via credit card rather than direct bank transfer?", "Statutory legal protection (Section 75 Consumer Credit Act) against faulty goods or company insolvency"),
                ("e", "What should you save and print immediately after completing an online trade order?", "The transaction confirmation page with order reference number and itemized VAT receipt"),
                ("f", "Why is sending debit card details via standard unencrypted email extremely unsafe?", "Emails travel in plain text across multiple servers and can be intercepted by cybercriminals"),
                ("g", "What is PayPal / Apple Pay and how does it protect your actual bank card number from merchants?", "Tokenized payment gateway: merchants receive a one-time token rather than your actual card details"),
                ("h", "What should you do immediately if you suspect your workplace payment card has been compromised?", "Notify finance immediately and contact the bank to freeze or cancel the card")
            ]
        }
    ],

    "digital-functional-skills-revision": [
        {
            "title": "Question 4: Data Security Legislation & GDPR Compliance",
            "instruction": "State the legal or professional data handling requirement under UK GDPR and Data Protection Act 2018:",
            "items": [
                ("a", "Under GDPR, what constitutes 'Personal Data'?", "Any information relating to an identified or identifiable living individual (name, address, NHS number)"),
                ("b", "How long is an organization permitted to retain customer data that is no longer required?", "No longer than necessary for the purpose for which it was originally collected"),
                ("c", "What must an organization obtain before sending promotional marketing emails to individual consumers?", "Explicit, informed, unambiguous opt-in consent"),
                ("d", "What right gives an individual the power to request a copy of all data held about them by an organization?", "Right of Access / Subject Access Request (SAR)"),
                ("e", "Within what timeframe must an organization report a serious data breach to the Information Commissioner's Office (ICO)?", "Within 72 hours of becoming aware of the breach"),
                ("f", "Why must digital patient files be encrypted when sent to an external clinic?", "Ensures that if the file is intercepted, the contents cannot be read without the decryption key"),
                ("g", "What is the legal consequence for an organization that commits gross negligence with customer data?", "Substantial financial fines from the ICO (up to £17.5 million or 4% of global turnover)"),
                ("h", "Why is writing passwords on sticky notes attached to monitor bezels a severe security breach?", "Allows anyone walking past physical sight of access credentials, breaching access control policies")
            ]
        },
        {
            "title": "Question 5: Digital Wellbeing, Ergonomics & Accessibility",
            "instruction": "Identify the ergonomic or accessibility solution for the workplace computing health risk:",
            "items": [
                ("a", "Experiencing wrist and forearm strain after long hours of typing and mouse navigation", "Use an ergonomic vertical mouse, wrist rest pad, and position keyboard with elbows at 90 degrees"),
                ("b", "Suffering from neck stiffness and headache after working on a laptop on a low desk", "Use a laptop riser stand and separate keyboard so the top of the screen is at eye level"),
                ("c", "Eye fatigue and dryness after staring at monitor screens for four consecutive hours", "Apply the 20-20-20 rule: every 20 minutes, look at an object 20 feet away for at least 20 seconds"),
                ("d", "Lower back ache caused by sitting in an unsupportive office chair", "Adjust chair height so feet rest flat on the floor, adjust lumbar support to curve of lower spine"),
                ("e", "A visually impaired colleague struggles to read small text in software applications", "Enable screen magnifier, increase display scaling in OS settings, or use high-contrast themes"),
                ("f", "A hearing-impaired employee attends a live video conference webinar", "Enable automated real-time closed captions (live subtitles) or provide a BSL interpreter"),
                ("g", "How does blue light emission from digital screens late at night affect sleep patterns?", "Suppresses melatonin production, disrupting the natural circadian rhythm and making sleep difficult"),
                ("h", "What is Repetitive Strain Injury (RSI) and how can workplace breaks prevent it?", "Damage to tendons/muscles from repetitive motions; prevented by taking regular 5-minute micro-breaks")
            ]
        }
    ],

    "entry-level-3-digital-skills": [
        {
            "title": "Question 2: Basic Computer Hardware & Input Devices",
            "instruction": "Name the computer device or action described:",
            "items": [
                ("a", "The screen that displays pictures and text from the computer", "Monitor / Display Screen"),
                ("b", "The handheld pointing device used to click on icons and move the cursor", "Mouse / Trackpad"),
                ("c", "The board of letter and number keys used to type words into documents", "Keyboard"),
                ("d", "Pressing the left mouse button twice quickly to open a program", "Double-click"),
                ("e", "Pressing the right mouse button to open a menu of options", "Right-click"),
                ("f", "Holding the mouse button down to move an icon from one folder to another", "Drag and drop"),
                ("g", "The small flashing vertical line on screen showing where typed letters will appear", "Cursor / Insertion point"),
                ("h", "The key used to create a blank space between two typed words", "Spacebar")
            ]
        },
        {
            "title": "Question 3: Using the Internet & Basic Web Navigation",
            "instruction": "Identify the internet tool or action for each simple task:",
            "items": [
                ("a", "A software program used to view websites (e.g. Chrome, Edge, Safari, Firefox)", "Web browser"),
                ("b", "The website address typed into the top bar to visit a page (e.g. www.nhs.uk)", "URL (Uniform Resource Locator) / Web address"),
                ("c", "Text on a web page that turns into a hand cursor and jumps to a new page when clicked", "Hyperlink (or link)"),
                ("d", "The button shaped like an arrow pointing left that takes you back to the previous webpage", "Back button"),
                ("e", "A website used to search for information across the entire internet (e.g. Google)", "Search engine"),
                ("f", "Saving a favourite website address so you can visit it again with one click", "Bookmark / Favourite"),
                ("g", "The key pressed to jump down to a new line when typing text", "Enter / Return key"),
                ("h", "The key used to delete the letter directly to the left of the cursor", "Backspace key")
            ]
        },
        {
            "title": "Question 4: Keeping Safe Online - Basic Rules",
            "instruction": "Choose the safe and sensible choice for each everyday online situation:",
            "items": [
                ("a", "A website asks for your password to see a funny video", "Do not enter your password; real videos never require your email password"),
                ("b", "You finish using a public computer at the local library", "Log out of all accounts and close the web browser before walking away"),
                ("c", "A stranger on social media asks you to send them money", "Do not send money; block and report the stranger immediately"),
                ("d", "You create a new password for your email account", "Make it a secret combination of letters and numbers that nobody can guess; never share it"),
                ("e", "Your computer screen shows an unfamiliar message asking you to install software", "Ask a supervisor, teacher, or IT technician before clicking yes or download"),
                ("f", "Someone you don't know sends you an email attachment called 'prize.exe'", "Do not open the attachment; delete the email immediately as it could contain a virus"),
                ("g", "You need to type your credit card into a shopping website", "Check that the website address begins with 'https' and has a padlock icon"),
                ("h", "You receive a message from a friend saying they are stranded abroad and need cash", "Phone your friend directly on their known phone number to verify before doing anything")
            ]
        }
    ],

    "printable-digital-skills": [
        {
            "title": "Question 3: Digital Printing Settings & Paper Economy",
            "instruction": "State the correct print dialog setting for each workplace printing requirement:",
            "items": [
                ("a", "Printing on both the front and back sides of each paper sheet to save paper", "Duplex printing / Print on both sides"),
                ("b", "Printing a wide financial spreadsheet table that does not fit on standard vertical paper", "Landscape orientation (instead of Portrait)"),
                ("c", "Printing only pages 4, 5, and 6 from a 50-page training manual", "Page Range: enter '4-6'"),
                ("d", "Printing three identical copies of a 10-page handout assembled as complete sets (1-10, 1-10, 1-10)", "Collate copies"),
                ("e", "Printing a draft document using less ink/toner to reduce environmental waste", "Draft mode / Eco-mode / Grayscale"),
                ("f", "Fitting two document pages onto a single sheet of paper to create a miniature booklet", "Multiple pages per sheet (2 pages per sheet)"),
                ("g", "Reviewing how the document will appear on paper before sending it to the printer", "Print Preview"),
                ("h", "Printing on heavy cardstock or envelopes without causing a paper feed jam", "Select correct paper tray and configure media type setting to 'Heavy Cardstock' / 'Envelope'")
            ]
        },
        {
            "title": "Question 4: Scanning, OCR & Digital Document Archiving",
            "instruction": "Explain the digital scanning feature or procedure:",
            "items": [
                ("a", "What does OCR (Optical Character Recognition) do when scanning a physical paper document?", "Converts scanned images of text into editable, searchable digital text"),
                ("b", "Why should high-resolution 600 DPI scanning be avoided for simple text memos?", "Creates unnecessarily massive file sizes that clog storage and cannot be emailed"),
                ("c", "What resolution (DPI) is standard for clear, readable, compact office document scans?", "200 to 300 DPI"),
                ("d", "Which file format should be selected when scanning a 5-page document into a single file?", "Multi-page PDF"),
                ("e", "Why should glass scanner platen beds be cleaned regularly with lint-free wipes?", "Dust and smudges create streaks or black spots on scanned clinical documents"),
                ("f", "What is an Automatic Document Feeder (ADF) on an office multifunction printer?", "A mechanical tray that feeds a stack of multiple pages through the scanner automatically"),
                ("g", "How should confidential paper documents be disposed of after being verified in the cloud archive?", "Cross-cut shredded in a certified confidential waste console"),
                ("h", "What is metadata in a scanned digital archive (e.g. date scanned, author, document type)?", "Structured indexing tags that enable fast electronic search and retrieval in record systems")
            ]
        }
    ]
}
