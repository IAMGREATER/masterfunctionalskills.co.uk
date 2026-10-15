#!/usr/bin/env python3
"""
Master Functional Skills - Bespoke English & Digital Worksheets Part 2 (35 Topics).
Covers Writing (13 slugs), Speaking, Listening & Communicating (11 slugs),
Cross-Cutting English (7 slugs), and Digital Functional Skills (4 slugs).
Every single question (Q1-Q6) contains genuine self-contained reading/writing/SLC excerpts,
flawed drafts, or spreadsheet scenarios, plus full step-by-step mark schemes and model answers.
"""

import re
from build_topic_dataset import make_english_topic, make_digital_topic
import english_reading_topics
import english_writing_topics
import english_slc_topics
import english_crosscutting_topics

# Build lookup of upgraded English revision topics
_ENG_REV_MAP = {}
for _lst, _cat in [
    (english_reading_topics.READING_TOPICS, "reading"),
    (english_writing_topics.WRITING_TOPICS, "writing"),
    (english_slc_topics.SLC_TOPICS, "slc"),
    (english_crosscutting_topics.CROSSCUTTING_TOPICS, "reading"),
]:
    for _item in _lst:
        _slug = _item["filename"].replace("functional-skills-", "").replace(".html", "")
        _ENG_REV_MAP[_slug] = (_cat, _item)


def _parse_eng_steps(steps_html):
    """Convert HTML solution_steps string into structured (step_text, mark_code) tuples."""
    parts = [re.sub(r"<[^>]+>", "", p).strip() for p in re.split(r"<br\s*/?>", steps_html) if p.strip()]
    if not parts:
        parts = ["1. Identify target language/structural feature", "2. Provide direct quotation or model rewrite"]
    rows = []
    for idx, p in enumerate(parts):
        clean_p = re.sub(r"^\d+\.\s*", "", p)
        code = "[A1]" if idx == len(parts) - 1 else "[M1]"
        rows.append((f"{idx + 1}. {clean_p}", code))
    return rows


def _parse_eng_model_steps(model_steps):
    """Convert worked_model['steps'] tuples into worksheet step_rows."""
    rows = []
    for idx, st in enumerate(model_steps, 1):
        title = re.sub(r"<[^>]+>", "", st[1]).strip()
        body = re.sub(r"<br\s*/?>", " | ", st[2])
        body = re.sub(r"<[^>]+>", "", body).strip()
        rows.append((f"{idx}. {title}: {body}", "[A1]"))
    return rows


# Bespoke Foundation Question 1 (2 Marks) for each of the 31 English Writing, SLC, and Cross-Cutting slugs
BESPOKE_ENGLISH_Q1 = {
    # CROSS-CUTTING (7 slugs)
    "assessing-the-basics": {
        "title": "Question 1 (Correcting Homophones, Apostrophes & Subject-Verb Agreement)",
        "marks": 2,
        "stem": "Read this flawed sentence from a clinic reception notice:<br><em>'All patients must bring there appointment letter to the desk, as the list of afternoon clinics are already full.'</em><br>Rewrite the sentence correcting <strong>both errors</strong>.",
        "lines": 3,
        "ans_label": "Corrected Sentence =",
        "choice_box": "Write your corrected sentence in the workspace.",
        "step_rows": [
            ("1. Correct homophone error: 'there' → 'their' (possessive)", "[A1]"),
            ("2. Correct singular collective subject-verb agreement: 'the list... are' → 'the list... is'", "[A1]")
        ],
        "final_answer": "All patients must bring their appointment letter to the desk, as the list of afternoon clinics is already full.",
        "pitfall": "Changing 'clinics' instead of changing 'are' to 'is' to agree with singular 'the list'.",
        "reverse_check": "Test: 'their appointment letter' (belonging to them) and 'the list is full'."
    },
    "common-mistakes": {
        "title": "Question 1 (Eliminating Comma Splices & Informal Slang)",
        "marks": 2,
        "stem": "Fix the comma splice and informal slang in this draft complaint sentence:<br><em>'The delivery van turned up mega late on Tuesday, it totally messed up our ward stock count.'</em>",
        "lines": 3,
        "ans_label": "Formal Corrected Sentence =",
        "choice_box": "Write your corrected formal sentence in the workspace.",
        "step_rows": [
            ("1. Replace comma splice with a subordinating conjunction ('which'/'because') or semicolon", "[A1]"),
            ("2. Upgrade informal slang ('turned up mega late', 'totally messed up') to formal register ('arrived significantly late', 'disrupted')", "[A1]")
        ],
        "final_answer": "The delivery van arrived significantly late on Tuesday, which severely disrupted our ward stock count.",
        "pitfall": "Upgrading the vocabulary while leaving the comma splice between the two main clauses.",
        "reverse_check": "Verify no comma separates two standalone sentences without a conjunction."
    },
    "detecting-language-techniques": {
        "title": "Question 1 (Naming & Quoting Persuasive DAFOREST Techniques)",
        "marks": 2,
        "stem": "Read this extract from a hospital blood-donation campaign:<br><em>'Donating blood takes just forty-five minutes, yet 84% of first-time donors say it is the proudest moment of their year. Will you step forward and save three lives today?'</em><br>Identify <strong>two distinct language techniques</strong> used in this extract and quote an example of each.",
        "lines": 3,
        "ans_label": "Two Techniques & Quotes =",
        "choice_box": "1: ________________________ | 2: ________________________",
        "step_rows": [
            ("1. Statistic / Numerical Fact: '84% of first-time donors' (or 'forty-five minutes' / 'three lives')", "[A1]"),
            ("2. Rhetorical Question / Direct Address: 'Will you step forward and save three lives today?'", "[A1]")
        ],
        "final_answer": "1. Statistic ('84% of first-time donors'); 2. Rhetorical question / Direct address ('Will you step forward and save three lives today?').",
        "pitfall": "Copying the quotes without naming the specific language techniques (Statistic and Rhetorical Question).",
        "reverse_check": "Both techniques are explicitly named and paired with exact short quotes."
    },
    "formality-and-bias": {
        "title": "Question 1 (Detecting One-Sided Bias & Loaded Language)",
        "marks": 2,
        "stem": "Read this extract from a local newsletter:<br><em>'Greedy council bosses are forcing through an outrageous £2.50 parking charge that will destroy our beloved park forever.'</em><br>Explain why this sentence is <strong>biased</strong> and quote <strong>two loaded words</strong> that reveal the writer's prejudice.",
        "lines": 3,
        "ans_label": "Bias Explanation & Two Quotes =",
        "choice_box": "Why biased: ________________ | Quotes: '________' and '________'",
        "step_rows": [
            ("1. Explain bias: Presents a one-sided attack without giving the council's reason for the £2.50 charge", "[A1]"),
            ("2. Quote two emotive/loaded words: 'Greedy', 'outrageous', or 'destroy'", "[A1]")
        ],
        "final_answer": "It presents a one-sided opinion with no counter-evidence, using loaded emotive words ('Greedy', 'outrageous', 'destroy').",
        "pitfall": "Quoting the factual figure '£2.50' instead of the biased adjectives.",
        "reverse_check": "Are the quoted words emotionally loaded rather than neutral facts?"
    },
    "piecing-it-together-comparing-texts": {
        "title": "Question 1 (Linking Two Texts with Comparative Connectives)",
        "marks": 2,
        "stem": "Read these two views on paperless hospital records:<br><strong>Text A (IT Director):</strong> <em>'Digital tablets eliminate lost paper charts and allow doctors to view blood results instantly.'</em><br><strong>Text B (Ward Sister):</strong> <em>'Instant blood results are helpful, but Wi-Fi blackspots on the ground floor often freeze the tablets mid-round.'</em><br>State <strong>one point of agreement</strong> and <strong>one difference</strong> between Text A and Text B.",
        "lines": 3,
        "ans_label": "Agreement & Difference =",
        "choice_box": "Agreement: ________________ | Difference: ________________",
        "step_rows": [
            ("1. Point of agreement: Both agree that instant access to blood results is beneficial", "[A1]"),
            ("2. Point of difference: Text A is wholly positive, whereas Text B warns that Wi-Fi blackspots freeze tablets mid-round", "[A1]")
        ],
        "final_answer": "Both agree instant blood results are useful, whereas Text B highlights that Wi-Fi blackspots freeze the tablets.",
        "pitfall": "Summarising Text A without contrasting it directly with Text B.",
        "reverse_check": "Check that both similarity and difference are clearly stated."
    },
    "piecing-it-together-key-and-detailed-points": {
        "title": "Question 1 (Distinguishing Overarching Key Points from Supporting Detail)",
        "marks": 2,
        "stem": "Read this workplace paragraph:<br><em>'To pass our annual fire safety inspection, all fire exit corridors must be kept completely clear at all times. Yesterday, inspectors found three linen cages blocking Stairwell B and two waste bins wedged against Door 4.'</em><br>Identify the <strong>main overarching key point</strong> and <strong>one specific supporting detail</strong>.",
        "lines": 3,
        "ans_label": "Key Point & Supporting Detail =",
        "choice_box": "Key Point: ________________ | Detail: ________________",
        "step_rows": [
            ("1. Overarching Key Point: All fire exit corridors must be kept completely clear at all times to pass inspection", "[A1]"),
            ("2. Supporting Detail: Three linen cages blocked Stairwell B (or two waste bins wedged against Door 4)", "[A1]")
        ],
        "final_answer": "Key Point: Fire exit corridors must be kept clear at all times. Supporting Detail: Three linen cages were found blocking Stairwell B.",
        "pitfall": "Confusing the specific example (three linen cages) with the main rule (keeping fire exits clear).",
        "reverse_check": "Does the supporting detail prove why the main rule is needed?"
    },
    "types-of-and-navigating-sources": {
        "title": "Question 1 (Using Organisational Features to Locate Information Fast)",
        "marks": 2,
        "stem": "A 12-page Staff Handbook contains the following structural sections:<br>• <strong>1.0</strong> Annual Leave Entitlements | <strong>2.0</strong> Sickness Absence Reporting | <strong>3.0</strong> Uniform & Dress Code | <strong>Appendix A:</strong> Glossary of Clinical Abbreviations<br><br>Which section should a new healthcare assistant consult to find out <strong>who to telephone at 06:30 if they are unwell</strong>, and which section explains the meaning of <strong>'PRN'</strong>?",
        "lines": 3,
        "ans_label": "Two Sections =",
        "choice_box": "Unwell call: ____________ | Meaning of PRN: ____________",
        "step_rows": [
            ("1. Sickness call procedure: Section 2.0 (Sickness Absence Reporting)", "[A1]"),
            ("2. Meaning of abbreviation 'PRN': Appendix A (Glossary of Clinical Abbreviations)", "[A1]")
        ],
        "final_answer": "Section 2.0 (Sickness Absence Reporting) and Appendix A (Glossary of Clinical Abbreviations).",
        "pitfall": "Guessing content without matching the subheading keywords ('Sickness Reporting' and 'Glossary').",
        "reverse_check": "A glossary always defines specialist terms and abbreviations."
    },
    # WRITING (13 slugs)
    "english-level-2-writing-blog": {
        "title": "Question 1 (Crafting an Engaging Level 2 Article/Blog Headline & Strapline)",
        "marks": 2,
        "stem": "You are writing a Level 2 online blog post for apprentice nurses titled <strong>How to Survive Your First Night Shift</strong>.<br>Write an engaging <strong>headline</strong> (using alliteration or a rhetorical question) and a one-sentence <strong>opening hook</strong> addressing the reader directly.",
        "lines": 3,
        "ans_label": "Headline & Opening Hook =",
        "choice_box": "Headline: ________________ | Hook: ________________",
        "step_rows": [
            ("1. Engaging headline using rhetorical device: e.g. 'Beat the 3 A.M. Burnout: The Apprentice Nurse's Guide to Night Shifts'", "[A1]"),
            ("2. Direct-address opening hook: e.g. 'Have you ever stared at the ward clock at 3 a.m. wondering how you will stay awake until handover?'", "[A1]")
        ],
        "final_answer": "Headline: Beat the 3 A.M. Burnout: Mastering Your First Night Shift | Hook: Have you ever stared at the ward clock at 3 a.m. wondering how to keep your energy up until morning handover?",
        "pitfall": "Using Dear Sir/Madam in a blog or article (letters only!).",
        "reverse_check": "Includes a catchy headline + direct address ('you') hook."
    },
    "writing-assessing-audience": {
        "title": "Question 1 (Adapting Register & Salutation to Match the Target Audience)",
        "marks": 2,
        "stem": "State the correct <strong>opening salutation</strong> and <strong>closing sign-off</strong> for:<br>(a) A formal complaint letter to an unnamed Chief Executive (`Dear Sir or Madam,`)<br>(b) A formal job application letter to a named recruiting manager (`Dear Ms Patel,`)",
        "lines": 3,
        "ans_label": "(a) & (b) Sign-offs =",
        "choice_box": "(a) Yours ____________ | (b) Yours ____________",
        "step_rows": [
            ("1. (a) Unnamed recipient ('Dear Sir or Madam,'): Close with 'Yours faithfully,'", "[A1]"),
            ("2. (b) Named recipient ('Dear Ms Patel,'): Close with 'Yours sincerely,'", "[A1]")
        ],
        "final_answer": "(a) Yours faithfully, | (b) Yours sincerely,",
        "pitfall": "Pairing 'Dear Ms Patel' with 'Yours faithfully' (Rule: Never put two S's together — Sir/Madam = Faithfully; Named = Sincerely).",
        "reverse_check": "Sir/Madam → Faithfully; Surname → Sincerely."
    },
    "writing-communicating": {
        "title": "Question 1 (Replacing Vague Ambiguity with Concrete Workplace Precision)",
        "marks": 2,
        "stem": "Rewrite this vague workplace email sentence so that it communicates clear, actionable details:<br><em>'Some of the stuff in the room downstairs is broken so someone needs to sort it out soon.'</em><br>(Use: <strong>Treatment Room 2, blood-pressure monitor, Estates Team, before 14:00 today</strong>).",
        "lines": 3,
        "ans_label": "Precise Sentence =",
        "choice_box": "Write your clear, specific sentence in the workspace.",
        "step_rows": [
            ("1. Replace vague nouns ('stuff', 'room downstairs') with exact terms ('the blood-pressure monitor in ground-floor Treatment Room 2')", "[A1]"),
            ("2. Specify who must act and by when ('must be repaired by the Estates Team before 14:00 today')", "[A1]")
        ],
        "final_answer": "The blood-pressure monitor in ground-floor Treatment Room 2 is faulty and must be repaired by the Estates Team before 14:00 today.",
        "pitfall": "Leaving words like 'stuff' or 'soon' in a formal workplace communication.",
        "reverse_check": "Contains What, Where, Who, and When."
    },
    "writing-context": {
        "title": "Question 1 (Decoding PAF: Purpose, Audience, and Format from an Exam Prompt)",
        "marks": 2,
        "stem": "Read this Pearson Edexcel Writing prompt:<br><em>'Your local council plans to close the town library to save money. Write a letter to the Editor of the local newspaper arguing why the library must remain open.'</em><br>Identify the exact <strong>Purpose</strong>, <strong>Audience</strong>, and <strong>Format</strong>.",
        "lines": 3,
        "ans_label": "Purpose, Audience & Format =",
        "choice_box": "Purpose: ________ | Audience: ________ | Format: ________",
        "step_rows": [
            ("1. Purpose: To persuade / argue that the town library should remain open", "[A1]"),
            ("2. Audience & Format: Newspaper Editor & local residents | Formal Letter (sender address, recipient address, date, salutation, sign-off)", "[A1]")
        ],
        "final_answer": "Purpose: Persuade/Argue | Audience: Newspaper Editor & local readers | Format: Formal Letter.",
        "pitfall": "Writing an article with a headline when the prompt explicitly asks for a 'letter to the Editor'.",
        "reverse_check": "Matches all three PAF pillars."
    },
    "writing-fantastic-finalising": {
        "title": "Question 1 (Spotting Three SPaG Errors in a Proofreading Check)",
        "marks": 2,
        "stem": "Proofread this draft sentence and rewrite it with <strong>all three errors corrected</strong>:<br><em>'We reccommend that all cycling helmets is checked before staff rides to work.'</em>",
        "lines": 3,
        "ans_label": "Proofread Sentence =",
        "choice_box": "Write your corrected sentence in the workspace.",
        "step_rows": [
            ("1. Fix spelling of 'reccommend' → 'recommend' (one c, two m's)", "[A1]"),
            ("2. Fix plural verb agreements: 'helmets is checked' → 'helmets are checked' and 'staff rides' → 'staff ride'", "[A1]")
        ],
        "final_answer": "We recommend that all cycling helmets are checked before staff ride to work.",
        "pitfall": "Fixing 'recommend' but overlooking 'helmets is' or 'staff rides'.",
        "reverse_check": "Check spelling (recommend) and plural verbs (helmets are, staff ride)."
    },
    "writing-form-presentational-and-language-features": {
        "title": "Question 1 (Mandatory Layout Features of a Formal Workplace Report)",
        "marks": 2,
        "stem": "List <strong>four mandatory layout and structural features</strong> required to earn full Format marks in a Level 2 <strong>Formal Report</strong>.",
        "lines": 3,
        "ans_label": "Four Report Features =",
        "choice_box": "1: ________ | 2: ________ | 3: ________ | 4: ________",
        "step_rows": [
            ("1. Report Title / Header block (To / From / Date / Subject) and an Introduction section", "[A1]"),
            ("2. Thematic Subheadings (e.g. Findings) + Numbered/Bulleted Recommendations conclusion", "[A1]")
        ],
        "final_answer": "1. Main Report Title (plus To/From/Date); 2. Introduction; 3. Subheadings for Findings; 4. Bulleted Recommendations.",
        "pitfall": "Starting a Formal Report with 'Dear Sir/Madam' and ending with 'Yours sincerely' (those belong to letters!).",
        "reverse_check": "Verify Title + Subheadings + Bullet points are present."
    },
    "writing-linking-up-your-answer": {
        "title": "Question 1 (Using Discourse Markers to Link Contrasting Ideas)",
        "marks": 2,
        "stem": "Combine these two short, disconnected sentences into one sophisticated complex sentence using a contrasting connective (e.g. <em>Although</em>, <em>Whereas</em>, or <em>Despite</em>):<br><em>'The new electric ambulances cost 15% more to purchase. They reduce annual fuel bills by £4,200 per vehicle.'</em>",
        "lines": 3,
        "ans_label": "Linked Sentence =",
        "choice_box": "Write your linked complex sentence in the workspace.",
        "step_rows": [
            ("1. Open with a subordinating contrasting conjunction ('Although' or 'While')", "[A1]"),
            ("2. Punctuate the subordinate clause with a comma before the main clause", "[A1]")
        ],
        "final_answer": "Although the new electric ambulances cost 15% more to purchase, they reduce annual fuel bills by £4,200 per vehicle.",
        "pitfall": "Joining the two sentences with a comma alone (comma splice) instead of a conjunction.",
        "reverse_check": "Subordinate clause + comma + main clause."
    },
    "writing-organisational-markers": {
        "title": "Question 1 (Writing Informative Subheadings for a Workplace Report)",
        "marks": 2,
        "stem": "You are writing a formal report investigating <strong>Staff Car Park Congestion</strong>.<br>Write <strong>three professional subheadings</strong> to organise the middle and final sections of your report.",
        "lines": 3,
        "ans_label": "Three Subheadings =",
        "choice_box": "1: ________________ | 2: ________________ | 3: ________________",
        "step_rows": [
            ("1. Diagnostic/Findings subheadings: e.g. '1. Current Peak-Hour Congestion Data' and '2. Safety & Late-Arrival Impacts'", "[A1]"),
            ("2. Action-oriented closing subheading: e.g. '3. Costed Recommendations & Permit Controls'", "[A1]")
        ],
        "final_answer": "1. Current Peak-Hour Congestion Findings | 2. Impact on Clinical Shift Handovers | 3. Proposed Permit & Park-and-Ride Recommendations",
        "pitfall": "Using vague one-word headings like 'Middle' or 'End' instead of topic-specific subheadings.",
        "reverse_check": "Each subheading clearly signposts the exact content of its section."
    },
    "writing-planning-your-answer": {
        "title": "Question 1 (Building a 4-Paragraph Bullet Plan Before Drafting)",
        "marks": 2,
        "stem": "An exam task asks you to write an email to staff explaining:<br>• Why the staff canteen is closing for 5 days<br>• Where temporary hot food vans will be parked<br>• How staff can claim a £5 daily meal voucher.<br>Outline a <strong>4-step paragraph plan</strong> (including opening and sign-off) that guarantees full coverage.",
        "lines": 3,
        "ans_label": "4-Step Plan =",
        "choice_box": "Para 1: ______ | Para 2: ______ | Para 3: ______ | Close: ______",
        "step_rows": [
            ("1. Map Email Subject Line + Para 1 (Reason & dates for 5-day canteen closure) + Para 2 (Location & hours of temporary food vans)", "[A1]"),
            ("2. Map Para 3 (Step-by-step instructions to claim £5 voucher) + Professional Sign-off ('Kind regards,')", "[A1]")
        ],
        "final_answer": "Subject Line → Para 1: 5-day refurbishment closure dates → Para 2: Courtyard location of hot food vans → Para 3: How to claim £5 voucher on intranet → Sign-off.",
        "pitfall": "Combining all three prompt bullets into a single unparagraphed block.",
        "reverse_check": "One paragraph per prompt bullet = guaranteed structure marks."
    },
    "writing-spelling": {
        "title": "Question 1 (High-Frequency Functional Skills Exam Spelling Corrections)",
        "marks": 2,
        "stem": "Correct the <strong>four misspelled words</strong> in this formal sentence:<br><em>'The hospital accomodation committee will definately recieve the maintenance scedule tomorrow.'</em>",
        "lines": 3,
        "ans_label": "Four Corrected Spellings =",
        "choice_box": "1: ____________ | 2: ____________ | 3: ____________ | 4: ____________",
        "step_rows": [
            ("1. Correct 'accomodation' → 'accommodation' (double c, double m) and 'definately' → 'definitely' (-ite-, not -ate-)", "[A1]"),
            ("2. Correct 'recieve' → 'receive' (i before e except after c) and 'scedule' → 'schedule' (sch-)", "[A1]")
        ],
        "final_answer": "accommodation, definitely, receive, schedule",
        "pitfall": "Spelling 'definitely' with an 'a' or 'accommodation' with only one 'm'.",
        "reverse_check": "Memory hooks: Double C, Double M in accommodation; 'finite' inside definitely; 'c' followed by 'ei' in receive."
    },
    "writing-tenses": {
        "title": "Question 1 (Eliminating Mid-Sentence Tense Drift)",
        "marks": 2,
        "stem": "Read this incident report sentence where the writer accidentally drifts between past and present tense:<br><em>'Yesterday morning, the fire alarm sounded at 09:15 and all staff evacuate the building before the fire brigade arrives.'</em><br>Rewrite the sentence so it remains consistently in the <strong>past tense</strong> throughout.",
        "lines": 3,
        "ans_label": "Consistent Past-Tense Sentence =",
        "choice_box": "Write your corrected sentence in the workspace.",
        "step_rows": [
            ("1. Change present tense 'evacuate' to past tense 'evacuated' to match 'Yesterday morning... sounded'", "[A1]"),
            ("2. Change present tense 'arrives' to past tense 'arrived'", "[A1]")
        ],
        "final_answer": "Yesterday morning, the fire alarm sounded at 09:15 and all staff evacuated the building before the fire brigade arrived.",
        "pitfall": "Changing 'sounded' to present tense when the time marker 'Yesterday morning' requires past tense.",
        "reverse_check": "Check all three verbs: sounded, evacuated, arrived (all past tense)."
    },
    "writing-the-exam": {
        "title": "Question 1 (Exam Time Allocation & SPaG Mark Weighting)",
        "marks": 2,
        "stem": "In the 60-minute Pearson Edexcel Writing exam (36 marks total), <strong>Task 1 is a shorter functional task (15 marks)</strong> and <strong>Task 2 is an extended task (21 marks)</strong>.<br>State what percentage of total Writing marks is awarded solely for <strong>Spelling, Punctuation, and Grammar (SPaG)</strong>, and how many minutes you should allocate to Task 1 vs Task 2.",
        "lines": 3,
        "ans_label": "SPaG % & Time Split =",
        "choice_box": "SPaG: ________% | Task 1: ____ mins | Task 2: ____ mins",
        "step_rows": [
            ("1. SPaG weighting: Approx. 42% of total marks (15 out of 36 marks across both tasks)", "[A1]"),
            ("2. Optimal 60-minute split: 25 minutes on Task 1 (15 marks) and 35 minutes on Task 2 (21 marks), including 5 minutes proofreading each", "[A1]")
        ],
        "final_answer": "42% (15/36 marks) for SPaG; 25 minutes for Task 1 and 35 minutes for Task 2.",
        "pitfall": "Spending 45 minutes on Task 1 and running out of time on the higher-tariff 21-mark Task 2.",
        "reverse_check": "25 mins + 35 mins = 60 mins total exam time."
    },
    "writing-why-are-you-writing": {
        "title": "Question 1 (Matching Language Choices to Persuasive vs Informative Purpose)",
        "marks": 2,
        "stem": "Write <strong>one informative sentence</strong> and <strong>one persuasive sentence</strong> about a hospital's new <strong>Staff Cycle-to-Work Scheme</strong>.",
        "lines": 3,
        "ans_label": "Informative & Persuasive Sentences =",
        "choice_box": "Informative: ________________ | Persuasive: ________________",
        "step_rows": [
            ("1. Informative sentence (neutral facts): e.g. 'The Staff Cycle-to-Work Scheme launches on 1 May and provides up to £1,000 towards a new bicycle.'", "[A1]"),
            ("2. Persuasive sentence (direct address/benefits): e.g. 'Join the scheme today to slash your commuting costs by 32% and beat morning traffic jams!'", "[A1]")
        ],
        "final_answer": "Informative: The scheme launches on 1 May with grants up to £1,000. | Persuasive: Sign up today to save 32% on a brand-new bike and transform your morning commute!",
        "pitfall": "Using emotional exclamation marks in a neutral informative notice.",
        "reverse_check": "Informative = factual and neutral; Persuasive = compelling and benefit-led."
    },
    # SLC (11 slugs)
    "slc-adapting": {
        "title": "Question 1 (Adapting Spoken Register from Casual Peer Chat to Formal Board Briefing)",
        "marks": 2,
        "stem": "Adapt this casual spoken remark to a colleague so that it is appropriate for a <strong>formal presentation to the NHS Trust Finance Director</strong>:<br><em>'The old printers on Ward 4 are proper rubbish and keep jamming up, so we're wasting loads of cash fixing them.'</em>",
        "lines": 3,
        "ans_label": "Formal Spoken Statement =",
        "choice_box": "Write your formal spoken adaptation in the workspace.",
        "step_rows": [
            ("1. Replace slang ('proper rubbish', 'loads of cash') with formal workplace diction ('unreliable', 'significant maintenance expenditure')", "[A1]"),
            ("2. Frame as a clear, professional operational recommendation", "[A1]")
        ],
        "final_answer": "'The legacy printers on Ward 4 are experiencing frequent mechanical jams, which is generating significant maintenance expenditure and delaying clinical admin.'",
        "pitfall": "Keeping colloquialisms like 'loads of' or 'rubbish' when addressing senior management.",
        "reverse_check": "Professional vocabulary, measured tone, zero slang."
    },
    "slc-asking": {
        "title": "Question 1 (Converting Closed Yes/No Questions into Open Probing Questions)",
        "marks": 2,
        "stem": "During a group discussion on staff wellbeing, a candidate asks:<br><em>'Do you think a longer lunch break is a good idea?'</em> (Closed question).<br>Rewrite this as an <strong>open, probing question</strong> that invites detailed explanation and evidence.",
        "lines": 3,
        "ans_label": "Open Probing Question =",
        "choice_box": "Write your open question in the workspace.",
        "step_rows": [
            ("1. Replace closed opener ('Do you think...') with an open interrogative ('How would...', 'What impact would...')", "[A1]"),
            ("2. Prompt the listener to consider practical effects on shift cover and morale", "[A1]")
        ],
        "final_answer": "'How would extending the staff lunch break to forty-five minutes affect afternoon clinic cover and overall team morale?'",
        "pitfall": "Asking a question that can still be answered with a single word ('Yes' or 'No').",
        "reverse_check": "Starts with 'How', 'Why', or 'What impact' so a full explanation is required."
    },
    "slc-communicating": {
        "title": "Question 1 (Eliminating Verbal Filler and Structuring a Clear Announcement)",
        "marks": 2,
        "stem": "Rewrite this hesitant, filler-heavy spoken announcement into a crisp, authoritative two-sentence briefing:<br><em>'Um, hi guys, basically the fire alarm test is like happening at ten o'clock today, so yeah, don't panic or leave the building unless it rings for more than thirty seconds.'</em>",
        "lines": 3,
        "ans_label": "Crisp Spoken Briefing =",
        "choice_box": "Write your clear spoken briefing in the workspace.",
        "step_rows": [
            ("1. Strip all verbal fillers ('Um', 'basically', 'like', 'so yeah') and informal 'hi guys'", "[A1]"),
            ("2. State the exact time (10:00) and clear 30-second evacuation threshold", "[A1]")
        ],
        "final_answer": "'Good morning everyone. Please note that a routine fire alarm test will take place at 10:00 today; you do not need to evacuate unless the siren sounds continuously for more than thirty seconds.'",
        "pitfall": "Omitting the crucial 30-second safety rule when shortening the announcement.",
        "reverse_check": "Zero filler words; clear time and action threshold."
    },
    "slc-contributing": {
        "title": "Question 1 (Using the Acknowledge-Build-Pivot Technique in Group Discussions)",
        "marks": 2,
        "stem": "In a group discussion about reducing hospital plastic waste, Speaker A says:<br><em>'We should ban all disposable plastic water cups in the waiting rooms immediately.'</em><br>Write a constructive spoken contribution that <strong>acknowledges</strong> Speaker A's point, <strong>adds a practical concern</strong>, and <strong>proposes a solution</strong>.",
        "lines": 3,
        "ans_label": "Spoken Contribution =",
        "choice_box": "Write your spoken response in the workspace.",
        "step_rows": [
            ("1. Acknowledge Speaker A's environmental aim respectfully ('I agree with your goal of cutting plastic waste...')", "[A1]"),
            ("2. Build/Pivot with a practical solution ('...however, patients still need drinking water, so we should replace plastic cups with biodegradable paper cones.')", "[A1]")
        ],
        "final_answer": "'I completely agree that we need to cut single-use plastic in our waiting areas; however, elderly patients still need access to water while waiting, so we could replace plastic cups with recyclable paper cones.'",
        "pitfall": "Interrupting or dismissing Speaker A rudely ('That's a terrible idea') instead of building constructively.",
        "reverse_check": "Follows Agree/Acknowledge → Practical Constraint → Constructive Alternative."
    },
    "slc-extracting-information": {
        "title": "Question 1 (Extracting Actionable Facts from a Spoken Handover)",
        "marks": 2,
        "stem": "Listen to (read) this spoken shift handover transcript:<br><em>'Before I finish, please remember that Bed 4 needs a repeat blood glucose check at 14:30, the pharmacy courier is collecting the controlled drugs box at 15:15, and Mrs Khan in Bed 9 has already had her discharge letter signed.'</em><br>Extract the <strong>two timed tasks</strong> that the incoming nurse must complete.",
        "lines": 3,
        "ans_label": "Two Timed Tasks =",
        "choice_box": "14:30 Task: ________________ | 15:15 Task: ________________",
        "step_rows": [
            ("1. Extract 14:30 task: Repeat blood glucose check for Bed 4", "[A1]"),
            ("2. Extract 15:15 task: Hand over controlled drugs box to pharmacy courier (ignore Bed 9 as already completed)", "[A1]")
        ],
        "final_answer": "1. 14:30 — Repeat blood glucose check for Bed 4; 2. 15:15 — Controlled drugs box collection by pharmacy courier.",
        "pitfall": "Listing Mrs Khan's discharge letter as a pending task when the speaker stated it is already signed.",
        "reverse_check": "Matches exact times (14:30 and 15:15) and actions."
    },
    "slc-language-in-context": {
        "title": "Question 1 (De-escalating a Frustrated Customer Using Empathetic Professional Language)",
        "marks": 2,
        "stem": "A patient at reception says angrily: <em>'I have been waiting forty minutes past my appointment time and nobody has told me what is going on!'</em><br>Write a calm, empathetic two-sentence spoken response that <strong>validates their frustration</strong> and <strong>provides an immediate practical action</strong>.",
        "lines": 3,
        "ans_label": "Empathetic Spoken Response =",
        "choice_box": "Write your spoken response in the workspace.",
        "step_rows": [
            ("1. Apologise sincerely and validate frustration without being defensive ('I completely understand how frustrating it is to wait forty minutes...')", "[A1]"),
            ("2. State immediate helpful action ('Let me telephone the clinic nurse right now to check exactly when you will be called in.')", "[A1]")
        ],
        "final_answer": "'I sincerely apologise that you have been kept waiting forty minutes without an update, and I completely understand your frustration. Let me call the clinic nurse right now so I can give you an exact time for your appointment.'",
        "pitfall": "Using defensive phrases like 'Calm down' or 'It's not my fault the doctor is busy'.",
        "reverse_check": "Empathetic acknowledgement + immediate concrete action."
    },
    "slc-line-of-argument-and-narratives": {
        "title": "Question 1 (Using Signposting Markers to Structure a Formal Presentation)",
        "marks": 2,
        "stem": "You are delivering a 4-minute Level 2 presentation proposing <strong>Staggered Shift Start Times</strong>.<br>Write <strong>two signposting sentences</strong>: one to introduce your first main argument, and one to transition into your final conclusion.",
        "lines": 3,
        "ans_label": "Two Signposting Sentences =",
        "choice_box": "Opening signpost: ____________ | Closing signpost: ____________",
        "step_rows": [
            ("1. Opening signpost: e.g. 'First of all, let us examine how staggered start times will reduce peak car-park congestion by 40%.'", "[A1]"),
            ("2. Closing signpost: e.g. 'To sum up the evidence presented today, staggered shifts benefit both staff wellbeing and patient punctuality.'", "[A1]")
        ],
        "final_answer": "Opening: 'First of all, let us examine how staggered shifts cut peak parking congestion by 40%.' | Closing: 'To sum up the evidence today, staggered start times improve both staff morale and clinic punctuality.'",
        "pitfall": "Jumping between slides or topics with no verbal transition markers.",
        "reverse_check": "Uses explicit discourse markers ('First of all...', 'To sum up...')."
    },
    "slc-responding": {
        "title": "Question 1 (Answering a Challenging Q&A Question Using the Bridge-and-Evidence Method)",
        "marks": 2,
        "stem": "At the end of your presentation on introducing electronic staff rotas, an audience member asks:<br><em>'Won't older staff who aren't confident with smartphones struggle to check their shifts?'</em><br>Write a respectful, evidence-backed spoken response.",
        "lines": 3,
        "ans_label": "Spoken Q&A Response =",
        "choice_box": "Write your spoken answer in the workspace.",
        "step_rows": [
            ("1. Validate the question ('That is an important point regarding digital accessibility...')", "[A1]"),
            ("2. Provide concrete reassurance/remedy ('...which is why we are running drop-in training sessions and keeping a printed rota on the staffroom noticeboard during the 3-month transition.')", "[A1]")
        ],
        "final_answer": "'That is a very important question regarding digital confidence. To ensure nobody is left behind, we will run 1-to-1 smartphone setup clinics next week and continue displaying a printed paper copy on the staffroom board throughout the three-month transition.'",
        "pitfall": "Dismissing the questioner's concern ('Everyone knows how to use a phone nowadays').",
        "reverse_check": "Validates the question + offers a concrete practical safeguard."
    },
    "slc-the-exam": {
        "title": "Question 1 (Pearson Edexcel SLC Assessment Components & Level 1 vs Level 2 Tasks)",
        "marks": 2,
        "stem": "State the <strong>two mandatory assessed activities</strong> you must complete to pass Pearson Edexcel Functional Skills Speaking, Listening & Communicating at <strong>Level 2</strong>, and explain why reading a speech word-for-word from a full script is penalised.",
        "lines": 3,
        "ans_label": "Two Tasks & Script Rule =",
        "choice_box": "Tasks: ____________________ | Script Rule: ____________________",
        "step_rows": [
            ("1. Two L2 tasks: Task 1 = Formal Presentation + Q&A (approx. 4–5 mins + Q&A); Task 2 = Formal Group Discussion (approx. 10–15 mins with 3+ participants)", "[A1]"),
            ("2. Script penalty: Reading word-for-word destroys eye contact and natural spoken intonation (use bulleted cue cards instead)", "[A1]")
        ],
        "final_answer": "Tasks: 1. Formal Presentation with Q&A; 2. Formal Group Discussion. Reading a full script blocks eye contact and natural spoken engagement—use bullet-point cue cards instead.",
        "pitfall": "Turning up to the Presentation without preparing to answer audience questions afterwards.",
        "reverse_check": "Presentation + Q&A + Group Discussion = complete SLC assessment."
    },
    "slc-using-evidence": {
        "title": "Question 1 (Strengthening a Vague Claim with Spoken Statistics and Examples)",
        "marks": 2,
        "stem": "Upgrade this weak, unsupported spoken opinion by incorporating the data provided in brackets:<br><em>'Lots of appointments get wasted when people forget to turn up, so text reminders are really good.'</em><br>(Data: <strong>140 missed appointments per month; SMS reminders reduced Did-Not-Attend rates by 38% in the pilot clinic</strong>).",
        "lines": 3,
        "ans_label": "Evidence-Backed Statement =",
        "choice_box": "Write your upgraded spoken statement in the workspace.",
        "step_rows": [
            ("1. Cite the baseline problem statistic ('Currently, our practice loses 140 appointments every month to Did-Not-Attends...')", "[A1]"),
            ("2. Cite the pilot outcome statistic ('...however, our pilot clinic proved that automated 24-hour SMS reminders cut missed appointments by 38%.')", "[A1]")
        ],
        "final_answer": "'Currently, our practice loses 140 clinical appointments every month to Did-Not-Attends; however, evidence from our pilot clinic proves that automated 24-hour SMS reminders reduce missed appointments by 38%.'",
        "pitfall": "Saying 'a lot of appointments' when exact figures (140 per month, 38% reduction) are available.",
        "reverse_check": "Includes both the 140 baseline figure and the 38% improvement figure."
    },
    "slc-your-turn": {
        "title": "Question 1 (Inviting a Quiet Group Member into the Discussion)",
        "marks": 2,
        "stem": "During your assessed group discussion on workplace recycling, you notice that **Sam** has not spoken for four minutes while two other speakers dominate.<br>Write a polite, natural spoken intervention that **summarises the current point** and **hands the floor directly to Sam**.",
        "lines": 3,
        "ans_label": "Turn-Sharing Intervention =",
        "choice_box": "Write your spoken handover sentence in the workspace.",
        "step_rows": [
            ("1. Briefly summarise the current point ('We have heard strong points on bin placement in the canteen...')", "[A1]"),
            ("2. Invite Sam by name with an open question ('...Sam, from your experience on the reception desk, what recycling challenges do you see in the main foyer?')", "[A1]")
        ],
        "final_answer": "'We have heard some great ideas about canteen bins so far—Sam, we haven't heard your perspective yet; what recycling challenges have you noticed at the main reception desk?'",
        "pitfall": "Putting the quiet candidate on the spot aggressively ('Why haven't you said anything, Sam?').",
        "reverse_check": "Polite summary + warm, specific open invitation by name."
    }
}

WORKSHEETS_ENGLISH_PART2 = []

# 1. Build the 31 English topics from _ENG_REV_MAP + BESPOKE_ENGLISH_Q1
for _slug, _q1 in BESPOKE_ENGLISH_Q1.items():
    _cat, _rev = _ENG_REV_MAP[_slug]
    _title = _rev["clean_topic"]
    _spec_list = [s["code"] for s in _rev.get("spec_This", [])]
    _spec_codes = " • ".join(_spec_list[:4]) if _spec_list else f"Pearson Edexcel Functional Skills English ({_cat.upper()})"
    _rules = _rev.get("golden_rules", [])
    _r0 = f"{_rules[0].get('title', '')}: {_rules[0].get('desc', '')}" if (_rules and isinstance(_rules[0], dict)) else (_rules[0] if _rules else "")
    _golden_rule = re.sub(r"<[^>]+>", "", _r0).strip() if _r0 else f"Master {_title}: Always align Purpose, Audience, Format, and Tone."
    _pqs = _rev["practice_questions"]
    _wms = _rev["worked_models"]
    _traps = _rev.get("examiner_traps", [])

    _q2 = {
        "title": f"Question 2 (Core Skill Application — {_pqs[0]['marks']})",
        "marks": 2,
        "stem": _pqs[0]["question"],
        "lines": 3,
        "ans_label": "Model Response =",
        "choice_box": "Write your response in the workspace provided.",
        "step_rows": _parse_eng_steps(_pqs[0]["solution_steps"]),
        "final_answer": _pqs[0]["correct_answer"],
        "pitfall": _traps[0]["desc"] if _traps else "Omitting specific textual evidence or using informal slang.",
        "reverse_check": _pqs[0]["tutor_tip"]
    }

    _q3 = {
        "title": f"Question 3 ({_wms[0]['title']})",
        "marks": 3,
        "stem": _wms[0]["question"],
        "lines": 4,
        "ans_label": "Structured Answer =",
        "choice_box": "Write your response in the workspace provided.",
        "step_rows": _parse_eng_model_steps(_wms[0]["steps"]),
        "final_answer": _wms[0]["final_answer"],
        "pitfall": _traps[0]["fix"] if _traps else "Check format conventions and SPaG accuracy.",
        "reverse_check": _wms[0]["tutor_tip"]
    }

    _q4 = {
        "title": f"Question 4 (Exam-Style Task — {_pqs[1]['marks']})",
        "marks": 3,
        "stem": _pqs[1]["question"],
        "lines": 4,
        "ans_label": "Model Answer =",
        "choice_box": "Write your response in the workspace provided.",
        "step_rows": _parse_eng_steps(_pqs[1]["solution_steps"]),
        "final_answer": _pqs[1]["correct_answer"],
        "pitfall": _traps[1]["desc"] if len(_traps) > 1 else "Ensure tone and register match the target audience.",
        "reverse_check": _pqs[1]["tutor_tip"]
    }

    _q5 = {
        "title": f"Question 5 ({_wms[1]['title']})",
        "marks": 4,
        "stem": _wms[1]["question"],
        "lines": 5,
        "ans_label": "Extended Model Response =",
        "choice_box": "Write your extended response in the workspace provided.",
        "step_rows": _parse_eng_model_steps(_wms[1]["steps"]),
        "final_answer": _wms[1]["final_answer"],
        "pitfall": _traps[1]["fix"] if len(_traps) > 1 else "Link all points cohesively using discourse markers.",
        "reverse_check": _wms[1]["tutor_tip"]
    }

    _q6 = {
        "title": f"Question 6 (Level 2 Mastery Challenge — {_pqs[2]['marks']})",
        "marks": 4,
        "stem": _pqs[2]["question"],
        "lines": 5,
        "ans_label": "Complete Model Solution =",
        "choice_box": "Write your complete response in the workspace provided.",
        "step_rows": _parse_eng_steps(_pqs[2]["solution_steps"]),
        "final_answer": _pqs[2]["correct_answer"],
        "pitfall": "Failing to proofread spelling, punctuation, and grammar after completing the draft.",
        "reverse_check": _pqs[2]["tutor_tip"]
    }

    WORKSHEETS_ENGLISH_PART2.append(
        make_english_topic(
            slug=_slug,
            title=_title,
            category=_cat,
            spec_codes=_spec_codes,
            golden_rule=_golden_rule,
            q1=_q1,
            q2=_q2,
            q3=_q3,
            q4=_q4,
            q5=_q5,
            q6=_q6
        )
    )

# 2. Add full 6-question bespoke definitions for the 4 Digital Functional Skills slugs
for _d_slug, _d_title in [
    ("digital-functional-skills-level-1", "Digital Functional Skills Level 1: Spreadsheets, Email & Cyber Hygiene"),
    ("digital-functional-skills-mock-exam", "Digital Functional Skills Mock Exam Practice: Formulas, Files & Security"),
    ("digital-functional-skills-revision", "Digital Functional Skills Core Revision: Devices, Cloud & Data Protection"),
    ("printable-digital-skills", "Digital Functional Skills Quick Reference & Formula Drill"),
]:
    WORKSHEETS_ENGLISH_PART2.append(
        make_digital_topic(
            slug=_d_slug,
            title=_d_title,
            spec_codes="DFS.1 • DFS.2 • DFS.3 • DFS.4 • DFS.5",
            golden_rule="Every spreadsheet formula MUST begin with an equals sign (=). Never use =SUM(A1/B1) for division — use =A1/B1. When emailing a large distribution list externally, always put recipient addresses in the BCC field to comply with UK GDPR.",
            q1={
                "title": "Question 1 (Spreadsheet Formulas: SUM, AVERAGE & Multiplication)",
                "marks": 2,
                "stem": "In a clinic stock spreadsheet, cells <strong>C2 to C15</strong> contain the monthly costs of 14 sterile supply orders.<br>(a) Write the exact spreadsheet formula to calculate the <strong>total cost</strong> across cells C2 to C15.<br>(b) Write the exact formula to calculate the <strong>mean (average) cost</strong> across cells C2 to C15.",
                "lines": 3,
                "ans_label": "(a) Total & (b) Average =",
                "choice_box": "(a) ____________________ | (b) ____________________",
                "step_rows": [
                    ("1. (a) Total formula starting with '=' and colon range: =SUM(C2:C15)", "[M1]"),
                    ("2. (b) Mean formula starting with '=' and colon range: =AVERAGE(C2:C15)", "[A1]")
                ],
                "final_answer": "(a) =SUM(C2:C15) | (b) =AVERAGE(C2:C15)",
                "pitfall": "Omitting the leading '=' sign or writing =AVG(C2:C15) instead of the full word =AVERAGE(C2:C15).",
                "reverse_check": "Both formulas start with '=' and use a colon ':' for the contiguous cell range."
            },
            q2={
                "title": "Question 2 (Absolute Cell References & VAT Calculation)",
                "marks": 2,
                "stem": "Cell <strong>B4</strong> contains a net equipment price of <strong>£240.00</strong>, and cell <strong>F1</strong> contains the VAT rate of <strong>20%</strong>.<br>You want to write a formula in cell <strong>C4</strong> to calculate the VAT amount and then drag-fill (replicate) that formula down column C from C4 to C20.<br>Write the exact formula for cell <strong>C4</strong> using an <strong>absolute cell reference</strong> for cell F1.",
                "lines": 3,
                "ans_label": "Formula in C4 =",
                "choice_box": "____________________",
                "step_rows": [
                    ("1. Multiply relative cell B4 by cell F1 using '*' operator", "[M1]"),
                    ("2. Lock cell F1 with dollar signs so it does not shift when dragged down: =B4*$F$1", "[A1]")
                ],
                "final_answer": "=B4*$F$1",
                "pitfall": "Writing =B4*F1 without '$' signs, which shifts to F2, F3, F4 when dragged down column C.",
                "reverse_check": "The '$' before F and before 1 locks both column F and row 1."
            },
            q3={
                "title": "Question 3 (Logical IF Statements in a Training Tracker)",
                "marks": 3,
                "stem": "In a staff mandatory training spreadsheet, cell <strong>D5</strong> holds an employee's fire-safety test score (out of 100).<br>The pass mark is <strong>75 or above</strong>.<br>Write an <strong>=IF</strong> formula in cell <strong>E5</strong> that displays <strong>\"Compliant\"</strong> if D5 is 75 or higher, and <strong>\"Retake Required\"</strong> if it is below 75.",
                "lines": 4,
                "ans_label": "IF Formula =",
                "choice_box": "=IF( ________________ , ________________ , ________________ )",
                "step_rows": [
                    ("1. Set logical condition testing if D5 is at least 75: D5>=75", "[M1]"),
                    ("2. Set value_if_true in double quotes: \"Compliant\"", "[M1]"),
                    ("3. Set value_if_false in double quotes: =IF(D5>=75, \"Compliant\", \"Retake Required\")", "[A1]")
                ],
                "final_answer": "=IF(D5>=75, \"Compliant\", \"Retake Required\")",
                "pitfall": "Using >75 instead of >=75 (which would wrongly fail someone who scored exactly 75), or forgetting quotation marks around text strings.",
                "reverse_check": "Test D5=75: 75>=75 is TRUE → returns \"Compliant\"."
            },
            q4={
                "title": "Question 4 (UK GDPR Email Security: CC vs BCC & File Encryption)",
                "marks": 3,
                "stem": "A clinic administrator needs to email a monthly appointment update to <strong>85 private patients</strong> and also send an attached spreadsheet containing <strong>patient dates of birth and NHS numbers</strong> to the Practice Manager.<br>Explain:<br>(a) Which email address field (<strong>To, CC, or BCC</strong>) must be used for the 85 patients and why.<br>(b) One technical security measure required before emailing the sensitive patient spreadsheet.",
                "lines": 4,
                "ans_label": "(a) Field & (b) Security Measure =",
                "choice_box": "(a) Field: ________ | (b) Security: ________________",
                "step_rows": [
                    ("1. (a) Use BCC (Blind Carbon Copy) for the 85 patients", "[M1]"),
                    ("2. (a) Reason: Hides patients' personal email addresses from one another, preventing a UK GDPR data breach", "[A1]"),
                    ("3. (b) Password-protect / encrypt the spreadsheet (and share the password via a separate channel such as SMS/telephone)", "[A1]")
                ],
                "final_answer": "(a) BCC — hides recipients' email addresses from each other under UK GDPR. (b) Encrypt/password-protect the spreadsheet and send the password via a separate channel.",
                "pitfall": "Putting 85 external patients in the 'CC' field, which exposes every patient's email address to all 84 other patients.",
                "reverse_check": "BCC = Blind Carbon Copy (external privacy); Encryption = file confidentiality."
            },
            q5={
                "title": "Question 5 (Spotting Phishing Attacks & Malicious URLs)",
                "marks": 4,
                "stem": "An accounts clerk receives this email:<br><strong>From:</strong> <code>security-alert@nhs-payrol-update.ru</code><br><strong>Subject:</strong> URGENT: Your NHS Pension Account Will Be Deleted in 2 Hours!<br><strong>Body:</strong> <em>'Dear User, click <u>http://bit.ly/3x99pQ</u> immediately and enter your staff login password and bank sort code to avoid suspension.'</em><br><br>Identify <strong>three red flags</strong> proving this email is a <strong>phishing attack</strong>, and state the <strong>correct workplace action</strong> the clerk should take.",
                "lines": 5,
                "ans_label": "Three Red Flags & Action =",
                "choice_box": "Flags: 1. ________ 2. ________ 3. ________ | Action: ________",
                "step_rows": [
                    ("1. Flag 1 (Spoofed/Suspicious Sender Domain): Misspelled 'payrol' and foreign '.ru' domain instead of official '@nhs.net'", "[P1]"),
                    ("2. Flag 2 (Artificial Urgency & Generic Greeting): 'Deleted in 2 Hours!' panic threat and impersonal 'Dear User'", "[P1]"),
                    ("3. Flag 3 (Masked Unsecure Link & Credential Request): Unsecure 'http://' shortened link asking for password and bank details", "[M1]"),
                    ("4. Correct Action: Do NOT click the link or reply; report the email immediately to the IT Security Helpdesk using the Report Phishing button", "[A1]")
                ],
                "final_answer": "Red flags: 1. Misspelled '.ru' sender domain ('payrol'); 2. Artificial 2-hour panic deadline & 'Dear User'; 3. Masked http link requesting password. Action: Do not click; report immediately to IT Security.",
                "pitfall": "Replying to the email to ask if it is genuine.",
                "reverse_check": "Check sender domain, urgency tone, URL protocol, and IT reporting protocol."
            },
            q6={
                "title": "Question 6 (Cloud File Management, Naming Conventions & Version Control)",
                "marks": 4,
                "stem": "A project team shares a folder containing these files:<br>• <code>rota.xlsx</code><br>• <code>rota_new_final2_johns_copy.xlsx</code><br>• <code>ward_budget_2026.pdf</code><br><br>(a) Explain why <code>rota_new_final2_johns_copy.xlsx</code> violates professional version-control standards, and write a clean, standardised filename for <strong>Version 2.1 of the Ward 4 Rota created on 14 October 2026</strong>.<br>(b) If the team wants 5 managers to view <code>rota.xlsx</code> on SharePoint <strong>without being able to accidentally delete or alter shift cells</strong>, what file permission level should be set?",
                "lines": 5,
                "ans_label": "(a) Filename & (b) Permission =",
                "choice_box": "(a) Filename: ________________________ | (b) Permission: ____________",
                "step_rows": [
                    ("1. (a) Critique: Ambiguous words like 'new_final2' make it impossible to sort chronologically or identify the latest authoritative file", "[P1]"),
                    ("2. (a) Standardised ISO filename: 2026-10-14_Ward4_Rota_v2.1.xlsx (or Ward4_Rota_2026-10-14_v2.1.xlsx)", "[M1]"),
                    ("3. (b) SharePoint permission level: Set to 'Read-Only' / 'View Only' (disable 'Can Edit')", "[P1]"),
                    ("4. (b) Benefit: Allows all 5 managers to view and download the rota while preventing accidental overwrites", "[A1]")
                ],
                "final_answer": "(a) Ambiguous naming causes version confusion; rename to '2026-10-14_Ward4_Rota_v2.1.xlsx'. (b) Set SharePoint access to 'View Only' / 'Read-Only'.",
                "pitfall": "Using spaces or slashes (14/10/2026) in filenames, which are invalid in operating system file paths.",
                "reverse_check": "YYYY-MM-DD_Topic_vX.X.ext sorts chronologically and prevents ambiguity."
            }
        )
    )

print(f"Loaded {len(WORKSHEETS_ENGLISH_PART2)} bespoke English & Digital worksheet topics in bespoke_worksheets_english_part2.py")
