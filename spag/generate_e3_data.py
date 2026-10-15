#!/usr/bin/env python3
"""
generate_e3_data.py
Creates the comprehensive data file spag_data_e3_84p.py containing:
- Theme & Diagnostic Assessment (24 Qs)
- 24 Units (Complete 2-page spreads: Left theory + Right 4-tier drills)
- 8 Pages of Phonics Rules & Master Word Banks
- 6 Pages of Mixed Proofreading Workouts
- 6 Pages of Practical Workplace Writing Tasks
- 6 Pages of Explanatory Answer Keys
- 1 Page of Candidate Self-Audit Checklist
"""

import sys
import os

units_data = [
    # -------------------------------------------------------------
    # UNIT 1
    # -------------------------------------------------------------
    {
        "unit": 1,
        "title": "Capital Letters for 'I', Personal Names & Titles",
        "subtitle": "Enrolment Forms, Staff ID Badges & Official Correspondence",
        "format": "Staff Sign-in & Visitor Registration",
        "anchor_title": "Official Identity & Workplace Registration",
        "anchor_text": "Whenever you sign in at a workplace reception, register for a vocational qualification, or send an official email to a supervisor, names and titles identify exactly who you are. Missing capital letters on names or writing the word 'i' in lowercase makes your writing appear careless and unprofessional.",
        "formula_title": "Core Syntax Architecture: 4 Rules for Capital Letters",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[1] Pronoun 'I'</span>
  <span>+</span>
  <span class="fpill fpill-verb">[2] Formal Titles (Mr, Mrs, Ms, Dr)</span>
  <span>+</span>
  <span class="fpill fpill-clause">[3] First Names</span>
  <span>+</span>
  <span class="fpill fpill-clause">[4] Surnames</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>The Personal Pronoun 'I':</strong> Always capitalised when standing alone (e.g. <em>"Today <strong>I</strong> completed my induction."</em> &mdash; never a small 'i').</li>
  <li><strong>Formal Titles:</strong> Capitalise abbreviations for people's titles (<em><strong>M</strong>r Green, <strong>M</strong>rs Patel, <strong>M</strong>s Davies, <strong>D</strong>r Ahmed</em>).</li>
  <li><strong>First Names &amp; Surnames:</strong> Every person's proper name begins with an uppercase letter (<em><strong>J</strong>ames <strong>W</strong>ilson, <strong>F</strong>atima <strong>B</strong>egum</em>).</li>
</ul>
""",
        "pitfall_text": "yesterday i met mr hassan and we signed the training contract.",
        "model_text": "Yesterday, I met Mr Hassan and we signed the training contract.",
        "why_text": "'Yesterday' starts the sentence; 'I' is the standalone pronoun; 'Mr' is a title; 'Hassan' is a surname. All require capital letters.",
        "golden_rule": "THE 'I' STAND-TALL RULE: Whenever you write about yourself, 'I' must stand as tall as a skyscraper! Titles like Mr, Mrs, and Dr are official badges&mdash;always give them a capital letter too.",
        "exercise_a": [
            ("Which sentence capitalises the personal pronoun 'I' correctly?",
             ["A) When i finish my shift, i wash my hands.", "B) When I finish my shift, I wash my hands.", "C) When I finish my shift, i wash my hands."], "B"),
            ("Which personal name and title is written correctly for an ID badge?",
             ["A) dr susan clarke", "B) Dr Susan Clarke", "C) Dr susan Clarke"], "B"),
            ("Which sentence contains zero capital letter errors?",
             ["A) Last week, I shadowed Mr David Taylor at the distribution depot.", "B) Last week, i shadowed Mr david taylor at the distribution depot.", "C) Last week, I shadowed mr David Taylor at the distribution depot."], "A"),
            ("Where is the capital letter error in this sentence: <em>'Before lunch, i delivered the package to Ms Jenkins.'</em>",
             ["A) 'lunch' should have a capital", "B) 'i' must be a capital 'I'", "C) 'Ms' should be lowercase"], "B")
        ],
        "exercise_b": [
            ("Correct the lowercase 'i' and title", "last monday i reported to mr evans for my health and safety briefing.", "Last Monday, I reported to Mr Evans for my health and safety briefing."),
            ("Capitalise the full name and title", "please hand this visitor pass to mrs fatima ali at reception.", "Please hand this visitor pass to Mrs Fatima Ali at reception."),
            ("Fix all 3 name and pronoun errors", "when i called dr patel, i explained the situation clearly.", "When I called Dr Patel, I explained the situation clearly.")
        ],
        "proofreading_title": "Workplace Visitor & Staff Registration Log",
        "proofreading_scenario": "A new trainee completed this shift handover log. Identify and correct all 5 capital letter errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
LOG DATE: 14 October 2026<br>
NOTES: At 08:30, <strong>i</strong> arrived at the staff entrance and greeted <strong>mr</strong> cooper. 
We reviewed the morning delivery manifest together. Later that morning, <strong>i</strong> assisted 
<strong>ms sarah taylor</strong> with the client files in office 3. All visitor passes were returned on time.
</div>""",
        "proofreading_errors": [
            "Change lowercase 'i' to capital 'I' ('At 08:30, I arrived...')",
            "Capitalise formal title 'mr' -> 'Mr Cooper'",
            "Change second lowercase 'i' to capital 'I' ('Later that morning, I assisted...')",
            "Capitalise title 'ms' -> 'Ms'",
            "Capitalise first name and surname 'sarah taylor' -> 'Sarah Taylor'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> introducing yourself and a supervisor for a workplace identity profile. Include your full name, your supervisor's title and surname (e.g. Mrs Evans or Mr Khan), and use the pronoun 'I' at least twice."
    },

    # -------------------------------------------------------------
    # UNIT 2
    # -------------------------------------------------------------
    {
        "unit": 2,
        "title": "Capital Letters for Places, Days of Week & Months",
        "subtitle": "Booking Shifts, Scheduling Deliveries & Travel Itineraries",
        "format": "Shift Rota & Training Schedule",
        "anchor_title": "Scheduling Shift Calendars & Regional Logistics",
        "anchor_text": "Shift rotas, training calendars, and delivery manifests rely on specific dates and geographical locations. If you write 'monday' or 'birmingham' in lowercase, official scheduling software and team rotas look untidy and are prone to misinterpretation.",
        "formula_title": "Core Syntax Architecture: The Calendar & Map Framework",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[1] Days of the Week</span>
  <span>+</span>
  <span class="fpill fpill-verb">[2] Months of the Year</span>
  <span>+</span>
  <span class="fpill fpill-conn">[3] Towns, Cities &amp; Countries</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Days of the Week:</strong> Always capitalised: <em><strong>M</strong>onday, <strong>T</strong>uesday, <strong>W</strong>ednesday, <strong>T</strong>hursday, <strong>F</strong>riday, <strong>S</strong>aturday, <strong>S</strong>unday</em>.</li>
  <li><strong>Months of the Year:</strong> Always capitalised: <em><strong>J</strong>anuary, <strong>F</strong>ebruary, <strong>M</strong>arch, <strong>A</strong>pril, <strong>M</strong>ay, <strong>J</strong>une, <strong>J</strong>uly, <strong>A</strong>ugust, <strong>S</strong>eptember, <strong>O</strong>ctober, <strong>N</strong>ovember, <strong>D</strong>ecember</em>.</li>
  <li><strong>Specific Places:</strong> Towns, cities, and countries: <em><strong>L</strong>eeds, <strong>M</strong>anchester, <strong>B</strong>ristol, <strong>S</strong>cotland, <strong>E</strong>ngland</em>.</li>
</ul>
""",
        "pitfall_text": "our new branch opens on friday in leeds during september.",
        "model_text": "Our new branch opens on Friday in Leeds during September.",
        "why_text": "'Friday' is a day of the week, 'Leeds' is a city, and 'September' is a calendar month. All must have capital letters.",
        "golden_rule": "THE CALENDAR & MAP RULE: If you can flip to it on a wall calendar (Days, Months) or locate it on a UK road map (Towns, Cities, Countries), it always gets a capital letter.",
        "exercise_a": [
            ("Which day of the week is capitalised correctly?",
             ["A) wednesday", "B) Wednesday", "C) wednesDay"], "B"),
            ("Which sentence contains no errors with calendar months?",
             ["A) The factory shuts down for maintenance in August.", "B) The factory shuts down for maintenance in august.", "C) The factory shuts down for maintenance in AUGUST only."], "A"),
            ("Which sentence capitalises both the city and the day correctly?",
             ["A) The regional manager travels to london every Tuesday.", "B) The regional manager travels to London every tuesday.", "C) The regional manager travels to London every Tuesday."], "C"),
            ("Identify the correctly punctuated sentence:",
             ["A) On Thursday, 12 October, our team relocates to Cardiff.", "B) On thursday, 12 october, our team relocates to cardiff.", "C) On Thursday, 12 october, our team relocates to Cardiff."], "A")
        ],
        "exercise_b": [
            ("Capitalise the day and city", "the team meeting takes place every wednesday at our office in liverpool.", "The team meeting takes place every Wednesday at our office in Liverpool."),
            ("Capitalise the month and day", "our fire evacuation drill is scheduled for the first tuesday in november.", "Our fire evacuation drill is scheduled for the first Tuesday in November."),
            ("Fix all place and date errors", "we sent three delivery vans to sheffield on monday morning.", "We sent three delivery vans to Sheffield on Monday morning.")
        ],
        "proofreading_title": "Regional Warehouse Logistics Bulletin",
        "proofreading_scenario": "This logistics bulletin has 5 errors involving days, months, and place names. Find and correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
TO: All Depot Drivers<br>
Starting on <strong>monday</strong> morning, all regional deliveries to <strong>bristol</strong> 
will depart from bay 4. During the month of <strong>november</strong>, extra freight loads 
will be dispatched to <strong>newcastle</strong>. Please submit your holiday requests for 
<strong>december</strong> before this Friday afternoon.
</div>""",
        "proofreading_errors": [
            "Capitalise day of the week: 'monday' -> 'Monday'",
            "Capitalise city name: 'bristol' -> 'Bristol'",
            "Capitalise calendar month: 'november' -> 'November'",
            "Capitalise city name: 'newcastle' -> 'Newcastle'",
            "Capitalise calendar month: 'december' -> 'December'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> explaining your working schedule for a new job. Name the day of the week you start (e.g. Monday), the month (e.g. November), and the city where your depot or office is located (e.g. Birmingham)."
    },

    # -------------------------------------------------------------
    # UNIT 3
    # -------------------------------------------------------------
    {
        "unit": 3,
        "title": "Capital Letters for Brand Names, Street Names & Postcodes",
        "subtitle": "Delivery Waybills, Supplier Invoices & Customer Addresses",
        "format": "Parcel Delivery Waybill & Address Label",
        "anchor_title": "Despatch Addresses & Courier Labels",
        "anchor_text": "In postal deliveries and retail operations, addresses must be 100% accurate. Royal Mail sorters and delivery drivers rely on capital letters to distinguish street names, commercial brands, and alphanumeric postal codes. Lowercase postcodes can cause severe delivery delays.",
        "formula_title": "Core Syntax Architecture: The Commercial Address Formula",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[1] Brand / Company Name</span>
  <span>+</span>
  <span class="fpill fpill-verb">[2] Number &amp; Street Name</span>
  <span>+</span>
  <span class="fpill fpill-conn">[3] UK Postcode (Full Caps)</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Brand &amp; Company Names:</strong> Official trading names need capitals: <em><strong>T</strong>esco, <strong>A</strong>sda, <strong>A</strong>mazon, <strong>S</strong>amsung, <strong>B</strong>&amp;<strong>Q</strong></em>.</li>
  <li><strong>Street &amp; Road Names:</strong> Both the name and the road type: <em><strong>H</strong>igh <strong>S</strong>treet, <strong>O</strong>xford <strong>R</strong>oad, <strong>K</strong>ing's <strong>A</strong>venue, <strong>C</strong>hurch <strong>L</strong>ane</em>.</li>
  <li><strong>UK Postal Codes:</strong> Always written in block uppercase letters: <em><strong>B</strong>1 1<strong>TT</strong>, <strong>M</strong>4 5<strong>BD</strong>, <strong>SW</strong>1<strong>A</strong> 1<strong>AA</strong>, <strong>LS</strong>2 8<strong>JT</strong></em>.</li>
</ul>
""",
        "pitfall_text": "deliver the parcel to boots pharmacy on london road, b1 2aa.",
        "model_text": "Deliver the parcel to Boots Pharmacy on London Road, B1 2AA.",
        "why_text": "'Boots Pharmacy' is a brand, 'London Road' is a proper street name, and 'B1 2AA' is an official UK postcode. All require capital letters.",
        "golden_rule": "THE ROYAL MAIL RULE: Commercial brands, named streets, and UK postcodes are legal postal coordinates. Write company names in title case and postcodes in full BLOCK CAPITALS.",
        "exercise_a": [
            ("Which address displays the street name with correct capitals?",
             ["A) 45 Victoria road", "B) 45 victoria road", "C) 45 Victoria Road"], "C"),
            ("Which UK postcode is formatted correctly in uppercase letters?",
             ["A) m1 4et", "B) M1 4ET", "C) M1 4et"], "B"),
            ("Which company and brand name is capitalised correctly?",
             ["A) sainsbury's supermarket", "B) Sainsbury's Supermarket", "C) Sainsbury's supermarket"], "B"),
            ("Identify the address label that is 100% error-free:",
             ["A) Argos Distribution, 12 Industrial Way, Coventry, CV1 3FZ", "B) argos Distribution, 12 industrial way, Coventry, cv1 3fz", "C) Argos distribution, 12 Industrial way, Coventry, CV1 3fz"], "A")
        ],
        "exercise_b": [
            ("Capitalise the store brand and road", "we collected the spare parts from screwfix on station road.", "We collected the spare parts from Screwfix on Station Road."),
            ("Capitalise the street name and postcode", "please send the invoice to 28 park lane, leeds, ls1 4hy.", "Please send the invoice to 28 Park Lane, Leeds, LS1 4HY."),
            ("Fix all brand, street, and postcode errors", "the delivery van stopped at morrisons on queen street, m60 2la.", "The delivery van stopped at Morrisons on Queen Street, M60 2LA.")
        ],
        "proofreading_title": "Courier Despatch Consignment Slip",
        "proofreading_scenario": "A despatch clerk wrote this parcel routing instruction with 5 capital letter errors. Find and correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
PARCEL ROUTING SLIP &bull; CONSIGNMENT #88219<br>
CONSIGNEE: <strong>marks &amp; spencer</strong> Logistics Centre<br>
ADDRESS: Unit 4, <strong>green lane</strong> Trading Estate<br>
TOWN: Derby<br>
POSTCODE: <strong>de21 4aw</strong><br>
SPECIAL INSTRUCTIONS: Collect returns for <strong>dhl express</strong> before 16:00.
</div>""",
        "proofreading_errors": [
            "Capitalise brand name: 'marks & spencer' -> 'Marks & Spencer'",
            "Capitalise street name: 'green lane' -> 'Green Lane'",
            "Capitalise postcode letters: 'de21 4aw' -> 'DE21 4AW'",
            "Capitalise brand name: 'dhl' -> 'DHL'",
            "Capitalise brand name: 'express' -> 'Express'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> confirming where you bought work equipment or where a parcel was dispatched. Include a specific shop or brand name (e.g. Screwfix or B&Q), a street name (e.g. High Street), and a UK postcode in block capitals."
    },

    # -------------------------------------------------------------
    # UNIT 4
    # -------------------------------------------------------------
    {
        "unit": 4,
        "title": "Full Stops — Ending a Complete Thought",
        "subtitle": "Daily Handover Notes, Maintenance Tickets & Incident Logs",
        "format": "Security Guard Handover Log",
        "anchor_title": "Marking Clear Sentence Boundaries in Shift Reports",
        "anchor_text": "In workplace incident logs and daily handover emails, information must be distinct and easy to read. If you let sentences run into each other without full stops, supervisors cannot tell where one action ended and the next action began. A full stop signals that a complete thought has finished.",
        "formula_title": "Core Syntax Architecture: The Complete Thought Cycle",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-punct">[Capital Letter]</span>
  <span>+</span>
  <span class="fpill fpill-subj">Subject (Who / What)</span>
  <span>+</span>
  <span class="fpill fpill-verb">Predicate Verb (Action)</span>
  <span>+</span>
  <span class="fpill fpill-punct">Full Stop [ . ]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Complete Thought Requirement:</strong> A sentence must make sense on its own. It tells the reader who did what.</li>
  <li><strong>The Sentence Boundary:</strong> Place the full stop firmly at the end of the thought. Do NOT put a comma where a full stop is needed.</li>
  <li><strong>The Reset:</strong> Every full stop must be followed immediately by a space and a capital letter for the next sentence.</li>
</ul>
""",
        "pitfall_text": "the security guard checked the perimeter fence he found no damage.",
        "model_text": "The security guard checked the perimeter fence. He found no damage.",
        "why_text": "These are two separate complete actions. Leaving out the full stop creates a confusing run-on sentence.",
        "golden_rule": "THE TRAFFIC LIGHT RULE: A full stop is a red traffic light for your reader's brain. When your complete idea finishes, stop completely (.), take a breath, and start the next idea with a green-light capital letter.",
        "exercise_a": [
            ("Which sentence boundary is punctuated correctly?",
             ["A) The warehouse heater failed the room was freezing.", "B) The warehouse heater failed. The room was freezing.", "C) The warehouse heater failed the room. Was freezing."], "B"),
            ("Where should the full stop be placed in this statement?",
             ["A) After 'van': <em>'Liam loaded the delivery van he locked the rear doors.'</em>", "B) After 'delivery': <em>'Liam loaded the delivery. Van he locked the rear doors.'</em>", "C) After 'doors': only at the very end with no middle stop."], "A"),
            ("Which option shows two complete, correctly separated sentences?",
             ["A) The cleaner mopped the reception floor. Customers waited outside.", "B) The cleaner mopped the reception floor customers waited outside.", "C) The cleaner mopped the reception floor, customers waited outside."], "A"),
            ("Identify the complete sentence that needs no extra punctuation:",
             ["A) Because the printer was out of black ink toner.", "B) The technician replaced the printer toner cartridge yesterday.", "C) Replacing the printer toner cartridge in the office."], "B")
        ],
        "exercise_b": [
            ("Insert the missing full stop and capital letter", "the forklift driver stacked the pallets he moved to aisle six.", "The forklift driver stacked the pallets. He moved to aisle six."),
            ("Split into two correct sentences", "the fire alarm sounded at ten staff evacuated calmly.", "The fire alarm sounded at ten. Staff evacuated calmly."),
            ("Punctuate the handover note", "we locked the main warehouse gates the night guard arrived.", "We locked the main warehouse gates. The night guard arrived.")
        ],
        "proofreading_title": "Security Desk Night Shift Handover Log",
        "proofreading_scenario": "This security log is missing full stops and capital letters, causing run-on sentences. Correct all 5 sentence boundary errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
SHIFT REPORT &bull; BUILDING B<br>
At 22:00, officer Davies patrolled the ground floor <strong>all</strong> fire exit doors 
were fully secured. The motion sensor in corridor 3 was activated by a cat 
<strong>the</strong> officer reset the alarm immediately. At 04:00, the bakery delivery van arrived 
<strong>the</strong> driver signed the visitor register. Morning staff arrived at 06:00 
<strong>the</strong> shift completed without incident.
</div>""",
        "proofreading_errors": [
            "Insert full stop after 'floor' and capitalise: 'floor. All fire exit doors...'",
            "Insert full stop after 'cat' and capitalise: 'cat. The officer reset...'",
            "Insert full stop after 'arrived' and capitalise: 'arrived. The driver signed...'",
            "Insert full stop after '06:00' and capitalise: '06:00. The shift completed...'",
            "Ensure final sentence ends with a full stop: 'without incident.'"
        ],
        "writing_prompt": "Write <strong>two separate sentences</strong> reporting two actions you completed during a workplace shift (e.g. cleaning a workspace, packing an order, or checking equipment). Make sure each sentence starts with a capital letter and ends with a full stop."
    },

    # -------------------------------------------------------------
    # UNIT 5
    # -------------------------------------------------------------
    {
        "unit": 5,
        "title": "Question Marks — Asking for Help & Information",
        "subtitle": "Customer Enquiries, IT Helpdesk Tickets & Supervisor Clarifications",
        "format": "Customer Service Helpdesk Ticket",
        "anchor_title": "Asking for Workplace Clarification & Client Assistance",
        "anchor_text": "In team communications and customer service emails, you frequently need to request assistance or ask customers for details. A question mark (?) tells the reader that an answer is expected. If you put a full stop on a question, your reader may not realise they need to reply.",
        "formula_title": "Core Syntax Architecture: The Question Inversion Pattern",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-conn">Question Starter</span>
  <span>+</span>
  <span class="fpill fpill-subj">Subject</span>
  <span>+</span>
  <span class="fpill fpill-verb">Action Verb</span>
  <span>+</span>
  <span class="fpill fpill-punct">Question Mark [ ? ]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>The '5W + 1H' Starters:</strong> <em><strong>W</strong>ho, <strong>W</strong>hat, <strong>W</strong>here, <strong>W</strong>hen, <strong>W</strong>hy, <strong>H</strong>ow</em>.</li>
  <li><strong>Modal &amp; Auxiliary Starters:</strong> <em><strong>C</strong>an, <strong>C</strong>ould, <strong>W</strong>ould, <strong>D</strong>o, <strong>D</strong>oes, <strong>I</strong>s, <strong>A</strong>re</em>.</li>
  <li><strong>Golden Grammar Rule:</strong> Never put a question mark on a plain statement of fact (e.g. <em>"I wonder if it will rain today."</em> &mdash; this is a statement, not a question).</li>
</ul>
""",
        "pitfall_text": "could you send me the updated stock catalogue.",
        "model_text": "Could you send me the updated stock catalogue?",
        "why_text": "'Could you send...' is a direct request asking someone to take action and reply. It requires a question mark at the end.",
        "golden_rule": "THE LISTENING EAR RULE: A question mark looks like a curved human ear with a dot underneath. If your sentence is listening for an answer or expecting a reply, it must wear a question mark (?).",
        "exercise_a": [
            ("Which of these sentences is a question that requires a question mark?",
             ["A) The staff meeting begins at two o'clock.", "B) What time does the staff meeting begin", "C) I will attend the staff meeting at two o'clock."], "B"),
            ("Which sentence is punctuated correctly?",
             ["A) Can you help me lift this heavy crate?", "B) Can you help me lift this heavy crate.", "C) Can you help me lift this heavy crate!"], "A"),
            ("Which sentence should NOT have a question mark?",
             ["A) Where is the nearest fire assembly point?", "B) How do I reset my computer password?", "C) The manager explained how to reset the password?"], "C"),
            ("Identify the correct enquiry to a supervisor:",
             ["A) Would it be possible to swap my Saturday shift with Marcus?", "B) Would it be possible to swap my Saturday shift with Marcus.", "C) If I can swap my Saturday shift with Marcus."], "A")
        ],
        "exercise_b": [
            ("Punctuate the customer enquiry", "what is the delivery charge for parcels over ten kilograms", "What is the delivery charge for parcels over ten kilograms?"),
            ("Punctuate the IT support question", "could you please unlock my user account before noon", "Could you please unlock my user account before noon?"),
            ("Turn this statement into a question", "You know where the first aid box is located.", "Do you know where the first aid box is located?")
        ],
        "proofreading_title": "IT Helpdesk & Equipment Enquiry Message",
        "proofreading_scenario": "A colleague typed this email to IT support. It contains 5 punctuation errors with questions and statements. Locate and fix all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
FROM: a.jones@company.co.uk<br>
TO: it-support@company.co.uk<br>
SUBJECT: Login Assistance<br>
Hello Support Team,<br>
I am unable to access the warehouse inventory portal this morning<strong>?</strong> 
<strong>could</strong> you please reset my network password<strong>.</strong> 
Also, <strong>where</strong> can I collect my new security key fob<strong>.</strong> 
Thank you for your assistance.
</div>""",
        "proofreading_errors": [
            "Remove incorrect question mark on statement: 'morning.' (not '?')",
            "Capitalise question starter: 'could' -> 'Could'",
            "Add question mark to direct request: 'network password?' (replace '.')",
            "Capitalise question word: 'where' -> 'Where'",
            "Add question mark to enquiry: 'key fob?' (replace '.')"
        ],
        "writing_prompt": "Write <strong>two complete question sentences</strong> asking a supervisor or customer service desk for information. Start one question with <em>'Could you...'</em> and the other with <em>'Where is...'</em>. Ensure both end with a question mark."
    },

    # -------------------------------------------------------------
    # UNIT 6
    # -------------------------------------------------------------
    {
        "unit": 6,
        "title": "Exclamation Marks — Warnings, Safety & Urgent Notices",
        "subtitle": "Health & Safety Notices, Emergency Signs & Critical Alerts",
        "format": "Factory Health & Safety Warning Poster",
        "anchor_title": "Urgent Health & Safety Alerts on Site",
        "anchor_text": "In industrial sites, kitchens, care homes, and construction environments, safety alerts protect workers from severe harm. An exclamation mark (!) gives a word or sentence urgent vocal force and signals danger. In professional writing, use them sparingly—never use more than one at a time.",
        "formula_title": "Core Syntax Architecture: The Urgent Safety Imperative",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-punct">[Capital Letter]</span>
  <span>+</span>
  <span class="fpill fpill-verb">Urgent Command / Hazard Warning</span>
  <span>+</span>
  <span class="fpill fpill-punct">Exclamation Mark [ ! ]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Immediate Danger Alerts:</strong> Single hazard words: <em><strong>D</strong>anger! <strong>C</strong>aution! <strong>W</strong>arning! <strong>S</strong>top!</em></li>
  <li><strong>Urgent Imperative Commands:</strong> Direct orders to prevent injury: <em><strong>E</strong>vacuate the building immediately!</em></li>
  <li><strong>The Workplace Golden Rule:</strong> Never use multiple exclamation marks (e.g. <em>'Danger!!!'</em>). One firm exclamation mark provides maximum legal clarity.</li>
</ul>
""",
        "pitfall_text": "fire exit blocked please clear it immediately???",
        "model_text": "Warning! The fire exit is blocked. Please clear it immediately!",
        "why_text": "Safety warnings require a single authoritative exclamation mark. Multiple question marks or exclamation marks look unprofessional and hysterical.",
        "golden_rule": "THE EMERGENCY BRAKE RULE: An exclamation mark is like an emergency brake in a vehicle. Use it ONLY when there is genuine danger, an urgent hazard, or a critical command. One mark is powerful; three marks is careless.",
        "exercise_a": [
            ("Which sentence is an urgent warning punctuated correctly?",
             ["A) Watch out for the wet floor.", "B) Watch out for the wet floor!", "C) Watch out for the wet floor?"], "B"),
            ("Which sign uses an exclamation mark appropriately?",
             ["A) Danger! High voltage electrical equipment inside.", "B) Danger? High voltage electrical equipment inside.", "C) Danger. High voltage electrical equipment inside."], "A"),
            ("How many exclamation marks should be used on an official notice?",
             ["A) Exactly three (!!!) to make people pay attention.", "B) Exactly one (!) for clear professional emphasis.", "C) As many as will fit on the poster banner."], "B"),
            ("Which of these routine workplace emails should NOT use an exclamation mark?",
             ["A) 'Caution! Hot steam valve!'", "B) 'Stop the conveyor belt at once!'", "C) 'The weekly sales report is attached!'"], "C")
        ],
        "exercise_b": [
            ("Turn into an urgent safety warning", "caution hot surfaces in this bakery area", "Caution! Hot surfaces in this bakery area!"),
            ("Correct the informal punctuation", "do not enter without eye protection goggles!!!", "Do not enter without eye protection goggles!"),
            ("Punctuate the emergency fire command", "sound the alarm and leave the building immediately", "Sound the alarm and leave the building immediately!")
        ],
        "proofreading_title": "Commercial Kitchen Health & Safety Poster",
        "proofreading_scenario": "A catering assistant drafted this kitchen safety poster. Correct all 5 punctuation and capitalisation errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
KITCHEN SAFETY DIRECTIVE &bull; STATION 4<br>
1. <strong>danger</strong>! Do not touch the deep fryer heating elements<strong>!!!</strong><br>
2. <strong>caution</strong>! Hot cooking oil causes severe burns<strong>?</strong><br>
3. In case of fire, pull the emergency power switch <strong>immediately</strong>.
</div>""",
        "proofreading_errors": [
            "Capitalise hazard word: 'danger' -> 'Danger!'",
            "Replace multiple marks '!!!' with single full stop or mark: 'elements.'",
            "Capitalise warning word: 'caution' -> 'Caution!'",
            "Replace incorrect question mark on warning: 'burns!' (not '?')",
            "Add exclamation mark to emergency command: 'immediately!'"
        ],
        "writing_prompt": "Write <strong>two short safety warning sentences</strong> for a workplace environment (such as a warehouse, care home, or workshop). Use one single hazard word ending with an exclamation mark (e.g. <em>'Caution!'</em>) and one urgent instruction."
    },

    # -------------------------------------------------------------
    # UNIT 7
    # -------------------------------------------------------------
    {
        "unit": 7,
        "title": "Simple Sentences — Subject, Verb, Object (SVO)",
        "subtitle": "Clear Workplace Documentation, Stock Logs & Maintenance Reports",
        "format": "Stockroom Inventory Inspection Note",
        "anchor_title": "Building Strong, Clear Sentences in the Workplace",
        "anchor_text": "Every professional report is built from simple sentences. If your sentence is missing a subject (who or what did it) or missing a verb (the action), it becomes an incomplete fragment. Writing clear Subject + Verb + Object (SVO) sentences ensures colleagues understand your reports instantly.",
        "formula_title": "Core Syntax Architecture: The SVO Sentence Engine",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[1] Subject (Who/What)</span>
  <span>+</span>
  <span class="fpill fpill-verb">[2] Verb (Action/State)</span>
  <span>+</span>
  <span class="fpill fpill-clause">[3] Object / Detail</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>The Subject:</strong> The person, machine, or thing performing the action (e.g. <em>The technician</em>, <em>The alarm</em>).</li>
  <li><strong>The Verb:</strong> The action word or state of being (e.g. <em>repaired</em>, <em>tested</em>, <em>is</em>). Every sentence MUST have a verb.</li>
  <li><strong>The Object / Completer:</strong> The person or thing receiving the action (e.g. <em>the motor</em>, <em>the safety valve</em>).</li>
</ul>
""",
        "pitfall_text": "the new delivery boxes in the corridor outside bay 2.",
        "model_text": "The warehouse assistant stacked the delivery boxes outside bay 2.",
        "why_text": "The pitfall is a fragment because it has no verb. Adding the subject 'assistant' and the verb 'stacked' creates a complete, grammatical sentence.",
        "golden_rule": "THE ENGINE & DRIVER TEST: Every sentence needs a Driver (the Subject) and an Engine (the Verb). If there is no verb engine, your sentence cannot move anywhere!",
        "exercise_a": [
            ("Which of the following is a complete simple sentence with a subject and verb?",
             ["A) Unpacking the fragile glass ornaments in aisle 4.", "B) The stock assistant unpacked the fragile glass ornaments.", "C) In aisle 4 with the fragile glass ornaments."], "B"),
            ("What is the VERB in this sentence: <em>'The driver delivered the medical supplies.'</em>",
             ["A) driver", "B) delivered", "C) supplies"], "B"),
            ("What is the SUBJECT in this sentence: <em>'The maintenance team replaced the broken lightbulb.'</em>",
             ["A) The maintenance team", "B) replaced", "C) the broken lightbulb"], "A"),
            ("Identify the sentence fragment that is missing a verb:",
             ["A) Maya signed the delivery receipt.", "B) Two security officers checked the gate.", "C) All five delivery vans in the depot yard."], "C")
        ],
        "exercise_b": [
            ("Add a subject to complete the sentence", "____________ inspected the fire extinguishers on Tuesday.", "The technician inspected the fire extinguishers on Tuesday."),
            ("Add an action verb to complete the sentence", "The store manager ____________ the main doors at eight o'clock.", "The store manager opened the main doors at eight o'clock."),
            ("Turn this fragment into a full SVO sentence", "The delivery parcel on the reception desk.", "The receptionist placed the delivery parcel on the reception desk.")
        ],
        "proofreading_title": "Daily Facility Maintenance Audit",
        "proofreading_scenario": "A junior maintenance helper wrote these audit notes. Three are broken fragments and two have missing capitals/full stops. Fix all 5 errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
FACILITY AUDIT NOTES &bull; ZONE C<br>
1. <strong>the</strong> cleaner emptied all recycling bins.<br>
2. The plumber <strong>repaired</strong> the leaking pipe in the staff washroom.<br>
3. <strong>two broken chairs in the conference room.</strong><br>
4. Liam <strong>tested</strong> the emergency lighting system yesterday<br>
5. <strong>the electrician replaced the blown fuse.</strong>
</div>""",
        "proofreading_errors": [
            "Capitalise sentence starter: 'the' -> 'The cleaner emptied...'",
            "Note 3 is a fragment missing a verb: change to 'Liam removed two broken chairs from the conference room.'",
            "Add missing full stop to note 4: 'yesterday.'",
            "Capitalise sentence starter in note 5: 'the' -> 'The electrician...'",
            "Ensure note 5 ends with a clear full stop."
        ],
        "writing_prompt": "Write <strong>two simple SVO sentences</strong> about tasks you do at work or college. Identify who does the task (Subject), what action they take (Verb), and what thing is handled (Object). Include full stops and capital letters."
    },

    # -------------------------------------------------------------
    # UNIT 8
    # -------------------------------------------------------------
    {
        "unit": 8,
        "title": "Joining Sentences with 'And' (Adding information)",
        "subtitle": "Order Packing, Process Steps & Daily Task Handover",
        "format": "Retail Shift Task Checklist",
        "anchor_title": "Connecting Related Workplace Tasks Smoothly",
        "anchor_text": "When you report daily tasks, you often perform two related actions together. Instead of writing lots of short, choppy sentences, you can join them smoothly using the connective 'and'. This shows that the two ideas belong together in the same workflow.",
        "formula_title": "Core Syntax Architecture: The Addition Bridge Formula",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[Idea 1: Complete Sentence]</span>
  <span>+</span>
  <span class="fpill fpill-conn">and</span>
  <span>+</span>
  <span class="fpill fpill-verb">[Idea 2: Complete Sentence or Verb]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Adding Information:</strong> 'And' links two ideas of equal importance (e.g. <em>"I sorted the mail <strong>and</strong> I delivered the parcels."</em>).</li>
  <li><strong>Shared Subjects:</strong> If both actions are done by the same person, you can connect the verbs directly (e.g. <em>"Emma swept the floor <strong>and</strong> emptied the bins."</em>).</li>
  <li><strong>The Run-on Warning:</strong> Do not use 'and' more than once in the same sentence. Never write: <em>'I did this and I did that and I went here and...'</em></li>
</ul>
""",
        "pitfall_text": "I checked the delivery and I counted the boxes and I signed the slip and I left.",
        "model_text": "I checked the delivery and I counted the boxes. Then, I signed the slip.",
        "why_text": "Overusing 'and' creates an endless, exhausting run-on sentence. Use 'and' once to join two ideas, then use a full stop.",
        "golden_rule": "THE SINGLE BRIDGE RULE: Think of 'and' as a sturdy footbridge between two islands of thought. Build one bridge per sentence, then finish the crossing with a firm full stop (.).",
        "exercise_a": [
            ("Which sentence joins two related actions correctly with 'and'?",
             ["A) Marcus washed the delivery van and he polished the mirrors.", "B) Marcus washed the delivery van and, and he polished the mirrors.", "C) Marcus washed the delivery van, and, he polished the mirrors."], "A"),
            ("Combine these two sentences using 'and': <em>'Rita answered the phone.'</em> + <em>'Rita took a message.'</em>",
             ["A) Rita answered the phone but took a message.", "B) Rita answered the phone and took a message.", "C) Rita answered the phone, so took a message."], "B"),
            ("Which sentence is an unacceptable run-on sentence?",
             ["A) We loaded the pallets and secured the straps.", "B) We loaded the pallets and secured the straps and drove to Leeds and unloaded.", "C) We loaded the pallets. Then, we secured the straps."], "B"),
            ("Identify the correct compound sentence:",
             ["A) The clinic opens at eight and appointments begin at nine.", "B) The clinic opens at eight, and, appointments begin at nine.", "C) The clinic opens at eight and. Appointments begin at nine."], "A")
        ],
        "exercise_b": [
            ("Join into one sentence with 'and'", "Kavita printed the invoices. Kavita filed them in the cabinet.", "Kavita printed the invoices and filed them in the cabinet."),
            ("Join two complete clauses with 'and'", "The store was busy. The staff worked very hard.", "The store was busy and the staff worked very hard."),
            ("Eliminate the run-on repetition of 'and'", "I cleaned the table and I washed the cups and I dried them.", "I cleaned the table and washed the cups. Then, I dried them.")
        ],
        "proofreading_title": "Warehouse Order Packing Log",
        "proofreading_scenario": "A packing assistant wrote this handover note with 5 errors involving runaway 'and' connections and missing punctuation. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
SHIFT REPORT &bull; DESPATCH BAY<br>
We packed fifty parcels this afternoon <strong>and</strong> and we labelled every box. 
Sam sealed the shipping cartons <strong>and</strong> he stacked them onto pallets 
<strong>and</strong> he wrapped them in plastic film. The courier arrived on time 
<strong>and</strong> he signed the collection manifest 
All freight left depot 4 safely.
</div>""",
        "proofreading_errors": [
            "Remove duplicate connective: 'and and' -> 'and'",
            "Break run-on chain: put a full stop after 'pallets': 'pallets. He wrapped them...'",
            "Remove extra 'and' before 'he wrapped'",
            "Add missing full stop after 'manifest': 'collection manifest.'",
            "Ensure final sentence begins with capital 'All' and ends with full stop."
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> about tasks you do in a workplace or at home. In each sentence, join two related actions using the connective 'and'. Ensure each sentence ends with a full stop."
    },

    # -------------------------------------------------------------
    # UNIT 9
    # -------------------------------------------------------------
    {
        "unit": 9,
        "title": "Joining Sentences with 'But' (Contrasting information)",
        "subtitle": "Reporting Problems, Stock Shortages & Unexpected Delays",
        "format": "Maintenance Fault & Exception Report",
        "anchor_title": "Reporting Exceptions & Contrasting Information",
        "anchor_text": "In workplace reports, things do not always go as planned. You might order twenty uniforms, but only ten arrive. You might check a machine, but find a fault. The connective 'but' signals an unexpected contrast or limitation between two ideas.",
        "formula_title": "Core Syntax Architecture: The Contrast See-Saw",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[Idea 1: Normal / Expected Fact]</span>
  <span>+</span>
  <span class="fpill fpill-conn">, but</span>
  <span>+</span>
  <span class="fpill fpill-clause">[Idea 2: Unexpected Contrast / Problem]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Contrasting Ideas:</strong> 'But' connects two clauses that show an opposite or surprising outcome (e.g. <em>"The alarm sounded, <strong>but</strong> there was no fire."</em>).</li>
  <li><strong>The Comma Signal:</strong> In compound sentences, a small comma before 'but' helps your reader pause before the twist.</li>
  <li><strong>Meaning Contrast:</strong> Never use 'and' when the second fact contradicts the first (e.g. <em>"He applied, <strong>but</strong> was unsuccessful."</em> &mdash; not 'and').</li>
</ul>
""",
        "pitfall_text": "We called the technician three times and he did not answer.",
        "model_text": "We called the technician three times, but he did not answer.",
        "why_text": "Not answering is an unexpected, contrasting problem. The connective 'but' is required to show the contrast.",
        "golden_rule": "THE SEE-SAW RULE: 'But' is a see-saw that tips your sentence in the opposite direction. If the second part of your sentence contradicts or limits the first part, use 'but'!",
        "exercise_a": [
            ("Which sentence correctly uses 'but' to show contrast?",
             ["A) The bus arrived on time, but it was completely full.", "B) The bus arrived on time and it was completely full.", "C) The bus arrived on time so it was completely full."], "A"),
            ("Choose the correct connective: <em>'We searched the whole warehouse, ______ we could not find the missing parcel.'</em>",
             ["A) because", "B) but", "C) and"], "B"),
            ("Which sentence is punctuated correctly?",
             ["A) Tariq passed the practical test, but he failed the theory exam.", "B) Tariq passed the practical test but, he failed the theory exam.", "C) Tariq passed the practical test but he failed, the theory exam."], "A"),
            ("Identify the sentence where 'but' is used incorrectly:",
             ["A) The shop was quiet, but we finished our restocking early.", "B) She loves cooking, but she works as a chef.", "C) I wanted to attend the course, but all tickets were sold out."], "B")
        ],
        "exercise_b": [
            ("Join these sentences using ', but'", "The sun was shining. The morning wind was freezing.", "The sun was shining, but the morning wind was freezing."),
            ("Complete the sentence with a contrasting idea", "We ordered thirty boxed lunches, but _____________________.", "We ordered thirty boxed lunches, but only twenty were delivered."),
            ("Fix the incorrect connective", "The laptop is brand new and the keyboard does not work.", "The laptop is brand new, but the keyboard does not work.")
        ],
        "proofreading_title": "Maintenance Exception & Delay Notification",
        "proofreading_scenario": "A building manager wrote this memo regarding boiler repairs. Correct all 5 connective, punctuation, and capitalisation errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
MEMORANDUM &bull; ESTATES &amp; FACILITIES<br>
The heating engineer arrived at 08:00 <strong>and</strong> he did not have the correct replacement valve. 
We contacted three local plumbing merchants <strong>but</strong> none of them had the part in stock. 
<strong>the</strong> building remains warm for now, <strong>and</strong> the temperature will drop tonight. 
Please leave all portable heaters on low <strong>but</strong> safe settings.
</div>""",
        "proofreading_errors": [
            "Change incorrect connective 'and' to contrast: '08:00, but he did not have...'",
            "Add comma before contrasting connective: 'merchants, but none...'",
            "Capitalise sentence starter: 'the' -> 'The building remains...'",
            "Change 'and' to contrasting connective: 'for now, but the temperature...'",
            "Ensure final sentence ends with a firm full stop."
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing a workplace or study challenge. In each sentence, use the connective <em>'but'</em> to contrast what you tried to do with a difficulty or unexpected result."
    },

    # -------------------------------------------------------------
    # UNIT 10
    # -------------------------------------------------------------
    {
        "unit": 10,
        "title": "Giving Reasons with 'Because'",
        "subtitle": "Absence Notifications, Return-to-Work Forms & Incident Causes",
        "format": "Employee Sickness & Absence Notification",
        "anchor_title": "Explaining Why Things Happened in the Workplace",
        "anchor_text": "In professional writing, stating what happened is only half the job. Supervisors and clients need to know WHY it happened. The connective 'because' introduces the underlying reason or explanation for an event or decision.",
        "formula_title": "Core Syntax Architecture: The Reason Anchor",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[Result / Action That Happened]</span>
  <span>+</span>
  <span class="fpill fpill-conn">because</span>
  <span>+</span>
  <span class="fpill fpill-clause">[Reason / Cause]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Explaining Causes:</strong> 'Because' links the action to its cause (e.g. <em>"I arrived late <strong>because</strong> the train was delayed."</em>).</li>
  <li><strong>The Fragment Danger:</strong> A 'because' clause cannot stand alone as a sentence. Never write: <em>"The store was closed. Because of bad weather."</em> Keep it joined!</li>
  <li><strong>Spelling Alert:</strong> Never use slang like 'cos' or 'cuz'. Always spell the full word: <strong>b-e-c-a-u-s-e</strong>.</li>
</ul>
""",
        "pitfall_text": "I could not attend work. Because I had a high fever.",
        "model_text": "I could not attend work because I had a high fever.",
        "why_text": "'Because I had a high fever' is an incomplete sentence fragment. It must be connected directly to the main clause.",
        "golden_rule": "THE 'WHY?' CONNECTOR: Whenever someone asks 'Why?', your answer starts with 'because'. Keep the reason attached to the action like a trailer hooked to a truck!",
        "exercise_a": [
            ("Which sentence uses 'because' correctly without creating a fragment?",
             ["A) The flight was cancelled because heavy snow covered the runway.", "B) The flight was cancelled. Because heavy snow covered the runway.", "C) Because the flight was cancelled so heavy snow covered the runway."], "A"),
            ("Choose the correct word to complete the sentence: <em>'We wore ear protectors ______ the machinery was loud.'</em>",
             ["A) but", "B) because", "C) and"], "B"),
            ("Which sentence contains a spelling or fragment error?",
             ["A) Jamal went home early cos he was unwell.", "B) Jamal went home early because he was unwell.", "C) Because he was unwell, Jamal went home early."], "A"),
            ("Identify the correctly constructed reason sentence:",
             ["A) The client called because her invoice had an incorrect total.", "B) The client called, because, her invoice had an incorrect total.", "C) The client called. Because her invoice had an incorrect total."], "A")
        ],
        "exercise_b": [
            ("Connect the action to the reason", "The safety inspection failed. Two emergency exit lights were broken.", "The safety inspection failed because two emergency exit lights were broken."),
            ("Fix the informal spelling", "We switched off the conveyor belt cos a package was jammed.", "We switched off the conveyor belt because a package was jammed."),
            ("Combine into one complete sentence", "Sophie wore thick gloves. The chemicals were hazardous.", "Sophie wore thick gloves because the chemicals were hazardous.")
        ],
        "proofreading_title": "Absence Notification & Return-to-Work Form",
        "proofreading_scenario": "An employee submitted this explanation note with 5 errors involving 'because' fragments, slang, and capitals. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
ABSENCE LOG &bull; EMPLOYEE #402<br>
I was absent on Tuesday <strong>cos</strong> I had a severe dental infection. 
I could not phone my line manager at eight. <strong>because</strong> my doctor was treating me. 
<strong>the</strong> clinic gave me a medical certificate <strong>because</strong> I needed three days of rest. 
I am returning to work today <strong>cuz</strong> I feel fully recovered.
</div>""",
        "proofreading_errors": [
            "Replace slang 'cos' with standard spelling 'because'",
            "Fix fragment: join 'at eight because my doctor...' (remove full stop and lowercase 'b')",
            "Capitalise sentence starter: 'the' -> 'The clinic'",
            "Replace second slang 'cuz' with standard spelling 'because'",
            "Ensure entire note ends with a clear full stop."
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> explaining why you made a specific decision at work or college (e.g. attending a course, asking for help, or taking a break). In each sentence, use the connective <em>'because'</em> to give a clear reason."
    },

    # -------------------------------------------------------------
    # UNIT 11
    # -------------------------------------------------------------
    {
        "unit": 11,
        "title": "Cause & Effect with 'So'",
        "subtitle": "Problem Solving, Action Logs & Customer Follow-Up",
        "format": "Customer Service Action Log",
        "anchor_title": "Reporting Actions Taken as a Direct Result",
        "anchor_text": "In workplace problem solving, describing what action you took in response to a problem is vital. The connective 'so' introduces the direct consequence, result, or solution. While 'because' looks backwards at the cause, 'so' looks forwards at what you did next.",
        "formula_title": "Core Syntax Architecture: The Result Consequence Chain",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[Problem / Situation]</span>
  <span>+</span>
  <span class="fpill fpill-conn">, so</span>
  <span>+</span>
  <span class="fpill fpill-verb">[Action Taken / Consequence]</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Showing the Result:</strong> 'So' connects a problem or event to the resulting action (e.g. <em>"The printer ran out of paper, <strong>so</strong> I refilled the tray."</em>).</li>
  <li><strong>Because vs So:</strong> 'Because' introduces the REASON; 'So' introduces the RESULT (e.g. <em>"The floor was wet, <strong>so</strong> I mopped it."</em> vs <em>"I mopped the floor <strong>because</strong> it was wet."</em>).</li>
  <li><strong>The Comma Signal:</strong> Place a small comma before 'so' when joining two complete clauses.</li>
</ul>
""",
        "pitfall_text": "The floor was greasy because I put down warning cones.",
        "model_text": "The floor was greasy, so I put down warning cones.",
        "why_text": "Putting down cones is the result of the greasy floor, not the cause of it. The connective 'so' is required.",
        "golden_rule": "THE 'WHAT NEXT?' TEST: If the second part of your sentence tells the reader what action you took next, connect it with ', so'. Cause happens first &rarr; so &rarr; Action follows!",
        "exercise_a": [
            ("Which sentence uses 'so' correctly to show a result?",
             ["A) The kitchen ran out of clean plates, so Lewis started the dishwasher.", "B) The kitchen ran out of clean plates because Lewis started the dishwasher.", "C) The kitchen ran out of clean plates so because Lewis started the dishwasher."], "A"),
            ("Choose the correct connective: <em>'The warehouse was cold, ______ Chloe put on her fleece jacket.'</em>",
             ["A) because", "B) so", "C) but"], "B"),
            ("Which sentence is punctuated correctly?",
             ["A) The package was damaged in transit, so we issued a full refund.", "B) The package was damaged in transit so, we issued a full refund.", "C) The package was damaged in transit so we issued, a full refund."], "A"),
            ("Identify the sentence where 'because' and 'so' are confused:",
             ["A) I was tired, so I went to bed early.", "B) The train was cancelled, so we took a taxi.", "C) The battery died so I had to recharge it because it was flat so I couldn't call."], "C")
        ],
        "exercise_b": [
            ("Join into one result sentence using ', so'", "The main server crashed. All staff worked offline.", "The main server crashed, so all staff worked offline."),
            ("Complete the sentence with an action result", "The delivery truck had a flat tyre, so __________________.", "The delivery truck had a flat tyre, so the driver called roadside recovery."),
            ("Change 'because' to 'so' by reversing the order", "I ordered extra tea bags because the staffroom had none.", "The staffroom had no tea bags, so I ordered extra.")
        ],
        "proofreading_title": "Facilities & Maintenance Incident Log",
        "proofreading_scenario": "A facilities officer wrote this incident report. It contains 5 errors involving confused connectives, commas, and capital letters. Fix all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
INCIDENT REPORT &bull; ROOM 104<br>
The radiator was leaking water on the carpet <strong>because</strong> I turned off the valve. 
The room smelled of damp <strong>so</strong> I opened both windows. 
<strong>the</strong> maintenance engineer was in a meeting, <strong>so</strong>, I left an urgent voicemail. 
He arrived at two o'clock <strong>so</strong> the leak was repaired safely.
</div>""",
        "proofreading_errors": [
            "Change incorrect 'because' to result: 'carpet, so I turned off...'",
            "Add comma before connective: 'damp, so I opened...'",
            "Capitalise sentence starter: 'the' -> 'The maintenance engineer'",
            "Remove misplaced comma after 'so': ', so I left an urgent...'",
            "Change final 'so' to connective 'and': 'o'clock and the leak was...'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing a practical problem you encountered at work, home, or college, and the action you took. Connect the problem and your solution using <em>', so'</em> in both sentences."
    },

    # -------------------------------------------------------------
    # UNIT 12
    # -------------------------------------------------------------
    {
        "unit": 12,
        "title": "Commas in Simple Shopping & Equipment Lists",
        "subtitle": "Stock Requisitions, Tool Inventories & Kitchen Prep Lists",
        "format": "Stock Requisition & Equipment Order Form",
        "anchor_title": "Separating Items in Commercial Lists & Requisitions",
        "anchor_text": "Whether ordering safety equipment for a building site, ingredients for a restaurant kitchen, or stationery for an office, you will frequently write lists of three or more items. Commas separate the items cleanly, while the word 'and' joins the final two items.",
        "formula_title": "Core Syntax Architecture: The List Separator Formula",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Item 1</span>
  <span class="fpill fpill-punct">,</span>
  <span class="fpill fpill-subj">Item 2</span>
  <span class="fpill fpill-punct">,</span>
  <span class="fpill fpill-subj">Item 3</span>
  <span class="fpill fpill-conn">and</span>
  <span class="fpill fpill-subj">Item 4</span>
  <span class="fpill fpill-punct">.</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>The List Comma:</strong> Place a comma after every item in a list except the last two.</li>
  <li><strong>The Final Pair:</strong> Use the word 'and' between the final two items instead of a comma.</li>
  <li><strong>No Comma After 'And':</strong> Never place a comma directly after 'and' (e.g. NOT <em>'and, milk'</em>).</li>
  <li><strong>No Comma Before the First Item:</strong> Do NOT put a comma immediately after the verb (e.g. NOT <em>'Please buy, apples...'</em>).</li>
</ul>
""",
        "pitfall_text": "Please bring safety goggles, steel boots, high-vis jackets, and, ear defenders.",
        "model_text": "Please bring safety goggles, steel boots, high-vis jackets and ear defenders.",
        "why_text": "In standard British English, commas separate the list items, and 'and' joins the final pair without extra commas.",
        "golden_rule": "THE SHOPPING TROLLEY RULE: Commas are the dividers between items in your shopping trolley. Put a comma after each item, but swap the last comma for the word 'and'!",
        "exercise_a": [
            ("Which sentence punctuates a list of office supplies correctly?",
             ["A) Please order paper pens staples and notebooks.", "B) Please order paper, pens, staples and notebooks.", "C) Please order paper, pens, staples, and, notebooks."], "B"),
            ("Where should the commas be placed in this sentence: <em>'The chef bought onions carrots potatoes and garlic.'</em>",
             ["A) After 'onions', 'carrots', and 'potatoes'", "B) After 'onions' and 'carrots' only", "C) After 'bought' and 'garlic'"], "B"),
            ("Which sentence contains a punctuation error in the list?",
             ["A) The van carries hammers, screwdrivers, drills and pliers.", "B) The van carries, hammers, screwdrivers, drills and pliers.", "C) The van carries hammers, screwdrivers and drills."], "B"),
            ("Identify the correctly punctuated PPE equipment list:",
             ["A) All staff must wear hard hats, safety boots, protective gloves and hi-vis vests.", "B) All staff must wear hard hats safety boots protective gloves and hi-vis vests.", "C) All staff must wear hard hats, safety boots, protective gloves, and, hi-vis vests."], "A")
        ],
        "exercise_b": [
            ("Insert commas correctly into the tool list", "The plumber packed copper pipes brass fittings flux and solder.", "The plumber packed copper pipes, brass fittings, flux and solder."),
            ("Fix the misplaced comma after 'and'", "We need white bread, brown bread, rolls, and, baguettes.", "We need white bread, brown bread, rolls and baguettes."),
            ("Punctuate the catering ingredients list", "The recipe requires butter sugar flour eggs and vanilla extract.", "The recipe requires butter, sugar, flour, eggs and vanilla extract.")
        ],
        "proofreading_title": "Catering Supply & Grocery Requisition Note",
        "proofreading_scenario": "A kitchen assistant wrote this stock order slip. Find and correct all 5 comma and punctuation errors in the lists.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
STOCK ORDER &bull; MAIN KITCHEN<br>
Please purchase <strong>milk eggs cheese and butter</strong> from the dairy supplier. 
For the bakery section, order <strong>flour, yeast, sugar, and, salt</strong>. 
For cleaning, we require bleach, mops <strong>buckets</strong> and rubber gloves. 
Deliver all goods before eleven o'clock.
</div>""",
        "proofreading_errors": [
            "Add commas between dairy items: 'milk, eggs, cheese and butter'",
            "Remove unnecessary comma before and after 'and': 'sugar and salt'",
            "Add missing comma in cleaning list: 'mops, buckets and...'",
            "Ensure first list begins after the colon without an extra comma",
            "Verify all items are separated cleanly before the final 'and'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> listing items you use at work, home, or in a trade. In the first sentence, list at least four tools or pieces of equipment. In the second sentence, list at least four grocery or stationery items. Use commas correctly."
    },

    # -------------------------------------------------------------
    # UNIT 13
    # -------------------------------------------------------------
    {
        "unit": 13,
        "title": "Present Tense — Daily Workplace Routines (Regular Verbs)",
        "subtitle": "Job Descriptions, Daily Checklists & Operational Standard Procedures",
        "format": "Cleaner & Care Assistant Daily Duty Rota",
        "anchor_title": "Documenting Daily Routines & Standard Operating Procedures",
        "anchor_text": "In job descriptions, daily handover checklists, and routine procedures, you explain what happens every day. When describing repeated habits or regular routines using 'I', 'we', or 'they', verbs stay in their simple base present tense form.",
        "formula_title": "Core Syntax Architecture: The Daily Routine Framework",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">I / You / We / They</span>
  <span>+</span>
  <span class="fpill fpill-verb">Base Verb (No Ending)</span>
  <span>+</span>
  <span class="fpill fpill-clause">Routine Time Expression</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Habitual Everyday Actions:</strong> Use base verbs for routines: <em>I <strong>check</strong>, we <strong>clean</strong>, they <strong>inspect</strong>, you <strong>sign</strong></em>.</li>
  <li><strong>Time Expressions:</strong> Frequently paired with: <em>every day, each morning, on Mondays, regularly, always</em>.</li>
  <li><strong>The Past Tense Trap:</strong> Never add '-ed' when describing ongoing daily routines (e.g. NOT <em>'Every morning I checked the stock'</em> &mdash; write <em>'I check'</em>).</li>
</ul>
""",
        "pitfall_text": "Every morning, I checked the temperature gauges and logged the readings.",
        "model_text": "Every morning, I check the temperature gauges and log the readings.",
        "why_text": "'Every morning' indicates a regular ongoing daily routine, so the verbs must be in the present tense ('check' and 'log').",
        "golden_rule": "THE DAILY CLOCK RULE: If you do it every shift, every week, or every day, keep the verb in the simple present! Do not add '-ed' to routine workplace habits.",
        "exercise_a": [
            ("Which sentence correctly describes a daily workplace routine in the present tense?",
             ["A) Every morning, I unlock the staff entrance and brew the tea.", "B) Every morning, I unlocked the staff entrance and brewed the tea.", "C) Every morning, I unlocking the staff entrance and brew the tea."], "A"),
            ("Choose the correct present tense verb: <em>'We ______ the fire extinguishers once every month.'</em>",
             ["A) inspected", "B) inspect", "C) inspecting"], "B"),
            ("Which sentence contains a tense error for a regular habit?",
             ["A) They clean the kitchen surfaces after every meal.", "B) They cleaned the kitchen surfaces every single evening.", "C) They clean the kitchen surfaces and sanitize the chopping boards."], "B"),
            ("Identify the correct daily handover statement:",
             ["A) At the end of each shift, we lock the cash drawer and count the float.", "B) At the end of each shift, we locked the cash drawer and counted the float.", "C) At the end of each shift, we locking the cash drawer and count the float."], "A")
        ],
        "exercise_b": [
            ("Convert from past to present routine", "Yesterday, we emptied the bins and washed the floors.", "Every day, we empty the bins and wash the floors."),
            ("Complete the routine sentence with the base verb 'pack'", "Every afternoon, the warehouse staff ____________ forty delivery boxes.", "Every afternoon, the warehouse staff pack forty delivery boxes."),
            ("Fix the incorrect '-ed' past verb in this daily duty", "On Mondays, I ordered fresh fruit for the care home residents.", "On Mondays, I order fresh fruit for the care home residents.")
        ],
        "proofreading_title": "Daily Care Home Morning Rota & Duties",
        "proofreading_scenario": "A newly appointed senior care assistant wrote this daily routine guide. Correct all 5 present tense verb and capitalisation errors.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
DAILY MORNING ROUTINE &bull; SUNSHINE CARE HOME<br>
Every morning at 07:30, we <strong>served</strong> breakfast to the residents in the dining room. 
After breakfast, care assistants <strong>helped</strong> residents with morning mobility exercises. 
At ten o'clock, <strong>i</strong> <strong>distributed</strong> the morning medication. 
We always <strong>recorded</strong> each dose in the daily care log immediately.
</div>""",
        "proofreading_errors": [
            "Change past verb to present routine: 'served' -> 'serve'",
            "Change past verb to present routine: 'helped' -> 'help'",
            "Capitalise personal pronoun: 'i' -> 'I'",
            "Change past verb to present routine: 'distributed' -> 'distribute'",
            "Change past verb to present routine: 'recorded' -> 'record'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing your daily workplace or study routine using present tense verbs (e.g. <em>check, clean, arrive, open, study</em>). Start your sentences with time markers like <em>'Every morning...'</em> or <em>'Each shift...'</em>."
    },

    # -------------------------------------------------------------
    # UNIT 14
    # -------------------------------------------------------------
    {
        "unit": 14,
        "title": "Present Tense — Verbs with He, She, It (Adding -s and -es)",
        "subtitle": "Supervisors, Colleagues & Machine Operation Reports",
        "format": "Supervisor Shift Observation Log",
        "anchor_title": "Reporting What a Single Colleague or Machine Does",
        "anchor_text": "When you report what a colleague (he or she) or a machine (it) does on shift, the verb changes its ending. In English grammar, singular third-person subjects take an '-s' or '-es' ending in the present tense. Forgetting the 's' is one of the most common SPaG exam errors.",
        "formula_title": "Core Syntax Architecture: The Third-Person 'S' Magnet",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">He / She / It / Colleague</span>
  <span>+</span>
  <span class="fpill fpill-verb">Verb + -s / -es</span>
  <span>+</span>
  <span class="fpill fpill-clause">Detail</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Standard Rule (+s):</strong> Most verbs simply add '-s': <em>He check<strong>s</strong>, she clean<strong>s</strong>, the van start<strong>s</strong>, Marcus walk<strong>s</strong></em>.</li>
  <li><strong>Verbs Ending in -ch, -sh, -ss, -x (+es):</strong> Add '-es': <em>She watch<strong>es</strong>, he wash<strong>es</strong>, the mechanic fix<strong>es</strong>, it pass<strong>es</strong></em>.</li>
  <li><strong>Irregular Present Verbs:</strong> <em>have &rarr; ha<strong>s</strong></em>, <em>do &rarr; doe<strong>s</strong></em>, <em>go &rarr; goe<strong>s</strong></em>.</li>
</ul>
""",
        "pitfall_text": "The supervisor check the rota and fix the schedule every morning.",
        "model_text": "The supervisor checks the rota and fixes the schedule every morning.",
        "why_text": "'The supervisor' is a singular third-person subject (he or she), so 'check' becomes 'checks' and 'fix' becomes 'fixes'.",
        "golden_rule": "THE 'S' MAGNET RULE: 'He', 'She', and 'It' are powerful magnets that pull an '-s' or '-es' onto the tail of the verb. If the subject is singular (one person or thing), add the 's'!",
        "exercise_a": [
            ("Which sentence uses the correct present tense verb for 'he'?",
             ["A) He inspect the goods carefully.", "B) He inspects the goods carefully.", "C) He inspecting the goods carefully."], "B"),
            ("Which sentence correctly adds '-es' to a verb ending in -sh or -ch?",
             ["A) The technician washes the test tubes and matches the batch codes.", "B) The technician wash the test tubes and match the batch codes.", "C) The technician washs the test tubes and matchs the batch codes."], "A"),
            ("Choose the correct verb form: <em>'The warehouse manager ______ the keys in the safe.'</em>",
             ["A) keep", "B) keeps", "C) keeping"], "B"),
            ("Which sentence shows correct third-person subject-verb agreement?",
             ["A) Sarah do the filing every Friday.", "B) Sarah does the filing every Friday.", "C) Sarah dose the filing every Friday."], "B")
        ],
        "exercise_b": [
            ("Add -s or -es to the verb in brackets", "Every Friday, Marcus (clean) ____________ the staff canteen.", "Every Friday, Marcus cleans the staff canteen."),
            ("Change the verb 'fix' for a singular subject", "The senior maintenance technician (fix) ____________ any broken conveyor belts.", "The senior maintenance technician fixes any broken conveyor belts."),
            ("Correct the missing 's' error", "She check the temperature of the pharmacy fridge twice a day.", "She checks the temperature of the pharmacy fridge twice a day.")
        ],
        "proofreading_title": "Supervisor Performance & Handover Report",
        "proofreading_scenario": "A team leader documented a colleague's duties with 5 missing '-s' and '-es' errors. Find and correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
COLLEAGUE OBSERVATION &bull; WAREHOUSE OPERATIVE<br>
During the morning shift, David <strong>manage</strong> the intake bay with great care. 
He <strong>inspect</strong> all incoming wooden pallets and <strong>cross</strong> the numbers off the invoice. 
When a carton is damaged, he <strong>report</strong> the issue to the warehouse manager immediately. 
David also <strong>wash</strong> the forklift truck before finishing his shift.
</div>""",
        "proofreading_errors": [
            "Add '-s' for singular subject: 'manage' -> 'manages'",
            "Add '-s' for singular subject: 'inspect' -> 'inspects'",
            "Add '-es' for verb ending in -ss: 'cross' -> 'crosses'",
            "Add '-s' for singular subject: 'report' -> 'reports'",
            "Add '-es' for verb ending in -sh: 'wash' -> 'washes'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing what a specific colleague, supervisor, or machine does every day at work. Ensure your verbs end in <em>-s</em> or <em>-es</em> (e.g. <em>checks, operates, washes, manages</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 15
    # -------------------------------------------------------------
    {
        "unit": 15,
        "title": "Past Tense — Regular Verbs with -ed",
        "subtitle": "Completed Work Logs, Incident Records & Signed-Off Tickets",
        "format": "Maintenance Sign-Off & Completed Work Log",
        "anchor_title": "Signing Off Completed Workplace Tasks",
        "anchor_text": "In official logs, incident reports, and timesheets, you must clearly document actions that are already finished. Regular English verbs form the past tense by adding '-ed'. Even though spoken English often sounds like /t/ or /d/, the written spelling must always end in '-ed'.",
        "formula_title": "Core Syntax Architecture: The Regular Past Suffix",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Subject</span>
  <span>+</span>
  <span class="fpill fpill-verb">Base Verb + -ed</span>
  <span>+</span>
  <span class="fpill fpill-clause">Completed Detail</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Standard Regular Past (+ed):</strong> <em>walk &rarr; walk<strong>ed</strong>, check &rarr; check<strong>ed</strong>, inspect &rarr; inspect<strong>ed</strong>, call &rarr; call<strong>ed</strong></em>.</li>
  <li><strong>Verbs Ending in 'e' (+d):</strong> If the verb already ends in 'e', simply add 'd': <em>close &rarr; close<strong>d</strong>, live &rarr; live<strong>d</strong>, phone &rarr; phone<strong>d</strong></em>.</li>
  <li><strong>The Spoken Sound Trap:</strong> 'Walked' sounds like 'walkt', but NEVER write 'walkt' or 'checkt'. The spelling is always <strong>-ed</strong>.</li>
</ul>
""",
        "pitfall_text": "Yesterday, the electrician checkt the wiring and fixt the light.",
        "model_text": "Yesterday, the electrician checked the wiring and fixed the light.",
        "why_text": "Regular past tense verbs always take the suffix '-ed', never the phonetic sound 't' or 'd'.",
        "golden_rule": "THE '-ED' COAT RULE: When an action happened yesterday or last week, put an '-ed' coat on the regular verb. Even if your mouth pronounces it as /t/, your pen must always write '-ed'!",
        "exercise_a": [
            ("Which sentence spells the regular past tense verb correctly?",
             ["A) We checkt the stock list yesterday.", "B) We checked the stock list yesterday.", "C) We checkid the stock list yesterday."], "B"),
            ("What is the past tense of 'clean'?",
             ["A) cleand", "B) cleant", "C) cleaned"], "C"),
            ("Which sentence correctly reports finished workplace actions?",
             ["A) The plumber drained the pipes and tested the water pressure.", "B) The plumber draint the pipes and testid the water pressure.", "C) The plumber drain the pipes and test the water pressure yesterday."], "A"),
            ("Identify the misspelled past tense verb:",
             ["A) arrived", "B) walkt", "C) repaired"], "B")
        ],
        "exercise_b": [
            ("Convert the base verb 'deliver' into the past tense", "Yesterday morning, the courier (deliver) ____________ twelve medical parcels.", "Yesterday morning, the courier delivered twelve medical parcels."),
            ("Fix the phonetic spelling error", "The security guard lockt the outer gates at ten.", "The security guard locked the outer gates at ten."),
            ("Rewrite in the past tense with '-ed'", "We paint the staffroom and clean the carpet.", "We painted the staffroom and cleaned the carpet.")
        ],
        "proofreading_title": "Facilities Completed Maintenance Ticket",
        "proofreading_scenario": "A contractor filled out this job sign-off sheet with 5 spelling and tense errors on regular past verbs. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
JOB SIGN-OFF SHEET &bull; TICKET #9941<br>
CONTRACTOR: Apex Facilities Ltd<br>
WORK COMPLETED: Yesterday afternoon, our engineer <strong>inspect</strong> the fire alarm system. 
He <strong>reparid</strong> the emergency exit sensor and <strong>testt</strong> the battery backup. 
The team <strong>wash</strong> all smoke detectors and <strong>cleand</strong> the control panel. 
All systems are fully functional.
</div>""",
        "proofreading_errors": [
            "Add '-ed' to base verb: 'inspect' -> 'inspected'",
            "Correct misspelling of past suffix: 'reparid' -> 'repaired'",
            "Correct misspelling: 'testt' -> 'tested'",
            "Add '-ed' to base verb: 'wash' -> 'washed'",
            "Correct spelling: 'cleand' -> 'cleaned'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing tasks you finished yesterday or last week at work or home. Use regular past tense verbs ending in <em>-ed</em> (e.g. <em>cleaned, checked, cooked, walked, repaired</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 16
    # -------------------------------------------------------------
    {
        "unit": 16,
        "title": "Past Tense — Doubling the Consonant (stopped, planned)",
        "subtitle": "Accident Reports, Shift Handover Forms & Travel Logs",
        "format": "Incident & Vehicle Log Sheet",
        "anchor_title": "Reporting Safety Incidents & Vehicle Movements",
        "anchor_text": "In official accident investigation reports and transport logs, precise spelling of short action verbs is essential. If a single-syllable word has a short vowel sound followed by one consonant, that consonant must be doubled before adding '-ed' or '-ing'. Forgetting to double the letter changes the word entirely.",
        "formula_title": "Core Syntax Architecture: The 1-1-1 Doubling Rule",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">1 Syllable Word</span>
  <span>+</span>
  <span class="fpill fpill-verb">1 Short Vowel (a, e, i, o, u)</span>
  <span>+</span>
  <span class="fpill fpill-conn">1 Final Consonant</span>
  <span>=</span>
  <span class="fpill fpill-punct">DOUBLE Consonant + -ed</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Core Rule:</strong> <em>stop &rarr; stop<strong>ped</strong>, plan &rarr; plan<strong>ned</strong>, drop &rarr; drop<strong>ped</strong>, fit &rarr; fit<strong>ted</strong>, slip &rarr; slip<strong>ped</strong></em>.</li>
  <li><strong>Why Double?</strong> Doubling preserves the short vowel sound. Without doubling, 'hopped' would become 'hoped' (long 'o'), and 'planned' would become 'planed'.</li>
  <li><strong>Suffix Consistency:</strong> The same doubling rule applies when adding '-ing': <em>stopping, planning, dropping, fitting</em>.</li>
</ul>
""",
        "pitfall_text": "The delivery driver stoped the van and droped the parcel on the path.",
        "model_text": "The delivery driver stopped the van and dropped the parcel on the path.",
        "why_text": "'Stop' and 'drop' have one short vowel and one final consonant. The final consonants 'p' must be doubled before adding '-ed'.",
        "golden_rule": "THE 1-1-1 GUARD RULE: 1 syllable, 1 short vowel, 1 final consonant. Double the consonant to guard the short vowel! (e.g. stop &rarr; stopped, plan &rarr; planned, slip &rarr; slipped).",
        "exercise_a": [
            ("Which word is the correctly spelled past tense of 'stop'?",
             ["A) stoped", "B) stopped", "C) stopd"], "B"),
            ("Which sentence spells all consonant-doubled verbs correctly?",
             ["A) We planned the route and fitted the new tyres yesterday.", "B) We planed the route and fited the new tyres yesterday.", "C) We pland the route and fitted the new tyres yesterday."], "A"),
            ("What happens to 'slip' when adding '-ed'?",
             ["A) sliped", "B) slipt", "C) slipped"], "C"),
            ("Identify the sentence with a spelling error:",
             ["A) The machine grabbed the cardboard sheet.", "B) The worker droped the heavy metal wrench.", "C) The manager stepped into the conference room."], "B")
        ],
        "exercise_b": [
            ("Double the consonant for the past tense of 'plan'", "Last month, the logistics team (plan) ____________ a new delivery schedule.", "Last month, the logistics team planned a new delivery schedule."),
            ("Correct the spelling of 'stoped'", "The security officer stoped the unauthorised vehicle at the gate.", "The security officer stopped the unauthorised vehicle at the gate."),
            ("Spell the past tense of 'fit' and 'drop'", "The mechanic (fit) ____________ the brake pads and carefully (drop) ____________ the jack.", "The mechanic fitted the brake pads and carefully dropped the jack.")
        ],
        "proofreading_title": "Warehouse Incident & Safety Investigation Log",
        "proofreading_scenario": "A health and safety representative logged this forklift accident report with 5 consonant-doubling errors. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
ACCIDENT INVESTIGATION &bull; DEPOT 2<br>
At 14:15, the forklift driver <strong>stoped</strong> suddenly near bay 6. 
A loose wooden pallet had <strong>sliped</strong> off the upper rack. 
The supervisor <strong>grabed</strong> the emergency brake lever and halted traffic. 
The team had not <strong>planed</strong> for oil on the floor. 
Fortunately, the technician <strong>fited</strong> new safety barriers by 16:00.
</div>""",
        "proofreading_errors": [
            "Double the 'p' before -ed: 'stoped' -> 'stopped'",
            "Double the 'p' before -ed: 'sliped' -> 'slipped'",
            "Double the 'b' before -ed: 'grabed' -> 'grabbed'",
            "Double the 'n' before -ed: 'planed' -> 'planned'",
            "Double the 't' before -ed: 'fited' -> 'fitted'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> about an action that was completed recently. Use at least two verbs that double their final consonant before adding <em>-ed</em> (choose from: <em>stopped, planned, dropped, fitted, slipped, grabbed</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 17
    # -------------------------------------------------------------
    {
        "unit": 17,
        "title": "Top 25 Irregular Past Verbs (Part 1: was, were, had, went, saw)",
        "subtitle": "Security Reports, Customer Encounters & Shift Recaps",
        "format": "Security Duty Incident Report",
        "anchor_title": "Reporting Real-World Events with Irregular Verbs",
        "anchor_text": "Many of the most common verbs in the English language do not follow the '-ed' rule. Instead, they change their spelling entirely in the past tense. Writing 'I goed' or 'we was' damages your professional reputation and loses vital marks in Functional Skills exams.",
        "formula_title": "Core Syntax Architecture: The Top 5 Irregular Past Forms",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Base: be (am/is) &rarr; <strong style="color:#1e40af;">was</strong></span>
  <span class="fpill fpill-subj">Base: be (are) &rarr; <strong style="color:#1e40af;">were</strong></span>
  <span class="fpill fpill-verb">Base: have &rarr; <strong style="color:#166534;">had</strong></span>
  <span class="fpill fpill-conn">Base: go &rarr; <strong style="color:#6b21a8;">went</strong></span>
  <span class="fpill fpill-clause">Base: see &rarr; <strong style="color:#9a3412;">saw</strong></span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Go &rarr; Went:</strong> Never say 'goed'. (e.g. <em>"Yesterday I <strong>went</strong> to the depot."</em>).</li>
  <li><strong>See &rarr; Saw:</strong> The past tense of see is 'saw'. Never write 'I seen' without a helper verb (e.g. <em>"I <strong>saw</strong> the intruder."</em> &mdash; NOT 'I seen').</li>
  <li><strong>Was vs Were:</strong> Singular takes 'was' (<em>I was, he was, it was</em>); Plural takes 'were' (<em>we were, they were, you were</em>).</li>
</ul>
""",
        "pitfall_text": "We was at the office when I seen the smoke, so I goed to investigate.",
        "model_text": "We were at the office when I saw the smoke, so I went to investigate.",
        "why_text": "'We' requires 'were'; the past tense of 'see' is 'saw'; the past tense of 'go' is 'went'.",
        "golden_rule": "THE IRREGULAR CHAMPIONS: 'Went', 'Saw', 'Had', 'Was', and 'Were' are the champions of workplace reports. Never add '-ed' to them. Treat them with respect and write them correctly!",
        "exercise_a": [
            ("Which sentence correctly uses the past tense of 'go' and 'see'?",
             ["A) I went to the store and saw the new stock.", "B) I goed to the store and seen the new stock.", "C) I went to the store and seen the new stock."], "A"),
            ("Choose the correct verb: <em>'The two security officers ______ on duty last night.'</em>",
             ["A) was", "B) were", "C) been"], "B"),
            ("Which sentence contains an irregular past verb error?",
             ["A) We had a team briefing at nine.", "B) The manager saw the damaged pallet.", "C) The technicians was in the server room."], "C"),
            ("Identify the standard English sentence:",
             ["A) I seen the delivery driver leave the depot.", "B) I saw the delivery driver leave the depot.", "C) I seed the delivery driver leave the depot."], "B")
        ],
        "exercise_b": [
            ("Change 'go' to the irregular past tense", "After lunch, the supervisor (go) ____________ to the head office.", "After lunch, the supervisor went to the head office."),
            ("Change 'see' to the irregular past tense", "The security guard (see) ____________ the broken window at 02:00.", "The security guard saw the broken window at 02:00."),
            ("Choose between 'was' and 'were'", "All three delivery vans (was / were) ____________ fully loaded with parcels.", "All three delivery vans were fully loaded with parcels.")
        ],
        "proofreading_title": "Security Guard Night Patrol Log",
        "proofreading_scenario": "A guard submitted this patrol recap containing 5 irregular verb errors. Correct all 5 to standard English.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
PATROL LOG &bull; INDUSTRIAL ZONE EAST<br>
At 23:00, officer Khan and I <strong>was</strong> on perimeter patrol. 
We <strong>goed</strong> to check the rear fence line behind warehouse 3. 
Officer Khan <strong>seen</strong> a cut padlock on gate 4. 
We <strong>haved</strong> our torches switched on at all times. 
Fortunately, the intruder <strong>goed</strong> before we arrived.
</div>""",
        "proofreading_errors": [
            "Change plural agreement: 'officer Khan and I was' -> 'were'",
            "Change incorrect 'goed' to 'went'",
            "Change non-standard 'seen' to past tense 'saw'",
            "Change incorrect 'haved' to past tense 'had'",
            "Change second 'goed' to past tense 'went'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing an event that happened at work or college last week. Use at least two irregular past verbs from this unit: <em>went, saw, had, was, were</em>."
    },

    # -------------------------------------------------------------
    # UNIT 18
    # -------------------------------------------------------------
    {
        "unit": 18,
        "title": "Top 25 Irregular Past Verbs (Part 2: came, did, said, took, gave)",
        "subtitle": "Customer Conversations, Supervisor Memos & Asset Tracking",
        "format": "Customer Service Complaint & Resolution Memo",
        "anchor_title": "Documenting Workplace Conversations & Actions Taken",
        "anchor_text": "In customer complaints and supervisor handovers, you must report who came by, what they said, what was done, and what was given. The irregular verbs 'came', 'did', 'said', 'took', and 'gave' appear on almost every workplace report. Using incorrect non-standard forms like 'comed' or 'gived' marks your writing as non-standard.",
        "formula_title": "Core Syntax Architecture: The Action Handover Quintet",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Base: come &rarr; <strong style="color:#1e40af;">came</strong></span>
  <span class="fpill fpill-verb">Base: do &rarr; <strong style="color:#166534;">did</strong></span>
  <span class="fpill fpill-conn">Base: say &rarr; <strong style="color:#6b21a8;">said</strong></span>
  <span class="fpill fpill-clause">Base: take &rarr; <strong style="color:#9a3412;">took</strong></span>
  <span class="fpill fpill-punct">Base: give &rarr; <strong style="color:#b45309;">gave</strong></span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Come &rarr; Came:</strong> (e.g. <em>"The courier <strong>came</strong> at noon."</em> &mdash; NOT 'comed').</li>
  <li><strong>Do &rarr; Did:</strong> (e.g. <em>"I <strong>did</strong> the stocktake yesterday."</em> &mdash; NOT 'I done the stocktake').</li>
  <li><strong>Say &rarr; Said:</strong> (e.g. <em>"The customer <strong>said</strong> the box was damaged."</em> &mdash; NOT 'sayed').</li>
  <li><strong>Take &rarr; Took &bull; Give &rarr; Gave:</strong> (e.g. <em>"He <strong>took</strong> the order and <strong>gave</strong> a receipt."</em>).</li>
</ul>
""",
        "pitfall_text": "The manager comed to the desk, done the inspection, and gived a refund.",
        "model_text": "The manager came to the desk, did the inspection, and gave a refund.",
        "why_text": "The standard irregular past forms are 'came' (not comed), 'did' (not done on its own), and 'gave' (not gived).",
        "golden_rule": "THE PROFESSIONAL REPUTATION RULE: Examiners look specifically for 'did' instead of 'done', and 'gave' instead of 'gived'. Lock these five power verbs into your memory!",
        "exercise_a": [
            ("Which sentence uses the correct past tense of 'do' and 'give'?",
             ["A) I did my duties and the manager gave me feedback.", "B) I done my duties and the manager gived me feedback.", "C) I did my duties and the manager gived me feedback."], "A"),
            ("What is the correct past tense of 'say'?",
             ["A) sayed", "B) said", "C) saide"], "B"),
            ("Choose the correct verb: <em>'The engineer ______ the broken motor back to the workshop.'</em>",
             ["A) took", "B) taked", "C) taken"], "A"),
            ("Identify the sentence with non-standard grammar:",
             ["A) The client came to our office yesterday.", "B) The customer done a complaint online.", "C) The technician said the machine was ready."], "B")
        ],
        "exercise_b": [
            ("Change 'come' and 'give' into the past tense", "The postal worker (come) ____________ at ten and (give) ____________ us the parcels.", "The postal worker came at ten and gave us the parcels."),
            ("Correct the non-standard 'done'", "Yesterday, we done all the filing for human resources.", "Yesterday, we did all the filing for human resources."),
            ("Change 'say' and 'take' into the past tense", "The supervisor (say) ____________ the work was excellent and (take) ____________ our timesheets.", "The supervisor said the work was excellent and took our timesheets.")
        ],
        "proofreading_title": "Customer Service Incident Handover Note",
        "proofreading_scenario": "A retail team member drafted this customer dispute summary. It contains 5 non-standard irregular verb errors. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
INCIDENT SUMMARY &bull; CUSTOMER SERVICE DESK<br>
A customer <strong>comed</strong> to the returns counter at 11:30. 
She <strong>sayed</strong> that the electric kettle stopped working after one day. 
I <strong>done</strong> a quick visual check and confirmed the fault. 
I <strong>taked</strong> the faulty item back into stock and <strong>gived</strong> the customer 
a full replacement with an updated receipt.
</div>""",
        "proofreading_errors": [
            "Change non-standard 'comed' to 'came'",
            "Change non-standard 'sayed' to 'said'",
            "Change non-standard 'done' to 'did'",
            "Change non-standard 'taked' to 'took'",
            "Change non-standard 'gived' to 'gave'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing an interaction with a customer, tutor, or colleague. Use at least two irregular verbs from this unit: <em>came, did, said, took, gave</em>."
    },

    # -------------------------------------------------------------
    # UNIT 19
    # -------------------------------------------------------------
    {
        "unit": 19,
        "title": "Subject-Verb Agreement — Singular (is, has, was)",
        "subtitle": "Patient Files, Single Asset Records & Machine Maintenance",
        "format": "Clinic Reception & Patient Intake Record",
        "anchor_title": "Matching Singular Subjects with Singular Verbs",
        "anchor_text": "In administrative writing, precision matters. When a sentence is about ONE person, ONE place, or ONE object, the verb must also be singular. In English, singular present and past verbs end in 's' (is, was, has). Matching your subject and verb is called subject-verb agreement.",
        "formula_title": "Core Syntax Architecture: The Singular Solo Formula",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">1 Person / 1 Object / 1 Place</span>
  <span>+</span>
  <span class="fpill fpill-verb">is / was / has</span>
  <span>+</span>
  <span class="fpill fpill-clause">Predicate Information</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Singular Present 'To Be':</strong> <em>The doctor <strong>is</strong> in room 4. The van <strong>is</strong> ready.</em></li>
  <li><strong>Singular Past 'To Be':</strong> <em>The patient <strong>was</strong> waiting. The door <strong>was</strong> locked.</em></li>
  <li><strong>Singular 'To Have':</strong> <em>The apprentice <strong>has</strong> finished the training module.</em> (Never 'have').</li>
  <li><strong>Pronoun Agreement:</strong> <em>He <strong>is/was/has</strong></em>, <em>She <strong>is/was/has</strong></em>, <em>It <strong>is/was/has</strong></em>.</li>
</ul>
""",
        "pitfall_text": "The new apprentice have the key and the manager were in the office.",
        "model_text": "The new apprentice has the key and the manager was in the office.",
        "why_text": "'Apprentice' and 'manager' are each single individuals. They must pair with singular verbs ending in 's': 'has' and 'was'.",
        "golden_rule": "THE 'S' FOR SINGULAR RULE: Singular subjects (one person or one thing) love verbs ending in 's'! Match one person with 'is', 'was', or 'has'.",
        "exercise_a": [
            ("Which sentence shows correct singular agreement?",
             ["A) The technician has completed the safety inspection.", "B) The technician have completed the safety inspection.", "C) The technician were completed the safety inspection."], "A"),
            ("Choose the correct verb: <em>'The main printer in the office ______ out of ink.'</em>",
             ["A) are", "B) is", "C) were"], "B"),
            ("Which sentence contains a subject-verb agreement error?",
             ["A) The nurse was checking the blood pressure records.", "B) The nurse were checking the blood pressure records.", "C) The nurse is checking the blood pressure records."], "B"),
            ("Identify the correct statement for an equipment log:",
             ["A) The emergency generator was tested yesterday and is working fine.", "B) The emergency generator were tested yesterday and are working fine.", "C) The emergency generator have been tested yesterday and were fine."], "A")
        ],
        "exercise_b": [
            ("Select the correct verb for a singular subject", "The delivery van (is / are) ____________ parked in bay 3.", "The delivery van is parked in bay 3."),
            ("Select the correct past verb", "The patient (was / were) ____________ seated in the waiting area.", "The patient was seated in the waiting area."),
            ("Correct the agreement error with 'have'", "The new supervisor have approved our overtime request.", "The new supervisor has approved our overtime request.")
        ],
        "proofreading_title": "Health Clinic Appointment & Reception Log",
        "proofreading_scenario": "A medical receptionist typed this patient update with 5 singular agreement errors. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
RECEPTION LOG &bull; WELLNESS MEDICAL CENTRE<br>
Dr Patel <strong>have</strong> arrived in clinic room 2 for the morning clinic. 
The first patient <strong>were</strong> waiting at reception since 08:45. 
Her medical chart <strong>have</strong> been updated on the computer system. 
The blood pressure monitor <strong>are</strong> fully calibrated. 
The pharmacy courier <strong>were</strong> scheduled to collect prescriptions at noon.
</div>""",
        "proofreading_errors": [
            "Change plural verb to singular: 'have' -> 'has' ('Dr Patel has arrived')",
            "Change plural past verb to singular: 'were' -> 'was' ('The first patient was waiting')",
            "Change plural verb to singular: 'have' -> 'has' ('Her medical chart has been')",
            "Change plural present verb to singular: 'are' -> 'is' ('The monitor is')",
            "Change plural past verb to singular: 'were' -> 'was' ('The courier was scheduled')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing a single piece of equipment or a single person at work or college. Use singular verbs ending in 's' (e.g. <em>is, was, has</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 20
    # -------------------------------------------------------------
    {
        "unit": 20,
        "title": "Subject-Verb Agreement — Plural (are, have, were)",
        "subtitle": "Team Rosters, Bulk Pallet Checks & Group Training Logs",
        "format": "Warehouse Team Shift Roster & Pallet Log",
        "anchor_title": "Coordinating Verbs for Teams, Groups & Multiple Items",
        "anchor_text": "When you report on teams of people, multiple delivery boxes, or several machines, the subject is plural. Plural subjects require plural verbs: 'are' (present), 'were' (past), and 'have'. Using 'the boxes was delivered' is non-standard English and will cost you marks in writing assessments.",
        "formula_title": "Core Syntax Architecture: The Plural Team Framework",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">2+ People / Objects / Plural Noun</span>
  <span>+</span>
  <span class="fpill fpill-verb">are / were / have</span>
  <span>+</span>
  <span class="fpill fpill-clause">Predicate Information</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Plural Present 'To Be':</strong> <em>The boxes <strong>are</strong> ready. The trainees <strong>are</strong> in the workshop.</em></li>
  <li><strong>Plural Past 'To Be':</strong> <em>The deliveries <strong>were</strong> on time. Both doors <strong>were</strong> open.</em> (Never 'was').</li>
  <li><strong>Plural 'To Have':</strong> <em>The managers <strong>have</strong> signed the agreement.</em></li>
  <li><strong>Compound Subjects (X and Y):</strong> Two singular people joined by 'and' make a plural subject: <em>Marcus and Sam <strong>were</strong> late.</em></li>
</ul>
""",
        "pitfall_text": "The delivery drivers was on break and the packages is waiting.",
        "model_text": "The delivery drivers were on break and the packages are waiting.",
        "why_text": "'Drivers' and 'packages' are plural nouns. They must pair with plural verbs: 'were' and 'are'.",
        "golden_rule": "THE TEAM RULE: Plural subjects travel in a crowd! When there are two or more people or things, use 'are', 'were', and 'have'—never use 'was' or 'is'.",
        "exercise_a": [
            ("Which sentence shows correct plural subject-verb agreement?",
             ["A) The warehouse staff was trained on fire safety.", "B) The warehouse staff were trained on fire safety.", "C) The warehouse staff is trained on fire safety yesterday."], "B"),
            ("Choose the correct verb: <em>'Both loading bays ______ fully occupied this morning.'</em>",
             ["A) was", "B) were", "C) is"], "B"),
            ("Which sentence correctly pairs a compound subject with a plural verb?",
             ["A) Liam and Sarah has completed their induction.", "B) Liam and Sarah have completed their induction.", "C) Liam and Sarah was completed their induction."], "B"),
            ("Identify the sentence with an agreement error:",
             ["A) The fire exit doors were locked.", "B) The parcels are packed securely.", "C) The forklift trucks was inspected this morning."], "C")
        ],
        "exercise_b": [
            ("Choose between 'was' and 'were'", "The safety helmets (was / were) ____________ placed in the lockers.", "The safety helmets were placed in the lockers."),
            ("Choose between 'is' and 'are'", "The weekly sales figures (is / are) ____________ ready for review.", "The weekly sales figures are ready for review."),
            ("Correct the agreement error with 'has'", "All ten candidates has passed the practical examination.", "All ten candidates have passed the practical examination.")
        ],
        "proofreading_title": "Warehouse Logistics Team Handover Briefing",
        "proofreading_scenario": "A shift coordinator drafted this morning briefing with 5 plural agreement errors. Find and fix all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
TEAM BRIEFING &bull; LOGISTICS HUB 4<br>
The new trainees <strong>was</strong> introduced to the team at 08:00. 
All heavy goods vehicles <strong>is</strong> parked in bay 7 awaiting clearance. 
The dispatch documents <strong>has</strong> been printed by admin. 
James and Rachel <strong>was</strong> assigned to inventory aisle 3. 
The loading ramps <strong>is</strong> currently undergoing routine safety checks.
</div>""",
        "proofreading_errors": [
            "Change singular past verb to plural: 'was' -> 'were' ('trainees were introduced')",
            "Change singular present verb to plural: 'is' -> 'are' ('vehicles are parked')",
            "Change singular verb to plural: 'has' -> 'have' ('documents have been printed')",
            "Change compound subject verb to plural: 'was' -> 'were' ('James and Rachel were assigned')",
            "Change singular present verb to plural: 'is' -> 'are' ('loading ramps are currently')"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> about a group of colleagues or multiple items of equipment at work or college. Use plural subjects with plural verbs (e.g. <em>are, were, have</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 21
    # -------------------------------------------------------------
    {
        "unit": 21,
        "title": "Plural Nouns — Adding -s and -es (boxes, dishes, matches)",
        "subtitle": "Supermarket Stocking, Kitchen Inventory & Hardware Supplies",
        "format": "Hardware & Catering Inventory Stock Sheet",
        "anchor_title": "Counting Multiple Items in Retail & Storage Inventories",
        "anchor_text": "In warehousing, catering, and retail, counting stock accurately requires correct plural spelling. Most English nouns simply add '-s' to form the plural. However, words ending in 'hissing' or 'buzzing' sounds (-s, -ss, -sh, -ch, -x) must add '-es' so the word can be pronounced clearly.",
        "formula_title": "Core Syntax Architecture: The Hiss & Buzz Plural Rule",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Regular Noun + -s</span>
  <span>|</span>
  <span class="fpill fpill-verb">Ends in -s, -ss, -sh, -ch, -x + -es</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Standard Plurals (+s):</strong> Most nouns: <em>pallet &rarr; pallet<strong>s</strong>, door &rarr; door<strong>s</strong>, file &rarr; file<strong>s</strong>, table &rarr; table<strong>s</strong></em>.</li>
  <li><strong>The Hissing/Buzzing Rule (+es):</strong>
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li>Ending in <strong>-x</strong>: <em>box &rarr; box<strong>es</strong>, fix &rarr; fix<strong>es</strong></em>.</li>
      <li>Ending in <strong>-sh</strong>: <em>dish &rarr; dish<strong>es</strong>, brush &rarr; brush<strong>es</strong></em>.</li>
      <li>Ending in <strong>-ch</strong>: <em>match &rarr; match<strong>es</strong>, branch &rarr; branch<strong>es</strong></em>.</li>
      <li>Ending in <strong>-s / -ss</strong>: <em>bus &rarr; bus<strong>es</strong>, glass &rarr; glass<strong>es</strong></em>.</li>
    </ul>
  </li>
</ul>
""",
        "pitfall_text": "Please stack the empty boxs and wash the dirty dishs in the sink.",
        "model_text": "Please stack the empty boxes and wash the dirty dishes in the sink.",
        "why_text": "Nouns ending in -x ('box') and -sh ('dish') require '-es' to form the plural ('boxes', 'dishes').",
        "golden_rule": "THE HISS & BUZZ RULE: If a noun ends with a hiss, buzz, or zap sound (-s, -ss, -sh, -ch, -x), add '-es'! That extra 'e' gives your tongue room to pronounce the extra syllable.",
        "exercise_a": [
            ("Which is the correct plural form of 'box'?",
             ["A) boxs", "B) boxes", "C) boxies"], "B"),
            ("Which sentence spells all plural nouns correctly?",
             ["A) The chef washed the dishes and replaced the sandwich boxes.", "B) The chef washed the dishs and replaced the sandwich boxs.", "C) The chef washed the dishies and replaced the sandwich boxies."], "A"),
            ("What is the plural of 'branch'?",
             ["A) branchs", "B) branch's", "C) branches"], "C"),
            ("Identify the misspelled plural noun:",
             ["A) glasses", "B) buss", "C) buses"], "B")
        ],
        "exercise_b": [
            ("Change the singular noun 'sandwich' to plural", "We prepared forty chicken (sandwich) ____________ for the lunch buffet.", "We prepared forty chicken sandwiches for the lunch buffet."),
            ("Change the singular noun 'brush' to plural", "The painter cleaned all paint (brush) ____________ with solvent.", "The painter cleaned all paint brushes with solvent."),
            ("Correct the spelling error: 'boxs'", "Please load twelve cardboard boxs onto the conveyor belt.", "Please load twelve cardboard boxes onto the conveyor belt.")
        ],
        "proofreading_title": "Catering & Kitchen Requisition Inventory",
        "proofreading_scenario": "A catering apprentice filled in this storeroom count sheet with 5 plural spelling errors. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
STOREROOM STOCK INVENTORY &bull; KITCHEN 2<br>
We received twenty wooden <strong>boxs</strong> containing ceramic cups. 
The kitchen porter washed all salad <strong>dishs</strong> and drinking <strong>glasss</strong>. 
Please order three new safety <strong>matchs</strong> for the gas ovens. 
All company <strong>branchs</strong> must submit their catering requisitions today.
</div>""",
        "proofreading_errors": [
            "Add '-es' to noun ending in -x: 'boxs' -> 'boxes'",
            "Add '-es' to noun ending in -sh: 'dishs' -> 'dishes'",
            "Add '-es' to noun ending in -ss: 'glasss' -> 'glasses'",
            "Add '-es' to noun ending in -ch: 'matchs' -> 'matches'",
            "Add '-es' to noun ending in -ch: 'branchs' -> 'branches'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> describing items in a storeroom, kitchen, or workshop. Use at least two plural nouns ending in <em>-es</em> (choose from: <em>boxes, dishes, glasses, matches, branches, brushes</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 22
    # -------------------------------------------------------------
    {
        "unit": 22,
        "title": "Plural Nouns — Changing -y to -ies (story -> stories)",
        "subtitle": "Delivery Depots, Local Authorities & Medical Records",
        "format": "Regional Logistics Delivery Log",
        "anchor_title": "Managing Plural Words Ending in 'Y'",
        "anchor_text": "In logistics, administration, and customer service, you regularly refer to deliveries, factories, companies, and categories. When a singular noun ends in a consonant followed by 'y', you must drop the 'y' and add '-ies'. However, if there is a vowel before the 'y', simply add '-s'.",
        "formula_title": "Core Syntax Architecture: The 'Y' Transformation Pattern",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">Consonant + y &rarr; <strong style="color:#1e40af;">-ies</strong></span>
  <span>|</span>
  <span class="fpill fpill-verb">Vowel + y &rarr; <strong style="color:#166534;">-ys (just add s)</strong></span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Consonant + Y &rarr; -ies:</strong>
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li><em>factor<strong>y</strong> &rarr; factor<strong>ies</strong></em> &bull; <em>deliver<strong>y</strong> &rarr; deliver<strong>ies</strong></em></li>
      <li><em>cit<strong>y</strong> &rarr; cit<strong>ies</strong></em> &bull; <em>compan<strong>y</strong> &rarr; compan<strong>ies</strong></em></li>
      <li><em>cop<strong>y</strong> &rarr; cop<strong>ies</strong></em> &bull; <em>polic<strong>y</strong> &rarr; polic<strong>ies</strong></em></li>
    </ul>
  </li>
  <li><strong>Vowel + Y &rarr; just add -s:</strong> If a vowel (a, e, o) comes before 'y', keep the 'y':
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li><em>d<strong>ay</strong> &rarr; day<strong>s</strong></em> &bull; <em>k<strong>ey</strong> &rarr; key<strong>s</strong></em> &bull; <em>t<strong>oy</strong> &rarr; toy<strong>s</strong></em></li>
    </ul>
  </li>
</ul>
""",
        "pitfall_text": "Our logistics firm manages deliverys to three major citys.",
        "model_text": "Our logistics firm manages deliveries to three major cities.",
        "why_text": "'Delivery' and 'city' end in a consonant + y (r+y, t+y). The 'y' must change to '-ies'.",
        "golden_rule": "THE NEIGHBOUR CHECK RULE: Look at the letter right in front of 'y'. If it's a consonant neighbour, 'y' runs away and becomes '-ies'! If it's a vowel neighbour (a, e, o), 'y' stays put and just adds 's'.",
        "exercise_a": [
            ("Which is the correct plural form of 'factory'?",
             ["A) factorys", "B) factories", "C) factoryes"], "B"),
            ("Which sentence spells all 'y' plurals correctly?",
             ["A) We have three company policies and two office keys.", "B) We have three company policys and two office keies.", "C) We have three company policies and two office keyes."], "A"),
            ("What is the plural form of 'day'?",
             ["A) daies", "B) days", "C) day's"], "B"),
            ("Identify the misspelled plural noun:",
             ["A) cities", "B) deliveries", "C) opportunitys"], "C")
        ],
        "exercise_b": [
            ("Make 'delivery' plural", "The courier completed thirty parcel (delivery) ____________ before noon.", "The courier completed thirty parcel deliveries before noon."),
            ("Make 'company' plural", "Both partner (company) ____________ signed the commercial lease.", "Both partner companies signed the commercial lease."),
            ("Correct the spelling error: 'copys'", "Please print six copys of the fire evacuation map.", "Please print six copies of the fire evacuation map.")
        ],
        "proofreading_title": "Regional Depot Operations Memo",
        "proofreading_scenario": "A transport supervisor wrote this memo containing 5 plural spelling errors on words ending in 'y'. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
OPERATIONS MEMO &bull; REGIONAL DISTRIBUTION<br>
Our firm coordinates freight across four northern <strong>citys</strong>. 
We operate two large <strong>factorys</strong> and three parcel sorting depots. 
Drivers must collect their vehicle <strong>keies</strong> from reception each morning. 
All scheduled <strong>deliverys</strong> must be logged in the database. 
Managers should review safety <strong>policys</strong> every three months.
</div>""",
        "proofreading_errors": [
            "Change consonant+y plural: 'citys' -> 'cities'",
            "Change consonant+y plural: 'factorys' -> 'factories'",
            "Change vowel+y plural: 'keies' -> 'keys' (vowel+y just adds 's')",
            "Change consonant+y plural: 'deliverys' -> 'deliveries'",
            "Change consonant+y plural: 'policys' -> 'policies'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> about workplace organisations, cities, or goods. Use at least two plural nouns ending in <em>-ies</em> (choose from: <em>companies, deliveries, factories, cities, copies, policies</em>)."
    },

    # -------------------------------------------------------------
    # UNIT 23
    # -------------------------------------------------------------
    {
        "unit": 23,
        "title": "Common Homophones (To/Two/Too, There/Their, Hear/Here)",
        "subtitle": "Workplace Emails, Customer Notices & Direction Slips",
        "format": "Staff Noticeboard Memo & Travel Directions",
        "anchor_title": "Choosing the Right Word for the Right Meaning",
        "anchor_text": "Homophones are words that sound identical to the ear, but have completely different spellings and meanings. Using the wrong homophone in an email (such as writing 'their' instead of 'there') confuses your reader and suggests a lack of attention to detail.",
        "formula_title": "Core Syntax Architecture: The 3 Master Homophone Sets",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">To (Direction) / Two (Number 2) / Too (Also / Excess)</span>
  <span>&bull;</span>
  <span class="fpill fpill-verb">There (Place) / Their (Belongs to them) / They're (They are)</span>
  <span>&bull;</span>
  <span class="fpill fpill-clause">Hear (With ear) / Here (Location)</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>To / Two / Too:</strong>
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li><em><strong>To</strong>: Direction / verb (walk <strong>to</strong> work).</em></li>
      <li><em><strong>Two</strong>: The number 2 (<strong>two</strong> hours).</em></li>
      <li><em><strong>Too</strong>: Also or excessive (me <strong>too</strong>; <strong>too</strong> hot).</em></li>
    </ul>
  </li>
  <li><strong>There / Their:</strong>
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li><em><strong>There</strong>: Points to a place (Put it over <strong>there</strong> &mdash; contains 'here').</em></li>
      <li><em><strong>Their</strong>: Ownership (It is <strong>their</strong> van &mdash; contains 'heir').</em></li>
    </ul>
  </li>
  <li><strong>Hear / Here:</strong>
    <ul style="margin:2px 0 0 12px; padding:0;">
      <li><em><strong>Hear</strong>: Listen with your <strong>ear</strong> (I can h<strong>ear</strong> the siren).</em></li>
      <li><em><strong>Here</strong>: This exact location (Please wait <strong>here</strong>).</em></li>
    </ul>
  </li>
</ul>
""",
        "pitfall_text": "The two managers parked there car over their because it was to cold.",
        "model_text": "The two managers parked their car over there because it was too cold.",
        "why_text": "'Their' indicates ownership; 'there' indicates location; 'too' means excessively.",
        "golden_rule": "THE MEANING FINGERPRINT RULE: Look for the hidden clues: tWO has 'W' for twenty; tHEIR has 'heir' (people own it); tHERE has 'here' (places); hEAR has an 'ear' (listening)!",
        "exercise_a": [
            ("Which sentence uses 'to', 'two', and 'too' correctly?",
             ["A) The two drivers went to London, and I went too.", "B) The to drivers went two London, and I went to.", "C) The too drivers went to London, and I went two."], "A"),
            ("Choose the correct homophone: <em>'All trainees must submit ______ coursework by Friday.'</em>",
             ["A) there", "B) their", "C) they're"], "B"),
            ("Which sentence uses 'hear' and 'here' correctly?",
             ["A) Stand here so you can hear the safety announcement.", "B) Stand hear so you can here the safety announcement.", "C) Stand here so you can here the safety announcement."], "A"),
            ("Identify the sentence with a homophone error:",
             ["A) The coffee machine is too hot to touch.", "B) Please place the parcel over their on the desk.", "C) Two technicians are working in room 4."], "B")
        ],
        "exercise_b": [
            ("Choose between 'there' and 'their'", "The drivers parked (there / their) ____________ vans in the staff bay.", "The drivers parked their vans in the staff bay."),
            ("Choose between 'to', 'two', and 'too'", "Marcus walked (to / two / too) ____________ the post office before lunch.", "Marcus walked to the post office before lunch."),
            ("Choose between 'hear' and 'here'", "I could not (hear / here) ____________ the supervisor because of the engine noise.", "I could not hear the supervisor because of the engine noise.")
        ],
        "proofreading_title": "Workplace Training Noticeboard Message",
        "proofreading_scenario": "A training assistant posted this directions memo with 5 homophone errors. Locate and fix all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
TRAINING SESSION DIRECTIONS &bull; ROOM 12<br>
All apprentices should report <strong>hear</strong> at 09:00 sharp. 
Please bring <strong>two</strong> pens and your induction handbook <strong>to</strong>. 
Trainees will complete <strong>there</strong> practical assessment in the workshop. 
The room is located over <strong>their</strong>, next to the main library entrance. 
Ensure you listen carefully so you can <strong>here</strong> the emergency instructions.
</div>""",
        "proofreading_errors": [
            "Change 'hear' to location: 'hear' -> 'here'",
            "Change 'to' to meaning 'also': 'to' -> 'too'",
            "Change 'there' to possessive: 'there' -> 'their practical assessment'",
            "Change 'their' to location: 'their' -> 'there'",
            "Change location 'here' to listening: 'here' -> 'hear'"
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> giving workplace or study directions. In the first sentence, use <em>'to'</em> and <em>'two'</em> correctly. In the second sentence, use <em>'their'</em> and <em>'there'</em> correctly."
    },

    # -------------------------------------------------------------
    # UNIT 24
    # -------------------------------------------------------------
    {
        "unit": 24,
        "title": "Filling Out Application Forms with Correct Capitals & Punctuation",
        "subtitle": "Job Applications, College Enrolment & Training Declarations",
        "format": "Official Vocational Course Enrolment Application",
        "anchor_title": "Submitting Professional Application Forms & Profiles",
        "anchor_text": "An application form is often your very first contact with an employer, college, or training provider. Missing capital letters on your name or address, lowercase postcodes, and poorly punctuated personal statements can cause your application to be rejected immediately.",
        "formula_title": "Core Syntax Architecture: The Official Form Standards",
        "formula_html": """
<div class="formula-strip">
  <span class="fpill fpill-subj">[1] Block Capitals for Personal Identifiers</span>
  <span>+</span>
  <span class="fpill fpill-verb">[2] Proper Noun Capitals for Address &amp; Title</span>
  <span>+</span>
  <span class="fpill fpill-clause">[3] Full SVO Sentences in Statement Box</span>
</div>
<ul style="margin:4px 0 0 16px; padding:0; font-size:7.9pt;">
  <li><strong>Identity &amp; Address Fields:</strong> Use clear title case for names and street addresses: <em>Mr David Miller, 14 Oxford Street, Leeds</em>.</li>
  <li><strong>Postcodes &amp; Ref Numbers:</strong> Full block uppercase: <em>LS2 8JT, ULN: 4892019</em>.</li>
  <li><strong>Personal Statement / Reasons Box:</strong> Must contain full grammatical sentences with capital letters and full stops (never bulleted fragments or lowercase 'i').</li>
</ul>
""",
        "pitfall_text": "i am applying for this course because i want to improve my skills i worked in care for two years",
        "model_text": "I am applying for this course because I want to improve my skills. I have worked in care for two years.",
        "why_text": "Form statements require capital 'I' throughout, correct connectives, and clear full stops between separate thoughts.",
        "golden_rule": "THE FIRST IMPRESSION TEST: Your application form is your professional ambassador! Treat every box with respect: give names proper capitals, write postcodes in uppercase, and write personal statements in full complete sentences.",
        "exercise_a": [
            ("Which name and address entry is formatted correctly for an application form?",
             ["A) mr john davies, 12 high street, manchester, m1 4et", "B) Mr John Davies, 12 High Street, Manchester, M1 4ET", "C) Mr John Davies, 12 high street, Manchester, m1 4ET"], "B"),
            ("Which personal statement section is punctuated correctly?",
             ["A) I am reliable and hardworking. I want to gain my Level 1 qualification.", "B) i am reliable and hardworking i want to gain my level 1 qualification.", "C) I am reliable and hardworking, I want to gain my Level 1 qualification."], "A"),
            ("What is wrong with this application form entry: <em>'TITLE: mr, SURNAME: Taylor, POSTCODE: cv1 2aa'</em>?",
             ["A) 'Taylor' should be lowercase", "B) 'mr' should be 'Mr' and postcode should be 'CV1 2AA'", "C) Everything is correct"], "B"),
            ("Identify the acceptable sentence for an application reasons box:",
             ["A) Because I enjoy helping older people and want to work in a care home.", "B) I enjoy helping older people, so I want to train as a care assistant.", "C) Enjoy helping older people and want to train as a care assistant."], "B")
        ],
        "exercise_b": [
            ("Format the applicant details with correct capitals", "applicant: mrs aisha khan, 45 station road, birmingham, b2 4nd", "Applicant: Mrs Aisha Khan, 45 Station Road, Birmingham, B2 4ND"),
            ("Fix the run-on statement in this form box", "i have three years of warehouse experience i hold a valid forklift licence.", "I have three years of warehouse experience. I hold a valid forklift licence."),
            ("Punctuate the application goal statement", "i want to enrol on this course because i want to secure a promotion.", "I want to enrol on this course because I want to secure a promotion.")
        ],
        "proofreading_title": "Adult College Enrolment & Personal Statement Form",
        "proofreading_scenario": "A prospective student completed this college application box with 5 SPaG errors. Correct all 5.",
        "proofreading_text": """<div style="font-family:'Courier New',monospace; font-size:8pt; line-height:1.45;">
APPLICATION FORM &bull; SECTION 3: REASONS FOR APPLYING<br>
APPLICANT: <strong>mark stevens</strong> &bull; POSTCODE: <strong>ls12 4re</strong><br>
STATEMENT: <strong>i</strong> am applying for the health and social care course at the leeds centre. 
I have worked as a hospital volunteer for two years <strong>and</strong> I really enjoy assisting patients. 
This qualification will help me gain full-time employment <strong>so</strong> I can support my family.
</div>""",
        "proofreading_errors": [
            "Capitalise applicant full name: 'mark stevens' -> 'Mark Stevens'",
            "Capitalise postcode letters: 'ls12 4re' -> 'LS12 4RE'",
            "Capitalise pronoun and sentence start: 'i am applying' -> 'I am applying'",
            "Capitalise city proper noun: 'leeds centre' -> 'Leeds Centre'",
            "Ensure statement ends with a firm full stop."
        ],
        "writing_prompt": "Write <strong>two complete sentences</strong> for a job or college application form explaining why you want to enrol on a training programme. Use correct capital letters, the pronoun 'I', and a connective (<em>because</em> or <em>so</em>)."
    }
]

print(f"Generated {len(units_data)} units successfully.")
