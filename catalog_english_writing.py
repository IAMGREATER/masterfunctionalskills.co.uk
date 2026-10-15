#!/usr/bin/env python3
"""
Catalog English Writing: Core Writing Standards.
Covers Formal Letter/Email conventions, Incident Reports, Articles, Paragraphing, Punctuation & SPaG.
"""
from build_topic_dataset import make_english_topic

CATALOG_ENGLISH_WRITING = [
    # 1. Grammar & Sentence Structures
    make_english_topic(
        slug="writing-grammar",
        title="Grammar & Sentence Structures",
        category="writing",
        spec_codes="L1.24 • L2.22",
        golden_rule="Vary sentence lengths using simple, compound, and complex sentences. Use coordinating conjunctions (FANBOYS: For, And, Nor, But, Or, Yet, So) for compound sentences, and subordinating conjunctions (Although, Because, Since, While, Unless) for complex sentences. Avoid comma splices and run-on sentences.",
        q1={
            "title": "Question 1 (Level 1 Compound Sentences with Conjunctions)",
            "marks": 2,
            "stem": "Join the two simple sentences below into a single compound sentence using a suitable coordinating conjunction (e.g. <em>and, but, so, yet</em>):<br>Sentence 1: <em>The clinic refurbishment was delayed by six weeks.</em><br>Sentence 2: <em>All scheduled patient consultations went ahead on time.</em>",
            "lines": 3,
            "ans_label": "Compound Sentence =",
            "choice_box": "________________________________________________________",
            "step_rows": [
                ("1. Select appropriate contrasting conjunction: 'but' OR 'yet'", "[M1]"),
                ("2. Punctuate accurately with comma before conjunction: 'The clinic refurbishment was delayed by six weeks, but all scheduled patient consultations went ahead on time.'", "[A1]")
            ],
            "final_answer": "The clinic refurbishment was delayed by six weeks, but all scheduled patient consultations went ahead on time.",
            "pitfall": "Using 'and' or 'so' which creates illogical meaning, or using a comma splice without a conjunction.",
            "reverse_check": "Both clauses are independent and express contrasting outcomes connected by 'but'."
        },
        q2={
            "title": "Question 2 (Level 2 Complex Sentence with Subordinating Conjunction)",
            "marks": 2,
            "stem": "Rewrite the following ideas as a single complex sentence starting with the subordinating conjunction <strong>'Although'</strong>:<br>Idea 1: <em>The ward team worked under intense winter pressures.</em><br>Idea 2: <em>They maintained a 98% patient satisfaction rating throughout January.</em>",
            "lines": 3,
            "ans_label": "Complex Sentence =",
            "choice_box": "Although _______________________________________________",
            "step_rows": [
                ("1. Start with 'Although' and place comma after introductory dependent clause", "[M1]"),
                ("2. Accurate sentence: 'Although the ward team worked under intense winter pressures, they maintained a 98% patient satisfaction rating throughout January.'", "[A1]")
            ],
            "final_answer": "Although the ward team worked under intense winter pressures, they maintained a 98% patient satisfaction rating throughout January.",
            "pitfall": "Omitting the comma separating the subordinate clause from the main clause.",
            "reverse_check": "'Although... pressures' is dependent; 'they maintained... January' is the main clause."
        },
        q3={
            "title": "Question 3 (Level 1 Subject-Verb Agreement Correction)",
            "marks": 3,
            "stem": "Identify and correct the <strong>three subject-verb agreement errors</strong> in the clinical handover note below:<br><em>'The team of nurses are meeting at 07:00. Either Sister Evans or Charge Nurse Davis were leading the handover. The supply of surgical gloves have been replenished.'</em>",
            "lines": 4,
            "ans_label": "Corrected verbs =",
            "choice_box": "1: are → _____ | 2: were → _____ | 3: have → _____ ",
            "step_rows": [
                ("1. 'The team of nurses' (singular collective noun 'team') → change 'are' to 'is'", "[A1]"),
                ("2. 'Either Sister Evans or Charge Nurse Davis' (singular subjects connected by 'or') → change 'were' to 'was'", "[A1]"),
                ("3. 'The supply of surgical gloves' (singular subject 'supply') → change 'have' to 'has'", "[A1]")
            ],
            "final_answer": "1. are → is;  2. were → was;  3. have → has",
            "pitfall": "Matching the verb with the nearest plural noun ('nurses', 'gloves') instead of the true singular subject ('team', 'supply').",
            "reverse_check": "The team IS... Either one WAS... The supply HAS."
        },
        q4={
            "title": "Question 4 (Level 2 Comma Splice Elimination)",
            "marks": 3,
            "stem": "The sentence below contains a <strong>comma splice</strong> (two complete sentences incorrectly joined only with a comma):<br><em>'The patient showed signs of allergic reaction, the nurse administered antihistamine immediately.'</em><br><br>Show <strong>two different ways</strong> to correct this comma splice grammatically (e.g. using a semicolon, a conjunction, or two separate sentences).",
            "lines": 4,
            "ans_label": "Two Corrections =",
            "choice_box": "Method 1: ________________ | Method 2: ________________",
            "step_rows": [
                ("1. Method 1 (Conjunction): 'The patient showed signs of allergic reaction, so the nurse administered antihistamine immediately.'", "[A1]"),
                ("2. Method 2 (Semicolon): 'The patient showed signs of allergic reaction; the nurse administered antihistamine immediately.'", "[A1]"),
                ("3. Alternative Method (Full stop): 'The patient showed signs of allergic reaction. The nurse administered antihistamine immediately.'", "[A1]")
            ],
            "final_answer": "Method 1: Add conjunction 'so'; Method 2: Use semicolon ';' or separate with a full stop.",
            "pitfall": "Leaving the comma and just capitalizing the second clause.",
            "reverse_check": "Both clauses are independent clauses requiring either a coordinator, semicolon, or full stop."
        },
        q5={
            "title": "Question 5 (Level 2 Workplace Incident Report Drafting)",
            "marks": 4,
            "stem": "A facilities apprentice reports a minor spill in a public hospital corridor.<br>Draft a concise, 4-sentence factual incident log for the health & safety register.<br>You must include:<br>• 1 simple sentence (stating exact time & location)<br>• 1 compound sentence (describing what spilled and who noticed it)<br>• 1 complex sentence starting with a subordinate conjunction (describing the hazard and immediate safety action taken)<br>• 1 sentence describing final resolution.",
            "lines": 5,
            "ans_label": "Drafted Report =",
            "choice_box": "Write your 4 sentences in the workspace provided below.",
            "step_rows": [
                ("1. Simple sentence with clear time and location accurately punctuated", "[A1]"),
                ("2. Compound sentence with coordinator ('and', 'but', 'so') joining two independent clauses", "[A1]"),
                ("3. Complex sentence with dependent clause starting with subordinating conjunction ('Because', 'After', 'When') with comma", "[A1]"),
                ("4. Concluding resolution sentence demonstrating accurate SPaG throughout", "[A1]")
            ],
            "final_answer": "Model: 'At 10:15 am, a liquid spillage occurred outside Outpatients Clinic 3. A visitor dropped a bottle of antiseptic solution, and the domestic assistant cordoned off the area immediately. Because wet linoleum presents a severe slip hazard, yellow warning cones were positioned around the perimeter. The area was cleaned, dried, and reopened safely by 10:35 am.'",
            "pitfall": "Writing fragments or informal notes instead of grammatically complete sentences.",
            "reverse_check": "Sentence 1 is simple; Sentence 2 is compound; Sentence 3 is complex; Sentence 4 is complete."
        },
        q6={
            "title": "Question 6 (Level 2 Formal Email Register Justification)",
            "marks": 4,
            "stem": "An apprentice writes this email to the Clinical Director:<br><em>'Hey Dr Patel, just letting u know the printer in ward 2 is totally busted again lol. We need a new one asap coz it’s a proper joke. Cheers, Dave.'</em><br><br>Critique this email for a professional workplace environment.<br>Identify three specific register errors, explain why they are inappropriate, and rewrite the email in a polished, formal professional register.",
            "lines": 5,
            "ans_label": "Critique & Polished Rewrite =",
            "choice_box": "Errors: ________________ | Professional Rewrite: ________________",
            "step_rows": [
                ("1. Identify errors: Inappropriate informal greeting ('Hey Dr Patel'), text slang/abbreviations ('u', 'coz', 'asap', 'lol'), informal colloquialisms ('totally busted', 'proper joke', 'Cheers')", "[A1]"),
                ("2. Explain: Lacks professional respect, undermines urgency, and fails NHS written communication standards", "[M1]"),
                ("3. Provide polished model rewrite with formal salutation, concise explanation of the issue, business impact, and polite sign-off", "[A1]"),
                ("4. Flawless SPaG throughout model response", "[A1]")
            ],
            "final_answer": "Critique: Unprofessional slang ('u', 'coz', 'lol'), casual greeting ('Hey'), colloquial tone ('proper joke'). Rewrite: 'Dear Dr Patel, I am writing to report that the printer in Ward 2 has malfunctioned again. This is causing significant administrative delays with patient handover sheets. Could you please authorize an urgent engineer callout or replacement? Kind regards, David Miller.'",
            "pitfall": "Rewriting in semi-formal tone while still using contractions or vague requests.",
            "reverse_check": "Model uses formal salutation ('Dear Dr Patel'), full sentences, professional tone, and courteous sign-off."
        }
    ),
    # 2. Perfecting Punctuation
    make_english_topic(
        slug="writing-perfecting-your-punctuation",
        title="Punctuation Mastery",
        category="writing",
        spec_codes="L1.25 • L2.23",
        golden_rule="Punctuation controls pace and clarity. Master capital letters for proper nouns/sentence starts, apostrophes for possession vs contraction, commas for introductory clauses and items in lists, and colons/semicolons for advanced sentence architecture.",
        q1={
            "title": "Question 1 (Level 1 Apostrophes for Possession vs Contraction)",
            "marks": 2,
            "stem": "Insert the apostrophe in the correct position in each sentence:<br>1. <em>The doctors stethoscope was left in consultation room 4.</em> (One doctor)<br>2. <em>Its essential that all staff wear photo identification badges.</em>",
            "lines": 3,
            "ans_label": "Punctuation correction =",
            "choice_box": "1: ____________________ | 2: ____________________",
            "step_rows": [
                ("1. Singular possession: 'The doctor's stethoscope...'", "[A1]"),
                ("2. Contraction of 'it is': 'It's essential that...'", "[A1]")
            ],
            "final_answer": "1. doctor's; 2. It's",
            "pitfall": "Using 'doctors'' (plural possession) or confusing possessive 'its' with contraction 'it's'.",
            "reverse_check": "1 doctor owns stethoscope = doctor's. 'It is essential' contracts to It's."
        },
        q2={
            "title": "Question 2 (Level 2 Colons & Semicolons)",
            "marks": 2,
            "stem": "Punctuate the sentence below using <strong>one colon</strong> and <strong>one semicolon</strong>:<br><em>'The inspection team audited three essential wards Ward 2, Ward 5, and Ward 9 all three passed with outstanding ratings.'</em>",
            "lines": 3,
            "ans_label": "Punctuated sentence =",
            "choice_box": "________________________________________________________",
            "step_rows": [
                ("1. Insert colon to introduce the list: '...three essential wards: Ward 2, Ward 5, and Ward 9...'", "[M1]"),
                ("2. Insert semicolon to join closely related independent clause: '...and Ward 9; all three passed with outstanding ratings.'", "[A1]")
            ],
            "final_answer": "The inspection team audited three essential wards: Ward 2, Ward 5, and Ward 9; all three passed with outstanding ratings.",
            "pitfall": "Swapping the positions of colon and semicolon.",
            "reverse_check": "Colon introduces the specific list; semicolon links the outcome clause."
        },
        q3={
            "title": "Question 3 (Level 1 Commas in Lists and Introductory Clauses)",
            "marks": 3,
            "stem": "Insert all missing punctuation (commas and full stops) into the following sentence:<br><em>'Before administering any medication the staff nurse verified the patient name date of birth allergy status and hospital number'</em>",
            "lines": 4,
            "ans_label": "Punctuated sentence =",
            "choice_box": "________________________________________________________",
            "step_rows": [
                ("1. Comma after introductory dependent clause: 'Before administering any medication, ...'", "[A1]"),
                ("2. Commas separating list items: '...patient name, date of birth, allergy status, ...'", "[A1]"),
                ("3. Full stop at the end: '...and hospital number.'", "[A1]")
            ],
            "final_answer": "Before administering any medication, the staff nurse verified the patient name, date of birth, allergy status and hospital number.",
            "pitfall": "Omitting the comma after the introductory clause 'Before administering any medication'.",
            "reverse_check": "Introductory clause separated by comma; list items punctuated; terminal full stop present."
        },
        q4={
            "title": "Question 4 (Level 2 Direct Speech and Quotation Punctuation)",
            "marks": 3,
            "stem": "Punctuate the direct speech sentence accurately:<br><em>the ward sister announced all visitors must sanitize their hands before entering</em>",
            "lines": 4,
            "ans_label": "Punctuated direct speech =",
            "choice_box": "________________________________________________________",
            "step_rows": [
                ("1. Capitalize first letter: 'The ward sister announced, ...'", "[A1]"),
                ("2. Comma before opening speech marks: 'announced, \"...\"'", "[A1]"),
                ("3. Capitalize first word inside speech marks and place full stop inside closing marks: '...announced, \"All visitors must sanitize their hands before entering.\"'", "[A1]")
            ],
            "final_answer": "The ward sister announced, \"All visitors must sanitize their hands before entering.\"",
            "pitfall": "Placing the full stop outside the closing quotation marks or omitting the introductory comma.",
            "reverse_check": "Speech marks enclose spoken words; punctuation sits inside quotation marks."
        },
        q5={
            "title": "Question 5 (Level 2 Proofreading Punctuation in a Policy Notice)",
            "marks": 4,
            "stem": "A junior administrator drafts a staff notice containing <strong>four distinct punctuation errors</strong>:<br><em>'emergency equipment must be checked daily. At 08:00 every morning the duty nurses inspect the defibrillators pads, batteries and oxygen supply its vital that no checks are missed'</em><br><br>Identify and correct all four punctuation errors.",
            "lines": 5,
            "ans_label": "Four Corrections =",
            "choice_box": "1: ________ | 2: ________ | 3: ________ | 4: ________",
            "step_rows": [
                ("1. Capital letter missing at start: 'Emergency equipment...'", "[A1]"),
                ("2. Comma after introductory time phrase: 'At 08:00 every morning, ...'", "[A1]"),
                ("3. Plural possession apostrophe on defibrillators: '...defibrillator's pads...' (or defibrillators' pads)", "[A1]"),
                ("4. Run-on sentence / missing apostrophe: Full stop before 'It's' OR semicolon + contraction apostrophe: '...oxygen supply. It's vital...'", "[A1]")
            ],
            "final_answer": "1. Capital 'E' for Emergency; 2. Comma after 08:00 every morning; 3. Defibrillator's pads; 4. Full stop after supply and apostrophe in It's.",
            "pitfall": "Missing the run-on sentence between 'oxygen supply' and 'its vital'.",
            "reverse_check": "Corrected text flows clearly with proper capitals, clause breaks, and apostrophes."
        },
        q6={
            "title": "Question 6 (Level 2 Ambiguity Caused by Missing Commas)",
            "marks": 4,
            "stem": "Explain how the presence or absence of a comma drastically alters the meaning in these two sentences:<br>Sentence A: <em>'The surgeon said the patient had died.'</em><br>Sentence B: <em>'The surgeon, said the patient, had died.'</em><br><br>Explain who died in Sentence A versus who died in Sentence B.<br>Explain what grammatical role the commas play in Sentence B.",
            "lines": 5,
            "ans_label": "Explanation of meaning =",
            "choice_box": "Sentence A meaning: ____________ | Sentence B meaning: ____________",
            "step_rows": [
                ("1. Sentence A meaning: The surgeon is speaking/reporting that the patient is deceased (the patient died).", "[M1]"),
                ("2. Sentence B meaning: The patient is speaking/reporting that the surgeon is deceased (the surgeon died).", "[M1]"),
                ("3. Grammatical role: In Sentence B, the commas enclose a parenthetical reporting clause ('said the patient'), making 'The surgeon... had died' the main clause.", "[A1]"),
                ("4. Clear, precise conclusion demonstrating understanding of how commas establish clause boundaries", "[A1]")
            ],
            "final_answer": "In Sentence A the patient died (surgeon speaks). In Sentence B the surgeon died (patient speaks). The commas enclose a parenthetical reporting clause.",
            "pitfall": "Thinking both sentences mean the same thing, missing the dramatic reversal of who died.",
            "reverse_check": "Read without parenthetical commas: Sentence B is 'The surgeon had died.'"
        }
    )
]

print(f"Loaded {len(CATALOG_ENGLISH_WRITING)} topics in catalog_english_writing.py")
