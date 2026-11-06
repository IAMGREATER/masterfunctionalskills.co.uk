# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Entry 3 Digital Skills Curriculum Data
Author: Abdul (MFS Pedagogical Systems)
Strictly adheres to:
- Official name: Entry 3 (never "Entry Level 3")
- Confidentiality: Strictly Master Functional Skills / generic vocational contexts
- Pearson Edexcel & C&G DFSQ standards
"""

ENTRY_3_TOPICS = [
    # -------------------------------------------------------------------------
    # Skill Area 1: Using Devices and Handling Information
    # -------------------------------------------------------------------------
    {
        "slug": "e3-hardware-software-devices",
        "code": "E3.1.1",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Hardware, Software and Digital Devices",
        "time": "15 Mins",
        "lead": "Understand the difference between computer hardware and software, recognise common digital devices used at work and home, and identify essential input and output equipment.",
        "objectives": [
            "Differentiate between physical hardware and digital software",
            "Identify desktop computers, laptops, tablets, and smartphones",
            "Classify everyday input devices (keyboard, mouse) and output devices (monitor, printer)"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Hardware vs Software & Peripherals",
        "steps": [
            {
                "title": "What is Hardware vs Software?",
                "body": "<p><strong>Hardware</strong> refers to the physical electronic parts you can see and touch with your hands — such as the screen, keyboard, mouse, or system unit.</p><p><strong>Software</strong> refers to the programs, apps, and operating systems that run inside the device to perform tasks. Without software, hardware cannot do anything.</p>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Golden Memory Rule",
                    "text": "If you can physically touch it, drop it, or plug it in, it is <strong>Hardware</strong>. If it is a digital program or app displayed on the screen, it is <strong>Software</strong>."
                }
            },
            {
                "title": "Input Devices vs Output Devices",
                "body": "<p>To interact with a digital device, you use peripherals:</p><ul><li><strong>Input Devices (Putting data IN):</strong> Keyboard (typing text), Mouse or Touchpad (pointing and clicking), Touchscreen (tapping commands), Microphone (recording voice).</li><li><strong>Output Devices (Getting data OUT):</strong> Monitor/Screen (displaying visual information), Printer (producing physical paper copies), Speakers or Headphones (playing audio alerts and speech).</li></ul>",
                "ui_sim": {
                    "title": "Device Peripheral Classification",
                    "content": "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px;'><div><strong style='color:#0284c7;'><i class='fa-solid fa-arrow-right-to-bracket'></i> INPUT (To Device)</strong><br>&bull; Keyboard &bull; Mouse<br>&bull; Touchscreen &bull; Scanner<br>&bull; Microphone &bull; Webcam</div><div><strong style='color:#0f766e;'><i class='fa-solid fa-arrow-up-right-from-square'></i> OUTPUT (From Device)</strong><br>&bull; Monitor Screen<br>&bull; Laser/Inkjet Printer<br>&bull; Audio Speakers<br>&bull; Headphones</div></div>"
                },
                "shortcuts": [
                    {"label": "Windows Settings", "key": "Win + I"},
                    {"label": "Help Screen", "key": "F1"}
                ]
            },
            {
                "title": "Operating Systems (OS)",
                "body": "<p>The <strong>Operating System</strong> is the master software that controls the whole computer. It starts up when you turn on the power and manages all other programs.</p><p>Common operating systems include <strong>Microsoft Windows</strong> (common on PCs and workplace laptops), <strong>macOS</strong> (Apple Mac computers), <strong>Android</strong> (tablets and smartphones), and <strong>iOS / iPadOS</strong> (Apple iPhones and iPads).</p>",
                "callout": {
                    "type": "vocational",
                    "title": "Workplace Scenario",
                    "text": "In a community healthcare clinic or busy administrative reception, staff use desktop computers running Windows to book appointments, barcode scanners (input) to scan patient wristbands, and receipt printers (output) for appointment cards."
                }
            }
        ],
        "exam_model": {
            "scenario": "A clinic administrator needs to set up a new digital reception desk. They must connect equipment that allows patients to type their check-in details, and an output device that prints their appointment ticket. State one suitable input device and one suitable output device.",
            "steps": [
                {
                    "action": "Identify the Input Device",
                    "solution": "Touchscreen or Keyboard",
                    "mark": "[B1]",
                    "rationale": "A touchscreen or keyboard allows user interaction by putting text or selection data directly into the check-in system."
                },
                {
                    "action": "Identify the Output Device",
                    "solution": "Printer (or Monitor Screen)",
                    "mark": "[B1]",
                    "rationale": "A printer outputs physical paper tickets containing the queue number, clearly satisfying the output criteria."
                }
            ],
            "tutor_rule": "In Entry 3 exams, questions often ask you to circle or tick items from a list. Always ask yourself: 'Does this put information into the computer, or does it give information out?'"
        },
        "drills": [
            {
                "question": "Which one of the following is an OUTPUT device?",
                "options": [
                    {"text": "Computer Keyboard", "correct": False},
                    {"text": "Optical Mouse", "correct": False},
                    {"text": "Laser Printer", "correct": True},
                    {"text": "Webcam", "correct": False}
                ],
                "explanation": "A Laser Printer produces physical documents from digital data, which makes it an output device. Keyboards, mice, and webcams send data into the computer."
            },
            {
                "question": "True or False: Microsoft Word and Google Chrome are examples of Computer Hardware.",
                "options": [
                    {"text": "True", "correct": False},
                    {"text": "False", "correct": True}
                ],
                "explanation": "False! Word and Chrome are programs/applications, which means they are Software, not physical hardware."
            },
            {
                "question": "Which piece of software is responsible for controlling the computer hardware and running applications?",
                "options": [
                    {"text": "Operating System (such as Windows)", "correct": True},
                    {"text": "Internet Browser", "correct": False},
                    {"text": "Spreadsheet Program", "correct": False},
                    {"text": "Anti-virus Scan", "correct": False}
                ],
                "explanation": "The Operating System (e.g. Windows, Android, macOS) is the core system software that manages hardware and runs all other user applications."
            }
        ],
        "practice": {
            "task": "A staff member at a local care facility is ordering new IT equipment. Look at the list below and classify each item as either Hardware or Software:<br>1. Monitor<br>2. Windows 11<br>3. USB Mouse<br>4. Email Application (Outlook)<br><br>Write your answers into the scratchpad.",
            "scaffold_starter": "1. Monitor: Hardware\n2. Windows 11: \n3. USB Mouse: \n4. Email Application (Outlook): ",
            "model_answer": "1. Monitor: Hardware\n2. Windows 11: Software (Operating System)\n3. USB Mouse: Hardware (Input Device)\n4. Email Application (Outlook): Software (Application)",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Correctly identifying Monitor and USB Mouse as Hardware."},
                {"tag": "[1 Mark]", "desc": "Correctly identifying Windows 11 and Email Application as Software."}
            ]
        },
        "revision_links": [
            {"label": "Power & Navigation", "href": "e3-device-controls-navigation.html"},
            {"label": "Display & Accessibility", "href": "e3-accessibility-display-settings.html"},
            {"label": "Files & Folders", "href": "e3-organising-files-folders.html"}
        ]
    },
    {
        "slug": "e3-device-controls-navigation",
        "code": "E3.1.2",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Power, Login and Desktop Navigation",
        "time": "15 Mins",
        "lead": "Master safe startup, unlocking, login credentials, sleep mode, restart, and shutting down digital devices, alongside confident desktop navigation.",
        "objectives": [
            "Turn on, unlock, restart, and safely shut down digital devices",
            "Understand the difference between Sleep, Restart, and Shut Down",
            "Navigate the desktop, taskbar, start menu, and system tray icons"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Safe Power & Desktop Navigation",
        "steps": [
            {
                "title": "Starting Up and Logging In",
                "body": "<p>To turn on a computer, press the physical <strong>Power Button</strong> once. When the lock screen appears, click or swipe up, then enter your <strong>Username</strong> and <strong>Password / PIN</strong>.</p><p>Never share your password with colleagues. If you walk away from your desk, lock the screen immediately to protect confidentiality.</p>",
                "shortcuts": [
                    {"label": "Lock Computer Immediately", "key": "Win + L"},
                    {"label": "Open Start Menu", "key": "Win Key"}
                ]
            },
            {
                "title": "Sleep vs Restart vs Shut Down",
                "body": "<p>Always use the software power menu rather than holding down the physical button:</p><ul><li><strong>Shut Down:</strong> Completely closes all open programs, saves system state, and turns off the electrical power safely. Use this at the end of the working day.</li><li><strong>Restart:</strong> Closes all programs, shuts down the system, and immediately turns it back on. Essential when installing updates or fixing glitches.</li><li><strong>Sleep Mode:</strong> Puts the computer into a low-power state. Open work remains in memory so you can resume work instantly when touching a key.</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Exam Trap: Unsaved Work",
                    "text": "Before choosing 'Shut Down' or 'Restart', always save your files! Shutting down without saving will cause you to lose unsaved progress."
                }
            },
            {
                "title": "Navigating the Desktop & Taskbar",
                "body": "<p>The main screen after logging in is the <strong>Desktop</strong>. At the bottom is the <strong>Taskbar</strong>:</p><ul><li><strong>Start Button:</strong> Click to view all installed applications, files, and power options.</li><li><strong>Pinned Apps:</strong> Frequently used icons kept on the taskbar for single-click opening.</li><li><strong>System Tray / Notification Area:</strong> Located on the bottom right, displaying the clock, Wi-Fi status, volume, and battery percentage.</li></ul>",
                "ui_sim": {
                    "title": "Windows Desktop Taskbar Layout",
                    "content": "<div style='display:flex; justify-content:space-between; align-items:center; background:#1e293b; color:#ffffff; padding:10px 14px; border-radius:6px;'><div><i class='fa-brands fa-windows' style='color:#38bdf8; font-size:1.2rem; margin-right:12px;'></i> <strong>Start</strong> &nbsp;|&nbsp; <i class='fa-regular fa-folder' style='color:#f59e0b;'></i> Files &nbsp;|&nbsp; <i class='fa-solid fa-globe' style='color:#38bdf8;'></i> Browser</div><div style='font-size:0.85rem;'><i class='fa-solid fa-wifi'></i> &nbsp; <i class='fa-solid fa-volume-high'></i> &nbsp; 100% &nbsp; <strong>09:30 AM</strong></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A clinic worker is leaving their desk for a 15-minute tea break. The computer contains confidential patient appointments. Explain what action the worker must take to keep the device secure while away from the desk.",
            "steps": [
                {
                    "action": "Select the correct security action",
                    "solution": "Lock the device (or press Windows Key + L)",
                    "mark": "[B1]",
                    "rationale": "Locking the device hides the active screen behind the password prompt while keeping programs open safely."
                },
                {
                    "action": "Explain why this protects data",
                    "solution": "Prevents unauthorized people from viewing or accessing sensitive information without logging in.",
                    "mark": "[B1]",
                    "rationale": "Demonstrates understanding of data security and confidentiality standards."
                }
            ],
            "tutor_rule": "In Entry 3 exams, questions often ask what to do when stepping away briefly: the answer is 'Lock the device'. At the end of the shift, the answer is 'Save work and Shut Down'."
        },
        "drills": [
            {
                "question": "What keyboard shortcut quickly locks a Windows computer when you step away from your desk?",
                "options": [
                    {"text": "Windows Key + L", "correct": True},
                    {"text": "Ctrl + Alt + Delete", "correct": False},
                    {"text": "Alt + F4", "correct": False},
                    {"text": "Windows Key + E", "correct": False}
                ],
                "explanation": "Pressing Windows Key + L instantly locks the screen, requiring a password or PIN to unlock."
            },
            {
                "question": "Which power option reboots the computer automatically, which is helpful after installing an update?",
                "options": [
                    {"text": "Shut Down", "correct": False},
                    {"text": "Restart", "correct": True},
                    {"text": "Sleep", "correct": False},
                    {"text": "Hibernate", "correct": False}
                ],
                "explanation": "Restart closes all programs, powers down the operating system, and boots it back up fresh."
            },
            {
                "question": "Where on the screen do you normally find the clock, battery level, and Wi-Fi signal icon?",
                "options": [
                    {"text": "In the Recycle Bin", "correct": False},
                    {"text": "In the System Tray / Notification Area (bottom right)", "correct": True},
                    {"text": "Inside the Documents folder", "correct": False},
                    {"text": "On the Title Bar of Microsoft Word", "correct": False}
                ],
                "explanation": "The System Tray on the bottom-right corner of the taskbar displays status icons like network, volume, and clock."
            }
        ],
        "practice": {
            "task": "You are finishing your shift at the office. State the two essential steps you must complete before leaving your computer workstation for the day.",
            "scaffold_starter": "Step 1 (Files): \nStep 2 (Power): ",
            "model_answer": "Step 1: Save and close all open files and programs.\nStep 2: Click the Start Menu, select Power, and click 'Shut down'.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Saving all open work/files before closing."},
                {"tag": "[1 Mark]", "desc": "Selecting the official Shut Down option from the Start/Power menu."}
            ]
        },
        "revision_links": [
            {"label": "Hardware & Devices", "href": "e3-hardware-software-devices.html"},
            {"label": "Connecting Wi-Fi", "href": "e3-connecting-wifi-bluetooth.html"},
            {"label": "Organising Folders", "href": "e3-organising-files-folders.html"}
        ]
    },
    {
        "slug": "e3-connecting-wifi-bluetooth",
        "code": "E3.1.3",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Connecting to Wi-Fi and Bluetooth Networks",
        "time": "15 Mins",
        "lead": "Learn how to find and connect your device to wireless internet (Wi-Fi), enter network security keys safely, and pair Bluetooth devices like wireless mice and headsets.",
        "objectives": [
            "Locate available Wi-Fi networks using the network icon",
            "Connect to a secure Wi-Fi network using the correct password / security key",
            "Pair and connect Bluetooth peripherals (wireless mouse, headphones)"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Wi-Fi Connections & Bluetooth Pairing",
        "steps": [
            {
                "title": "Connecting to a Wi-Fi Network",
                "body": "<p>Wi-Fi allows your device to connect to the internet without plugging in a physical cable:</p><ol><li>Click the <strong>Network / Wi-Fi icon</strong> in the bottom right taskbar (or top right on mobile devices).</li><li>A list of available network names (SSIDs) will appear. Click on your organisation or home network name.</li><li>Ensure <strong>'Connect automatically'</strong> is ticked if it is a trusted network.</li><li>Click <strong>Connect</strong> and type the exact <strong>Network Security Key (password)</strong>. Passwords are case-sensitive.</li></ol>",
                "ui_sim": {
                    "title": "Wi-Fi Network Selection Dialogue",
                    "content": "<div style='background:#f1f5f9; padding:12px; border-radius:6px;'><div style='display:flex; justify-content:space-between; margin-bottom:8px; font-weight:700;'><span style='color:#0f172a;'><i class='fa-solid fa-wifi' style='color:#0284c7;'></i> Clinic_Staff_Secure</span><span style='color:#0f766e;'><i class='fa-solid fa-lock'></i> Secured</span></div><div style='background:#ffffff; border:1px solid #cbd5e1; padding:8px 12px; border-radius:4px; font-size:0.9rem; margin-bottom:8px;'><i class='fa-solid fa-key' style='color:#94a3b8; margin-right:6px;'></i> Enter network security key: &bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</div><button style='background:#0284c7; color:#ffffff; border:none; padding:6px 14px; border-radius:4px; font-weight:700; cursor:pointer;'>Connect</button></div>"
                }
            },
            {
                "title": "Recognising Secure vs Open Wi-Fi",
                "body": "<p>When viewing Wi-Fi networks, look closely at the symbol:</p><ul><li><strong>Padlock Icon:</strong> Indicates a <strong>Secured Network</strong>. You must enter a password. Data transmitted between your device and the router is encrypted.</li><li><strong>No Padlock / Shield Warning:</strong> Indicates an <strong>Open Public Network</strong> (e.g. at a café or train station). Anyone can connect without a password, but your data could be monitored by others.</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Security Golden Rule",
                    "text": "Never carry out online banking, input credit card numbers, or view confidential medical records on an unsecured public Wi-Fi network without encryption."
                }
            },
            {
                "title": "Connecting Bluetooth Peripherals",
                "body": "<p><strong>Bluetooth</strong> is a short-range wireless technology used to connect nearby accessories (typically within 10 metres) such as wireless mice, keyboards, and headsets.</p><p>To pair a device: Turn on Bluetooth on your computer, switch your accessory into pairing mode, click <strong>Add Bluetooth Device</strong> in Settings, and choose your accessory from the list.</p>",
                "shortcuts": [
                    {"label": "Quick Settings Panel", "key": "Win + A"}
                ]
            }
        ],
        "exam_model": {
            "scenario": "A community worker arrives at a new office with their work laptop. They need to connect to the office internet. The network list shows 'Office_Staff' with a padlock icon, and 'Guest_Free' with no padlock. Explain which network they should choose and what information they will need.",
            "steps": [
                {
                    "action": "Select the correct network",
                    "solution": "Office_Staff",
                    "mark": "[B1]",
                    "rationale": "It is a secured network with a padlock icon, protecting work data from being intercepted."
                },
                {
                    "action": "Identify the required credential",
                    "solution": "Network security key / Wi-Fi password",
                    "mark": "[B1]",
                    "rationale": "A secured network requires an authorized password or security key to connect."
                }
            ],
            "tutor_rule": "Always look for the padlock icon in exam screenshots. Padlock means secured and encrypted."
        },
        "drills": [
            {
                "question": "What does a padlock icon next to a Wi-Fi network name mean?",
                "options": [
                    {"text": "The network is broken and cannot be used", "correct": False},
                    {"text": "The network is password-protected and secure", "correct": True},
                    {"text": "The network is only available to guests", "correct": False},
                    {"text": "The network has no internet connection", "correct": False}
                ],
                "explanation": "A padlock icon indicates a secured network that requires a password/key and encrypts your connection."
            },
            {
                "question": "Which wireless technology is typically used to connect a wireless mouse or headset to a laptop over short distances?",
                "options": [
                    {"text": "Bluetooth", "correct": True},
                    {"text": "Satellite Broadband", "correct": False},
                    {"text": "Ethernet Cable", "correct": False},
                    {"text": "4G Mobile Data", "correct": False}
                ],
                "explanation": "Bluetooth is designed specifically for short-range cable-free connections between devices and nearby accessories."
            },
            {
                "question": "True or False: Passwords for Wi-Fi networks are case-sensitive, meaning capital letters and lowercase letters must match exactly.",
                "options": [
                    {"text": "True", "correct": True},
                    {"text": "False", "correct": False}
                ],
                "explanation": "True! Network security keys treat 'Password' and 'password' as completely different words."
            }
        ],
        "practice": {
            "task": "A student needs to connect their tablet to their home Wi-Fi. Write down the three steps they must follow using the onscreen settings menu.",
            "scaffold_starter": "Step 1: Open the Wi-Fi list by...\nStep 2: Tap on...\nStep 3: Type the...",
            "model_answer": "Step 1: Tap the Wi-Fi or network icon to display available networks.\nStep 2: Select their home network name (SSID) from the list.\nStep 3: Enter the correct network security key (Wi-Fi password) and tap Connect.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Opening/viewing available network list."},
                {"tag": "[1 Mark]", "desc": "Selecting the correct network and entering the security key/password."}
            ]
        },
        "revision_links": [
            {"label": "Power & Navigation", "href": "e3-device-controls-navigation.html"},
            {"label": "Online Passwords & Scams", "href": "e3-passwords-privacy-scams.html"},
            {"label": "Email Attachments", "href": "e3-email-attachments-contacts.html"}
        ]
    },
    {
        "slug": "e3-accessibility-display-settings",
        "code": "E3.1.4",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Display and Accessibility Settings",
        "time": "15 Mins",
        "lead": "Customise your computer screen and sound settings to suit your personal needs, including screen brightness, font size, high contrast, volume, and text-to-speech features.",
        "objectives": [
            "Adjust screen brightness and speaker volume controls",
            "Increase text size and enable high-contrast display modes",
            "Use built-in assistive technologies like Magnifier and Screen Reader"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Accessibility & Display Settings",
        "steps": [
            {
                "title": "Adjusting Volume and Screen Brightness",
                "body": "<p>Maintaining comfortable screen brightness and audio volume protects your eyes and ears from fatigue:</p><ul><li><strong>Audio Volume:</strong> Click the speaker icon in the bottom right corner of the taskbar. Drag the slider to the right to increase volume, or click the speaker symbol to mute.</li><li><strong>Screen Brightness:</strong> Open Windows Settings (Win + I), click <strong>System &gt; Display</strong>, and drag the brightness slider. Reducing brightness saves battery life and reduces glare in low light.</li></ul>",
                "ui_sim": {
                    "title": "System Volume & Brightness Sliders",
                    "content": "<div style='display:flex; flex-direction:column; gap:10px; background:#f8fafc; padding:12px; border-radius:6px;'><div style='display:flex; align-items:center; gap:10px;'><i class='fa-solid fa-volume-high' style='color:#0284c7; width:20px;'></i> <div style='flex-grow:1; height:8px; background:#cbd5e1; border-radius:4px; position:relative;'><div style='width:65%; height:100%; background:#0284c7; border-radius:4px;'></div></div> <span style='font-size:0.85rem; font-weight:700;'>65%</span></div><div style='display:flex; align-items:center; gap:10px;'><i class='fa-solid fa-sun' style='color:#f59e0b; width:20px;'></i> <div style='flex-grow:1; height:8px; background:#cbd5e1; border-radius:4px; position:relative;'><div style='width:80%; height:100%; background:#f59e0b; border-radius:4px;'></div></div> <span style='font-size:0.85rem; font-weight:700;'>80%</span></div></div>"
                }
            },
            {
                "title": "Text Size and High Contrast for Visual Clarity",
                "body": "<p>For people with visual impairments or dyslexia, standard text can be difficult to read:</p><ul><li><strong>Make Text Bigger:</strong> In Settings, choose <strong>Accessibility &gt; Text size</strong>. Drag the slider until sample text is comfortable to read without squinting, then click <strong>Apply</strong>.</li><li><strong>High Contrast Themes:</strong> Replaces low-contrast grey backgrounds with distinct black and yellow/white high-visibility colour schemes, making letters clearly stand out.</li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Dyslexia Readability Tip",
                    "text": "Pairing larger text sizes with a soft cream or peach background tint reduces visual stress and eliminates glare when reading long documents."
                }
            },
            {
                "title": "Magnifier and Screen Readers",
                "body": "<p>Operating systems include built-in assistive tools:</p><ul><li><strong>Magnifier:</strong> Zooms in on any section of the screen (press <kbd class='dfs-kbd'>Win</kbd> + <kbd class='dfs-kbd'>+</kbd>).</li><li><strong>Narrator / Screen Reader:</strong> Speaks the text on the screen aloud for users with visual disabilities.</li></ul>",
                "shortcuts": [
                    {"label": "Open Magnifier Zoom In", "key": "Win + Plus"},
                    {"label": "Zoom Out Magnifier", "key": "Win + Minus"},
                    {"label": "Exit Magnifier", "key": "Win + Esc"}
                ]
            }
        ],
        "exam_model": {
            "scenario": "A worker with mild visual impairment finds the text on their computer screen too small to read comfortably during their shift. Give two settings or accessibility tools built into the operating system that will make text easier to read.",
            "steps": [
                {
                    "action": "State first accessibility feature",
                    "solution": "Increase text size slider in Accessibility / Display settings",
                    "mark": "[B1]",
                    "rationale": "Larger fonts improve text legibility across all windows and menus."
                },
                {
                    "action": "State second accessibility feature",
                    "solution": "Turn on Screen Magnifier (or High Contrast mode)",
                    "mark": "[B1]",
                    "rationale": "Magnifier zooms into specific content; high contrast increases boundary sharpness."
                }
            ],
            "tutor_rule": "In Entry 3 exams, accessibility questions focus on making things easier to see or hear: text size, magnifier, contrast themes, and volume."
        },
        "drills": [
            {
                "question": "Which accessibility feature speaks the text displayed on the screen aloud for users who cannot see the monitor?",
                "options": [
                    {"text": "Screen Reader / Narrator", "correct": True},
                    {"text": "Spell Checker", "correct": False},
                    {"text": "Screen Saver", "correct": False},
                    {"text": "Bluetooth Manager", "correct": False}
                ],
                "explanation": "A Screen Reader (such as Windows Narrator) reads aloud text, buttons, and menus using synthetic speech."
            },
            {
                "question": "If screen glare is hurting a worker's eyes in a dimly lit office, what display setting should they adjust?",
                "options": [
                    {"text": "Increase volume to maximum", "correct": False},
                    {"text": "Decrease screen brightness", "correct": True},
                    {"text": "Change the computer password", "correct": False},
                    {"text": "Empty the Recycle Bin", "correct": False}
                ],
                "explanation": "Lowering screen brightness reduces glare and eye strain in low-light environments."
            },
            {
                "question": "What keyboard shortcut turns on the built-in Magnifier tool to zoom in on the screen in Windows?",
                "options": [
                    {"text": "Windows Key + Plus (+)", "correct": True},
                    {"text": "Ctrl + P", "correct": False},
                    {"text": "Alt + Tab", "correct": False},
                    {"text": "Shift + Delete", "correct": False}
                ],
                "explanation": "Windows Key + Plus activates the Magnifier tool and zooms in."
            }
        ],
        "practice": {
            "task": "A colleague is struggling to hear training video instructions on their computer speakers. Explain two different ways they can resolve this sound issue.",
            "scaffold_starter": "Solution 1: \nSolution 2: ",
            "model_answer": "Solution 1: Click the speaker icon in the taskbar and increase the volume slider (or un-mute).\nSolution 2: Connect a pair of headphones to hear the audio clearly without background noise.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Adjusting system volume slider / checking mute setting."},
                {"tag": "[1 Mark]", "desc": "Using headphones or external amplified speakers."}
            ]
        },
        "revision_links": [
            {"label": "Hardware & Devices", "href": "e3-hardware-software-devices.html"},
            {"label": "Power & Navigation", "href": "e3-device-controls-navigation.html"},
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"}
        ]
    },
    {
        "slug": "e3-organising-files-folders",
        "code": "E3.1.5",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Organising Files and Folders",
        "time": "15 Mins",
        "lead": "Learn how to structure your work logically: create new folders, give meaningful names to files, move documents between folders, delete unwanted files, and recover deleted items from the Recycle Bin.",
        "objectives": [
            "Create new folders and rename them with clear, logical names",
            "Move, copy, and organise files into suitable subfolders",
            "Delete unwanted files safely and restore accidentally deleted files from the Recycle Bin"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Creating Folders & Managing Files",
        "steps": [
            {
                "title": "Why Folders Matter & How to Create One",
                "body": "<p>A <strong>Folder</strong> acts like a digital drawer that groups related documents together. Without folders, all your files sit in one messy pile, making it hard to find important work.</p><p>To create a folder in File Explorer:</p><ol><li>Open the location where you want the folder (e.g. <strong>Documents</strong>).</li><li>Click <strong>New Folder</strong> on the top toolbar (or right-click in a blank space &gt; <strong>New &gt; Folder</strong>).</li><li>Type a clear, descriptive name (e.g. <code>Clinic Invoices 2026</code>) and press <kbd class='dfs-kbd'>Enter</kbd>.</li></ol>",
                "shortcuts": [
                    {"label": "New Folder Shortcut", "key": "Ctrl + Shift + N"},
                    {"label": "Rename Selected Item", "key": "F2"}
                ]
            },
            {
                "title": "Naming Conventions for Files",
                "body": "<p>Always name files so that anyone in your workplace can understand what the file contains without opening it:</p><ul><li><strong>Poor Name:</strong> <code>doc1.docx</code>, <code>stuff.pdf</code>, <code>final.xlsx</code></li><li><strong>Good Name:</strong> <code>Staff Training Rota October 2026.docx</code>, <code>Equipment Order Form.pdf</code></li></ul>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Naming Rule",
                    "text": "Include the topic and the date: <code>Meeting Minutes 2026-10-15.docx</code>. Avoid symbols like <code>/ \\ : * ? \" &lt; &gt; |</code> as operating systems do not allow them in filenames."
                }
            },
            {
                "title": "Deleting and the Recycle Bin",
                "body": "<p>When you delete a file from your computer's local drive, it is not permanently gone immediately — it moves to the <strong>Recycle Bin</strong> (or Trash):</p><ul><li>To delete: Select the file and press <kbd class='dfs-kbd'>Delete</kbd> (or right-click &gt; Delete).</li><li>To restore a file: Open the Recycle Bin, right-click the deleted file, and click <strong>Restore</strong>. It returns to its exact original location!</li><li>To delete permanently: Click <strong>Empty Recycle Bin</strong>. Once emptied, the file cannot be easily recovered.</li></ul>",
                "ui_sim": {
                    "title": "Recycle Bin Restore Dialogue",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:10px; border-radius:4px;'><div style='color:#0f172a; font-weight:700; margin-bottom:6px;'><i class='fa-regular fa-trash-can' style='color:#dc2626;'></i> Recycle Bin &gt; 'Staff Rota.docx'</div><button style='background:#10b981; color:#ffffff; border:none; padding:6px 12px; border-radius:4px; font-weight:700; cursor:pointer; margin-right:8px;'><i class='fa-solid fa-rotate-left'></i> Restore this item</button><button style='background:#e2e8f0; color:#475569; border:none; padding:6px 12px; border-radius:4px; font-weight:600;'>Empty Recycle Bin</button></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A dental practice has three files saved on their desktop: 'Patient Fees June.xlsx', 'Patient Fees July.xlsx', and 'Dental Care Guide.pdf'. The receptionist needs to organise these. Explain how they should create a suitable folder and move the financial spreadsheets into it.",
            "steps": [
                {
                    "action": "Create and name the folder",
                    "solution": "Create a new folder and name it 'Patient Fees' (or 'Fees 2026')",
                    "mark": "[B1]",
                    "rationale": "Creates a logical container with an appropriate descriptive name."
                },
                {
                    "action": "Move the spreadsheets",
                    "solution": "Drag and drop the two spreadsheet files into the new 'Patient Fees' folder.",
                    "mark": "[M1]",
                    "rationale": "Groups related files together while leaving unrelated guides separate."
                }
            ],
            "tutor_rule": "In Entry 3 exams, folder tasks check that you give sensible names and separate files logically."
        },
        "drills": [
            {
                "question": "What happens when you delete a document from your computer's local hard drive?",
                "options": [
                    {"text": "It is permanently destroyed instantly and can never be retrieved", "correct": False},
                    {"text": "It moves to the Recycle Bin where it can be restored if needed", "correct": True},
                    {"text": "It is automatically emailed to your manager", "correct": False},
                    {"text": "It is printed onto paper automatically", "correct": False}
                ],
                "explanation": "Deleted local files are sent to the Recycle Bin, allowing you to restore them if deleted by accident."
            },
            {
                "question": "Which of the following is the most professional and clear filename for an invoice?",
                "options": [
                    {"text": "inv.xlsx", "correct": False},
                    {"text": "Supplier Invoice Medical Supplies Oct 2026.xlsx", "correct": True},
                    {"text": "document(1).xlsx", "correct": False},
                    {"text": "stuff to pay.xlsx", "correct": False}
                ],
                "explanation": "A descriptive filename tells the user the document type, company/topic, and date clearly."
            },
            {
                "question": "Which keyboard key allows you to quickly rename a selected folder in Windows?",
                "options": [
                    {"text": "F2", "correct": True},
                    {"text": "F5", "correct": False},
                    {"text": "Esc", "correct": False},
                    {"text": "Spacebar", "correct": False}
                ],
                "explanation": "Pressing F2 enters rename mode on any selected file or folder."
            }
        ],
        "practice": {
            "task": "A worker accidentally deleted an important staff survey file two minutes ago. Explain the step-by-step process they must take to get the file back.",
            "scaffold_starter": "Step 1: Open the...\nStep 2: Locate the...\nStep 3: Right-click and choose...",
            "model_answer": "Step 1: Open the Recycle Bin icon on the desktop.\nStep 2: Find the deleted staff survey file in the list.\nStep 3: Right-click the file and click 'Restore'. The file will return to its original folder.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Opening the Recycle Bin."},
                {"tag": "[1 Mark]", "desc": "Selecting the file and choosing the Restore action."}
            ]
        },
        "revision_links": [
            {"label": "Searching Files & Cloud", "href": "e3-searching-files-local-cloud.html"},
            {"label": "Word Processing Basics", "href": "e3-word-processing-basics.html"},
            {"label": "Saving Documents", "href": "e3-spellcheck-proofing-saving.html"}
        ]
    },
    {
        "slug": "e3-searching-files-local-cloud",
        "code": "E3.1.6",
        "skill_area": "1. Using Devices and Handling Information",
        "title": "Searching Files and Local vs Cloud Storage",
        "time": "15 Mins",
        "lead": "Master quick file searching using search bars and keywords, and understand the difference between saving files locally on your device versus saving to cloud storage.",
        "objectives": [
            "Use the search box in File Explorer to quickly find lost documents",
            "Understand local storage (Hard Drive / USB) vs Cloud storage (OneDrive, Google Drive)",
            "Identify the benefits of cloud storage for remote working and automatic backup"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Searching Files & Local vs Cloud Storage",
        "steps": [
            {
                "title": "Searching for Files When You Forget Where They Are",
                "body": "<p>If you cannot remember which folder you saved a document in, you can search for it:</p><ol><li>Open <strong>File Explorer</strong> (<kbd class='dfs-kbd'>Win + E</kbd>).</li><li>Click in the <strong>Search Box</strong> in the top-right corner.</li><li>Type part of the file name (e.g. <code>Rota</code> or <code>Invoice</code>) or a key word inside the document.</li><li>Press <kbd class='dfs-kbd'>Enter</kbd>. The computer will scan folders and display matching files.</li></ol>",
                "shortcuts": [
                    {"label": "Open File Explorer", "key": "Win + E"},
                    {"label": "Focus Search Bar", "key": "Ctrl + F"}
                ]
            },
            {
                "title": "Local Storage vs Cloud Storage",
                "body": "<p>Where your files live makes a big difference to how you access them:</p><ul><li><strong>Local Storage:</strong> Files are saved physically onto your device's internal hard drive or an attached USB memory stick. You do not need the internet to open them, but if your laptop breaks or gets lost, the files are lost with it.</li><li><strong>Cloud Storage:</strong> Files are saved online on secure remote servers managed by providers like Microsoft OneDrive, Google Drive, or Apple iCloud.</li></ul>",
                "ui_sim": {
                    "title": "Storage Location Comparison",
                    "content": "<div style='display:grid; grid-template-columns:1fr 1fr; gap:14px;'><div><strong style='color:#0f172a;'><i class='fa-solid fa-hard-drive'></i> LOCAL STORAGE</strong><br>&bull; Saved on this device only<br>&bull; Works offline (no internet)<br>&bull; Risk of loss if laptop breaks</div><div><strong style='color:#0284c7;'><i class='fa-solid fa-cloud'></i> CLOUD STORAGE</strong><br>&bull; Saved on secure internet servers<br>&bull; Accessible from any device<br>&bull; Automatic backup &amp; sharing</div></div>"
                }
            },
            {
                "title": "Key Advantages of Cloud Storage",
                "body": "<p>Workplaces rely heavily on cloud storage for three main reasons:</p><ol><li><strong>Anywhere Access:</strong> You can start a report on your office computer, view it on your mobile phone on the train, and finish it on your home tablet.</li><li><strong>Disaster Recovery &amp; Backup:</strong> If your laptop is stolen or damaged by water, your files remain 100% safe in the cloud.</li><li><strong>Collaboration:</strong> Multiple team members can work on the same document together in real time.</li></ol>",
                "callout": {
                    "type": "vocational",
                    "title": "Workplace Health Context",
                    "text": "Community nurses use cloud storage so that clinical care plans updated at a patient's home sync immediately to the clinic database for doctors to review."
                }
            }
        ],
        "exam_model": {
            "scenario": "A support worker needs to access their training notes from both their office PC and their tablet at home. Give one reason why saving the notes to cloud storage is better than saving them to the office PC's local hard drive.",
            "steps": [
                {
                    "action": "State advantage of cloud storage",
                    "solution": "Cloud storage allows the worker to access the notes from any device connected to the internet, including their home tablet.",
                    "mark": "[B1]",
                    "rationale": "Identifies universal multi-device access as the key benefit over a single local hard drive."
                }
            ],
            "tutor_rule": "Whenever an exam question mentions accessing files from multiple locations or different devices, 'Cloud Storage' (OneDrive/Google Drive) is the model answer."
        },
        "drills": [
            {
                "question": "Which of the following is an example of CLOUD storage?",
                "options": [
                    {"text": "A USB Flash Drive", "correct": False},
                    {"text": "Microsoft OneDrive", "correct": True},
                    {"text": "The computer's internal C: drive", "correct": False},
                    {"text": "An external CD-ROM disc", "correct": False}
                ],
                "explanation": "Microsoft OneDrive, Google Drive, and iCloud store files on secure remote servers accessible via the internet."
            },
            {
                "question": "What is the fastest way to find a file on your computer when you don't know which folder it is in?",
                "options": [
                    {"text": "Open every single folder one by one", "correct": False},
                    {"text": "Type a keyword into the File Explorer search bar", "correct": True},
                    {"text": "Turn the computer off and on again", "correct": False},
                    {"text": "Delete the Recycle Bin", "correct": False}
                ],
                "explanation": "Typing a keyword or filename into the File Explorer search bar searches all subfolders automatically."
            },
            {
                "question": "What is required to access files that are stored in the cloud?",
                "options": [
                    {"text": "An active internet connection", "correct": True},
                    {"text": "A colour laser printer", "correct": False},
                    {"text": "A USB cable plugged into your wall", "correct": False},
                    {"text": "A DVD drive", "correct": False}
                ],
                "explanation": "Accessing files stored on cloud servers requires an active internet connection (Wi-Fi, ethernet, or mobile data)."
            }
        ],
        "practice": {
            "task": "A company is deciding whether to keep storing all client files on USB memory sticks or switch to cloud storage. Give two benefits of using cloud storage instead of USB memory sticks.",
            "scaffold_starter": "Benefit 1 (Security/Loss): \nBenefit 2 (Access): ",
            "model_answer": "Benefit 1: USB sticks can easily be lost, stolen, or damaged, whereas cloud storage provides safe automatic backups.\nBenefit 2: Cloud storage lets authorised staff access files from any computer or location without having to carry physical USB drives.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Mentioning prevention of physical loss / automatic backup protection."},
                {"tag": "[1 Mark]", "desc": "Mentioning accessibility from any location or device with internet."}
            ]
        },
        "revision_links": [
            {"label": "Organising Files & Folders", "href": "e3-organising-files-folders.html"},
            {"label": "Connecting Wi-Fi", "href": "e3-connecting-wifi-bluetooth.html"},
            {"label": "Online Passwords & Scams", "href": "e3-passwords-privacy-scams.html"}
        ]
    }
]

from dfs_data_entry3_skill2_3 import ENTRY_3_SKILL_2_3
from dfs_data_entry3_skill4_5 import ENTRY_3_SKILL_4_5

ALL_ENTRY_3_TOPICS = ENTRY_3_TOPICS + ENTRY_3_SKILL_2_3 + ENTRY_3_SKILL_4_5

