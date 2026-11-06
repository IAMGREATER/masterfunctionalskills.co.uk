# -*- coding: utf-8 -*-
"""
Master Functional Skills (MFS) - Entry 3 Digital Skills (Skill Areas 4 & 5)
Author: Abdul (MFS Pedagogical Systems)
"""

ENTRY_3_SKILL_4_5 = [
    # -------------------------------------------------------------------------
    # Skill Area 4: Transacting
    # -------------------------------------------------------------------------
    {
        "slug": "e3-online-forms-account-setup",
        "code": "E3.4.1",
        "skill_area": "4. Transacting",
        "title": "Filling Online Forms and Account Registration",
        "time": "15 Mins",
        "lead": "Master navigating and completing online forms accurately: identify required fields (asterisks), text boxes, drop-down menus, radio buttons, checkboxes, and fixing input validation errors.",
        "objectives": [
            "Identify mandatory fields marked with an asterisk (*)",
            "Differentiate between radio buttons (single choice) and checkboxes (multiple choice)",
            "Select items from drop-down menus and resolve form validation errors"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Online Forms & Account Creation",
        "steps": [
            {
                "title": "Understanding Online Form Elements",
                "body": "<p>Online forms are used to register for training, apply for jobs, and book medical appointments. Common form controls include:</p><ul><li><strong>Text Box:</strong> Single line for typing names, phone numbers, or postcodes.</li><li><strong>Drop-down Menu:</strong> Click the arrow to choose one option from a hidden list (e.g. Month of Birth, Country).</li><li><strong>Radio Buttons (Circular):</strong> Used when you must pick <strong>ONLY ONE</strong> option (e.g. Yes / No, Gender). Selecting a new radio button deselects the previous one.</li><li><strong>Checkboxes (Square):</strong> Used when you can select <strong>MORE THAN ONE</strong> option (e.g. choosing interests or agreeing to terms).</li></ul>",
                "ui_sim": {
                    "title": "Online Registration Form Elements",
                    "content": "<div style='background:#f8fafc; border:1px solid #cbd5e1; padding:12px; border-radius:4px; font-size:0.88rem;'><div style='margin-bottom:8px;'><label>Full Name <span style='color:#dc2626;'>*</span></label><br><input type='text' value='Sarah Jenkins' style='width:90%; padding:4px 8px; border:1px solid #94a3b8; border-radius:4px;'></div><div style='margin-bottom:8px;'><label>Preferred Contact Method (Select One):</label><br><label><input type='radio' name='c' checked> Email</label> &nbsp; <label><input type='radio' name='c'> Phone</label></div><div><label><input type='checkbox' checked> I agree to the terms and conditions <span style='color:#dc2626;'>*</span></label></div></div>"
                }
            },
            {
                "title": "Mandatory Fields and Asterisks (*)",
                "body": "<p>When completing an online form, look for a red asterisk (<strong>*</strong>) or the word <strong>(Required)</strong> next to a question. This means the field is <strong>mandatory</strong>. If you leave it blank, the form will not submit!</p>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Form Rule",
                    "text": "Before clicking 'Submit', scan the whole page for asterisks. If a field has an asterisk, you cannot skip it."
                }
            },
            {
                "title": "Resolving Validation Errors",
                "body": "<p>If you click <strong>Submit</strong> and the page jumps back with a red warning message (e.g. <em>'Invalid email format'</em> or <em>'Postcode must be entered'</em>), do not panic:</p><ol><li>Look for the boxes highlighted in red.</li><li>Read the error message carefully (for example, you might have forgotten the <code>@</code> in your email address).</li><li>Correct the error and click Submit again.</li></ol>"
            }
        ],
        "exam_model": {
            "scenario": "A learner is registering on an online portal. They type their name and address, leave the 'Email Address*' box blank, and click Submit. The form does not submit and shows a red warning. Explain why this happened and how to fix it.",
            "steps": [
                {
                    "action": "Explain the cause of error",
                    "solution": "The email box has an asterisk (*), which means it is a required / mandatory field.",
                    "mark": "[B1]",
                    "rationale": "Identifies the asterisk as a symbol for mandatory data entry."
                },
                {
                    "action": "State the remedy",
                    "solution": "Type a valid email address into the box and click Submit again.",
                    "mark": "[B1]",
                    "rationale": "Provides the correct remedial action to complete the form."
                }
            ],
            "tutor_rule": "In Entry 3 exams, questions frequently show a screenshot of a form with a red error banner. Always identify the box with the asterisk or missing information."
        },
        "drills": [
            {
                "question": "What does a red asterisk (*) next to a form question indicate?",
                "options": [
                    {"text": "The field is mandatory and must be filled in to submit", "correct": True},
                    {"text": "The field is optional and can be skipped", "correct": False},
                    {"text": "The question contains a secret password", "correct": False},
                    {"text": "The question is only for administrators", "correct": False}
                ],
                "explanation": "An asterisk (*) marks a required/mandatory question that cannot be left blank."
            },
            {
                "question": "Which form control should be used when the user must choose ONLY ONE option from a list of three?",
                "options": [
                    {"text": "Radio buttons (circular)", "correct": True},
                    {"text": "Checkboxes (square)", "correct": False},
                    {"text": "A multi-line text box", "correct": False},
                    {"text": "A file upload button", "correct": False}
                ],
                "explanation": "Radio buttons enforce single-choice selection, whereas checkboxes allow selecting multiple options."
            },
            {
                "question": "What should you do if an online form displays a red warning: 'Please enter a valid telephone number'?",
                "options": [
                    {"text": "Check the phone number for typos or missing digits, fix it, and click submit again", "correct": True},
                    {"text": "Turn off your computer monitor", "correct": False},
                    {"text": "Delete your email account", "correct": False},
                    {"text": "Ignore the message and close the window", "correct": False}
                ],
                "explanation": "Validation errors tell you what needs correcting so the system can accept the data."
            }
        ],
        "practice": {
            "task": "Look at the registration form requirements below:<br>- First Name*<br>- Surname*<br>- Date of Birth*<br>- Dietary Requirements (Optional)<br>- Tick box: Agree to Terms*<br><br>State which fields MUST be completed before the form can be submitted successfully.",
            "scaffold_starter": "Required fields: \nOptional field: ",
            "model_answer": "Required fields: First Name, Surname, Date of Birth, and the 'Agree to Terms' checkbox (all marked with an asterisk).\nOptional field: Dietary Requirements.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Listing all four fields marked with an asterisk (*)."},
                {"tag": "[1 Mark]", "desc": "Recognising that Dietary Requirements is optional and can be left blank."}
            ]
        },
        "revision_links": [
            {"label": "Online Shopping & Booking", "href": "e3-online-shopping-booking.html"},
            {"label": "Strong Passwords & Privacy", "href": "e3-passwords-privacy-scams.html"},
            {"label": "Composing Emails", "href": "e3-email-compose-reply-forward.html"}
        ]
    },
    {
        "slug": "e3-online-shopping-booking",
        "code": "E3.4.2",
        "skill_area": "4. Transacting",
        "title": "Searching, Buying and Booking Services Online",
        "time": "15 Mins",
        "lead": "Learn how to search for products and services online, apply filters, manage a digital shopping basket, and verify secure payment pages using the padlock icon and HTTPS.",
        "objectives": [
            "Use search filters (price, size, rating) to find specific items or services online",
            "Add items to a shopping basket and review order totals before purchasing",
            "Identify the secure padlock icon and https:// in the browser address bar before paying"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Searching & Buying Safely Online",
        "steps": [
            {
                "title": "Searching and Filtering Online",
                "body": "<p>When booking a ticket or shopping on an e-commerce website:</p><ol><li>Type what you need into the <strong>Search Bar</strong> (e.g. <em>'First Aid Kit Wall Mounted'</em>).</li><li>Use <strong>Filters</strong> on the side menu to narrow down your choices: filter by <strong>Price (Low to High)</strong>, <strong>Customer Rating</strong>, or <strong>Delivery Date</strong>.</li><li>Click on an item to read the detailed description, specifications, and customer reviews.</li></ol>",
                "shortcuts": [
                    {"label": "Focus Browser Search", "key": "Ctrl + E"},
                    {"label": "Reload Webpage", "key": "F5"}
                ]
            },
            {
                "title": "Managing the Shopping Basket and Checkout",
                "body": "<p>When you decide to purchase:</p><ul><li>Click <strong>Add to Basket / Cart</strong>. You can choose the quantity (e.g. 2).</li><li>Click the <strong>Basket icon</strong> at the top right to review your order. Check that quantities and prices are correct.</li><li>Click <strong>Proceed to Checkout</strong>.</li><li>Enter your delivery address and choose your delivery speed (Standard vs Express).</li></ul>"
            },
            {
                "title": "Verifying Secure Payment: Padlocks and HTTPS",
                "body": "<p>Before typing credit card details or making a payment, <strong>STOP and check the address bar:</strong></p><ul><li><strong>The Padlock Symbol:</strong> A closed padlock icon must appear next to the web address.</li><li><strong>HTTPS:</strong> The web address must begin with <code>https://</code> (the 'S' stands for <strong>Secure</strong>). This encrypts your financial data so hackers cannot intercept your card numbers.</li></ul>",
                "ui_sim": {
                    "title": "Browser Address Bar Security Check",
                    "content": "<div style='display:flex; align-items:center; gap:8px; background:#f1f5f9; padding:8px 12px; border-radius:20px; border:1px solid #cbd5e1; font-family:monospace; font-size:0.88rem;'><i class='fa-solid fa-lock' style='color:#10b981;'></i> <span style='color:#0f766e; font-weight:700;'>https://</span><span style='color:#0f172a;'>secure.medicalsupplies.co.uk/checkout</span></div>"
                },
                "callout": {
                    "type": "warning",
                    "title": "Never Pay on HTTP!",
                    "text": "If a website only shows <code>http://</code> (without the S) or displays 'Not Secure' with an open red lock, <strong>never enter your card details</strong>!"
                }
            }
        ],
        "exam_model": {
            "scenario": "A worker is booking train tickets online for an official training seminar. Before typing their debit card number on the payment page, what two security indicators must they look for in the browser to ensure the page is safe?",
            "steps": [
                {
                    "action": "Identify first security indicator",
                    "solution": "A closed Padlock icon next to the web address",
                    "mark": "[B1]",
                    "rationale": "Confirms an active SSL/TLS encrypted connection."
                },
                {
                    "action": "Identify second security indicator",
                    "solution": "The address starts with 'https://' (with the letter 's')",
                    "mark": "[B1]",
                    "rationale": "Indicates Hypertext Transfer Protocol Secure."
                }
            ],
            "tutor_rule": "In Entry 3 exams, the two answers for payment security are ALWAYS: 1. Padlock symbol; 2. 'https://'."
        },
        "drills": [
            {
                "question": "What does the 's' in 'https://' stand for in a website address?",
                "options": [
                    {"text": "Secure", "correct": True},
                    {"text": "Standard", "correct": False},
                    {"text": "Speed", "correct": False},
                    {"text": "Software", "correct": False}
                ],
                "explanation": "The 's' stands for Secure, meaning the connection between your computer and the server is encrypted."
            },
            {
                "question": "What should you check in your online shopping basket BEFORE clicking 'Pay Now'?",
                "options": [
                    {"text": "Check that the item quantities, delivery address, and total price are correct", "correct": True},
                    {"text": "Check that your printer is turned on", "correct": False},
                    {"text": "Delete your browser history", "correct": False},
                    {"text": "Change your desktop background image", "correct": False}
                ],
                "explanation": "Reviewing basket contents prevents accidentally ordering wrong quantities or paying incorrect totals."
            },
            {
                "question": "What tool on a shopping website allows you to view only items under £20?",
                "options": [
                    {"text": "Price Filter (or Sort by Price)", "correct": True},
                    {"text": "Spell Check", "correct": False},
                    {"text": "High Contrast Mode", "correct": False},
                    {"text": "Zoom Slider", "correct": False}
                ],
                "explanation": "Filters allow shoppers to narrow search results by price, brand, rating, or delivery time."
            }
        ],
        "practice": {
            "task": "You are purchasing stationery for your office on a supplier website. Explain the four stages of making this transaction from finding the items to finalising the order.",
            "scaffold_starter": "1. Search: \n2. Basket: \n3. Security Check: \n4. Payment: ",
            "model_answer": "1. Search for the stationery using the search bar and filters.\n2. Add the items to the shopping basket and review the quantities and total cost.\n3. Verify that the payment page has a closed padlock and 'https://' in the address bar.\n4. Enter the delivery address and payment details securely, then confirm the order.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Searching, adding to basket, and reviewing quantities/prices."},
                {"tag": "[1 Mark]", "desc": "Verifying security (padlock/https) before entering payment details."}
            ]
        },
        "revision_links": [
            {"label": "Filling Online Forms", "href": "e3-online-forms-account-setup.html"},
            {"label": "Strong Passwords & Privacy", "href": "e3-passwords-privacy-scams.html"},
            {"label": "Connecting to Wi-Fi", "href": "e3-connecting-wifi-bluetooth.html"}
        ]
    },

    # -------------------------------------------------------------------------
    # Skill Area 5: Being Safe and Responsible Online
    # -------------------------------------------------------------------------
    {
        "slug": "e3-passwords-privacy-scams",
        "code": "E3.5.1",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "Strong Passwords, Personal Privacy and Spotting Scams",
        "time": "15 Mins",
        "lead": "Protect yourself and your workplace from online crime: create strong, unbreakable passwords, keep personal data private, and spot scam emails, phishing messages, and suspicious links.",
        "objectives": [
            "Create strong, secure passwords combining letters, numbers, and symbols",
            "Identify sensitive personal information that must never be shared publicly",
            "Recognise the warning signs of scam emails, fake texts (smishing), and phishing links"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Passwords & Phishing Scams",
        "steps": [
            {
                "title": "Creating Strong Passwords",
                "body": "<p>A weak password is like leaving your front door unlocked. Cybercriminals use automated software that guesses thousands of common passwords every second.</p><ul><li><strong>Weak Passwords (BAD):</strong> <code>123456</code>, <code>password</code>, <code>admin</code>, your pet's name, or your birthday.</li><li><strong>Strong Password Rules:</strong> At least <strong>8 to 12 characters</strong> long, containing a mixture of <strong>UPPERCASE</strong> letters, <strong>lowercase</strong> letters, <strong>numbers (0-9)</strong>, and <strong>symbols (!@#$%)</strong>.</li><li><strong>Passphrase Method:</strong> Combine three or four random words: <code>Purple!Tiger#Jumps9</code>. Easy for you to remember, impossible for hackers to guess!</li></ul>",
                "callout": {
                    "type": "warning",
                    "title": "Golden Rule of Passwords",
                    "text": "<strong>Never share your password with anyone!</strong> IT support, banks, and managers will NEVER ask you for your password."
                }
            },
            {
                "title": "Protecting Personal Data (Privacy)",
                "body": "<p><strong>Personal Data</strong> is any information that identifies you or someone else. Never post the following on public social media or unverified websites:</p><ul><li>Your full date of birth, home address, or national insurance number.</li><li>Bank account numbers, PINs, or credit card security codes (CVV).</li><li>Workplace photos showing patient ID badges, hospital files, or computer screens.</li></ul>"
            },
            {
                "title": "Spotting Phishing and Scam Emails",
                "body": "<p><strong>Phishing</strong> is a trick used by criminals who pretend to be a trustworthy organisation (like HMRC, Royal Mail, your bank, or IT department) to steal your login details.</p><p>Look out for these <strong>four telltale warning signs:</strong></p><ol><li><strong>Sense of Extreme Urgency:</strong> <em>'Your account will be suspended in 24 hours unless you click here immediately!'</em></li><li><strong>Generic Greeting:</strong> <em>'Dear Customer'</em> or <em>'Dear User'</em> instead of your real name.</li><li><strong>Suspicious Sender Address:</strong> The display name says 'Royal Mail', but the actual address is <code>delivery@random-scam-xyz123.com</code>.</li><li><strong>Fake Web Links:</strong> Hover your mouse over the link without clicking — look where it really points!</li></ol>",
                "ui_sim": {
                    "title": "Phishing Email Warning Breakdown",
                    "content": "<div style='background:#fef2f2; border:1px solid #f87171; padding:12px; border-radius:4px; font-size:0.88rem;'><div style='color:#991b1b; font-weight:700; margin-bottom:4px;'><i class='fa-solid fa-triangle-exclamation'></i> Suspicious Message Alert</div><div><strong>From:</strong> UK Tax Office &lt;refund@service-gov-tax-update88.net&gt;<br><strong>Subject:</strong> URGENT: You have an unclaimed tax refund of £485.20!<br><br>Dear Citizen,<br>Click the link below to enter your debit card and claim immediately:<br><a href='#' style='color:#dc2626; font-weight:700;'>http://claim-tax-now-update.info/login</a></div></div>"
                }
            }
        ],
        "exam_model": {
            "scenario": "A clinic worker receives an unexpected email stating: 'Your clinic email password will expire today! Click this link to confirm your password or your account will be deleted.' State two reasons why the worker should suspect this is a phishing scam.",
            "steps": [
                {
                    "action": "Identify first warning sign",
                    "solution": "It creates a false sense of urgency/panic (threatens account deletion today).",
                    "mark": "[B1]",
                    "rationale": "Urgent threatening language is a classic social engineering tactic."
                },
                {
                    "action": "Identify second warning sign",
                    "solution": "It asks the user to click a link to reveal/enter their password.",
                    "mark": "[B1]",
                    "rationale": "Legitimate IT services never send links requesting current passwords."
                }
            ],
            "tutor_rule": "In Entry 3 exams, if an email asks for your password or card details via a link, it is ALWAYS a phishing scam. Never click the link!"
        },
        "drills": [
            {
                "question": "Which of the following passwords is the STRONGEST?",
                "options": [
                    {"text": "BlueSky!2026#", "correct": True},
                    {"text": "12345678", "correct": False},
                    {"text": "password", "correct": False},
                    {"text": "subi", "correct": False}
                ],
                "explanation": "'BlueSky!2026#' is long and contains uppercase letters, lowercase letters, numbers, and symbols."
            },
            {
                "question": "What is 'Phishing'?",
                "options": [
                    {"text": "A scam email or text that tricks you into revealing private passwords or bank details", "correct": True},
                    {"text": "A computer game about catching fish", "correct": False},
                    {"text": "A program used to print photographs", "correct": False},
                    {"text": "A way of cleaning your computer keyboard", "correct": False}
                ],
                "explanation": "Phishing is fraudulent communication designed to deceive victims into giving away sensitive information."
            },
            {
                "question": "What should you do if your bank sends an email asking you to click a link and type your 4-digit card PIN?",
                "options": [
                    {"text": "Do not click the link and delete the email; banks never ask for your PIN by email", "correct": True},
                    {"text": "Click the link and type your PIN immediately", "correct": False},
                    {"text": "Forward the email to your friends", "correct": False},
                    {"text": "Print the email and post it to the bank", "correct": False}
                ],
                "explanation": "Real banks will NEVER ask for your full password or PIN via email or text message."
            }
        ],
        "practice": {
            "task": "You receive a text message on your phone saying: 'Royal Mail: Your parcel has an unpaid fee of £1.45. Pay now at www.royalmail-fee-pay.xyz or your parcel will be returned.'<br><br>State two reasons why this is a scam, and describe what action you should take.",
            "scaffold_starter": "Reason 1: \nReason 2: \nAction to take: ",
            "model_answer": "Reason 1: The web link is suspicious and fake (ends in .xyz rather than official royalmail.com).\nReason 2: It uses urgent language demanding money for a parcel you may not even have ordered.\nAction: Do not click the link, do not enter any card details, report and delete the message.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Identifying fake website address / urgent demand for money."},
                {"tag": "[1 Mark]", "desc": "Stating not to click the link and deleting/reporting the message."}
            ]
        },
        "revision_links": [
            {"label": "Digital Wellbeing & Posture", "href": "e3-digital-wellbeing-posture.html"},
            {"label": "Online Shopping & Security", "href": "e3-online-shopping-booking.html"},
            {"label": "Email Attachments Safely", "href": "e3-email-attachments-contacts.html"}
        ]
    },
    {
        "slug": "e3-digital-wellbeing-posture",
        "code": "E3.5.2",
        "skill_area": "5. Being Safe and Responsible Online",
        "title": "Digital Wellbeing, Screen Breaks and Online Footprints",
        "time": "15 Mins",
        "lead": "Protect your physical health and mental wellbeing while working on digital devices: apply healthy workstation ergonomics, take regular screen breaks, and understand your permanent digital footprint.",
        "objectives": [
            "Apply healthy posture and ergonomic workstation guidelines to avoid eye and back strain",
            "Use the 20-20-20 rule and take regular breaks from display screens",
            "Understand that content shared online creates a lasting digital footprint"
        ],
        "youtube_id": "https://www.youtube.com/@MasterFunctionalSkills",
        "youtube_title": "Entry 3 Digital Skills - Ergonomics & Digital Wellbeing",
        "steps": [
            {
                "title": "Healthy Posture and Ergonomics",
                "body": "<p>Sitting at a computer for hours can cause neck pain, backache, and repetitive strain injury (RSI) unless you set up your workstation correctly:</p><ul><li><strong>Screen Position:</strong> The top of your monitor should be at <strong>eye level</strong>, roughly an arm's length (50-70 cm) away from your face.</li><li><strong>Chair &amp; Back:</strong> Adjust chair height so your feet rest flat on the floor with your knees at a 90-degree angle. Your lower back should be fully supported.</li><li><strong>Wrists &amp; Hands:</strong> Keep your wrists straight when typing, not bent up or resting on sharp desk edges.</li></ul>",
                "ui_sim": {
                    "title": "Ideal Ergonomic Workstation Layout",
                    "content": "<div style='display:grid; grid-template-columns:1fr 1fr; gap:12px; background:#f8fafc; padding:10px; border-radius:4px; font-size:0.85rem;'><div style='border-left:3px solid #10b981; padding-left:8px;'><strong style='color:#065f46;'>Eyes &amp; Screen</strong><br>&bull; Top of monitor at eye level<br>&bull; Arm's length away<br>&bull; Avoid window glare</div><div style='border-left:3px solid #0284c7; padding-left:8px;'><strong style='color:#0369a1;'>Posture &amp; Arms</strong><br>&bull; Back upright &amp; supported<br>&bull; Elbows at 90 degrees<br>&bull; Feet flat on floor</div></div>"
                }
            },
            {
                "title": "The 20-20-20 Rule for Eye Strain",
                "body": "<p>Staring at brightly lit screens causes eye fatigue, headaches, and dry eyes. Prevent this using the <strong>20-20-20 rule:</strong></p><blockquote><strong>Every 20 minutes, look away from your screen at an object 20 feet away for at least 20 seconds.</strong></blockquote><p>Also, stand up, stretch your legs, and walk around every 45 to 60 minutes.</p>",
                "callout": {
                    "type": "tutor",
                    "title": "Tutor Abdul's Health Tip",
                    "text": "Regular screen breaks make you more productive and alert. In exams, questions will ask how to prevent eye strain: 'Take regular screen breaks' is always an accredited answer."
                }
            },
            {
                "title": "Understanding Your Digital Footprint",
                "body": "<p>Your <strong>Digital Footprint</strong> is the trail of data you leave behind whenever you use the internet — including social media posts, comments, photos, search history, and website visits.</p><ul><li><strong>Permanent Nature:</strong> Even if you delete a photo or angry comment, others may have saved a screenshot.</li><li><strong>Workplace Impact:</strong> Employers frequently check candidates' public online presence before hiring. Always keep public profiles polite, respectful, and professional.</li></ul>"
            }
        ],
        "exam_model": {
            "scenario": "A medical records administrator spends seven hours a day typing on a computer. By mid-afternoon, they suffer from headaches and lower back pain. State two adjustments they can make to their workstation or daily routine to relieve these symptoms.",
            "steps": [
                {
                    "action": "First health recommendation",
                    "solution": "Take regular screen breaks (e.g. following the 20-20-20 rule or standing up every hour).",
                    "mark": "[B1]",
                    "rationale": "Screen breaks relieve eye muscle tension and prevent digital fatigue."
                },
                {
                    "action": "Second ergonomic recommendation",
                    "solution": "Adjust chair height and back support so feet are flat on the floor and screen is at eye level.",
                    "mark": "[B1]",
                    "rationale": "Correct ergonomic setup aligns the spine and reduces lower back strain."
                }
            ],
            "tutor_rule": "In Entry 3 exams, health and safety questions always reward practical, common-sense advice: screen breaks, chair adjustments, and monitor eye-level alignment."
        },
        "drills": [
            {
                "question": "What is the 20-20-20 rule designed to prevent when using digital devices?",
                "options": [
                    {"text": "Eye strain and headaches", "correct": True},
                    {"text": "Low battery power", "correct": False},
                    {"text": "Computer viruses", "correct": False},
                    {"text": "Slow internet speeds", "correct": False}
                ],
                "explanation": "Looking at an object 20 feet away for 20 seconds every 20 minutes relaxes eye muscles."
            },
            {
                "question": "Where should the top of your computer monitor be positioned relative to your head?",
                "options": [
                    {"text": "At eye level roughly an arm's length away", "correct": True},
                    {"text": "Down on the floor near your feet", "correct": False},
                    {"text": "Way above your head so you have to look up", "correct": False},
                    {"text": "Directly touching your nose", "correct": False}
                ],
                "explanation": "Positioning the top of the monitor at eye level prevents neck hyperextension and strain."
            },
            {
                "question": "What is meant by your 'Digital Footprint'?",
                "options": [
                    {"text": "The permanent trail of information, posts, and records left behind when you use the internet", "correct": True},
                    {"text": "The size of your computer mouse", "correct": False},
                    {"text": "How heavy your laptop is", "correct": False},
                    {"text": "The amount of electricity your printer uses", "correct": False}
                ],
                "explanation": "Your digital footprint is the traceable history of your online actions, posts, and browsing data."
            }
        ],
        "practice": {
            "task": "A young apprentice is starting their first office job. Explain what advice you would give them regarding their online digital footprint and how they should conduct themselves on social media.",
            "scaffold_starter": "Advice 1 (Privacy/Posting): \nAdvice 2 (Workplace Reputation): ",
            "model_answer": "Advice 1: Be careful what you post publicly; never post confidential work details, inappropriate photos, or offensive comments, as digital content can be permanent.\nAdvice 2: Check your privacy settings so personal posts are visible only to trusted friends and family, and maintain a professional online image.",
            "marking_scheme": [
                {"tag": "[1 Mark]", "desc": "Understanding that online posts are permanent and should remain professional."},
                {"tag": "[1 Mark]", "desc": "Managing privacy settings and never sharing confidential work information."}
            ]
        },
        "revision_links": [
            {"label": "Strong Passwords & Privacy", "href": "e3-passwords-privacy-scams.html"},
            {"label": "Display & Accessibility", "href": "e3-accessibility-display-settings.html"},
            {"label": "Hardware & Devices", "href": "e3-hardware-software-devices.html"}
        ]
    }
]
