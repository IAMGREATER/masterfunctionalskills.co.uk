#!/usr/bin/env python3
"""Area 1: Using Devices and Handling Information (Cards 1-10)"""
import xml.etree.ElementTree as ET
CARDS = [ { 'answer_text': 'A screen reader (or text-to-speech / Narrator).',
    'challenge_prompt': 'Which accessibility feature allows a user with visual '
                        'impairment to hear text read aloud from the screen?',
    'dfe_code': 'DFS 1.1',
    'golden_rule': 'Accessibility features ensure digital inclusion for all '
                   'users!',
    'id': 'dfs-01',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 1,
    'rule_body': 'Accessibility settings assist users with physical or '
                 'cognitive impairments: High Contrast Mode (visual clarity), '
                 'Text Scaling / Magnifier (enlarging text), Screen Reader '
                 '(Narrator), Sticky Keys (motor support).',
    'rule_heading': 'Tailoring Your Device',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#9a3412" '
                'text-anchor="middle">ACCESSIBILITY SETTINGS</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="700" fill="#0f172a">• High Contrast &amp; Dark '
                'Mode (Low vision)</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="700" fill="#0f172a">• Screen Magnifier / Zoom '
                '(Large font scaling)</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="700" fill="#0f172a">• Screen Reader / '
                'Text-to-Speech (Dyslexia &amp; blind)</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'OS Settings &amp; Accessibility',
    'watch_out': "Don't confuse display brightness with high-contrast "
                 'accessibility themes.'},
  { 'answer_text': 'Staff_Training_Plan_Oct2024_v2.docx.',
    'challenge_prompt': 'Suggest a professional filename for the second draft '
                        'of a staff training plan written in October 2024.',
    'dfe_code': 'DFS 1.2',
    'golden_rule': 'Include the date (YYYY-MM-DD) and version number (v1, v2) '
                   'in filename!',
    'id': 'dfs-02',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 2,
    'rule_body': 'Organise files into logical tree hierarchies: Root Folder → '
                 'Subfolder → Specific file. Meaningful naming convention: '
                 'Topic_Project_Date_Version (e.g. Budget_Q3_2024_v2.xlsx). '
                 "Avoid 'Doc1.docx'.",
    'rule_heading': 'Hierarchical Folders &amp; Version Control',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="25" y="26" font-size="11" '
                'font-weight="800" fill="#0f172a">📁 Documents (Root '
                'Folder)</text>\n'
                '            <text x="45" y="52" font-size="10.5" '
                'font-weight="700" fill="#2563eb">└── 📁 Oxford_Health_Project '
                '(Subfolder)</text>\n'
                '            <text x="70" y="76" font-size="10" '
                'font-weight="700" fill="#475569">├── 📄 '
                'Meeting_Notes_12Oct24.docx</text>\n'
                '            <text x="70" y="98" font-size="10" '
                'font-weight="700" fill="#475569">└── 📊 '
                'Financial_Forecast_v3.xlsx</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'File Management &amp; Naming',
    'watch_out': 'Avoid saving everything to your Desktop — it causes system '
                 'clutter and data loss risk.'},
  { 'answer_text': 'PDF (.pdf - Portable Document Format).',
    'challenge_prompt': 'Which file format should you choose to ensure a '
                        'formal report cannot be accidentally altered by the '
                        'recipient?',
    'dfe_code': 'DFS 1.3',
    'golden_rule': 'Export to PDF before sharing to keep layout and formatting intact!',
    'id': 'dfs-03',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 3,
    'rule_body': '.docx = Word processing. .pdf = Portable read-only document '
                 '(universal). .xlsx / .csv = Spreadsheets / raw '
                 'comma-separated data. .pptx = Slideshow. .png / .jpg = '
                 'Images. .mp4 = Video. .zip = Compressed folder.',
    'rule_heading': 'Recognising Common File Types',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="190" y="26" font-size="12" '
                'font-weight="900" fill="#0f172a" text-anchor="middle">FILE '
                'FORMAT QUICK REFERENCE</text>\n'
                '            <text x="25" y="55" font-size="11" '
                'font-weight="800" fill="#2563eb">• .docx: Editable text '
                'document (Word)</text>\n'
                '            <text x="25" y="78" font-size="11" '
                'font-weight="800" fill="#dc2626">• .pdf: Fixed layout, '
                'non-editable reader format</text>\n'
                '            <text x="25" y="101" font-size="11" '
                'font-weight="800" fill="#16a34a">• .xlsx / .csv: Financial '
                'spreadsheets &amp; data tables</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'File Extensions &amp; Formats',
    'watch_out': 'A .csv file saves raw data only — all formulas and styling are lost.'},
  { 'answer_text': '1. Files are backed up remotely if the physical device is '
                   'lost/damaged. 2. Documents can be accessed from any '
                   'location or device with internet.',
    'challenge_prompt': 'State two benefits of saving business documents to '
                        'cloud storage rather than a local USB flash drive.',
    'dfe_code': 'DFS 1.4',
    'golden_rule': 'Cloud files protect you against hardware crashes, fires, '
                   'or stolen laptops!',
    'id': 'dfs-04',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 4,
    'rule_body': 'Cloud storage (OneDrive, Google Drive, iCloud) stores files '
                 'on secure remote servers over the Internet. Benefits: '
                 'Automatic backup, access from any device, easy real-time '
                 'collaboration. Requires internet connectivity.',
    'rule_heading': 'Remote Servers &amp; Multi-Device Access',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#1e40af" text-anchor="middle">CLOUD '
                'STORAGE ADVANTAGES</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="700" fill="#0f172a">✓ Access files from phone, '
                'tablet, and PC</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="700" fill="#0f172a">✓ Automatic real-time '
                'off-site backup</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#059669">✓ Multiple people can edit '
                'simultaneously</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Cloud Storage &amp; Syncing',
    'watch_out': "If you don't enable 'Keep on this device' (offline mode), "
                 'you cannot open cloud files without Wi-Fi.'},
  { 'answer_text': '"NHS dental fees" -private (or site:nhs.uk "dental fees").',
    'challenge_prompt': 'What search query would you type to find exact '
                        'information on NHS dental fees while excluding '
                        'private dentists?',
    'dfe_code': 'DFS 1.5',
    'golden_rule': 'Use quotation marks to search for exact multi-word terms!',
    'id': 'dfs-05',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 5,
    'rule_body': 'Quotation Marks ("..."): Searches for the EXACT phrase in '
                 'that precise order. Minus Sign (-word): Excludes unwanted '
                 'results. site:gov.uk: Restricts search to official '
                 'government websites.',
    'rule_heading': 'Boolean &amp; Precision Search Tricks',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="190" y="26" font-size="12" '
                'font-weight="900" fill="#0f172a" '
                'text-anchor="middle">ADVANCED SEARCH OPERATORS</text>\n'
                '            <text x="25" y="55" font-size="11" '
                'font-weight="800" fill="#2563eb">"functional skills maths" → '
                'Exact phrase only</text>\n'
                '            <text x="25" y="80" font-size="11" '
                'font-weight="800" fill="#dc2626">jaguar speed -car → Excludes '
                'automobile results</text>\n'
                '            <text x="25" y="105" font-size="11" '
                'font-weight="800" fill="#16a34a">site:gov.uk apprenticeship → '
                'Official sites only</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Search Engine Operators',
    'watch_out': "Don't put a space after the minus sign (type '-car', NOT '- "
                 "car')."},
  { 'answer_text': '.gov.uk is the official UK government portal, whereas .com '
                   'sites are commercial agencies that often charge extra '
                   'fees.',
    'challenge_prompt': 'Why is information found on a .gov.uk website '
                        'generally more reliable than a .com website for '
                        'renewing a passport?',
    'dfe_code': 'DFS 1.6',
    'golden_rule': 'Cross-check web information across at least two trusted sources!',
    'id': 'dfs-06',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 6,
    'rule_body': 'Top-level domains: .gov.uk = Official UK government. .ac.uk '
                 '= Universities. .org = Non-profit organisations. .com / '
                 ".co.uk = Commercial businesses. Look out for 'Sponsored / "
                 "Ad' tags at top of search results.",
    'rule_heading': 'Domains &amp; Sponsored Ads',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#1e40af" '
                'text-anchor="middle">CHECKING WEBSITE RELIABILITY</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="800" fill="#16a34a">.gov.uk &amp; .nhs.uk: '
                'Highly authoritative</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="700" fill="#0f172a">.ac.uk: Academic university '
                'research</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#dc2626">Sponsored / Ad tags: '
                'Commercial promotion</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Evaluating Online Information',
    'watch_out': 'Watch for lookalike URLs and typosquatting domains (e.g. paypa1.com).'},
  { 'answer_text': '1. Delete unused apps or clear app caches. 2. Back up '
                   'photos/videos to cloud storage or delete large video '
                   'files.',
    'challenge_prompt': 'State two actions you can take if your smartphone '
                        "displays a 'Storage Full' warning.",
    'dfe_code': 'DFS 1.7',
    'golden_rule': 'Empty your Recycle Bin / Trash to permanently reclaim disk '
                   'storage!',
    'id': 'dfs-07',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 7,
    'rule_body': 'Storage (GB/TB): Permanent memory holding files and apps '
                 'when PC is turned off. RAM (Random Access Memory): Temporary '
                 'working memory used while apps are open. Free up storage by '
                 'deleting temp files and emptying Recycle Bin.',
    'rule_heading': 'Storage (SSD/Hard Drive) vs RAM',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#1e40af" text-anchor="middle">STORAGE '
                '(SSD/HDD)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Permanent file '
                'storage</text>\n'
                '            <text x="15" y="78" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• 256 GB / 1 TB</text>\n'
                '            <text x="15" y="101" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Survives restarts</text>\n'
                '          </g>\n'
                '          <g transform="translate(240, 20)">\n'
                '            <rect x="0" y="0" width="180" height="125" rx="8" '
                'fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>\n'
                '            <text x="90" y="24" font-size="12" '
                'font-weight="800" fill="#15803d" text-anchor="middle">MEMORY '
                '(RAM)</text>\n'
                '            <text x="15" y="55" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Active app '
                'workspace</text>\n'
                '            <text x="15" y="78" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• 8 GB / 16 GB</text>\n'
                '            <text x="15" y="101" font-size="10.5" '
                'font-weight="700" fill="#0f172a">• Clears on restart</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Device Storage vs RAM',
    'watch_out': 'Running out of RAM makes your computer freeze; running out '
                 'of Storage prevents saving new files.'},
  { 'answer_text': 'Zipping reduces the overall file size to fit within email '
                   'attachment limits and bundles all images into one file.',
    'challenge_prompt': 'Why is it beneficial to zip five large image files '
                        'before sending them by email?',
    'dfe_code': 'DFS 1.8',
    'golden_rule': 'You must EXTRACT files before you can properly edit and '
                   'save them!',
    'id': 'dfs-08',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 8,
    'rule_body': 'Compress (Zip): Shrinks file size and bundles multiple '
                 'documents into one single .zip folder for emailing. Extract: '
                 'Unpacks the zipped files into normal editable documents.',
    'rule_heading': 'Reducing File Size for Email',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#0f172a" text-anchor="middle">ZIPPING '
                '&amp; EXTRACTING FILES</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="800" fill="#2563eb">Compress: Right-click → '
                "'Send to compressed folder'</text>\n"
                '            <text x="30" y="80" font-size="11" '
                'font-weight="700" fill="#475569">Combines 10 files into 1 '
                'small .zip attachment</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#059669">Extract: Right-click .zip → '
                "'Extract All...' to view</text>\n"
                '          </g>\n'
                '</svg>',
    'title': 'Compressing &amp; Extracting (.zip)',
    'watch_out': 'If you edit files directly inside an unextracted zip, '
                 'changes may be lost.'},
  { 'answer_text': 'Ctrl + Shift + Esc (or Ctrl + Alt + Delete).',
    'challenge_prompt': 'What keyboard shortcut opens Windows Task Manager '
                        'directly to close a frozen program?',
    'dfe_code': 'DFS 1.9',
    'golden_rule': 'Restarting clears memory caches — try it first before calling support!',
    'id': 'dfs-09',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 9,
    'rule_body': 'App frozen: Open Task Manager (Ctrl + Shift + Esc) and '
                 "select 'End Task'. Wi-Fi dropped: Check flight mode, restart "
                 'router, toggle Wi-Fi off and on. Total system freeze: Hold '
                 'power button for 10 seconds to reboot.',
    'rule_heading': 'First Steps When Tech Fails',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(40, 20)">\n'
                '            <rect x="0" y="0" width="380" height="130" rx="8" '
                'fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>\n'
                '            <text x="190" y="26" font-size="12" '
                'font-weight="900" fill="#991b1b" text-anchor="middle">FIRST '
                'RESPONSE TROUBLESHOOTING</text>\n'
                '            <text x="25" y="55" font-size="11" '
                'font-weight="800" fill="#0f172a">1. App Frozen? Press '
                "Ctrl+Shift+Esc → 'End Task'</text>\n"
                '            <text x="25" y="80" font-size="11" '
                'font-weight="800" fill="#0f172a">2. No Internet? Check '
                'Airplane mode &amp; restart Wi-Fi router</text>\n'
                '            <text x="25" y="105" font-size="11" '
                'font-weight="800" fill="#059669">3. The Golden Rule: Restart '
                'the computer before calling IT!</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Basic Troubleshooting',
    'watch_out': 'Never unplug a PC while it is writing data or installing updates.'},
  { 'answer_text': '1. Use strong password protection / encryption. 2. Lock '
                   'your screen whenever stepping away from the device.',
    'challenge_prompt': 'State two ways you can protect sensitive customer '
                        'data on a workplace laptop.',
    'dfe_code': 'DFS 1.10',
    'golden_rule': 'Always lock your computer screen (Win + L) when leaving '
                   'your desk!',
    'id': 'dfs-10',
    'level': 'l2',
    'level_label': 'Level 1 / 2',
    'number': 10,
    'rule_body': 'Personal data relates to an identifiable living person '
                 '(names, NHS numbers, addresses). Under UK GDPR: 1. Process '
                 'lawfully, fairly, and transparently. 2. Keep accurate and '
                 'secure. 3. Delete when no longer required.',
    'rule_heading': 'Handling Personal Data Lawfully',
    'strand_name': 'Devices & Handling',
    'strand_theme': 'orange',
    'subject': 'digital',
    'subject_label': 'Digital Skills',
    'svg_html': '<svg viewBox="0 0 460 170" width="100%" height="170" '
                'xmlns="http://www.w3.org/2000/svg">\n'
                '\n'
                '          <g transform="translate(60, 20)">\n'
                '            <rect x="0" y="0" width="340" height="130" rx="8" '
                'fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>\n'
                '            <text x="170" y="26" font-size="12" '
                'font-weight="900" fill="#15803d" text-anchor="middle">UK GDPR '
                'KEY PRINCIPLES</text>\n'
                '            <text x="30" y="55" font-size="11" '
                'font-weight="700" fill="#0f172a">• Collect only the data that '
                'is strictly necessary</text>\n'
                '            <text x="30" y="80" font-size="11" '
                'font-weight="700" fill="#0f172a">• Keep data secure with '
                'encryption &amp; passwords</text>\n'
                '            <text x="30" y="105" font-size="11" '
                'font-weight="800" fill="#dc2626">• Never share patient/client '
                'records without consent</text>\n'
                '          </g>\n'
                '</svg>',
    'title': 'Data Protection &amp; UK GDPR',
    'watch_out': 'Leaving customer spreadsheets visible on an unattended '
                 'screen is a serious GDPR data breach.'}]
for card in CARDS:
    ET.fromstring(card["svg_html"])
