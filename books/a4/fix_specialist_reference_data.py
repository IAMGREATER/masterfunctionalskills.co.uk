"""
books/a4/fix_specialist_reference_data.py
Ensures specialist_suite_reference.py contains:
- DIGITAL_SKILLS_SHORTCUTS
- DIGITAL_SKILLS_GLOSSARY
- DIGITAL_SKILLS_INDEX
- BKSB_PAPERS_SOLUTIONS
"""

from pathlib import Path

REF_FILE = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/specialist_suite_reference.py")

SHORTCUTS_AND_GLOSSARY = '''
DIGITAL_SKILLS_SHORTCUTS = r"""<div style='font-size:10pt; line-height:1.4;'>
<p><b>Universal Operating System Shortcuts (Windows / macOS):</b><br>
&bull; Copy: <code>Ctrl + C</code> (Win) / <code>Cmd + C</code> (Mac)<br>
&bull; Paste: <code>Ctrl + V</code> (Win) / <code>Cmd + V</code> (Mac)<br>
&bull; Cut: <code>Ctrl + X</code> (Win) / <code>Cmd + X</code> (Mac)<br>
&bull; Undo / Redo: <code>Ctrl + Z</code> / <code>Ctrl + Y</code><br>
&bull; Select All: <code>Ctrl + A</code><br>
&bull; Find in Page: <code>Ctrl + F</code><br>
&bull; Save Document: <code>Ctrl + S</code><br>
&bull; Print / Save as PDF: <code>Ctrl + P</code><br>
&bull; Lock Workstation: <code>Win + L</code><br>
&bull; File Explorer: <code>Win + E</code><br>
&bull; Task Manager: <code>Ctrl + Shift + Esc</code></p>

<p><b>Web Browser Shortcuts (Chrome / Edge / Firefox):</b><br>
&bull; New Tab: <code>Ctrl + T</code> &emsp; Close Tab: <code>Ctrl + W</code><br>
&bull; Reopen Closed Tab: <code>Ctrl + Shift + T</code><br>
&bull; Incognito / InPrivate: <code>Ctrl + Shift + N</code><br>
&bull; Bookmark Current Page: <code>Ctrl + D</code><br>
&bull; Hard Refresh (Clear Cache): <code>Ctrl + F5</code> or <code>Ctrl + Shift + R</code><br>
&bull; Zoom In / Out / Reset: <code>Ctrl + Plus</code> / <code>Ctrl + Minus</code> / <code>Ctrl + 0</code></p>

<p><b>Spreadsheet Modeling Shortcuts (Excel / Google Sheets):</b><br>
&bull; Edit Active Cell: <code>F2</code><br>
&bull; Toggle Absolute Reference ($): <code>F4</code> (cycles A1 &rarr; $A$1 &rarr; A$1 &rarr; $A1)<br>
&bull; AutoSum Selected Range: <code>Alt + =</code><br>
&bull; Insert Current Date: <code>Ctrl + ;</code><br>
&bull; Fill Down / Fill Right: <code>Ctrl + D</code> / <code>Ctrl + R</code><br>
&bull; Select Entire Column: <code>Ctrl + Space</code> &emsp; Entire Row: <code>Shift + Space</code><br>
&bull; Format as Currency: <code>Ctrl + Shift + 4</code> ($ / &pound;)<br>
&bull; Format as Percentage: <code>Ctrl + Shift + 5</code> (%)</p>
</div>"""

DIGITAL_SKILLS_GLOSSARY = [
    ("Absolute Cell Reference ($A$1)", "A locked cell coordinate in a spreadsheet formula that does not change when autofilled into adjacent cells."),
    ("Bandwidth", "The maximum rate of data transfer across a given network path, measured in Megabits per second (Mbps)."),
    ("Cloud Synchronization", "The automated process of mirroring local files to a secure remote cloud server (e.g. OneDrive, Nextcloud)."),
    ("Cybersecurity Hygiene", "Routine practices (e.g. unique passphrases, regular patching, MFA) that maintain security and protect data."),
    ("Data Subject Access Request (DSAR)", "A formal request under GDPR allowing individuals to obtain a copy of personal data held by an organization."),
    ("DSE Assessment", "Display Screen Equipment risk assessment mandated by Health and Safety regulations to prevent ergonomic strain."),
    ("Encryption (End-to-End)", "A communication system where only the communicating users can read the messages, preventing eavesdropping."),
    ("Multi-Factor Authentication (MFA)", "An authentication method requiring two or more verification factors (password + authenticator app code)."),
    ("Netiquette", "The conventional rules of polite, professional, and respectful behavior in online and email communications."),
    ("Phishing", "A fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity in electronic communications."),
    ("Ransomware", "Malicious software designed to block access to a computer system or encrypt files until a sum of money is paid."),
    ("URL (Uniform Resource Locator)", "The unique address used to identify and locate a specific webpage or file on the World Wide Web."),
    ("VPN (Virtual Private Network)", "An encrypted connection over the internet from a device to a network, shielding online activity.")
]

DIGITAL_SKILLS_INDEX = [
    ("A", [("Absolute cell references ($A$1)", "4, 18"), ("Account security & credentials", "3, 12, 24"), ("Anti-virus & malware protection", "5, 20")]),
    ("B", [("Backup strategies (3-2-1 rule)", "6, 22"), ("Browser safety & SSL padlocks", "5, 16"), ("Budgeting spreadsheets", "14, 28")]),
    ("C", [("Cloud collaboration & sharing permissions", "7, 26"), ("Conditional formatting rules", "15, 29"), ("Cybersecurity essentials", "5, 12, 30")]),
    ("D", [("Data Protection Act & GDPR", "8, 32"), ("Data validation dropdowns", "14, 28"), ("Digital footprint management", "8, 34")]),
    ("E", [("Email attachments & file size limits", "9, 36"), ("Email etiquette & professional register", "9, 38"), ("Excel / Sheets formulas", "4, 14, 28")]),
    ("F", [("File folder hierarchy & naming conventions", "10, 40"), ("Firewalls & network security", "5, 20")]),
    ("I", [("IF statements & logical formulas", "4, 15, 29"), ("Incognito & private browsing", "5, 17")]),
    ("M", [("Mocks 1-4 workplace scenarios", "44-59"), ("Multi-factor authentication (MFA)", "3, 12, 24")]),
    ("P", [("Password complexity & managers", "3, 12"), ("Phishing & email fraud identification", "5, 21"), ("Privacy settings on social platforms", "8, 35")]),
    ("S", [("Shortcuts matrix (Windows & Mac)", "60"), ("Solutions for Units 1-10 Drills", "61-75"), ("SUM and AVERAGE formulas", "4, 14, 28")]),
    ("T", [("Troubleshooting device connectivity", "11, 42"), ("Two-factor authentication (2FA)", "3, 12, 24")]),
    ("V", [("Version control in cloud documents", "7, 27"), ("Virtual Private Networks (VPN)", "5, 19")])
]
'''

def fix():
    with open(REF_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    if "DIGITAL_SKILLS_SHORTCUTS" not in text:
        target = text.find("# 4. BKSB REMEDIATION WORKBOOK")
        if target != -1:
            text = text[:target] + SHORTCUTS_AND_GLOSSARY + "\n\n" + text[target:]
            print("DIGITAL_SKILLS shortcuts, glossary, and index inserted.")
        else:
            text += "\n" + SHORTCUTS_AND_GLOSSARY
            print("DIGITAL_SKILLS shortcuts appended.")

    with open(REF_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    print("specialist_suite_reference.py fixed successfully!")

if __name__ == "__main__":
    fix()
