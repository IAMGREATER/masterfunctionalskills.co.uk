"""Reference data, benchmark solutions, mark schemes, glossary and index for Functional Skills English Writing suite.
Used by K.ref_pages to render condensed, black-and-white reference back matter.
"""

# Official Pearson Edexcel Band Descriptors
PEARSON_L2_BAND_DESCRIPTORS = {
    "task1_comp": [
        ("Band 4 (10–12 marks)", "Text is fully fit for purpose and audience. Register and tone are consistently sophisticated and appropriate. Information is logically sequenced with complex paragraphs and diverse discourse markers. All bullet points are comprehensively developed with rich supporting detail and justified arguments."),
        ("Band 3 (7–9 marks)", "Text is fit for purpose and audience. Tone and format are appropriate with minor lapses. Paragraphs are clear and structured with topic sentences and linking devices. All bullet points are addressed with appropriate detail and relevant supporting ideas."),
        ("Band 2 (4–6 marks)", "Text is partially fit for purpose. Register may be inconsistent or too informal. Paragraphing is attempted but ideas may wander. Bullet points are partially addressed; some points lack development or clarity."),
        ("Band 1 (1–3 marks)", "Text shows limited awareness of purpose and audience. Little or no paragraphing. Bullet points are omitted or only briefly mentioned. Meaning is frequently unclear.")
    ],
    "task1_spag": [
        ("Band 3 (7–9 marks)", "Punctuation is consistently accurate across a wide range (full stops, capital letters, commas in clauses, semicolons, colons, apostrophes). Spelling is accurate, including complex, irregular, and specialist words. Grammar is secure; complex sentences are managed with varied clauses and consistent tense."),
        ("Band 2 (4–6 marks)", "Punctuation is mostly accurate for basic sentence demarcation (full stops, capitals); some errors with commas or apostrophes. Spelling of common and everyday words is accurate; occasional errors with specialist vocabulary. Grammar is generally sound with some tense or agreement slips."),
        ("Band 1 (1–3 marks)", "Punctuation is frequently omitted or inaccurate (run-on sentences, comma splices). Frequent spelling errors hinder meaning. Grammar errors in basic subject-verb agreement and tense.")
    ],
    "task2_comp": [
        ("Band 3 (7–9 marks)", "Content is fully relevant and engaging for the specified audience. Format conventions (subject lines, bullet points, salutations) are accurately implemented. Logical structure with fluent transitions between points. All prompt requirements are thoroughly met within the target word count."),
        ("Band 2 (4–6 marks)", "Content is mostly relevant with an appropriate tone. Main format conventions are present. Paragraphs separate distinct points. Most prompt requirements are addressed with sufficient detail."),
        ("Band 1 (1–3 marks)", "Content has limited relevance or inappropriate tone. Key format markers are missing. Disorganised structure. Prompt requirements are largely ignored or superficially treated.")
    ],
    "task2_spag": [
        ("Band 3 (5–6 marks)", "High level of SPaG accuracy. Accurate complex punctuation, accurate specialist spelling, and sophisticated sentence structures."),
        ("Band 2 (3–4 marks)", "Sound SPaG accuracy. Basic punctuation secure; minor slips in complex structures or specialist spelling."),
        ("Band 1 (1–2 marks)", "Persistent SPaG errors in basic sentence boundaries, common spelling, and simple syntax.")
    ]
}

PEARSON_L1_BAND_DESCRIPTORS = {
    "task1_comp": [
        ("Band 4 (10–12 marks)", "Writing is clear, organised, and fully suited to purpose and audience. All bullet points are developed with relevant detail. Clear paragraphs with connectives (because, although, however, first, finally). Appropriate format features (addresses, dates, salutations, subject lines)."),
        ("Band 3 (7–9 marks)", "Writing communicates meaning clearly. All bullet points are covered. Basic paragraphing is used. Format features are mostly correct."),
        ("Band 2 (4–6 marks)", "Some awareness of purpose and audience. Some bullet points are covered, but points are brief. Weak paragraphing."),
        ("Band 1 (1–3 marks)", "Limited communication. Bullet points omitted. Disorganised writing with little sense of audience.")
    ],
    "task1_spag": [
        ("Band 3 (7–9 marks)", "Sentences are correctly demarcated with capital letters and full stops throughout. Commas are used in lists and simple pauses. Spelling of common words and straightforward vocabulary is accurate. Tenses are consistent."),
        ("Band 2 (4–6 marks)", "Most sentences have capital letters and full stops. Occasional spelling errors with common words. Basic grammar is generally correct."),
        ("Band 1 (1–3 marks)", "Frequent omission of capital letters and full stops. Numerous spelling mistakes make reading difficult. Grammatical errors throughout.")
    ],
    "task2_comp": [
        ("Band 3 (7–9 marks)", "Clear, effective communication tailored to the task. Format conventions followed. All bullet points developed."),
        ("Band 2 (4–6 marks)", "Adequate communication. Main format features present. Most bullet points addressed."),
        ("Band 1 (1–3 marks)", "Unclear message. Few format features. Bullet points largely missing.")
    ],
    "task2_spag": [
        ("Band 3 (5–6 marks)", "Correct sentence punctuation throughout. Accurate spelling of common and key workplace words. Good subject-verb agreement."),
        ("Band 2 (3–4 marks)", "Basic punctuation mostly correct. Minor spelling errors that do not obscure meaning."),
        ("Band 1 (1–2 marks)", "Punctuation errors in most sentences. Frequent spelling and grammatical mistakes.")
    ]
}

# SPaG Solutions
SPAG_L2_SOLUTIONS = {
    1: [
        ("1", "The delivery arrived two hours late; consequently, the frozen goods had already started to thaw.", "1", "Semicolon or period to separate independent clauses; eliminates comma splice."),
        ("2", "The morning shift completed their inventory audit; the evening shift still needs to tally the damaged stock.", "1", "Semicolon links two closely related clauses without a conjunction."),
        ("3", "Customer complaints have surged this month; therefore, the management team must review our telephone response times.", "1", "Semicolon followed by conjunctive adverb 'therefore'."),
        ("4", "All staff must attend the fire drill tomorrow. Attendance is compulsory for permanent and agency employees alike.", "1", "Separated into two distinct, well-demarcated sentences.")
    ],
    2: [
        ("1", "Although the warehouse was exceptionally busy, the dispatch team successfully met every delivery target.", "1", "Subordinating conjunction 'Although' creates complex sentence showing contrast."),
        ("2", "Agency drivers will not be permitted on site unless they have completed the mandatory safety briefing.", "1", "'Unless' establishes a clear condition."),
        ("3", "While electric vehicles require a higher initial capital investment, their long-term running costs are significantly lower.", "1", "'While' balances contrasting points in a formal register."),
        ("4", "Staff may request hybrid working, provided that they consistently maintain their weekly performance targets.", "1", "'Provided that' introduces a formal contractual condition.")
    ],
    3: [
        ("1", "A pallet of glass bottles was dropped in the loading bay due to excessive forklift speed.", "1", "Passive voice removes personal blame and focuses objectively on the incident and cause."),
        ("2", "The chemical storage cabinet was left unlocked prior to the laboratory closure.", "1", "Passive structure suitable for an official health and safety log."),
        ("3", "The mandatory inspection of the elevator cables was not conducted on Friday.", "1", "Objective compliance phrasing."),
        ("4", "Incorrect appointment times were issued to four dental patients.", "1", "Professional passive framing focusing on the systemic error.")
    ],
    4: [
        ("1", "Unless departmental laptop hardware is upgraded promptly, operational efficiency is likely to decline significantly.", "1", "Replaces hyperbolic 'department will fail' with calibrated probability."),
        ("2", "Discrepancies in the client's records suggest that payment may not have been remitted on the date claimed.", "1", "Professional diplomatic phrasing avoiding accusatory 'lying'."),
        ("3", "Installing commercial solar panels could substantially reduce our quarterly energy expenditure.", "1", "Realistic modal qualification ('could substantially reduce' rather than 'completely eliminate forever')."),
        ("4", "The proposed shift rota alterations risk causing widespread staff dissatisfaction and potential turnover.", "1", "Measured workplace risk assessment phrasing.")
    ],
    5: [
        ("1", "<b>Standardised Imperative Action List:</b><br>&bull; <b>Sound</b> the fire alarm immediately upon detecting smoke.<br>&bull; <b>Escort</b> all visitors and contractors to Assembly Point C.<br>&bull; <b>Do not re-enter</b> the premises until authorised by the Chief Fire Warden.<br>&bull; <b>Inspect</b> all restrooms and conference suites for remaining personnel.", "2", "All bullets start consistently with active imperative verbs (Sound, Escort, Do not re-enter, Inspect).")
    ],
    6: [
        ("1", "The nurses' union submitted its formal petition to the hospital director's office.", "1", "Plural possessive (nurses'), possessive pronoun (its - no apostrophe), singular possessive (director's)."),
        ("2", "All client files must be returned to the manager's desk before the day's end.", "1", "Singular possessive (manager's) and temporal possessive (day's)."),
        ("3", "The company announced its new policy regarding children's nursery vouchers.", "1", "Possessive pronoun (its) and irregular plural possessive (children's)."),
        ("4", "Both drivers' vehicles were damaged when the warehouse roof lost its guttering.", "1", "Plural possessive (drivers') and possessive pronoun (its).")
    ],
    7: [
        ("1", "At 08:30, the facility experienced an unexpected power outage. <b>Fortunately</b>, the auxiliary backup generators activated within thirty seconds; <b>consequently</b>, the IT server infrastructure sustained zero data loss. <b>However</b>, the automated packing conveyor lines shut down temporarily. <b>As a result</b>, logistics personnel were required to pack customer orders manually until mains power was fully restored.", "2", "Integrates sophisticated discourse markers (Fortunately, consequently, However, As a result) to achieve seamless coherence.")
    ],
    8: [
        ("1", "Management must investigate the excessive weekly expenditure resulting from paper consumption.", "1", "Nominalisation: 'investigate the expenditure' replaces 'look into how much money we're wasting'."),
        ("2", "Declining employee morale and perceived managerial inadequacy correlate directly with diminished workforce productivity.", "1", "Sophisticated professional register."),
        ("3", "A comprehensive trial of the updated booking portal revealed substantial navigation and functional deficiencies.", "1", "Executive critique phrasing."),
        ("4", "The department manager issued a formal reprimand concerning persistent punctuality non-compliance.", "1", "Formal administrative vocabulary.")
    ]
}

SPAG_L1_SOLUTIONS = {
    1: [
        ("1", "The new warehouse opens next Monday. All staff must wear safety boots.", "1", "Two complete sentences correctly demarcated with full stops and capital letters."),
        ("2", "Customer orders increased rapidly, but our delivery vans arrived on time.", "1", "Comma before coordinating conjunction 'but' joining two clauses."),
        ("3", "Are you available for the health and safety training session tomorrow morning?", "1", "Question mark replaces full stop."),
        ("4", "Please submit your completed timesheet to the office by 5:00 pm on Friday.", "1", "Proper noun (Friday) capitalised; sentence closed with full stop.")
    ],
    2: [
        ("1", "We ordered paper, pens, printer ink, and envelopes for the office.", "1", "Commas separate items in a list."),
        ("2", "Because the bus was delayed, I arrived ten minutes late for my shift.", "1", "Comma separates opening subordinate clause from main clause."),
        ("3", "The manager inspected the kitchen, found it spotless, and signed the audit form.", "1", "Commas separate coordinated predicate actions."),
        ("4", "If you need assistance with the till, please ask Sarah or David.", "1", "Comma after conditional clause.")
    ],
    3: [
        ("1", "I worked in the stockroom yesterday, and I will tidy the shop floor tomorrow.", "1", "Consistent past tense ('worked') and future tense ('will tidy') matching time adverbs."),
        ("2", "The supervisor checks the temperature logs every morning at eight o'clock.", "1", "Third-person singular agreement ('supervisor checks')."),
        ("3", "They were very pleased with the prompt delivery of their parcel.", "1", "Standard plural agreement ('They were' not 'They was')."),
        ("4", "We have completed the stock audit and submitted the final figures.", "1", "Present perfect construction.")
    ],
    4: [
        ("1", "The customer's coat was left in the reception area.", "1", "Singular possessive apostrophe (customer's)."),
        ("2", "It's important to lock the main entrance door before leaving.", "1", "Contraction for 'It is' (It's)."),
        ("3", "The boys' football tournament will take place on Saturday afternoon.", "1", "Plural possessive (boys')."),
        ("4", "The company updated its opening hours on the website.", "1", "Possessive pronoun (its - no apostrophe).")
    ],
    5: [
        ("1", "I enjoy working in retail <b>because</b> I like helping customers solve problems.", "1", "Causal conjunction 'because'."),
        ("2", "The computer was expensive, <b>although</b> it came with a two-year warranty.", "1", "Concessive conjunction 'although'."),
        ("3", "You can travel by train, <b>or</b> you can catch the express bus from the high street.", "1", "Alternative conjunction 'or'."),
        ("4", "First, unpack the delivery boxes. <b>Next</b>, verify the quantities against the invoice.", "1", "Sequential connective 'Next'.")
    ],
    6: [
        ("1", "Spelling corrections: <b>necessary</b>, <b>business</b>, <b>disappointed</b>, <b>environment</b>.", "1", "Correct spellings of frequently misspelt Functional Skills Level 1 words."),
        ("2", "Plural corrections: <b>companies</b> (not companys), <b>knives</b> (not knifes), <b>boxes</b> (not boxs).", "1", "Application of standard plural spelling rules (-ies, -ves, -es)."),
        ("3", "Prefix additions: <b>uncomfortable</b>, <b>disagree</b>, <b>incorrect</b>, <b>misunderstand</b>.", "1", "Correct negative prefixes (un-, dis-, in-, mis-)."),
        ("4", "Homophones: 'We went to <b>their</b> house to collect <b>two</b> parcels, but nobody was <b>there</b>.'", "1", "Correct homophone distinction (their, two, there).")
    ],
    7: [
        ("1", "<b>Informal:</b> 'I'm writing coz I wanna know when the job starts.'<br><b>Formal:</b> 'I am writing to enquire about the official start date for this position.'", "1", "Replaces slang and contractions with professional formal inquiry."),
        ("2", "<b>Informal:</b> 'The food was gross and we waited ages.'<br><b>Formal:</b> 'The meal was substandard and we experienced an unacceptable delay in service.'", "1", "Elevates vocabulary suitable for a formal customer complaint."),
        ("3", "<b>Informal:</b> 'Tell me how much the tickets cost ASAP.'<br><b>Formal:</b> 'Could you please confirm the ticket prices at your earliest convenience?'", "1", "Polite professional request phrasing."),
        ("4", "<b>Informal:</b> 'Cheers mate, see ya later.'<br><b>Formal:</b> 'Thank you for your assistance. Yours sincerely, Sam Taylor.'", "1", "Formal closing convention.")
    ],
    8: [
        ("1", "<b>Corrected Proofreading Passage (5 errors corrected):</b><br>On Tuesday morning, Mrs Patel visited the health centre to collect her prescription. <b>Unfortunately</b> [spelling], the pharmacist was in a meeting, <b>so</b> [connective] she had to wait twenty <b>minutes</b> [spelling]. The receptionist was very polite <b>and</b> [conjunction] offered her a glass of water. Mrs Patel thanked the team <b>for</b> [preposition] their assistance.", "2", "All 5 demarcation, spelling, and connective errors corrected.")
    ]
}

# Comprehensive Glossaries
GLOSSARY_L2 = [
    ("Active voice", "A sentence structure where the subject performs the action (e.g. 'The supervisor audited the records'). Compare with passive voice."),
    ("Audience", "The intended readership of a text (e.g. senior manager, local council, general public). Dictates register, tone, and vocabulary."),
    ("Byline", "A line in an article or newsletter naming the writer (e.g. 'By Alex Morgan, Community Liaison Officer')."),
    ("Cohesion", "The grammatical and lexical linking within a text that holds it together and makes ideas flow logically."),
    ("Colloquialism", "Informal, conversational language or slang (e.g. 'kids', 'gross', 'a lot of hassle'). Avoid in formal writing."),
    ("Colon", "A punctuation mark (:) used to introduce an explanation, expansion, or list of items."),
    ("Comma splice", "A serious grammatical error where two independent clauses are joined with only a comma instead of a conjunction, semicolon, or full stop."),
    ("Complex sentence", "A sentence containing one independent main clause and one or more dependent subordinate clauses."),
    ("Compound sentence", "A sentence formed by joining two independent clauses with a coordinating conjunction (FANBOYS: for, and, nor, but, or, yet, so)."),
    ("Conjunctive adverb", "An adverb that connects two clauses (e.g. 'furthermore', 'consequently', 'therefore', 'nevertheless'). Preceded by a semicolon."),
    ("Contraction", "A shortened word form using an apostrophe of omission (e.g. 'don't', 'it's'). Generally avoided in formal reports and letters."),
    ("Discourse markers", "Words or phrases that signpost the structure and direction of writing (e.g. 'In contrast', 'Furthermore', 'To summarise')."),
    ("Formal register", "A style of language characterized by standard English, complex sentences, objective tone, and absence of slang."),
    ("Format markers", "Visual and structural layout features required by specific document types (e.g. addresses, subject lines, subheadings, bullet points)."),
    ("Imperative verb", "A bossy or commanding verb used to give instructions or advice (e.g. 'Wear safety goggles', 'Submit your form')."),
    ("Incident report", "A formal, objective document detailing the chronological events, causes, impacts, and actions following a workplace accident."),
    ("Informal register", "A casual, conversational style suitable for personal emails or informal social forum posts."),
    ("Inverted commas", "Quotation marks ('...' or \"...\") used to indicate direct speech, quotations, or specialist article headlines."),
    ("Modal verb", "An auxiliary verb expressing possibility, necessity, or certainty (e.g. 'could', 'should', 'may', 'might', 'must'). Essential for professional hedging."),
    ("Nominalisation", "Transforming verbs or adjectives into abstract nouns to create a more authoritative, formal tone (e.g. 'fail' -> 'failure', 'react' -> 'reaction')."),
    ("Passive voice", "A sentence structure where the object becomes the subject and receives the action (e.g. 'The audit was conducted by the supervisor'). Promotes objectivity."),
    ("Purpose", "The primary communicative goal of writing (e.g. to inform, persuade, complain, explain, instruct, evaluate)."),
    ("Register", "The degree of formality and linguistic style adopted to suit a specific audience and context."),
    ("Rhetorical question", "A question asked for effect or emphasis without expecting an answer, used to engage readers in articles and speeches."),
    ("Salutation", "The opening greeting of a letter or email (e.g. 'Dear Mr Davies', 'Dear Sir or Madam', 'Dear Colleagues')."),
    ("Semicolon", "A punctuation mark (;) used to join two closely related independent clauses or to separate complex items in a list containing internal commas."),
    ("Sign-off", "The closing valediction of a correspondence (e.g. 'Yours sincerely' when recipient is named, 'Yours faithfully' when unnamed)."),
    ("Standard English", "The widely accepted formal dialect of English taught in education and used in professional business, law, and publishing."),
    ("Subordinate clause", "A dependent clause that adds detail to a main clause but cannot stand alone as a grammatical sentence."),
    ("Topic sentence", "The opening sentence of a paragraph that introduces its central theme or main idea.")
]

GLOSSARY_L1 = [
    ("Address", "The recipient and sender postal details placed at the top of a formal letter."),
    ("Adjective", "A describing word that gives more detail about a noun (e.g. 'cold rain', 'heavy boxes')."),
    ("Adverb", "A word that describes a verb, indicating how, when, or where an action occurs (e.g. 'quickly', 'yesterday')."),
    ("Apostrophe", "A punctuation mark (') used to show omission (don't = do not) or possession (the manager's desk)."),
    ("Article", "A piece of writing for a newspaper, magazine, or community website with a headline, subheadings, and paragraphs."),
    ("Bullet points", "Symbols used to list key facts, actions, or recommendations clearly in reports, leaflets, and emails."),
    ("Capital letter", "An uppercase letter used for the first word in a sentence, proper nouns (names, days, places), and 'I'."),
    ("Comma", "A punctuation mark (,) used to separate items in a list or mark a brief pause in a sentence."),
    ("Conjunction", "A linking word used to join words, phrases, or clauses together (e.g. 'and', 'but', 'because', 'although')."),
    ("Drafting", "Writing out your initial response using your plan before proofreading and checking."),
    ("Email", "An electronic correspondence containing recipient address, subject line, greeting, message body, and sign-off."),
    ("Exclamation mark", "A punctuation mark (!) used to express strong emotion, urgency, or warning. Use sparingly."),
    ("Formal letter", "A structured letter written to a business, landlord, or authority figure with addresses, date, and formal sign-offs."),
    ("Full stop", "A punctuation mark (.) used to mark the end of a complete statement."),
    ("Headline", "The catchy title of an article or newsletter designed to attract the reader's attention."),
    ("Leaflet", "An informational sheet using subheadings, bullet points, and helpful tips to advise or guide the reader."),
    ("Noun", "A word representing a person, place, thing, or concept (e.g. 'student', 'college', 'computer')."),
    ("Paragraph", "A distinct section of writing dealing with a single main idea, separated by a blank line."),
    ("Proofreading", "Carefully checking written work to find and correct spelling, punctuation, and grammar mistakes."),
    ("Question mark", "A punctuation mark (?) placed at the end of a sentence that asks for information."),
    ("Review", "A balanced evaluation of a service, shop, book, or product giving honest opinions and a recommendation."),
    ("Salutation", "The greeting at the start of a letter or email (e.g. 'Dear Mr Smith', 'Dear Customer Service')."),
    ("Sentence", "A group of words containing a subject and a verb that expresses a complete thought."),
    ("Sign-off", "The polite closing words of a letter or email (e.g. 'Yours sincerely', 'Kind regards')."),
    ("Subject line", "A brief heading at the top of an email summarising its main purpose."),
    ("Verb", "An action or state word (e.g. 'deliver', 'inspect', 'calculate', 'is').")
]

# Real Alphabetical Indices with verified page anchors
INDEX_L2 = [
    ("A", [("Active and passive voice", "53, 54, 82"), ("Advice leaflet format", "25–28"), ("Apostrophes of omission & possession", "59, 60, 83"), ("Article writing format", "5–8"), ("Assessment criteria & marking rubrics", "77–80")]),
    ("B", [("Band 1 to 4 marking descriptors", "77–80"), ("Bullet points & parallel syntax", "57, 58, 83"), ("Byline conventions", "5, 41")]),
    ("C", [("Cohesive discourse markers", "61, 62, 84"), ("Colons in business communication", "55, 56"), ("Comma splice elimination", "49, 50, 81"), ("Complex sentence structures", "51, 52, 82")]),
    ("D", [("Diary and reflective log format", "45–48"), ("Discursive essay & argument flow", "61, 62")]),
    ("E", [("Email (formal workplace) format", "9–12"), ("Exam timing & mark distribution (21m/15m)", "3, 65, 71")]),
    ("F", [("Feedback form (online) format", "33–36"), ("Formal letter of complaint", "13–16"), ("Forum and blog post format", "37–40")]),
    ("G", [("Glossary of writing terminology", "94–96")]),
    ("I", [("Incident report format", "17–20"), ("Index of subjects and formats", "97–99")]),
    ("M", [("Mock Examination Paper 1", "65–70"), ("Mock Examination Paper 2", "71–76"), ("Modal verbs & professional hedging", "55, 56, 82"), ("Model answers (Band 4 benchmarks)", "7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 86–93")]),
    ("N", [("Newsletter writing format", "41–44"), ("Nominalisation & executive register", "63, 64, 84")]),
    ("P", [("Paragraph structure & topic sentences", "61, 62"), ("Pre-exam candidate readiness checklist", "4, 100")]),
    ("R", [("Report writing (workplace/facilities)", "21–24"), ("Review format (evaluative)", "29–32")]),
    ("S", [("Semicolons in linked clauses", "49, 50, 81"), ("Specialist vocabulary banks", "7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47"), ("Subordinating conjunctions", "51, 52, 82")])
]

INDEX_L1 = [
    ("A", [("Advice leaflet format", "25–28"), ("Apostrophes (possession and omission)", "55, 56, 82"), ("Article format & headline", "5–8"), ("Audience and purpose awareness", "3, 4")]),
    ("B", [("Bullet points layout", "21, 25, 57"), ("Business email format", "9–12")]),
    ("C", [("Capital letters and sentence demarcation", "49, 50, 81"), ("Commas in lists and clauses", "51, 52, 81"), ("Connectives & joining words", "57, 58, 83")]),
    ("D", [("Diary / learning log format", "45–48")]),
    ("E", [("Email to manager/tutor", "9–12"), ("Exam structure (21m / 15m tasks)", "3, 65, 71")]),
    ("F", [("Feedback form format", "33–36"), ("Formal letter format & addresses", "13–16"), ("Formal vs informal register", "61, 62, 84"), ("Forum and blog post format", "37–40")]),
    ("G", [("Glossary of Level 1 writing terms", "94–96")]),
    ("I", [("Incident report format", "17–20"), ("Index of topics and formats", "97–99")]),
    ("M", [("Marking rubrics (Bands 1–4)", "77–80"), ("Mock Writing Examination 1", "65–70"), ("Mock Writing Examination 2", "71–76"), ("Model answers (benchmark exemplars)", "7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 86–93")]),
    ("N", [("Newsletter format", "41–44")]),
    ("P", [("Paragraphing rules", "57, 58"), ("Plurals spelling rules (-s, -es, -ies)", "59, 60, 83"), ("Prefixes and suffixes", "59, 60, 83"), ("Proofreading checklist", "63, 64, 84")]),
    ("R", [("Report format", "21–24"), ("Review format", "29–32")]),
    ("S", [("Spelling tips & common word lists", "59, 60, 83"), ("Subject-verb agreement & tenses", "53, 54, 82")])
]
