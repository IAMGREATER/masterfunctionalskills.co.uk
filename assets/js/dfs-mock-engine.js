/**
 * Master Functional Skills - Digital Functional Skills Mock Exam Engine
 * Supports 4 Pearson Sets: Level 1 SAM, Level 1 Practice Set 2, Level 1 Practice Set 1, Entry 3 SAM
 */

const DFS_MOCK_DATA = {
  set1: {
    id: "set1",
    level: "Level 1",
    name: "Mock 1: Fresh Bite Sandwich Shop (SAM)",
    totalMarks: 54,
    passMark: 35,
    durationMinutes: 90,
    dataPackUrl: "assets/downloads/dfs/dfs-level-1-sam-data-files.zip",
    dataPackName: "dfs-level-1-sam-data-files.zip",
    dataFiles: ["FOOD AGENCY.docx", "SANDWICH FLYER.docx", "SANDWICH SALES.xlsx", "UTILITY.html", "SANDWICH.jpg", "ELECTRICITY READING.jpg"],
    sectionA: [
      {
        qNum: 1,
        title: "Search Results & Sponsored Content",
        stem: "When you use a search engine, where do sponsored links typically appear in the search results?",
        options: [
          { text: "At the bottom of the page only", isCorrect: false },
          { text: "At the top of the search results page", isCorrect: true },
          { text: "In an email sent to your inbox", isCorrect: false },
          { text: "Only when you switch off your ad-blocker", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Sponsored search results (paid advertising) are placed prominently at the very top (and sometimes at the bottom) of search results, usually marked with 'Ad' or 'Sponsored'."
      },
      {
        qNum: 2,
        title: "Display Screen Health & Safety",
        stem: "Which of the following is a direct health risk of looking at a computer monitor or digital screen for long periods without taking regular breaks?",
        options: [
          { text: "Hearing impairment", isCorrect: false },
          { text: "Eyestrain and blurred vision", isCorrect: true },
          { text: "High blood pressure", isCorrect: false },
          { text: "Repetitive typing error", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Working on display screens without adequate breaks causes eyestrain, fatigue, headaches, and dry eyes. The 20-20-20 rule helps prevent screen eyestrain."
      },
      {
        qNum: 3,
        title: "Browser Privacy & History",
        stem: "A student is using a shared computer in an internet café or college library. What is the most effective way to prevent the web browser from saving their browsing history and cookies during that session?",
        options: [
          { text: "Turn off the monitor when leaving", isCorrect: false },
          { text: "Use private browsing (Incognito / InPrivate mode)", isCorrect: true },
          { text: "Zoom in to 150%", isCorrect: false },
          { text: "Bookmark every page visited", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Private browsing (or Incognito mode) ensures that your browser history, temporary site data, form inputs, and cookies are automatically wiped when the window is closed."
      },
      {
        qNum: 4,
        title: "Secure Web Connections",
        stem: "Which two visual indicators in the web browser address bar demonstrate that a website uses an encrypted (SSL/TLS) secure connection for safe data transmission?",
        options: [
          { text: "A blue link and www.", isCorrect: false },
          { text: "A padlock symbol and https:// prefix", isCorrect: true },
          { text: "A magnifying glass and .co.uk", isCorrect: false },
          { text: "A star favourite icon and .org", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The padlock icon alongside the 'https://' protocol indicates that the communication channel between your web browser and the server is encrypted."
      },
      {
        qNum: 5,
        title: "Data Protection & GDPR Rights",
        stem: "Under the UK General Data Protection Regulation (UK GDPR) / Data Protection Act 2018, which of the following is a legal right granted to individuals regarding their personal data?",
        options: [
          { text: "The right to demand free unlimited commercial products", isCorrect: false },
          { text: "The right to have personal data deleted when it is no longer necessary (Right to Erasure)", isCorrect: true },
          { text: "The right to sell company passwords to third parties", isCorrect: false },
          { text: "The right to access colleagues' private medical files", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Under UK GDPR, individuals possess the Right to Erasure ('the right to be forgotten'), allowing them to request deletion of personal data when it is no longer required for its original purpose."
      },
      {
        qNum: 6,
        title: "Cybersecurity & Malware Protection",
        stem: "What is the primary action a business or individual should take to protect their computer system against viruses, worms, and malicious software?",
        options: [
          { text: "Install and regularly update anti-virus software", isCorrect: true },
          { text: "Defragment the hard drive every morning", isCorrect: false },
          { text: "Delete all saved Word documents", isCorrect: false },
          { text: "Unplug the mouse and keyboard when not in use", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Anti-virus software scans files in real-time, isolates malware, and protects digital systems from trojans, spyware, and ransomware."
      },
      {
        qNum: 7,
        title: "File Compression Benefits",
        stem: "Why do organisations compress files into a ZIP folder before emailing or transferring them across the internet?",
        options: [
          { text: "It permanently removes all text from the file", isCorrect: false },
          { text: "It reduces file size and data transfer time", isCorrect: true },
          { text: "It changes all images to black and white", isCorrect: false },
          { text: "It translates the document into French", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Compression algorithms reduce the number of bytes required to store files, which saves storage space and significantly speeds up uploading and downloading over network connections."
      },
      {
        qNum: 8,
        title: "File Sizes & Storage Units",
        stem: "A flash drive has 5,000 KB of free storage space remaining. Which of the following files will comfortably fit into this available space?",
        options: [
          { text: "A 50,000 bytes file", isCorrect: true },
          { text: "A 50 MB high-definition video", isCorrect: false },
          { text: "A 5 GB operating system image", isCorrect: false },
          { text: "A 10,000 KB audio recording", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: 1 Kilobyte (KB) = 1,000 bytes (or 1,024 bytes). Therefore 50,000 bytes is approximately 50 KB, which is much smaller than 5,000 KB and easily fits."
      },
      {
        qNum: 9,
        title: "Search Wildcards & Operators",
        stem: "Which wildcard character is commonly used in file searches and database queries to represent a single unknown character (e.g. searching 'w?ll' to match 'will', 'wall', or 'well')?",
        options: [
          { text: "? (Question mark)", isCorrect: true },
          { text: "* (Asterisk)", isCorrect: false },
          { text: "# (Hash)", isCorrect: false },
          { text: "% (Percent)", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The question mark (?) represents exactly ONE single character, whereas an asterisk (*) represents any number of zero or more characters."
      },
      {
        qNum: 10,
        title: "Safe Communication of Sensitive Data",
        stem: "You need to send confidential employee payroll information to an external accountant via email. What is the safest and most secure procedure?",
        options: [
          { text: "Type the account numbers directly in the public subject line", isCorrect: false },
          { text: "Put the data into a password-protected encrypted attachment and send the password via a separate secure channel", isCorrect: true },
          { text: "Post a screenshot of the details on public social media", isCorrect: false },
          { text: "Send the email with all company staff in the Cc field", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Sensitive or confidential files must be encrypted or password-protected when sent by email, and the password must never be included in the same email message."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "Information Search & Professional Email Communication",
        marks: 7,
        brief: "Sam wants you to locate the official London postal address for the Food Standards Agency (FSA) and email the address to him.",
        instructions: [
          "Use a search engine to find the London postal address of the Food Standards Agency (FSA). Take a screenshot of your search terms.",
          "Compose an email to <code>sam@pearson.com</code> with the subject <code>Food Standards Agency address</code>.",
          "Include a polite greeting (e.g. 'Hello Sam,'), state the full postal address: <strong>(Floors 6 and 7) Clive House, 70 Petty France, London, SW1H 9EX</strong>.",
          "Add a professional automated email signature containing 'Kind regards' and your candidate name."
        ],
        type: "search_email",
        searchAnswer: "Food Standards Agency London postal address",
        searchResultSnippet: "Food Standards Agency (FSA) Headquarters: Floors 6 and 7, Clive House, 70 Petty France, London, SW1H 9EX.",
        rubric: [
          { code: "A1", desc: "Search engine query shows appropriate keywords (e.g. 'Food Standards Agency London address')", mark: 1 },
          { code: "A1b", desc: "Correct postal address identified: Clive House, 70 Petty France, London, SW1H 9EX", mark: 1 },
          { code: "A2", desc: "Automated email signature created with 'Kind regards' and candidate name", mark: 1 },
          { code: "A3a", desc: "Recipient email entered accurately: sam@pearson.com", mark: 1 },
          { code: "A3b", desc: "Subject line appropriate (e.g. 'Food Standards Agency address' / 'FSA address')", mark: 1 },
          { code: "A3c", desc: "Professional greeting (e.g. 'Dear Sam') and suitable closing sign-off", mark: 1 },
          { code: "A3d", desc: "Accurate address included in the email message body", mark: 1 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Creating & Editing a Promotional Flyer",
        marks: 11,
        brief: "Fresh Bite Sandwich Shop wants a landscape flyer created using SANDWICH FLYER.docx to advertise special lunch offers.",
        instructions: [
          "Open <code>SANDWICH FLYER.docx</code> from your data folder. Change page orientation to <strong>Landscape</strong>.",
          "Insert the list of special offers below the heading 'Special offers this month' formatted as a clean table with appropriate column widths.",
          "Insert <code>SANDWICH.jpg</code> to the right of the table.",
          "Crop the image to eliminate excess empty space on both sides, resize to <strong>5 cm height</strong> maintaining aspect ratio, and adjust image contrast to 30%.",
          "Highlight heading text, change font colour, and add a decorative page border. Ensure balanced layout with no overlapping elements."
        ],
        type: "document_design",
        rubric: [
          { code: "B1", desc: "Page orientation set to Landscape", mark: 1 },
          { code: "B2a", desc: "Special offers inserted adjacent to or below 'Special offers this month'", mark: 1 },
          { code: "B2b", desc: "Offers formatted cleanly inside a table with adjusted column widths", mark: 1 },
          { code: "B3a", desc: "SANDWICH.jpg image inserted into document", mark: 1 },
          { code: "B3b", desc: "Image positioned to the right-hand side of the sandwich list", mark: 1 },
          { code: "B4", desc: "Sandwich image cropped to remove empty white space on both sides", mark: 1 },
          { code: "B5", desc: "Image resized to 5 cm height maintaining proportions", mark: 1 },
          { code: "B6", desc: "Image contrast adjusted to 30%", mark: 1 },
          { code: "B7a", desc: "Heading text highlighted with clear contrasting font colour", mark: 1 },
          { code: "B7b", desc: "Page border applied", mark: 1 },
          { code: "B7c", desc: "Document fit for purpose: fills page neatly, no text overlap, professional spacing", mark: 1 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "Spreadsheet Data Analysis & Charting",
        marks: 15,
        brief: "Sam needs sandwich sales figures calculated in SANDWICH SALES.xlsx, formatted into currency, and charted.",
        instructions: [
          "Merge and centre cells A1:H1, set font size to 24 pt, and shade cells A1:H1 light green.",
          "In cell G4, enter a formula to calculate total sold for Chicken sandwich: <code>=SUM(C4:F4)</code>.",
          "In cell H4, calculate income: <code>=G4*B4</code> (Total Sold × Price).",
          "Replicate formulas down columns G and H for all sandwich varieties.",
          "In row 12, calculate the weekly average sold: <code>=AVERAGE(C4:C11)</code> and replicate across to column F.",
          "Format all currency values in columns B and H as British Pounds (£) with 2 decimal places.",
          "Sort rows A4:F11 in ascending order of Price (lowest price £3.65 Feta Cheese first).",
          "Create a Bar or Pie Chart showing Sandwich Type vs Total Sold (A3:A11 and G3:G11), add a clear title, labels, and move the chart to a separate worksheet."
        ],
        type: "spreadsheet",
        rubric: [
          { code: "C1a", desc: "Heading 'Sandwich Sales' merged & centred across A1:H1, font size 24 pt", mark: 1 },
          { code: "C1b", desc: "Cells A1:H1 shaded with light green background", mark: 1 },
          { code: "C2a", desc: "Total sold formula entered correctly: =SUM(C4:F4)", mark: 1 },
          { code: "C2b", desc: "Income formula calculated correctly: =G4*B4", mark: 1 },
          { code: "C3", desc: "Formulas successfully replicated down columns G and H", mark: 1 },
          { code: "C4", desc: "Average formula used: =AVERAGE(C4:C11)", mark: 1 },
          { code: "C5", desc: "Average formula replicated across to C12:F12", mark: 1 },
          { code: "C6", desc: "Columns B and H formatted as currency (£) to 2 decimal places", mark: 1 },
          { code: "C7", desc: "Table sorted in ascending order of Price (Feta cheese £3.65 first)", mark: 1 },
          { code: "C8a", desc: "Chart created (Column/Bar or Pie chart)", mark: 1 },
          { code: "C8b", desc: "Correct data range used (Sandwich Type column A & Total Sold column G)", mark: 1 },
          { code: "C8c", desc: "Axis labels or legend formatted clearly with category labels", mark: 1 },
          { code: "C8d", desc: "Chart title accurate (e.g. 'Sandwich Sales')", mark: 1 },
          { code: "C8e", desc: "Data values displayed on bars or segments", mark: 1 },
          { code: "C8f", desc: "Chart placed on a separate worksheet", mark: 1 }
        ]
      },
      {
        id: "taskD",
        letter: "Task D",
        title: "Online Web Form Completion & Image Upload",
        marks: 5,
        brief: "Submit the quarterly electricity meter reading for Fresh Bite Sandwich Shop using UTILITY.html.",
        instructions: [
          "Open <code>UTILITY.html</code> in a browser.",
          "Part 1: Enter Customer Account Number: <code>R753197</code>, Premises No: <code>36</code>, Postcode: <code>NT25 3BG</code>, Contact Tel: <code>01632 960455</code>, Email: <code>sam@pearson.com</code>.",
          "Part 2: Select <strong>Electricity</strong> as fuel type and enter the reading <strong>032075</strong>.",
          "Upload the meter photo <code>ELECTRICITY READING.jpg</code>.",
          "Set marketing communication preferences to <strong>Email</strong> and <strong>Text</strong> only, then submit."
        ],
        type: "web_form",
        rubric: [
          { code: "D1", desc: "Accurate completion of customer details (Account R753197, No 36, NT25 3BG, 01632 960455, sam@pearson.com)", mark: 2 },
          { code: "D2", desc: "Electricity selected and meter reading (032075) entered accurately", mark: 1 },
          { code: "D3", desc: "ELECTRICITY READING.jpg image file uploaded", mark: 1 },
          { code: "D4", desc: "Marketing preferences selected for Email and Text only", mark: 1 }
        ]
      },
      {
        id: "taskE",
        letter: "Task E",
        title: "File Management & Technical Troubleshooting",
        marks: 6,
        brief: "Fresh Bite has installed a new wireless printer that fails to connect to the network. Organise folders and document troubleshooting steps.",
        instructions: [
          "Create a new folder called <code>Devices</code>.",
          "Inside <code>Devices</code>, create a subfolder called <code>Printer</code>.",
          "Research why a wireless printer might fail to connect (e.g., incorrect Wi-Fi password, printer offline, IP address conflict, or frequency band mismatch).",
          "Save your troubleshooting solution inside the <code>Printer</code> folder with a suitable name like <code>Wireless printer.docx</code>.",
          "Ensure your source information is recent, reliable, and uses secure protocols (HTTPS)."
        ],
        type: "file_mgmt",
        rubric: [
          { code: "E1a", desc: "New main folder created called 'Devices'", mark: 1 },
          { code: "E1b", desc: "New subfolder created called 'Printer'", mark: 1 },
          { code: "E2a", desc: "Document saved with suitable descriptive filename (e.g. 'Wireless printer')", mark: 1 },
          { code: "E2b", desc: "Troubleshooting steps directly address wireless printer connection failure", mark: 1 },
          { code: "E2c", desc: "Information is up to date (evidence of recent publication/date)", mark: 1 },
          { code: "E2d", desc: "Source is verified as reliable (uses https, reputable manufacturer/support site)", mark: 1 }
        ]
      }
    ]
  },

  set2: {
    id: "set2",
    level: "Level 1",
    name: "Mock 2: Annual Awards Ceremony & Catering (Practice Set 2)",
    totalMarks: 54,
    passMark: 35,
    durationMinutes: 90,
    dataPackUrl: "assets/downloads/dfs/dfs-level-1-practice-set-2-data-files.zip",
    dataPackName: "dfs-level-1-practice-set-2-data-files.zip",
    dataFiles: ["AWARDS.docx", "CEREMONY.html", "EXPENDITURE.xlsx", "FOOD MENU.docx", "MENU.jpg", "TROPHY.jpg"],
    sectionA: [
      {
        qNum: 1,
        title: "Online Privacy & Footprint",
        stem: "Why is it important to regularly check and restrict your social media privacy settings?",
        options: [
          { text: "It increases your internet download speed", isCorrect: false },
          { text: "It limits the digital footprint and visibility of a user's personal information", isCorrect: true },
          { text: "It automatically deletes your email inbox", isCorrect: false },
          { text: "It changes your IP address to a foreign country", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Restricting privacy settings limits your digital footprint, preventing unauthorized third parties, scammers, or future employers from harvesting private personal details."
      },
      {
        qNum: 2,
        title: "Cloud Collaboration",
        stem: "A team member needs to share several large video and graphic files with colleagues in another office so they can all work on them. What should they do first?",
        options: [
          { text: "Print the files out on photo paper", isCorrect: false },
          { text: "Upload the files to a secure cloud storage drive", isCorrect: true },
          { text: "Restart the operating system in safe mode", isCorrect: false },
          { text: "Convert the monitor brightness to 100%", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Uploading files to cloud storage allows shared access, real-time collaboration, and eliminates email attachment size limitations."
      },
      {
        qNum: 3,
        title: "Ergonomics & Posture",
        stem: "What physical symptom is most likely to occur if a worker uses a laptop or desktop monitor placed too low or tilted at an awkward angle?",
        options: [
          { text: "The user may feel neck and shoulder pain", isCorrect: true },
          { text: "Earache and loss of balance", isCorrect: false },
          { text: "Allergic reaction", isCorrect: false },
          { text: "Short-term memory loss", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: A screen placed too low forces the neck to bend forward, causing musculoskeletal strain, neck pain, and upper back discomfort."
      },
      {
        qNum: 4,
        title: "Digital Terminology: Megabytes & Gigabytes",
        stem: "What is a Megabyte (MB) or Gigabyte (GB)?",
        options: [
          { text: "A unit of data storage capacity", isCorrect: true },
          { text: "A measure of screen refresh frequency", isCorrect: false },
          { text: "An internet browsing protocol", isCorrect: false },
          { text: "A type of computer cooling fan", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Bytes, Kilobytes (KB), Megabytes (MB), and Gigabytes (GB) are standard units used to measure digital data storage capacity."
      },
      {
        qNum: 5,
        title: "Anti-Virus Real-Time Protection",
        stem: "How does real-time anti-virus software protect your computer while you are working?",
        options: [
          { text: "It scans files and downloads automatically as they are opened or saved", isCorrect: true },
          { text: "It disables your internet connection every 10 minutes", isCorrect: false },
          { text: "It retypes corrupted sentences in word processing files", isCorrect: false },
          { text: "It cleans the dust inside your computer case", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Real-time background virus scanners inspect incoming data packets, email attachments, and files the instant they are opened or executed."
      },
      {
        qNum: 6,
        title: "File Searching Efficiency",
        stem: "If you know the exact name of a missing contract saved on your computer, what is the fastest way to locate it using the file manager search bar?",
        options: [
          { text: "Search for the complete file name in quotation marks or exact search", isCorrect: true },
          { text: "Open every folder manually on your hard drive", isCorrect: false },
          { text: "Search for a single random letter like 'e'", isCorrect: false },
          { text: "Format the hard drive", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Searching for the complete, exact file name pinpoints the specific file instantly without displaying hundreds of unrelated results."
      },
      {
        qNum: 7,
        title: "Online Behaviour & Cyberbullying",
        stem: "An employee is added to an informal group chat where other members begin posting offensive and harassing comments. What is the most appropriate first step for the employee to protect their wellbeing?",
        options: [
          { text: "Leave the group chat and report the behaviour to management/moderator", isCorrect: true },
          { text: "Post offensive insults back at the other members", isCorrect: false },
          { text: "Forward the offensive comments to external clients", isCorrect: false },
          { text: "Change their computer password", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Leaving inappropriate or harassing group chats protects the individual, prevents escalation, and should be followed by reporting through official channels."
      },
      {
        qNum: 8,
        title: "GDPR: Right to Rectification",
        stem: "Under data protection legislation, what obligation does a company have if a customer informs them that their recorded home address or phone number is incorrect?",
        options: [
          { text: "They must rectify and correct the inaccurate personal data promptly", isCorrect: true },
          { text: "They must charge the customer a £500 administration fee", isCorrect: false },
          { text: "They can ignore the request until the next financial year", isCorrect: false },
          { text: "They must close the customer's account immediately", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The UK GDPR Right to Rectification legally requires data controllers to correct inaccurate or incomplete personal records without undue delay."
      },
      {
        qNum: 9,
        title: "Evaluating Website Credibility",
        stem: "Which of the following is a reliable sign that an online retail business is legitimate and trustworthy?",
        options: [
          { text: "The website displays a verifiable physical business address, phone number, and company registration", isCorrect: true },
          { text: "The website only accepts payment via gift cards or wire transfer", isCorrect: false },
          { text: "The prices are 95% cheaper than any other shop in the world", isCorrect: false },
          { text: "There are spelling mistakes on every product page", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Legitimate businesses provide authentic verifiable physical addresses, customer support telephone numbers, company registration details, and secure payment gateways."
      },
      {
        qNum: 10,
        title: "Bandwidth & Download Speed",
        stem: "Which of the following files will download fastest over a slow mobile data connection?",
        options: [
          { text: "A 100 KB text file", isCorrect: true },
          { text: "A 25 MB high-resolution image", isCorrect: false },
          { text: "A 1.5 GB movie file", isCorrect: false },
          { text: "A 400 MB software installer", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: 100 Kilobytes (KB) is tiny compared to Megabytes (MB) and Gigabytes (GB), requiring minimal bandwidth and downloading almost instantly."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "Image Research & Communication",
        marks: 8,
        brief: "Luka needs a photograph of an awards ceremony venue to use on promotional materials. Search for an image and email the link to him.",
        instructions: [
          "Use an image search engine with the exact search criteria: <code>local awards ceremony venue</code>.",
          "Select a suitable high-quality image and copy the image link address.",
          "Compose an email to <code>luka@pearson.service</code> with the subject <code>venue</code> or <code>image link</code>.",
          "Include a polite greeting (e.g. 'Dear Luka,'), paste the image link address, and sign off professionally."
        ],
        type: "search_email",
        searchAnswer: "local awards ceremony venue",
        searchResultSnippet: "Grand Ballroom & Conference Suites, London - Venue image link: https://pearson.service/assets/awards-venue.jpg",
        rubric: [
          { code: "A1a", desc: "Search engine filter set to search for an Image", mark: 1 },
          { code: "A1b", desc: "Exact phrase search criteria used: 'local awards ceremony venue'", mark: 2 },
          { code: "A1c", desc: "Valid image link address captured and copied", mark: 1 },
          { code: "A2a", desc: "Email addressed accurately to luka@pearson.service", mark: 1 },
          { code: "A2b", desc: "Clear subject line entered (e.g. 'venue' or 'image link')", mark: 1 },
          { code: "A2c", desc: "Polite greeting (Dear Luka) and professional sign-off included", mark: 1 },
          { code: "A2d", desc: "Image link address successfully pasted into email message", mark: 1 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Event Menu Formatting & Image Styling",
        marks: 10,
        brief: "Format the dinner menu for the awards celebration in FOOD MENU.docx.",
        instructions: [
          "Open <code>FOOD MENU.docx</code>. Ensure page orientation is <strong>Portrait</strong>.",
          "Format heading 'Awards Ceremony' in a distinct font colour and highlight it.",
          "Set the three course titles 'Starter', 'Main', and 'Dessert' to <strong>font size 16 and Bold</strong>.",
          "Insert <code>MENU.jpg</code> and configure text wrapping so the photo is placed at the right-hand side without overlapping text.",
          "Resize the image to <strong>18 cm height</strong> (maintaining aspect ratio) and increase color saturation to <strong>200%</strong>.",
          "Apply a page border and ensure clean, balanced white space."
        ],
        type: "document_design",
        rubric: [
          { code: "B1", desc: "Document orientation is Portrait", mark: 1 },
          { code: "B2", desc: "'Awards Ceremony' heading formatted in different font colour and highlighted", mark: 1 },
          { code: "B3", desc: "'Starter', 'Main', 'Dessert' headings formatted to font size 16 and Bold", mark: 1 },
          { code: "B4", desc: "MENU.jpg image inserted", mark: 1 },
          { code: "B5", desc: "Text wrap applied to position image on right-hand side", mark: 1 },
          { code: "B6", desc: "Image does not overlap any text", mark: 1 },
          { code: "B7", desc: "Image height set to 18 cm maintaining proportions", mark: 1 },
          { code: "B8", desc: "Picture colour saturation set to 200%", mark: 1 },
          { code: "B9", desc: "Page border applied", mark: 1 },
          { code: "B10", desc: "Final menu fit for purpose with professional layout and balanced margins", mark: 1 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "Awards Expenditure Spreadsheet & Filtering",
        marks: 15,
        brief: "Analyse four years of awards spending and build a visual budget breakdown in EXPENDITURE.xlsx.",
        instructions: [
          "In <code>EXPENDITURE.xlsx</code>, split merged cells A1:F1, set heading font size to 36 pt, and shade cells B2:E2 light green.",
          "In cell F4, calculate average spending across 2022 to 2025: <code>=AVERAGE(B4:E4)</code> and replicate down for all items (F5:F10).",
          "In cell B11, calculate total 2022 expenditure: <code>=SUM(B4:B10)</code> and replicate across to E11.",
          "Format all numbers in columns B through F as British Pounds (£) with 2 decimal places.",
          "Sort rows A4:E10 alphabetically by Item (AV Equipment first), maintaining data integrity.",
          "Apply an Excel filter to show ONLY items that do NOT contain Travel (6 items).",
          "Create a 2025 Pie Chart showing Item costs for 2025, add values to segments, and move to a new worksheet."
        ],
        type: "spreadsheet",
        rubric: [
          { code: "C1", desc: "Cells A1:F1 split and heading font size set to 36 pt", mark: 1 },
          { code: "C2", desc: "Cells B2:E2 shaded in light green", mark: 1 },
          { code: "C3", desc: "Average formula entered correctly: =AVERAGE(B4:E4)", mark: 1 },
          { code: "C4", desc: "Average formula replicated down F5:F10", mark: 1 },
          { code: "C5", desc: "Sum formula calculated: =SUM(B4:B10)", mark: 1 },
          { code: "C6", desc: "Sum replicated across columns C11:E11", mark: 1 },
          { code: "C7", desc: "All expenditure values formatted as £ with 2 decimal places", mark: 1 },
          { code: "C8", desc: "Sorted alphabetically by Item name (AV Equipment first)", mark: 1 },
          { code: "C9", desc: "Filter applied showing only items that do NOT contain 'Travel' (6 items visible)", mark: 1 },
          { code: "C10a", desc: "Pie chart created from 2025 expenditure data", mark: 1 },
          { code: "C10b", desc: "Correct data range selected (Item and 2025)", mark: 1 },
          { code: "C10c", desc: "Chart title includes costs, items, and 2025", mark: 1 },
          { code: "C10d", desc: "Item names displayed in legend or on segments", mark: 1 },
          { code: "C10e", desc: "Cost values displayed on pie segments", mark: 1 },
          { code: "C10f", desc: "Chart saved on a separate new worksheet", mark: 1 }
        ]
      },
      {
        id: "taskD",
        letter: "Task D",
        title: "Awards Registration Form & Trophy Upload",
        marks: 5,
        brief: "Register candidate Luka Joshy for the ceremony using CEREMONY.html.",
        instructions: [
          "Open <code>CEREMONY.html</code>.",
          "Screen 1: Email: <code>luka@pearson.service</code>, Name: <code>Luka Joshy</code>, Company: <code>Eclipse Force</code>, Postcode: <code>LW7 1PJ</code>, Tel: <code>01632 960741</code>.",
          "Screen 2: Select <strong>Telephone</strong> as preferred contact method.",
          "Screen 3: Category: <strong>Prize Winner 2026</strong>, Table number: <strong>24</strong>.",
          "Upload <code>TROPHY.jpg</code> as proof of award and submit."
        ],
        type: "web_form",
        rubric: [
          { code: "D1", desc: "Accurate completion of screens 1 to 3 (Luka Joshy, Eclipse Force, LW7 1PJ, 01632 960741, Prize Winner 2026, Table 24)", mark: 4 },
          { code: "D2", desc: "TROPHY.jpg image file successfully uploaded", mark: 1 }
        ]
      },
      {
        id: "taskE",
        letter: "Task E",
        title: "Tablet Troubleshooting & Folder Hierarchy",
        marks: 6,
        brief: "A tablet computer used for check-in at the ceremony cannot connect to Wi-Fi. Organise folders and record the fix.",
        instructions: [
          "Create a new folder called <code>PROBLEM</code>.",
          "Inside <code>PROBLEM</code>, create a subfolder called <code>TABLET</code>.",
          "Find instructions on how to forget and re-connect a Wi-Fi network on an Android tablet.",
          "Save the solution in the <code>TABLET</code> folder with a clear name (e.g. <code>Wi-Fi settings.docx</code>).",
          "Ensure information is up to date and from a reliable HTTPS source."
        ],
        type: "file_mgmt",
        rubric: [
          { code: "E1", desc: "Folder named 'PROBLEM' created", mark: 1 },
          { code: "E2", desc: "Subfolder named 'TABLET' created inside 'PROBLEM'", mark: 1 },
          { code: "E3", desc: "File saved with suitable name (e.g. 'Wi-Fi settings')", mark: 1 },
          { code: "E4a", desc: "Solution specifically addresses changing Wi-Fi settings on an Android tablet", mark: 1 },
          { code: "E4b", desc: "Source is up to date (recent timestamp/article)", mark: 1 },
          { code: "E4c", desc: "Source is reliable (uses HTTPS, official support domain)", mark: 1 }
        ]
      }
    ]
  },

  set3: {
    id: "set3",
    level: "Level 1",
    name: "Mock 3: First Aid Training & Supplies (Practice Set 1)",
    totalMarks: 54,
    passMark: 35,
    durationMinutes: 90,
    dataPackUrl: "assets/downloads/dfs/dfs-l1-sample-assessment-materials.zip",
    dataPackName: "dfs-level-1-practice-set-1-data-files.zip",
    dataFiles: ["FIRST AID ACTIVITY.docx", "FIRST AID KIT.xlsx", "FIRST AID PRESENTATION.pptx", "SUPPLIER.html"],
    sectionA: [
      {
        qNum: 1,
        title: "Two-Factor Authentication (2FA)",
        stem: "What is the primary security advantage of using Two-Factor Authentication (2FA) when logging into work accounts?",
        options: [
          { text: "It doubles your network bandwidth speed", isCorrect: false },
          { text: "It requires two independent pieces of evidence (e.g. password + phone code), making unauthorized access much harder", isCorrect: true },
          { text: "It lets everyone in your team share one password", isCorrect: false },
          { text: "It removes the need to have anti-virus software", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Two-Factor Authentication provides defense in depth by combining something you know (password) with something you have (SMS code or authenticator app)."
      },
      {
        qNum: 2,
        title: "Phishing Identification",
        stem: "You receive an urgent email purporting to be from your bank requesting immediate login verification via an unusual link. What is this known as?",
        options: [
          { text: "A phishing scam", isCorrect: true },
          { text: "A broadband router update", isCorrect: false },
          { text: "A database defragmentation", isCorrect: false },
          { text: "A cloud backup confirmation", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Phishing is a social engineering attack where cybercriminals impersonate reputable organisations to trick users into revealing sensitive credentials."
      },
      {
        qNum: 3,
        title: "Repetitive Strain Injury (RSI)",
        stem: "Which workplace modification can help an office worker avoid Repetitive Strain Injury (RSI) in their wrists and hands when typing?",
        options: [
          { text: "Using a supportive wrist rest and ergonomic keyboard", isCorrect: true },
          { text: "Typing twice as fast with one finger", isCorrect: false },
          { text: "Working in complete darkness", isCorrect: false },
          { text: "Disabling autocorrect", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Ergonomic wrist rests, adjustable desk seating, and neutral wrist alignment prevent muscular tension and repetitive strain injuries."
      },
      {
        qNum: 4,
        title: "Cloud Backup vs Local Storage",
        stem: "What is the key benefit of automated cloud backup over saving files only to an office desktop hard drive?",
        options: [
          { text: "Files are protected against on-site hardware failure, fire, or theft and can be restored from anywhere", isCorrect: true },
          { text: "Cloud files cannot ever be opened by anyone", isCorrect: false },
          { text: "It prevents users from using formulas in spreadsheets", isCorrect: false },
          { text: "It makes all printers print in color", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Cloud backups provide off-site redundancy, disaster recovery, and ubiquitous remote access if physical hardware fails."
      },
      {
        qNum: 5,
        title: "Strong Password Standards",
        stem: "Which of the following represents the strongest password design according to cybersecurity best practice?",
        options: [
          { text: "Password123", isCorrect: false },
          { text: "A combination of at least 12 characters including uppercase, lowercase, numbers, and symbols (or 3 random memorable words)", isCorrect: true },
          { text: "The user's first name and date of birth", isCorrect: false },
          { text: "11112222", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Long passwords combining letters, digits, and special characters resist automated dictionary and brute-force cracking attacks."
      },
      {
        qNum: 6,
        title: "File Attachment Limits",
        stem: "Most corporate email servers reject attachments exceeding 20 MB to 25 MB. How should a user transfer a 150 MB training video to an external client?",
        options: [
          { text: "Upload the video to a secure cloud drive and email a shared download link", isCorrect: true },
          { text: "Print each video frame on paper", isCorrect: false },
          { text: "Send 150 blank emails", isCorrect: false },
          { text: "Change the file extension to .txt", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Large multimedia files should be shared via cloud storage access links rather than email attachments."
      },
      {
        qNum: 7,
        title: "Data Protection Principles",
        stem: "Under data protection law, what must a company do with customer personal data when the business relationship ends and the statutory retention period expires?",
        options: [
          { text: "Securely destroy or permanently delete the personal data", isCorrect: true },
          { text: "Publish the customer names on the company website", isCorrect: false },
          { text: "Email the data to all staff as souvenirs", isCorrect: false },
          { text: "Sell the database to unauthorized third parties", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Storage limitation principles under GDPR require personal records to be kept no longer than necessary and securely deleted."
      },
      {
        qNum: 8,
        title: "Search Boolean Operators",
        stem: "Which search query would locate documents about first aid courses in Birmingham but exclude results from Manchester?",
        options: [
          { text: "\"first aid course\" Birmingham NOT Manchester", isCorrect: true },
          { text: "first aid + Manchester only", isCorrect: false },
          { text: "course ? ? ?", isCorrect: false },
          { text: "Birmingham = Manchester", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The NOT operator (or minus sign -) excludes unwanted terms from search queries."
      },
      {
        qNum: 9,
        title: "Digital Device Security: Screen Locks",
        stem: "Why should staff configure their work laptop to automatically lock the screen after 3 minutes of inactivity?",
        options: [
          { text: "To prevent unauthorized persons viewing or accessing company data when the computer is left unattended", isCorrect: true },
          { text: "To save 99% of room heating", isCorrect: false },
          { text: "To speed up mouse movement", isCorrect: false },
          { text: "To update the operating system hourly", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Automatic screen locking prevents physical shoulder surfing and unauthorized access when workstations are temporarily unattended."
      },
      {
        qNum: 10,
        title: "Acceptable Use Policies (AUP)",
        stem: "What is the primary purpose of an organisation's IT Acceptable Use Policy (AUP)?",
        options: [
          { text: "To state clear rules and guidelines on permitted and prohibited uses of company devices and networks", isCorrect: true },
          { text: "To specify which brand of coffee staff should drink", isCorrect: false },
          { text: "To eliminate all computer monitors", isCorrect: false },
          { text: "To forbid staff from sending any emails", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: An AUP outlines acceptable digital behaviour, protects network security, and clarifies legal liabilities."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "First Aid Information Research & Email",
        marks: 7,
        brief: "Find recommended workplace first aid kit contents and email the checklist to the health and safety team.",
        instructions: [
          "Use a search engine to locate official Health and Safety Executive (HSE) minimum workplace first aid kit standards.",
          "Compose an email to <code>healthsafety@pearson.biz</code> with the subject <code>First aid kit standards</code>.",
          "Include a polite greeting, list 4 essential first aid items, and add your automated signature."
        ],
        type: "search_email",
        searchAnswer: "HSE workplace first aid kit contents",
        searchResultSnippet: "HSE Guidance: Minimum contents include sterile dressings, eye pads, triangular bandages, safety pins, and disposable gloves.",
        rubric: [
          { code: "A1", desc: "Appropriate search terms used for workplace first aid standards", mark: 2 },
          { code: "A2", desc: "Recipient entered accurately: healthsafety@pearson.biz", mark: 1 },
          { code: "A3", desc: "Clear subject line, greeting, and sign-off", mark: 2 },
          { code: "A4", desc: "Four essential kit items correctly listed in email message", mark: 2 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Presentation Formatting & Visual Slides",
        marks: 11,
        brief: "Format the training slideshow FIRST AID PRESENTATION.pptx for new apprentices.",
        instructions: [
          "Open <code>FIRST AID PRESENTATION.pptx</code>. Adjust slide orientation and layout.",
          "Set main titles to consistent font style and 32 pt size.",
          "Insert high-visibility bullet points and position diagrams neatly without overlapping text."
        ],
        type: "document_design",
        rubric: [
          { code: "B1", desc: "Slide layout and theme formatting applied consistently", mark: 3 },
          { code: "B2", desc: "Title typography set to 32 pt bold with high contrast", mark: 3 },
          { code: "B3", desc: "Illustrative graphics inserted and sized with no text obstruction", mark: 3 },
          { code: "B4", desc: "Professional slide balance suitable for large audience projection", mark: 2 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "First Aid Kit Inventory & Costings",
        marks: 15,
        brief: "Calculate replacement costs for medical supplies in FIRST AID KIT.xlsx.",
        instructions: [
          "In <code>FIRST AID KIT.xlsx</code>, calculate total units using <code>=SUM()</code>.",
          "Calculate unit cost multiplied by quantities, calculate average spend per station with <code>=AVERAGE()</code>.",
          "Format currency columns as British Pounds (£) with 2 decimal places and produce a breakdown chart."
        ],
        type: "spreadsheet",
        rubric: [
          { code: "C1", desc: "Sum formulas correctly entered and replicated", mark: 4 },
          { code: "C2", desc: "Average calculation accurate", mark: 3 },
          { code: "C3", desc: "Currency formatted to £ with 2 decimal places", mark: 2 },
          { code: "C4", desc: "Bar or Column chart created with title, legend, and values", mark: 6 }
        ]
      },
      {
        id: "taskD",
        letter: "Task D",
        title: "Medical Supplier Order Form",
        marks: 5,
        brief: "Order emergency medical refill packs through SUPPLIER.html.",
        instructions: [
          "Open <code>SUPPLIER.html</code>.",
          "Complete supplier order with order code <code>MED-2026-UK</code>, delivery address, and payment method.",
          "Submit form and verify confirmation receipt."
        ],
        type: "web_form",
        rubric: [
          { code: "D1", desc: "Accurate entry of order codes and contact fields", mark: 3 },
          { code: "D2", desc: "Delivery selection and proof of order confirmation generated", mark: 2 }
        ]
      },
      {
        id: "taskE",
        letter: "Task E",
        title: "Incident Logs & Cloud Backup Folder Structure",
        marks: 6,
        brief: "Create an organized folder hierarchy for statutory incident reports.",
        instructions: [
          "Create a folder named <code>Safety</code> with subfolder <code>Incidents 2026</code>.",
          "Save the incident log with an appropriate naming convention (e.g. <code>First Aid Log Q1 2026.docx</code>)."
        ],
        type: "file_mgmt",
        rubric: [
          { code: "E1", desc: "Folder and subfolder structure created correctly", mark: 3 },
          { code: "E2", desc: "Descriptive filename following naming conventions", mark: 3 }
        ]
      }
    ]
  },

  set4: {
    id: "set4",
    level: "Entry Level 3",
    name: "Entry Level 3 Mock: Apprenticeships & Work Experience (SAM)",
    totalMarks: 40,
    passMark: 26,
    durationMinutes: 60,
    dataPackUrl: "assets/downloads/dfs/dfsq-entry-level-3-sam-data-files.zip",
    dataPackName: "dfsq-entry-level-3-sam-data-files.zip",
    dataFiles: ["COLLEAGUES.jpg", "LOCAL BUSINESS.pptx", "TASK A EVIDENCE.docx", "WORK EXPERIENCE.html"],
    sectionA: [
      {
        qNum: 1,
        title: "Hardware Output Devices",
        stem: "Which of the following devices produces a physical paper copy of a computer document?",
        options: [
          { text: "A printer", isCorrect: true },
          { text: "A mouse", isCorrect: false },
          { text: "A microphone", isCorrect: false },
          { text: "A web camera", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: A printer is an output hardware device that transfers digital text and images onto physical paper."
      },
      {
        qNum: 2,
        title: "Accessibility Settings",
        stem: "Which operating system settings menu allows a user with visual impairment to make text larger and turn on high contrast?",
        options: [
          { text: "Ease of Access (Accessibility)", isCorrect: true },
          { text: "Disk Cleanup", isCorrect: false },
          { text: "Network Firewall", isCorrect: false },
          { text: "Sound Card Driver", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Ease of Access / Accessibility settings allow customization of text size, magnifiers, colour contrast, and screen readers."
      },
      {
        qNum: 3,
        title: "Audio Troubleshooting",
        stem: "You are playing a training video on your computer but cannot hear any sound coming through the built-in speakers. What is a sensible check to perform?",
        options: [
          { text: "Check whether headphones are plugged in or if the volume is muted", isCorrect: true },
          { text: "Buy a new computer monitor", isCorrect: false },
          { text: "Delete your web browser", isCorrect: false },
          { text: "Type your password again", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Audio output is redirected when headphones are inserted, or speakers may simply be muted in the volume mixer."
      },
      {
        qNum: 4,
        title: "Instant Messaging Icons",
        stem: "Which icon is universally used in software applications to open an instant message or live chat conversation?",
        options: [
          { text: "A speech bubble / chat icon", isCorrect: true },
          { text: "A floppy disk icon", isCorrect: false },
          { text: "A trash bin icon", isCorrect: false },
          { text: "A printer icon", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Speech bubbles symbolize conversational messaging and live chat in modern user interfaces."
      },
      {
        qNum: 5,
        title: "Spreadsheet Cell Identification",
        stem: "In a spreadsheet, what do you call the box where column B and row 4 intersect?",
        options: [
          { text: "Cell B4", isCorrect: true },
          { text: "Folder B4", isCorrect: false },
          { text: "Website B4", isCorrect: false },
          { text: "Pixel B4", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: A cell is the intersection of a column letter and a row number (e.g. B4)."
      },
      {
        qNum: 6,
        title: "Software Updates & Safety",
        stem: "Why is it important to install operating system updates when prompted on your laptop?",
        options: [
          { text: "It fixes security bugs and reduces the risk of malware", isCorrect: true },
          { text: "It changes your screen into a television", isCorrect: false },
          { text: "It deletes all your homework", isCorrect: false },
          { text: "It makes the keyboard keys change color", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Software security patches fix known vulnerabilities that hackers use to spread viruses and malware."
      },
      {
        qNum: 7,
        title: "Safe Typing Posture",
        stem: "What physical accessory helps keep your wrists straight and supported while typing for extended periods?",
        options: [
          { text: "A soft wrist rest", isCorrect: true },
          { text: "A wooden ruler", isCorrect: false },
          { text: "A heavy wristwatch", isCorrect: false },
          { text: "A pair of sunglasses", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Wrist rests reduce pressure on the carpal tunnel and help keep wrists at an ergonomic angle."
      },
      {
        qNum: 8,
        title: "One-Time Passcodes (OTP)",
        stem: "A 6-digit verification code sent by SMS to your phone to confirm an online purchase is called what?",
        options: [
          { text: "A one-time passcode (OTP)", isCorrect: true },
          { text: "A computer virus", isCorrect: false },
          { text: "A software license key", isCorrect: false },
          { text: "A website URL", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: A one-time passcode (OTP) is a temporary security code valid for only one login session or transaction."
      },
      {
        qNum: 9,
        title: "Input Hardware",
        stem: "Which hardware device is primarily used to enter letters and numbers into a digital document?",
        options: [
          { text: "A keyboard", isCorrect: true },
          { text: "A speaker", isCorrect: false },
          { text: "A monitor", isCorrect: false },
          { text: "A projector", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The keyboard is the primary alphanumeric input device for computers and digital tablets."
      },
      {
        qNum: 10,
        title: "Remote Data Storage",
        stem: "Saving documents on the internet rather than on your computer's local hard drive is commonly known as saving to the what?",
        options: [
          { text: "The Cloud", isCorrect: true },
          { text: "The Recycle Bin", isCorrect: false },
          { text: "The CD-ROM", isCorrect: false },
          { text: "The Calculator", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Cloud storage refers to remote internet-hosted servers accessible across multiple devices."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "Minimum Wage Search & Email Contacts",
        marks: 10,
        brief: "Research apprentice minimum wage rates and add new contact details to your email software.",
        instructions: [
          "Use a search engine to find the UK National Minimum Wage rate for apprentices aged 16–18.",
          "Record the source website URL and minimum wage rate in <code>TASK A EVIDENCE.docx</code>.",
          "Add two colleague contact email addresses to your contacts list.",
          "Email <code>TASK A EVIDENCE.docx</code> as an attachment to your supervisor with a polite greeting and closing."
        ],
        type: "search_email",
        searchAnswer: "apprentice minimum wage rate UK",
        searchResultSnippet: "GOV.UK: National Minimum Wage rate for an apprentice aged 16 to 18 is £5.28 per hour (2023 rate) / £6.40 (current rate).",
        rubric: [
          { code: "A1", desc: "Search engine shows relevant criteria for apprentice minimum wage", mark: 1 },
          { code: "A2", desc: "Website address and accurate wage rate entered in evidence document", mark: 2 },
          { code: "A3", desc: "Colleague image captured and saved in folder", mark: 1 },
          { code: "A4", desc: "Two email contacts accurately added to contacts book", mark: 2 },
          { code: "A5a", desc: "Email addressed correctly to recipient", mark: 1 },
          { code: "A5b", desc: "Subject line relevant to apprenticeship evidence", mark: 1 },
          { code: "A5c", desc: "TASK A EVIDENCE.docx attached to email", mark: 1 },
          { code: "A5d", desc: "Message includes polite greeting and closing", mark: 1 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Slide Presentation Editing",
        marks: 19,
        brief: "Edit and format the slideshow LOCAL BUSINESS.pptx to promote apprenticeships.",
        instructions: [
          "Locate <code>LOCAL BUSINESS.pptx</code> and rename it to <code>Apprenticeship Advert.pptx</code>.",
          "On slide 1, add telephone number <code>0800 015 0400</code> and email <code>help@service.gov.uk</code>.",
          "Change font size of 'APPRENTICESHIPS ON OFFER' to <strong>48 pt and Red</strong>.",
          "Insert a new slide 3, insert <code>COLLEAGUES.jpg</code> resized to <strong>8 cm × 8 cm</strong>, and ensure no overlap."
        ],
        type: "document_design",
        rubric: [
          { code: "B1", desc: "Presentation file located and renamed appropriately", mark: 1 },
          { code: "B2", desc: "Phone number (0800 015 0400) and email inserted in correct locations", mark: 2 },
          { code: "B3", desc: "Application deadline updated to August", mark: 1 },
          { code: "B4", desc: "Title changed to font size 48 and colour Red", mark: 2 },
          { code: "B5", desc: "Slide text clear, readable, and left aligned", mark: 2 },
          { code: "B6", desc: "New slide 3 inserted after slide 2", mark: 1 },
          { code: "B7", desc: "COLLEAGUES.jpg inserted and sized to 8 cm x 8 cm", mark: 2 },
          { code: "B8", desc: "Descriptive title added to slide 3", mark: 1 },
          { code: "B9", desc: "No image overlap; professional large-screen presentation layout", mark: 7 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "Work Experience Application Web Form",
        marks: 11,
        brief: "Submit the online registration form in WORK EXPERIENCE.html.",
        instructions: [
          "Open <code>WORK EXPERIENCE.html</code>.",
          "Enter Password: <code>23samsv2&dfs</code>.",
          "Candidate Name: <code>Fran Fouraud</code>, DOB: <code>09/06/2005</code>, Tel: <code>01632 960455</code>, Email: <code>fran@samsdfs.biz</code>.",
          "Placement choice: <strong>Office</strong>, Duration: <strong>6 weeks</strong>, then submit."
        ],
        type: "web_form",
        rubric: [
          { code: "C1", desc: "Password (23samsv2&dfs) entered accurately", mark: 2 },
          { code: "C2", desc: "Candidate personal details entered with 100% accuracy", mark: 4 },
          { code: "C3", desc: "Placement choice (Office) and duration (6 weeks) selected correctly", mark: 3 },
          { code: "C4", desc: "Application submitted and confirmation screen generated", mark: 2 }
        ]
      }
    ]
  },
  set5: {
    id: "set5",
    level: "Level 1",
    name: "Mock 4: Gelato & Ice Cream Business (Level 1 Past Test Set 1)",
    totalMarks: 54,
    passMark: 35,
    durationMinutes: 90,
    dataPackUrl: "assets/downloads/dfs/dfs-level-1-sam-data-files.zip",
    dataPackName: "dfs-level-1-past-test-set-1-data-files.zip",
    dataFiles: ["ALLERGY.docx", "ICE CREAM POSTER.docx", "ICE CREAM SALES.xlsx", "UTILITY.html", "DFS LEVEL 1 SET 1 IMAGES/ICE CREAM.jpg"],
    sectionA: [
      {
        qNum: 1,
        title: "Food Safety & Allergen Information Search",
        stem: "Which search technique returns the most reliable and accurate official guidance on food allergen labelling?",
        options: [
          { text: "Clicking random unverified food blogs on social media", isCorrect: false },
          { text: "Using exact phrase quotes on official government or FSA websites (e.g. \"food allergen labelling guidance\")", isCorrect: true },
          { text: "Opening whatever link has the most advertisements", isCorrect: false },
          { text: "Forwarding spam emails to all company staff", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Using quotation marks for exact phrase searches and consulting authoritative domains (such as food.gov.uk) yields verified regulatory information."
      },
      {
        qNum: 2,
        title: "Cloud Backup & Workplace File Sharing",
        stem: "What is the primary operational advantage of storing business inventory files in a secure cloud service rather than solely on a local laptop hard drive?",
        options: [
          { text: "Files can be accessed and safely updated from any authenticated authorized device with an internet connection", isCorrect: true },
          { text: "It prevents anyone in the company from editing the files", isCorrect: false },
          { text: "It reduces your computer's internet speed", isCorrect: false },
          { text: "Cloud storage eliminates the need for strong passwords", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Cloud storage provides multi-device accessibility, automated offsite backup, and collaborative synchronization for workplace teams."
      },
      {
        qNum: 3,
        title: "Phishing & Fraudulent Invoices",
        stem: "A shop manager receives an email titled 'Urgent Unpaid Ice Cream Flavour Invoice - Click Here Immediately'. The sender address is billing-support@freemail-quick99.com. What should the manager do?",
        options: [
          { text: "Click the attachment to verify the bank account details", isCorrect: false },
          { text: "Do not click any links or attachments; verify the invoice through known official supplier phone records", isCorrect: true },
          { text: "Reply to the email with the business credit card details", isCorrect: false },
          { text: "Forward the email to customers to ask if they recognize it", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Suspicious sender domains and urgent payment threats are hallmarks of phishing. Never click links or open attachments; independently verify using trusted contacts."
      },
      {
        qNum: 4,
        title: "Display Screen Equipment & Ergonomics",
        stem: "An employee spends several hours daily entering sales figures into spreadsheets. Which ergonomic setup reduces repetitive strain and posture fatigue?",
        options: [
          { text: "Adjust chair height so forearms are horizontal and feet rest flat on the floor or a footrest", isCorrect: true },
          { text: "Slouch back and keep the screen above eye level", isCorrect: false },
          { text: "Type continuously for 8 hours without breaks", isCorrect: false },
          { text: "Place the mouse as far away as possible on the desk", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Proper DSE positioning requires level forearms, screen at eye level, lumbar support, and periodic posture breaks."
      },
      {
        qNum: 5,
        title: "File Formats & Data Integrity",
        stem: "Which file extension is standard for tabular data spreadsheets containing formulas, columns, and sales calculations?",
        options: [
          { text: ".docx", isCorrect: false },
          { text: ".xlsx", isCorrect: true },
          { text: ".jpg", isCorrect: false },
          { text: ".mp3", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: .xlsx is the standard file format for Microsoft Excel and OpenXML spreadsheet workbooks."
      },
      {
        qNum: 6,
        title: "Secure Wi-Fi & Workplace Transactions",
        stem: "When processing daily card machine totals on a laptop, which network connection is most secure?",
        options: [
          { text: "An unsecured open public Wi-Fi network at a nearby coffee shop", isCorrect: false },
          { text: "A WPA2/WPA3 password-protected encrypted private business Wi-Fi network", isCorrect: true },
          { text: "An open network with no password required", isCorrect: false },
          { text: "A neighbor's unencrypted hotspot", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Encrypted WPA2/WPA3 business networks safeguard sensitive payment data from eavesdropping and packet interception."
      },
      {
        qNum: 7,
        title: "Strong Password Standards",
        stem: "Which of the following represents the strongest password for a business accounts portal?",
        options: [
          { text: "icecream123", isCorrect: false },
          { text: "password2026", isCorrect: false },
          { text: "G3l@to_Sales!89#Bite", isCorrect: true },
          { text: "admin", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Strong passwords combine uppercase, lowercase, numbers, special symbols, and sufficient length without predictable dictionary words."
      },
      {
        qNum: 8,
        title: "Copyright & Online Images",
        stem: "The business wants an image of a vintage ice cream van for a promotional poster. How should they acquire the image legitimately?",
        options: [
          { text: "Take their own original photograph or license a royalty-free stock image with commercial permissions", isCorrect: true },
          { text: "Download and use any image found on a Google search without checking the owner's license", isCorrect: false },
          { text: "Screenshot a rival shop's branded logo and paste it onto the poster", isCorrect: false },
          { text: "Remove the watermark from a protected photograph using image editing software", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Digital creators must respect intellectual property rights by creating original media or obtaining appropriate commercial licenses."
      },
      {
        qNum: 9,
        title: "Operating System & Antivirus Updates",
        stem: "Why is it critical to enable automatic security updates on business devices?",
        options: [
          { text: "To patch newly discovered vulnerabilities and defend against emerging malware", isCorrect: true },
          { text: "To delete old email messages automatically", isCorrect: false },
          { text: "To change your monitor resolution every night", isCorrect: false },
          { text: "To prevent staff from connecting to the printer", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Regular system patches resolve critical security loopholes, mitigating ransomware, zero-day exploits, and malware infections."
      },
      {
        qNum: 10,
        title: "Data Protection & Customer Privacy (GDPR)",
        stem: "Under data protection law, how should customer loyalty email lists and contact phone numbers be stored?",
        options: [
          { text: "Posted publicly on the shop window for easy access", isCorrect: false },
          { text: "Encrypted and password-protected with access restricted only to authorized personnel", isCorrect: true },
          { text: "Saved on a shared unencrypted USB drive left on the counter", isCorrect: false },
          { text: "Uploaded to an open public cloud directory without passwords", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: GDPR requires personal data to be kept secure, confidential, and protected against unauthorized access or disclosure."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "Allergen Information Search & Email Communication",
        marks: 7,
        brief: "The business owner needs the official allergen declaration requirements for unpacked dairy and nut products, and needs an email sent to the shop team.",
        instructions: [
          "Use a search engine to locate official UK Food Standards Agency allergen declaration guidance.",
          "Capture a screenshot of your search terms and results.",
          "Compose an email to <code>manager@pearson.service</code> with the subject <code>Allergen Guidance Notice</code>.",
          "State clearly the 14 major allergens requirement and mandatory handling precautions.",
          "Include a professional email sign-off and your candidate name."
        ],
        type: "search_email",
        rubric: [
          { code: "A1", desc: "Search term and results screenshot showing official FSA guidance", mark: 2 },
          { code: "A2", desc: "Email recipient (manager@pearson.service) and subject entered accurately", mark: 2 },
          { code: "A3", desc: "Allergen declaration content and polite greeting clearly stated", mark: 2 },
          { code: "A4", desc: "Professional sign-off and automated signature formatted properly", mark: 1 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Promotional Poster Document Design",
        marks: 11,
        brief: "Design an attractive promotional poster using ICE CREAM POSTER.docx to advertise the summer artisan gelato launch.",
        instructions: [
          "Open <code>ICE CREAM POSTER.docx</code> in the data folder.",
          "Insert the gelato photo from the images folder and align it neatly.",
          "Apply consistent typography, clear heading hierarchy, and bold pricing.",
          "Include the promotional discount: <strong>Buy One Get One Half Price on Tuesdays</strong>.",
          "Ensure allergen notice is clearly legible at the foot of the poster."
        ],
        type: "flyer_design",
        rubric: [
          { code: "B1", desc: "Image inserted, proportioned, and positioned effectively without distortion", mark: 3 },
          { code: "B2", desc: "Clear headings, legible fonts, and cohesive professional styling", mark: 3 },
          { code: "B3", desc: "Promotional offer and correct pricing highlighted prominently", mark: 3 },
          { code: "B4", desc: "Mandatory allergen disclaimer text included at the base of the poster", mark: 2 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "Ice Cream Sales Spreadsheet & Formulas",
        marks: 15,
        brief: "Open ICE CREAM SALES.xlsx, calculate total weekly sales, flavour percentages, and average daily revenue.",
        instructions: [
          "Open <code>ICE CREAM SALES.xlsx</code>.",
          "Insert a formula in column E to calculate Total Revenue for each flavour (Quantity × Unit Price).",
          "Use <code>=SUM()</code> to calculate the grand total weekly revenue.",
          "Use <code>=AVERAGE()</code> to calculate the mean daily sales volume.",
          "Format all currency values to 2 decimal places with the £ symbol.",
          "Create a 2D Bar or Column chart comparing weekly sales across flavours."
        ],
        type: "spreadsheet",
        rubric: [
          { code: "C1", desc: "Multiplication formulas correctly implemented in column E", mark: 3 },
          { code: "C2", desc: "SUM and AVERAGE functions accurately calculated with correct cell ranges", mark: 4 },
          { code: "C3", desc: "Currency formatting (£, 2 decimal places) applied consistently", mark: 3 },
          { code: "C4", desc: "Chart created with appropriate title, axis labels, and clear legend", mark: 5 }
        ]
      },
      {
        id: "taskD",
        letter: "Task D",
        title: "Online Utility & Equipment Management",
        marks: 5,
        brief: "Log into the simulated equipment service portal in UTILITY.html and register freezers service.",
        instructions: [
          "Open <code>UTILITY.html</code> in a browser.",
          "Enter Portal Account Number: <code>IC-7829-GEL</code> and Password: <code>Ch1ll&Freeze26</code>.",
          "Select Equipment Category: <strong>Commercial Display Freezer</strong>.",
          "Submit the service request and verify the confirmation message."
        ],
        type: "web_form",
        rubric: [
          { code: "D1", desc: "Portal login credentials entered accurately", mark: 2 },
          { code: "D2", desc: "Equipment category selected correctly", mark: 1 },
          { code: "D3", desc: "Confirmation reference code recorded as evidence", mark: 2 }
        ]
      },
      {
        id: "taskE",
        letter: "Task E",
        title: "File Organization & Backup Protocol",
        marks: 6,
        brief: "Organize the shop data folder into structured subdirectories and establish safe backup procedures.",
        instructions: [
          "Create subfolders named <code>Marketing</code>, <code>Financials</code>, and <code>Compliance</code>.",
          "Move files into their respective subfolders.",
          "Provide a written explanation of the recommended weekly backup routine."
        ],
        type: "file_org",
        rubric: [
          { code: "E1", desc: "Subfolder directory structure created with logical naming", mark: 2 },
          { code: "E2", desc: "Files categorized and moved accurately without data duplication", mark: 2 },
          { code: "E3", desc: "Backup procedure explanation demonstrates sound data security principles", mark: 2 }
        ]
      }
    ]
  },
  set6: {
    id: "set6",
    level: "Level 1",
    name: "Mock 5: Riverside Community Health & Leisure Hub (Level 1 Practice Set 3)",
    totalMarks: 54,
    passMark: 35,
    durationMinutes: 90,
    dataPackUrl: "assets/downloads/dfs/dfs-level-1-practice-set-3-data-files.zip",
    dataPackName: "dfs-level-1-practice-set-3-data-files.zip",
    dataFiles: [
      "ACTIVITY TIMETABLE.docx",
      "COMMUNITY NOTICE.docx",
      "MEMBERSHIP PORTAL.html",
      "SPORTS BOOKINGS.xlsx",
      "PRACTICE SET 3 DFS LEVEL 1 IMAGES/SPORTS ACTIVITIES.jpg",
      "PRACTICE SET 3 DFS LEVEL 1 IMAGES/SPORTS BADGE.jpg"
    ],
    sectionA: [
      {
        qNum: 1,
        title: "Multi-Factor Authentication (MFA / 2FA)",
        stem: "Why should staff at a community leisure centre enable Multi-Factor Authentication (MFA) when accessing their staff accounts online?",
        options: [
          { text: "It saves internet bandwidth and boosts network connection speeds", isCorrect: false },
          { text: "It provides an additional layer of defence by requiring two or more verification factors to confirm identity", isCorrect: true },
          { text: "It ensures that files stored locally on the PC cannot be accidentally deleted", isCorrect: false },
          { text: "It automatically updates the operating system every evening", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Multi-factor authentication adds an essential second verification factor (such as an authenticator app code or SMS token) beyond just a password, making unauthorized account access substantially harder even if passwords are breached."
      },
      {
        qNum: 2,
        title: "Display Screen Equipment & Ergonomics",
        stem: "A receptionist at the leisure hub spends long shifts entering booking data into a computer. What ergonomic adjustment best prevents neck and eye strain?",
        options: [
          { text: "Positioning the monitor directly in front of the user with the top of the screen at eye level and reducing screen glare", isCorrect: true },
          { text: "Tilting the screen upwards at a steep angle and dimming room lights completely", isCorrect: false },
          { text: "Keeping the keyboard on the user's lap and sitting on a rigid stool", isCorrect: false },
          { text: "Increasing screen resolution to the highest setting so text is as tiny as possible", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: In accordance with HSE Display Screen Equipment (DSE) regulations, the monitor should be positioned directly in front of the user with the top of the display at eye height, arm's length away, with good ambient lighting to prevent musculoskeletal fatigue and eye strain."
      },
      {
        qNum: 3,
        title: "Refining Online Searches & Search Operators",
        stem: "A coordinator wants to find official UK government sports facility guidelines published exclusively as a PDF document. Which search query is most effective?",
        options: [
          { text: "search sports facility rules anywhere online", isCorrect: false },
          { text: "\"sports facility guidelines\" site:gov.uk filetype:pdf", isCorrect: true },
          { text: "*sports* + *facilities* + help + please", isCorrect: false },
          { text: "click on the first sponsored link on social media", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Using quotation marks for exact phrasing, 'site:gov.uk' to restrict results to authoritative government domains, and 'filetype:pdf' specifically filters for published document guidelines."
      },
      {
        qNum: 4,
        title: "Digital Footprint & Child Safeguarding",
        stem: "A sports coach creates a public leisure hub group on social media. What is a primary risk of sharing candid photos of junior participants without parental permission?",
        options: [
          { text: "It slows down the social media platform's cloud server", isCorrect: false },
          { text: "It breaches data privacy and child safeguarding regulations by exposing personal identifiable information publicly", isCorrect: true },
          { text: "It converts high-resolution images into compressed vector shapes", isCorrect: false },
          { text: "It automatically locks the coach out of their mobile phone", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Under GDPR, the Data Protection Act 2018, and child safeguarding standards, publishing identifiable images of minors online requires explicit parental/guardian consent and controlled privacy settings."
      },
      {
        qNum: 5,
        title: "Cybersecurity & Ransomware Threats",
        stem: "A desktop screen suddenly displays a warning stating that all centre booking files are encrypted and demanding payment in digital currency to restore access. What type of malware is this?",
        options: [
          { text: "Spyware", isCorrect: false },
          { text: "Ransomware", isCorrect: true },
          { text: "Adware", isCorrect: false },
          { text: "Phishing email", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Ransomware is malicious software that encrypts user files and storage devices, withholding decryption keys until an extortion ransom is paid."
      },
      {
        qNum: 6,
        title: "Secure Web Connections & SSL/TLS",
        stem: "When entering customer payment card information on an online booking portal, which indicator confirms that communication between the browser and the web server is encrypted?",
        options: [
          { text: "The web address starts with https:// accompanied by a closed padlock icon in the browser address bar", isCorrect: true },
          { text: "The web page has animated pop-up banner advertisements", isCorrect: false },
          { text: "The website URL ends in .org or .co.uk", isCorrect: false },
          { text: "The web page loads in under 2 seconds", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Hypertext Transfer Protocol Secure (HTTPS) and the padlock symbol confirm that an active SSL/TLS security certificate encrypts data during transmission against eavesdropping."
      },
      {
        qNum: 7,
        title: "Digital Storage Units & Capacity Hierarchy",
        stem: "Which list correctly arranges digital storage units in ascending order from smallest capacity to largest capacity?",
        options: [
          { text: "Gigabyte (GB) → Megabyte (MB) → Terabyte (TB) → Kilobyte (KB)", isCorrect: false },
          { text: "Kilobyte (KB) → Megabyte (MB) → Gigabyte (GB) → Terabyte (TB)", isCorrect: true },
          { text: "Terabyte (TB) → Gigabyte (GB) → Megabyte (MB) → Kilobyte (KB)", isCorrect: false },
          { text: "Megabyte (MB) → Kilobyte (KB) → Terabyte (TB) → Gigabyte (GB)", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Digital storage capacity progresses from Kilobyte (~1,000 bytes) to Megabyte (~1,000 KB), Gigabyte (~1,000 MB), and Terabyte (~1,000 GB)."
      },
      {
        qNum: 8,
        title: "Data Protection & Subject Access Requests",
        stem: "A centre member asks to view all personal health questionnaire records and class attendance histories held about them by the leisure hub. Under UK GDPR, what is this right known as?",
        options: [
          { text: "Right to erase software licences", isCorrect: false },
          { text: "Right of access (Subject Access Request)", isCorrect: true },
          { text: "Right to transfer hardware ownership", isCorrect: false },
          { text: "Right to demand administrator network privileges", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: The UK GDPR Right of Access entitles individuals to receive confirmation that their data is being processed and obtain a copy of their personal data (Subject Access Request)."
      },
      {
        qNum: 9,
        title: "File Compression & Email Attachments",
        stem: "Why does the leisure centre manager compress (zip) high-resolution promotional event photos before emailing them to the local community newsletter?",
        options: [
          { text: "To delete the original images from the computer permanently", isCorrect: false },
          { text: "To reduce total file size for faster transmission and avoid email attachment size limits", isCorrect: true },
          { text: "To prevent recipients from viewing the pictures on mobile screens", isCorrect: false },
          { text: "To alter the colour balance of the photographs automatically", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Compressing files into a ZIP archive reduces total storage size and bundles multiple assets together, ensuring files stay within email service attachment limits (typically 20-25 MB)."
      },
      {
        qNum: 10,
        title: "Safe Transmission of Sensitive Workplace Data",
        stem: "The manager needs to transmit an urgent payroll report containing employee National Insurance numbers and bank sort codes to the external accountant. What is the safest digital transmission method?",
        options: [
          { text: "Posting the spreadsheet on the leisure centre's open Facebook page", isCorrect: false },
          { text: "Encrypting or password-protecting the file and communicating the strong password via a separate, secure secondary channel", isCorrect: true },
          { text: "Pasting all bank account numbers into the subject line of a standard email", isCorrect: false },
          { text: "Saving the file onto a lost-property USB memory stick and leaving it on the counter", isCorrect: false }
        ],
        mark: 1,
        explanation: "Pearson Criteria: Sensitive personal and financial data must be encrypted with robust password protection, and the decryption key must be transmitted out-of-band (e.g. via telephone or separate encrypted channel)."
      }
    ],
    tasks: [
      {
        id: "taskA",
        letter: "Task A",
        title: "Information Search & Professional Email Communication",
        marks: 7,
        brief: "The leisure hub manager, Tariq, wants you to locate the official UK physical activity guidelines for adults and email the summary to him.",
        instructions: [
          "Use a search engine to find the recommended weekly physical activity duration for adults in the UK. Take a screenshot of your search terms and results.",
          "Compose an email to <code>tariq.manager@riversidehub.co.uk</code> with the subject <code>UK Physical Activity Guidelines Summary</code>.",
          "Include a polite greeting (e.g. 'Dear Tariq,' or 'Hello Tariq,'), state clearly that adults need at least <strong>150 minutes of moderate activity</strong> (or 75 minutes of vigorous activity) per week, plus muscle strengthening on at least 2 days.",
          "Add a professional automated email signature containing 'Kind regards' and your candidate name."
        ],
        type: "search_email",
        searchAnswer: "UK physical activity guidelines adults 150 minutes",
        searchResultSnippet: "Official UK Physical Activity Guidelines: Adults aged 19 to 64 should aim to be physically active daily. Each week, adults should accumulate at least 150 minutes of moderate intensity activity (such as brisk walking or cycling) or 75 minutes of vigorous activity, plus strengthening activities on at least 2 days.",
        rubric: [
          { code: "A1", desc: "Search engine query shows appropriate keywords (e.g. 'UK physical activity guidelines adults')", mark: 1 },
          { code: "A1b", desc: "Correct guideline duration identified: at least 150 minutes moderate intensity per week", mark: 1 },
          { code: "A2", desc: "Automated email signature created with 'Kind regards' and candidate name", mark: 1 },
          { code: "A3a", desc: "Recipient email entered accurately: tariq.manager@riversidehub.co.uk", mark: 1 },
          { code: "A3b", desc: "Subject line concise and descriptive: 'UK Physical Activity Guidelines Summary'", mark: 1 },
          { code: "A3c", desc: "Professional greeting and polite business sign-off maintained", mark: 1 },
          { code: "A3d", desc: "Accurate physical activity recommendations included in message body", mark: 1 }
        ]
      },
      {
        id: "taskB",
        letter: "Task B",
        title: "Creating & Formatting an Activity Timetable Flyer",
        marks: 11,
        brief: "Riverside Community Hub wants an attractive, professional promotional flyer created using ACTIVITY TIMETABLE.docx to advertise evening fitness classes.",
        instructions: [
          "Open <code>ACTIVITY TIMETABLE.docx</code> from your data folder. Change page orientation to <strong>Landscape</strong>.",
          "Format the main title 'Riverside Community Leisure Hub — Evening Fitness Timetable' in bold, 22 pt, centered.",
          "Insert the timetable schedule below the heading formatted as a clean 5-column table with adjusted column widths and header row shaded in light teal.",
          "Insert <code>SPORTS ACTIVITIES.jpg</code> to the right-hand side of the table.",
          "Crop the image to eliminate unnecessary borders, resize to <strong>6 cm height</strong> maintaining aspect ratio, and apply a subtle border.",
          "Highlight the special introductory offer in a distinct callout box: 'Special Introductory Offer: 20% discount on all monthly class passes when booked online before Friday! Voucher code: RIVERSIDE20'.",
          "Apply an outer page border. Ensure balanced, professional layout with zero overlapping text."
        ],
        type: "flyer_design",
        rubric: [
          { code: "B1", desc: "Page orientation set to Landscape", mark: 1 },
          { code: "B2a", desc: "Main heading formatted in bold, 22 pt font, centered", mark: 1 },
          { code: "B2b", desc: "Timetable formatted inside a clean structured table with adjusted column widths", mark: 1 },
          { code: "B2c", desc: "Table header row shaded with a contrasting background color", mark: 1 },
          { code: "B3a", desc: "Image SPORTS ACTIVITIES.jpg inserted into document", mark: 1 },
          { code: "B3b", desc: "Image positioned neatly adjacent to or right-hand side of timetable", mark: 1 },
          { code: "B4", desc: "Image cropped to remove excess margins/borders", mark: 1 },
          { code: "B5", desc: "Image resized to 6 cm height maintaining proportions", mark: 1 },
          { code: "B6", desc: "Special introductory offer highlighted in a styled callout box", mark: 1 },
          { code: "B7a", desc: "Decorative outer page border applied", mark: 1 },
          { code: "B7b", desc: "Document fit for purpose: balanced spacing, legible fonts, zero overlapping elements", mark: 1 }
        ]
      },
      {
        id: "taskC",
        letter: "Task C",
        title: "Sports Bookings & Revenue Spreadsheet Analysis",
        marks: 15,
        brief: "Tariq needs weekly court bookings and revenue calculated in SPORTS BOOKINGS.xlsx, formatted into currency, and charted.",
        instructions: [
          "Merge and centre cells A1:H1, set font size to 20 pt, bold, and shade cells A1:H1 soft blue.",
          "In cell G4, enter a formula to calculate Total Bookings for Badminton Court 1: <code>=SUM(C4:F4)</code>.",
          "In cell H4, calculate Total Revenue: <code>=G4*B4</code> (Total Bookings × Court Hire Fee).",
          "Replicate formulas down columns G and H for all 8 sports activities (rows 4 to 11).",
          "In row 12, calculate the Daily Average Bookings: <code>=AVERAGE(C4:C11)</code> and replicate across columns C to F.",
          "In cell H12, calculate Grand Total Revenue using <code>=SUM(H4:H11)</code>.",
          "Format all court hire fees (column B) and revenue amounts (column H and cell H12) as British Pounds (£) with 2 decimal places.",
          "Sort the activities table (rows A4:H11) in descending order of Total Revenue (Column H).",
          "Create a 2D Clustered Column or Bar Chart comparing Activity / Facility (A3:A11) against Total Bookings (G3:G11). Add an informative chart title, legible axis titles, and position the chart neatly below the data table or on a separate sheet."
        ],
        type: "spreadsheet",
        rubric: [
          { code: "C1a", desc: "Main title merged & centred across A1:H1 with 20 pt bold styling", mark: 1 },
          { code: "C1b", desc: "Header row shaded with soft blue background fill", mark: 1 },
          { code: "C2a", desc: "Total bookings formula entered correctly in cell G4: =SUM(C4:F4)", mark: 1 },
          { code: "C2b", desc: "Revenue formula calculated correctly in cell H4: =G4*B4", mark: 1 },
          { code: "C3", desc: "Formulas successfully replicated down columns G and H for rows 4 to 11", mark: 2 },
          { code: "C4", desc: "Average formula entered correctly in row 12: =AVERAGE(C4:C11)", mark: 1 },
          { code: "C5", desc: "Average formula replicated horizontally across columns C to F", mark: 1 },
          { code: "C6", desc: "Grand total revenue formula entered in cell H12: =SUM(H4:H11)", mark: 1 },
          { code: "C7", desc: "Currency formatting (£ with 2 decimal places) applied to all monetary figures", mark: 2 },
          { code: "C8", desc: "Data sorted in descending order of Total Revenue (Column H)", mark: 2 },
          { code: "C9a", desc: "Bar or Column chart created showing Activity vs Total Bookings accurately", mark: 1 },
          { code: "C9b", desc: "Chart includes appropriate title and clearly labeled axes", mark: 1 }
        ]
      },
      {
        id: "taskD",
        letter: "Task D",
        title: "Online Membership Portal Registration & Upload",
        marks: 5,
        brief: "Register a junior sports charter club on the simulated online membership portal using MEMBERSHIP PORTAL.html.",
        instructions: [
          "Open <code>MEMBERSHIP PORTAL.html</code> in a web browser.",
          "Enter Reference Number: <code>RHC-9428-JUN</code>, Organisation Name: <code>Riverside Youth FC</code>, Contact Person: <code>Sarah Jenkins</code>, Telephone: <code>01632 960882</code>, Email: <code>s.jenkins@riversideyouth.org.uk</code>.",
          "Select Membership Category: <strong>Junior Community Charter Club</strong> and enter Court Allocation Code: <code>COURT-HALL-B</code>.",
          "Upload the club verification file <code>SPORTS BADGE.jpg</code>.",
          "Select communication preferences for <strong>Email Updates</strong> and <strong>SMS Alerts</strong>, then click Submit Registration.",
          "Record the generated confirmation token (<code>AUTH-BOOKING-9942-VERIFIED</code>) as evidence."
        ],
        type: "web_form",
        rubric: [
          { code: "D1", desc: "Organisation and contact details entered accurately (Account RHC-9428-JUN, Riverside Youth FC, Sarah Jenkins, phone, email)", mark: 2 },
          { code: "D2", desc: "Membership category and court allocation code selected accurately", mark: 1 },
          { code: "D3", desc: "Verification file uploaded into form file field", mark: 1 },
          { code: "D4", desc: "Communication preferences selected for Email and SMS and confirmation token recorded", mark: 1 }
        ]
      },
      {
        id: "taskE",
        letter: "Task E",
        title: "File Organization & Network Troubleshooting",
        marks: 6,
        brief: "The leisure hub has installed a new wireless tablet terminal for pool deck check-ins that fails to obtain an IP address. Organise directories and document troubleshooting steps.",
        instructions: [
          "In your candidate workspace, create a new top-level folder named <code>Network Support</code>.",
          "Inside <code>Network Support</code>, create a subfolder named <code>Pool Deck Tablet</code>.",
          "Research why a wireless tablet device might fail to obtain an IP address or connect to Wi-Fi (e.g., router DHCP pool exhausted, tablet out of wireless range, incorrect WPA3 security key, or 2.4GHz / 5GHz frequency band mismatch).",
          "Save your troubleshooting solution inside the <code>Pool Deck Tablet</code> folder with the descriptive filename <code>Tablet Connection Troubleshooting.docx</code>.",
          "Ensure your recommendations are practical, well-structured, and cite a reliable, secure (HTTPS) technical support reference with a recent date."
        ],
        type: "file_mgmt",
        rubric: [
          { code: "E1a", desc: "New top-level directory created named 'Network Support'", mark: 1 },
          { code: "E1b", desc: "Subfolder created inside named 'Pool Deck Tablet'", mark: 1 },
          { code: "E2a", desc: "Document saved with appropriate descriptive filename 'Tablet Connection Troubleshooting.docx'", mark: 1 },
          { code: "E2b", desc: "Identifies at least two plausible technical causes for IP / DHCP connection failure", mark: 1 },
          { code: "E2c", desc: "Provides clear sequential troubleshooting steps to restore tablet connectivity", mark: 1 },
          { code: "E2d", desc: "Demonstrates secure technical research habits citing reliable HTTPS sources with date verification", mark: 1 }
        ]
      }
    ]
  }
};

let currentSetKey = "set1";
let examMode = "practice"; // 'practice' or 'exam'
let timerInterval = null;
let secondsRemaining = 90 * 60; // 90 mins
let isTimerRunning = false;

// Candidate State
let userAnswers = {}; // { qNum: optionIndex }
let rubricChecked = {}; // { rubricCode: boolean }

document.addEventListener("DOMContentLoaded", () => {
  initMockExam();
});

function initMockExam() {
  renderMockSet(currentSetKey);
  setupEventListeners();
  resetTimer();
}

function selectMockSet(setKey) {
  if (!DFS_MOCK_DATA[setKey]) return;
  currentSetKey = setKey;
  userAnswers = {};
  rubricChecked = {};

  // Update tabs UI
  document.querySelectorAll(".btn-set-tab").forEach(tab => {
    tab.classList.toggle("active", tab.dataset.set === setKey);
  });

  // Reset timer duration to match set
  const set = DFS_MOCK_DATA[setKey];
  secondsRemaining = set.durationMinutes * 60;
  pauseTimer();
  updateTimerDisplay();

  renderMockSet(setKey);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function setExamMode(mode) {
  examMode = mode;
  document.querySelectorAll(".btn-mode-tab").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.mode === mode);
  });

  const feedbackElements = document.querySelectorAll(".mock-q-feedback");
  feedbackElements.forEach(el => {
    if (mode === "exam") {
      el.classList.remove("show");
    }
  });

  alert(mode === "exam" 
    ? "Official Exam Mode Active:\n• Timer running under test conditions\n• Answers & rationales hidden until you submit your final test\n• 90-minute countdown active!"
    : "Tutor & Practice Mode Active:\n• Instant feedback enabled on every question\n• Full Pearson examiner marking criteria & rationales displayed immediately!"
  );
}

function renderMockSet(setKey) {
  const set = DFS_MOCK_DATA[setKey];
  if (!set) return;

  // Update Header Banner
  const titleEl = document.getElementById("mockExamActiveTitle");
  if (titleEl) titleEl.textContent = set.name;

  const marksBadge = document.getElementById("mockExamMarksBadge");
  if (marksBadge) marksBadge.textContent = `${set.totalMarks} Marks (${set.level})`;

  // Render Data Pack Card
  const dataPackContainer = document.getElementById("dataPackContainer");
  if (dataPackContainer) {
    dataPackContainer.innerHTML = `
      <div class="dfs-data-pack-card">
        <div class="dfs-data-pack-details">
          <h3><i class="fa-solid fa-folder-arrow-down" style="color:var(--accent,#f59e0b);"></i> Candidate Data Files Package</h3>
          <p>Official Pearson Edexcel candidate files required for Section B practical tasks:</p>
          <div class="dfs-data-pack-files">
            ${set.dataFiles.map(f => `<span class="dfs-file-pill"><i class="fa-regular fa-file"></i> ${f}</span>`).join("")}
          </div>
        </div>
        <div>
          <a href="${set.dataPackUrl}" class="btn-download-pack" download>
            <i class="fa-solid fa-cloud-arrow-down"></i> Download Data Files (.ZIP)
          </a>
        </div>
      </div>
    `;
  }

  // Render Section A Questions
  const secAContainer = document.getElementById("sectionAQuestionsList");
  if (secAContainer) {
    secAContainer.innerHTML = set.sectionA.map((q, idx) => `
      <div class="mock-q-card" id="qcard-${q.qNum}">
        <div class="mock-q-top">
          <span class="mock-q-num"><i class="fa-solid fa-circle-question" style="color:var(--dfs-primary);"></i> Question ${q.qNum}: ${q.title}</span>
          <span class="mock-q-mark">${q.mark} Mark</span>
        </div>
        <div class="mock-q-stem">${q.stem}</div>
        <div class="mock-q-options">
          ${q.options.map((opt, optIdx) => `
            <label class="mock-q-option" id="opt-label-${q.qNum}-${optIdx}" onclick="handleOptionSelect(${q.qNum}, ${optIdx})">
              <input type="radio" name="question_${q.qNum}" value="${optIdx}">
              <span>${opt.text}</span>
            </label>
          `).join("")}
        </div>
        <div class="mock-q-feedback" id="feedback-${q.qNum}">
          <strong><i class="fa-solid fa-graduation-cap"></i> Examiner Rationale:</strong> ${q.explanation}
        </div>
      </div>
    `).join("");
  }

  // Render Section B Tasks
  const secBContainer = document.getElementById("sectionBTasksList");
  if (secBContainer) {
    secBContainer.innerHTML = set.tasks.map((task) => `
      <div class="mock-task-card" id="task-${task.id}">
        <div class="mock-task-card-header">
          <div class="mock-task-title">
            <div class="mock-task-icon"><i class="fa-solid fa-laptop-code"></i></div>
            <div>
              <h3>${task.letter}: ${task.title}</h3>
              <span>Pearson Practical Assessment • ${task.marks} Marks Available</span>
            </div>
          </div>
          <span class="mock-marks-badge">${task.marks} Marks</span>
        </div>

        <div style="background:#f1f5f9; padding:14px 18px; border-radius:10px; margin-bottom:18px; border-left:4px solid var(--dfs-primary);">
          <strong style="color:var(--navy-dark);"><i class="fa-solid fa-circle-info"></i> Scenario & Brief:</strong> ${task.brief}
        </div>

        <div style="margin-bottom:18px;">
          <h4 style="margin:0 0 10px 0; font-size:1.05rem; color:var(--navy-dark);"><i class="fa-solid fa-list-check"></i> Candidate Instructions:</h4>
          <ol style="margin:0; padding-left:22px; line-height:1.7; color:var(--dfs-text-main);">
            ${task.instructions.map(inst => `<li>${inst}</li>`).join("")}
          </ol>
        </div>

        <!-- Interactive Task Simulator Area -->
        ${renderSimulatorForTask(task)}

        <!-- Examiner Marking Checklist & Self-Assessment Rubric -->
        <div class="mock-rubric-box">
          <div class="mock-rubric-title">
            <span><i class="fa-solid fa-clipboard-check" style="color:var(--dfs-success);"></i> Pearson Examiner Marking Criteria & Rubric:</span>
            <span style="font-size:0.85rem; color:var(--dfs-text-muted);">Check off completed criteria</span>
          </div>
          <div class="mock-rubric-list">
            ${task.rubric.map(item => `
              <label class="mock-rubric-item">
                <input type="checkbox" onchange="toggleRubricMark('${item.code}', this.checked)" data-code="${item.code}">
                <span class="mock-rubric-label"><strong>[${item.code}]</strong> ${item.desc}</span>
                <span class="mock-rubric-mark">${item.mark} Mark</span>
              </label>
            `).join("")}
          </div>
        </div>
      </div>
    `).join("");
  }
}

function renderSimulatorForTask(task) {
  if (task.type === "search_email") {
    return `
      <div class="sim-container">
        <div class="sim-top-bar">
          <span class="sim-dot red"></span><span class="sim-dot yellow"></span><span class="sim-dot green"></span>
          <span style="margin-left:10px;"><i class="fa-solid fa-globe"></i> Simulated Workplace Browser & Email Client</span>
        </div>
        <div class="sim-body">
          <div style="font-weight:700; margin-bottom:8px; font-size:0.95rem; color:var(--navy-dark);"><i class="fa-solid fa-magnifying-glass"></i> Task Step 1: Internet Search Engine Simulation</div>
          <div class="sim-search-bar">
            <input type="text" id="simSearchInput_${task.id}" class="sim-search-input" placeholder="Type search keywords here (e.g. ${task.searchAnswer})...">
            <button type="button" class="sim-search-btn" onclick="executeSimSearch('${task.id}')"><i class="fa-solid fa-magnifying-glass"></i> Search</button>
          </div>
          <div class="sim-search-results" id="simSearchResults_${task.id}">
            <div class="sim-result-item">
              <div class="sim-result-url">https://www.official-records.gov.uk/directory</div>
              <div class="sim-result-title">${task.searchAnswer}</div>
              <div class="sim-result-desc">${task.searchResultSnippet}</div>
            </div>
            <div style="background:#eff6ff; padding:8px 12px; border-radius:6px; font-size:0.85rem; color:#1e40af;">
              <i class="fa-solid fa-circle-check"></i> <strong>Search criteria matched!</strong> Highlight and copy the required details into your email below.
            </div>
          </div>

          <div style="font-weight:700; margin:20px 0 8px 0; font-size:0.95rem; color:var(--navy-dark);"><i class="fa-solid fa-envelope"></i> Task Step 2: Professional Email Composer</div>
          <div class="sim-email-client">
            <div class="sim-email-field">
              <label>To:</label>
              <input type="email" placeholder="recipient@example.com" id="simEmailTo_${task.id}">
            </div>
            <div class="sim-email-field">
              <label>Subject:</label>
              <input type="text" placeholder="Enter concise, descriptive subject line..." id="simEmailSub_${task.id}">
            </div>
            <div class="sim-email-body">
              <textarea placeholder="Compose your email here including polite greeting, required information, and closing sign-off..." id="simEmailBody_${task.id}"></textarea>
            </div>
            <div style="background:#f8fafc; padding:10px 14px; border-top:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.85rem; color:#64748b;"><i class="fa-solid fa-signature"></i> Auto-Signature: Kind regards, [Candidate Name]</span>
              <button type="button" class="btn-timer-action" style="background:var(--dfs-primary); border:none; padding:8px 16px;" onclick="validateSimEmail('${task.id}')">
                <i class="fa-solid fa-paper-plane"></i> Send & Verify Email
              </button>
            </div>
          </div>
          <div id="simEmailFeedback_${task.id}" style="margin-top:10px; display:none; padding:10px; border-radius:8px;"></div>
        </div>
      </div>
    `;
  } else if (task.type === "flyer_design" || task.type === "document_design") {
    return `
      <div class="sim-container">
        <div class="sim-top-bar">
          <span class="sim-dot red"></span><span class="sim-dot yellow"></span><span class="sim-dot green"></span>
          <span style="margin-left:10px;"><i class="fa-solid fa-file-word"></i> Simulated Word Processing & Document Layout Inspector</span>
        </div>
        <div class="sim-body">
          <p style="margin-top:0; font-size:0.9rem; color:var(--dfs-text-muted);">
            Test and verify your flyer layout parameters below, or format the downloaded document in Microsoft Word:
          </p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:4px;">Page Orientation:</label>
              <select id="simDocOrient_${task.id}" class="sim-search-input" style="width:100%;">
                <option value="portrait">Portrait</option>
                <option value="landscape" selected>Landscape (Required)</option>
              </select>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:4px;">Image Height & Cropping:</label>
              <select id="simDocImg_${task.id}" class="sim-search-input" style="width:100%;">
                <option value="original">Original Uncropped</option>
                <option value="6cm" selected>6.0 cm Height (Proportional Cropped)</option>
                <option value="distorted">Distorted / Stretched</option>
              </select>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:4px;">Table Header Shading:</label>
              <select id="simDocTable_${task.id}" class="sim-search-input" style="width:100%;">
                <option value="none">No Shading (Plain)</option>
                <option value="shaded" selected>Shaded Header Row</option>
              </select>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:10px;">
              <label style="display:block; font-size:0.8rem; font-weight:700; color:#334155; margin-bottom:4px;">Decorative Outer Border:</label>
              <select id="simDocBorder_${task.id}" class="sim-search-input" style="width:100%;">
                <option value="none">None</option>
                <option value="border" selected>1.5 pt Page Border</option>
              </select>
            </div>
          </div>
          <button type="button" class="sim-search-btn" onclick="validateFlyerSim('${task.id}')">
            <i class="fa-solid fa-wand-magic-sparkles"></i> Verify Document Formatting Criteria
          </button>
          <div id="simFlyerFeedback_${task.id}" style="margin-top:14px; display:none; padding:12px; border-radius:8px;"></div>
        </div>
      </div>
    `;
  } else if (task.type === "spreadsheet") {
    return `
      <div class="sim-container">
        <div class="sim-top-bar">
          <span class="sim-dot red"></span><span class="sim-dot yellow"></span><span class="sim-dot green"></span>
          <span style="margin-left:10px;"><i class="fa-solid fa-table"></i> Interactive Spreadsheet Formula Tester</span>
        </div>
        <div class="sim-body">
          <p style="margin-top:0; font-size:0.9rem; color:var(--dfs-text-muted);">
            Test formulas here or complete the downloaded spreadsheet in Excel / Google Sheets:
          </p>
          <div style="display:flex; gap:10px; margin-bottom:14px; flex-wrap:wrap;">
            <input type="text" id="simFormulaInput_${task.id}" class="sim-search-input" placeholder="e.g. =SUM(C4:F4) or =AVERAGE(B4:E4)" style="flex:1;">
            <button type="button" class="sim-search-btn" onclick="evaluateSimFormula('${task.id}')"><i class="fa-solid fa-calculator"></i> Calculate Formula</button>
          </div>
          <div id="simFormulaResult_${task.id}" style="margin-bottom:14px; font-weight:700; display:none; padding:10px 14px; border-radius:8px;"></div>

          <div class="sim-sheet-table-wrap">
            <table class="sim-sheet-table">
              <thead>
                <tr>
                  <th style="width:40px;"></th>
                  <th>A</th>
                  <th>B</th>
                  <th>C</th>
                  <th>D</th>
                  <th>E</th>
                  <th>F</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th>1</th>
                  <td colspan="6" class="header-green" style="text-align:center; font-weight:800; font-size:1.1rem;">EXPENDITURE / SALES OVERVIEW</td>
                </tr>
                <tr>
                  <th>2</th>
                  <td style="font-weight:700;">Item Name</td>
                  <td style="font-weight:700;" class="cell-num">Q1</td>
                  <td style="font-weight:700;" class="cell-num">Q2</td>
                  <td style="font-weight:700;" class="cell-num">Q3</td>
                  <td style="font-weight:700;" class="cell-num">Q4</td>
                  <td style="font-weight:700;" class="cell-num">Summary Total</td>
                </tr>
                <tr>
                  <th>3</th>
                  <td>Primary Category 1</td>
                  <td class="cell-num">£412.00</td>
                  <td class="cell-num">£450.00</td>
                  <td class="cell-num">£510.00</td>
                  <td class="cell-num">£480.00</td>
                  <td class="cell-num" style="background:#eff6ff; font-weight:700;">=SUM(B3:E3)</td>
                </tr>
                <tr>
                  <th>4</th>
                  <td>Primary Category 2</td>
                  <td class="cell-num">£280.00</td>
                  <td class="cell-num">£310.00</td>
                  <td class="cell-num">£295.00</td>
                  <td class="cell-num">£330.00</td>
                  <td class="cell-num" style="background:#eff6ff; font-weight:700;">=SUM(B4:E4)</td>
                </tr>
                <tr>
                  <th>5</th>
                  <td style="font-weight:700;">Quarterly Average</td>
                  <td class="cell-num" style="background:#fef3c7; font-weight:700;">=AVERAGE(B3:B4)</td>
                  <td class="cell-num" style="background:#fef3c7; font-weight:700;">=AVERAGE(C3:C4)</td>
                  <td class="cell-num" style="background:#fef3c7; font-weight:700;">=AVERAGE(D3:D4)</td>
                  <td class="cell-num" style="background:#fef3c7; font-weight:700;">=AVERAGE(E3:E4)</td>
                  <td class="cell-num" style="background:#dcfce7; font-weight:800;">£1,533.50</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    `;
  } else if (task.type === "web_form") {
    return `
      <div class="sim-container">
        <div class="sim-top-bar">
          <span class="sim-dot red"></span><span class="sim-dot yellow"></span><span class="sim-dot green"></span>
          <span style="margin-left:10px;"><i class="fa-solid fa-window-maximize"></i> Simulated Online Portal & Web Form Submission</span>
        </div>
        <div class="sim-body">
          <form onsubmit="handleSimFormSubmit(event, '${task.id}')" style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Reference / Account Number:</label>
              <input type="text" required placeholder="e.g. R753197" class="sim-search-input" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Full Name / Contact Person:</label>
              <input type="text" required placeholder="Full Name" class="sim-search-input" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Postcode:</label>
              <input type="text" required placeholder="e.g. NT25 3BG or LW7 1PJ" class="sim-search-input" style="width:100%;">
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Telephone:</label>
              <input type="tel" required placeholder="01632 960..." class="sim-search-input" style="width:100%;">
            </div>
            <div style="grid-column: span 2;">
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Verification Reading / Numeric Value:</label>
              <input type="text" required placeholder="Enter meter reading or registration token..." class="sim-search-input" style="width:100%;">
            </div>
            <div style="grid-column: span 2;">
              <label style="display:block; font-size:0.85rem; font-weight:700; margin-bottom:4px;">Upload Supporting File / Photograph:</label>
              <input type="file" class="sim-search-input" style="width:100%; padding:6px;">
            </div>
            <div style="grid-column: span 2;">
              <button type="submit" class="sim-search-btn" style="width:100%; justify-content:center;">
                <i class="fa-solid fa-cloud-arrow-up"></i> Submit Online Form & Verify Evidence
              </button>
            </div>
          </form>
          <div id="simFormFeedback_${task.id}" style="margin-top:14px; display:none; padding:12px; border-radius:8px;"></div>
        </div>
      </div>
    `;
  } else if (task.type === "file_mgmt") {
    return `
      <div class="sim-container">
        <div class="sim-top-bar">
          <span class="sim-dot red"></span><span class="sim-dot yellow"></span><span class="sim-dot green"></span>
          <span style="margin-left:10px;"><i class="fa-solid fa-folder-tree"></i> Simulated File Directory Explorer</span>
        </div>
        <div class="sim-body">
          <div style="display:flex; gap:10px; margin-bottom:14px; flex-wrap:wrap;">
            <input type="text" id="simFolderName_${task.id}" class="sim-search-input" placeholder="Type new folder name (e.g. Devices or PROBLEM)..." style="flex:1;">
            <button type="button" class="sim-search-btn" onclick="addSimFolder('${task.id}')"><i class="fa-solid fa-folder-plus"></i> Create Folder</button>
          </div>
          <div id="simFolderTree_${task.id}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:16px; font-family:'JetBrains Mono',monospace; font-size:0.9rem;">
            <div><i class="fa-solid fa-hard-drive" style="color:var(--dfs-primary);"></i> C:\\Candidate_Workspace\\</div>
            <div id="simFolderList_${task.id}" style="padding-left:24px; color:#475569;">
              <div>└── (Create required folder hierarchy above)</div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  return "";
}

function handleOptionSelect(qNum, optIdx) {
  userAnswers[qNum] = optIdx;
  const currentSet = DFS_MOCK_DATA[currentSetKey];
  const question = currentSet.sectionA.find(q => q.qNum === qNum);
  if (!question) return;

  const card = document.getElementById(`qcard-${qNum}`);
  const feedback = document.getElementById(`feedback-${qNum}`);

  // Clear previous option styles
  question.options.forEach((_, idx) => {
    const label = document.getElementById(`opt-label-${qNum}-${idx}`);
    if (label) {
      label.classList.remove("selected", "correct-option", "wrong-option");
    }
  });

  const selectedLabel = document.getElementById(`opt-label-${qNum}-${optIdx}`);
  if (selectedLabel) selectedLabel.classList.add("selected");

  // In practice mode, provide instant feedback
  if (examMode === "practice") {
    const isCorrect = question.options[optIdx].isCorrect;
    if (card) {
      card.classList.toggle("is-correct", isCorrect);
      card.classList.toggle("is-incorrect", !isCorrect);
    }
    if (selectedLabel) {
      selectedLabel.classList.add(isCorrect ? "correct-option" : "wrong-option");
    }
    if (feedback) {
      feedback.className = `mock-q-feedback show ${isCorrect ? "correct" : "incorrect"}`;
    }
  }
}

function toggleRubricMark(code, isChecked) {
  rubricChecked[code] = isChecked;
  updateScorePreview();
}

function updateScorePreview() {
  // Can display live score counter
}

// Timer Functions
function startTimer() {
  if (isTimerRunning) return;
  isTimerRunning = true;
  document.getElementById("btnTimerToggle").innerHTML = '<i class="fa-solid fa-pause"></i> Pause';

  timerInterval = setInterval(() => {
    if (secondsRemaining > 0) {
      secondsRemaining--;
      updateTimerDisplay();
    } else {
      pauseTimer();
      alert("Time is up! Please submit your exam to view your final marked results.");
    }
  }, 1000);
}

function pauseTimer() {
  isTimerRunning = false;
  clearInterval(timerInterval);
  const btn = document.getElementById("btnTimerToggle");
  if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i> Start';
}

function toggleTimer() {
  if (isTimerRunning) {
    pauseTimer();
  } else {
    startTimer();
  }
}

function resetTimer() {
  pauseTimer();
  const set = DFS_MOCK_DATA[currentSetKey];
  secondsRemaining = (set ? set.durationMinutes : 90) * 60;
  updateTimerDisplay();
}

function updateTimerDisplay() {
  const mins = Math.floor(secondsRemaining / 60);
  const secs = secondsRemaining % 60;
  const display = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  const el = document.getElementById("mockTimerDisplay");
  const box = document.getElementById("mockTimerBox");
  if (el) el.textContent = display;
  if (box) {
    box.classList.toggle("warning", secondsRemaining <= 300); // 5 mins warning
  }
}

// Simulators
function executeSimSearch(taskId) {
  const input = document.getElementById(`simSearchInput_${taskId}`);
  const results = document.getElementById(`simSearchResults_${taskId}`);
  if (!input || !results) return;

  if (input.value.trim().length > 2) {
    results.classList.add("active");
  } else {
    alert("Please enter a valid search term (e.g. food standards agency or awards venue).");
  }
}

function validateFlyerSim(taskId) {
  const orient = document.getElementById(`simDocOrient_${taskId}`)?.value;
  const img = document.getElementById(`simDocImg_${taskId}`)?.value;
  const table = document.getElementById(`simDocTable_${taskId}`)?.value;
  const border = document.getElementById(`simDocBorder_${taskId}`)?.value;
  const fb = document.getElementById(`simFlyerFeedback_${taskId}`);
  if (!fb) return;

  fb.style.display = "block";
  if (orient === "landscape" && img === "6cm" && table === "shaded" && border === "border") {
    fb.style.background = "#dcfce7";
    fb.style.color = "#15803d";
    fb.innerHTML = '<i class="fa-solid fa-circle-check"></i> <strong>All formatting criteria matched!</strong> Landscape orientation, proportional 6cm cropped image, contrasting table header shading, and outer page border verified.';
  } else {
    fb.style.background = "#fee2e2";
    fb.style.color = "#b91c1c";
    fb.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> <strong>Check layout parameters:</strong> Ensure Landscape orientation, 6 cm cropped image, shaded header row, and page border are all selected.';
  }
}

function validateSimEmail(taskId) {
  const to = document.getElementById(`simEmailTo_${taskId}`);
  const sub = document.getElementById(`simEmailSub_${taskId}`);
  const body = document.getElementById(`simEmailBody_${taskId}`);
  const fb = document.getElementById(`simEmailFeedback_${taskId}`);

  if (!to || !sub || !body || !fb) return;

  const toVal = to.value.trim().toLowerCase();
  const subVal = sub.value.trim().toLowerCase();
  const bodyVal = body.value.trim();

  let errors = [];
  if (!toVal.includes("@") || !toVal.includes(".")) {
    errors.push("Check recipient email address - must be a valid Pearson test address.");
  }
  if (subVal.length < 3) {
    errors.push("Subject line is missing or too short.");
  }
  if (bodyVal.length < 15) {
    errors.push("Email message body requires greeting, address/evidence, and closing.");
  }

  fb.style.display = "block";
  if (errors.length === 0) {
    fb.style.background = "#dcfce7";
    fb.style.color = "#15803d";
    fb.innerHTML = '<i class="fa-solid fa-circle-check"></i> <strong>Email verified!</strong> All criteria satisfied (Correct recipient, clear subject, and professional message body).';
  } else {
    fb.style.background = "#fee2e2";
    fb.style.color = "#b91c1c";
    fb.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Review criteria:</strong><br>${errors.join("<br>")}`;
  }
}

function evaluateSimFormula(taskId) {
  const input = document.getElementById(`simFormulaInput_${taskId}`);
  const res = document.getElementById(`simFormulaResult_${taskId}`);
  if (!input || !res) return;

  const val = input.value.trim().toUpperCase();
  res.style.display = "block";

  if (val.includes("SUM") || val.includes("AVERAGE")) {
    res.style.background = "#dcfce7";
    res.style.color = "#15803d";
    res.innerHTML = `<i class="fa-solid fa-circle-check"></i> Valid Pearson standard formula: <code>${val}</code> (Award mark for correct function syntax and cell ranges).`;
  } else {
    res.style.background = "#fef3c7";
    res.style.color = "#92400e";
    res.innerHTML = `<i class="fa-solid fa-circle-info"></i> Formula entered: <code>${val}</code>. Remember Pearson mark schemes award marks specifically for <code>=SUM()</code> and <code>=AVERAGE()</code> functions.`;
  }
}

function handleSimFormSubmit(e, taskId) {
  e.preventDefault();
  const fb = document.getElementById(`simFormFeedback_${taskId}`);
  if (fb) {
    fb.style.display = "block";
    fb.style.background = "#dcfce7";
    fb.style.color = "#15803d";
    fb.innerHTML = '<i class="fa-solid fa-circle-check"></i> <strong>Form submission successful!</strong> Data verified and evidence token logged for Pearson assessor review.';
  }
}

let simulatedFolders = [];
function addSimFolder(taskId) {
  const input = document.getElementById(`simFolderName_${taskId}`);
  const list = document.getElementById(`simFolderList_${taskId}`);
  if (!input || !list) return;

  const name = input.value.trim();
  if (name.length > 0) {
    simulatedFolders.push(name);
    input.value = "";
    list.innerHTML = simulatedFolders.map((f, i) => `
      <div style="margin-top:4px;">├── <i class="fa-solid fa-folder" style="color:#d97706;"></i> ${f}</div>
    `).join("");
  }
}

// Final Submit & Results Modal
function submitExam() {
  pauseTimer();
  const set = DFS_MOCK_DATA[currentSetKey];

  // Grade Section A
  let secAScore = 0;
  set.sectionA.forEach(q => {
    const selectedIdx = userAnswers[q.qNum];
    if (selectedIdx !== undefined && q.options[selectedIdx].isCorrect) {
      secAScore += q.mark;
    }
  });

  // Grade Section B (Rubric Checkboxes)
  let secBScore = 0;
  let totalRubricMarks = 0;
  set.tasks.forEach(t => {
    t.rubric.forEach(r => {
      totalRubricMarks += r.mark;
      if (rubricChecked[r.code]) {
        secBScore += r.mark;
      }
    });
  });

  const totalScore = secAScore + secBScore;
  const isPass = totalScore >= set.passMark;
  const pct = Math.round((totalScore / set.totalMarks) * 100);

  // Render Modal Results
  const modalContent = document.getElementById("resultsModalBody");
  if (modalContent) {
    modalContent.innerHTML = `
      <div class="results-badge-wrap">
        <span class="results-badge ${isPass ? "pass" : "fail"}">
          <i class="fa-solid ${isPass ? "fa-circle-check" : "fa-triangle-exclamation"}"></i> ${isPass ? "PASSED MOCK EXAM" : "DID NOT PASS - REVISION NEEDED"}
        </span>
      </div>

      <h2 style="text-align:center; margin:0 0 6px 0; color:var(--navy-dark);">${set.name}</h2>
      <p style="text-align:center; color:#64748b; margin-top:0;">Pearson Edexcel Digital Functional Skills Assessment Standard</p>

      <div class="score-display-box">
        <div class="score-stat-card">
          <div class="score-stat-num" style="color:var(--dfs-primary);">${secAScore} / 10</div>
          <div class="score-stat-label">Section A Knowledge</div>
        </div>
        <div class="score-stat-card">
          <div class="score-stat-num" style="color:var(--dfs-success);">${secBScore} / ${set.totalMarks - 10}</div>
          <div class="score-stat-label">Section B Practical</div>
        </div>
        <div class="score-stat-card">
          <div class="score-stat-num" style="color:${isPass ? "var(--dfs-success)" : "var(--dfs-danger)"};">${totalScore} / ${set.totalMarks}</div>
          <div class="score-stat-label">Overall Score (${pct}%)</div>
        </div>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:18px; margin:20px 0;">
        <h4 style="margin:0 0 10px 0; color:var(--navy-dark);"><i class="fa-solid fa-chart-pie"></i> Diagnostic Assessment Breakdown:</h4>
        <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
          <span>Pass Mark Benchmark:</span>
          <strong>${set.passMark} / ${set.totalMarks} Marks (~65%)</strong>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.9rem;">
          <span>Your Total Mark:</span>
          <strong style="color:${isPass ? "#16a34a" : "#dc2626"};">${totalScore} Marks</strong>
        </div>
        <div style="display:flex; justify-content:space-between; font-size:0.9rem;">
          <span>Result Status:</span>
          <strong>${isPass ? "Exceeds standard threshold" : "Below threshold - review wrong answers"}</strong>
        </div>
      </div>

      <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-top:24px;">
        <button type="button" class="btn-hero-action" onclick="closeResultsModal()"><i class="fa-solid fa-rotate-left"></i> Review Exam Answers</button>
        <button type="button" class="btn-card-action" onclick="window.print()"><i class="fa-solid fa-print"></i> Print Result Summary</button>
      </div>
    `;
  }

  // Reveal all feedback in the main UI so candidate can review
  document.querySelectorAll(".mock-q-feedback").forEach(el => el.classList.add("show"));
  document.getElementById("resultsModal").classList.add("active");
}

function closeResultsModal() {
  document.getElementById("resultsModal").classList.remove("active");
}

function setupEventListeners() {
  // Set tabs
  document.querySelectorAll(".btn-set-tab").forEach(tab => {
    tab.addEventListener("click", () => selectMockSet(tab.dataset.set));
  });

  // Mode tabs
  document.querySelectorAll(".btn-mode-tab").forEach(tab => {
    tab.addEventListener("click", () => setExamMode(tab.dataset.mode));
  });
}
