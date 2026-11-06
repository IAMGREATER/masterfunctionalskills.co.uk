# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Level 1 Digital Skills (Skill Area 1)
Author: Abdul (MFS Pedagogical Systems)
"""

LEVEL_1_SKILL_1 = [
    {
        "slug": "l1-file-management-hierarchies",
        "code": "L1.1.1",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Folder Hierarchies, File Types and Sizes",
        "time": "15 Mins",
        "lead": "Master professional directory structures using subfolders, identify common file extensions (.docx, .xlsx, .pdf, .jpg), and compare storage capacities across Bytes, KB, MB, and GB.",
        "objectives": [
            "Build logical folder and subfolder hierarchies for workplace records",
            "Identify standard file extensions and their corresponding applications",
            "Compare digital file sizes and storage units (Bytes, KB, MB, GB, TB)"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Folder Hierarchies & File Sizes",
        "steps": [
            {
                "title": "Creating Structured Folder Hierarchies (Subfolders)",
                "body": "<p>In workplace environments, files cannot sit in one root folder. You must create <strong>hierarchies</strong> using main folders and targeted <strong>subfolders</strong>:</p><ul><li><strong>Root Folder:</strong> <code>Healthcare_Clinic_Records</code></li><li><strong>Year Subfolder:</strong> <code>Healthcare_Clinic_Records / 2026</code></li><li><strong>Department Subfolder:</strong> <code>Healthcare_Clinic_Records / 2026 / Staff_Rotas</code></li></ul><p>This allows any authorised team member to navigate directly to the correct file in seconds.</p>",
                "shortcuts": [
                    {"label": "New Subfolder", "key": "Ctrl + Shift + N"},
                    {"label": "Navigate Up One Level", "key": "Alt + Up Arrow"}
                ]
            },
            {
                "title": "Common File Extensions & Associations",
                "body": "<p>A <strong>file extension</strong> is the suffix of 3 or 4 letters following the dot at the end of a filename that tells the operating system which software opens it:</p><ul><li><code>.docx</code>: Microsoft Word document (word processing, letters, reports).</li><li><code>.xlsx</code>: Microsoft Excel spreadsheet (data tables, accounts, calculations).</li><li><code>.pdf</code>: Portable Document Format (universal read-only format; looks identical on all devices).</li><li><code>.jpg</code> / <code>.png</code>: Image files (photos, clinic logos).</li><li><code>.zip</code>: Compressed archive containing multiple packaged files.</li></ul>",
                "ui_sim": {
                    "title": "File Types & Associated Icons",
                    "content": "<div style='display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:0.88rem;'><div><i class='fa-regular fa-file-word' style='color:#2563eb; width:20px;'></i> <strong>.docx:</strong> Word Processor<br><i class='fa-regular fa-file-excel' style='color:#16a34a; width:20px;'></i> <strong>.xlsx:</strong> Spreadsheet Grid</div><div><i class='fa-regular fa-file-pdf' style='color:#dc2626; width:20px;'></i> <strong>.pdf:</strong> Read-Only Document<br><i class='fa-regular fa-file-zipper' style='color:#f59e0b; width:20px;'></i> <strong>.zip:</strong> Compressed Archive</div></div>"
                }
            },
            {
                "title": "Understanding File Sizes: From Bytes to Gigabytes",
                "body": "<p>Storage size measures how much memory a file consumes on a disk. Learn the hierarchy from smallest to largest:</p><ol><li><strong>Byte (B):</strong> Single character of text (e.g. the letter 'A').</li><li><strong>Kilobyte (KB):</strong> Approx. 1,000 Bytes. A plain email or 2-page Word document is typically <strong>50 KB to 300 KB</strong>.</li><li><strong>Megabyte (MB):</strong> Approx. 1,000 KB (1 million Bytes). A high-resolution photo or 10-page illustrated report is <strong>3 MB to 15 MB</strong>.</li><li><strong>Gigabyte (GB):</strong> Approx. 1,000 MB (1 billion Bytes). An HD video recording or complete operating system backup is <strong>2 GB to 10 GB</strong>.</li></ol>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Conversion Rule",
                    "text": "Remember the order: <strong>Byte &lt; Kilobyte (KB) &lt; Megabyte (MB) &lt; Gigabyte (GB) &lt; Terabyte (TB)</strong>. Each unit is roughly 1,000 times larger than the previous one!"
                }
            }
        ],
        "exam_model": {
            "scenario": "A medical clinic administrator has four files saved on a USB drive: 'Audit.docx' (120 KB), 'Scan.jpg' (4.2 MB), 'Training_Video.mp4' (1.8 GB), and 'Notes.txt' (800 Bytes). Put these four files in order of file size, starting with the SMALLEST.",
            "steps": [
                {
                    "action": "Order the storage units",
                    "solution": "1. Notes.txt (800 Bytes)\n2. Audit.docx (120 KB)\n3. Scan.jpg (4.2 MB)\n4. Training_Video.mp4 (1.8 GB)",
                    "mark": "[B1]",
                    "rationale": "Correctly orders Bytes < KB < MB < GB."
                }
            ],
            "tutor_rule": "In Level 1 exams, you will almost certainly be asked to arrange files from smallest to largest or explain why a 35 MB video cannot be emailed as a standard 25 MB email attachment."
        },
        "drills": [
            {
                "question": "Which of the following file sizes is the LARGEST?",
                "options": [
                    {"text": "2.5 GB", "correct": True},
                    {"text": "500 MB", "correct": False},
                    {"text": "850 KB", "correct": False},
                    {"text": "9,000 Bytes", "correct": False}
                ],
                "explanation": "2.5 GB equals roughly 2,500 MB, which is much larger than 500 MB or any KB/Byte value."
            },
            {
                "question": "Which file extension indicates a spreadsheet document created in software like Microsoft Excel?",
                "options": [
                    {"text": ".xlsx", "correct": True},
                    {"text": ".docx", "correct": False},
                    {"text": ".mp3", "correct": False},
                    {"text": ".pdf", "correct": False}
                ],
                "explanation": ".xlsx is the standard open XML spreadsheet file extension used by Excel."
            },
            {
                "question": "Why would an administrator save an employee handbook as a .PDF file rather than a .DOCX file before publishing it on the staff portal?",
                "options": [
                    {"text": "PDF files preserve formatting and prevent readers from accidentally altering text", "correct": True},
                    {"text": "PDF files can only be opened on desktop computers", "correct": False},
                    {"text": "Word documents cannot be read on the internet", "correct": False},
                    {"text": "PDF files automatically delete themselves after 7 days", "correct": False}
                ],
                "explanation": "PDFs maintain universal formatting across all devices and prevent unintended edits."
            }
        ],
        "practice": {
            "task": "A company requires you to organise files for the Finance Department. Explain how you would create a logical subfolder structure for storing supplier invoices from 2025 and 2026, and recommend a clear naming convention for an invoice from 'Medical Supplies Ltd' dated 15 October 2026.",
            "scaffold_starter": "Folder structure: \nSubfolders: \nRecommended filename: ",
            "model_answer": "Folder structure: Create a main folder named 'Finance'.\nSubfolders: Inside 'Finance', create two subfolders: 'Invoices_2025' and 'Invoices_2026'.\nRecommended filename: 'Medical_Supplies_Ltd_Invoice_2026-10-15.pdf' (or .docx).",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Logical multi-level hierarchy (Main folder > Year subfolders)."},
                {"tag": "[1 Mark]", "desc": "Consistent, descriptive filename containing supplier name, document type, and date."}
            ]
        },
        "revision_links": [
            {"label": "File Compression & Zipping", "href": "l1-file-compression-zipping.html"},
            {"label": "Cloud Backups & Sync", "href": "l1-backups-cloud-sync.html"},
            {"label": "Professional Word Formatting", "href": "l1-word-processing-professional.html"}
        ]
    },
    {
        "slug": "l1-file-compression-zipping",
        "code": "L1.1.2",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "File Compression and Archiving (ZIP)",
        "time": "15 Mins",
        "lead": "Learn how file compression works, how to create ZIP archive folders to bundle multiple files and reduce file size for email transmission, and how to extract compressed files.",
        "objectives": [
            "Explain the benefits of file compression (saving disk space and faster transmission)",
            "Create a compressed ZIP folder containing multiple documents or images",
            "Extract (unzip) files from a compressed archive into a destination folder"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Creating & Extracting ZIP Files",
        "steps": [
            {
                "title": "What is File Compression?",
                "body": "<p><strong>Compression</strong> uses mathematical algorithms to pack data more efficiently, reducing the total number of bytes needed to store it. Think of it like using a vacuum storage bag for clothing!</p><ul><li><strong>Saves Storage Space:</strong> Reduces the amount of disk or cloud memory used.</li><li><strong>Faster Email &amp; Web Transfer:</strong> Smaller files upload and download significantly faster.</li><li><strong>Bundles Multiple Files:</strong> Instead of attaching 15 separate photos to an email, you can bundle them into <strong>one single .zip file</strong>.</li></ul>"
            },
            {
                "title": "How to Create a Compressed ZIP Folder in Windows",
                "body": "<ol><li>Open File Explorer and select the files or folders you want to compress (hold <kbd class='dfs-kbd'>Ctrl</kbd> to select multiple files).</li><li>Right-click on any of the selected files.</li><li>Click <strong>Compress to ZIP file</strong> (or <strong>Send to &gt; Compressed (zipped) folder</strong>).</li><li>A new folder with a zipper icon (<i class='fa-regular fa-file-zipper'></i>) will appear. Type a clear name and press <kbd class='dfs-kbd'>Enter</kbd>.</li></ol>",
                "ui_sim": {
                    "title": "Context Menu: Compress to ZIP",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; box-shadow:0 4px 6px rgba(0,0,0,0.1); width:230px; padding:6px; border-radius:4px; font-size:0.85rem;'><div style='padding:4px 8px;'><i class='fa-regular fa-copy' style='margin-right:8px;'></i> Copy</div><div style='padding:4px 8px; background:#e0f2fe; color:#0369a1; font-weight:700; border-radius:4px;'><i class='fa-regular fa-file-zipper' style='margin-right:8px;'></i> Compress to ZIP file</div><div style='padding:4px 8px;'><i class='fa-solid fa-trash' style='margin-right:8px;'></i> Delete</div></div>"
                }
            },
            {
                "title": "How to Extract (Unzip) Files",
                "body": "<p>When you download or receive a .zip file, you cannot always edit the files directly inside it. You must <strong>extract</strong> them first:</p><ol><li>Right-click the ZIP folder.</li><li>Click <strong>Extract All...</strong></li><li>Choose the destination folder where you want the uncompressed files saved.</li><li>Tick <em>'Show extracted files when complete'</em> and click <strong>Extract</strong>.</li></ol>",
                "callout": {
                    "type": "warning",
                    "title": "Exam Trap: Read-Only Files",
                    "text": "If you open a file directly inside a ZIP without extracting it, your changes may NOT save! Always extract files first before making edits."
                }
            }
        ],
        "exam_model": {
            "scenario": "An employee needs to email 12 high-resolution medical posters to a training venue. The total size of the loose files is 45 MB, but their email provider only allows attachments up to 25 MB. Explain two reasons why compressing these files into a ZIP folder solves this problem.",
            "steps": [
                {
                    "action": "First benefit: File size reduction",
                    "solution": "Compressing reduces the overall file size, potentially bringing it under the 25 MB email attachment limit.",
                    "mark": "[B1]",
                    "rationale": "Identifies size reduction as the primary technical mechanism."
                },
                {
                    "action": "Second benefit: Single file transmission",
                    "solution": "It bundles all 12 separate posters into a single archive file, making it much easier to attach and send in one email.",
                    "mark": "[B1]",
                    "rationale": "Identifies grouping/bundling multiple items into one package."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever large files or multiple attachments are mentioned, the solution is always 'Compress into a ZIP folder'."
        },
        "drills": [
            {
                "question": "What is the main purpose of creating a compressed (ZIP) folder?",
                "options": [
                    {"text": "To reduce file size and bundle multiple files together for easier transmission", "correct": True},
                    {"text": "To convert Word documents into Excel spreadsheets", "correct": False},
                    {"text": "To permanently delete old files from your hard drive", "correct": False},
                    {"text": "To increase screen brightness", "correct": False}
                ],
                "explanation": "Compression reduces file size and allows bundling several files into a single container."
            },
            {
                "question": "What must you do to a received ZIP archive before you can properly edit and save the files inside it?",
                "options": [
                    {"text": "Extract All files to a destination folder", "correct": True},
                    {"text": "Rename the extension to .exe", "correct": False},
                    {"text": "Turn off your computer Wi-Fi", "correct": False},
                    {"text": "Print the ZIP folder onto paper", "correct": False}
                ],
                "explanation": "Extracting decompresses the files and writes full editable copies to your hard drive."
            },
            {
                "question": "Which icon symbol is typically used by operating systems to identify a compressed folder?",
                "options": [
                    {"text": "A folder with a zipper down the middle", "correct": True},
                    {"text": "A recycling bin with paper inside", "correct": False},
                    {"text": "A blue globe", "correct": False},
                    {"text": "A speaker emitting sound waves", "correct": False}
                ],
                "explanation": "A zipper icon visually indicates a compressed archive folder."
            }
        ],
        "practice": {
            "task": "A colleague has emailed you an archive called 'Patient_Brochures.zip'. Describe the three steps you must take to extract all brochures into your Documents folder.",
            "scaffold_starter": "Step 1: Right-click...\nStep 2: Select...\nStep 3: Browse to...",
            "model_answer": "Step 1: Right-click the 'Patient_Brochures.zip' file.\nStep 2: Select 'Extract All...' from the context menu.\nStep 3: Click Browse, select the 'Documents' folder as the destination, and click 'Extract'.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Right-clicking and choosing 'Extract All...'."},
                {"tag": "[1 Mark]", "desc": "Specifying the Documents folder as the destination and confirming extraction."}
            ]
        },
        "revision_links": [
            {"label": "Folder Hierarchies & File Sizes", "href": "l1-file-management-hierarchies.html"},
            {"label": "Workplace Email Etiquette", "href": "l1-workplace-email-etiquette.html"},
            {"label": "Data Backup & Cloud Sync", "href": "l1-backups-cloud-sync.html"}
        ]
    },
    {
        "slug": "l1-network-connections-security",
        "code": "L1.1.3",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Network Security and Public Wi-Fi Risks",
        "time": "15 Mins",
        "lead": "Understand the cybersecurity risks of using open public Wi-Fi networks, configure mobile tethering hotspots safely, and understand how Virtual Private Networks (VPNs) protect workplace data.",
        "objectives": [
            "Identify security vulnerabilities associated with unsecured public Wi-Fi hotspots",
            "Understand how Virtual Private Networks (VPNs) encrypt corporate data traffic",
            "Set up a secure mobile hotspot (tethering) with a strong WPA2/WPA3 password"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Network Security & Public Wi-Fi",
        "steps": [
            {
                "title": "The Dangers of Open Public Wi-Fi",
                "body": "<p>Public Wi-Fi networks in coffee shops, hotels, and airports are convenient, but they carry severe risks:</p><ul><li><strong>Unencrypted Traffic:</strong> Open networks without passwords transmit data in plain text. Criminals on the same network can 'eavesdrop' on your web traffic (called packet sniffing).</li><li><strong>Fake Hotspots (Evil Twins):</strong> Criminals set up rogue Wi-Fi networks with names like <em>'Free_Airport_WiFi'</em> to trick people into connecting so they can intercept usernames and credit cards.</li><li><strong>Malware Distribution:</strong> Unsecured networks can be used to inject malicious pop-ups and fake software updates into your browser.</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Workplace Data Security Rule",
                    "text": "Never access confidential customer records, financial accounts, or internal hospital databases on an open public Wi-Fi network without a corporate VPN active!"
                }
            },
            {
                "title": "Virtual Private Networks (VPNs)",
                "body": "<p>A <strong>VPN</strong> creates an encrypted digital 'tunnel' between your device and your organisation's network:</p><ol><li>Even if you are connected to an untrusted public Wi-Fi, the VPN encrypts all data leaving your laptop.</li><li>Any hacker snooping on the network only sees scrambled, unreadable code.</li><li>It allows remote staff to access internal workplace servers securely from home.</li></ol>",
                "ui_sim": {
                    "title": "Corporate VPN Connection Status",
                    "content": "<div style='display:flex; justify-content:space-between; align-items:center; background:#0f172a; color:#ffffff; padding:12px 16px; border-radius:6px;'><div style='display:flex; align-items:center; gap:10px;'><i class='fa-solid fa-shield-halved' style='color:#10b981; font-size:1.3rem;'></i> <div><strong>MFS Secure Workplace VPN</strong><br><span style='color:#10b981; font-size:0.8rem;'>Connected (AES-256 Encrypted)</span></div></div><button style='background:#334155; border:none; color:#ffffff; padding:6px 12px; border-radius:4px; font-weight:600;'>Disconnect</button></div>"
                }
            },
            {
                "title": "Using Mobile Tethering Safely",
                "body": "<p>If trusted Wi-Fi is unavailable, you can turn your smartphone into a <strong>Personal Mobile Hotspot</strong>:</p><ul><li>Shares your phone's 4G/5G mobile data with your laptop.</li><li>Always set a strong password (WPA2/WPA3 encryption). Never leave your hotspot open!</li><li>Be mindful of data limits — video streaming consumes mobile allowances rapidly.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A community healthcare worker is travelling on a train and needs to access confidential patient records on their laptop. The train offers free public Wi-Fi with no password required. Explain two precautions the worker must take to keep patient data secure.",
            "steps": [
                {
                    "action": "State first security precaution",
                    "solution": "Connect through their organisation's secure VPN (Virtual Private Network) before logging into patient databases.",
                    "mark": "[B1]",
                    "rationale": "VPN encrypts the transmission over unsecure networks."
                },
                {
                    "action": "State second alternative precaution",
                    "solution": "Use their own encrypted mobile phone hotspot instead of the open public train Wi-Fi.",
                    "mark": "[B1]",
                    "rationale": "Cellular tethering bypasses shared public network risks."
                }
            ],
            "tutor_rule": "In Level 1 exams, whenever public Wi-Fi is mentioned in a scenario, the accredited answers are: 1. Use a VPN; 2. Use a secure personal mobile hotspot."
        },
        "drills": [
            {
                "question": "What is the primary risk of using an open public Wi-Fi network without a password?",
                "options": [
                    {"text": "Other users on the network may intercept unencrypted data, including passwords and banking details", "correct": True},
                    {"text": "The computer screen will automatically turn off", "correct": False},
                    {"text": "Your printer ink will run out", "correct": False},
                    {"text": "The laptop keyboard will lock permanently", "correct": False}
                ],
                "explanation": "Open networks lack encryption, allowing malicious actors to intercept transmitted packets."
            },
            {
                "question": "What does a VPN (Virtual Private Network) do?",
                "options": [
                    {"text": "Encrypts your internet traffic so third parties cannot view your data", "correct": True},
                    {"text": "Charges your laptop battery wirelessly", "correct": False},
                    {"text": "Increases the physical size of your hard drive", "correct": False},
                    {"text": "Translates documents from French to English automatically", "correct": False}
                ],
                "explanation": "A VPN wraps internet communications in an encrypted tunnel to protect privacy."
            },
            {
                "question": "Which security setting should always be enabled when using a mobile phone hotspot for tethering?",
                "options": [
                    {"text": "Set a strong WPA2 or WPA3 password", "correct": True},
                    {"text": "Leave the hotspot open with no password so anyone can join", "correct": False},
                    {"text": "Turn off the phone screen", "correct": False},
                    {"text": "Delete your text messages", "correct": False}
                ],
                "explanation": "Protecting a mobile hotspot with WPA2/WPA3 password prevents unauthorised users from accessing your network."
            }
        ],
        "practice": {
            "task": "A company is drafting a Remote Working Security Policy for staff using laptops in cafés and hotels. Write down two mandatory rules that employees must follow when connecting to the internet away from the main office.",
            "scaffold_starter": "Rule 1 (Network Connections): \nRule 2 (Corporate Security): ",
            "model_answer": "Rule 1: Staff must never conduct confidential work on open, password-free public Wi-Fi networks without an active corporate VPN.\nRule 2: Staff should use password-protected personal mobile hotspots (tethering) or an approved VPN connection at all times when working remotely.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Mandating VPN usage when connecting over public networks."},
                {"tag": "[1 Mark]", "desc": "Requiring secure/encrypted connections or personal mobile hotspots."}
            ]
        },
        "revision_links": [
            {"label": "Cybersecurity & Malware Defence", "href": "l1-cybersecurity-malware-defence.html"},
            {"label": "UK GDPR & Privacy", "href": "l1-uk-gdpr-data-protection-privacy.html"},
            {"label": "Multi-Factor Authentication", "href": "l1-multi-factor-authentication-banking.html"}
        ]
    },
    {
        "slug": "l1-troubleshooting-system-errors",
        "code": "L1.1.4",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Troubleshooting Routine IT and Hardware Issues",
        "time": "15 Mins",
        "lead": "Solve everyday technical problems independently: deal with frozen applications using Task Manager, resolve printer queue jams, troubleshoot lost Wi-Fi connections, and manage low disk space alerts.",
        "objectives": [
            "Use Task Manager to identify and force-close unresponsive applications (Not Responding)",
            "Troubleshoot printer errors (paper jams, offline status, clearing print queues)",
            "Diagnose network connectivity issues and manage low disk storage warnings"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Troubleshooting IT Glitches & Errors",
        "steps": [
            {
                "title": "Handling Frozen Applications (Not Responding)",
                "body": "<p>When a program freezes and displays <em>'(Not Responding)'</em>, clicking the screen repeatedly will not help. Use <strong>Task Manager</strong> to close it safely:</p><ol><li>Press <kbd class='dfs-kbd'>Ctrl + Shift + Esc</kbd> (or <kbd class='dfs-kbd'>Ctrl + Alt + Delete</kbd> &gt; Task Manager).</li><li>Look at the <strong>Processes</strong> tab for the program with high CPU usage or marked 'Not responding'.</li><li>Click the application name and click <strong>End Task</strong>.</li><li>The frozen program closes immediately, freeing up system memory so you can reopen it.</li></ol>",
                "shortcuts": [
                    {"label": "Open Task Manager Instantly", "key": "Ctrl + Shift + Esc"},
                    {"label": "Force Quit Window", "key": "Alt + F4"}
                ]
            },
            {
                "title": "Resolving Printer Problems",
                "body": "<p>Printers are the most common source of office IT headaches. Common fixes include:</p><ul><li><strong>Printer Offline:</strong> Check physical USB or network cables. Ensure the power light is steady green.</li><li><strong>Paper Jam:</strong> Open the printer access door gently, pull jammed paper out in the direction of feed (do not tear it), and close the door firmly.</li><li><strong>Stuck Print Queue:</strong> Open <em>Printers &amp; Scanners &gt; Open Queue</em>. Right-click corrupted print jobs and click <strong>Cancel All Documents</strong>, then reprint.</li></ul>",
                "ui_sim": {
                    "title": "Windows Task Manager Interface",
                    "content": "<div style='background:#ffffff; border:1px solid #cbd5e1; border-radius:4px; font-size:0.85rem;'><div style='background:#f1f5f9; padding:6px 12px; font-weight:700; border-bottom:1px solid #cbd5e1; display:flex; justify-content:space-between;'><span>Task Manager (Processes)</span><button style='background:#dc2626; color:#ffffff; border:none; padding:3px 10px; border-radius:4px; font-weight:700;'>End Task</button></div><div style='padding:8px 12px;'><div style='display:flex; justify-content:space-between; padding:4px 0; border-bottom:1px solid #f1f5f9;'><span style='color:#0f172a;'><i class='fa-regular fa-file-word' style='color:#2563eb;'></i> Microsoft Word</span><span style='color:#dc2626; font-weight:700;'>Not Responding</span></div><div style='display:flex; justify-content:space-between; padding:4px 0;'><span style='color:#0f172a;'><i class='fa-solid fa-globe' style='color:#38bdf8;'></i> Google Chrome</span><span style='color:#16a34a;'>Running (0.8% CPU)</span></div></div></div>"
                }
            },
            {
                "title": "Troubleshooting Lost Wi-Fi & Low Storage",
                "body": "<p>When internet stops working:</p><ul><li>Toggle <strong>Airplane Mode</strong> ON for 10 seconds, then OFF to force your network card to reconnect.</li><li>Restart your home or office broadband router.</li><li>For <strong>'Low Disk Space'</strong> warnings: Run <strong>Disk Cleanup</strong> or Storage Sense to clear temporary internet cache and empty the Recycle Bin.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A worker is typing an urgent report when Microsoft Word freezes. The window says 'Word (Not Responding)' and will not close when clicking the top right X. Explain how the worker can close this frozen program without turning off the entire computer.",
            "steps": [
                {
                    "action": "Open Task Manager",
                    "solution": "Press Ctrl + Shift + Esc (or Ctrl + Alt + Delete) to open Task Manager.",
                    "mark": "[B1]",
                    "rationale": "Task Manager is the system diagnostic tool for process management."
                },
                {
                    "action": "Terminate the frozen process",
                    "solution": "Select Microsoft Word from the process list and click 'End Task'.",
                    "mark": "[B1]",
                    "rationale": "Terminates the hung application cleanly while preserving operating system stability."
                }
            ],
            "tutor_rule": "Never recommend 'Unplug the power cord' in an exam! The accredited answer for a frozen program is always 'Open Task Manager and click End Task'."
        },
        "drills": [
            {
                "question": "Which Windows tool allows you to force-close an unresponsive application that is frozen on your screen?",
                "options": [
                    {"text": "Task Manager (Ctrl + Shift + Esc)", "correct": True},
                    {"text": "Recycle Bin", "correct": False},
                    {"text": "Notepad", "correct": False},
                    {"text": "Calculator", "correct": False}
                ],
                "explanation": "Task Manager lists all active processes and provides the 'End Task' command to shut down frozen software."
            },
            {
                "question": "A worker clicks 'Print' three times, but nothing prints and the printer queue shows three pending jobs. What should they do first?",
                "options": [
                    {"text": "Open the print queue and cancel the stuck print jobs before checking paper and ink", "correct": True},
                    {"text": "Buy a brand new computer", "correct": False},
                    {"text": "Click print another twenty times", "correct": False},
                    {"text": "Pour water into the paper tray", "correct": False}
                ],
                "explanation": "Clearing the jammed print queue removes corrupted spooler tasks that block subsequent printing."
            },
            {
                "question": "What is the quickest way to free up hard drive space when a computer displays a 'Low Disk Space' warning?",
                "options": [
                    {"text": "Empty the Recycle Bin and run Disk Cleanup to delete temporary files", "correct": True},
                    {"text": "Change your desktop wallpaper", "correct": False},
                    {"text": "Mute the system speakers", "correct": False},
                    {"text": "Install three new games", "correct": False}
                ],
                "explanation": "Emptying the Recycle Bin and cleaning temporary files immediately recovers occupied storage."
            }
        ],
        "practice": {
            "task": "A colleague calls you for advice: their laptop suddenly lost internet connection while working from home. List two basic troubleshooting steps they should attempt before calling external technical support.",
            "scaffold_starter": "Troubleshooting Step 1: \nTroubleshooting Step 2: ",
            "model_answer": "Troubleshooting Step 1: Check the Wi-Fi icon, toggle Airplane mode ON and OFF (or disconnect and reconnect to the home Wi-Fi).\nTroubleshooting Step 2: Restart the home broadband router / hub and restart the laptop to reset the network adapter.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Checking Wi-Fi settings / toggling network connection or airplane mode."},
                {"tag": "[1 Mark]", "desc": "Restarting the broadband router or restarting the device."}
            ]
        },
        "revision_links": [
            {"label": "Network Security & VPNs", "href": "l1-network-connections-security.html"},
            {"label": "Data Backups & Cloud Sync", "href": "l1-backups-cloud-sync.html"},
            {"label": "Folder Hierarchies & Sizes", "href": "l1-file-management-hierarchies.html"}
        ]
    },
    {
        "slug": "l1-backups-cloud-sync",
        "code": "L1.1.5",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Data Backup and Cloud Synchronisation",
        "time": "15 Mins",
        "lead": "Protect valuable digital work against hard drive failure, theft, and ransomware: implement the 3-2-1 backup strategy, configure automatic cloud synchronisation, and restore previous file versions.",
        "objectives": [
            "Explain the importance of regular data backups for disaster recovery",
            "Differentiate between manual external backups and automated cloud synchronisation",
            "Use Version History to restore previous drafts of documents after accidental overwrites"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Level 1 Digital Skills - Backups & Version History",
        "steps": [
            {
                "title": "Why Backups Are Essential",
                "body": "<p>Computers can fail at any moment due to hardware crashes, water spills, malware encryption (ransomware), or theft. A <strong>Backup</strong> is a separate duplicate copy of your data kept in a different physical or digital location.</p><p>Without backups, losing a computer could mean losing years of financial accounts, client records, and legal compliance files.</p>"
            },
            {
                "title": "Automated Cloud Sync vs Manual Backups",
                "body": "<p>Organisations combine two main backup methods:</p><ul><li><strong>Automated Cloud Synchronisation (OneDrive / Google Drive):</strong> Runs silently in the background. As soon as you save a document, the cloud client uploads the latest version to encrypted remote servers automatically.</li><li><strong>External Physical Backup:</strong> Copying folders to an external encrypted USB hard drive or NAS drive kept in a fireproof safe off-site.</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "The Industry Standard 3-2-1 Backup Rule",
                    "text": "Keep <strong>3 copies</strong> of your data, on <strong>2 different types of media</strong> (e.g. computer hard drive + cloud), with <strong>1 copy stored off-site</strong>!"
                }
            },
            {
                "title": "Using Version History to Recover Overwritten Files",
                "body": "<p>Have you ever accidentally deleted three pages of a report, clicked Save, and then panicked? Cloud storage solves this with <strong>Version History</strong>:</p><ol><li>Open the document in Word or Excel.</li><li>Click the title bar at the top or go to <strong>File &gt; Info &gt; Version History</strong>.</li><li>A panel appears showing older autosaved versions timestamped by date and author.</li><li>Select a previous version and click <strong>Restore</strong> to recover your lost work!</li></ol>",
                "ui_sim": {
                    "title": "Cloud Version History Panel",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='font-weight:700; color:#0f172a; margin-bottom:6px;'><i class='fa-solid fa-clock-rotate-left' style='color:#0284c7;'></i> Version History &gt; Annual_Report.docx</div><div style='display:flex; flex-direction:column; gap:4px;'><div style='background:#e0f2fe; padding:6px; border-radius:4px; display:flex; justify-content:space-between;'><span><strong>Today, 14:22</strong> (Current Version)</span><span style='color:#64748b;'>Abdul</span></div><div style='background:#ffffff; padding:6px; border-radius:4px; display:flex; justify-content:space-between;'><span>Yesterday, 09:15</span><button style='background:#10b981; color:#ffffff; border:none; padding:2px 8px; border-radius:4px; font-weight:700;'>Restore</button></div></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A medical centre stores all patient survey spreadsheets on a single desktop computer in reception. The centre manager is worried about what would happen if the hard drive failed. State two recommendations to ensure their data is protected against hardware failure.",
            "steps": [
                {
                    "action": "First backup recommendation",
                    "solution": "Enable automated cloud backup (e.g. OneDrive) so spreadsheets sync continuously to secure remote servers.",
                    "mark": "[B1]",
                    "rationale": "Automated cloud backup guarantees real-time off-site disaster recovery."
                },
                {
                    "action": "Second backup recommendation",
                    "solution": "Perform regular scheduled backups to an external hard drive stored securely away from the machine.",
                    "mark": "[B1]",
                    "rationale": "Provides a secondary offline physical backup copy."
                }
            ],
            "tutor_rule": "In Level 1 exams, backup answers should include 'regularity' (daily/weekly) and 'location' (cloud or off-site storage)."
        },
        "drills": [
            {
                "question": "What is the primary purpose of creating regular data backups?",
                "options": [
                    {"text": "To recover your files if your computer is stolen, infected with ransomware, or suffers hardware failure", "correct": True},
                    {"text": "To make your internet connection faster", "correct": False},
                    {"text": "To reduce the price of your software subscriptions", "correct": False},
                    {"text": "To automatically turn off your computer at night", "correct": False}
                ],
                "explanation": "Backups ensure business continuity and disaster recovery in the event of hardware or cyber failure."
            },
            {
                "question": "What feature allows you to restore an earlier draft of a document if a colleague accidentally overwrites important paragraphs?",
                "options": [
                    {"text": "Version History", "correct": True},
                    {"text": "Screen Magnifier", "correct": False},
                    {"text": "High Contrast Mode", "correct": False},
                    {"text": "Spell Checker", "correct": False}
                ],
                "explanation": "Version History stores previous timestamps of files, allowing users to roll back unwanted edits."
            },
            {
                "question": "In the 3-2-1 backup rule, what does the '1' stand for?",
                "options": [
                    {"text": "Keep at least 1 backup copy off-site or in the cloud", "correct": True},
                    {"text": "Only back up 1 file per week", "correct": False},
                    {"text": "Use only 1 password for everything", "correct": False},
                    {"text": "Have only 1 computer in your office", "correct": False}
                ],
                "explanation": "1 copy must be kept off-site (cloud or remote safe) so local disasters like fire or flood do not destroy all copies."
            }
        ],
        "practice": {
            "task": "A charity organisation currently saves all volunteer records onto a single laptop. Explain two reasons why relying solely on local laptop storage is dangerous, and what backup solution they should implement.",
            "scaffold_starter": "Risk 1: \nRisk 2: \nRecommended backup solution: ",
            "model_answer": "Risk 1: If the laptop is lost, stolen, or damaged, all records will be permanently lost with no way to recover them.\nRisk 2: If the laptop is infected with ransomware or a virus, the local files could be encrypted or corrupted.\nSolution: Set up automated cloud synchronisation (e.g. OneDrive) and perform regular backups to an external encrypted hard drive.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Identifying risks of physical loss, hardware failure, or malware."},
                {"tag": "[1 Mark]", "desc": "Recommending cloud backup or external drive scheduled backup."}
            ]
        },
        "revision_links": [
            {"label": "Troubleshooting IT Issues", "href": "l1-troubleshooting-system-errors.html"},
            {"label": "Folder Hierarchies & Sizes", "href": "l1-file-management-hierarchies.html"},
            {"label": "Cybersecurity & Malware", "href": "l1-cybersecurity-malware-defence.html"}
        ]
    }
]
