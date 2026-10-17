#!/usr/bin/env python3
"""
Catalog English Reading: 13 Core Reading Standards.
Covers Fact vs Opinion, Language Features, Presentational Devices, Comparing Texts, Bias & Purpose.
"""
from build_topic_dataset import make_english_topic

CATALOG_ENGLISH_READING = [
    # 1. Fact or Opinion
    make_english_topic(
        slug="reading-fact-or-opinion",
        title="Fact or Opinion",
        category="reading",
        spec_codes="L1.13 • L2.11",
        golden_rule="A FACT is a statement that can be proven true or false with objective evidence, statistics, dates, or measurements. An OPINION is a personal belief, viewpoint, or subjective judgment that contains emotive adjectives (e.g. 'wonderful', 'worst', 'unacceptable') and cannot be scientifically verified.",
        q1={
            "title": "Question 1 (Level 1 Fact Identification)",
            "marks": 2,
            "stem": "Read the following statements from a hospital newsletter:<br>1. <em>'The new outpatient wing opened on 14th September with 24 consultation rooms.'</em><br>2. <em>'The interior design of the waiting lounge is the most soothing in the entire county.'</em><br><br>Identify which statement is a <strong>fact</strong> and which is an <strong>opinion</strong>. Give one reason for each.",
            "lines": 3,
            "ans_label": "Classification & Reason =",
            "choice_box": "Statement 1: ________________ | Statement 2: ________________",
            "step_rows": [
                ("1. Statement 1 is a FACT: Contains verifiable date (14th Sept) and room count (24)", "[A1]"),
                ("2. Statement 2 is an OPINION: 'Most soothing' is subjective value judgment that cannot be proven", "[A1]")
            ],
            "final_answer": "Statement 1 is a Fact; Statement 2 is an Opinion",
            "pitfall": "Confusing opinion with fact when an opinion sounds authoritative or confident.",
            "reverse_check": "Can Statement 1 be checked against official records? Yes. Can 'most soothing' be proven? No."
        },
        q2={
            "title": "Question 2 (Level 2 Fact vs Opinion in a Workplace Email)",
            "marks": 2,
            "stem": "An estates officer emails staff:<br><em>'Our energy consumption dropped by 18% following the installation of smart sensors. Everyone agrees that the new system is far superior to our previous heating setup.'</em><br><br>Extract <strong>one fact</strong> and <strong>one opinion</strong> from the email excerpt.",
            "lines": 3,
            "ans_label": "Extracted statements =",
            "choice_box": "Fact: ________________ | Opinion: ________________",
            "step_rows": [
                ("1. Fact: 'energy consumption dropped by 18%' (measurable statistic)", "[A1]"),
                ("2. Opinion: 'Everyone agrees that the new system is far superior' (unsubstantiated generalization / subjective)", "[A1]")
            ],
            "final_answer": "Fact: 18% energy drop; Opinion: New system is far superior",
            "pitfall": "Quoting the whole sentence instead of identifying the exact factual vs opinion phrase.",
            "reverse_check": "18% is a measurable data point (fact); 'far superior' is an evaluative judgment (opinion)."
        },
        q3={
            "title": "Question 3 (Level 1 Healthcare Campaign Text Analysis)",
            "marks": 3,
            "stem": "Read this paragraph from a staff wellness campaign:<br><em>'Over 450 nurses attended our mindfulness workshop last month. Mental fatigue is an intolerable burden that destroys workplace productivity. The workshop ran for 45 minutes and offered practical breathing techniques.'</em><br><br>Identify <strong>two facts</strong> and <strong>one opinion</strong> from the text.",
            "lines": 4,
            "ans_label": "Classified sentences =",
            "choice_box": "Facts: (1) ________________ (2) ________________ | Opinion: ________________",
            "step_rows": [
                ("1. Fact 1: 'Over 450 nurses attended our mindfulness workshop last month'", "[A1]"),
                ("2. Fact 2: 'The workshop ran for 45 minutes and offered practical breathing techniques'", "[A1]"),
                ("3. Opinion: 'Mental fatigue is an intolerable burden that destroys workplace productivity' (emotive adjectives 'intolerable')", "[A1]")
            ],
            "final_answer": "Facts: 450 nurses attended; ran for 45 minutes. Opinion: Intolerable burden that destroys productivity.",
            "pitfall": "Assuming 'practical techniques' makes the last sentence an opinion; the primary clause is factual.",
            "reverse_check": "450 nurses and 45 minutes are verifiable records."
        },
        q4={
            "title": "Question 4 (Level 2 Identifying Opinion Disguised as Fact)",
            "marks": 3,
            "stem": "A union newsletter writes:<br><em>'It is an undeniable truth that management's parking charge increase is an unfair penalty on dedicated staff who arrive at 6:30 am.'</em><br><br>Explain why the phrase <em>'It is an undeniable truth that...'</em> does <strong>not</strong> make the statement a factual claim.<br>Identify the subjective language that confirms it is an opinion.",
            "lines": 4,
            "ans_label": "Explanation & Subjective words =",
            "choice_box": "Explanation: ________________ | Words: ________________",
            "step_rows": [
                ("1. Explain: The writer uses rhetorical assertion ('undeniable truth') to present a subjective viewpoint as indisputable", "[P1]"),
                ("2. Identify subjective word: 'unfair penalty' (evaluative opinion on fairness)", "[A1]"),
                ("3. Identify subjective word: 'dedicated staff' (value judgment)", "[A1]")
            ],
            "final_answer": "Assertion does not equal evidence; 'unfair penalty' and 'dedicated' are subjective value judgments.",
            "pitfall": "Believing that statements beginning with 'The fact is...' or 'It is true that...' are automatically factual.",
            "reverse_check": "'Unfair' cannot be measured scientifically or proven in court without policy definition."
        },
        q5={
            "title": "Question 5 (Level 2 Paired Text Analysis - Fact vs Opinion)",
            "marks": 4,
            "stem": "<strong>Text A (Trust Official Policy):</strong><br><em>'The hospital shuttle bus operates every 15 minutes between 06:00 and 22:00, carrying an average of 1,200 passengers daily at a standard return fare of £1.50.'</em><br><br><strong>Text B (User Feedback Forum):</strong><br><em>'The shuttle service is utterly unreliable and always dangerously packed during morning handovers. The £1.50 ticket price is extortionate for junior apprentices.'</em><br><br>Compare Text A and Text B. Identify two facts in Text A and two opinions in Text B.",
            "lines": 5,
            "ans_label": "Comparative Analysis =",
            "choice_box": "Text A Facts: (1) ____________ (2) ____________ | Text B Opinions: (1) ____________ (2) ____________",
            "step_rows": [
                ("1. Text A Fact 1: 'operates every 15 minutes between 06:00 and 22:00'", "[A1]"),
                ("2. Text A Fact 2: 'carrying average 1,200 passengers daily' OR 'fare of £1.50'", "[A1]"),
                ("3. Text B Opinion 1: 'utterly unreliable and always dangerously packed' (exaggeration/hyperbole)", "[A1]"),
                ("4. Text B Opinion 2: 'ticket price is extortionate' (subjective judgment)", "[A1]")
            ],
            "final_answer": "Text A Facts: Frequency (15 mins/06:00-22:00) & Passenger count (1,200). Text B Opinions: 'utterly unreliable' & 'extortionate'.",
            "pitfall": "Mixing up the sources or classifying £1.50 in Text B as an opinion rather than 'extortionate'.",
            "reverse_check": "Text A provides verifiable operational parameters; Text B provides emotional user sentiment."
        },
        q6={
            "title": "Question 6 (Level 2 Author Bias Evaluation & Justification)",
            "marks": 4,
            "stem": "A journalist writes: <em>'The council's disgraceful waste disposal policy has completely ruined local tourism, proving that councillors care nothing for residents.'</em><br><br>A reader complains: <em>'This article is biased and presents personal opinions as proven facts.'</em><br><br>Is the reader's complaint justified?<br>Analyse the language used by the journalist, cite at least two pieces of evidence from the text, and give a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Text Evidence =",
            "choice_box": "Justified / Not Justified: Evidence 1: ________ | Evidence 2: ________",
            "step_rows": [
                ("1. State clear conclusion: <strong>Yes, the reader's complaint is fully justified</strong>", "[A1]"),
                ("2. Evidence 1: Use of biased, emotive adjective 'disgraceful' to describe the policy without explaining its details", "[M1]"),
                ("3. Evidence 2: Extreme hyperbole 'completely ruined local tourism' without citing any visitor statistics or revenue data", "[M1]"),
                ("4. Evidence 3: Sweeping, unproven claim about motives ('councillors care nothing for residents')", "[A1]")
            ],
            "final_answer": "Justified (Uses emotive language 'disgraceful', unsubstantiated hyperbole 'completely ruined', and unsupported assumption of motives)",
            "pitfall": "Writing 'Yes' without directly quoting and analysing the specific words used by the journalist.",
            "reverse_check": "None of the claims cite statistical evidence or balanced opposing council perspectives."
        }
    ),
    # 2. Language Features
    make_english_topic(
        slug="reading-language-features",
        title="Language Features & Devices",
        category="reading",
        spec_codes="L1.15 • L2.13",
        golden_rule="Writers use language devices (PERSUASIVE: Rhetorical questions, Emotive words, Statistics, Rule of three, Direct address 'you', Alliteration, Hyperbole) to create specific effects on the reader. Always identify the device AND explain its intended impact.",
        q1={
            "title": "Question 1 (Level 1 Identifying Persuasive Devices)",
            "marks": 2,
            "stem": "Match the excerpt with the correct language technique:<br>A. <em>'Over 85% of healthcare workers surveyed support flexible shift scheduling.'</em><br>B. <em>'Can you afford to ignore the warning signs of burnout?'</em><br><br>Techniques: <strong>Statistic / Fact &nbsp;|&nbsp; Rhetorical Question &nbsp;|&nbsp; Emotive Language</strong>",
            "lines": 3,
            "ans_label": "Matched Techniques =",
            "choice_box": "A: ____________________ | B: ____________________",
            "step_rows": [
                ("1. Excerpt A matches: Statistic / Numerical Fact (85%)", "[A1]"),
                ("2. Excerpt B matches: Rhetorical Question (question requiring self-reflection, not direct answer)", "[A1]")
            ],
            "final_answer": "A: Statistic / Fact; B: Rhetorical Question",
            "pitfall": "Confusing a direct question with a rhetorical question.",
            "reverse_check": "A has numbers (statistic); B has a question mark engaging the reader without expecting reply."
        },
        q2={
            "title": "Question 2 (Level 2 Rule of Three & Emotive Language)",
            "marks": 2,
            "stem": "Read this campaign slogan: <em>'Together we can build a safer, cleaner, and healthier clinic for every patient.'</em><br><br>Identify the language technique used and explain its effect on the reader.",
            "lines": 3,
            "ans_label": "Technique & Effect =",
            "choice_box": "Technique: ________________ | Effect: ________________",
            "step_rows": [
                ("1. Technique: Rule of three (triad) / three complementary adjectives", "[A1]"),
                ("2. Effect: Creates a memorable rhythm, reinforces key priorities, and persuades the reader that improvement is comprehensive", "[A1]")
            ],
            "final_answer": "Technique: Rule of three; Effect: Makes the vision memorable, rhythmic, and persuasive.",
            "pitfall": "Simply naming the technique without explaining how it influences the reader's feelings or thoughts.",
            "reverse_check": "'Safer, cleaner, healthier' are three parallel comparative adjectives."
        },
        q3={
            "title": "Question 3 (Level 1 Direct Address & Call to Action)",
            "marks": 3,
            "stem": "An infection prevention poster states:<br><em>'Clean hands save lives. Every time you wash your hands, you protect a vulnerable patient. Join our ward safety champion team today!'</em><br><br>Identify <strong>two language features</strong> used in this text and quote an example of each.",
            "lines": 4,
            "ans_label": "Techniques & Quotes =",
            "choice_box": "Feature 1: ________________ (Quote: ____________) | Feature 2: ________________ (Quote: ____________)",
            "step_rows": [
                ("1. Feature 1: Direct address ('you', 'your hands') - personalises the responsibility", "[A1]"),
                ("2. Feature 2: Imperative / Command / Call to action ('Join our ward safety champion team today!')", "[A1]"),
                ("3. Alternative Feature: Alliteration or punchy slogan ('Clean hands save lives')", "[A1]")
            ],
            "final_answer": "Direct address ('you') and Imperative / Call to action ('Join our ward safety champion team today!')",
            "pitfall": "Quoting text without naming the language feature.",
            "reverse_check": "'You' directly engages reader; 'Join' is an imperative verb."
        },
        q4={
            "title": "Question 4 (Level 2 Hyperbole and Emotive Tone)",
            "marks": 3,
            "stem": "A patient charity leaflet writes:<br><em>'Waiting four agonizing hours in a freezing corridor is an absolute nightmare that tears families apart.'</em><br><br>Identify <strong>two emotive words</strong> and <strong>one example of exaggeration (hyperbole)</strong> in the sentence.",
            "lines": 4,
            "ans_label": "Identified Language =",
            "choice_box": "Emotive words: (1) ________ (2) ________ | Hyperbole: ________________",
            "step_rows": [
                ("1. Emotive word 1: 'agonizing' (or 'freezing')", "[A1]"),
                ("2. Emotive word 2: 'nightmare'", "[A1]"),
                ("3. Hyperbole: 'tears families apart' (or 'absolute nightmare')", "[A1]")
            ],
            "final_answer": "Emotive words: 'agonizing', 'nightmare'; Hyperbole: 'tears families apart'",
            "pitfall": "Choosing 'four hours' as hyperbole when that is a literal measurement of time.",
            "reverse_check": "'Tears families apart' exaggerates the effect of a corridor wait for emotional impact."
        },
        q5={
            "title": "Question 5 (Level 2 Text Comparison - Persuasive Impact)",
            "marks": 4,
            "stem": "<strong>Text A (Formal Trust Notice):</strong><br><em>'Flu vaccination clinics operate weekdays in Seminar Room 2. Evidence demonstrates vaccination reduces seasonal staff absenteeism by 32%.'</em><br><br><strong>Text B (Staff Union Poster):</strong><br><em>'Don't bring the flu home to your loved ones! Protect your family, shield your patients, and safeguard your colleagues. Get jabbed this week!'</em><br><br>Compare the different language techniques used in Text A and Text B to encourage staff vaccination.<br>Give at least two specific language features from each text.",
            "lines": 5,
            "ans_label": "Comparative Language Features =",
            "choice_box": "Text A Devices: ________________ | Text B Devices: ________________",
            "step_rows": [
                ("1. Text A Device 1: Statistical evidence ('reduces absenteeism by 32%')", "[A1]"),
                ("2. Text A Device 2: Formal, neutral informative tone / factual statements without emotional bias", "[A1]"),
                ("3. Text B Device 1: Rule of three with parallel verbs ('Protect your family, shield your patients, safeguard your colleagues')", "[A1]"),
                ("4. Text B Device 2: Emotive appeal / personal direct address ('your loved ones') and imperative command ('Get jabbed this week!')", "[A1]")
            ],
            "final_answer": "Text A uses statistics and neutral informative tone; Text B uses rule of three, emotional appeal to family, and imperatives.",
            "pitfall": "Describing what the texts are about rather than analysing the language devices used.",
            "reverse_check": "Text A appeals to logic/data; Text B appeals to emotion, duty, and protective instincts."
        },
        q6={
            "title": "Question 6 (Level 2 Writer's Perspective & Technique Evaluation)",
            "marks": 4,
            "stem": "An apprentice blogger writes:<br><em>'Is it fair that apprentice nurses shoulder enormous clinical responsibilities while surviving on poverty wages? We are the beating heart of our hospitals, yet we are cast aside like disposable instruments.'</em><br><br>Analyse how the writer uses language to position the reader to support higher apprentice wages.<br>Identify two distinct techniques, quote evidence, and explain their persuasive effect.",
            "lines": 5,
            "ans_label": "Techniques, Evidence & Effect =",
            "choice_box": "Technique 1 & Effect: ________________ | Technique 2 & Effect: ________________",
            "step_rows": [
                ("1. Technique 1: Rhetorical question with emotive vocabulary ('Is it fair that... poverty wages?'). Effect: Provokes reader indignation and moral discomfort, forcing the reader to agree that current pay is unjust.", "[M1]"),
                ("2. Quote 1 provided accurately and linked to effect", "[A1]"),
                ("3. Technique 2: Metaphor and Simile ('beating heart of our hospitals', 'cast aside like disposable instruments'). Effect: Emphasizes vital clinical necessity while contrasting it sharply with feeling undervalued and exploited.", "[M1]"),
                ("4. Quote 2 provided accurately and linked to effect", "[A1]")
            ],
            "final_answer": "Rhetorical question provokes moral indignation; Metaphor ('beating heart') and Simile ('like disposable instruments') dramatise mistreatment.",
            "pitfall": "Vague comments like 'it makes the reader feel bad' without identifying metaphor, rhetorical question, or emotive diction.",
            "reverse_check": "The rhetorical devices create a contrast between noble clinical work and unfair compensation."
        }
    )
]

print(f"Loaded {len(CATALOG_ENGLISH_READING)} topics in catalog_english_reading.py")
