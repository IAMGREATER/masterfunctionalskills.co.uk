# Enrichment blocks for Functional Skills English Reading topics to guarantee >= 30 questions per worksheet.
# Covers all 19 reading topics with authentic vocational contexts (Healthcare, retail, hospitality, office administration, logistics).

ENRICHMENT_ENGLISH_READING = {
    "reading-fact-or-opinion": [
        {
            "title": "Question 3: Distinguishing Workplace Facts from Subjective Opinions",
            "instruction": "Identify whether each statement is a Fact (verifiable evidence) or an Opinion (belief/view):",
            "items": [
                ("a", "The staff canteen opens from 07:30 to 14:00 Monday to Friday.", "Fact"),
                ("b", "The canteen offers the most delicious and comforting hot soups in the county.", "Opinion"),
                ("c", "All warehouse operatives must complete fire drill induction prior to their first shift.", "Fact"),
                ("d", "Working night shifts is much more stressful and demanding than day shifts.", "Opinion"),
                ("e", "The electric forklift was fully recharged at 06:15 this morning.", "Fact"),
                ("f", "Our team leader is undeniably the fairest and most supportive manager in the company.", "Opinion"),
                ("g", "NHS guidelines recommend washing hands with soap and warm water for at least 20 seconds.", "Fact"),
                ("h", "Hand sanitizer feels far nicer on the skin than standard anti-bacterial soap.", "Opinion")
            ]
        },
        {
            "title": "Question 4: Identifying Subtle Bias and Evaluative Vocabulary in Customer Feedback",
            "instruction": "Classify the statement as Fact, Opinion, or Mixed/Evaluative:",
            "items": [
                ("a", "Our customer satisfaction rating reached 94% following the training seminar.", "Fact"),
                ("b", "Our team provides an unmatched, world-class standard of personal attention.", "Opinion"),
                ("c", "The order was dispatched on Tuesday, which was far too late for our urgent event.", "Mixed (Date is fact; 'far too late' is opinion/judgement)"),
                ("d", "Over 250 patients attended the minor injuries triage clinic last weekend.", "Fact"),
                ("e", "The modern digital booking portal is needlessly complicated and frustrating to use.", "Opinion"),
                ("f", "Room temperature in the medical sample lab is monitored continuously at 4°C.", "Fact"),
                ("g", "Electric vans are obviously superior in every possible way to traditional diesel vans.", "Opinion"),
                ("h", "The company turnover increased by 8.4% during the last financial quarter.", "Fact")
            ]
        },
        {
            "title": "Question 5: Exam-Style Fact vs Opinion Detection in Complex Passages",
            "instruction": "Determine whether each quotation from an official inspection report is Fact or Opinion:",
            "items": [
                ("a", "'Inspectors noted four fire doors were obstructed by empty cardboard crates.'", "Fact"),
                ("b", "'The maintenance crew appeared unmotivated and disinterested during the walkthrough.'", "Opinion"),
                ("c", "'All clinical medicine storage cabinets were fitted with biometric digital locks.'", "Fact"),
                ("d", "'The vibrant blue colour scheme creates an exceptionally tranquil healing environment.'", "Opinion"),
                ("e", "'Accident logbooks documented 14 minor slip incidents during the winter months.'", "Fact"),
                ("f", "'The reception area is thoroughly unwelcoming and poorly laid out for elderly visitors.'", "Opinion"),
                ("g", "'The facility has been in continuous operation since November 2012.'", "Fact"),
                ("h", "'The catering contractor provides substandard meals that fail to nourish patients.'", "Opinion")
            ]
        }
    ],

    "reading-language-features": [
        {
            "title": "Question 3: Identifying Figurative Language & Stylistic Devices",
            "instruction": "Name the specific language device used in each excerpt (e.g. Metaphor, Simile, Alliteration, Personification, Rhetorical Question):",
            "items": [
                ("a", "'The warehouse was an absolute beehive of non-stop festive activity.'", "Metaphor"),
                ("b", "'The medical scanner hummed quietly like a gentle summer breeze.'", "Simile"),
                ("c", "'Fast, friendly, and faultless customer care every single day.'", "Alliteration / Rule of Three"),
                ("d", "'Why should hardworking care staff accept unfair scheduling changes?'", "Rhetorical Question"),
                ("e", "'The cold wind whispered through the drafty ambulance bay.'", "Personification"),
                ("f", "'Don't throw your hard-earned savings down the drain on overpriced software.'", "Idiom / Metaphor"),
                ("g", "'Safe, secure, and supportive living spaces for independent seniors.'", "Rule of Three / Alliteration"),
                ("h", "'Are you truly prepared for the new data compliance audit?'", "Rhetorical Question")
            ]
        },
        {
            "title": "Question 4: Emotive Language & Persuasive Devices in Workplace Campaigns",
            "instruction": "Identify the persuasive device and explain its emotional impact on the reader:",
            "items": [
                ("a", "'Vulnerable patients suffer in agony while bureaucracy stalls basic decisions.'", "Emotive language (evokes sympathy and moral urgency)"),
                ("b", "'Over 98% of surveyed NHS apprentices reported increased career confidence.'", "Statistical evidence / Expert appeal (builds credibility and trust)"),
                ("c", "'Join our caring family and make an unforgettable difference to a lonely elder today.'", "Direct address / Emotive vocabulary (creates personal obligation)"),
                ("d", "'Act immediately! Only five subsidised training places remain this term!'", "Urgency / Scarcity appeal (compels prompt action)"),
                ("e", "'We cannot stand by while our beloved local healthcare clinic is stripped of funds.'", "Inclusive pronouns / Emotive words (fosters team solidarity)"),
                ("f", "'Drastic, devastating cuts will inevitably destroy patient aftercare services.'", "Hyperbole / Strong emotive adjectives (creates fear/alarm)"),
                ("g", "'Thousands of local families rely wholeheartedly on our community transport.'", "Appeal to community values / Hyperbolic scale (reinforces social importance)"),
                ("h", "'Why risk your team's physical safety when certified training takes just one hour?'", "Rhetorical question (makes non-compliance seem irrational)")
            ]
        },
        {
            "title": "Question 5: Analyzing Imperatives & Professional Jargon",
            "instruction": "Identify the tone and linguistic function of each statement:",
            "items": [
                ("a", "'Ensure all sterile surgical packs are stored upright in dry conditions.'", "Imperative command (clear instructional compliance)"),
                ("b", "'Submissions received after 17:00 will strictly not be processed.'", "Formal authoritative tone (firm boundary/consequence)"),
                ("c", "'Deploy proactive mitigation strategies to reduce quarterly KPI deficits.'", "Corporate jargon / Specialist register (formal business communication)"),
                ("d", "'Please kindly remember to log out of shared clinical terminals after use.'", "Polite request / Semi-formal directive (workplace etiquette)"),
                ("e", "'Failure to wear eye protection will result in immediate disciplinary suspension.'", "Regulatory command / Warning tone (enforces legal safety standard)"),
                ("f", "'Always verify the patient's full name, NHS number, and date of birth.'", "Imperative / Procedural mandate (eliminates clinical error)"),
                ("g", "'We warmly invite feedback from all ward housekeeping team members.'", "Inviting / Inclusive tone (encourages open communication)"),
                ("h", "'Notify line management immediately should cold storage exceed 8°C.'", "Urgent conditional imperative (critical emergency protocol)")
            ]
        }
    ],

    "reading-investigating-layout": [
        {
            "title": "Question 3: Organizational Features & Navigation Aids",
            "instruction": "State the organizational layout feature described and its practical reading benefit:",
            "items": [
                ("a", "Short bulleted points outlining emergency evacuation procedures", "Bullet points (allows rapid scanning in urgent emergencies)"),
                ("b", "A distinct shaded sidebar displaying out-of-hours telephone contacts", "Text box / Sidebar (separates key contact data for instant retrieval)"),
                ("c", "Bold headings separating distinct policy sections (e.g. Sick Leave, Holiday Entitlement)", "Headings / Subheadings (structures text and aids quick navigation)"),
                ("d", "A chronological timeline highlighting key rollout milestone dates", "Timeline / Process chart (clarifies sequence of events visually)"),
                ("e", "Underlined hyperlinked text leading to downloadable HR policy documents", "Hyperlinks (connects reader directly to supplementary resources)"),
                ("f", "A bold callout box containing a clinical hazard warning icon", "Callout box / Warning icon (draws eye immediately to safety critical information)"),
                ("g", "A two-column comparison table contrasting old and new shift patterns", "Table (enables clear, side-by-side comparative analysis)"),
                ("h", "Numbered step-by-step instructions for operating an autoclave sterilizer", "Numbered list (ensures actions are followed in exact sequential order)")
            ]
        },
        {
            "title": "Question 4: Font Formatting, Hierarchy & White Space",
            "instruction": "Explain why the graphic designer or writer selected the specific typographical choice:",
            "items": [
                ("a", "Using 24pt bold sans-serif font for the document title", "Establishes clear visual hierarchy and immediate subject clarity"),
                ("b", "Printing warning text in bold red lettering within a caution border", "Alerts reader to danger and signals high priority compliance"),
                ("c", "Including generous white margins and line spacing around complex text", "Improves legibility, reduces cognitive fatigue, and supports dyslexia readers"),
                ("d", "Using italics for Latin botanical plant names in a gardening catalogue", "Distinguishes scientific taxonomy from common conversational names"),
                ("e", "Placing key performance indicators (KPIs) in large, colorful graphic tiles", "Enables rapid dashboard comprehension for busy workplace executives"),
                ("f", "Capitalizing all letters in 'DANGER: HIGH VOLTAGE' on electrical switchgear", "Maximizes legibility from a distance and conveys extreme urgency"),
                ("g", "Using a soft grey background for secondary terms and conditions footnotes", "Signals non-core supplementary information without distracting from main content"),
                ("h", "Aligning monetary prices to the right-hand margin in a trade quotation", "Facilitates quick vertical scanning and column arithmetic")
            ]
        },
        {
            "title": "Question 5: Digital Layout & Online Reading Tools",
            "instruction": "Identify the digital layout element and how it aids online user experience:",
            "items": [
                ("a", "A sticky top navigation bar that stays fixed as the user scrolls down", "Maintains constant access to main menu sections on long web pages"),
                ("b", "An expandable FAQ accordion drawer that opens on user tap/click", "Reduces visual clutter while keeping detailed answers readily accessible"),
                ("c", "A breadcrumb trail: Home > Healthcare > Policies > Infection Control", "Shows user location in site hierarchy and offers one-click backward navigation"),
                ("d", "A floating 'Back to Top' button in the bottom-right corner", "Saves user time returning to the document header on mobile devices"),
                ("e", "A prominent search bar with auto-suggest query capabilities", "Allows users to pinpoint specific technical topics without browsing menus"),
                ("f", "Responsive single-column reflow on narrow smartphone screens", "Prevents awkward horizontal scrolling and keeps text comfortably readable"),
                ("g", "Interactive progress bar indicating 60% completion of an online module", "Provides motivating visual feedback regarding task progress"),
                ("h", "Tooltips displaying definitions when hovering over clinical abbreviations", "Clarifies technical jargon without cluttering the primary sentence structure")
            ]
        }
    ],

    "reading-investigating-image": [
        {
            "title": "Question 3: Interpreting Infographics & Visual Data Displays",
            "instruction": "Identify what information the graphic communicates and why a visual is used rather than words alone:",
            "items": [
                ("a", "A pie chart showing proportion of hospital waste that is recycled vs incinerated", "Pie chart shows parts of a whole instantly; visual proportions are easier to grasp than raw percentages"),
                ("b", "A colour-coded map of a multi-storey hospital showing department locations", "Floor plan / Map helps visitors orient themselves and plan physical walking routes quickly"),
                ("c", "A line graph showing monthly staff sickness absence rates over five years", "Line graph reveals trends, seasonal spikes, and patterns over time at a glance"),
                ("d", "A photograph of a completed sterile tray setup before minor surgery", "Photo provides an unambiguous visual standard for nurses setting up clinical trays"),
                ("e", "An exploded diagram of an industrial vacuum cleaner showing filter placement", "Diagram clarifies internal spatial relationships that would be awkward to describe in words"),
                ("f", "A bar chart comparing customer ratings across four regional car dealerships", "Bar chart allows instant horizontal or vertical height comparisons between discrete categories"),
                ("g", "A visual flow chart mapping patient triage steps from arrival to doctor consultation", "Flow chart outlines decision logic (Yes/No branches) clearly for triage practitioners"),
                ("h", "A high-resolution photograph of correct PPE donning order on a locker room poster", "Photo ensures immediate recall and compliance among multi-lingual staff")
            ]
        },
        {
            "title": "Question 4: Purpose & Impact of Promotional & Editorial Images",
            "instruction": "Analyze the emotional impact or rhetorical purpose of the visual:",
            "items": [
                ("a", "A photograph of an apprentice proudly holding their qualification certificate", "Inspirational / Promotional: encourages prospective students to enroll"),
                ("b", "A stark image of a severely damaged car wheel rim next to an article on potholes", "Evidence / Persuasive: reinforces the severity and financial cost of road neglect"),
                ("c", "A smiling nurse gently holding an elderly resident's hand in a care home leaflet", "Reassuring: conveys warmth, compassionate care, and personal dignity to family members"),
                ("d", "A close-up image of fresh, brightly coloured organic vegetables on a supermarket website", "Appetizing / Commercial: entices shoppers and emphasizes freshness and healthiness"),
                ("e", "An infographic displaying five trees saved for every tonne of office paper recycled", "Motivational: translates abstract environmental data into tangible, rewarding achievements"),
                ("f", "A dramatic photo of empty shelves in a supermarket during a supply chain disruption", "Alarming / Editorial: dramatizes the urgency of logistics resilience in news reporting"),
                ("g", "A graphic of a padlock next to an online banking login button", "Security / Reassurance: instils confidence that transactions are encrypted and protected"),
                ("h", "A cartoon character with a bandage smiling next to a children's dental clinic notice", "Disarming / Friendly: reduces anxiety for young patients visiting the surgery")
            ]
        },
        {
            "title": "Question 5: Critiquing Images & Detecting Misleading Graphics",
            "instruction": "Explain how the visual choice might mislead, confuse, or distort the reader's understanding:",
            "items": [
                ("a", "A bar chart with a vertical y-axis that starts at 80% rather than 0%", "Truncated axis exaggerates tiny differences, making slight increases look enormous"),
                ("b", "A 3D pie chart tilted towards the viewer where the front slice appears much larger", "Perspective distortion tricks the eye into thinking the foreground category is bigger than it is"),
                ("c", "Using a stock photo of an ultra-modern glass laboratory for an underfunded rural clinic", "Misrepresents reality, giving potential clients false expectations of facilities"),
                ("d", "A line graph showing sales growth where the time intervals on the x-axis are uneven", "Distorts the rate of growth by compressing long slow periods and stretching short spikes"),
                ("e", "Pictograms where larger quantities use larger icons rather than more icons of the same size", "Scaling area/volume instead of height cubes the visual impact, dramatically overstating differences"),
                ("f", "An image of diverse happy workers placed on a brochure for a company with no diversity", "Tokenism / Misleading branding: conveys an inaccurate impression of workplace culture"),
                ("g", "A product photo on packaging showing serving suggestions with ingredients not in the box", "May mislead consumers regarding actual contents unless clearly labelled 'Serving Suggestion'"),
                ("h", "Using red shading for positive profits and green shading for financial losses on a report", "Violates intuitive colour associations, causing readers to misinterpret financial trends")
            ]
        }
    ],

    "reading-meaning": [
        {
            "title": "Question 3: Deciphering Contextual & Polysemic Words",
            "instruction": "State the exact meaning of the word as used in the given sentence:",
            "items": [
                ("a", "'The patient was discharged after making satisfactory progress.' (discharged)", "Officially permitted to leave the hospital / clinical facility"),
                ("b", "'The battery discharged completely overnight due to a loose wire.' (discharged)", "Lost electrical charge / power drained completely"),
                ("c", "'The logistics director gave clear direction to the warehouse crew.' (direction)", "Instruction, guidance, or authoritative operational orders"),
                ("d", "'The delivery driver took the wrong direction at the junction.' (direction)", "Physical course or path along which someone moves"),
                ("e", "'Please file all accident report sheets in the green cabinet.' (file)", "To store or catalogue physical documents systematically"),
                ("f", "'The union representative decided to file an official grievance.' (file)", "To officially submit or lodge a formal workplace complaint"),
                ("g", "'The firm offers a comprehensive package of employee benefits.' (package)", "A collection or bundle of related perks and entitlements"),
                ("h", "'Handle the fragile medical diagnostic package with extreme care.' (package)", "A parcel or wrapped container containing physical goods")
            ]
        },
        {
            "title": "Question 4: Connotation, Denotation & Nuanced Synonyms",
            "instruction": "Explain the difference in connotation between the two underlined words in context:",
            "items": [
                ("a", "'She is a shrewd negotiator' vs 'She is a cunning negotiator'", "'Shrewd' has positive connotations of astute business intelligence; 'cunning' implies deceitful trickery"),
                ("b", "'The product was inexpensive' vs 'The product was cheap'", "'Inexpensive' suggests good value for money; 'cheap' implies inferior quality and poor durability"),
                ("c", "'An assertive team supervisor' vs 'An aggressive team supervisor'", "'Assertive' indicates confident, fair leadership; 'aggressive' implies hostile and intimidating behaviour"),
                ("d", "'A cautious financial manager' vs 'A cowardly financial manager'", "'Cautious' connotes sensible prudence and risk control; 'cowardly' connotes irrational timidity"),
                ("e", "'The meeting was brief' vs 'The meeting was rushed'", "'Brief' suggests concise, efficient time management; 'rushed' implies careless haste and missed items"),
                ("f", "'A curious apprentice' vs 'A nosy apprentice'", "'Curious' suggests an eager desire to learn; 'nosy' implies prying into inappropriate personal matters"),
                ("g", "'Demanding customers' vs 'Fastidious customers'", "'Demanding' suggests burdensome and unreasonable pressure; 'fastidious' indicates high standards of precision"),
                ("h", "'A vintage workplace policy' vs 'An obsolete workplace policy'", "'Vintage' has positive nostalgic charm; 'obsolete' means totally outdated, useless, and superseded")
            ]
        },
        {
            "title": "Question 5: Interpreting Subtext & Implied Meaning",
            "instruction": "Explain what the speaker or writer is actually implying without saying it outright:",
            "items": [
                ("a", "'While some managers leave at five, Sarah is still reviewing safety logs at seven.'", "Implies Sarah is exceptionally dedicated and hard-working compared to her peers"),
                ("b", "'The new inventory system works well when the network miraculously stays online.'", "Implies the computer network crashes frequently and is fundamentally unreliable"),
                ("c", "'I was surprised to see how clean the warehouse floor was during the audit.'", "Implies the warehouse is usually dirty or untidy on ordinary working days"),
                ("d", "'Our previous supplier was certainly very colourful with their delivery estimates.'", "Implies the previous supplier lied or was untrustworthy regarding delivery times"),
                ("e", "'It is interesting that you chose not to mention the inventory deficit in your summary.'", "Implies deliberate omission, concealment, or evasion of an important problem"),
                ("f", "'We look forward to seeing your project completed by the revised deadline.'", "Subtly reminds the worker that they have already missed the original deadline"),
                ("g", "'He has plenty of enthusiasm, even if technical expertise is still developing.'", "Politely implies that he lacks the necessary skills and technical competence right now"),
                ("h", "'Thank you for returning the equipment in the condition you deemed acceptable.'", "Subtly signals strong dissatisfaction with how dirty or damaged the returned gear is")
            ]
        }
    ],

    "reading-point-of-view-and-line-of-argument": [
        {
            "title": "Question 3: Identifying the Writer's Perspective & Stance",
            "instruction": "State whether the writer is For, Against, or Neutral towards the topic in each extract:",
            "items": [
                ("a", "'Mandatory weekend shifts destroy family life and cause dangerous levels of burnout.'", "Against (opposes mandatory weekend working)"),
                ("b", "'Weekend coverage ensures vulnerable hospital patients receive vital uninterrupted care.'", "For (supports weekend staffing)"),
                ("c", "'The consultation document lists both potential staffing costs and projected patient outcomes.'", "Neutral (objective informational presentation)"),
                ("d", "'Electric delivery vans are an expensive gimmick with completely unproven battery life.'", "Against (skeptical of electric vehicle adoption)"),
                ("e", "'Transitioning our fleet to zero-emission vehicles will drastically cut city pollution.'", "For (advocates fleet electrification)"),
                ("f", "'Quarterly vehicle running logs recorded mileage, fuel consumption, and battery degradation.'", "Neutral (presents factual data without value judgements)"),
                ("g", "'Zero-hours contracts provide invaluable flexibility for university students balancing studies.'", "For (defends flexible casual contracts)"),
                ("h", "'Casual workers face chronic financial insecurity and lack basic sick pay entitlements.'", "Against (criticizes casual employment practices)")
            ]
        },
        {
            "title": "Question 4: Deconstructing Arguments & Tracing Logic",
            "instruction": "Identify the Premise (evidence) and the Conclusion (claim) in each argument:",
            "items": [
                ("a", "'Slip accidents increased by 40% during wet weather; therefore, anti-slip mats must be installed.'", "Premise: accidents increased by 40%. Conclusion: anti-slip mats must be installed."),
                ("b", "'Staff morale has fallen since flexible hours were cancelled, so management should reinstate them.'", "Premise: morale dropped after cancellation. Conclusion: management should reinstate flexible hours."),
                ("c", "'Fuel prices are at historic highs, which means the logistics team must optimize delivery routes.'", "Premise: record fuel prices. Conclusion: logistics team must optimize routes."),
                ("d", "'Automated checkouts reduce queuing times by 3 minutes, proving they enhance customer service.'", "Premise: queues reduced by 3 minutes. Conclusion: checkouts enhance customer service."),
                ("e", "'Apprentices who receive weekly mentor support achieve higher pass marks, so mentoring is essential.'", "Premise: mentored apprentices achieve higher marks. Conclusion: weekly mentoring is essential."),
                ("f", "'Online training modules save £12,000 annually in venue hire, making digital training cost-effective.'", "Premise: modules save £12,000 in venue hire. Conclusion: digital training is cost-effective."),
                ("g", "'Customer complaints doubled after packaging changed, showing the new boxes are inadequate.'", "Premise: complaints doubled post-change. Conclusion: new packaging is inadequate."),
                ("h", "'Regular maintenance prevents catastrophic machine breakdowns, so monthly checks are imperative.'", "Premise: maintenance stops breakdowns. Conclusion: monthly checks are imperative.")
            ]
        },
        {
            "title": "Question 5: Evaluating Counterarguments & Concessions",
            "instruction": "Identify the Concession (point acknowledged) and the Rebuttal (counter-punch):",
            "items": [
                ("a", "'Although solar panels have high upfront costs, they save tens of thousands in long-term power bills.'", "Concession: high upfront costs. Rebuttal: saves tens of thousands long-term."),
                ("b", "'While remote work may reduce spontaneous office chats, it dramatically boosts individual productivity.'", "Concession: reduces spontaneous chats. Rebuttal: dramatically boosts productivity."),
                ("c", "'Even though electronic logbooks require staff training, they eliminate catastrophic clinical drug errors.'", "Concession: requires staff training. Rebuttal: eliminates fatal drug errors."),
                ("d", "'Despite initial customer resistance to self-service kiosks, 85% of shoppers now prefer using them.'", "Concession: initial customer resistance. Rebuttal: 85% now prefer using them."),
                ("e", "'Admittedly, buying organic produce increases ingredient costs, but diner loyalty rises significantly.'", "Concession: increases ingredient costs. Rebuttal: significantly builds diner loyalty."),
                ("f", "'While safety goggles can mist up in humid rooms, they prevent irreversible corneal eye damage.'", "Concession: goggles can mist up. Rebuttal: prevents irreversible blindness/eye damage."),
                ("g", "'Though electric forklifts run quietly, reversing beepers ensure complete pedestrian awareness.'", "Concession: forklifts run quietly. Rebuttal: beepers ensure complete awareness."),
                ("h", "'Even if audit preparation takes two full days, it guarantees ISO quality certification renewal.'", "Concession: preparation takes two days. Rebuttal: guarantees vital ISO certification.")
            ]
        }
    ],

    "reading-presentational-features": [
        {
            "title": "Question 3: Identifying Header and Text Presentational Features",
            "instruction": "Name the presentational feature and explain how it influences the reader:",
            "items": [
                ("a", "Underlining key terms in an operating handbook", "Draws immediate visual attention to critical technical terminology"),
                ("b", "Using bulleted lists for dietary allergen ingredients", "Separates each allergen distinctly to prevent dangerous ingestion mistakes"),
                ("c", "Placing an excerpt inside an eye-catching coloured quotation callout box", "Highlights notable soundbites or testimonials to enhance credibility"),
                ("d", "Using an exclamation mark inside a yellow triangle symbol", "Instantly signifies danger or physical hazard according to universal safety code"),
                ("e", "Dividing a long staff handbook into numbered sections with bold headings", "Structures document logically and allows quick indexing and scanning"),
                ("f", "Printing critical contact numbers in enlarged bold typeface at the top of the page", "Ensures immediate readability during time-critical emergency situations"),
                ("g", "Placing a watermark across a draft contract stating 'CONFIDENTIAL - DRAFT'", "Prevents accidental public distribution and signals legal sensitivity"),
                ("h", "Using a horizontal dividing rule line between different job vacancy listings", "Clearly demarcates boundaries between separate job adverts on a noticeboard")
            ]
        },
        {
            "title": "Question 4: Presentational Design for Accessibility & Inclusion",
            "instruction": "Explain how the design choice improves accessibility for all readers, including dyslexia:",
            "items": [
                ("a", "Using dark navy text on an off-white cream or soft pastel background", "Reduces harsh screen glare and visual stress, making reading far more comfortable"),
                ("b", "Selecting a clean sans-serif font such as Arial, Calibri, or OpenDyslexic", "Prevents visual crowding and confusion between ornate serif letter hooks"),
                ("c", "Left-aligning text rather than fully justifying both left and right margins", "Avoids uneven gaps and 'rivers of white space' that disorient dyslexic readers"),
                ("d", "Maintaining line spacing of 1.5 with distinct paragraph spacing", "Stops reader's eyes from accidentally jumping to adjacent text lines"),
                ("e", "Adding alternative text (alt-text) descriptions behind all digital website images", "Allows screen readers to describe images to visually impaired users"),
                ("f", "Providing high contrast between text and background colours (at least 4.5:1 ratio)", "Ensures people with low vision or colour blindness can comfortably read content"),
                ("g", "Keeping line lengths between 60 to 70 characters per line", "Prevents eye strain from tracking across excessively wide widescreen displays"),
                ("h", "Using clear bolding rather than italics or underlining for emphasis", "Italics cause letters to slant and blur together; bolding preserves letter shapes")
            ]
        },
        {
            "title": "Question 5: Exam-Style Evaluation of Presentational Choices",
            "instruction": "Evaluate why the author selected this specific presentation for the target audience:",
            "items": [
                ("a", "A vibrant full-page glossy image on the front of an apprenticeship prospectus", "Catches teenager/school leaver attention and projects an exciting vocational future"),
                ("b", "A compact tri-fold leaflet format for an NHS patient advice pamphlet", "Easy for elderly patients to slip into a coat pocket or handbag after a consultation"),
                ("c", "A clean spreadsheet grid format with alternating shaded row stripes ('zebra striping')", "Allows accounts staff to scan across long numerical rows without losing their place"),
                ("d", "A high-visibility luminous yellow sticker on an electrical isolation switch", "Grabs attention immediately in dim industrial plant environments"),
                ("e", "A flow diagram with green checkmarks and red crosses for hand hygiene audits", "Communicates protocol across diverse multi-lingual healthcare teams without language barriers"),
                ("f", "A QR code prominently printed on a physical recruitment poster at a bus stop", "Allows commuters to instantly jump to the digital application form on their mobile"),
                ("g", "An index table at the end of a 50-page legal employment contract", "Enables rapid navigation directly to specific contractual clauses and appendices"),
                ("h", "A step-by-step cartoon strip demonstrating correct PPE removal technique", "Engages visual learners and makes strict compliance procedures less intimidating")
            ]
        }
    ],

    "reading-specialist-words": [
        {
            "title": "Question 3: Decoding Healthcare & Clinical Terminology",
            "instruction": "Match each specialist clinical word with its plain-English definition:",
            "items": [
                ("a", "Triage", "Prioritizing patient care based on clinical severity"),
                ("b", "Intravenous (IV)", "Administered directly into a vein"),
                ("c", "Palliative", "Care focused on relieving pain and symptoms rather than curing"),
                ("d", "Contraindication", "A medical reason why a specific drug or procedure must not be used"),
                ("e", "Sterilization", "Complete eradication of all living microorganisms and bacteria"),
                ("f", "Chronic", "Long-lasting or recurring illness that persists over time"),
                ("g", "Acute", "Sudden onset of severe symptoms requiring immediate attention"),
                ("h", "Hypertension", "Abnormally high blood pressure")
            ]
        },
        {
            "title": "Question 4: Workplace Jargon & Business Acronyms",
            "instruction": "Define the workplace acronym or business term in plain professional language:",
            "items": [
                ("a", "COSHH", "Control of Substances Hazardous to Health regulations"),
                ("b", "PPE", "Personal Protective Equipment (masks, gloves, eye protection)"),
                ("c", "KPI", "Key Performance Indicator (measurable goal to gauge performance)"),
                ("d", "GDPR", "General Data Protection Regulation (laws governing personal data privacy)"),
                ("e", "SOP", "Standard Operating Procedure (documented step-by-step workplace rules)"),
                ("f", "RIDDOR", "Reporting of Injuries, Diseases and Dangerous Occurrences Regulations"),
                ("g", "FTE", "Full-Time Equivalent (measure of employee workload comparison)"),
                ("h", "B2B / B2C", "Business-to-Business (selling to companies) vs Business-to-Consumer (public)")
            ]
        },
        {
            "title": "Question 5: Context Clues for Unfamiliar Technical Terms",
            "instruction": "Use the context clue in the sentence to deduce the meaning of the underlined specialist word:",
            "items": [
                ("a", "'The chemical was highly volatile, evaporating almost instantaneously into fumes when uncapped.'", "Volatile: easily evaporated at normal temperatures"),
                ("b", "'The boiler showed signs of corrosion, with rusted metal flaking off the pipes.'", "Corrosion: damage or wear to metal caused by chemical reaction / rust"),
                ("c", "'The logistics network was redundant, having multiple backup routes in case the main motorway closed.'", "Redundant: possessing duplicate backup systems to prevent failure"),
                ("d", "'The audit revealed several discrepancies, where stock figures failed to match physical counts.'", "Discrepancy: an inconsistency or lack of agreement between two sets of data"),
                ("e", "'The company became insolvent when debts exceeded assets and invoices went unpaid.'", "Insolvent: unable to pay debts owed; bankrupt"),
                ("f", "'The team demonstrated resilience, bouncing back quickly after the supply disruption.'", "Resilience: capacity to recover quickly from difficulties and adapt"),
                ("g", "'The new ventilation system was dormant during the winter, remaining completely unpowered.'", "Dormant: temporarily inactive or inoperative"),
                ("h", "'The medication had an analgesic effect, significantly dulling the patient's hip pain.'", "Analgesic: pain-relieving substance")
            ]
        }
    ],

    "reading-styles-of-writing-and-voice": [
        {
            "title": "Question 3: Identifying Tone and Register",
            "instruction": "Classify the register and tone of each communication (e.g. Formal, Informal, Urgent, Sarcastic, Empathetic):",
            "items": [
                ("a", "'We deeply regret the disruption caused to your morning travel plans.'", "Formal / Apologetic"),
                ("b", "'Hey folks, don't forget it's pizza Friday in the canteen! See ya there!'", "Informal / Enthusiastic"),
                ("c", "'All personnel must evacuate the premises immediately via marked fire doors.'", "Urgent / Authoritative"),
                ("d", "'Oh brilliant, another software update right in the middle of our inventory count.'", "Sarcastic / Frustrated"),
                ("e", "'We appreciate how challenging this bereavement period is for you and your family.'", "Empathetic / Compassionate"),
                ("f", "'Please find attached the quarterly financial balance sheet for your perusal.'", "Formal / Professional"),
                ("g", "'Drop whatever you are doing right now and phone head office immediately.'", "Urgent / Directive"),
                ("h", "'Can you believe how lucky we got with that last delivery slot? Total lifesaver!'", "Informal / Relieved")
            ]
        },
        {
            "title": "Question 4: Active vs Passive Voice & Professional Distance",
            "instruction": "Identify whether the sentence is written in the Active or Passive voice:",
            "items": [
                ("a", "The nurse administered the medication at 08:00 sharp.", "Active"),
                ("b", "The medication was administered at 08:00 sharp by the nurse.", "Passive"),
                ("c", "Management investigated the breach of safety protocol.", "Active"),
                ("d", "The safety breach was investigated by senior management.", "Passive"),
                ("e", "Ten pallets of medical PPE were delivered to the loading bay.", "Passive"),
                ("f", "The driver delivered ten pallets of medical PPE to the loading bay.", "Active"),
                ("g", "Mistakes were made during the initial shift handover.", "Passive (avoids assigning direct blame)"),
                ("h", "The night team made mistakes during the shift handover.", "Active")
            ]
        },
        {
            "title": "Question 5: Analyzing Writer's Voice & Personality",
            "instruction": "Describe the persona or voice projected by the writer in each extract:",
            "items": [
                ("a", "'As a veteran paramedic of twenty years, I urge parents to secure car seats properly.'", "Authoritative, trustworthy expert with first-hand experience"),
                ("b", "'I was completely terrified when the computer screen went black, but let me tell you what happened next!'", "Relatable, dramatic conversationalist who connects through vulnerability"),
                ("c", "'Our corporate mission is to pioneer synergy across multifaceted stakeholder matrices.'", "Impersonal, corporate, jargon-heavy bureaucrat"),
                ("d", "'Take a deep breath. You're not alone, and together we will take this recovery one day at a time.'", "Nurturing, calm mentor offering emotional reassurance"),
                ("e", "'No excuses, no shortcuts: wear your hard hat on site or leave immediately.'", "Strict, non-negotiable disciplinarian prioritizing site safety"),
                ("f", "'Ever wondered what goes on behind the scenes at a busy Michelin-starred restaurant? Let's take a peek.'", "Inquisitive, engaging insider welcoming the reader into an exclusive world"),
                ("g", "'Pursuant to Section 4 of the Employment Rights Act, notice is hereby served.'", "Legalistic, detached, strictly procedural formalist"),
                ("h", "'We messed up our delivery schedule yesterday, and we are working flat out to make things right.'", "Humble, accountable, authentic leader taking personal responsibility")
            ]
        }
    ],

    "reading-text-types": [
        {
            "title": "Question 3: Identifying Text Types by Purpose and Conventions",
            "instruction": "Name the text type for each scenario (e.g. Formal Letter, Email, Report, Article, Leaflet, Policy, Review):",
            "items": [
                ("a", "A document with Dear Mr Harrison, subject heading, formal paragraphs, and Yours sincerely", "Formal Letter"),
                ("b", "A folded brochure with pictures, bullet points, and helpline numbers for new parents", "Leaflet / Information Pamphlet"),
                ("c", "A document with To, From, Subject, Date, and attachments regarding a project update", "Workplace Email"),
                ("d", "An analytical document with Executive Summary, Findings, Data Tables, and Recommendations", "Business / Technical Report"),
                ("e", "A published piece with headline, byline, subheadings, and quotes exploring apprenticeships", "Feature Article / Magazine Article"),
                ("f", "An official company document detailing procedures and sanctions regarding staff sick leave", "Workplace Policy Document"),
                ("g", "A short piece on an online shopping portal giving 4 stars and evaluating product durability", "Customer Product Review"),
                ("h", "A step-by-step instructional sheet with warning symbols for assembling flat-pack shelving", "Instruction Manual / User Guide")
            ]
        },
        {
            "title": "Question 4: Primary Purpose of Different Text Types",
            "instruction": "State the primary communicative purpose of each text (Persuade, Inform, Instruct, Advise, or Entertain):",
            "items": [
                ("a", "A leaflet explaining how to apply for tax-free childcare vouchers", "Inform / Instruct"),
                ("b", "An advert urging readers to sign up for private health insurance before April", "Persuade"),
                ("c", "A humorous blog post about a trainee chef's first disastrous attempt at making soufflés", "Entertain"),
                ("d", "A clinic safety poster demonstrating the six stages of hygienic hand rubbing", "Instruct"),
                ("e", "A letter from a GP suggesting lifestyle modifications to lower cholesterol", "Advise"),
                ("f", "A brochure praising the luxurious amenities of a brand-new retirement village", "Persuade"),
                ("g", "A timetable showing weekend bus departure times from the central station", "Inform"),
                ("h", "A troubleshooting flowchart for fixing a jammed office photocopier", "Instruct / Advise")
            ]
        },
        {
            "title": "Question 5: Conventions & Audience Expectations across Text Types",
            "instruction": "Identify the missing convention or design flaw that weakens the text type:",
            "items": [
                ("a", "A formal letter of complaint that opens with 'Hey mate' and ends with 'Cheers'", "Inappropriate informal salutation and sign-off; violates formal letter etiquette"),
                ("b", "A recipe that gives cooking instructions without listing ingredient quantities first", "Missing ingredients list; forces reader to hunt through text for amounts"),
                ("c", "An emergency fire action notice written in a single unbroken 500-word paragraph", "Lacks visual hierarchy, bold headings, and bullet points needed for quick scanning"),
                ("d", "A newspaper article that contains no headline, byline, or journalistic lead sentence", "Violates journalistic structure; fails to hook reader or summarize story"),
                ("e", "A customer survey that only provides open blank essays rather than tick boxes and rating scales", "Excessive burden on respondents; lowers completion rates"),
                ("f", "A technical report that presents conclusions without providing data or findings to support them", "Unsubstantiated claims; undermines credibility of recommendations"),
                ("g", "A promotional sales email with no call-to-action button or website link", "Fails to guide user to next step; results in lost customer conversions"),
                ("h", "A medicine dosage leaflet printed in 6pt faint grey font with no subheadings", "Poor legibility; risks patient safety due to unreadable dosage instructions")
            ]
        }
    ],

    "reading-the-exam": [
        {
            "title": "Question 3: Navigating Functional Skills Reading Exam Papers",
            "instruction": "Identify the correct exam technique or rule for Pearson Edexcel Functional Skills Reading:",
            "items": [
                ("a", "Should you read the questions before reading the comprehension texts?", "Yes (reading questions first provides clear purpose and keywords to look for)"),
                ("b", "How many texts are typically provided in a Level 1 / Level 2 Reading exam paper?", "Two to three texts (often on a shared theme with differing viewpoints)"),
                ("c", "What must you always include when a question asks for 'evidence from the text'?", "Direct quotation or specific reference with quotation marks"),
                ("d", "If a question is worth 3 marks, how many distinct points or quotes should you provide?", "Three distinct points/explanations (one per mark)"),
                ("e", "Can you use your own personal general knowledge to answer comprehension questions?", "No (answers must be based strictly on information contained within the texts)"),
                ("f", "What is the consequence of failing to state which text you are quoting from in comparison questions?", "Loss of comparative marks; must clearly label 'Text A' or 'Text B'"),
                ("g", "Why should you highlight or underline keywords in both the question and the texts?", "Keeps focus sharp and prevents overlooking critical criteria or qualifiers"),
                ("h", "What should you do if you finish 15 minutes before the exam time expires?", "Proofread answers, verify quotes match text exactly, and check question instructions")
            ]
        },
        {
            "title": "Question 4: Deconstructing Exam Question Command Words",
            "instruction": "Explain what the exam command word requires the student to do:",
            "items": [
                ("a", "'Identify two language devices used by the author...'", "Name/label the devices and provide short illustrative quotes"),
                ("b", "'Compare how Text A and Text B present the issue of hybrid working...'", "Show similarities and differences between both texts, citing evidence from both"),
                ("c", "'Explain what the writer implies by the phrase...'", "Explain the subtext, hidden meaning, or nuance beyond the literal words"),
                ("d", "'Summarize the key safety precautions outlined in Text C...'", "Condense the main points concisely in your own words without minor details"),
                ("e", "'Evaluate how effectively Text A persuades the reader...'", "Judge the strength of arguments, language techniques, and evidence used"),
                ("f", "'Give two reasons why the author uses bullet points in Text B...'", "State two functional benefits of layout (e.g. rapid scanning, readability)"),
                ("g", "'Analyze the writer's perspective on electric vehicles...'", "Break down the author's stance, bias, tone, and rhetorical choices"),
                ("h", "'Deduce the meaning of the word from its context...'", "Work out the definition using surrounding clues rather than a dictionary")
            ]
        },
        {
            "title": "Question 5: Avoiding Common Exam Pitfalls",
            "instruction": "Identify the exam mistake being made and state the correct approach:",
            "items": [
                ("a", "Candidate writes: 'Text A is written nicely and uses good words.'", "Vague evaluative comment; must name specific devices (e.g. rule of three, metaphor) with quotes"),
                ("b", "Candidate quotes half a page of text instead of a concise phrase.", "Over-quoting; candidate must select the precise 3-5 word phrase that answers the question"),
                ("c", "Candidate describes their own personal car journey instead of answering from Text B.", "Basing answer on personal anecdote instead of textual evidence from the passage"),
                ("d", "Candidate answers a question about Text A by quoting exclusively from Text B.", "Misreading text references; must check which source text the question targets"),
                ("e", "Candidate leaves multiple-choice questions blank because they are unsure.", "Always select an answer; blank scores zero, while educated guessing may earn marks"),
                ("f", "Candidate writes full paragraphs for a 1-mark 'Identify' question.", "Poor time management; 1-mark identify questions need only a brief phrase or word"),
                ("g", "Candidate forgets to compare both texts in a 6-mark comparison question.", "Only discussing one text caps marks at half; must compare both sides systematically"),
                ("h", "Candidate writes in illegible handwriting or outside the designated response borders.", "Risk of unreadable scripts or missed scanning; must write legibly inside answer boxes")
            ]
        }
    ],

    "reading-why-do-writers-write": [
        {
            "title": "Question 3: Identifying Authorial Intent in Workplace & Civic Texts",
            "instruction": "State the writer's primary intent (Inform, Persuade, Instruct, Warn, Entertain, or Complain):",
            "items": [
                ("a", "'Faulty charging cables can ignite and cause devastating warehouse fires.'", "Warn"),
                ("b", "'Invest in our premier solar roofing system and slash your carbon footprint today.'", "Persuade"),
                ("c", "'To reset your system password: click settings, enter code, and confirm via SMS.'", "Instruct"),
                ("d", "'Our annual sustainability report outlines water conservation metrics for 2025.'", "Inform"),
                ("e", "'My dining experience was utterly ruined by cold soup and rude, dismissive staff.'", "Complain"),
                ("f", "'You won't believe the hilarious mix-up that happened in our laundry room yesterday!'", "Entertain"),
                ("g", "'Caution: Wet floor surfaces during cleaning operations between 06:00 and 08:00.'", "Warn"),
                ("h", "'Support our petition to safeguard local bus services from council budget cuts.'", "Persuade")
            ]
        },
        {
            "title": "Question 4: Dual and Secondary Purposes in Public Communications",
            "instruction": "Identify both the explicit (primary) purpose and the implicit (secondary) purpose:",
            "items": [
                ("a", "A council leaflet detailing recycling rules that also promotes council achievements", "Primary: Inform/instruct on recycling. Secondary: Promote council efficiency to voters."),
                ("b", "A blog post sharing 5 tips for stress relief written by a private therapist", "Primary: Advise on wellness. Secondary: Market the therapist's private clinic sessions."),
                ("c", "An airline magazine article exploring scenic hiking trails in Spain", "Primary: Entertain/inform tourists. Secondary: Persuade readers to book flights to Spain."),
                ("d", "A hospital annual review celebrating staff awards while mentioning budget shortages", "Primary: Inform and celebrate staff. Secondary: Lobby government/public for increased funding."),
                ("e", "A trade union notice explaining new pension rules while urging members to vote yes to strike", "Primary: Inform on pension changes. Secondary: Persuade members to back industrial action."),
                ("f", "A supermarket poster describing animal welfare standards on partner farms", "Primary: Inform on farming. Secondary: Reassure shoppers and enhance brand reputation."),
                ("g", "A police safety campaign about bicycle theft featuring free bike marking events", "Primary: Warn against theft. Secondary: Build positive community engagement with police."),
                ("h", "A celebrity chef's recipe book preamble sharing personal childhood memories", "Primary: Instruct on cooking. Secondary: Entertain and build emotional rapport with fans.")
            ]
        },
        {
            "title": "Question 5: Detecting Hidden Agendas & Commercial Motives",
            "instruction": "Identify how the writer's motive shapes what is included or omitted from the text:",
            "items": [
                ("a", "A pharmaceutical blog praising a new painkiller that fails to mention known side effects", "Commercial bias: highlights benefits to drive sales while omitting safety risks"),
                ("b", "A real estate brochure photographing a house on a sunny day with wide-angle lens", "Promotional bias: flatters space and light while obscuring small room sizes"),
                ("c", "A car manufacturer emphasizing electric range while burying battery replacement costs", "Sales marketing: emphasizes low running costs while hiding future maintenance expense"),
                ("d", "A private college highlighting its 95% pass rate without mentioning 50% dropped out before exams", "Selective statistics: inflates apparent success by filtering out non-completers"),
                ("e", "A fast-food company publishing nutritional guides emphasizing protein while minimizing sugar", "Reputation management: frames products as wholesome while downplaying dietary hazards"),
                ("f", "An energy supplier urging customers to switch to smart meters without noting remote disconnections", "Operational agenda: benefits supplier billing while omitting consumer privacy/disconnection risks"),
                ("g", "A candidate's election flyer listing their charity work while ignoring their voting record", "Political spin: projects compassion while avoiding controversial legislative choices"),
                ("h", "A tech firm article warning against fixing your own phone instead of visiting certified stores", "Monopoly protection: scares consumers to protect proprietary repair revenue")
            ]
        }
    ],

    "reading-comparing-texts": [
        {
            "title": "Question 3: Identifying Agreement and Disagreement Between Texts",
            "instruction": "Compare Text A and Text B and state whether they Agree, Disagree, or Focus on Different Aspects:",
            "items": [
                ("a", "Text A: 'Apprenticeships provide essential hands-on skills.' | Text B: 'Vocational training gives learners real workplace readiness.'", "Agree (both praise vocational learning benefits)"),
                ("b", "Text A: 'Electric buses are too expensive to maintain.' | Text B: 'Green buses deliver massive fuel savings over 10 years.'", "Disagree (conflicting views on financial viability)"),
                ("c", "Text A details safety equipment required on building sites. | Text B discusses legal compensation claims for site injuries.", "Different aspects of the same topic (prevention vs legal aftermath)"),
                ("d", "Text A: 'Care workers deserve higher basic wages.' | Text B: 'Care staff pay must increase to reflect their vital role.'", "Agree (both advocate pay rises for care staff)"),
                ("e", "Text A: 'Remote working isolates staff and harms teamwork.' | Text B: 'Working from home improves work-life balance and focus.'", "Disagree (conflicting perspectives on remote work)"),
                ("f", "Text A focuses on nutritional recipes for school meals. | Text B reviews government funding allowances for school kitchens.", "Different aspects (culinary content vs fiscal policy)"),
                ("g", "Text A: 'Smartphones distract students from classroom learning.' | Text B: 'Mobile devices are powerful educational research tools.'", "Disagree (opposing views on classroom technology)"),
                ("h", "Text A: 'Regular exercise reduces cardiovascular disease risks.' | Text B: 'Daily brisk walking significantly strengthens the heart.'", "Agree (both confirm physical activity protects heart health)")
            ]
        },
        {
            "title": "Question 4: Comparing Tone and Register Across Two Sources",
            "instruction": "Contrast the tone of Text A with Text B on the same topic:",
            "items": [
                ("a", "Text A: Formal NHS advisory on diabetes. | Text B: Humorous personal lifestyle blog on cutting sugar.", "Text A is authoritative, objective, and clinical; Text B is lighthearted, colloquial, and relatable"),
                ("b", "Text A: Enthusiastic sales brochure for an electric car. | Text B: Critical investigative report on lithium battery disposal.", "Text A is persuasive, upbeat, and celebratory; Text B is cautious, serious, and skeptical"),
                ("c", "Text A: Urgent union strike ballot notice. | Text B: Measured management email inviting dialogue.", "Text A is impassioned, assertive, and defiant; Text B is calm, conciliatory, and diplomatic"),
                ("d", "Text A: Emotional charity appeal featuring a rescued dog. | Text B: Government statistics on stray animal populations.", "Text A is emotive, heartwarming, and poignant; Text B is detached, factual, and analytical"),
                ("e", "Text A: Angry customer complaint about delayed flight. | Text B: Standard airline compensation terms and conditions.", "Text A is indignant, frustrated, and accusatory; Text B is legalistic, neutral, and matter-of-fact"),
                ("f", "Text A: Academic research paper on sleep deprivation. | Text B: Teen magazine article on morning routines.", "Text A is scholarly, complex, and formal; Text B is informal, punchy, and accessible"),
                ("g", "Text A: Step-by-step operating instructions for a chainsaw. | Text B: News report on a forestry work accident.", "Text A is instructive, imperative, and methodical; Text B is dramatic, sensational, and descriptive"),
                ("h", "Text A: Enthusiastic festival promotion poster. | Text B: Residents' petition against festival noise.", "Text A is vibrant, festive, and enticing; Text B is formal, concerned, and aggrieved")
            ]
        },
        {
            "title": "Question 5: Synthesizing Information & Formulating Comparative Sentences",
            "instruction": "Select the correct comparative connective (whereas, similarly, conversely, in contrast, likewise) to complete the synthesis:",
            "items": [
                ("a", "Text A highlights financial incentives, (whereas / likewise) Text B focuses on environmental benefits.", "whereas (signals contrast)"),
                ("b", "Text A warns of rising energy bills; (similarly / in contrast), Text B predicts severe winter heating costs.", "similarly (signals agreement)"),
                ("c", "Text A advocates strict disciplinary sanctions, (conversely / likewise) Text B promotes restorative mediation.", "conversely (signals opposing strategy)"),
                ("d", "Text A emphasizes technological innovation; (likewise / in contrast), Text B champions digital automation.", "likewise (signals parallel endorsement)"),
                ("e", "Text A argues that homework consolidates learning, (in contrast to / similarly to) Text B which claims it causes stress.", "in contrast to (signals direct contradiction)"),
                ("f", "Text A reports high satisfaction rates among apprentices; (similarly / conversely), Text B notes strong completion statistics.", "similarly (signals supporting evidence)"),
                ("g", "Text A recommends purchasing second-hand machinery, (whereas / likewise) Text B insists brand-new models are essential.", "whereas (signals practical disagreement)"),
                ("h", "Text A details clinical hygiene standards; (equally / in contrast), Text B outlines strict surgical sterilization rules.", "equally (signals complementary alignment)")
            ]
        }
    ],

    "detecting-language-techniques": [
        {
            "title": "Question 3: Identifying Rhetorical Devices in Persuasive Texts",
            "instruction": "Name the specific persuasive device used in each excerpt (e.g. Rule of Three, Hyperbole, Rhetorical Question, Anecdote, Statistics):",
            "items": [
                ("a", "'Over 87% of surveyed NHS workers would recommend their ward to friends.'", "Statistics / Empirical evidence"),
                ("b", "'Are we prepared to let our beloved community library close its doors forever?'", "Rhetorical question"),
                ("c", "'We will deliver cleaner streets, safer parks, and brighter futures for our youth.'", "Rule of Three / Tricolon"),
                ("d", "'This revolutionary new vacuum cleaner is a million times faster than sweeping.'", "Hyperbole / Exaggeration"),
                ("e", "'Last year, local resident Mrs Jenkins had to wait four hours in the rain for a bus.'", "Anecdote / Human interest story"),
                ("f", "'Don't let rogue cowboy builders steal your family's precious future.'", "Emotive language / Pejorative nouns"),
                ("g", "'Professor Davies, Chief Virologist at Oxford, confirms the safety of the vaccine.'", "Appeal to authority / Expert testimony"),
                ("h", "'We cannot afford to wait. We cannot afford to hesitate. We cannot afford to fail.'", "Repetition / Anaphora")
            ]
        },
        {
            "title": "Question 4: Analyzing the Functional Effect of Language Choices",
            "instruction": "Explain how the underlined phrase influences the thoughts or feelings of the reader:",
            "items": [
                ("a", "'Heartless corporate landlords are hiking rents without remorse.'", "Demonizes landlords as unfeeling villains and evokes sympathy for vulnerable tenants"),
                ("b", "'Our award-winning, state-of-the-art diagnostic equipment.'", "Reassures patients of clinical excellence and justifies higher service prestige"),
                ("c", "'Imagine returning home to a sparkling, spotless living room every evening.'", "Prompts reader to visualize a stress-free outcome, motivating them to hire cleaners"),
                ("d", "'Time is running out to claim your statutory heating allowance.'", "Instils a sense of urgency, driving eligible readers to submit applications quickly"),
                ("e", "'You hold the power to save an innocent animal's life today.'", "Empowers the reader while placing personal moral responsibility on them to donate"),
                ("f", "'A catastrophic failure of basic leadership led to this workplace tragedy.'", "Allocates clear blame to senior management and emphasizes the gravity of the incident"),
                ("g", "'Our friendly team will guide you through every single step with gentle patience.'", "Allays anxiety and reassures nervous applicants that they will not be judged"),
                ("h", "'Every single penny of your monthly subscription directly feeds a hungry child.'", "Builds trust and eliminates skepticism regarding charity administrative overheads")
            ]
        },
        {
            "title": "Question 5: Distinguishing Subtle Literary Devices in Non-Fiction",
            "instruction": "Identify the literary technique used (Oxymoron, Irony, Pun, Sibilance, Onomatopoeia):",
            "items": [
                ("a", "'The new hospital parking policy was an open secret among clinic staff.'", "Oxymoron ('open secret')"),
                ("b", "'The fire station tragically burned to the ground during the night shift.'", "Situational Irony"),
                ("c", "'Our bakery team always rises to the occasion.'", "Pun / Play on words ('rises')"),
                ("d", "'Silent, sinister shadows slipped across the clinical ward corridor.'", "Sibilance (repetition of soft 's' sounds)"),
                ("e", "'The heavy industrial press slammed down with a deafening crash.'", "Onomatopoeia ('crash', 'slammed')"),
                ("f", "'The mechanic's own car broke down on his way to work.'", "Situational Irony"),
                ("g", "'A deafening silence filled the boardroom when the deficit was announced.'", "Oxymoron ('deafening silence')"),
                ("h", "'The bee keeper described his staff as buzzing with fresh ideas.'", "Pun / Extended metaphor")
            ]
        }
    ],

    "formality-and-bias": [
        {
            "title": "Question 3: Identifying Markers of Bias and Slanted Reporting",
            "instruction": "Identify how bias is introduced in the sentence (Loaded adjectives, One-sided quotes, Omission, Generalisation):",
            "items": [
                ("a", "'Selfish striking train drivers plunged millions of innocent commuters into utter misery.'", "Loaded / Emotive adjectives ('selfish', 'innocent', 'utter misery')"),
                ("b", "'All young apprentices are lazy and lack basic timekeeping skills.'", "Sweeping generalisation / Stereotyping"),
                ("c", "'Article interviews three disgruntled passengers but quotes no representatives from the airline.'", "One-sided sourcing / Selection bias"),
                ("d", "'The council wasted millions on useless cycle lanes that nobody ever uses.'", "Exaggeration / Dismissive hyperbole ('nobody ever uses')"),
                ("e", "'The report highlights business tax cuts while omitting cuts to local hospital services.'", "Omission / Selective presentation of facts"),
                ("f", "'Greedy tech corporations are leeching wealth out of honest British high streets.'", "Pejorative metaphor / Demonizing language ('greedy', 'leeching')"),
                ("g", "'Every single resident in town strongly opposes the proposed housing development.'", "Absolutist language / False consensus ('every single resident')"),
                ("h", "'Only positive five-star customer testimonials are displayed on the marketing page.'", "Confirmation bias / Review cherry-picking")
            ]
        },
        {
            "title": "Question 4: Rewriting Biased Statements into Objective Workplace Neutrality",
            "instruction": "Replace the biased phrasing with professional, objective, balanced language:",
            "items": [
                ("a", "'The lazy cleaner didn't bother mopping the corridor properly.'", "'The corridor floor was only partially mopped during the cleaning shift.'"),
                ("b", "'The boss threw a childish tantrum during the weekly team catch-up.'", "'The department manager expressed strong frustration during the meeting.'"),
                ("c", "'Customer was screeching hysterically about a minor five-minute delay.'", "'Customer raised their voice when expressing concern regarding the five-minute delay.'"),
                ("d", "'Our brilliant software completely crushes all clunky competitor systems.'", "'Our software offers faster processing speeds than competing solutions.'"),
                ("e", "'The supplier sent useless, damaged junk to our warehouse.'", "'The delivery arrived with damaged goods that did not meet quality specifications.'"),
                ("f", "'He gave a rambling, pointless presentation that put the audience to sleep.'", "'The presentation lacked clear structure and exceeded the allocated speaking time.'"),
                ("g", "'Management tried to sneak through an unfair change to our contract.'", "'Management proposed contractual amendments without prior staff consultation.'"),
                ("h", "'The finance director fabricated ridiculous numbers to justify layoffs.'", "'The trade union contested the financial projections used to justify redundancies.'")
            ]
        },
        {
            "title": "Question 5: Identifying Register Clashes & Appropriateness",
            "instruction": "Determine whether the register is Appropriate or Inappropriate for the specified context:",
            "items": [
                ("a", "Writing 'Sup mate, need some cash back ASAP' in a formal insurance compensation claim", "Inappropriate (slang and casual idioms undermine legal claims)"),
                ("b", "Writing 'I am writing to formally request an extension to my assignment deadline' to a college tutor", "Appropriate (polite, respectful, formal academic register)"),
                ("c", "Writing 'Hey guys! Fire in the building, best head outside lol' on an emergency safety bulletin", "Inappropriate (trivialises danger and undermines emergency evacuation seriousness)"),
                ("d", "Writing 'Dear Resident, please be advised of scheduled water main maintenance on Tuesday' from a utility firm", "Appropriate (courteous, informative, professional public communication)"),
                ("e", "Writing 'That presentation was pure garbage' in an official HR peer review appraisal form", "Inappropriate (unprofessional, destructive, offensive phrasing)"),
                ("f", "Writing 'The candidate presented their portfolio with commendable clarity and technical confidence'", "Appropriate (balanced, constructive professional praise)"),
                ("g", "Using emojis like laughing tears 😂 and shrugs 🤷‍♂️ in an email responding to a patient grievance", "Inappropriate (signals mockery and lack of clinical empathy)"),
                ("h", "Writing 'We kindly remind all delegates to wear name badges throughout the conference'", "Appropriate (courteous directive suited to a corporate event)")
            ]
        }
    ],

    "piecing-it-together-comparing-texts": [
        {
            "title": "Question 3: Cross-Referencing Practical Information Across Multiple Sources",
            "instruction": "Extract and combine information from Source A and Source B to answer the query:",
            "items": [
                ("a", "Source A: Course runs Mondays 18:00-20:00. Source B: Parking fee £2.50 after 17:30. Total parking cost for 6 weeks?", "£15.00 (6 sessions × £2.50)"),
                ("b", "Source A: Tool hire is £40/day. Source B: 20% discount on rentals of 5 days or more. Cost for 5 days?", "£160.00 (5 × £40 = £200; 20% off £200 = £160)"),
                ("c", "Source A: Van holds 12 cubic metres. Source B: Delivery requires moving 30 cubic metres. How many trips?", "3 trips (12 + 12 + 6)"),
                ("d", "Source A: Shift allowance is £1.50/hr after 20:00. Source B: Operative works 16:00 to 22:00. Bonus pay?", "£3.00 (2 hours from 20:00 to 22:00 × £1.50)"),
                ("e", "Source A: Clinic opens at 08:30. Source B: Fasting blood tests must be taken within 1 hr of opening. Latest test time?", "09:30"),
                ("f", "Source A: Delivery takes 3 working days. Source B: Order placed on Thursday at 14:00. Expected delivery day?", "Tuesday (Friday, Monday, Tuesday)"),
                ("g", "Source A: Ticket costs £18. Source B: Group discount gives 1 free ticket for every 4 bought. Cost for 5 tickets?", "£72.00 (pay for 4 tickets, 5th is free)"),
                ("h", "Source A: Weight limit is 500 kg. Source B: 18 boxes weighing 25 kg each. Can the lift carry all boxes at once?", "Yes (18 × 25 kg = 450 kg, which is within the 500 kg limit)")
            ]
        },
        {
            "title": "Question 4: Resolving Conflicting Advice Across Healthcare Guidelines",
            "instruction": "Identify the discrepancy and state which protocol takes precedence according to seniority or date:",
            "items": [
                ("a", "Poster on wall (2020) says sanitize for 15s. Staff memo (2025) says sanitize for 20s. Which rule applies?", "Staff memo (2025) takes precedence as it is the most recent updated clinical guideline"),
                ("b", "Junior nurse advises hot compress; Senior consultant prescribes cold ice pack. Which action should be taken?", "Senior consultant's prescription takes clinical precedence"),
                ("c", "Brochure lists visiting hours until 20:00; Noticeboard states ward is under lockdown from 18:00. Which applies today?", "Lockdown notice on noticeboard applies immediately to protect infection control"),
                ("d", "Website FAQ says free parking on Sundays; Barrier sign states £3 Sunday fee introduced last week.", "Barrier sign takes precedence as it reflects the current operational system"),
                ("e", "General company handbook grants 25 days leave; Individual signed contract specifies 28 days. Which entitlement applies?", "Individual signed contract (legally binding personal agreement)"),
                ("f", "Manufacturer guide suggests oiling gears weekly; Senior technician notes excessive dust requires daily oiling.", "Senior technician's adaptation for environmental workplace conditions"),
                ("g", "Old printed catalog shows price as £45; Digital checkout scans at £52. What must the retailer do?", "Retailer must honor policy; digital price is legally correct unless store chooses good-will honor"),
                ("h", "Supplier email claims part arrived on Tuesday; Warehouse goods-in ledger records arrival on Thursday.", "Warehouse physical goods-in ledger provides verifiable factual delivery record")
            ]
        },
        {
            "title": "Question 5: Exam Synthesis Skills - Formulating Comparative Summaries",
            "instruction": "Draft a one-sentence comparative synthesis identifying the shared theme and differing solutions:",
            "items": [
                ("a", "Theme: Staff retention. Text A suggests higher wages; Text B proposes flexible working hours.", "While both texts address staff retention, Text A advocates higher wages whereas Text B proposes flexible hours."),
                ("b", "Theme: Reducing food waste. Text A urges supermarket discounts; Text B promotes food bank donations.", "Both texts aim to reduce food waste, but Text A focuses on commercial discounting while Text B champions charity donations."),
                ("c", "Theme: Energy costs. Text A recommends solar panels; Text B suggests building insulation upgrades.", "Although both texts tackle rising energy costs, Text A promotes solar generation whereas Text B emphasizes heat insulation."),
                ("d", "Theme: Apprentice recruitment. Text A targets school leavers; Text B recruits career changers.", "Both sources focus on hiring apprentices, but Text A targets young school leavers whereas Text B recruits mature career changers."),
                ("e", "Theme: Stress reduction. Text A advocates mindfulness apps; Text B calls for lower workplace workloads.", "While both texts explore employee stress, Text A promotes individual coping strategies whereas Text B demands workload reductions."),
                ("f", "Theme: Hospital parking. Text A complains about high charges; Text B argues charges fund clinical equipment.", "Both texts examine hospital parking fees, but Text A criticizes high costs while Text B justifies charges as vital hospital funding."),
                ("g", "Theme: Fleet transport. Text A supports electric vans; Text B favors hydrogen fuel cells.", "Both sources seek greener fleet transport, with Text A backing battery-electric vans while Text B champions hydrogen technology."),
                ("h", "Theme: Customer communication. Text A favors telephone helplines; Text B recommends AI webchat.", "While both texts discuss customer support channels, Text A prioritizes personal phone calls whereas Text B recommends automated AI chat.")
            ]
        }
    ],

    "piecing-it-together-key-and-detailed-points": [
        {
            "title": "Question 3: Distinguishing Main Ideas from Supporting Details",
            "instruction": "State whether the statement represents the Main Idea or a Supporting Detail:",
            "items": [
                ("a", "The healthcare trust must cut operational carbon emissions by 30% by 2030.", "Main Idea"),
                ("b", "Switching ward lighting to energy-efficient LED bulbs saved 4,000 kWh last quarter.", "Supporting Detail"),
                ("c", "Installing double-glazed windows in the maternity wing reduced heating loss by 12%.", "Supporting Detail"),
                ("d", "Apprenticeships significantly enhance workplace productivity and staff loyalty.", "Main Idea"),
                ("e", "A recent survey showed 82% of apprentices remain with their employer for over three years.", "Supporting Detail"),
                ("f", "Apprentice mentor programs require one hour of scheduled supervisor time per week.", "Supporting Detail"),
                ("g", "Strict adherence to hygiene protocols prevents the spread of hospital-acquired infections.", "Main Idea"),
                ("h", "Alcohol hand sanitizers must contain a minimum of 60% alcohol concentration.", "Supporting Detail")
            ]
        },
        {
            "title": "Question 4: Extracting Key Numerical and Operational Facts",
            "instruction": "Read the workplace notice excerpt and extract the exact factual data required:",
            "items": [
                ("a", "'All orders over £75 qualify for free next-day delivery.' What is the spending threshold?", "£75.00"),
                ("b", "'Staff room fridges will be defrosted every second Friday at 16:30.' What time does defrosting begin?", "16:30"),
                ("c", "'Maximum lift occupancy is 8 persons or 630 kg.' What is the maximum passenger capacity?", "8 persons"),
                ("d", "'Accident reports must be submitted within 24 hours of occurrence.' What is the submission deadline?", "Within 24 hours"),
                ("e", "'To secure the early-bird booking rate of £120, register before 31st March.' What is the cutoff date?", "31st March"),
                ("f", "'Minimum room temperature in clinical care wards must not fall below 18°C.' What is the minimum temp?", "18°C"),
                ("g", "'Employees working over 6 hours are entitled to an uninterrupted rest break of 20 minutes.' Break length?", "20 minutes"),
                ("h", "'The emergency generator provides auxiliary power for up to 72 continuous hours.' Maximum runtime?", "72 hours")
            ]
        },
        {
            "title": "Question 5: Summarizing Core Paragraph Themes in Three Words or Fewer",
            "instruction": "Condense the central theme of each paragraph into three words or fewer:",
            "items": [
                ("a", "Paragraph discussing proper lifting techniques to protect the lower spine and avoid muscle tears", "Manual handling safety"),
                ("b", "Paragraph detailing procedures for locking computer screens and storing sensitive patient case files", "Data security compliance"),
                ("c", "Paragraph explaining fire exit routes, assembly points, and designated fire warden duties", "Fire evacuation procedures"),
                ("d", "Paragraph outlining company rules regarding uniform cleanliness, ironed tunics, and ID badges", "Staff dress code"),
                ("e", "Paragraph describing mental health first aiders, counseling hotlines, and quiet wellness spaces", "Employee wellbeing support"),
                ("f", "Paragraph reviewing recycling bins, food waste composting, and paperless billing transitions", "Environmental sustainability"),
                ("g", "Paragraph setting out procedures for requesting annual leave, holiday limits, and peak period bans", "Holiday booking policy"),
                ("h", "Paragraph summarizing safety goggles, ear defenders, steel-toe boots, and high-visibility vests", "Personal protective equipment (PPE)")
            ]
        }
    ],

    "types-of-and-navigating-sources": [
        {
            "title": "Question 3: Primary vs Secondary Sources of Information",
            "instruction": "Classify each item as a Primary Source (first-hand testimony/raw data) or a Secondary Source (analysis/summary):",
            "items": [
                ("a", "An eyewitness statement from a warehouse operative regarding a forklift collision", "Primary Source"),
                ("b", "A newspaper article summarizing the court case regarding the forklift collision", "Secondary Source"),
                ("c", "The official audio recording of an emergency 999 telephone call", "Primary Source"),
                ("d", "A medical textbook explaining the treatment of crush injuries", "Secondary Source"),
                ("e", "The original handwritten clinical notes made by a paramedic at the scene", "Primary Source"),
                ("f", "A documentary film analyzing hospital emergency response times", "Secondary Source"),
                ("g", "Raw census survey data collected by the Office for National Statistics", "Primary Source"),
                ("h", "An opinion blog post critiquing the latest census figures", "Secondary Source")
            ]
        },
        {
            "title": "Question 4: Digital Navigation Tools & Website Architecture",
            "instruction": "State which navigation tool should be used for the given search task (Search bar, Site map, FAQ, Breadcrumbs, Dropdown menu):",
            "items": [
                ("a", "Looking for a specific policy form when you already know its reference number ('HR-POL-04')", "Search bar"),
                ("b", "Wanting an overarching high-level birds-eye view of all categories and pages on an intranet", "Site map"),
                ("c", "Quickly checking whether visitors are allowed to bring flowers into clinical wards", "FAQ (Frequently Asked Questions)"),
                ("d", "Returning directly to the main 'Employee Benefits' hub from a sub-page on childcare vouchers", "Breadcrumb trail"),
                ("e", "Browsing different department contact numbers grouped by clinical specialty", "Dropdown navigation menu"),
                ("f", "Pinpointing downloadable PDF terms and conditions at the bottom of every page", "Footer links"),
                ("g", "Jumping straight down to 'Section 5: Sick Pay' in a long continuous 20-page web guide", "Table of contents / Anchor links"),
                ("h", "Filtering catalogue items by price, size, and brand on an e-commerce website", "Faceted filter sidebar")
            ]
        },
        {
            "title": "Question 5: Evaluating Credibility & Source Reliability",
            "instruction": "Assess the credibility of the information source (High, Moderate, or Low) and give the reason:",
            "items": [
                ("a", "A health advice article published on the official NHS.uk website", "High (peer-reviewed, authorless, government health authority)"),
                ("b", "An unverified anonymous comment left under a tabloid newspaper article", "Low (unregulated, anonymous, prone to misinformation and bias)"),
                ("c", "A sponsored promotional blog post paid for by a diet pill manufacturer", "Low (commercial conflict of interest and unvetted claims)"),
                ("d", "A published academic study in the British Medical Journal (BMJ)", "High (rigorous peer review and methodology transparency)"),
                ("e", "A Wikipedia article on a recent breaking news story with multiple 'citation needed' flags", "Moderate/Low (editable by anyone, unverified flags indicate missing evidence)"),
                ("f", "An official statistical release by the UK Health Security Agency", "High (official statutory public data provider)"),
                ("g", "A viral TikTok video claiming lemon water cures diabetes", "Low (social media algorithm, dangerous medical inaccuracy)"),
                ("h", "A product review from a verified purchaser on a reputable trade site", "Moderate (authentic personal experience, but individual anecdotal sample)")
            ]
        }
    ],

    "assessing-the-basics": [
        {
            "title": "Question 3: Alphabetical Ordering & Filing Systems",
            "instruction": "Place the four patient or client names in correct alphabetical order (by surname):",
            "items": [
                ("a", "Smith, John; Davies, Karen; Brown, Peter; Adams, Sarah", "1. Adams, Sarah; 2. Brown, Peter; 3. Davies, Karen; 4. Smith, John"),
                ("b", "Taylor, Chris; Thomas, Mary; Turner, Alan; Thompson, Rachel", "1. Taylor, Chris; 2. Thomas, Mary; 3. Thompson, Rachel; 4. Turner, Alan"),
                ("c", "MacDonald, Ian; McDonald, Anna; MacIntyre, Fiona; Mackintosh, Donald", "1. MacDonald, Ian; 2. MacIntyre, Fiona; 3. Mackintosh, Donald; 4. McDonald, Anna"),
                ("d", "Green, David; Green, Alice; Green, Sophie; Green, Oliver", "1. Green, Alice; 2. Green, David; 3. Green, Oliver; 4. Green, Sophie"),
                ("e", "Clarke, Brian; Clark, Anthony; Clarkson, David; Clarke, Edward", "1. Clark, Anthony; 2. Clarke, Brian; 3. Clarke, Edward; 4. Clarkson, David"),
                ("f", "O'Connor, Liam; O'Brien, Patrick; O'Neill, Siobhan; O'Donnell, Ciara", "1. O'Brien, Patrick; 2. O'Connor, Liam; 3. O'Donnell, Ciara; 4. O'Neill, Siobhan"),
                ("g", "Wilson, James; Williams, Keith; Wilkinson, Laura; Williamson, Craig", "1. Wilkinson, Laura; 2. Williams, Keith; 3. Williamson, Craig; 4. Wilson, James"),
                ("h", "Jackson, Paul; Jenkins, Mark; Jarvis, Susan; Jacobs, Hannah", "1. Jacobs, Hannah; 2. Jarvis, Susan; 3. Jackson, Paul; 4. Jenkins, Mark")
            ]
        },
        {
            "title": "Question 4: Understanding Common Workplace Abbreviations & Signs",
            "instruction": "State the meaning of the common workplace sign, symbol, or abbreviation:",
            "items": [
                ("a", "'e.g.' (exempli gratia)", "For example"),
                ("b", "'i.e.' (id est)", "That is / In other words"),
                ("c", "'etc.' (et cetera)", "And so forth / And other similar things"),
                ("d", "'NB' (nota bene)", "Note well / Take special notice"),
                ("e", "A circular blue sign showing white boots", "Mandatory requirement: safety footwear must be worn"),
                ("f", "A triangular yellow sign with a black lightning bolt", "Hazard warning: danger of high voltage electricity"),
                ("g", "A square green sign showing a white cross", "First aid facility or first aid box location"),
                ("h", "A circular red sign with a diagonal line over a burning match", "Prohibition: no naked flames / smoking prohibited")
            ]
        },
        {
            "title": "Question 5: Chronological Ordering & Schedule Interpretation",
            "instruction": "Order the following daily care home events in chronological time sequence:",
            "items": [
                ("a", "14:00 Bingo in lounge; 08:30 Breakfast served; 19:00 Evening drinks; 12:30 Lunch served", "1. 08:30 Breakfast; 2. 12:30 Lunch; 3. 14:00 Bingo; 4. 19:00 Evening drinks"),
                ("b", "11:15 Mid-morning tea; 07:00 Shift handover; 16:45 Dinner prep; 09:30 Medication round", "1. 07:00 Shift handover; 2. 09:30 Medication round; 3. 11:15 Mid-morning tea; 4. 16:45 Dinner prep"),
                ("c", "22:00 Night round; 15:30 Garden walk; 10:00 Physiotherapy; 13:15 Quiet rest hour", "1. 10:00 Physiotherapy; 2. 13:15 Quiet rest; 3. 15:30 Garden walk; 4. 22:00 Night round"),
                ("d", "18:00 Dinner served; 06:30 Early wake-up; 12:00 Hydration check; 17:00 Visitor arrivals", "1. 06:30 Early wake-up; 2. 12:00 Hydration check; 3. 17:00 Visitor arrivals; 4. 18:00 Dinner served"),
                ("e", "If a prescription must be taken 'TDS' (three times daily with meals), what are reasonable times?", "08:30 (Breakfast), 12:30 (Lunch), 18:00 (Dinner)"),
                ("f", "If an operative arrives 15 minutes prior to their 07:45 shift, what time do they arrive?", "07:30"),
                ("g", "A meeting lasts 1 hour and 45 minutes starting at 10:30. What time does it conclude?", "12:15"),
                ("h", "A delivery booked for 14:15 arrives 35 minutes late. What time does it pull into the bay?", "14:50")
            ]
        }
    ]
}
