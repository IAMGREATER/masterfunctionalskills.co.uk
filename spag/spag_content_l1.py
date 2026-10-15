# spag_content.py
# Comprehensive, pedagogically rigorous SPaG content mapped to the 11 Pearson Edexcel Writing Formats
# for Level 1 and Level 2 Functional Skills English.

L1_UNITS = [
    {
        "unit": 1,
        "format": "Article",
        "title": "Sentence Boundaries, Complete Sentences & Capital Letters",
        "subtitle": "Writing Catchy Article Headlines & Punchy Paragraphs",
        "rule_title": "Core Grammar Rule: What Makes a Complete Sentence?",
        "rule_text": """A complete sentence must contain three things: <strong>a subject</strong> (who or what), <strong>a main verb</strong> (the action or state of being), and <strong>a complete thought</strong>. It must start with a capital letter and conclude with an end mark (full stop, question mark, or exclamation mark).<br><br>
<strong>Common Pitfalls in Articles:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Sentence Fragments:</strong> Incomplete thoughts missing a subject or verb (e.g. <em>"Because it is very healthy."</em> &rarr; Fix: <em>"Many people enjoy walking because it is very healthy."</em>).</li>
  <li><strong>Run-on Sentences:</strong> Two complete sentences joined together with no punctuation (e.g. <em>"The gym opened today it has great facilities."</em> &rarr; Fix: <em>"The gym opened today. It has great facilities."</em>).</li>
  <li><strong>Capital Letter Rules:</strong> Always capitalise the pronoun <strong>'I'</strong>, proper nouns (names of people, places, days, months), and the first word of every sentence and headline.</li>
</ul>""",
        "format_link": "In articles, clear sentence boundaries ensure your headline hooks the reader and your paragraphs flow smoothly without confusing run-ons.",
        "worked_bad": "last saturday i visited the new community garden it was amazing. Because lots of volunteers helped.",
        "worked_good": "Last Saturday, I visited the new community garden. It was amazing because lots of volunteers helped.",
        "worked_why": "Capitalised 'Last' and 'I', split the run-on with a full stop, and joined the fragment into a single cohesive sentence.",
        "exercise_a": [
            ("Choose the correct option to fix the fragment: <em>'Although the class starts at seven.'</em>",
             ["A) Although the class starts at seven?", "B) The class starts at seven, so please arrive early.", "C) Although starting at seven."],
             "B"),
            ("Which sentence correctly capitalises all proper nouns and the pronoun 'I'?",
             ["A) Every monday, i travel to london with mr davies.", "B) Every Monday, I travel to London with Mr Davies.", "C) Every monday, I travel to London with mr Davies."],
             "B"),
            ("Identify the run-on sentence that needs a full stop:",
             ["A) Regular exercise boosts your energy it also helps you sleep.", "B) Regular exercise boosts your energy and helps you sleep.", "C) If you exercise regularly, you sleep better."],
             "A"),
            ("Which headline uses correct capitalisation and punctuation?",
             ["A) Discover your hidden talent at our town workshop!", "B) discover your Hidden Talent at our town workshop", "C) Discover Your Hidden Talent at Our Town Workshop!"],
             "C")
        ],
        "proofreading_title": "Format 1 Applied Proofreading: Community Magazine Article",
        "proofreading_scenario": "A student drafted this article for the local town magazine. There are <strong>5 SPaG errors</strong> (fragments, missing capital letters, and run-ons).",
        "proofreading_text": """<h4 style="margin:0 0 4px 0; color:#0f766e;">why everyone should try gardening this spring</h4>
<p style="margin:0 0 6px 0;">gardening is one of the most rewarding outdoor hobbies you can start. last month, i joined the greenfields allotment project on station road. It was fantastic to see how much we accomplished together.</p>
<p style="margin:0 0 6px 0;">working outdoors gives you fresh air and gentle exercise it also improves your mood. when you grow your own vegetables. you save money on your weekly shopping bill.</p>""",
        "proofreading_errors": [
            "Missing capital letter in headline ('why' -> 'Why')",
            "Missing capital letter at start of paragraph 1 ('gardening' -> 'Gardening')",
            "Missing capital letter on 'last' and pronoun 'i' ('last month, i joined' -> 'Last month, I joined')",
            "Run-on sentence between 'exercise' and 'it' (needs full stop: 'exercise. It also')",
            "Sentence fragment ('when you grow your own vegetables. you save' -> 'When you grow your own vegetables, you save')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> for an article encouraging people to join a local sports club. Include at least one proper noun and ensure both sentences have correct capital letters and full stops."
    },
    {
        "unit": 2,
        "format": "Workplace Email",
        "title": "Subject-Verb Agreement & Polite Modals",
        "subtitle": "Professional Workplace Communication & Tone",
        "rule_title": "Core Grammar Rule: Singular vs. Plural Verbs & Polite Modals",
        "rule_text": """The verb must agree in number with its subject. A singular subject takes a singular verb; a plural subject takes a plural verb.<br><br>
<strong>Key Agreement Rules for Emails:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Singular vs. Plural:</strong> <em>The manager <strong>is</strong> pleased</em> (singular) vs. <em>The managers <strong>are</strong> pleased</em> (plural).</li>
  <li><strong>Was vs. Were:</strong> <em>He <strong>was</strong> present</em> (singular) vs. <em>They <strong>were</strong> present</em> (plural). Watch out for: <em>You <strong>were</strong></em> (always plural verb with 'you').</li>
  <li><strong>Polite Workplace Modals:</strong> In workplace emails, use polite modal auxiliary verbs (<em>could, would, may</em>) rather than harsh imperatives (e.g. <em>"Could you please send the report?"</em> instead of <em>"Send the report now."</em>).</li>
</ul>""",
        "format_link": "In workplace emails, incorrect subject-verb agreement (e.g. 'the team were happy' or 'he don't know') looks unprofessional and costs marks under Pearson SPaG criteria.",
        "worked_bad": "Dear Mr Harrison, The students is excited about the trip. We was hoping you could approve it.",
        "worked_good": "Dear Mr Harrison, The students are excited about the trip. We were hoping you could approve it.",
        "worked_why": "'Students' is plural so it requires 'are'. 'We' is plural so it requires 'were'.",
        "exercise_a": [
            ("Select the correct verb: <em>'The new shift rota [ is / are ] displayed on the staff noticeboard.'</em>",
             ["A) is", "B) are"],
             "A"),
            ("Select the correct verb: <em>'Both members of the IT team [ was / were ] available to assist.'</em>",
             ["A) was", "B) were"],
             "B"),
            ("Choose the most professional and polite modal phrasing for an email request:",
             ["A) You must give me Friday off.", "B) Would you mind confirming if I can take Friday as leave?", "C) I want Friday off."],
             "B"),
            ("Select the sentence with correct subject-verb agreement:",
             ["A) Every employee in our department have completed the training.", "B) Every employee in our department has completed the training.", "C) Every employee in our department were completing the training."],
             "B")
        ],
        "proofreading_title": "Format 2 Applied Proofreading: Workplace Email Request",
        "proofreading_scenario": "An apprentice sent this draft email to their supervisor. There are <strong>5 SPaG errors</strong> involving subject-verb agreement and pronoun/verb mismatches.",
        "proofreading_text": """<div style="background:#f8fafc; border:1px solid #cbd5e1; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>To:</strong> karen.patel@greengrove.co.uk | <strong>Subject:</strong> Request for Staff Training Rota
</div>
<p style="margin:0 0 4px 0;">Dear Karen,</p>
<p style="margin:0 0 6px 0;">I am writing because the team are worried about the new weekend shifts. Several workers has asked if they was scheduled for Saturday morning. The customer service supervisor do not have the updated sheet yet.</p>
<p style="margin:0 0 4px 0;">Could you please sends us the finalised rota today?</p>
<p style="margin:0;">Kind regards,<br>Jordan Lee</p>""",
        "proofreading_errors": [
            "'team are worried' -> 'team is worried' (singular collective noun in formal writing)",
            "'Several workers has asked' -> 'Several workers have asked' (plural subject)",
            "'if they was scheduled' -> 'if they were scheduled' (plural pronoun)",
            "'supervisor do not have' -> 'supervisor does not have' (singular subject)",
            "'Could you please sends us' -> 'Could you please send us' (modal verb takes bare infinitive)"
        ],
        "writing_prompt": "Write <strong>two polite sentences</strong> in an email to your line manager requesting permission to attend a workplace safety course. Use a polite modal verb (<em>could / would</em>) and correct subject-verb agreement."
    },
    {
        "unit": 3,
        "format": "Formal Letter",
        "title": "Punctuation in Formal Correspondence",
        "subtitle": "Commas in Addresses, Salutations & Formal Sign-offs",
        "rule_title": "Core Grammar Rule: Correspondence Punctuation & Register",
        "rule_text": """Formal letters follow strict punctuation conventions for addresses, dates, salutations, and valedictions (sign-offs).<br><br>
<strong>Punctuation Rules for Formal Letters:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Salutation Matching:</strong> If you know the recipient's name (<em>Dear Mrs Campbell,</em>), end with <em>Yours sincerely,</em>. If you do not know the name (<em>Dear Sir or Madam,</em>), end with <em>Yours faithfully,</em>. Both salutation and sign-off are followed by a <strong>comma</strong>.</li>
  <li><strong>Addresses &amp; Dates:</strong> Capitalise street names, towns, and postcodes (<em>High Street, Oakford, OK2 4BL</em>). Write the date fully (<em>18 October 2026</em>).</li>
  <li><strong>No Contractions in Formal Letters:</strong> Avoid informal contractions. Write <em>do not</em> (not <em>don't</em>), <em>cannot</em> (not <em>can't</em>), and <em>I am</em> (not <em>I'm</em>).</li>
</ul>""",
        "format_link": "Pearson examiners award top SPaG marks when candidates maintain a formal register without slipping into informal abbreviations or omitting correspondence commas.",
        "worked_bad": "dear Mrs Campbell I am writing coz the road is bad. I cant drive safely. yours Faithfully, Jordan",
        "worked_good": "Dear Mrs Campbell, I am writing to complain about the hazardous road conditions. I cannot drive safely. Yours sincerely, Jordan Reed",
        "worked_why": "Added commas to salutation and sign-off, expanded slang ('coz') and contractions ('cant' -> 'cannot'), and matched 'Dear Mrs Campbell' with 'Yours sincerely'.",
        "exercise_a": [
            ("Which sign-off correctly matches the salutation <em>'Dear Mr Jenkins,'</em>?",
             ["A) Yours faithfully,", "B) Yours sincerely,", "C) Best regards,"],
             "B"),
            ("Which sign-off correctly matches the salutation <em>'Dear Sir or Madam,'</em>?",
             ["A) Yours faithfully,", "B) Yours sincerely,", "C) Cheers,"],
             "A"),
            ("Identify the sentence written in an appropriate formal register:",
             ["A) I won't pay the bill coz your plumber didn't fix the tap.", "B) I am unwilling to settle the invoice as the repair was not completed.", "C) The tap's still leaking mate."],
             "B"),
            ("Select the correctly punctuated address line:",
             ["A) 14 the coppice oakford ok3 8dy", "B) 14 The Coppice, Oakford, OK3 8DY", "C) 14 The coppice, oakford, OK3 8DY"],
             "B")
        ],
        "proofreading_title": "Format 3 Applied Proofreading: Formal Council Complaint Letter",
        "proofreading_scenario": "A resident wrote this formal complaint letter to the local highways department. There are <strong>5 SPaG errors</strong> involving letter punctuation and informal register.",
        "proofreading_text": """<p style="margin:0 0 2px 0;">mrs fiona campbell<br>Highways department, town hall, okford</p>
<p style="margin:4px 0 2px 0;">Dear Mrs Campbell</p>
<p style="margin:0 0 6px 0;">I am writing to tell you about the massive potholes outside the health clinic. Drivers cant avoid them and its dangerous for elderly patients.</p>
<p style="margin:0 0 6px 0;">I want you to sort this out within two weeks.</p>
<p style="margin:0;">Yours faithfully<br>Jordan Reed</p>""",
        "proofreading_errors": [
            "Missing capital letters in recipient address ('mrs fiona campbell' -> 'Mrs Fiona Campbell')",
            "Missing comma after salutation ('Dear Mrs Campbell' -> 'Dear Mrs Campbell,')",
            "Informal contractions without apostrophes ('cant' -> 'cannot', 'its' -> 'it is')",
            "Overly abrupt/informal phrasing ('sort this out' -> 'resolve this issue')",
            "Incorrect sign-off matching and missing comma ('Yours faithfully' -> 'Yours sincerely,')"
        ],
        "writing_prompt": "Write the opening sentence and the closing sign-off of a formal letter of complaint to a customer relations manager (Mr Mark Davis) regarding a damaged parcel. Ensure 100% accurate correspondence punctuation."
    },
    {
        "unit": 4,
        "format": "Report",
        "title": "Capitalisation, Acronyms & Bullet List Punctuation",
        "subtitle": "Formatting Structured Reports & Executive Headings",
        "rule_title": "Core Grammar Rule: Punctuating Lists & Professional Acronyms",
        "rule_text": """In business and community reports, bullet points and numbered sections must be punctuated with consistent, grammatically complete sentences.<br><br>
<strong>Pearson Edexcel Requirement for Bullet Points:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Full Sentences:</strong> Every bullet point in your report must be a complete grammatical sentence. It must start with a capital letter and end with a full stop.</li>
  <li><strong>Avoid Fragment Bullets:</strong> Do not write single words or broken phrases like <em>'broken printer'</em>. Instead write: <em>'The shared printer is broken and causes frequent paper jams.'</em></li>
  <li><strong>Acronyms:</strong> Capitalise standard organisational acronyms fully without full stops (e.g. <em>IT, NHS, Wi-Fi, HR, CCTV, GCSE</em>).</li>
</ul>""",
        "format_link": "Pearson examiners specifically penalise fragmented bullet lists in reports. Writing each bullet as a full grammatical sentence is essential for Level 1 and Level 2 success.",
        "worked_bad": "2. Problems: - slow wi-fi - broken chairs - noisy air con",
        "worked_good": "2. Findings: The study room suffers from slow Wi-Fi connectivity. Furthermore, several chairs have broken legs and the air conditioning unit is noisy.",
        "worked_why": "Replaced fragments with complete sentences containing subjects, verbs, and ending punctuation.",
        "exercise_a": [
            ("Which bullet point complies with Pearson's full-sentence rule?",
             ["A) - Replacement of old keyboards.", "B) The IT department should replace all obsolete keyboards before term starts.", "C) - new keyboards needed urgently."],
             "B"),
            ("Identify the correct acronym format:",
             ["A) N.H.S.", "B) nhs", "C) NHS"],
             "C"),
            ("Choose the correctly punctuated bulleted list:",
             ["A) • Upgrade the computers. • Install high-speed Wi-Fi.", "B) • upgrade the computers • install high-speed Wi-Fi", "C) • Upgrading computers, • and installing Wi-Fi,"],
             "A"),
            ("Select the report heading with appropriate capitalisation:",
             ["A) 3. recommendations For future funding", "B) 3. Recommendations for Future Funding", "C) 3. recommendations for future funding"],
             "B")
        ],
        "proofreading_title": "Format 4 Applied Proofreading: Centre Facilities Report",
        "proofreading_scenario": "A volunteer compiled this report section for the community centre manager. There are <strong>5 SPaG errors</strong> involving bullet punctuation, acronyms, and headings.",
        "proofreading_text": """<h4 style="margin:0 0 4px 0; color:#0f766e;">2. findings and user feedback</h4>
<p style="margin:0 0 4px 0;">we surveyed thirty learners regarding the it suite. The main issues identified are:</p>
<ul style="margin:0 0 6px 16px; padding:0;">
  <li>slow internet speeds during peak morning hours</li>
  <li>the laser printer is frequently offline due to faulty cabling</li>
  <li>lack of quiet study desks</li>
</ul>
<p style="margin:0;">Staff from the hr department confirmed that funding is available.</p>""",
        "proofreading_errors": [
            "Missing capital letters in heading ('2. findings' -> '2. Findings')",
            "Missing capital letter at start of sentence ('we surveyed' -> 'We surveyed')",
            "Lowercase acronym ('it suite' -> 'IT suite')",
            "Bullet points 1 and 3 are fragments missing capitalisation/full stops (must be complete sentences)",
            "Lowercase acronym in final sentence ('hr department' -> 'HR department')"
        ],
        "writing_prompt": "Write <strong>two report recommendations</strong> for improving a college library. Format each recommendation as a complete grammatical bullet point ending with a full stop."
    },
    {
        "unit": 5,
        "format": "Incident Report",
        "title": "Past Tense Consistency & Time Sequencing Connectives",
        "subtitle": "Recording Chronological Events & Workplace Safety",
        "rule_title": "Core Grammar Rule: Maintaining Past Tense in Incident Reports",
        "rule_text": """An incident report documents events that have already occurred. Therefore, all descriptions of what happened, injuries sustained, and immediate actions taken must be written consistently in the <strong>past tense</strong>.<br><br>
<strong>Past Tense &amp; Sequencing Rules:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Avoid Tense Shifting:</strong> Do not switch between past and present (e.g. <em>'The worker slipped and falls'</em> &rarr; Fix: <em>'The worker slipped and fell'</em>).</li>
  <li><strong>Regular vs. Irregular Past Verbs:</strong> Regular verbs add <em>-ed</em> (<em>checked, alerted, reported</em>). Irregular verbs change form (<em>fall &rarr; fell, see &rarr; saw, break &rarr; broke, hurt &rarr; hurt</em>).</li>
  <li><strong>Time Sequencing Connectives:</strong> Use clear chronological connectives to establish the timeline: <em>initially, immediately, five minutes later, subsequently, following this</em>.</li>
</ul>""",
        "format_link": "Factual accuracy and professional credibility in incident reports depend on consistent past tense verbs and precise time sequence markers.",
        "worked_bad": "At 11:15 AM, Mrs Davies slip on the floor. I rush over and call the first aider who attends immediately.",
        "worked_good": "At 11:15 AM, Mrs Davies slipped on the floor. I rushed over and called the first aider, who attended immediately.",
        "worked_why": "All verbs ('slipped', 'rushed', 'called', 'attended') are consistently in the simple past tense.",
        "exercise_a": [
            ("Select the sentence with consistent past tense verbs:",
             ["A) The customer slipped on the oil and breaks her wrist.", "B) The customer slipped on the oil and broke her wrist.", "C) The customer slips on the oil and broke her wrist."],
             "B"),
            ("Choose the correct irregular past tense form of the verb <em>'see'</em>:",
             ["A) seed", "B) saw", "C) seen"],
             "B"),
            ("Select the best time connective to show rapid emergency response:",
             ["A) Eventually", "B) Immediately", "C) Sometimes"],
             "B"),
            ("Identify the sentence free from grammatical tense errors:",
             ["A) The duty manager inspects the hazard and called maintenance.", "B) The duty manager inspected the hazard and called maintenance.", "C) The duty manager was inspect the hazard."],
             "B")
        ],
        "proofreading_title": "Format 5 Applied Proofreading: Supermarket Accident Report",
        "proofreading_scenario": "A customer assistant submitted this draft incident report. There are <strong>5 SPaG errors</strong> involving irregular verbs, tense shifting, and missing punctuation.",
        "proofreading_text": """<div style="background:#f8fafc; border:1px solid #cbd5e1; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Incident Date:</strong> 17 October 2026 | <strong>Location:</strong> Aisle 4
</div>
<p style="margin:0 0 4px 0;"><strong>Incident Summary:</strong><br>
At 11:20 AM, Mrs Brenda Davies was walking down Aisle 4 when she slip on spilled vegetable oil. She fall heavily and cutted her right arm on a shelf edge.</p>
<p style="margin:0 0 4px 0;">I immediately alerted the first-aider and place yellow warning cones around the spill. The cleaning team arrives five minutes later to mop the floor.</p>""",
        "proofreading_errors": [
            "Tense shift to present ('she slip' -> 'she slipped')",
            "Incorrect present tense verb ('She fall' -> 'She fell')",
            "Incorrect irregular past tense ('cutted' -> 'cut')",
            "Tense shift in action taken ('and place yellow cones' -> 'and placed yellow cones')",
            "Tense shift in final sentence ('cleaning team arrives' -> 'cleaning team arrived')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> for an incident report describing an apprentice finding a frayed electrical cable in a workshop and reporting it to a tutor. Ensure all verbs are in the past tense."
    },
    {
        "unit": 6,
        "format": "Advice Leaflet",
        "title": "Imperative Verbs, Exclamation Control & Direct Address",
        "subtitle": "Writing Actionable, Welcoming Advisory Leaflets",
        "rule_title": "Core Grammar Rule: Instructional Verbs & Tone Control",
        "rule_text": """An advice leaflet guides the reader through practical instructions and reassuring recommendations.<br><br>
<strong>Grammar &amp; Punctuation Rules for Leaflets:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Imperative (Action) Verbs:</strong> Start instructional advice with clear command verbs: <em>Arrive on time, Check your contract, Ask questions politely, Keep your phone out of sight</em>.</li>
  <li><strong>Second-Person Direct Address:</strong> Use the pronoun <em>'you'</em> and <em>'your'</em> to engage the reader personally (e.g. <em>'Your supervisor wants you to succeed.'</em>).</li>
  <li><strong>Control Exclamation Marks:</strong> Do not overuse exclamation marks (e.g. <em>'Good luck!!! Do your best!!!'</em>). One well-placed exclamation mark in the title or conclusion is sufficient. In professional leaflets, full stops convey calm confidence.</li>
</ul>""",
        "format_link": "Advice leaflets require a fine balance: clear imperative verbs for clarity, warm second-person pronouns for rapport, and controlled punctuation to prevent an aggressive or amateur tone.",
        "worked_bad": "You should check your timetable! Arrive early! Don't be late! It is vital!",
        "worked_good": "Check your timetable the evening before. Arrive at least ten minutes early so you feel calm and prepared.",
        "worked_why": "Replaced repetitive exclamation marks with calm full stops, and expanded imperative instructions with reassuring explanations.",
        "exercise_a": [
            ("Which sentence starts with an imperative verb suitable for a leaflet?",
             ["A) You might want to consider checking your payslip.", "B) Check your payslip carefully each month.", "C) Checking your payslip is good."],
             "B"),
            ("Choose the leaflet sentence with appropriate punctuation:",
             ["A) Welcome to our team!! We hope you love working here!!!!", "B) Welcome to our team. We hope you enjoy working with us.", "C) Welcome to our team! We hope you love it!!!"],
             "B"),
            ("Select the imperative verb that best completes this sentence: <em>'[ ________ ] your supervisor immediately if you notice a hazard.'</em>",
             ["A) Alert", "B) Alerting", "C) Alerted"],
             "A"),
            ("Identify the sentence using second-person direct address effectively:",
             ["A) Employees should remember their badges.", "B) Remember to wear your identity badge at all times.", "C) One must wear an identity badge."],
             "B")
        ],
        "proofreading_title": "Format 6 Applied Proofreading: New Starter Advice Leaflet",
        "proofreading_scenario": "A trainee drafted this section for a workplace welcome leaflet. There are <strong>5 SPaG errors</strong> involving imperative verbs, excessive exclamation marks, and missing punctuation.",
        "proofreading_text": """<h4 style="margin:0 0 4px 0; color:#0f766e;">Tips for Your First Week!</h4>
<p style="margin:0 0 6px 0;">starting a new job can feel scary! But following these simple steps will help you settle in quickly!!!</p>
<ul style="margin:0 0 6px 16px; padding:0;">
  <li>always listens carefully when your manager gives instructions.</li>
  <li>writes down important notes in a pocket notepad</li>
  <li>Ask for help if you do not understand a task!</li>
</ul>""",
        "proofreading_errors": [
            "Missing capital letter at start of paragraph ('starting a new job' -> 'Starting a new job')",
            "Excessive exclamation marks ('scary! ... quickly!!!' -> replace with full stops)",
            "Incorrect verb form for imperative bullet ('always listens' -> 'Always listen')",
            "Incorrect verb form and missing full stop in bullet 2 ('writes down ... notepad' -> 'Write down important notes in a pocket notepad.')",
            "Exclamation mark in bullet 3 should be a professional full stop"
        ],
        "writing_prompt": "Write <strong>two advice bullet points</strong> for an energy-saving leaflet advising households on how to reduce their winter heating bills. Begin each bullet with an imperative verb and end with a full stop."
    },
    {
        "unit": 7,
        "format": "Review",
        "title": "Comparative & Superlative Adjectives",
        "subtitle": "Evaluative Language & Commas in Descriptive Lists",
        "rule_title": "Core Grammar Rule: Comparing Products & Services Accurately",
        "rule_text": """A review evaluates a product, service, or venue. To explain why something is good or bad, you must use comparative and superlative adjectives accurately.<br><br>
<strong>Comparison &amp; Comma Rules:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Short Adjectives:</strong> Add <em>-er</em> for comparatives and <em>-est</em> for superlatives (<em>clean &rarr; cleaner &rarr; cleanest; fast &rarr; faster &rarr; fastest</em>).</li>
  <li><strong>Long Adjectives (2+ syllables):</strong> Use <em>more</em> or <em>most</em> (<em>reliable &rarr; more reliable &rarr; most reliable; comfortable &rarr; more comfortable &rarr; most comfortable</em>). Never say <em>'more cleaner'</em> or <em>'most fastest'</em>.</li>
  <li><strong>Irregular Adjectives:</strong> <em>good &rarr; better &rarr; best; bad &rarr; worse &rarr; worst</em> (not <em>'more good'</em> or <em>'baddest'</em>).</li>
  <li><strong>Commas in Lists of Adjectives:</strong> Separate coordinate adjectives with commas: <em>'The bus was clean, spacious, and punctual.'</em></li>
</ul>""",
        "format_link": "Examiners look for sophisticated evaluative vocabulary in reviews. Correct comparative forms demonstrate your ability to judge value and express balanced opinions.",
        "worked_bad": "The Route 42 bus is more cheap than the train, but the seats are more bad than before.",
        "worked_good": "The Route 42 bus is cheaper than the train, but the seating is worse than it was previously.",
        "worked_why": "'Cheap' is a single syllable, so it takes '-er' ('cheaper'). 'Bad' is irregular, so its comparative form is 'worse'.",
        "exercise_a": [
            ("Choose the correct comparative form: <em>'The new cinema is [ more comfortable / comfortabler ] than the old town theatre.'</em>",
             ["A) comfortabler", "B) more comfortable"],
             "B"),
            ("Choose the correct irregular comparative: <em>'The weekend traffic was [ more worse / worse ] than Monday morning.'</em>",
             ["A) more worse", "B) worse", "C) worser"],
             "B"),
            ("Select the sentence with correct list comma punctuation:",
             ["A) The driver was polite patient and helpful.", "B) The driver was polite, patient, and helpful.", "C) The driver was polite, patient and, helpful."],
             "B"),
            ("Identify the sentence free from double-comparative errors:",
             ["A) This is the most cleanest train on the network.", "B) This is the cleanest train on the network.", "C) This is the more cleaner train."],
             "B")
        ],
        "proofreading_title": "Format 7 Applied Proofreading: Bus Service Review",
        "proofreading_scenario": "A passenger posted this review of the Route 42 bus service online. There are <strong>5 SPaG errors</strong> involving comparatives, commas, and apostrophes.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#0f766e;">Route 42: An Affordable Commute</h4>
<p style="margin:0 0 4px 0; color:#d97706; font-size:8pt;">★★★☆☆ (3 out of 5 stars)</p>
<p style="margin:0 0 6px 0;">I have used Route 42 for six months. The buses are more cleaner than the town trains, and the ticket prices are cheap than driving.</p>
<p style="margin:0;">However morning crowding is getting more worse every week. The drivers are friendly polite and patient, but the companys timetable needs updating.</p>""",
        "proofreading_errors": [
            "Double comparative ('more cleaner' -> 'cleaner')",
            "Incorrect comparative ('cheap than' -> 'cheaper than')",
            "Double comparative ('more worse' -> 'worse')",
            "Missing list commas ('friendly polite and patient' -> 'friendly, polite, and patient')",
            "Missing apostrophe in singular possessive ('companys timetable' -> 'company\\'s timetable')"
        ],
        "writing_prompt": "Write <strong>two review sentences</strong> comparing two local cafes or supermarkets. Use at least one comparative adjective (e.g. <em>quieter, more affordable, freshest</em>) and correct comma punctuation."
    },
    {
        "unit": 8,
        "format": "Online Feedback Form",
        "title": "Apostrophes of Contraction vs. Possession",
        "subtitle": "Customer Complaints & Factual Redress Requests",
        "rule_title": "Core Grammar Rule: Mastering the Two Uses of Apostrophes",
        "rule_text": """Apostrophes have only two jobs in English: to show missing letters (<strong>omission / contraction</strong>) or to show ownership (<strong>possession</strong>).<br><br>
<strong>Key Apostrophe Rules:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Contractions (Missing Letters):</strong> Put the apostrophe exactly where letters are removed: <em>do not &rarr; don't; cannot &rarr; can't; did not &rarr; didn't; was not &rarr; wasn't</em>.</li>
  <li><strong>Singular Possession (Ownership):</strong> Add <em>'s</em> to the owner: <em>the customer's bag; the driver's cab; the train's heating</em>.</li>
  <li><strong>The Big Exam Trap: It's vs. Its:</strong>
    <ul style="margin:0 0 0 14px;">
      <li><em>It's</em> = short for <em>it is</em> or <em>it has</em> (e.g. <em>It's delayed</em>).</li>
      <li><em>Its</em> = belonging to it (possessive pronoun, NO apostrophe, e.g. <em>The train lost its power</em>).</li>
    </ul>
  </li>
</ul>""",
        "format_link": "Customer service portals demand factual precision. Confusing 'its' and 'it's' or omitting apostrophes in complaints makes your writing look careless to examiners.",
        "worked_bad": "The trains air con broke down. Its unacceptable and the customers bags got wet.",
        "worked_good": "The train's air conditioning broke down. It's unacceptable, and the customer's bags got wet.",
        "worked_why": "Added possessive apostrophe to 'train's', contraction apostrophe to 'It's' (it is), and possessive apostrophe to 'customer's'.",
        "exercise_a": [
            ("Choose the correct word: <em>'The airline cancelled [ its / it's ] evening flight without notice.'</em>",
             ["A) its", "B) it's"],
             "A"),
            ("Choose the correct word: <em>'[ Its / It's ] been three weeks since I requested a refund.'</em>",
             ["A) Its", "B) It's"],
             "B"),
            ("Select the sentence with correct possessive apostrophes:",
             ["A) The passengers luggage was placed in the guards van.", "B) The passenger's luggage was placed in the guard's van.", "C) The passengers's luggage was placed in the guards' van."],
             "B"),
            ("Identify the correctly punctuated contraction:",
             ["A) could'nt", "B) couldn't", "C) coul'dnt"],
             "B")
        ],
        "proofreading_title": "Format 8 Applied Proofreading: Rail Delay Compensation Form",
        "proofreading_scenario": "A passenger completed this online feedback submission for SwiftRail. There are <strong>5 SPaG errors</strong> involving apostrophes and possessive nouns.",
        "proofreading_text": """<div style="background:#f8fafc; border:1px solid #cbd5e1; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Portal:</strong> SwiftRail Claims | <strong>Booking Ref:</strong> TR-72819
</div>
<p style="margin:0 0 4px 0;"><strong>Statement of Complaint:</strong><br>
I am writing because my trains engine failed outside Rugby. Its unacceptable that passengers were kept onboard in thirty-degree heat without water.</p>
<p style="margin:0;">The guards announcement was unclear, and my managers meeting was missed as a result. I demand a full refund for my tickets cost.</p>""",
        "proofreading_errors": [
            "Missing possessive apostrophe ('my trains engine' -> 'my train\\'s engine')",
            "Missing contraction apostrophe ('Its unacceptable' -> 'It\\'s unacceptable')",
            "Missing possessive apostrophe ('The guards announcement' -> 'The guard\\'s announcement')",
            "Missing possessive apostrophe ('my managers meeting' -> 'my manager\\'s meeting')",
            "Missing possessive apostrophe ('tickets cost' -> 'ticket\\'s cost')"
        ],
        "writing_prompt": "Write <strong>two sentences</strong> for an online customer complaint form regarding a parcel delivery. Include one contraction (e.g. <em>didn't</em>) and one possessive noun (e.g. <em>driver's</em>), punctuating both with 100% accuracy."
    },
    {
        "unit": 9,
        "format": "Online Forum / Blog Post",
        "title": "Discourse Markers & Connecting Words",
        "subtitle": "Structuring Opinions, Counterpoints & Discussion Threads",
        "rule_title": "Core Grammar Rule: Linking Ideas with Conjunctions & Connectives",
        "rule_text": """In online forums and blog posts, you share personal opinions, compare different perspectives, and invite others to comment. Discourse markers guide the reader through your line of reasoning.<br><br>
<strong>Connective Types &amp; Punctuation:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Adding Information:</strong> <em>In addition, furthermore, also, moreover</em> (e.g. <em>'Furthermore, batch cooking saves money.'</em>).</li>
  <li><strong>Contrasting Ideas:</strong> <em>However, on the other hand, although, whereas, but</em> (e.g. <em>'Ready meals are quick. However, they are expensive.'</em>).</li>
  <li><strong>Showing Cause &amp; Effect:</strong> <em>Because, therefore, consequently, as a result, so</em> (e.g. <em>'As a result, our grocery bill decreased.'</em>).</li>
  <li><strong>Comma Rule for Connectives:</strong> When a connective starts a sentence, it must be followed by a <strong>comma</strong> (e.g. <em>'However, ...'</em> or <em>'In addition, ...'</em>).</li>
</ul>""",
        "format_link": "Using varied connectives prevents short, childish sentences and allows you to present a balanced argument in discussion boards.",
        "worked_bad": "Ready meals are fast. They are salty. I cook fresh food. It takes longer. It is cheaper.",
        "worked_good": "Ready meals are fast, but they often contain high levels of salt. On the other hand, cooking fresh food takes longer, although it is significantly cheaper.",
        "worked_why": "Joined choppy simple sentences into cohesive compound-complex structures using 'but', 'on the other hand', and 'although'.",
        "exercise_a": [
            ("Choose the best connective to show contrast: <em>'Home cooking is healthy. [ ________ ], it requires time and planning.'</em>",
             ["A) Furthermore", "B) However", "C) Because"],
             "B"),
            ("Choose the best connective to show cause: <em>'She learned how to bake [ ________ ] she wanted to save money on bread.'</em>",
             ["A) although", "B) because", "C) whereas"],
             "B"),
            ("Select the correctly punctuated sentence:",
             ["A) However I prefer cooking from scratch.", "B) However, I prefer cooking from scratch.", "C) However; I prefer cooking from scratch."],
             "B"),
            ("Which sentence successfully links two contrasting viewpoints?",
             ["A) Dogs need exercise although some park visitors dislike them.", "B) Dogs need exercise because park visitors dislike them.", "C) Dogs need exercise so park visitors dislike them."],
             "A")
        ],
        "proofreading_title": "Format 9 Applied Proofreading: Community Forum Discussion",
        "proofreading_scenario": "A forum user posted this reply in a discussion thread about cooking on a budget. There are <strong>5 SPaG errors</strong> involving connectives, commas, and spelling.",
        "proofreading_text": """<div style="background:#f1f5f9; border-left:3px solid #0f766e; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Forum Thread:</strong> Budget Living &gt; <em>Cooking vs. Ready Meals</em>
</div>
<p style="margin:0 0 4px 0;">Hi everyone,</p>
<p style="margin:0 0 6px 0;">I used to buy convenience meals every night. Because I was too tierd to cook after work. However my food bill was massive.</p>
<p style="margin:0;">Last month, I started batch cooking lentil curry. Furthermore it tastes much better than shop meals, and it saves me money. What are you're favourite budget recipes?</p>""",
        "proofreading_errors": [
            "Sentence fragment starting with 'Because' (should link to previous sentence)",
            "Misspelled high-frequency word ('tierd' -> 'tired')",
            "Missing comma after fronted connective ('However my food bill' -> 'However, my food bill')",
            "Missing comma after fronted connective ('Furthermore it tastes' -> 'Furthermore, it tastes')",
            "Confused homophone ('What are you\\'re favourite' -> 'What are your favourite')"
        ],
        "writing_prompt": "Write <strong>two forum post sentences</strong> arguing whether public parks should have designated dog-free zones. Use at least two contrasting connectives (e.g. <em>however, on the other hand, although</em>) punctuated correctly with commas."
    },
    {
        "unit": 10,
        "format": "Newsletter",
        "title": "Relative Clauses & Commas for Extra Information",
        "subtitle": "Community Announcements & Volunteer Features",
        "rule_title": "Core Grammar Rule: Expanding Sentences with Relative Clauses",
        "rule_text": """Newsletters bring together community highlights, volunteer spotlights, and future event dates. Relative clauses allow you to add rich extra details without starting repetitive new sentences.<br><br>
<strong>Relative Pronouns &amp; Punctuation:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Relative Pronouns:</strong> Use <strong>who</strong> for people, <strong>which</strong> for things/events, <strong>that</strong> for items/rules, and <strong>where</strong> for places.</li>
  <li><strong>Commas for Extra Information (Non-Defining):</strong> When the clause adds non-essential background information, enclose it between <strong>two commas</strong>:
    <div style="background:#f8fafc; padding:3px 6px; margin:2px 0; border-left:2px solid #0f766e;">
      <em>'Mrs Green, who has volunteered for ten years, baked the harvest cakes.'</em><br>
      (If you remove 'who has volunteered for ten years', the sentence still makes complete sense).
    </div>
  </li>
  <li><strong>No Commas for Essential Information (Defining):</strong> <em>'Volunteers who arrive before 08:00 will receive free parking.'</em> (No commas because 'who arrive before 08:00' defines which volunteers).</li>
</ul>""",
        "format_link": "Newsletters require lively, informative reporting. Using relative clauses allows you to credit volunteers and detail achievements concisely.",
        "worked_bad": "Sarah Jenkins won the race. She is seventeen years old. She trains at our sports club.",
        "worked_good": "Sarah Jenkins, who is seventeen years old, won the race and trains regularly at our sports club.",
        "worked_why": "Combined three repetitive short sentences into a single flowing sentence using a relative clause with commas.",
        "exercise_a": [
            ("Choose the correct relative pronoun: <em>'We thanked the local baker [ who / which ] donated fifty bread rolls.'</em>",
             ["A) who", "B) which", "C) where"],
             "A"),
            ("Choose the correct relative pronoun: <em>'The annual 5k race, [ who / which ] raised £1,200, was a huge success.'</em>",
             ["A) who", "B) which", "C) that"],
             "B"),
            ("Select the sentence with correct parenthetical commas around extra information:",
             ["A) Our team mascot, Barnaby Bear, entertained the children at the finish line.", "B) Our team mascot Barnaby Bear entertained, the children at the finish line.", "C) Our team mascot, Barnaby Bear entertained the children."],
             "A"),
            ("Identify the sentence with correct relative pronoun and punctuation:",
             ["A) The sports hall where we train has new lighting.", "B) The sports hall which we train has new lighting.", "C) The sports hall who we train has new lighting."],
             "A")
        ],
        "proofreading_title": "Format 10 Applied Proofreading: Sports Club Newsletter",
        "proofreading_scenario": "The club secretary drafted this announcement for the monthly newsletter. There are <strong>5 SPaG errors</strong> involving relative pronouns, commas, and capitalisation.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#0f766e;">riverside sports club news • october edition</h4>
<p style="margin:0 0 4px 0;">Our annual charity fun run which took place last Saturday, was our most successful event ever.</p>
<p style="margin:0 0 4px 0;">We want to thank Dave Miller which marshalled the water station for five hours. Dave, who joined the club in 2020 always supports our fundraising days.</p>
<p style="margin:0;">New badminton classes will start on monday 2 November.</p>""",
        "proofreading_errors": [
            "Missing capital letters in masthead banner ('riverside sports club news' -> 'Riverside Sports Club News')",
            "Missing opening comma in non-defining relative clause ('fun run, which took place last Saturday, was')",
            "Incorrect relative pronoun for a person ('Dave Miller which marshalled' -> 'Dave Miller who marshalled')",
            "Missing closing comma in relative clause ('Dave, who joined the club in 2020, always supports')",
            "Missing capital letter for day of the week ('monday' -> 'Monday')"
        ],
        "writing_prompt": "Write <strong>two newsletter sentences</strong> announcing a community fundraising event. In one of the sentences, include a relative clause starting with <em>who</em> or <em>which</em>, punctuated with correct commas."
    },
    {
        "unit": 11,
        "format": "Diary / Learning Log",
        "title": "First-Person Pronouns & Reflective Verb Consistency",
        "subtitle": "Personal Learning Logs & Vocational Self-Evaluation",
        "rule_title": "Core Grammar Rule: First-Person Accuracy & Reflective Past Tense",
        "rule_text": """A diary entry or vocational learning log records your personal reflections on what happened, how you felt, and what targets you will set.<br><br>
<strong>Grammar Rules for Learning Logs:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>First-Person Pronouns:</strong> Use subject pronoun <strong>'I'</strong> when you perform the action, and object pronoun <strong>'me'</strong> when the action happens to you (e.g. <em>'My supervisor helped <strong>me</strong>'</em> vs. <em>'<strong>I</strong> resolved the issue'</em>). Never use 'myself' as a subject (e.g. <em>'Myself and Chloe served customers'</em> &rarr; Fix: <em>'Chloe and I served customers'</em>).</li>
  <li><strong>Past Continuous vs. Simple Past:</strong> Use past continuous to set the background scene and past simple for the main event: <em>'I was restocking the shelves when a customer approached me.'</em></li>
  <li><strong>Reflective Sentence Openers:</strong> Start evaluative sentences with reflective phrases followed by commas: <em>'Looking back, ...'</em>, <em>'On reflection, ...'</em>, <em>'In future, ...'</em>.</li>
</ul>""",
        "format_link": "Vocational learning logs require self-awareness. Accurate first-person pronouns and reflective past tenses ensure your portfolio meets professional standards.",
        "worked_bad": "Me and the supervisor was dealing with an upset customer. Myself explained the refund policy.",
        "worked_good": "My supervisor and I were dealing with an upset customer. I calmly explained the store refund policy.",
        "worked_why": "Changed 'Me and the supervisor' to 'My supervisor and I', corrected verb to plural 'were', and replaced incorrect 'Myself' with subject pronoun 'I'.",
        "exercise_a": [
            ("Choose the correct pronoun: <em>'The tutor gave valuable feedback to Chloe and [ I / me ].'</em>",
             ["A) I", "B) me"],
             "B"),
            ("Choose the correct subject phrasing: <em>'[ Myself and Liam / Liam and I ] chaired the project meeting.'</em>",
             ["A) Myself and Liam", "B) Liam and I"],
             "B"),
            ("Select the sentence with correct past continuous and simple past verbs:",
             ["A) I was processing a refund when the computer crashed.", "B) I am processing a refund when the computer crash.", "C) I processed a refund when the computer was crash."],
             "A"),
            ("Identify the correctly punctuated reflective sentence:",
             ["A) On reflection I should have asked for assistance sooner.", "B) On reflection, I should have asked for assistance sooner.", "C) On reflection; I should have asked for assistance sooner."],
             "B")
        ],
        "proofreading_title": "Format 11 Applied Proofreading: Vocational Learning Log",
        "proofreading_scenario": "A student completed this reflective diary entry for their retail coursework workbook. There are <strong>5 SPaG errors</strong> involving pronouns, verb agreement, and reflective openers.",
        "proofreading_text": """<div style="border-bottom:1px solid #cbd5e1; padding-bottom:2px; margin-bottom:4px; font-size:7.5pt; font-weight:bold; color:#0f766e;">
Vocational Learning Log | Saturday, 24 October 2026
</div>
<p style="margin:0 0 4px 0;">Today was my first busy shift on the customer desk. Me and Megan was handling returns all morning.</p>
<p style="margin:0 0 4px 0;">At midday, an upset customer complained about a broken radio. Myself listened patiently and offered a replacement voucher.</p>
<p style="margin:0;">Looking back I handled the pressure well. In future I will study the warranty guide more closely.</p>""",
        "proofreading_errors": [
            "Incorrect subject pronoun and verb agreement ('Me and Megan was' -> 'Megan and I were')",
            "Incorrect reflexive pronoun as subject ('Myself listened' -> 'I listened')",
            "Missing comma after reflective opener ('Looking back I handled' -> 'Looking back, I handled')",
            "Missing comma after reflective opener ('In future I will' -> 'In future, I will')",
            "Missing hyphen in compound modifier ('first busy shift on the customer desk' -> 'customer service desk')"
        ],
        "writing_prompt": "Write <strong>two reflective sentences</strong> for a vocational learning log describing a practical task you completed and one skill you want to improve next time. Use 'I' correctly and include a reflective opener followed by a comma."
    }
]

