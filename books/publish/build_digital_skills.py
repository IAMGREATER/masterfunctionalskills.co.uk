#!/usr/bin/env python3
"""
build_digital_skills.py
Compiles the complete 84-page publication:
MasterFunctionalSkills_Digital_Skills_Handbook.pdf

Covering the 5 DfE Statutory Essential Digital Skills (EDSQ) Areas:
1. Using Devices and Handling Information
2. Creating and Editing
3. Communicating
4. Transacting
5. Being Safe and Responsible Online

Full CGP-style visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7),
annotated UI diagrams, workspaces, 5 software workflow labs, 2 security audits,
3 full practical mock exam assignments, and complete explanatory answer keys.
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import (
    SHARED_CSS, render_book_to_pdf, BOOKS_IMG_DIR
)

def build_digital_skills_book():
    front_img = os.path.join(BOOKS_IMG_DIR, "digital_skills_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "digital_skills_cover_page-2.png")
    
    pages = []
    
    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>
""")

    # -------------------------------------------------------------
    # PAGE 2: INSIDE COVER & BLUEPRINT
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Essential Digital Skills</div>
    <div class="page-header-strand">Candidate Blueprint &amp; Framework</div>
  </div>

  <h2>Essential Digital Skills (EDSQ &bull; Entry 3 / Level 1)</h2>
  <p>In modern employment, vocational apprenticeships, and daily community life, digital proficiency is just as essential as reading and numeracy. This study handbook is built strictly upon the Department for Education (DfE) National Standards for Essential Digital Skills.</p>

  <div class="card-concept" style="border-left-color:#0284c7; background:#f0f9ff;">
    <h3 style="color:#0284c7; margin-top:0;">The 5 Statutory DfE Skill Areas</h3>
    <table class="data-table" style="font-size:7.8pt;">
      <tr><th>Skill Area</th><th>Core Workplace Capabilities</th></tr>
      <tr>
        <td><strong>1. Using Devices &amp; Handling Information</strong></td>
        <td>Hardware, OS settings, file management, cloud storage hierarchies, search operators, data backup (3-2-1 rule), and assistive accessibility tools.</td>
      </tr>
      <tr>
        <td><strong>2. Creating &amp; Editing</strong></td>
        <td>Word processing, styles, tables, spreadsheet formulas (SUM, AVERAGE, MIN, MAX, IF), cell formatting, charts, and slide presentation design.</td>
      </tr>
      <tr>
        <td><strong>3. Communicating</strong></td>
        <td>Professional email etiquette, distribution fields (To, CC, BCC), attachments, calendar scheduling, and video conferencing protocols.</td>
      </tr>
      <tr>
        <td><strong>4. Transacting</strong></td>
        <td>E-commerce navigation, digital marketplaces, secure online payments (SSL padlock), public digital services (Gov.uk, NHS App), and account management.</td>
      </tr>
      <tr>
        <td><strong>5. Being Safe &amp; Responsible Online</strong></td>
        <td>Password security, Multi-Factor Authentication (MFA), phishing detection, privacy controls, UK GDPR data rights, digital footprints, and ergonomics.</td>
      </tr>
    </table>
  </div>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-method">
      <h3 style="color:#16a34a; margin-top:0;">Assessment Architecture</h3>
      <p>Official EDSQ assessments (Pearson, City &amp; Guilds, NCFE, Highfield) consist of two practical sections:</p>
      <p><strong>Section 1: Knowledge &amp; Safety:</strong> Multiple-choice and scenario questions covering cybersecurity, privacy, and online transactions.</p>
      <p><strong>Section 2: Practical Tasks:</strong> Real-world tasks requiring document creation, spreadsheet modeling, email drafting, and file management.</p>
    </div>
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Candidate Record</h3>
      <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-top:4px;">
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Provider / Centre:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part I: 20 Core Units:</strong></td><td style="border-bottom:1px solid #cbd5e1;">[ &nbsp; ] Completed</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part II: 5 Software Labs:</strong></td><td style="border-bottom:1px solid #cbd5e1;">[ &nbsp; ] Mastered</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part III: Security Audits:</strong></td><td style="border-bottom:1px solid #cbd5e1;">[ &nbsp; ] Verified</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part IV: Mock Exam 1:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 30</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part IV: Mock Exam 2:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 30</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Part IV: Mock Exam 3:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 30</td></tr>
      </table>
    </div>
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills (EDSQ) Practical Study Handbook</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: CONTENTS & COMPETENCY MATRIX TRACKER
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Essential Digital Skills</div>
    <div class="page-header-strand">Contents &amp; Competency Matrix</div>
  </div>

  <h2>Curriculum Contents &amp; Skills Audit</h2>
  <p>Track your progress across the complete 84-page practical curriculum:</p>

  <table class="data-table" style="font-size:7pt; margin-top:2px;">
    <tr>
      <th style="width:18%;">Curriculum Section</th>
      <th style="width:48%;">DfE Standard &amp; Module Topic</th>
      <th style="width:14%;">Pages</th>
      <th style="width:10%;">Status</th>
    </tr>
    <tr><td><strong>Part I &bull; Area 1 (U1–U4)</strong></td><td>Devices, File Hierarchies, Search Operators, Backups &amp; Accessibility</td><td>Pages 4–11</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Part I &bull; Area 2 (U5–U10)</strong></td><td>Word Processing, Spreadsheets, Data Formulas, Visual Charts &amp; Presentations</td><td>Pages 12–23</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Part I &bull; Area 3 (U11–U13)</strong></td><td>Email Etiquette, Cloud File Sharing Permissions, Video Conferencing</td><td>Pages 24–29</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Part I &bull; Area 4 (U14–U16)</strong></td><td>E-Commerce Navigation, Secure Payments (SSL), Public Services (Gov.uk/NHS)</td><td>Pages 30–35</td><td>[ &nbsp; ]</td></tr>
    <tr><td><strong>Part I &bull; Area 5 (U17–U20)</strong></td><td>Passwords, MFA, Phishing Defence, Social Footprints, GDPR &amp; Ergonomics</td><td>Pages 36–43</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Part II &bull; Software Lab 1</strong></td><td>Master Word Processing: Layout, Styles, Mail Merge &amp; PDF Export</td><td>Pages 44–45</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Part II &bull; Software Lab 2</strong></td><td>Master Spreadsheets: Absolute Referencing, IF, VLOOKUP &amp; Dynamic Charts</td><td>Pages 46–47</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Part II &bull; Software Lab 3</strong></td><td>Master Slide Decks: Master Layouts, Media, Transitions &amp; Presenter View</td><td>Pages 48–49</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Part II &bull; Software Lab 4</strong></td><td>Master Email &amp; Calendar: Inbox Rules, Scheduling, Recurring Team Meetings</td><td>Pages 50–51</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#e0f2fe;"><td><strong>Part II &bull; Software Lab 5</strong></td><td>Master Cloud Collaboration: Version History, Shared Drives &amp; Role Permissions</td><td>Pages 52–53</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fef3c7;"><td><strong>Part III &bull; Security Audit 1</strong></td><td>Workplace Cyber Threat Vectors, Phishing Defense &amp; Password Vault Checklist</td><td>Pages 54–55</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fef3c7;"><td><strong>Part III &bull; Security Audit 2</strong></td><td>Device Hardening, Wi-Fi Encryption, 3-2-1 Backups &amp; UK GDPR Compliance</td><td>Pages 56–57</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fae8ff;"><td><strong>Part IV &bull; Practical Mock 1</strong></td><td>Community Charity Campaign: Budget Spreadsheet, Event Flyer &amp; Outreach</td><td>Pages 58–61</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fae8ff;"><td><strong>Part IV &bull; Practical Mock 2</strong></td><td>Healthcare Patient Onboarding: Records Database, Mail Merge &amp; GDPR</td><td>Pages 62–65</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#fae8ff;"><td><strong>Part IV &bull; Practical Mock 3</strong></td><td>Retail E-Commerce Transition: Inventory Formulas, Pitch Deck &amp; Inquiries</td><td>Pages 66–69</td><td>[ &nbsp; ]</td></tr>
    <tr style="background:#dcfce7;"><td><strong>Part V &bull; Answer Keys</strong></td><td>Comprehensive Step-by-Step Solutions &amp; Marking Rubrics (Units 1–20, Labs, Mocks)</td><td>Pages 70–83</td><td>[ &nbsp; ]</td></tr>
  </table>

  <div class="page-footer">
    <div>Essential Digital Skills (EDSQ) Practical Study Handbook</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 20 DIGITAL SKILLS UNITS (2 Pages each = 40 pages total, Pages 4 to 43)
    # -------------------------------------------------------------
    dfs_units_data = [
        # Unit 1
        ("Unit 1: Hardware, Operating Systems & Settings", "Area 1: Using Devices & Handling Information",
         """Digital devices require hardware components and an operating system (Windows, macOS, iOS, Android, ChromeOS) to run applications and manage resources.""",
         """<strong>Essential Device Fundamentals:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Input Devices:</strong> Keyboard, mouse, touchscreen, microphone, barcode scanner.</li>
           <li><strong>Output Devices:</strong> Monitor screen, printer, speakers, headphones.</li>
           <li><strong>Storage:</strong> Internal SSD/HDD, USB flash drive, SD card, Cloud storage.</li>
           <li><strong>Key System Settings:</strong> Wi-Fi network connection, Bluetooth pairing, screen brightness, volume, and display zoom.</li>
         </ul>""",
         "A new office laptop cannot connect to the internet. Describe the 3 steps to connect it to the secure office Wi-Fi network.",
         """1. Click the <strong>Network / Wi-Fi icon</strong> in the system tray (bottom-right on Windows or top-right on Mac).<br>2. Select the office network name (SSID) from the list of available networks.<br>3. Click <strong>Connect</strong>, enter the secure WPA2/WPA3 password, and tick 'Connect automatically'.<br><strong>Status:</strong> The icon will change to show active Wi-Fi signal waves.""",
         "Never connect to an unknown public Wi-Fi network without a VPN or password protection.",
         "Keep your operating system updated regularly to ensure security patches and bug fixes are installed.",
         [
           ("Classify each item as an Input or Output device: a) Barcode scanner &nbsp;&nbsp; b) Laser printer &nbsp;&nbsp; c) Touchscreen", "[3 Marks]"),
           ("Where in the operating system do you adjust screen resolution and text magnification?", "[1 Mark]"),
           ("Explain the function of an Operating System (OS).", "[2 Marks]"),
           ("What should you do if an application freezes and will not close normally?", "[1 Mark]")
         ]),

        # Unit 2
        ("Unit 2: File Organisation & Cloud Syncing", "Area 1: Using Devices & Handling Information",
         """Efficient file management ensures workplace documents can be stored logically, retrieved quickly, and backed up securely.""",
         """<strong>Folder Hierarchy Best Practice:</strong>
         <div class="ui-window" style="margin:4px 0;">
           <div class="ui-titlebar">File Explorer / Finder &bull; Structured Folder Tree</div>
           <div class="ui-body" style="font-family:'JetBrains Mono',monospace; font-size:7.5pt;">
             &boxvr;&boxh; <strong>Documents</strong><br>
             &nbsp;&nbsp;&boxvr;&boxh; <strong>Customers</strong><br>
             &nbsp;&nbsp;&boxv;&nbsp;&nbsp;&boxvr;&boxh; Smith_John_Invoice_2026-10.pdf<br>
             &nbsp;&nbsp;&boxv;&nbsp;&nbsp;&boxur;&boxh; Taylor_Sarah_Quote.docx<br>
             &nbsp;&nbsp;&boxur;&boxh; <strong>Financial_Reports</strong><br>
             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&boxh; Q3_Summary_Final_v2.xlsx
           </div>
         </div>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Meaningful File Naming:</strong> Include Project, Client/Subject, Date (YYYY-MM-DD), and Version (e.g. <code>Sales_Report_2026-10-15_v2.docx</code>).</li>
           <li><strong>Common File Extensions:</strong> <code>.docx</code> (Word document), <code>.xlsx</code> (Excel spreadsheet), <code>.pdf</code> (Portable Document Format &mdash; read-only), <code>.jpg/.png</code> (Images).</li>
         </ul>""",
         "A colleague names an important budget document <em>'doc1.xlsx'</em> and saves it on the desktop. Explain two problems with this and suggest an improved name.",
         """1. Problem 1: The name 'doc1' gives no indication of the file's content or department.<br>2. Problem 2: Saving on the desktop creates clutter and risks accidental deletion.<br><strong>Improved Name:</strong> <code>Department_Annual_Budget_2026_Final.xlsx</code> saved in <code>Documents / Finance / 2026</code>.""",
         "Avoid saving all your work on the desktop! Desktop clutter slows down your computer and makes finding files difficult.",
         "Always use the PDF format when sending final documents to clients so formatting cannot be accidentally altered.",
         [
           ("Which file format is best suited for sending an uneditable contract to a client: .docx, .txt, or .pdf?", "[1 Mark]"),
           ("Create an effective folder hierarchy for storing a college student's coursework across 3 subjects.", "[2 Marks]"),
           ("What do the letters 'v1' and 'v2' mean at the end of a file name?", "[1 Mark]"),
           ("Explain how Cloud storage (like OneDrive or Google Drive) protects files compared to saving only on a local hard drive.", "[2 Marks]")
         ]),

        # Unit 3
        ("Unit 3: Search Engines & Evaluating Information", "Area 1: Using Devices & Handling Information",
         """Finding accurate information online requires effective querying techniques and critical evaluation of source credibility.""",
         """<strong>Advanced Search Operators:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Quotation Marks (<code>"..."</code>):</strong> Search for an exact phrase (e.g. <code>"health and safety at work act"</code>).</li>
           <li><strong>Minus Sign (<code>-</code>):</strong> Exclude unwanted words (e.g. <code>jaguar speed -car</code>).</li>
           <li><strong>Site Search (<code>site:</code>):</strong> Search only within specific domain types (e.g. <code>apprenticeships site:.gov.uk</code>).</li>
         </ul>
         <strong>The CRAAP Evaluation Test:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Currency:</strong> When was the information published or updated?</li>
           <li><strong>Reliability / Authority:</strong> Who wrote it? Is it an official government (.gov.uk), university (.ac.uk), or accredited body?</li>
           <li><strong>Purpose:</strong> Is the website trying to inform, or are they trying to sell products / spread bias?</li>
         </ul>""",
         "You need official UK minimum wage rates for 2026. Write an exact search query to find this on official government pages.",
         """1. Use keywords: <code>"national minimum wage" rates 2026</code>.<br>2. Restrict to official government domain: <code>site:.gov.uk</code>.<br><strong>Full Query:</strong> <code>"national minimum wage rates" 2026 site:.gov.uk</code>.<br><strong>Why:</strong> Guarantees official statutory data directly from Gov.uk rather than marketing blogs.""",
         "Never trust the first search result blindly! The top links are often paid advertisements (marked 'Sponsored').",
         "Check the web domain: .gov.uk and .nhs.uk are strictly verified UK public sector sources.",
         [
           ("What do quotation marks <code>" "</code> do when typed into an internet search engine?", "[1 Mark]"),
           ("Which website domain is most trustworthy for medical advice: a commercial forum (.com) or the NHS website (.nhs.uk)? Explain why.", "[2 Marks]"),
           ("How can you verify whether a viral news article shared on social media is accurate?", "[2 Marks]"),
           ("Write a search query to find electric vehicle charging grants on UK government websites.", "[1 Mark]")
         ]),

        # Unit 4
        ("Unit 4: Storage Media, Backup & Accessibility", "Area 1: Using Devices & Handling Information",
         """Securing data with regular backups and customising operating system accessibility features allows all users to work safely and effectively.""",
         """<strong>The 3-2-1 Backup Rule:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>Maintain at least <strong>3</strong> copies of your important data.</li>
           <li>Store the copies on <strong>2</strong> different types of media (e.g. internal drive + external USB drive).</li>
           <li>Keep at least <strong>1</strong> copy <strong>off-site</strong> (e.g. Cloud backup: OneDrive, Google Drive, iCloud).</li>
         </ul>
         <strong>Essential Accessibility Features:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Screen Magnifier / Zoom:</strong> Enlarge sections of the screen for low-vision users.</li>
           <li><strong>High Contrast Mode:</strong> Increases distinction between background and text.</li>
           <li><strong>Screen Reader / Text-to-Speech:</strong> Reads displayed words aloud.</li>
           <li><strong>Speech-to-Text (Dictation):</strong> Allows typing using your voice.</li>
         </ul>""",
         "A small business owner keeps all customer invoices on a single USB thumb drive in her office. Explain two risks and recommend a safe backup strategy.",
         """1. Risk 1: The USB stick could be lost, stolen, or mechanically damaged.<br>2. Risk 2: If a fire occurs in the office, the data is completely lost with no copy.<br><strong>Recommendation:</strong> Implement the 3-2-1 rule: store files on computer drive, back up weekly to an external hard drive, and synchronize with encrypted Cloud storage.""",
         "A USB memory stick is a transport device, NOT a permanent archive! They are easily corrupted or misplaced.",
         "Turn on automatic Cloud syncing so your work is backed up continuously without relying on memory.",
         [
           ("Explain the 3-2-1 backup strategy in simple terms.", "[3 Marks]"),
           ("Name two operating system accessibility tools that assist users with visual impairments.", "[2 Marks]"),
           ("State one advantage and one disadvantage of storing files on an external hard drive compared to Cloud storage.", "[2 Marks]")
         ]),

        # Unit 5
        ("Unit 5: Word Processing & Document Layout", "Area 2: Creating & Editing",
         """Professional documents require clear typographic hierarchy, consistent paragraph styling, and appropriate margins.""",
         """<strong>Essential Document Formatting Tools:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Headings &amp; Styles:</strong> Apply 'Heading 1', 'Heading 2', and 'Normal' styles to ensure screen-reader accessibility and automatic Table of Contents generation.</li>
           <li><strong>Alignment &amp; Spacing:</strong> Use left-alignment for body text (never justified for dyslexia accessibility). Set line spacing to 1.15 or 1.5.</li>
           <li><strong>Lists:</strong> Use numbered lists for sequential chronological steps; use bullet points for unordered items.</li>
           <li><strong>Cut, Copy &amp; Paste:</strong> <code>Ctrl+X</code> (Cut), <code>Ctrl+C</code> (Copy), <code>Ctrl+V</code> (Paste), <code>Ctrl+Z</code> (Undo).</li>
         </ul>""",
         "A trainee formats a report by highlighting titles and manually making them 18pt bold instead of using the 'Heading 1' style. Explain why using built-in styles is superior.",
         """1. <strong>Consistency:</strong> If you change the font theme, all headings update automatically across the entire document.<br>2. <strong>Accessibility:</strong> Screen-reading software uses heading tags (H1, H2) to help visually impaired users navigate sections.<br>3. <strong>Automation:</strong> Enables the automatic generation of an interactive Table of Contents with page numbers.""",
         "Never use multiple spaces or blank 'Enter' lines to position text on a page! Use Page Breaks (Ctrl+Enter) instead.",
         "Keep fonts clean and legible: Arial, Calibri, Open Sans, or Lexend are ideal for business reading.",
         [
           ("What is the keyboard shortcut for: a) Copy &nbsp;&nbsp; b) Paste &nbsp;&nbsp; c) Undo?", "[3 Marks]"),
           ("Explain two advantages of applying 'Heading Styles' rather than manual font formatting in a long report.", "[2 Marks]"),
           ("Why is left-aligned text recommended over justified text for readability?", "[1 Mark]")
         ]),

        # Unit 6
        ("Unit 6: Tables, Images & Page Setup", "Area 2: Creating & Editing",
         """Enhancing documents with formatted tables, cropped images with alt-text, and proper page orientation improves visual engagement.""",
         """<strong>Working with Tables &amp; Images:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Tables:</strong> Insert via <code>Insert &rarr; Table</code>. Set a clear Header Row, format border lines, and ensure numbers align to the right while text aligns to the left.</li>
           <li><strong>Image Placement:</strong> Set Text Wrapping to <em>'Square'</em> or <em>'In Line with Text'</em>. Resize proportionally using corner handles.</li>
           <li><strong>Alt Text:</strong> Right-click image &rarr; <em>'Edit Alt Text'</em> to provide a concise description for users who rely on screen readers.</li>
           <li><strong>Page Orientation:</strong> Switch between Portrait (standard reports) and Landscape (wide tables and charts) via <code>Layout &rarr; Orientation</code>.</li>
         </ul>""",
         "You need to insert a wide monthly sales table into a portrait-oriented company report without distorting text. Describe the steps required.",
         """1. Position the cursor immediately before the table location.<br>2. Go to <code>Layout &rarr; Breaks &rarr; Section Break (Next Page)</code>.<br>3. Change orientation for the new section: <code>Layout &rarr; Orientation &rarr; Landscape</code>.<br>4. Insert the table and adjust column widths.<br>5. Insert another Section Break (Next Page) below the table and switch back to <code>Portrait</code> for subsequent text.""",
         "Never drag images by side handles &mdash; this squashes or stretches the graphic out of proportion! Always drag corner handles.",
         "Add Alt Text to all images to ensure your document complies with UK digital accessibility standards.",
         [
           ("What happens if you resize an image using a side handle instead of a corner handle?", "[1 Mark]"),
           ("Explain the purpose of 'Alt Text' when adding images to digital documents.", "[2 Marks]"),
           ("How do you change a single page in a Word document to Landscape without affecting the rest of the pages?", "[2 Marks]"),
           ("Why should numerical figures in tables usually be right-aligned?", "[1 Mark]")
         ]),

        # Unit 7
        ("Unit 7: Spreadsheets &ndash; Cell Referencing &amp; Formatting", "Area 2: Creating & Editing",
         """Spreadsheets organize numerical data into grid cells defined by column letters and row numbers, enabling dynamic calculations.""",
         """<strong>Spreadsheet Structure &amp; Cell Types:</strong>
         <div class="ui-window" style="margin:4px 0;">
           <div class="ui-titlebar">Spreadsheet Grid &bull; Cell Reference Matrix</div>
           <div class="ui-body" style="font-size:7.5pt;">
             <table class="data-table" style="margin:0; font-size:7.5pt;">
               <tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th></tr>
               <tr><td><strong>1</strong></td><td><strong>Item Description</strong></td><td><strong>Quantity</strong></td><td><strong>Unit Price (£)</strong></td><td><strong>Total (£)</strong></td></tr>
               <tr><td><strong>2</strong></td><td>Safety Helmets</td><td>25</td><td>£12.50</td><td><code>=B2*C2</code></td></tr>
               <tr><td><strong>3</strong></td><td>Hi-Vis Vests</td><td>40</td><td>£4.20</td><td><code>=B3*C3</code></td></tr>
             </table>
           </div>
         </div>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Cell Coordinates:</strong> Column letter followed by Row number (e.g. <code>C2</code>).</li>
           <li><strong>Data Types:</strong> Text (labels &mdash; left-aligned), Numbers (quantities &mdash; right-aligned), Currency (£ with 2 decimal places), Dates.</li>
           <li><strong>Autofill Handle:</strong> Drag the small green square in the bottom-right corner of a cell to replicate formulas down a column.</li>
         </ul>""",
         "A user types '£12.50' directly into cell C2, but when multiplying <code>=B2*C2</code>, the spreadsheet returns <code>#VALUE!</code>. Explain why and how to fix it.",
         """1. <strong>Why:</strong> The user manually typed the currency symbol '£' inside the cell, causing the software to treat the entry as text rather than a calculable number.<br>2. <strong>Fix:</strong> Type only the number <code>12.50</code> into the cell, then apply the <strong>Currency (£) format</strong> using the toolbar formatting ribbon.""",
         "Never type currency symbols (£ or $) directly into calculation cells! Format the cell as 'Currency' instead.",
         "Check for the small green triangle error indicator in cell corners &mdash; it alerts you to formula inconsistencies.",
         [
           ("What is the cell reference for the cell in Column D and Row 14?", "[1 Mark]"),
           ("Explain why entering text into a numerical calculation cell causes a '#VALUE!' error.", "[2 Marks]"),
           ("What tool allows you to copy a formula down 50 rows instantly without retyping?", "[1 Mark]"),
           ("How do you format a cell to display numbers as pounds with two decimal places (e.g. £14.50)?", "[1 Mark]")
         ]),

        # Unit 8
        ("Unit 8: Spreadsheet Formulas & Functions", "Area 2: Creating & Editing",
         """Automating calculations with built-in functions ensures speed, accuracy, and dynamic recalculation when inputs change.""",
         """<strong>The Big 5 Spreadsheet Functions:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Every formula must start with an equals sign (<code>=</code>).</strong></li>
           <li><code>=SUM(D2:D15)</code> &rarr; Adds all numbers in the specified cell range.</li>
           <li><code>=AVERAGE(D2:D15)</code> &rarr; Calculates the arithmetic mean.</li>
           <li><code>=MIN(D2:D15)</code> &rarr; Finds the lowest value in the range.</li>
           <li><code>=MAX(D2:D15)</code> &rarr; Finds the highest value in the range.</li>
           <li><code>=COUNT(D2:D15)</code> &rarr; Counts how many cells contain numbers.</li>
         </ul>
         <strong>Basic Arithmetic Operators:</strong> Addition (<code>+</code>), Subtraction (<code>-</code>), Multiplication (<code>*</code>), Division (<code>/</code>).""",
         "Write the exact formula to calculate the total cost in cell D2 by multiplying quantity in B2 by unit price in C2, plus 20% VAT.",
         """1. Basic subtotal: <code>B2 * C2</code>.<br>2. Add 20% VAT by multiplying by 1.20.<br><strong>Exact Formula:</strong> <code>=(B2*C2)*1.20</code> &nbsp;or&nbsp; <code>=B2*C2*1.2</code>.<br><strong>Alternative with separate VAT rate cell:</strong> <code>=B2*C2*(1+$F$1)</code> where F1 contains 20%.""",
         "Never type <code>=SUM(A1+B1)</code>! The word SUM already means add. Use either <code>=A1+B1</code> or <code>=SUM(A1:B1)</code>.",
         "Use uppercase for function names (SUM, AVERAGE) to maintain professional spreadsheet hygiene.",
         [
           ("Write the exact formula to find the average score of cells B2 to B28.", "[1 Mark]"),
           ("Write the formula to calculate the difference between cell C10 (Sales) and cell D10 (Costs).", "[1 Mark]"),
           ("What formula would you use to find the lowest price in cells E5 to E50?", "[1 Mark]"),
           ("Explain what happens to a formula in cell D2 (=B2*C2) when you change the number in B2.", "[2 Marks]")
         ]),

        # Unit 9
        ("Unit 9: Data Visualisation &amp; Charts", "Area 2: Creating & Editing",
         """Charts translate raw spreadsheet figures into immediate visual insights, highlighting trends, distributions, and comparisons.""",
         """<strong>Selecting the Right Chart Type:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Column / Bar Chart:</strong> Best for comparing discrete categories (e.g. sales across 4 different branches).</li>
           <li><strong>Line Graph:</strong> Ideal for showing trends over time (e.g. monthly temperatures or revenue across 12 months).</li>
           <li><strong>Pie Chart:</strong> Best for displaying proportions of a whole (must total 100%, e.g. market share or budget breakdown). Avoid using if there are more than 6 categories!</li>
         </ul>
         <strong>Essential Chart Elements (Mark Scheme Checklist):</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Chart Title:</strong> Clear, informative description (e.g. <em>"Quarterly Departmental Expenditure 2026"</em>).</li>
           <li><strong>Axis Titles:</strong> X-axis label (Category) and Y-axis label (Units &mdash; e.g. <em>"Revenue (£ Thousands)"</em>).</li>
           <li><strong>Data Labels / Legend:</strong> Distinguishes series clearly.</li>
         </ul>""",
         "A manager wants to display company market share compared to four competitors. Recommend the best chart type and two essential formatting features.",
         """1. <strong>Recommended Chart:</strong> <strong>Pie Chart</strong> (or Doughnut Chart), because it clearly displays proportional parts of a 100% total.<br>2. <strong>Feature 1:</strong> Percentage data labels displayed directly on each slice.<br>3. <strong>Feature 2:</strong> A clear chart legend distinguishing each competitor by colour with a descriptive title.""",
         "Never produce a chart without axis labels! In official exams, missing axis labels results in losing 50% of the chart marks.",
         "Keep pie charts simple: if you have more than 5 or 6 slices, use a bar chart instead for readability.",
         [
           ("Which chart type is best for showing how vehicle sales changed month-by-month over a 2-year period?", "[1 Mark]"),
           ("State two essential labels that must be included on every bar or column chart to avoid losing exam marks.", "[2 Marks]"),
           ("Why is a pie chart unsuitable for showing daily temperature changes across 30 days?", "[2 Marks]"),
           ("How do you create a chart in Excel from selected data in cells A1:B8?", "[1 Mark]")
         ]),

        # Unit 10
        ("Unit 10: Digital Presentations &amp; Slide Design", "Area 2: Creating & Editing",
         """Effective digital slide decks support oral presentations using visual hierarchy, concise bullet points, and restrained multimedia.""",
         """<strong>The 6 &times; 6 Rule for Slide Legibility:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>No more than <strong>6 bullet points</strong> per slide.</li>
           <li>No more than <strong>6 words</strong> per bullet point.</li>
           <li>Slides are visual cues for the audience, NOT a teleprompter for the speaker!</li>
         </ul>
         <strong>Slide Master &amp; Formatting Best Practice:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>Use <strong>Slide Master</strong> (<code>View &rarr; Slide Master</code>) to set consistent corporate colours, fonts, and logos across all slides in one step.</li>
           <li>Maintain strong contrast: dark text on light cream backgrounds.</li>
           <li>Use subtle slide transitions (<em>'Fade'</em> or <em>'Push'</em>). Avoid distracting animations (spinning or flying text).</li>
           <li>Add detailed notes to the <strong>Presenter Notes Pane</strong> rather than cluttering the visible slide.</li>
         </ul>""",
         "A presenter pastes three full paragraphs of dense text onto a single presentation slide. Explain two reasons why this is ineffective and suggest two improvements.",
         """1. <strong>Ineffective 1:</strong> The audience will try to read the slide rather than listening to the speaker.<br>2. <strong>Ineffective 2:</strong> Small font size makes it illegible from the back of the room.<br><strong>Improvements:</strong> Condense the paragraphs into 3–4 concise bullet points (under 6 words each) and move the explanatory text into the Presenter Notes pane.""",
         "Avoid wild, noisy animations and rainbow colours! Professional presentations use clean, restrained styling.",
         "Always run 'Slide Show' mode (F5) before your meeting to verify that all images and fonts display correctly.",
         [
           ("Explain the '6 &times; 6 rule' in presentation slide design.", "[2 Marks]"),
           ("What is the purpose of the 'Presenter Notes' section at the bottom of a slide?", "[1 Mark]"),
           ("How does using the 'Slide Master' save time when building a 20-slide presentation?", "[2 Marks]"),
           ("State two font formatting practices that ensure slides are readable from a distance.", "[2 Marks]")
         ]),

        # Unit 11
        ("Unit 11: Professional Email Etiquette", "Area 3: Communicating",
         """Workplace email requires clear addressing protocols, concise subject lines, formal tone, and appropriate sign-offs.""",
         """<strong>Email Header Architecture:</strong>
         <div class="ui-window" style="margin:4px 0;">
           <div class="ui-titlebar">Email Client &bull; Message Header Fields</div>
           <div class="ui-body" style="font-size:7.5pt;">
             <strong>To:</strong> primary.recipient@company.co.uk &nbsp;<em>(Action required)</em><br>
             <strong>Cc:</strong> project.manager@company.co.uk &nbsp;<em>(Carbon Copy &mdash; For information only)</em><br>
             <strong>Bcc:</strong> compliance@company.co.uk &nbsp;<em>(Blind Carbon Copy &mdash; Hidden from all other recipients)</em><br>
             <strong>Subject:</strong> <code>Urgent: Q3 Logistics Schedule Review &ndash; Meeting 15 Oct</code>
           </div>
         </div>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Subject Line:</strong> Must be concise, specific, and actionable. Never leave blank!</li>
           <li><strong>When to use BCC:</strong> Essential when sending mass emails to multiple external clients to protect their privacy under UK GDPR.</li>
         </ul>""",
         "A marketing manager sends an email newsletter to 80 private customers by putting all their email addresses in the 'Cc' field. Explain the critical error.",
         """1. <strong>Data Breach:</strong> Every recipient can see the private email addresses of all 79 other customers.<br>2. <strong>Legal Violation:</strong> This constitutes a direct breach of the UK General Data Protection Regulation (UK GDPR), exposing the company to regulatory fines.<br><strong>Correct Method:</strong> The manager should place her own address in 'To' and all 80 customer addresses in <strong>'Bcc' (Blind Carbon Copy)</strong>.""",
         "NEVER write emails entirely in CAPITAL LETTERS &mdash; in digital communication, this is interpreted as aggressive shouting!",
         "Always double-check recipient addresses before hitting Send, especially when using autocomplete.",
         [
           ("Explain the difference between the 'Cc' and 'Bcc' fields in an email.", "[2 Marks]"),
           ("Why is the subject line 'Hello' or leaving it blank poor professional practice?", "[1 Mark]"),
           ("Explain why putting a list of customer email addresses into 'Cc' violates UK GDPR data protection.", "[2 Marks]"),
           ("Write a professional subject line for an email rescheduling a team meeting from Tuesday to Thursday.", "[1 Mark]")
         ]),

        # Unit 12
        ("Unit 12: Attachments, Cloud Links &amp; Calendars", "Area 3: Communicating",
         """Sharing documents securely and coordinating schedules using digital calendars are vital modern workplace collaboration capabilities.""",
         """<strong>Attachments vs Cloud Sharing Links:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Direct Attachment:</strong> Good for small, final files (&lt; 10 MB). Disadvantages: creates multiple disconnected versions; can be blocked by mail servers.</li>
           <li><strong>Cloud Link (OneDrive / Google Drive):</strong> Ideal for large files and collaborative documents. Allows setting permissions: <em>'Can view only'</em> or <em>'Can edit'</em>. You can revoke access at any time.</li>
         </ul>
         <strong>Digital Calendar Invitations:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>Include: Event Title, Date, Start &amp; End Time, Physical Location or Video Call Link, and Agenda.</li>
           <li>Use recurring settings for regular weekly/monthly team meetings.</li>
         </ul>""",
         "You need to share a 45 MB video file and a 200-page training manual with 15 colleagues for review. Describe the best method.",
         """1. Do not attach the files directly to an email (they exceed standard 25 MB email attachment limits).<br>2. Upload the files to the company's secure Cloud storage (e.g. OneDrive / SharePoint).<br>3. Generate a secure sharing link set to <strong>'Specific People'</strong> with <strong>'Can edit'</strong> or <strong>'Can view'</strong> permissions.<br>4. Paste the link into an email with instructions.<br><strong>Advantage:</strong> Eliminates file size bounces and ensures everyone reviews the single live version.""",
         "Always mention attachments in your email body (e.g. 'Please find the quote attached') so recipients know to look for them.",
         "Check file size before attaching: files larger than 20 MB should always be shared via a Cloud link.",
         [
           ("Give two reasons why sharing a document via a Cloud link is superior to sending a 30 MB email attachment.", "[2 Marks]"),
           ("What is the difference between setting Cloud link permissions to 'Can view' versus 'Can edit'?", "[2 Marks]"),
           ("List three essential details that must be included when sending a digital calendar invitation for a meeting.", "[2 Marks]")
         ]),

        # Unit 13
        ("Unit 13: Video Conferencing &amp; Virtual Meetings", "Area 3: Communicating",
         """Participating professionally in Microsoft Teams, Zoom, or Google Meet calls requires audio-visual setup, screen sharing, and meeting etiquette.""",
         """<strong>Virtual Meeting Protocols:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Mute When Not Speaking:</strong> Eliminates distracting background noise (traffic, keyboard clatter, breathing).</li>
           <li><strong>Camera &amp; Background:</strong> Ensure good lighting (light source in front, not behind). Apply a subtle blurred or professional virtual background.</li>
           <li><strong>Chat &amp; Reactions:</strong> Use the <em>'Raise Hand'</em> feature before speaking in large meetings. Use meeting chat for relevant links and questions.</li>
           <li><strong>Screen Sharing Safety:</strong> Close personal browser tabs, email inboxes, and confidential documents BEFORE sharing your screen! Share specific application windows rather than your entire desktop.</li>
         </ul>""",
         "A team member is about to share their screen during a client presentation. State two privacy precautions they must take before clicking 'Share'.",
         """1. <strong>Close Confidential Windows:</strong> Shut down personal email, internal chat channels (Slack/Teams), and confidential client files to prevent accidental data leaks.<br>2. <strong>Select Application Window:</strong> Choose to share only the specific PowerPoint application window rather than 'Entire Desktop' &mdash; this prevents personal notifications appearing on screen.""",
         "Never share your 'Entire Desktop' if you have personal messages or banking windows open in the background!",
         "Always test your microphone and speakers in the settings menu 5 minutes before joining an important meeting.",
         [
           ("Why should participants mute their microphones when someone else is presenting in a virtual meeting?", "[1 Mark]"),
           ("State two precautions you must take before sharing your screen in a public or client meeting.", "[2 Marks]"),
           ("Explain how using a 'Blurred Background' protects privacy during home-working video calls.", "[1 Mark]"),
           ("What feature should you use to signal that you wish to speak without interrupting the speaker?", "[1 Mark]")
         ]),

        # Unit 14
        ("Unit 14: E-Commerce Navigation &amp; Filtering", "Area 4: Transacting",
         """Navigating online retailers, comparing prices, and utilizing search filters allows users to make informed purchasing decisions.""",
         """<strong>Effective E-Commerce Search &amp; Filtering:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Filters:</strong> Narrow thousands of products by Price (low to high), Brand, Customer Rating (4+ stars), Size, and Delivery Speed.</li>
           <li><strong>Product Specifications:</strong> Verify dimensions, warranty, and compatibility before adding to basket.</li>
           <li><strong>Customer Reviews:</strong> Read verified purchase reviews; look for patterns in 1-star and 2-star feedback rather than relying solely on overall averages.</li>
           <li><strong>Delivery &amp; Returns Policy:</strong> Check delivery charges, return window (e.g. 14 or 30 days), and who pays return postage.</li>
         </ul>""",
         "An administrative assistant needs to order 5 ergonomic office chairs under a £120 per chair budget with next-day delivery. Describe how to use website filters to find them.",
         """1. Type 'ergonomic office chair' into the store search bar.<br>2. Apply the <strong>Price Filter</strong>: set maximum price to £120.<br>3. Apply the <strong>Delivery Filter</strong>: select 'Next Day Delivery' or 'In Stock for Immediate Dispatch'.<br>4. Sort results by <strong>Customer Rating (Highest to Lowest)</strong> to identify top-quality models within budget.""",
         "Watch out for hidden shipping fees that only appear at the final checkout screen!",
         "Always check the returns policy: under UK Consumer Contracts Regulations, you generally have 14 days to cancel online purchases.",
         [
           ("Explain how applying online filters saves time when shopping on a large e-commerce website.", "[2 Marks]"),
           ("Why is it beneficial to check both positive and negative customer reviews before purchasing an expensive electronic item?", "[2 Marks]"),
           ("Under UK online shopping rules, how long do consumers generally have to return goods bought online?", "[1 Mark]")
         ]),

        # Unit 15
        ("Unit 15: Secure Online Payments &amp; Protection", "Area 4: Transacting",
         """Protecting financial details during online transactions requires verifying SSL encryption, choosing secure payment gateways, and checking consumer rights.""",
         """<strong>Online Payment Security Checklist:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>HTTPS &amp; Padlock:</strong> Ensure URL starts with <code>https://</code> (the 's' stands for secure) and displays a closed padlock icon in the browser address bar.</li>
           <li><strong>Credit Card vs Debit Card:</strong> Credit cards offer statutory protection under <strong>Section 75 of the Consumer Credit Act</strong> for purchases between £100 and £30,000 if the retailer goes bust.</li>
           <li><strong>Secure Gateways:</strong> Use trusted intermediaries (PayPal, Apple Pay, Google Pay) so the retailer never sees your card numbers.</li>
           <li><strong>3D Secure Authentication:</strong> Entering a one-time passcode (OTP) or confirming via your banking mobile app before payment clears.</li>
         </ul>""",
         "A website offers designer trainers at an 80% discount, but the URL begins with <code>http://</code> (no 's') and asks for payment via direct bank transfer. Identify two major danger signs.",
         """1. <strong>Danger 1 (No HTTPS):</strong> The connection is unencrypted (<code>http://</code>), meaning card details can be intercepted by hackers.<br>2. <strong>Danger 2 (Direct Bank Transfer):</strong> Fraudsters demand bank transfers because transfers offer zero fraud protection and cannot be refunded like card payments.<br><strong>Action:</strong> Do not purchase; leave the website immediately.""",
         "NEVER pay an unknown online seller via direct bank transfer &mdash; bank transfers offer virtually zero fraud chargeback protection!",
         "Look for the closed padlock symbol next to the web address before entering any personal or financial information.",
         [
           ("What does the 's' in 'https://' indicate about a website connection?", "[1 Mark]"),
           ("Why is paying with a credit card generally safer for expensive purchases (£100+) than paying with a debit card or bank transfer?", "[2 Marks]"),
           ("What is Two-Factor Authentication (or 3D Secure) in online banking transactions?", "[2 Marks]"),
           ("State two warning signs that an e-commerce website might be fraudulent.", "[2 Marks]")
         ]),

        # Unit 16
        ("Unit 16: Public Digital Services (Gov.uk &amp; NHS)", "Area 4: Transacting",
         """Accessing civic and healthcare digital portals allows UK residents to manage taxation, renew driving licences, and book appointments securely.""",
         """<strong>Navigating Official UK Public Portals:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>GOV.UK:</strong> The single trusted gateway for UK government services (universal credit, tax returns, passport renewal, vehicle road tax, DBS checks).</li>
           <li><strong>Government Gateway:</strong> Secure login system using User ID, password, and SMS mobile security code.</li>
           <li><strong>NHS App &amp; NHS.UK:</strong> Secure digital access to repeat prescription ordering, medical history records, organ donation choices, and GP appointment booking.</li>
           <li><strong>Local Council Portals:</strong> Council tax payments, electoral register enrollment, parking permits, and bulky waste collection.</li>
         </ul>""",
         "A citizen receives a text message: <em>'GOV-UK: You have an unclaimed energy refund of £420. Click http://gov-energy-claim.org to enter your bank details.'</em> Explain how to verify this safely.",
         """1. <strong>Do Not Click:</strong> The link is a fraudulent scam mimicking government branding.<br>2. <strong>Verification:</strong> Official UK government domains always end strictly with <code>.gov.uk</code> (never .org, .net, or .com).<br>3. <strong>Safe Action:</strong> Open a browser independently, navigate to <code>www.gov.uk</code>, log into your personal tax account, and check official messages. Forward the scam SMS to <strong>7726</strong>.""",
         "Government departments (HMRC, DWP) will NEVER send a text asking you to input bank details for a refund via an unverified link!",
         "Bookmark www.gov.uk and use official mobile apps directly from the Apple App Store or Google Play Store.",
         [
           ("Which domain extension is used exclusively by official UK government departments?", "[1 Mark]"),
           ("List three public services that UK citizens can complete online via GOV.UK.", "[3 Marks]"),
           ("How does the NHS App help patients manage their healthcare more efficiently?", "[2 Marks]"),
           ("What number should you forward suspicious UK scam text messages to?", "[1 Mark]")
         ]),

        # Unit 17
        ("Unit 17: Passwords, MFA &amp; Biometrics", "Area 5: Being Safe & Responsible Online",
         """Strong authentication safeguards personal and corporate digital identities against credential stuffing and brute-force dictionary attacks.""",
         """<strong>Building Unbreakable Passwords:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>The Three Random Words Method (NCSC Guidance):</strong> Combine three memorable but unrelated words with numbers and symbols (e.g. <code>Purple!Giraffe#Anchor72</code>).</li>
           <li>Minimum length: at least <strong>12 characters</strong>.</li>
           <li>Never reuse passwords across multiple accounts! If one service is breached, all your accounts are compromised.</li>
           <li><strong>Password Managers:</strong> Encrypted digital vaults (Bitwarden, 1Password) that generate and autofill complex unique passwords.</li>
         </ul>
         <strong>Multi-Factor Authentication (MFA / 2FA):</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>Requires two different types of verification: 1. Something you know (password) + 2. Something you have (authenticator app code) or something you are (fingerprint / Face ID).</li>
         </ul>""",
         "A user uses the password <em>'Summer2026!'</em> for both their personal email and their workplace accounting software. Identify two security risks and suggest an improved strategy.",
         """1. <strong>Risk 1 (Predictability):</strong> Seasons combined with years are among the most common passwords and are cracked in seconds by automated dictionaries.<br>2. <strong>Risk 2 (Credential Reuse):</strong> If one service is compromised, criminals will test those exact credentials on all other accounts.<br><strong>Solution:</strong> Use a password manager to generate unique 16-character passwords and enable Multi-Factor Authentication (MFA) on both accounts.""",
         "Never write passwords on sticky notes attached to your monitor! This is a severe workplace security violation.",
         "Enable Multi-Factor Authentication (MFA) on your email account &mdash; it blocks over 99% of automated credential attacks.",
         [
           ("Explain the UK National Cyber Security Centre (NCSC) 'three random words' password advice.", "[2 Marks]"),
           ("What is Multi-Factor Authentication (MFA), and why is it safer than a password alone?", "[2 Marks]"),
           ("Name two biometric authentication methods commonly used on smartphones.", "[2 Marks]"),
           ("Why is reusing the same password across multiple websites dangerous?", "[1 Mark]")
         ]),

        # Unit 18
        ("Unit 18: Phishing Threats &amp; Social Engineering", "Area 5: Being Safe & Responsible Online",
         """Recognizing fraudulent emails, deceptive text messages (smishing), and social engineering scams prevents malware infection and identity theft.""",
         """<strong>Top Phishing Red Flags:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Deceptive Sender Address:</strong> The display name says 'PayPal', but the actual email address is <code>service@pay-pal-security-update24.co</code>.</li>
           <li><strong>Artificial Urgency:</strong> Demands immediate action: <em>'Your account will be suspended in 2 hours unless you verify now!'</em></li>
           <li><strong>Suspicious Links:</strong> Hover your mouse over the link without clicking to reveal the real destination URL in the status bar.</li>
           <li><strong>Generic Greetings:</strong> <em>'Dear Customer'</em> or <em>'Dear User'</em> instead of your full registered name.</li>
           <li><strong>Malicious Attachments:</strong> Unsolicited files named <code>Invoice_Overdue.zip</code> or <code>Receipt.exe</code>.</li>
         </ul>""",
         "You receive an email claiming to be from your bank requesting you to click a link to update security details. List three immediate actions you should take.",
         """1. <strong>Do Not Click:</strong> Do not click any links or download attachments inside the email.<br>2. <strong>Inspect Sender Address:</strong> Check the domain after the @ symbol to verify if it is the bank's exact official domain.<br>3. <strong>Verify Independently:</strong> Navigate to the bank's official app or call the verified phone number on the back of your payment card.<br>4. <strong>Report:</strong> Forward phishing emails to the UK reporting service: <code>report@phishing.gov.uk</code>.""",
         "Hover before you click! Always check the destination URL preview in your browser before opening any hyperlink.",
         "Legitimate banks will never ask you to transfer money to a 'safe account' or ask for your online banking PIN.",
         [
           ("Explain what a 'phishing' attack is in digital communication.", "[2 Marks]"),
           ("List three visual red flags that indicate an email may be a phishing attempt.", "[3 Marks]"),
           ("What does hovering your mouse over a link in an email allow you to see?", "[1 Mark]"),
           ("To what official email address can UK citizens forward suspicious phishing emails?", "[1 Mark]")
         ]),

        # Unit 19
        ("Unit 19: Privacy Controls &amp; UK GDPR Rights", "Area 5: Being Safe & Responsible Online",
         """Managing online privacy settings and understanding statutory data protection rights protects personal privacy and autonomy.""",
         """<strong>The UK General Data Protection Regulation (UK GDPR):</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Right to be Informed:</strong> Organisations must clearly explain how your data is collected and used.</li>
           <li><strong>Right of Access (SAR):</strong> You can submit a Subject Access Request to receive a free copy of all personal data an organisation holds about you within 1 calendar month.</li>
           <li><strong>Right to Erasure ('Right to be Forgotten'):</strong> Request deletion of your data when it is no longer required.</li>
         </ul>
         <strong>Social Media Privacy Hygiene:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li>Set profiles to <em>'Private / Friends Only'</em> rather than public.</li>
           <li>Disable location tagging on photo posts.</li>
           <li>Audit third-party apps connected to your social accounts and revoke access to inactive apps.</li>
         </ul>""",
         "A customer discovers that a company has shared their telephone number with marketing agencies without their permission. What rights do they have under UK GDPR?",
         """1. <strong>Right to Object:</strong> The individual can immediately demand that the organisation stops processing their data for direct marketing.<br>2. <strong>Right to Erasure:</strong> They can demand their details are deleted from third-party databases.<br>3. <strong>Regulatory Complaint:</strong> They can submit a formal complaint to the <strong>Information Commissioner's Office (ICO)</strong>, which can investigate and issue substantial fines to the offending company.""",
         "Remember that everything posted publicly online contributes to your permanent digital footprint &mdash; employers often screen social profiles!",
         "Check cookie banners: click 'Reject All' or 'Essential Only' to stop websites tracking your browsing across the internet.",
         [
           ("What UK organisation regulates data protection and investigates GDPR breaches?", "[1 Mark]"),
           ("Explain the 'Right of Access' (Subject Access Request) under UK GDPR.", "[2 Marks]"),
           ("State two privacy adjustments you can make on social media to prevent identity theft.", "[2 Marks]"),
           ("What is a 'digital footprint'?", "[1 Mark]")
         ]),

        # Unit 20
        ("Unit 20: Digital Wellbeing &amp; Ergonomics", "Area 5: Being Safe & Responsible Online",
         """Maintaining a healthy relationship with digital technology requires physical ergonomic setup, managing screen fatigue, and establishing work-life boundaries.""",
         """<strong>Workplace Ergonomics Checklist:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>Monitor Position:</strong> Top of screen aligned at eye level, approximately arm's length away (50–70 cm).</li>
           <li><strong>Seating Posture:</strong> Feet flat on floor or footrest; lower back supported by chair lumbar curve; elbows at 90 degrees level with desk.</li>
           <li><strong>Wrist Support:</strong> Keep wrists straight when typing; do not bend hands back awkwardly.</li>
         </ul>
         <strong>Managing Screen Fatigue &amp; Wellbeing:</strong>
         <ul style="margin:4px 0 0 16px;">
           <li><strong>The 20-20-20 Rule:</strong> Every 20 minutes, look at an object 20 feet away for at least 20 seconds to relax eye muscles.</li>
           <li><strong>Blue Light Reduction:</strong> Turn on 'Night Light' or warm display mode during evening hours to support healthy sleep cycles.</li>
           <li><strong>Digital Boundaries:</strong> Turn off work message notifications outside scheduled employment hours.</li>
         </ul>""",
         "An employee working from a laptop on the sofa reports chronic neck pain and evening headaches. Identify two ergonomic mistakes and suggest two solutions.",
         """1. <strong>Mistake 1:</strong> Looking down at a low laptop screen strains cervical neck vertebrae.<br>2. <strong>Mistake 2:</strong> Slouching on a soft sofa provides zero lumbar lower back support.<br><strong>Solutions:</strong><br>&bull; Place laptop on a desk using a laptop stand so the screen is at eye level, paired with a separate external keyboard and mouse.<br>&bull; Sit in an adjustable office chair with firm lumbar support, taking regular micro-breaks.""",
         "Never work on a laptop for hours with your neck bent downwards! Use a laptop stand with an external keyboard.",
         "Practice the 20-20-20 rule daily to reduce headaches and digital eye strain.",
         [
           ("Explain the '20-20-20 rule' used to combat digital eye strain.", "[2 Marks]"),
           ("Where should the top of your computer monitor be positioned relative to your eyes for good ergonomics?", "[1 Mark]"),
           ("State two physical symptoms of poor computer desk ergonomics.", "[2 Marks]"),
           ("Why is using an external keyboard and mouse recommended when using a laptop on a desk?", "[1 Mark]")
         ])
    ]

    for u_idx, (u_title, strand, overview, fundamentals, exam_q, model_ans, trap, tip, drills) in enumerate(dfs_units_data, 1):
        # 2 Pages per Unit: Pages 4 to 43
        base_page = 4 + (u_idx - 1) * 2

        # Unit Page 1: Theory, Concept, Model Scenario
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Essential Digital Skills</div>
    <div class="page-header-strand">{strand}</div>
  </div>

  <h2>{u_title}</h2>
  <div class="card-concept" style="margin-bottom:6px;">
    {overview}
  </div>

  <div class="card-method" style="margin-bottom:6px;">
    {fundamentals}
  </div>

  <div class="card-exam" style="margin-bottom:6px;">
    <h3 style="color:#7c3aed; margin-top:0;">Model Practical Scenario &bull; Examiner Solution</h3>
    <p><strong>Scenario:</strong> {exam_q}</p>
    <div style="background:#ffffff; border:1px solid #e9d5ff; padding:5px 8px; border-radius:4px; font-size:7.8pt;">
      {model_ans}
    </div>
  </div>

  <div class="grid-2" style="margin-top:auto;">
    <div class="card-trap" style="margin-bottom:0;">
      <strong>Common Pitfall:</strong> {trap}
    </div>
    <div class="card-tip" style="margin-bottom:0;">
      <strong>Pro Tip:</strong> {tip}
    </div>
  </div>

  <div class="page-footer">
    <div>{u_title} &bull; Study &amp; Model Guide</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Unit Page 2: Graded Practice Drills & Workspace
        drills_html = ""
        for d_idx, (d_q, d_marks) in enumerate(drills, 1):
            drills_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>Question {d_idx}:</strong> <span class="mark-badge" style="background:#0284c7;">{d_marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:8pt;">{d_q}</p>
  <div class="workspace-ruled" style="min-height:50px;">Show answer and technical explanation here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Essential Digital Skills</div>
    <div class="page-header-strand">{strand} &bull; Practice Drills</div>
  </div>

  <h2>{u_title} &bull; Practical Graded Drills</h2>
  <p style="margin-bottom:8px;">Complete the practical questions below. Use precise technical terminology to secure full marks.</p>

  {drills_html}

  <div class="card-tip" style="margin-top:auto;">
    <strong>Self-Check:</strong> Review your technical vocabulary. Ensure all file extensions, keyboard shortcuts, and security protocols are accurately stated.
  </div>

  <div class="page-footer">
    <div>{u_title} &bull; Graded Practice Drills</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART II: MASTER SOFTWARE WORKFLOW LABORATORIES (10 Pages, Pages 44 to 53)
    # -------------------------------------------------------------
    labs_data = [
        # Lab 1: Word Processing Masterclass
        ("Software Lab 1: Professional Word Processing &amp; Document Design",
         """This laboratory trains you in the end-to-end production of formal enterprise documentation using Microsoft Word and Google Docs. Mastery of paragraph styles, section breaks, and mail merge is essential for Level 1/Level 2 qualifications.""",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Workflow Stage</th><th>Ribbon Path &amp; Shortcut</th><th>Action &amp; Professional Standard</th></tr>
           <tr><td><strong>1. Page Setup</strong></td><td><code>Layout &rarr; Margins &rarr; Normal (2.54cm)</code></td><td>Set uniform page borders; verify A4 portrait paper size.</td></tr>
           <tr><td><strong>2. Style Hierarchy</strong></td><td><code>Home &rarr; Styles Pane (Ctrl+Alt+1, 2)</code></td><td>Apply Heading 1 for document titles; Heading 2 for subtopics; Normal for paragraphs.</td></tr>
           <tr><td><strong>3. Section Breaks</strong></td><td><code>Layout &rarr; Breaks &rarr; Next Page</code></td><td>Isolate landscape pages or uncouple header/footer pagination numbering.</td></tr>
           <tr><td><strong>4. Mail Merge</strong></td><td><code>Mailings &rarr; Start Mail Merge &rarr; Letters</code></td><td>Connect Excel recipient database; insert merge fields: <code>&laquo;First_Name&raquo;</code>.</td></tr>
           <tr><td><strong>5. PDF Export</strong></td><td><code>File &rarr; Export &rarr; Create PDF/XPS</code></td><td>Lock layout formatting, embed font rendering, and secure against alterations.</td></tr>
         </table>""",
         [
           ("Lab Task 1.1: Multi-Page Formatting", "[4 Marks]", "Explain how to insert a Landscape orientation page containing a wide finance table between two Portrait pages without altering the orientation of the surrounding document."),
           ("Lab Task 1.2: Mail Merge Implementation", "[4 Marks]", "Detail the step-by-step procedure to generate 60 personalized client award certificates from an Excel spreadsheet named 'Recipients.xlsx'."),
           ("Lab Task 1.3: Document Accessibility", "[3 Marks]", "State three design choices that make a digital word document accessible to visually impaired colleagues using screen readers.")
         ]),

        # Lab 2: Workplace Spreadsheets Masterclass
        ("Software Lab 2: Workplace Spreadsheets, Modeling &amp; Data Analysis",
         """Spreadsheet modeling represents over 35% of all EDSQ practical marks. You must master absolute cell referencing ($A$1), logical conditional formulas, and data visual formatting.""",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Formula / Tool</th><th>Syntax / Menu Path</th><th>Function &amp; Examiner Benchmark</th></tr>
           <tr><td><strong>Absolute Reference</strong></td><td><code>$F$2</code> (Press <code>F4</code> key)</td><td>Locks row and column coordinate when formula is replicated down rows.</td></tr>
           <tr><td><strong>IF Logical Test</strong></td><td><code>=IF(C4&gt;=50, "Pass", "Refer")</code></td><td>Evaluates condition; returns value if true, alternate value if false.</td></tr>
           <tr><td><strong>VLOOKUP / XLOOKUP</strong></td><td><code>=VLOOKUP(A2, Products!$A$2:$D$50, 3, FALSE)</code></td><td>Searches first column of table; extracts value from specified column index.</td></tr>
           <tr><td><strong>Conditional Formatting</strong></td><td><code>Home &rarr; Conditional Formatting &rarr; Highlight</code></td><td>Applies automated colour fills (e.g. red fill if overdue; green fill if paid).</td></tr>
           <tr><td><strong>Chart Construction</strong></td><td><code>Insert &rarr; Recommended Charts (Alt+F1)</code></td><td>Generates visual charts with dual axis labels and informative titles.</td></tr>
         </table>""",
         [
           ("Lab Task 2.1: Absolute Cell Referencing", "[4 Marks]", "A spreadsheet applies a VAT rate stored in cell G1 (20%) to net prices in column C. Explain why the formula <code>=C4*G1</code> fails when copied down to row 5, and state the correct syntax."),
           ("Lab Task 2.2: Nested Logical Decisions", "[4 Marks]", "Write an exact spreadsheet formula in cell E2 that awards a 10% discount on sales (column D) if order quantity (column C) is 50 or greater, otherwise 0%."),
           ("Lab Task 2.3: Professional Data Presentation", "[3 Marks]", "Describe three formatting steps required to turn an unformatted block of numbers into an executive financial summary.")
         ]),

        # Lab 3: Business Presentation Slide Decks
        ("Software Lab 3: Presentation Slide Decks &amp; Visual Communication",
         """Presenting complex commercial data visually requires mastery of Slide Master templating, animation restraint, media integration, and audience engagement tools.""",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Presentation Feature</th><th>Application Path</th><th>Best Practice &amp; Professional Standard</th></tr>
           <tr><td><strong>Slide Master Layout</strong></td><td><code>View &rarr; Slide Master</code></td><td>Enforce uniform corporate branding, logo placement, and header typography.</td></tr>
           <tr><td><strong>Visual Hierarchy</strong></td><td><code>Home &rarr; Layouts</code></td><td>Single primary takeaway per slide; minimum 28pt heading and 18pt body text.</td></tr>
           <tr><td><strong>Media Embedding</strong></td><td><code>Insert &rarr; Video / Audio / Icons</code></td><td>Compress media files to prevent bloated file sizes; include descriptive captions.</td></tr>
           <tr><td><strong>Transition Restraint</strong></td><td><code>Transitions &rarr; Fade &rarr; Apply to All</code></td><td>Use uniform 0.5s fade transitions; strictly avoid jarring spinning animations.</td></tr>
           <tr><td><strong>Presenter View</strong></td><td><code>Slide Show &rarr; Use Presenter View (Alt+F5)</code></td><td>Enables viewing elapsed timers and private speaker notes while audience sees slides.</td></tr>
         </table>""",
         [
           ("Lab Task 3.1: Slide Master Efficiency", "[4 Marks]", "Describe the operational steps to insert a corporate logo onto all 30 slides of a presentation simultaneously so it cannot be accidentally moved during editing."),
           ("Lab Task 3.2: Visual Communication Critique", "[4 Marks]", "A slide contains 14 lines of tiny text, 4 bright primary background colours, and flashing star animations. Provide a professional design critique and 4 actionable improvements."),
           ("Lab Task 3.3: Presenter View Setup", "[3 Marks]", "Explain how Presenter View enables confident, professional public delivery during a live client meeting.")
         ]),

        # Lab 4: Email Client & Scheduling Systems
        ("Software Lab 4: Professional Email, Contact Management &amp; Scheduling",
         """Efficient digital communication in Microsoft Outlook or Google Workspace requires automated mail filtering, calendar appointment scheduling, and contact privacy protection.""",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>System Capability</th><th>Navigation Path</th><th>Action &amp; Practical Standard</th></tr>
           <tr><td><strong>Automated Mail Rules</strong></td><td><code>Home &rarr; Rules &rarr; Create Rule</code></td><td>Automatically sorts incoming emails into client or priority subfolders based on sender or subject.</td></tr>
           <tr><td><strong>Recurring Calendar Invites</strong></td><td><code>Calendar &rarr; New Meeting &rarr; Recurrence</code></td><td>Coordinates ongoing departmental meetings with automated Teams/Zoom video links.</td></tr>
           <tr><td><strong>Out of Office Auto-Reply</strong></td><td><code>File &rarr; Automatic Replies</code></td><td>Sets external and internal automatic responses during annual leave with alternate contact details.</td></tr>
           <tr><td><strong>Distribution Lists (BCC)</strong></td><td><code>Contacts &rarr; New Contact Group</code></td><td>Aggregates multiple client emails for simultaneous messaging while preserving GDPR anonymity.</td></tr>
           <tr><td><strong>Digital Signatures</strong></td><td><code>Insert &rarr; Signature</code></td><td>Embeds legal disclaimer, company registration number, and professional contact credentials.</td></tr>
         </table>""",
         [
           ("Lab Task 4.1: Automated Inbox Management", "[4 Marks]", "Outline the steps to configure an email rule that automatically moves all incoming messages containing the word 'Invoice' into an 'Accounts_Payable' folder and flags them for follow-up."),
           ("Lab Task 4.2: Conflict-Free Meeting Scheduling", "[4 Marks]", "Describe how to use the 'Scheduling Assistant' in a calendar application to coordinate a 1-hour board meeting for 6 busy managers without manual email ping-pong."),
           ("Lab Task 4.3: Professional Out-of-Office Notice", "[3 Marks]", "Draft a complete, professional Out-of-Office auto-reply including all statutory and courtesy elements.")
         ]),

        # Lab 5: Cloud Collaboration & Shared Drives
        ("Software Lab 5: Cloud Collaboration, File Versioning &amp; Permissions",
         """Working in shared enterprise environments (Microsoft OneDrive, SharePoint, Google Drive) requires strict governance over sharing links, version recovery, and document co-authoring.""",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Cloud Governance Action</th><th>Interface Menu Path</th><th>Security Standard &amp; Risk Mitigation</th></tr>
           <tr><td><strong>Role-Based Access</strong></td><td><code>Share &rarr; Manage Access &rarr; Specific People</code></td><td>Restricts editing rights; grants 'Viewer' (read-only) or 'Editor' to authenticated emails.</td></tr>
           <tr><td><strong>Version History Recovery</strong></td><td><code>File &rarr; Info &rarr; Version History</code></td><td>Audits chronological edits; restores previous versions if data is corrupted or deleted.</td></tr>
           <tr><td><strong>Live Co-Authoring</strong></td><td><code>Real-Time Presence Indicators</code></td><td>Simultaneous multi-user editing; displays coloured cursor tags and locks edited paragraphs.</td></tr>
           <tr><td><strong>Expiring Share Links</strong></td><td><code>Link Settings &rarr; Set Expiration Date</code></td><td>Automatically revokes third-party access after 7 or 30 days to prevent orphaned data access.</td></tr>
           <tr><td><strong>Password-Protected Links</strong></td><td><code>Link Settings &rarr; Set Password</code></td><td>Mandates external authentication code before confidential attachments can be downloaded.</td></tr>
         </table>""",
         [
           ("Lab Task 5.1: Version History Restoration", "[4 Marks]", "A junior colleague accidentally deletes three essential worksheets from a shared Cloud budget workbook. Describe how to recover the lost data using Version History."),
           ("Lab Task 5.2: Shared Cloud Permission Governance", "[4 Marks]", "Explain the crucial security differences between sharing a file via: a) 'Anyone with the link can edit' &nbsp;&nbsp; b) 'Specific people can view'. Identify the associated risks."),
           ("Lab Task 5.3: Co-Authoring Conflict Prevention", "[3 Marks]", "State two guidelines for teams working concurrently on the same live cloud document to avoid conflicting edits.")
         ])
    ]

    for lab_idx, (lab_title, lab_desc, lab_table, lab_tasks) in enumerate(labs_data, 1):
        base_page = 44 + (lab_idx - 1) * 2

        # Lab Page 1: Architecture & Technical Table
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Software Labs</div>
    <div class="page-header-strand">Laboratory {lab_idx} of 5 &bull; Hands-On Architecture</div>
  </div>

  <h2>{lab_title}</h2>
  <div class="card-concept" style="margin-bottom:6px;">
    {lab_desc}
  </div>

  <div class="card-method" style="margin-bottom:6px;">
    <h3 style="color:#16a34a; margin-top:0;">Professional Workflow Reference Table</h3>
    {lab_table}
  </div>

  <div class="card-exam" style="margin-top:auto;">
    <h3 style="color:#7c3aed; margin-top:0;">Industry Performance Standard</h3>
    <p style="font-size:7.8pt; margin:0;">Awarding bodies require candidates to demonstrate not just theoretical understanding, but active procedural fluency: knowing exactly which ribbon tab, dialog launcher, or shortcut executes the task cleanly under exam time constraints.</p>
  </div>

  <div class="page-footer">
    <div>Software Lab {lab_idx} &bull; Technical Architecture</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Lab Page 2: Hands-On Exercises & Workspaces
        tasks_html = ""
        for t_title, t_marks, t_text in lab_tasks:
            tasks_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>{t_title}:</strong> <span class="mark-badge" style="background:#0284c7;">{t_marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:7.8pt;">{t_text}</p>
  <div class="workspace-ruled" style="min-height:55px;">Show step-by-step technical execution here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Software Labs</div>
    <div class="page-header-strand">Laboratory {lab_idx} of 5 &bull; Practical Execution</div>
  </div>

  <h2>{lab_title} &bull; Practical Execution</h2>
  <p style="margin-bottom:8px;">Execute the software laboratory tasks below. Detail exact software paths, formula syntax, and technical rationales.</p>

  {tasks_html}

  <div class="card-tip" style="margin-top:auto;">
    <strong>Laboratory Benchmark:</strong> Ensure your formula syntax is strictly valid and that all dialog box parameters are fully articulated.
  </div>

  <div class="page-footer">
    <div>Software Lab {lab_idx} &bull; Practical Execution</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART III: CYBERSECURITY, PRIVACY & COMPLIANCE AUDITS (4 Pages, Pages 54 to 57)
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Security &amp; Compliance</div>
    <div class="page-header-strand">Audit Checklist 1 &bull; Cyber Threat Defense</div>
  </div>

  <h2>Workplace Cyber Threat Vectors &amp; Phishing Defense Audit</h2>
  <p>Cybersecurity is an institutional responsibility. Over 88% of UK enterprise data breaches originate from social engineering. Review and apply this comprehensive threat mitigation checklist:</p>

  <div class="grid-2" style="font-size:7.5pt;">
    <div class="card-trap" style="padding:6px 10px;">
      <h3 style="color:#dc2626; margin-top:0;">Top Social Engineering Attack Vectors</h3>
      <ul style="margin:2px 0 0 12px; padding:0;">
        <li><strong>Spear Phishing:</strong> Highly targeted deceptive emails addressing recipients by name, referencing real workplace projects to induce credential entry.</li>
        <li><strong>Smishing &amp; Vishing:</strong> SMS or telephone impersonation claiming urgent banking anomalies or unpaid courier shipping fees.</li>
        <li><strong>Watering Hole &amp; Drive-by:</strong> Compromised industry websites that infect visitor browsers with background malware.</li>
        <li><strong>Baiting &amp; Rogue USBs:</strong> Malware-loaded USB drives deliberately dropped in office car parks or communal breakrooms.</li>
      </ul>
    </div>

    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Operational Defense Architecture</h3>
      <ul style="margin:2px 0 0 12px; padding:0;">
        <li><strong>Sender SPF/DKIM Verification:</strong> Check underlying authentication headers to detect spoofed display names.</li>
        <li><strong>Domain Sandboxing:</strong> Open untrusted attachments strictly within isolated virtualised enterprise sandboxes.</li>
        <li><strong>Multi-Factor Hardening:</strong> Mandate biometric or hardware FIDO2 security keys; deprecate SMS verification where possible.</li>
        <li><strong>NCSC Incident Reporting:</strong> Report malicious phishing emails to <code>report@phishing.gov.uk</code> and suspicious texts to <code>7726</code>.</li>
      </ul>
    </div>
  </div>

  <div class="card-practice" style="border-left-color:#0284c7; margin-top:6px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Workplace Security Incident Protocol:</strong><br>
    If an employee accidentally clicks a suspicious link or enters credentials into an unverified portal:
    <ol style="margin:2px 0 0 14px; padding:0;">
      <li><strong>Disconnect Instantly:</strong> Unplug the Ethernet network cable and disable Wi-Fi to stop lateral malware propagation.</li>
      <li><strong>Notify IT Security:</strong> Immediately contact the Information Security Officer via telephone (extension 2222).</li>
      <li><strong>Credential Reset:</strong> Reset corporate passwords immediately from an uncompromised secondary device.</li>
    </ol>
  </div>

  <div class="page-footer">
    <div>Cybersecurity Audit 1 &bull; Threat Vectors &amp; Incident Protocols</div>
    <div class="page-num">Page 54</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Security &amp; Compliance</div>
    <div class="page-header-strand">Audit Checklist 1 &bull; Practical Audit Drills</div>
  </div>

  <h2>Cybersecurity Defense &bull; Workplace Audit Tasks</h2>
  <p style="margin-bottom:8px;">Evaluate the security scenarios below and state the exact procedural responses required.</p>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 1.1: Phishing Deconstruction</strong> <span class="mark-badge" style="background:#0284c7;">[4 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">An email arrives titled <em>"HMRC: Final Notice Tax Rebate Pending"</em> from <code>refunds@hmrc-tax-portal-gov.co.uk</code> containing a PDF named <code>Claim_Form_2026.exe</code>. Identify 4 distinct red flags proving this is malicious.</p>
    <div class="workspace-ruled" style="min-height:55px;">Detail the 4 technical red flags here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 1.2: Password Vault Implementation</strong> <span class="mark-badge" style="background:#0284c7;">[4 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">Explain how an enterprise password manager functions and describe how it eliminates both credential fatigue and dictionary cracking attacks.</p>
    <div class="workspace-ruled" style="min-height:55px;">Detail password manager mechanics here...</div>
  </div>

  <div style="margin-bottom:6px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 1.3: Incident Containment Steps</strong> <span class="mark-badge" style="background:#0284c7;">[3 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">A coworker realizes they have just entered their corporate login credentials into a fraudulent web page. State the first three actions they must take immediately.</p>
    <div class="workspace-ruled" style="min-height:50px;">State the 3 containment actions here...</div>
  </div>

  <div class="page-footer">
    <div>Cybersecurity Audit 1 &bull; Practical Audit Drills</div>
    <div class="page-num">Page 55</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Security &amp; Compliance</div>
    <div class="page-header-strand">Audit Checklist 2 &bull; Device Hardening &amp; GDPR</div>
  </div>

  <h2>Device Hardening, Backup Protocols &amp; UK GDPR Compliance</h2>
  <p>Institutional digital compliance mandates physical device security, immutable data backups, and adherence to the statutory principles of UK GDPR:</p>

  <div class="grid-2" style="font-size:7.5pt;">
    <div class="card-concept" style="border-left-color:#0284c7; padding:6px 10px;">
      <h3 style="color:#0284c7; margin-top:0;">Device &amp; Endpoint Hardening</h3>
      <ul style="margin:2px 0 0 12px; padding:0;">
        <li><strong>Full-Disk Encryption:</strong> Enable BitLocker (Windows) or FileVault (macOS) to protect data if laptops are stolen.</li>
        <li><strong>Automatic Screen Timeout:</strong> Set screens to lock automatically after 3 minutes of inactivity (Win+L key).</li>
        <li><strong>Patch Management:</strong> Install operating system and application security updates within 14 days of release.</li>
        <li><strong>Network Segmentation:</strong> Isolate guest Wi-Fi networks from core corporate database infrastructure.</li>
      </ul>
    </div>

    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">UK GDPR Core Data Principles</h3>
      <ul style="margin:2px 0 0 12px; padding:0;">
        <li><strong>Lawfulness, Fairness &amp; Transparency:</strong> Clear legal basis and privacy notice for collecting data.</li>
        <li><strong>Purpose Limitation:</strong> Data must be collected only for specified, explicit, and legitimate purposes.</li>
        <li><strong>Data Minimisation:</strong> Restrict collection strictly to what is necessary for the stated purpose.</li>
        <li><strong>Accuracy &amp; Storage Limitation:</strong> Keep data accurate; delete immediately once retention period expires.</li>
      </ul>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px; font-size:7.5pt;">
    <h3 style="color:#d97706; margin-top:0;">The 3-2-1-1-0 Enterprise Backup Standard</h3>
    <p style="margin:0;">Maintain <strong>3</strong> copies of data on <strong>2</strong> different media types, with <strong>1</strong> off-site copy, <strong>1</strong> offline air-gapped immutable copy (protected against ransomware), and <strong>0</strong> errors verified through periodic restoration drills.</p>
  </div>

  <div class="page-footer">
    <div>Cybersecurity Audit 2 &bull; Hardening &amp; GDPR Compliance</div>
    <div class="page-num">Page 56</div>
  </div>
</div>
""")

    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Security &amp; Compliance</div>
    <div class="page-header-strand">Audit Checklist 2 &bull; Compliance Audit Drills</div>
  </div>

  <h2>Device Hardening &amp; GDPR Compliance &bull; Audit Drills</h2>
  <p style="margin-bottom:8px;">Complete the regulatory compliance audits below. Cite statutory principles and best-practice controls.</p>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 2.1: Data Minimisation Audit</strong> <span class="mark-badge" style="background:#0284c7;">[4 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">An online newsletter registration form asks users for: Full Name, Email Address, Home Street Address, Date of Birth, and Mother's Maiden Name. Evaluate this against the UK GDPR principle of Data Minimisation.</p>
    <div class="workspace-ruled" style="min-height:55px;">Show GDPR evaluation here...</div>
  </div>

  <div style="margin-bottom:8px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 2.2: Subject Access Request (SAR) Protocol</strong> <span class="mark-badge" style="background:#0284c7;">[4 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">A former customer emails demanding all records, phone call transcripts, and purchase histories your company holds about them. State the legal deadline to respond, whether a fee can be charged, and the required data format.</p>
    <div class="workspace-ruled" style="min-height:55px;">Show SAR protocol requirements here...</div>
  </div>

  <div style="margin-bottom:6px;">
    <div style="display:flex; justify-content:space-between;"><strong>Audit Task 2.3: Ransomware Defense Audit</strong> <span class="mark-badge" style="background:#0284c7;">[3 Marks]</span></div>
    <p style="font-size:7.8pt; margin:2px 0;">Explain why storing backups on a permanently connected network shared drive (NAS) does not protect an organisation against modern ransomware attacks, and describe the solution.</p>
    <div class="workspace-ruled" style="min-height:50px;">Show ransomware defense solution here...</div>
  </div>

  <div class="page-footer">
    <div>Cybersecurity Audit 2 &bull; Compliance Audit Drills</div>
    <div class="page-num">Page 57</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART IV: 3 COMPLETE PRACTICAL MOCK EXAMINATIONS (12 Pages, Pages 58 to 69)
    # -------------------------------------------------------------
    mock_exams_data = [
        # Mock 1
        ("Practical Mock 1: Community Charity Gala Digital Campaign",
         "Community Outreach Trust (Registered Charity #104829)",
         "You are the Digital Communications Officer for a regional charity. You must organize the annual fundraising gala campaign: analyzing ticket and sponsorship revenue using a spreadsheet, designing a promotional flyer in a word processor, coordinating volunteer communication via email, and ensuring donor data protection.",
         [
           ("Task 1.1: Financial Budget Modeling", "[8 Marks]",
            "A spreadsheet records ticket sales and gala costs across rows 4 to 15. Column B is 'Ticket Category', Column C is 'Price (£)', Column D is 'Units Sold', Column E is 'Gross Income'.<br>a) Write the exact formula for cell E4 to calculate Gross Income.<br>b) Write the formula in cell E16 to calculate Total Gala Revenue.<br>c) Write a formula in cell F4 that checks if Units Sold (D4) exceeds the target of 50 units, displaying 'Target Met' if true, otherwise 'Under Target'."),
           ("Task 1.2: Visual Fundraising Chart", "[5 Marks]",
            "Describe how to create a 3D or 2D Column Chart comparing Gross Income across all 5 ticket tiers. Detail the exact data range to select, required chart title, and two axis labels.")
         ],
         [
           ("Task 1.3: Event Promotional Flyer", "[8 Marks]",
            "In your word processor, design the layout for an accessible digital gala flyer. State four formatting features you would implement to ensure maximum readability, visual appeal, and screen-reader accessibility."),
           ("Task 1.4: Professional Donor Outreach Email", "[5 Marks]",
            "Draft a professional sponsorship invitation email to a local corporate director (m.harrison@vanguard.co.uk). Include an appropriate Subject Line, salutation, value proposition, and formal sign-off."),
           ("Task 1.5: Donor Privacy & GDPR Safeguard", "[4 Marks]",
            "When sending the event details to 120 individual ticket holders, what email field MUST you use to insert their email addresses, and what specific GDPR violation does this prevent?")
         ]),

        # Mock 2
        ("Practical Mock 2: Healthcare Clinic Patient Onboarding & Records",
         "St Jude Community Health &amp; Diagnostic Centre",
         "You work as the Practice Digital Coordinator. The clinic is transitioning from paper records to an integrated electronic health record (EHR) database. You must configure patient intake spreadsheets, generate automated confirmation letters using Mail Merge, and establish strict confidentiality protocols.",
         [
           ("Task 2.1: Clinic Schedule Spreadsheet Analysis", "[8 Marks]",
            "A spreadsheet monitors patient appointment durations in minutes in Column D (rows 2 to 45).<br>a) State the formula to calculate the average patient consultation time.<br>b) State the formula to identify the longest consultation time.<br>c) Write a formula in cell E2 that flags 'Review Needed' if consultation time (D2) exceeds 30 minutes, otherwise 'Standard'."),
           ("Task 2.2: Attendance Proportions Visualisation", "[5 Marks]",
            "You need to display the percentage breakdown of appointment types (GP, Nurse, Phlebotomy, Physiotherapy) for the monthly board report. Recommend the best chart type and explain how to format data labels.")
         ],
         [
           ("Task 2.3: Patient Appointment Mail Merge", "[8 Marks]",
            "Describe the complete operational workflow to merge an appointment confirmation template in Word with patient records in 'Appointments_Oct.xlsx'. Detail the ribbon tabs, placeholder fields, and final review check."),
           ("Task 2.4: Confidential Patient Portal Email", "[5 Marks]",
            "A patient emails asking for their medical blood test results to be sent via an unencrypted standard email attachment. Draft a polite, professional reply explaining clinic data security policy and guiding them to access the secure NHS App."),
           ("Task 2.5: Caldicott Principle & Physical Security", "[4 Marks]",
            "State two physical security precautions clinic reception staff must maintain regarding workstation screens and printouts to protect confidential patient health data.")
         ]),

        # Mock 3
        ("Practical Mock 3: Retail Boutique E-Commerce Transition",
         "Heritage Artisans & Co. (Independent Retail Enterprise)",
         "You are hired to manage the digital transformation of an established brick-and-mortar retail business launching an online store. You must build an inventory and profit-margin spreadsheet, design an investor pitch slide deck, and resolve online customer order queries.",
         [
           ("Task 3.1: Inventory & Profit Margin Modeling", "[8 Marks]",
            "A stock spreadsheet lists wholesale cost in Column C and retail selling price in Column D.<br>a) Write the exact formula in cell E2 to calculate gross profit margin: <code>(Price - Cost) / Price</code> expressed as a percentage.<br>b) The store applies a seasonal 15% discount stored in cell H1. Write the formula in cell F2 to calculate discounted price using an absolute cell reference.<br>c) Write a formula in cell G2 to find the total inventory value of item 2 (Units in B2 multiplied by Cost in C2)."),
           ("Task 3.2: Best-Seller Comparison Chart", "[5 Marks]",
            "Describe how to generate a Bar Chart comparing stock quantities across 8 product categories. Detail selection ranges and title conventions.")
         ],
         [
           ("Task 3.3: Investor Pitch Slide Deck", "[8 Marks]",
            "Outline a 4-slide presentation deck proposing the e-commerce transition to store investors. Specify the layout, slide title, and concise content points for each slide following the 6 &times; 6 rule."),
           ("Task 3.4: Customer Service Complaint Resolution", "[5 Marks]",
            "An online customer emails complaining that an artisan ceramic bowl arrived cracked due to poor packaging. Draft a prompt, courteous, and professional resolution email offering a replacement and prepaid return label."),
           ("Task 3.5: E-Commerce Payment Gateway Security", "[4 Marks]",
            "State two cybersecurity checks the business must verify when choosing an online payment gateway (e.g. Stripe / PayPal) to process customer debit card transactions safely.")
         ])
    ]

    for m_idx, (m_title, m_org, m_scenario, m_sec1, m_sec2) in enumerate(mock_exams_data, 1):
        base_page = 58 + (m_idx - 1) * 4

        # Mock Page 1: Scenario Overview & Section 1 (Spreadsheets)
        s1_html = ""
        for t_title, t_marks, t_text in m_sec1:
            s1_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>{t_title}:</strong> <span class="mark-badge" style="background:#0284c7;">{t_marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:7.8pt;">{t_text}</p>
  <div class="workspace-ruled" style="min-height:55px;">Show formula syntax and spreadsheet methods here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Examination</div>
    <div class="page-header-strand">Mock Assignment {m_idx} of 3 &bull; Section 1</div>
  </div>

  <h2>{m_title}</h2>
  <div class="card-concept" style="margin-bottom:6px;">
    <strong>Organisation:</strong> {m_org}<br>
    <strong>Assignment Brief:</strong> {m_scenario}
  </div>

  <div class="card-method" style="margin-bottom:6px;">
    <strong>Section 1: Data Modeling &amp; Spreadsheet Analysis (13 Marks &bull; 35 Minutes)</strong>
  </div>

  {s1_html}

  <div class="page-footer">
    <div>Mock Assignment {m_idx} &bull; Section 1 (Spreadsheet Analysis)</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Mock Page 2: Section 1 Grid / Workspace
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Examination</div>
    <div class="page-header-strand">Mock Assignment {m_idx} of 3 &bull; Section 1 Modeling Grid</div>
  </div>

  <h2>Section 1: Candidate Spreadsheet Architecture Grid</h2>
  <p style="margin-bottom:6px;">Use this grid workspace to plan cell layouts, formulate coordinate mappings, and draft chart configurations:</p>

  <div class="workspace-grid" style="min-height:710px; font-size:8pt;">
    Draw cell coordinates, columns, rows, formulas, and chart layout sketches here...
  </div>

  <div class="page-footer">
    <div>Mock Assignment {m_idx} &bull; Section 1 Grid Workspace</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

        # Mock Page 3: Section 2 Tasks (Documents, Comms & Security)
        s2_html = ""
        for t_title, t_marks, t_text in m_sec2:
            s2_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>{t_title}:</strong> <span class="mark-badge" style="background:#0284c7;">{t_marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:7.8pt;">{t_text}</p>
  <div class="workspace-ruled" style="min-height:55px;">Show document layouts, draft emails, and security protocols here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Examination</div>
    <div class="page-header-strand">Mock Assignment {m_idx} of 3 &bull; Section 2</div>
  </div>

  <h2>Section 2: Document Creation, Digital Comms &amp; Safety (17 Marks &bull; 40 Mins)</h2>
  <p style="margin-bottom:6px;">Execute the workplace communication and security tasks below:</p>

  {s2_html}

  <div class="page-footer">
    <div>Mock Assignment {m_idx} &bull; Section 2 (Documents &amp; Comms)</div>
    <div class="page-num">Page {base_page + 2}</div>
  </div>
</div>
""")

        # Mock Page 4: Section 2 Writing Booklet / Workspace
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Examination</div>
    <div class="page-header-strand">Mock Assignment {m_idx} of 3 &bull; Section 2 Response Booklet</div>
  </div>

  <h2>Section 2: Candidate Professional Writing &amp; Draft Booklet</h2>
  <p style="margin-bottom:6px;">Draft your formal workplace email or promotional text response below (Target: 120–160 words):</p>

  <div class="workspace-ruled" style="min-height:710px; line-height:22px; font-size:8.5pt;">
    Write your full professional draft here (including Subject line, salutation, body text, and sign-off)...
  </div>

  <div class="page-footer">
    <div>Mock Assignment {m_idx} &bull; Section 2 Candidate Booklet</div>
    <div class="page-num">Page {base_page + 3}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PART V: COMPREHENSIVE EXPLANATORY ANSWER KEYS (14 Pages, Pages 70 to 83)
    # -------------------------------------------------------------
    # Pages 70 to 79: Units 1 to 20 Answer Keys (10 pages, 2 units per page)
    unit_answers = [
        # Page 70: Units 1 & 2
        ("Units 1 &amp; 2: Hardware, Systems &amp; File Management",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 1: Hardware, Operating Systems &amp; Settings (Page 5)</strong><br>
           1. a) Barcode scanner: <strong>Input</strong> [1m] &bull; b) Laser printer: <strong>Output</strong> [1m] &bull; c) Touchscreen: <strong>Both (Input &amp; Output)</strong> [1m].<br>
           2. Navigate to: <code>Settings &rarr; Display</code> (or Control Panel &rarr; Display Settings &rarr; Scale and Layout) [1m].<br>
           3. An Operating System manages computer hardware resources (CPU, RAM, storage), facilitates peripheral device communication via drivers, and provides a graphical user interface (GUI) to run software applications [2m].<br>
           4. Open Task Manager by pressing <code>Ctrl + Shift + Esc</code> (or Ctrl + Alt + Del), highlight the frozen application in the Processes list, and click <strong>'End Task'</strong> [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 2: File Organisation &amp; Cloud Syncing (Page 7)</strong><br>
           1. <strong>.pdf (Portable Document Format)</strong> &mdash; preserves exact formatting and cannot be easily edited [1m].<br>
           2. Root folder: <code>Coursework</code> &rarr; Subfolders: <code>/Maths</code>, <code>/English</code>, <code>/Digital_Skills</code> &rarr; individual files formatted with date and version (e.g. <code>Assignment1_2026-10_v1.docx</code>) [2m].<br>
           3. 'v1' and 'v2' denote <strong>Version 1</strong> and <strong>Version 2</strong>, indicating chronological draft revisions [1m].<br>
           4. Cloud storage protects against physical hardware loss (theft, fire, hard drive crash), provides automated continuous backup, and enables multi-device remote synchronization [2m].
         </div>"""),

        # Page 71: Units 3 & 4
        ("Units 3 &amp; 4: Search Engines, Backups &amp; Accessibility",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 3: Search Engines &amp; Evaluating Information (Page 9)</strong><br>
           1. Quotation marks force the search engine to return results containing the <strong>exact phrase</strong> in that precise word order [1m].<br>
           2. The NHS website (<code>.nhs.uk</code>) is far more trustworthy because content is authored and peer-reviewed by certified medical professionals without commercial sales bias, whereas commercial forums may contain unverified opinions or sponsored products [2m].<br>
           3. Cross-reference the article against established reputable news agencies (BBC, Reuters), verify author credentials, check publication dates, and use independent fact-checking sites (e.g. Full Fact) [2m].<br>
           4. Exact query: <code>"electric vehicle charging grant" site:.gov.uk</code> [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 4: Storage Media, Backup &amp; Accessibility (Page 11)</strong><br>
           1. <strong>3-2-1 Rule:</strong> Maintain at least <strong>3</strong> copies of critical data, stored across <strong>2</strong> different physical media types (e.g. SSD + external drive), with at least <strong>1</strong> copy stored off-site in the Cloud [3m].<br>
           2. (a) <strong>Screen Magnifier:</strong> Enlarges parts of the screen; (b) <strong>High Contrast Mode:</strong> Distinguishes text from background; (c) <strong>Screen Reader:</strong> Reads text aloud [2m].<br>
           3. Advantage: High-speed local transfer without internet connection [1m]. Disadvantage: Vulnerable to physical theft, damage, or fire in the same office [1m].
         </div>"""),

        # Page 72: Units 5 & 6
        ("Units 5 &amp; 6: Word Processing &amp; Visual Document Layout",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 5: Word Processing &amp; Document Layout (Page 13)</strong><br>
           1. a) Copy: <code>Ctrl + C</code> [1m] &bull; b) Paste: <code>Ctrl + V</code> [1m] &bull; c) Undo: <code>Ctrl + Z</code> [1m].<br>
           2. Advantage 1: Allows instantaneous global document styling changes in one click [1m]; Advantage 2: Enables screen readers to parse navigation tags and allows Word to generate an automated interactive Table of Contents [1m].<br>
           3. Left-aligned text maintains a consistent, predictable starting edge for the eye without the irregular, disjointed word-spacing created by full justification, significantly aiding dyslexic readers [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 6: Tables, Images &amp; Page Setup (Page 15)</strong><br>
           1. Pulling a side handle stretches or squashes the image, distorting its aspect ratio and making content look unprofessional [1m].<br>
           2. <strong>Alt Text (Alternative Text)</strong> provides a written textual description of an image for visually impaired users who rely on screen-reading software [2m].<br>
           3. Insert a <strong>Section Break (Next Page)</strong> before the table, set orientation to Landscape, insert another Section Break (Next Page) after the table, and switch back to Portrait [2m].<br>
           4. Right-aligning numbers ensures that decimal points, units, tens, and hundreds align in straight vertical columns, making comparative magnitude easy to evaluate [1m].
         </div>"""),

        # Page 73: Units 7 & 8
        ("Units 7 &amp; 8: Spreadsheets, Referencing &amp; Core Formulas",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 7: Spreadsheets &ndash; Cell Referencing &amp; Formatting (Page 17)</strong><br>
           1. Cell reference: <strong>D14</strong> [1m].<br>
           2. Software cannot perform mathematical arithmetic operations on alphabetic text characters; the formula encounters non-numeric data and returns <code>#VALUE!</code> [2m].<br>
           3. The <strong>Autofill Handle</strong> (the small square icon in the bottom-right corner of the active cell) [1m].<br>
           4. Select cell &rarr; Right-click &rarr; <code>Format Cells &rarr; Number &rarr; Currency</code> &rarr; Symbol: <strong>£</strong>, Decimal places: <strong>2</strong> [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 8: Spreadsheet Formulas &amp; Functions (Page 19)</strong><br>
           1. Exact formula: <code>=AVERAGE(B2:B28)</code> [1m].<br>
           2. Exact formula: <code>=C10-D10</code> [1m].<br>
           3. Exact formula: <code>=MIN(E5:E50)</code> [1m].<br>
           4. Dynamic recalculation: The formula automatically recalculates instantly, updating the displayed output in D2 to reflect the new input value in B2 [2m].
         </div>"""),

        # Page 74: Units 9 & 10
        ("Units 9 &amp; 10: Data Visualisation &amp; Presentation Slide Decks",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 9: Data Visualisation &amp; Charts (Page 21)</strong><br>
           1. A <strong>Line Graph</strong> is ideal for showing continuous trend data over time [1m].<br>
           2. (a) <strong>X-axis Title</strong> (Category descriptor) [1m]; (b) <strong>Y-axis Title</strong> (Units of measure &mdash; e.g. 'Revenue (£)') [1m].<br>
           3. A pie chart with 30 slices creates an indecipherable visual mess with overlapping text labels; pie charts should only represent 2 to 6 proportional categories [2m].<br>
           4. Highlight cell range A1:B8 &rarr; Click <code>Insert &rarr; Recommended Charts &rarr; Select Chart &rarr; OK</code> [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 10: Digital Presentations &amp; Slide Design (Page 23)</strong><br>
           1. Maximum <strong>6 bullet points</strong> per slide, and maximum <strong>6 words</strong> per bullet point, ensuring concise readability [2m].<br>
           2. Presenter Notes hold confidential speaking reminders visible only to the speaker on their laptop screen while the audience views clean slides [1m].<br>
           3. Editing the Slide Master updates layouts, corporate colours, and font sizes across all slides globally, eliminating repetitive slide-by-slide editing [2m].<br>
           4. (a) High-contrast font colours (dark text on cream background) [1m]; (b) Sans-serif typeface (Arial/Lexend) at minimum 24–28pt font size [1m].
         </div>"""),

        # Page 75: Units 11 & 12
        ("Units 11 &amp; 12: Professional Email &amp; Cloud Scheduling",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 11: Professional Email Etiquette (Page 25)</strong><br>
           1. <strong>Cc (Carbon Copy):</strong> Recipients are visible to all readers, indicating they are receiving the message for information only. <strong>Bcc (Blind Carbon Copy):</strong> Recipient addresses are completely hidden from all other recipients [2m].<br>
           2. Vague or empty subject lines prevent recipients from assessing urgency, cause messages to be flagged as spam, and make searching archives difficult [1m].<br>
           3. Exposing personal email addresses to third parties without consent constitutes an unlawful disclosure of personal identifiable data under UK GDPR [2m].<br>
           4. Example: <code>Rescheduled: Weekly Operations Team Meeting &ndash; Thursday 14:00 (Room 3)</code> [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 12: Attachments, Cloud Links &amp; Calendars (Page 27)</strong><br>
           1. (a) Avoids exceeding corporate mail server file size limits (usually 20–25 MB) [1m]; (b) Ensures all collaborators view and edit a single, live master version rather than conflicting email attachments [1m].<br>
           2. 'Can view' allows recipients to read and download the document without modifying contents; 'Can edit' grants full permission to alter text and delete data [2m].<br>
           3. (a) Exact date, start time, and duration; (b) Meeting location or video call hyperlink; (c) Concise agenda of discussion topics [2m].
         </div>"""),

        # Page 76: Units 13 & 14
        ("Units 13 &amp; 14: Virtual Meetings &amp; E-Commerce Navigation",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 13: Video Conferencing &amp; Virtual Meetings (Page 29)</strong><br>
           1. Muting prevents background acoustic echoes, keyboard clatter, coughing, and household noises from interrupting the active speaker [1m].<br>
           2. (a) Close all confidential documents, email inboxes, and internal chats [1m]; (b) Share the specific application window rather than the full desktop [1m].<br>
           3. It obscures the user's domestic living space, protecting personal privacy and hiding family members or personal possessions from view [1m].<br>
           4. The virtual <strong>'Raise Hand'</strong> reaction button [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 14: E-Commerce Navigation &amp; Filtering (Page 31)</strong><br>
           1. Filters eliminate irrelevant items instantly by narrowing products according to specific budget limits, sizes, brands, and delivery constraints [2m].<br>
           2. Checking 5-star reviews confirms product benefits, while checking 1-star and 2-star reviews reveals chronic manufacturing flaws or recurring defects [2m].<br>
           3. Under the UK Consumer Contracts Regulations, buyers have <strong>14 calendar days</strong> from delivery to cancel and return online purchases for a refund [1m].
         </div>"""),

        # Page 77: Units 15 & 16
        ("Units 15 &amp; 16: Payment Security &amp; Public Portals",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 15: Secure Online Payments &amp; Protection (Page 33)</strong><br>
           1. The 's' indicates <strong>Secure (HTTPS)</strong>, confirming the web connection is protected by SSL/TLS encryption [1m].<br>
           2. Under <strong>Section 75 of the Consumer Credit Act</strong>, the credit card company is jointly liable with the retailer for purchases over £100 if goods are faulty or the firm collapses; bank transfers offer zero statutory chargeback rights [2m].<br>
           3. 3D Secure requires entering a one-time SMS verification code or approving a prompt in a mobile banking app before payment completes [2m].<br>
           4. (a) Connection lacks HTTPS (starts with <code>http://</code>); (b) Seller demands payment strictly via direct bank transfer or cryptocurrency [2m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 16: Public Digital Services (Gov.uk &amp; NHS) (Page 35)</strong><br>
           1. <strong>.gov.uk</strong> is exclusively reserved for verified UK public sector institutions [1m].<br>
           2. (a) Renewing a UK passport; (b) Paying road vehicle tax; (c) Filing annual Self Assessment tax returns [3m].<br>
           3. Allows ordering repeat prescriptions online, viewing immunization records, booking GP appointments, and managing organ donation preferences securely [2m].<br>
           4. Forward scam SMS messages to <strong>7726</strong> (spells 'SPAM' on a telephone keypad) [1m].
         </div>"""),

        # Page 78: Units 17 & 18
        ("Units 17 &amp; 18: Passwords, MFA &amp; Phishing Defense",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 17: Passwords, MFA &amp; Biometrics (Page 37)</strong><br>
           1. Combining three memorable, unrelated dictionary words (e.g. <code>Coffee!Giraffe#Anchor44</code>) creates high character length that resists brute-force cracking while remaining easy to remember [2m].<br>
           2. MFA requires two distinct authentication factors: something you know (password) plus something you have (phone/app code); even if a password is stolen, hackers cannot access the account [2m].<br>
           3. (a) Fingerprint scanning (Touch ID); (b) Facial recognition (Face ID) [2m].<br>
           4. If one service experiences a credential data breach, hackers immediately test the compromised password across all other banking and personal accounts (credential stuffing) [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 18: Phishing Threats &amp; Social Engineering (Page 39)</strong><br>
           1. A deceptive fraudulent attempt by cybercriminals to manipulate individuals into disclosing sensitive passwords or financial credentials by posing as a trusted organisation [2m].<br>
           2. (a) Artificial sense of panic/urgency; (b) Generic salutation ('Dear Customer'); (c) Deceptive sender domain address [3m].<br>
           3. Displays the true underlying destination URL in the status bar before clicking [1m].<br>
           4. Forward suspicious phishing emails to: <code>report@phishing.gov.uk</code> [1m].
         </div>"""),

        # Page 79: Units 19 & 20
        ("Units 19 &amp; 20: GDPR Data Rights &amp; Workplace Ergonomics",
         """<div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 19: Privacy Controls &amp; UK GDPR Rights (Page 41)</strong><br>
           1. The <strong>Information Commissioner's Office (ICO)</strong> [1m].<br>
           2. Under UK GDPR, individuals have the legal right to request and receive a free copy of all personal data an organisation holds about them within 1 calendar month [2m].<br>
           3. (a) Set profile visibility to 'Friends Only' / Private; (b) Disable geolocation tagging on published photographs [2m].<br>
           4. The permanent record of all digital activity, browsing histories, posts, comments, and data trails left behind when using the internet [1m].
         </div>
         <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
           <strong style="color:#0284c7;">Unit 20: Digital Wellbeing &amp; Ergonomics (Page 43)</strong><br>
           1. Every <strong>20 minutes</strong>, look at an object at least <strong>20 feet away</strong> for at least <strong>20 seconds</strong> to relax the ciliary eye muscles and prevent strain [2m].<br>
           2. The top edge of the monitor screen should be aligned directly <strong>at eye level</strong> [1m].<br>
           3. (a) Chronic cervical neck stiffness; (b) Lower lumbar back pain; (c) Repetitive Strain Injury (RSI) in wrists [2m].<br>
           4. Elevating the laptop screen to eye level on a stand forces your hands up; an external keyboard and mouse allow your forearms and wrists to rest in an ergonomically neutral position [1m].
         </div>""")
    ]

    for p_num, (ans_title, ans_content) in enumerate(unit_answers, 70):
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Essential Digital Skills</div>
    <div class="page-header-strand">Complete Explanatory Answer Key &bull; Part I Units</div>
  </div>

  <h2>{ans_title}</h2>
  <p style="margin-bottom:6px;">Step-by-step marking rubric and technical answer keys:</p>

  {ans_content}

  <div class="page-footer">
    <div>Essential Digital Skills (EDSQ) Practical Study Handbook &bull; Answer Key</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
""")

    # Page 80: Software Labs 1 to 3 Answers
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Software Labs</div>
    <div class="page-header-strand">Explanatory Answer Key &bull; Software Labs 1 to 3</div>
  </div>

  <h2>Software Workflow Laboratories 1 to 3 &bull; Model Solutions</h2>
  <p style="margin-bottom:6px;">Exemplar solutions and marking criteria for Labs 1, 2, and 3:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Lab 1: Word Processing &amp; Mail Merge (Page 45)</strong><br>
    <strong>Task 1.1:</strong> Insert Section Break (Next Page) &rarr; Page Setup &rarr; Orientation: Landscape &rarr; Insert table &rarr; Insert second Section Break (Next Page) &rarr; Orientation: Portrait [4m].<br>
    <strong>Task 1.2:</strong> Mailings tab &rarr; Start Mail Merge: Letters &rarr; Select Recipients &rarr; Use Existing List: 'Recipients.xlsx' &rarr; Insert Merge Fields (<code>&laquo;First_Name&raquo;</code>, <code>&laquo;Award&raquo;</code>) &rarr; Preview Results &rarr; Finish &amp; Merge: Print/Save [4m].<br>
    <strong>Task 1.3:</strong> (a) Use Heading styles (H1, H2); (b) Add Alt Text to all graphics; (c) Use minimum 1.2 line spacing and left text alignment [3m].
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Lab 2: Spreadsheets &amp; Data Modeling (Page 47)</strong><br>
    <strong>Task 2.1:</strong> Relative referencing shifts G1 to G2 (empty cell) when dragged down. Correct formula: <code>=C4*$G$1</code> using dollar signs to lock cell G1 [4m].<br>
    <strong>Task 2.2:</strong> Exact formula: <code>=IF(C2&gt;=50, D2*0.90, D2)</code> (or <code>=IF(C2&gt;=50, D2*0.10, 0)</code> for discount amount) [4m].<br>
    <strong>Task 2.3:</strong> (a) Format currency figures as Currency (£) with 2 decimal places; (b) Apply bold formatting and contrasting header fills; (c) Enable text wrapping and widen columns to prevent <code>###</code> display errors [3m].
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Lab 3: Presentation Slide Decks (Page 49)</strong><br>
    <strong>Task 3.1:</strong> View &rarr; Slide Master &rarr; Select topmost master slide &rarr; Insert logo image &rarr; Position in corner &rarr; Close Slide Master. Logo is locked across all slides [4m].<br>
    <strong>Task 3.2:</strong> Critique: Cognitive overload, poor contrast, distracting animation. Solutions: Apply 6&times;6 rule; use high-contrast dark text on light background; replace spinning animation with subtle 0.5s fade; move paragraphs to speaker notes [4m].<br>
    <strong>Task 3.3:</strong> Presenter View displays elapsed presentation timer, upcoming slide preview, and private speaker prompts on laptop, ensuring confident presentation pacing [3m].
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills &bull; Software Labs Answer Key</div>
    <div class="page-num">Page 80</div>
  </div>
</div>
""")

    # Page 81: Software Labs 4 to 5 & Security Audits Answers
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Security &amp; Labs</div>
    <div class="page-header-strand">Explanatory Answer Key &bull; Labs 4–5 &amp; Audits</div>
  </div>

  <h2>Software Labs 4–5 &amp; Cybersecurity Audits &bull; Solutions</h2>
  <p style="margin-bottom:6px;">Exemplar solutions and marking criteria for Labs 4, 5, and Cybersecurity Audits 1 &amp; 2:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Lab 4: Email Rules &amp; Scheduling (Page 51)</strong><br>
    <strong>Task 4.1:</strong> Home &rarr; Rules &rarr; Create Rule &rarr; Condition: Subject contains 'Invoice' &rarr; Action: Move item to 'Accounts_Payable' &rarr; Flag for follow-up &rarr; Finish [4m].<br>
    <strong>Task 4.2:</strong> Calendar &rarr; New Meeting &rarr; Add 6 attendees &rarr; Open 'Scheduling Assistant' &rarr; Identify shared white open slot &rarr; Send invitation [4m].<br>
    <strong>Task 4.3:</strong> Professional Out-of-Office: Exact departure/return dates, reason (annual leave), alternate contact name and email, notice of zero inbox monitoring [3m].
  </div>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:5px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Lab 5: Cloud Governance &amp; Versioning (Page 53)</strong><br>
    <strong>Task 5.1:</strong> File &rarr; Info &rarr; Version History &rarr; Select timestamp prior to deletion &rarr; Click 'Restore' to revert workbook [4m].<br>
    <strong>Task 5.2:</strong> 'Anyone can edit' creates anonymous open vulnerability; 'Specific people can view' enforces authenticated, read-only access [4m].<br>
    <strong>Task 5.3:</strong> Work on distinct designated sections; use cell commenting rather than overwriting live collaborator cells [3m].
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Cybersecurity Audits 1 &amp; 2 (Pages 55 &amp; 57)</strong><br>
    <strong>Audit 1.1:</strong> (1) Domain is <code>.co.uk</code> instead of <code>.gov.uk</code>; (2) Attachment is an executable <code>.exe</code> file; (3) HMRC never issues tax rebates via email; (4) Artificial urgency [4m].<br>
    <strong>Audit 2.1:</strong> Collecting maiden names and home addresses for a simple newsletter violates Data Minimisation; only Name and Email are necessary [4m].<br>
    <strong>Audit 2.2:</strong> Deadline: 1 calendar month; Fee: strictly free of charge; Format: accessible electronic format [4m].
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills &bull; Audits &amp; Labs Answer Key</div>
    <div class="page-num">Page 81</div>
  </div>
</div>
""")

    # Page 82: Practical Mock Exam 1 & 2 Answers
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Marking</div>
    <div class="page-header-strand">Examiner Mark Scheme &bull; Mocks 1 &amp; 2</div>
  </div>

  <h2>Practical Mock Examinations 1 &amp; 2 &bull; Marking Rubric</h2>
  <p style="margin-bottom:6px;">Award marks according to official awarding body criteria (30 Marks per Mock):</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Mock Assignment 1: Community Charity Gala (Pages 58–61 &bull; 30 Marks)</strong><br>
    &bull; <strong>Task 1.1 Spreadsheet Formulas:</strong> a) <code>=C4*D4</code> [2m] &bull; b) <code>=SUM(E4:E15)</code> [2m] &bull; c) <code>=IF(D4&gt;=50, "Target Met", "Under Target")</code> [4m].<br>
    &bull; <strong>Task 1.2 Chart:</strong> Select categories B4:B8 and gross revenue E4:E8; Title: <em>"Gala Ticket Revenue by Tier"</em>; X-axis: <em>"Ticket Category"</em>; Y-axis: <em>"Revenue (£)"</em> [5m].<br>
    &bull; <strong>Task 1.3 Event Flyer:</strong> Large title, high-contrast palette, H1/H2 styles, bulleted highlights, clear call-to-action link, Alt Text on charity logo [8m].<br>
    &bull; <strong>Task 1.4 Sponsor Email:</strong> Subject: <em>"Sponsorship Partnership Invitation &ndash; Community Gala 2026"</em>; formal salutation; clear charitable impact; professional closing [5m].<br>
    &bull; <strong>Task 1.5 Donor Privacy:</strong> Must use <strong>BCC (Blind Carbon Copy)</strong> field; prevents unlawful data disclosure of donor email addresses under UK GDPR [4m].
  </div>

  <div class="card-practice" style="padding:6px 10px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Mock Assignment 2: Healthcare Patient Onboarding (Pages 62–65 &bull; 30 Marks)</strong><br>
    &bull; <strong>Task 2.1 Spreadsheet Formulas:</strong> a) <code>=AVERAGE(D2:D45)</code> [2m] &bull; b) <code>=MAX(D2:D45)</code> [2m] &bull; c) <code>=IF(D2&gt;30, "Review Needed", "Standard")</code> [4m].<br>
    &bull; <strong>Task 2.2 Attendance Chart:</strong> Recommend <strong>Pie Chart</strong> (4 categories total 100%); add percentage data labels; include clear legend [5m].<br>
    &bull; <strong>Task 2.3 Mail Merge:</strong> Select Recipients &rarr; 'Appointments_Oct.xlsx' &rarr; Insert <code>&laquo;Title&raquo;</code>, <code>&laquo;Last_Name&raquo;</code>, <code>&laquo;Date&raquo;</code>, <code>&laquo;Time&raquo;</code> &rarr; Complete merge [8m].<br>
    &bull; <strong>Task 2.4 Patient Portal Email:</strong> Professional explanation that unencrypted email violates Caldicott health privacy standards; clear guidance to access the NHS App [5m].<br>
    &bull; <strong>Task 2.5 Physical Security:</strong> Lock screen (Win+L) when stepping away from desk; keep confidential patient printouts face down or locked in cabinets [4m].
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills &bull; Practical Mock 1 &amp; 2 Mark Scheme</div>
    <div class="page-num">Page 82</div>
  </div>
</div>
""")

    # Page 83: Practical Mock Exam 3 Answers & Grade Thresholds
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; Practical Mock Marking</div>
    <div class="page-header-strand">Examiner Mark Scheme &bull; Mock 3 &amp; Boundaries</div>
  </div>

  <h2>Practical Mock Exam 3 &amp; Official Grade Boundaries</h2>
  <p style="margin-bottom:6px;">Marking rubric for Mock 3 and qualification passing standards:</p>

  <div class="card-practice" style="padding:6px 10px; margin-bottom:6px; font-size:7.5pt;">
    <strong style="color:#0284c7;">Mock Assignment 3: Retail E-Commerce Transition (Pages 66–69 &bull; 30 Marks)</strong><br>
    &bull; <strong>Task 3.1 Inventory Formulas:</strong> a) <code>=(D2-C2)/D2</code> [2m] &bull; b) <code>=D2*(1-$H$1)</code> (or <code>=D2*0.85</code>) with absolute cell reference [3m] &bull; c) <code>=B2*C2</code> [3m].<br>
    &bull; <strong>Task 3.2 Best-Seller Chart:</strong> Highlight products and quantities; Bar Chart with title <em>"Inventory Stock Levels by Category"</em>; X-axis: <em>"Units in Stock"</em>; Y-axis: <em>"Product Category"</em> [5m].<br>
    &bull; <strong>Task 3.3 Pitch Slide Deck:</strong> 4 slides following 6&times;6 rule: 1. Title/Vision; 2. E-Commerce Market Growth; 3. Projected Financial Return; 4. Implementation Timeline [8m].<br>
    &bull; <strong>Task 3.4 Customer Email:</strong> Empathetic opening; immediate apology; confirmation of replacement dispatch; prepaid return label attachment [5m].<br>
    &bull; <strong>Task 3.5 Payment Gateway Security:</strong> (1) PCI-DSS level 1 compliance; (2) End-to-end tokenization and 3D Secure fraud authentication [4m].
  </div>

  <div class="card-concept" style="border-left-color:#0284c7; font-size:7.5pt;">
    <strong style="color:#0284c7;">Official EDSQ Grade Boundaries &amp; Pass Criteria:</strong><br>
    To achieve an accredited pass in the Essential Digital Skills Qualification (Level 1 / Entry 3):
    <table class="data-table" style="font-size:7pt; margin-top:4px;">
      <tr><th>Component</th><th>Marks Available</th><th>Pass Threshold</th><th>Percentage Required</th></tr>
      <tr><td>Section 1: Knowledge &amp; Security</td><td>15 Marks</td><td>10 – 11 Marks</td><td>~70%</td></tr>
      <tr><td>Section 2: Practical Application Tasks</td><td>30 Marks</td><td>21 – 22 Marks</td><td>~70%</td></tr>
      <tr style="background:#e0f2fe; font-weight:bold;"><td>Total Qualification Assessment</td><td>45 Marks</td><td>31 – 33 Marks</td><td>~70% Pass Standard</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <div>Essential Digital Skills &bull; Practical Mock 3 Mark Scheme</div>
    <div class="page-num">Page 83</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 84: BACK COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>
""")

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Essential Digital Skills Practical Handbook</title>
{SHARED_CSS}
<style>
  :root {{
    --theme: #0284c7;
    --accent: #00e5ff;
  }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    pdf_filename = "MasterFunctionalSkills_Digital_Skills_Handbook.pdf"
    count = render_book_to_pdf(full_html, pdf_filename)
    return count

if __name__ == "__main__":
    build_digital_skills_book()
