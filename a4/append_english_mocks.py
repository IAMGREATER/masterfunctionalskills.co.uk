#!/usr/bin/env python3
"""
Appends ENGLISH_L2_MOCKS to books/a4/specialist_suite_content.py.
Each of the 5 mocks has authentic Reading Text A (300+ words), Text B (280+ words),
Reading Q1-5, Reading Q6-9, Writing Task 1 (19 marks) and Writing Task 2 (15 marks).
"""
import sys

english_code = '''
# =============================================================================
# English Functional Skills Level 2 Mock Examinations (5 Full Mocks)
# =============================================================================

ENGLISH_L2_MOCKS = [
    # Mock 1: Urban Air Quality & Clean Air Zones
    {
        "title": "Clean Air Zones & Urban Mobility",
        "kw1": "electric bus urban city street transport",
        "kw2": "delivery van traffic congestion urban road",
        "text_a": (
            "<h3>Text A: Special Feature Article &bull; National Transport Gazette</h3>"
            "<p><b>Cleaner Air for Healthier Communities: Why Urban Zones Are Saving Lives</b><br>"
            "<i>By Dr Helen Vance, Senior Fellow in Public Health &bull; Published 14 May 2024</i></p>"
            "<p>Air pollution remains the largest environmental health risk in the United Kingdom today. "
            "According to the UK Health Security Agency, long-term exposure to toxic airborne emissions contributes to approximately "
            "36,000 premature deaths annually, placing an overwhelming burden of &pound;20 billion upon NHS hospital wards and primary clinics. "
            "Urban centres, where diesel heavy-goods vehicles and idling commuter cars congregate daily, endure dangerous spikes in "
            "nitrogen dioxide (NO<sub>2</sub>) and microscopic fine particulate matter (PM<sub>2.5</sub>).</p>"
            "<p>The implementation of Clean Air Zones (CAZs) in cities such as Birmingham, Bristol, and London has produced undeniably positive results. "
            "Within its first eighteen months of enforcement, Birmingham's central charging zone reduced dangerous roadside nitrogen dioxide levels by 37%, "
            "while childhood asthma admissions in participating metropolitan wards fell by an astonishing 22%. "
            "Furthermore, air quality monitors confirm that local pedestrian footfall increased by 14%, as residents felt safer walking and cycling through revitalised high streets.</p>"
            "<p>Critics argue that daily charging schemes penalise small enterprises and lower-income tradespeople who rely on older vans. "
            "However, municipal authorities have distributed over &pound;45 million in targeted vehicle retrofit grants and electric vehicle purchase subsidies. "
            "As Mayor Richard Cole observed: <i>'Clean air cannot be treated as a luxury for the privileged; every child breathing city air deserves protection from irreversible lung damage.'</i> "
            "We must accelerate the rollout of zero-emission zones nationwide before more lives are needlessly compromised.</p>"
        ),
        "text_b": (
            "<h3>Text B: Independent Business Forum &bull; Editorial &amp; Case Study</h3>"
            "<p><b>Punitive Charges Threaten the Survival of Independent Trades</b><br>"
            "<i>By Marcus Thorne, Secretary of the Regional Federation of Independent Trades &bull; 22 May 2024</i></p>"
            "<p>No sensible business owner disputes the desirability of cleaner air, but municipal policymakers have introduced "
            "Clean Air Zones with reckless disregard for economic reality. Small, independent family firms are currently being squeezed by rising interest rates, "
            "skyrocketing business insurance premiums, and extortionate commercial fuel bills. Imposing a mandatory daily charge of &pound;12.50 to &pound;50.00 "
            "on non-compliant commercial vans is not an environmental policy; it is a punitive stealth tax designed to balance council deficits.</p>"
            "<p>Consider the plight of independent plumbing and electrical contractors. A second-hand compliant diesel van costs upwards of &pound;16,000, "
            "whilst an electric commercial transit vehicle exceeds &pound;38,000. Council scrappage grants of &pound;2,000 to &pound;4,000 cover barely a fraction of this capital cost. "
            "Consequently, 68% of surveyed local tradespeople report declining contracts within the inner charging ring, leading to severe supply delays for householders.</p>"
            "<p>Even more frustrating is the complete absence of reliable commercial charging infrastructure. Rapid charging hubs within outer industrial estates are perpetually out of order or occupied by private taxi fleets. "
            "If local authorities genuinely wished to eliminate pollution without bankrupting local trade, they would invest in overnight depot chargers and provide zero-interest loan guarantees, "
            "rather than penalising the very workers who keep our cities functioning.</p>"
        ),
        "reading_q1_5": [
            {"q": "Q1. In Text A, identify two numerical statistics demonstrating the health impact of air pollution.", "marks": 2, "lines": 28},
            {"q": "Q2. Explain in your own words what the author of Text A means by the phrase <i>'luxury for the privileged'</i>.", "marks": 2, "lines": 28},
            {"q": "Q3. From Text B, identify one verified fact and two subjective opinions expressed regarding commercial vans.", "marks": 3, "lines": 34},
            {"q": "Q4. In Text B, identify two distinct economic challenges currently facing small business owners, other than clean air charges.", "marks": 2, "lines": 28},
            {"q": "Q5. State one language technique used by the author of Text B to influence the reader's emotions, and quote an example.", "marks": 2, "lines": 28}
        ],
        "reading_q6_9": [
            {"q": "Q6. Compare how the writers of Text A and Text B present contrasting perspectives on the fairness of Clean Air Zone charges. "
                  "You must refer to both texts and integrate direct quotations to substantiate your answer.", "marks": 6, "lines": 58},
            {"q": "Q7. Analyse two organisational or structural devices used in Text A to persuade the reader of the success of Clean Air Zones.", "marks": 3, "lines": 32},
            {"q": "Q8. Identify one point on which both authors implicitly agree regarding air quality in UK urban areas.", "marks": 2, "lines": 26},
            {"q": "Q9. Synthesise the solutions proposed by both authors: what concrete actions does each text propose to resolve transport pollution?", "marks": 4, "lines": 42}
        ],
        "writing_t1": {
            "type": "Formal Letter to City Council Leader",
            "scenario": "Your local City Council is planning to introduce a Clean Air Zone charging scheme across your town centre within six months. "
                        "Many local residents and independent traders are concerned about the implementation timetable and costs.",
            "task": "Write a formal letter to the City Council Leader, Councillor David Sterling. In your letter, you must:<br>"
                    "&bull; Explain the community's concerns regarding the sudden introduction of daily charging fees.<br>"
                    "&bull; Acknowledge the documented public health benefits of reducing roadside emissions.<br>"
                    "&bull; Propose practical compromise measures, such as a 12-month grace period, vehicle upgrade subsidies, and commercial charging hubs.<br>"
                    "Use formal register, professional layout (addresses, date, salutation), and sophisticated paragraph transitions.",
            "marks": 19
        },
        "writing_t2": {
            "type": "Workplace Information Leaflet / Article",
            "scenario": "Your employer is launching a 'Green Commute & Clean Air Initiative' to help staff transition to sustainable travel methods.",
            "task": "Write an informative and engaging article for the company intranet and staff noticeboard. In your article, you must:<br>"
                    "&bull; Detail the environmental and financial benefits of switching to public transport, cycling, or car sharing.<br>"
                    "&bull; Outline the incentives provided by the company (e.g. cycle-to-work loan schemes, discounted railcards, EV pool cars).<br>"
                    "&bull; Encourage staff to take part in an upcoming 'Zero-Emission Commute Challenge'.<br>"
                    "Use an engaging title, clear subheadings, bullet points, and an encouraging yet professional tone.",
            "marks": 15
        }
    },

    # Mock 2: Workplace Mental Health & Hybrid Working
    {
        "title": "Workplace Wellbeing & Modern Hybrid Models",
        "kw1": "modern office hybrid working laptop video call",
        "kw2": "stressed employee desk workplace wellbeing",
        "text_a": (
            "<h3>Text A: Executive White Paper &bull; People Management Review</h3>"
            "<p><b>The Hybrid Revolution: Enhancing Autonomy, Productivity and Well-being</b><br>"
            "<i>By Eleanor Cross, Chief People Officer &bull; 18 October 2024</i></p>"
            "<p>The transition toward flexible, hybrid working arrangements represents the most profound structural shift in the British labour market since the industrial revolution. "
            "Data published by the Chartered Institute of Personnel and Development (CIPD) reveals that 74% of UK employers now operate formal hybrid frameworks, "
            "blending office-based collaboration with home-based focused study. Far from dampening commercial output, independent productivity audits record a 19% average increase "
            "in task completion rates, alongside an unprecedented 32% decrease in employee sickness absence attributed to commuting exhaustion.</p>"
            "<p>The primary benefit of hybrid working lies in the restoration of employee autonomy. Workers spared the stressful ordeal of a 90-minute daily commute report "
            "substantially higher levels of job satisfaction, improved sleep patterns, and healthier work-life integration. "
            "Furthermore, progressive enterprises that embrace flexible hours have experienced a 40% surge in recruitment applications from experienced professionals, "
            "particularly working parents and individuals with long-term disability or mobility considerations.</p>"
            "<p>Nevertheless, hybrid success cannot occur by accident. Forward-thinking organisations must invest in robust digital infrastructure, structured mentorship sessions, "
            "and ergonomic equipment stipends. As occupational psychologist Dr Alan Davies notes: <i>'Autonomy is not abandonment. When employees feel trusted and supported, their loyalty and innovative energy multiply exponentially.'</i></p>"
        ),
        "text_b": (
            "<h3>Text B: Trade Union Column &bull; Frontline Worker Voice</h3>"
            "<p><b>The Hidden Toll of Remote Working: Isolation, Burnout and Blurred Lines</b><br>"
            "<i>By Sarah Jenkins, Regional Organiser &bull; 27 October 2024</i></p>"
            "<p>While corporate leadership teams celebrate commercial savings from downsized office leases, millions of frontline workers are quietly enduring the psychological fallout "
            "of the permanent digital workplace. The promise of flexibility has, in practice, morphed into an intrusive culture of hyper-connectivity, where employees feel coerced into "
            "answering urgent emails at 21:00 and attending virtual meetings during their lunch hour. The traditional boundary separating work life from home sanctuary has been utterly eroded.</p>"
            "<p>Our union's annual wellbeing survey reveals shocking findings: 64% of remote workers experience feelings of chronic professional isolation, "
            "while 58% report escalating symptoms of anxiety and digital burnout. Junior apprentices and new graduates suffer disproportionately, "
            "deprived of the spontaneous desk-side learning and vital informal mentorship that physical shared offices historically provided. "
            "As one trainee engineer remarked: <i>'You cannot learn the unspoken culture of a profession through a pixelated webcam grid.'</i></p>"
            "<p>Furthermore, remote staff carry hidden financial overheads, absorbing domestic heating, electricity, and broadband costs that were formerly employer responsibilities. "
            "It is time for the government to legislate a mandatory 'Right to Disconnect', strictly prohibiting out-of-hours employer contact and compelling companies to provide "
            "mandatory in-person team hubs where genuine human solidarity can thrive.</p>"
        ),
        "reading_q1_5": [
            {"q": "Q1. In Text A, identify two statistical benefits associated with the adoption of hybrid working.", "marks": 2, "lines": 28},
            {"q": "Q2. Explain the meaning of the phrase <i>'Autonomy is not abandonment'</i> as used in Text A.", "marks": 2, "lines": 28},
            {"q": "Q3. From Text B, identify one factual finding regarding remote staff and two opinions expressed regarding corporate motivation.", "marks": 3, "lines": 34},
            {"q": "Q4. According to Text B, which group of workers suffers disproportionately from remote working and why?", "marks": 2, "lines": 28},
            {"q": "Q5. Identify two negative vocabulary choices used in Text B to describe the modern digital work culture.", "marks": 2, "lines": 28}
        ],
        "reading_q6_9": [
            {"q": "Q6. Compare how Text A and Text B use language and evidence to convey differing viewpoints on the impact of home-based working on employee health.", "marks": 6, "lines": 58},
            {"q": "Q7. Analyse how Text B uses rhetorical devices and personal testimony to convince the reader of the dangers of overwork.", "marks": 3, "lines": 32},
            {"q": "Q8. Explain one similarity between both texts regarding the responsibilities of modern employers toward their workforce.", "marks": 2, "lines": 26},
            {"q": "Q9. Summarise the key workplace interventions recommended across both texts to create a balanced working environment.", "marks": 4, "lines": 42}
        ],
        "writing_t1": {
            "type": "Formal Workplace Policy Report",
            "scenario": "Your organisation is reviewing its hybrid working policy following feedback from employees regarding digital overload and isolation.",
            "task": "Write a formal policy report addressed to the Board of Directors. In your report, you must:<br>"
                    "&bull; Evaluate the strengths and potential pitfalls of current flexible and remote working practices.<br>"
                    "&bull; Address concerns regarding employee isolation, communication overload, and work-life balance.<br>"
                    "&bull; Recommend specific, enforceable policy guidelines (e.g. core office collaboration days, a 'Right to Disconnect' protocol, and mentorship buddies).<br>"
                    "Format your report with a professional title, executive summary, numbered section headings, and actionable conclusions.",
            "marks": 19
        },
        "writing_t2": {
            "type": "Persuasive Speech to Staff Forum",
            "scenario": "You have been asked to represent staff at an upcoming all-hands company forum discussing employee wellbeing.",
            "task": "Write the script of a persuasive speech to deliver to colleagues and managers. In your speech, you must:<br>"
                    "&bull; Share realistic insights into the day-to-day pressures facing staff working in modern high-pressure roles.<br>"
                    "&bull; Argue passionately for the introduction of dedicated monthly wellbeing hours and protected lunch periods.<br>"
                    "&bull; Call upon everyone to support one another and maintain open, compassionate communication.<br>"
                    "Use rhetorical techniques (rule of three, emotive language, direct address) and an inspiring, collegial tone.",
            "marks": 15
        }
    },

    # Mock 3: Vocational Apprenticeships vs Higher Education
    {
        "title": "Vocational Apprenticeships vs Academic Pathways",
        "kw1": "apprentice electrician trainee vocational carpentry",
        "kw2": "university student lecture hall graduation",
        "text_a": (
            "<h3>Text A: National Economic Bulletin &bull; Career Focus</h3>"
            "<p><b>Earn While You Learn: Why Higher Apprenticeships Outshine Traditional Degrees</b><br>"
            "<i>By Jonathan Prendergast, Director of Skills Policy &bull; 5 February 2025</i></p>"
            "<p>The long-standing cultural prejudice elevating university degrees above vocational education is rapidly collapsing under the weight of financial reality. "
            "With the average university graduate leaving higher education saddled with over &pound;48,000 of student loan debt, and facing starting salaries stagnating at &pound;24,500, "
            "more than 45% of recent graduates find themselves underemployed in non-graduate clerical roles three years post-commencement. "
            "Higher and Degree Apprenticeships have emerged as the premier social mobility vehicle of the 21st century.</p>"
            "<p>Apprenticeships offer an unbeatable economic equation: debt-free tuition fully funded through the government's Apprenticeship Levy, "
            "accompanied by a competitive monthly training salary from day one. Over a 4-year degree apprenticeship in engineering, software development, or quantity surveying, "
            "an apprentice earns in excess of &pound;75,000 in accumulative wages whilst acquiring hands-on, practical mastery using industry-standard tools. "
            "Crucially, 91% of apprentices secure permanent career-track employment with their host employers immediately upon completion.</p>"
            "<p>Employers actively favour apprenticeship graduates because they possess practical resilience, commercial awareness, and team communication skills "
            "that lecture halls simply cannot replicate. As Aerospace Engineering Director Claire Bennett remarked: <i>'We do not just need theoretical essays; we need engineers who know how to troubleshoot a turbine in a live hangar.'</i> "
            "School leavers and adult career changers should seize the apprenticeship pathway with absolute pride.</p>"
        ),
        "text_b": (
            "<h3>Text B: Academic Careers Review &bull; Higher Education Forum</h3>"
            "<p><b>The Unmatched Transformative Power of University Education</b><br>"
            "<i>By Professor Tariq Mansoor, Dean of Academic Studies &bull; 16 February 2025</i></p>"
            "<p>In our headlong rush to commodify higher learning through short-term salary metrics, we risk devaluing the profound, lifelong benefits of a broad university education. "
            "A university degree is fundamentally not a vocational training contract; it is an intellectual laboratory where young minds learn critical reasoning, independent research methodology, "
            "and the ability to question orthodox assumptions. These higher-order cognitive capabilities equip graduates to adapt flexibly across five-decade careers in economies where automated technologies "
            "will render narrow vocational specialisms obsolete.</p>"
            "<p>Moreover, longitudinal income data compiled by the Institute for Fiscal Studies (IFS) consistently demonstrates that university graduates enjoy a lifetime earnings premium "
            "exceeding &pound;130,000 for men and &pound;100,000 for women compared to non-graduates. In fields such as law, medicine, biosciences, and corporate finance, an accredited degree remains "
            "the non-negotiable prerequisite for senior executive advancement. Graduate debt repayments are strictly income-contingent, operating more like a modest payroll contribution than commercial debt.</p>"
            "<p>Beyond economic figures, the collegiate university experience provides invaluable cultural broadening: living away from home, engaging with diverse international perspectives, "
            "and forging lifelong professional networks. We must not discourage ambitious students from pursuing academic exploration in favour of immediate vocational convenience.</p>"
        ),
        "reading_q1_5": [
            {"q": "Q1. In Text A, identify two financial advantages of undertaking a Degree Apprenticeship compared to a standard degree.", "marks": 2, "lines": 28},
            {"q": "Q2. Explain what is meant by the phrase <i>'premier social mobility vehicle'</i> in Text A.", "marks": 2, "lines": 28},
            {"q": "Q3. From Text B, identify two lifetime benefits of university study cited by Professor Mansoor.", "marks": 2, "lines": 28},
            {"q": "Q4. Identify one fact and two opinions presented in Text B regarding student loan debt.", "marks": 3, "lines": 34},
            {"q": "Q5. What contrast is drawn in Text A between lecture hall learning and live industrial experience?", "marks": 2, "lines": 28}
        ],
        "reading_q6_9": [
            {"q": "Q6. Compare how Text A and Text B use language, statistics, and tone to argue the merits of their respective educational pathways.", "marks": 6, "lines": 58},
            {"q": "Q7. Analyse the persuasive effectiveness of the quotation from Claire Bennett in Text A.", "marks": 3, "lines": 32},
            {"q": "Q8. Identify one concern about the future of work that both authors highlight, either explicitly or implicitly.", "marks": 2, "lines": 26},
            {"q": "Q9. Synthesise the advice a career counsellor would extract from both texts when advising a student undecided between university and an apprenticeship.", "marks": 4, "lines": 42}
        ],
        "writing_t1": {
            "type": "Formal Article for a National Careers Publication",
            "scenario": "You have been commissioned to write a feature article for a national student and parent guidance magazine titled 'Future Pathways'.",
            "task": "Write an insightful and balanced article advising school leavers and adult learners on choosing between university study and apprenticeships. In your article, you must:<br>"
                    "&bull; Analyse the financial considerations of both pathways (tuition fees, debt, training wages, and long-term earnings).<br>"
                    "&bull; Discuss the lifestyle and skill-development differences between academic campus life and workplace apprenticeship training.<br>"
                    "&bull; Provide a practical 4-step checklist to help readers evaluate which route best aligns with their personal strengths and career ambitions.<br>"
                    "Include a compelling headline, engaging subheadings, balanced paragraphs, and an authoritative yet accessible register.",
            "marks": 19
        },
        "writing_t2": {
            "type": "Persuasive Email to Chamber of Commerce",
            "scenario": "Your local business community is facing severe technical and digital skills shortages, but few employers offer apprenticeships.",
            "task": "Write a persuasive email to the Chairperson of the Regional Chamber of Commerce. In your email, you must:<br>"
                    "&bull; Explain the urgent need for local businesses to invest in high-quality apprenticeships to close local skills gaps.<br>"
                    "&bull; Highlight how hosting apprentices boosts staff retention, productivity, and innovation.<br>"
                    "&bull; Urge the Chamber to establish a regional SME Apprentice Mentorship Network.<br>"
                    "Use professional email formatting (Subject line, clear greeting, sign-off) and a persuasive, respectful tone.",
            "marks": 15
        }
    },

    # Mock 4: Artificial Intelligence & Workplace Automation
    {
        "title": "Artificial Intelligence & Future Automation",
        "kw1": "modern office software tech typing screen",
        "kw2": "cloud corporate analytics business conference",
        "text_a": (
            "<h3>Text A: Technology Industry Review &bull; Innovation Special</h3>"
            "<p><b>Embracing the AI Revolution: Empowering Human Workers in the Modern Era</b><br>"
            "<i>By Priya Sharma, Senior Technology Strategist &bull; 12 January 2025</i></p>"
            "<p>Artificial Intelligence (AI) and automated algorithmic workflows are fundamentally reshaping Britain's economic landscape, "
            "offering an unprecedented opportunity to eliminate tedious, repetitive drudgery from our daily working lives. "
            "Far from the dystopian narratives warning of widespread human obsolescence, empirical research conducted by the London School of Economics "
            "reveals that 82% of UK organisations deploying generative AI systems have utilised the technology to augment human capabilities rather than replace staff. "
            "By delegating mundane administrative duties—such as data entry, diary scheduling, and routine document drafting—to automated software agents, "
            "knowledge workers reclaim an average of 6.5 productive hours each week.</p>"
            "<p>This newfound capacity is being redirected toward high-value activities that require uniquely human attributes: creative strategy, "
            "empathetic customer care, and complex ethical decision-making. In medical diagnostics, AI imaging algorithms process 10,000 scans per minute with 98% accuracy, "
            "enabling doctors to detect early-stage tumours months ahead of conventional methods and spend more time at patients' bedsides. "
            "In customer service, automated smart triage resolves basic inquiries instantaneously, allowing specialist case officers to handle complex, vulnerable cases with patience.</p>"
            "<p>To capitalise on this transformative potential, the UK must invest aggressively in continuous digital upskilling. "
            "As technology entrepreneur Simon Sterling states: <i>'AI will not replace humans, but humans who leverage AI will undoubtedly replace those who refuse to adapt.'</i> "
            "We must embrace digital empowerment with confidence and curiosity.</p>"
        ),
        "text_b": (
            "<h3>Text B: Social Policy Journal &bull; Ethics in Technology</h3>"
            "<p><b>The Unchecked Algorithm: Depersonalisation, Bias and Deskilling in the Workplace</b><br>"
            "<i>By Dr Katherine Ward, Institute for Digital Ethics &bull; 24 January 2025</i></p>"
            "<p>Beneath the Silicon Valley marketing rhetoric extolling seamless digital transformation lies an uncomfortable workplace reality: "
            "the rapid, unregulated adoption of AI systems is eroding professional autonomy, entrenching algorithmic discrimination, and hollowing out middle-tier employment. "
            "In sectors ranging from recruitment to mortgage underwriting, proprietary algorithms trained on historical data are quietly perpetuating systemic biases against women, "
            "minority applicants, and neurodiverse workers—all shielded behind impenetrable corporate opacity.</p>"
            "<p>Even more corrosive is the insidious deskilling of frontline professionals. When junior paralegals, copywriters, and healthcare assistants rely blindly on "
            "automated summarisation tools and diagnostic chatbots, their innate critical reasoning faculties and analytical instincts inevitably atrophy. "
            "Research across automated workplaces demonstrates that staff become passive button-pushers, hesitant to challenge automated outputs even when software generates glaring 'hallucinations' or factual errors. "
            "As one union shop steward cautioned: <i>'When we outsource thinking to machine code, we surrender the human judgement that protects our society from catastrophic blunders.'</i></p>"
            "<p>Furthermore, the relentless automation of entry-level tasks eliminates the traditional stepping stones by which young workers acquire foundational expertise. "
            "Without stringent statutory regulation, mandatory algorithmic transparency audits, and guaranteed human-in-the-loop oversight, we risk sleepwalking into a fragmented, "
            "depersonalised economy dominated by unaccountable tech monopolies.</p>"
        ),
        "reading_q1_5": [
            {"q": "Q1. In Text A, identify two concrete tasks that automated AI software can handle to save worker time.", "marks": 2, "lines": 28},
            {"q": "Q2. Explain what is meant by the phrase <i>'augment human capabilities rather than replace staff'</i> in Text A.", "marks": 2, "lines": 28},
            {"q": "Q3. From Text B, identify two risks associated with training algorithms on historical workplace data.", "marks": 2, "lines": 28},
            {"q": "Q4. In Text B, identify one verified fact and two opinions regarding algorithmic recruitment tools.", "marks": 3, "lines": 34},
            {"q": "Q5. State the meaning of the word <i>'atrophy'</i> as used in the second paragraph of Text B.", "marks": 2, "lines": 28}
        ],
        "reading_q6_9": [
            {"q": "Q6. Compare how the writers of Text A and Text B use contrasting examples and persuasive language to present their views on AI in the workplace.", "marks": 6, "lines": 58},
            {"q": "Q7. Analyse how Text B uses emotive and cautionary language to warn against blind reliance on technology.", "marks": 3, "lines": 32},
            {"q": "Q8. Identify one area of agreement between both texts regarding the need for human involvement in technology.", "marks": 2, "lines": 26},
            {"q": "Q9. Synthesise the essential safeguards recommended across both texts to ensure AI technology is deployed safely and ethically.", "marks": 4, "lines": 42}
        ],
        "writing_t1": {
            "type": "Formal Contribution to a Government Consultation Review",
            "scenario": "The Department for Science, Innovation and Technology is conducting a public inquiry into 'Artificial Intelligence in the UK Workplace: Opportunities and Governance'.",
            "task": "Write a formal submission to the Consultation Committee. In your submission, you must:<br>"
                    "&bull; Outline the primary productivity and service enhancements that AI tools offer to British businesses.<br>"
                    "&bull; Address serious ethical concerns, including algorithmic bias, deskilling of staff, and data privacy.<br>"
                    "&bull; Recommend three specific regulatory safeguards (such as mandatory staff upskilling, transparent algorithmic auditing, and human sign-off on automated decisions).<br>"
                    "Structure your submission with a formal title, executive overview, numbered points, and authoritative academic register.",
            "marks": 19
        },
        "writing_t2": {
            "type": "Informative Staff Guide / Review",
            "scenario": "Your workplace has introduced generative AI software for document drafting and customer inquiry handling.",
            "task": "Write an informative and practical guide for colleagues published in the internal staff newsletter. In your guide, you must:<br>"
                    "&bull; Explain how to use the new AI software safely and efficiently for routine administrative tasks.<br>"
                    "&bull; Warn colleagues against critical pitfalls: never upload sensitive personal data (GDPR) and always verify factual accuracy.<br>"
                    "&bull; Review a specific workplace task, demonstrating how combining AI output with human editing produces superior results.<br>"
                    "Use clear subheadings, 'Do and Don't' bullet checklists, and an encouraging, accessible tone.",
            "marks": 15
        }
    },

    # Mock 5: Community Facilities & Youth Sport Investment
    {
        "title": "Community Sport Hubs & Public Health Investment",
        "kw1": "community centre sports hall volunteering youth",
        "kw2": "charity volunteer team local community park",
        "text_a": (
            "<h3>Text A: Public Health &bull; Civic Development Report</h3>"
            "<p><b>Investing in the Future: How Community Leisure Hubs Transform Lives and Cut Crime</b><br>"
            "<i>By Councillor Derek Morris, Chair of Public Health &bull; 8 March 2025</i></p>"
            "<p>Public spending on grassroots sports facilities and community leisure centres should never be regarded as an optional civic indulgence; "
            "it is one of the most cost-effective preventative health and social crime-reduction investments available to local government. "
            "A landmark five-year study published by Sport England demonstrates that every &pound;1 invested in community sports infrastructure generates "
            "&pound;3.91 in combined social and economic value, including &pound;1.20 in direct healthcare savings through reduced obesity, diabetes, and adolescent depression.</p>"
            "<p>In the Borough of Redgrave, the reopening of the community sports pavilion and floodlit all-weather pitch produced immediate social dividends. "
            "Police records show that anti-social behaviour incidents among teenagers fell by 44% during evening peak hours, as over 350 local youths engaged in "
            "subsidised boxing, football, and gymnastics academies. Furthermore, the centre acts as a vital multi-generational community anchor: mornings host gentle exercise "
            "and mobility classes for elderly residents combating social isolation, whilst afternoons provide inclusive sensory play sessions for neurodivergent children.</p>"
            "<p>Physical activity instils discipline, teamwork, and emotional resilience that transform life outcomes. "
            "As local youth coach Marcus Adeleke testified: <i>'A sports hall gives a kid a safe space, a positive mentor, and a sense of belonging that keeps them away from street gangs.'</i> "
            "We must resist short-sighted austerity cuts and champion community sport as the heartbeat of civic renewal.</p>"
        ),
        "text_b": (
            "<h3>Text B: Local Taxpayers' Alliance &bull; Opinion Editorial</h3>"
            "<p><b>Fiscal Realism: Why Municipalities Cannot Afford Uncontrolled Leisure Subsidies</b><br>"
            "<i>By Victoria Hemming, Local Taxpayer Spokesperson &bull; 19 March 2025</i></p>"
            "<p>While everyone supports healthy recreation in principle, local taxpayers are entitled to demand financial accountability from cash-strapped local councils. "
            "Across our region, municipal authorities face crippling statutory budget shortfalls in adult social care, child protection, and special educational needs provision. "
            "In this dire fiscal climate, spending &pound;4.2 million of borrowed public funds on a municipal sports complex—which requires an ongoing &pound;380,000 annual operational subsidy—is "
            "an act of profound fiscal irresponsibility.</p>"
            "<p>The reality is that municipal leisure centres are notorious financial black holes. Council run facilities frequently suffer from bureaucratic mismanagement, "
            "perpetually broken swimming pool boilers, and neglected equipment, leading to dismal attendance rates. "
            "Meanwhile, private budget gyms and non-profit community clubs deliver modern, high-quality fitness facilities at zero cost to the ratepayer, "
            "charging as little as &pound;15 per month without dipping into public coffers.</p>"
            "<p>If sports facilities are genuinely valued by local residents, they should be managed by independent sports trusts or commercial operators under self-sustaining models. "
            "Council taxes have increased by 28% over the past four years; struggling families cannot afford to foot the bill for council vanity projects while potholes go unrepaired "
            "and elderly care services are slashed. Let us prioritise mandatory statutory duties before subsidising discretionary leisure ventures.</p>"
        ),
        "reading_q1_5": [
            {"q": "Q1. In Text A, what return on investment is achieved for every &pound;1 invested in community sports infrastructure?", "marks": 2, "lines": 28},
            {"q": "Q2. Identify two distinct community groups that benefit from the Redgrave sports pavilion in Text A.", "marks": 2, "lines": 28},
            {"q": "Q3. From Text B, identify two statutory services that the author argues are being compromised by leisure spending.", "marks": 2, "lines": 28},
            {"q": "Q4. Identify one fact and two subjective opinions expressed in Text B regarding council-run sports facilities.", "marks": 3, "lines": 34},
            {"q": "Q5. Explain what the author of Text B means by the term <i>'vanity projects'</i>.", "marks": 2, "lines": 28}
        ],
        "reading_q6_9": [
            {"q": "Q6. Compare how Text A and Text B use language, statistics, and contrasting tones to debate whether municipal funds should be spent on sports centres.", "marks": 6, "lines": 58},
            {"q": "Q7. Analyse the persuasive language devices used by Councillor Morris in Text A to present leisure spending as a necessity rather than an indulgence.", "marks": 3, "lines": 32},
            {"q": "Q8. Identify one common goal regarding community well-being that both authors acknowledge, despite their opposing financial arguments.", "marks": 2, "lines": 26},
            {"q": "Q9. Synthesise the alternative delivery models proposed across both texts for funding and operating community recreational facilities.", "marks": 4, "lines": 42}
        ],
        "writing_t1": {
            "type": "Formal Proposal Letter to National Lottery Community Fund",
            "scenario": "Your local community sports pavilion is in severe disrepair and faces closure unless funds are raised for modernisation.",
            "task": "Write a formal grant funding proposal letter to the National Lottery Community Fund. In your letter, you must:<br>"
                    "&bull; Detail the current dilapidated condition of the sports pavilion and the community impact if it closes.<br>"
                    "&bull; Present compelling evidence of how a refurbished hub will improve public health, youth engagement, and social inclusion.<br>"
                    "&bull; Set out a clear, costed plan showing how the grant funding will be spent and how the facility will achieve long-term financial sustainability.<br>"
                    "Use formal business letter structure (addresses, date, subject line, salutation), authoritative evidence, and a compelling persuasive register.",
            "marks": 19
        },
        "writing_t2": {
            "type": "Inspiring Local Newspaper Article / Volunteer Appeal",
            "scenario": "A community sports club is seeking adult volunteers, coaches, and local business sponsors to launch a weekend youth sports academy.",
            "task": "Write an inspiring and engaging article for the local gazette. In your article, you must:<br>"
                    "&bull; Celebrate the positive impact that volunteer-run sport has had on local youngsters.<br>"
                    "&bull; Outline the specific volunteer roles available (e.g. coaching, refereeing, event catering, equipment maintenance) and business sponsorship packages.<br>"
                    "&bull; Issue an impassioned call to action inviting readers to attend an upcoming launch meeting.<br>"
                    "Include a captivating headline, motivational subheadings, bullet points, and an enthusiastic, community-spirited tone.",
            "marks": 15
        }
    }
]

print("ENGLISH_L2_MOCKS defined successfully: 5 complete mocks with authentic texts and questions!")
'''

with open('books/a4/specialist_suite_content.py', 'a') as f:
    f.write(english_code)

print("Appended ENGLISH_L2_MOCKS to specialist_suite_content.py!")
