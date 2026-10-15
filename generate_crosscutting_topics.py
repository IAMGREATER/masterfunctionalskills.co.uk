#!/usr/bin/env python3
import sys

CROSSCUTTING_TOPICS = [
    {
        "filename": "piecing-it-together-key-and-detailed-points.html",
        "clean_topic": "Key vs Detailed Points in Reading & Writing",
        "intro_lead": "Learn to distinguish overarching central arguments from minor supporting details, enabling rapid information retrieval and cohesive, well-supported analytical answers in Functional Skills assessments.",
        "next_file": "piecing-it-together-comparing-texts.html",
        "next_name": "Comparing Texts & Cross-Text Synthesis",
        "spec_points": [
            ("L1.8 / L2.8", "Identify different types of text and extract main points and supporting detail."),
            ("L2.12", "Synthesise information and arguments from different authorities and sources.")
        ],
        "golden_rules": [
            {
                "icon": "fa-tree",
                "title": "Golden Rule 1: The Trunk vs Branch Analogy",
                "desc": "The main point is the tree trunk — the core message the author wants you to remember. Detailed points are the branches — specific dates, statistics, case examples, or quotes that support that trunk.",
                "badge": "Main Point = Core Message | Detailed Point = Evidence / Example"
            },
            {
                "icon": "fa-highlighter",
                "title": "Golden Rule 2: In Writing, Every Paragraph Needs Both",
                "desc": "A strong functional paragraph starts with a topic sentence stating the main point, followed by 2–3 detailed points containing specific evidence or procedural steps.",
                "badge": "Topic Sentence (Main Point) + Supporting Details (Evidence/Steps)"
            }
        ],
        "skills": [
            {
                "title": "Main Point vs Supporting Detail Comparison",
                "summary": "How to classify information quickly under exam time constraints.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Feature</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Main / Key Point</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Detailed / Supporting Point</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Function</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Expresses the overarching argument or policy goal.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Provides specific proof, times, names, or measurements.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Location</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">First or final sentence of a paragraph, headlines, summaries.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Middle of paragraphs, bulleted lists, sub-clauses.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Healthcare Example</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Hand hygiene compliance must improve to reduce MRSA transmission."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Rub hands with alcohol gel for 20 seconds using the 6-step WHO technique."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "NHS Trust Waste Audit Analysis",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Environmental Healthcare Management",
                "question": "Read the extract from the hospital facilities report:<br><em>'Clinical waste disposal costs reached £420,000 last year due to widespread misclassification. Staff frequently discard non-contaminated packaging into orange clinical waste sacks rather than domestic clear bags, inflating disposal tariffs by £180 per tonne.'</em><br>(a) Identify the main point of this extract.<br>(b) Identify two supporting detailed points.",
                "steps": [
                    ("Step 1", "Identify the central overarching point", "The main point is that clinical waste disposal costs have risen significantly (£420k) due to incorrect waste classification by staff.", "1 Mark (A1 Main Point)"),
                    ("Step 2", "Identify Supporting Detail 1", "Staff discard non-contaminated packaging into orange clinical waste bags instead of clear domestic bags.", "1 Mark (A1 Detail 1)"),
                    ("Step 3", "Identify Supporting Detail 2", "This misclassification inflates disposal tariffs by £180 per tonne.", "1 Mark (A1 Detail 2)")
                ],
                "final_answer": "Main Point: Misclassification of waste has driven clinical disposal costs to £420,000. Supporting Details: 1. Staff put non-contaminated packaging into orange sacks. 2. This raises costs by £180 per tonne.",
                "tutor_tip": "Do not confuse the cost penalty (£180/tonne) with the overall message. The penalty is a detail proving why the overall problem is serious."
            }
        ],
        "examiner_traps": [
            {
                "title": "Quoting a Detail When Asked for the Main Idea",
                "desc": "If a question asks 'What is the main message of Text A?', giving a specific statistic like '£180 per tonne' scores zero because it represents only one detail.",
                "fix": "Ask yourself: 'What is the headline takeaway of the entire text?'"
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics newsletter states: <em>'Fleet electrification has achieved substantial operational savings across our Midland depots. By replacing 25 diesel vans with Nissan Townstar EVs, depot fuel costs fell by 42% over six months, while tailpipe emissions decreased by 18 tonnes.'</em><br>Identify one main point and one detailed supporting point.",
                "solution_steps": "Main Point: Fleet electrification has generated major operational savings across Midland depots.<br>Detailed Point: Fuel costs fell by 42% OR tailpipe emissions dropped by 18 tonnes.",
                "correct_answer": "Main: Electrification brought operational savings | Detail: 42% fuel drop / 18 tonnes emission reduction.",
                "tutor_tip": "Extract the broad statement of success as the main point and the exact percentage or metric as the detail."
            }
        ]
    },
    {
        "filename": "piecing-it-together-comparing-texts.html",
        "clean_topic": "Comparing Texts & Cross-Text Synthesis",
        "intro_lead": "Master cross-text analysis for Level 2 Functional Skills English: extract contrasting viewpoints, compare presentational techniques, and synthesize evidence using comparison matrices.",
        "next_file": "formality-and-bias.html",
        "next_name": "Formality, Register & Detecting Bias",
        "spec_points": [
            ("L2.12", "Compare information, ideas, and of perspectives across two extended texts."),
            ("L2.13", "Synthesise information and arguments from different authorities and sources.")
        ],
        "golden_rules": [
            {
                "icon": "fa-code-compare",
                "title": "Golden Rule 1: Always Anchor Comparisons with Connectives",
                "desc": "Never write about Text A in isolation and then Text B in isolation. Weave them together using comparative connectives ('similarly', 'in contrast', 'whereas', 'on the other hand').",
                "badge": "Text A Point + Comparative Connective + Text B Point"
            },
            {
                "icon": "fa-table-columns",
                "title": "Golden Rule 2: Compare Ideas, Presentation, and Tone",
                "desc": "Functional Skills Level 2 questions frequently ask you to compare how two texts present the same issue. Compare factual content, visual layout features, and author tone.",
                "badge": "Content (What) • Layout (How it looks) • Tone (How it sounds)"
            }
        ],
        "skills": [
            {
                "title": "The Cross-Text Synthesis Matrix",
                "summary": "The rapid planning grid to structure 4-mark and 6-mark comparative exam answers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Comparison Dimension</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Text A (e.g. Official Policy Document)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">Text B (e.g. Staff Blog / Forum Post)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Purpose &amp; Stance</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To inform and mandate; authoritative, objective tone.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To express personal experience; informal, emotive tone.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Layout Devices</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Numbered clauses, bold statutory headings, tables of data.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">First-person narrative, rhetorical questions, exclamation marks.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Evidence Used</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Official regulatory statistics, legal statutes (HSE, CQC).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Individual personal workplace anecdotes, opinions.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Comparing Two Texts on 12-Hour Hospital Shifts",
                "marks": "4 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Shift Scheduling Analysis",
                "question": "Text A is a management circular arguing that 12-hour shifts improve continuity of patient care. Text B is a nursing union article warning of clinical burnout. Compare how the two texts convey their perspectives.",
                "steps": [
                    ("Step 1", "Compare Central Message with connective", "Both texts focus on 12-hour nursing shifts; however, while Text A promotes the model by citing a 15% reduction in handover errors, Text B opposes it, highlighting that chronic nurse fatigue doubles medication administration errors after 10 hours.", "2 Marks (Content Comparison)"),
                    ("Step 2", "Compare Tone and Register with connective", "Text A adopts an objective, formal corporate tone using professional terminology like 'operational continuity'. In contrast, Text B employs an emotive, urgent tone with rhetorical questions such as 'Can tired staff keep patients safe?' to rally union members.", "2 Marks (Tone & Language Comparison)")
                ],
                "final_answer": "Complete 4-mark response contrasting factual claims, statistical evidence, and the writer's tone using explicit comparative connectives ('however', 'in contrast').",
                "tutor_tip": "Always mention BOTH texts in EVERY comparative paragraph. If you write only about Text A in paragraph 1 and Text B in paragraph 2 without cross-referencing, examiners cap your mark."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Separate Summaries Without Direct Comparison",
                "desc": "Writing two separate summaries with no linking connectives prevents you from demonstrating synthesis.",
                "fix": "Use sentence frames: 'While Text A argues [X], Text B contends that [Y]. Furthermore, whereas Text A relies on [Z], Text B utilizes [W].'"
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Text 1 is a council press release announcing new parking charges. Text 2 is a petition from local high-street shopkeepers. Identify one similarity and two differences in how the texts present the issue of town center parking.",
                "solution_steps": "Similarity: Both texts agree that town center parking spaces are heavily congested during business hours.<br>Difference 1 (Stance): Text 1 argues charges will increase turnover and reduce emissions, whereas Text 2 claims fees will drive shoppers to out-of-town retail parks.<br>Difference 2 (Format): Text 1 uses formal subheadings and official council statistics, whereas Text 2 uses emotive quotes and direct appeals to sign the petition.",
                "correct_answer": "1 similarity + 2 contrasted differences covering stance and formatting.",
                "tutor_tip": "Ensure you clearly label which text is which and highlight comparative words."
            }
        ]
    },
    {
        "filename": "formality-and-bias.html",
        "clean_topic": "Formality, Register & Detecting Bias",
        "intro_lead": "Analyze author objectivity, detect overt and covert bias, and master register calibration between formal workplace communications and informal dialogue.",
        "next_file": "common-mistakes.html",
        "next_name": "Common Pitfalls & High-Frequency Exam Mistakes",
        "spec_points": [
            ("L2.14", "Recognise bias and determine whether statements represent verifiable facts or subjective interpretation."),
            ("L1.2 / L2.6", "Use appropriate language and register suitable for purpose, subject, and audience.")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-unbalanced",
                "title": "Golden Rule 1: Bias Stems from Selective Evidence and Loaded Language",
                "desc": "An author is biased if they present only one side of an argument, suppress counter-evidence, or use emotive, loaded adjectives designed to sway the reader's emotions.",
                "badge": "Signs of Bias: One-sided data • Loaded adjectives • Exaggerated claims"
            },
            {
                "icon": "fa-user-tie",
                "title": "Golden Rule 2: Match Formality to Professional Hierarchy",
                "desc": "Formal writing avoids colloquialisms, contractions ('don't' -> 'do not'), and slang. It uses passive voice appropriately, precise specialist terminology, and polite salutations.",
                "badge": "Formal: No contractions • Impersonal tone • Precise terminology"
            }
        ],
        "skills": [
            {
                "title": "Detecting Subtle / Covert Bias in Professional Texts",
                "summary": "Three forensic reading tests to expose author bias in vocational reports.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Check Commercial or Vested Interest:</strong> Who funded the article? If a private agency produces a report stating NHS bank nursing is inefficient, they have an obvious financial incentive to sell private locum staff.</li>
                    <li><strong>Inspect Adjective Choices (Loaded Words):</strong> Does the author write <em>"The reasonable proposal was reviewed"</em> or <em>"The draconian scheme was forced through"</em>? Evaluative adjectives expose emotional bias.</li>
                    <li><strong>Look for Cherry-Picked Data:</strong> Does the text cite only positive feedback while burying negative statistics in footnotes? A balanced text always acknowledges counter-arguments.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Auditing a Commercial Software Pitch for Bias",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Procurement Appraisal",
                "question": "Read the promotional flyer from MedTech Solutions:<br><em>'Our revolutionary CareFlow tablet system is unquestionably the most advanced clinical app ever built. Outdated paper systems are a catastrophic waste of taxpayer funds, and any care home that fails to install CareFlow immediately is putting residents at risk.'</em><br>Identify two examples of bias in this extract and explain why the text cannot be considered an objective assessment.",
                "steps": [
                    ("Step 1", "Identify Example 1 of Bias (Hyperbolic / Superlative Language)", "'Unquestionably the most advanced clinical app ever built' — this is an unverified commercial superlative designed to sell the product.", "1 Mark (A1 Bias Example 1)"),
                    ("Step 2", "Identify Example 2 of Bias (Loaded / Fear-Inducing Adjectives)", "'Catastrophic waste' and claiming homes not buying it are 'putting residents at risk' — uses emotionally manipulative fear tactics.", "1 Mark (A1 Bias Example 2)"),
                    ("Step 3", "Explain why the text lacks objectivity", "The text is written by a vendor with a commercial profit motive. It provides zero comparative clinical trial data and dismisses all alternative solutions with emotional hyperbole.", "1 Mark (A1 Objective Explanation)")
                ],
                "final_answer": "Bias 1: Commercial superlative 'unquestionably the most advanced'. Bias 2: Manipulative fear phrasing 'putting residents at risk'. Reason: Written by a commercial seller lacking objective trial data.",
                "tutor_tip": "In Functional Skills Reading, linking the author's commercial motive to their choice of loaded words secures maximum marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming Any Strong Argument is Biased",
                "desc": "An argument is NOT automatically biased just because the author takes a strong stance, provided they support it with fair, verifiable data from both sides.",
                "fix": "Look for unfair suppression of facts or emotionally loaded language before declaring a text biased."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A trade union newsletter states: <em>'Greedy depot bosses are deliberately slashing shift allowances to line their own pockets.'</em><br>Explain how the writer's language indicates bias in this sentence.",
                "solution_steps": "1. Pejorative loaded language: The author uses emotive, insulting adjectives ('greedy') and verbs ('slashing') to demonize management.<br>2. Subjective assumption: The writer claims bosses act 'to line their own pockets' without providing financial audit evidence.",
                "correct_answer": "Uses emotive loaded vocabulary ('greedy', 'slashing') and unsubstantiated personal motives.",
                "tutor_tip": "Always quote the exact loaded words in your answer."
            }
        ]
    },
    {
        "filename": "common-mistakes.html",
        "clean_topic": "Top 10 High-Frequency English Exam Mistakes & Fixes",
        "intro_lead": "A definitive guide to the ten most catastrophic exam pitfalls that cost Functional Skills candidates valuable marks in Reading, Writing, and SLC — and the exact steps to avoid them.",
        "next_file": "detecting-language-techniques.html",
        "next_name": "Detecting Language Techniques & Rhetorical Devices",
        "spec_points": [
            ("L1 / L2 Universal Standards", "Spelling, punctuation, grammar, reading comprehension, and format conventions across all awarding bodies.")
        ],
        "golden_rules": [
            {
                "icon": "fa-triangle-exclamation",
                "title": "Golden Rule 1: Format Conventions Are Non-Negotiable",
                "desc": "In writing tasks, failing to include standard structural conventions (recipient address in a letter, sender/subject in an email, clear headline in an article) immediately caps your format marks.",
                "badge": "Letter: Addresses + Date | Email: To/Subject | Article: Headline/Byline"
            },
            {
                "icon": "fa-scissors",
                "title": "Golden Rule 2: Eliminate the Comma Splice Forever",
                "desc": "Joining two complete standalone sentences with a comma is the single most common grammatical error flagged by Pearson Edexcel examiners. Use a full stop, semicolon, or conjunction.",
                "badge": "Never: 'The ward was busy, we worked late.' → 'The ward was busy. We worked late.'"
            }
        ],
        "skills": [
            {
                "title": "The Top 10 High-Frequency Functional Skills Pitfalls",
                "summary": "Master this hit list of examiner bugbears to safeguard your pass mark.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>The Comma Splice:</strong> Replacing a full stop with a comma between two independent clauses. <em>Fix: Use a full stop or 'and/because'.</em></li>
                    <li><strong>Missing Word Count Minimum:</strong> Submitting under 200 words on a 250–350 word task caps your content and organization mark at Band 1.</li>
                    <li><strong>Omitting Letter Conventions:</strong> Forgetting the sender's address, recipient's address, date, or matching sign-offs (<em>Dear Sir/Madam</em> → <em>Yours faithfully</em>).</li>
                    <li><strong>Quoting Half a Sentence in Reading:</strong> Answering with a single vague word instead of copying the full, specific factual evidence requested.</li>
                    <li><strong>Confusing Their / There / They're:</strong> Persistently confusing core homophones immediately degrades SPaG marks.</li>
                    <li><strong>Apostrophe Confusion (Its vs It's):</strong> Using <em>it's</em> for possession (incorrect) instead of contraction for <em>it is</em>.</li>
                    <li><strong>Ignoring One Half of a Two-Part Question:</strong> Failing to answer the 'and explain why' part of a reading question.</li>
                    <li><strong>Writing in One Giant Monolithic Block:</strong> Omitting paragraphs in an extended report or article.</li>
                    <li><strong>Dominating or Going Mute in SLC:</strong> Talking non-stop or failing to speak during the assessed group discussion.</li>
                    <li><strong>Leaving 0 Minutes for Proofreading:</strong> Rushing to the final second without catching obvious slip-ups in capitalization and spelling.</li>
                  </ol>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Repairing a High-Frequency Comma Splice & Formatting Failure",
                "marks": "SPaG Diagnostic & Fix",
                "context": "Workplace Health & Safety Report Submission",
                "question": "A candidate writes the following opening sentence in an exam report:<br><em>'The fire exits in warehouse B were blocked by wooden pallets, this is a serious hazard, we must clear them immediately.'</em><br>Diagnose the grammatical error and provide the corrected version.",
                "steps": [
                    ("Step 1", "Diagnose the error", "The sentence contains two comma splices: three independent clauses ('fire exits were blocked', 'this is a serious hazard', 'we must clear them') joined improperly by commas alone.", "Identifies comma splice fault"),
                    ("Step 2", "Apply correct punctuation demarcation", "Separate into distinct sentences or combine using appropriate subordinating conjunctions: 'The fire exits in warehouse B were blocked by wooden pallets. This is a serious hazard; therefore, we must clear them immediately.'", "Applies full stops and semicolons"),
                    ("Step 3", "Review syntactic flow and impact", "The corrected version establishes clear grammatical boundaries, improves professional readability, and secures full SPaG criteria.", "Confirms compliance with L2 SPaG criteria")
                ],
                "final_answer": "'The fire exits in warehouse B were blocked by wooden pallets. This represents a serious hazard, and they must be cleared immediately.'",
                "tutor_tip": "If a group of words can stand alone as a sentence, it must end in a full stop, semicolon, or be linked with a conjunction."
            }
        ],
        "examiner_traps": [
            {
                "title": "Using 'Yours Sincerely' with 'Dear Sir/Madam'",
                "desc": "This classic error is penalized in every exam series. If you do not know the recipient's name, you MUST use 'Yours faithfully'.",
                "fix": "Rule: Named recipient (Dear Mr Smith) = Yours sincerely. Unnamed recipient (Dear Sir/Madam) = Yours faithfully."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Correct the three punctuation and grammar errors in this extract: <em>'The doctors surgery was closed on wednesday, all emergency patients was directed to A&E.'</em>",
                "solution_steps": "1. Apostrophe error: 'doctors' should be 'doctor's' or 'doctors''.<br>2. Capitalization: 'wednesday' must be capitalized as 'Wednesday'.<br>3. Comma splice & subject-verb agreement: Replace comma with a full stop and change 'was directed' to 'were directed'.",
                "correct_answer": "'The doctor's surgery was closed on Wednesday. All emergency patients were directed to A&E.'",
                "tutor_tip": "Three distinct errors must be fixed: possessive apostrophe, capital letter for day of the week, and subject-verb agreement / sentence boundary."
            }
        ]
    },
    {
        "filename": "detecting-language-techniques.html",
        "clean_topic": "Detecting Language Techniques & Rhetorical Devices",
        "intro_lead": "Identify rhetorical devices, figurative language, emotive vocabulary, and persuasive structural techniques, explaining their precise psychological impact on target audiences.",
        "next_file": "types-of-and-navigating-sources.html",
        "next_name": "Types of Sources, Layout & Organizational Devices",
        "spec_points": [
            ("L1.10 / L2.10", "Identify and analyse how language features and devices convey meaning and persuade readers."),
            ("L2.11", "Analyse implicit and explicit techniques used by authors to influence opinions.")
        ],
        "golden_rules": [
            {
                "icon": "fa-wand-magic-sparkles",
                "title": "Golden Rule 1: Always Explain the Effect, Not Just the Label",
                "desc": "Identifying a rhetorical question or metaphor earns only 1 mark. To get full marks, you MUST explain the psychological effect on the reader: does it create urgency, evoke guilt, or reassure?",
                "badge": "Device Label + Quotation + Precise Effect on Reader"
            },
            {
                "icon": "fa-bullhorn",
                "title": "Golden Rule 2: Memorize the PERSUADE Mnemonic",
                "desc": "P: Personal Pronouns ('we', 'you') • E: Emotive Language • R: Rhetorical Questions • S: Statistics • U: Urgent Verbs • A: Alliteration • D: Direct Address • E: Rule of Three (Triads).",
                "badge": "PERSUADE: Pronouns • Emotive • Rhetorical • Stats • Urgency • Alliteration • Direct • Triads"
            }
        ],
        "skills": [
            {
                "title": "Rhetorical Devices & Reader Impact Glossary",
                "summary": "Essential language techniques assessed in Functional Skills English Reading and Writing.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Device</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Vocational Example</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Intended Effect on Reader</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rule of Three</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Safe, reliable, and compassionate care."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Creates a rhythmic, memorable impression of complete excellence and reliability.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Direct Address</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Your vigilance can prevent workplace accidents."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Instills personal responsibility and engages the reader individually.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rhetorical Question</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Can our NHS wards afford another winter of staff shortages?"</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Forces the reader to consider the obvious answer, highlighting urgency and crisis.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Hyperbole / Emotive</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Neglecting fire safety drills is an utter disaster waiting to strike."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Evokes anxiety and shock to compel immediate compliance.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Analyzing Rhetorical Persuasion in an NHS Staff Wellbeing Campaign",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Public Sector Employee Engagement",
                "question": "Read the campaign extract:<br><em>'Our dedicated nurses are the beating heart of this hospital, yet they are stretched to breaking point. Are we truly willing to stand by while our caring colleagues collapse under exhaustion?'</em><br>Identify two language techniques used by the author and explain their effect.",
                "steps": [
                    ("Step 1", "Identify Technique 1 & Quotation", "Metaphor: 'beating heart of this hospital' (and 'stretched to breaking point').", "1 Mark (A1 Identification)"),
                    ("Step 2", "Identify Technique 2 & Quotation", "Rhetorical question: 'Are we truly willing to stand by while our caring colleagues collapse under exhaustion?'", "1 Mark (A1 Identification)"),
                    ("Step 3", "Explain Reader Effect", "The metaphor emphasizes how essential nurses are to the hospital's survival, while the rhetorical question evokes moral guilt and empathy, challenging hospital leadership to take immediate welfare action.", "1 Mark (A1 Effect Explanation)")
                ],
                "final_answer": "Technique 1: Metaphor ('beating heart') emphasizes vital indispensability. Technique 2: Rhetorical question provokes moral guilt and compels leadership intervention.",
                "tutor_tip": "Avoid writing vague effects like 'it makes the reader want to read on'. Always name the specific emotion: guilt, urgency, pride, empathy, or outrage."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Layout Devices with Language Features",
                "desc": "Listing 'bullet points' or 'bold text' when asked for a language technique scores zero. Bullet points are presentational layout devices, not language techniques.",
                "fix": "Language techniques relate to words, figures of speech, and grammar (metaphors, alliteration, questions)."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A safety poster displays the slogan: <em>'Stop. Look. Listen. Protect your life today.'</em><br>Name the language device used in the first sentence and explain its persuasive effect on warehouse operators.",
                "solution_steps": "Device: Imperative verbs / Rule of three ('Stop. Look. Listen.').<br>Effect: Creates urgent, punchy direct commands that cut through background distraction, forcing workers to pause and check for forklifts.",
                "correct_answer": "Device: Imperative verbs / Rule of three | Effect: Imparts urgent commanding focus that prompts immediate safety precautions.",
                "tutor_tip": "Short one-word sentences are also known as minor sentences or imperative commands."
            }
        ]
    },
    {
        "filename": "types-of-and-navigating-sources.html",
        "clean_topic": "Types of Sources, Layout & Organizational Devices",
        "intro_lead": "Evaluate primary vs secondary sources, master visual layout features, and navigate complex informational texts swiftly using organizational signposts.",
        "next_file": "assessing-the-basics.html",
        "next_name": "Core Literacy Baseline: Grammar & Punctuation",
        "spec_points": [
            ("L1.7 / L2.7", "Identify different types of text and utilise organisational markers and layout features to locate key information."),
            ("L2.8", "Analyse how presentational devices and format guide reader navigation.")
        ],
        "golden_rules": [
            {
                "icon": "fa-compass",
                "title": "Golden Rule 1: Distinguish Primary from Secondary Sources",
                "desc": "Primary sources are firsthand eyewitness records, clinical charts, or original legislation. Secondary sources are secondhand analyses, news commentaries, or textbook summaries.",
                "badge": "Primary: Eyewitness / Original Data | Secondary: Summary / Review / Article"
            },
            {
                "icon": "fa-bars-staggered",
                "title": "Golden Rule 2: Layout Devices Must Serve Function, Not Just Decoration",
                "desc": "When asked why an author used a layout feature, always link the visual format to reader utility: bullet points simplify complex procedures; subheadings enable skimming.",
                "badge": "Format Feature → Reader Utility (Fast Scanning / Visual Clarity)"
            }
        ],
        "skills": [
            {
                "title": "Organizational Layout Devices & Their Specific Functions",
                "summary": "Key structural elements used across professional documentation.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Device</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Visual Appearance</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Navigational Function</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Subheadings</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Bold, larger section titles.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Divides the text into distinct thematic modules; allows readers to locate specific topics without reading every word.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Bulleted Lists</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Dot points with hanging indents.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Breaks down complex instructions or multi-item lists into digestible, scannable steps.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Callout Boxes / Sidebars</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Shaded or bordered rectangular container.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Isolates vital statutory warnings, contact hotlines, or key summaries from the main body text.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Glossary / Footnotes</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Alphabetical list or small footer text.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Defines specialized technical acronyms and terms without cluttering the primary narrative.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Evaluating Organizational Features in a Clinical Standard Operating Procedure",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Compliance Procedure (SOP)",
                "question": "A hospital blood transfusion protocol uses bold numbered steps, an amber warning callout box, and an alphabetical glossary at the end. Explain how these three devices assist clinical staff during an emergency.",
                "steps": [
                    ("Step 1", "Analyze Bold Numbered Steps", "Bold numbered steps provide a rigid chronological sequence, ensuring nurses do not skip critical cross-checking procedures under pressure.", "1 Mark (A1 Sequence Analysis)"),
                    ("Step 2", "Analyze Amber Warning Box", "The amber warning box draws immediate visual attention to life-threatening contraindications and reaction risks.", "1 Mark (A1 Visual Alert Analysis)"),
                    ("Step 3", "Analyze Alphabetical Glossary", "The glossary enables staff to quickly verify unfamiliar abbreviations (e.g., ABO incompatibility) without leaving the clinical area.", "1 Mark (A1 Terminology Verification)")
                ],
                "final_answer": "1. Bold numbered steps ensure mandatory chronological compliance. 2. Amber callout box highlights critical hazards. 3. Glossary provides instant clarification of technical medical acronyms.",
                "tutor_tip": "Always link the device to the reader's real-world workplace action (e.g., 'ensures nurses do not skip steps under pressure')."
            }
        ],
        "examiner_traps": [
            {
                "title": "Stating That Layout Features Are 'Just to Make It Look Nice'",
                "desc": "Writing 'It looks attractive' or 'It makes it colorful' earns zero marks. Presentational devices in Functional English exist for cognitive navigation and efficiency.",
                "fix": "Explain how the feature assists the user: rapid scanning, highlighting danger, or structuring data."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics driver handbook contains a table showing maximum vehicle weights and bridge clearances. Explain two reasons why a table is more effective than continuous prose for this information.",
                "solution_steps": "Reason 1: A table arranges numerical data into clear rows and columns, allowing drivers to find their specific vehicle clearance in seconds.<br>Reason 2: It avoids visual clutter, reducing the risk of a driver misreading critical weight limits in continuous paragraphs.",
                "correct_answer": "Row/column structure enables rapid lookups | Prevents numerical misreading from dense prose.",
                "tutor_tip": "Focus on speed of access and elimination of reading error."
            }
        ]
    },
    {
        "filename": "assessing-the-basics.html",
        "clean_topic": "Core Literacy Baseline: Grammar, Punctuation & Spelling",
        "intro_lead": "Secure your foundation with this essential Functional Skills literacy benchmark: sentence demarcation, core homophones, subject-verb agreement, and high-frequency spelling rules.",
        "next_file": "functional-skills-english-level-2.html",
        "next_name": "Functional Skills English Level 2 Directory",
        "spec_points": [
            ("L1 / L2 SPaG Benchmark", "Demonstrate control of standard English spelling, punctuation, and grammar across diverse functional contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-spell-check",
                "title": "Golden Rule 1: The Non-Negotiable Core Homophone Trio",
                "desc": "Master the three most heavily penalized homophone groups: They're / Their / There; You're / Your; Its / It's. A single error here alerts the examiner to weak SPaG control.",
                "badge": "They're (They are) • Their (Belongs to them) • There (Location/Fact)"
            },
            {
                "icon": "fa-link",
                "title": "Golden Rule 2: Ensure Subject-Verb Numerical Agreement",
                "desc": "A singular subject requires a singular verb; a plural subject requires a plural verb. Watch out for collective nouns and intervening prepositional phrases.",
                "badge": "'The team of nurses IS ready' (NOT 'are ready') — 'team' is singular."
            }
        ],
        "skills": [
            {
                "title": "The Core Punctuation Toolkit",
                "summary": "Rules for five essential punctuation marks tested in writing tasks.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Full Stop (.):</strong> Concludes an independent sentence containing a complete thought with subject and verb.</li>
                    <li><strong>Comma (,):</strong> Separates items in a list, sets off introductory clauses (<em>'In conclusion, we recommend...'</em>), and brackets parenthetical information. Never use to join two independent sentences!</li>
                    <li><strong>Apostrophe ('):</strong> Used for contractions (<em>do not → don't</em>) and possession (<em>the patient's chart, the workers' lockers</em>). Remember: <em>its</em> (possessive) has NO apostrophe.</li>
                    <li><strong>Colon (:):</strong> Introduces an itemized list, quote, or explanatory clause that expands on the preceding independent statement.</li>
                    <li><strong>Semicolon (;):</strong> Links two closely related independent clauses without needing a conjunction (<em>'The patient is stable; her vitals will be checked hourly.'</em>).</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Proofreading and Editing an Incident Log Entry",
                "marks": "4 Marks (Pearson Edexcel Writing Level 2 SPaG)",
                "context": "Care Home Incident Log Error Correction",
                "question": "Identify and correct four SPaG errors in this incident report entry:<br><em>'On friday evening, the night shift were delayed because there car broke down. The care assistants done their best, but it's battery was completely flat.'</em>",
                "steps": [
                    ("Step 1", "Capitalization of Proper Noun", "'friday' must be capitalized as 'Friday'.", "1 Mark (Proper Noun Capitalization)"),
                    ("Step 2", "Homophone Correction (There vs Their)", "'there car' must be corrected to possessive 'their car'.", "1 Mark (Possessive Homophone)"),
                    ("Step 3", "Non-Standard Verb Correction (Done vs Did)", "'The care assistants done their best' is non-standard dialect; correct to 'did their best'.", "1 Mark (Standard English Verb Form)"),
                    ("Step 4", "Possessive Pronoun Apostrophe Correction (It's vs Its)", "'it's battery' must be corrected to possessive 'its battery' (no apostrophe).", "1 Mark (Punctuation Control)")
                ],
                "final_answer": "'On Friday evening, the night shift was delayed because their car broke down. The care assistants did their best, but its battery was completely flat.'",
                "tutor_tip": "Notice 'it's' with an apostrophe means 'it is'. A car's battery cannot be 'it is battery', so 'its' without an apostrophe is correct."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing 'Should of' with 'Should have'",
                "desc": "Writing 'we should of ordered more PPE' is a phonetic error that heavily damages SPaG marks. The correct modal phrase is 'should have'.",
                "fix": "Always write 'should have', 'could have', 'would have'."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Insert the missing punctuation and correct the spelling in this sentence: <em>'The nurses station requires three items sanitiser gloves and aprons however its currently out of stock.'</em>",
                "solution_steps": "1. Possessive apostrophe: 'nurses' station' (or nurse's station).<br>2. Colon and list commas: '...requires three items: sanitiser, gloves, and aprons...'<br>3. Semicolon or full stop before connective: '; however, it is currently out of stock.'",
                "correct_answer": "'The nurses' station requires three items: sanitiser, gloves, and aprons; however, it is currently out of stock.'",
                "tutor_tip": "Use a colon to introduce the three items and commas to separate them."
            }
        ]
    }
]

# Write out to english_crosscutting_topics.py
out_file = "/home/subi/Projects/masterfunctionalskills.co.uk/english_crosscutting_topics.py"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""\nEnglish Cross-Cutting Topics (7 Topics)\n')
    f.write('Master Functional Skills Curriculum Suite\n')
    f.write('"""\n\n')
    f.write("CROSSCUTTING_TOPICS = " + repr(CROSSCUTTING_TOPICS) + "\n")

print(f"Successfully generated english_crosscutting_topics.py with {len(CROSSCUTTING_TOPICS)} topics!")
