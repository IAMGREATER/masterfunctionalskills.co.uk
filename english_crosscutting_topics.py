#!/usr/bin/env python3
"""
English Cross-Cutting Topics (7 Topics)
Master Functional Skills Curriculum Suite — Deep Pedagogical Overhaul
"""

CROSSCUTTING_TOPICS = [
    # 1. Key vs Detailed Points
    {
        "filename": "piecing-it-together-key-and-detailed-points.html",
        "clean_topic": "Key vs Detailed Points in Reading & Writing",
        "intro_lead": "Distinguish overarching central arguments from minor supporting details, enabling rapid information retrieval in Reading papers and cohesive, well-supported paragraphs in Writing assessments.",
        "next_file": "piecing-it-together-comparing-texts.html",
        "next_name": "Comparing Texts & Cross-Text Synthesis",
        "spec_points": [
            ("L1.9 / L2.11", "Identify and understand the main points, ideas, and details in texts of varying complexity."),
            ("L1.10 / L2.12", "Compare and synthesise information, main ideas, and supporting details across workplace documents."),
            ("L1.22 / L2.25", "Communicate information, ideas, and opinions clearly, coherently, and effectively using topic sentences and supporting evidence.")
        ],
        "golden_rules": [
            {
                "icon": "fa-tree",
                "title": "Golden Rule 1: The Trunk vs Branch Analogy",
                "desc": "The main point is the tree trunk — the overarching message or policy conclusion the author wants you to remember. Detailed points are the branches — specific dates, statistics, financial figures, or case examples that prove the trunk is true.",
                "badge": "Main Point = Umbrella Claim | Detailed Point = Specific Proof / Statistic / Date"
            },
            {
                "icon": "fa-highlighter",
                "title": "Golden Rule 2: Every Exam Paragraph Needs Both",
                "desc": "In Reading, never quote a minor statistic when asked for the 'main purpose or main point'. In Writing, open every paragraph with a clear topic sentence (main point) followed by 2–3 specific details.",
                "badge": "Topic Sentence (Main Point) + Supporting Details (Evidence / Examples)"
            }
        ],
        "skills": [
            {
                "title": "Main Point vs Supporting Detail Comparison Matrix",
                "summary": "How to classify overarching arguments versus granular evidence under exam time constraints.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">In Pearson Edexcel and City &amp; Guilds exams, candidates frequently lose marks by giving a narrow statistic when the question asks for the <strong>main point</strong>, or giving a vague summary when asked for <strong>specific details</strong>. Use this diagnostic matrix to separate the two instantly:</p>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Feature</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Main / Key Point (The Umbrella)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Detailed / Supporting Point (The Proof)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Primary Function</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">States the overarching argument, policy shift, or core conclusion of a paragraph or text.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Provides verifiable statistics, dates, names, costs, or step-by-step examples that back up the main point.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Typical Location</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Opening topic sentence, concluding summary sentence, or section subheading.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Middle sentences of a paragraph, bulleted lists, parenthetical brackets, or data tables.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Healthcare Example</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Strict hand hygiene compliance is essential to reduce hospital-acquired infections."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Staff must rub hands with 70% alcohol gel for 20 seconds across all 6 WHO steps before touching a patient."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Deletion Test</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">If removed, the paragraph loses its overall direction and meaning.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">If removed, the main claim still makes sense but has less factual proof.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Syntactic Signposts That Signal Key vs Detailed Points",
                "summary": "Recognize the exact linking words authors use to introduce main claims versus supporting evidence.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Writers use specific discourse markers to tell the reader whether they are stating an overarching rule or drilling down into a granular example:</p>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                    <h4 style="color:#0369a1; margin-top:0; margin-bottom:8px;">Main Point Signposts (Umbrella)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><strong>"Crucially, the primary objective is..."</strong></li>
                      <li><strong>"Overall, the audit demonstrates that..."</strong></li>
                      <li><strong>"Above all, staff must ensure..."</strong></li>
                      <li><strong>"In summary, the core issue remains..."</strong></li>
                    </ul>
                  </div>
                  <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                    <h4 style="color:#166534; margin-top:0; margin-bottom:8px;">Supporting Detail Signposts (Evidence)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><strong>"For instance, in October 2025..."</strong></li>
                      <li><strong>"Specifically, figures rose by 18%..."</strong></li>
                      <li><strong>"Namely, Wards 3, 4, and 7..."</strong></li>
                      <li><strong>"According to the Q3 payroll log..."</strong></li>
                    </ul>
                  </div>
                </div>
                <p style="color:#334155; line-height:1.7; margin-top:12px;"><strong>Level 1 vs Level 2 Distinction:</strong> At Level 1, main points are usually explicitly stated in the first sentence of a paragraph. At Level 2, the main point may be <em>implied</em> across several sentences or placed at the end of a complex paragraph after a counter-argument (e.g., <em>"While initial setup costs were high, the transition to digital stock control has ultimately transformed warehouse efficiency."</em>).</p>
                """
            },
            {
                "title": "Applying the P-E-E Structure in Functional Writing",
                "summary": "How to build high-scoring paragraphs in emails, letters, and reports by pairing key points with detailed evidence.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Understanding key vs detailed points is equally vital in the <strong>Writing paper</strong>. Examiners award top marks for organisation and coherence when every body paragraph follows the <strong>Point &rarr; Evidence &rarr; Explanation (P-E-E)</strong> blueprint:</p>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="margin-top:0; color:#0f172a;"><strong>Annotated Model Paragraph (Workplace Proposal):</strong></p>
                  <p style="line-height:1.8; color:#334155; background:#fff; padding:14px; border-radius:6px; border:1px solid #e2e8f0;">
                    <span style="background:#dbeafe; padding:2px 6px; border-radius:4px; font-weight:600;">[KEY POINT / TOPIC SENTENCE] Upgrading our clinic's telephone triage system is urgently required to reduce patient complaints.</span>
                    <span style="background:#dcfce7; padding:2px 6px; border-radius:4px;">[DETAILED POINT 1] Last month alone, 34% of incoming calls between 08:00 and 09:30 were disconnected due to line congestion, resulting in 28 formal written complaints.</span>
                    <span style="background:#fef9c3; padding:2px 6px; border-radius:4px;">[DETAILED POINT 2 / ACTION] Installing an automated callback queue costs £140 per month and guarantees that vulnerable patients hold their place in line without staying on the phone.</span>
                  </p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Extracting Key and Detailed Points from a Staff Notice (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Retail Distribution Centre Safety Update",
                "question": "Read the notice from the Warehouse Manager:<br><em>'All loading bay operatives must wear high-visibility vests and steel-toe boots at all times to prevent serious crush injuries. Last quarter, two agency workers suffered foot fractures near Bay 4 after entering the forklift zone in standard trainers.'</em><br>(a) Identify the <strong>main point</strong> of the notice. [1 Mark]<br>(b) Identify <strong>one detailed point</strong> that supports the manager's rule. [1 Mark]",
                "steps": [
                    ("Step 1", "Locate the overarching rule or message (Main Point)", "The first sentence sets out the core policy rule that applies to everyone: all loading bay staff must wear high-visibility vests and steel-toe boots to prevent crush injuries.", "1 Mark [A1 Main Point]"),
                    ("Step 2", "Extract the specific incident evidence (Detailed Point)", "The second sentence gives the specific factual proof: two agency workers suffered foot fractures near Bay 4 last quarter while wearing standard trainers.", "1 Mark [A1 Detailed Point]")
                ],
                "final_answer": "(a) Main Point: Operatives must wear high-visibility vests and steel-toe boots at all times for safety. | (b) Detailed Point: Two agency staff broke bones in their feet near Bay 4 last quarter while wearing trainers.",
                "tutor_tip": "Never swap the two around! If you write 'Two agency workers broke their feet near Bay 4' as the main point, you score 0 for part (a) because that is a past incident example, not the overarching workplace instruction."
            },
            {
                "title": "NHS Trust Waste Audit Multi-Point Synthesis (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Environmental Healthcare Management",
                "question": "Read the extract from the hospital facilities report:<br><em>'Clinical waste disposal costs reached £420,000 last year due to widespread misclassification across surgical wards. Staff frequently discard non-contaminated cardboard packaging into orange clinical waste sacks rather than domestic clear bags, inflating incineration tariffs by £180 per tonne.'</em><br>(a) Identify the overarching <strong>main point</strong> of this extract. [1 Mark]<br>(b) Identify <strong>two distinct supporting detailed points</strong> used as evidence. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify the central overarching point", "The main point is that hospital waste disposal costs have risen heavily (£420,000) because staff are misclassifying waste on surgical wards.", "1 Mark [A1 Main Point]"),
                    ("Step 2", "Identify Supporting Detail 1 (Specific Action)", "Staff put non-contaminated cardboard packaging into orange clinical waste sacks instead of clear domestic bags.", "1 Mark [A1 Detail 1]"),
                    ("Step 3", "Identify Supporting Detail 2 (Specific Financial Metric)", "This incorrect sorting inflates incineration tariffs by £180 per tonne.", "1 Mark [A1 Detail 2]")
                ],
                "final_answer": "(a) Main Point: Misclassification of waste across wards has driven clinical disposal costs up to £420,000. | (b) Supporting Details: 1. Staff place uncontaminated cardboard in orange clinical sacks instead of clear bags. 2. This error increases tariffs by £180 per tonne.",
                "tutor_tip": "Do not confuse the specific cost penalty (£180 per tonne) with the overall message. The £180 per tonne figure is a granular detail proving why misclassification is so expensive."
            }
        ],
        "examiner_traps": [
            {
                "title": "Quoting a Minor Statistic When Asked for the Main Idea",
                "desc": "If a question asks 'What is the main message of Text A?', quoting a narrow figure like '£180 per tonne' or 'Bay 4' scores zero because it represents only one supporting branch, not the trunk.",
                "fix": "Ask yourself: 'What is the headline takeaway that covers the whole paragraph?'"
            },
            {
                "title": "Copying the Entire Paragraph Word-for-Word",
                "desc": "Some candidates copy out three full sentences hoping the examiner will pick out the main point for them. Examiners mark this down because it shows you cannot distinguish the main point from the details.",
                "fix": "Isolate only the specific clause or sentence that answers the prompt cleanly."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "Read this extract from a logistics company newsletter:<br><em>'Fleet electrification has achieved substantial operational savings across our Midland depots. By replacing 25 diesel vans with Nissan Townstar EVs, depot fuel costs fell by 42% over six months, while tailpipe emissions decreased by 18 tonnes.'</em><br>Identify <strong>one main point</strong> and <strong>one detailed supporting point</strong>.",
                "solution_steps": "1. Main Point: Fleet electrification has generated major operational savings across the Midland depots [1 Mark].<br>2. Detailed Point: Replacing 25 diesel vans cut depot fuel costs by 42% over six months (or reduced emissions by 18 tonnes) [1 Mark].",
                "correct_answer": "Main Point: Electrifying the vehicle fleet has delivered significant operational savings. | Detailed Point: Fuel costs fell by 42% (or 25 diesel vans were replaced / emissions dropped by 18 tonnes).",
                "tutor_tip": "Extract the broad statement of success in the opening sentence as the main point, and cite the exact percentage or tonnage from the second sentence as your supporting detail."
            },
            {
                "marks": "3 Marks",
                "question": "Read this paragraph from a dental practice hygiene memo:<br><em>'Cross-contamination in treatment rooms remains our highest clinical risk during busy afternoon clinics. Yesterday's spot audit revealed that autoclave sterilisation logs were left unsigned in Surgery 2, and three ultrasonic bath filters had not been flushed since Tuesday.'</em><br>State the <strong>main point</strong> [1 Mark] and extract <strong>two detailed points</strong> [2 Marks].",
                "solution_steps": "1. Main Point: Cross-contamination in treatment rooms is the clinic's highest clinical risk during busy afternoon shifts [1 Mark].<br>2. Detailed Point 1: Autoclave sterilisation logs were left unsigned in Surgery 2 during yesterday's audit [1 Mark].<br>3. Detailed Point 2: Three ultrasonic bath filters had not been flushed since Tuesday [1 Mark].",
                "correct_answer": "Main Point: Cross-contamination in treatment rooms is the highest clinical risk. | Detail 1: Autoclave logs were unsigned in Surgery 2. | Detail 2: Three ultrasonic bath filters were unushed since Tuesday.",
                "tutor_tip": "Notice how the two audit findings in the second sentence provide concrete proof of the overarching risk stated in the first sentence."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a college Principal's report:<br><em>'Although installing swipe-card barriers at the main campus entrance cost £18,500 in July and caused brief queues during enrolment week, the new security gates have dramatically improved student safety and eliminated unauthorised trespassers.'</em><br>(a) What is the writer's <strong>main point</strong>? [1 Mark]<br>(b) Give <strong>two detailed points</strong> mentioned about the installation. [2 Marks]",
                "solution_steps": "1. Main Point: Located in the main clause after the introductory concession — the new swipe-card barriers have dramatically improved student safety and stopped unauthorised trespassers [1 Mark].<br>2. Detailed Point 1: Installing the barriers cost £18,500 in July [1 Mark].<br>3. Detailed Point 2: The barriers caused brief queues during enrolment week [1 Mark].",
                "correct_answer": "(a) Main Point: The new security barriers have significantly improved student safety and stopped trespassers. | (b) Details: 1. They cost £18,500 in July. 2. They caused brief queues during enrolment week.",
                "tutor_tip": "In Level 2 texts starting with 'Although' or 'While', the main point is always in the second half of the sentence after the comma!"
            }
        ]
    },
    # 2. Comparing Texts
    {
        "filename": "piecing-it-together-comparing-texts.html",
        "clean_topic": "Comparing Texts & Cross-Text Synthesis",
        "intro_lead": "Master cross-text analysis for Level 1 and Level 2 Functional Skills English: extract contrasting viewpoints, compare presentational and language techniques, and synthesize evidence using comparative connectives.",
        "next_file": "formality-and-bias.html",
        "next_name": "Formality, Register & Detecting Bias",
        "spec_points": [
            ("L1.10 / L2.12", "Compare information, ideas, and opinions in different texts, identifying similarities and differences."),
            ("L2.15", "Analyse how two writers use different language, tone, and structural styles to convey contrasting perspectives.")
        ],
        "golden_rules": [
            {
                "icon": "fa-code-compare",
                "title": "Golden Rule 1: Always Anchor Comparisons with Connectives",
                "desc": "Never write about Text A in isolation and then Text B in isolation. Weave them together in the same sentence or paired sentences using comparative connectives ('similarly', 'in contrast', 'whereas', 'on the other hand').",
                "badge": "Formula: [Text A Point + Quote] + [Comparative Connective] + [Text B Point + Quote]"
            },
            {
                "icon": "fa-table-columns",
                "title": "Golden Rule 2: Compare Like-with-Like Across Three Dimensions",
                "desc": "Compare the same theme across both texts (e.g. cost vs cost, safety vs safety). In Level 2, check whether the question asks you to compare WHAT the texts say (content/ideas) or HOW they say it (tone/language/layout).",
                "badge": "Content (What is said) • Tone (Attitude) • Methods (Language & Layout)"
            }
        ],
        "skills": [
            {
                "title": "The Cross-Text Synthesis Matrix",
                "summary": "The rapid planning grid to structure 3-mark to 6-mark comparative exam answers.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Before writing a multi-mark comparison answer, mentally map how the two documents differ across core dimensions:</p>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Comparison Dimension</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Text A (e.g. Official Corporate Policy)</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">Text B (e.g. Staff Forum / Union Blog)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Purpose &amp; Stance</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To inform and mandate compliance; positive or neutral institutional stance.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">To critique or share frontline frustrations; sceptical, urgent, or campaigning stance.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Tone &amp; Register</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Formal, objective, detached, third-person register.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Informal or passionate, subjective, first-person ('we', 'our') and direct address ('you').</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Evidence Used</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Audit percentages, financial projections, legal statutes (HSE, CQC).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Personal lived anecdotes, rhetorical questions, emotive case examples.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "The Comparative Connective Bank (Similarities vs Differences)",
                "summary": "High-impact discourse markers that signal direct cross-text synthesis to the examiner.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Examiners scan your answer specifically for comparative discourse markers. Using these connectives guarantees your points are credited as <strong>comparisons</strong> rather than isolated observations:</p>
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:16px; border-radius:8px;">
                    <h4 style="color:#166534; margin-top:0; margin-bottom:8px;">Signalling Similarities (Agreement)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><strong>"Both Text A and Text B agree that..."</strong></li>
                      <li><strong>"Similarly, Text B also highlights..."</strong></li>
                      <li><strong>"In the same way, the author of Text B..."</strong></li>
                      <li><strong>"Likewise, both writers acknowledge..."</strong></li>
                    </ul>
                  </div>
                  <div style="background:#fff7ed; border:1px solid #fed7aa; padding:16px; border-radius:8px;">
                    <h4 style="color:#c2410c; margin-top:0; margin-bottom:8px;">Signalling Differences (Contrast)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><strong>"Whereas Text A argues..., Text B claims..."</strong></li>
                      <li><strong>"In sharp contrast, Text B focuses on..."</strong></li>
                      <li><strong>"On the other hand, the writer of Text B..."</strong></li>
                      <li><strong>"Conversely, while Text A uses formal statistics..."</strong></li>
                    </ul>
                  </div>
                </div>
                """
            },
            {
                "title": "Comparing Content vs Comparing Methods (Level 1 vs Level 2)",
                "summary": "Understand when to compare facts/opinions and when to compare language/presentational techniques.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Always read the exact wording of the comparison question:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>"Compare the views / information in Text A and Text B" (L1 &amp; L2):</strong> Focus on <em>what</em> the writers say — their opinions, costs, benefits, and factual claims, supported by short quotes from each text.</li>
                  <li><strong>"Compare how the writers convey their views" (L2 Higher-Order Question):</strong> You must compare both <em>perspective</em> AND <em>language/tone</em> (e.g., <em>"Text A conveys a reassuring corporate view using positive statistics ('94% satisfaction'), whereas Text B conveys bitter frustration using hyperbole ('an absolute staffing catastrophe')."</em>).</li>
                </ul>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Comparing Two Staff Emails on Canteen Changes (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Workplace Catering Consultation",
                "question": "Read the two extracts:<br><strong>Text A (Facilities Manager):</strong> <em>'Replacing our staffed hot canteen with smart vending machines will save £22,000 a year and provide 24-hour food access for night-shift workers.'</em><br><strong>Text B (Warehouse Supervisor):</strong> <em>'While 24-hour access for night staff is welcome, vending machines only sell processed snacks rather than the hot, nutritious meals our manual workers need.'</em><br>(a) Identify <strong>one point of agreement</strong> between Text A and Text B. [1 Mark]<br>(b) Identify <strong>one point of disagreement</strong> about the food provided. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify shared agreement across both extracts", "Both Text A and Text B agree that providing 24-hour food access for night-shift staff is a positive benefit.", "1 Mark [A1 Similarity]"),
                    ("Step 2", "Contrast their views on the food using a connective", "Whereas Text A views smart vending machines as a cost-saving upgrade (£22,000 saved), Text B argues they only provide 'processed snacks' instead of the hot, nutritious meals workers need.", "1 Mark [A1 Difference]")
                ],
                "final_answer": "(a) Agreement: Both agree that 24-hour food access for night-shift workers is beneficial. | (b) Disagreement: Text A promotes vending machines to save £22,000, whereas Text B criticises them for serving processed snacks instead of hot, nutritious meals.",
                "tutor_tip": "Even in a 2-mark Level 1 question, always mention both texts explicitly when explaining a disagreement."
            },
            {
                "title": "Comparing Perspectives and Language on 12-Hour Hospital Shifts (Level 2)",
                "marks": "4 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Shift Scheduling Analysis",
                "question": "Read the two extracts:<br><strong>Text A (Hospital Trust Circular):</strong> <em>'Transitioning to 12-hour nursing rosters has reduced clinical handover errors by 15% and guarantees seamless operational continuity for acute patients.'</em><br><strong>Text B (Nursing Union Blog):</strong> <em>'Exhausted nurses are being pushed to breaking point! Working gruelling 12-hour marathons doubles medication errors after the tenth hour — how can exhausted staff keep patients safe?'</em><br>Compare the writers' views on 12-hour shifts and how they use language to convey their perspectives. [4 Marks]",
                "steps": [
                    ("Step 1", "Compare central viewpoints on patient safety with quotes", "Both texts focus on patient safety during 12-hour shifts; however, Text A supports the shifts by claiming they 'reduced clinical handover errors by 15%', whereas Text B opposes them, claiming they 'double medication errors after the tenth hour'.", "2 Marks [A1 Content & Quote Comparison]"),
                    ("Step 2", "Compare tone and language devices with quotes", "Text A uses a formal, reassuring corporate tone with professional vocabulary ('seamless operational continuity'). In contrast, Text B uses an urgent, emotive tone featuring metaphors ('gruelling 12-hour marathons') and a rhetorical question ('how can exhausted staff keep patients safe?') to provoke concern.", "2 Marks [A1 Language & Tone Comparison]")
                ],
                "final_answer": "Text A supports 12-hour shifts, citing a '15%' drop in handover errors in a formal, objective tone ('seamless operational continuity'). Conversely, Text B strongly opposes 12-hour shifts, warning that 'medication errors' double and using emotive language ('pushed to breaking point') and a rhetorical question ('how can exhausted staff keep patients safe?') to highlight staff burnout.",
                "tutor_tip": "Always mention BOTH texts in EVERY comparative paragraph. If you write only about Text A in paragraph 1 and Text B in paragraph 2 without cross-referencing, examiners cap your mark."
            }
        ],
        "examiner_traps": [
            {
                "title": "Writing Separate Summaries Without Direct Comparison",
                "desc": "Writing a summary of Text A followed by an unrelated summary of Text B prevents you from demonstrating synthesis and caps your mark at 1 out of 4.",
                "fix": "Use comparative sentence frames: 'While Text A argues [X], Text B contends that [Y].'"
            },
            {
                "title": "Comparing Unmatched Topics (Apples vs Oranges)",
                "desc": "Saying 'Text A talks about parking costs whereas Text B talks about uniform rules' is not a valid comparison because the two points are not about the same sub-topic.",
                "fix": "Always match the exact same theme across both texts (e.g. how both view costs, or how both view staff morale)."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Read the two extracts on town centre parking:<br><strong>Text 1 (Council Press Release):</strong> <em>'Increasing high-street parking tariffs by £1.20 per hour will relieve severe daytime congestion and cut town centre exhaust emissions by 20%.'</em><br><strong>Text 2 (Shopkeepers' Petition):</strong> <em>'Although town centre traffic is undeniably congested, this greedy £1.20 parking hike will drive loyal shoppers straight to out-of-town retail parks!'</em><br>Identify <strong>one similarity</strong> and <strong>two differences</strong> in how the texts present the parking issue.",
                "solution_steps": "1. Similarity: Both Text 1 and Text 2 agree that town centre parking/traffic is heavily congested [1 Mark].<br>2. Difference 1 (Impact): Text 1 argues the £1.20 increase will cut emissions by 20%, whereas Text 2 warns it will drive shoppers away to out-of-town retail parks [1 Mark].<br>3. Difference 2 (Tone/Language): Text 1 uses formal, objective statistics ('20%'), whereas Text 2 uses emotive, critical language ('greedy', exclamation mark) [1 Mark].",
                "correct_answer": "Similarity: Both agree the town centre is congested. | Difference 1: Text 1 claims the £1.20 rise cuts emissions by 20%, whereas Text 2 claims it will drive shoppers to retail parks. | Difference 2: Text 1 uses a formal statistical tone, while Text 2 uses emotive language ('greedy').",
                "tutor_tip": "Ensure you clearly label which text is which and use comparative connectives like 'whereas' and 'both'."
            },
            {
                "marks": "3 Marks",
                "question": "Read the two extracts about open-plan offices:<br><strong>Text A (Office Architect):</strong> <em>'Open-plan workspaces foster instant team collaboration, spark creative ideas, and reduce partitioning costs by 35%.'</em><br><strong>Text B (Software Developer):</strong> <em>'Working in a noisy fishbowl of constant chatter destroys deep concentration and leaves neurodivergent staff exhausted by 3 p.m.'</em><br>Compare how the two writers view open-plan offices and identify one language technique used in Text B.",
                "solution_steps": "1. Viewpoint Comparison: Text A views open-plan offices positively as collaborative and cost-effective ('reduce partitioning costs by 35%'), whereas Text B views them negatively as distracting and exhausting ('destroys deep concentration') [2 Marks].<br>2. Language Technique in Text B: Metaphor ('noisy fishbowl') or emotive verb ('destroys'), emphasizing lack of privacy and sensory overload [1 Mark].",
                "correct_answer": "Text A praises open-plan offices for boosting collaboration and cutting costs by 35%, whereas Text B criticises them for ruining concentration and exhausting staff. Text B uses the metaphor 'noisy fishbowl' to highlight the lack of privacy.",
                "tutor_tip": "Quote short phrases from both extracts to anchor your comparison."
            },
            {
                "marks": "4 Marks",
                "question": "Read these two extracts on AI customer service chatbots:<br><strong>Text A (Tech Vendor):</strong> <em>'Our AI Assistant resolves 82% of routine billing queries in under 10 seconds, freeing human agents to handle complex cases.'</em><br><strong>Text B (Consumer Watchdog):</strong> <em>'Frustrated customers are trapped in endless automated loops when trying to report urgent banking fraud. Why replace empathetic human advisors with robotic scripts?'</em><br>Compare how Text A and Text B present AI chatbots, referring to both content and language. [4 Marks]",
                "steps_hint": "Compare speed/efficiency vs customer frustration, and statistics vs emotive/rhetorical language.",
                "solution_steps": "1. Content comparison: Text A presents AI chatbots as fast and helpful ('resolves 82% of routine billing queries in under 10 seconds'), whereas Text B presents them as obstructive during urgent emergencies ('trapped in endless automated loops') [2 Marks].<br>2. Language comparison: Text A relies on persuasive statistics ('82%', '10 seconds') and a professional tone, whereas Text B uses emotive imagery ('trapped in endless... loops') and a rhetorical question ('Why replace empathetic human advisors with robotic scripts?') [2 Marks].",
                "correct_answer": "Text A portrays AI chatbots as efficient support tools that free up staff ('resolves 82%... in under 10 seconds'), using factual statistics. In contrast, Text B portrays them as frustrating barriers ('trapped in endless automated loops'), using emotive language and a rhetorical question to defend human advisors.",
                "tutor_tip": "Four-mark comparison questions require two well-developed comparisons supported by direct quotes from both texts."
            }
        ]
    },
    # 3. Formality and Bias
    {
        "filename": "formality-and-bias.html",
        "clean_topic": "Formality, Register & Detecting Bias",
        "intro_lead": "Analyze author objectivity, detect overt and covert bias in workplace and media texts, and master register calibration between formal business writing and informal dialogue.",
        "next_file": "common-mistakes.html",
        "next_name": "Common Pitfalls & High-Frequency Exam Mistakes",
        "spec_points": [
            ("L2.14", "Recognise bias and determine whether statements represent verifiable facts, balanced evaluation, or one-sided subjective persuasion."),
            ("L1.20 / L2.23", "Use language, register, and style suited to audience, purpose, and medium across formal and informal contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-unbalanced",
                "title": "Golden Rule 1: Bias Stems from One-Sided Evidence & Loaded Words",
                "desc": "An author is biased when they present only one side of an issue, omit legitimate counter-arguments, have a commercial/personal vested interest, or use emotionally loaded vocabulary ('disastrous', 'miraculous') to manipulate the reader.",
                "badge": "Bias Checklist: Vested Interest • One-Sided Facts • Loaded Adjectives"
            },
            {
                "icon": "fa-user-tie",
                "title": "Golden Rule 2: Match Formality to Professional Hierarchy",
                "desc": "Formal register avoids slang, exclamation marks, and contractions ('don't' -> 'do not'). It uses precise vocational terminology, objective phrasing, and standard salutations ('Dear Ms Patel / Yours sincerely').",
                "badge": "Formal: No contractions • Objective tone • Standard salutations"
            }
        ],
        "skills": [
            {
                "title": "Detecting Overt vs Covert Bias in Functional Texts",
                "summary": "Three forensic reading tests to expose author bias and vested interest in Level 2 exams.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">In Level 2 Reading exams, you are frequently asked whether a text is <strong>balanced or biased</strong>, and to provide evidence from the passage. Apply these three tests:</p>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>Check the Author's Vested Interest (Byline / Bio):</strong> Who wrote or funded the text? If the Sales Director of a private scooter firm writes an article praising electric scooters and attacking cycle lanes, they have a direct commercial motive.</li>
                    <li><strong>Inspect Evaluative Adjectives (Loaded Language):</strong> Compare neutral reporting (<em>"The council revised the bin collection schedule"</em>) with biased reporting (<em>"Reckless councillors forced through a chaotic bin scheme"</em>).</li>
                    <li><strong>Check for Omission of Counter-Arguments:</strong> A balanced article includes concessions (<em>"While critics point out the £5m cost, supporters highlight..."</em>). A biased text ignores all drawbacks completely.</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "The Register Calibration Table: Informal vs Formal English",
                "summary": "How to identify register in Reading and upgrade informal phrasing in Writing.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Linguistic Feature</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#ea580c;">Informal / Conversational Register</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Formal / Professional Register</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Contractions &amp; Slang</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"We can't put up with dodgy Wi-Fi any longer!"</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Staff cannot operate effectively with unreliable network connectivity."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Verb Choice</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Phrasal verbs: <em>look into, sort out, let down, put off</em>.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Single Latinate verbs: <em>investigate, resolve, disappoint, postpone</em>.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Typical Text Types</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Community forum posts, peer-to-peer emails, friendly blogs.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Statutory reports, job application letters, official complaint responses.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "How Writers Blend Informality with Professional Purpose",
                "summary": "Why some workplace texts deliberately use a semi-formal, conversational register.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Not all workplace texts are strictly formal. In Level 2 exams, you will often see <strong>semi-formal</strong> articles or staff intranet guides that combine accurate facts with conversational hooks (e.g., <em>"Feeling frazzled by Friday? Our new Employee Assistance Helpline offers confidential clinical counselling 24/7."</em>).</p>
                <p style="color:#334155; line-height:1.7; margin:0;"><strong>Why do writers do this?</strong> Using an approachable, conversational opening builds rapport and prevents readers from feeling intimidated, while the formal factual details build trust and credibility.</p>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Register and Rewriting for Formal Compliance (Level 1/2)",
                "marks": "2 Marks (Pearson Edexcel Reading & Writing)",
                "context": "Customer Service Complaint Handling",
                "question": "Read this draft sentence from a trainee manager's letter to a client:<br><em>'Sorry our driver messed up your Tuesday delivery — we'll sort out a replacement parcel ASAP.'</em><br>(a) Identify two features that make this sentence <strong>too informal</strong> for a client letter. [1 Mark]<br>(b) Rewrite the sentence in an appropriate <strong>formal register</strong>. [1 Mark]",
                "steps": [
                    ("Step 1", "Identify informal colloquialisms and contractions", "Uses colloquial phrasal verbs ('messed up', 'sort out'), a contraction ('we'll'), and an informal conversational abbreviation ('ASAP').", "1 Mark [A1 Register Analysis]"),
                    ("Step 2", "Convert into formal professional Standard English", "'Please accept our sincere apologies for the error with your delivery on Tuesday; we will arrange a replacement consignment immediately.'", "1 Mark [A1 Formal Rewrite]")
                ],
                "final_answer": "(a) Informal features: slang/phrasal verbs ('messed up', 'sort out') and contraction ('we'll'). | (b) Formal rewrite: 'We sincerely apologise for the error regarding your Tuesday delivery and will dispatch a replacement order immediately.'",
                "tutor_tip": "Replacing phrasal verbs ('messed up' -> 'error', 'sort out' -> 'arrange') is the fastest way to elevate register in formal letters and reports."
            },
            {
                "title": "Auditing a Commercial Software Pitch for Bias (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Procurement Appraisal",
                "question": "Read the promotional extract written by the Sales Director of MedTech Solutions:<br><em>'Our revolutionary CareFlow tablet system is unquestionably the most advanced clinical app ever built. Outdated paper charts are a catastrophic waste of taxpayer funds, and any care home that fails to install CareFlow immediately is putting residents in grave danger.'</em><br>Explain why this extract is <strong>biased</strong>, supporting your answer with <strong>two quotations</strong> and commenting on the writer's position. [3 Marks]",
                "steps": [
                    ("Step 1", "Quote and explain hyperbolic superlative language", "'Unquestionably the most advanced clinical app ever built' — uses an unverified commercial superlative as if it were an indisputable fact.", "1 Mark [A1 Quote & Explanation 1]"),
                    ("Step 2", "Quote and explain loaded fear-mongering language", "'Catastrophic waste' and 'putting residents in grave danger' — uses emotionally manipulative language to guilt care home managers into buying the product.", "1 Mark [A1 Quote & Explanation 2]"),
                    ("Step 3", "Evaluate the author's vested commercial interest", "The writer is the Sales Director of MedTech Solutions, meaning they have a direct financial motive to praise CareFlow and omit any setup costs or software limitations.", "1 Mark [A1 Vested Interest]")
                ],
                "final_answer": "The text is biased because it is written by the Sales Director of MedTech Solutions, who has a financial motive to sell the product. It uses exaggerated superlatives ('unquestionably the most advanced') and emotionally loaded fear tactics ('putting residents in grave danger') without providing independent clinical evidence.",
                "tutor_tip": "In Functional Skills Reading, linking the author's job title/vested motive to their choice of loaded words secures maximum marks."
            }
        ],
        "examiner_traps": [
            {
                "title": "Assuming Any Strong Argument is Automatically Biased",
                "desc": "An article is NOT automatically biased just because the author reaches a clear conclusion, provided they weigh up evidence from both sides fairly first.",
                "fix": "Look for unfair suppression of counter-arguments, vested financial interest, or emotionally loaded insults before declaring a text biased."
            },
            {
                "title": "Using Contractions in Formal Letters and Reports",
                "desc": "Writing 'don't', 'can't', or 'it's' in a formal letter to a council or employer signals inconsistent register control.",
                "fix": "Always expand contractions to 'do not', 'cannot', and 'it is' in formal tasks."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A trade union newsletter states: <em>'Greedy depot bosses are deliberately slashing shift allowances to line their own pockets.'</em><br>Explain how the writer's language indicates <strong>bias</strong> in this sentence, quoting specific words.",
                "solution_steps": "1. Pejorative loaded language: The author uses emotive, insulting words ('Greedy', 'slashing') to attack management [1 Mark].<br>2. Unproven accusation/one-sided view: Claims bosses act 'to line their own pockets' without presenting management's operational reasons or financial evidence [1 Mark].",
                "correct_answer": "Uses loaded, insulting vocabulary ('Greedy', 'slashing') and makes an unproven personal accusation ('line their own pockets') without giving management's perspective.",
                "tutor_tip": "Always quote the exact loaded words inside quotation marks when answering bias questions."
            },
            {
                "marks": "2 Marks",
                "question": "Read this extract from a staff health guide:<br><em>'Ditch the lift and take the stairs! You'll burn calories, boost your mood, and dodge that mid-afternoon slump.'</em><br>Describe the <strong>register and tone</strong> of this extract and give <strong>one language feature</strong> that creates it.",
                "solution_steps": "1. Register and tone: Informal, lively, friendly, and encouraging [1 Mark].<br>2. Language feature: Colloquial imperatives ('Ditch the lift', 'dodge'), contraction ('You'll'), or direct address ('your mood') [1 Mark].",
                "correct_answer": "Register/Tone: Informal, friendly, and upbeat. | Feature: Colloquial verbs ('Ditch', 'dodge') or contraction ('You'll').",
                "tutor_tip": "Pair a clear tone adjective (informal/upbeat) with a quoted word from the sentence."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a consumer technology review:<br><em>'While the Apex Laptop boasts a crisp 4K display and a 14-hour battery life, its £1,600 price tag and lack of USB-A ports make it difficult to recommend for budget-conscious students.'</em><br>Is this extract <strong>balanced or biased</strong>? Explain your answer with evidence from the text. [3 Marks]",
                "solution_steps": "1. Judgment: The extract is balanced / objective [1 Mark].<br>2. Evidence of positives: It acknowledges specific strengths ('crisp 4K display and a 14-hour battery life') [1 Mark].<br>3. Evidence of negatives: It weighs those strengths fairly against drawbacks ('£1,600 price tag and lack of USB-A ports') to give a reasoned conclusion [1 Mark].",
                "correct_answer": "Balanced: The reviewer weighs up positive features ('crisp 4K display', '14-hour battery life') alongside negative limitations ('£1,600 price tag', 'lack of USB-A ports') using measured, non-emotive language.",
                "tutor_tip": "Look out for exam questions where the text is actually balanced! Mentioning both the pros and cons quoted in the text proves why it is unbiased."
            }
        ]
    },
    # 4. Common Mistakes
    {
        "filename": "common-mistakes.html",
        "clean_topic": "Top 10 High-Frequency English Exam Mistakes & Fixes",
        "intro_lead": "A forensic guide to the ten most costly exam pitfalls in Functional Skills Reading, Writing, and Speaking, Listening & Communicating (SLC) — with instant diagnostic fixes.",
        "next_file": "detecting-language-techniques.html",
        "next_name": "Detecting Language Techniques & Rhetorical Devices",
        "spec_points": [
            ("L1 / L2 Reading Standards", "Extract exact evidence, distinguish layout from language devices, and answer both halves of two-part questions."),
            ("L1 / L2 Writing SPaG & Format", "Eliminate comma splices, apply full document formatting conventions, and maintain homophone and verb agreement accuracy.")
        ],
        "golden_rules": [
            {
                "icon": "fa-triangle-exclamation",
                "title": "Golden Rule 1: Format Conventions Are Non-Negotiable in Writing",
                "desc": "In Writing tasks, omitting standard format features (sender/recipient addresses and date in a formal letter; To/Subject header in an email; headline and subheadings in an article/report) immediately penalises your organisation mark.",
                "badge": "Letter: 2 Addresses + Date + Matched Sign-off | Report: Title + Subheadings"
            },
            {
                "icon": "fa-scissors",
                "title": "Golden Rule 2: Eliminate the Comma Splice Forever",
                "desc": "Joining two complete standalone sentences with a comma alone is the #1 grammatical penalty in Pearson Edexcel Writing papers. Separate them with a full stop, link them with a semicolon, or add a coordinating conjunction ('and', 'but', 'so').",
                "badge": "Wrong: 'The shift ended, I went home.' -> Right: 'The shift ended, so I went home.'"
            }
        ],
        "skills": [
            {
                "title": "The Top 5 Reading Paper Mistakes & How to Fix Them",
                "summary": "Why candidates lose easy marks in Reading comprehension and analysis.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#be123c;">Common Reading Mistake</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Why It Loses Marks</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Examiner-Approved Fix</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">1. Confusing Language vs Layout</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Writing 'bullet points' or 'bold heading' when asked for a <em>language feature</em> scores 0.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><strong>Language</strong> = words/phrases (metaphor, rule of three, rhetorical question). <strong>Layout/Presentation</strong> = visual formatting (bold, subheadings, boxes).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">2. Vague Effect Statements</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Writing <em>"It catches the reader's eye and makes them read on"</em> is banned by mark schemes.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">State the specific emotion or thought triggered: <em>"It provokes urgency about fire safety"</em> or <em>"It reassures nervous patients."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">3. Using Personal Knowledge</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Giving real-world workplace advice that is not printed in the source text scores 0.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Treat the source text as your only universe of facts. Every answer must be lifted or deduced directly from the text.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">4. Ignoring the Second Half of a Prompt</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Naming a technique without giving the requested quotation or explanation drops 50% of the marks.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Tick off each command verb in the question (e.g. <em>Identify</em> [✓] + <em>Quote</em> [✓] + <em>Explain</em> [✓]).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">5. Isolated Text Summaries</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Describing Text A and Text B separately without linking them caps comparison marks.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Use <em>"Whereas Text A states..., Text B argues..."</em> in every comparison sentence.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "The Top 5 Writing & SPaG Mistakes & How to Fix Them",
                "summary": "Eliminate the grammatical and structural errors that cost candidates a pass in Writing.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                    <li><strong>The Comma Splice:</strong> Joining two independent clauses with a comma (<em>"The delivery arrived late, the stock was damaged."</em>). <strong>Fix:</strong> Replace the comma with a full stop, semicolon, or <em>', and'</em>.</li>
                    <li><strong>Mismatched Letter Salutations:</strong> Pairing <em>"Dear Sir/Madam"</em> with <em>"Yours sincerely"</em>. <strong>Fix:</strong> <em>Dear Sir/Madam &rarr; Yours faithfully</em>; <em>Dear Mr/Ms [Surname] &rarr; Yours sincerely</em>.</li>
                    <li><strong>Homophone &amp; Apostrophe Confusions:</strong> Mixing up <em>their / there / they're</em>, <em>your / you're</em>, or writing <em>it's</em> for possession (<em>"the company changed it's policy"</em> &rarr; should be <em>its policy</em>).</li>
                    <li><strong>Non-Standard Verb Forms:</strong> Writing <em>"we could of gone"</em> instead of <em>"we could have gone"</em>, or <em>"the staff was unhappy"</em> / <em>"all patients was seen"</em> instead of <em>"were"</em>.</li>
                    <li><strong>Ignoring Bullet Point Prompts:</strong> Every Writing task gives 3–4 bullet points telling you what to cover. Omitting even one bullet point caps your Content mark!</li>
                  </ol>
                </div>
                """
            },
            {
                "title": "The 5-Minute Final Proofreading Protocol",
                "summary": "A systematic four-pass check to rescue 3–5 SPaG marks at the end of every Writing exam.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">Do not read your essay passively at the end of the exam. Scan through four targeted passes:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155; margin:0;">
                  <li><strong>Pass 1 (Format Check):</strong> Have I included addresses/date (letter), To/Subject (email), or Headline/Subheadings (article/report)?</li>
                  <li><strong>Pass 2 (Comma Splice Scan):</strong> Look at every comma you wrote. Is there a complete sentence on both sides of it? If yes, turn that comma into a full stop or semicolon!</li>
                  <li><strong>Pass 3 (Capital Letters &amp; Apostrophes):</strong> Check capital 'I', days of the week, months, street names, and check every <em>it's / its</em>.</li>
                  <li><strong>Pass 4 (Double-Letter Spelling Traps):</strong> Verify high-frequency exam spellings: <em>accommodation, necessary, recommend, opportunity, sincerely, disappointed, environment, immediately</em>.</li>
                </ul>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Diagnosing a Flawed Reading Exam Answer (Level 1/2)",
                "marks": "2 Marks (Reading Technique Diagnostic)",
                "context": "Reading Exam Answer Audit",
                "question": "An exam source text states: <em>'Over 92% of dental nurses reported back strain before ergonomic stools were introduced. Are you still risking your spine on outdated seating?'</em><br>The exam question asks: <strong>'Give one language feature used in this extract and explain its effect. [2 Marks]'</strong><br>A candidate writes: <em>'Bold font — it catches the reader's eye and makes them read on.'</em><br>Explain <strong>two reasons</strong> why this candidate scored 0 marks, and write a full-mark model answer.",
                "steps": [
                    ("Step 1", "Diagnose Mistake 1 (Presentational vs Language)", "'Bold font' is a presentational/layout device, not a language feature. The candidate needed to choose the statistic ('92%') or the rhetorical question ('Are you still risking your spine...?').", "1 Mark [Diagnostic 1]"),
                    ("Step 2", "Diagnose Mistake 2 (Generic Effect Phrase) & Write Model Answer", "'Catches the reader's eye and makes them read on' is a vague cliché that earns 0 marks. Model Answer: Rhetorical question ('Are you still risking your spine on outdated seating?') — directly challenges the reader to reflect on their own health and creates urgency to upgrade their seating.", "1 Mark [Diagnostic 2 & Fix]")
                ],
                "final_answer": "Mistakes: 1. Named a layout feature (bold font) instead of a language feature. 2. Gave a vague cliché ('makes them read on'). | Full-Mark Answer: Rhetorical question ('Are you still risking your spine...?') — prompts dental staff to worry about their own posture and persuades them to switch to ergonomic stools.",
                "tutor_tip": "Whenever a question asks for a 'language feature', banned answers include bullet points, bold text, subheadings, pictures, and text boxes."
            },
            {
                "title": "Repairing Comma Splices, Homophones & Letter Sign-Offs (Level 2)",
                "marks": "4 Marks (Pearson Edexcel Writing SPaG Diagnostic)",
                "context": "Workplace Health & Safety Letter Proofreading",
                "question": "Read this closing extract from a candidate's formal letter to an unnamed Council Environmental Health Officer (opened with <em>'Dear Sir/Madam'</em>):<br><em>'The fire exits in warehouse B was blocked by wooden pallets, this is a serious hazard, the manager should of cleared there walkways immediately. Yours sincerely, J. Patel.'</em><br>Identify and correct <strong>four distinct errors</strong> in grammar, punctuation, spelling, or letter convention. [4 Marks]",
                "steps": [
                    ("Step 1", "Fix Subject-Verb Agreement", "'The fire exits... was blocked' -> plural subject ('exits') requires plural verb 'were blocked'.", "1 Mark [Grammar Agreement]"),
                    ("Step 2", "Eliminate Comma Splices", "Replace the commas joining independent clauses with full stops or semicolons: '...wooden pallets. This is a serious hazard; therefore, the manager...'", "1 Mark [Punctuation Control]"),
                    ("Step 3", "Fix Non-Standard Modal & Homophone", "'should of' -> 'should have'; 'there walkways' -> possessive 'their walkways'.", "1 Mark [Spelling & Usage]"),
                    ("Step 4", "Fix Formal Letter Sign-Off Convention", "Because the letter opened with 'Dear Sir/Madam', the sign-off must be 'Yours faithfully', not 'Yours sincerely'.", "1 Mark [Format Convention]")
                ],
                "final_answer": "'The fire exits in Warehouse B were blocked by wooden pallets. This is a serious hazard; the manager should have cleared their walkways immediately. Yours faithfully, J. Patel.'",
                "tutor_tip": "If a group of words can stand alone as a complete sentence, never join it to the next complete sentence with just a comma."
            }
        ],
        "examiner_traps": [
            {
                "title": "Using 'Yours Sincerely' with 'Dear Sir/Madam'",
                "desc": "This classic error is penalised in every exam series. Remember the 'S' rule: never put two S's together (Sir + Sincerely = Wrong!).",
                "fix": "Named recipient (Dear Mr Smith) = Yours sincerely. Unnamed recipient (Dear Sir/Madam) = Yours faithfully."
            },
            {
                "title": "Writing Under the Minimum Word Count in Writing Tasks",
                "desc": "When a Level 2 task specifies 'Write 250–300 words', writing only 140 words severely restricts your ability to develop detailed points and caps your composition mark.",
                "fix": "Aim squarely for the target word band by writing 4 well-developed paragraphs (Introduction, 2 Main Body Paragraphs, Conclusion)."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Correct the <strong>three SPaG errors</strong> in this sentence:<br><em>'The doctors surgery was closed on wednesday, all emergency patients was directed to A&amp;E.'</em>",
                "solution_steps": "1. Apostrophe of possession: 'doctors surgery' must be 'doctor's surgery' (or 'doctors' surgery') [1 Mark].<br>2. Capital letter for day of the week: 'wednesday' must be 'Wednesday' [1 Mark].<br>3. Comma splice and verb agreement: Replace the comma with a full stop (or '; therefore,') and change 'was directed' to 'were directed' [1 Mark].",
                "correct_answer": "'The doctor's surgery was closed on Wednesday. All emergency patients were directed to A&E.'",
                "tutor_tip": "Always check plural subjects ('patients') to ensure they are paired with plural verbs ('were', not 'was')."
            },
            {
                "marks": "3 Marks",
                "question": "Identify and correct <strong>three errors</strong> in this workplace email sentence:<br><em>'Their is no excuse for arriving late, staff could of checked the train timetable on they're phones.'</em>",
                "solution_steps": "1. Homophone 1: 'Their is' should be 'There is' [1 Mark].<br>2. Comma splice & modal verb: Replace comma after 'late' with a full stop or 'because', and change 'could of' to 'could have' [1 Mark].<br>3. Homophone 2: 'they're phones' (they are) should be possessive 'their phones' [1 Mark].",
                "correct_answer": "'There is no excuse for arriving late; staff could have checked the train timetable on their phones.'",
                "tutor_tip": "Test 'they're' by expanding it to 'they are' — 'on they are phones' makes no sense, proving you need 'their'."
            },
            {
                "marks": "2 Marks",
                "question": "Read this short text:<br><em>'Warning: Forklift trucks operate in Aisle 6. Wear high-visibility jackets at all times.'</em><br>A student is asked to identify one <strong>language feature</strong> and writes: <em>'The word Warning is in bold.'</em> Explain why this is wrong and name one correct language feature from the extract.",
                "solution_steps": "1. Why it is wrong: 'Bold' is a presentational/layout device, not a language feature [1 Mark].<br>2. Correct language feature: Imperative command verb ('Wear high-visibility jackets...') or direct, cautionary vocabulary ('Warning') [1 Mark].",
                "correct_answer": "Bold font is a presentational feature, not a language feature. A correct language feature is the imperative verb command ('Wear high-visibility jackets at all times').",
                "tutor_tip": "Imperative verbs ('Wear', 'Keep', 'Do not enter') are the most common language feature in safety notices."
            }
        ]
    },
    # 5. Detecting Language Techniques
    {
        "filename": "detecting-language-techniques.html",
        "clean_topic": "Detecting Language Techniques & Rhetorical Devices",
        "intro_lead": "Identify rhetorical devices, figurative imagery, emotive vocabulary, and persuasive sentence structures in Reading texts, and explain their exact psychological effect on target audiences.",
        "next_file": "types-of-and-navigating-sources.html",
        "next_name": "Types of Sources, Layout & Organizational Devices",
        "spec_points": [
            ("L1.12 / L2.13", "Identify and analyse how language features and rhetorical devices convey meaning and influence the reader."),
            ("L2.14 / L2.15", "Evaluate how implicit and explicit language choices shape tone, perspective, and persuasive impact.")
        ],
        "golden_rules": [
            {
                "icon": "fa-wand-magic-sparkles",
                "title": "Golden Rule 1: The 3-Part Formula (Name -> Quote -> Specific Impact)",
                "desc": "Simply writing 'Rhetorical question' earns at most 1 mark. To secure full marks on 2-mark and 3-mark language questions, state the technique name, copy the exact short quotation, and explain how it makes the reader think or feel about that specific topic.",
                "badge": "Formula: Technique Name + Exact Quote + Specific Psychological Effect"
            },
            {
                "icon": "fa-bullhorn",
                "title": "Golden Rule 2: Memorize the PERSUADE Mnemonic",
                "desc": "P: Personal Pronouns / Direct Address ('you', 'we') • E: Emotive Language • R: Rhetorical Questions • S: Statistics & Facts • U: Urgent Imperative Verbs • A: Alliteration • D: Metaphor / Simile (Descriptive Imagery) • E: Exaggeration (Hyperbole) & Rule of Three.",
                "badge": "PERSUADE covers 95% of all language features tested in Functional Skills."
            }
        ],
        "skills": [
            {
                "title": "Rhetorical Devices & Reader Impact Master Glossary",
                "summary": "The essential language techniques assessed across Pearson Edexcel, City & Guilds, and NCFE papers.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Language Device</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Vocational Example</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Specific Effect on the Reader</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rule of Three (Triad)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Safe, reliable, and compassionate care."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Creates a rhythmic, memorable summary that convinces the reader the service is thorough and complete.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Direct Address ('You')</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Your vigilance can prevent warehouse accidents."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Speaks directly to the individual reader, placing personal moral responsibility on them to act safely.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Rhetorical Question</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Can our wards afford another winter of shortages?"</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Forces the reader to mentally supply the obvious answer ('No'), compelling agreement with the writer.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Hyperbole (Exaggeration)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Staff are drowning in mountains of pointless admin."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Dramatises the scale of staff workload to provoke sympathy and urgent management reform.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Imperative Verbs</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Isolate the circuit before removing the panel."</em></td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Delivers an authoritative, unambiguous command that leaves no room for hesitation in hazardous tasks.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Decoding Figurative Language: Metaphors, Similes & Idioms",
                "summary": "How to explain non-literal imagery clearly in Level 2 Reading answers.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Level 2 texts frequently use figurative imagery to make abstract workplace issues vivid and memorable:</p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Metaphor (states one thing IS another):</strong> <em>"Community pharmacies are the front line of winter healthcare."</em> &rarr; Compares pharmacies to a military battlefront, emphasising how vital and pressured pharmacists are in protecting hospitals.</li>
                  <li><strong>Simile (compares using 'like' or 'as'):</strong> <em>"New agency staff are treated like disposable parts."</em> &rarr; Highlights how dehumanised and easily replaceable temporary workers feel.</li>
                  <li><strong>Idiom (established figurative phrase):</strong> <em>"Cutting maintenance budgets is a ticking time bomb."</em> &rarr; Conveys that ignoring repairs will inevitably result in a sudden, catastrophic breakdown.</li>
                </ul>
                """
            },
            {
                "title": "Upgrading Vague Effect Answers into Full-Mark Explanations",
                "summary": "Side-by-side comparison of zero-mark clichés versus accredited Pearson Edexcel explanations.",
                "content_html": """
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:16px 0;">
                  <div style="background:#fef2f2; border-left:4px solid #ef4444; padding:16px; border-radius:6px;">
                    <h4 style="color:#b91c1c; margin-top:0; margin-bottom:8px;">0-Mark Vague Clichés (Avoid!)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><em>"It makes the reader want to read on."</em></li>
                      <li><em>"It sticks in the reader's head."</em></li>
                      <li><em>"It makes the text more interesting and punchy."</em></li>
                    </ul>
                  </div>
                  <div style="background:#f0fdf4; border-left:4px solid #16a34a; padding:16px; border-radius:6px;">
                    <h4 style="color:#166534; margin-top:0; margin-bottom:8px;">Full-Mark Specific Effects (Use!)</h4>
                    <ul style="padding-left:18px; line-height:1.7; color:#1e293b; margin:0;">
                      <li><em>"It provokes guilt about wasted food and urges households to compost."</em></li>
                      <li><em>"It builds institutional credibility by proving the training cut accidents by 40%."</em></li>
                      <li><em>"It creates a sense of shared collective duty ('we', 'our') among staff."</em></li>
                    </ul>
                  </div>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Identifying Persuasive Devices in a Community Poster (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Local Blood Donation Drive",
                "question": "Read the poster extract:<br><em>'Every blood donation can save up to three lives! Book your 45-minute appointment at the Town Hall this Friday and become a local lifesaver.'</em><br>Identify <strong>two language features</strong> used in this extract and give the matching quote for each. [2 Marks]",
                "steps": [
                    ("Step 1", "Identify Feature 1 and quote", "Numerical fact / statistic + exclamation: 'Every blood donation can save up to three lives!'", "1 Mark [A1 Feature 1]"),
                    ("Step 2", "Identify Feature 2 and quote", "Imperative command / direct address / alliteration: 'Book your 45-minute appointment' or 'local lifesaver'.", "1 Mark [A1 Feature 2]")
                ],
                "final_answer": "1. Statistic / Fact: 'save up to three lives'. | 2. Direct address / Imperative command: 'Book your 45-minute appointment' (or alliteration: 'local lifesaver').",
                "tutor_tip": "Always pair the name of the language feature with the exact words quoted from the extract."
            },
            {
                "title": "Analyzing Rhetorical Persuasion in an NHS Staff Wellbeing Campaign (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Public Sector Employee Engagement",
                "question": "Read the campaign extract:<br><em>'Our dedicated nurses are the beating heart of this hospital, yet they are stretched to breaking point. Are we truly willing to stand by while our caring colleagues collapse under exhaustion?'</em><br>Identify <strong>two language techniques</strong> used by the author, quote an example of each, and explain their combined persuasive effect on hospital management. [3 Marks]",
                "steps": [
                    ("Step 1", "Identify Technique 1 & Quotation", "Metaphor: 'beating heart of this hospital' (or 'stretched to breaking point').", "1 Mark [A1 Technique 1 & Quote]"),
                    ("Step 2", "Identify Technique 2 & Quotation", "Rhetorical question (with inclusive pronoun 'we' and alliteration 'caring colleagues collapse'): 'Are we truly willing to stand by while our caring colleagues collapse under exhaustion?'", "1 Mark [A1 Technique 2 & Quote]"),
                    ("Step 3", "Explain Specific Reader Effect", "The metaphor emphasises that nurses are essential to keeping the hospital alive, while the rhetorical question provokes moral guilt and urgency, pressuring management to act before staff burn out.", "1 Mark [A1 Specific Effect]")
                ],
                "final_answer": "Technique 1: Metaphor ('beating heart of this hospital'). Technique 2: Rhetorical question ('Are we truly willing to stand by while our caring colleagues collapse under exhaustion?'). Effect: Emphasises how vital nurses are while provoking moral guilt and urgency so management improves working conditions immediately.",
                "tutor_tip": "Avoid writing vague effects like 'it makes the reader want to read on'. Always name the specific emotion: guilt, urgency, pride, empathy, or outrage."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing Layout Devices with Language Features",
                "desc": "Listing 'bullet points', 'subheadings', or 'bold text' when asked for a language technique scores zero. Those are presentational/layout devices.",
                "fix": "Language techniques relate strictly to words, figures of speech, and sentence grammar (metaphors, alliteration, rhetorical questions, rule of three)."
            },
            {
                "title": "Quoting a Whole Paragraph Instead of the Exact Device",
                "desc": "If you identify 'alliteration' and quote a 25-word sentence, the examiner cannot tell which two words you think are alliterative.",
                "fix": "Quote only the crisp 2–6 words that contain the technique (e.g., 'caring colleagues collapse')."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A warehouse safety poster displays the slogan: <em>'Stop. Look. Listen. Protect your life around forklifts today.'</em><br>Name <strong>one language device</strong> used in the slogan and explain its persuasive effect on warehouse operators.",
                "solution_steps": "1. Device: Rule of three / short imperative verbs ('Stop. Look. Listen.') or direct address ('Protect your life') [1 Mark].<br>2. Effect: Delivers punchy, authoritative commands that cut through workplace distraction and force operators to check for moving forklifts immediately [1 Mark].",
                "correct_answer": "Device: Imperative verbs / Rule of three ('Stop. Look. Listen.'). | Effect: Delivers urgent, memorable commands that prompt workers to pause and check for hazards immediately.",
                "tutor_tip": "Short one-word commands are called imperative verbs or minor sentences."
            },
            {
                "marks": "3 Marks",
                "question": "Read this extract from a coastal conservation leaflet:<br><em>'Every single minute, a rubbish truck of plastic is dumped into our suffocating oceans. Will you help us turn the tide on marine pollution before our beaches become toxic wastelands?'</em><br>Identify <strong>two language features</strong> with quotes [2 Marks] and explain how they persuade the reader [1 Mark].",
                "solution_steps": "1. Feature 1 & Quote: Emotive personification/metaphor ('suffocating oceans' / 'toxic wastelands') or shocking statistic ('a rubbish truck of plastic every single minute') [1 Mark].<br>2. Feature 2 & Quote: Rhetorical question / direct address ('Will you help us turn the tide...?') [1 Mark].<br>3. Effect: Creates shock and alarm at the scale of ocean damage and directly challenges the individual reader to join the clean-up effort [1 Mark].",
                "correct_answer": "Features: 1. Emotive imagery ('suffocating oceans' / 'toxic wastelands'). 2. Rhetorical question with direct address ('Will you help us turn the tide...?'). Effect: Shocks the reader with vivid imagery of environmental harm and places personal responsibility on them to act.",
                "tutor_tip": "Always connect the imagery ('suffocating oceans') to the emotional response it triggers (alarm/guilt)."
            },
            {
                "marks": "2 Marks",
                "question": "Read this sentence from an apprenticeship recruitment brochure:<br><em>'Earn while you learn: gain practical skills, industry qualifications, and debt-free confidence.'</em><br>Identify <strong>two language techniques</strong> used in this sentence.",
                "solution_steps": "1. Technique 1: Internal rhyme / imperative catchphrase ('Earn while you learn') or direct address ('you') [1 Mark].<br>2. Technique 2: Rule of three ('practical skills, industry qualifications, and debt-free confidence') [1 Mark].",
                "correct_answer": "1. Direct address / internal rhyme ('Earn while you learn'). | 2. Rule of three ('practical skills, industry qualifications, and debt-free confidence').",
                "tutor_tip": "Look out for three noun phrases separated by commas — that is a classic Rule of Three!"
            }
        ]
    },
    # 6. Types of and Navigating Sources
    {
        "filename": "types-of-and-navigating-sources.html",
        "clean_topic": "Types of Sources, Layout & Organizational Devices",
        "intro_lead": "Evaluate primary vs secondary sources, master visual layout and organisational features, and navigate complex informational texts swiftly using structural signposts.",
        "next_file": "assessing-the-basics.html",
        "next_name": "Core Literacy Baseline: Grammar & Punctuation",
        "spec_points": [
            ("L1.14 / L2.16", "Understand organisational and structural features and use them to locate and interpret information efficiently."),
            ("L1.16 / L2.17", "Recognise different types of texts, sources, and presentational devices and explain how they support the writer's purpose.")
        ],
        "golden_rules": [
            {
                "icon": "fa-compass",
                "title": "Golden Rule 1: Distinguish Primary from Secondary Sources",
                "desc": "Primary sources are raw, firsthand records created at the time of an event (witness logs, clinical blood pressure charts, original survey responses). Secondary sources analyse, summarise, or comment on primary data (newspaper articles, textbook chapters, review reports).",
                "badge": "Primary = Firsthand Raw Record | Secondary = Secondhand Analysis / Article"
            },
            {
                "icon": "fa-bars-staggered",
                "title": "Golden Rule 2: Link Every Layout Device to Reader Navigation",
                "desc": "When asked why an author used subheadings, tables, sidebars, or numbered lists, always explain how that structural feature helps a busy reader locate or process specific information without reading every word.",
                "badge": "Structural Feature -> Cognitive Shortcut (Skimming, Scanning, Sequencing)"
            }
        ],
        "skills": [
            {
                "title": "Organisational Layout Devices & Their Navigational Functions",
                "summary": "How structural features organize complex workplace documents.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Structural Device</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Visual Appearance</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Exact Navigational Purpose</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Subheadings</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Bold section titles above thematic paragraphs.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Divides long texts into clear topic sections so readers can scan straight to the section they need.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Numbered Lists</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">1, 2, 3 sequential points.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Shows chronological order or priority ranking that must be followed step-by-step (e.g. emergency drills).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Callout / Shaded Boxes</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Bordered or tinted rectangular panel.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Separates urgent warnings, emergency phone numbers, or key takeaways from dense body text.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Glossary / Footnotes</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Alphabetical definition list or superscript notes (¹).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Explains technical jargon or acronyms (e.g. COSHH, RIDDOR) for non-specialist readers.</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Data Tables</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Grid of labelled rows and columns.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Aligns multi-variable figures (e.g. dosage by patient weight) for rapid cross-referencing without misreading.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Skimming vs Scanning vs Close Reading",
                "summary": "The three reading speeds every candidate must switch between during an exam.",
                "content_html": """
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Skimming (Gist Reading — 30 seconds):</strong> Reading only the main headline, subheadings, opening topic sentences, and caption boxes to identify the text type, audience, and overall purpose.</li>
                  <li><strong>Scanning (Keyword Hunting — 15 seconds):</strong> Moving your eyes rapidly across the page looking for a specific visual target (e.g. a capitalised name, a date like <em>2026</em>, a £ sign, or a percentage) without reading every sentence.</li>
                  <li><strong>Close Intensive Reading:</strong> Once scanning locates the target paragraph, reading the sentence before, the target sentence, and the sentence after word-for-word to verify nuances like <em>"except"</em>, <em>"unless"</em>, or <em>"minimum"</em>.</li>
                </ul>
                """
            },
            {
                "title": "Evaluating Source Credibility & Authority (Level 2)",
                "summary": "How to judge whether a source is reliable, official, or anecdotal.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:12px;">In Level 2 exams, you may be asked why one source is more reliable than another:</p>
                <div style="background:#eff6ff; border-left:4px solid #0284c7; padding:16px; border-radius:6px;">
                  <p style="margin:0; color:#1e293b; line-height:1.7;"><strong>High-Credibility Statutory/Peer-Reviewed Sources:</strong> Official NHS guidelines, Health and Safety Executive (HSE) codes of practice, Office for National Statistics (ONS) datasets. Backed by large sample sizes and legal accountability.<br><strong>Lower-Credibility Anecdotal Sources:</strong> Anonymous public comment threads, personal blogs, or unsourced social media posts based on a single person's unverified experience.</p>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Using Subheadings and Tables to Locate Information (Level 1)",
                "marks": "2 Marks (Pearson Edexcel Reading Level 1)",
                "context": "Sports Centre Membership Leaflet",
                "question": "A leisure centre leaflet includes the following subheadings: <strong>1. Swimming Pool Timetable | 2. Concessionary Pricing &amp; Discounts | 3. Gym Induction Rules</strong>.<br>Under Section 2, prices are presented in a three-column table (Peak, Off-Peak, Student/Senior).<br>(a) Which section should a retired resident read to find out if they qualify for a cheaper pass? [1 Mark]<br>(b) Explain why a table is used in Section 2 instead of a paragraph. [1 Mark]",
                "steps": [
                    ("Step 1", "Match reader query to the exact subheading", "Section 2: 'Concessionary Pricing & Discounts' covers reduced rates for retired/senior residents.", "1 Mark [A1 Navigation]"),
                    ("Step 2", "Explain the functional benefit of the table", "The table aligns Peak, Off-Peak, and Senior prices in clear columns so readers can compare costs at a glance without reading dense sentences.", "1 Mark [A1 Layout Function]")
                ],
                "final_answer": "(a) Section 2: Concessionary Pricing & Discounts. | (b) The table organises different membership tiers and prices into clear rows and columns for quick comparison.",
                "tutor_tip": "When asked 'which section', copy the exact subheading title from the prompt."
            },
            {
                "title": "Evaluating Organizational Features in a Clinical SOP (Level 2)",
                "marks": "3 Marks (Pearson Edexcel Reading Level 2)",
                "context": "Healthcare Compliance Procedure (SOP)",
                "question": "A hospital blood transfusion protocol uses:<br>• <strong>Bold numbered steps (1 to 8)</strong> for bedside patient ID checks<br>• An <strong>amber shaded warning box</strong> at the top reading: <em>'STOP: Never transfuse blood without two registered nurses verifying the wristband barcode.'</em><br>• An <strong>alphabetical glossary</strong> at the bottom defining terms like <em>'Haemolytic Reaction'</em>.<br>Explain how each of these three structural devices assists clinical staff during an emergency. [3 Marks]",
                "steps": [
                    ("Step 1", "Analyze Bold Numbered Steps", "Bold numbered steps enforce a strict chronological sequence (1 to 8), ensuring nurses do not skip or muddle vital patient ID checks under time pressure.", "1 Mark [A1 Sequence Analysis]"),
                    ("Step 2", "Analyze Amber Warning Box", "The amber shaded box visually isolates the critical two-nurse safety rule at the very top of the page so staff see the life-saving warning before starting.", "1 Mark [A1 Visual Alert Analysis]"),
                    ("Step 3", "Analyze Alphabetical Glossary", "The alphabetical glossary allows newly qualified staff to quickly look up complex medical terms like 'Haemolytic Reaction' without cluttering the step-by-step instructions.", "1 Mark [A1 Terminology Verification]")
                ],
                "final_answer": "1. Bold numbered steps ensure staff follow the mandatory chronological order without skipping steps. 2. The amber warning box draws immediate attention to the critical two-nurse check rule. 3. The glossary defines technical medical terms quickly without interrupting the main checklist.",
                "tutor_tip": "Always link each layout device to the reader's practical workplace need (e.g., 'ensures nurses do not skip steps under pressure')."
            }
        ],
        "examiner_traps": [
            {
                "title": "Stating That Layout Features Are 'Just to Make It Look Nice'",
                "desc": "Writing 'It looks attractive' or 'It breaks up the page so it isn't boring' earns zero marks. Presentational devices in Functional English exist for rapid navigation and safety.",
                "fix": "Explain how the feature assists the user functionally: rapid scanning, chronological ordering, or highlighting hazards."
            },
            {
                "title": "Confusing Bullet Points with Numbered Lists",
                "desc": "Unordered bullet points group non-sequential items (e.g. a kit list), whereas numbered lists mandate a strict chronological sequence (Step 1 before Step 2).",
                "fix": "When analysing a numbered list, always use words like 'chronological sequence' or 'step-by-step order'."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A logistics driver handbook contains a bordered grid showing maximum vehicle weights (3.5t, 7.5t, 18t) alongside low-bridge height clearances. Explain <strong>two reasons</strong> why a table is more effective than continuous prose for this information.",
                "solution_steps": "1. Reason 1: Organises vehicle weights and bridge clearances into aligned rows and columns so drivers can cross-reference their specific lorry size in seconds [1 Mark].<br>2. Reason 2: Prevents drivers from misreading critical height figures buried inside long paragraphs, reducing bridge-strike accidents [1 Mark].",
                "correct_answer": "1. Aligns weights and clearances in rows/columns for instant lookup. | 2. Reduces the risk of misreading vital height limits in dense paragraphs.",
                "tutor_tip": "Focus on speed of lookup and prevention of reading errors."
            },
            {
                "marks": "2 Marks",
                "question": "An appliance repair guide includes a footnote mark (*) next to the word <em>'Capacitor*'</em> and prints at the bottom of the page: <em>'*Capacitor: an electronic component that stores high-voltage charge even after the plug is removed.'</em><br>Identify this organisational feature and explain why the writer included it.",
                "solution_steps": "1. Feature: Footnote / asterisked glossary note [1 Mark].<br>2. Purpose: Explains a specialist electrical term and warns non-expert readers of the hidden high-voltage shock risk without interrupting the main sentence [1 Mark].",
                "correct_answer": "Feature: Footnote / glossary definition. | Purpose: Defines the technical term 'Capacitor' and explains its stored voltage hazard for non-specialist readers.",
                "tutor_tip": "Always refer to the specific word ('Capacitor') when explaining why the footnote is helpful."
            },
            {
                "marks": "3 Marks",
                "question": "You are researching workplace stress and find two sources:<br><strong>Source A:</strong> An official Health and Safety Executive (HSE) annual statistical report based on 45,000 UK employees.<br><strong>Source B:</strong> An anonymous comment posted on an internet chat forum reading: <em>'Nobody in my office ever takes sick leave for stress — it's all made up by lazy workers!'</em><br>Identify which source is more reliable and give <strong>two reasons</strong> why. [3 Marks]",
                "solution_steps": "1. Selection: Source A (the HSE report) is far more reliable [1 Mark].<br>2. Reason 1: It is compiled by an official national regulatory body using a massive sample size of 45,000 employees [1 Mark].<br>3. Reason 2: Source B is an unverified, biased personal opinion from an anonymous forum user based on a single office [1 Mark].",
                "correct_answer": "Source A is more reliable because: 1. It is official statistical data from the HSE covering 45,000 employees. 2. Source B is an anonymous, biased anecdote ('lazy workers') with no verifiable evidence.",
                "tutor_tip": "Contrast the sample size and official authority of Source A against the anonymity and bias of Source B."
            }
        ]
    },
    # 7. Assessing the Basics
    {
        "filename": "assessing-the-basics.html",
        "clean_topic": "Core Literacy Baseline: Grammar, Punctuation & Spelling",
        "intro_lead": "Secure your 42% SPaG mark allocation in Functional Skills Writing: sentence demarcation, the core homophone trio, subject-verb agreement, apostrophe control, and high-frequency workplace spellings.",
        "next_file": "functional-skills-english-level-2.html",
        "next_name": "Functional Skills English Level 2 Directory",
        "spec_points": [
            ("L1.17 / L2.20", "Punctuate writing correctly using a wide range of punctuation markers (full stops, commas, apostrophes, colons, semicolons)."),
            ("L1.18 / L2.21", "Use correct grammar including subject-verb agreement, consistent verb tense, and standard English modality."),
            ("L1.19 / L2.22", "Spell words used in work, study, and daily life accurately, including specialist vocabulary and homophones.")
        ],
        "golden_rules": [
            {
                "icon": "fa-spell-check",
                "title": "Golden Rule 1: Master the Non-Negotiable Homophone & Apostrophe Trio",
                "desc": "Examiners immediately spot errors in: (1) They're / Their / There, (2) You're / Your, and (3) It's / Its. Remember: 'It's' ALWAYS means 'It is' or 'It has'. Possessive 'its' (belonging to it) NEVER takes an apostrophe.",
                "badge": "It's = It is | Its = Belonging to it (NO apostrophe!) | They're = They are"
            },
            {
                "icon": "fa-link",
                "title": "Golden Rule 2: Enforce Subject-Verb & Tense Agreement",
                "desc": "A singular subject takes a singular verb ('The team of nurses IS ready'); a plural subject takes a plural verb ('The nurses ARE ready'). Never write 'we was' or 'patients was'.",
                "badge": "Singular: The box of gloves IS full | Plural: The gloves ARE in the box"
            }
        ],
        "skills": [
            {
                "title": "The Core Punctuation Toolkit (Level 1 & Level 2)",
                "summary": "Exact rules for the five punctuation marks that determine your SPaG band.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse;">
                    <thead>
                      <tr style="background:#f1f5f9; text-align:left;">
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0f172a;">Punctuation Mark</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#0369a1;">Core Rule</th>
                        <th style="padding:10px; border:1px solid #cbd5e1; color:#166534;">Correct Workplace Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Full Stop (.)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Ends a complete independent statement.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The audit finished at 4 p.m. All records matched."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Comma (,)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Separates list items, follows fronted adverbials, or brackets extra info.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"However, before starting the shift, staff must sign the log."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Apostrophe (')</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Shows omission (<em>don't</em>) or possession (singular <em>'s</em> vs plural <em>s'</em>).</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"One patient's chart"</em> (1 patient) vs <em>"The nurses' locker room"</em> (multiple nurses).</td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Colon (:)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Follows a complete clause to introduce a list, explanation, or verdict.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"Bring three items: photo ID, steel-toe boots, and a pad."</em></td>
                      </tr>
                      <tr>
                        <td style="padding:10px; border:1px solid #cbd5e1; font-weight:700;">Semicolon (;)</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;">Links two closely related complete sentences without a conjunction.</td>
                        <td style="padding:10px; border:1px solid #cbd5e1;"><em>"The ward is full; elective admissions have been paused."</em></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "title": "Singular vs Plural Possessive Apostrophes Made Simple",
                "summary": "How to place the apostrophe accurately every single time.",
                "content_html": """
                <p style="color:#334155; line-height:1.7; margin-bottom:14px;">Ask yourself: <strong>Who owns the item — one person/thing, or more than one?</strong></p>
                <ul style="padding-left:22px; line-height:1.8; color:#334155;">
                  <li><strong>Singular Owner (Add 's):</strong> <em>the manager's office</em> (one manager), <em>Mr James's van</em>, <em>the company's profits</em>.</li>
                  <li><strong>Regular Plural Owner Ending in -s (Add ' after the s):</strong> <em>the residents' lounge</em> (for many residents), <em>four weeks' notice</em>, <em>employees' pensions</em>.</li>
                  <li><strong>Irregular Plural Owner NOT Ending in -s (Add 's):</strong> <em>children's ward</em>, <em>men's changing room</em>, <em>women's health clinic</em>, <em>people's views</em>.</li>
                </ul>
                """
            },
            {
                "title": "High-Frequency Vocational Spelling Hit-List",
                "summary": "Memorize the top 12 words adult learners misspell under exam pressure.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:22px; line-height:1.8; color:#334155; margin:0; columns:2;">
                    <li><strong>Ac-comm-o-da-tion</strong> (double C, double M)</li>
                    <li><strong>Nec-ess-ary</strong> (1 Collar, 2 Sleeves: 1 C, 2 S)</li>
                    <li><strong>Rec-omm-end</strong> (1 C, double M)</li>
                    <li><strong>Opp-or-tun-ity</strong> (double P)</li>
                    <li><strong>En-vir-on-ment</strong> (silent N before M)</li>
                    <li><strong>Gov-ern-ment</strong> (silent N before M)</li>
                    <li><strong>Sep-a-rate</strong> ('there is A RAT in separate')</li>
                    <li><strong>Def-i-nite-ly</strong> (finite, no 'A'!)</li>
                    <li><strong>Sin-cere-ly</strong> (keep the E before LY)</li>
                    <li><strong>Im-med-i-ate-ly</strong> (double M)</li>
                    <li><strong>Col-league</strong> (double L, ends in -gue)</li>
                    <li><strong>Main-ten-ance</strong> (ten, not tain!)</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Homophone and Apostrophe Proofreading Drill (Level 1)",
                "marks": "3 Marks (Pearson Edexcel SPaG Check)",
                "context": "Reception Desk Handover Note",
                "question": "Read this handover note and correct <strong>three errors</strong> in homophones or apostrophes:<br><em>'Please tell the visitors that there permits are at reception. The childrens play area is closed because it's floor is being polished.'</em> [3 Marks]",
                "steps": [
                    ("Step 1", "Fix Homophone Error (there vs their)", "'there permits' refers to permits belonging to the visitors, so it must be spelled 'their permits'.", "1 Mark [Homophone]"),
                    ("Step 2", "Fix Irregular Plural Possessive Apostrophe", "'childrens play area' requires an apostrophe before the s because 'children' is already plural: 'children's play area'.", "1 Mark [Possessive Apostrophe]"),
                    ("Step 3", "Fix Possessive Pronoun 'its'", "'it's floor' means 'it is floor', which is incorrect. Possessive 'its' has no apostrophe: 'its floor'.", "1 Mark [Its vs It's]")
                ],
                "final_answer": "'Please tell the visitors that their permits are at reception. The children's play area is closed because its floor is being polished.'",
                "tutor_tip": "Because 'children', 'men', and 'women' are already plural without an 's', the apostrophe always goes BEFORE the 's' ('children's', 'women's')."
            },
            {
                "title": "Proofreading and Editing an Incident Log Entry (Level 2)",
                "marks": "4 Marks (Pearson Edexcel Writing Level 2 SPaG)",
                "context": "Care Home Incident Log Error Correction",
                "question": "Identify and correct <strong>four SPaG errors</strong> in this incident report entry:<br><em>'On friday evening, the night shift nurses was delayed because there minibus broke down. The care assistants done their best, but it's battery was completely flat.'</em> [4 Marks]",
                "steps": [
                    ("Step 1", "Capitalization & Subject-Verb Agreement", "'friday' must be capitalized as 'Friday', and plural 'nurses was delayed' must be 'nurses were delayed'.", "1 Mark [Capitalization & Agreement]"),
                    ("Step 2", "Homophone Correction (There vs Their)", "'there minibus' must be corrected to possessive 'their minibus'.", "1 Mark [Possessive Homophone]"),
                    ("Step 3", "Non-Standard Past Tense Verb (Done vs Did)", "'The care assistants done their best' is non-standard; correct to 'did their best'.", "1 Mark [Standard English Verb Form]"),
                    ("Step 4", "Possessive Pronoun Apostrophe (It's vs Its)", "'it's battery' must be corrected to possessive 'its battery' (no apostrophe).", "1 Mark [Punctuation Control]")
                ],
                "final_answer": "'On Friday evening, the night shift nurses were delayed because their minibus broke down. The care assistants did their best, but its battery was completely flat.'",
                "tutor_tip": "Notice 'it's' with an apostrophe means 'it is'. A minibus's battery cannot be 'it is battery', so 'its' without an apostrophe is always right for possession."
            }
        ],
        "examiner_traps": [
            {
                "title": "Confusing 'Should of' with 'Should have'",
                "desc": "Writing 'we should of ordered more PPE' is a spoken phonetic habit that heavily damages SPaG marks. The correct modal verb phrase is always 'should have'.",
                "fix": "Always write 'should have', 'could have', and 'would have' in full."
            },
            {
                "title": "Putting Apostrophes in Simple Plural Nouns (Greengrocer's Apostrophe)",
                "desc": "Writing 'Two lorry's arrived with ten box's of apples' is incorrect because nobody owns anything — they are simple plurals.",
                "fix": "Never use an apostrophe just to make a word plural: write 'lorries' and 'boxes'."
            }
        ],
        "practice_questions": [
            {
                "marks": "3 Marks",
                "question": "Insert the missing punctuation and correct the homophone in this sentence:<br><em>'The nurses station requires three items sanitiser gloves and aprons however its currently out of stock.'</em>",
                "solution_steps": "1. Possessive apostrophe: 'nurses' station' (or 'nurse's station') [1 Mark].<br>2. Colon and list commas: '...requires three items: sanitiser, gloves, and aprons' [1 Mark].<br>3. Sentence boundary & contraction: '; however, it's (or it is) currently out of stock.' [1 Mark].",
                "correct_answer": "'The nurses' station requires three items: sanitiser, gloves, and aprons; however, it is currently out of stock.'",
                "tutor_tip": "Here 'its currently out of stock' means 'it is currently out of stock', so expand it to 'it is' (or 'it's') and precede 'however' with a semicolon or full stop."
            },
            {
                "marks": "3 Marks",
                "question": "Correct the <strong>three spellingerrors</strong> in this workplace sentence:<br><em>'We definately recomend booking overnight accomodation before the conference.'</em>",
                "solution_steps": "1. 'definately' -> 'definitely' (spelled with an 'i', from finite) [1 Mark].<br>2. 'recomend' -> 'recommend' (one c, double m) [1 Mark].<br>3. 'accomodation' -> 'accommodation' (double c, double m) [1 Mark].",
                "correct_answer": "'We definitely recommend booking overnight accommodation before the conference.'",
                "tutor_tip": "Definitely, recommend, and accommodation are three of the most frequently tested spellings across all awarding bodies."
            },
            {
                "marks": "2 Marks",
                "question": "Choose the correct verb form in brackets for each sentence:<br>(a) <em>'The box of sterile syringes (is / are) stored in the locked cabinet.'</em><br>(b) <em>'Neither the supervisor nor the operatives (was / were) informed of the delay.'</em>",
                "solution_steps": "1. Sentence (a): The head noun of the subject is singular ('The box'), not 'syringes', so the verb must be singular: 'is' [1 Mark].<br>2. Sentence (b): With 'neither... nor', the verb agrees with the closer plural noun ('operatives'), so the verb is plural: 'were' [1 Mark].",
                "correct_answer": "(a) is ('The box... is stored'). | (b) were ('...the operatives were informed').",
                "tutor_tip": "In sentence (a), cross out the prepositional phrase 'of sterile syringes' — you are left with 'The box is stored', which makes the singular subject obvious!"
            }
        ]
    }
]
