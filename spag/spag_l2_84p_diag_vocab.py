"""
spag_l2_84p_diag_vocab.py
Comprehensive Educational Content for Level 2 SPaG Mastery:
1. 40 Tagged Baseline Diagnostic Assessment Questions (Pages 3 to 6)
2. 6 Vocabulary in Use Master Modules (Pages 59 to 64)
3. 6 Murphy-Style Mixed Additional Workouts (Pages 65 to 70)
Strictly 100% Dyslexia-Friendly, Authentic UK Workplace Contexts, Zero Placeholders.
"""

# =============================================================================
# 40 TAGGED BASELINE DIAGNOSTIC ASSESSMENT QUESTIONS (Pages 3 to 6)
# =============================================================================

DIAGNOSTIC_QUESTIONS = [
    # PAGE 3: QUESTIONS 1 TO 10
    {
        "num": 1,
        "routes_to": 1,
        "topic": "Unit 1: Sentence Boundaries",
        "prompt": "Identify the sentence that correctly resolves the sentence fragment:",
        "options": [
            "A) Because the health and safety inspector identified severe damp in the basement.",
            "B) Because the health and safety inspector identified severe damp in the basement, remedial waterproofing was scheduled.",
            "C) The health and safety inspector identifying severe damp in the basement.",
            "D) Identified severe damp in the basement on Wednesday morning."
        ],
        "correct": "B",
        "rationale": "Option B joins the dependent clause introduced by 'Because' to a complete independent clause with a subject ('remedial waterproofing') and finite verb ('was scheduled'). Options A, C, and D are fragments."
    },
    {
        "num": 2,
        "routes_to": 2,
        "topic": "Unit 2: Comma Splices",
        "prompt": "Which sentence correctly repairs the comma splice between two independent clauses?",
        "options": [
            "A) The quarterly sales target was achieved, the director authorized bonuses.",
            "B) The quarterly sales target was achieved; consequently, the director authorized bonuses.",
            "C) The quarterly sales target was achieved, consequently the director authorized bonuses.",
            "D) The quarterly sales target was achieved, but however bonuses were authorized."
        ],
        "correct": "B",
        "rationale": "Option B links the two independent clauses with a semicolon and conjunctive adverb ('consequently') followed by a comma. Option A is a comma splice; Option C lacks a semicolon."
    },
    {
        "num": 3,
        "routes_to": 3,
        "topic": "Unit 3: Coordinating Conjunctions (FANBOYS)",
        "prompt": "Select the sentence with accurate comma placement before a coordinating conjunction:",
        "options": [
            "A) The technician calibrated the sensor and, reset the digital telemetry log.",
            "B) The technician calibrated the sensor, and reset the digital telemetry log.",
            "C) The technician calibrated the sensor, and she reset the digital telemetry log.",
            "D) The technician calibrated the sensor and she reset, the digital telemetry log."
        ],
        "correct": "C",
        "rationale": "Option C correctly places a comma before 'and' because a complete second independent clause with its own subject ('she') follows. Option B has a compound predicate without a second subject."
    },
    {
        "num": 4,
        "routes_to": 4,
        "topic": "Unit 4: Fronted Adverbials",
        "prompt": "Which sentence correctly punctuates the fronted subordinate clause?",
        "options": [
            "A) Although the fire alarm sounded three times none of the staff evacuated.",
            "B) Although the fire alarm sounded three times, none of the staff evacuated.",
            "C) Although, the fire alarm sounded three times none of the staff evacuated.",
            "D) Although the fire alarm sounded three times none of the staff, evacuated."
        ],
        "correct": "B",
        "rationale": "A fronted subordinate clause ('Although the fire alarm sounded three times') must be separated from the main clause by a comma."
    },
    {
        "num": 5,
        "routes_to": 5,
        "topic": "Unit 5: Parenthesis & Non-Essential Clauses",
        "prompt": "Choose the sentence with correct parenthetical comma punctuation:",
        "options": [
            "A) Mr Davies, who manages regional distribution will lead the briefing.",
            "B) Mr Davies who manages regional distribution, will lead the briefing.",
            "C) Mr Davies, who manages regional distribution, will lead the briefing.",
            "D) Mr Davies who manages regional distribution will lead the briefing."
        ],
        "correct": "C",
        "rationale": "Parenthetical non-essential clauses require a pair of commas: one before ('Mr Davies,') and one after ('distribution,')."
    },
    {
        "num": 6,
        "routes_to": 6,
        "topic": "Unit 6: Semicolons",
        "prompt": "Identify the sentence that correctly employs a semicolon to join independent clauses:",
        "options": [
            "A) The audit was completed early; because the documents were pre-sorted.",
            "B) The audit was completed early; the compliance team submitted their report by noon.",
            "C) The audit was completed early; including the finance records.",
            "D) The audit was completed early; and the compliance team was pleased."
        ],
        "correct": "B",
        "rationale": "A semicolon must connect two independent clauses capable of standing alone as complete sentences. In A and C, the second part is a dependent fragment."
    },
    {
        "num": 7,
        "routes_to": 7,
        "topic": "Unit 7: Colons",
        "prompt": "Select the sentence where a colon is correctly introduced by a complete independent clause:",
        "options": [
            "A) The new safety policy requires: steel-toed boots, high-vis vests, and hard hats.",
            "B) All site operatives must wear the following items: steel-toed boots, high-vis vests, and hard hats.",
            "C) The mandatory items include: steel-toed boots, high-vis vests, and hard hats.",
            "D) Mandatory PPE items are: steel-toed boots, high-vis vests, and hard hats."
        ],
        "correct": "B",
        "rationale": "The clause preceding a colon must stand alone as a complete sentence ('All site operatives must wear the following items'). Colons must never follow linking verbs like 'requires:', 'include:', or 'are:'."
    },
    {
        "num": 8,
        "routes_to": 8,
        "topic": "Unit 8: Dashes & Brackets",
        "prompt": "Which sentence correctly encloses supplementary technical information in brackets?",
        "options": [
            "A) The Health and Safety Executive HSE published new guidance (in 2026).",
            "B) The Health and Safety Executive (HSE) published new guidance in October 2026.",
            "C) The Health and Safety Executive &mdash; HSE) published new guidance in 2026.",
            "D) The Health and Safety Executive (HSE published new guidance in 2026)."
        ],
        "correct": "B",
        "rationale": "Round brackets (parentheses) correctly enclose acronym definitions immediately following the full term."
    },
    {
        "num": 9,
        "routes_to": 9,
        "topic": "Unit 9: Hyphens",
        "prompt": "Identify the sentence that correctly hyphenates the compound adjective before a noun:",
        "options": [
            "A) The company recruited a highly-skilled electrical technician.",
            "B) The company recruited a highly skilled electrical technician for a full-time role.",
            "C) The company recruited a highly skilled electrical technician for a full time role.",
            "D) The role is full-time and highly-skilled."
        ],
        "correct": "B",
        "rationale": "Adverbs ending in -ly ('highly') never take a hyphen, while compound adjectives placed directly before a noun ('full-time role') must be hyphenated."
    },
    {
        "num": 10,
        "routes_to": 10,
        "topic": "Unit 10: Apostrophes of Omission",
        "prompt": "Choose the sentence that correctly spells the contraction of 'does not':",
        "options": [
            "A) The commercial vehicle dose'nt require immediate servicing.",
            "B) The commercial vehicle doesn't require immediate servicing.",
            "C) The commercial vehicle does'nt require immediate servicing.",
            "D) The commercial vehicle dosent require immediate servicing."
        ],
        "correct": "B",
        "rationale": "The apostrophe replaces the omitted letter 'o' in 'not', so it must sit precisely between the 'n' and 't' ('doesn't')."
    },

    # PAGE 4: QUESTIONS 11 TO 20
    {
        "num": 11,
        "routes_to": 11,
        "topic": "Unit 11: Apostrophes of Possession",
        "prompt": "Select the sentence with 100% accurate possessive apostrophes for singular and plural nouns:",
        "options": [
            "A) The manager's office overlooks the employees' car park.",
            "B) The managers' office overlooks the employee's car park.",
            "C) The managers office overlooks the employees' car park.",
            "D) The manager's office overlooks the employees car park."
        ],
        "correct": "A",
        "rationale": "Singular manager ('manager's') and plural employees ('employees'') both correctly demonstrate standard possessive rules."
    },
    {
        "num": 12,
        "routes_to": 12,
        "topic": "Unit 12: Its vs It's",
        "prompt": "Choose the sentence that correctly uses both 'its' and 'it's':",
        "options": [
            "A) Its obvious that the machine has reached the end of it's operational life.",
            "B) It's obvious that the machine has reached the end of its operational life.",
            "C) It's obvious that the machine has reached the end of it's operational life.",
            "D) Its obvious that the machine has reached the end of its operational life."
        ],
        "correct": "B",
        "rationale": "'It's' = 'It is' (contraction); 'its' = belonging to it (possessive pronoun). Replace mentally: 'It is obvious... end of its life'."
    },
    {
        "num": 13,
        "routes_to": 13,
        "topic": "Unit 13: Past Simple vs Present Perfect",
        "prompt": "Identify the sentence that correctly uses the Past Simple with a specific past time anchor:",
        "options": [
            "A) The electrical engineer has inspected the circuit breakers yesterday morning.",
            "B) The electrical engineer inspected the circuit breakers yesterday morning.",
            "C) The electrical engineer inspects the circuit breakers yesterday morning.",
            "D) The electrical engineer was inspected the circuit breakers yesterday morning."
        ],
        "correct": "B",
        "rationale": "When a specific finished time is stated ('yesterday morning'), the Past Simple ('inspected') must be used, not the Present Perfect ('has inspected')."
    },
    {
        "num": 14,
        "routes_to": 14,
        "topic": "Unit 14: Past Continuous",
        "prompt": "Which sentence correctly combines the Past Continuous background action with a Past Simple interruption?",
        "options": [
            "A) While the operative was cleaning the conveyor, the safety sensor tripped.",
            "B) While the operative cleaned the conveyor, the safety sensor was tripping.",
            "C) While the operative was cleaning the conveyor, the safety sensor trips.",
            "D) The operative cleaned the conveyor while the safety sensor was tripped."
        ],
        "correct": "A",
        "rationale": "The ongoing background action in progress uses the Past Continuous ('was cleaning'), while the sudden event uses the Past Simple ('tripped')."
    },
    {
        "num": 15,
        "routes_to": 15,
        "topic": "Unit 15: Modal Diplomacy",
        "prompt": "Select the sentence expressing the most diplomatic and professional request:",
        "options": [
            "A) You must immediately send the updated expenditure ledger.",
            "B) Could you please forward the updated expenditure ledger by 14:00 today?",
            "C) Send the updated expenditure ledger right now.",
            "D) You ought to send the updated expenditure ledger immediately."
        ],
        "correct": "B",
        "rationale": "'Could you please...' calibrates the request with courteous workplace diplomacy, avoiding aggressive imperatives or confrontational modal demands."
    },
    {
        "num": 16,
        "routes_to": 16,
        "topic": "Unit 16: Active vs Passive Voice",
        "prompt": "Which sentence demonstrates the most objective, diplomatic passive construction for an error?",
        "options": [
            "A) The apprentice dropped the delicate optical sensor on the floor.",
            "B) The delicate optical sensor was dropped during shift handover.",
            "C) You dropped the delicate optical sensor during your shift.",
            "D) Somebody dropped the delicate optical sensor carelessly."
        ],
        "correct": "B",
        "rationale": "Passive voice ('was dropped') reports the incident objectively without personal finger-pointing or inflammatory blame."
    },
    {
        "num": 17,
        "routes_to": 17,
        "topic": "Unit 17: Agreement with Indefinite Pronouns",
        "prompt": "Choose the sentence with correct subject-verb agreement with 'Everyone':",
        "options": [
            "A) Everyone on the steering committee are required to attend the AGM.",
            "B) Everyone on the steering committee is required to attend the AGM.",
            "C) Everyone on the steering committee have agreed to attend the AGM.",
            "D) Everyone on the steering committee were attending the AGM."
        ],
        "correct": "B",
        "rationale": "'Everyone' is grammatically singular and requires the singular verb 'is required', regardless of the plural noun 'committee' in the prepositional phrase."
    },
    {
        "num": 18,
        "routes_to": 18,
        "topic": "Unit 18: Agreement with Neither/Either & Collective Nouns",
        "prompt": "Apply the rule of proximity: which sentence correctly completes the verb agreement?",
        "options": [
            "A) Neither the shift supervisor nor the machine operators was aware of the gas leak.",
            "B) Neither the shift supervisor nor the machine operators were aware of the gas leak.",
            "C) Neither the shift supervisor nor the machine operators is aware of the gas leak.",
            "D) Neither the shift supervisor nor the machine operators has been aware."
        ],
        "correct": "B",
        "rationale": "Under the rule of proximity, the verb agrees with the closest subject ('machine operators' - plural), requiring 'were aware'."
    },
    {
        "num": 19,
        "routes_to": 19,
        "topic": "Unit 19: Complex Subordination",
        "prompt": "Identify the sentence that avoids the double-conjunction error:",
        "options": [
            "A) Although the initial tender price was high, but the contractor offered superior warranties.",
            "B) Although the initial tender price was high, the contractor offered superior warranties.",
            "C) Although the initial tender price was high, yet the contractor offered superior warranties.",
            "D) Because the tender price was high so the contractor offered warranties."
        ],
        "correct": "B",
        "rationale": "Option B uses one subordinating conjunction ('Although') followed by a comma before the main clause. Options A, C, and D commit the fatal 'double-join' error."
    },
    {
        "num": 20,
        "routes_to": 20,
        "topic": "Unit 20: Relative Clauses",
        "prompt": "Select the sentence with correct relative pronoun usage for an individual professional:",
        "options": [
            "A) The clinical lead which inspected the ward approved the hygiene plan.",
            "B) The clinical lead who inspected the ward approved the hygiene plan.",
            "C) The clinical lead which that inspected the ward approved the hygiene plan.",
            "D) The clinical lead whom inspected the ward approved the hygiene plan."
        ],
        "correct": "B",
        "rationale": "Use 'who' for people acting as the subject of the clause ('who inspected'). 'Which' is reserved for inanimate objects or animals."
    },

    # PAGE 5: QUESTIONS 21 TO 30
    {
        "num": 21,
        "routes_to": 21,
        "topic": "Unit 21: Parallel Structure in Lists",
        "prompt": "Identify the bulleted list that demonstrates 100% parallel grammatical structure:",
        "options": [
            "A) • Inspect fire alarms. • Testing emergency lighting. • Replace backup batteries.",
            "B) • Inspect fire alarms. • Test emergency lighting. • Replace backup batteries.",
            "C) • Inspection of alarms. • Test emergency lighting. • Replacing batteries.",
            "D) • To inspect fire alarms. • Testing emergency lighting. • Battery replacement."
        ],
        "correct": "B",
        "rationale": "Every bullet in Option B begins with an imperative base verb ('Inspect', 'Test', 'Replace'), maintaining flawless parallelism."
    },
    {
        "num": 22,
        "routes_to": 22,
        "topic": "Unit 22: Register Transformation",
        "prompt": "Which sentence demonstrates the most formal, objective workplace register?",
        "options": [
            "A) We got in touch with the supplier because they totally messed up our delivery.",
            "B) We contacted the supplier regarding substantial discrepancies in the delivered consignment.",
            "C) We phoned the supplier to tell them their delivery was a total disaster.",
            "D) We dropped the supplier a line to ask what on earth happened to our goods."
        ],
        "correct": "B",
        "rationale": "Option B uses formal Latinate vocabulary ('contacted', 'substantial discrepancies', 'consignment') instead of informal phrasal verbs and slang."
    },
    {
        "num": 23,
        "routes_to": 23,
        "topic": "Unit 23: Affect vs Effect",
        "prompt": "Choose the sentence with correct usage of 'affect' (verb) and 'effect' (noun):",
        "options": [
            "A) The new regulations will effect staff morale, but the overall affect will be positive.",
            "B) The new regulations will affect staff morale, but the overall effect will be positive.",
            "C) The new regulations will affect staff morale, but the overall affect will be positive.",
            "D) The new regulations will effect staff morale, but the overall effect will be positive."
        ],
        "correct": "B",
        "rationale": "RAVEN: Affect is a Verb ('will affect'); Effect is a Noun ('the overall effect')."
    },
    {
        "num": 24,
        "routes_to": 23,
        "topic": "Unit 23: Practice vs Practise",
        "prompt": "Select the sentence with correct UK spelling of 'practice' (noun) and 'practise' (verb):",
        "options": [
            "A) Qualified nurses must practice clinical skills to maintain good professional practise.",
            "B) Qualified nurses must practise clinical skills to maintain good professional practice.",
            "C) Qualified nurses must practise clinical skills to maintain good professional practise.",
            "D) Qualified nurses must practice clinical skills to maintain good professional practice."
        ],
        "correct": "B",
        "rationale": "ICE is a noun (practice); -ise is a verb (practise). 'must practise' (verb); 'professional practice' (noun)."
    },
    {
        "num": 25,
        "routes_to": 24,
        "topic": "Unit 24: Principal vs Principle",
        "prompt": "Which sentence correctly distinguishes 'principal' from 'principle'?",
        "options": [
            "A) The principle reason for the policy update was to reinforce ethical principals.",
            "B) The principal reason for the policy update was to reinforce ethical principles.",
            "C) The principal reason for the policy update was to reinforce ethical principals.",
            "D) The principle reason for the policy update was to reinforce ethical principles."
        ],
        "correct": "B",
        "rationale": "'Principal' = main / head / primary; 'Principle' = moral rule or fundamental standard (ends in -le like rule)."
    },
    {
        "num": 26,
        "routes_to": 24,
        "topic": "Unit 24: Loose vs Lose",
        "prompt": "Identify the sentence that correctly distinguishes 'loose' from 'lose':",
        "options": [
            "A) If the drive belt is loose, the generator may lose electrical power.",
            "B) If the drive belt is lose, the generator may loose electrical power.",
            "C) If the drive belt is loose, the generator may loose electrical power.",
            "D) If the drive belt is lose, the generator may lose electrical power."
        ],
        "correct": "A",
        "rationale": "'Loose' (adjective, two O's) means not tight; 'Lose' (verb) means to suffer loss or misplace."
    },
    {
        "num": 27,
        "routes_to": 25,
        "topic": "Unit 25: Word Morphology (Negative Prefixes)",
        "prompt": "Which word correctly forms a negative adjective using the prefix 'in-' / 'im-' / 'il-' / 'ir-'?",
        "options": [
            "A) unresponsible",
            "B) irresponsible",
            "C) disresponsible",
            "D) misresponsible"
        ],
        "correct": "B",
        "rationale": "Before the letter 'r', the prefix 'in-' assimilates to 'ir-' ('irresponsible')."
    },
    {
        "num": 28,
        "routes_to": 25,
        "topic": "Unit 25: Suffix Spelling Rules (Doubling Consonant)",
        "prompt": "Select the correctly spelled word following the consonant doubling rule:",
        "options": [
            "A) refered",
            "B) referred",
            "C) referrd",
            "D) reffered"
        ],
        "correct": "B",
        "rationale": "In multi-syllable words ending in consonant-vowel-consonant where the stress is on the final syllable (re-FER), double the final consonant ('referred')."
    },
    {
        "num": 29,
        "routes_to": 26,
        "topic": "Unit 26: Prepositional Collocations",
        "prompt": "Which preposition correctly collocates with 'comply' and 'adhere'?",
        "options": [
            "A) comply to / adhere with",
            "B) comply with / adhere to",
            "C) comply at / adhere by",
            "D) comply for / adhere with"
        ],
        "correct": "B",
        "rationale": "Fixed collocations: 'comply WITH statutory rules' and 'adhere TO clinical guidelines'."
    },
    {
        "num": 30,
        "routes_to": 26,
        "topic": "Unit 26: Prepositional Collocations",
        "prompt": "Select the sentence with correct prepositional collocations throughout:",
        "options": [
            "A) The candidate is eligible for the bursary and capable of completing the research.",
            "B) The candidate is eligible to the bursary and capable to complete the research.",
            "C) The candidate is eligible with the bursary and capable for completing the research.",
            "D) The candidate is eligible at the bursary and capable with completing the research."
        ],
        "correct": "A",
        "rationale": "'Eligible FOR' and 'capable OF' are the mandatory prepositional pairings in standard English."
    },

    # PAGE 6: QUESTIONS 31 TO 40 + SCORING GUIDANCE
    {
        "num": 31,
        "routes_to": 1,
        "topic": "Unit 1: Sentence Boundaries",
        "prompt": "Identify the sentence that contains an ungrammatical run-on with no punctuation:",
        "options": [
            "A) The delivery arrived at dawn the warehouse opened an hour later.",
            "B) The delivery arrived at dawn; the warehouse opened an hour later.",
            "C) When the delivery arrived at dawn, the warehouse opened an hour later.",
            "D) The delivery arrived at dawn, and the warehouse opened an hour later."
        ],
        "correct": "A",
        "rationale": "Option A fuses two independent clauses together with zero punctuation, creating a severe run-on sentence."
    },
    {
        "num": 32,
        "routes_to": 2,
        "topic": "Unit 2: Comma Splices",
        "prompt": "Which sentence contains a comma splice masked by a transitional adverb?",
        "options": [
            "A) Production halted for two hours; however, backlog orders were cleared by dusk.",
            "B) Production halted for two hours, however backlog orders were cleared by dusk.",
            "C) Although production halted for two hours, backlog orders were cleared by dusk.",
            "D) Production halted for two hours, but backlog orders were cleared by dusk."
        ],
        "correct": "B",
        "rationale": "Option B uses only a comma before 'however' between two independent clauses, which is an ungrammatical comma splice. A semicolon is required before 'however'."
    },
    {
        "num": 33,
        "routes_to": 6,
        "topic": "Unit 6: Semicolons with Complex Lists",
        "prompt": "Select the sentence that correctly uses semicolons to separate items in an internally punctuated list:",
        "options": [
            "A) We visited Bristol, England, Cardiff, Wales, and Edinburgh, Scotland.",
            "B) We visited Bristol, England; Cardiff, Wales; and Edinburgh, Scotland.",
            "C) We visited Bristol; England, Cardiff; Wales, and Edinburgh; Scotland.",
            "D) We visited: Bristol, England, Cardiff, Wales, and Edinburgh, Scotland."
        ],
        "correct": "B",
        "rationale": "When list items themselves contain internal commas (City, Country), semicolons are required to separate the major list items."
    },
    {
        "num": 34,
        "routes_to": 10,
        "topic": "Unit 10: Contractions in Formal Writing",
        "prompt": "Which sentence demonstrates the appropriate formal register for an official board report?",
        "options": [
            "A) The executive team couldn't accept the tender because it didn't meet criteria.",
            "B) The executive team could not accept the tender because it did not meet criteria.",
            "C) The executive team could'nt accept the tender because it did'nt meet criteria.",
            "D) The executive team would of accepted the tender if costs were lower."
        ],
        "correct": "B",
        "rationale": "Formal board reports avoid contractions entirely, using the full forms 'could not' and 'did not'."
    },
    {
        "num": 35,
        "routes_to": 11,
        "topic": "Unit 11: Irregular Plural Possession",
        "prompt": "Choose the sentence with correct possessive punctuation for irregular plural nouns:",
        "options": [
            "A) The womens' committee submitted the childrens' healthcare proposal.",
            "B) The women's committee submitted the children's healthcare proposal.",
            "C) The womens committee submitted the childrens healthcare proposal.",
            "D) The women's' committee submitted the children's' healthcare proposal."
        ],
        "correct": "B",
        "rationale": "Irregular plurals that do not end in 's' (women, children) take an apostrophe followed by 's' ('women's', 'children's')."
    },
    {
        "num": 36,
        "routes_to": 16,
        "topic": "Unit 16: Active Voice for Direct Accountability",
        "prompt": "Which sentence correctly uses the active voice to pinpoint executive responsibility?",
        "options": [
            "A) The budget cuts were implemented by the managing director.",
            "B) The managing director implemented the budget cuts.",
            "C) Budget cuts were being implemented across all regional divisions.",
            "D) The implementation of budget cuts was authorized by management."
        ],
        "correct": "B",
        "rationale": "In Option B, the subject ('managing director') directly performs the action ('implemented') upon the object ('budget cuts')."
    },
    {
        "num": 37,
        "routes_to": 17,
        "topic": "Unit 17: Indefinite Pronoun Agreement",
        "prompt": "Select the sentence with correct verb agreement for 'Each':",
        "options": [
            "A) Each of the audited files have been archived in secure storage.",
            "B) Each of the audited files has been archived in secure storage.",
            "C) Each of the audited files were archived in secure storage.",
            "D) Each of the audited files are archiving in secure storage."
        ],
        "correct": "B",
        "rationale": "'Each' is singular and requires the singular auxiliary verb 'has been archived'."
    },
    {
        "num": 38,
        "routes_to": 22,
        "topic": "Unit 22: Phrasal Verb Replacement",
        "prompt": "Which Latinate verb best replaces the informal phrasal verb 'put off' in a formal meeting agenda?",
        "options": [
            "A) cancel",
            "B) postpone",
            "C) forget",
            "D) terminate"
        ],
        "correct": "B",
        "rationale": "'Postpone' is the formal equivalent of 'put off' (delaying an event to a later date)."
    },
    {
        "num": 39,
        "routes_to": 24,
        "topic": "Unit 24: Accept vs Except",
        "prompt": "Choose the correct sentence distinguishing 'accept' from 'except':",
        "options": [
            "A) All departments except marketing agreed to accept the new software platform.",
            "B) All departments accept marketing agreed to except the new software platform.",
            "C) All departments except marketing agreed to except the new software platform.",
            "D) All departments accept marketing agreed to accept the new software platform."
        ],
        "correct": "A",
        "rationale": "'Except' = apart from / excluding; 'Accept' = to agree to receive."
    },
    {
        "num": 40,
        "routes_to": 25,
        "topic": "Unit 25: Word Morphology",
        "prompt": "Identify the correctly spelled word with the suffix '-able' / '-ible':",
        "options": [
            "A) relyable",
            "B) reliable",
            "C) relible",
            "D) relyible"
        ],
        "correct": "B",
        "rationale": "When adding a suffix to a base word ending in a consonant + 'y' ('rely'), change 'y' to 'i' ('reliable')."
    }
]


# =============================================================================
# 6 VOCABULARY IN USE MASTER MODULES (Pages 59 to 64)
# =============================================================================

VOCABULARY_MODULES = [
    {
        "module": 1,
        "page": 59,
        "title": "Module 1: Latin & Greek Prefixes in Professional English",
        "subtitle": "Word Formation Architecture: Decoding Meaning & Elevating Precision",
        "theory_title": "Prefix Morphology: Structural Logic & Vocational Value",
        "theory_text": """In vocational communication, understanding prefixes allows you to decipher complex terminology instantly and express nuanced relationships without awkward phrasing.
<ul style="margin:2px 0 0 14px; padding:0; line-height:1.4;">
  <li><strong>Sub- (Under / Secondary):</strong> <em>subcontractor</em>, <em>substandard</em>, <em>subsequent</em>, <em>subordinate</em>.</li>
  <li><strong>Trans- (Across / Beyond):</strong> <em>transnational</em>, <em>transmission</em>, <em>transformation</em>, <em>transaction</em>.</li>
  <li><strong>Inter- (Between / Mutual):</strong> <em>interpersonal</em>, <em>interdependent</em>, <em>intermediate</em>, <em>interdepartmental</em>.</li>
  <li><strong>Intra- (Within / Inside):</strong> <em>intranet</em>, <em>intravenous</em>, <em>intra-organizational</em>.</li>
  <li><strong>Contra- / Counter- (Against / Opposite):</strong> <em>contradict</em>, <em>counterproductive</em>, <em>counter-proposal</em>.</li>
  <li><strong>Assimilation Rules:</strong> The negative prefix <em>in-</em> changes to <em>im-</em> before m/p (<em>impartial, impossible</em>), <em>il-</em> before l (<em>illogical</em>), and <em>ir-</em> before r (<em>irregular</em>).</li>
</ul>""",
        "table_headers": ["Prefix", "Core Meaning", "Workplace Example", "Contextual Application"],
        "table_rows": [
            ("Anti-", "Opposed to / Against", "Antivirus / Anti-discriminatory", "Ensuring IT networks and HR policies comply with statutory law."),
            ("Bi-", "Two / Twice", "Biannual / Bilateral", "Convening bilateral negotiations between union and management."),
            ("Co- / Con-", "Together / Jointly", "Collaborative / Concurrent", "Managing concurrent construction phases on the transport hub."),
            ("De-", "Reverse / Remove / Down", "De-escalate / Decarbonize", "De-escalating aggressive customer grievances through mediation."),
            ("Fore-", "Before / In advance", "Forecast / Foresight", "Preparing financial forecasts for capital expenditure reviews."),
            ("Mal-", "Bad / Faulty / Wrong", "Malfunction / Malpractice", "Investigating clinical malpractice allegations under safeguarding rules."),
            ("Mis-", "Incorrect / Wrongly", "Miscalculated / Misconduct", "Issuing formal disciplinary warnings for gross misconduct."),
            ("Multi-", "Many / Multiple", "Multidisciplinary / Multifaceted", "Assembling a multidisciplinary team of NHS healthcare specialists.")
        ],
        "exercises": [
            ("Form the antonym using an assimilating prefix (im-, il-, ir-, in-): 'rational' &rarr; ________", "irrational"),
            ("Form the antonym using an assimilating prefix: 'legitimate' &rarr; ________", "illegitimate"),
            ("Form the antonym using an assimilating prefix: 'practicable' &rarr; ________", "impracticable"),
            ("Select the correct prefix for 'actions that produce opposite of intended result': [counter / inter]productive &rarr; ________", "counterproductive"),
            ("Complete the sentence: 'The firm signed a ________lateral (two-party) agreement.' &rarr; ________", "bilateral"),
            ("Complete the sentence: 'Hospital staff must ________escalate tense situations.' &rarr; ________", "de-escalate")
        ]
    },
    {
        "module": 2,
        "page": 60,
        "title": "Module 2: High-Impact Suffixes & Word Class Transformations",
        "subtitle": "Morphological Engineering: Converting Nouns, Verbs, Adjectives & Adverbs",
        "theory_title": "Suffix Architecture: Changing Word Classes Without Errors",
        "theory_text": """Suffixes attach to the end of root words, systematically transforming their grammatical part of speech. Mastering suffix transformations allows candidates to eliminate clumsy, repetitive phrasing in Level 2 exam compositions.
<ul style="margin:2px 0 0 14px; padding:0; line-height:1.4;">
  <li><strong>Noun-Forming Suffixes:</strong> <em>-tion</em> (demonstrate &rarr; <em>demonstration</em>), <em>-ment</em> (manage &rarr; <em>management</em>), <em>-ity</em> (feasible &rarr; <em>feasibility</em>), <em>-ance / -ence</em> (compliant &rarr; <em>compliance</em>), <em>-ness</em> (effective &rarr; <em>effectiveness</em>).</li>
  <li><strong>Verb-Forming Suffixes:</strong> <em>-ise / -ize</em> (standard &rarr; <em>standardise</em>), <em>-ify</em> (clear &rarr; <em>clarify</em>), <em>-ate</em> (valid &rarr; <em>validate</em>).</li>
  <li><strong>Adjective-Forming Suffixes:</strong> <em>-able / -ible</em> (access &rarr; <em>accessible</em>), <em>-ous</em> (hazard &rarr; <em>hazardous</em>), <em>-ful</em> (resource &rarr; <em>resourceful</em>), <em>-ive</em> (prevent &rarr; <em>preventive</em>).</li>
  <li><strong>Spelling Trap:</strong> Silent 'e' is dropped before vowel suffixes (<em>create &rarr; creation</em>), but retained before consonant suffixes (<em>arrange &rarr; arrangement</em>).</li>
</ul>""",
        "table_headers": ["Base Root", "Noun Form", "Verb Form", "Adjective Form"],
        "table_rows": [
            ("Standard", "Standardisation", "Standardise", "Standardised"),
            ("Economy", "Economics / Economy", "Economise", "Economical / Economic"),
            ("Assess", "Assessment", "Assess", "Assessable"),
            ("Comply", "Compliance", "Comply", "Compliant"),
            ("Prior", "Priority / Prioritisation", "Prioritise", "Prioritised"),
            ("Signify", "Significance", "Signify", "Significant"),
            ("Rely", "Reliance", "Rely", "Reliable"),
            ("Justify", "Justification", "Justify", "Justifiable")
        ],
        "exercises": [
            ("Convert 'facilitate' into a noun meaning 'the person who aids a meeting': ________", "facilitator"),
            ("Convert 'sustain' into an adjective suitable for environmental policy: ________", "sustainable"),
            ("Convert 'author' into a noun meaning legal power or permission: ________", "authority / authorization"),
            ("Transform: 'The supervisor explained why it was feasible.' &rarr; 'The supervisor evaluated its ________.'", "feasibility"),
            ("Transform: 'We must make the procedures simple.' &rarr; 'We must ________ the procedures.'", "simplify"),
            ("Transform: 'The team was able to adapt.' &rarr; 'The team demonstrated high ________.'", "adaptability")
        ]
    },
    {
        "module": 3,
        "page": 61,
        "title": "Module 3: Workplace Register & Lexical Precision",
        "subtitle": "Eliminating Conversational Slang & Elevated Latinate Vocabulary",
        "theory_title": "The Register Transformation Continuum",
        "theory_text": """Functional Skills Level 2 examiners strictly evaluate candidate register. Everyday conversational phrasal verbs, idioms, and contractions degrade formal proposals, incident reports, and letters of appeal. Candidates must deploy precise, elevated Latinate equivalents to command the higher mark bands.
<ul style="margin:2px 0 0 14px; padding:0; line-height:1.4;">
  <li><strong>Phrasal Verbs vs Latinate Verbs:</strong> Phrasal verbs (<em>look into, carry out, put off</em>) are informal; Latinate verbs (<em>investigate, execute / implement, postpone</em>) convey executive authority.</li>
  <li><strong>Subjective Exaggeration vs Measured Fact:</strong> Replace hyperbolic slang (<em>'totally ridiculous mess'</em>) with professional understatement (<em>'significant administrative oversight'</em>).</li>
  <li><strong>Hedging &amp; Objectivity:</strong> Use formal modal structures (<em>'Evidence suggests that...'</em> rather than <em>'Obviously everyone knows...'</em>).</li>
</ul>""",
        "table_headers": ["Informal / Phrasal Verb", "Formal Professional Alternative", "Vocational Sentence Context"],
        "table_rows": [
            ("Find out", "Ascertain / Determine", "We conducted an internal audit to ascertain the exact financial shortfall."),
            ("Look into", "Investigate / Examine", "Senior management will investigate the health and safety violation."),
            ("Carry out", "Execute / Implement / Conduct", "The facilities team will conduct unannounced inspections weekly."),
            ("Put off", "Postpone / Defer", "The disciplinary hearing was postponed until legal counsel arrived."),
            ("Get rid of", "Eradicate / Eliminate / Dispose of", "The hospital introduced protocols to eliminate clinical contamination."),
            ("Bring in", "Introduce / Implement", "The logistics hub will introduce biometric access barriers."),
            ("Go over", "Review / Scrutinise", "Auditors must scrutinise all purchase invoices before sign-off."),
            ("Turn down", "Decline / Reject", "The borough planning committee voted to reject the commercial application.")
        ],
        "exercises": [
            ("Rewrite informally: 'We need to sort out this problem ASAP.' &rarr; Professional formal:", "We must address and resolve this matter immediately."),
            ("Rewrite informally: 'The boss turned down my request for time off.' &rarr; Professional formal:", "The line manager declined my application for leave."),
            ("Rewrite informally: 'The police are looking into the break-in.' &rarr; Professional formal:", "The authorities are investigating the security breach."),
            ("Replace 'put up with': 'We cannot put up with late deliveries.' &rarr; Professional formal:", "We cannot tolerate continued delivery delays."),
            ("Replace 'set up': 'The council will set up an enquiry.' &rarr; Professional formal:", "The local authority will establish an official enquiry."),
            ("Replace 'talk about': 'We met to talk about the budget.' &rarr; Professional formal:", "We convened to discuss the budgetary allocation.")
        ]
    },
    {
        "module": 4,
        "page": 62,
        "title": "Module 4: Essential Business & Administrative Collocations",
        "subtitle": "Natural Lexical Pairings: Verb + Noun & Adjective + Noun Combinations",
        "theory_title": "Collocational Competence in Corporate & Public Sector English",
        "theory_text": """Collocations are conventional word pairings that native speakers produce automatically. In Functional Skills English, using unnatural combinations (e.g. <em>'make a crime'</em> instead of <em>'commit an offence'</em>, or <em>'do a decision'</em> instead of <em>'reach a decision'</em>) immediately flags weak fluency.
<ul style="margin:2px 0 0 14px; padding:0; line-height:1.4;">
  <li><strong>Verb + Noun Collocations:</strong> Verbs frequently select specific abstract nouns: <em>reach a consensus</em>, <em>conduct an audit</em>, <em>implement recommendations</em>, <em>exercise discretion</em>, <em>breach a contract</em>.</li>
  <li><strong>Adjective + Noun Collocations:</strong> Fixed descriptive pairs: <em>vested interest</em>, <em>mitigating circumstances</em>, <em>stringent regulations</em>, <em>foregone conclusion</em>, <em>paramount importance</em>.</li>
  <li><strong>Noun + Preposition Collocations:</strong> Fixed connections: <em>discrepancy between</em>, <em>compliance with</em>, <em>adherence to</em>, <em>exception to</em>.</li>
</ul>""",
        "table_headers": ["Verb Collocation", "Adjective Collocation", "Prepositional Collocation"],
        "table_rows": [
            ("Conduct an audit", "Stringent regulations", "In compliance with"),
            ("Reach a consensus", "Mitigating circumstances", "Adherence to"),
            ("Implement measures", "Paramount importance", "Eligible for"),
            ("Exercise discretion", "Vested interest", "Discrepancy between"),
            ("Breach a contract", "Binding agreement", "Subject to"),
            ("Lodge a complaint", "Unprecedented demand", "Subsequent to"),
            ("Discharge duties", "Substandard performance", "Responsible for"),
            ("Convene a meeting", "Comprehensive review", "Capable of")
        ],
        "exercises": [
            ("Select the correct verb: Management decided to [make / reach / do] a consensus regarding shift patterns.", "reach"),
            ("Select the correct verb: The customer formally [dropped / lodged / placed] a complaint against the vendor.", "lodged"),
            ("Select the correct adjective: Maintaining sterile surgical equipment is of [paramount / extreme / giant] importance.", "paramount"),
            ("Complete the pairing: The contractor was in [breach / break / split] of statutory employment law.", "breach"),
            ("Complete the pairing: The panel reviewed the [mitigating / softening / easing] circumstances surrounding the absence.", "mitigating"),
            ("Complete the pairing: All employees must act in [compliance / complying / complied] with GDPR guidelines.", "compliance")
        ]
    },
    {
        "module": 5,
        "page": 63,
        "title": "Module 5: Academic & Professional Discourse Markers",
        "subtitle": "Textual Architecture: Signposting Arguments, Contrast, Causality & Concession",
        "theory_title": "Discourse Cohesion: Linking Ideas with Authority",
        "theory_text": """Discourse markers (connectives and signposts) structure paragraphs, direct the reader through complex arguments, and indicate relationships between evidence and conclusions. Level 2 criteria require logical sequencing and sophisticated transitions.
<ul style="margin:2px 0 0 14px; padding:0; line-height:1.4;">
  <li><strong>Addition &amp; Reinforcement:</strong> <em>Furthermore, Moreover, In addition, Additionally</em> (Capitalize and follow with a comma when fronted).</li>
  <li><strong>Contrast &amp; Concession:</strong> <em>Conversely, Nevertheless, On the contrary, Notwithstanding, Whereas, Although</em>.</li>
  <li><strong>Causality &amp; Consequence:</strong> <em>Consequently, Therefore, Accordingly, As a result, Thus</em>.</li>
  <li><strong>Exemplification &amp; Clarification:</strong> <em>Specifically, For instance, Namely, In particular</em>.</li>
  <li><strong>Summary &amp; Recommendation:</strong> <em>In conclusion, To summarise, Ultimately, On balance</em>.</li>
</ul>""",
        "table_headers": ["Rhetorical Purpose", "Fronted Discourse Marker", "Structural Function in Reports"],
        "table_rows": [
            ("Reinforcing a Point", "Furthermore, / Moreover,", "Adds weight to an existing finding or recommendation."),
            ("Conceding / Contrasting", "Nevertheless, / Conversely,", "Introduces counter-arguments or unexpected limitations."),
            ("Demonstrating Cause", "Consequently, / Therefore,", "Connects an empirical finding directly to its business impact."),
            ("Providing Detail", "Specifically, / For instance,", "Presents specific technical data, dates, or regulations."),
            ("Stating Priority", "Above all, / Fundamentally,", "Highlights the core imperative among several considerations."),
            ("Expressing Condition", "Provided that, / Unless,", "Establishes non-negotiable contractual or legal prerequisites.")
        ],
        "exercises": [
            ("Insert an appropriate marker of consequence: 'The supply chain collapsed; ________, factory operations were suspended.'", "consequently / therefore"),
            ("Insert an appropriate marker of contrast: 'Profits grew rapidly; ________, customer satisfaction declined by 12%.'", "nevertheless / conversely"),
            ("Insert an appropriate marker of reinforcement: 'The system is secure. ________, it has been certified by the Cabinet Office.'", "Furthermore / Moreover"),
            ("Punctuate correctly: 'Consequently the board authorized immediate funding.' &rarr; Punctuation needed:", "Comma after 'Consequently' ('Consequently, the board...')"),
            ("Punctuate correctly: 'The policy was revised; however the implementation date remains unchanged.' &rarr; Punctuation:", "Comma after 'however' ('; however, the implementation...')"),
            ("Choose the best marker: '[Specifically / Conversely], Section 4.2 outlines statutory sickness benefits.'", "Specifically")
        ]
    },
    {
        "module": 6,
        "page": 64,
        "title": "Module 6: Sector-Specific Technical Vocabulary & Glossary",
        "subtitle": "Master Lexicon Across 6 Major UK Vocational Pathways",
        "theory_title": "Vocational Lexical Precision Across Key Employment Sectors",
        "theory_text": """Functional Skills English writing scenarios draw directly from authentic UK vocational pathways. Using precise sector terminology rather than vague generic terms (e.g. <em>'vital signs monitoring'</em> instead of <em>'checking the patient'</em>, or <em>'structural integrity'</em> instead of <em>'how strong the wall is'</em>) secures top-band marks for composition and vocational suitability.
<p style="margin:2px 0 0 0; font-size:7.8pt;">Master the core terminology below across the six primary Functional Skills employment sectors:</p>""",
        "table_headers": ["Vocational Sector", "Key Technical Lexicon", "Definition & Contextual Usage"],
        "table_rows": [
            ("Healthcare & Social Care", "Safeguarding, Triage, Phlebotomy, Palliative, Holism, Efficacy", "Protocols protecting vulnerable adults, prioritizing clinical urgency, and ensuring holistic patient care."),
            ("Construction & Trades", "Load-bearing, Remediation, Scaffolding, Subcontractor, Specification, Tolerance", "Structural engineering parameters, environmental site clean-up, and compliance with building regulations."),
            ("Business & Administration", "Procurement, Depreciation, Amortisation, Governance, Stakeholder, Restitution", "Corporate purchasing pipelines, asset balance sheets, board oversight, and legal dispute settlement."),
            ("Digital & Information Technology", "Latency, Bandwidth, Virtualisation, Encryption, Hypervisor, Redundancy", "Network latency thresholds, cryptographic data security, and hardware backup failover mechanisms."),
            ("Logistics & Supply Chain", "Consignment, Intermodal, Telematics, Manifest, Demurrage, Inventory", "Freight cargo documentation, vehicle fleet GPS telemetry tracking, and port detention penalty tariffs."),
            ("Customer Care & Hospitality", "Mediation, Discretionary, Restitution, Escalation, De-escalation, Retention", "Managing customer grievances constructively, offering compensatory goodwill, and reducing client churn.")
        ],
        "exercises": [
            ("Sector Identification: Which sector uses 'triage', 'safeguarding', and 'phlebotomy'? &rarr; ________", "Healthcare & Social Care"),
            ("Sector Identification: Which sector uses 'telematics', 'manifest', and 'consignment'? &rarr; ________", "Logistics & Supply Chain"),
            ("Sector Identification: Which sector uses 'load-bearing', 'remediation', and 'tolerance'? &rarr; ________", "Construction & Trades"),
            ("Define 'restitution' in commercial disputes: ________", "Financial compensation or restoration of losses to an injured party"),
            ("Define 'latency' in IT network maintenance: ________", "The delay before a transfer of data begins following an instruction"),
            ("Define 'demurrage' in freight logistics: ________", "A charge payable to an owner of a chartered ship/container in respect of failure to load/unload within agreed time")
        ]
    }
]


# =============================================================================
# 6 MURPHY-STYLE MIXED ADDITIONAL WORKOUTS (Pages 65 to 70)
# =============================================================================

MIXED_WORKOUTS = [
    {
        "workout": 1,
        "page": 65,
        "title": "Additional Workout 1: Sentence Architecture & Boundary Control",
        "coverage": "Units 1 to 5 Synthesis: Fragments, Comma Splices, FANBOYS, Fronted Adverbials & Parenthesis",
        "drill_1_title": "Drill 1: Forensic Boundary Identification (5 Marks)",
        "drill_1_items": [
            ("The delivery arrived late, the warehouse staff had already gone home.", "Comma Splice (Fix with semicolon or ', and')"),
            ("Because heavy snow blocked the motorway access road on Monday morning.", "Sentence Fragment (Stranded subordinate clause)"),
            ("In accordance with Section 14 of the Health and Safety at Work Act 1974, all operatives must wear PPE.", "Correctly Punctuated Sentence (Fronted adverbial + comma)"),
            ("The audit manager inspected the balance sheets, and discovered a £12,000 discrepancy.", "Unnecessary Comma (Compound predicate shares subject 'audit manager')"),
            ("Ms Sarah Jenkins who was appointed head of customer care last month, has resigned.", "Missing Opening Parenthetical Comma (Requires comma after 'Jenkins')")
        ],
        "drill_2_title": "Drill 2: Controlled Sentence Transformation (4 Marks)",
        "drill_2_items": [
            ("Fix comma splice using a semicolon + conjunctive adverb: 'The fire alarm sounded, everyone evacuated the building.'",
             "The fire alarm sounded; consequently, everyone evacuated the building."),
            ("Fix fragment by attaching a main clause: 'Although funding was cut.'",
             "Although funding was cut, the youth centre remained open through community donations."),
            ("Insert parenthetical commas correctly: 'The site supervisor Mr Paul Davies inspected the scaffolding.'",
             "The site supervisor, Mr Paul Davies, inspected the scaffolding."),
            ("Correct coordinating conjunction punctuation: 'The courier attempted delivery at noon but, nobody was in the office.'",
             "The courier attempted delivery at noon, but nobody was in the office.")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "INTERNAL MEMO: FACILITY AIR CONDITIONING BREAKDOWN",
        "doc_text": """At 08:30 on Monday the main chiller unit on the roof failed completely. Because the ambient office temperature climbed to 31 degrees Celsius by mid-day. Staff were permitted to work remotely for the remainder of the afternoon, the facilities director contacted emergency heating and ventilation engineers. Furthermore replacement compressor parts, will not arrive until Thursday morning. The maintenance manager who was on site throughout the incident ensured all server room auxiliary chillers remained operational.""",
        "errors_list": [
            "Missing comma after fronted time phrase ('At 08:30 on Monday, the main')",
            "Sentence fragment in sentence 2 ('Because the ambient... by mid-day.' -> attach to sentence 1)",
            "Comma splice in sentence 3 ('afternoon, the facilities director' -> use semicolon or ', and')",
            "Misplaced comma after subject in sentence 4 ('replacement compressor parts, will not' -> remove comma)",
            "Missing opening parenthetical comma in sentence 5 ('The maintenance manager, who was on site throughout the incident, ensured')"
        ]
    },
    {
        "workout": 2,
        "page": 66,
        "title": "Additional Workout 2: Advanced Punctuation Mechanics",
        "coverage": "Units 6 to 9 Synthesis: Semicolons, Colons, Dashes, Brackets & Hyphens",
        "drill_1_title": "Drill 1: Advanced Punctuation Discrimination (5 Marks)",
        "drill_1_items": [
            ("Identify correct colon lead-in: The primary objectives are: / We identified three primary objectives:", "We identified three primary objectives: (Must be a complete independent clause)"),
            ("Choose correct dash/bracket pair: The apprentice (aged nineteen &mdash; operated the machine. / The apprentice &mdash; aged nineteen &mdash; operated the machine.", "The apprentice &mdash; aged nineteen &mdash; operated the machine. (Never mix bracket with dash)"),
            ("Identify correct compound adjective: a state-of-the-art laboratory / a state of the art laboratory", "a state-of-the-art laboratory (Hyphenated before noun)"),
            ("Choose correct adverbial: a rapidly-expanding business / a rapidly expanding business", "a rapidly expanding business (-ly adverbs never take hyphens)"),
            ("Identify correct semicolon usage: Staff completed the training; because it was mandatory. / Staff completed the training; it was mandatory.", "Staff completed the training; it was mandatory. (Both sides must be independent)")
        ],
        "drill_2_title": "Drill 2: Mechanical Punctuation Insertion (4 Marks)",
        "drill_2_items": [
            ("Insert colon correctly: 'Operators must equip three mandatory items ear defenders safety goggles and steel boots.'",
             "Operators must equip three mandatory items: ear defenders, safety goggles, and steel boots."),
            ("Insert single dash for emphatic twist: 'The real cause of the structural failure was not metal fatigue it was contractor negligence.'",
             "The real cause of the structural failure was not metal fatigue &mdash; it was contractor negligence."),
            ("Insert brackets for technical acronym: 'The National Health Service NHS introduced digital patient portals in 2024.'",
             "The National Health Service (NHS) introduced digital patient portals in 2024."),
            ("Insert hyphens where required: 'We require twenty four hour on call technical support.'",
             "We require 24-hour on-call technical support.")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "TECHNICAL BULLETIN: HIGH-PRESSURE HYDRAULIC VALVE RETROFIT",
        "doc_text": """Before commencing the valve retrofit technicians must: isolate all secondary pressure lines. The maintenance toolkit must include three specialized instruments; a digital torque wrench, a laser alignment caliper, and an ultrasonic flaw detector. The pressure relief valve &mdash; which had been inspected only last month (failed catastrophically during initial pressurization. Workshop engineers were operating in a highly-pressurized environment. Fortunately the emergency shut-off system was state of the art.""",
        "errors_list": [
            "Ungrammatical colon after modal verb in sentence 1 ('technicians must: isolate' -> remove colon)",
            "Incorrect semicolon before a list in sentence 2 ('instruments; a digital torque' -> replace with colon ':')",
            "Mismatched dash and bracket in sentence 3 ('&mdash; which had been inspected only last month (failed' -> close with dash '&mdash; failed')",
            "Ungrammatical hyphen after -ly adverb in sentence 4 ('highly-pressurized environment' -> 'highly pressurized environment')",
            "Missing hyphens in compound adjective before noun in sentence 5 ('was state of the art' is predicate, but if modifying it needs hyphens; here check: missing comma after 'Fortunately, the emergency' and predicate is correct)"
        ]
    },
    {
        "workout": 3,
        "page": 67,
        "title": "Additional Workout 3: Apostrophes, Contractions & Ownership",
        "coverage": "Units 10 to 12 Synthesis: Apostrophes of Omission, Singular/Plural Possession & Its vs It's",
        "drill_1_title": "Drill 1: Apostrophe Precision Discrimination (5 Marks)",
        "drill_1_items": [
            ("Identify correct contraction: does'nt / doesn't / dosent", "doesn't (Apostrophe replaces omitted 'o')"),
            ("Choose correct phrase: would of completed / would've completed / would ov completed", "would've completed (Contraction of 'would have')"),
            ("Identify correct possessive: the directors' board / the director's' board / the directors board", "the directors' board (Plural noun ending in 's' takes apostrophe after 's')"),
            ("Choose correct irregular plural possessive: childrens' playground / children's playground", "children's playground (Irregular plural not ending in 's' takes 's)"),
            ("Identify correct usage: The dog wagged it's tail / The dog wagged its tail", "The dog wagged its tail (Possessive pronoun 'its' has no apostrophe)")
        ],
        "drill_2_title": "Drill 2: Controlled Contraction & Possession Transformation (4 Marks)",
        "drill_2_items": [
            ("Transform into formal business English: 'We haven't received the client's payment and we'll escalate.'",
             "We have not received the client's payment and we will escalate."),
            ("Correct the greengrocer's apostrophe: 'The cafe sells fresh sandwich's and hot pastie's.'",
             "The cafe sells fresh sandwiches and hot pasties."),
            ("Form singular possessive: 'The car belonging to the boss was damaged.'",
             "The boss's car was damaged."),
            ("Insert 'its' or 'it's': '______ undeniable that the company has expanded ______ global footprint.'",
             "It's undeniable that the company has expanded its global footprint.")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "PROPERTY MANAGEMENT ADVISORY: COMMERCIAL CAR PARK ALLOCATIONS",
        "doc_text": """All tenant's must ensure that their employees park only in designated company bays. The landlord's representative has noted that several delivery driver's have blocked the emergency access lane. Its imperative that the estate management office maintains it's records accurately. The business centre provides dedicated mens and womens changing suites on the ground floor. If a vehicle does'nt display a valid permit, an automated parking charge notice will be issued immediately.""",
        "errors_list": [
            "Greengrocer's apostrophe on simple plural in sentence 1 ('All tenant's must' -> 'All tenants must')",
            "Greengrocer's apostrophe on simple plural in sentence 2 ('delivery driver's have' -> 'delivery drivers have')",
            "Missing apostrophe in contraction in sentence 3 ('Its imperative' -> 'It\'s imperative' [It is])",
            "Incorrect apostrophe on possessive pronoun in sentence 3 ('maintains it\'s records' -> 'maintains its records')",
            "Missing possessive apostrophes on irregular plurals in sentence 4 ('mens and womens' -> 'men\'s and women\'s') and misplaced apostrophe in sentence 5 ('does\'nt' -> 'doesn\'t')"
        ]
    },
    {
        "workout": 4,
        "page": 68,
        "title": "Additional Workout 4: Verbs, Tense, Aspect & Diplomatic Voice",
        "coverage": "Units 13 to 16 Synthesis: Past Simple vs Present Perfect, Past Continuous, Modals & Voice",
        "drill_1_title": "Drill 1: Verb Tense & Aspect Discrimination (5 Marks)",
        "drill_1_items": [
            ("Identify correct tense with finished time: We completed the survey yesterday. / We have completed the survey yesterday.",
             "We completed the survey yesterday. (Past Simple required with finished time)"),
            ("Choose correct aspect: While the engineer was inspecting the cable, sparks were flying. / sparks flew.",
             "While the engineer was inspecting the cable, sparks flew. (Past Simple interruption)"),
            ("Select diplomatic modal: You must rewrite this immediately. / Could you please review Section 2?",
             "Could you please review Section 2? (Diplomatic workplace register)"),
            ("Identify passive voice: The auditor reviewed twelve files. / Twelve files were reviewed by the auditor.",
             "Twelve files were reviewed by the auditor. (Passive: receiver + be + past participle)"),
            ("Choose correct modal syntax: The contractor must to submit risk assessments. / must submit",
             "must submit (Modal auxiliaries take bare infinitive without 'to')")
        ],
        "drill_2_title": "Drill 2: Controlled Tense & Voice Transformations (4 Marks)",
        "drill_2_items": [
            ("Transform into diplomatic passive voice: 'Your technician broke the optical fiber switch.'",
             "The optical fiber switch was damaged during recent technical maintenance."),
            ("Transform into direct active voice: 'The annual financial budget was authorized by the chief executive.'",
             "The chief executive authorized the annual financial budget."),
            ("Correct erratic tense shift: 'The nurse entered the ward at 08:00 and administers medication.'",
             "The nurse entered the ward at 08:00 and administered medication."),
            ("Complete using Present Perfect: 'So far this month, our division (achieve) ______ all safety targets.'",
             "So far this month, our division has achieved all safety targets.")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "INCIDENT INVESTIGATION SUMMARY: DISTRIBUTION WAREHOUSE 3",
        "doc_text": """At 14:10 on Thursday, operative Liam Gallagher was driving a counterbalance forklift along Aisle 7 when he notices a hydraulic fluid spill. He immediately applies the handbrake, but the vehicle skids and collided with a shelving rack. Liam has completed his mandatory forklift refresher certification last month. The accident was investigated by the health and safety committee, and several damaged pallets was removed from the bay. Operatives must to adhere strictly to speed limits at all times.""",
        "errors_list": [
            "Erratic shift to present tense in sentence 1 ('when he notices' -> 'when he noticed')",
            "Erratic shift to present tense in sentence 2 ('He immediately applies' -> 'He immediately applied')",
            "Incorrect Present Perfect with specific past time in sentence 3 ('has completed his... last month' -> 'completed his... last month')",
            "Subject-verb mismatch in passive construction in sentence 4 ('damaged pallets was removed' -> 'damaged pallets were removed')",
            "Incorrect infinitive after modal in sentence 5 ('must to adhere' -> 'must adhere')"
        ]
    },
    {
        "workout": 5,
        "page": 69,
        "title": "Additional Workout 5: Agreement, Subordination & Structural Parallelism",
        "coverage": "Units 17 to 21 Synthesis: Indefinite Pronouns, Collective Nouns, Subordination, Relative Clauses & Lists",
        "drill_1_title": "Drill 1: Agreement & Syntax Discrimination (5 Marks)",
        "drill_1_items": [
            ("Select correct agreement: Each of the managers have signed. / Each of the managers has signed.",
             "Each of the managers has signed. ('Each' is grammatically singular)"),
            ("Apply rule of proximity: Neither the director nor the supervisors was / were informed.",
             "were informed (Agrees with closest subject 'supervisors' - plural)"),
            ("Choose correct relative pronoun for a person: The nurse which / who administered the drug.",
             "The nurse who administered the drug ('who' for human beings)"),
            ("Identify non-restrictive punctuation: Server A, which hosts payroll data, crashed. / Server A which hosts payroll data crashed.",
             "Server A, which hosts payroll data, crashed. (Non-essential clause requires commas)"),
            ("Detect double-conjunction error: Although it rained, but we worked. / Although it rained, we worked.",
             "Although it rained, we worked. (Never combine 'Although... but')")
        ],
        "drill_2_title": "Drill 2: Controlled Structural Parallelism (4 Marks)",
        "drill_2_items": [
            ("Make parallel with imperative verbs: '• Inspect extinguishers. • Checking exit routes. • The replacement of signage.'",
             "• Inspect extinguishers. • Check exit routes. • Replace signage."),
            ("Combine without double-conjunction: 'The deadline was tight. We finished the tender on time.' (Use 'Although')",
             "Although the deadline was tight, we finished the tender on time."),
            ("Correct agreement with collective noun: 'The committee have published its annual governance review.'",
             "The committee has published its annual governance review."),
            ("Correct agreement with indefinite pronoun: 'Everyone in the customer care team are entitled to a bonus.'",
             "Everyone in the customer care team is entitled to a bonus.")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "STANDARD OPERATING PROCEDURE: EMERGENCY FIRE EVACUATION",
        "doc_text": """When the fire evacuation alarm sounds, all personnel must follow statutory evacuation protocols:
&bull; Cease all workshop machinery operations immediately.
&bull; Evacuating through the nearest designated emergency fire exit.
&bull; Report directly to the assembly coordinator on Car Park B.
&bull; Do not re-enter the facility under any circumstances;
Everyone in the administration offices are instructed to leave personal belongings behind. The emergency response team which was established last year has completed the floor sweep. Although the alarm was triggered accidentally but staff responded promptly.""",
        "errors_list": [
            "Loss of parallelism in bullet 2 ('Evacuating through' -> 'Evacuate through')",
            "Inconsistent terminal punctuation on bullet 4 (ended in semicolon ';' instead of full stop '.')",
            "Subject-verb mismatch with 'Everyone' ('Everyone... are instructed' -> 'Everyone... is instructed')",
            "Missing parenthetical commas around non-defining clause ('team, which was established last year, has')",
            "Double-conjunction error in final sentence ('Although the alarm was triggered accidentally but staff' -> remove 'but')"
        ]
    },
    {
        "workout": 6,
        "page": 70,
        "title": "Additional Workout 6: Lexical Register, Morphology & Confusables",
        "coverage": "Units 22 to 26 Synthesis: Formal Register, Tricky Homophones, Confusable Pairs, Morphology & Collocations",
        "drill_1_title": "Drill 1: Lexical Precision & Homophone Discrimination (5 Marks)",
        "drill_1_items": [
            ("Select correct homophone: The policy will severely affect / effect our overtime allocation.",
             "affect (Verb meaning to influence)"),
            ("Choose correct noun spelling: Trainees must observe standard clinical practice / practise.",
             "practice (ICE is a noun in UK English)"),
            ("Distinguish confusable pair: The principal / principle reason was contractor insolvency.",
             "principal (Meaning primary / main)"),
            ("Choose correct pair: Tighten the bolts or you will loose / lose the wheel.",
             "lose (Verb meaning to suffer loss / misplace)"),
            ("Identify correct collocation: All staff must comply with / comply to the statutory code.",
             "comply with ('Comply' pairs with 'with')")
        ],
        "drill_2_title": "Drill 2: Morphological Transformations & Register Elevators (4 Marks)",
        "drill_2_items": [
            ("Form negative adjective using correct prefix: 'accurate' &rarr; ________", "inaccurate"),
            ("Elevate informal phrasal verb: 'We must look into the customer's complaint.'",
             "We must investigate the customer's complaint."),
            ("Apply doubling consonant rule: 'submit' + '-ed' &rarr; ________", "submitted"),
            ("Insert correct preposition: 'The candidate is eligible ______ statutory maternity pay.'", "for ('eligible for')")
        ],
        "drill_3_title": "Drill 3: Workplace Document Proofreading Challenge (5 Deliberate Errors)",
        "doc_title": "PROCUREMENT POLICY UPDATE: TENDER SUBMISSION COMPLIANCE",
        "doc_text": """The local authority cannot except any commercial bids submitted after the midday deadline. All prospective contractors must adhere with mandatory ethical procurement principals. The overall affect of the revised procurement code will be to ensure total transparency. Suppliers who submit uncomplete documentation will be disqualified from future frameworks. We will look into all submitted tenders thoroughly before awarding the contract.""",
        "errors_list": [
            "Incorrect 'except' for 'accept' in sentence 1 ('cannot except' -> 'cannot accept')",
            "Incorrect preposition with 'adhere' in sentence 2 ('adhere with' -> 'adhere to')",
            "Incorrect 'principals' for 'principles' in sentence 2 ('ethical procurement principals' -> 'principles')",
            "Incorrect 'affect' for noun 'effect' in sentence 3 ('The overall affect' -> 'The overall effect')",
            "Incorrect negative prefix in sentence 4 ('uncomplete' -> 'incomplete') and informal phrasal verb in sentence 5 ('look into' -> 'scrutinise / examine')"
        ]
    }
]
