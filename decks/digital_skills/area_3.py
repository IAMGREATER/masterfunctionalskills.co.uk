#!/usr/bin/env python3
"""
Area 3: Communicating Online (Cards 25-32)
"""
import xml.etree.ElementTree as ET

def wrap_svg(inner_content, height=170):
    svg = f'<svg viewBox="0 0 460 {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">\n{inner_content}\n</svg>'
    ET.fromstring(svg)
    return svg

CARDS = [
    # 25. Email Etiquette & Professional Standards
    {
        "id": "dfs-25",
        "number": 25,
        "title": "Professional Email Structure",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.1",
        "rule_heading": "Clear, Actionable Email Hierarchy",
        "rule_body": "A professional email includes: 1. A clear, specific subject line. 2. A polite formal salutation. 3. Concise body paragraphs stating the main purpose. 4. An unambiguous call-to-action or deadline. 5. A professional sign-off and signature block.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
            <rect x="0" y="0" width="370" height="28" rx="8" fill="#7c3aed"/>
            <text x="185" y="19" font-size="11.5" font-weight="900" fill="#ffffff" text-anchor="middle">PROFESSIONAL EMAIL STRUCTURE</text>
            <text x="20" y="48" font-size="11" font-weight="800" fill="#4c1d95">Subject: Project Update: Q3 Budget Review - 14 Oct</text>
            <text x="20" y="70" font-size="10.5" font-weight="700" fill="#1e293b">Dear Ms Higgins, / Hi Team,</text>
            <text x="20" y="90" font-size="10" font-weight="600" fill="#475569">Please find attached the updated figures for your review.</text>
            <text x="20" y="110" font-size="10" font-weight="800" fill="#047857">Action: Kindly confirm sign-off by 5pm this Thursday.</text>
            <text x="20" y="132" font-size="10" font-weight="700" fill="#64748b">Kind regards, | Alex Patel (Senior Analyst)</text>
          </g>"""),
        "golden_rule": "Always write a descriptive subject line before composing the email body!",
        "watch_out": "Avoid vague or blank subject lines like 'urgent' or 'hi' which trigger spam filters.",
        "challenge_prompt": "Why is 'Q3 Budget Review - Approval Needed by Thursday' far more effective than just 'Budget' as an email subject line?",
        "answer_text": "It specifies the exact topic, the action required (approval), and the deadline, allowing the recipient to prioritize immediately."
    },

    # 26. Email Recipients: To, Cc, and Bcc
    {
        "id": "dfs-26",
        "number": 26,
        "title": "Email Fields: To, Cc &amp; Bcc",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.2",
        "rule_heading": "Direct Action vs Courtesy vs Privacy",
        "rule_body": "To: Direct recipients expected to read and take action. Cc (Carbon Copy): People kept informed for visibility; no direct action expected. Bcc (Blind Carbon Copy): Hidden recipients; preserves privacy and complies with UK GDPR when emailing groups.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- To row -->
            <rect x="15" y="14" width="60" height="26" rx="4" fill="#dbeafe"/>
            <text x="45" y="31" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">To:</text>
            <text x="85" y="31" font-size="11" font-weight="700" fill="#0f172a">Action Owner (e.g. John - needs to complete task)</text>
            <!-- Cc row -->
            <rect x="15" y="56" width="60" height="26" rx="4" fill="#fef3c7"/>
            <text x="45" y="73" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">Cc:</text>
            <text x="85" y="73" font-size="11" font-weight="700" fill="#0f172a">Informed only (e.g. Manager - keeps in the loop)</text>
            <!-- Bcc row -->
            <rect x="15" y="98" width="60" height="26" rx="4" fill="#fee2e2"/>
            <text x="45" y="115" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">Bcc:</text>
            <text x="85" y="115" font-size="10.5" font-weight="800" fill="#b91c1c">Hidden / Blind (protects privacy &amp; UK GDPR)</text>
            <text x="85" y="132" font-size="9.5" font-weight="600" fill="#64748b">Recipients cannot see each other's email addresses</text>
          </g>"""),
        "golden_rule": 'Use Bcc for group emails to keep recipient email addresses private!',
        "watch_out": "Putting client emails in 'To' or 'Cc' is a direct GDPR violation.",
        "challenge_prompt": "A community organiser is emailing 120 residents about a neighbourhood meeting. Should they use To, Cc, or Bcc?",
        "answer_text": "Bcc (Blind Carbon Copy), to prevent exposing residents' private email addresses to one another in violation of UK GDPR."
    },

    # 27. Email Attachments & Cloud File Sharing
    {
        "id": "dfs-27",
        "number": 27,
        "title": "Email Attachments &amp; Cloud Links",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.3",
        "rule_heading": "Direct File vs Cloud Share Link",
        "rule_body": "Email Attachments: Suitable for small individual files under 15-20 MB. Cloud Links (OneDrive, Google Drive): Best for large files, videos, or collaborative live editing. Cloud links prevent mailbox quota exhaustion and allow permission revoking.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 15)">
            <!-- Left box: Direct attachment -->
            <rect x="0" y="0" width="175" height="135" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.6"/>
            <text x="87" y="24" font-size="11" font-weight="900" fill="#334155" text-anchor="middle">DIRECT ATTACHMENT</text>
            <text x="18" y="52" font-size="10" font-weight="700" fill="#475569">• File size limit (~20 MB)</text>
            <text x="18" y="74" font-size="10" font-weight="700" fill="#475569">• Static snapshot copy</text>
            <text x="18" y="96" font-size="10" font-weight="700" fill="#dc2626">• Cannot revoke access</text>
            <text x="18" y="118" font-size="9.5" font-weight="800" fill="#64748b">Best for: Final invoices, receipts</text>
            <!-- Right box: Cloud link -->
            <rect x="195" y="0" width="175" height="135" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
            <text x="282" y="24" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">CLOUD SHARE LINK</text>
            <text x="210" y="52" font-size="10" font-weight="700" fill="#1e3a8a">• Unlimited file size</text>
            <text x="210" y="74" font-size="10" font-weight="700" fill="#1e3a8a">• Real-time live collaboration</text>
            <text x="210" y="96" font-size="10" font-weight="700" fill="#059669">• Permissions can be revoked</text>
            <text x="210" y="118" font-size="9.5" font-weight="800" fill="#2563eb">Best for: Large decks, team docs</text>
          </g>"""),
        "golden_rule": "Use cloud links instead of heavy attachments to avoid bouncing emails!",
        "watch_out": "Check sharing permissions before sending a cloud link so recipients can actually open it.",
        "challenge_prompt": "Why might an email containing a 65 MB video attachment fail to reach the recipient?",
        "answer_text": "Most email providers enforce attachment size limits between 20 MB and 25 MB, causing larger files to be rejected."
    },

    # 28. Video Calling Etiquette (Teams/Zoom)
    {
        "id": "dfs-28",
        "number": 28,
        "title": "Video Calling Setup &amp; Etiquette",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.4",
        "rule_heading": "Mute, Backgrounds &amp; Participation",
        "rule_body": "Key video meeting protocols: 1. Keep microphone MUTED when not speaking to eliminate background noise. 2. Enable Background Blur or a neutral virtual background for privacy. 3. Use 'Raise Hand' feature to speak without interrupting. 4. Maintain eye contact near camera.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.6"/>
            <!-- Video tiles -->
            <rect x="15" y="15" width="165" height="85" rx="6" fill="#334155"/>
            <text x="97" y="55" font-size="11" font-weight="800" fill="#94a3b8" text-anchor="middle">Speaker (Camera ON)</text>
            <rect x="190" y="15" width="165" height="85" rx="6" fill="#0f172a"/>
            <text x="272" y="55" font-size="11" font-weight="800" fill="#64748b" text-anchor="middle">Blur Background (Privacy)</text>
            <!-- Controls bar -->
            <rect x="15" y="108" width="340" height="26" rx="13" fill="#0f172a"/>
            <text x="65" y="125" font-size="10" font-weight="800" fill="#ef4444" text-anchor="middle">🔇 Mic Muted</text>
            <text x="145" y="125" font-size="10" font-weight="800" fill="#10b981" text-anchor="middle">📹 Cam Active</text>
            <text x="230" y="125" font-size="10" font-weight="800" fill="#f59e0b" text-anchor="middle">✋ Raise Hand</text>
            <text x="305" y="125" font-size="10" font-weight="800" fill="#38bdf8" text-anchor="middle">💬 Chat</text>
          </g>"""),
        "golden_rule": 'Mute your microphone when not speaking to eliminate background noise!',
        "watch_out": 'Place light in FRONT of you — backlighting turns you into a shadow.',
        "challenge_prompt": "What two features in Microsoft Teams help protect your home privacy and prevent talking over colleagues?",
        "answer_text": "Background Blur (protects privacy) and the 'Raise Hand' button (prevents speaking over others)."
    },

    # 29. Workplace Chat & Collaboration (Teams/Slack)
    {
        "id": "dfs-29",
        "number": 29,
        "title": "Workplace Messaging (Teams/Slack)",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.5",
        "rule_heading": "Channels vs Direct Messages (DMs)",
        "rule_body": "Organise chat communication efficiently: 1. Use Channels for team-wide project topics and public discussions. 2. Use Direct Messages (DMs) for private, 1-to-1 conversations. 3. Use thread replies to keep specific conversations clustered. 4. Use @mentions sparingly.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Sidebar -->
            <rect x="0" y="0" width="120" height="145" rx="8" fill="#312e81"/>
            <text x="60" y="24" font-size="11" font-weight="900" fill="#c7d2fe" text-anchor="middle">CHANNELS</text>
            <text x="15" y="48" font-size="10" font-weight="800" fill="#ffffff"># general</text>
            <text x="15" y="70" font-size="10" font-weight="800" fill="#a5b4fc"># project-alpha</text>
            <text x="15" y="92" font-size="10" font-weight="800" fill="#a5b4fc"># it-support</text>
            <text x="15" y="122" font-size="9.5" font-weight="800" fill="#fbbf24">💬 DMs (1-to-1)</text>
            <!-- Chat panel -->
            <text x="140" y="30" font-size="11" font-weight="900" fill="#1e1b4b"># project-alpha &gt; Thread</text>
            <rect x="135" y="42" width="225" height="42" rx="6" fill="#e0e7ff"/>
            <text x="143" y="58" font-size="9" font-weight="800" fill="#3730a3">Sarah: @David has client report been sent?</text>
            <text x="143" y="74" font-size="8.5" font-weight="600" fill="#4338ca">Use @mention to notify specific owners directly</text>
            <rect x="135" y="92" width="225" height="38" rx="6" fill="#f1f5f9"/>
            <text x="143" y="112" font-size="9" font-weight="800" fill="#0f172a">David: Replying in thread: Yes, sent at 2pm! ✓</text>
          </g>"""),
        "golden_rule": 'Use @mentions only when an immediate action or response is required!',
        "watch_out": 'Avoid @everyone for routine updates — it creates notification fatigue.',
        "challenge_prompt": "When should you discuss a work issue in a public project channel rather than sending a private direct message?",
        "answer_text": "When the information, decision, or answer is relevant to the entire team and should be searchable in future."
    },

    # 30. Calendar Invites & Scheduling
    {
        "id": "dfs-30",
        "number": 30,
        "title": "Online Calendar Invites &amp; Scheduling",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.6",
        "rule_heading": "Creating Invites, Times &amp; Agendas",
        "rule_body": "To schedule effective meetings: 1. Add clear Title and meeting purpose. 2. Specify Date, Start time, and Duration. 3. Include meeting link (Teams/Meet) or physical room. 4. Use Scheduling Assistant to check attendees' free/busy availability. 5. Include an agenda.",
        "svg_html": wrap_svg("""
          <g transform="translate(45, 12)">
            <rect x="0" y="0" width="370" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <rect x="0" y="0" width="370" height="26" rx="8" fill="#4338ca"/>
            <text x="185" y="18" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">NEW MEETING INVITATION</text>
            <text x="20" y="48" font-size="10.5" font-weight="800" fill="#0f172a">Title: Monthly Team Performance Review</text>
            <text x="20" y="68" font-size="10" font-weight="700" fill="#475569">When: Wed 15 Nov 2024, 10:00 - 11:00 AM (1 hr)</text>
            <text x="20" y="88" font-size="10" font-weight="700" fill="#2563eb">Location: Microsoft Teams Online Meeting (Link Auto-Generated)</text>
            <rect x="20" y="98" width="330" height="36" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
            <text x="30" y="113" font-size="9.5" font-weight="800" fill="#334155">Scheduling Assistant Check: [✓ All Required Attendees Free]</text>
            <text x="30" y="127" font-size="9" font-weight="600" fill="#64748b">RSVP Tracking: Accepted (8) | Tentative (1) | Declined (0)</text>
          </g>"""),
        "golden_rule": 'Always include the video link and agenda in the calendar description!',
        "watch_out": 'Check colleague availability and working hours before sending invites.',
        "challenge_prompt": "What calendar feature lets you view whether your colleagues are in other meetings before scheduling an appointment?",
        "answer_text": "The Scheduling Assistant (or 'Find a Time' view)."
    },

    # 31. Digital Netiquette & Tone
    {
        "id": "dfs-31",
        "number": 31,
        "title": "Digital Netiquette &amp; Tone",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.7",
        "rule_heading": "Written Nuance in Online Spaces",
        "rule_body": "Digital messages lack body language and vocal inflections. Follow core netiquette: 1. NEVER WRITE IN ALL CAPS (read as shouting). 2. Avoid ambiguous sarcasm or irony. 3. Be polite, constructive, and concise. 4. Proofread messages before hitting send.",
        "svg_html": wrap_svg("""
          <g transform="translate(38, 12)">
            <rect x="0" y="0" width="384" height="145" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Bad tone box -->
            <rect x="14" y="15" width="172" height="115" rx="6" fill="#fef2f2" stroke="#f87171" stroke-width="1.4"/>
            <text x="100" y="34" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">POOR NETIQUETTE ✗</text>
            <text x="24" y="53" font-size="9.5" font-weight="800" fill="#dc2626">"WHY HAVEN'T YOU</text>
            <text x="24" y="67" font-size="9.5" font-weight="800" fill="#dc2626">DONE THIS YET??"</text>
            <text x="24" y="87" font-size="8.8" font-weight="700" fill="#7f1d1d">• ALL CAPS = shouting</text>
            <text x="24" y="105" font-size="8.8" font-weight="700" fill="#7f1d1d">• Aggressive &amp; accusatory</text>
            <!-- Good tone box -->
            <rect x="198" y="15" width="172" height="115" rx="6" fill="#f0fdf4" stroke="#4ade80" stroke-width="1.4"/>
            <text x="284" y="34" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">EXCELLENT NETIQUETTE ✓</text>
            <text x="208" y="53" font-size="9.5" font-weight="700" fill="#15803d">"Hi Sam, please could</text>
            <text x="208" y="67" font-size="9.5" font-weight="700" fill="#15803d">you send the report?"</text>
            <text x="208" y="87" font-size="8.8" font-weight="700" fill="#14532d">• Polite, clear &amp; professional</text>
            <text x="208" y="105" font-size="8.8" font-weight="700" fill="#14532d">• Constructive collaboration</text>
          </g>"""),
        "golden_rule": "Re-read your message through the recipient's eyes before clicking send!",
        "watch_out": "Words typed in CAPITAL LETTERS are universally understood online as shouting.",
        "challenge_prompt": "Why is typing workplace communications in capital letters considered unacceptable digital practice?",
        "answer_text": "Typing in all capital letters is universally perceived as shouting, aggressive, or hostile."
    },

    # 32. Document Sharing Permissions
    {
        "id": "dfs-32",
        "number": 32,
        "title": "Document Sharing Permissions",
        "subject": "digital",
        "level": "l2",
        "subject_label": "Digital Skills",
        "level_label": "Level 1 / 2",
        "strand_name": "Communicating Online",
        "strand_theme": "purple",
        "dfe_code": "DFS 3.8",
        "rule_heading": "Viewer vs Commenter vs Editor Roles",
        "rule_body": "Protect cloud files by assigning the minimum required permissions: 1. Can View (Read-Only; cannot modify or delete content). 2. Can Comment (can read and leave margin feedback notes without altering text). 3. Can Edit (Full read/write permissions). Restrict links to specific people.",
        "svg_html": wrap_svg("""
          <g transform="translate(35, 12)">
            <rect x="0" y="0" width="390" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
            <!-- Tier 1: View -->
            <rect x="12" y="14" width="366" height="34" rx="6" fill="#f1f5f9"/>
            <text x="24" y="35" font-size="11" font-weight="900" fill="#0f172a">👁 Can View</text>
            <text x="135" y="35" font-size="9" font-weight="600" fill="#475569">Recipients can read &amp; download; cannot edit</text>
            <!-- Tier 2: Comment -->
            <rect x="12" y="55" width="366" height="34" rx="6" fill="#e0f2fe"/>
            <text x="24" y="76" font-size="11" font-weight="900" fill="#0369a1">💬 Can Comment</text>
            <text x="135" y="76" font-size="9" font-weight="600" fill="#0284c7">Can suggest edits &amp; add margin comments</text>
            <!-- Tier 3: Edit -->
            <rect x="12" y="96" width="366" height="34" rx="6" fill="#fef3c7"/>
            <text x="24" y="117" font-size="11" font-weight="900" fill="#92400e">✏️ Can Edit</text>
            <text x="135" y="117" font-size="9" font-weight="600" fill="#b45309">Can modify text, delete content &amp; share</text>
          </g>"""),
        "golden_rule": "Set permissions to 'Can View' unless collaborative editing is needed!",
        "watch_out": "Never set links to 'Anyone with the link can edit' for company files.",
        "challenge_prompt": "Which sharing permission should you give a client to let them review a proposal and suggest changes without risking text deletion?",
        "answer_text": "'Can Comment' (Commenter permission)."
    }
]

for card in CARDS:
    ET.fromstring(card["svg_html"])
print(f"Validated DFS Area 3: {len(CARDS)} cards")
