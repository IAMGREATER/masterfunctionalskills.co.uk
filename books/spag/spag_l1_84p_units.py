# spag_l1_84p_units.py
# 26 Complete Two-Page Murphy-Style Units for Functional Skills English Level 1 SPaG Mastery
# Publication: Master Functional Skills English Level 1 SPaG Mastery (84-Page Edition)

L1_UNITS_26 = [
    # -------------------------------------------------------------------------
    # UNIT 1
    # -------------------------------------------------------------------------
    {
        "unit": 1,
        "title": "Sentence Basics — Capital Letters & Full Stops",
        "format": "Workplace Shift Handover Log",
        "anchor_title": "Shift Handover Log & Daily Operational Notes",
        "anchor_text": "In a busy logistics warehouse, the morning shift supervisor logs machine maintenance updates. If thoughts run together without full stops or capital letters, colleagues misread critical safety boundaries, leading to costly operational downtime.",
        "rule_formula_title": "Complete Sentence Architecture: Subject + Finite Verb + Complete Thought",
        "rule_formula_html": """A complete grammatical sentence must express a single finished thought and contain two essential pillars:
<div class="formula-strip">
  <span class="fpill fpill-punct">Capital Letter</span> &rarr;
  <span class="fpill fpill-subj">[Subject: Who/What]</span> +
  <span class="fpill fpill-verb">[Finite Verb: Action/State]</span> +
  <span class="fpill fpill-clause">[Complete Sense]</span> &rarr;
  <span class="fpill fpill-punct">Full Stop (.)</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Sentence Fragment:</strong> Missing a finite verb or subject (e.g. <em>"Because the conveyor stopped."</em> &mdash; this is an incomplete dependent clause).</li>
  <li><strong>Run-on Sentence:</strong> Two independent sentences fused together with no terminal punctuation (e.g. <em>"The conveyor stopped the engineer arrived."</em>).</li>
  <li><strong>Full Stop Rule:</strong> Conclude every declarative sentence with a solid full stop (.). The subsequent sentence must open with a crisp capital letter.</li>
</ul>""",
        "worked_bad": "the morning shift finished at eight all safety gates was locked secure. Because the team followed protocol.",
        "worked_good": "The morning shift finished at eight. All safety gates were locked securely because the team followed protocol.",
        "worked_why": "Capitalised the sentence starters ('The', 'All'), split the run-on with a full stop, and joined the dangling fragment into a complete causal sentence.",
        "golden_rule": "THE BREATH TEST: Read your sentence aloud. When your voice drops and your breath pauses naturally before a new thought, insert a full stop and start the next word with a capital letter.",
        "exercise_a": [
            ("Which sentence contains both a capital letter and a correct terminal full stop?",
             ["A) the warehouse shutter opened at dawn.", "B) The warehouse shutter opened at dawn.", "C) The warehouse shutter opened at dawn"],
             "B"),
            ("Identify the sentence fragment that cannot stand alone as a complete sentence:",
             ["A) Forklift 3 passed its hydraulic inspection.", "B) After the technician tested the emergency brake.", "C) We ordered replacement filters this morning."],
             "B"),
            ("Choose the correctly punctuated option to repair this run-on: <em>'The printer jammed we phoned IT.'</em>",
             ["A) The printer jammed, we phoned IT.", "B) The printer jammed we phoned IT.", "C) The printer jammed. We phoned IT."],
             "C"),
            ("Select the option with zero sentence boundary errors:",
             ["A) Stock arrives on Monday. Delivery drivers must wear high-visibility vests.", "B) Stock arrives on Monday delivery drivers must wear high-visibility vests.", "C) stock arrives on Monday. delivery drivers must wear vests."],
             "A")
        ],
        "exercise_b": [
            ("Rewrite with capital letter and full stop", "the delivery docket was signed by the depot manager", "The delivery docket was signed by the depot manager."),
            ("Split the fused run-on into two sentences", "safety helmets are mandatory visitors must sign in", "Safety helmets are mandatory. Visitors must sign in."),
            ("Complete the fragment to make a valid sentence", "before entering the packing line", "Before entering the packing line, staff must wash their hands.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Depot Daily Log",
        "proofreading_scenario": "Review the morning handover entry written by a trainee depot supervisor. There are exactly 4 sentence boundary errors (missing capital letters, missing full stops, or fused run-ons).",
        "proofreading_text": "all parcel chutes were cleared before 06:00. the night crew sorted four thousand parcels without delays the main conveyor belt operated smoothly throughout the shift. fresh battery packs have been placed in charging bay 2",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing capital letter at start ('all' -> 'All')",
            "Missing capital letter at start of second sentence ('the' -> 'The')",
            "Fused run-on between 'delays' and 'the' (needs full stop and capital: 'delays. The main')",
            "Missing full stop at the end of the final sentence ('bay 2' -> 'bay 2.')"
        ],
        "writing_prompt": "Write two complete, correctly punctuated sentences describing two routine opening tasks completed at your workplace this morning. Ensure each sentence starts with a capital letter and concludes with a full stop."
    },

    # -------------------------------------------------------------------------
    # UNIT 2
    # -------------------------------------------------------------------------
    {
        "unit": 2,
        "title": "Question Marks vs Exclamation Marks in Customer Service",
        "format": "Customer Service Email & Chat Protocol",
        "anchor_title": "Customer Helpdesk & Client Correspondence",
        "anchor_text": "Customer service advisors respond to enquiries, complaints, and emergencies. Using a full stop instead of a question mark looks indifferent or careless, while overuse of exclamation marks appears unprofessional, aggressive, or hysterical.",
        "rule_formula_title": "Direct Inquiry vs Urgent Exclamation Grammar",
        "rule_formula_html": """Punctuation governs customer tone and transactional clarity:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Direct Question]</span> &rarr; Inversion (Auxiliary + Subject) &rarr;
  <span class="fpill fpill-punct">Question Mark (?)</span>
</div>
<div class="formula-strip" style="margin-top:3px;">
  <span class="fpill fpill-conn">[Safety Hazard / Urgent Warning]</span> &rarr; High Alarm &rarr;
  <span class="fpill fpill-punct">Exclamation Mark (!)</span> (Maximum ONE)
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Direct Question:</strong> Requires an answer or action from the reader (e.g. <em>"Would you prefer a refund or an exchange?"</em>). Conclude with a question mark.</li>
  <li><strong>Indirect Statement:</strong> Do not place a question mark on indirect reported questions (e.g. <em>"The customer asked if the parcel had arrived."</em> &mdash; end with a full stop).</li>
  <li><strong>Exclamation Control:</strong> Reserved exclusively for urgent hazard warnings (e.g. <em>"Caution! Wet floor."</em>). Never use multiple marks (<em>!!</em> or <em>!?!?</em>) in workplace writing.</li>
</ul>""",
        "worked_bad": "Could you please confirm your invoice number. Hurry up and reply immediately!!!",
        "worked_good": "Could you please confirm your invoice number? Please reply at your earliest convenience.",
        "worked_why": "Replaced the careless full stop with a required question mark and eliminated triple exclamation marks to maintain polite professional composure.",
        "golden_rule": "THE REACTION TEST: If you expect the reader to provide an answer, end with a question mark (?). If you are declaring an emergency safety hazard, use exactly ONE exclamation mark (!). Never use exclamation marks for polite requests.",
        "exercise_a": [
            ("Which sentence requires a question mark at the end?",
             ["A) I am writing to ask about your return policy.", "B) Could you confirm your tracking reference number", "C) We received your replacement order yesterday."],
             "B"),
            ("Select the sentence with professional, appropriate exclamation mark usage:",
             ["A) Warning! Isolate electrical supply before opening panel.", "B) Thanks for your email today!!!!!!", "C) Please help me right now!!!"],
             "A"),
            ("Identify the indirect question that correctly ends with a full stop:",
             ["A) Where did the delivery driver leave the crate?", "B) The client enquired whether weekend delivery was available.", "C) Did the client enquire about weekend delivery."],
             "B"),
            ("Which customer response maintains an authoritative yet polite tone?",
             ["A) Why have you not responded yet!", "B) Would 2:00 pm suit you for the engineer's visit?", "C) Call us back immediately!"],
             "B")
        ],
        "exercise_b": [
            ("Add the correct terminal mark (? or .)", "Would you like me to reserve the appointment for Thursday", "Would you like me to reserve the appointment for Thursday?"),
            ("Remove informal exclamation marks", "Your order has been dispatched today!!! Have a lovely weekend!!", "Your order has been dispatched today. Have a lovely weekend."),
            ("Punctuate the safety warning correctly", "Danger Do not enter while machinery is in operation", "Danger! Do not enter while machinery is in operation.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Customer Resolution Email",
        "proofreading_scenario": "Examine this draft email from a customer service representative to a client whose delivery was delayed. There are exactly 4 terminal punctuation errors.",
        "proofreading_text": "Dear Mr Patel, Thank you for contacting our customer support team today! Would you mind confirming your delivery postcode. We investigated the delay and located your consignment in our regional hub! Would you like us to reschedule the courier for tomorrow morning.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Over-enthusiastic exclamation mark after routine greeting ('today!' -> 'today.')",
            "Missing question mark on polite request ('postcode.' -> 'postcode?')",
            "Inappropriate exclamation mark on routine status update ('regional hub!' -> 'regional hub.')",
            "Missing question mark on direct closing offer ('tomorrow morning.' -> 'tomorrow morning?')"
        ],
        "writing_prompt": "Write two professional sentences for an online customer enquiry response: one polite direct question asking for the customer's account reference, and one sentence stating when your department opens."
    },

    # -------------------------------------------------------------------------
    # UNIT 3
    # -------------------------------------------------------------------------
    {
        "unit": 3,
        "title": "Capital Letters for Proper Nouns, Acronyms & Titles (MINTS)",
        "format": "Corporate Visitor Badge & Event Roster",
        "anchor_title": "Conference Registration & Corporate Identity",
        "anchor_text": "Administrative assistants process delegate badges, client correspondence, and statutory paperwork. Forgetting to capitalise proper names, days, months, and official accreditations signals disrespect and damages organizational credibility.",
        "rule_formula_title": "The MINTS Framework for Flawless Capitalisation",
        "rule_formula_html": """Remember the five essential categories that demand capital letters:
<div class="formula-strip">
  <span class="fpill fpill-punct">M</span> Months &amp; Days &bull;
  <span class="fpill fpill-subj">I</span> The Pronoun 'I' &bull;
  <span class="fpill fpill-verb">N</span> Names &amp; Places &bull;
  <span class="fpill fpill-conn">T</span> Titles &amp; Headings &bull;
  <span class="fpill fpill-clause">S</span> Start of Sentences
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Months &amp; Days:</strong> Always capitalise <em>Monday, Friday, January, September</em>. Do not capitalise general seasons (<em>spring, autumn</em>) unless part of a proper title.</li>
  <li><strong>Names, Places &amp; Nationalities:</strong> <em>Sarah Jenkins, Manchester, British, English, NHS</em>.</li>
  <li><strong>Job Titles &amp; Honorifics:</strong> Capitalise specific individual titles (<em>Dr Evans, Prime Minister, General Manager Patel</em>), but use lowercase for general job roles (<em>our manager, the technician</em>).</li>
  <li><strong>Acronyms:</strong> Initialisms and acronyms are set in full capitals: <em>UK, Ofqual, PPE, CCTV, HR</em>.</li>
</ul>""",
        "worked_bad": "on wednesday, i accompanied dr green to manchester general hospital to inspect the new ppe store.",
        "worked_good": "On Wednesday, I accompanied Dr Green to Manchester General Hospital to inspect the new PPE store.",
        "worked_why": "Applied capitals to day ('Wednesday'), pronoun ('I'), title ('Dr Green'), hospital proper name ('Manchester General Hospital'), and acronym ('PPE').",
        "golden_rule": "THE PASSPORT TEST: If a word is a specific official name found on a passport, calendar, or geographical map, give it a capital letter. Common things (hospital, manager, day) stay lowercase.",
        "exercise_a": [
            ("Which sentence capitalises all days, months, and proper nouns correctly?",
             ["A) The audit begins on Tuesday, 14 october at St Mary's clinic.", "B) The audit begins on Tuesday, 14 October at St Mary's Clinic.", "C) The audit begins on tuesday, 14 October at St Mary's clinic."],
             "B"),
            ("Select the sentence where the pronoun 'I' and job titles are handled accurately:",
             ["A) After meeting Director Patel, i completed the health assessment.", "B) After meeting director Patel, I completed the health assessment.", "C) After meeting Director Patel, I completed the health assessment."],
             "C"),
            ("Which acronym and place name combination is 100% correct?",
             ["A) Security reviewed the cctv footage recorded in Birmingham.", "B) Security reviewed the CCTV footage recorded in Birmingham.", "C) Security reviewed the CCTV footage recorded in birmingham."],
             "B"),
            ("Identify the sentence with no capitalisation errors:",
             ["A) We are visiting london in August to attend an NHS training workshop.", "B) We are visiting London in august to attend an NHS training workshop.", "C) We are visiting London in August to attend an NHS training workshop."],
             "C")
        ],
        "exercise_b": [
            ("Capitalise days and months", "the staff training commences on friday, 4 november", "The staff training commences on Friday, 4 November."),
            ("Correct the pronoun and proper noun", "yesterday i met david brown at leeds central station", "Yesterday I met David Brown at Leeds Central Station."),
            ("Capitalise workplace acronyms", "all warehouse visitors must report to hr and wear ppe", "All warehouse visitors must report to HR and wear PPE.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Visitor Induction Form",
        "proofreading_scenario": "Proofread this visitor notice posted in the reception of Apex Healthcare Solutions in Bristol. Identify exactly 5 missing capital letters.",
        "proofreading_text": "Welcome to apex health centre. on thursday, ms claire taylor will conduct an induction for new apprentices from bath college. all delegates must sign the visitor ledger, present photo id, and collect a security pass from reception before entering building b.",
        "proofreading_err_count": 5,
        "proofreading_errors": [
            "Missing capital on organisation name ('apex health centre' -> 'Apex Health Centre')",
            "Missing capital at sentence start / day of week ('on thursday' -> 'On Thursday')",
            "Missing capital on proper name ('ms claire taylor' -> 'Ms Claire Taylor')",
            "Missing capital on college name ('bath college' -> 'Bath College')",
            "Missing capital at start of sentence ('all delegates' -> 'All delegates')"
        ],
        "writing_prompt": "Write two sentences describing an upcoming meeting. Mention the day of the week, the month, the name of a colleague or supervisor, and an organization or city name with correct capital letters."
    },

    # -------------------------------------------------------------------------
    # UNIT 4
    # -------------------------------------------------------------------------
    {
        "unit": 4,
        "title": "Joining Sentences with Coordinating Conjunctions (And, But, Or, So)",
        "format": "Health & Safety Incident Briefing",
        "anchor_title": "Incident Log & Risk Assessment Updates",
        "anchor_text": "When writing risk assessments, joining related facts clearly shows cause, contrast, or alternatives. Writing only short, choppy sentences makes reports sound juvenile, while joining sentences incorrectly creates confusing run-ons.",
        "rule_formula_title": "The FANBOYS Toolkit: Coordinating Equal Clauses",
        "rule_formula_html": """Coordinating conjunctions connect two independent, grammatically equal clauses:
<div class="formula-strip">
  <span class="fpill fpill-clause">[Independent Clause 1]</span> +
  <span class="fpill fpill-punct">,</span>
  <span class="fpill fpill-conn">[and / but / or / so]</span> +
  <span class="fpill fpill-clause">[Independent Clause 2]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>AND:</strong> Adds similar information (e.g. <em>"The fire alarm sounded, and all staff evacuated immediately."</em>).</li>
  <li><strong>BUT:</strong> Signals an unexpected contrast (e.g. <em>"The engineer arrived on time, but the replacement valve was missing."</em>).</li>
  <li><strong>OR:</strong> Offers choices or alternatives (e.g. <em>"You can submit the paper timesheet, or you can log your hours online."</em>).</li>
  <li><strong>SO:</strong> Shows a direct logical result (e.g. <em>"The access road was flooded, so deliveries were redirected."</em>).</li>
</ul>""",
        "worked_bad": "The forklift battery died. The operator plugged it in. The backup charger was broken.",
        "worked_good": "The forklift battery died, so the operator plugged it in, but the backup charger was broken.",
        "worked_why": "Combined choppy repetitive fragments using 'so' (logical outcome) and 'but' (contrast), improving flow and cohesion.",
        "golden_rule": "THE LOGIC MATCH: Never use 'and' when you mean 'but' or 'so'. Use 'but' for surprises/contrast, 'so' for results, and 'or' for alternatives.",
        "exercise_a": [
            ("Choose the best conjunction to show a contrast: <em>'We ordered fifty safety vests, [______] only twenty arrived.'</em>",
             ["A) and", "B) but", "C) so"],
             "B"),
            ("Choose the conjunction indicating a result: <em>'The printer toner was empty, [______] Marcus replaced the cartridge.'</em>",
             ["A) or", "B) but", "C) so"],
             "C"),
            ("Which sentence joins two complete thoughts correctly with a conjunction?",
             ["A) The kitchen passed the inspection, and the hygiene certificate was renewed.", "B) The kitchen passed the inspection and, the hygiene certificate was renewed.", "C) The kitchen passed the inspection, but the hygiene certificate was renewed."],
             "A"),
            ("Identify the sentence presenting two clear workplace alternatives:",
             ["A) You must wear ear protection or leave the machine hall.", "B) You must wear ear protection so leave the machine hall.", "C) You must wear ear protection but leave the machine hall."],
             "A")
        ],
        "exercise_b": [
            ("Join with 'but' to show contrast", "The technician tested the heating unit. It failed the safety check.", "The technician tested the heating unit, but it failed the safety check."),
            ("Join with 'so' to show a result", "The delivery lorry arrived early. The stock team unloaded the goods.", "The delivery lorry arrived early, so the stock team unloaded the goods."),
            ("Join with 'or' to present an option", "Staff can book annual leave by email. They can complete a paper form.", "Staff can book annual leave by email, or they can complete a paper form.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Warehouse Equipment Audit",
        "proofreading_scenario": "Read this brief incident summary. Exactly 4 conjunctions or punctuation joins have been misused, obscuring the logical relationship between events.",
        "proofreading_text": "The hydraulic lift malfunctioned at 09:30 and the warehouse manager was notified immediately. An external contractor arrived within twenty minutes so he did not have the correct replacement seals. The supervisor offered to halt work on Bay 4 but the team moved to Bay 5 to maintain packing targets. Staff could wait for repairs and they could clean the packing benches.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Misused 'and' for logical consequence ('at 09:30 and the manager' -> 'at 09:30, so the manager')",
            "Misused 'so' for contrast ('within twenty minutes so he did not' -> 'within twenty minutes, but he did not')",
            "Misused 'but' where 'so' is required ('halt work on Bay 4 but the team' -> 'halt work on Bay 4, so the team')",
            "Misused 'and' where 'or' is required for choices ('for repairs and they could clean' -> 'for repairs, or they could clean')"
        ],
        "writing_prompt": "Write a compound sentence describing two actions during an emergency fire drill at your college or workplace. Use either 'but' or 'so' to join the two thoughts smoothly."
    },

    # -------------------------------------------------------------------------
    # UNIT 5
    # -------------------------------------------------------------------------
    {
        "unit": 5,
        "title": "Joining Sentences with Subordinating Conjunctions (Because, Although, When)",
        "format": "Staff Appraisal & Performance Review",
        "anchor_title": "Staff Performance Appraisal & Action Planning",
        "anchor_text": "In professional appraisals and development plans, employees explain why targets were met or what challenges occurred. Subordinating conjunctions link causes, concessions, and conditions with precision.",
        "rule_formula_title": "Complex Sentence Hierarchy: Main Clause + Subordinate Clause",
        "rule_formula_html": """A complex sentence contains an independent main clause and a dependent subordinate clause:
<div class="formula-strip">
  <span class="fpill fpill-clause">[Main Clause]</span> +
  <span class="fpill fpill-conn">[because / although / when / if]</span> +
  <span class="fpill fpill-clause">[Subordinate Clause]</span>
</div>
<div class="formula-strip" style="margin-top:3px;">
  <span class="fpill fpill-conn">[Subordinating Conjunction]</span> +
  <span class="fpill fpill-clause">[Subordinate Clause]</span> +
  <span class="fpill fpill-punct">,</span> +
  <span class="fpill fpill-clause">[Main Clause]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>BECAUSE (Reason):</strong> <em>"Hannah exceeded her sales target because she phoned prospective clients daily."</em></li>
  <li><strong>ALTHOUGH (Concession):</strong> <em>"Although the software crashed twice, James submitted the payroll report on schedule."</em></li>
  <li><strong>WHEN / IF (Condition/Time):</strong> <em>"When the customer arrives, please escort them to Meeting Room 3."</em></li>
  <li><strong>Comma Rule:</strong> When the subordinate clause comes FIRST, place a comma after it. When it comes second, no comma is required.</li>
</ul>""",
        "worked_bad": "Because Priya completed her training course early. She was promoted to team leader.",
        "worked_good": "Because Priya completed her training course early, she was promoted to team leader.",
        "worked_why": "Removed the incorrect full stop that isolated the subordinate clause into a fragment, adding a required comma before the main clause.",
        "golden_rule": "THE COMMA FLIP-FLOP: If 'Because', 'Although', or 'When' opens the sentence, put a comma in the middle. If it sits in the middle, you generally need no comma.",
        "exercise_a": [
            ("Choose the subordinating conjunction showing concession: <em>'[______] the team was short-staffed, they finished all patient rounds.'</em>",
             ["A) Because", "B) Although", "C) When"],
             "B"),
            ("Which sentence is punctuated correctly with a subordinate clause at the start?",
             ["A) When the alarm rings please evacuate to Assembly Point A.", "B) When the alarm rings, please evacuate to Assembly Point A.", "C) When, the alarm rings please evacuate."],
             "B"),
            ("Identify the sentence fragment that cannot stand by itself:",
             ["A) Although the delivery van broke down on the M1.", "B) The delivery van broke down on the M1 yesterday.", "C) We booked a replacement vehicle immediately."],
             "A"),
            ("Select the sentence with correct middle subordinating conjunction usage (no unnecessary comma):",
             ["A) Tariq received a bonus, because he mentored three apprentices.", "B) Tariq received a bonus because he mentored three apprentices.", "C) Tariq, received a bonus because he mentored three apprentices."],
             "B")
        ],
        "exercise_b": [
            ("Combine using 'because' at the beginning", "The clinic postponed appointments. The heating system broke down.", "Because the heating system broke down, the clinic postponed appointments."),
            ("Combine using 'although' in the middle", "Leon passed his driving test. He was extremely nervous.", "Leon passed his driving test although he was extremely nervous."),
            ("Combine using 'when' at the beginning", "The supervisor signs the form. You can collect your safety boots.", "When the supervisor signs the form, you can collect your safety boots.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Performance Appraisal Summary",
        "proofreading_scenario": "Read this appraisal excerpt for a hospitality trainee. Identify exactly 4 subordinate clause and comma punctuation errors.",
        "proofreading_text": "Although Jack joined the catering department only three months ago. He has adapted exceptionally well. Because he demonstrated excellent knife skills he was assigned to the pastry section. Jack always washes his hands thoroughly, when he enters the commercial kitchen. If guests make dietary requests Jack communicates them clearly to the head chef.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Fragment created by full stop after introductory although-clause ('ago. He has' -> 'ago, he has')",
            "Missing comma after introductory because-clause ('skills he was' -> 'skills, he was')",
            "Unnecessary comma before middle when-clause ('thoroughly, when he' -> 'thoroughly when he')",
            "Missing comma after introductory if-clause ('requests Jack' -> 'requests, Jack')"
        ],
        "writing_prompt": "Write a complex sentence starting with 'Although' explaining how you overcame a difficult workplace or study challenge to achieve a positive outcome. Remember the comma!"
    },

    # -------------------------------------------------------------------------
    # UNIT 6
    # -------------------------------------------------------------------------
    {
        "unit": 6,
        "title": "Commas in Everyday Lists of Items & Actions",
        "format": "Stock Requisition & Procurement Order",
        "anchor_title": "Catering Stock Orders & Kitchen Inventory",
        "anchor_text": "Head chefs and procurement officers order perishable ingredients and industrial equipment daily. Missing or misplaced commas in requisition orders cause confusion between distinct items, resulting in incorrect deliveries and wasted budgets.",
        "rule_formula_title": "Listing Mechanics: Items, Adjectives & Actions",
        "rule_formula_html": """Commas separate three or more items, modifiers, or verb phrases in a series:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Item 1]</span> <span class="fpill fpill-punct">,</span>
  <span class="fpill fpill-subj">[Item 2]</span> <span class="fpill fpill-punct">,</span>
  <span class="fpill fpill-subj">[Item 3]</span>
  <span class="fpill fpill-conn">and</span>
  <span class="fpill fpill-subj">[Item 4]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Serial Commas:</strong> Use commas between every item in a list of three or more nouns (e.g. <em>"Please order milk, butter, cheddar cheese and double cream."</em>).</li>
  <li><strong>Actions in Series:</strong> Separate consecutive verb phrases (e.g. <em>"The technician checked the fluid level, replaced the gasket, cleaned the housing and tested the pump."</em>).</li>
  <li><strong>Two Items Only:</strong> Never insert a comma when joining only two items (e.g. <em>"Order bread and butter."</em> NOT <em>"Order bread, and butter."</em>).</li>
  <li><strong>The 'And' Rule:</strong> In standard Level 1 UK writing, do not place a comma immediately before or after 'and' unless required to prevent ambiguity.</li>
</ul>""",
        "worked_bad": "The pantry order requires flour sugar eggs, baking powder, and, vanilla essence.",
        "worked_good": "The pantry order requires flour, sugar, eggs, baking powder and vanilla essence.",
        "worked_why": "Inserted missing commas between the first three items and deleted unnecessary commas around 'and'.",
        "golden_rule": "THE SEPARATION TEST: If you have 3 or more items, put commas between each one except before the final 'and'. If you only have 2 items, use 'and' with no comma at all.",
        "exercise_a": [
            ("Which sentence punctuates a list of office supplies correctly?",
             ["A) We ordered pens paper clips envelopes and printer ink.", "B) We ordered pens, paper clips, envelopes and printer ink.", "C) We ordered, pens paper clips envelopes and printer ink."],
             "B"),
            ("Identify the sentence that incorrectly adds a comma between two items only:",
             ["A) The apprentice repaired the faulty plug, and fitted the new fuse.", "B) The apprentice repaired the faulty plug and fitted the new fuse.", "C) The apprentice checked both cables."],
             "A"),
            ("Select the sentence with correctly separated consecutive actions:",
             ["A) Maria logged into the system, verified the invoice, printed the label and packed the parcel.", "B) Maria logged into the system verified the invoice printed the label and packed the parcel.", "C) Maria logged into the system, verified the invoice printed the label, and packed the parcel."],
             "A"),
            ("Where should commas be placed? <em>'Please collect the mop bucket sanitiser spray and microfiber cloths.'</em>",
             ["A) after mop, bucket, and spray", "B) after mop, after spray", "C) after bucket, after spray"],
             "A")
        ],
        "exercise_b": [
            ("Add missing list commas", "The tool chest holds pliers screwdrivers wire strippers and a tape measure", "The tool chest holds pliers, screwdrivers, wire strippers and a tape measure."),
            ("Remove commas from a two-item phrase", "Every morning we inspect the forklift, and clean the loading bay", "Every morning we inspect the forklift and clean the loading bay."),
            ("Punctuate three actions in a row", "He unlocked the door turned on the lights and checked the safe", "He unlocked the door, turned on the lights and checked the safe.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Kitchen Requisition Sheet",
        "proofreading_scenario": "Check this catering purchase memo drafted by a kitchen commis chef. There are exactly 4 comma listing errors (missing commas or incorrect placements).",
        "proofreading_text": "Chef, for tomorrow's banquet we must order fresh carrots potatoes onions and parsnips from the local greengrocer. In addition, the dry store requires basmati rice olive oil, and plain flour. When the delivery arrives, please inspect the crates verify the quantities, and sign the delivery docket. The prep team will peel the vegetables, and chop the herbs before noon.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing commas between vegetables in list ('carrots potatoes onions' -> 'carrots, potatoes, onions')",
            "Unnecessary comma before 'and' in three-item list ('olive oil, and plain' -> 'olive oil and plain')",
            "Missing comma between first two actions ('inspect the crates verify' -> 'inspect the crates, verify')",
            "Unnecessary comma between two joined actions ('vegetables, and chop' -> 'vegetables and chop')"
        ],
        "writing_prompt": "Write a sentence listing four pieces of safety equipment or tools you need to carry out a practical task in your trade or workplace. Use commas accurately."
    },

    # -------------------------------------------------------------------------
    # UNIT 7
    # -------------------------------------------------------------------------
    {
        "unit": 7,
        "title": "Commas after Introductory Phrases & Time Words",
        "format": "Emergency Evacuation & Protocol Notice",
        "anchor_title": "Fire Evacuation & Security Operating Procedures",
        "anchor_text": "Standard Operating Procedure (SOP) manuals give sequential, time-critical directions. Inserting a comma after introductory time markers or conditional preambles gives the reader time to process conditions before taking action.",
        "rule_formula_title": "Introductory Fronting: Time, Place & Manner Phrases",
        "rule_formula_html": """When an introductory phrase or time word opens a sentence, set it off with a comma:
<div class="formula-strip">
  <span class="fpill fpill-punct">[Introductory Time / Transition Word]</span> +
  <span class="fpill fpill-punct">,</span> +
  <span class="fpill fpill-subj">[Subject]</span> +
  <span class="fpill fpill-verb">[Main Action / Instruction]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Time Words &amp; Sequencing:</strong> <em>First, Next, Finally, Yesterday, At 08:30, Last Tuesday</em> (e.g. <em>"Last Monday, the fire marshals conducted an unannounced drill."</em>).</li>
  <li><strong>Introductory Prepositional Phrases:</strong> <em>In the event of a fire, Under health and safety regulations, Before operating the machinery</em> (e.g. <em>"In the event of an alarm, leave your belongings."</em>).</li>
  <li><strong>Transition Linkers:</strong> <em>However, Therefore, In addition, For example, Furthermore</em> (e.g. <em>"However, the second stairwell remained blocked."</em>).</li>
</ul>""",
        "worked_bad": "Yesterday morning our safety representative checked all twenty fire doors.",
        "worked_good": "Yesterday morning, our safety representative checked all twenty fire doors.",
        "worked_why": "Placed a comma after the introductory time phrase ('Yesterday morning') to create a clear boundary before the main clause.",
        "golden_rule": "THE SIGNPOST RULE: Think of introductory words as road signs. When you put a signpost at the front of your sentence (First, However, Last week), plant a comma right after it before continuing.",
        "exercise_a": [
            ("Which sentence places a comma correctly after an introductory time phrase?",
             ["A) In September the new apprentices begin their rotations.", "B) In September, the new apprentices begin their rotations.", "C) In, September the new apprentices begin their rotations."],
             "B"),
            ("Select the sentence with correct punctuation after a workplace transition word:",
             ["A) However the fire exit was blocked by wooden pallets.", "B) However, the fire exit was blocked by wooden pallets.", "C) However; the fire exit was blocked by wooden pallets."],
             "B"),
            ("Identify the sentence requiring a comma after its introductory prepositional phrase:",
             ["A) Before switching on the generator you must inspect the fuel level.", "B) Before switching on the generator, you must inspect the fuel level.", "C) Before, switching on the generator you must inspect the fuel level."],
             "B"),
            ("Which instruction has zero comma errors?",
             ["A) Finally, assemble in the staff car park and await roll call.", "B) Finally assemble in the staff car park and await roll call.", "C) Finally assemble, in the staff car park and await roll call."],
             "A")
        ],
        "exercise_b": [
            ("Insert a comma after the time phrase", "Last Friday our team completed the quarterly stocktake", "Last Friday, our team completed the quarterly stocktake."),
            ("Punctuate the transition linker", "In addition staff must wear protective eyewear in the machining bay", "In addition, staff must wear protective eyewear in the machining bay."),
            ("Punctuate the introductory condition", "In the event of a power cut do not use the passenger lifts", "In the event of a power cut, do not use the passenger lifts.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Site Evacuation Protocol",
        "proofreading_scenario": "Proofread this standard safety instruction card posted beside factory exit doors. Find exactly 4 missing commas after introductory phrases.",
        "proofreading_text": "In the event of a continuous alarm staff must cease operations immediately. Without collecting personal coats or bags walk briskly towards the marked fire escape doors. Under no circumstances should personnel re-enter the facility until permitted by the chief warden. Outside the building report immediately to your designated team supervisor at Assembly Point C.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing comma after introductory conditional phrase ('In the event of a continuous alarm' -> '...alarm, staff')",
            "Missing comma after introductory prepositional phrase ('Without collecting personal coats or bags' -> '...bags, walk')",
            "Missing comma after introductory negative phrase ('Under no circumstances' -> '...circumstances, should')",
            "Missing comma after introductory spatial phrase ('Outside the building' -> '...building, report')"
        ],
        "writing_prompt": "Write two safety instructions for your workplace or training centre. Start the first sentence with 'First,' and the second sentence with 'In case of an emergency,' ensuring commas follow both introductory phrases."
    },

    # -------------------------------------------------------------------------
    # UNIT 8
    # -------------------------------------------------------------------------
    {
        "unit": 8,
        "title": "Apostrophes for Contractions (Don't, Can't, Wouldn't)",
        "format": "Internal Team WhatsApp & SMS Bulletin",
        "anchor_title": "Staff Shift Cover & Immediate Operational Messaging",
        "anchor_text": "Informal workplace communication relies on short forms and contractions. When employees misplace the apostrophe or omit it entirely (writing 'dont', 'cant', or 'would'nt'), messages look careless and can confuse critical work instructions.",
        "rule_formula_title": "Contraction Mechanics: The Apostrophe Replaces Missing Letters",
        "rule_formula_html": """An apostrophe of contraction marks exactly where letters have been omitted when two words merge:
<div class="formula-strip">
  <span class="fpill fpill-subj">do not</span> &rarr;
  <span class="fpill fpill-verb">don't</span> (omits 'o') &bull;
  <span class="fpill fpill-subj">cannot</span> &rarr;
  <span class="fpill fpill-verb">can't</span> (omits 'no') &bull;
  <span class="fpill fpill-subj">would not</span> &rarr;
  <span class="fpill fpill-verb">wouldn't</span> (omits 'o')
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Exact Letter Replacement:</strong> The apostrophe sits inside the word precisely where the missing letter used to be (e.g. <em>does not &rarr; doesn't</em>; NOT <em>does'nt</em>).</li>
  <li><strong>Top Contractions:</strong> <em>isn't, aren't, hasn't, haven't, didn't, won't, it's (= it is)</em>.</li>
  <li><strong>Exam Awareness:</strong> In formal letters and incident reports, examiners prefer full uncontracted forms (<em>do not, will not</em>), but in informal emails and chat logs, contractions must be formed flawlessly.</li>
</ul>""",
        "worked_bad": "We could'nt open the safe because the supervisor has'nt arrived and they dont have the key.",
        "worked_good": "We couldn't open the safe because the supervisor hasn't arrived and they don't have the key.",
        "worked_why": "Corrected misplaced apostrophes in 'couldn't' and 'hasn't' (between 'n' and 't'), and added the missing apostrophe to 'don't'.",
        "golden_rule": "THE 'NOT' RULE: In negative contractions (don't, couldn't, haven't), the apostrophe ALWAYS goes between the 'n' and the 't' because it replaces the letter 'o' in 'not'. Never write n't as 'nt or 'nt.",
        "exercise_a": [
            ("Which contraction is spelled with the apostrophe in the correct position?",
             ["A) did'nt", "B) didn't", "C) didnt"],
             "B"),
            ("Choose the correct contracted form of <em>'we will'</em>:",
             ["A) we'll", "B) well", "C) w'ell"],
             "A"),
            ("Which sentence uses contraction apostrophes accurately throughout?",
             ["A) You shouldn't enter if you haven't scanned your badge.", "B) You should'nt enter if you have'nt scanned your badge.", "C) You shouldnt enter if you havent scanned your badge."],
             "A"),
            ("Identify the error in this sentence: <em>'The technician says it's broken, but he cant fix it today.'</em>",
             ["A) 'it's' should be 'its'", "B) 'cant' is missing an apostrophe ('can't')", "C) 'broken' is misspelled"],
             "B")
        ],
        "exercise_b": [
            ("Contract 'they have not'", "they have not received the delivery", "they haven't received the delivery"),
            ("Correct the misplaced apostrophe", "the driver was'nt able to reverse into bay 3", "the driver wasn't able to reverse into bay 3"),
            ("Contract 'it is'", "it is essential that all doors remain locked", "It's essential that all doors remain locked")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Shift Handover Text Bulletin",
        "proofreading_scenario": "Read this urgent staff text bulletin sent to evening shift staff at a retail supermarket. Identify exactly 4 contraction errors.",
        "proofreading_text": "Hi team, please note that the cold room chiller isnt working properly tonight. The engineer could'nt attend before 18:00, so weve moved dairy crates into Chiller 2. You should'nt stack boxes above shoulder height, and please ensure the door is firmly latched after each visit.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing apostrophe in 'isnt' ('isnt' -> 'isn't')",
            "Misplaced apostrophe in 'could'nt' ('could'nt' -> 'couldn't')",
            "Missing apostrophe in 'weve' ('weve' -> 'we've')",
            "Misplaced apostrophe in 'should'nt' ('should'nt' -> 'shouldn't')"
        ],
        "writing_prompt": "Write two informal sentences to a colleague explaining why you cannot attend tomorrow's briefing and when you will arrive instead. Include at least two correctly formed contractions (e.g. can't, I'll, won't)."
    },

    # -------------------------------------------------------------------------
    # UNIT 9
    # -------------------------------------------------------------------------
    {
        "unit": 9,
        "title": "Apostrophes for Singular Possession (The customer's order)",
        "format": "Customer Returns & Property Log",
        "anchor_title": "Customer Returns Desk & Lost Property Ledger",
        "anchor_text": "Retail and hospitality staff handle lost property, customer repairs, and personal belongings. Using possessive apostrophes correctly ensures legal ownership is clear and prevents disputes over property rights.",
        "rule_formula_title": "Singular Ownership Architecture: Singular Noun + 's",
        "rule_formula_html": """To show that ONE person, animal, or entity owns something, add an apostrophe followed by 's':
<div class="formula-strip">
  <span class="fpill fpill-subj">[Singular Owner: Noun]</span> +
  <span class="fpill fpill-punct">'s</span> +
  <span class="fpill fpill-clause">[Item Possessed]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Singular Ownership:</strong> <em>the customer's order</em> (one customer), <em>the doctor's signature</em> (one doctor), <em>the company's policy</em> (one company).</li>
  <li><strong>Names Ending in -s:</strong> For singular names ending in -s, add 's in modern functional English (e.g. <em>James's locker, Charles's coat</em>).</li>
  <li><strong>No Ownership = No Apostrophe:</strong> Simple plurals do not take an apostrophe (e.g. <em>"Five customers waited"</em> NOT <em>"Five customer's waited"</em>).</li>
  <li><strong>Its vs It's:</strong> <em>Its</em> (no apostrophe) shows possession (e.g. <em>"The cat licked its paw; the printer lost its power"</em>). <em>It's</em> ALWAYS means <em>it is</em>.</li>
</ul>""",
        "worked_bad": "We found the drivers phone in the managers office near the staff lockers.",
        "worked_good": "We found the driver's phone in the manager's office near the staff lockers.",
        "worked_why": "Added apostrophes to show singular ownership: one driver owned the phone ('driver's'), and one manager occupied the office ('manager's').",
        "golden_rule": "THE 'BELONGS TO' CHECK: Ask yourself: 'Who does it belong to?' If it belongs to one person (the client), write that exact word first, then add 's &rarr; the client's account.",
        "exercise_a": [
            ("Which sentence correctly indicates that an umbrella belongs to one customer?",
             ["A) The customers umbrella was left at reception.", "B) The customer's umbrella was left at reception.", "C) The customers' umbrella was left at reception."],
             "B"),
            ("Choose the option demonstrating correct singular possession for an employee's tool:",
             ["A) The electrician's multimeter passed calibration.", "B) The electricians multimeter passed calibration.", "C) The electrican's multimeter passed calibration."],
             "A"),
            ("Which sentence distinguishes correctly between a plural noun and a singular possessive noun?",
             ["A) Three supervisors inspected the worker's badge.", "B) Three supervisor's inspected the worker's badge.", "C) Three supervisors inspected the workers badge."],
             "A"),
            ("Select the sentence that uses possessive 'its' (no apostrophe) correctly:",
             ["A) The printer has stopped because it's paper tray is empty.", "B) The printer has stopped because its paper tray is empty.", "C) The printer has stopped because its' paper tray is empty."],
             "B")
        ],
        "exercise_b": [
            ("Make singular possessive: the locker of the nurse", "the locker belonging to the nurse", "the nurse's locker"),
            ("Insert the singular possessive apostrophe", "We received the client signature on yesterday contract", "We received the client's signature on yesterday's contract."),
            ("Choose between its and it's", "The delivery van has lost [its / it's] front registration plate", "The delivery van has lost its front registration plate.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Lost Property Log Sheet",
        "proofreading_scenario": "Examine this lost property log recorded by a gym duty receptionist. There are exactly 4 singular possessive apostrophe errors (missing or misapplied apostrophes).",
        "proofreading_text": "Yesterday afternoon, a member found a visitors wallet near the weights bench. The wallet contained one drivers licence, fifty pounds in cash, and a train ticket. In addition, Sarah found the gym cleaner mop bucket left in the main corridor. The security camera showed that a guest child left a red rucksack in the cafe area.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing singular possessive apostrophe on 'visitors' ('visitors wallet' -> 'visitor's wallet')",
            "Missing singular possessive apostrophe on 'drivers' ('drivers licence' -> 'driver's licence')",
            "Missing singular possessive apostrophe on 'cleaner' ('cleaner mop' -> 'cleaner's mop')",
            "Missing singular possessive apostrophe on 'guest' ('guest child' -> 'guest's child')"
        ],
        "writing_prompt": "Write two sentences recording the return of a piece of lost workplace equipment. Use the singular possessive form for both a colleague's tool and a supervisor's desk."
    },

    # -------------------------------------------------------------------------
    # UNIT 10
    # -------------------------------------------------------------------------
    {
        "unit": 10,
        "title": "Plural Nouns — Regular (-s, -es) and Irregular (children, men, feet)",
        "format": "Health & Safety Facilities Audit",
        "anchor_title": "Workplace Facilities & Welfare Provision Audit",
        "anchor_text": "Facility managers must maintain accurate counts of fixtures, amenities, and personnel for health and safety compliance. Confusing regular plurals (-s, -es) or misforming irregular plurals damages the credibility of official inspection reports.",
        "rule_formula_title": "Pluralisation Rules: Regular Suffixes vs Irregular Roots",
        "rule_formula_html": """Plural nouns represent more than one person, place, or thing:
<div class="formula-strip">
  <span class="fpill fpill-subj">Regular:</span> Noun + -s &bull;
  <span class="fpill fpill-subj">Hissing Sounds (-ch, -sh, -s, -x, -z):</span> Noun + -es &bull;
  <span class="fpill fpill-verb">Irregular:</span> Root Vowel Shift
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Standard Rule (-s):</strong> <em>desk &rarr; desks, tool &rarr; tools, computer &rarr; computers</em>.</li>
  <li><strong>The -es Rule:</strong> When a singular noun ends in <em>-s, -ss, -sh, -ch</em>, or <em>-x</em>, add <strong>-es</strong> to create a pronounceable syllable (e.g. <em>box &rarr; boxes, branch &rarr; branches, bus &rarr; buses</em>).</li>
  <li><strong>Top Irregular Plurals:</strong> Never add -s to nouns that change their root vowels or forms:
    <em>man &rarr; men, woman &rarr; women, child &rarr; children, foot &rarr; feet, tooth &rarr; teeth, person &rarr; people</em>.</li>
  <li><strong>No Apostrophe for Plurals:</strong> Never use an apostrophe to form a simple plural (e.g. <em>"apple's for sale"</em> is WRONG; write <em>"apples"</em>).</li>
</ul>""",
        "worked_bad": "All fire boxs must be checked by the two security mans and their childs.",
        "worked_good": "All fire boxes must be checked by the two security men and their children.",
        "worked_why": "Added -es to 'box' ('boxes') and replaced incorrect pluralisations 'mans' and 'childs' with proper irregular forms 'men' and 'children'.",
        "golden_rule": "THE HISS TEST: If a word ends with a hiss or buzz sound (s, sh, ch, x), add -ES so you can pronounce the plural. If it's a human irregular (men, women, children, people), never add an -s!",
        "exercise_a": [
            ("What is the correct plural form of the word <em>'bench'</em>?",
             ["A) benchs", "B) benches", "C) bench's"],
             "B"),
            ("Select the correct plural form of <em>'woman'</em>:",
             ["A) womans", "B) women", "C) womens"],
             "B"),
            ("Which sentence contains zero pluralisation errors?",
             ["A) The warehouse has twelve fire extinguishers and five emergency exit doors.", "B) The warehouse has twelve fire extinguisheres and five emergency exit doors.", "C) The warehouse has twelve fire extinguisher's and five exit doors."],
             "A"),
            ("Choose the correct irregular plural to complete: <em>'Both [______] must wear safety boots to protect their [______].'</em>",
             ["A) men / foots", "B) mans / feet", "C) men / feet"],
             "C")
        ],
        "exercise_b": [
            ("Form the plural of 'tax' and 'glass'", "The company pays several [tax] and ordered fifty [glass]", "taxes / glasses"),
            ("Correct the irregular plural error", "Several persons and their childs attended the family open day", "Several people and their children attended the family open day."),
            ("Remove greengrocer's apostrophes", "Please stack the pallet's and wash the tray's", "Please stack the pallets and wash the trays.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Factory Welfare Report",
        "proofreading_scenario": "Review this excerpt from an annual factory facilities inspection. Identify exactly 4 pluralisation errors (regular -es, irregular plurals, or greengrocer apostrophes).",
        "proofreading_text": "The factory refurbishment is progressing well across all three floor's. Contractors installed twelve new wash basin's in the welfare facilities. Male and female changing room facilities have separate shower stalles for all workers. Both security mans confirmed that all emergency supply boxs are fully stocked.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Apostrophe on simple plural ('floor's' -> 'floors')",
            "Apostrophe on simple plural ('basin's' -> 'basins')",
            "Misspelled regular plural ('stalles' -> 'stalls')",
            "Misformed irregular and regular plurals ('mans... boxs' -> 'men... boxes')"
        ],
        "writing_prompt": "Write two sentences describing equipment and people in a workshop or kitchen. Use at least one regular plural ending in -es (e.g. boxes, dishes, brushes) and one irregular plural noun (e.g. people, men, women, children)."
    },

    # -------------------------------------------------------------------------
    # UNIT 11
    # -------------------------------------------------------------------------
    {
        "unit": 11,
        "title": "Plural Nouns ending in -y to -ies vs vowel+y",
        "format": "Company Policy & Operational Guidelines",
        "anchor_title": "Corporate Compliance & Human Resources Directives",
        "anchor_text": "HR officers maintain staff policy handbooks, holiday schedules, and workplace directories. Confusing the spelling rules for nouns ending in 'y' produces unprofessional documentation that undermines institutional standards.",
        "rule_formula_title": "The Consonant-Y vs Vowel-Y Orthographic Rule",
        "rule_formula_html": """Look at the letter immediately before the final 'y' to determine the plural spelling:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Consonant + Y]</span> &rarr; Drop 'y', add
  <span class="fpill fpill-punct">-IES</span> (e.g. factory &rarr; factor<strong>ies</strong>)
</div>
<div class="formula-strip" style="margin-top:3px;">
  <span class="fpill fpill-subj">[Vowel + Y]</span> &rarr; Keep 'y', add
  <span class="fpill fpill-verb">-S</span> (e.g. day &rarr; day<strong>s</strong>)
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Consonant + Y:</strong> <em>company &rarr; companies, policy &rarr; policies, delivery &rarr; deliveries, category &rarr; categories, facility &rarr; facilities</em>.</li>
  <li><strong>Vowel + Y (a, e, i, o, u + y):</strong> <em>delay &rarr; delays, journey &rarr; journeys, key &rarr; keys, holiday &rarr; holidays, display &rarr; displays</em>.</li>
  <li><strong>Common Pitfall:</strong> Never write <em>delaiyes</em> or <em>companys</em>. Check the preceding letter every single time!</li>
</ul>""",
        "worked_bad": "All local deliverys were postponed because both companys updated their internal policys.",
        "worked_good": "All local deliveries were postponed because both companies updated their internal policies.",
        "worked_why": "Since 'delivery', 'company', and 'policy' each end in a consonant + y (r-y, n-y, c-y), the 'y' changes to '-ies'.",
        "golden_rule": "THE VOWEL GUARD: If a vowel (A, E, I, O, U) stands right in front of the 'y', it guards it: just add -S (keys, days, holidays). If a consonant is there, change 'y' to -IES (parties, supplies, policies).",
        "exercise_a": [
            ("What is the correct plural form of <em>'company'</em>?",
             ["A) companys", "B) companies", "C) company's"],
             "B"),
            ("Choose the correct plural form of <em>'holiday'</em>:",
             ["A) holidays", "B) holidies", "C) holiday's"],
             "A"),
            ("Which sentence spells both y-ending plural nouns correctly?",
             ["A) Transport delays affected emergency deliveries across the region.", "B) Transport delaies affected emergency deliverys across the region.", "C) Transport delays affected emergency deliverys across the region."],
             "A"),
            ("Select the sentence with zero spelling errors in plural nouns:",
             ["A) The warehouse holds extra supplys and spare keys for all security vans.", "B) The warehouse holds extra supplies and spare keys for all security vans.", "C) The warehouse holds extra supplies and spare keyes for all security vans."],
             "B")
        ],
        "exercise_b": [
            ("Change to plural: factory / facility", "The town contains three large [factory] and two training [facility]", "factories / facilities"),
            ("Change to plural: journey / tray", "The drivers recorded all daily [journey] and stacked the wooden [tray]", "journeys / trays"),
            ("Correct the spelling error", "Staff must review all safeguarding policys before taking their annual holidaies", "Staff must review all safeguarding policies before taking their annual holidays.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: HR Policy Update Memo",
        "proofreading_scenario": "Read this excerpt from an internal HR memo sent to all branch supervisors. Identify exactly 4 plural spelling errors involving words ending in -y.",
        "proofreading_text": "Apex Logistics operates twelve regional facilitays across England and Wales. Due to recent bank holidaies, head office noted minor delaies in order processing. All department managers must update their shift categorise and submit holiday requests before Friday noon.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Misspelled consonant+y plural ('facilitays' -> 'facilities')",
            "Misspelled vowel+y plural ('holidaies' -> 'holidays')",
            "Misspelled vowel+y plural ('delaies' -> 'delays')",
            "Misspelled consonant+y plural ('categorise' -> 'categories')"
        ],
        "writing_prompt": "Write two sentences about staff training and company guidelines. Use the plural form of 'company' (companies) and the plural form of 'key' (keys) accurately."
    },

    # -------------------------------------------------------------------------
    # UNIT 12
    # -------------------------------------------------------------------------
    {
        "unit": 12,
        "title": "Apostrophes with Regular Plural Nouns (The managers' meeting)",
        "format": "Staff Room Notice & Meeting Agenda",
        "anchor_title": "Executive Boardroom & Staff Noticeboard",
        "anchor_text": "Administrative coordinators publish meeting notices, allocate designated staff parking, and manage group amenities. Putting the apostrophe before the 's' for plural groups implies only one person is involved, causing confusion in official rosters.",
        "rule_formula_title": "Plural Possession Architecture: Regular Plurals Ending in -s Take Only an Apostrophe",
        "rule_formula_html": """When showing that a PLURAL group ending in -s owns something, place the apostrophe AFTER the -s:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Plural Owners Ending in -s]</span> +
  <span class="fpill fpill-punct">'</span> (apostrophe only) +
  <span class="fpill fpill-clause">[Item / Event Owned]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Regular Plural Ownership:</strong> <em>the managers' meeting</em> (meeting of multiple managers), <em>the drivers' rest room</em> (room for all drivers), <em>the teachers' staff room</em>.</li>
  <li><strong>Singular vs Plural Contrast:</strong>
    <br>&bull; <em>The worker's lunch</em> = belonging to ONE worker.
    <br>&bull; <em>The workers' lockers</em> = belonging to MANY workers.</li>
  <li><strong>Irregular Plurals (men, women, children, people):</strong> Because they do NOT end in -s, treat them like singular nouns: add <strong>'s</strong> (e.g. <em>the children's ward, the women's changing room, the people's choice</em>).</li>
</ul>""",
        "worked_bad": "The supervisor inspected the driver's rest area and the apprentice's toolboxes.",
        "worked_good": "The supervisor inspected the drivers' rest area and the apprentices' toolboxes.",
        "worked_why": "Moved the apostrophe to after the 's' ('drivers'', 'apprentices'') because multiple drivers share the rest area and multiple apprentices own the toolboxes.",
        "golden_rule": "THE 'MORE THAN ONE' RULE: Write the plural word first (drivers, managers, nurses). If it already ends in 's', just crown it with an apostrophe at the very end: drivers' room, managers' meeting.",
        "exercise_a": [
            ("Which phrase correctly describes a briefing for multiple supervisors?",
             ["A) the supervisor's briefing", "B) the supervisors' briefing", "C) the supervisors briefing's"],
             "B"),
            ("Choose the correct punctuation for a cloakroom used by many nurses:",
             ["A) the nurses' cloakroom", "B) the nurse's cloakroom", "C) the nurses cloakroom's"],
             "A"),
            ("Select the sentence with correct irregular plural possession:",
             ["A) The childrens' play area has reopened.", "B) The children's play area has reopened.", "C) The childrens play's area has reopened."],
             "B"),
            ("Which sentence accurately distinguishes singular from regular plural possession?",
             ["A) The manager's car was parked outside, while the workers' bicycles were locked in the shed.", "B) The managers' car was parked outside, while the worker's bicycles were locked in the shed.", "C) The managers car was parked outside, while the workers's bicycles were locked in the shed."],
             "A")
        ],
        "exercise_b": [
            ("Make plural possessive: the changing room for teachers", "the changing room of the teachers", "the teachers' changing room"),
            ("Make plural possessive: the union of workers", "the union belonging to all workers", "the workers' union"),
            ("Correct irregular plural possession", "We painted the womens staff room yesterday", "We painted the women's staff room yesterday.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Depot Welfare Guidelines",
        "proofreading_scenario": "Proofread this notice posted in the reception of a regional delivery depot. Find exactly 4 apostrophe errors involving regular and irregular plural possession.",
        "proofreading_text": "Welcome to our regional depot. All visitor badges must be collected from the security desk before 08:30. The courier's vehicles must be parked in Bay 4 to keep the main gate clear. Staff can access the worker's rest room and the drivers's kitchen on Level 1. Please note that the childrens' charity collection box is situated in the main foyer.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Singular apostrophe used for plural couriers ('courier's vehicles' -> 'couriers' vehicles')",
            "Singular apostrophe used for plural workers ('worker's rest room' -> 'workers' rest room')",
            "Double-s apostrophe on regular plural ('drivers's' -> 'drivers'')",
            "Misplaced apostrophe on irregular plural ('childrens'' -> 'children's')"
        ],
        "writing_prompt": "Write two sentences describing communal workplace facilities. Use one regular plural possessive noun (e.g. the technicians' workshop, the managers' rota) and one irregular plural possessive noun (e.g. the men's locker room, the women's team)."
    },

    # -------------------------------------------------------------------------
    # UNIT 13
    # -------------------------------------------------------------------------
    {
        "unit": 13,
        "title": "Present Simple Tense for Daily Routines & Shift Handover",
        "format": "Daily Operating Checklist & Duty Handover",
        "anchor_title": "Daily Operating Routines & Duty Rota",
        "anchor_text": "Care home workers and facility coordinators document daily routines and handover logs. The present simple tense describes habitual actions, timetables, and standing facts. Omitting third-person '-s' creates ungrammatical, non-standard English.",
        "rule_formula_title": "Present Simple Architecture: Habitual Routine & Third-Person Suffix",
        "rule_formula_html": """Use the present simple for routines, schedules, and permanent facts:
<div class="formula-strip">
  <span class="fpill fpill-subj">[I / You / We / They]</span> +
  <span class="fpill fpill-verb">[Base Verb]</span> (e.g. inspect, clean) &bull;
  <span class="fpill fpill-subj">[He / She / It / Singular Noun]</span> +
  <span class="fpill fpill-verb">[Base Verb + -s / -es]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>First Person / Plural:</strong> <em>"We record temperatures every hour; they sanitize the surfaces."</em></li>
  <li><strong>Third Person Singular:</strong> Always add <strong>-s</strong> or <strong>-es</strong> for singular subjects (e.g. <em>"The nurse administer<strong>s</strong> medication; the supervisor inspect<strong>s</strong> the fire doors."</em>).</li>
  <li><strong>Verbs ending in -ch, -sh, -s, -o:</strong> Add <strong>-es</strong> (e.g. <em>he watches, she washes, the motor passes, he does, she goes</em>).</li>
</ul>""",
        "worked_bad": "Every morning, the care assistant empty the laundry bin and check the call alarms.",
        "worked_good": "Every morning, the care assistant empties the laundry bin and checks the call alarms.",
        "worked_why": "Added third-person singular endings ('empties', 'checks') to match the singular subject 'the care assistant'.",
        "golden_rule": "THE 'HE/SHE/IT' S TEST: Whenever your subject is one single person or object (the nurse, the manager, the machine), your verb MUST wear an 'S' at the end: she checks, it runs, he cleans.",
        "exercise_a": [
            ("Which sentence uses the correct present simple verb for a daily routine?",
             ["A) The caretaker unlocks the main gates at 07:00 every day.", "B) The caretaker unlock the main gates at 07:00 every day.", "C) The caretaker unlocking the main gates at 07:00 every day."],
             "A"),
            ("Choose the correct verb form for a plural subject: <em>'Both apprentices [______] the warehouse inventory every afternoon.'</em>",
             ["A) updates", "B) update", "C) updated"],
             "B"),
            ("Which sentence demonstrates correct spelling of third-person -es verbs?",
             ["A) Dr Evans watchs patient monitors and fixs the sensor.", "B) Dr Evans watches patient monitors and fixes the sensor.", "C) Dr Evans watch patient monitors and fix the sensor."],
             "B"),
            ("Select the sentence with perfect present simple agreement:",
             ["A) Our delivery driver always check his tire pressure before leaving.", "B) Our delivery driver always checks his tyre pressure before leaving.", "C) Our delivery driver always checking his tyre pressure."],
             "B")
        ],
        "exercise_b": [
            ("Apply third-person singular -s", "The supervisor [inspect] the safety log every Friday", "The supervisor inspects the safety log every Friday."),
            ("Apply third-person singular -es", "The technician [wash] his hands and [go] to the staff room", "The technician washes his hands and goes to the staff room."),
            ("Correct the agreement error", "Every evening, the cleaner empty all the office recycling bins", "Every evening, the cleaner empties all the office recycling bins.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Care Home Daily Routine",
        "proofreading_scenario": "Examine this excerpt from a residential care home shift handover log. Identify exactly 4 present simple verb errors.",
        "proofreading_text": "The senior care worker arrive at 07:30 to begin the breakfast handover. She review all medication records and dispense prescription tablets to residents. Meanwhile, the night assistant restock the linen cupboard before leaving the premises. Both team members signs the attendance register at the end of each shift.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing -s on singular verb ('worker arrive' -> 'worker arrives')",
            "Missing -s on singular verbs ('review... dispense' -> 'reviews... dispenses')",
            "Missing -s on singular verb ('assistant restock' -> 'assistant restocks')",
            "Incorrect -s on plural verb ('members signs' -> 'members sign')"
        ],
        "writing_prompt": "Write two sentences describing your regular morning workplace or college routine. In the first sentence, describe an action you do ('I...'); in the second, describe an action your manager or tutor does ('He/She...')."
    },

    # -------------------------------------------------------------------------
    # UNIT 14
    # -------------------------------------------------------------------------
    {
        "unit": 14,
        "title": "Present Continuous for Current Tasks ('is working')",
        "format": "Real-Time IT Support Ticket & Task Status",
        "anchor_title": "Live IT Helpdesk & Live Incident Dispatch",
        "anchor_text": "Technical support teams log live actions to show what is happening right now during an outage. Using the present continuous tense precisely distinguishes actions currently underway from permanent everyday routines.",
        "rule_formula_title": "Present Continuous Architecture: Auxiliary (be) + Present Participle (-ing)",
        "rule_formula_html": """Form the present continuous using the auxiliary verb 'to be' plus the base verb ending in '-ing':
<div class="formula-strip">
  <span class="fpill fpill-subj">[Subject]</span> +
  <span class="fpill fpill-verb">[am / is / are]</span> +
  <span class="fpill fpill-conn">[Base Verb + -ing]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>I &rarr; am:</strong> <em>"I am updating the network security credentials now."</em></li>
  <li><strong>He / She / It / Singular Noun &rarr; is:</strong> <em>"The engineer is replacing the router; software is downloading."</em></li>
  <li><strong>We / You / They / Plural Noun &rarr; are:</strong> <em>"Technicians are testing the fiber-optic cable connection."</em></li>
  <li><strong>Spelling Rules for -ing:</strong>
    <br>&bull; Drop silent 'e': <em>configure &rarr; configuring, write &rarr; writing</em>.
    <br>&bull; Double consonant after single short vowel: <em>run &rarr; running, stop &rarr; stopping</em>.</li>
</ul>""",
        "worked_bad": "Currently, the IT technician updating the server and two engineers is running diagnostic tests.",
        "worked_good": "Currently, the IT technician is updating the server and two engineers are running diagnostic tests.",
        "worked_why": "Supplied the missing auxiliary 'is' for the singular technician and corrected 'is' to 'are' for the plural engineers.",
        "golden_rule": "THE TWO-PIECE VERB: The continuous tense needs TWO pieces like a suit: a form of 'to be' (am/is/are) PLUS the -ing verb. Never leave out the helping verb (do not say 'he working').",
        "exercise_a": [
            ("Which sentence forms the present continuous tense correctly?",
             ["A) The electrician currently rewiring the main circuit breaker.", "B) The electrician is currently rewiring the main circuit breaker.", "C) The electrician are currently rewiring the main circuit breaker."],
             "B"),
            ("Choose the correct auxiliary verb: <em>'At this moment, our team [______] reviewing the security logs.'</em>",
             ["A) is", "B) are", "C) am"],
             "B"),
            ("Which sentence spells the -ing verb correctly?",
             ["A) We are runing diagnostic scans across all laptops.", "B) We are running diagnostic scans across all laptops.", "C) We are runeing diagnostic scans across all laptops."],
             "B"),
            ("Identify the sentence showing an action happening right now:",
             ["A) The technician repairs computers every Tuesday.", "B) The technician repaired the computer yesterday.", "C) The technician is repairing the computer right now."],
             "C")
        ],
        "exercise_b": [
            ("Add the missing auxiliary verb", "The network administrator [install] security patches at present", "The network administrator is installing security patches at present."),
            ("Apply spelling rule: double consonant", "The database backup is [stop] due to a connection error", "The database backup is stopping due to a connection error."),
            ("Apply spelling rule: drop silent 'e'", "Our team is [write] a summary incident report for management", "Our team is writing a summary incident report for management.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: IT Helpdesk Live Status Log",
        "proofreading_scenario": "Review this live status report drafted by an IT apprentice during an office server outage. Identify exactly 4 present continuous tense and auxiliary errors.",
        "proofreading_text": "System Status Update at 11:15: Network engineers currently investigating the server fault on Floor 3. Sandra is configureing the backup power supply to prevent data loss. At the same time, two junior technicians is scanning all connected terminals for malware. We are runing full diagnostics and expect full recovery by noon.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing auxiliary 'are' ('engineers currently investigating' -> 'engineers are currently investigating')",
            "Retained silent 'e' in -ing verb ('configureing' -> 'configuring')",
            "Incorrect singular auxiliary for plural subject ('technicians is' -> 'technicians are')",
            "Failed to double consonant in short vowel verb ('runing' -> 'running')"
        ],
        "writing_prompt": "Write two sentences describing live tasks happening right now in your training department or workplace. Use the present continuous tense ('is/are doing') accurately in both sentences."
    },

    # -------------------------------------------------------------------------
    # UNIT 15
    # -------------------------------------------------------------------------
    {
        "unit": 15,
        "title": "Past Simple — Regular Verbs with -ed Spelling Rules",
        "format": "Accident & Injury Workplace Report",
        "anchor_title": "Accident Log & HSE Official Investigation",
        "anchor_text": "Health and Safety Executive (HSE) incident reports require objective, factual statements of past events. Using the past simple correctly documents completed actions and prevents legal disputes regarding who took which safety precaution.",
        "rule_formula_title": "Past Simple Regular Suffixes: -ed Spelling Mechanics",
        "rule_formula_html": """Add -ed to the base form of regular verbs to describe completed past actions:
<div class="formula-strip">
  <span class="fpill fpill-subj">Regular:</span> Verb + -ed &bull;
  <span class="fpill fpill-subj">Ends in -e:</span> Verb + -d &bull;
  <span class="fpill fpill-verb">Consonant-Vowel-Consonant (CVC):</span> Double Final Letter + -ed &bull;
  <span class="fpill fpill-punct">Consonant + y:</span> Change to -ied
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Standard Addition:</strong> <em>inspect &rarr; inspected, check &rarr; checked, report &rarr; reported, clean &rarr; cleaned</em>.</li>
  <li><strong>Ends in Silent -e:</strong> Add only <strong>-d</strong> (e.g. <em>arrive &rarr; arrived, close &rarr; closed, operate &rarr; operated</em>).</li>
  <li><strong>1-Syllable Short Vowel (CVC):</strong> Double final consonant (e.g. <em>slip &rarr; slipped, stop &rarr; stopped, plan &rarr; planned, drop &rarr; dropped</em>).</li>
  <li><strong>Consonant + y:</strong> Change 'y' to 'i' and add -ed (e.g. <em>carry &rarr; carried, tidy &rarr; tidied, rely &rarr; relied</em>).</li>
</ul>""",
        "worked_bad": "Yesterday, the worker sliped on the wet floor, so we stoped the line and carryed him to medical.",
        "worked_good": "Yesterday, the worker slipped on the wet floor, so we stopped the line and carried him to medical.",
        "worked_why": "Doubled final consonants for 'slipped' and 'stopped' (CVC rule), and changed 'y' to 'i' in 'carried'.",
        "golden_rule": "THE 1-1-1 SPELLING RULE: If a regular verb has 1 syllable, 1 short vowel, and 1 consonant at the end (slip, stop, plan), double the consonant before adding -ed: slipped, stopped, planned.",
        "exercise_a": [
            ("What is the correct past simple spelling of <em>'slip'</em>?",
             ["A) sliped", "B) slipped", "C) slipt"],
             "B"),
            ("What is the correct past simple spelling of <em>'carry'</em>?",
             ["A) carryed", "B) carried", "C) carred"],
             "B"),
            ("Which sentence spells all regular past simple verbs correctly?",
             ["A) The manager droped the keys and planed the morning meeting.", "B) The manager dropped the keys and planned the morning meeting.", "C) The manager droped the keys and planned the morning meeting."],
             "B"),
            ("Select the sentence with zero regular past tense errors:",
             ["A) First aiders arrived promptly and cleaned the graze.", "B) First aiders arrived promptly and cleanned the graze.", "C) First aiders arrivved promptly and cleaned the graze."],
             "A")
        ],
        "exercise_b": [
            ("Apply past simple CVC doubling rule", "The forklift driver [stop] immediately and [drop] the pallet", "stopped / dropped"),
            ("Apply past simple consonant + y rule", "The warehouse apprentice [tidy] the shelving and [empty] the bins", "tidied / emptied"),
            ("Apply past simple silent -e rule", "The safety auditor [notice] the hazard and [close] the entrance", "noticed / closed")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: First Aid Incident Log",
        "proofreading_scenario": "Examine this official first aid incident log recorded by a warehouse safety marshal. Identify exactly 4 regular past tense spelling errors.",
        "proofreading_text": "Incident Log: 14 October, 14:15. While walking along Bay 2, trainee stock clerk Liam Davies sliped on water that leaked from an overhead chiller unit. Liam droped a cardboard box and bruised his right knee. The duty supervisor stoped the conveyor and hurryed across to provide an ice pack.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing double consonant in short vowel verb ('sliped' -> 'slipped')",
            "Missing double consonant in short vowel verb ('droped' -> 'dropped')",
            "Missing double consonant in short vowel verb ('stoped' -> 'stopped')",
            "Misspelled consonant+y past verb ('hurryed' -> 'hurried')"
        ],
        "writing_prompt": "Write two sentences describing a completed workplace task or safety check carried out yesterday. Include at least two regular past tense verbs ending in -ed (e.g. checked, cleaned, stopped, tidied)."
    },

    # -------------------------------------------------------------------------
    # UNIT 16
    # -------------------------------------------------------------------------
    {
        "unit": 16,
        "title": "Past Simple — Top 40 Irregular Verbs (went, saw, took, wrote, came)",
        "format": "Security Incident Report & Witness Statement",
        "anchor_title": "Security Log & Formal Witness Statement",
        "anchor_text": "Security guards and duty managers write formal witness statements following thefts, disputes, or equipment damage. Irregular verbs do not add '-ed'. Writing non-standard forms like 'writed' or 'seed' discredits legal evidence.",
        "rule_formula_title": "Irregular Past Morphology: Root Changes (No -ed)",
        "rule_formula_html": """Irregular verbs completely change their form in the past simple:
<div class="formula-strip">
  <span class="fpill fpill-subj">go &rarr; went</span> &bull;
  <span class="fpill fpill-subj">see &rarr; saw</span> &bull;
  <span class="fpill fpill-verb">take &rarr; took</span> &bull;
  <span class="fpill fpill-conn">write &rarr; wrote</span> &bull;
  <span class="fpill fpill-clause">come &rarr; came</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Top Workplace Irregular Past Forms:</strong>
    <br>&bull; <em>give &rarr; gave, tell &rarr; told, find &rarr; found, make &rarr; made, buy &rarr; bought</em>.
    <br>&bull; <em>leave &rarr; left, hear &rarr; heard, speak &rarr; spoke, break &rarr; broke, bring &rarr; brought</em>.
    <br>&bull; <em>meet &rarr; met, understand &rarr; understood, know &rarr; knew, spend &rarr; spent, send &rarr; sent</em>.</li>
  <li><strong>Fatal Non-Standard Pitfalls:</strong> Never use <em>seen</em> for <em>saw</em> without 'have/had' (say: <em>"I saw the intruder"</em> NOT <em>"I seen the intruder"</em>). Never say <em>"He done it"</em> (say: <em>"He did it"</em>).</li>
</ul>""",
        "worked_bad": "Yesterday, I seen the broken lock and writed an incident report before the manager come in.",
        "worked_good": "Yesterday, I saw the broken lock and wrote an incident report before the manager came in.",
        "worked_why": "Replaced non-standard 'seen' with 'saw', 'writed' with 'wrote', and present tense 'come' with past tense 'came'.",
        "golden_rule": "THE 'NO -ED' RULE: Irregular verbs refuse to wear an -ed coat! Learn their past forms by heart: go &rarr; went, see &rarr; saw, take &rarr; took, write &rarr; wrote. Never write 'goed' or 'taked'.",
        "exercise_a": [
            ("Which option is the correct past simple form of the verb <em>'write'</em>?",
             ["A) writed", "B) wrote", "C) written"],
             "B"),
            ("Choose the correct Standard English past form: <em>'The security guard [______] the broken padlock on the gate.'</em>",
             ["A) seen", "B) seed", "C) saw"],
             "C"),
            ("Which sentence contains zero irregular past tense errors?",
             ["A) We took the visitor log and gave it to the officer.", "B) We taked the visitor log and gived it to the officer.", "C) We taken the visitor log and given it to the officer."],
             "A"),
            ("Select the correct past form of <em>'bring'</em> and <em>'leave'</em>:",
             ["A) brought / left", "B) brang / leaved", "C) brought / leaved"],
             "A")
        ],
        "exercise_b": [
            ("Convert present to past simple", "The manager [tell] us about the inspection and [give] instructions", "told / gave"),
            ("Convert present to past simple", "I [see] the intruder and [speak] to security immediately", "saw / spoke"),
            ("Correct the non-standard dialect form", "The engineer done the repairs and writed the certificate", "The engineer did the repairs and wrote the certificate.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Security Guard Statement",
        "proofreading_scenario": "Proofread this official witness statement written by a night security officer following a break-in at a construction depot. Identify exactly 4 irregular verb errors.",
        "proofreading_text": "Witness Statement: At 23:45, I heard a suspicious noise near Gate B. I went to investigate and seen that someone broke the perimeter security latch. The intruders taked three industrial drill batteries and runned towards the railway embankment before police arrived.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Non-standard past verb ('seen' -> 'saw')",
            "Past participle used incorrectly without auxiliary ('broke' is correct; check 'taked' -> 'took')",
            "Invented regular past form ('taked' -> 'took')",
            "Invented regular past form ('runned' -> 'ran')"
        ],
        "writing_prompt": "Write two sentences describing actions you took during a busy shift or study session yesterday. Use at least two irregular past tense verbs (e.g. went, saw, took, wrote, spoke, met)."
    },

    # -------------------------------------------------------------------------
    # UNIT 17
    # -------------------------------------------------------------------------
    {
        "unit": 17,
        "title": "Future Intentions — 'Going to' vs 'Will' in Planning",
        "format": "Project Management Plan & Client Proposal",
        "anchor_title": "Client Project Schedule & Team Resource Plan",
        "anchor_text": "Project coordinators and team leaders map future deadlines, staffing plans, and client commitments. Expressing future plans with grammatical accuracy avoids ambiguity between prior intentions and spontaneous decisions.",
        "rule_formula_title": "Future Form Architecture: Planned Intentions vs Promises / Spontaneous Decisions",
        "rule_formula_html": """Select your future tense construction based on whether the action was pre-planned:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Be + Going to + Verb]</span> &rarr; Prior Decision / Planned Intention &bull;
  <span class="fpill fpill-verb">[Will + Verb]</span> &rarr; Instant Decision / Firm Promise
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>'Going to' for Pre-Planned Intentions:</strong> <em>"The management team is going to review departmental budgets next month."</em> (Decided beforehand).</li>
  <li><strong>'Will' for Spontaneous Decisions &amp; Offers:</strong> <em>"The phone is ringing; I will answer it."</em></li>
  <li><strong>'Will' for Formal Promises &amp; Guarantees:</strong> <em>"We will deliver your furniture by Friday at 17:00."</em></li>
  <li><strong>Grammatical Trap:</strong> Never omit the auxiliary verb with 'going to' (do not say: <em>"We going to inspect"</em>; write: <em>"We are going to inspect"</em>).</li>
</ul>""",
        "worked_bad": "Next week, the contractor going to install new windows and we will definitely completed on time.",
        "worked_good": "Next week, the contractor is going to install new windows, and we will definitely complete the project on time.",
        "worked_why": "Inserted missing auxiliary 'is' before 'going to' and corrected 'completed' to base verb 'complete' after modal 'will'.",
        "golden_rule": "THE THREE-PART INTENTION: 'Going to' always needs its helping partner: Subject + AM/IS/ARE + going to + Base Verb. Never drop the helping verb (am/is/are)!",
        "exercise_a": [
            ("Which sentence expresses a planned future intention with correct grammar?",
             ["A) We going to launch the new company website in March.", "B) We are going to launch the new company website in March.", "C) We will to launch the new company website in March."],
             "B"),
            ("Choose the correct verb following the modal 'will': <em>'Our logistics partner will [______] the shipment on Thursday.'</em>",
             ["A) dispatch", "B) dispatched", "C) dispatching"],
             "A"),
            ("Which response represents a professional spontaneous offer to a client?",
             ["A) I am going to email you that price quote right away.", "B) I will email you that price quote right away.", "C) I will emailing you that quote."],
             "B"),
            ("Select the sentence with zero future tense errors:",
             ["A) The architects are going to visit the building site tomorrow.", "B) The architects is going to visit the building site tomorrow.", "C) The architects going to visit the building site tomorrow."],
             "A")
        ],
        "exercise_b": [
            ("Insert the missing auxiliary for 'going to'", "Next Monday, our company [going to] upgrade its payment terminals", "Next Monday, our company is going to upgrade its payment terminals."),
            ("Use 'will' + base verb for a client promise", "Apex Solutions [guarantee] delivery within forty-eight hours", "Apex Solutions will guarantee delivery within forty-eight hours."),
            ("Correct the modal verb construction", "The supervisor will inspects the work area before signing off", "The supervisor will inspect the work area before signing off.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Project Milestones Email",
        "proofreading_scenario": "Check this update email sent by a junior site coordinator to commercial clients regarding future renovation phases. Identify exactly 4 future tense errors.",
        "proofreading_text": "Dear Clients, We are please to update you on our future renovation schedule. Next Monday, our plumbing team going to install the new water valves on Level 2. The electrical contractors will arrived on Wednesday morning to rewire the lighting. We will ensuring that disruption is kept to a minimum throughout.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Missing -d on passive/participle adjective ('are please' -> 'are pleased')",
            "Missing auxiliary verb before 'going to' ('team going to' -> 'team is going to')",
            "Past tense used after modal 'will' ('will arrived' -> 'will arrive')",
            "Present participle used after modal 'will' ('will ensuring' -> 'will ensure')"
        ],
        "writing_prompt": "Write two sentences outlining plans for your next work shift or study week: one planned action using 'am/is/are going to' and one professional commitment using 'will'."
    },

    # -------------------------------------------------------------------------
    # UNIT 18
    # -------------------------------------------------------------------------
    {
        "unit": 18,
        "title": "Subject-Verb Agreement — Singular vs Plural (is/are, was/were)",
        "format": "Human Resources Disciplinary Record",
        "anchor_title": "Formal Disciplinary & Incident Record",
        "anchor_text": "HR officers draft formal hearing notes and investigation summaries. Subject-verb agreement errors (such as 'they was' or 'the files is') make formal records appear uneducated and undermine legal credibility.",
        "rule_formula_title": "Subject-Verb Concord: Matching Number and Person",
        "rule_formula_html": """A singular subject takes a singular verb; a plural subject takes a plural verb:
<div class="formula-strip">
  <span class="fpill fpill-subj">[Singular Subject]</span> &rarr;
  <span class="fpill fpill-verb">is / was / has / does</span> &bull;
  <span class="fpill fpill-subj">[Plural Subject]</span> &rarr;
  <span class="fpill fpill-verb">are / were / have / do</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Present Tense:</strong> <em>"The manager is satisfied; the employees are ready."</em></li>
  <li><strong>Past Tense:</strong> <em>"The apprentice was punctual; the technicians were delayed."</em></li>
  <li><strong>Intervening Prepositional Phrases:</strong> Words between the subject and verb do not change the subject's number (e.g. <em>"The box [of spare fuses] <strong>is</strong> heavy"</em> &mdash; 'box' is singular!).</li>
  <li><strong>Compound Subjects Joined by 'and':</strong> Take a plural verb (e.g. <em>"David and Emma <strong>were</strong> present at the hearing."</em>).</li>
</ul>""",
        "worked_bad": "Both witnesses was interviewed by the panel, but the supervisor were absent.",
        "worked_good": "Both witnesses were interviewed by the panel, but the supervisor was absent.",
        "worked_why": "Changed 'was' to plural 'were' to match 'both witnesses', and 'were' to singular 'was' to match 'the supervisor'.",
        "golden_rule": "THE BRACKET TRICK: Put mental brackets around any words between the subject and verb (e.g. The crate [of surgical gloves] IS on the shelf). Match your verb directly to the main subject word outside the brackets!",
        "exercise_a": [
            ("Choose the correct verb for subject-verb agreement: <em>'The quality manager [______] reviewing the shift report.'</em>",
             ["A) is", "B) are", "C) were"],
             "A"),
            ("Select the correct past tense verb: <em>'All four delivery drivers [______] trained on the new tail-lift.'</em>",
             ["A) was", "B) were", "C) is"],
             "B"),
            ("Which sentence demonstrates correct subject-verb agreement with an intervening phrase?",
             ["A) The box of surgical instruments were sterilised yesterday.", "B) The box of surgical instruments was sterilised yesterday.", "C) The box of surgical instruments are sterilised yesterday."],
             "B"),
            ("Identify the sentence with zero subject-verb agreement errors:",
             ["A) The reports was filed in the cabinet and the manager was notified.", "B) The reports were filed in the cabinet and the manager was notified.", "C) The reports were filed in the cabinet and the manager were notified."],
             "B")
        ],
        "exercise_b": [
            ("Choose between was and were", "Both security cameras [was / were] disabled during the power surge", "Both security cameras were disabled during the power surge."),
            ("Choose between is and are", "The list of approved suppliers [is / are] pinned to the staff noticeboard", "The list of approved suppliers is pinned to the staff noticeboard."),
            ("Correct the agreement error", "The apprentice and the technician was commended for their quick response", "The apprentice and the technician were commended for their quick response.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: HR Grievance Meeting Summary",
        "proofreading_scenario": "Proofread this formal summary note written by a junior HR clerk following a disciplinary investigation. Identify exactly 4 subject-verb agreement errors.",
        "proofreading_text": "Meeting Record: The shop floor representative and the employee was present at 10:00. The folder of grievance documents were placed on the conference table. Both committee members was satisfied that fair process had been followed. The employee were advised of the right to appeal within five working days.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Singular verb used for compound plural subject ('representative and employee was' -> 'were')",
            "Plural verb used for singular subject with intervening phrase ('folder... were' -> 'folder... was')",
            "Singular verb used for plural subject ('members was' -> 'members were')",
            "Plural verb used for singular subject ('employee were' -> 'employee was')"
        ],
        "writing_prompt": "Write two sentences reporting the outcome of a workplace inspection. Ensure one sentence has a singular subject with 'was' and the other has a plural subject with 'were'."
    },

    # -------------------------------------------------------------------------
    # UNIT 19
    # -------------------------------------------------------------------------
    {
        "unit": 19,
        "title": "Subject-Verb Agreement with There is / There are",
        "format": "Warehouse Stocktake & Discrepancy Notice",
        "anchor_title": "Inventory Audit & Stock Discrepancy Bulletin",
        "anchor_text": "Stock inventory clerks compile discrepancy notices informing management of missing or surplus stock. Using 'there is' for plural items (e.g. 'there is five pallets') sounds uneducated and confuses stock records.",
        "rule_formula_title": "Existential Agreement: The True Subject Follows the Verb",
        "rule_formula_html": """In sentences opening with 'There is' or 'There are', the word 'There' is merely a placeholder; the verb matches the noun that follows:
<div class="formula-strip">
  <span class="fpill fpill-subj">There is / There was</span> +
  <span class="fpill fpill-verb">[Singular Noun / Uncountable Noun]</span> &bull;
  <span class="fpill fpill-subj">There are / There were</span> +
  <span class="fpill fpill-verb">[Plural Noun]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Singular / Uncountable:</strong> <em>"There is a severe leak in Bay 2; there is water on the floor."</em></li>
  <li><strong>Plural:</strong> <em>"There are forty parcels waiting in the holding area; there were three discrepancies."</em></li>
  <li><strong>Spoken English Trap:</strong> In casual speech, people frequently contract 'There's' for plurals (e.g. <em>"There's three boxes"</em>). In Functional Skills Level 1 writing, this is an agreement error. You MUST write: <em>"There are three boxes."</em></li>
</ul>""",
        "worked_bad": "There is fifty damaged cartons in Bay 1 and there was no forklift drivers available.",
        "worked_good": "There are fifty damaged cartons in Bay 1 and there were no forklift drivers available.",
        "worked_why": "Changed 'there is' to 'there are' (matching plural 'fifty cartons') and 'there was' to 'there were' (matching plural 'drivers').",
        "golden_rule": "THE REVERSAL TEST: Flip the sentence around mentally: 'Fifty cartons ARE in Bay 1'. If you need 'are' when flipped, you MUST say 'There are', never 'There is'!",
        "exercise_a": [
            ("Choose the correct present tense form: <em>'[______] several safety hazards identified in the machine shop.'</em>",
             ["A) There is", "B) There are", "C) There's"],
             "B"),
            ("Choose the correct past tense form: <em>'[______] a significant discrepancy in yesterday's stock count.'</em>",
             ["A) There were", "B) There was", "C) There are"],
             "B"),
            ("Which sentence demonstrates correct agreement with 'there are'?",
             ["A) There are twenty new computers installed in the IT suite.", "B) There is twenty new computers installed in the IT suite.", "C) There's twenty new computers installed in the IT suite."],
             "A"),
            ("Select the sentence with zero existential agreement errors:",
             ["A) There was two supervisors on duty when the fire alarm sounded.", "B) There were two supervisors on duty when the fire alarm sounded.", "C) There is two supervisors on duty when the fire alarm sounded."],
             "B")
        ],
        "exercise_b": [
            ("Choose between There is and There are", "[There is / There are] six replacement air filters on Shelf B", "There are six replacement air filters on Shelf B."),
            ("Choose between There was and There were", "[There was / There were] only one fire extinguisher in the corridor", "There was only one fire extinguisher in the corridor."),
            ("Correct the informal spoken contraction", "There's three visitors waiting at the security gate", "There are three visitors waiting at the security gate.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Stocktake Discrepancy Memo",
        "proofreading_scenario": "Check this stock audit report submitted to the logistics manager. Identify exactly 4 agreement errors involving 'there is' and 'there was'.",
        "proofreading_text": "Audit Summary: During the physical count on Monday, there was four discrepancies noted in Aisle 6. There is two damaged pallets stored near the loading bay that require immediate disposal. In addition, there was thirty units of safety goggles missing from the storage cupboard. Fortunately, there are no immediate delay to client shipments.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Singular past verb with plural noun ('there was four discrepancies' -> 'there were')",
            "Singular present verb with plural noun ('there is two damaged pallets' -> 'there are')",
            "Singular past verb with plural noun ('there was thirty units' -> 'there were')",
            "Plural verb with singular noun ('there are no immediate delay' -> 'there is')"
        ],
        "writing_prompt": "Write two sentences describing items currently in your training classroom or workshop. Use 'There is' for a singular item and 'There are' for a plural group of items."
    },

    # -------------------------------------------------------------------------
    # UNIT 20
    # -------------------------------------------------------------------------
    {
        "unit": 20,
        "title": "Pronoun Consistency — Avoiding Switching between You, I, and They",
        "format": "Staff Advice Sheet & Workplace Guidance",
        "anchor_title": "Employee Health & Wellbeing Information Leaflet",
        "anchor_text": "Workplace advisors write informational guidance sheets on mental wellbeing, safety, and training. Shifting erratically between person points of view (e.g. from 'one' to 'you' to 'we') disorients the reader and weakens advisory authority.",
        "rule_formula_title": "Point of View Consistency Architecture: Maintain Perspective",
        "rule_formula_html": """Choose your point of view and maintain it throughout the entire paragraph:
<div class="formula-strip">
  <span class="fpill fpill-subj">First Person (I / We):</span> Personal reflection, direct organizational reports &bull;
  <span class="fpill fpill-verb">Second Person (You):</span> Direct instructional guidance &bull;
  <span class="fpill fpill-clause">Third Person (They / Employees):</span> Objective policy
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Second Person (Instructional):</strong> <em>"When <strong>you</strong> enter the clean room, <strong>you</strong> must wash <strong>your</strong> hands."</em></li>
  <li><strong>Third Person (General Policy):</strong> <em>"When <strong>employees</strong> enter the clean room, <strong>they</strong> must wash <strong>their</strong> hands."</em></li>
  <li><strong>Unintended Pronoun Shift Pitfall:</strong> <em>"If an employee feels unwell, <strong>you</strong> should inform <strong>your</strong> manager."</em> &rarr; Fix: <em>"If an employee feels unwell, <strong>they</strong> should inform <strong>their</strong> manager."</em></li>
</ul>""",
        "worked_bad": "When a worker arrives on site, you must sign in so that we can track your attendance.",
        "worked_good": "When workers arrive on site, they must sign in so that supervisors can track their attendance.",
        "worked_why": "Eliminated the confusing shift from third person ('a worker') to second person ('you/your'), creating consistent third-person perspective.",
        "golden_rule": "THE PERSPECTIVE COMPASS: Decide who you are talking to before writing. If you start with 'employees', stick with 'they/their'. If you address the reader as 'you', stay with 'you/your' to the very end!",
        "exercise_a": [
            ("Which sentence maintains consistent second-person pronouns throughout?",
             ["A) When you join the gym, employees must complete a health form.", "B) When you join the gym, you must complete a health form.", "C) When you join the gym, we must complete a health form."],
             "B"),
            ("Choose the option that maintains consistent third-person plural pronouns:",
             ["A) If candidates pass the exam, you will receive a certificate.", "B) If candidates pass the exam, they will receive their certificates.", "C) If candidates pass the exam, he will receive your certificate."],
             "B"),
            ("Identify the sentence with an erratic pronoun shift:",
             ["A) All staff must wear ID badges so security can verify their identity.", "B) When a visitor arrives, you must show them to reception.", "C) If a visitor arrives, they must wait until their host collects them."],
             "B"),
            ("Select the sentence with perfect pronoun harmony:",
             ["A) We inspected the depot yesterday, and our team identified several hazards.", "B) We inspected the depot yesterday, and your team identified several hazards.", "C) We inspected the depot yesterday, and their team identified several hazards."],
             "A")
        ],
        "exercise_b": [
            ("Correct pronoun shift to second person", "When a worker lifts a heavy box, you must bend your knees", "When you lift a heavy box, you must bend your knees."),
            ("Correct pronoun shift to third person", "If an apprentice needs advice, you should consult your mentor", "If an apprentice needs advice, they should consult their mentor."),
            ("Maintain first-person plural consistency", "Our company values our staff and we reward your hard work", "Our company values our staff and we reward our team's hard work.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Employee Guidance Leaflet",
        "proofreading_scenario": "Examine this excerpt from an advice leaflet on managing workplace stress. Identify exactly 4 erratic pronoun shifts.",
        "proofreading_text": "Managing Workplace Stress: When an employee feels overwhelmed by heavy workloads, you should take regular screen breaks. They should discuss your concerns openly with your line manager. If workers need confidential counselling, you can access the employee assistance programme whenever one needs support.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Shift from third person singular ('an employee') to second person ('you should' -> 'they should')",
            "Shift from third person ('They should discuss') to second person ('your concerns' -> 'their concerns')",
            "Shift from third person ('workers') to second person ('you can access' -> 'they can access')",
            "Archaic/inconsistent pronoun switch ('whenever one needs' -> 'whenever they need')"
        ],
        "writing_prompt": "Write two instructional sentences advising new colleagues how to access the company staff intranet. Maintain consistent second-person pronouns ('you', 'your') across both sentences."
    },

    # -------------------------------------------------------------------------
    # UNIT 21
    # -------------------------------------------------------------------------
    {
        "unit": 21,
        "title": "Standard English vs Informal Slang (Done vs Did, Seen vs Saw)",
        "format": "Formal Letter of Complaint & Rectification",
        "anchor_title": "Formal Customer Complaint & Legal Rectification Letter",
        "anchor_text": "Writing to external regulatory authorities or senior management requires Standard English. Slang, regionalisms, and colloquial verb forms undermine professional authority and will cause marks to be lost in exam writing criteria.",
        "rule_formula_title": "Standard English Architecture: High Register vs Colloquial Speech",
        "rule_formula_html": """Standard English is the universally accepted formal dialect of business and academia:
<div class="formula-strip">
  <span class="fpill fpill-subj">Non-Standard / Slang:</span> done it &bull; seen it &bull; would of &bull; gonna &bull; ain't &bull; innit
</div>
<div class="formula-strip" style="margin-top:3px;">
  <span class="fpill fpill-verb">Standard English:</span> did it &bull; saw it &bull; would have &bull; going to &bull; is not
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>Did vs Done:</strong> <em>"I <strong>did</strong> the stock check"</em> (Simple past) vs <em>"I <strong>have done</strong> the stock check"</em> (With helper 'have'). Never say <em>"I done it"</em>.</li>
  <li><strong>Saw vs Seen:</strong> <em>"We <strong>saw</strong> the problem"</em> (Simple past) vs <em>"We <strong>have seen</strong> the problem"</em>. Never say <em>"We seen it"</em>.</li>
  <li><strong>Would have (NOT 'would of'):</strong> <em>"The engineer <strong>would have</strong> fixed the machine if parts were available."</em></li>
  <li><strong>Double Negatives:</strong> Never use double negatives (e.g. <em>"We haven't got no stock"</em> &rarr; <em>"We do not have any stock"</em>).</li>
</ul>""",
        "worked_bad": "We seen the leak and done what we could, but we couldn't do nothing because we ain't got no tools.",
        "worked_good": "We saw the leak and did what we could, but we could not do anything because we did not have any tools.",
        "worked_why": "Replaced non-standard 'seen' with 'saw', 'done' with 'did', and eradicated both double negatives ('couldn't do nothing' and 'ain't got no').",
        "golden_rule": "THE JOB INTERVIEW TEST: If a word sounds like casual street chat with friends (done it, seen it, would of, ain't), leave it at home! In professional writing, use 'did', 'saw', 'would have', and 'is not'.",
        "exercise_a": [
            ("Choose the sentence written in correct Standard English:",
             ["A) I seen the delivery lorry arrive at noon.", "B) I saw the delivery lorry arrive at noon.", "C) I done saw the delivery lorry arrive at noon."],
             "B"),
            ("Identify the correct form of the helper verb construction:",
             ["A) The manager would of approved the overtime.", "B) The manager would have approved the overtime.", "C) The manager would off approved the overtime."],
             "B"),
            ("Which sentence successfully eliminates the double negative?",
             ["A) We didn't receive no notification from the depot.", "B) We didn't receive any notification from the depot.", "C) We ain't received no notification from the depot."],
             "B"),
            ("Select the sentence suitable for a formal business letter:",
             ["A) The supervisor did the risk assessment yesterday.", "B) The supervisor done the risk assessment yesterday.", "C) The supervisor done did the risk assessment yesterday."],
             "A")
        ],
        "exercise_b": [
            ("Replace non-standard 'done' with 'did'", "The technician done all the electrical tests this morning", "The technician did all the electrical tests this morning."),
            ("Replace 'would of' with 'would have'", "Our team would of completed the order if the power stayed on", "Our team would have completed the order if the power stayed on."),
            ("Eliminate the double negative", "The warehouse hasn't got no spare safety helmets", "The warehouse has no spare safety helmets.")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Formal Complaint Response",
        "proofreading_scenario": "Review this draft letter prepared by a junior clerk responding to a commercial client's service complaint. Identify exactly 4 non-standard English slang and grammatical errors.",
        "proofreading_text": "Dear Mr Robinson, We received your letter regarding the delayed order. Our dispatch team done everything possible to resolve the issue. We seen the courier tracking update, and the driver should of notified you sooner. The depot supervisor confirmed that we ain't got no records of your earlier phone call.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Non-standard past verb ('done everything' -> 'did everything')",
            "Non-standard past verb ('seen the courier' -> 'saw the courier')",
            "Phonetic misspelling of 'would have' ('should of notified' -> 'should have notified')",
            "Slang and double negative ('ain't got no records' -> 'do not have any records')"
        ],
        "writing_prompt": "Write two formal sentences for a workplace incident log explaining what you saw happen and what actions you did to rectify the problem. Ensure 100% Standard English."
    },

    # -------------------------------------------------------------------------
    # UNIT 22
    # -------------------------------------------------------------------------
    {
        "unit": 22,
        "title": "Homophones Set 1 — Their, There, They're",
        "format": "Facilities Management Memo & Relocation Plan",
        "anchor_title": "Office Relocation & Workspace Allocation Notice",
        "anchor_text": "Facilities officers coordinate office moves, desk allocations, and equipment logistics. Confusing 'their', 'there', and 'they're' is one of the most visible spelling errors in English and immediately lowers marking bands in writing exams.",
        "rule_formula_title": "The Big Three Homophones: Possession, Place & Contraction",
        "rule_formula_html": """Master the three distinct meanings and orthographies:
<div class="formula-strip">
  <span class="fpill fpill-subj">THEIR</span> = Belongs to them (Possession: 'HEIR' owns property) &bull;
  <span class="fpill fpill-verb">THERE</span> = A location / Place (Contains 'HERE') &bull;
  <span class="fpill fpill-punct">THEY'RE</span> = They are (Contraction: apostrophe replaces 'a')
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>THEIR (Possessive):</strong> <em>"All employees must collect <strong>their</strong> new security passes."</em></li>
  <li><strong>THERE (Place / Existence):</strong> <em>"Please stack the crates over <strong>there</strong>; <strong>there</strong> are forty chairs."</em></li>
  <li><strong>THEY'RE (They Are):</strong> <em>"<strong>They're</strong> going to finish painting the conference room before noon."</em></li>
</ul>""",
        "worked_bad": "The managers parked there cars over their because they're permits was expired.",
        "worked_good": "The managers parked their cars over there because their permits were expired.",
        "worked_why": "Corrected 'there cars' to possessive 'their', 'over their' to location 'there', and 'they're permits' to possessive 'their'.",
        "golden_rule": "THE 'THEY ARE' TEST: Try replacing the word with 'THEY ARE'. If 'they are' fits sensibly, write THEY'RE. If it's a place (like HERE), write THERE. If it belongs to them, write THEIR.",
        "exercise_a": [
            ("Choose the correct homophone: <em>'The contractors left [______] toolkits in the basement.'</em>",
             ["A) there", "B) their", "C) they're"],
             "B"),
            ("Choose the correct homophone: <em>'Please place the new first aid box over [______].'</em>",
             ["A) their", "B) there", "C) they're"],
             "B"),
            ("Which sentence uses <em>'they're'</em> correctly?",
             ["A) They're arriving on the 09:15 train from London.", "B) The nurses hung they're coats in the wardrobe.", "C) Put the package right they're."],
             "A"),
            ("Select the sentence with zero homophone errors:",
             ["A) Their are three forklifts parked over they're by their charging station.", "B) There are three forklifts parked over there by their charging station.", "C) There are three forklifts parked over their by they're charging station."],
             "B")
        ],
        "exercise_b": [
            ("Insert their, there, or they're", "All technicians must bring [______] safety certificates", "their"),
            ("Insert their, there, or they're", "[______] are six meeting rooms available on Floor 2", "There"),
            ("Insert their, there, or they're", "The trainees said that [______] ready for the practical assessment", "they're")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Office Relocation Plan",
        "proofreading_scenario": "Read this staff briefing memo concerning office desk relocations. Identify exactly 4 homophone errors involving their, there, and they're.",
        "proofreading_text": "Internal Memo: Desk Moves for Finance Team. On Friday, the IT team will move all computers over their to Wing B. Staff should pack all they're personal files into cardboard crates before 16:00. Their are twenty labels provided for each desk. If employees need extra packing tape, they're welcome to collect it from reception.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Used possessive 'their' for place ('over their' -> 'over there')",
            "Used contraction 'they're' for possession ('they're personal files' -> 'their personal files')",
            "Used possessive 'Their' for existential 'There' ('Their are twenty' -> 'There are twenty')",
            "Contraction 'they're' is correct; check text for another error or verify count."
        ],
        "writing_prompt": "Write two sentences advising colleagues where to place their belongings in a new office. Use both 'their' and 'there' correctly."
    },

    # -------------------------------------------------------------------------
    # UNIT 23
    # -------------------------------------------------------------------------
    {
        "unit": 23,
        "title": "Homophones Set 2 — Two, To, Too",
        "format": "Commercial Quotation & Supply Agreement",
        "anchor_title": "Trade Quotation & Client Scope of Work",
        "anchor_text": "Commercial estimators provide binding financial quotations for building contracts. Confusing 'two', 'to', and 'too' damages commercial credibility and creates legal ambiguities regarding pricing and quantities.",
        "rule_formula_title": "Number, Direction & Excess Mechanics",
        "rule_formula_html": """Distinguish the number, the preposition, and the adverb:
<div class="formula-strip">
  <span class="fpill fpill-subj">TWO</span> = The Number 2 &bull;
  <span class="fpill fpill-verb">TO</span> = Direction / Preposition / Infinitive Verb &bull;
  <span class="fpill fpill-punct">TOO</span> = Also / As well / Excessively (Extra 'O' = Extra amount!)
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>TWO (Number 2):</strong> <em>"The quotation includes <strong>two</strong> replacement industrial boilers."</em></li>
  <li><strong>TO (Direction / Action):</strong> <em>"Send the invoice <strong>to</strong> accounts; we need <strong>to</strong> order parts."</em></li>
  <li><strong>TOO (Excessive / Also):</strong> <em>"The crane is <strong>too</strong> heavy for the bridge; the apprentice wants to attend <strong>too</strong>."</em></li>
</ul>""",
        "worked_bad": "We sent to apprentices too the warehouse, but the crate was to heavy to lift.",
        "worked_good": "We sent two apprentices to the warehouse, but the crate was too heavy to lift.",
        "worked_why": "Corrected 'to apprentices' to number 'two', 'too the warehouse' to direction 'to', and 'to heavy' to excessive 'too'.",
        "golden_rule": "THE 'EXTRA O' TRICK: 'Too' has an extra 'o' because it means extra! Use 'too' for too much, too hot, too heavy, or when it means 'as well'. Use 'two' for the number 2. For everything else, use 'to'.",
        "exercise_a": [
            ("Choose the correct word for the number 2: <em>'The contractor submitted [______] separate bids.'</em>",
             ["A) to", "B) too", "C) two"],
             "C"),
            ("Choose the correct word meaning 'also': <em>'Marcus completed the safety test, and Elena passed it [______].'</em>",
             ["A) to", "B) too", "C) two"],
             "B"),
            ("Which sentence uses <em>'to'</em>, <em>'too'</em>, and <em>'two'</em> correctly?",
             ["A) We walked to the site to inspect two generators, but it was too cold.", "B) We walked too the site to inspect to generators, but it was two cold.", "C) We walked to the site to inspect too generators, but it was to cold."],
             "A"),
            ("Identify the sentence with a homophone error:",
             ["A) The warehouse manager is going to order more packaging tape.", "B) The shipment arrived to late for the morning delivery schedule.", "C) Two drivers were assigned to the regional route."],
             "B")
        ],
        "exercise_b": [
            ("Insert to, too, or two", "The pallet is [______] wide to fit through the doorway", "too"),
            ("Insert to, too, or two", "Please deliver these documents [______] the accounts department", "to"),
            ("Insert to, too, or two", "The job requires [______] qualified electricians and one apprentice", "two")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Trade Quotation Cover Letter",
        "proofreading_scenario": "Proofread this quotation letter sent by a commercial electrical contractor to a school bursar. Identify exactly 4 errors involving to, too, and two.",
        "proofreading_text": "Dear Mrs Higgins, Apex Electrical is pleased too provide this formal quotation for rewiring your IT laboratory. We have allocated to senior electricians to complete the installation over the half-term break. Please note that the existing main distribution board is to old to meet modern safety codes. If you require extra power points, we can supply those to.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Used 'too' instead of preposition 'to' ('pleased too provide' -> 'pleased to provide')",
            "Used 'to' instead of number 'two' ('allocated to senior' -> 'allocated two senior')",
            "Used 'to' instead of excess 'too' ('is to old' -> 'is too old')",
            "Used 'to' instead of 'as well' 'too' ('supply those to' -> 'supply those too')"
        ],
        "writing_prompt": "Write two sentences describing a work task involving materials or equipment. Include the number 'two', the preposition 'to', and the adverb 'too' (meaning also or excessively) across your sentences."
    },

    # -------------------------------------------------------------------------
    # UNIT 24
    # -------------------------------------------------------------------------
    {
        "unit": 24,
        "title": "Homophones Set 3 — Hear/Here, Wear/Where, New/Knew",
        "format": "Staff Noticeboard & Workplace Safety Bulletin",
        "anchor_title": "Factory Workshop Noticeboard & PPE Directive",
        "anchor_text": "Safety officers post permanent instructional placards across machine workshops. Confusing homophones like 'wear' and 'where', or 'hear' and 'here' makes official safety directives look careless and risks confusing mandatory instructions.",
        "rule_formula_title": "Sensory & Spatial Homophones: Orthographic Anchors",
        "rule_formula_html": """Pair each homophone with its visual memory anchor:
<div class="formula-strip">
  <span class="fpill fpill-subj">HEAR</span> (Listen with your EAR) vs <span class="fpill fpill-subj">HERE</span> (This place) &bull;
  <span class="fpill fpill-verb">WEAR</span> (Clothing/PPE) vs <span class="fpill fpill-verb">WHERE</span> (Location question) &bull;
  <span class="fpill fpill-conn">NEW</span> (Fresh/Recent) vs <span class="fpill fpill-conn">KNEW</span> (Past of 'know')
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>HEAR vs HERE:</strong> <em>"Can you <strong>hear</strong> the fire alarm over <strong>here</strong>?"</em> (Hear has an 'EAR' inside it).</li>
  <li><strong>WEAR vs WHERE:</strong> <em>"You must <strong>wear</strong> eye goggles <strong>where</strong> machinery is operating."</em></li>
  <li><strong>NEW vs KNEW:</strong> <em>"The apprentice <strong>knew</strong> how to operate the <strong>new</strong> laser cutter."</em> (Knew has a silent 'K' like knowledge).</li>
</ul>""",
        "worked_bad": "Sign here if you can't here the siren, and check wear you should where your ear defenders.",
        "worked_good": "Sign here if you can't hear the siren, and check where you should wear your ear defenders.",
        "worked_why": "Corrected 'here the siren' to 'hear' (auditory) and flipped 'wear/where' so that 'where' indicates location and 'wear' indicates putting on clothing.",
        "golden_rule": "THE EAR HOOK: You hEAR with your EAR (h-EAR). You knEW facts using knoWledge (k-n-e-w). Clothe yourself in what you WEAR.",
        "exercise_a": [
            ("Choose the correct word: <em>'Please register your attendance [______] at reception.'</em>",
             ["A) hear", "B) here", "C) heare"],
             "B"),
            ("Choose the correct word: <em>'All machine operators must [______] protective boots.'</em>",
             ["A) where", "B) ware", "C) wear"],
             "C"),
            ("Which sentence uses <em>'knew'</em> and <em>'new'</em> correctly?",
             ["A) The manager knew that the new delivery had arrived.", "B) The manager new that the knew delivery had arrived.", "C) The manager knew that the knew delivery had arrived."],
             "A"),
            ("Select the sentence with zero homophone errors:",
             ["A) Where did you leave the new safety manual? Come here and look.", "B) Wear did you leave the knew safety manual? Come hear and look.", "C) Where did you leave the knew safety manual? Come here and look."],
             "A")
        ],
        "exercise_b": [
            ("Choose between hear and here", "Stand [______] so that you can [______] the supervisor's briefing", "here / hear"),
            ("Choose between wear and where", "Do you know [______] staff must [______] high-visibility vests?", "where / wear"),
            ("Choose between new and knew", "She already [______] how to set up the [______] printer", "knew / new")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Workshop Safety Notice",
        "proofreading_scenario": "Check this safety advisory notice posted above the entrance to the industrial wood-machining workshop. Identify exactly 4 homophone errors.",
        "proofreading_text": "Attention All Workshop Staff: Before entering this bay, you must sign the register located hear on the counter. Noise levels in this area are hazardous; if you cannot here verbal warnings, alert your team leader. Staff must check the chart to see wear they are required to where mandatory ear defenders.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Used 'hear' instead of location 'here' ('located hear' -> 'located here')",
            "Used 'here' instead of listen 'hear' ('cannot here verbal' -> 'cannot hear verbal')",
            "Used 'wear' instead of location 'where' ('to see wear' -> 'to see where')",
            "Used 'where' instead of clothing 'wear' ('required to where mandatory' -> 'required to wear mandatory')"
        ],
        "writing_prompt": "Write two sentences advising a new employee about personal protective equipment in a factory. Use the words 'wear', 'where', 'hear', and 'new' across your sentences."
    },

    # -------------------------------------------------------------------------
    # UNIT 25
    # -------------------------------------------------------------------------
    {
        "unit": 25,
        "title": "Prefixes — Un-, Dis-, Mis-, Re-",
        "format": "Quality Assurance & Defect Audit",
        "anchor_title": "Quality Control & Manufacturing Defect Log",
        "anchor_text": "Quality assurance inspectors document assembly defects, misaligned components, and disconnected systems. Applying prefixes accurately alters word meanings to describe precise corrective actions without spelling errors.",
        "rule_formula_title": "Prefix Mechanics: Modifying Root Words Without Altering Base Spelling",
        "rule_formula_html": """A prefix attaches to the front of a base root word without changing the root's spelling:
<div class="formula-strip">
  <span class="fpill fpill-punct">UN-</span> = Not / Reverse &bull;
  <span class="fpill fpill-subj">DIS-</span> = Opposite / Away &bull;
  <span class="fpill fpill-verb">MIS-</span> = Badly / Wrongly &bull;
  <span class="fpill fpill-conn">RE-</span> = Again / Back
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>UN- (Not / Undo):</strong> <em>unsafe, unpack, unclear, unauthorized, unlocked</em>.</li>
  <li><strong>DIS- (Opposite):</strong> <em>disconnect, disinfect, disagree, disable, disappear</em>.</li>
  <li><strong>MIS- (Wrongly / Inaccurately):</strong> <em>misread, miscalculate, misplace, misunderstand, mislabel</em>. (Notice: <em>mis + spell = misspell</em> with double 's'!).</li>
  <li><strong>RE- (Again):</strong> <em>rebuild, reload, retest, restart, refund, replace</em>.</li>
  <li><strong>The Golden Spelling Rule:</strong> Simply glue the prefix directly onto the unchanged root word: <em>un + happy = unhappy</em>; <em>dis + satisfied = dissatisfied</em> (keep both 's's!).</li>
</ul>""",
        "worked_bad": "The technician dissconnected the cable because the container was misslabelled and uncomplete.",
        "worked_good": "The technician disconnected the cable because the container was mislabelled and incomplete.",
        "worked_why": "Corrected 'dissconnected' (dis + connect has only one 's'), 'misslabelled' (mis + label has only one 's'), and replaced 'uncomplete' with proper 'incomplete'.",
        "golden_rule": "THE GLUE RULE: A prefix is just a sticker! Never change, drop, or double letters from the original root word when sticking on un-, dis-, mis-, or re-. Just glue them together cleanly.",
        "exercise_a": [
            ("Which prefix creates a word meaning <em>'to calculate incorrectly'</em>?",
             ["A) un-", "B) dis-", "C) mis-"],
             "C"),
            ("What is the correct spelling when attaching the prefix <em>'dis-'</em> to <em>'satisfied'</em>?",
             ["A) disatisfied", "B) dissatisfied", "C) dissatsfied"],
             "B"),
            ("Choose the word that means <em>'to test a machine for a second time'</em>:",
             ["A) untest", "B) retest", "C) distest"],
             "B"),
            ("Select the sentence with zero prefix spelling errors:",
             ["A) The operator miscalculated the dimensions and had to restart the machine.", "B) The operator misscalculated the dimensions and had to restart the machine.", "C) The operator miscalculated the dimensions and had to re-start the machine."],
             "A")
        ],
        "exercise_b": [
            ("Add 'mis-' to 'place'", "Be careful not to [mis + place] the security swipe card", "misplace"),
            ("Add 'dis-' to 'connect'", "Always [dis + connect] the appliance before maintenance", "disconnect"),
            ("Add 're-' to 'build'", "The team must [re + build] the damaged brick wall", "rebuild")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Quality Defect Log Sheet",
        "proofreading_scenario": "Examine this quality control log submitted by a manufacturing line inspector. Identify exactly 4 prefix spelling errors.",
        "proofreading_text": "Batch Audit: Line 4. The quality team inspected fifty electronic sensors. Three units were rejected because an apprentice dissconnected the grounding terminal during assembly. In addition, operator Barnes missread the technical drawing and attached an uncorrect circuit board. Technicians must now retest all units before dispatch.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Doubled 's' when attaching dis- ('dissconnected' -> 'disconnected')",
            "Doubled 's' when attaching mis- ('missread' -> 'misread')",
            "Wrong negative prefix used on correct ('uncorrect' -> 'incorrect')",
            "Re-prefix issue or verify consistency ('retest' is correct; look for fourth error)."
        ],
        "writing_prompt": "Write two sentences describing a workplace error and the corrective action taken to fix it. Use at least two words with prefixes from: un-, dis-, mis-, or re- (e.g. mislabeled, disconnected, rechecked)."
    },

    # -------------------------------------------------------------------------
    # UNIT 26
    # -------------------------------------------------------------------------
    {
        "unit": 26,
        "title": "Suffixes — -ful, -less, -ly, -ment",
        "format": "Employee Performance Review & Reference",
        "anchor_title": "Staff Appraisal & Employment Reference",
        "anchor_text": "Supervisors write references and performance evaluations to support job applications and promotions. Adding suffixes transforms adjectives and verbs into adverbs and nouns. Dropping or duplicating letters when attaching suffixes ruins written professional tone.",
        "rule_formula_title": "Suffix Mechanics: -ful, -less, -ly, -ment",
        "rule_formula_html": """Suffixes attach to the ends of words to change their grammatical function:
<div class="formula-strip">
  <span class="fpill fpill-punct">-FUL</span> = Full of (Always ONE 'l'!) &bull;
  <span class="fpill fpill-subj">-LESS</span> = Without (Always TWO 's's!) &bull;
  <span class="fpill fpill-verb">-LY</span> = Adverb (How something is done) &bull;
  <span class="fpill fpill-conn">-MENT</span> = State or result of action
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt; line-height:1.42;">
  <li><strong>The -FUL Rule:</strong> The suffix <em>-ful</em> has ONLY ONE 'L': <em>careful, helpful, successful, grateful, stressful</em>. Never spell it with -full!</li>
  <li><strong>The -LESS Rule:</strong> <em>careless, spotless, endless, painless</em>.</li>
  <li><strong>The -LY Rule:</strong> Turns adjectives into adverbs: <em>quick &rarr; quickly, polite &rarr; politely, careful &rarr; carefully</em> (notice: <em>careful + ly = carefully</em> with two 'l's!).</li>
  <li><strong>The -MENT Rule:</strong> Creates nouns from verbs: <em>develop &rarr; development, manage &rarr; management, equip &rarr; equipment</em>. Keep the silent 'e' in most cases!</li>
</ul>""",
        "worked_bad": "Marcus is a carefull worker who completes every assignement quickley and shows great managment.",
        "worked_good": "Marcus is a careful worker who completes every assignment quickly and shows great management.",
        "worked_why": "Corrected 'carefull' to single 'l' (-ful), fixed spelling of 'assignment' and 'quickly', and restored silent 'e' in 'management'.",
        "golden_rule": "THE SINGLE 'L' OF -FUL: Remember: 'Full' has two L's when alone, but when it becomes a suffix (-ful), it drops one L! Be careful, be helpful, be successful.",
        "exercise_a": [
            ("Which word is spelled correctly with the suffix <em>'-ful'</em>?",
             ["A) successfull", "B) successful", "C) succesful"],
             "B"),
            ("How do you form the adverb from the adjective <em>'careful'</em>?",
             ["A) carefully", "B) carefuly", "C) carefullly"],
             "A"),
            ("Select the correct noun formed by adding <em>'-ment'</em> to <em>'equip'</em>:",
             ["A) equipement", "B) equipment", "C) equiptment"],
             "B"),
            ("Which sentence contains zero suffix spelling errors?",
             ["A) Elena communicated politely and demonstrated exceptional leadership management.", "B) Elena communicated politeley and demonstrated exceptional leadership managment.", "C) Elena communicated politely and demonstrated exceptional leadership managment."],
             "A")
        ],
        "exercise_b": [
            ("Add -ful to 'skill'", "David is a [skill + ful] carpenter", "skilful / skillful"),
            ("Add -ly to 'prompt'", "The IT desk resolved our enquiry [prompt + ly]", "promptly"),
            ("Add -ment to 'develop'", "The apprentice made rapid [develop + ment] across all modules", "development")
        ],
        "proofreading_title": "Forensic Workplace Proofreading: Employee Reference Letter",
        "proofreading_scenario": "Proofread this formal job reference written by a retail store manager for a departing supervisor. Identify exactly 4 suffix spelling errors.",
        "proofreading_text": "Reference for Sarah Jenkins: Sarah has been a powerfull asset to our sales team. She handles customer complaints politeley and is always helpfull during busy weekend shifts. Her punctuality is spotless, and she has contributed significantly to the continuous developement of our department.",
        "proofreading_err_count": 4,
        "proofreading_errors": [
            "Double 'l' in -ful suffix ('powerfull' -> 'powerful')",
            "Misspelled -ly adverb suffix ('politeley' -> 'politely')",
            "Double 'l' in -ful suffix ('helpfull' -> 'helpful')",
            "Misspelled -ment noun suffix ('developement' -> 'development')"
        ],
        "writing_prompt": "Write two sentences commending a team member's performance. Use at least one adjective ending in -ful (e.g. careful, helpful) and one adverb ending in -ly (e.g. quickly, politely, efficiently)."
    }
]
