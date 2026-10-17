"""
books/a4/populate_english_solutions.py
Populates comprehensive, authentic Band 4 exemplars and Reading Q1-Q9 solutions
for Mocks 2, 3, 4, 5, and 6 in specialist_suite_reference.py.
"""

from pathlib import Path

REF_FILE = Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/specialist_suite_reference.py")

MOCKS_SOLUTIONS_EXPANSION = '''
ENGLISH_L2_MOCK_SOLUTIONS = {
    1: [
        ("Mock 1 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Electric vans now account for 28% of our urban delivery fleet.'</i> (Verified verifiable statistic). Opinion: <i>'The transition has been an absolute triumph for driver morale.'</i> (Subjective value judgment).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'kicking the carbon can down the road'</i> implies that traditional courier companies are postponing necessary decarbonization measures and shifting the environmental burden to future generations without resolving systemic pollution.<br>"
         "<b>Q3. Organisational Features in Text A:</b> (1) Subheadings segment key discussion areas (e.g. Charging Infrastructure, Capital Expenditure). (2) Bullet points emphasize operational metrics clearly.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Rhetorical question: <i>'Can small family hauliers realistically shoulder the cost of rapid electrification?'</i> (engages the reader and highlights financial strain). (2) Emotive adjective: <i>'crippling upfront battery costs'</i> (conveys severe economic pressure).<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'prohibitive'</i> means excessively high or unaffordable, preventing hauliers from making capital investments.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To advocate for government transitional subsidies and protect independent transport businesses from rapid regulatory penalties.<br>"
         "<b>Q7. Synthesizing Text A and Text B:</b> While Text A celebrates the long-term operational savings and air quality benefits of electric fleets, Text B cautions that without public infrastructure funding, independent owner-drivers face bankruptcy.<br>"
         "<b>Q8. Comparing Ideas Across Both Texts:</b> Both texts acknowledge that charging network density is currently insufficient. Text A views depot rapid-chargers as the private solution, whereas Text B argues national public charging networks must be subsidized before mandates take effect.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A provides verifiable fleet statistics from audited green logistics trials, whereas Text B relies heavily on anecdotal testimonies from individual hauliers, making Text A more empirically robust but Text B more representative of micro-business sentiment."),
        ("Mock 1 &bull; Writing Exemplar &bull; Task 1 (Formal Workplace Report)",
         "<b>Task 1 Benchmark Exemplar: Formal Recommendation Report</b><br>"
         "<b>To:</b> Board of Operations, GreenRoute Logistics<br>"
         "<b>From:</b> Subi, Senior Logistics Analyst<br>"
         "<b>Date:</b> 14 October 2026<br>"
         "<b>Subject:</b> Fleet Electrification Feasibility Assessment &amp; Infrastructure Roadmap<br><br>"
         "<b>1. Executive Summary</b><br>"
         "This report evaluates the operational and commercial viability of transitioning our regional delivery fleet of 45 diesel vans to battery electric vehicles (BEVs) over a 24-month horizon. While initial capital expenditure is substantial, projected fuel and maintenance savings yield a break-even point at 38 months.<br><br>"
         "<b>2. Key Operational Findings</b><br>"
         "Analysis of urban distribution routes indicates average daily mileage of 82 miles, well within the 160-mile range of commercial BEVs. Furthermore, telematics data reveals that our depot dwell times (19:00 to 05:30) provide ideal low-tariff overnight charging windows.<br><br>"
         "<b>3. Risk Analysis &amp; Mitigation</b><br>"
         "Grid supply capacity at the Birmingham hub requires a 100 kVA substation upgrade (&pound;18,500). To mitigate downtime risks, a phased rollout of 15 vans per quarter is strongly advised alongside dual-socket 22 kW AC depot chargers.<br><br>"
         "<b>4. Strategic Recommendations</b><br>"
         "&bull; Secure government Workplace Charging Scheme grants prior to procurement.<br>"
         "&bull; Pilot 5 electric vans on inner-city routes starting Q1 2027.<br>"
         "&bull; Implement mandatory eco-driving and regenerative braking training for all delivery operatives."),
        ("Mock 1 &bull; Writing Exemplar &bull; Task 2 (Persuasive Public Article)",
         "<b>Task 2 Benchmark Exemplar: Community Newspaper Article</b><br>"
         "<b>Title: Charging Ahead: Why Our High Street Must Welcome Clean Transport</b><br>"
         "<b>Byline:</b> Local Business Correspondent<br><br>"
         "Picture this: a bustling Saturday afternoon where shoppers breathe crisp, fresh air instead of diesel particulates. Sound like an impossible utopia? In reality, sustainable urban transport is already transforming towns across Britain.<br><br>"
         "For decades, high street retailers have feared pedestrianization and clean air zones, worrying that delivery restrictions would choke trade. Yet evidence reveals the opposite: footfall increases by up to 16% in clean, quiet town centres. Customers linger longer in outdoor cafes when they are not subjected to idling delivery trucks.<br><br>"
         "Critics argue that small businesses cannot adapt. However, regional delivery co-operatives and electric cargo bike hubs have demonstrated that low-emission logistics are not only affordable but significantly faster through congested urban corridors.<br><br>"
         "The time for procrastination has passed. Local council leaders and business owners must unite to install shared fast-chargers and loading bays. Let us build a town centre that champions health, commerce, and future generations.")
    ],
    2: [
        ("Mock 2 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Over 4.4 million UK workers currently operate on hybrid schedules.'</i> (Empirical labor force survey datum). Opinion: <i>'Remote working has permanently destroyed spontaneous workplace innovation.'</i> (Unverified subjective viewpoint).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The metaphor <i>'presenteeism in digital disguise'</i> implies that employees feel pressured to remain permanently visible online and answer emails after hours, creating an illusion of output rather than authentic productivity.<br>"
         "<b>Q3. Structural Features in Text A:</b> Clear numbered section headings, bold key terms for cognitive anchoring, and a concluding executive bullet-point summary.<br>"
         "<b>Q4. Persuasive Language in Text B:</b> (1) Triadic listing: <i>'flexibility, autonomy, and work-life balance'</i>. (2) High-modality modal verbs: <i>'employers must adapt or they will inevitably bleed top talent'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 2 of Text B, <i>'retention'</i> denotes the capacity of a company to keep its employees and prevent them from resigning.<br>"
         "<b>Q6. The Writer's Purpose in Text B:</b> To persuade corporate leadership that offering agile working models is an indispensable recruitment strategy in competitive industries.<br>"
         "<b>Q7. Cross-Text Synthesis:</b> Text A emphasizes supervisory oversight and collaborative cohesion in office environments, whereas Text B prioritizes personal autonomy and mental wellbeing achieved through remote flexibility.<br>"
         "<b>Q8. Comparing Workplace Values:</b> Both texts concede that organizational trust is foundational. Text A posits that trust is reinforced through structured face-to-face mentorship, while Text B insists trust is proven by measuring task deliverables rather than desk hours.<br>"
         "<b>Q9. Evaluating Evidentiary Weight:</b> Text A draws upon multi-industry performance benchmarks and human resources audit metrics, giving it high evidential validity, whereas Text B leverages subjective employee sentiment polls."),
        ("Mock 2 &bull; Writing Exemplar &bull; Task 1 (Formal Workplace Policy Report)",
         "<b>Task 1 Benchmark Exemplar: Formal Hybrid Working Policy Report</b><br>"
         "<b>To:</b> Executive Management Board, Apex Global Enterprises<br>"
         "<b>From:</b> Subi, Lead HR Strategy Consultant<br>"
         "<b>Date:</b> 18 October 2026<br>"
         "<b>Subject:</b> Enterprise Hybrid Working Framework &amp; Core Productivity Standards<br><br>"
         "<b>1. Purpose &amp; Scope</b><br>"
         "This policy document establishes standardized operational guidelines for hybrid working across all divisional departments, balancing individual autonomy with organizational performance.<br><br>"
         "<b>2. Proposed Core Attendance Model</b><br>"
         "Departmental teams will adopt a '3/2' agile structure: three days in office (including mandatory collaboration Tuesdays and Thursdays) and two days remote. Core collaboration hours are set between 10:00 and 15:00.<br><br>"
         "<b>3. Technology &amp; Ergonomic Compliance</b><br>"
         "Every remote employee must complete a DSE ergonomic workstation assessment. Apex will provide dual-screen monitors, encrypted VPN hardware keys, and noise-cancelling headsets to guarantee GDPR compliance.<br><br>"
         "<b>4. Accountability &amp; Output Metrics</b><br>"
         "Performance will be appraised through quarterly objective key results (OKRs) and project milestone completions rather than keystroke monitoring software.<br><br>"
         "<b>5. Recommendations for Implementation</b><br>"
         "&bull; Launch 60-day departmental trial starting November 2026.<br>"
         "&bull; Deliver line-manager workshops on asynchronous team leadership.<br>"
         "&bull; Review sickness absence and productivity indices after 6 months."),
        ("Mock 2 &bull; Writing Exemplar &bull; Task 2 (Persuasive Speech to Staff Forum)",
         "<b>Task 2 Benchmark Exemplar: Staff Forum Persuasive Speech</b><br>"
         "<b>Title: Embracing Agile Collaboration: Why Our Culture Thrives on Flexibility</b><br>"
         "<b>Delivered by:</b> Staff Employee Representative<br><br>"
         "Good morning colleagues and members of the leadership team.<br><br>"
         "We stand at a defining crossroads in our company's history. Behind us lies the rigid, outdated five-day office grind; ahead lies the opportunity to forge an agile, trust-based working culture where everyone can excel.<br><br>"
         "Let me be unequivocally clear: hybrid working is not about working less. It is about working smarter. When we eliminate the exhausting two-hour daily commute, we gain focus, renewed energy, and precious time with our families. We return to the office on team days energized, creative, and ready to collaborate.<br><br>"
         "Some voice concerns that team spirit will dissipate. But culture is built on mutual respect and shared objectives, not on sitting at adjacent desks wearing headphones in silence! By establishing structured in-person brainstorming sessions alongside dedicated remote focus days, we achieve the best of both worlds.<br><br>"
         "Let us champion this policy with professional accountability. Let us prove that autonomy drives excellence. Thank you.")
    ],
    3: [
        ("Mock 3 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Degree apprenticeships combine full-time salaried employment with debt-free university study.'</i> (Factual definition). Opinion: <i>'Traditional university degrees are obsolete relics of an elitist education system.'</i> (Polemical opinion).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'golden handcuffs of entry-level debt'</i> suggests that graduates are financially constrained for decades by student loan repayments, limiting their career and home-ownership prospects.<br>"
         "<b>Q3. Visual &amp; Typographical Features in Text A:</b> Callout case-study panels, bold comparative salary statistics, and clear tabular breakdowns of tuition fees.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Metaphor: <i>'an intellectual incubator where critical minds are forged'</i>. (2) Alliteration: <i>'broadening horizons through borderless debate'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 4 of Text B, <i>'versatility'</i> indicates the capacity to adapt across diverse intellectual disciplines and career trajectories.<br>"
         "<b>Q6. Writer's Purpose in Text B:</b> To defend the enduring academic, civic, and philosophical value of traditional campus-based degree education against purely vocational metrics.<br>"
         "<b>Q7. Synthesizing Educational Pathways:</b> Both texts emphasize that modern industry demands adaptable problem solvers. Text A argues that vocational apprenticeship embedding provides superior day-one readiness, while Text B maintains that academic theory fosters deeper analytical rigor.<br>"
         "<b>Q8. Comparison of Financial Arguments:</b> Text A presents compelling evidence that apprenticeship candidates graduate with &pound;0 debt and &pound;80,000 in accumulated earnings, whereas Text B contends that long-term graduate lifetime earnings still justify initial borrowing.<br>"
         "<b>Q9. Evaluating Tone and Credibility:</b> Text A maintains an objective, informational tone supported by Institute for Apprenticeships data, whereas Text B adopts an impassioned academic defense that borders on nostalgic rhetoric."),
        ("Mock 3 &bull; Writing Exemplar &bull; Task 1 (Formal Article for a National Careers Publication)",
         "<b>Task 1 Benchmark Exemplar: Careers Feature Article</b><br>"
         "<b>Title: Degree Apprenticeship or Traditional Campus? Navigating Modern Career Gateways</b><br>"
         "<b>Byline:</b> Subi, Lead Vocational Education Specialist<br><br>"
         "For generations of school leavers, the path to professional success followed an unchanging script: finish Sixth Form, secure university admission, and graduate into the corporate world. Today, skyrocketing tuition fees and the rapid rise of Degree Apprenticeships have fundamentally disrupted that conventional narrative.<br><br>"
         "<b>The Apprenticeship Advantage: Earn While You Learn</b><br>"
         "Degree apprenticeships offer an undeniable financial proposition: zero tuition debt, a full employee salary from day one, and immediate immersion in corporate culture. In fields like software engineering, quantity surveying, and digital marketing, candidates accumulate four years of workplace experience while simultaneously earning a BSc or BEng.<br><br>"
         "<b>The Campus Experience: Intellectual Autonomy</b><br>"
         "Conversely, the traditional university journey fosters independent critical inquiry, cultural exploration, and networking beyond the constraints of a single employer's commercial remit. For careers in medicine, law, or academic research, the conventional degree remains essential.<br><br>"
         "<b>Verdict for the Modern Learner</b><br>"
         "Prospective candidates must audit their learning preferences. Those who thrive under practical mentorship and structured accountability should pursue apprenticeships; those seeking broad exploratory academic growth will find campus life irreplaceable."),
        ("Mock 3 &bull; Writing Exemplar &bull; Task 2 (Persuasive Email to Chamber of Commerce)",
         "<b>Task 2 Benchmark Exemplar: Business Consultation Email</b><br>"
         "<b>To:</b> chairperson@regionalchamber.org.uk<br>"
         "<b>From:</b> abdul.skills@workforcedevelopment.co.uk<br>"
         "<b>Date:</b> 21 October 2026<br>"
         "<b>Subject:</b> Urgent Proposal: Expanding SME Apprenticeship Consortium Grants<br><br>"
         "Dear Madam Chairperson,<br><br>"
         "I am writing on behalf of regional training providers to urge the Chamber of Commerce to spearhead an Apprenticeship Levy Transfer Consortium for local small and medium-sized enterprises (SMEs).<br><br>"
         "As our local business community grapples with severe technical skills shortages, over &pound;4.2 million in unspent Levy funds from large regional corporations continues to expire and return to the Treasury unutilized each year. By establishing an agile Chamber-led transfer hub, we can redirect these funds to cover 100% of training costs for 250 local SME apprentices across engineering, logistics, and digital services.<br><br>"
         "This initiative will provide three immediate regional dividends:<br>"
         "1. Close critical technician and engineering vacancies without capital cost to small firms.<br>"
         "2. Create high-value, salaried career pathways for school leavers from disadvantaged postcodes.<br>"
         "3. Retain top young talent within our regional economy.<br><br>"
         "I would welcome the opportunity to present a 15-minute briefing paper at the upcoming Executive Committee meeting on 5 November. Thank you for your leadership on regional economic growth.<br><br>"
         "Yours sincerely,<br><br>"
         "Subi<br>"
         "Lead Vocational Workforce Consultant")
    ],
    4: [
        ("Mock 4 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Generative AI tools processed over 1.2 billion administrative queries in UK financial firms last year.'</i> (Quantifiable empirical metric). Opinion: <i>'Automation will eradicate all junior professional roles within five years.'</i> (Speculative prediction).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'algorithmic safety nets'</i> implies automated systems designed to intercept human errors before regulatory disclosures occur.<br>"
         "<b>Q3. Organisational Features in Text A:</b> Infographic workflow diagrams, bold technical nomenclature, and boxed compliance callouts.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive metaphor: <i>'surrendering our human intuition to black-box decision making'</i>. (2) Rhetorical antithesis: <i>'fast but flawed, efficient yet devoid of empathy'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 2 of Text B, <i>'hallucination'</i> refers to an AI model producing plausible but entirely fabricated and inaccurate information.<br>"
         "<b>Q6. The Writer's Purpose in Text B:</b> To alert corporate governance teams to the ethical, legal, and copyright liabilities inherent in unchecked automated software integration.<br>"
         "<b>Q7. Synthesizing AI Integration Perspectives:</b> Text A focuses on exponential productivity leaps and repetitive task reduction, while Text B highlights risk mitigation, data privacy vulnerabilities, and the preservation of human critical thinking.<br>"
         "<b>Q8. Comparison of Regulatory Approaches:</b> Both authors concur that internal governance frameworks must be established. Text A advocates for agile vendor auditing, while Text B insists on mandatory human-in-the-loop sign-off protocols.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A provides verifiable industry survey data from chartered accountants, whereas Text B relies on philosophical and ethical essays, making Text A superior for commercial planning but Text B vital for risk ethics."),
        ("Mock 4 &bull; Writing Exemplar &bull; Task 1 (Formal Contribution to a Government Consultation Review)",
         "<b>Task 1 Benchmark Exemplar: Government Consultation Submission</b><br>"
         "<b>To:</b> Parliamentary Select Committee on Science, Innovation and Technology<br>"
         "<b>From:</b> Subi, Senior Digital Ethics &amp; Functional Skills Lead<br>"
         "<b>Date:</b> 25 October 2026<br>"
         "<b>Subject:</b> Written Evidence: AI Integration Standards in Vocational &amp; Enterprise Education<br><br>"
         "<b>1. Introduction &amp; Terms of Reference</b><br>"
         "This evidence submission addresses the urgent need to embed AI literacy and critical validation frameworks within the statutory national curriculum for adult and vocational education.<br><br>"
         "<b>2. Workplace Vulnerabilities &amp; The Skills Gap</b><br>"
         "While modern business software rapidly incorporates automated synthesis, frontline workers lack formal instruction in prompt engineering, data privacy, and output verification. Inadvertent disclosure of personal client data into public cloud models represents a catastrophic GDPR compliance vulnerability.<br><br>"
         "<b>3. The Critical Verification Protocol (CVP)</b><br>"
         "We recommend mandating the 3-step 'Critical Verification Protocol' across all accredited vocational training:<br>"
         "&bull; <i>Source Origin Verification:</i> Requiring human tracing of algorithmic outputs to primary authoritative records.<br>"
         "&bull; <i>Bias &amp; Hallucination Audit:</i> Cross-referencing numerical claims against certified national statistics.<br>"
         "&bull; <i>Ethical Attribution:</i> Transparent disclosure of automated drafting assistance in commercial documents.<br><br>"
         "<b>4. Conclusion &amp; Policy Recommendations</b><br>"
         "The UK can lead responsible technological adoption by establishing funded Level 2 and Level 3 Digital Safety modules within adult education budgets."),
        ("Mock 4 &bull; Writing Exemplar &bull; Task 2 (Informative Staff Guide / Review)",
         "<b>Task 2 Benchmark Exemplar: Internal Staff Guidance Article</b><br>"
         "<b>Title: Working Alongside AI: 5 Golden Rules for Daily Productivity &amp; Security</b><br>"
         "<b>Published in:</b> Enterprise Operations Monthly Newsletter<br><br>"
         "Artificial Intelligence is no longer sci-fi theory; it is embedded in the word processors, spreadsheets, and email clients we use daily. When harnessed strategically, these tools liberate us from repetitive drudgery. However, cutting corners can lead to costly blunders.<br><br>"
         "Here are the five mandatory golden rules every team member must adhere to:<br><br>"
         "<b>1. Never Paste Confidential Client Data into Public Tools</b><br>"
         "Any information uploaded to public web models enters the vendor's training corpus. Always use our corporate enterprise-licensed, closed-circuit software.<br><br>"
         "<b>2. You Are Legally Responsible for Every Word You Send</b><br>"
         "Saying 'the AI generated that error' is not a valid defense before our clients or regulators. Every summary, calculation, and document requires thorough human proofreading.<br><br>"
         "<b>3. Beware the Plausible Hallucination</b><br>"
         "Language models excel at generating fluent prose, but they can invent citations, case law, and statistics with convincing authority. Verify every datum independently.<br><br>"
         "<b>4. Treat Algorithms as Junior Assistants, Not Senior Directors</b><br>"
         "Use tools to generate outlines, brainstorm email drafts, or format raw data. Reserve strategic judgment, empathy, and final decisions for human expertise.<br><br>"
         "<b>5. Continually Upgrade Your Prompting Skills</b><br>"
         "Clear context yields precise answers. Attend our weekly Wednesday lunchtime digital skills drop-in workshops to master advanced prompt syntax!")
    ],
    5: [
        ("Mock 5 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Over 18,000 residents utilize local green recreational corridors weekly.'</i> (Empirical council footfall tally). Opinion: <i>'Converting wild parkland into leisure complexes is a heartless betrayal of community heritage.'</i> (Subjective moral judgment).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'concrete creep'</i> implies gradual, insidious urban encroachment that permanently destroys biodiverse habitats without explicit public consultation.<br>"
         "<b>Q3. Structural Features in Text A:</b> Quotation pull-quotes, bulleted biodiversity statistics, and a highlighted petition signature counter.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive appeal to civic pride: <i>'rejuvenating our forgotten industrial riverside into a thriving beacon of prosperity'</i>. (2) Contrast: <i>'derelict wasteland transformed into state-of-the-art facilities'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'regeneration'</i> denotes the economic and social revitalization of an urban area through capital development.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To persuade local council planning officers and business owners to approve commercial development by accentuating economic dividends.<br>"
         "<b>Q7. Synthesizing Environmental &amp; Commercial Priorities:</b> Text A champions ecological preservation, public health, and free access to open nature, whereas Text B prioritizes job creation, municipal tax revenue, and modern indoor leisure facilities.<br>"
         "<b>Q8. Comparison of Community Value:</b> Both texts claim to advocate for community wellbeing. Text A defines wellbeing as clean air, native trees, and tranquil walking spaces; Text B defines wellbeing as modern leisure centers, youth sports facilities, and employment opportunities.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A includes certified botanical and ornithological survey data, establishing strong scientific credibility, whereas Text B relies heavily on developer promotional forecasts."),
        ("Mock 5 &bull; Writing Exemplar &bull; Task 1 (Formal Proposal Letter to National Lottery Community Fund)",
         "<b>Task 1 Benchmark Exemplar: Grant Funding Proposal Letter</b><br>"
         "<b>The Grant Assessment Committee</b><br>"
         "National Lottery Community Fund<br>"
         "100 Wharf Road, London, SE1 7NN<br><br>"
         "<b>From:</b> Subi, Project Director, GreenCorridor Community Trust<br>"
         "<b>Date:</b> 28 October 2026<br>"
         "<b>Subject:</b> Grant Application: Riverside Wildlife &amp; Wellbeing Community Trail (&pound;48,500)<br><br>"
         "Dear Members of the Committee,<br><br>"
         "On behalf of the GreenCorridor Community Trust, I am proud to submit our funding proposal to establish the Riverside Wildlife &amp; Wellbeing Community Trail, transforming 3.5 kilometres of neglected riverbank into an accessible, biodiverse green haven for 25,000 local residents.<br><br>"
         "<b>1. Community Need &amp; Social Cohesion</b><br>"
         "Our ward ranks within the top 15% most deprived urban areas nationally for accessible green space. Over 40% of local families live in flats without private gardens. This project directly addresses post-pandemic social isolation and pediatric physical inactivity by creating an inclusive space for all ages.<br><br>"
         "<b>2. Proposed Capital Works &amp; Accessibility</b><br>"
         "The requested &pound;48,500 grant will fund:<br>"
         "&bull; <b>Accessible All-Weather Pathway:</b> Installing recycled permeable gravel pathways suitable for wheelchairs, mobility scooters, and prams (&pound;22,000).<br>"
         "&bull; <b>Sensory Community Garden &amp; Seating:</b> Designing native flower meadows, raised herb planters, and timber benches (&pound;16,500).<br>"
         "&bull; <b>Educational Signage &amp; Youth Wildlife Club:</b> Installing Braille-enabled interactive wildlife boards and funding 12 weekend nature workshops (&pound;10,000).<br><br>"
         "<b>3. Project Sustainability &amp; Volunteer Legacy</b><br>"
         "Over 65 local volunteers have pledged ongoing maintenance support, partnered with the local vocational college horticultural department. We enclose our detailed financial audit, risk assessments, and council planning letters for your review.<br><br>"
         "Thank you for considering our application to create a lasting green legacy.<br><br>"
         "Yours sincerely,<br><br>"
         "Subi<br>"
         "Project Director, GreenCorridor Community Trust"),
        ("Mock 5 &bull; Writing Exemplar &bull; Task 2 (Inspiring Local Newspaper Article / Volunteer Appeal)",
         "<b>Task 2 Benchmark Exemplar: Local Gazette Feature Article</b><br>"
         "<b>Title: Reclaiming Our Riverbank: Join the Green Revolution on Your Doorstep!</b><br>"
         "<b>Byline:</b> Community Action Champion<br><br>"
         "Take a stroll down to the Old Mill Bridge this morning. What do you see? For years, the answer was heart-breaking: rusted shopping trolleys, discarded plastic bottles, and overgrown brambles choking what should be the crown jewel of our town.<br><br>"
         "Now, close your eyes and imagine something extraordinary: Kingfishers darting across clear water, children learning to identify bumblebees in wildflower meadows, and grandparents enjoying a peaceful, smooth stroll along an accessible sunlit boardwalk.<br><br>"
         "That vibrant dream is becoming reality—and YOU hold the power to make it happen!<br><br>"
         "This Saturday, 1 November, the Riverside Trust is hosting our Great Autumn Community Action Day. Armed with garden rakes, planting trowels, and sheer community pride, over 100 neighbors of all ages will unite to plant 500 native trees and clear historical litter from the riverbank.<br><br>"
         "No gardening expertise is necessary. Whether you can dig planting holes for an hour, serve hot tea and soup, or build hedgehog shelters with our youth club, every single pair of hands matters. Free gloves, high-vis vests, and refreshments are provided.<br><br>"
         "Let us refuse to leave our town's environment to chance. Meet us at Old Mill Wharf at 09:30 AM this Saturday. Let us plant the seeds of a greener, healthier community together!")
    ],
    6: [
        ("Mock 6 &bull; Reading Section Model Answers (Q1&ndash;Q9)",
         "<b>Q1. Fact vs Opinion in Text A:</b> Fact: <i>'Specialist geriatric bed capacity decreased by 14% over the preceding decade.'</i> (Audited NHS statistical record). Opinion: <i>'Decentralized community care is an unmitigated disaster created purely to cut funding.'</i> (Subjective polemical claim).<br>"
         "<b>Q2. Implicit Meaning in Text A:</b> The phrase <i>'bed-blocking through bureaucratic paralysis'</i> implies that vulnerable patients remain stranded in hospital wards not due to clinical illness, but because social care assessment paperwork is hopelessly delayed.<br>"
         "<b>Q3. Organisational Features in Text A:</b> Analytical bar charts comparing hospital stay durations, authoritative clinical footnotes, and clear institutional subheadings.<br>"
         "<b>Q4. Language Devices in Text B:</b> (1) Emotive anecdote: <i>'an 84-year-old widow clutching her teacup, thriving among her beloved garden memories'</i>. (2) High-modality vocabulary: <i>'dignity, autonomy, and familiar comfort'</i>.<br>"
         "<b>Q5. Vocabulary in Context:</b> In paragraph 3 of Text B, <i>'domiciliary'</i> refers to medical or supportive care delivered directly inside a patient's private home rather than a hospital.<br>"
         "<b>Q6. Author's Purpose in Text B:</b> To advocate for massive investment into professional home-care packages as the most humane, clinically effective, and cost-efficient care delivery model.<br>"
         "<b>Q7. Synthesizing Healthcare Reform Proposals:</b> Text A focuses on secondary care hospital bottlenecks, clinical bed management, and emergency ward pressures, while Text B provides the long-term solution: robust community-based social care that prevents hospital admissions altogether.<br>"
         "<b>Q8. Comparison of Fiscal Metrics:</b> Both authors recognize the current model is fiscally unsustainable. Text A demonstrates that an acute NHS bed costs &pound;480 per night, whereas Text B proves that equivalent comprehensive home-care support costs less than &pound;95 per day.<br>"
         "<b>Q9. Critical Evaluation of Source Validity:</b> Text A draws upon peer-reviewed clinical audit data from the British Medical Journal, ensuring highest empirical validity, whereas Text B offers inspiring qualitative case studies that capture patient dignity powerfully."),
        ("Mock 6 &bull; Writing Exemplar &bull; Task 1 (Formal Briefing Memo to Hospital Management Board)",
         "<b>Task 1 Benchmark Exemplar: Executive Healthcare Memo</b><br>"
         "<b>MEMORANDUM</b><br>"
         "<b>To:</b> Chief Executive &amp; Management Board, St Jude's NHS Healthcare Trust<br>"
         "<b>From:</b> Subi, Clinical Operations Integration Manager<br>"
         "<b>Date:</b> 30 October 2026<br>"
         "<b>Subject:</b> Urgent Operational Strategy: Mitigating Delayed Discharge Through Hospital-to-Home Pathways<br><br>"
         "<b>1. Purpose of Briefing</b><br>"
         "This memorandum outlines immediate operational interventions to address delayed transfers of care (DTOC), which currently account for 18.4% of non-elective bed occupancy across acute wards.<br><br>"
         "<b>2. Current Capacity Crisis &amp; Bottlenecks</b><br>"
         "Over 62 medically optimized patients remain stranded in acute beds due to delays in securing adult social care assessments and medication delivery. This logjam creates severe emergency department ambulance handover delays (averaging 74 minutes).<br><br>"
         "<b>3. The 'Discharge to Assess' (D2A) Action Model</b><br>"
         "We propose implementing an integrated 4-tier Discharge to Assess protocol:<br>"
         "&bull; <i>Dedicated Trust Transport Fleet:</i> Guaranteeing same-day morning patient transfers with essential 48-hour medication packs.<br>"
         "&bull; <i>Co-Located Social Workers:</i> Embedding council social work coordinators directly on ward rounds at 08:30 daily.<br>"
         "&bull; <i>Rapid Community Response Team:</i> Conducting occupational therapy home visits within 4 hours of patient arrival.<br><br>"
         "<b>4. Financial &amp; Clinical Impact</b><br>"
         "Repurposing &pound;120,000 from temporary agency nursing into dedicated community bridge-carers will release 42 acute beds daily, saving &pound;640,000 in bed-day penalties within six months.<br><br>"
         "<b>5. Next Steps</b><br>"
         "Board authorization is requested to launch the D2A pathway across Wards 4, 7, and 9 effective Monday 10 November 2026."),
        ("Mock 6 &bull; Writing Exemplar &bull; Task 2 (Persuasive Opinion Article for Local Newspaper)",
         "<b>Task 2 Benchmark Exemplar: Regional Opinion Article</b><br>"
         "<b>Title: Caring for Our Elders: Why Home, Not Hospital, is Where Healing Happens</b><br>"
         "<b>Byline:</b> Health &amp; Society Columnist<br><br>"
         "Imagine spending six weeks trapped in a sterile, fluorescent-lit hospital ward. You are clinically recovered, yet the exit door remains firmly shut because nobody has arrived to assess your front doorstep for a wooden ramp.<br><br>"
         "This is not a dramatic fiction; it is the daily reality for hundreds of vulnerable pensioners across our county. Our hospitals are remarkable at saving lives in acute crises. But a noisy, impersonal ward is the worst possible place for an elderly patient to regain independence.<br><br>"
         "In a hospital bed, elderly muscles atrophy. Within ten days of bed rest, an older adult can lose up to 10% of muscle mass. Confusion and delirium spike. Yet back in their own armchair, surrounded by familiar tea mugs, family photos, and the radio playing softly, recovery accelerates dramatically.<br><br>"
         "Why then do we continue to pump millions into acute beds while starving community home-carers of fair wages and travel allowances? It defies both common humanity and economic sense.<br><br>"
         "Let us demand that our regional health commissioners redirect resources where they belong: into well-paid, highly respected domiciliary carers. Our parents and grandparents spent their lifetimes building our community. The very least they deserve is the dignity of growing old in the comfort of their own homes.")
    ]
}
'''

def update():
    with open(REF_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find where ENGLISH_L2_MOCK_SOLUTIONS starts
    start_pos = content.find("ENGLISH_L2_MOCK_SOLUTIONS = {")
    if start_pos == -1:
        print("ERROR: ENGLISH_L2_MOCK_SOLUTIONS not found!")
        return

    # Find the end of this dict
    end_pos = content.find("DIGITAL_SKILLS_SOLUTIONS = {", start_pos)
    if end_pos == -1:
        print("ERROR: DIGITAL_SKILLS_SOLUTIONS not found!")
        return

    new_content = content[:start_pos] + MOCKS_SOLUTIONS_EXPANSION.strip() + "\n\n" + content[end_pos:]
    with open(REF_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("specialist_suite_reference.py updated with rich solutions for all 6 English mocks!")

if __name__ == "__main__":
    update()
