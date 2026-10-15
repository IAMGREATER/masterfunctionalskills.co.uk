# spag_unit_models.py
# High-pedagogy SPaG formulas, exemplar models, syntax breakdowns, repetitive practice questions,
# quick-fire reinforcement drills, and baseline diagnostic assessments for Level 1 and Level 2 SPaG Workbooks.

L1_MODELS = {
    1: {
        "formula": "<code>[Capital Letter]</code> + <code>[Subject / Who or What]</code> + <code>[Action Verb]</code> + <code>[Complete Thought]</code> + <code>[End Mark: . / ! / ?]</code>",
        "exemplar": "Every Saturday morning, enthusiastic local volunteers clean the community riverside trail to protect wildlife and encourage family recreation.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> local volunteers &bull; <span class='syntax-badge syntax-verb'>Verb:</span> clean &bull; <span class='syntax-badge syntax-conn'>Connective:</span> to protect ... and encourage &bull; <span class='syntax-badge syntax-punc'>End Punctuation:</span> full stop .",
        "extra_drill": ("Select the complete, correctly punctuated sentence suitable for an article:",
                        ["A) In our neighbourhood with many friendly neighbours.",
                         "B) In our neighbourhood, many friendly neighbours organise weekly social events.",
                         "C) In our neighbourhood, many friendly neighbours organising weekly social events?"],
                        "B"),
        "reinforce": [
            ("Fix the sentence fragment: <em>'Because our local leisure centre offers free swimming lessons.'</em>",
             "Our local leisure centre is very popular because it offers free swimming lessons."),
            ("Fix the missing capital letters and run-on: <em>'next friday i will visit leeds it is a great city.'</em>",
             "Next Friday, I will visit Leeds. It is a great city.")
        ]
    },
    2: {
        "formula": "<code>[Polite Modal: Could / Would]</code> + <code>[Subject: you]</code> + <code>[Base Verb]</code> + <code>[Workplace Request]</code> + <code>[Question Mark: ?]</code>",
        "exemplar": "Could you please confirm whether the customer service department has completed the updated fire safety training rota?",
        "breakdown": "<span class='syntax-badge syntax-conn'>Modal:</span> Could you please &bull; <span class='syntax-badge syntax-verb'>Base Verb:</span> confirm &bull; <span class='syntax-badge syntax-sub'>Singular Collective:</span> department &bull; <span class='syntax-badge syntax-verb'>Singular Verb:</span> has completed &bull; <span class='syntax-badge syntax-punc'>End Mark:</span> ?",
        "extra_drill": ("Which sentence uses correct subject-verb agreement with a collective workplace noun?",
                        ["A) The health and safety committee have approved the new warehouse guidelines.",
                         "B) The health and safety committee has approved the new warehouse guidelines.",
                         "C) The health and safety committee were approving the new warehouse guidelines."],
                        "B"),
        "reinforce": [
            ("Fix the subject-verb mismatch: <em>'Both shift supervisors was happy with your progress.'</em>",
             "Both shift supervisors were happy with your progress."),
            ("Rewrite politely using a modal verb: <em>'Send me the inventory report right now.'</em>",
             "Could you please send me the inventory report today?")
        ]
    },
    3: {
        "formula": "<code>[Salutation: Dear Title Surname,]</code> + <code>[Formal Complex Statement]</code> + <code>[Matching Sign-off: Yours sincerely,]</code>",
        "exemplar": "Dear Mrs Campbell, I am writing to formally request that the highways department inspects the hazardous road surface outside our health clinic.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Salutation Comma:</span> Dear Mrs Campbell, &bull; <span class='syntax-badge syntax-sub'>Subject:</span> I &bull; <span class='syntax-badge syntax-verb'>Formal Verb:</span> am writing to request &bull; <span class='syntax-badge syntax-conn'>Subordinate Clause:</span> that the department inspects... &bull; <span class='syntax-badge syntax-punc'>Sign-off:</span> Yours sincerely,",
        "extra_drill": ("Which formal correspondence salutation and sign-off pair is correctly matched?",
                        ["A) Dear Sir or Madam, ... Yours sincerely,",
                         "B) Dear Mr Henderson, ... Yours sincerely,",
                         "C) Dear Mrs Davies, ... Yours faithfully,"],
                        "B"),
        "reinforce": [
            ("Correct the sign-off error: <em>'Dear Sir, ... Yours sincerely,'</em>",
             "Dear Sir, ... Yours faithfully,"),
            ("Fix the comma splice in this formal letter: <em>'I received your letter, I will reply tomorrow.'</em>",
             "I received your letter. I will reply tomorrow.")
        ]
    },
    4: {
        "formula": "<code>[Lead-in Stem with Colon :]</code> + <code>[Bullet 1: Capital + Verb Clause + Full Stop .]</code> + <code>[Bullet 2: Capital + Verb Clause + Full Stop .]</code>",
        "exemplar": "The facilities audit recommends the following safety measures:<br>&bull; Install non-slip rubber flooring across all high-traffic corridors.<br>&bull; Conduct monthly emergency evacuation drills for all departmental staff.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Colon:</span> introduces list &bull; <span class='syntax-badge syntax-verb'>Parallel Imperative:</span> Install ... Conduct &bull; <span class='syntax-badge syntax-punc'>Punctuation:</span> Each bullet begins with a capital letter and ends with a full stop .",
        "extra_drill": ("Identify the bullet list that complies with Pearson report punctuation standards:",
                        ["A) • installing better lighting • repairing fire exits",
                         "B) • Install energy-efficient lighting in all classrooms. • Repair all fire exit doors immediately.",
                         "C) • Install energy-efficient lighting in all classrooms, • repair all fire exit doors immediately;"],
                        "B"),
        "reinforce": [
            ("Fix the incomplete bullet point fragment: <em>'• more recycling bins in canteen'</em>",
             "• Place additional recycling bins in the college canteen."),
            ("Correct the acronym and capitalisation: <em>'the nhs trust and the dfe published new safety advice.'</em>",
             "The NHS Trust and the DfE published new safety advice.")
        ]
    },
    5: {
        "formula": "<code>[Time Adverbial: At 14:15 on Tuesday,]</code> + <code>[Subject]</code> + <code>[Past Simple Verb]</code> + <code>[Sequential Connective: Immediately / Subsequently]</code> + <code>[Follow-up Verb]</code>",
        "exemplar": "At 09:45 on Monday, a forklift driver noticed hydraulic fluid leaking on Aisle 4, so he immediately isolated the vehicle and contacted the maintenance engineer.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Fronted Time Phrase:</span> At 09:45 on Monday, &bull; <span class='syntax-badge syntax-sub'>Subject:</span> a forklift driver &bull; <span class='syntax-badge syntax-verb'>Past Simple:</span> noticed ... isolated ... contacted &bull; <span class='syntax-badge syntax-conn'>Connective:</span> so ... immediately",
        "extra_drill": ("Which incident report entry maintains consistent past tense throughout?",
                        ["A) The worker slipped on the wet ramp, falls heavily, and bruised his wrist.",
                         "B) The worker slipped on the wet ramp, fell heavily, and bruised his wrist.",
                         "C) The worker slips on the wet ramp, fell heavily, and bruises his wrist."],
                        "B"),
        "reinforce": [
            ("Fix the tense shift: <em>'The supervisor arrived at 10:00, inspects the damage, and reported the incident.'</em>",
             "The supervisor arrived at 10:00, inspected the damage, and reported the incident."),
            ("Correct the irregular past tense form: <em>'The apprentice hurted his ankle and runned for assistance.'</em>",
             "The apprentice hurt his ankle and ran for assistance.")
        ]
    },
    6: {
        "formula": "<code>[Imperative Base Verb: Drink / Set / Create]</code> + <code>[Direct Object / Advice]</code> + <code>[Subordinate Purpose Clause: so that / to + benefit]</code>",
        "exemplar": "Organise your study materials into weekly folders so that you can find revision notes quickly before each examination.",
        "breakdown": "<span class='syntax-badge syntax-verb'>Imperative Verb:</span> Organise &bull; <span class='syntax-badge syntax-sub'>Direct Object:</span> your study materials &bull; <span class='syntax-badge syntax-conn'>Purpose Conjunction:</span> so that &bull; <span class='syntax-badge syntax-verb'>Result Clause:</span> you can find revision notes quickly",
        "extra_drill": ("Choose the imperative sentence most appropriate for an advisory health leaflet:",
                        ["A) You should probably think about drinking more water perhaps.",
                         "B) Drink at least six glasses of fresh water daily to maintain concentration and energy.",
                         "C) Drink lots of water right now or you will get very sick!!!"],
                        "B"),
        "reinforce": [
            ("Transform into an imperative sentence: <em>'You ought to create a quiet study area at home.'</em>",
             "Create a quiet study area at home to minimise distractions."),
            ("Fix the excessive exclamation marks and tone: <em>'Never forget to take regular breaks while studying!!!!'</em>",
             "Remember to take regular five-minute breaks while studying.")
        ]
    },
    7: {
        "formula": "<code>[Subject: Venue / Service]</code> + <code>[Linking Verb]</code> + <code>[Comparative / Superlative: better / more spacious / most reliable]</code> + <code>[Prepositional / Concessive Clause]</code>",
        "exemplar": "Although ticket prices are slightly higher than at the old leisure centre, the modern gymnasium facilities are far more spacious and well-maintained.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Concession Clause:</span> Although ticket prices are higher... &bull; <span class='syntax-badge syntax-sub'>Subject:</span> facilities &bull; <span class='syntax-badge syntax-verb'>Linking Verb:</span> are &bull; <span class='syntax-badge syntax-conn'>Intensified Comparative:</span> far more spacious",
        "extra_drill": ("Which sentence uses comparative and superlative adjectives correctly?",
                        ["A) This bakery is more better than the supermarket, but their cakes are the most expensivest.",
                         "B) This bakery is much better than the supermarket, but their cakes are the most expensive.",
                         "C) This bakery is best than the supermarket, but their cakes are more expensive."],
                        "B"),
        "reinforce": [
            ("Fix the double comparative: <em>'The customer lounge is more wider and more cleaner.'</em>",
             "The customer lounge is wider and cleaner."),
            ("Fix the irregular superlative error: <em>'This was the most bad meal I have ever ordered.'</em>",
             "This was the worst meal I have ever ordered.")
        ]
    },
    8: {
        "formula": "<code>[Contraction: It's = It is]</code> vs. <code>[Singular Possessive: driver's / company's]</code> vs. <code>[Plural Noun: drivers / parcels]</code>",
        "exemplar": "It's disappointing that the delivery company's parcel was damaged, and I haven't received an apology from customer support.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Contraction:</span> It's (It is) &bull; <span class='syntax-badge syntax-sub'>Singular Possessive:</span> company's parcel &bull; <span class='syntax-badge syntax-conn'>Negative Contraction:</span> haven't (have not)",
        "extra_drill": ("Which sentence uses apostrophes with 100% accuracy?",
                        ["A) It's clear that the customer's parcel was delivered to the wrong address.",
                         "B) Its clear that the customers parcel was delivered to the wrong address.",
                         "C) It's clear that the customers' parcel was delivered to the wrong address."],
                        "A"),
        "reinforce": [
            ("Remove the greengrocer's apostrophe: <em>'The café serves fresh sandwich's, cake's, and coffee's.'</em>",
             "The café serves fresh sandwiches, cakes, and coffees."),
            ("Fix the confusion between its and it's: <em>'Its obvious that the company has lost it's reputation.'</em>",
             "It's obvious that the company has lost its reputation.")
        ]
    },
    9: {
        "formula": "<code>[Independent Clause 1]</code> . + <code>[Discourse Marker: However / In addition / Furthermore,]</code> + <code>[Independent Clause 2]</code> .",
        "exemplar": "Adopting a rescue dog provides enormous companionship for families. However, prospective owners must ensure they have sufficient time for daily outdoor exercise.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Main Clause 1:</span> Adopting a rescue dog provides companionship... &bull; <span class='syntax-badge syntax-conn'>Discourse Marker:</span> However, &bull; <span class='syntax-badge syntax-sub'>Contrasting Clause 2:</span> prospective owners must ensure...",
        "extra_drill": ("Which sentence correctly punctuates the discourse marker 'however'?",
                        ["A) Cycling is fast and healthy however busy roads can be dangerous.",
                         "B) Cycling is fast and healthy. However, busy roads can be dangerous.",
                         "C) Cycling is fast and healthy, however, busy roads can be dangerous."],
                        "B"),
        "reinforce": [
            ("Fix the comma splice with a discourse marker: <em>'Solar panels reduce electricity bills, they are expensive to install initially.'</em>",
             "Solar panels reduce electricity bills. However, they are expensive to install initially."),
            ("Insert an addition connective with correct punctuation: <em>'The community centre offers free wifi it also provides warm meals.'</em>",
             "The community centre offers free wifi. In addition, it provides warm meals.")
        ]
    },
    10: {
        "formula": "<code>[Main Subject Noun]</code> , + <code>[Non-Defining Relative Clause: which / who / where + extra detail]</code> , + <code>[Main Predicate & Verb]</code> .",
        "exemplar": "Our annual charity run, which takes place in Oakwood Park next Sunday, will raise vital funds for the local children's hospice.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> Our annual charity run, &bull; <span class='syntax-badge syntax-conn'>Relative Clause:</span> which takes place in Oakwood Park next Sunday, &bull; <span class='syntax-badge syntax-verb'>Main Verb:</span> will raise &bull; <span class='syntax-badge syntax-punc'>Pair of Commas:</span> enclose extra info",
        "extra_drill": ("Select the sentence that correctly punctuates the relative clause with a pair of commas:",
                        ["A) Mrs Jenkins who has taught here for twenty years is retiring in July.",
                         "B) Mrs Jenkins, who has taught here for twenty years, is retiring in July.",
                         "C) Mrs Jenkins, who has taught here for twenty years is retiring in July."],
                        "B"),
        "reinforce": [
            ("Insert the missing pair of commas around the relative clause: <em>'The new leisure pool which opened last week has already attracted hundreds of swimmers.'</em>",
             "The new leisure pool, which opened last week, has already attracted hundreds of swimmers."),
            ("Correct the relative pronoun (who vs. which): <em>'The dedicated volunteers which collected donations were praised by the mayor.'</em>",
             "The dedicated volunteers who collected donations were praised by the mayor.")
        ]
    },
    11: {
        "formula": "<code>[Fronted Time Adverbial: Yesterday / Last week,]</code> + <code>[Capital 'I']</code> + <code>[Past Action Verb]</code> + <code>[Conjunction: and / so]</code> + <code>[Evaluative Verb: realized / learned]</code>",
        "exemplar": "During my workshop shift yesterday, I completed my first electrical diagnostic check, and I realized that I need to practise reading circuit diagrams more quickly.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Time Opener:</span> During my workshop shift yesterday, &bull; <span class='syntax-badge syntax-sub'>Capital 'I':</span> I completed &bull; <span class='syntax-badge syntax-verb'>Past Simple:</span> completed ... realized &bull; <span class='syntax-badge syntax-conn'>Future Target:</span> that I need to practise...",
        "extra_drill": ("Which reflective diary entry correctly capitalises all instances of the pronoun 'I'?",
                        ["A) When i arrived at the garage, I checked the workshop rota.",
                         "B) When I arrived at the garage, I checked the workshop rota.",
                         "C) When i arrived at the garage, i checked the workshop rota."],
                        "B"),
        "reinforce": [
            ("Fix the pronoun capitalisation in this reflective entry: <em>'yesterday, i shadow the lead technician and i learned how to service the brakes.'</em>",
             "Yesterday, I shadowed the lead technician and I learned how to service the brakes."),
            ("Fix the tense slip: <em>'I listened carefully to the customer, but I forget to take his contact details.'</em>",
             "I listened carefully to the customer, but I forgot to take his contact details.")
        ]
    }
}

L2_MODELS = {
    1: {
        "formula": "<code>[Subordinate Clause with Subordinating Conjunction: Although / While / Because]</code> , + <code>[Independent Main Clause]</code> . OR <code>[Independent Clause 1]</code> ; + <code>[Independent Clause 2]</code> .",
        "exemplar": "While digital shopping platforms offer undeniable speed and doorstep convenience, brick-and-mortar retailers foster irreplaceable human connections; therefore, municipal councils must invest in vibrant high street amenities.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Subordinate Clause:</span> While digital shopping platforms offer... &bull; <span class='syntax-badge syntax-punc'>Comma:</span> separates clauses &bull; <span class='syntax-badge syntax-sub'>Main Clause 1:</span> brick-and-mortar retailers foster... &bull; <span class='syntax-badge syntax-punc'>Semicolon &amp; Conjunctive Adverb:</span> ; therefore, &bull; <span class='syntax-badge syntax-verb'>Result Clause</span>",
        "extra_drill": ("Select the sentence that successfully eliminates the comma splice using advanced punctuation:",
                        ["A) Hybrid working offers greater flexibility, many employees report feeling isolated.",
                         "B) Hybrid working offers greater flexibility; however, many employees report feeling isolated.",
                         "C) Hybrid working offers greater flexibility, however, many employees report feeling isolated."],
                        "B"),
        "reinforce": [
            ("Eliminate the comma splice using a semicolon: <em>'The sales team exceeded their quarterly targets, the operations division struggled with staffing.'</em>",
             "The sales team exceeded their quarterly targets; the operations division struggled with staffing."),
            ("Subordinate the first clause with 'Although': <em>'Electric vehicles reduce carbon emissions, their high initial purchase cost deters many buyers.'</em>",
             "Although electric vehicles reduce carbon emissions, their high initial purchase cost deters many buyers.")
        ]
    },
    2: {
        "formula": "<code>[Participial / Present Perfect Frame: Having reviewed...]</code> + <code>[Formal Purpose Statement: I am writing to formally propose...]</code> + <code>[Inversion / Conditional Clause: Should the executive board approve...]</code>",
        "exemplar": "Having reviewed the recent staff retention figures with senior department heads, I am writing to formally propose a structured leadership mentoring programme starting next quarter. Should the executive board approve this allocation, I would be delighted to coordinate the pilot workshops.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Participial Opener:</span> Having reviewed... &bull; <span class='syntax-badge syntax-verb'>Formal Verb:</span> am writing to formally propose &bull; <span class='syntax-badge syntax-sub'>Formal Inversion:</span> Should the executive board approve... &bull; <span class='syntax-badge syntax-verb'>Conditional Modal:</span> would be delighted",
        "extra_drill": ("Which sentence demonstrates correct tense consistency and formal subordination in an executive proposal?",
                        ["A) Having completed the survey, the data indicates that staff morale was low.",
                         "B) Having analysed the survey responses, we established that employee satisfaction has increased significantly.",
                         "C) Having analyse the survey responses, we establish that employee satisfaction had increased."],
                        "B"),
        "reinforce": [
            ("Fix the dangling modifier: <em>'Having reviewed the audit, several discrepancies were noticed by the accountant.'</em>",
             "Having reviewed the audit, the accountant noticed several discrepancies."),
            ("Elevate register using conditional inversion ('Should you...'): <em>'If you require further information, please contact my office.'</em>",
             "Should you require further information, please do not hesitate to contact my office.")
        ]
    },
    3: {
        "formula": "<code>[Independent Clause 1: General Principle]</code> : + <code>[Independent Clause 2: Specific Amplification]</code> ; + <code>[Conjunctive Adverb: Furthermore / Consequently ,]</code> + <code>[Result Clause]</code>",
        "exemplar": "The hospitality provided during our corporate retreat was wholly unacceptable: air conditioning units failed during peak afternoon temperatures; furthermore, hotel management declined to offer alternative accommodations or statutory compensation.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Main Assertion:</span> The hospitality provided was unacceptable &bull; <span class='syntax-badge syntax-punc'>Colon:</span> introduces direct evidence &bull; <span class='syntax-badge syntax-verb'>Evidence Clause:</span> air conditioning failed... &bull; <span class='syntax-badge syntax-punc'>Semicolon:</span> links independent clauses &bull; <span class='syntax-badge syntax-conn'>Furthermore,</span>",
        "extra_drill": ("Identify the formal sentence that uses colons and semicolons with strict grammatical accuracy:",
                        ["A) The board identified two primary concerns: rising energy tariffs and freight bottlenecks; consequently, capital expenditure has been paused.",
                         "B) The board identified two primary concerns; rising energy tariffs and freight bottlenecks: consequently, capital expenditure has been paused.",
                         "C) The board identified two primary concerns, rising energy tariffs and freight bottlenecks; consequently capital expenditure has been paused."],
                        "A"),
        "reinforce": [
            ("Use a colon to introduce an explanation: <em>'The construction project has been halted for one primary reason the contractor failed to secure environmental permits.'</em>",
             "The construction project has been halted for one primary reason: the contractor failed to secure environmental permits."),
            ("Link these two related sentences with a semicolon: <em>'The initial consultation phase has concluded. The executive committee will publish its findings on Friday.'</em>",
             "The initial consultation phase has concluded; the executive committee will publish its findings on Friday.")
        ]
    },
    4: {
        "formula": "<code>[Formal Passive Subject]</code> + <code>[Auxiliary: was / were / has been / have been]</code> + <code>[Past Participle]</code> + <code>[Objective Context / Agent Prepositional Phrase]</code>",
        "exemplar": "A comprehensive spatial audit of collegiate facilities was conducted during peak afternoon attendance hours, during which it was determined that 84% of independent study workstations were continuously occupied.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Passive Subject:</span> A spatial audit &bull; <span class='syntax-badge syntax-verb'>Passive Verb:</span> was conducted ... it was determined &bull; <span class='syntax-badge syntax-conn'>Relative Prepositional Phrase:</span> during which... &bull; <span class='syntax-badge syntax-verb'>State:</span> were continuously occupied",
        "extra_drill": ("Which sentence demonstrates correct passive voice suitable for an executive report?",
                        ["A) We inspected all warehouse fire doors and we found several severe safety defects.",
                         "B) All warehouse fire doors were thoroughly inspected, and several severe safety defects were identified.",
                         "C) All warehouse fire doors were thoroughly inspecting, and several severe safety defects had found."],
                        "B"),
        "reinforce": [
            ("Convert this active sentence into the objective passive voice: <em>'The safety inspector examined the machinery yesterday.'</em>",
             "The machinery was thoroughly examined by the safety inspector yesterday."),
            ("Remove informal first-person phrasing from this report finding: <em>'I think that the company should modernise its IT infrastructure.'</em>",
             "It is recommended that the company's IT infrastructure be modernised immediately.")
        ]
    },
    5: {
        "formula": "<code>[Fronted Prepositional Time/Cause Phrase]</code> , + <code>[Passive Core Incident Statement]</code> ; + <code>[Conjunctive Adverb: consequently / as a result ,]</code> + <code>[Remedial Action Clause]</code>",
        "exemplar": "At approximately 11:20 on Thursday, a hydraulic line ruptured on Forklift 3 due to severe seal degradation; consequently, five litres of fluid were discharged across Bay 4 before containment booms were deployed.",
        "breakdown": "<span class='syntax-badge syntax-punc'>Time/Cause Phrase:</span> At approximately 11:20 ... due to seal degradation &bull; <span class='syntax-badge syntax-sub'>Main Incident:</span> a hydraulic line ruptured &bull; <span class='syntax-badge syntax-punc'>Semicolon:</span> ; consequently, &bull; <span class='syntax-badge syntax-verb'>Passive Result:</span> five litres were discharged... were deployed",
        "extra_drill": ("Which sentence accurately expresses cause-and-effect in an official incident log?",
                        ["A) Owing to severe water ingress, the main switchgear tripped; consequently, factory operations were suspended.",
                         "B) Owing to severe water ingress the main switchgear tripped, consequently factory operations were suspended.",
                         "C) Owing to severe water ingress, the main switchgear tripped, factory operations were suspended."],
                        "A"),
        "reinforce": [
            ("Fix the run-on with a cause-and-effect connective: <em>'The conveyor belt snapped operations ceased immediately.'</em>",
             "The conveyor belt snapped; as a result, warehouse operations ceased immediately."),
            ("Correct the chronological prepositional phrasing: <em>'Prior of the explosion, no warning alarms had sounded.'</em>",
             "Prior to the incident, no warning alarms had sounded.")
        ]
    },
    6: {
        "formula": "<code>[Modal Auxiliary of Obligation: must / should / ought to]</code> + <code>[Bare Infinitive]</code> + <code>[Compound Adjective with Hyphen before Noun: evidence-based / cost-effective]</code>",
        "exemplar": "To protect their financial well-being, young adults must establish disciplined, long-term saving habits and seek independent, fee-free debt advice before signing credit agreements.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Infinitive Purpose:</span> To protect... &bull; <span class='syntax-badge syntax-sub'>Subject:</span> young adults &bull; <span class='syntax-badge syntax-verb'>Modal of Obligation:</span> must establish &bull; <span class='syntax-badge syntax-punc'>Hyphenated Compound:</span> long-term saving habits ... fee-free debt advice",
        "extra_drill": ("Choose the sentence that correctly punctuates compound adjectives before a noun in an advisory leaflet:",
                        ["A) Apprentices should adopt a well organised, forward looking approach to professional development.",
                         "B) Apprentices should adopt a well-organised, forward-looking approach to professional development.",
                         "C) Apprentices should adopt a well-organised, forward-looking-approach to professional development."],
                        "B"),
        "reinforce": [
            ("Hyphenate the compound adjective modifying the noun: <em>'The council introduced a state of the art recycling facility.'</em>",
             "The council introduced a state-of-the-art recycling facility."),
            ("Upgrade this informal advice into professional modal obligation: <em>'You better not spend all your money at once.'</em>",
             "Individuals should avoid expending all discretionary income simultaneously.")
        ]
    },
    7: {
        "formula": "<code>[Evaluative Clause with Intensified Adverb]</code> + <code>[Parenthetical Clarification in Brackets ( ... ) or Dashes &mdash; ... &mdash;]</code> + <code>[Comparative Synthesis]</code>",
        "exemplar": "The newly commissioned community health centre is exceptionally well-resourced (boasting twelve fully equipped consultation suites), representing a vastly superior clinical environment to the antiquated municipal clinic it replaced.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> community health centre &bull; <span class='syntax-badge syntax-conn'>Adverb of Degree:</span> exceptionally well-resourced &bull; <span class='syntax-badge syntax-punc'>Parenthesis:</span> (boasting twelve suites) &bull; <span class='syntax-badge syntax-verb'>Participial Evaluation:</span> representing a vastly superior clinical environment...",
        "extra_drill": ("Select the evaluative sentence that employs parenthesis and modifiers with high formal precision:",
                        ["A) The dining room—despite having undergone extensive refurbishment—remains uncomfortably draughty and poorly illuminated.",
                         "B) The dining room, despite having undergone extensive refurbishment remains uncomfortably draughty and poorly illuminated.",
                         "C) The dining room (despite having undergone extensive refurbishment remains uncomfortably draughty."],
                        "A"),
        "reinforce": [
            ("Insert parenthetical dashes around the non-essential descriptive detail: <em>'The acoustic quality in the auditorium notably during orchestral performances is peerless.'</em>",
             "The acoustic quality in the auditorium—notably during orchestral performances—is peerless."),
            ("Enhance this evaluative claim with an adverb of degree: <em>'The customer service was disappointing.'</em>",
             "The customer service was profoundly disappointing and unacceptable.")
        ]
    },
    8: {
        "formula": "<code>[Plural Noun ending in -s]</code> + <code>[Apostrophe AFTER the -s: passengers' / consumers']</code> + <code>[Correct Confusable Pair: affect vs. effect / stationary vs. stationery]</code>",
        "exemplar": "The abrupt suspension of regional commuter services had a catastrophic effect on two hundred passengers' daily working arrangements, leaving commuters stranded on stationary trains.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> suspension of services &bull; <span class='syntax-badge syntax-verb'>Correct Noun:</span> effect &bull; <span class='syntax-badge syntax-punc'>Plural Possessive:</span> passengers' daily arrangements &bull; <span class='syntax-badge syntax-conn'>Correct Adjective:</span> stationary (motionless)",
        "extra_drill": ("Which sentence demonstrates flawless plural possessive apostrophe placement and confusable word choice?",
                        ["A) The severe delays had a detrimental affect on all ten client's schedules.",
                         "B) The severe delays had a detrimental effect on all ten clients' schedules.",
                         "C) The severe delays had a detrimental affect on all ten clients' schedules."],
                        "B"),
        "reinforce": [
            ("Place the apostrophe correctly for plural possession: <em>'The five tenants deposits were withheld unfairly by the landlord.'</em>",
             "The five tenants' deposits were withheld unfairly by the landlord."),
            ("Correct the confusable pair: <em>'The unexpected policy change will severely effect staff morale.'</em>",
             "The unexpected policy change will severely affect staff morale.")
        ]
    },
    9: {
        "formula": "<code>[Subordinate Concession Clause: While / Although...]</code> , + <code>[Independent Counter-Assertion]</code> ; + <code>[Emphatic Synthesis with Dash &mdash; / Colon :]</code>",
        "exemplar": "While municipal authorities understandably prioritise commercial urban expansion, historical conservation must not be compromised; indeed, safeguarding architectural heritage remains a community's foremost cultural responsibility.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Concession:</span> While authorities prioritise... &bull; <span class='syntax-badge syntax-sub'>Main Assertion:</span> conservation must not be compromised &bull; <span class='syntax-badge syntax-punc'>Semicolon:</span> ; indeed, &bull; <span class='syntax-badge syntax-verb'>Synthesis:</span> safeguarding heritage remains...",
        "extra_drill": ("Which debate statement effectively integrates a concession clause and formal transitional punctuation?",
                        ["A) Although remote instruction democratises access to educational materials, it undeniably dilutes collaborative classroom dynamics; therefore, institutions should adopt hybrid models.",
                         "B) Although remote instruction democratises access to educational materials it undeniably dilutes collaborative classroom dynamics, therefore institutions should adopt hybrid models.",
                         "C) Although remote instruction democratises access, it dilutes dynamics, institutions should adopt hybrid models."],
                        "A"),
        "reinforce": [
            ("Introduce the opposing view with a concession clause starting with 'Whereas': <em>'Older generations prefer paper bank statements. Younger consumers rely exclusively on mobile banking apps.'</em>",
             "Whereas older generations frequently prefer paper bank statements, younger consumers rely almost exclusively on mobile applications."),
            ("Punctuate the debate transition: <em>'Public subsidies for electric cars are popular however their long term sustainability is questionable.'</em>",
             "Public subsidies for electric cars are popular; however, their long-term sustainability remains questionable.")
        ]
    },
    10: {
        "formula": "<code>[Subject Noun]</code> , + <code>[Appositive Noun Phrase / Non-Finite Participial Clause]</code> , + <code>[Main Verb & Predicate]</code>",
        "exemplar": "Dr Eleanor Vance, a distinguished environmental toxicologist from Leeds University, presented compelling empirical evidence demonstrating that local atmospheric particulate levels have breached statutory thresholds.",
        "breakdown": "<span class='syntax-badge syntax-sub'>Subject:</span> Dr Eleanor Vance, &bull; <span class='syntax-badge syntax-conn'>Appositive Phrase:</span> a distinguished environmental toxicologist... &bull; <span class='syntax-badge syntax-punc'>Pair of Commas:</span> enclose apposition &bull; <span class='syntax-badge syntax-verb'>Main Predicate:</span> presented compelling evidence...",
        "extra_drill": ("Identify the sentence that correctly punctuates an embedded appositive noun phrase:",
                        ["A) Marcus Thorne the newly appointed managing director has initiated a corporate restructuring programme.",
                         "B) Marcus Thorne, the newly appointed managing director, has initiated a corporate restructuring programme.",
                         "C) Marcus Thorne, the newly appointed managing director has initiated a corporate restructuring programme."],
                        "B"),
        "reinforce": [
            ("Insert commas to enclose the appositive phrase: <em>'The River Ouse an essential migratory corridor for Atlantic salmon requires comprehensive ecological protection.'</em>",
             "The River Ouse, an essential migratory corridor for Atlantic salmon, requires comprehensive ecological protection."),
            ("Combine into a single sentence using a participial opener ('Recognising...'): <em>'The trustees recognised the urgent need for expansion. They authorised a £2m fundraising campaign.'</em>",
             "Recognising the urgent need for collegiate expansion, the trustees authorised a £2m fundraising campaign.")
        ]
    },
    11: {
        "formula": "<code>[Third Conditional: If + Subject + had + Past Participle]</code> , + <code>[Subject + would have / could have + Past Participle]</code> ; + <code>[Target: In future, I will...]</code>",
        "exemplar": "If I had established an explicit meeting agenda with allocated time boundaries beforehand, the inter-departmental conflict would have been averted; consequently, in future sessions, I will distribute structured discussion frameworks in advance.",
        "breakdown": "<span class='syntax-badge syntax-conn'>Hypothetical Past (Condition):</span> If I had established... &bull; <span class='syntax-badge syntax-verb'>Past Result:</span> conflict would have been averted &bull; <span class='syntax-badge syntax-punc'>Semicolon:</span> ; consequently, &bull; <span class='syntax-badge syntax-sub'>Action Target:</span> in future sessions, I will distribute...",
        "extra_drill": ("Which reflective sentence uses the third conditional with strict grammatical accuracy?",
                        ["A) If I would have reviewed the technical manual, I wouldn't of made the error.",
                         "B) If I had reviewed the technical specifications, I would have avoided the assembly error.",
                         "C) If I had reviewed the technical specifications, I would of avoided the assembly error."],
                        "B"),
        "reinforce": [
            ("Correct the grammatical slip in this reflective modal: <em>'I should of verified the client's billing address before dispatching the invoice.'</em>",
             "I should have verified the client's billing address before dispatching the invoice."),
            ("Formulate a correct third conditional sentence from these notes: <em>'not double-check figures / report contain errors'</em>",
             "If I had double-checked the financial figures, the quarterly report would not have contained discrepancies.")
        ]
    }
}

L1_DIAGNOSTIC = [
    ("Sentence Boundaries:", "Identify the option that forms a complete, correctly punctuated grammatical sentence:",
     ["A) Because the train was delayed by twenty minutes this morning.",
      "B) The train was delayed by twenty minutes this morning, so we arrived late for work.",
      "C) Delaying the morning train by twenty minutes on the track."],
     "B"),
    ("Capitalisation Rules:", "Which sentence capitalises all proper nouns, days, and the pronoun 'I' with 100% accuracy?",
     ["A) Every tuesday, i travel to birmingham with dr smith to visit our regional branch.",
      "B) Every Tuesday, I travel to Birmingham with Dr Smith to visit our regional branch.",
      "C) Every Tuesday, I travel to Birmingham with dr Smith to visit our regional branch."],
     "B"),
    ("Subject-Verb Agreement:", "Select the sentence with correct subject-verb agreement for a plural subject:",
     ["A) Both shift supervisors was extremely pleased with the apprentice's progress.",
      "B) Both shift supervisors were extremely pleased with the apprentice's progress.",
      "C) Both shift supervisors is extremely pleased with the apprentice's progress."],
     "B"),
    ("Homophone Precision:", "Choose the sentence that uses the possessive homophone 'their' correctly:",
     ["A) All volunteers must submit there timesheets before Friday afternoon.",
      "B) All volunteers must submit their timesheets before Friday afternoon.",
      "C) All volunteers must submit they're timesheets before Friday afternoon."],
     "B"),
    ("Apostrophe Control:", "Which sentence uses the apostrophe of possession correctly without creating a plural error?",
     ["A) The customers complaint was investigated by the store's general manager.",
      "B) The customer's complaint was investigated by the store's general manager.",
      "C) The customers's complaint was investigated by the stores general manager."],
     "B")
]

L2_DIAGNOSTIC = [
    ("Comma Splice Elimination:", "Identify the sentence that correctly coordinates two independent clauses without a comma splice:",
     ["A) Commercial rents increased sharply last year, many local businesses were forced to relocate.",
      "B) Commercial rents increased sharply last year; consequently, many local businesses were forced to relocate.",
      "C) Commercial rents increased sharply last year, consequently, many local businesses were forced to relocate."],
     "B"),
    ("High-Stakes Confusables:", "Choose the sentence that uses 'affect' and 'effect' with complete grammatical precision:",
     ["A) The unprecedented supply chain disruptions had a catastrophic affect on quarterly revenue.",
      "B) The unprecedented supply chain disruptions had a catastrophic effect on quarterly revenue.",
      "C) The supply chain disruptions effected staff morale by creating a negative affect."],
     "B"),
    ("Plural Possessive Apostrophes:", "Select the sentence that places the plural possessive apostrophe correctly after the plural 's':",
     ["A) The airline ignored two hundred passenger's statutory compensation claims.",
      "B) The airline ignored two hundred passengers' statutory compensation claims.",
      "C) The airline ignored two hundred passengers's statutory compensation claims."],
     "B"),
    ("Executive Passive Voice:", "Which sentence maintains objective formal passive construction without agent ambiguity?",
     ["A) All fire exit mechanisms were thoroughly examined, and several severe defects were documented.",
      "B) We thoroughly examined all fire exit mechanisms and we found several defects.",
      "C) All fire exit mechanisms were thoroughly examining by our team during yesterday."],
     "A"),
    ("Advanced Conditional Register:", "Identify the grammatically flawless third conditional construction:",
     ["A) If the safety director would have intervened sooner, the chemical spill would of been averted.",
      "B) Had the safety director intervened sooner, the chemical spill would have been averted.",
      "C) If the safety director intervened sooner, the chemical spill would of been averted."],
     "B")
]
