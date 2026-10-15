# Append Section: Phonics, Word Banks, Mixed Workouts, Writing Tasks, Answers & Audit to spag_data_e3_84p.py

PHONICS_RULES_PAGES = [
    # Page 55
    {
        "page_num": 55,
        "title": "Rule 1: Short Vowels & Consonant Doubling (+ed, +ing)",
        "subtitle": "Protecting Short Vowel Sounds in Workplace Action Verbs",
        "rule_summary": "When a single-syllable word has ONE short vowel followed by ONE final consonant (the 1-1-1 pattern), DOUBLE the final consonant before adding '-ed' or '-ing'. This prevents the short vowel from turning into a long vowel.",
        "examples_table": [
            ("stop", "stopped", "stopping", "The driver stopped at the security gate."),
            ("plan", "planned", "planning", "We planned the delivery rota carefully."),
            ("drop", "dropped", "dropping", "The courier dropped the fragile carton."),
            ("fit", "fitted", "fitting", "The engineer fitted a replacement valve."),
            ("slip", "slipped", "slipping", "The worker slipped on the wet kitchen tiles."),
            ("grab", "grabbed", "grabbing", "She grabbed the fire extinguisher quickly."),
            ("shop", "shopped", "shopping", "They shopped for wholesale ingredients."),
            ("spot", "spotted", "spotting", "The supervisor spotted a safety hazard.")
        ],
        "contrast_note": "<strong>Why do we NOT double in 'clean' or 'help'?</strong><br>&bull; <em>clean &rarr; cleaned:</em> Has TWO vowels (ea), so the vowel is already protected.<br>&bull; <em>help &rarr; helped:</em> Has TWO consonants (lp), so doubling is not needed.",
        "cloze_drills": [
            ("The technician (fit) ____________ the new safety valve yesterday.", "fitted"),
            ("We are (plan) ____________ a fire evacuation drill for next week.", "planning"),
            ("The machine suddenly (stop) ____________ running at two o'clock.", "stopped"),
            ("A warehouse assistant (drop) ____________ the metal wrench on the floor.", "dropped"),
            ("He (slip) ____________ on the greasy workshop ramp this morning.", "slipped")
        ]
    },
    # Page 56
    {
        "page_num": 56,
        "title": "Rule 2: The Silent Final 'e' Rule (Drop 'e' before Vowels)",
        "subtitle": "Adding Suffixes to Words Ending in a Silent 'e'",
        "rule_summary": "When a word ends in a silent 'e' and you add a suffix starting with a VOWEL (-ing, -ed, -er, -able), DROP the final 'e'! But when adding a suffix starting with a CONSONANT (-ful, -less, -ly, -ment), KEEP the final 'e'.",
        "drop_table": [
            ("make", "-ing", "making", "Drop 'e' before vowel suffix"),
            ("hope", "-ing", "hoping", "Drop 'e' before vowel suffix"),
            ("care", "-ing", "caring", "Drop 'e' before vowel suffix"),
            ("write", "-ing", "writing", "Drop 'e' before vowel suffix"),
            ("close", "-ed", "closed", "Drop 'e' before vowel suffix"),
            ("use", "-ed", "used", "Drop 'e' before vowel suffix"),
            ("drive", "-er", "driver", "Drop 'e' before vowel suffix"),
            ("safe", "-ty", "safety", "Keep/drop depends on suffix")
        ],
        "keep_table": [
            ("care", "-ful", "careful", "Keep 'e' before consonant suffix"),
            ("hope", "-ful", "hopeful", "Keep 'e' before consonant suffix"),
            ("safe", "-ly", "safely", "Keep 'e' before consonant suffix"),
            ("arrange", "-ment", "arrangement", "Keep 'e' before consonant suffix"),
            ("polite", "-ly", "politely", "Keep 'e' before consonant suffix"),
            ("late", "-ly", "lately", "Keep 'e' before consonant suffix")
        ],
        "cloze_drills": [
            ("The chef is (make) ____________ forty fresh sandwiches for the buffet.", "making"),
            ("Please drive (safe) ____________ in the warehouse yard.", "safely"),
            ("I am (write) ____________ an email to my course tutor.", "writing"),
            ("All staff made an (arrange) ____________ to share transport.", "arrangement"),
            ("Be very (care) ____________ when handling hot kitchen liquids.", "careful")
        ]
    },
    # Page 57
    {
        "page_num": 57,
        "title": "Rule 3: 'i before e except after c' for the /i:/ Sound",
        "subtitle": "Mastering the Most Famous English Spelling Rule in Workplace Words",
        "rule_summary": "Write <strong>'i' before 'e'</strong> (ie) when the word makes the long /i:/ ('ee') sound. BUT write <strong>'e' before 'i'</strong> (ei) when it comes immediately after the letter <strong>'c'</strong>.",
        "ie_words": [
            ("piece", "A piece of machinery was damaged during transit."),
            ("chief", "The chief fire warden conducted the headcount."),
            ("brief", "The manager gave a brief safety presentation."),
            ("field", "The staff parked their cars on the overflow field."),
            ("niece", "My niece completed her childcare apprenticeship."),
            ("relief", "It was a great relief when the power was restored.")
        ],
        "cei_words": [
            ("receive", "Did you receive the updated shift rota by email?"),
            ("receipt", "Always give the customer an official VAT receipt."),
            ("ceiling", "The maintenance contractor painted the office ceiling."),
            ("deceive", "Never try to deceive a health and safety auditor.")
        ],
        "special_note": "<strong>The 'Friend' Memory Hook:</strong><br><em>'Friend'</em> has <strong>ie</strong>, but makes a short /e/ sound. Remember: <em>'A true fr<strong>ie</strong>nd stays to the <strong>end</strong>!'</em>",
        "cloze_drills": [
            ("Please keep your purchase (receipt) ____________ for warranty claims.", "receipt"),
            ("The team held a (brief) ____________ meeting before starting work.", "brief"),
            ("Did you (receive) ____________ the delivery note from the driver?", "receive"),
            ("Replace the broken (piece) ____________ of glass immediately.", "piece"),
            ("Water was leaking from the storeroom (ceiling) ____________.", "ceiling")
        ]
    },
    # Page 58
    {
        "page_num": 58,
        "title": "Rule 4: Changing 'y' to 'i' before Suffixes",
        "subtitle": "Plurals, Past Verbs and Adverbs Ending in 'y'",
        "rule_summary": "When a base word ends in a CONSONANT + 'y', change the <strong>'y' to 'i'</strong> before adding suffixes like <em>-es, -ed, -er, -est, -ly</em>. But if the word ends in a VOWEL + 'y', keep the 'y' unchanged!",
        "consonant_y_table": [
            ("hurry", "hurries", "hurried", "Consonant 'r' + y &rarr; change to 'i'"),
            ("carry", "carries", "carried", "Consonant 'r' + y &rarr; change to 'i'"),
            ("copy", "copies", "copied", "Consonant 'p' + y &rarr; change to 'i'"),
            ("study", "studies", "studied", "Consonant 'd' + y &rarr; change to 'i'"),
            ("happy", "happier", "happily", "Consonant 'p' + y &rarr; change to 'i'"),
            ("heavy", "heavier", "heavily", "Consonant 'v' + y &rarr; change to 'i'")
        ],
        "vowel_y_table": [
            ("play", "plays", "played", "Vowel 'a' + y &rarr; KEEP 'y'"),
            ("stay", "stays", "stayed", "Vowel 'a' + y &rarr; KEEP 'y'"),
            ("delay", "delays", "delayed", "Vowel 'a' + y &rarr; KEEP 'y'"),
            ("employ", "employs", "employed", "Vowel 'o' + y &rarr; KEEP 'y'")
        ],
        "ing_exception": "<strong>The -ing Exception:</strong> When adding '-ing', always keep the 'y' so you do not get a double 'ii' (e.g. <em>hurrying, carrying, studying, copying</em>).",
        "cloze_drills": [
            ("The delivery driver (carry) ____________ two boxes up the stairs.", "carried"),
            ("The train was (delay) ____________ by twenty minutes.", "delayed"),
            ("Marcus (hurry) ____________ to catch the morning staff bus.", "hurried"),
            ("She completed the audit task (happy) ____________.", "happily"),
            ("The apprentice is (study) ____________ for his technical diploma.", "studying")
        ]
    }
]

WORD_BANKS_PAGES = [
    # Page 59
    {
        "page_num": 59,
        "title": "Master Word Bank 1: Calendar, Days, Months & Time",
        "subtitle": "Essential Functional Vocabulary for Scheduling Shifts & Appointments",
        "days": [
            ("Monday", "Mon-day", "First day of the working week"),
            ("Tuesday", "Tues-day", "Silent 'e' in Tues"),
            ("Wednesday", "Wed-nes-day", "Wed + nes + day (Say Wed-nes-day to spell)"),
            ("Thursday", "Thurs-day", "Starts with 'Th' sound"),
            ("Friday", "Fri-day", "Starts with capital 'F'"),
            ("Saturday", "Satur-day", "Satur + day"),
            ("Sunday", "Sun-day", "Sun + day")
        ],
        "months": [
            ("January", "Jan-u-ary", "Winter month 1"),
            ("February", "Feb-ru-ary", "Notice the 'r' after 'b'"),
            ("March", "March", "Spring month"),
            ("April", "A-pril", "Starts with capital 'A'"),
            ("May", "May", "Short 3-letter month"),
            ("June", "June", "Silent 'e' at end"),
            ("July", "Ju-ly", "Summer month"),
            ("August", "Au-gust", "Au sound at start"),
            ("September", "Sep-tem-ber", "Autumn month"),
            ("October", "Oc-to-ber", "Autumn month"),
            ("November", "No-vem-ber", "Autumn month"),
            ("December", "De-cem-ber", "Winter month 12")
        ],
        "time_terms": [
            ("morning", "06:00 to 12:00"),
            ("afternoon", "12:00 to 18:00"),
            ("evening", "18:00 to 22:00"),
            ("yesterday", "The day before today"),
            ("tomorrow", "The day after today (One 'm', two 'r's)"),
            ("calendar", "Spelled with -ar at the end, not -er"),
            ("schedule", "Daily timetable of tasks"),
            ("quarter", "15 minutes or 1/4"),
            ("minute", "60 seconds in an hour"),
            ("appointment", "Booked official meeting time")
        ],
        "challenge": "Proofread: <em>'on wensday, 14 feburary, i have an apointment.'</em> &rarr; <strong>On Wednesday, 14 February, I have an appointment.</strong>"
    },
    # Page 60
    {
        "page_num": 60,
        "title": "Master Word Bank 2: Workplace Roles, Departments & Operations",
        "subtitle": "Professional Terms for Job Applications, CVs & Organisational Charts",
        "roles": [
            ("manager", "Person in charge of a department or team"),
            ("supervisor", "Person who oversees daily practical tasks"),
            ("assistant", "Person who supports a senior colleague"),
            ("apprentice", "Trainee learning a trade or skilled job"),
            ("colleague", "A person you work alongside (co-worker)"),
            ("technician", "Specialist who operates technical equipment"),
            ("receptionist", "Staff member greeting visitors at the front desk"),
            ("customer", "Person or organisation purchasing goods/services")
        ],
        "departments": [
            ("reception", "Front desk welcoming area"),
            ("warehouse", "Storage facility for wholesale goods"),
            ("administration", "Office team managing records and paperwork"),
            ("facilities", "Team maintaining buildings and grounds"),
            ("logistics", "Organisation of goods transport and deliveries"),
            ("catering", "Food preparation and hospitality team")
        ],
        "operations": [
            ("signature", "Your handwritten official legal name"),
            ("application", "Formal request for a job or course place"),
            ("enquiry", "Question asking for information or prices"),
            ("interview", "Formal meeting to evaluate a candidate"),
            ("contract", "Legally binding agreement between parties"),
            ("delivery", "Bringing goods to a specified destination")
        ],
        "challenge": "Proofread: <em>'the warehouse supervizer signed the contrct.'</em> &rarr; <strong>The warehouse supervisor signed the contract.</strong>"
    },
    # Page 61
    {
        "page_num": 61,
        "title": "Master Word Bank 3: Health, Safety, Hazards & First Aid",
        "subtitle": "Critical Vocabulary for Site Safety Signs, Risk Forms & Emergency Logs",
        "hazards": [
            ("caution", "Take care; potential minor risk ahead"),
            ("danger", "Immediate risk of serious physical injury"),
            ("warning", "Notice alerting staff to a hazard"),
            ("hazard", "Any source of potential damage or harm"),
            ("emergency", "Serious unexpected situation needing urgent action"),
            ("accident", "Unintended event resulting in injury or damage")
        ],
        "ppe": [
            ("equipment", "Tools and protective gear (spelled equip-ment)"),
            ("protective", "Designed to shield a worker from harm"),
            ("goggles", "Protective eyewear guarding against splashes"),
            ("gloves", "Protective handwear shielding from cuts or chemicals"),
            ("helmet", "Hard safety hat protecting the head"),
            ("uniform", "Official designated workplace clothing")
        ],
        "emergency_terms": [
            ("first aid", "Initial medical assistance given on site"),
            ("extinguisher", "Portable device for extinguishing small fires"),
            ("evacuation", "Clearing a building calmly during an alarm"),
            ("assembly point", "Safe designated outdoor meeting location"),
            ("incident", "An occurrence, breakdown, or safety breach"),
            ("maintenance", "Routine upkeep keeping equipment safe (-ten-ance)")
        ],
        "challenge": "Proofread: <em>'in an emergancy, grab the fire extingwisher.'</em> &rarr; <strong>In an emergency, grab the fire extinguisher.</strong>"
    },
    # Page 62
    {
        "page_num": 62,
        "title": "Master Word Bank 4: Everyday Admin & Application Forms",
        "subtitle": "Official Form-Filling Terminology & Essential Identity Records",
        "personal_fields": [
            ("surname", "Official family name or last name"),
            ("forename", "First name given at birth"),
            ("address", "House number, street name, town (two 'd's, two 's's)"),
            ("postcode", "Alphanumeric UK postal routing code (e.g. LS1 4ET)"),
            ("telephone", "Phone contact number for workplace or home"),
            ("declaration", "Official statement confirming details are true")
        ],
        "administrative_terms": [
            ("confirmation", "Official verification of a booking or agreement"),
            ("enrolment", "Registration process onto an educational course"),
            ("statement", "Written account of facts, reasons, or finances"),
            ("qualification", "Certified proof of acquired skills or knowledge"),
            ("attendance", "Record of being present on shift or in class"),
            ("reference", "Written character or work testimony from an employer")
        ],
        "action_verbs": [
            ("complete", "To finish filling in every required box"),
            ("submit", "To send or hand in an official document"),
            ("verify", "To check and prove that information is accurate"),
            ("authorise", "To give official permission for an action"),
            ("attach", "To join a file or paper slip to a form")
        ],
        "challenge": "Proofread: <em>'please compleat your full adress and telepone number.'</em> &rarr; <strong>Please complete your full address and telephone number.</strong>"
    }
]

MIXED_WORKOUTS_PAGES = [
    # Page 63: Workout 1
    {
        "page_num": 63,
        "title": "Mixed SPaG Workout 1: Retail & Customer Incident Log",
        "scenario": "You are a customer service assistant in a busy retail supermarket. A customer reported an incident near the dairy aisle. Proofread the incident memo and complete the sentence expansion drills.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
INCIDENT LOG &bull; STORE #142 (LEEDS)<br>
On <strong>tuesday</strong> morning, a customer reported a broken jar of jam in aisle 4. 
I placed yellow caution cones around the area <strong>because</strong> I went to fetch a mop. 
A stock assistant <strong>cleand</strong> the tiles thoroughly with detergent. 
The customer was very polite, <strong>and</strong> she was in a hurry to catch her bus. 
The store manager <strong>were</strong> informed at eleven o'clock. 
The area was declared safe at 11:15.
</div>""",
        "errors": [
            "Capitalise day of the week: 'tuesday' -> 'Tuesday'",
            "Change incorrect connective 'because' to 'and' or 'so': '...cones around the area, and I went...'",
            "Fix regular past tense spelling: 'cleand' -> 'cleaned'",
            "Change connective 'and' to contrast 'but': '...polite, but she was in a hurry...'",
            "Change plural verb to singular agreement: 'store manager were' -> 'was informed'",
            "Ensure final sentence ends with a clear full stop."
        ],
        "expansion_prompt": "Combine these short sentences into professional compound sentences:",
        "expansion_drills": [
            ("The cash register jammed. The cashier called the duty supervisor.", "The cash register jammed, so the cashier called the duty supervisor."),
            ("We offered the customer a replacement. The product was out of stock.", "We offered the customer a replacement, but the product was out of stock.")
        ]
    },
    # Page 64: Workout 2
    {
        "page_num": 64,
        "title": "Mixed SPaG Workout 2: Warehouse Logistics Shift Handover",
        "scenario": "A warehouse team leader prepared this shift handover summary for the night shift supervisor. Proofread the memo and complete the sentence building drills.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
SHIFT HANDOVER &bull; INTAKE BAY 3<br>
The afternoon crew unloaded forty wooden <strong>pallet</strong> from the delivery truck. 
The driver <strong>stoped</strong> his vehicle in bay 2 and signed the consignment sheet. 
Both forklift trucks <strong>is</strong> parked in the charging bay overnight. 
Rachel and David <strong>done</strong> a full count of all damaged cartons. 
All high-vis vests <strong>was</strong> returned to the equipment locker.
</div>""",
        "errors": [
            "Change singular noun to plural: 'wooden pallet' -> 'pallets'",
            "Double the consonant in past tense: 'stoped' -> 'stopped'",
            "Change singular verb to plural agreement: 'trucks is' -> 'are parked'",
            "Change non-standard 'done' to standard past tense: 'done' -> 'did'",
            "Change singular verb to plural agreement: 'vests was' -> 'were returned'",
            "Ensure final sentence ends with a clear full stop."
        ],
        "expansion_prompt": "Combine these sentences using the connectives <em>because</em> and <em>so</em>:",
        "expansion_drills": [
            ("The loading bay door was damaged. The maintenance technician arrived quickly.", "The loading bay door was damaged, so the maintenance technician arrived quickly."),
            ("The driver wore steel safety boots. Heavy pallets were moving across the floor.", "The driver wore steel safety boots because heavy pallets were moving across the floor.")
        ]
    },
    # Page 65: Workout 3
    {
        "page_num": 65,
        "title": "Mixed SPaG Workout 3: Care Home Daily Activity & Medication Handover",
        "scenario": "A senior healthcare assistant logged this evening activity update for residents at Meadowbrook Care Home. Find all 6 deliberate SPaG errors and complete the punctuation drills.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
CARE LOG &bull; MEADOWBROOK RESIDENTIAL HOME<br>
During the afternoon, <strong>dr ahmed</strong> visited room 6 to examine Mrs Davies. 
Her prescription was updated, <strong>so</strong> <strong>i</strong> collected the tablets from the pharmacy. 
The residents enjoyed afternoon tea with biscuits, cake <strong>and</strong> fruit. 
<strong>could</strong> you please check her room temperature at ten o'clock<strong>.</strong> 
All night duty care assistants <strong>has</strong> signed the medication administration sheet.
</div>""",
        "errors": [
            "Capitalise formal title and surname: 'dr ahmed' -> 'Dr Ahmed'",
            "Capitalise standalone personal pronoun: 'i' -> 'I'",
            "Add comma in simple list: 'biscuits, cake, and fruit' or 'biscuits, cake and fruit' (verify separator)",
            "Capitalise question starter: 'could' -> 'Could'",
            "Change full stop on direct request to question mark: 'ten o'clock?'",
            "Change singular verb to plural agreement: 'assistants has' -> 'have signed'"
        ],
        "expansion_prompt": "Form complete, correctly punctuated questions and statements:",
        "expansion_drills": [
            ("where / is / the / first aid / kit / stored", "Where is the first aid kit stored?"),
            ("mrs davies / drank / her / medicine / and / rested / quietly", "Mrs Davies drank her medicine and rested quietly.")
        ]
    },
    # Page 66: Workout 4
    {
        "page_num": 66,
        "title": "Mixed SPaG Workout 4: Facilities & Maintenance Repair Request",
        "scenario": "A building caretaker submitted this urgent repair ticket for the office heating and plumbing network. Correct all 7 SPaG errors and join the clauses.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
FACILITY WORK ORDER &bull; TICKET #4418<br>
On <strong>friday</strong> afternoon, the ground floor heating pipe burst near office 3. 
Water was leaking rapidly, <strong>because</strong> I turned off the isolation valve immediately. 
The caretaker <strong>callt</strong> Apex Plumbing on <strong>high street</strong>. 
The engineer <strong>comed</strong> at 15:30 with two new copper <strong>pipe</strong>. 
He replaced the valve <strong>and</strong> tested the water pressure.
</div>""",
        "errors": [
            "Capitalise day of the week: 'friday' -> 'Friday'",
            "Change incorrect connective 'because' to 'so': '...rapidly, so I turned off...'",
            "Fix regular past tense spelling: 'callt' -> 'called'",
            "Capitalise proper street name: 'high street' -> 'High Street'",
            "Change non-standard 'comed' to irregular past tense: 'came'",
            "Make noun plural: 'two new copper pipe' -> 'pipes'",
            "Ensure entire work order ends with a clear full stop."
        ],
        "expansion_prompt": "Combine these sentences using the correct punctuation and connectives:",
        "expansion_drills": [
            ("The radiators were freezing. The boiler pilot light had gone out.", "The radiators were freezing because the boiler pilot light had gone out."),
            ("The engineer fixed the pipe. He tested the radiators.", "The engineer fixed the pipe and tested the radiators.")
        ]
    },
    # Page 67: Workout 5
    {
        "page_num": 67,
        "title": "Mixed SPaG Workout 5: Hospitality & Food Hygiene Briefing",
        "scenario": "A head chef wrote this kitchen preparation and food hygiene briefing before a busy weekend dinner service. Identify all 7 SPaG errors and complete the sentence structure drills.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
KITCHEN BRIEFING &bull; BELLA VISTA BISTRO<br>
All kitchen staff must wash <strong>there</strong> hands before touching food. 
Marcus prepared forty fresh chicken <strong>sandwichs</strong> for the lunch counter. 
The chef ordered potatoes, carrots, onions <strong>and</strong> garlic from the farm. 
The walk-in fridge <strong>were</strong> inspected at 10:00 and <strong>it's</strong> temperature was perfect. 
<strong>caution</strong>! The soup kettle is extremely hot 
Please serve all lunch orders promptly.
</div>""",
        "errors": [
            "Correct homophone: 'there hands' -> 'their hands'",
            "Correct plural noun ending in -ch: 'sandwichs' -> 'sandwiches'",
            "Add comma in list if needed or ensure correct separator before 'and'",
            "Change plural verb to singular agreement: 'fridge were' -> 'was inspected'",
            "Fix homophone/apostrophe: 'it's temperature' -> 'its temperature'",
            "Capitalise hazard warning: 'caution' -> 'Caution!'",
            "Add exclamation mark to warning: 'extremely hot!'"
        ],
        "expansion_prompt": "Complete the food hygiene sentences with correct past tense verbs:",
        "expansion_drills": [
            ("Yesterday, the kitchen porter (mop) ____________ the floor and (empty) ____________ the bins.", "Yesterday, the kitchen porter mopped the floor and emptied the bins."),
            ("The head chef (see) ____________ the delivery and (give) ____________ the driver a receipt.", "The head chef saw the delivery and gave the driver a receipt.")
        ]
    },
    # Page 68: Workout 6
    {
        "page_num": 68,
        "title": "Mixed SPaG Workout 6: Office Administration & Visitor Protocol",
        "scenario": "An office manager circulated this visitor registration policy to all administrative staff. Correct all 7 deliberate errors and practice sentence combining.",
        "text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
ADMINISTRATIVE DIRECTIVE &bull; HEAD OFFICE<br>
When a visitor arrives at reception, <strong>i</strong> ask them to sign the guest register. 
Every visitor must wear a security badge <strong>cos</strong> site safety is essential. 
Yesterday, <strong>mr davies</strong> visited our IT department on <strong>church lane</strong>. 
He <strong>taked</strong> the visitor lanyard and returned it at 17:00. 
<strong>all</strong> contractors <strong>is</strong> required to follow this official protocol.
</div>""",
        "errors": [
            "Capitalise standalone pronoun: 'i' -> 'I'",
            "Replace slang with standard connective: 'cos' -> 'because'",
            "Capitalise formal title and surname: 'mr davies' -> 'Mr Davies'",
            "Capitalise street proper noun: 'church lane' -> 'Church Lane'",
            "Change non-standard 'taked' to irregular past tense: 'took'",
            "Capitalise sentence starter: 'all' -> 'All contractors'",
            "Change singular verb to plural agreement: 'contractors is' -> 'are required'"
        ],
        "expansion_prompt": "Join the clauses into complete, polished sentences:",
        "expansion_drills": [
            ("The visitor signed the register. The receptionist handed over the security pass.", "The visitor signed the register and the receptionist handed over the security pass."),
            ("The meeting ended at four. The clients stayed for tea.", "The meeting ended at four, but the clients stayed for tea.")
        ]
    }
]

WRITING_TASKS_PAGES = [
    # Page 69: Task 1
    {
        "page_num": 69,
        "task_num": 1,
        "title": "Writing Task 1: Workplace Email Requesting Annual Leave / Shift Swap",
        "format": "Internal Workplace Email",
        "scenario": "You need to request three days of annual leave next month (or swap a weekend shift with a colleague) to attend a family wedding in Manchester. Write a short, formal email to your line manager, Mrs Jenkins.",
        "criteria": [
            "Include a professional subject line and formal greeting (e.g. <em>Dear Mrs Jenkins,</em>).",
            "State the exact dates and the reason for your request using the connective <em>because</em>.",
            "Explain how your shift duties will be covered (e.g. <em>Marcus has agreed to cover my shift...</em>).",
            "Use correct capital letters for 'I', names, days of the week, and months."
        ],
        "template_lines": 8
    },
    # Page 70: Task 2
    {
        "page_num": 70,
        "task_num": 2,
        "title": "Writing Task 2: Official Workplace Incident Report Form",
        "format": "Health & Safety Incident Report Form",
        "scenario": "You are working in a warehouse or store. At 10:30 on Monday morning, a colleague tripped over a loose cable in corridor B. Complete the official incident report form explaining what happened and what action was taken.",
        "criteria": [
            "Complete the incident details: Date, Time, Location, and Staff Member Involved.",
            "Write two complete sentences describing the incident using regular and irregular past tense verbs (e.g. <em>tripped, fell, saw, helped</em>).",
            "Write one sentence explaining the action taken using the connective <em>so</em>.",
            "Check all sentence boundaries with full stops and capital letters."
        ],
        "template_lines": 8
    },
    # Page 71: Task 3
    {
        "page_num": 71,
        "task_num": 3,
        "title": "Writing Task 3: Customer Service Enquiry Reply Note",
        "format": "Customer Service Message / Reply Slip",
        "scenario": "A customer, Mr Robert Clarke, sent an enquiry asking why his parcel delivery was delayed. Write a polite customer service reply note explaining the delay and confirming when the parcel will arrive.",
        "criteria": [
            "Use a polite greeting (e.g. <em>Dear Mr Clarke,</em>) and formal sign-off.",
            "Explain the reason for the delay using <em>because</em> (e.g. bad weather or vehicle breakdown).",
            "Confirm the new delivery day and time using correct capital letters for days and months.",
            "Include a list of items inside the parcel separated by commas (e.g. <em>two shirts, one jacket and shoes</em>)."
        ],
        "template_lines": 8
    },
    # Page 72: Task 4
    {
        "page_num": 72,
        "task_num": 4,
        "title": "Writing Task 4: New Colleague Welcome & Daily Induction Guide",
        "format": "New Staff Induction Note",
        "scenario": "A new trainee is joining your team next Monday. Write a friendly, professional welcome note explaining three daily routines they must follow on shift.",
        "criteria": [
            "Greet the new colleague by name and welcome them to the company.",
            "Describe three daily routines using present tense verbs (e.g. <em>sign, check, wear, clean</em>).",
            "Include a list of required safety equipment using commas correctly (e.g. <em>safety boots, high-vis vest and gloves</em>).",
            "End with an encouraging sentence and your name."
        ],
        "template_lines": 8
    },
    # Page 73: Task 5
    {
        "page_num": 73,
        "task_num": 5,
        "title": "Writing Task 5: Maintenance & Equipment Fault Repair Request",
        "format": "Facilities Work Order Ticket",
        "scenario": "The commercial dishwasher in the staff canteen (or the conveyor belt in the warehouse) has broken down. Write a maintenance repair request note to the facilities supervisor, Mr Taylor.",
        "criteria": [
            "State the exact location of the equipment and what fault occurred.",
            "Use past tense verbs to describe what happened (e.g. <em>stopped, leaked, failed</em>).",
            "Explain what safety action you took immediately using <em>so</em> or <em>because</em>.",
            "Ask a polite question about when the repair will be completed, using a question mark (?)."
        ],
        "template_lines": 8
    },
    # Page 74: Task 6
    {
        "page_num": 74,
        "task_num": 6,
        "title": "Writing Task 6: College Course / Vocational Enrolment Statement",
        "format": "Enrolment Application Personal Statement",
        "scenario": "You are applying for an Entry Level 3 or Level 1 Functional Skills English / Vocational training course at Leeds City College. Complete the personal statement box explaining why you want to take the course and your future career goals.",
        "criteria": [
            "Complete applicant identity details with capital letters: Full Name, Address, and Postcode.",
            "Write three complete sentences explaining your reasons for applying using <em>because</em> and <em>so</em>.",
            "Mention past experience using the past tense (e.g. <em>I worked, I completed, I learned</em>).",
            "Check that every 'I' stands tall as a capital letter and every sentence ends with a full stop."
        ],
        "template_lines": 8
    }
]
