#!/usr/bin/env python3
"""
Area 5: Being Safe and Responsible Online (Cards 41-50)
"""
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS = [
    # 41. Creating Strong Passwords & Passphrases
    {
        "id": "dfs-41",
        "number": 41,
        "title": "Strong Passwords &amp; Passphrases",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.1",
        "rule_heading": "Length Trumps Complexity: Three Random Words",
        "rule_body": "UK NCSC recommendation: Use 'Three Random Words' to build long, uncrackable passphrases that are easy to remember (e.g. 'CoffeePlanetLizard!'). Minimum 12-16 characters. Combine uppercase, lowercase, numbers, and symbols. NEVER reuse passwords across accounts.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Weak password -->
            <rect x="15" y="14" width="340" height="34" rx="6" fill="#fef2f2" stroke="#fca5a5"/>
            <text x="25" y="35" font-size="10.5" font-weight="800" fill="#991b1b">Weak: password123 / Welcome1!</text>
            <text x="240" y="35" font-size="10" font-weight="800" fill="#dc2626">Cracked in seconds ✗</text>
            <!-- Medium password -->
            <rect x="15" y="55" width="340" height="34" rx="6" fill="#fffbeb" stroke="#fcd34d"/>
            <text x="25" y="76" font-size="10.5" font-weight="800" fill="#92400e">Medium: P@ssw0rd!99</text>
            <text x="240" y="76" font-size="10" font-weight="800" fill="#b45309">Cracked in 2 hours ⚠️</text>
            <!-- Strong passphrase -->
            <rect x="15" y="96" width="340" height="36" rx="6" fill="#ecfdf5" stroke="#6ee7b7"/>
            <text x="25" y="114" font-size="10.5" font-weight="900" fill="#065f46">Strong: CoffeePlanetLizard!42</text>
            <text x="240" y="114" font-size="10" font-weight="900" fill="#047857">4,000+ years to crack ✓</text>
            <text x="25" y="126" font-size="8.5" font-weight="700" fill="#047857">NCSC 3 Random Words: High length + easy human memory</text>
          </g>"""),
        "golden_rule": 'Combine three random words into a 14+ character secure passphrase!',
        "watch_out": 'Never reuse your primary email password on any other website.',
        "challenge_prompt": "Why is 'RocketTeapotBlanket!' a stronger password than 'P@ssw0rd1' despite being easier to remember?",
        "answer_text": "Because length is the primary defence against brute-force attacks; 19 characters takes centuries to crack, while 9 characters takes minutes."
    },

    # 42. Password Managers & Safe Storage
    {
        "id": "dfs-42",
        "number": 42,
        "title": "Password Managers &amp; Safe Storage",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.2",
        "rule_heading": "Encrypted Vaults &amp; Unique Logins",
        "rule_body": "Password managers (Bitwarden, 1Password, Apple Keychain) store all your passwords inside a military-grade encrypted digital vault. Benefits: 1. You only need to remember ONE strong Master Password. 2. Auto-generates random 20-character passwords. 3. Autofills logins on trusted sites.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Vault concept -->
            <rect x="15" y="15" width="115" height="115" rx="8" fill="#1e293b"/>
            <text x="72" y="38" font-size="10.5" font-weight="900" fill="#f8fafc" text-anchor="middle">ENCRYPTED VAULT</text>
            <text x="72" y="65" font-size="24" text-anchor="middle">🔐</text>
            <text x="72" y="98" font-size="9" font-weight="700" fill="#94a3b8" text-anchor="middle">Protected by 1 Master</text>
            <text x="72" y="112" font-size="9" font-weight="700" fill="#94a3b8" text-anchor="middle">Passphrase + 2FA</text>
            <!-- Connected sites -->
            <g transform="translate(145, 18)">
              <rect x="0" y="0" width="210" height="32" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="10" y="20" font-size="9.5" font-weight="800" fill="#0f172a">Online Banking: 9xK#mQ2$pL9@...</text>
              <rect x="0" y="38" width="210" height="32" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="10" y="58" font-size="9.5" font-weight="800" fill="#0f172a">Work Email: tR7!vN4#zW1&amp;...</text>
              <rect x="0" y="76" width="210" height="32" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="10" y="96" font-size="9.5" font-weight="800" fill="#0f172a">Shopping: 3bA^kP8*vM6?...</text>
            </g>
          </g>"""),
        "golden_rule": 'Use a password manager so every account has a unique, strong password!',
        "watch_out": 'Never write passwords on sticky notes or keep them in unencrypted files.',
        "challenge_prompt": "What is the primary security advantage of using a password manager over using the same password for 10 different websites?",
        "answer_text": "If one website suffers a security breach, your other accounts remain completely secure because each site has a unique password."
    },

    # 43. Phishing Scams (Email & Smishing)
    {
        "id": "dfs-43",
        "number": 43,
        "title": "Spotting Phishing &amp; Smishing",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.3",
        "rule_heading": "Urgency, Sender Spoofing &amp; Malicious Links",
        "rule_body": "Spotting fraudulent messages: 1. Artificial urgency ('Account suspended in 24 hrs!'). 2. Fake sender email domain (e.g. service@hmrc-tax-refunds.com instead of gov.uk). 3. Generic salutations ('Dear Customer'). 4. Suspicious links (hover cursor to view true destination URL).",
        "svg_html": wrap_svg("""
          <g transform="translate(35, 10)">
            <rect x="0" y="0" width="390" height="148" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
            <text x="195" y="22" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">ANATOMY OF A PHISHING ATTACK</text>
            <!-- Red flag 1: From -->
            <rect x="12" y="32" width="366" height="24" rx="4" fill="#ffffff"/>
            <text x="20" y="48" font-size="9.2" font-weight="800" fill="#dc2626">🚩 Fake Sender: security@paypal-verification-uk.com (Not paypal.com!)</text>
            <!-- Red flag 2: Urgency -->
            <rect x="12" y="60" width="366" height="24" rx="4" fill="#ffffff"/>
            <text x="20" y="76" font-size="9.2" font-weight="800" fill="#dc2626">🚩 Panic &amp; Threat: "Your account will be suspended within 2 hours!"</text>
            <!-- Red flag 3: Fake link -->
            <rect x="12" y="88" width="366" height="24" rx="4" fill="#ffffff"/>
            <text x="20" y="104" font-size="9.2" font-weight="800" fill="#dc2626">🚩 Deceptive Link: Display says "Login" but points to "scam-site.ru"</text>
            <text x="195" y="125" font-size="8.8" font-weight="800" fill="#7f1d1d" text-anchor="middle">Hover over links to inspect real destination address</text>
            <text x="195" y="139" font-size="8.8" font-weight="800" fill="#7f1d1d" text-anchor="middle">Forward suspicious emails to: report@phishing.gov.uk</text>
          </g>"""),
        "golden_rule": 'Hover over links to verify the actual destination URL before clicking!',
        "watch_out": 'HMRC and banks never text or email links asking for security details.',
        "challenge_prompt": "What should you do before clicking on a link in an unexpected email claiming your account has been compromised?",
        "answer_text": "Hover your mouse over the link to verify the true destination URL, or visit the official website directly via your browser."
    },

    # 44. Malware, Viruses & Ransomware Awareness
    {
        "id": "dfs-44",
        "number": 44,
        "title": "Malware, Viruses &amp; Ransomware",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.4",
        "rule_heading": "Malicious Software Types &amp; Defence",
        "rule_body": "Key malware categories: 1. Virus/Trojan: Malicious code hidden inside innocent-looking files. 2. Spyware/Keylogger: Silently records passwords and browsing habits. 3. Ransomware: Encrypts your files and demands money for decryption. Defence: Active antivirus and regular offline backups.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Ransomware box -->
            <rect x="15" y="15" width="105" height="115" rx="6" fill="#fef2f2" stroke="#ef4444"/>
            <text x="67" y="36" font-size="10.5" font-weight="900" fill="#991b1b" text-anchor="middle">RANSOMWARE</text>
            <text x="67" y="58" font-size="9" font-weight="700" fill="#b91c1c" text-anchor="middle">Encrypts files</text>
            <text x="67" y="74" font-size="9" font-weight="700" fill="#b91c1c" text-anchor="middle">Demands extortion</text>
            <text x="67" y="105" font-size="8.5" font-weight="800" fill="#7f1d1d" text-anchor="middle">Fix: Offline backups</text>
            <!-- Spyware box -->
            <rect x="132" y="15" width="105" height="115" rx="6" fill="#fffbeb" stroke="#f59e0b"/>
            <text x="184" y="36" font-size="10.5" font-weight="900" fill="#92400e" text-anchor="middle">SPYWARE</text>
            <text x="184" y="58" font-size="9" font-weight="700" fill="#b45309" text-anchor="middle">Logs keystrokes</text>
            <text x="184" y="74" font-size="9" font-weight="700" fill="#b45309" text-anchor="middle">Steals passwords</text>
            <text x="184" y="105" font-size="8.5" font-weight="800" fill="#78350f" text-anchor="middle">Fix: Antivirus scan</text>
            <!-- Protection Shield -->
            <rect x="250" y="15" width="105" height="115" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="302" y="36" font-size="10.5" font-weight="900" fill="#065f46" text-anchor="middle">ACTIVE DEFENCE</text>
            <text x="302" y="58" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">• Live Antivirus</text>
            <text x="302" y="74" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">• OS Firewall ON</text>
            <text x="302" y="105" font-size="8.5" font-weight="800" fill="#064e3b" text-anchor="middle">3-2-1 Backup rule ✓</text>
          </g>"""),
        "golden_rule": 'Maintain offline backups of critical data to safeguard from ransomware!',
        "watch_out": 'Never enable macros on unexpected email attachments from strangers.',
        "challenge_prompt": "What is ransomware, and what proactive step best ensures you never have to pay a ransom to recover files?",
        "answer_text": "Ransomware is malicious software that encrypts your files and demands payment. Maintaining regular offline backups ensures you can restore files without paying."
    },

    # 45. Software Updates & Security Patches
    {
        "id": "dfs-45",
        "number": 45,
        "title": "Software Updates &amp; Security Patches",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.5",
        "rule_heading": "Zero-Day Flaws &amp; Automatic Updates",
        "rule_body": "Software and operating system updates provide critical security patches that close vulnerabilities before cybercriminals exploit them. Always enable automatic updates for: Windows/macOS, smartphones (iOS/Android), web browsers (Chrome/Edge), and antivirus software.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <rect x="0" y="0" width="370" height="26" rx="8" fill="#1e293b"/>
            <text x="185" y="18" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">SYSTEM SECURITY UPDATE AVAILABLE</text>
            <g transform="translate(20, 36)">
              <text x="0" y="18" font-size="11" font-weight="800" fill="#0f172a">Security Patch KB5031455 (Critical)</text>
              <text x="0" y="36" font-size="9.5" font-weight="600" fill="#475569">• Fixes 14 zero-day vulnerabilities in network stack</text>
              <text x="0" y="52" font-size="9.5" font-weight="600" fill="#475569">• Closes remote code execution backdoor</text>
            </g>
            <rect x="20" y="98" width="330" height="34" rx="6" fill="#ecfdf5" stroke="#10b981"/>
            <text x="35" y="119" font-size="10.5" font-weight="900" fill="#065f46">✓ Automatic Updates: [ ENABLED ]</text>
            <text x="210" y="119" font-size="9.5" font-weight="700" fill="#047857">Installs patches overnight</text>
          </g>"""),
        "golden_rule": 'Enable automatic updates so operating systems and apps patch flaws fast!',
        "watch_out": 'Postponing security updates leaves systems vulnerable to known exploits.',
        "challenge_prompt": "Why is installing operating system updates vital even if you do not care about new visual features?",
        "answer_text": "Because updates contain security patches that fix discovered vulnerabilities, preventing hackers and malware from exploiting them."
    },

    # 46. Public Wi-Fi Risks & VPN Security
    {
        "id": "dfs-46",
        "number": 46,
        "title": "Public Wi-Fi Risks &amp; VPNs",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.6",
        "rule_heading": "Unencrypted Networks &amp; Encrypted Tunnels",
        "rule_body": "Public Wi-Fi in cafes, hotels, and airports carries risks: 1. Man-in-the-Middle attacks (eavesdropping unencrypted packets). 2. Fake rogue hotspots ('Evil Twins'). Safety rules: Avoid banking on public Wi-Fi; use mobile 4G/5G tethering; use a reputable Virtual Private Network (VPN).",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Open Public WiFi -->
            <rect x="15" y="15" width="165" height="115" rx="6" fill="#fef2f2" stroke="#f87171"/>
            <text x="97" y="35" font-size="10.5" font-weight="900" fill="#991b1b" text-anchor="middle">OPEN PUBLIC WI-FI ✗</text>
            <text x="25" y="60" font-size="9.5" font-weight="700" fill="#dc2626">• Unencrypted radio broadcast</text>
            <text x="25" y="80" font-size="9.5" font-weight="700" fill="#dc2626">• Snooping / packet sniffing</text>
            <text x="25" y="100" font-size="9.5" font-weight="700" fill="#dc2626">• Rogue 'Evil Twin' fake APs</text>
            <text x="25" y="118" font-size="9" font-weight="800" fill="#991b1b">Never use for banking</text>
            <!-- Protected with VPN -->
            <rect x="190" y="15" width="165" height="115" rx="6" fill="#ecfdf5" stroke="#34d399"/>
            <text x="272" y="35" font-size="10.5" font-weight="900" fill="#065f46" text-anchor="middle">WITH VPN / 4G HOTSPOT ✓</text>
            <text x="200" y="60" font-size="9.5" font-weight="700" fill="#047857">• Military encrypted tunnel</text>
            <text x="200" y="80" font-size="9.5" font-weight="700" fill="#047857">• IP address hidden</text>
            <text x="200" y="100" font-size="9.5" font-weight="700" fill="#047857">• Traffic invisible to hackers</text>
            <text x="200" y="118" font-size="9" font-weight="800" fill="#065f46">Safe for work &amp; login</text>
          </g>"""),
        "golden_rule": 'Use mobile data hotspot or a VPN when connecting on public Wi-Fi!',
        "watch_out": 'Rogue open Wi-Fi hotspots can intercept unencrypted network passwords.',
        "challenge_prompt": "What does a Virtual Private Network (VPN) do to protect your data when using public Wi-Fi?",
        "answer_text": "It creates an encrypted tunnel between your device and the internet, preventing anyone on the public network from viewing your data."
    },

    # 47. Privacy Settings on Social Media
    {
        "id": "dfs-47",
        "number": 47,
        "title": "Social Media Privacy Settings",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.7",
        "rule_heading": "Auditing Visibility, Location Tags &amp; Permissions",
        "rule_body": "Safeguarding social media profiles: 1. Set account visibility to 'Private' or 'Friends Only' (never Public). 2. Disable location tagging on posts and photos. 3. Audit third-party apps connected to your profile. 4. Never post identifying details (birth year, mother's maiden name, holiday dates).",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <rect x="0" y="0" width="370" height="26" rx="8" fill="#7c3aed"/>
            <text x="185" y="18" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">SOCIAL PRIVACY AUDIT CHECKLIST</text>
            <g transform="translate(20, 36)">
              <rect x="0" y="0" width="330" height="22" rx="4" fill="#f5f3ff"/>
              <text x="10" y="15" font-size="9.5" font-weight="800" fill="#5b21b6">✓ Account Privacy: Set to 'Friends Only' (Hidden from public search)</text>
              <rect x="0" y="26" width="330" height="22" rx="4" fill="#f5f3ff"/>
              <text x="10" y="41" font-size="9.5" font-weight="800" fill="#5b21b6">✓ Location Services: Geotagging turned OFF on photos</text>
              <rect x="0" y="52" width="330" height="22" rx="4" fill="#f5f3ff"/>
              <text x="10" y="67" font-size="9.5" font-weight="800" fill="#5b21b6">✓ Connected Apps: Revoked permissions for unused quizzes &amp; games</text>
              <rect x="0" y="78" width="330" height="22" rx="4" fill="#f5f3ff"/>
              <text x="10" y="93" font-size="9.5" font-weight="800" fill="#5b21b6">✓ Sensitive Data: Full birth date, phone &amp; home address hidden</text>
            </g>
          </g>"""),
        "golden_rule": 'Keep profiles private and avoid posting live location updates when away!',
        "watch_out": 'Never post photos of boarding passes — barcodes contain sensitive data.',
        "challenge_prompt": "Why is announcing on public social media that your family is departing for a 2-week holiday a significant security risk?",
        "answer_text": "It alerts potential burglars that your home will be unoccupied during that exact timeframe."
    },

    # 48. Digital Footprint & Online Reputation
    {
        "id": "dfs-48",
        "number": 48,
        "title": "Digital Footprint &amp; Reputation",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.8",
        "rule_heading": "Permanent Traces &amp; Employer Background Checks",
        "rule_body": "Your digital footprint is the permanent trail of data left by your online activities: comments, posts, tagged photos, forum reviews. Facts: 1. Deleted posts can be archived or screenshotted. 2. 70%+ of UK employers check applicants' public online profiles. 3. Follow the 'billboard test'.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <text x="185" y="24" font-size="11.5" font-weight="900" fill="#0f172a" text-anchor="middle">YOUR DIGITAL FOOTPRINT IS PERMANENT</text>
            <!-- Graphic components -->
            <rect x="15" y="38" width="165" height="95" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="97" y="58" font-size="10.5" font-weight="900" fill="#1e40af" text-anchor="middle">WHAT IS TRACKED?</text>
            <text x="25" y="78" font-size="9" font-weight="700" fill="#1e3a8a">• Public social comments</text>
            <text x="25" y="94" font-size="9" font-weight="700" fill="#1e3a8a">• Tagged photos &amp; videos</text>
            <text x="25" y="110" font-size="9" font-weight="700" fill="#1e3a8a">• Search history &amp; reviews</text>
            <rect x="190" y="38" width="165" height="95" rx="6" fill="#fdf2f8" stroke="#ec4899"/>
            <text x="272" y="58" font-size="10.5" font-weight="900" fill="#9d174d" text-anchor="middle">EMPLOYER AUDITS</text>
            <text x="200" y="78" font-size="9" font-weight="700" fill="#be185d">• 70%+ check social media</text>
            <text x="200" y="94" font-size="9" font-weight="700" fill="#be185d">• Offensive posts lose jobs</text>
            <text x="200" y="118" font-size="8.5" font-weight="800" fill="#831843">"Billboard test": Post wisely!</text>
          </g>"""),
        "golden_rule": 'Only post content you would be comfortable showing to an employer!',
        "watch_out": 'Deleting a post does not remove cached versions or viewer screenshots.',
        "challenge_prompt": "What is a 'digital footprint', and how can it impact a person's career prospects?",
        "answer_text": "It is the permanent trail of online activity; employers routinely research candidates online, and inappropriate posts can result in rejected applications."
    },

    # 49. Digital Wellbeing & Screen Time Management
    {
        "id": "dfs-49",
        "number": 49,
        "title": "Digital Wellbeing &amp; Ergonomics",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.9",
        "rule_heading": "The 20-20-20 Rule, Posture &amp; Screen Limits",
        "rule_body": "Health habits for computer users: 1. 20-20-20 Rule: Every 20 minutes, look at an object 20 feet away for 20 seconds to prevent digital eye strain. 2. Ergonomics: Top of screen at eye level, 90° elbow angle, feet flat. 3. Night light / Blue light filter to safeguard sleep cycles.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- 20-20-20 Box -->
            <rect x="15" y="15" width="165" height="115" rx="6" fill="#f0fdf4" stroke="#22c55e"/>
            <text x="97" y="35" font-size="10.5" font-weight="900" fill="#15803d" text-anchor="middle">THE 20-20-20 RULE</text>
            <text x="25" y="60" font-size="9.5" font-weight="800" fill="#166534">⏱ Every 20 minutes</text>
            <text x="25" y="80" font-size="9.5" font-weight="800" fill="#166534">👀 Look 20 feet away</text>
            <text x="25" y="100" font-size="9.5" font-weight="800" fill="#166534">⏳ For 20 seconds</text>
            <text x="25" y="118" font-size="9" font-weight="700" fill="#14532d">Relieves eye fatigue</text>
            <!-- Ergonomics Box -->
            <rect x="190" y="15" width="165" height="115" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
            <text x="272" y="35" font-size="10.5" font-weight="900" fill="#1e40af" text-anchor="middle">DESK ERGONOMICS</text>
            <text x="200" y="60" font-size="9.5" font-weight="700" fill="#1e3a8a">• Screen top at eye level</text>
            <text x="200" y="80" font-size="9.5" font-weight="700" fill="#1e3a8a">• Elbows at 90-degree angle</text>
            <text x="200" y="100" font-size="9.5" font-weight="700" fill="#1e3a8a">• Feet flat on the floor</text>
            <text x="200" y="118" font-size="9" font-weight="700" fill="#1e3a8a">• Blue light filter at night</text>
          </g>"""),
        "golden_rule": 'Follow the 20-20-20 rule to prevent digital eye strain during desk work!',
        "watch_out": 'Blue light in bed disrupts natural melatonin and degrades sleep quality.',
        "challenge_prompt": "What does the 20-20-20 rule recommend to help prevent screen-related eye strain?",
        "answer_text": "Every 20 minutes, take a 20-second break to look at an object at least 20 feet away."
    },

    # 50. Copyright, Creative Commons & Fair Use
    {
        "id": "dfs-50",
        "number": 50,
        "title": "Copyright &amp; Creative Commons",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Safe & Responsible",
        "strand_theme": "rose",
        "dfe_code": "DFS 5.10",
        "rule_heading": "Intellectual Property, CC Licences &amp; Attribution",
        "rule_body": "Digital media ownership rules: 1. Copyright (©): Automatic legal ownership; you cannot copy or distribute without the author's permission. 2. Creative Commons (CC): Licences allowing free reuse under specific conditions (e.g. CC-BY requires attribution). 3. Public Domain: Free for anyone.",
        "svg_html": wrap_svg("""
          <g transform="translate(40, 12)">
            <rect x="0" y="0" width="380" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Copyright -->
            <rect x="12" y="15" width="112" height="115" rx="6" fill="#fef2f2" stroke="#f87171"/>
            <text x="68" y="36" font-size="10" font-weight="900" fill="#991b1b" text-anchor="middle">© COPYRIGHT</text>
            <text x="68" y="58" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">All Rights Reserved</text>
            <text x="68" y="74" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">Cannot use without</text>
            <text x="68" y="90" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">written permission</text>
            <text x="68" y="115" font-size="8.5" font-weight="800" fill="#7f1d1d" text-anchor="middle">Default protection</text>
            <!-- Creative Commons -->
            <rect x="134" y="15" width="112" height="115" rx="6" fill="#eff6ff" stroke="#60a5fa"/>
            <text x="190" y="36" font-size="9.5" font-weight="900" fill="#1e40af" text-anchor="middle">CREATIVE COMMONS</text>
            <text x="190" y="58" font-size="9" font-weight="700" fill="#2563eb" text-anchor="middle">Free to share &amp; use</text>
            <text x="190" y="74" font-size="9" font-weight="700" fill="#2563eb" text-anchor="middle">Must follow rules:</text>
            <text x="190" y="90" font-size="9" font-weight="700" fill="#2563eb" text-anchor="middle">e.g. BY (Attribute)</text>
            <text x="190" y="115" font-size="8.5" font-weight="800" fill="#1d4ed8" text-anchor="middle">Attribution required ✓</text>
            <!-- Public Domain -->
            <rect x="256" y="15" width="112" height="115" rx="6" fill="#ecfdf5" stroke="#34d399"/>
            <text x="312" y="36" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">PUBLIC DOMAIN</text>
            <text x="312" y="58" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">Copyright expired</text>
            <text x="312" y="74" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">or waived (CC0)</text>
            <text x="312" y="90" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">Free for commercial</text>
            <text x="312" y="115" font-size="8.5" font-weight="800" fill="#047857" text-anchor="middle">Unrestricted ✓</text>
          </g>"""),
        "golden_rule": 'Verify image license terms before using web images in published work!',
        "watch_out": 'Google Image results are NOT automatically free or cleared for use.',
        "challenge_prompt": "What does a Creative Commons 'Attribution' (CC-BY) license require you to do when using someone else's digital graphic?",
        "answer_text": "You must credit the original creator, provide a link to the license, and indicate if changes were made."
    }
]

for card in CARDS:
    ET.fromstring(card["svg_html"])
print(f"Validated DFS Area 5: {len(CARDS)} cards")
