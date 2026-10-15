# spag_content_extras.py
# Spelling rules, vocabulary banks, mixed exam workouts, and answer keys for Level 1 and Level 2 SPaG Workbooks.

L1_SPELLING_DATA = {
    "rules": [
        ("1. Plural Noun Endings (-s, -es, -ies, -ves)",
         "Most English words simply add <strong>-s</strong> (<em>job &rarr; jobs, desk &rarr; desks, report &rarr; reports</em>).<br>"
         "Words ending in a hissing sound (<em>-s, -ss, -sh, -ch, -x, -z</em>) add <strong>-es</strong> (<em>bus &rarr; buses, address &rarr; addresses, wish &rarr; wishes, match &rarr; matches, box &rarr; boxes</em>).<br>"
         "Words ending in a consonant + <em>y</em> drop the <em>y</em> and add <strong>-ies</strong> (<em>company &rarr; companies, community &rarr; communities, category &rarr; categories</em>). (If preceded by a vowel, just add <em>-s</em>: <em>day &rarr; days, key &rarr; keys</em>).<br>"
         "Words ending in <em>-f</em> or <em>-fe</em> often change to <strong>-ves</strong>: <em>shelf &rarr; shelves, knife &rarr; knives, leaf &rarr; leaves</em>."),

        ("2. Doubling Final Consonants (The 1-1-1 Rule)",
         "In short 1-syllable words with <strong>1 short vowel</strong> ending in <strong>1 consonant</strong>, you must double the final consonant before adding vowel suffixes (<em>-ed, -ing, -er</em>):<br>"
         "<em>plan &rarr; planned / planning, drop &rarr; dropped / dropping, slip &rarr; slipped / slipping, fit &rarr; fitted / fitting, stop &rarr; stopped / stopping</em>.<br>"
         "<strong>Exam Warning:</strong> Never write <em>droped, sliped,</em> or <em>planed</em> on your exam script!"),

        ("3. Dropping or Keeping Silent 'e'",
         "<strong>Drop silent 'e'</strong> when adding a suffix starting with a vowel (<em>-ing, -ed, -able</em>): <em>hope &rarr; hoping, write &rarr; writing, close &rarr; closing, arrive &rarr; arrival, create &rarr; creative</em>.<br>"
         "<strong>Keep silent 'e'</strong> when adding a suffix starting with a consonant (<em>-ful, -ment, -ly, -ness</em>): <em>hope &rarr; hopeful, safe &rarr; safely, manage &rarr; management, polite &rarr; politely, care &rarr; careless</em>."),

        ("4. Changing 'y' to 'i' Before Suffixes",
         "When a base word ends in a consonant + <em>y</em>, change the <em>y</em> to <strong>i</strong> before any suffix (except <em>-ing</em>):<br>"
         "<em>happy &rarr; happily / happiness, easy &rarr; easily, beauty &rarr; beautiful, heavy &rarr; heavily, tidy &rarr; tidied</em>.<br>"
         "Keep the <em>y</em> before <em>-ing</em> to prevent double 'ii': <em>hurry &rarr; hurrying, reply &rarr; replying, carry &rarr; carrying</em>."),

        ("5. The 'i before e except after c' Rule & Exceptions",
         "Put <strong>i before e</strong> when sounding like 'ee': <em>believe, achieve, piece, relief, chief, friend</em>.<br>"
         "Except immediately <strong>after c</strong>: <em>receive, receipt, ceiling, deceive, conceit</em>.<br>"
         "<strong>Key Exam Exceptions to Memorise:</strong> <em>their, neighbour, weigh, weight, foreign, leisure, neither, height</em>."),

        ("6. High-Frequency Exam Homophones Mastery",
         "<strong>There</strong> (location / statement: <em>over there / there is a delay</em>) vs. <strong>Their</strong> (possession: <em>their manager</em>) vs. <strong>They're</strong> (short for <em>they are</em>).<br>"
         "<strong>To</strong> (direction / infinitive: <em>travel to college</em>) vs. <strong>Too</strong> (also / excessive: <em>too cold</em>) vs. <strong>Two</strong> (the number 2).<br>"
         "<strong>Its</strong> (possession: <em>the company changed its name</em>) vs. <strong>It's</strong> (contraction: <em>it is / it has</em>).<br>"
         "<strong>Hear</strong> (listen with ear) vs. <strong>Here</strong> (in this place) &bull; <strong>Buy</strong> (purchase) vs. <strong>By</strong> (near / beside / created by).<br>"
         "<strong>Passed</strong> (past tense verb: <em>passed the exam</em>) vs. <strong>Past</strong> (time / preposition: <em>walked past the library</em>)."),

        ("7. Silent Letters & Hidden Consonant Traps",
         "Many everyday functional words contain silent letters that learners easily omit when writing phonetically:<br>"
         "Silent <strong>b</strong>: <em>dou<strong>b</strong>t, de<strong>b</strong>t, com<strong>b</strong></em> &bull; Silent <strong>w</strong>: <em><strong>w</strong>rite, <strong>w</strong>rong, ans<strong>w</strong>er</em> &bull; Silent <strong>k</strong>: <em><strong>k</strong>now, <strong>k</strong>nee, <strong>k</strong>nife</em>.<br>"
         "Silent <strong>t</strong>: <em>lis<strong>t</strong>en, fas<strong>t</strong>en, cas<strong>t</strong>le</em> &bull; Silent <strong>n</strong>: <em>autum<strong>n</strong>, colum<strong>n</strong></em> &bull; Silent <strong>l</strong>: <em>hal<strong>f</strong>, ca<strong>l</strong>m, wou<strong>l</strong>d</em>.<br>"
         "Tricky calendar words: <em>Wed<strong>nes</strong>day, Fe<strong>bru</strong>ary</em> &bull; Civic terms: <em>gove<strong>rn</strong>ment, enviro<strong>nm</strong>ent</em>."),

        ("8. Prefix & Suffix Pitfalls (-ful, -ly, dis-, mis-)",
         "The suffix <strong>-ful</strong> always has only <strong>one 'l'</strong>: <em>careful, useful, helpful, grateful, beautiful, successful</em>. (Only the standalone word <em>full</em> has two).<br>"
         "When adding <em>-ly</em> to <em>-ful</em> words, use <strong>-fully</strong>: <em>carefully, successfully, helpfully</em>.<br>"
         "Prefixes <strong>dis-</strong> and <strong>mis-</strong> attach directly without removing letters: <em>disagree, disappear, disappoint (one s, two p's!), misspell (two s's!), mistake</em>.")
    ],
    "vocab_bank": [
        ("1. Workplace, Management & Professional Communication",
         ["colleague", "supervisor", "apprentice", "interview", "schedule", "experience", "equipment", "department", "employment", "punctuality", "responsibility", "correspondence", "contract", "management"]),
        ("2. Health, Safety, Welfare & Incident Reporting",
         ["incident", "emergency", "prevention", "hazard", "immediate", "injuries", "treatment", "maintenance", "first-aider", "precaution", "evacuation", "protective", "procedure", "ambulance"]),
        ("3. Community, Leisure & Civic Engagement",
         ["community", "volunteer", "activity", "committee", "facility", "neighbour", "environment", "recreation", "resident", "council", "initiative", "accessibility", "pedestrian", "gathering"]),
        ("4. Consumer Affairs, Complaints & Reviews",
         ["recommend", "advantage", "convenient", "beneficial", "disappointed", "reliable", "essential", "satisfactory", "complaint", "replacement", "refund", "delivery", "purchase", "apology"]),
        ("5. Education, Training & Apprenticeships",
         ["qualification", "assessment", "coursework", "achievement", "certificate", "attendance", "curriculum", "practical", "progress", "guidance", "assignment", "opportunity", "develop", "instructor"]),
        ("6. Analytical, Evaluative & Persuasive Terminology",
         ["positive", "negative", "improvement", "effective", "suitable", "reasonable", "crucial", "valuable", "especially", "definitely", "certainly", "although", "therefore", "consequently"])
    ],
    "spelling_test": [
        ("Which is the correct spelling for someone you work with in an office?", ["A) collegue", "B) colleague", "C) collaegue"], "B"),
        ("Which word correctly doubles the consonant under the 1-1-1 rule?", ["A) droped", "B) dropped", "C) dropt"], "B"),
        ("Choose the correct homophone: <em>'The students collected [ their / there / they're ] certificates.'</em>", ["A) their", "B) there", "C) they're"], "A"),
        ("Select the correct plural form of 'community':", ["A) communitys", "B) communities", "C) communityes"], "B"),
        ("Which word follows the 'i before e except after c' rule correctly?", ["A) recieve", "B) receive", "C) receeve"], "B"),
        ("Select the correct spelling with the single 'l' suffix:", ["A) carefull", "B) careful", "C) carful"], "B"),
        ("Which spelling correctly preserves the prefix:", ["A) dissappoint", "B) disapoint", "C) disappoint"], "C"),
        ("Choose the correct spelling with the silent letter:", ["A) enviroment", "B) environment", "C) envirament"], "B")
    ]
}

L2_SPELLING_DATA = {
    "rules": [
        ("1. The -able vs. -ible Suffix Distinction",
         "Use <strong>-able</strong> when the root is a complete English base word: <em>rely &rarr; reliable, adapt &rarr; adaptable, avoid &rarr; avoidable, accept &rarr; acceptable, manage &rarr; manageable, reason &rarr; reasonable</em>.<br>"
         "Use <strong>-ible</strong> when the root is incomplete, ends in a soft <em>c/s</em>, or derives directly from Latin: <em>audible, visible, credible, eligible, accessible, responsible, flexible, irreversible, feasible, digestible</em>."),

        ("2. The -ance vs. -ence / -ant vs. -ent Suffix System",
         "Words ending in <strong>-ance</strong> correspond to adjectives ending in <strong>-ant</strong>: <em>important &rarr; importance, distant &rarr; distance, reluctant &rarr; reluctance, arrogant &rarr; arrogance</em>.<br>"
         "Words ending in <strong>-ence</strong> correspond to adjectives ending in <strong>-ent</strong>: <em>convenient &rarr; convenience, different &rarr; difference, permanent &rarr; permanence, confident &rarr; confidence, evident &rarr; evidence</em>."),

        ("3. High-Stakes Confusable Pairs in Formal Registers",
         "<strong>Affect</strong> (verb: to influence / alter: <em>the policy affects staff</em>) vs. <strong>Effect</strong> (noun: result / consequence: <em>had a positive effect</em>; verb: to bring about: <em>effect change</em>).<br>"
         "<strong>Principal</strong> (head of college / main: <em>principal reason</em>) vs. <strong>Principle</strong> (fundamental moral rule / law: <em>matter of principle</em>).<br>"
         "<strong>Stationery</strong> (paper / pens / envelopes - remember 'e' for envelope) vs. <strong>Stationary</strong> (motionless / stopped).<br>"
         "<strong>Practice</strong> (noun: <em>medical practice / standard practice</em>) vs. <strong>Practise</strong> (verb in British English: <em>to practise skills</em>).<br>"
         "<strong>Compliment</strong> (praise / flattery) vs. <strong>Complement</strong> (to enhance / complete / balance).<br>"
         "<strong>Discrete</strong> (separate / distinct) vs. <strong>Discreet</strong> (tactful / confidential)."),

        ("4. Consonant Doubling in Multi-Syllable Verbs (The Stress Rule)",
         "Only double the final consonant if the primary stress falls on the <strong>final syllable</strong>:<br>"
         "<em>re-FER &rarr; referred / referring, oc-CUR &rarr; occurred / occurring, com-MIT &rarr; committed, pre-FER &rarr; preferred, trans-FER &rarr; transferred</em>.<br>"
         "Do <strong>NOT</strong> double if the stress is on the <strong>first syllable</strong>:<br>"
         "<em>BEN-e-fit &rarr; benefited / benefiting, TAR-get &rarr; targeted / targeting, VIS-it &rarr; visited, OF-fer &rarr; offered</em>."),

        ("5. The -ceed, -cede, and -sede Distinction",
         "Only ONE word in the English language ends in <strong>-sede</strong>: <em>supersede</em>.<br>"
         "Only THREE common words end in <strong>-ceed</strong>: <em>exceed, proceed, succeed</em>.<br>"
         "All other related words end in <strong>-cede</strong>: <em>concede, precede, recede, intercede, accede</em>."),

        ("6. Advanced Confusables & Pronoun Traps",
         "<strong>Loose</strong> (adjective: not tight / unbound) vs. <strong>Lose</strong> (verb: to misplace / be defeated).<br>"
         "<strong>Ensure</strong> (to make certain: <em>ensure safety</em>) vs. <strong>Insure</strong> (financial policy: <em>insure a vehicle</em>) vs. <strong>Assure</strong> (to tell positively: <em>assure the client</em>).<br>"
         "<strong>Weather</strong> (meteorological conditions) vs. <strong>Whether</strong> (conjunction expressing alternative / doubt).<br>"
         "<strong>Advice</strong> (noun: guidance given) vs. <strong>Advise</strong> (verb: to offer guidance)."),

        ("7. Unstressed Internal Vowels & Polysyllabic Traps",
         "Many Level 2 errors stem from slurring internal unstressed syllables:<br>"
         "<em>cat-e-go-ry</em> (never write <em>catagory</em>) &bull; <em>def-i-nite-ly</em> (never write <em>definately</em>) &bull; <em>sep-a-rate</em> (remember 'a rat' in sep-a-rate).<br>"
         "<em>ac-com-mo-da-tion</em> (two c's and two m's) &bull; <em>em-bar-rass-ment</em> (two r's and two s's) &bull; <em>nec-es-sa-ry</em> (one c, two s's).<br>"
         "<em>oc-ca-sion-al-ly</em> (two c's, one s, two l's) &bull; <em>main-te-nance</em> (from maintain, but spelled maintenance)."),

        ("8. Compound Hyphenation & Negative Prefixes",
         "Use hyphens in compound adjectives <strong>before a noun</strong>: <em>well-established protocol, high-risk strategy, state-of-the-art laboratory, long-term impact</em>.<br>"
         "Negative prefixes do not delete the root's initial letter: <em>dis + satisfied = dissatisfied, mis + spent = misspent, ir + relevant = irrelevant, il + literate = illiterate</em>.")
    ],
    "vocab_bank": [
        ("1. Executive, Governance & Professional Management",
         ["remuneration", "accountability", "feasibility", "infrastructure", "expenditure", "stakeholder", "implementation", "methodology", "strategic", "statutory", "procurement", "compliance", "delegation", "benchmark"]),
        ("2. Civic, Legal & Environmental Policy",
         ["statutory", "regulations", "consultation", "environmental", "biodiversity", "particulates", "unacceptable", "tribunal", "sustainability", "conservation", "mitigation", "congestion", "jurisdiction", "emissions"]),
        ("3. Analytical, Technical & Empirical Research",
         ["algorithm", "automation", "comprehensive", "quantitative", "qualitative", "discrepancy", "significantly", "consequently", "correlation", "statistical", "hypothesis", "empirical", "diagnostic", "verification"]),
        ("4. Evaluative, Critical & Persuasive Discourse",
         ["compelling", "unprecedented", "substantiated", "deficiencies", "invaluable", "reprehensible", "prioritised", "collaborative", "paramount", "imperative", "indispensable", "plausible", "incontrovertible", "justifiable"]),
        ("5. Vocational, Operational & Workplace Relations",
         ["appraisal", "productivity", "probationary", "grievance", "competency", "standardisation", "protocol", "operational", "facilitation", "transition", "absenteeism", "workforce", "resolution", "redundancy"]),
        ("6. Consumer Redress, Commercial & Contract Law",
         ["compensation", "contractual", "reimbursement", "liability", "repudiation", "merchantable", "indemnification", "warranty", "transaction", "restitution", "non-compliance", "breach", "correspondence", "admissible"])
    ],
    "spelling_test": [
        ("Choose the correct suffix for: <em>'The meeting room is easily [ accessable / accessible ].'</em>", ["A) accessable", "B) accessible"], "B"),
        ("Select the sentence with correct confusable usage:",
         ["A) The severe weather had a catastrophic affect on rail transport.",
          "B) The severe weather had a catastrophic effect on rail transport.",
          "C) The severe weather effected a catastrophic affect."], "B"),
        ("Which word correctly doubles the consonant under the multi-syllable stress rule?", ["A) targetted", "B) targeted", "C) targetting"], "B"),
        ("Choose the correct spelling: <em>'The college [ principle / principal ] addressed the students.'</em>", ["A) principle", "B) principal"], "B"),
        ("Select the correct spelling ending in -ceed, -cede, or -sede:", ["A) supercede", "B) supersede", "C) superceed"], "B"),
        ("Which sentence uses the correct British English verb form?",
         ["A) Candidates must practise their proofreading daily.",
          "B) Candidates must practice their proofreading daily.",
          "C) Daily practice will practise your speed."], "A"),
        ("Identify the correctly spelled word with unstressed vowels:", ["A) definately", "B) definitely", "C) defanitely"], "B"),
        ("Select the correctly hyphenated compound adjective before the noun:",
         ["A) a state of the art facility", "B) a state-of-the-art facility", "C) a state of the-art facility"], "B")
    ]
}

L1_MIXED_WORKOUT = [
    {
        "num": 1,
        "format": "Formal Letter of Complaint",
        "title": "Workout 1: Road Safety & Highway Defect Letter",
        "scenario": "A local resident drafted this letter to the council highways department. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Dear Mrs Campbell<br>
I am writing to tell you about the massive potholes outside the health clinic. Drivers swerves into oncoming traffic and its very dangerous. My elderly neighbour sliped on the loose gravel last tuesday. You should resurface the road immediately.<br>
Yours faithfully,<br>
Jordan Reed""",
        "errors": [
            "Missing comma after salutation ('Dear Mrs Campbell' &rarr; 'Dear Mrs Campbell,')",
            "Subject-verb agreement error ('Drivers swerves' &rarr; 'Drivers swerve')",
            "Missing contraction apostrophe ('its very dangerous' &rarr; 'it\\'s very dangerous')",
            "Consonant doubling spelling error ('sliped' &rarr; 'slipped')",
            "Incorrect sign-off matching ('Dear Mrs Campbell' requires 'Yours sincerely,', not 'faithfully')"
        ]
    },
    {
        "num": 2,
        "format": "Workplace Incident Report",
        "title": "Workout 2: Retail Stockroom Accident Log",
        "scenario": "A warehouse assistant recorded this safety log after a colleague slipped. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Date: 17 October 2026 | Location: Aisle 4<br>
At 11:20 AM, Mrs Davies slip on spilled cooking oil. She fall heavily and hurted her right wrist. I immediately called the first aider. Yellow warning cones was placed around the spill to prevent further accidents.<br>
Reported by: Liam Patel""",
        "errors": [
            "Tense shift in narrative ('Mrs Davies slip' &rarr; 'Mrs Davies slipped')",
            "Incorrect present tense verb ('She fall' &rarr; 'She fell')",
            "Incorrect irregular past tense ('hurted' &rarr; 'hurt')",
            "Missing hyphen in compound noun ('first aider' &rarr; 'first-aider')",
            "Subject-verb agreement error ('cones was placed' &rarr; 'cones were placed')"
        ]
    },
    {
        "num": 3,
        "format": "Community Article",
        "title": "Workout 3: Community Garden Feature Article",
        "scenario": "A volunteer wrote this article for the quarterly town newsletter. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """why you should try gardening this autumn<br>
gardening is a brilliant outdoor hobby. Last saturday, i helped plant winter vegetables at the park. It was fantastic exercise it also helped me make friends. Because fresh air is great for your mental health.<br>
By Samira Khan""",
        "errors": [
            "Missing capital letters in title ('why you should try' &rarr; 'Why You Should Try')",
            "Missing capital letter at start of sentence ('gardening is' &rarr; 'Gardening is')",
            "Missing capital letter on day and pronoun 'I' ('saturday, i helped' &rarr; 'Saturday, I helped')",
            "Run-on sentence ('exercise it also' &rarr; 'exercise. It also')",
            "Sentence fragment starting with 'Because' (link with previous sentence or add main clause)"
        ]
    },
    {
        "num": 4,
        "format": "Online Customer Feedback",
        "title": "Workout 4: Public Transport Complaint Form",
        "scenario": "A commuter submitted this complaint regarding a delayed train. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Portal: SwiftRail Claims | Booking Ref: TR-72819<br>
I am writing because my trains heating broke down in freezing weather. Its totally unacceptable and the guards explanation was unhelpful. My managers meeting was delayed as a result. I demand a full refund for my tickets price.""",
        "errors": [
            "Missing possessive apostrophe ('my trains heating' &rarr; 'my train\\'s heating')",
            "Missing contraction apostrophe ('Its totally unacceptable' &rarr; 'It\\'s totally unacceptable')",
            "Missing possessive apostrophe ('the guards explanation' &rarr; 'the guard\\'s explanation')",
            "Missing possessive apostrophe ('My managers meeting' &rarr; 'My manager\\'s meeting')",
            "Missing possessive apostrophe ('tickets price' &rarr; 'ticket\\'s price')"
        ]
    }
]

L2_MIXED_WORKOUT = [
    {
        "num": 1,
        "format": "Executive Environmental Report",
        "title": "Workout 1: Greenbelt Distribution Hub Audit",
        "scenario": "An environmental consultant prepared this audit for the council. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """2. Findings &amp; Ecological Assessment<br>
The proposed logistics facility occupies twenty-four acres of protected greenbelt land, commercial development is fundamentally inappropriate. An independent audit was conduct in September. Endangered bat species will lose there natural woodland habitats; and stormwater run-off will aggravate flood risks along the River Ouse. Mandatory environmental mitigations has not been provided.""",
        "errors": [
            "Comma splice in sentence 1 ('greenbelt land, commercial' &rarr; use semicolon: 'land; commercial')",
            "Incorrect passive past participle ('was conduct' &rarr; 'was conducted')",
            "Confused homophone ('there natural' &rarr; 'their natural')",
            "Incorrect coordination with semicolon and 'and' ('habitats; and stormwater' &rarr; remove 'and' or use comma)",
            "Subject-verb agreement error ('mitigations has not been' &rarr; 'mitigations have not been')"
        ]
    },
    {
        "num": 2,
        "format": "Official Customer Redress Submission",
        "title": "Workout 2: Airline Statutory Compensation Claim",
        "scenario": "A passenger completed this claim for SkyLink Airways. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Portal: SkyLink Customer Redress | Ref: SK-904128<br>
The abrupt cancellation of flight SL-482 had an immediate detrimental affect on two hundred passenger's travel arrangements. The aircraft remained stationery on the tarmac for three hours without air conditioning, therefore passengers endured extreme heat distress. Furthermore ground staff deserted the gate. It is my legal entitlement under CAA regulations to claim reimbursement.""",
        "errors": [
            "Confusable word error ('detrimental affect' &rarr; 'detrimental effect')",
            "Misplaced plural possessive apostrophe ('passenger\\'s' &rarr; 'passengers\\'')",
            "Confusable word error ('stationery' &rarr; 'stationary' - motionless)",
            "Comma splice before conjunctive adverb ('conditioning, therefore' &rarr; use semicolon: 'conditioning; therefore,')",
            "Missing comma after fronted adverbial ('Furthermore ground staff' &rarr; 'Furthermore, ground staff')"
        ]
    },
    {
        "num": 3,
        "format": "Workplace Policy Proposal Email",
        "title": "Workout 3: Corporate Cycle Scheme Email",
        "scenario": "A committee chair drafted this proposal to the Operations Director. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """To: m.vance@apexlogistics.co.uk | Subject: Cycle-to-Work Scheme Proposal<br>
Dear Mr Vance<br>
Our committee has recently completed a transport survey, we discovered that 45% of employees wishes to cycle to work. However staff can't store bicycles safely because the storage shed lacks secure locking racks. We would be grateful if you would consider approving this proposal, it aligns with our CSR targets.""",
        "errors": [
            "Missing comma after salutation ('Dear Mr Vance' &rarr; 'Dear Mr Vance,')",
            "Comma splice in sentence 1 ('transport survey, we discovered' &rarr; use semicolon: 'survey; we discovered')",
            "Subject-verb agreement with plural percentage ('employees wishes' &rarr; 'employees wish')",
            "Informal contraction in formal executive email ('can\\'t store' &rarr; 'cannot store')",
            "Comma splice in final sentence ('approving this proposal, it aligns' &rarr; use semicolon: 'proposal; it aligns')"
        ]
    },
    {
        "num": 4,
        "format": "Professional Learning Journal",
        "title": "Workout 4: Leadership Meeting Reflection",
        "scenario": "A vocational apprentice completed this reflective log entry. Find and correct the <strong>5 SPaG errors</strong>.",
        "text": """Leadership Learning Log | Session: Final Project Planning | Date: 28 October 2026<br>
Today I chaired our student marketing team meeting. A heated dispute erupted between Liam and Chloe regarding target demographics, it threatened our project timeline. On reflection, I should of intervened sooner to de-escalate the tension. If I had prepared an explicit agenda with allocated speaking times, the confrontation would of been avoided. In future sessions I will distribute a structured framework beforehand.""",
        "errors": [
            "Missing comma after introductory time adverbial ('Today I chaired' &rarr; 'Today, I chaired')",
            "Comma splice in sentence 2 ('target demographics, it threatened' &rarr; use semicolon: 'demographics; it threatened')",
            "Grammatical error in reflective modal ('should of intervened' &rarr; 'should have intervened')",
            "Grammatical error in third conditional ('would of been avoided' &rarr; 'would have been avoided')",
            "Missing comma after fronted prepositional phrase ('In future sessions I will' &rarr; 'In future sessions, I will')"
        ]
    }
]
