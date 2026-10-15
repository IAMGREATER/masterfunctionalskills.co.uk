#!/usr/bin/env python3
"""
Complete Builder for Deck 5: Digital Functional Skills (50 Cards)
Covers all 5 National National Standards for DFSQ (Ofqual / Pearson / C&G).
"""
import os
import pprint
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS_1 = [
    # 1. OS Settings & Accessibility
    {
        "id": "dfs-01",
        "number": 1,
        "title": "OS Settings &amp; Accessibility",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.1",
        "rule_heading": "Tailoring Your Device",
        "rule_body": "Accessibility settings assist users with physical or cognitive impairments: High Contrast Mode (visual clarity), Text Scaling / Magnifier (enlarging text), Screen Reader (Narrator), Sticky Keys (motor support).",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#9a3412" text-anchor="middle">ACCESSIBILITY SETTINGS</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">• High Contrast &amp; Dark Mode (Low vision)</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">• Screen Magnifier / Zoom (Large font scaling)</text>
            <text x="30" y="105" font-size="11" font-weight="700" fill="#0f172a">• Screen Reader / Text-to-Speech (Dyslexia &amp; blind)</text>
          </g>"""),
        "golden_rule": "Accessibility features ensure digital inclusion for all users!",
        "watch_out": "Don't confuse display brightness with high-contrast accessibility themes.",
        "challenge_prompt": "Which accessibility feature allows a user with visual impairment to hear text read aloud from the screen?",
        "answer_text": "A screen reader (or text-to-speech / Narrator)."
    },

    # 2. File Management & Hierarchies
    {
        "id": "dfs-02",
        "number": 2,
        "title": "File Management &amp; Naming",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.2",
        "rule_heading": "Hierarchical Folders &amp; Version Control",
        "rule_body": "Organise files into logical tree hierarchies: Root Folder → Subfolder → Specific file. Meaningful naming convention: Topic_Project_Date_Version (e.g. Budget_Q3_2024_v2.xlsx). Avoid 'Doc1.docx'.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="25" y="26" font-size="11" font-weight="800" fill="#0f172a">📁 Documents (Root Folder)</text>
            <text x="45" y="52" font-size="10.5" font-weight="700" fill="#2563eb">└── 📁 Oxford_Health_Project (Subfolder)</text>
            <text x="70" y="76" font-size="10" font-weight="700" fill="#475569">├── 📄 Meeting_Notes_12Oct24.docx</text>
            <text x="70" y="98" font-size="10" font-weight="700" fill="#475569">└── 📊 Financial_Forecast_v3.xlsx</text>
          </g>"""),
        "golden_rule": "Include the date (YYYY-MM-DD) and version number (v1, v2) in filename!",
        "watch_out": "Avoid saving everything to your Desktop — it causes system clutter and data loss risk.",
        "challenge_prompt": "Suggest a professional filename for the second draft of a staff training plan written in October 2024.",
        "answer_text": "Staff_Training_Plan_Oct2024_v2.docx."
    },

    # 3. File Extensions & Formats
    {
        "id": "dfs-03",
        "number": 3,
        "title": "File Extensions &amp; Formats",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.3",
        "rule_heading": "Recognising Common File Types",
        "rule_body": ".docx = Word processing. .pdf = Portable read-only document (universal). .xlsx / .csv = Spreadsheets / raw comma-separated data. .pptx = Slideshow. .png / .jpg = Images. .mp4 = Video. .zip = Compressed folder.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">FILE FORMAT QUICK REFERENCE</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#2563eb">• .docx: Editable text document (Word)</text>
            <text x="25" y="78" font-size="11" font-weight="800" fill="#dc2626">• .pdf: Fixed layout, non-editable reader format</text>
            <text x="25" y="101" font-size="11" font-weight="800" fill="#16a34a">• .xlsx / .csv: Financial spreadsheets &amp; data tables</text>
          </g>"""),
        "golden_rule": "Always convert to PDF before sending official CVs or contracts so formatting never shifts!",
        "watch_out": "A .csv file only saves raw text and numbers — it CANNOT store cell colours or chart graphics.",
        "challenge_prompt": "Which file format should you choose to ensure a formal report cannot be accidentally altered by the recipient?",
        "answer_text": "PDF (.pdf - Portable Document Format)."
    },

    # 4. Cloud Storage & Syncing
    {
        "id": "dfs-04",
        "number": 4,
        "title": "Cloud Storage &amp; Syncing",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.4",
        "rule_heading": "Remote Servers &amp; Multi-Device Access",
        "rule_body": "Cloud storage (OneDrive, Google Drive, iCloud) stores files on secure remote servers over the Internet. Benefits: Automatic backup, access from any device, easy real-time collaboration. Requires internet connectivity.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">CLOUD STORAGE ADVANTAGES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">✓ Access files from phone, tablet, and PC</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">✓ Automatic real-time off-site backup</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">✓ Multiple people can edit simultaneously</text>
          </g>"""),
        "golden_rule": "Cloud files protect you against hardware crashes, fires, or stolen laptops!",
        "watch_out": "If you don't enable 'Keep on this device' (offline mode), you cannot open cloud files without Wi-Fi.",
        "challenge_prompt": "State two benefits of saving business documents to cloud storage rather than a local USB flash drive.",
        "answer_text": "1. Files are backed up remotely if the physical device is lost/damaged. 2. Documents can be accessed from any location or device with internet."
    },

    # 5. Search Engines: Advanced Operators
    {
        "id": "dfs-05",
        "number": 5,
        "title": "Search Engine Operators",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.5",
        "rule_heading": "Boolean &amp; Precision Search Tricks",
        "rule_body": "Quotation Marks (\"...\"): Searches for the EXACT phrase in that precise order. Minus Sign (-word): Excludes unwanted results. site:gov.uk: Restricts search to official government websites.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">ADVANCED SEARCH OPERATORS</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#2563eb">"functional skills maths" → Exact phrase only</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#dc2626">jaguar speed -car → Excludes automobile results</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#16a34a">site:gov.uk apprenticeship → Official sites only</text>
          </g>"""),
        "golden_rule": "Use quotation marks to search for exact multi-word terms!",
        "watch_out": "Don't put a space after the minus sign (type '-car', NOT '- car').",
        "challenge_prompt": "What search query would you type to find exact information on NHS dental fees while excluding private dentists?",
        "answer_text": "\"NHS dental fees\" -private (or site:nhs.uk \"dental fees\")."
    },

    # 6. Evaluating Search Results
    {
        "id": "dfs-06",
        "number": 6,
        "title": "Evaluating Online Information",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.6",
        "rule_heading": "Domains &amp; Sponsored Ads",
        "rule_body": "Top-level domains: .gov.uk = Official UK government. .ac.uk = Universities. .org = Non-profit organisations. .com / .co.uk = Commercial businesses. Look out for 'Sponsored / Ad' tags at top of search results.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#1e40af" text-anchor="middle">CHECKING WEBSITE RELIABILITY</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#16a34a">.gov.uk &amp; .nhs.uk: Highly authoritative</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">.ac.uk: Academic university research</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#dc2626">Sponsored / Ad tags: Commercial promotion</text>
          </g>"""),
        "golden_rule": "Never rely on the first search result without checking if it has a 'Sponsored' tag!",
        "watch_out": "Beware of fake lookalike domains with typos (e.g. 'gov-uk-tax.com' instead of 'gov.uk').",
        "challenge_prompt": "Why is information found on a .gov.uk website generally more reliable than a .com website for renewing a passport?",
        "answer_text": ".gov.uk is the official UK government portal, whereas .com sites are commercial agencies that often charge extra fees."
    },

    # 7. Managing Device Storage & Memory
    {
        "id": "dfs-07",
        "number": 7,
        "title": "Device Storage vs RAM",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.7",
        "rule_heading": "Storage (SSD/Hard Drive) vs RAM",
        "rule_body": "Storage (GB/TB): Permanent memory holding files and apps when PC is turned off. RAM (Random Access Memory): Temporary working memory used while apps are open. Free up storage by deleting temp files and emptying Recycle Bin.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">STORAGE (SSD/HDD)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Permanent file storage</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• 256 GB / 1 TB</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• Survives restarts</text>
          </g>
          <g transform="translate(240, 20)">
            <rect x="0" y="0" width="180" height="125" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
            <text x="90" y="24" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">MEMORY (RAM)</text>
            <text x="15" y="55" font-size="10.5" font-weight="700" fill="#0f172a">• Active app workspace</text>
            <text x="15" y="78" font-size="10.5" font-weight="700" fill="#0f172a">• 8 GB / 16 GB</text>
            <text x="15" y="101" font-size="10.5" font-weight="700" fill="#0f172a">• Clears on restart</text>
          </g>"""),
        "golden_rule": "Empty your Recycle Bin / Trash to permanently reclaim disk storage!",
        "watch_out": "Running out of RAM makes your computer freeze; running out of Storage prevents saving new files.",
        "challenge_prompt": "State two actions you can take if your smartphone displays a 'Storage Full' warning.",
        "answer_text": "1. Delete unused apps or clear app caches. 2. Back up photos/videos to cloud storage or delete large video files."
    },

    # 8. Compressing & Extracting (.zip)
    {
        "id": "dfs-08",
        "number": 8,
        "title": "Compressing &amp; Extracting (.zip)",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.8",
        "rule_heading": "Reducing File Size for Email",
        "rule_body": "Compress (Zip): Shrinks file size and bundles multiple documents into one single .zip folder for emailing. Extract: Unpacks the zipped files into normal editable documents.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">ZIPPING &amp; EXTRACTING FILES</text>
            <text x="30" y="55" font-size="11" font-weight="800" fill="#2563eb">Compress: Right-click → 'Send to compressed folder'</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#475569">Combines 10 files into 1 small .zip attachment</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#059669">Extract: Right-click .zip → 'Extract All...' to view</text>
          </g>"""),
        "golden_rule": "You must EXTRACT files before you can properly edit and save them!",
        "watch_out": "If you edit files directly inside an unextracted zip, changes may be lost.",
        "challenge_prompt": "Why is it beneficial to zip five large image files before sending them by email?",
        "answer_text": "Zipping reduces the overall file size to fit within email attachment limits and bundles all images into one file."
    },

    # 9. Troubleshooting Freezes & Connectivity
    {
        "id": "dfs-09",
        "number": 9,
        "title": "Basic Troubleshooting",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.9",
        "rule_heading": "First Steps When Tech Fails",
        "rule_body": "App frozen: Open Task Manager (Ctrl + Shift + Esc) and select 'End Task'. Wi-Fi dropped: Check flight mode, restart router, toggle Wi-Fi off and on. Total system freeze: Hold power button for 10 seconds to reboot.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="380" height="130" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="190" y="26" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">FIRST RESPONSE TROUBLESHOOTING</text>
            <text x="25" y="55" font-size="11" font-weight="800" fill="#0f172a">1. App Frozen? Press Ctrl+Shift+Esc → 'End Task'</text>
            <text x="25" y="80" font-size="11" font-weight="800" fill="#0f172a">2. No Internet? Check Airplane mode &amp; restart Wi-Fi router</text>
            <text x="25" y="105" font-size="11" font-weight="800" fill="#059669">3. The Golden Rule: Restart the computer before calling IT!</text>
          </g>"""),
        "golden_rule": "Restarting clears temporary memory glitches in over 80% of minor software issues!",
        "watch_out": "Don't yank out the power cable while a PC is writing data — always force shut down properly.",
        "challenge_prompt": "What keyboard shortcut opens Windows Task Manager directly to close a frozen program?",
        "answer_text": "Ctrl + Shift + Esc (or Ctrl + Alt + Delete)."
    },

    # 10. Data Protection Principles (GDPR)
    {
        "id": "dfs-10",
        "number": 10,
        "title": "Data Protection &amp; UK GDPR",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Devices & Handling",
        "strand_theme": "orange",
        "dfe_code": "DFS 1.10",
        "rule_heading": "Handling Personal Data Lawfully",
        "rule_body": "Personal data relates to an identifiable living person (names, NHS numbers, addresses). Under UK GDPR: 1. Process lawfully, fairly, and transparently. 2. Keep accurate and secure. 3. Delete when no longer required.",
        "svg_html": wrap_svg("""
          <g transform="translate(60, 20)">
            <rect x="0" y="0" width="340" height="130" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
            <text x="170" y="26" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">UK GDPR KEY PRINCIPLES</text>
            <text x="30" y="55" font-size="11" font-weight="700" fill="#0f172a">• Collect only the data that is strictly necessary</text>
            <text x="30" y="80" font-size="11" font-weight="700" fill="#0f172a">• Keep data secure with encryption &amp; passwords</text>
            <text x="30" y="105" font-size="11" font-weight="800" fill="#dc2626">• Never share patient/client records without consent</text>
          </g>"""),
        "golden_rule": "Always lock your computer screen (Win + L) when leaving your desk!",
        "watch_out": "Leaving customer spreadsheets visible on an unattended screen is a serious GDPR data breach.",
        "challenge_prompt": "State two ways you can protect sensitive customer data on a workplace laptop.",
        "answer_text": "1. Use strong password protection / encryption. 2. Lock your screen whenever stepping away from the device."
    }
]

print(f"Validated DFS Area 1: {len(CARDS_1)} cards")
