# spag_content_l2.py
# Comprehensive Level 2 SPaG units mapped to the 11 Pearson Edexcel Writing Formats.

L2_UNITS = [
    {
        "unit": 1,
        "format": "Article",
        "title": "Complex Sentences, Subordination & Eliminating Comma Splices",
        "subtitle": "Crafting Sophisticated Article Openers & Compelling Arguments",
        "rule_title": "Core Grammar Rule: The Comma Splice & Complex Sentence Architecture",
        "rule_text": """At Level 2, Pearson examiners strictly penalise <strong>comma splices</strong>. A comma splice occurs when two independent clauses (complete thoughts that could stand alone as separate sentences) are joined with only a comma (e.g. <em>'Artificial intelligence is advancing rapidly, it will transform the labour market.'</em>).<br><br>
<strong>Three Ways to Fix a Comma Splice:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>1. Use a Semicolon (;):</strong> Connects two closely related independent clauses without a conjunction: <em>'Artificial intelligence is advancing rapidly; it will transform the labour market.'</em></li>
  <li><strong>2. Use a Coordinating Conjunction (FANBOYS):</strong> Add a comma and <em>for, and, nor, but, or, yet, so</em>: <em>'Artificial intelligence is advancing rapidly, and it will transform the labour market.'</em></li>
  <li><strong>3. Subordination (Complex Sentence):</strong> Convert one clause into a dependent subordinate clause: <em>'Because artificial intelligence is advancing rapidly, it will fundamentally transform the labour market.'</em></li>
</ul>""",
        "format_link": "In journalistic articles, using sophisticated complex sentences with subordinate clauses creates persuasive momentum and establishes top-band composition.",
        "worked_bad": "AI tools can automate repetitive administrative duties, workers will need to learn new digital skills.",
        "worked_good": "While artificial intelligence tools can automate repetitive administrative duties, human workers will inevitably need to acquire advanced digital and analytical competencies.",
        "worked_why": "Subordinated the first clause with 'While', creating a complex sentence with nuanced balance rather than an ungrammatical comma splice.",
        "exercise_a": [
            ("Identify the sentence containing an ungrammatical comma splice:",
             ["A) Automation improves efficiency; however, it also requires significant workforce training.",
              "B) Automation improves efficiency, it also requires significant workforce training.",
              "C) Although automation improves efficiency, it requires significant workforce training."],
             "B"),
            ("Choose the correct punctuation to join these two independent clauses: <em>'The high street faces unprecedented challenges [ ___ ] independent retailers must adapt swiftly.'</em>",
             ["A) ,", "B) ;", "C) :"],
             "B"),
            ("Which sentence demonstrates correct subordination without a comma splice?",
             ["A) Retailers are investing in digital storefronts, therefore footfall is recovering.",
              "B) Because retailers are investing in digital storefronts, footfall has shown encouraging recovery.",
              "C) Retailers are investing in digital storefronts, footfall has recovered."],
             "B"),
            ("Select the sentence with correct comma placement after an introductory subordinate clause:",
             ["A) As technological disruption accelerates, lifelong learning becomes an imperative.",
              "B) As technological disruption accelerates lifelong learning, becomes an imperative.",
              "C) As technological disruption accelerates lifelong learning becomes an imperative."],
             "A")
        ],
        "proofreading_title": "Format 1 Applied Proofreading: Careers Magazine Feature Article",
        "proofreading_scenario": "A student submitted this draft article for Modern Careers Magazine. There are <strong>5 SPaG errors</strong> involving comma splices, run-ons, and missing subordinate commas.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#1e3a8a;">The Evolution of Work: Embracing the Digital Shift</h4>
<p style="margin:0 0 4px 0; font-size:7.5pt; color:#64748b; font-style:italic;">By Alex Vance</p>
<p style="margin:0 0 6px 0;">Algorithmic machine learning is transforming commerce, many traditional roles are being reshaped overnight. Although routine data entry can now be automated emotional intelligence remains uniquely human.</p>
<p style="margin:0;">Workers must cultivate analytical problem-solving skills, these capabilities cannot be replicated by software. Furthermore educational institutions and commercial employers must collaborate, they need to design flexible apprenticeship pathways.</p>""",
        "proofreading_errors": [
            "Comma splice in paragraph 1 ('transforming commerce, many' -> use semicolon or conjunction)",
            "Missing comma after introductory subordinate clause ('Although routine data entry can now be automated, emotional')",
            "Comma splice in paragraph 2 ('problem-solving skills, these capabilities' -> use semicolon or full stop)",
            "Missing comma after fronted adverbial ('Furthermore educational' -> 'Furthermore, educational')",
            "Comma splice in final sentence ('must collaborate, they need' -> 'must collaborate because they need')"
        ],
        "writing_prompt": "Write <strong>two complex sentences</strong> for an article discussing the future of high-street retail versus online shopping. Use at least one subordinating conjunction (e.g. <em>whereas, although, while</em>) and one semicolon between closely related independent clauses."
    },
    {
        "unit": 2,
        "format": "Workplace Email",
        "title": "Professional Tense Consistency & Subordinate Clauses",
        "subtitle": "Navigating Past Background, Present Requests & Future Action",
        "rule_title": "Core Grammar Rule: Controlled Tense Transitions in Executive Correspondence",
        "rule_text": """Workplace emails frequently synthesize information across different timeframes: explaining a past problem, outlining a present proposal, and requesting a future response. Maintaining strict grammatical control across these tense shifts is essential for Level 2.<br><br>
<strong>Tense Hierarchy in Professional Emails:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Present Perfect for Recent Context:</strong> Use <em>has/have + past participle</em> for past actions with current relevance: <em>'The wellbeing committee <strong>has conducted</strong> a comprehensive audit.'</em></li>
  <li><strong>Present Simple / Continuous for Current Reality:</strong> <em>'We <strong>are currently evaluating</strong> infrastructural options.'</em></li>
  <li><strong>Modal Auxiliary Verbs for Proposals &amp; Requests:</strong> Use <em>would, could, should</em> for professional diplomacy: <em>'We <strong>would welcome</strong> the opportunity to discuss this initiative.'</em></li>
  <li><strong>Avoid Colloquial Slang &amp; Contractions:</strong> Use <em>do not</em> (not <em>don't</em>), <em>cannot</em> (not <em>can't</em>), and <em>we would be grateful</em> (not <em>we'd love</em>).</li>
</ul>""",
        "format_link": "In formal workplace proposals and funding requests, haphazard tense shifting confuses senior management and undermines your professional authority.",
        "worked_bad": "Last month our committee reviewed the bike shed and we find that staff wants showers. We would be grateful if you approve this.",
        "worked_good": "Last month, our committee reviewed the current cycling facilities and found that employees urgently require secure lockers. We would be grateful if you would consider approving this proposal.",
        "worked_why": "Aligned past tense actions ('reviewed', 'found') and used precise conditional modal phrasing ('would consider approving') for senior management.",
        "exercise_a": [
            ("Select the sentence maintaining correct tense consistency:",
             ["A) Over the past six months, employee demand for sustainable transport has increased significantly.",
              "B) Over the past six months, employee demand for sustainable transport was increase significantly.",
              "C) Over the past six months, employee demand for sustainable transport is increasing significant."],
             "A"),
            ("Choose the most professional phrasing for an executive email request:",
             ["A) We want you to review the attached figures right now.",
              "B) We would be grateful if you could review the attached financial projections at your earliest convenience.",
              "C) You should look at these figures ASAP."],
             "B"),
            ("Identify the correct conditional construction:",
             ["A) If the board approves the capital grant, we will initiate facility renovations in November.",
              "B) If the board will approve the capital grant, we initiated facility renovations in November.",
              "C) If the board approved the capital grant, we will initiate renovations."],
             "A"),
            ("Select the sentence free from informal contractions and colloquialisms:",
             ["A) Staff can't use the showers coz the boiler isn't working.",
              "B) Employees are unable to access the shower facilities due to a boiler defect.",
              "C) Personnel shouldn't worry about the showers' defect."],
             "B")
        ],
        "proofreading_title": "Format 2 Applied Proofreading: Executive Workplace Email",
        "proofreading_scenario": "A staff representative drafted this proposal email to the Operations Director. There are <strong>5 SPaG errors</strong> involving tense inconsistency, contractions, and agreement.",
        "proofreading_text": """<div style="background:#f1f5f9; padding:4px 8px; font-size:7.5pt; border:1px solid #cbd5e1; margin-bottom:4px;">
<strong>To:</strong> m.vance@apexlogistics.co.uk | <strong>Subject:</strong> Proposal: Cycle-to-Work Scheme
</div>
<p style="margin:0 0 4px 0;">Dear Mr Vance,</p>
<p style="margin:0 0 6px 0;">I am writing to formally propose that Apex Logistics introduces a cycle-to-work salary sacrifice scheme. Last quarter our committee has surveyed ninety employees and discover that over 40% would commute by bicycle if secure facilities were provided.</p>
<p style="margin:0 0 6px 0;">However staff can't store high-value bicycles safely because the current storage shed lack adequate locking racks.</p>
<p style="margin:0;">We would appreciate the opportunity to presented our detailed budget at next Tuesday's meeting.<br><br>Kind regards,<br>Rachel Hall</p>""",
        "proofreading_errors": [
            "Tense clash ('Last quarter our committee has surveyed' -> 'Last quarter, our committee surveyed')",
            "Tense clash in past coordination ('and discover' -> 'and discovered')",
            "Informal contraction in formal proposal ('can\\'t store' -> 'cannot store')",
            "Subject-verb agreement error ('shed lack' -> 'shed lacks')",
            "Incorrect verb form after modal infinitive ('to presented' -> 'to present')"
        ],
        "writing_prompt": "Write <strong>two professional email sentences</strong> to a senior manager requesting funding for a staff professional development course. Balance past background context with a polite conditional request using formal vocabulary."
    },
    {
        "unit": 3,
        "format": "Formal Letter",
        "title": "Colons, Semicolons & Advanced Formal Register",
        "subtitle": "Petitions, Official Planning Objections & Declarations",
        "rule_title": "Core Grammar Rule: Semicolons & Colons in High-Stakes Correspondence",
        "rule_text": """At Level 2, formal letters of objection, complaint, and petition require command of advanced punctuation to structure complex legal, environmental, or civic arguments.<br><br>
<strong>Advanced Punctuation for Formal Letters:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Colons (:) for Formal Reference Lines &amp; Specifications:</strong> Use a colon after formal subject identifiers (e.g. <em>'Re: Planning Application Ref: PL/2026/0894'</em>) and to introduce a decisive summary or enumeration.</li>
  <li><strong>Semicolons (;) to Balance Antithetical Arguments:</strong> Use a semicolon to contrast opposing points without a conjunction: <em>'The developer promises economic regeneration; however, independent assessments forecast catastrophic ecological damage.'</em></li>
  <li><strong>Conjunctive Adverbs with Semicolons &amp; Commas:</strong> When using words like <em>however, therefore, furthermore, consequently</em> between two independent clauses, place a <strong>semicolon before</strong> and a <strong>comma after</strong> (e.g. <em>'...greenbelt; consequently, the application must be refused.'</em>).</li>
</ul>""",
        "format_link": "Official planning objections and legal correspondence demand rigorous syntactic precision. Semicolons and colons enable you to present balanced, highly persuasive civic arguments.",
        "worked_bad": "The road cannot take HGVs, they cause noise pollution, the council should reject it.",
        "worked_good": "The existing rural road network cannot sustain continuous freight traffic; the inevitable increase in heavy goods vehicles will generate intolerable nocturnal noise pollution.",
        "worked_why": "Replaced run-on comma splices with an authoritative semicolon linking the infrastructural deficiency directly to its acoustic impact.",
        "exercise_a": [
            ("Select the correctly punctuated sentence using a semicolon and conjunctive adverb:",
             ["A) The proposed development breaches greenbelt policy; therefore, the council must reject it.",
              "B) The proposed development breaches greenbelt policy, therefore, the council must reject it.",
              "C) The proposed development breaches greenbelt policy; therefore the council must reject it."],
             "A"),
            ("Choose the correct use of a colon in formal correspondence:",
             ["A) We object to: the noise and traffic.",
              "B) Re: Formal Objection to Planning Application Ref: PL/2026/0894",
              "C) Re: Formal Objection to: Planning Application Ref: PL/2026/0894"],
             "B"),
            ("Identify the sentence free from informal register and contractions:",
             ["A) Residents don't want 24-hour lorries rumbling past our houses.",
              "B) Local residents strongly object to round-the-clock freight operations traversing residential roads.",
              "C) We can't tolerate continuous HGV noise."],
             "B"),
            ("Select the sentence with accurate parenthetical comma punctuation:",
             ["A) The ancient woodland, which harbours protected bat species would be irreparably destroyed.",
              "B) The ancient woodland, which harbours protected bat species, would be irreparably destroyed.",
              "C) The ancient woodland which harbours protected bat species, would be irreparably destroyed."],
             "B")
        ],
        "proofreading_title": "Format 3 Applied Proofreading: Greenbelt Planning Objection Letter",
        "proofreading_scenario": "The secretary of a residents' alliance drafted this formal objection to the Chief Planning Officer. There are <strong>5 SPaG errors</strong> involving semicolons, commas, and register.",
        "proofreading_text": """<p style="margin:0 0 2px 0;">Diana Sterling, Chief Planning Officer<br>Borough Development Directorate</p>
<p style="margin:4px 0 2px 0;"><strong>Re Planning Application PL/2026/0894</strong></p>
<p style="margin:0 0 4px 0;">Dear Ms Sterling</p>
<p style="margin:0 0 6px 0;">I am writing to register our formal objection to the proposed logistics hub on Greenfields Farm. The site occupies protected greenbelt land, therefore commercial development is fundamentally inappropriate.</p>
<p style="margin:0 0 6px 0;">Furthermore, freight traffic will increase nocturnal noise pollution; and diesel exhaust particulates will compromise air quality outside St Luke's Primary School.</p>
<p style="margin:0;">Yours faithfully,<br>Eleanor Vance</p>""",
        "proofreading_errors": [
            "Missing colon in formal reference line ('Re Planning Application' -> 'Re: Planning Application Ref:')",
            "Missing comma after salutation ('Dear Ms Sterling' -> 'Dear Ms Sterling,')",
            "Comma splice before conjunctive adverb ('protected greenbelt land, therefore' -> use semicolon: 'land; therefore,')",
            "Incorrect coordination with semicolon and 'and' ('noise pollution; and diesel' -> remove 'and' or change semicolon to comma)",
            "Incorrect sign-off matching ('Yours faithfully' with named recipient 'Dear Ms Sterling' -> must be 'Yours sincerely,')"
        ],
        "writing_prompt": "Write <strong>two formal sentences</strong> objecting to a commercial development on greenbelt land. Incorporate a semicolon and a conjunctive adverb (e.g. <em>consequently, furthermore, therefore</em>) followed by a comma."
    },
    {
        "unit": 4,
        "format": "Report",
        "title": "The Passive Voice & Objective Executive Grammar",
        "subtitle": "Impersonal Findings, Institutional Audits & Prioritised Recommendations",
        "rule_title": "Core Grammar Rule: Achieving an Objective, Impersonal Tone",
        "rule_text": """Formal reports require an objective, detached, and authoritative register. In executive reports, the writer emphasizes the findings and recommendations rather than their own personal feelings.<br><br>
<strong>Passive Voice &amp; Impersonal Constructions:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Active vs. Passive Voice:</strong>
    <ul style="margin:0 0 0 14px;">
      <li><em>Active:</em> 'We surveyed 600 students and found high anxiety.' (Emphasizes 'we').</li>
      <li><em>Passive:</em> 'Over 600 students <strong>were surveyed</strong>, and acute academic anxiety <strong>was recorded</strong>.' (Emphasizes the evidence).</li>
    </ul>
  </li>
  <li><strong>Impersonal Sentence Starters:</strong> Use objective reporting frames: <em>'It was observed that...', 'Evidence indicates that...', 'It is recommended that...'</em> instead of <em>'I think that...'</em> or <em>'In my view...'</em>.</li>
  <li><strong>Nominalisation (Noun-Heavy Style):</strong> Convert weak verbs into formal abstract nouns (e.g. <em>'improve facilities' &rarr; 'the improvement of facilities'; 'decide quickly' &rarr; 'a prompt decision'</em>).</li>
</ul>""",
        "format_link": "Executive boards and college principals expect reports written in an analytical, unbiased register. Mastering passive and impersonal constructions secures top-tier marks in Level 2 Composition and SPaG.",
        "worked_bad": "I looked at the counselling wait times and I noticed students wait seven weeks. I think this is terrible.",
        "worked_good": "An audit of therapeutic support services revealed that student waiting times have escalated to seven weeks. It is evident that existing pastoral capacity is severely overstretched.",
        "worked_why": "Replaced informal first-person commentary ('I looked', 'I think this is terrible') with rigorous impersonal framing ('An audit revealed', 'It is evident that').",
        "exercise_a": [
            ("Convert this active sentence to the formal passive voice: <em>'The college board commissioned this audit.'</em>",
             ["A) This audit was commissioned by the college board.",
              "B) This audit is commissioning the college board.",
              "C) The college board was commissioning this audit."],
             "A"),
            ("Select the sentence demonstrating the most objective executive register:",
             ["A) I believe the library computers are completely useless.",
              "B) Evidence gathered during the audit indicates that existing computing workstations are obsolete.",
              "C) In my honest opinion, we really need better computers."],
             "B"),
            ("Choose the correctly nominalised phrase to replace <em>'when students apply for support'</em>:",
             ["A) upon student application for support",
              "B) when applying by students",
              "C) as students are applying"],
             "A"),
            ("Identify the report recommendation adhering strictly to Pearson's full-sentence rule:",
             ["A) 1. Additional full-time counsellor needed urgently.",
              "B) 1. It is recommended that an additional full-time counsellor be recruited to reduce appointment backlogs.",
              "C) 1. Recruiting more counsellors before next term."],
             "B")
        ],
        "proofreading_title": "Format 4 Applied Proofreading: Student Pastoral Review Report",
        "proofreading_scenario": "A student liaison officer drafted this section of a pastoral provision report for the College Board. There are <strong>5 SPaG errors</strong> involving informal personal register, passive auxiliary errors, and bullet punctuation.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#1e3a8a;">2. Investigative Findings &amp; Pastoral Pressures</h4>
<p style="margin:0 0 4px 0;">A comprehensive survey was conduct across all academic departments. I found that over 68% of second-year students suffers from severe assessment anxiety.</p>
<p style="margin:0 0 4px 0;">Furthermore, therapeutic appointments was delayed by up to seven weeks. The following actions is recommended:</p>
<ul style="margin:0 0 6px 16px; padding:0;">
  <li>recruitment of a digital wellbeing coordinator</li>
  <li>Establishment of an accredited peer-mentoring programme before January 2027.</li>
</ul>""",
        "proofreading_errors": [
            "Incorrect passive past participle ('was conduct' -> 'was conducted')",
            "Subject-verb agreement error with plural percentage ('students suffers' -> 'students suffer')",
            "Subject-verb agreement in passive construction ('appointments was delayed' -> 'appointments were delayed')",
            "Subject-verb agreement error ('actions is recommended' -> 'actions are recommended')",
            "First bullet point is an uncapitalised fragment lacking a finite verb and full stop"
        ],
        "writing_prompt": "Write <strong>two objective report sentences</strong> evaluating campus study facilities. Use the passive voice (e.g. <em>'It was observed that...', 'Workstations were found to be...'</em>) and nominalisation to maintain an executive register."
    },
    {
        "unit": 5,
        "format": "Incident Report",
        "title": "Cause-and-Effect Connectives & Chronological Prepositions",
        "subtitle": "Root Cause Analysis & Forensic Incident Documentation",
        "rule_title": "Core Grammar Rule: Forensic Accuracy & Causal Subordination",
        "rule_text": """Workplace safety incident reports require rigorous chronological precision and exact causal syntax to establish liability and root causes without ambiguity.<br><br>
<strong>Causal Syntax &amp; Prepositional Accuracy:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Causal Connectives:</strong> Connect the physical defect directly to the accident: <em>consequently, as a direct result of, owing to, resulting from</em> (e.g. <em>'The ladder stile fractured owing to metal fatigue, resulting in the operative's fall.'</em>).</li>
  <li><strong>Avoid Informal 'Due to' Misuse:</strong> Remember that <em>due to</em> modifies nouns, whereas <em>because of / owing to</em> modifies verbs (e.g. <em>'The accident was due to equipment failure'</em> vs. <em>'The worker fell because of equipment failure'</em>).</li>
  <li><strong>Temporal Prepositions:</strong> Pinpoint exact timings: <em>'At approximately 14:15', 'Prior to the incident', 'Concurrently with first aid intervention', 'Subsequent to site quarantine'</em>.</li>
</ul>""",
        "format_link": "In legal and regulatory safety reporting, sloppy causal grammar obscures what actually caused the accident. Clear cause-and-effect clauses ensure your report withstands scrutiny.",
        "worked_bad": "Jason fell off the ladder due to it broke because of it was old and he hurt his wrist.",
        "worked_good": "At 14:15, Jason Miller fell from the fourth rung of an aluminum stepladder owing to structural failure of the rubber anti-slip foot, sustaining severe ligament sprains to his right wrist.",
        "worked_why": "Combined timestamps, specific mechanical defect terminology, and formal causal prepositions into an authoritative forensic sentence.",
        "exercise_a": [
            ("Select the sentence with correct cause-and-effect prepositional grammar:",
             ["A) The spillage occurred owing to a cracked drum valve, resulting in hazardous chemical vapor.",
              "B) The spillage occurred due to a cracked drum valve, resulting in hazardous chemical vapor.",
              "C) The spillage occurred because a cracked drum valve."],
             "A"),
            ("Choose the correct past participle for passive incident reporting: <em>'The defective stepladder was immediately [ ________ ] with safety lockout tags.'</em>",
             ["A) quarantine", "B) quarantined", "C) quarantining"],
             "B"),
            ("Identify the sentence using precise chronological prepositions:",
             ["A) Around that time, the first aider came and helped.",
              "B) Concurrently with the dispatch of emergency first aid, safety marshals established an exclusion perimeter.",
              "C) After some minutes we did first aid."],
             "B"),
            ("Select the correctly punctuated preventative recommendation:",
             ["A) Mandatory pre-use equipment inspections must be recorded weekly, this will prevent future falls.",
              "B) Mandatory pre-use equipment inspections must be recorded weekly; this protocol will prevent future falls.",
              "C) Mandatory pre-use equipment inspections must be recorded weekly this protocol will prevent future falls."],
             "B")
        ],
        "proofreading_title": "Format 5 Applied Proofreading: Warehouse Loading Bay Incident",
        "proofreading_scenario": "A shift supervisor drafted this incident log following a stockroom ladder collapse. There are <strong>5 SPaG errors</strong> involving causal grammar, past participles, and agreement.",
        "proofreading_text": """<div style="background:#f8fafc; border:1px solid #cbd5e1; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Incident Reference:</strong> INC-2026-088 | <strong>Location:</strong> Stockroom Bay 3
</div>
<p style="margin:0 0 4px 0;"><strong>Account of Occurrence:</strong><br>
At 14:15 on 18 October, stockroom assistant Jason Miller was retrieving inventory when the front stile of the stepladder detach without warning. Consequently Mr Miller lost balance and fell four feet onto the concrete floor.</p>
<p style="margin:0 0 4px 0;">First-aid treatment were administered immediately by David Ross, who bandaged the injured operative's wrist. The defective ladder was withdrew from service and tagged out.</p>
<p style="margin:0;">Weekly access equipment audits has been scheduled to commence immediately.</p>""",
        "proofreading_errors": [
            "Tense clash in verb form ('stile ... detach' -> 'stile ... detached')",
            "Missing comma after fronted causal connective ('Consequently Mr Miller' -> 'Consequently, Mr Miller')",
            "Subject-verb agreement in passive construction ('First-aid treatment were administered' -> 'treatment was administered')",
            "Incorrect irregular verb form ('was withdrew' -> 'was withdrawn')",
            "Subject-verb agreement error ('Weekly access equipment audits has been' -> 'audits have been scheduled')"
        ],
        "writing_prompt": "Write <strong>two forensic incident report sentences</strong> detailing a spillage incident in a commercial loading bay. Include a specific time reference, a cause-and-effect connective (e.g. <em>as a direct consequence of, resulting in</em>), and passive containment actions."
    },
    {
        "unit": 6,
        "format": "Advice Leaflet",
        "title": "Modal Verbs of Obligation & Hyphenated Compound Adjectives",
        "subtitle": "Clarifying Statutory Rights, Workplace Duties & Advisory Nuance",
        "rule_title": "Core Grammar Rule: Modals of Obligation & Compound Modifiers",
        "rule_text": """Advice leaflets must communicate complex legal, statutory, or technical information in an accessible yet legally precise manner.<br><br>
<strong>Modal Verbs &amp; Hyphenation Rules:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Graduated Modal Auxiliaries of Obligation:</strong>
    <ul style="margin:0 0 0 14px;">
      <li><em>Must / Shall:</em> Strict legal requirement (e.g. <em>'Employers <strong>must</strong> provide a written statement of terms.'</em>).</li>
      <li><em>Should / Ought to:</em> Recommended best practice (e.g. <em>'You <strong>should</strong> document all overtime hours.'</em>).</li>
      <li><em>May / Can:</em> Statutory entitlement or option (e.g. <em>'Employees <strong>may</strong> request union representation.'</em>).</li>
    </ul>
  </li>
  <li><strong>Hyphenated Compound Adjectives:</strong> When two or more words act as a single unit modifying a noun that follows them, join them with a <strong>hyphen</strong>: <em>'step-by-step guidance', 'zero-hour contracts', 'cost-effective solution', 'high-risk environment', 'user-friendly platform'</em>.<br>
  <em>Note:</em> Do NOT hyphenate when the compound follows the noun (e.g. <em>'guidance that is step by step'</em>) or with adverbs ending in <em>-ly</em> (e.g. <em>'highly qualified staff'</em>).</li>
</ul>""",
        "format_link": "In public guidance leaflets regarding employment rights or mental wellbeing, precise modal verbs prevent legal misunderstandings, while compound hyphens ensure polished readability.",
        "worked_bad": "You can get a rest break if you work six hours. Look at your low pay rates.",
        "worked_good": "Under statutory employment regulations, workers are legally entitled to an uninterrupted twenty-minute rest break during any shift exceeding six hours.",
        "worked_why": "Employed precise statutory terminology and hyphenated compound time modifiers to provide legally accurate guidance.",
        "exercise_a": [
            ("Select the modal verb indicating a mandatory legal requirement: <em>'All UK employers [ ________ ] pay at least the statutory National Minimum Wage.'</em>",
             ["A) may", "B) must", "C) could"],
             "B"),
            ("Choose the correctly hyphenated compound adjective before a noun:",
             ["A) A zero hour contract", "B) A zero-hour contract", "C) A zero - hour contract"],
             "B"),
            ("Identify the sentence with correct hyphenation:",
             ["A) The leaflet provides up-to-date employment advice.",
              "B) The leaflet provides up to date employment advice.",
              "C) The leaflet provides highly-detailed employment advice."],
             "A"),
            ("Select the sentence with correct modal nuance for an advice leaflet:",
             ["A) You must sue your boss if there is a mistake.",
              "B) If you identify a wage discrepancy, you should raise an informal inquiry with payroll first.",
              "C) You might want to consider maybe mentioning your pay."],
             "B")
        ],
        "proofreading_title": "Format 6 Applied Proofreading: Employment Rights Leaflet",
        "proofreading_scenario": "A careers advisor drafted this section of an advice leaflet for young workers. There are <strong>5 SPaG errors</strong> involving compound hyphens, modal auxiliary agreement, and punctuation.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#1e3a8a;">Know Your Rights: A Young Workers Guide</h4>
<p style="margin:0 0 4px 0;">Starting work is a major milestone, but young employees must understands their statutory entitlements before signing any contract.</p>
<p style="margin:0 0 6px 0;">Under UK law, employers must not pay below legal minimum wage brackets, nor can they deduct uniform costs if doing so reduces pay below statutory thresholds. Workers should always insist on a well structured written contract.</p>
<p style="margin:0;">If disputes arise, you ought contact ACAS for free confidential mediation.</p>""",
        "proofreading_errors": [
            "Missing plural possessive apostrophe in heading ('Young Workers Guide' -> 'Young Workers\\' Guide')",
            "Subject-verb agreement error with modal auxiliary ('must understands' -> 'must understand')",
            "Missing hyphen in compound adjective before noun ('well structured written contract' -> 'well-structured')",
            "Missing infinitive particle after 'ought' ('you ought contact' -> 'you ought to contact')",
            "Missing comma between coordinate adjectives ('free confidential' -> 'free, confidential')"
        ],
        "writing_prompt": "Write <strong>two advice sentences</strong> for an employee leaflet on managing workplace stress. Incorporate two hyphenated compound adjectives (e.g. <em>work-related, long-term, self-care</em>) and a graduated modal verb (<em>should / must</em>)."
    },
    {
        "unit": 7,
        "format": "Review",
        "title": "Adverbs of Degree, Evaluative Modifiers & Parenthesis",
        "subtitle": "Nuanced Software, Product & Service Critiques",
        "rule_title": "Core Grammar Rule: Precision Adverbs & Parenthetical Punctuation",
        "rule_text": """Top-scoring Level 2 reviews avoid simplistic praise or crude condemnation. Instead, they employ graduated adverbs of degree and parenthetical punctuation (brackets or dashes) to deliver balanced, credible evaluations.<br><br>
<strong>Evaluative Adverbs &amp; Parenthetical Rules:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Adverbs of Degree:</strong> Modulate your critique with analytical adverbs: <em>exceptionally, remarkably, moderately, somewhat, marginally, disappointingly, inconsistently</em> (e.g. <em>'The interface is <strong>remarkably intuitive</strong>, though the notification engine operates <strong>disappointingly inconsistently</strong>.'</em>).</li>
  <li><strong>Parenthetical Brackets ():</strong> Use brackets to insert technical specifications, pricing details, or brief clarifications without disrupting sentence flow: <em>'The core tier is entirely free, while the premium tier (£3.99 per month) unlocks automated calendar sync.'</em></li>
  <li><strong>Em-Dashes (—) for Evaluative Emphasis:</strong> Use paired dashes for parenthetical amplification: <em>'The scheduling tool—the application's strongest asset—consolidates assignments effortlessly.'</em></li>
</ul>""",
        "format_link": "High-level reviews published on technology blogs or consumer websites rely on sophisticated modifiers and parenthesis to convey objectivity and expertise.",
        "worked_bad": "PlanSmart is good but it has bugs. It costs 3.99 a month which is okay.",
        "worked_good": "While PlanSmart delivers exceptionally robust task-scheduling features, its premium subscription tier (£3.99 per month) is somewhat undermined by occasional notification latency.",
        "worked_why": "Enhanced generic adjectives ('good', 'okay') with analytical adverbs ('exceptionally robust', 'somewhat undermined') and integrated parenthetical pricing.",
        "exercise_a": [
            ("Choose the adverb of degree that expresses slight, balanced criticism:",
             ["A) completely", "B) somewhat", "C) utterly"],
             "B"),
            ("Select the sentence demonstrating correct parenthetical bracket punctuation:",
             ["A) The software (compatible with iOS and Android operates smoothly.",
              "B) The software (compatible with iOS and Android) operates smoothly.",
              "C) The software compatible with (iOS and Android) operates smoothly."],
             "B"),
            ("Identify the sentence using paired dashes correctly for evaluative emphasis:",
             ["A) The cloud backup feature—essential for remote collaboration—performed flawlessly throughout our testing.",
              "B) The cloud backup feature—essential for remote collaboration performed flawlessly throughout our testing.",
              "C) The cloud backup feature-essential for remote collaboration-performed flawlessly."],
             "A"),
            ("Select the evaluative sentence maintaining a sophisticated Level 2 register:",
             ["A) The app is super amazing and I totally love using it every day.",
              "B) The platform exhibits impressive versatility, although its offline functionality remains moderately restricted.",
              "C) It is a really good app with no bad stuff."],
             "B")
        ],
        "proofreading_title": "Format 7 Applied Proofreading: Technology App Review",
        "proofreading_scenario": "A tech journalist drafted this critique of the PlanSmart productivity app. There are <strong>5 SPaG errors</strong> involving evaluative adverbs, brackets, dashes, and comma splices.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#1e3a8a;">PlanSmart: Streamlined Productivity with Minor Mobile Glitches</h4>
<p style="margin:0 0 4px 0; color:#d97706; font-size:7.5pt; font-weight:bold;">★★★★☆ (4.2 out of 5 Stars) | By Callum Hughes</p>
<p style="margin:0 0 6px 0;">Engineered for tertiary students, PlanSmart offers an intuitive visual timeline, it simplifies complex modular deadlines effectively.</p>
<p style="margin:0 0 6px 0;">The applications synchronization engine—its most celebrated feature—integrates seamlessly with Outlook and Google Calendar. However the premium subscription tier £3.99 per month is moderately expensive for learners on tight budgets.</p>
<p style="margin:0;">Overall the software performs exceptional well under heavy daily usage.</p>""",
        "proofreading_errors": [
            "Comma splice in paragraph 1 ('visual timeline, it simplifies' -> use semicolon or conjunction)",
            "Missing possessive apostrophe in noun ('applications synchronization' -> 'application\\'s synchronization')",
            "Missing comma after fronted adverbial ('However the premium' -> 'However, the premium')",
            "Missing parenthetical brackets around pricing details ('tier (£3.99 per month) is')",
            "Adverb form error in evaluative modifier ('performs exceptional well' -> 'performs exceptionally well')"
        ],
        "writing_prompt": "Write <strong>two review sentences</strong> evaluating a digital gadget, software app, or hospitality venue. Incorporate an adverb of degree (e.g. <em>exceptionally, marginally, disappointingly</em>) and parenthetical brackets containing factual detail."
    },
    {
        "unit": 8,
        "format": "Online Feedback Form",
        "title": "Plural Possessive Apostrophes & Confusing Words",
        "subtitle": "Customer Redress Portals, Statutory Rights & Compensation Claims",
        "rule_title": "Core Grammar Rule: Plural Possession & High-Frequency Confusables",
        "rule_text": """Online complaint submissions require exact grammatical precision. Errors in plural possession or basic word choice undermine your legal credibility when claiming financial compensation.<br><br>
<strong>Plural Possession &amp; Confusable Words:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Plural Possessive Apostrophes:</strong>
    <ul style="margin:0 0 0 14px;">
      <li>Regular Plurals ending in <em>-s</em>: Add an apostrophe <strong>after the -s</strong>: <em>the passengers' rights; the managers' decisions; the customers' complaints</em>.</li>
      <li>Irregular Plurals NOT ending in <em>-s</em>: Add <em>'s</em>: <em>the children's luggage; the women's team; people's expectations</em>.</li>
    </ul>
  </li>
  <li><strong>The Big Level 2 Confusable Pairs:</strong>
    <ul style="margin:0 0 0 14px;">
      <li><strong>Affect vs. Effect:</strong> <em>Affect</em> is usually a verb (to influence: <em>'The delay will affect my schedule'</em>). <em>Effect</em> is usually a noun (the result: <em>'The delay had a severe effect on my plans'</em>).</li>
      <li><strong>Practice vs. Practise:</strong> In British English, <em>practice</em> is the noun (<em>'good practice'</em>); <em>practise</em> is the verb (<em>'they practise daily'</em>).</li>
      <li><strong>Stationery vs. Stationary:</strong> <em>Stationery</em> with an 'e' is envelopes/paper; <em>stationary</em> with an 'a' means motionless.</li>
    </ul>
  </li>
</ul>""",
        "format_link": "Statutory claims under Civil Aviation or consumer protection regulations require rigorous precision. Confusing 'affect' with 'effect' or misplacing plural apostrophes looks uneducated to assessors.",
        "worked_bad": "The flight cancellation had a bad affect on 180 passenger's plans. The plane remained stationery on the tarmac.",
        "worked_good": "The sudden cancellation had a catastrophic effect on 180 passengers' travel arrangements, as the aircraft remained stationary on the tarmac for three hours.",
        "worked_why": "Corrected 'affect' (verb) to 'effect' (noun), positioned the plural possessive apostrophe after the -s ('passengers''), and corrected 'stationery' to 'stationary' (motionless).",
        "exercise_a": [
            ("Select the correct confusable word: <em>'The prolonged tarmac delay had a detrimental [ affect / effect ] on passenger morale.'</em>",
             ["A) affect", "B) effect"],
             "B"),
            ("Select the correct confusable word: <em>'The railway company failed to adhere to standard industry [ practice / practise ].'</em>",
             ["A) practice", "B) practise"],
             "A"),
            ("Choose the sentence with correct plural possessive apostrophes:",
             ["A) Ground staff ignored the passengers' statutory rights.",
              "B) Ground staff ignored the passenger's statutory rights when referring to 200 people.",
              "C) Ground staff ignored the passengers's statutory rights."],
             "A"),
            ("Select the sentence free from confusable word errors:",
             ["A) The train remained stationery outside the station.",
              "B) The train remained stationary outside the station.",
              "C) The delay did not effect our connection."],
             "B")
        ],
        "proofreading_title": "Format 8 Applied Proofreading: Airline Customer Complaint",
        "proofreading_scenario": "A stranded passenger submitted this online complaint to SkyLink Airways. There are <strong>5 SPaG errors</strong> involving plural apostrophes, confusing words, and punctuation.",
        "proofreading_text": """<div style="background:#f8fafc; border:1px solid #cbd5e1; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Portal:</strong> SkyLink Customer Redress | <strong>Ref:</strong> SK-904128
</div>
<p style="margin:0 0 4px 0;"><strong>Formal Complaint Details:</strong><br>
I am writing following the cancellation of flight SL-482. The sudden cancellation had an immediate negative affect on over two hundred passenger's onward journeys.</p>
<p style="margin:0 0 4px 0;">The aircraft was held stationery on the runway for two hours without air conditioning, causing severe physical distress. Ground staff failed to put into practise standard passenger duty-of-care protocols.</p>
<p style="margin:0;">I demand full reimbursement of my £196 expenses, its my statutory right under aviation regulations.</p>""",
        "proofreading_errors": [
            "Confusable word error ('negative affect' -> 'negative effect')",
            "Misplaced plural possessive apostrophe ('two hundred passenger\\'s' -> 'passengers\\'')",
            "Confusable word error ('held stationery' -> 'held stationary')",
            "Confusable word error ('put into practise' -> 'put into practice' - noun)",
            "Comma splice with missing contraction apostrophe ('£196 expenses, its my statutory' -> use semicolon: 'expenses; it\\'s my statutory')"
        ],
        "writing_prompt": "Write <strong>two formal sentences</strong> for a customer redress portal demanding reimbursement for an unexpected hotel bill following a cancellation. Use the plural possessive noun <em>passengers'</em> and use <em>effect</em> correctly as a noun."
    },
    {
        "unit": 9,
        "format": "Online Forum / Blog Post",
        "title": "Concession Clauses & Rhetorical Punctuation in Debate",
        "subtitle": "Balancing Complex Societal Debates & Counter-Arguments",
        "rule_title": "Core Grammar Rule: Constructing Concession Clauses & Nuanced Rhetoric",
        "rule_text": """Extended forum debates and intellectual blog posts require the ability to acknowledge counter-arguments respectfully before delivering a decisive rebuttal.<br><br>
<strong>Concession Connectives &amp; Rhetorical Punctuation:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Subordinating Concession Connectives:</strong> Use formal concession openers: <em>Notwithstanding the fact that..., While it is undoubtedly true that..., Although proponents argue that..., Granted that...</em> (e.g. <em>'While commercial trials demonstrate measurable productivity gains, customer-facing sectors encounter severe scheduling friction.'</em>).</li>
  <li><strong>Rhetorical Questions:</strong> Punctuate authentic rhetorical questions with a question mark, but avoid conversational whining (e.g. <em>'Can modern service economies realistically compress customer support into four calendar days?'</em>).</li>
  <li><strong>Em-Dashes (—) for Contrast:</strong> Use an em-dash to introduce an emphatic contrast or reality check: <em>'The four-day week promises operational liberation—yet without flexible workforce rotation, it risks catastrophic employee burnout.'</em></li>
</ul>""",
        "format_link": "In public debate forums regarding flexible working models or education policy, concession clauses demonstrate maturity of thought and analytical sophistication.",
        "worked_bad": "Some people like the four day week. But it won't work for hospitals. I think it is stupid.",
        "worked_good": "Notwithstanding the compelling mental health dividends evidenced in white-collar commercial trials, operational reality dictates that emergency services cannot simply shutter operations on Friday afternoons.",
        "worked_why": "Substituted conversational dismissals with a formal concession clause ('Notwithstanding the compelling...') and sophisticated socio-economic vocabulary.",
        "exercise_a": [
            ("Choose the most sophisticated concession connective to start a counter-argument:",
             ["A) Although", "B) But", "C) And"],
             "A"),
            ("Select the sentence correctly punctuating a concession clause with a comma:",
             ["A) While shortened working hours alleviate fatigue continuous client coverage remains essential.",
              "B) While shortened working hours alleviate fatigue, continuous client coverage remains essential.",
              "C) While shortened working hours alleviate fatigue; continuous client coverage remains essential."],
             "B"),
            ("Identify the sentence using a rhetorical dash effectively for debate emphasis:",
             ["A) The proposal promises reduced overheads—yet it demands rigorous workforce discipline.",
              "B) The proposal promises reduced overheads-yet it demands rigorous workforce discipline.",
              "C) The proposal promises reduced overheads; yet it demands rigorous workforce discipline."],
             "A"),
            ("Select the correctly punctuated rhetorical question:",
             ["A) How can organisations balance reduced hours with client accessibility.",
              "B) How can organisations balance reduced hours with client accessibility?",
              "C) How can organisations balance reduced hours with client accessibility!?"],
             "B")
        ],
        "proofreading_title": "Format 9 Applied Proofreading: Workplace Debate Forum Post",
        "proofreading_scenario": "An operations manager contributed this analysis to an industry debate on the four-day working week. There are <strong>5 SPaG errors</strong> involving concession punctuation, comma splices, and spelling.",
        "proofreading_text": """<div style="background:#f1f5f9; border-left:3px solid #1e3a8a; padding:4px 8px; font-size:7.5pt; margin-bottom:4px;">
<strong>Forum:</strong> Workplace Futures &gt; <em>The Four-Day Week: Miracle or Mirage?</em>
</div>
<p style="margin:0 0 4px 0;">The ongoing debate is too frequently polarised by rigid ideological stances.</p>
<p style="margin:0 0 6px 0;">While extensive trials demonstrate significant redution in chronic workplace stress operational logistics in customer-facing sectors remain highly problematic. Squeezing forty hours of intensive labour into four condensed shifts causes severe exhaustion, it compromises employee wellbeing.</p>
<p style="margin:0;">Can we honestly afford to ignore these friction points. Staggered team rotations provide the only viable compromise—yet many firms refuse to adopt them.</p>""",
        "proofreading_errors": [
            "Spelling error in academic vocabulary ('redution' -> 'reduction')",
            "Missing comma after introductory concession clause ('workplace stress, operational')",
            "Comma splice between independent clauses ('condensed shifts causes severe exhaustion, it compromises' -> use semicolon)",
            "Incorrect punctuation for a rhetorical question (ends in full stop instead of question mark: 'friction points?')",
            "Missing hyphen in compound modifier ('customer facing' -> 'customer-facing')"
        ],
        "writing_prompt": "Write <strong>two extended forum sentences</strong> debating degree apprenticeships versus traditional university education. Begin the first sentence with a formal concession clause (e.g. <em>While traditional university degrees provide..., Notwithstanding the cost of...</em>)."
    },
    {
        "unit": 10,
        "format": "Newsletter",
        "title": "Embedded Parenthetical Clauses, Appositives & Participials",
        "subtitle": "Writing Engaging Corporate & Community Newsletter Stories",
        "rule_title": "Core Grammar Rule: Syntactic Variety with Appositives & Participial Phrases",
        "rule_text": """Staff and community newsletters must deliver high volumes of diverse information (celebrating milestones, profiling volunteers, announcing competitions) concisely and engagingly.<br><br>
<strong>Appositives &amp; Participial Phrases:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Appositives (Nouns in Apposition):</strong> A noun phrase placed next to another noun to rename or describe it, enclosed in <strong>paired commas</strong>: <em>'Marcus Vance, <strong>our Operations Director</strong>, presented the awards.'</em></li>
  <li><strong>Present Participial Phrases (-ing):</strong> Action openers that link events smoothly: <em>'<strong>Having surpassed</strong> our environmental targets, the warehouse team celebrated with a lunch.'</em> (Ensure the subject following the comma actually performed the action to avoid dangling modifiers!).</li>
  <li><strong>Past Participial Phrases (-ed / irregular):</strong> <em>'<strong>Disturbed</strong> by excessive landfill waste, the Green Champions launched a recycling challenge.'</em></li>
</ul>""",
        "format_link": "In newsletters, starting every sentence with 'We' or 'The company' produces monotony. Appositives and participial phrases inject professional energy into your journalistic style.",
        "worked_bad": "Apex Logistics reduced waste by 40%. The company installed 350 solar panels. They celebrated yesterday.",
        "worked_good": "Having slashed commercial landfill waste by 40% through rigorous warehouse recycling, Apex Logistics celebrated a major milestone yesterday by activating 350 high-efficiency rooftop solar panels.",
        "worked_why": "Combined three repetitive simple sentences into an energetic compound-complex sentence using an introductory present participial phrase.",
        "exercise_a": [
            ("Select the sentence with correctly punctuated appositives around the job title:",
             ["A) Rachel Hall our Facilities Coordinator, initiated the project.",
              "B) Rachel Hall, our Facilities Coordinator, initiated the project.",
              "C) Rachel Hall, our Facilities Coordinator initiated the project."],
             "B"),
            ("Choose the correctly structured sentence using an introductory participial phrase:",
             ["A) Operating across six European hubs, Apex Logistics handles 10,000 consignments daily.",
              "B) Operating across six European hubs, 10,000 consignments are handled daily by Apex Logistics.",
              "C) Operating across six European hubs 10,000 consignments daily."],
             "A"),
            ("Identify the sentence free from dangling modifiers:",
             ["A) Walking through the distribution depot, several safety hazards were noticed by the manager.",
              "B) Walking through the distribution depot, the manager noticed several safety hazards.",
              "C) Walking through the distribution depot, safety hazards appeared."],
             "B"),
            ("Select the sentence with correct coordinating punctuation:",
             ["A) Teams will compete to conserve energy; the winning department will receive the Green Champions Cup.",
              "B) Teams will compete to conserve energy, the winning department will receive the Green Champions Cup.",
              "C) Teams will compete to conserve energy the winning department will receive the cup."],
             "A")
        ],
        "proofreading_title": "Format 10 Applied Proofreading: Corporate Staff Newsletter",
        "proofreading_scenario": "An internal communications officer drafted this lead article for the staff newsletter. There are <strong>5 SPaG errors</strong> involving appositive commas, participial modifiers, and semicolons.",
        "proofreading_text": """<h4 style="margin:0 0 2px 0; color:#1e3a8a;">Apex Horizons • Internal Staff Newsletter • November Edition</h4>
<p style="margin:0 0 4px 0;">We are delighted to celebrate a remarkable corporate milestone.</p>
<p style="margin:0 0 6px 0;">Marcus Vance our Chief Operating Officer praised the warehouse logistics team for cutting landfill disposal by 40%. Having installed 350 photovoltaic solar panels the central facility now generates 25% of its own electrical power.</p>
<p style="margin:0;">The annual volunteering week commences on 16 November, staff are encouraged to register via the intranet portal.</p>""",
        "proofreading_errors": [
            "Missing paired commas around the appositive phrase ('Marcus Vance our Chief Operating Officer praised' -> 'Marcus Vance, our Chief Operating Officer, praised')",
            "Missing comma after introductory participial phrase ('photovoltaic solar panels the central' -> 'photovoltaic solar panels, the central')",
            "Comma splice in final sentence ('commences on 16 November, staff are' -> use semicolon: 'November; staff are')",
            "Proper noun capitalisation error ('volunteering week' -> 'Volunteering Week')",
            "Missing hyphen in compound modifier ('landfill disposal' vs other modifiers)"
        ],
        "writing_prompt": "Write <strong>two engaging newsletter sentences</strong> announcing an employee achievement or charity volunteering day. Include an appositive phrase enclosed in paired commas (e.g. <em>David Ross, our senior logistics coordinator,</em>) and an introductory participial phrase."
    },
    {
        "unit": 11,
        "format": "Reflective Log / Diary",
        "title": "Third Conditionals & Evaluative Target-Setting Syntax",
        "subtitle": "Critical Self-Assessment & Strategic Vocational Growth",
        "rule_title": "Core Grammar Rule: Hypothetical Past Conditionals & Reflective Modals",
        "rule_text": """In vocational reflective logs and professional learning journals, learners must demonstrate critical self-awareness. You must analyse why a situation occurred, evaluate your response, and articulate how you would handle it differently in future.<br><br>
<strong>Third Conditional &amp; Target-Setting Grammar:</strong>
<ul style="margin:2px 0 0 16px; padding:0;">
  <li><strong>Third Conditional (Hypothetical Past Evaluation):</strong> Used to evaluate an event that has already happened:
    <div style="background:#f8fafc; padding:3px 6px; margin:2px 0; border-left:2px solid #1e3a8a;">
      <em>'If + past perfect [had done], ... would have + past participle [would have done]'</em><br>
      Example: <em>'If I <strong>had distributed</strong> the meeting agenda beforehand, the disagreement <strong>would not have escalated</strong>.'</em><br>
      <em>Inversion (Formal):</em> <em>'<strong>Had I distributed</strong> the agenda beforehand, the disagreement would not have escalated.'</em>
    </div>
  </li>
  <li><strong>Reflective Modal Evaluators:</strong> <em>'I should have intervened sooner', 'I could have articulated the brief more clearly'</em>. Never write <em>'should of'</em> or <em>'could of'</em> (always <em>should have / could have</em>).</li>
  <li><strong>Future Target Syntax:</strong> Use decisive modal verbs for forward action: <em>'In subsequent committee sessions, I shall institute strict time allocations...'</em></li>
</ul>""",
        "format_link": "Vocational assessors and Pearson examiners award the highest marks when learners use advanced conditional structures to demonstrate authentic professional self-reflection.",
        "worked_bad": "I should of stopped the argument between Liam and Chloe. If I knew they were angry I would of stepped in.",
        "worked_good": "On reflection, I should have intervened more assertively when ideological friction arose. Had I established structured speaking turns earlier, the confrontational dispute would have been averted entirely.",
        "worked_why": "Eliminated the grammatical error 'should of' -> 'should have', and employed an inverted third conditional ('Had I established...') to express sophisticated self-evaluation.",
        "exercise_a": [
            ("Select the grammatically correct reflective modal phrase:",
             ["A) I should of clarified the assignment parameters earlier.",
              "B) I should have clarified the assignment parameters earlier.",
              "C) I should off clarified the assignment parameters earlier."],
             "B"),
            ("Choose the correct third conditional sentence:",
             ["A) If I had anticipated the customer's objection, I would have prepared the warranty terms in advance.",
              "B) If I anticipated the customer's objection, I would have prepared the warranty terms.",
              "C) If I had anticipated the customer's objection, I would prepare the warranty terms."],
             "A"),
            ("Identify the formal inverted conditional construction:",
             ["A) Had I managed the meeting schedule more rigorously, the deadline would have been met.",
              "B) If I managed the meeting schedule more rigorously, the deadline was met.",
              "C) Managing the meeting schedule, the deadline would be met."],
             "A"),
            ("Select the forward-looking target statement demonstrating executive commitment:",
             ["A) I might try to maybe be better next week.",
              "B) In future group presentations, I shall allocate dedicated rehearsal slots to ensure seamless role transitions.",
              "C) I hope things go better next time."],
             "B")
        ],
        "proofreading_title": "Format 11 Applied Proofreading: Professional Leadership Log",
        "proofreading_scenario": "A business management student completed this reflective log entry after chairing a project planning meeting. There are <strong>5 SPaG errors</strong> involving reflective modals, conditionals, and comma splices.",
        "proofreading_text": """<div style="border-bottom:1px solid #cbd5e1; padding-bottom:2px; margin-bottom:4px; font-size:7.5pt; font-weight:bold; color:#1e3a8a;">
Leadership Learning Log | Session: Final Project Planning | Date: 28 October 2026
</div>
<p style="margin:0 0 4px 0;"><strong>Context &amp; Dynamics:</strong><br>
Today I chaired our final marketing strategy meeting. A heated dispute erupted between Liam and Chloe regarding target demographics, it threatened our project timeline.</p>
<p style="margin:0 0 4px 0;"><strong>Self-Critique:</strong><br>
On reflection, I should of intervened sooner to de-escalate the tension. If I had prepared an explicit agenda with allocated speaking times, the confrontation would of been avoided.</p>
<p style="margin:0;"><strong>Target:</strong><br>
In future sessions I will distribute a structured discussion framework beforehand.</p>""",
        "proofreading_errors": [
            "Missing comma after introductory time adverbial ('Today I chaired' -> 'Today, I chaired')",
            "Comma splice in context description ('regarding target demographics, it threatened' -> use semicolon)",
            "Grammatical error in reflective modal ('should of intervened' -> 'should have intervened')",
            "Grammatical error in third conditional ('would of been avoided' -> 'would have been avoided')",
            "Missing comma after fronted prepositional phrase ('In future sessions I will' -> 'In future sessions, I will')"
        ],
        "writing_prompt": "Write <strong>two reflective sentences</strong> evaluating your performance in a demanding workplace or educational task. In the first sentence, use a third conditional (e.g. <em>Had I prepared..., I would have...</em>); in the second, articulate a clear forward target using <em>shall / will</em>."
    }
]
