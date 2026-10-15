import os, sys, re, json

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def generate_english_content():
    print("Generating English Suite Content...")

    format_l2_models = {
        1: """<p><strong>Flat 4B, Highfield Towers, Birmingham, B15 2QU</strong><br>
18 November 2026<br><br>
<strong>Mr Julian Vance, Managing Director</strong><br>
Sovereign Facilities Management Ltd, 45 Colmore Row, Birmingham, B3 2AS<br><br>
Dear Mr Vance,<br><br>
<strong>RE: Formal Letter of Grievance &ndash; Unresolved Facilities Failures at Highfield Towers</strong><br><br>
I am writing in my capacity as Chairperson of the Highfield Residents and Tenants Association to register an urgent formal grievance regarding the unacceptable deterioration of essential services within our building. Over the past three weeks, residents &ndash; including elderly individuals, wheelchair users, and families with young infants &ndash; have endured hazardous living conditions resulting directly from administrative neglect.<br><br>
Firstly, the primary passenger elevator has remained completely inoperative for eighteen consecutive days. As a consequence, mobility-impaired residents residing on the upper six floors have been effectively confined to their homes, missing crucial medical appointments and requiring neighbours to carry heavy provisions upstairs. Furthermore, the electronic vehicular security gates have failed in the open position, compromising tenant security and resulting in unauthorised parking across designated emergency access bays. To exacerbate matters, communal domestic refuse has not been collected for a fortnight, generating significant environmental and public health hazards.<br><br>
Despite repeated logged telephone inquiries to your customer helpdesk (logged under reference FM-8821), no contractor has attended the site. Consequently, our association formally requires the following remedial measures:</p>
<ul>
  <li>Immediate deployment of emergency lift engineers to restore full elevator functionality within 24 hours.</li>
  <li>Emergency removal and sanitisation of the communal refuse storage areas by Friday 21 November.</li>
  <li>A formal written maintenance action plan outlining long-term preventative measures to avoid recurrent failures.</li>
</ul>
<p>Should these urgent rectifications not be initiated within forty-eight hours, our committee will submit a joint statutory complaint to the Environmental Health Department and the Property Ombudsman. I await your prompt response.</p>
<p>Yours sincerely,<br><br><strong>Marcus Gallagher</strong><br>Chairperson, Highfield Residents Association</p>""",

        2: """<p style='margin-top:0;'><strong>CONFIDENTIAL &bull; WORKPLACE INCIDENT &amp; SAFETY INVESTIGATION REPORT</strong><br>
<strong>Reference:</strong> AIR-2026-104 &emsp; <strong>Date of Occurrence:</strong> 14 October 2026 &bull; 10:15 am<br>
<strong>Location:</strong> Transit Loading Bay C, Apex Express Distribution Hub, Leeds<br>
<strong>Lead Investigator:</strong> Sarah Jenkins (Senior Logistics Operations Leader)</p>
<p><strong>1. Executive Summary &amp; Overview of Incident:</strong><br>
At approximately 10:15 am on Tuesday 14 October, a high-potential near-miss and equipment collision occurred in Loading Bay C. Counterbalance forklift truck FLT-04, operated by temporary agency operative Jordan Mills, reversed out of aisle 4 and collided with vertical support upright RU-12. The impact dislodged four pallets of consumer electronics, causing them to topple across the primary pedestrian walkway. Operative David Clarke jumped clear, sustaining a minor wrist sprain.</p>
<p><strong>2. Immediate Containment &amp; Physical Evidence:</strong><br>
First responder protocols were initiated immediately. First aiders attended to David Clarke; he was subsequently transferred to the regional minor injuries unit. The collision perimeter was cordoned off with high-visibility barrier tape. Flammable substances were isolated, and structural integrity engineers conducted preliminary ultrasonic load-testing on the damaged racking upright.</p>
<p><strong>3. Root-Cause Analysis (Human &amp; Environmental Factors):</strong><br>
CCTV audit reveals that the forklift speed exceeded our site terminal limit of 5 mph. Operative Mills was operating under high turnaround pressure during morning dispatch. Critically, pre-shift agency inductions failed to verify conversion training for heavy-chassis trucks. Moreover, the floor-mounted collision guardrail at RU-12 had been removed during electrical cabling installations three weeks prior and was never re-installed.</p>
<p><strong>4. Preventative Recommendations &amp; Action Plan:</strong></p>
<ul>
  <li>Re-anchor reinforced steel bollards at all loading aisle uprights by 20 October (Action: Site Facilities).</li>
  <li>Implement biometric ignition interlocks restricting forklift activation to verified, fully inducted drivers (Action: Fleet Safety).</li>
  <li>Establish dedicated painted pedestrian transit corridors segregated by physical barriers (Action: Safety Officer).</li>
</ul>""",

        3: """<h3 style='margin-top:0;color:var(--primary);'>Why Investing in Modern Apprenticeships is the Lifeline British Industry Needs</h3>
<p style='font-style:italic;color:#64748b;'>By Jordan Taylor &bull; Business &amp; Workforce Strategist &bull; Yorkshire Business Review</p>
<p>Walk onto any contemporary factory floor, IT campus, or logistics distribution terminal, and the conversation inevitably gravitates toward one pervasive dilemma: an acute shortage of technical skills. For too long, conventional corporate rhetoric has dismissed apprenticeships as costly, time-consuming distractions that siphon managerial hours. However, in our rapidly evolving industrial landscape, that assumption is not merely obsolete; it is actively damaging economic resilience.</p>
<p>First and foremost, apprenticeships provide an unparalleled mechanism for building custom organizational capability. Unlike generalist university graduates who often require months of operational unlearning, apprentices absorb company culture, compliance frameworks, and proprietary software from day one. Crucially, empirical research demonstrates that 85% of apprentices remain with their training employer three years post-qualification, dramatically reducing the crippling overheads associated with external headhunting and agency churn.</p>
<p>Furthermore, apprentice cohorts introduce refreshing diversity, digital agility, and innovative problem-solving into established teams. In an age where digital automation and AI are transforming routine workflows, apprentice technicians frequently bridge the generational divide, accelerating modernization across legacy systems.</p>
<p>To those business leaders hesitating at the threshold: investing in young talent is no charitable indulgence; it is a calculated commercial imperative. If our regional economy is to thrive on the national and global stage, we must stop lamenting skill shortages and start actively cultivating the workforce of tomorrow.</p>""",

        4: """<h3 style='margin-top:0;color:var(--primary);'>Platform Evaluation: CloudSuite Pro Project Management Software</h3>
<p style='font-style:italic;color:#64748b;'>An Objective Technical Review by the Digital Systems Taskforce &bull; Commercial Review Monthly</p>
<p>Following a rigorous four-week trial across sixty administrative and project coordinators, this review evaluates the functional utility, user ergonomics, and enterprise integration capabilities of CloudSuite Pro version 4.2.</p>
<p><strong>Core Capabilities &amp; System Strengths:</strong><br>
The platform's primary asset lies in its intuitive Kanban interface and automated Gantt scheduling modules. User onboarding proved seamless; non-technical personnel mastered milestone tracking and document collaboration within two working days. Automated sprint updates reduced internal email volume by an estimated 28%. Furthermore, the integrated timesheet portal aligns cleanly with payroll exports, eliminating manual spreadsheet reconciliation.</p>
<p><strong>System Bottlenecks &amp; Operational Shortcomings:</strong><br>
Nevertheless, the trial uncovered noticeable limitations. Mobile client responsiveness on iOS and Android devices exhibited latency when loading files exceeding 25MB. More critically, the proprietary permissions engine lacks granular security controls: project contributors cannot be restricted from viewing sensitive client billing rates without locking them out of document editing entirely. Customer technical support response times averaged sixteen hours &ndash; well below our four-hour enterprise service level agreement.</p>
<p><strong>Final Verdict &amp; Procurement Recommendation:</strong><br>
While CloudSuite Pro delivers exceptional visual task management, its enterprise security constraints cannot be overlooked. We recommend conditional procurement, subject to the vendor implementing role-based access tiers and dedicated 24/7 technical support.</p>""",

        5: """<p style='margin-top:0;'><strong>FROM:</strong> Marcus Vance (Senior Sustainability &amp; Energy Lead)<br>
<strong>TO:</strong> Elena Rostova (Chief Executive Officer) &amp; Operational Board<br>
<strong>DATE:</strong> 12 November 2026<br>
<strong>SUBJECT:</strong> Strategic Proposal: Accelerating Our Transition to Net Zero 2030</p>
<p>Dear Elena and Members of the Board,</p>
<p>As we approach the end of the financial quarter, I am submitting for your formal consideration an integrated strategic proposal designed to align our commercial operations with our public Net Zero 2030 sustainability commitments, while generating measurable operational efficiencies.</p>
<p><strong>1. Fleet Decarbonisation &amp; Capital Investment:</strong><br>
Our commercial fleet currently accounts for 62% of our total carbon footprint. With escalating fuel surcharges and expanding clean air zones across regional city centres, continuing to run diesel delivery vans carries mounting financial penalties. I propose phasing in electric commercial vans across forty high-density urban routes. Financial modelling indicates that lower kilowatt-hour fuel costs and reduced road-tax liabilities will deliver full capital payback within 3.8 years.</p>
<p><strong>2. Facilities Packaging &amp; Waste Elimination:</strong><br>
Secondly, an internal supply-chain audit revealed that our packaging bays produce over eight tonnes of non-recyclable plastic wrapping monthly. By partnering with certified biodegradable packaging providers and introducing reusable tote containers, we can diminish packaging expenditure by 14% while qualifying for carbon-offset business tax exemptions.</p>
<p><strong>3. Implementation Roadmap &amp; Board Governance:</strong><br>
I recommend commissioning a technical feasibility pilot at our Birmingham regional depot starting in January. I would appreciate the opportunity to deliver a ten-minute briefing presentation at the upcoming executive meeting on 28 November to answer any technical questions.</p>
<p>Warm regards,<br><strong>Marcus Vance</strong> &bull; Senior Sustainability Lead</p>""",

        6: """<div style='border:2px solid var(--primary);padding:3mm;border-radius:6px;'>
<h2 style='text-align:center;color:var(--primary);margin:0 0 2mm 0;'>Protecting Your Health &amp; Energy: The Shift Worker&rsquo;s Guide</h2>
<p style='text-align:center;font-weight:700;color:#64748b;margin:0 0 3mm 0;'>Essential Evidence-Based Guidance for Healthcare &amp; Logistics Professionals</p>

<p>Working rotational or night shifts is essential to 24/7 public operations, yet disrupted circadian rhythms can significantly impact cardiovascular health, cognitive focus, and emotional wellbeing. By adopting proactive sleep and nutrition habits, shift workers can protect their long-term vitality.</p>

<h4 style='color:var(--primary);margin:2mm 0 1mm 0;'>1. The Sleep Sanctuary Protocol</h4>
<ul>
  <li><strong>Light Control:</strong> Wear dark polarized sunglasses on your morning journey home to prevent morning sunlight from suppressing melatonin production. Use blackout blinds in your bedroom.</li>
  <li><strong>Acoustic Isolation:</strong> Use earplugs or high-frequency white noise generators to mask daytime domestic noise.</li>
  <li><strong>Wind-Down Routine:</strong> Disconnect from digital smartphones and LED tablets at least 45 minutes before attempting sleep.</li>
</ul>

<h4 style='color:var(--primary);margin:2mm 0 1mm 0;'>2. Nutritional Timing on Shift</h4>
<ul>
  <li><strong>Avoid Midnight Heavy Feasts:</strong> Digestion slows significantly at night. Choose high-protein snacks (nuts, Greek yogurt, wholemeal wraps) over refined sugar confectionary that triggers energy crashes.</li>
  <li><strong>Strategic Caffeine Intake:</strong> Consume coffee or tea early in the shift; avoid all caffeinated beverages within five hours of planned bedtime.</li>
  <li><strong>Hydration Discipline:</strong> Drink water consistently throughout your shift to prevent fatigue and headaches.</li>
</ul>

<p style='background:var(--soft);padding:2mm;border-radius:4px;margin-top:2mm;font-size:11.5pt;'><strong>Occupational Health Support:</strong> Confidentially access 24/7 counseling and physiological health assessments through our Employee Assistance Programme: <strong>ext. 4410</strong> or email <em>wellbeing@workplace.org.uk</em>.</p>
</div>""",

        7: """<h3 style='margin-top:0;color:var(--primary);'>Unlocking Your Potential Through Vocational Skills &amp; Apprenticeships</h3>
<p style='font-style:italic;color:#64748b;'>Transcript of the Keynote Address Delivered by Rachel Sterling at the West Midlands Adult Careers Congress</p>
<p>Good morning ladies and gentlemen, esteemed delegates, and fellow learners.</p>
<p>Looking out across this hall today, I see people at pivotal crossroads in their working lives. Some of you have recently left school, unsure which trajectory to choose. Others are seasoned workers seeking to retrain following industry restructuring. But whatever path brought you through those doors, you are likely carrying the same quiet anxiety: 'Do I have what it takes to thrive in today&rsquo;s competitive job market?'</p>
<p>I stand before you to tell you unequivocally: yes, you do. And the most direct, empowering route to building that future is not through mounting academic debt, but through hands-on, high-value vocational apprenticeships.</p>
<p>When you undertake an apprenticeship, you are not simply an observer in a lecture theatre. You are in the arena. You are applying mathematical reasoning to civil engineering blueprints, mastering complex medical compliance on hospital wards, or configuring enterprise network security for corporate servers. You earn a wage from your very first day, learning directly beside industry mentors who have dedicated decades to their craft.</p>
<p>Do not let past academic setbacks define the boundary of your capabilities. British industry does not merely need paper qualifications; it desperately needs your determination, your resilience, and your practical intelligence. Take this opportunity. Enrol in an apprenticeship today, and build a career you can be proud of for a lifetime.</p>
<p>Thank you.</p>""",

        8: """<p style='margin-top:0;'><strong>MINUTES OF THE QUARTERLY HEALTH, SAFETY &amp; ENVIRONMENTAL COMMITTEE</strong><br>
<strong>Meeting Date:</strong> 15 October 2026 &bull; 14:00 &ndash; 15:30 &bull; Boardroom A &amp; Hybrid Video Link<br>
<strong>Chairperson:</strong> David Henderson (Head of Operations) &emsp; <strong>Minutes Recorded By:</strong> Karen Ellis (Compliance Admin)</p>
<p><strong>Present:</strong> D. Henderson, K. Ellis, M. Vance (Sustainability), J. Cooper (Lead Shop Steward), T. Morris (Facilities)<br>
<strong>Apologies:</strong> Dr A. Patel (Occupational Physician)</p>
<p><strong>1. Matters Arising from Previous Minutes:</strong><br>
The minutes of the previous meeting on 12 July were reviewed, approved as an accurate record, and formally signed. T. Morris confirmed that all fire extinguishers in Warehouse 2 had passed their statutory pressure tests.</p>
<p><strong>2. Workplace Safety Incident Logs &amp; Near-Miss Trends:</strong><br>
K. Ellis presented the quarterly incident digest. Total recorded incidents fell by 12% across the quarter; however, near-miss slips and trips around the external dispatch ramp rose slightly during wet weather. J. Cooper emphasized the need for slip-resistant decking paint.</p>
<p><strong>3. Review of Mandatory Noise &amp; Vibration Assessments:</strong><br>
D. Henderson reported that noise level dosimetry conducted across Fabrication Bay B met HSE compliance standards. Nevertheless, enhanced hearing defenders will be issued to all full-time CNC operators.</p>
<p><strong>4. Environmental Sustainability &amp; Waste Management:</strong><br>
M. Vance presented findings from the plastic waste audit. Board approval will be sought to switch to compostable pallet wrapping by Q1 2027.</p>
<p><strong>5. Agreed Action Points &amp; Named Responsibilities:</strong></p>
<ul>
  <li><strong>ACTION 01:</strong> T. Morris to procure and apply non-slip epoxy coating to external dispatch ramp by 30 October.</li>
  <li><strong>ACTION 02:</strong> J. Cooper to distribute upgraded hearing PPE and verify operative fit by 7 November.</li>
  <li><strong>ACTION 03:</strong> M. Vance to submit final biodegradable packaging business case to Board by 15 November.</li>
</ul>
<p><strong>Next Meeting:</strong> Thursday 21 January 2027 at 14:00 in Boardroom A.</p>""",

        9: """<h3 style='margin-top:0;color:var(--primary);'>Will Artificial Intelligence Enhance or Diminish Administrative Employment?</h3>
<p style='font-style:italic;color:#64748b;'>A Discursive Policy Essay &bull; Candidate Examination Benchmark Script</p>
<p>The rapid proliferation of generative artificial intelligence and robotic process automation across British commerce has ignited fierce debate among economists, trade unions, and enterprise leaders. While proponents celebrate unprecedented gains in administrative efficiency, critics argue that automation threatens to render thousands of traditional clerical roles redundant. Examining this issue reveals that while routine administrative tasks are undeniably transforming, AI is more likely to augment administrative productivity than trigger wholesale unemployment.</p>
<p>On one hand, skeptics point out that automated algorithms can execute document processing, data entry, and schedule synchronization at speeds far exceeding human capability. In sectors such as financial underwriting and legal document discovery, automated systems have already compressed workflows that once occupied dozens of paralegals and administrative clerks into mere seconds. Consequently, employees performing purely repetitive data transfer face genuine vulnerability unless their skill sets evolve.</p>
<p>Conversely, advocates highlight that automating mundane administrative drudgery liberates human professionals to focus on high-value cognitive responsibilities. Complex stakeholder negotiation, sensitive customer dispute resolution, ethical discretion, and nuanced internal communication cannot be replicated by language models. Rather than eliminating the administrator, AI elevates the profession into that of an executive coordinator and workflow strategist.</p>
<p>In conclusion, artificial intelligence represents an evolutionary pivot rather than an existential crisis for administrative employment. Employers and educational institutions must collaborate to provide continuous digital upskilling, ensuring the modern administrative workforce harnesses technological tools effectively rather than being superseded by them.</p>""",

        10: """<h3 style='margin-top:0;color:var(--primary);'>Apprenticeship or University Degree? What Modern Employers Really Look For</h3>
<p style='font-style:italic;color:#64748b;'>Published by Nathan Brooks &bull; Digital Talent &amp; Skills Blog &bull; 4 Min Read &bull; 128 Comments</p>
<p>Every autumn, thousands of aspiring professionals face the same monumental crossroads: commit to three years of university and accumulate &pound;40,000 in student loan debt, or enrol in an employer-sponsored apprenticeship? As an internal talent acquisition manager who screens hundreds of CVs every month, let me give you the unvarnished reality from inside the boardroom.</p>
<p>Ten years ago, a generic undergraduate degree was the default prerequisite for corporate employment. Today, that narrative has shifted radically. When our hiring managers evaluate entry-level candidates, theoretical knowledge without practical workplace immersion is viewed as an incomplete foundation. In contrast, an apprentice candidate arrives with two to three years of verified corporate experience, established professional etiquette, and mastery of enterprise workflow tools.</p>
<p><strong>The Core Benefits of the Apprenticeship Pathway:</strong></p>
<ul>
  <li><strong>Zero Student Debt:</strong> Your tuition is funded entirely via the government apprenticeship levy, and you receive a competitive salary from day one.</li>
  <li><strong>Accelerated Promotion Trajectories:</strong> Apprentices frequently transition directly into supervisory and team lead positions ahead of university peers.</li>
  <li><strong>Real-World Problem Solving:</strong> You tackle authentic commercial challenges rather than theoretical hypothetical assignments.</li>
</ul>
<p>While specialised disciplines like medicine and veterinary surgery rightly remain degree-exclusive, vocational apprenticeships across software engineering, project management, accounting, and logistics provide a demonstrably faster launchpad to career success.</p>
<p><em>What has been your experience? Would you advise a school leaver today to pursue an apprenticeship or university degree? Share your perspectives in the comment section below!</em></p>""",

        11: """<div style='border:2px solid #b91c1c;padding:3mm;border-radius:6px;'>
<p style='margin:0 0 2mm 0;font-weight:700;color:#b91c1c;font-size:13pt;text-align:center;'>MANDATORY INTERNAL OPERATIONAL MEMORANDUM</p>
<p style='margin:0;font-size:11.5pt;'>
<strong>TO:</strong> All Retail Branch Supervisors, Cashiers &amp; Stockroom Personnel<br>
<strong>FROM:</strong> Regional Security &amp; Loss-Prevention Directorate<br>
<strong>DATE:</strong> 18 November 2026<br>
<strong>SUBJECT:</strong> Urgent Compliance Directive: Revised Loss Prevention &amp; Till Audit Protocols
</p>
<hr style='border:none;border-top:1px solid #cbd5e1;margin:2mm 0;'>
<p><strong>1. Purpose of Directive:</strong><br>
Following our quarterly inventory reconciliation, internal shrink across regional retail outlets increased by 3.4%, predominantly driven by stock discrepancies in high-value electronics and till transaction mismatches. With the seasonal holiday shopping period commencing next Monday, immediate adherence to revised security protocols is mandatory for all branch staff.</p>
<p><strong>2. Core Operational Mandates:</strong></p>
<ul>
  <li><strong>Mandatory Double-Count on Till Floats:</strong> Morning floats (&pound;250) must be independently counted and countersigned by both the cashier and shift supervisor prior to opening.</li>
  <li><strong>High-Value Tagging:</strong> All merchandise with a retail value exceeding &pound;50.00 must have alarmed security tags attached before being moved from the stockroom onto the shop floor.</li>
  <li><strong>Keyholder Log Enforcement:</strong> Stockroom keys must be signed out from the secure keybox with exact timestamps; keys must never be handed directly between staff members.</li>
  <li><strong>End-of-Shift Bag Searches:</strong> Staff exiting premises at the conclusion of shifts must submit bags and personal belongings for visual verification by an authorized supervisor.</li>
</ul>
<p style='margin-bottom:0;'><strong>Compliance Note:</strong> Failure to comply with these statutory loss-prevention procedures will result in formal disciplinary action under our standard code of conduct. If you observe suspicious activity, contact the anonymous security hotline: <strong>ext. 2204</strong>.</p>
</div>"""
    }

    spag_l2_exercises = {
        1: {
            "title": "Sentence Demarcation & Semicolons",
            "rule": "Eliminate comma splices by replacing commas between independent clauses with a semicolon or full stop.",
            "inputs": [
                "1. The delivery arrived two hours late, the frozen goods had already started to thaw.",
                "2. The morning shift completed their inventory audit, the evening shift still needs to tally the damaged stock.",
                "3. Customer complaints have surged this month, the management team must review our telephone response times.",
                "4. All staff must attend the fire drill tomorrow, attendance is compulsory for permanent and agency employees."
            ],
            "instruction": "Rewrite each sentence using an appropriate semicolon (;) or full stop followed by a capital letter."
        },
        2: {
            "title": "Subordinating Conjunctions & Complex Sentences",
            "rule": "Join clauses using subordinating conjunctions: although, whereas, unless, while, provided that.",
            "inputs": [
                "1. The warehouse was exceptionally busy. The dispatch team met every delivery target.",
                "2. Agency drivers will not be permitted on site. They must complete the mandatory safety briefing first.",
                "3. Electric vehicles require higher initial capital investment. Their running costs are significantly lower.",
                "4. Staff may request hybrid working. They must maintain their weekly performance targets."
            ],
            "instruction": "Combine each pair of simple sentences into a sophisticated complex sentence using the specified subordinating conjunctions."
        },
        3: {
            "title": "Active vs Passive Voice in Workplace Writing",
            "rule": "Transform informal active blame into objective, professional passive phrasing suitable for official reports.",
            "inputs": [
                "1. Jordan dropped a pallet of glass bottles because he was rushing his forklift.",
                "2. Someone forgot to lock the chemical cabinet before leaving the laboratory.",
                "3. The maintenance contractor didn't inspect the elevator cables last Friday.",
                "4. Our receptionists gave incorrect appointment times to four dental patients."
            ],
            "instruction": "Rewrite each statement in the professional passive voice to focus objectively on actions, causes, and impacts."
        },
        4: {
            "title": "Modal Verbs & Professional Hedging",
            "rule": "Calibrate certainty with precision: replace aggressive absolutes with appropriate modal verbs (could, should, is likely to).",
            "inputs": [
                "1. If we don't buy new laptops right now, the entire department will fail.",
                "2. The client is definitely lying about when they sent the payment cheque.",
                "3. Installing solar panels will completely eliminate all our energy bills forever.",
                "4. The new shift rota is going to make all staff quit within a month."
            ],
            "instruction": "Rewrite each blunt or exaggerated statement using professional modal hedging suitable for an executive briefing."
        },
        5: {
            "title": "Parallel Structure in Bulleted Lists",
            "rule": "Ensure all bullet items start with matching grammatical forms (e.g. all imperative verbs or all gerunds).",
            "inputs": [
                "Review the mixed list below for an incident response plan:<br>"
                "&bull; Sounding the alarm immediately upon detecting smoke.<br>"
                "&bull; You must escort all visitors to Assembly Point C.<br>"
                "&bull; Do not re-enter the facility until given clearance.<br>"
                "&bull; Checking the toilets and meeting rooms for stranded personnel."
            ],
            "instruction": "Rewrite the bulleted list so that every single point starts consistently with an active imperative verb."
        },
        6: {
            "title": "Apostrophes of Possession & Omission",
            "rule": "Correct apostrophe misuse: distinguish singular possession, plural possession, irregular plurals, and its vs it's.",
            "inputs": [
                "1. The nurses union submitted it's formal petition to the hospital directors office.",
                "2. All client files must be returned to the managers desk before the day's end.",
                "3. The company announced its new policy regarding childrens nursery vouchers.",
                "4. Both driver's vehicles were damaged when the warehouse roof lost it's guttering."
            ],
            "instruction": "Identify every misplaced or missing apostrophe in the sentences above and rewrite them correctly."
        },
        7: {
            "title": "Discourse Markers & Paragraph Linking",
            "rule": "Use sophisticated cohesive devices: Furthermore, Consequently, In contrast, Nevertheless, As a result.",
            "inputs": [
                "Connect this fragmented report extract into a unified paragraph:<br>"
                "The facility experienced an unexpected power outage at 08:30. "
                "The backup generators activated within thirty seconds. "
                "The IT server room sustained no data loss. "
                "The automated packing conveyor lines shut down temporarily. "
                "Staff had to pack customer parcels manually until power was restored."
            ],
            "instruction": "Re-write the extract into a fluent paragraph using at least three distinct discourse markers."
        },
        8: {
            "title": "Formal Vocabulary & Nominalisation",
            "rule": "Raise the register of your writing by transforming verbs and casual adjectives into formal executive nouns.",
            "inputs": [
                "1. We need to look into how much money we're wasting on paper every week.",
                "2. When workers get fed up with their bosses, they don't work as hard.",
                "3. We tried out the new booking website and it was really clunky and annoying.",
                "4. The manager told everyone off because people kept turning up late for shifts."
            ],
            "instruction": "Rewrite each colloquial statement into formal executive prose using nominalisation and sophisticated vocabulary."
        }
    }

    mock_english_l2_papers = [
        # Mock 1
        {
            "paper_num": 1,
            "theme": "Community Facilities & Sustainable Infrastructure",
            "task1": {
                "title": "Task 1: Formal Proposal Letter &bull; Community Healthcare Grant",
                "marks": 15,
                "time": "45 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You are an administrative coordinator at a community health clinic in an urban borough. The Regional Health Trust has announced a &pound;5,000 community investment grant to fund grassroots facility improvements. Write a formal proposal letter to the Trust Director, Dr Angela Simmons, proposing how your clinic would utilize this funding.",
                "bullets": [
                    "Explain specific accessibility and physical access barriers currently experienced by patients at your clinic.",
                    "Detail two distinct initiatives the &pound;5,000 grant would finance and how each will be implemented.",
                    "Outline how the clinical team will evaluate the success of the improvements over the next twelve months."
                ]
            },
            "task2": {
                "title": "Task 2: Informative &amp; Persuasive Article &bull; Electric Urban Travel",
                "marks": 15,
                "time": "40 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "A regional lifestyle and motoring magazine is publishing a special issue titled 'Urban Travel in 2030'. Many motorists are anxious about moving away from petrol and diesel cars. Write an engaging, balanced article evaluating whether electric vehicles and public charging networks are ready for everyday family use.",
                "bullets": [
                    "Evaluate the practical and financial advantages of switching to electric vehicles.",
                    "Address genuine public concerns regarding charging infrastructure, range, and battery lifespan.",
                    "Provide a clear, balanced conclusion advising motorists on whether now is the right time to transition."
                ]
            }
        },
        # Mock 2
        {
            "paper_num": 2,
            "theme": "Logistics Safety & Vocational Apprenticeships",
            "task1": {
                "title": "Task 1: Workplace Incident &amp; Safety Investigation Report",
                "marks": 15,
                "time": "45 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You are the Senior Logistics Team Leader at Apex Express Distribution Hub in Leeds. On Tuesday morning at 10:15 am, a serious near-miss and forklift collision occurred in Loading Bay C: a forklift truck dislodged four pallets of consumer electronics, causing them to topple across a pedestrian walkway. Operative David Clarke suffered a sprained wrist. Write an official investigation report to Regional Operations Director Mr Robert Keane.",
                "bullets": [
                    "Provide an objective factual account of the collision, including date, time, location, and equipment involved.",
                    "Analyze the human, training, and physical site factors that contributed to the incident.",
                    "Recommend three mandatory preventative safety measures with assigned deadlines to prevent a recurrence."
                ]
            },
            "task2": {
                "title": "Task 2: Persuasive Article for Regional Business Journal",
                "marks": 15,
                "time": "40 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "The Yorkshire Business Review has invited opinion pieces on solving the national technical skills crisis. While some business executives complain that training apprentices is too expensive and time-consuming, others credit apprenticeships with business growth. Write a persuasive article arguing why investing in modern apprenticeships is vital for regional industry.",
                "bullets": [
                    "Analyze the causes and corporate costs of persistent skill shortages in modern industry.",
                    "Present compelling arguments demonstrating how apprenticeships reduce employee turnover and enhance productivity.",
                    "Conclude with a persuasive call to action urging corporate leaders to commit to vocational training."
                ]
            }
        },
        # Mock 3
        {
            "paper_num": 3,
            "theme": "Residential Facilities & Workplace Wellbeing",
            "task1": {
                "title": "Task 1: Formal Letter of Grievance &amp; Demanded Rectification",
                "marks": 15,
                "time": "45 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You are Chairperson of the Highfield Residents Association in Birmingham. Over the past month, tenants in Highfield Towers (a 12-storey block with elderly and disabled residents) have experienced persistent failures by Sovereign Facilities Management: the primary elevator has been broken for 18 days, the main security gates are unlocked, and communal refuse is overflowing. Write a formal grievance letter to Managing Director Mr Julian Vance.",
                "bullets": [
                    "Detail the specific service failures and explain the direct impact on vulnerable residents.",
                    "Criticize the inadequate response and lack of communication from the facilities management helpdesk.",
                    "State three explicit remedial actions demanded and establish a strict 48-hour deadline before legal escalation."
                ]
            },
            "task2": {
                "title": "Task 2: Workplace Health &amp; Wellbeing Guidance Leaflet",
                "marks": 15,
                "time": "40 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You are a Health and Safety Representative at St Jude's NHS Trust. Following an internal survey revealing high levels of physical exhaustion and insomnia among rotational shift workers, management has asked you to produce an authoritative guidance leaflet to be distributed in staff rest areas titled: 'Protecting Your Health & Energy: The Shift Worker's Guide'.",
                "bullets": [
                    "Explain practical strategies for optimizing daytime sleep and creating an effective sleep environment.",
                    "Offer actionable advice on meal timing, hydration, and avoiding energy-crashing foods on shift.",
                    "Provide clear contact information for internal support services and confidential counseling."
                ]
            }
        },
        # Mock 4
        {
            "paper_num": 4,
            "theme": "Corporate Decarbonisation & Adult Careers",
            "task1": {
                "title": "Task 1: Strategic Workplace Email to Executive Board",
                "marks": 15,
                "time": "45 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You are the Sustainability Lead at Meridian Retail Logistics. Operating 45 diesel delivery vans and generating over 8 tons of plastic waste monthly, the company faces growing criticism from corporate clients. The CEO, Ms Elena Rostova, has invited staff proposals for the company's 'Net Zero 2030' roadmap. Draft a formal proposal email to the Executive Board.",
                "bullets": [
                    "Outline the commercial and environmental risks of maintaining current high-carbon operations.",
                    "Propose two high-impact initiatives (e.g. electric fleet transition and biodegradable packaging) with estimated timelines.",
                    "Explain how achieving Net Zero credentials will enhance corporate reputation and attract commercial tenders."
                ]
            },
            "task2": {
                "title": "Task 2: Inspiring Persuasive Speech for Careers Convention",
                "marks": 15,
                "time": "40 Minutes",
                "words": "200&ndash;250 words",
                "scenario": "You have been invited to deliver the keynote address at the West Midlands Adult Skills & Apprenticeships Fair. The audience consists of school leavers, career changers, and adult jobseekers who may feel anxious, underqualified, or discouraged by previous negative experiences in formal schooling. Write the complete speech script titled: 'Unlocking Your Potential Through Modern Skills'.",
                "bullets": [
                    "Acknowledge common anxieties about returning to learning and validate the audience's lived experience.",
                    "Inspire the audience with concrete benefits of hands-on vocational training and earning while learning.",
                    "Deliver an impassioned conclusion urging attendees to speak with training mentors and take their first step today."
                ]
            }
        }
    ]

    workbook_l2_prompts = [
        # 22 Worksheets across authentic vocational sectors
        {
            "id": 1, "sector": "Healthcare & NHS", "format": "Formal Letter",
            "scenario": "You are a Patient Experience Coordinator at St Luke's Hospital. A patient, Mrs Brenda Cooper, wrote a letter complaining about a three-hour delay in the outpatient orthopedic clinic and unhelpful reception staff.",
            "bullets": ["Acknowledge Mrs Cooper's frustration and validate her concerns politely.", "Explain the mitigating circumstances (emergency trauma admissions) that caused clinic backlogs.", "Detail two remedial actions taken to improve communication and offer a follow-up appointment."]
        },
        {
            "id": 2, "sector": "Construction & Civil Engineering", "format": "Incident Report",
            "scenario": "You are a Site Safety Supervisor at Apex Construction. An unsecured scaffolding board on the second-tier staging shifted in high winds, narrowly missing a ground worker and damaging a cement mixer below.",
            "bullets": ["Record the date, time, weather conditions, and exact location of the scaffolding incident.", "Analyze why the toe-boards and scaffolding clips failed to hold the timber securely.", "Specify immediate corrective actions and updated daily scaffolding sign-off procedures."]
        },
        {
            "id": 3, "sector": "Warehousing & Logistics", "format": "Formal Email",
            "scenario": "You are an Inventory Controller at Vanguard Freight Hub. A pallet of high-value medical supplies arrived from your carrier, SwiftTrans Ltd, with torn weatherproofing and water damage to six packaging cartons.",
            "bullets": ["State consignment tracking numbers, delivery time, and the exact physical condition upon arrival.", "Request a full credit note or replacement dispatch within forty-eight hours.", "Specify required freight insurance documentation and photographic evidence attached."]
        },
        {
            "id": 4, "sector": "Retail Management", "format": "Newsletter Article",
            "scenario": "You are an Assistant Store Manager at a busy high-street department store. The store is launching a seasonal campaign to reduce shoplifting while maintaining friendly, attentive customer service.",
            "bullets": ["Highlight the financial impact of stock shrinkage on store bonuses and inventory availability.", "Explain how attentive customer greetings and eye contact serve as effective deterrents to theft.", "Remind staff of strict personal safety protocols and reporting lines when observing suspicious behavior."]
        },
        {
            "id": 5, "sector": "Hospitality & Catering", "format": "Critical Review",
            "scenario": "You are a Catering Operations Consultant writing for Hospitality Management Journal. You recently conducted a scheduled food safety and kitchen workflow inspection at a 200-cover banqueting hotel.",
            "bullets": ["Evaluate the kitchen's hygiene practices, cold-storage temperature logging, and allergen controls.", "Identify operational bottlenecks observed during peak banquet plating service.", "Provide constructive, actionable recommendations for optimizing kitchen workflow and staff training."]
        },
        {
            "id": 6, "sector": "Social Care & Community", "format": "Information Leaflet",
            "scenario": "You are a Senior Care Coordinator at Oakwood Community Care Trust. The trust is launching a respite support service for family members caring for relatives with early-stage dementia.",
            "bullets": ["Explain what respite care is and how it benefits both the caregiver and the family member.", "Detail the range of day activities, specialist memory sessions, and transportation options provided.", "Outline straightforward assessment steps and provide direct telephone and web contact details."]
        },
        {
            "id": 7, "sector": "Information Technology", "format": "Proposal Email",
            "scenario": "You are an IT Security Technician at Greenfield Financial. Following a series of phishing attempts across the sector, you believe the company must mandate two-factor authentication (2FA) for all 150 staff.",
            "bullets": ["Explain the cybersecurity vulnerabilities associated with single-password credentials.", "Outline how implementing authenticator apps will safeguard sensitive client financial records.", "Propose a rollout timeline, including 15-minute training webinars and helpdesk support."]
        },
        {
            "id": 8, "sector": "Customer Service", "format": "Response Letter",
            "scenario": "You are a Senior Customer Relations Officer at Horizon Travel. A customer, Mr Tariq Ahmed, demanded a refund after their coach tour to Scotland was delayed by four hours due to a motorway closure.",
            "bullets": ["Express sincere regret for the travel disruption while explaining the road closure circumstances.", "Outline the refreshments and updates provided by the coach driver during the incident.", "Offer a 25% goodwill travel voucher towards their next booking and explain terms."]
        },
        {
            "id": 9, "sector": "Fleet & Transport", "format": "Incident Report",
            "scenario": "You are a Fleet Maintenance Coordinator at Metro Parcel Express. Delivery van VN-19 broke down on the A38 due to total alternator failure, delaying 65 parcel deliveries and requiring a tow recovery.",
            "bullets": ["Detail the vehicle registration, driver details, time of breakdown, and recovery arrival.", "Investigate why the scheduled 10,000-mile diagnostic check missed early alternator belt wear.", "Recommend revised preventative maintenance checks for all high-mileage delivery vans."]
        },
        {
            "id": 10, "sector": "Sports & Leisure", "format": "Press Article",
            "scenario": "You are a Marketing Officer at a municipal leisure centre. The centre is launching a discounted corporate fitness membership scheme for local NHS, police, and council workers.",
            "bullets": ["Promote the health and mental wellbeing benefits of regular cardiovascular exercise for shift workers.", "Detail the facilities included: 25m swimming pool, functional training gym, and classes.", "Explain the simple sign-up process and provide open-day weekend dates with free taster sessions."]
        },
        {
            "id": 11, "sector": "Corporate Finance", "format": "Staff Memo",
            "scenario": "You are an Internal Audit Manager at Crestview Global. Several departments have submitted travel expense claims exceeding agreed meal and mileage limits without receipts.",
            "bullets": ["Clarify statutory allowable subsistence rates (&pound;10 lunch, &pound;25 dinner) and 45p mileage caps.", "State the mandatory requirement for itemized VAT receipts for every expense claim.", "Establish a strict deadline for monthly submissions and warn that non-compliant claims will be rejected."]
        },
        {
            "id": 12, "sector": "Early Years Education", "format": "Parent Information Leaflet",
            "scenario": "You are a Nursery Manager at Little Acorns Daycare. The nursery is introducing a weekly 'Forest School' outdoor learning curriculum to encourage environmental exploration in all weather.",
            "bullets": ["Explain the developmental benefits of outdoor exploratory play for young children's motor skills.", "List essential clothing items parents must provide (wellies, waterproof all-in-ones, warm layers).", "Reassure parents regarding site risk assessments, trained pediatric first aiders, and hygiene routines."]
        },
        {
            "id": 13, "sector": "Manufacturing & Engineering", "format": "Safety Notice",
            "scenario": "You are a Health and Safety Officer at Precision Tooling Ltd. Machine operators have occasionally been spotted not wearing mandatory eye protection near high-speed lathes.",
            "bullets": ["Remind all employees of the statutory PPE requirements under the Health and Safety at Work Act.", "Highlight the severe risks of ocular trauma from metal swarf and flying coolant droplets.", "Confirm that failure to wear prescribed safety goggles in designated zones will trigger disciplinary warnings."]
        },
        {
            "id": 14, "sector": "Estate Management", "format": "Tenant Advisory Letter",
            "scenario": "You are a Commercial Property Manager at Trinity Business Park. The annual full-scale fire alarm and automatic sprinkler system testing is scheduled for next Thursday.",
            "bullets": ["State the date, start time (07:00), and expected conclusion (11:00) of the alarm testing.", "Explain what tenants should expect: intermittent sirens, strobe lights, and security gate cycling.", "Advise tenants on informing office staff in advance and confirm emergency contact telephone numbers."]
        },
        {
            "id": 15, "sector": "Human Resources", "format": "Company-Wide Email",
            "scenario": "You are an HR Director at Apex Commercial Services. The company is formally codifying its hybrid working policy, requiring staff to work two core days in the office and up to three days remote.",
            "bullets": ["Explain the business and wellbeing rationale for balancing team collaboration with remote focus.", "Define core office attendance days (Tuesdays and Thursdays) and working hour expectations.", "Provide the schedule for department manager consultation sessions and policy start dates."]
        },
        {
            "id": 16, "sector": "Dental & Primary Healthcare", "format": "Patient Information Leaflet",
            "scenario": "You are a Practice Manager at High Street Dental Surgery. Many patients are unclear on what constitutes a dental emergency versus routine care, leading to overwhelmed triage lines.",
            "bullets": ["Define acute dental emergencies: uncontrolled bleeding, severe facial trauma, and swelling affecting breathing.", "Explain procedure for urgent same-day appointments and the out-of-hours NHS 111 service.", "Offer practical guidance on temporary toothache relief and remind patients of preventive check-ups."]
        },
        {
            "id": 17, "sector": "Automotive Engineering", "format": "Incident Investigation Report",
            "scenario": "You are a Workshop Manager at Premier Autocentre. A hydraulic lift experienced a seal rupture, dropping a car chassis 20cm onto mechanical safety lockdogs and spilling 5 litres of hydraulic oil.",
            "bullets": ["Describe the vehicle, technician involved, time of hydraulic seal failure, and initial containment.", "Examine why the safety lockdogs engaged correctly while the hydraulic cylinder failed.", "Recommend immediate ultrasonic pressure tests on all vehicle lifts and revision of maintenance logs."]
        },
        {
            "id": 18, "sector": "Local Government & Civic", "format": "Town Hall Speech",
            "scenario": "You are a Community Council Representative addressing a council planning committee meeting. Local residents are demanding speed-calming chicanes and a 20mph zone outside St Matthew's Primary School.",
            "bullets": ["Highlight recent traffic speed data showing vehicles regularly exceeding 40mph during school runs.", "Share residents' and parents' safety anxieties, referencing two recent near-miss pedestrian incidents.", "Urge the planning committee to allocate traffic-calming funds from the annual highways budget."]
        },
        {
            "id": 19, "sector": "Hospitality & Events", "format": "Professional Venue Review",
            "scenario": "You are a Conference Coordinator writing for Events Industry Weekly. You attended a two-day regional corporate expo hosted at the newly refurbished Millennium Exhibition Centre in Leeds.",
            "bullets": ["Review the venue's audio-visual technology, stage lighting, and digital attendee check-in speed.", "Critique the catering facilities, pointing out long lunchtime queues and limited vegetarian selections.", "Provide an overall star rating and suggest practical operational improvements for future exhibitions."]
        },
        {
            "id": 20, "sector": "Security & Loss Prevention", "format": "Security Directive Memo",
            "scenario": "You are a Chief Security Officer at a corporate research facility. Contractors have repeatedly failed to return electronic visitor access fobs, posing a confidentiality risk.",
            "bullets": ["Explain the security risks of unaccounted building access cards in restricted laboratory areas.", "Mandate that all visitors must surrender photo ID at reception before receiving temporary badges.", "Confirm that contractor companies will be fined &pound;50 per unreturned fob and access will be revoked."]
        },
        {
            "id": 21, "sector": "Environmental Health", "format": "Formal Advisory Letter",
            "scenario": "You are an Environmental Health Officer at City Council. An inspection of the rear service alley behind 'The Golden Dragon' restaurant found overflowing commercial bins attracting vermin.",
            "bullets": ["Detail specific violations of the Environmental Protection Act: unlidded bins and grease spillages.", "Require immediate commercial pressure washing and secure locking bin lids within 7 days.", "Warn of formal statutory improvement notices and potential court summons if issues persist."]
        },
        {
            "id": 22, "sector": "Career Progression & Professional Development", "format": "Internal Application Statement",
            "scenario": "You are a Senior Customer Service Representative at an insurance call centre applying for the advertised position of Team Leader / Operations Supervisor.",
            "bullets": ["Outline your track record: meeting resolution targets, mentoring new recruits, and handling escalations.", "Explain your leadership style: constructive coaching, clear delegation, and empathetic communication.", "Describe how you will support department goals to improve first-call resolution by 15% this year."]
        }
    ]

        out_file = os.path.join(PROJECT_DIR, "books", "a4", "english_suite_content.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-
")
        f.write('"""
English Suite Real Content & Examination Data Module.
')
        f.write('Contains authentic Pearson Edexcel Band 4 models, SPaG exercises, mocks, and prompts.
"""

')
        f.write('FORMAT_L2_MODELS = ' + repr(format_l2_models) + '

')
        f.write('SPAG_L2_EXERCISES = ' + repr(spag_l2_exercises) + '

')
        f.write('MOCK_ENGLISH_L2_PAPERS = ' + repr(mock_english_l2_papers) + '

')
        f.write('WORKBOOK_L2_PROMPTS = ' + repr(workbook_l2_prompts) + '

')
        f.write('FORMAT_L1_MODELS = ' + repr(format_l1_models) + '

')
        f.write('MOCK_ENGLISH_L1_PAPERS = ' + repr(mock_english_l1_papers) + '

')

    print(f"Generated {out_file} successfully! Size: {os.path.getsize(out_file)} bytes")

if __name__ == "__main__":
    generate_english_content()
