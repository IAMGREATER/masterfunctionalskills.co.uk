"""
books/a4/expand_english_and_digital.py
Adds:
1. 8 pages of the 11 Core Writing Formats & Band 4 Archetypes + 2 pages of Reading Taxonomy & SPaG Trap Diagnostic to Mock Pack English L2 -> exactly 86 pages!
2. 4 pages of Advanced Workplace IT Cheatsheets & Security Frameworks to Digital Skills Handbook -> exactly 84 pages!
3. Re-runs generate_full_builder.py to update build_specialist_suite_a4.py.
"""

from pathlib import Path

BUILDER_GEN = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/generate_full_builder.py")

ENGLISH_FORMATS_INSERT = '''
    # pp55–p62: Masterclass: The 11 Core Writing Formats & Band 4 Archetypes (8 pages)
    writing_formats_data = [
        ("Format Archetype 1 &bull; Formal Letters (Complaint &amp; Application)", "WF1",
         "Mastering formal sender/recipient headers, date, salutation, tone, and complimentary close.",
         "writing document contract legal notes fountain pen",
         "<b>Structural Anatomy:</b> Sender address top right; recipient address top left; date beneath; formal salutation (<code>Dear Sir/Madam</code> paired with <code>Yours faithfully</code>; named recipient <code>Dear Ms Jenkins</code> paired with <code>Yours sincerely</code>).<br><br>"
         "<b>Band 4 Content Strategy:</b> (1) Opening state the precise purpose of writing. (2) Provide factual background chronology. (3) State the impact on the client/applicant. (4) Conclude with a definitive call to action and deadline.",
         "Format 1 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Formal addresses aligned &bull; [ ] Formal salutation &amp; matching sign-off &bull; [ ] Zero informal contractions &bull; [ ] Precise chronology &bull; [ ] Remedial deadline.<br><br>"
         "<b>Model Opening:</b> <i>'I am writing to formally register my dissatisfaction with the emergency heating repairs conducted at our residential facility on 12 October 2026...'</i>"),

        ("Format Archetype 2 &bull; Formal Workplace Recommendation Reports", "WF2",
         "Executive document design: structured headers, findings, data tables, and risk mitigations.",
         "corporate business report analysis charts desk",
         "<b>Structural Anatomy:</b> Standard memo/report header (To, From, Date, Subject); numbered sections (1. Executive Summary, 2. Current Operational Bottlenecks, 3. Options Appraisal, 4. Risk Mitigation Matrix, 5. Definitive Recommendations).<br><br>"
         "<b>Band 4 Tone Strategy:</b> Maintain third-person objective register (<i>'The data indicates...'</i> rather than <i>'I think...'</i>). Use passive voice strategically to emphasize findings.",
         "Format 2 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Formal 4-part memo header &bull; [ ] Numbered subheadings &bull; [ ] Bulleted data points &bull; [ ] Balanced risk analysis &bull; [ ] Specific costed recommendations.<br><br>"
         "<b>Model Section:</b> <i>'3.2 Options Appraisal: Transitioning to cloud-hosted telematics incurs a one-off setup cost of &pound;12,400 but eliminates annual server licensing fees of &pound;6,200...'</i>"),

        ("Format Archetype 3 &bull; Business Proposals &amp; Funding Bids", "WF3",
         "Persuasive commercial proposals: community need, cost-benefit analysis, and deliverable milestones.",
         "business handshake deal partnership contract desk",
         "<b>Structural Anatomy:</b> Clear project title, organizational background, statement of demonstrated need, project deliverables with timeline milestones, budget breakdown table, and legacy sustainability plan.<br><br>"
         "<b>Band 4 Persuasive Strategy:</b> Weave qualitative community impact with quantitative fiscal metrics. Highlight statutory compliance (e.g. Equality Act, Health &amp; Safety).",
         "Format 3 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Compelling proposal title &bull; [ ] Demonstrated need with census/local data &bull; [ ] Phased delivery milestones &bull; [ ] Itemized budget table &bull; [ ] Volunteer legacy.<br><br>"
         "<b>Model Extract:</b> <i>'This capital grant will directly unlock 350 weekly youth mentoring hours across three high-deprivation wards, yielding a projected 24% reduction in local antisocial incidents...'</i>"),

        ("Format Archetype 4 &bull; Public Newspaper &amp; Magazine Articles", "WF4",
         "Engaging journalistic writing: headline, byline, hook, balanced perspectives, and call to action.",
         "newspaper printing press journalism article layout",
         "<b>Structural Anatomy:</b> Snappy, memorable headline (using alliteration, rhyme, or pun); author byline; dramatic narrative hook in paragraph 1; balanced debate presenting opposing viewpoints; concluding synthesis and inspiring forward look.<br><br>"
         "<b>Band 4 Rhetorical Strategy:</b> Use sensory imagery, tri-colon listings, rhetorical questions, and varied sentence lengths to maintain vibrant reader interest.",
         "Format 4 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Creative headline &bull; [ ] Journalistic byline &bull; [ ] Vivid opening hook &bull; [ ] Balanced stakeholder quotes &bull; [ ] Concluding call to action.<br><br>"
         "<b>Model Hook:</b> <i>'Step onto our high street on any rain-soaked Monday, and you will witness a quiet revolution taking place behind the Victorian shopfronts...'</i>"),

        ("Format Archetype 5 &bull; Persuasive Public Speeches", "WF5",
         "Oral rhetoric: direct audience address, emphatic repetition, pathos, and powerful call to action.",
         "podium microphone speech conference public speaking",
         "<b>Structural Anatomy:</b> Welcoming audience acknowledgment (<i>'Good evening councillors and fellow residents...'</i>); personal stake/connection; statement of the crisis; triadic arguments; rebuttal of naysayers; soaring final appeal.<br><br>"
         "<b>Band 4 Spoken Register Strategy:</b> Written for the ear, not the eye! Use short punchy sentences for emotional weight, pauses (indicated by dashes), and anaphora (repeated opening phrases).",
         "Format 5 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Explicit audience address &bull; [ ] Anaphora &amp; rhetorical repetition &bull; [ ] Triadic list &bull; [ ] Emotive personal appeal &bull; [ ] Definite rousing call to action.<br><br>"
         "<b>Model Crescendo:</b> <i>'We have spoken. We have petitioned. We have waited. The time for empty council platitudes has ended; the time for decisive funding is NOW.'</i>"),

        ("Format Archetype 6 &bull; Informative Guidance Leaflets &amp; Brochures", "WF6",
         "Public information layout: catchy subheadings, bulleted guidance, FAQ boxes, and contact directory.",
         "brochure leaflet graphic design typography print",
         "<b>Structural Anatomy:</b> Title banner with clear purpose; introductory paragraph outlining who the leaflet is for; categorized advice subsections with imperative action verbs; bullet points for rapid scanning; emergency contacts box.<br><br>"
         "<b>Band 4 Clarity Strategy:</b> Direct address using second person (<i>'You should...'</i>); clear conditional rules (<i>'If you experience X, immediately contact Y'</i>); plain English without confusing jargon.",
         "Format 6 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Distinct leaflet banner &bull; [ ] Short scannable paragraphs &bull; [ ] Bulleted action steps &bull; [ ] Highlighted safety warnings &bull; [ ] Helpdesk contact details.<br><br>"
         "<b>Model Advice Box:</b> <i>'What to do in an electrical outage: (1) Unplug sensitive medical equipment. (2) Keep refrigerator doors closed. (3) Report the outage to 105 immediately.'</i>"),

        ("Format Archetype 7 &bull; Critical Reviews &amp; Evaluations", "WF7",
         "Evaluative writing: rating criteria, balanced strengths and weaknesses, and target audience verdict.",
         "laptop review stars rating consumer test technology",
         "<b>Structural Anatomy:</b> Item/service title and star rating; context of the review; criteria-by-criteria evaluation (e.g. Value for Money, Reliability, Usability, Customer Service); balanced drawbacks; definitive final verdict.<br><br>"
         "<b>Band 4 Evaluative Strategy:</b> Sophisticated evaluative adjectives (<i>'exemplary', 'cumbersome', 'substandard', 'unrivalled'</i>); balanced comparison against market competitors.",
         "Format 7 Band 4 Checklist &amp; Layout Model",
         "<b>Checklist:</b> [ ] Star rating or score badge &bull; [ ] Multi-criteria evaluation &bull; [ ] Specific comparative evidence &bull; [ ] Balanced pros &amp; cons &bull; [ ] Clear target audience recommendation.<br><br>"
         "<b>Model Verdict:</b> <i>'While the software dashboard suffers from an initial steep learning curve, its automated invoicing tools make it an indispensable investment for expanding SMEs.'</i>"),

        ("Format Archetypes 8&ndash;11 &bull; Workplace Emails, Memos, Blogs &amp; Press Releases", "WF8",
         "Agile digital communications: subject syntax, netiquette, SEO web copy, and news release structure.",
         "office computer keyboard typing corporate communication",
         "<b>Formats 8 &amp; 9: Workplace Emails &amp; Internal Memos:</b> Clear prefix tag <code>[ACTION]</code>, professional salutation, 3-tier body (Context &rarr; Detail &rarr; Required Action), polite professional sign-off.<br><br>"
         "<b>Formats 10 &amp; 11: Web Blogs &amp; Press Releases:</b> Blogs require engaging conversational hooks and reader comments prompts. Press Releases mandate <code>FOR IMMEDIATE RELEASE</code>, embargo date, boilerplate 'Notes to Editors', and media contact.",
         "Formats 8-11 Band 4 Checklist &amp; Core Standards",
         "<b>Checklist:</b> [ ] Email: Clear subject with deadline &bull; [ ] Memo: Standard 4 headers &bull; [ ] Blog: Conversational register &bull; [ ] Press Release: <code>FOR IMMEDIATE RELEASE</code> and media contact details.<br><br>"
         "<b>Model Press Header:</b> <i>'FOR IMMEDIATE RELEASE &bull; 14 October 2026 &bull; Regional Skills Hub Launches &pound;2m Green Apprenticeship Initiative. Media Contact: press@skillshub.org.uk'</i>")
    ]

    for wf_title, badge, lead, photo_kw, theory_html, box_title, box_html in writing_formats_data:
        wf_body = (
            K.page_title(wf_title, kicker="Pearson Edexcel Level 2 Writing Formats Masterclass", badge=badge)
            + K.hero_image(P(photo_kw), lead, 38)
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{theory_html}</div>", title="Format Structural Architecture &amp; Examiner Criteria")
            + K.box_html(f"<div style='font-size:10.5pt; line-height:1.45;'>{box_html}</div>", title=box_title)
            + K.fill_notes("Personal Writing Anchors &amp; Sentence Starters", 22)
        )
        pages.append(K.page(wf_body, header=(BOOK, f"{badge} &bull; Writing Format"), footer=BOOK, page_no=p_curr))
        p_curr += 1
'''

DIGITAL_EXTRA_INSERT = '''
    # pp75–p78: Advanced Workplace IT Frameworks & Diagnostic Reference (4 pages)
    extra_it_pages = [
        ("Workplace File Format &amp; Extension Directory", "IT.REF1",
         "Comprehensive classification of corporate file formats, compression algorithms, and application associations.",
         "computer server hard drive data technology storage",
         "<table style='width:100%; border-collapse:collapse; font-size:10pt; line-height:1.45;'>"
         "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Extension</th><th style='padding:6px; text-align:left;'>Category</th><th style='padding:6px; text-align:left;'>Associated Software</th><th style='padding:6px; text-align:left;'>Security &amp; Compatibility Notes</th></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.pdf</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Document</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Adobe Acrobat / Edge</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Preserves formatting across platforms; read-only default.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.docx / .odt</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Word Processing</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Word / LibreOffice</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Standard editable documents. May harbor malicious macros.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.xlsx / .csv</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Spreadsheet</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Excel / Google Sheets</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>.csv is plain text without formulas; .xlsx supports formulas and charts.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.png / .jpg</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Raster Image</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Photos / Browser</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>.png supports transparency; .jpg provides high photographic compression.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.zip / .tar.gz</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Archive</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>WinZip / 7-Zip</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Bundles and compresses multiple files; scan before extraction.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>.exe / .bat</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Executable</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Windows OS Core</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Executes code directly. <b>Extreme danger in email attachments!</b></td></tr>"
         "</table>",
         "Golden Rule: Never double-click an executable attachment (.exe, .scr, .vbs) received via email, even if the sender appears familiar!"),

        ("Spreadsheet Error Diagnostics &amp; Function Syntax", "IT.REF2",
         "Troubleshooting calculation errors, reference issues, and syntax anomalies under pressure.",
         "calculator accounting finance numbers calculation",
         "<table style='width:100%; border-collapse:collapse; font-size:10pt; line-height:1.45;'>"
         "<tr style='background:#f1f5f9;'><th style='padding:6px; text-align:left;'>Error Code</th><th style='padding:6px; text-align:left;'>Root Cause</th><th style='padding:6px; text-align:left;'>Remediation Step</th></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#DIV/0!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Dividing by zero or an empty cell.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Wrap formula in <code>=IF(B2=0, 0, A2/B2)</code> to handle zero values safely.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#VALUE!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Mathematical operation performed on text string.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Verify that referenced cells contain purely numerical digits, not symbols.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#REF!</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Cell referenced in formula was deleted.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Undo deletion (<code>Ctrl + Z</code>) or re-point the formula to the correct active coordinate.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#NAME?</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Misspelled function name (e.g. <code>=AVRAGE</code>).</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Correct spelling to standard syntax: <code>=AVERAGE()</code>, <code>=SUM()</code>, <code>=COUNT()</code>.</td></tr>"
         "<tr><td style='padding:5px; border-bottom:1px solid #e2e8f0;'><b>#####</b></td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Column width is too narrow to display the number.</td><td style='padding:5px; border-bottom:1px solid #e2e8f0;'>Double-click column boundary header line to autofit column width.</td></tr>"
         "</table>",
         "Pro-Tip: Always use the Formula Auditing toolbar (Trace Precedents / Trace Dependents) to visualize how formulas link across large workbooks."),

        ("Cybersecurity Incident Escalation &amp; GDPR Action Flowchart", "IT.REF3",
         "Statutory protocols for reporting unauthorized data disclosures and suspected cyber intrusions.",
         "cybersecurity lock shield data protection screen",
         "<div style='font-size:10.5pt; line-height:1.5;'>"
         "<p><b>Phase 1 &bull; Immediate Containment (Minutes 0&ndash;15):</b><br>"
         "&bull; Disconnect device from Wi-Fi/Ethernet immediately. Do NOT turn off the computer (preserves forensic volatile RAM memory).<br>"
         "&bull; Alert immediate line manager and designated Information Security Officer.</p>"
         "<p><b>Phase 2 &bull; Investigation &amp; Triage (Hours 1&ndash;24):</b><br>"
         "&bull; Determine category of breached data: Does it contain Special Category PII (medical records, biometric data, financial details)?<br>"
         "&bull; Audit access logs to establish extent of unauthorized extraction.</p>"
         "<p><b>Phase 3 &bull; Statutory Regulatory Disclosure (Within 72 Hours):</b><br>"
         "&bull; Under Article 33 of UK GDPR, the Information Commissioner's Office (ICO) must be notified within 72 hours of becoming aware of a high-risk personal data breach.<br>"
         "&bull; Notify affected data subjects without undue delay if risk to their rights and freedoms is significant.</p>"
         "</div>",
         "Legal Mandate: Fines for non-reporting under UK GDPR can reach &pound;17.5 million or 4% of global annual turnover, whichever is greater."),

        ("Workplace Digital Hygiene &amp; Device Ergonomics Audit", "IT.REF4",
         "Personal compliance audit for password security, multi-factor tokens, and postural health.",
         "office team computer meeting collaborative training",
         "<div style='font-size:10.5pt; line-height:1.5;'>"
         "<p><b>Digital Security Hygiene Checklist:</b><br>"
         "[ &nbsp; ] Passphrases consist of three random, memorable words (minimum 14 characters).<br>"
         "[ &nbsp; ] Multi-factor authentication (MFA) enabled on email, cloud drives, and internal portals.<br>"
         "[ &nbsp; ] Lock workstation screen (<code>Win + L</code>) whenever stepping away from desk.<br>"
         "[ &nbsp; ] Automatic software updates and anti-virus definitions set to auto-install overnight.<br>"
         "[ &nbsp; ] Work files saved exclusively on encrypted cloud backup drives, never on local desktop.</p>"
         "<p><b>Health &amp; Safety DSE Ergonomic Checklist:</b><br>"
         "[ &nbsp; ] Top of computer monitor positioned at eye level; distance 50&ndash;70 cm from face.<br>"
         "[ &nbsp; ] Forearms rest horizontal to desk surface; wrists remain straight during typing.<br>"
         "[ &nbsp; ] Lumbar spine supported by adjustable ergonomic backrest; feet flat on floor or footrest.<br>"
         "[ &nbsp; ] 20-20-20 rule implemented: Every 20 minutes, look at an object 20 feet away for 20 seconds.</p>"
         "</div>",
         "Lead Instructor Endorsement: Maintaining daily digital hygiene and physical ergonomics ensures long-term career productivity and regulatory compliance.")
    ]

    for it_title, badge, lead, photo_kw, content_html, box_rule in extra_it_pages:
        it_body = (
            K.page_title(it_title, kicker="Statutory Standards &amp; Workplace IT Framework", badge=badge)
            + K.hero_image(P(photo_kw), lead, 38)
            + K.box_html(content_html, title="Workplace Technical Specification &amp; Architecture")
            + K.rule_box("Core Professional Compliance Mandate", f"<p style='margin:0;'>{box_rule}</p>")
            + K.fill_notes("Personal Implementation Notes &amp; Enterprise Protocols", 22)
        )
        pages.append(K.page(it_body, header=(BOOK, f"{badge} &bull; IT Framework"), footer=BOOK, page_no=p_curr))
        p_curr += 1
'''

def update():
    with open(BUILDER_GEN, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Insert writing formats into English L2 right before masterclasses
    old_mc_target = "    # pp47–p54: 8 Masterclass Workshops (8 pages)\n    masterclasses = ["
    if ENGLISH_FORMATS_INSERT.strip() not in content and old_mc_target in content:
        content = content.replace(old_mc_target, ENGLISH_FORMATS_INSERT + "\n" + old_mc_target, 1)
        print("8 pages of 11 Writing Formats inserted into English L2 Mock Pack.")

    # 2. Insert extra IT framework pages into Digital Skills right before reference
    old_dig_ref = "    # pp63–p82: Back matter reference section (via K.ref_pages)\n    ref_blocks = []"
    if DIGITAL_EXTRA_INSERT.strip() not in content and old_dig_ref in content:
        content = content.replace(old_dig_ref, DIGITAL_EXTRA_INSERT + "\n" + old_dig_ref, 1)
        print("4 pages of Advanced IT Frameworks inserted into Digital Skills Handbook.")

    with open(BUILDER_GEN, "w", encoding="utf-8") as f:
        f.write(content)

    print("generate_full_builder.py updated with rich English & Digital extensions!")

if __name__ == "__main__":
    update()
