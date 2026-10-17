#!/usr/bin/env python3
"""
Authentic Fluency Workouts: Digital Functional Skills
5 Core Topics:
- digital-functional-skills
- digital-functional-skills-revision
- digital-functional-skills-level-1
- digital-functional-skills-mock-exam
- printable-digital-skills
"""

DIGITAL_WORKOUTS = {
    # 1. Core Digital Functional Skills
    "digital-functional-skills": {
        "title": "Digital Functional Skills Core",
        "slug": "digital-functional-skills",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel DFS: Core Specification",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Core Digital Principles & File Rules",
            "points": [
                "Always check file extensions before opening: .exe, .scr, .vbs can carry malware; .docx, .xlsx, .pdf are standard document formats.",
                "Spreadsheet formulas always start with an equals sign (=). Never use commas inside mathematical operations without a function.",
                "When emailing multiple external recipients, use BCC to protect personal data under UK GDPR.",
                "Use strong passwords with at least 12 characters, including uppercase, lowercase, numbers, and symbols.",
                "Always back up essential files to a secure cloud drive or encrypted external media."
            ],
            "calc_tip": "In Excel, press F4 while editing a formula to quickly convert a relative reference (e.g. B2) into an absolute reference ($B$2)."
        },
        "workout_blocks": [
            {
                "title": "File Types & System Recognitions",
                "instruction": "Identify the primary file type and application for each extension:",
                "items": [
                    ("a", ".docx extension", "Microsoft Word / Word Processor document"),
                    ("b", ".xlsx extension", "Microsoft Excel / Spreadsheet workbook"),
                    ("c", ".pdf extension", "Portable Document Format / Read-only document"),
                    ("d", ".csv extension", "Comma-Separated Values / Plain-text spreadsheet data"),
                    ("e", ".jpg / .jpeg", "Compressed digital image file"),
                    ("f", ".png extension", "Lossless image with transparency support"),
                    ("g", ".zip extension", "Compressed archive folder containing multiple files"),
                    ("h", ".mp4 extension", "Digital video recording file")
                ]
            },
            {
                "title": "Essential Spreadsheet Formula Drills",
                "instruction": "Write the exact spreadsheet formula for each instruction:",
                "items": [
                    ("a", "Add cells B2, B3, B4, B5 together", "=SUM(B2:B5)"),
                    ("b", "Calculate the average of cells C2 to C20", "=AVERAGE(C2:C20)"),
                    ("c", "Multiply cell D4 by cell E4", "=D4*E4"),
                    ("d", "Subtract cell F5 from cell F4", "=F4-F5"),
                    ("e", "Divide cell G10 by cell H10", "=G10/H10"),
                    ("f", "Find the largest number in cells A1 to A30", "=MAX(A1:A30)"),
                    ("g", "Find the smallest number in cells B2 to B15", "=MIN(B2:B15)"),
                    ("h", "Lock cell C1 as an absolute reference", "$C$1")
                ]
            },
            {
                "title": "Cyber Hygiene & Online Safety Drills",
                "instruction": "State whether each statement is Safe, Unsafe, or Required under UK GDPR:",
                "items": [
                    ("a", "Clicking a link in an unexpected email from 'admin@pay-pal-alert.com'", "Unsafe (Phishing risk)"),
                    ("b", "Putting 40 client email addresses in the BCC field", "Safe / Required under UK GDPR"),
                    ("c", "Writing your system password on a sticky note under your keyboard", "Unsafe (Security breach)"),
                    ("d", "Using Multi-Factor Authentication (MFA) to log into workplace email", "Safe / Recommended best practice"),
                    ("e", "Plugging an unlabelled USB flash drive found in a car park into a work PC", "Unsafe (Malware / USB drop attack)"),
                    ("f", "Locking your screen (Windows Key + L) whenever leaving your desk", "Safe / Mandatory workplace practice")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Healthcare Clinic Administration",
                "stem": "A medical receptionist manages a patient appointment spreadsheet. Column C contains the consultation fee for 15 patients (cells <strong>C2 to C16</strong>). The clinic offers a <strong>15% prompt payment discount</strong> recorded in cell <strong>F1</strong>.<br>(a) Write the formula in cell D2 to calculate the discount amount using an absolute reference for F1.<br>(b) Write the formula to calculate the total fee collected across cells C2 to C16.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Part (a): Multiply relative cell C2 by absolute discount cell $F$1: =C2*$F$1", "[M1]"),
                    ("Part (b): Use =SUM with colon range: =SUM(C2:C16)", "[A1]"),
                    ("Check: Ensure leading '=' is included in both formulas and F1 is locked with dollar signs.", "[A1]")
                ],
                "final_answer": "(a) =C2*$F$1 | (b) =SUM(C2:C16)",
                "reverse_check": "Dragging =C2*$F$1 down to D3 becomes =C3*$F$1, correctly preserving cell F1.",
                "pitfall": "Forgetting the '$' signs in $F$1, causing F1 to drift to F2, F3, etc."
            },
            {
                "context_tag": "Workplace Data Protection & Email",
                "stem": "An administrative apprentice is preparing to email a confidential staff salary report to the Finance Director.<br>The apprentice accidentally enters the Director's email into the <strong>CC</strong> field instead of <strong>To</strong>, and also enters 50 department managers in the <strong>To</strong> field.<br>Explain what error has occurred and describe two corrective steps before sending.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Identify error: Placing 50 managers in 'To' will expose everyone's email and broadcast confidential executive salary data to all 50 staff members.", "[P1]"),
                    ("Corrective step 1: Remove all 50 managers immediately; send salary data ONLY to the Finance Director in the 'To' field.", "[M1]"),
                    ("Corrective step 2: Encrypt or password-protect the confidential file attachment before emailing.", "[A1]")
                ],
                "final_answer": "Remove all 50 managers from the email, address exclusively to the Finance Director, and password-protect the attachment.",
                "reverse_check": "Only authorized payroll personnel should receive confidential salary data.",
                "pitfall": "Hitting 'Send' without checking the recipient list, leading to a catastrophic UK GDPR data breach."
            }
        ]
    },

    # 2. Digital Functional Skills Revision
    "digital-functional-skills-revision": {
        "title": "Digital Functional Skills Core Revision: Devices, Cloud & Data Protection",
        "slug": "digital-functional-skills-revision",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel DFS: Devices, Cloud & Data Protection",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Storage Units, Cloud Storage & Backup Rules",
            "points": [
                "Memory hierarchy: 1 Kilobyte (KB) = 1,000 Bytes, 1 Megabyte (MB) = 1,000 KB, 1 Gigabyte (GB) = 1,000 MB, 1 Terabyte (TB) = 1,000 GB.",
                "Operating Systems (Windows, macOS, Linux, iOS, Android) manage hardware and run application software (Word, Excel, Chrome).",
                "Cloud storage allows synchronization across multiple devices, automatic revision history, and off-site disaster recovery.",
                "3-2-1 Backup Strategy: Keep 3 copies of your data, across 2 different media types, with 1 copy stored off-site in the cloud.",
                "Under UK GDPR, personal identifiable data (names, medical record numbers, bank details) must be stored securely and deleted when no longer required."
            ],
            "calc_tip": "To convert GB to MB, multiply by 1,000. To convert MB to GB, divide by 1,000."
        },
        "workout_blocks": [
            {
                "title": "Storage Capacity & Unit Conversions",
                "instruction": "Convert the storage units or answer the capacity questions:",
                "items": [
                    ("a", "How many Megabytes (MB) in 4 Gigabytes (GB)?", "4,000 MB"),
                    ("b", "How many Gigabytes (GB) in 2 Terabytes (TB)?", "2,000 GB"),
                    ("c", "How many Kilobytes (KB) in 5 Megabytes (MB)?", "5,000 KB"),
                    ("d", "Convert 8,500 MB into Gigabytes (GB)", "8.5 GB"),
                    ("e", "Convert 500 GB into Terabytes (TB)", "0.5 TB"),
                    ("f", "Which is larger: 1.5 GB or 1,200 MB?", "1.5 GB (1,500 MB)"),
                    ("g", "Which is smaller: 750 KB or 1 MB?", "750 KB (1 MB = 1,000 KB)"),
                    ("h", "Number of 500 MB videos that fit on a 32 GB drive", "64 videos (32,000 ÷ 500)")
                ]
            },
            {
                "title": "Hardware, OS & Software Classification",
                "instruction": "Classify each item as Input Device, Output Device, Storage Device, or Operating System:",
                "items": [
                    ("a", "Barcode scanner", "Input Device"),
                    ("b", "Solid State Drive (SSD)", "Storage Device"),
                    ("c", "Microsoft Windows 11", "Operating System"),
                    ("d", "Laser printer", "Output Device"),
                    ("e", "Touchscreen monitor", "Input & Output Device (Hybrid)"),
                    ("f", "Apple iOS", "Operating System (Mobile)"),
                    ("g", "USB Flash Drive", "Storage Device"),
                    ("h", "Biometric fingerprint reader", "Input Device (Security)")
                ]
            },
            {
                "title": "Data Protection & Cloud Security Fluency",
                "instruction": "State the correct technical term for each description:",
                "items": [
                    ("a", "Law governing personal data privacy in the UK", "UK GDPR / Data Protection Act 2018"),
                    ("b", "Scramble data into unreadable code requiring a secret key to open", "Encryption"),
                    ("c", "Verifying identity via password plus a mobile push notification", "Multi-Factor Authentication (MFA)"),
                    ("d", "Software that secretly logs keystrokes to steal passwords", "Keylogger / Spyware"),
                    ("e", "Fake website designed to look like a bank login page", "Phishing / Spoof website"),
                    ("f", "Private secure encrypted tunnel across the public internet", "VPN (Virtual Private Network)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Mobile Healthcare Worker",
                "stem": "A community district nurse visits patients at home using a clinical tablet computer.<br>The nurse needs to save <strong>12 high-resolution wound clinical photographs</strong> (each photo is <strong>25 MB</strong>) and <strong>3 patient assessment videos</strong> (each video is <strong>450 MB</strong>).<br>Calculate the total storage space required in Megabytes (MB), and state whether this data will fit onto a secure <strong>2 GB encrypted memory card</strong>.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Calculate photos storage: 12 × 25 MB = 300 MB", "[M1]"),
                    ("Calculate videos storage: 3 × 450 MB = 1,350 MB", "[M1]"),
                    ("Total storage: 300 + 1,350 = 1,650 MB. Convert card to MB: 2 GB = 2,000 MB. 1,650 MB < 2,000 MB, so Yes, it will fit.", "[A1]")
                ],
                "final_answer": "Total = 1,650 MB. Yes, it will comfortably fit on the 2 GB (2,000 MB) card.",
                "reverse_check": "2,000 MB - 1,650 MB = 350 MB spare capacity.",
                "pitfall": "Assuming 2 GB is 200 MB or failing to convert units before comparing."
            }
        ]
    },

    # 3. Level 1 DFS
    "digital-functional-skills-level-1": {
        "title": "Digital Functional Skills Level 1: Spreadsheets, Email & Cyber Hygiene",
        "slug": "digital-functional-skills-level-1",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel DFS: Level 1 Standard",
        "level": "Level 1",
        "method_card": {
            "title": "Spreadsheet Operators & Email Etiquette",
            "points": [
                "Maths symbols in spreadsheets: Addition (+), Subtraction (-), Multiplication (*), Division (/).",
                "Use colon (:) for cell ranges (e.g. A1:A10), and comma (,) for individual distinct cells (e.g. A1, A5).",
                "Formatting numbers: Format financial values as Currency (£) with 2 decimal places.",
                "Sorting: Ascending order means A to Z (smallest to largest); Descending means Z to A (largest to smallest).",
                "Always write clear email subject lines that include the topic and urgency."
            ],
            "calc_tip": "When entering currency in Excel, do NOT type the £ sign into the cell manually; type the raw number and click the 'Currency' format button (£)."
        },
        "workout_blocks": [
            {
                "title": "Formula Mechanics & Cell Referencing",
                "instruction": "Write the exact formula starting with '=':",
                "items": [
                    ("a", "Add cell A1 to cell B1", "=A1+B1"),
                    ("b", "Subtract cell D3 from cell C3", "=C3-D3"),
                    ("c", "Multiply cell E2 by cell F2", "=E2*F2"),
                    ("d", "Divide cell G4 by cell H4", "=G4/H4"),
                    ("e", "Sum the range from B5 to B25", "=SUM(B5:B25)"),
                    ("f", "Calculate the average of range D1 to D12", "=AVERAGE(D1:D12)"),
                    ("g", "Lock row 2 absolutely while leaving column A relative", "A$2"),
                    ("h", "Lock column B absolutely while leaving row 5 relative", "$B5")
                ]
            },
            {
                "title": "Spreadsheet Formatting & Tools",
                "instruction": "Name the specific feature or formatting tool in Microsoft Excel:",
                "items": [
                    ("a", "Tool used to combine multiple cells into one large cell", "Merge & Center"),
                    ("b", "Feature to display long text on multiple lines within a cell", "Wrap Text"),
                    ("c", "Format applied to display 45.5 as £45.50", "Currency format (2 decimal places)"),
                    ("d", "Tool used to display only records that meet specific criteria", "Filter (AutoFilter)"),
                    ("e", "Feature used to automatically colour cells based on value", "Conditional Formatting"),
                    ("f", "Corner square dragged to copy formulas down a column", "Fill Handle (AutoFill)")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Care Home Food Supplies",
                "stem": "A residential care home kitchen orders supplies. In their spreadsheet:<br>• Cell <strong>B2</strong> has item quantity: <strong>24</strong><br>• Cell <strong>C2</strong> has unit price: <strong>£3.50</strong><br>• Cell <strong>D2</strong> calculates total cost: <code>=B2*C2</code><br>• Delivery charge in cell <strong>F1</strong> is <strong>£6.00</strong>.<br>(a) What is the evaluated cost in cell D2?<br>(b) Write a formula in cell E2 to add the delivery charge ($F$1) to D2.",
                "marks": 3,
                "prefix": "£",
                "steps": [
                    ("Calculate D2: 24 × £3.50 = £84.00", "[M1]"),
                    ("Write formula for E2: =D2+$F$1", "[A1]"),
                    ("Calculate overall total in E2: £84.00 + £6.00 = £90.00", "[A1]")
                ],
                "final_answer": "(a) £84.00 | (b) =D2+$F$1 (Total = £90.00)",
                "reverse_check": "£90.00 - £6.00 = £84.00; £84.00 ÷ 24 = £3.50.",
                "pitfall": "Writing =D2+6 instead of referencing cell $F$1."
            }
        ]
    },

    # 4. Mock Exam Practice
    "digital-functional-skills-mock-exam": {
        "title": "Digital Functional Skills Mock Exam Practice: Word Processing, Calculations & Communication",
        "slug": "digital-functional-skills-mock-exam",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel DFS: Level 1 & Level 2 Benchmark",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Exam Strategies & Mark Allocation",
            "points": [
                "Read every scenario brief completely before typing or formatting.",
                "In word processing tasks: Ensure consistent fonts (Arial, Calibri), headings (14–16pt bold), body text (11–12pt), and 1.15–1.5 line spacing.",
                "In spreadsheet tasks: Always use built-in functions (=SUM, =AVERAGE, =COUNT, =MAX, =MIN, =IF) rather than typing calculated numbers manually.",
                "Always save your exam file using the designated naming convention specified in the instructions."
            ],
            "calc_tip": "In Excel, check your formula bar to ensure no accidental spaces or quotation marks are misplaced inside calculations."
        },
        "workout_blocks": [
            {
                "title": "Exam Command Words & Functions",
                "instruction": "State the exact Excel function required for each exam requirement:",
                "items": [
                    ("a", "Calculate the total score of all students", "=SUM(...)"),
                    ("b", "Find the mean average attendance percentage", "=AVERAGE(...)"),
                    ("c", "Count how many rows contain numbers", "=COUNT(...)"),
                    ("d", "Count how many rows contain any data (numbers or text)", "=COUNTA(...)"),
                    ("e", "Display 'Pass' if cell C2 is 60 or more, else 'Fail'", "=IF(C2>=60, \"Pass\", \"Fail\")"),
                    ("f", "Identify the highest expenditure on the ward", "=MAX(...)"),
                    ("g", "Identify the lowest temperature recorded", "=MIN(...)"),
                    ("h", "Count how many items equal 'Urgent'", "=COUNTIF(range, \"Urgent\")")
                ]
            },
            {
                "title": "Document Layout & Typographical Accuracy",
                "instruction": "Identify the formatting defect or best practice rule:",
                "items": [
                    ("a", "Why is ALL-CAPS text discouraged in formal business letters?", "Difficult to read and perceived as aggressive shouting"),
                    ("b", "Recommended alignment for body paragraphs (Left, Right, or Center)", "Left-aligned (easier tracking for dyslexic readers)"),
                    ("c", "Best practice for presenting 5 sequential steps in a manual", "Numbered list (1, 2, 3...)"),
                    ("d", "Best practice for presenting 5 non-ordered safety rules", "Bulleted list"),
                    ("e", "Feature used to repeat company logo at top of every page", "Header"),
                    ("f", "Feature used to display page numbers (e.g. 'Page 1 of 4')", "Footer")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Apprenticeship Showcase Event",
                "stem": "An apprentice creates a promotional flyer for a college apprenticeship recruitment evening.<br>The brief requires:<br>• A main title in <strong>20pt bold</strong>.<br>• Three key apprenticeship benefits displayed in a <strong>bulleted list</strong>.<br>• Date, time, and location in a <strong>distinct shaded box</strong>.<br>State why structuring information this way helps prospective students absorb key details quickly.",
                "marks": 3,
                "prefix": "",
                "steps": [
                    ("Visual hierarchy: 20pt bold heading immediately grabs attention and clarifies document purpose.", "[M1]"),
                    ("Chunking: Bulleted list chunks benefits into digestible items avoiding text overload.", "[M1]"),
                    ("Signposting: Shaded box isolates essential logistical details so readers can find times and venue instantly.", "[A1]")
                ],
                "final_answer": "Establishes visual hierarchy, chunks key benefits for quick scanning, and highlights logistics in a prominent callout box.",
                "reverse_check": "Meets Pearson Edexcel criteria for layout, presentation, and target audience adaptation.",
                "pitfall": "Writing all information as one continuous unformatted paragraph."
            }
        ]
    },

    # 5. Printable Digital Skills
    "printable-digital-skills": {
        "title": "Digital Functional Skills Quick Reference, Formula Drills & Troubleshooting",
        "slug": "printable-digital-skills",
        "subject": "Digital Functional Skills",
        "spec_codes": "Pearson Edexcel DFS: Reference & Troubleshooting",
        "level": "Level 1 & Level 2",
        "method_card": {
            "title": "Formula Syntax Cheatsheet & Error Debugging",
            "points": [
                "##### Error: The column is too narrow to display the number. Solution: Double-click column header boundary to widen.",
                "#DIV/0! Error: Formula attempts to divide by zero or an empty cell. Solution: Check divisor cell.",
                "#VALUE! Error: Formula contains incompatible data types (e.g. text inside arithmetic). Solution: Check all referenced cells are numbers.",
                "#REF! Error: Formula refers to a cell that has been deleted. Solution: Re-enter valid cell reference.",
                "#NAME? Error: Typo in the function name (e.g. =SUMM or =AVG). Solution: Correct spelling to =SUM or =AVERAGE."
            ],
            "calc_tip": "Use Ctrl + Z immediately if you make a mistake to undo your last action in any software application."
        },
        "workout_blocks": [
            {
                "title": "Excel Error Code Rapid Debugging",
                "instruction": "Identify the cause of each error message:",
                "items": [
                    ("a", "A cell displays '#####'", "Column width too narrow to display formatted value"),
                    ("b", "A cell displays '#DIV/0!'", "Formula attempts to divide by zero or empty cell"),
                    ("c", "A cell displays '#VALUE!'", "Wrong data type (e.g. trying to multiply text)"),
                    ("d", "A cell displays '#REF!'", "Referenced cell was deleted or cut"),
                    ("e", "A cell displays '#NAME?'", "Misspelled function name (e.g. =SUMM)"),
                    ("f", "A cell displays '#N/A'", "Value not available (e.g. in a lookup formula)")
                ]
            },
            {
                "title": "Essential Workplace Keyboard Shortcuts",
                "instruction": "State the standard Windows shortcut for each action:",
                "items": [
                    ("a", "Copy selected text or cell", "Ctrl + C"),
                    ("b", "Paste copied content", "Ctrl + V"),
                    ("c", "Cut selected content", "Ctrl + X"),
                    ("d", "Undo last action", "Ctrl + Z"),
                    ("e", "Redo last undone action", "Ctrl + Y"),
                    ("f", "Save current document", "Ctrl + S"),
                    ("g", "Print document", "Ctrl + P"),
                    ("h", "Select all content", "Ctrl + A")
                ]
            }
        ],
        "apply_questions": [
            {
                "context_tag": "Hospital Pharmacy Audit",
                "stem": "A pharmacy technician writes a formula in cell F10: <code>=SUM(F2:F9)/D10</code>.<br>Cell D10 is currently empty. The cell immediately displays <strong>#DIV/0!</strong>.<br>(a) Explain why this error appeared.<br>(b) How should the technician resolve this error?",
                "marks": 2,
                "prefix": "",
                "steps": [
                    ("Cause: Cell D10 is empty, which Excel evaluates as 0; mathematical division by zero is impossible.", "[M1]"),
                    ("Resolution: Enter the valid divisor value in cell D10 (or use =IF(D10=0, 0, SUM(F2:F9)/D10)).", "[A1]")
                ],
                "final_answer": "(a) Dividing by an empty cell (evaluated as 0). (b) Enter the correct non-zero number in cell D10.",
                "reverse_check": "Entering a valid number in D10 immediately recalculates the formula.",
                "pitfall": "Deleting the formula instead of fixing the missing data in cell D10."
            }
        ]
    }
}
