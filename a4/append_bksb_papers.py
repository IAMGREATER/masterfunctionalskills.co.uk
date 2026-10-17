#!/usr/bin/env python3
"""
append_bksb_papers.py
Adds 4 full diagnostic exam papers (16 pages) to specialist_suite_content.py
and their full worked solutions to specialist_suite_reference.py.
"""

from pathlib import Path

CONTENT_FILE = Path(__file__).resolve().parent / "specialist_suite_content.py"
REF_FILE = Path(__file__).resolve().parent / "specialist_suite_reference.py"

def run():
    bksb_papers = """
# Appended BKSB Diagnostic Examination Papers
BKSB_PAPERS = [
    {
        "num": 1,
        "title": "Diagnostic Paper 1: Mathematics Non-Calculator Sectional Mock",
        "badge": "DP1",
        "kw1": "maths exam test paper calculation pencil desk",
        "kw2": "adult student working numbers exam quiet room",
        "pages": [
            {
                "subtitle": "Section A &bull; Number, Decimals &amp; Invoicing",
                "intro": "Duration: 25 minutes | Total Marks: 16 Marks | Calculators STRICTLY FORBIDDEN.<br>Show all intermediate columnar steps. Process marks are awarded for valid mathematical strategies.",
                "questions": [
                    {"q": "<b>Question 1:</b> Commercial Invoicing: A warehouse distribution hub orders 18 packing tape dispensers at &pound;14.80 each and 5 heavy-duty strapping tools at &pound;46.50 each. A business customer trade discount of 10% is deducted from the combined order total. Calculate the final amount payable.", "marks": 4, "weight": 1.1},
                    {"q": "<b>Question 2:</b> Circle Geometry: A circular grain silo has a concrete base with a radius of 2.5 metres. Using &pi; = 3.14, calculate the area of the concrete base. State the correct units in your answer.", "marks": 4, "weight": 1.1}
                ]
            },
            {
                "subtitle": "Section A &bull; Fractions &amp; Reverse Percentage",
                "intro": "Candidate Working Grid &bull; Show full fraction and reverse calculation steps clearly.",
                "questions": [
                    {"q": "<b>Question 3:</b> Mixed Number Fractions: Work out: 2 <sup>1</sup>/<sub>3</sub> + 1 <sup>3</sup>/<sub>5</sub>. Give your final answer as a mixed number in its simplest form.", "marks": 4, "weight": 1.1},
                    {"q": "<b>Question 4:</b> Reverse Percentage: A commercial equipment lease fee is reduced by 20% during an autumn promotional campaign. The discounted monthly fee is &pound;280.00. Calculate the original lease fee before the discount. Show an inverse check of your answer.", "marks": 4, "weight": 1.1}
                ]
            },
            {
                "subtitle": "Section A &bull; Ratio &amp; Financial Sharing",
                "intro": "Candidate Working Grid &bull; Multi-part ratio allocation and metric conversion.",
                "questions": [
                    {"q": "<b>Question 5:</b> Ratio Sharing in Construction: A concrete foundation requires cement, sharp sand, and gravel mixed in the ratio 1 : 2 : 4. A contractor needs 2,100 kg of dry mix in total. Calculate the mass of gravel required in kilograms.", "marks": 4, "weight": 1.1},
                    {"q": "<b>Question 6:</b> Unit Conversions &amp; Scale: A technical architectural drawing uses a scale of 1 : 50. On the plan, a partition wall measures 8.4 cm. Calculate the actual real-world length of the wall in metres.", "marks": 4, "weight": 1.1}
                ]
            },
            {
                "subtitle": "Section A &bull; Synthesis &amp; Sign-Off",
                "intro": "Section A Verification Protocol &bull; Confirm all units and inverse checks before handing in.",
                "questions": [
                    {"q": "<b>Question 7:</b> Long Division &amp; Remainder: A packaging depot has 1,485 diagnostic sample kits to pack into master shipping cartons holding 36 kits each. Calculate the total number of master cartons needed to pack all the sample kits.", "marks": 4, "weight": 1.1}
                ]
            }
        ]
    },
    {
        "num": 2,
        "title": "Diagnostic Paper 2: Mathematics Calculator Sectional Mock",
        "badge": "DP2",
        "kw1": "calculator business student finance accounting desk",
        "kw2": "logistics warehouse transport forklift planning",
        "pages": [
            {
                "subtitle": "Section B &bull; Payroll &amp; Commercial Area",
                "intro": "Duration: 1 hour 15 minutes | Total Marks: 40 Marks | Calculators Permitted.<br>State standard formulas and intermediate substitution steps clearly to secure process marks.",
                "questions": [
                    {"q": "<b>Question 1:</b> Logistics Staffing Payroll: A distribution centre employs 14 warehouse order pickers working 37.5 hours each at &pound;11.44 per hour, and 3 dispatch team supervisors working 40.0 hours each at &pound;16.80 per hour. Calculate the total gross wage expenditure.", "marks": 5, "weight": 1.2},
                    {"q": "<b>Question 2:</b> Warehouse Tarmac Resurfacing: A rectangular delivery yard measures 28.0 m by 15.5 m. A storm drainage basin measuring 4.0 m by 3.0 m is excluded. Each bag of cold-lay tarmac repair compound covers 1.5 m&sup2; and costs &pound;18.20. Calculate the total cost of tarmac compound needed.", "marks": 5, "weight": 1.2}
                ]
            },
            {
                "subtitle": "Section B &bull; Estimated Mean &amp; Fuel Economy",
                "intro": "Candidate Working Grid &bull; Grouped frequency tables and multi-step rate calculations.",
                "questions": [
                    {"q": "<b>Question 3:</b> Grouped Mean Delivery Time: A courier firm monitors delivery times for 50 consignments: [10-14 min: 8], [15-19 min: 18], [20-24 min: 16], [25-29 min: 8]. Calculate the estimated mean delivery duration in minutes.", "marks": 5, "weight": 1.2},
                    {"q": "<b>Question 4:</b> Fleet Transit Van Economy: A commercial delivery van covers 276 miles at an average fuel economy of 46 mpg. Diesel costs &pound;1.52 per litre. (1 gallon &asymp; 4.55 litres). Calculate the fuel cost for the delivery route.", "marks": 5, "weight": 1.2}
                ]
            },
            {
                "subtitle": "Section B &bull; 3D Volume &amp; Financial Margins",
                "intro": "Candidate Working Grid &bull; Cylinders and commercial percentage profit margins.",
                "questions": [
                    {"q": "<b>Question 5:</b> Cylindrical Fuel Storage Tank: A cylindrical bulk diesel storage tank has a radius of 1.2 metres and a height of 3.0 metres. Using &pi; = 3.142, calculate the capacity of the tank in litres (1 m&sup3; = 1,000 litres).", "marks": 5, "weight": 1.2},
                    {"q": "<b>Question 6:</b> Retail Trading Margin: In September, an online distribution store generated &pound;36,400 in sales revenue. Total operating costs were &pound;24,800. Calculate the operating profit as a percentage of total revenue, rounded to 1 decimal place.", "marks": 5, "weight": 1.2}
                ]
            },
            {
                "subtitle": "Section B &bull; Speed, Arrival &amp; Pythagoras Synthesis",
                "intro": "Candidate Working Grid &bull; Decimal time conversion and right-angled triangle theorem.",
                "questions": [
                    {"q": "<b>Question 7:</b> Road Haulage Arrival Time: A long-distance haulage truck leaves the regional depot at 11:35 to complete a 154-mile delivery run at an average speed of 44 mph. Calculate the expected arrival time at the destination depot.", "marks": 5, "weight": 1.2},
                    {"q": "<b>Question 8:</b> Loading Ramp Hypotenuse: A heavy equipment loading ramp rises vertically by 1.5 metres over a horizontal distance of 5.5 metres. Use Pythagoras theorem to calculate the sloping length of the ramp.", "marks": 5, "weight": 1.2}
                ]
            }
        ]
    },
    {
        "num": 3,
        "title": "Diagnostic Paper 3: English Reading Sectional Mock",
        "badge": "DP3",
        "kw1": "student reading library books text analysis magnifying glass",
        "kw2": "collaborative team discussion documents office meeting",
        "pages": [
            {
                "subtitle": "Reading Source Text A &bull; Workplace Apprenticeships",
                "intro": "Read Text A carefully before answering Questions 1 to 4 on page 2.",
                "questions": [
                    {"q": "<b>Text A Headline:</b> Building Tomorrow's Workforce: Why Higher Apprenticeships Outshine Degrees<br><b>Source:</b> National Vocational Education Review<br><br>Over the past five years, the landscape of post-18 education has experienced a fundamental transformation. With undergraduate university tuition fees exceeding &pound;9,250 annually and average graduate student debt climbing past &pound;45,000, school leavers are increasingly turning toward Level 4 and Level 5 degree apprenticeships.<br><br>Under the apprenticeship model, learners earn a guaranteed salary while gaining direct hands-on workplace experience with leading corporate employers. All tuition and examination fees are funded entirely through the government apprenticeship levy. Statistics show that 91% of apprentices remain in full-time employment upon completing their qualification, compared to 76% of traditional university graduates.<br><br>Furthermore, employers report that apprentice-trained staff demonstrate superior workplace resilience, immediate technical capability, and long-term organizational loyalty.", "marks": 0, "weight": 1.0}
                ]
            },
            {
                "subtitle": "Reading Source Text B &bull; Small Business Perspectives",
                "intro": "Read Text B carefully before answering the comparative questions.",
                "questions": [
                    {"q": "<b>Text B Headline:</b> The True Cost of Mentoring: Small Business Realities in Technical Training<br><b>Source:</b> Federation of Independent Employers Journal<br><br>While government ministers champion apprenticeships as the universal panacea for national productivity, small and medium enterprises (SMEs) face distinct operational burdens. For an enterprise employing fewer than twenty staff, assigning a senior engineer to mentor an apprentice for twenty percent off-the-job training creates genuine resourcing strains.<br><br>Marcus Bennett, Managing Director of Precision Tooling Ltd, observes: 'We fully endorse vocational training, but losing our most experienced master craftsman for one full day every week slows our production line. Training is an investment, but the administrative compliance and assessment burdens placed on small employers can be overwhelming.'<br><br>To ensure apprenticeship accessibility across all sectors, employer bodies are urging funding reforms, including targeted mentoring subsidies and simplified digital portfolio administration.", "marks": 0, "weight": 1.0}
                ]
            },
            {
                "subtitle": "Reading Comprehension Questions 1 to 4",
                "intro": "Answer Questions 1 to 4 using information from Text A and Text B.",
                "questions": [
                    {"q": "<b>Question 1:</b> In Text A, identify two numerical statistics demonstrating the financial advantage of apprenticeships over degrees.", "marks": 2, "weight": 1.0},
                    {"q": "<b>Question 2:</b> Identify one fact and one opinion expressed in Text B regarding the small business training experience.", "marks": 2, "weight": 1.0},
                    {"q": "<b>Question 3:</b> Analyze the writer's tone in Text A, citing one brief quotation to support your answer.", "marks": 2, "weight": 1.0},
                    {"q": "<b>Question 4:</b> What does the phrase 'universal panacea' mean as used in paragraph 1 of Text B?", "marks": 1, "weight": 1.0}
                ]
            },
            {
                "subtitle": "Comparative Synthesis Questions 5 to 7",
                "intro": "Synthesize and compare ideas across both source texts.",
                "questions": [
                    {"q": "<b>Question 5:</b> Compare how the writers of Text A and Text B present the impact of apprenticeship programmes on employers.", "marks": 3, "weight": 1.0},
                    {"q": "<b>Question 6:</b> Identify three organizational features used in Text A or Text B to guide the reader through the text.", "marks": 3, "weight": 1.0},
                    {"q": "<b>Question 7:</b> Using information from both texts, evaluate the steps government and industry could take to make vocational training successful for both learners and small firms.", "marks": 3, "weight": 1.0}
                ]
            }
        ]
    },
    {
        "num": 4,
        "title": "Diagnostic Paper 4: English Writing Sectional Mock",
        "badge": "DP4",
        "kw1": "fountain pen writing signature business contract notes",
        "kw2": "modern office conference presentation speech podium",
        "pages": [
            {
                "subtitle": "Writing Task 1 &bull; Formal Recommendation Report",
                "intro": "Duration: 1 hour | Total Marks: 30 Marks | High marks depend on format, vocabulary, and SPaG.<br>Format: Formal Report &emsp;|&emsp; Suggested Length: 250–300 words &emsp;|&emsp; Target: 15 Marks",
                "questions": [
                    {"q": "<b>Task 1 Context:</b> You work as an apprentice coordinator for a regional manufacturing company. Management wants to establish a new mentoring programme to support entry-level technical trainees.<br><b>Task:</b> Write a formal report to the Operations Director. In your report, you must:<br>&bull; Detail the operational benefits of introducing structured mentor training.<br>&bull; Address potential productivity risks when senior staff mentor apprentices during peak hours.<br>&bull; Recommend a practical schedule, such as dedicated weekly coaching slots and rotational shadow shifts.<br>Use formal report layout (To, From, Date, Subject, numbered headings), objective register, and bulleted recommendations.", "marks": 15, "weight": 1.2}
                ]
            },
            {
                "subtitle": "Writing Task 1 &bull; Candidate Response Lines",
                "intro": "Candidate Lined Writing Booklet &bull; Task 1 (Formal Report Continued)",
                "questions": [
                    {"q": "Continue and conclude your formal report below. Ensure accurate punctuation, appropriate paragraph transitions, and zero comma splices.", "marks": 0, "weight": 1.0}
                ]
            },
            {
                "subtitle": "Writing Task 2 &bull; Persuasive Speech to School Leavers",
                "intro": "Format: Spoken Speech &emsp;|&emsp; Suggested Length: 200–250 words &emsp;|&emsp; Target: 15 Marks",
                "questions": [
                    {"q": "<b>Task 2 Context:</b> You have been invited to your former secondary school's annual careers evening to speak to Year 11 and Year 12 students about vocational training paths.<br><b>Task:</b> Write the speech you will deliver to the students and their parents. In your speech, you must:<br>&bull; Capture the audience's attention with an inspiring opening about career choices.<br>&bull; Contrast the debt burden of university with the earned income and career progression of apprenticeships.<br>&bull; Deploy persuasive rhetorical devices (AFOREST: facts, tri-colon, rhetorical questions) to motivate students.<br>&bull; Conclude with a memorable call to action urging them to explore technical qualifications.", "marks": 15, "weight": 1.2}
                ]
            },
            {
                "subtitle": "Writing Task 2 &bull; Candidate Response Lines &amp; Sign-Off",
                "intro": "Candidate Lined Writing Booklet &bull; Task 2 (Speech Continued)",
                "questions": [
                    {"q": "Conclude your speech and review your response against the SPaG criteria checklist before submitting your paper.", "marks": 0, "weight": 1.0}
                ]
            }
        ]
    }
]
"""

    with open(CONTENT_FILE, "a", encoding="utf-8") as f:
        f.write(bksb_papers)
    print("BKSB Diagnostic Papers 1-4 appended to specialist_suite_content.py!")

    # 2. Append Solutions for BKSB Diagnostic Papers to specialist_suite_reference.py
    bksb_ref_papers = """
# Appended Solutions for BKSB Diagnostic Papers 1 to 4
BKSB_PAPERS_SOLUTIONS = {
    1: [
        ("Diagnostic Paper 1 Model Solutions (Maths Non-Calculator)",
         "<b>Q1. Warehouse Invoice:</b> (18 &times; &pound;14.80) + (5 &times; &pound;46.50) = &pound;266.40 + &pound;232.50 = &pound;498.90. Discount 10% = &pound;49.89. Total payable = &pound;498.90 - &pound;49.89 = <b>&pound;449.01</b>.<br>"
         "<b>Q2. Grain Silo Base Area:</b> Radius r = 2.5 m. Area = 3.14 &times; (2.5)&sup2; = 3.14 &times; 6.25 = <b>19.63 m&sup2;</b> (or 19.625 m&sup2;).<br>"
         "<b>Q3. Mixed Fractions:</b> 2 1/3 + 1 3/5 = 7/3 + 8/5 = (35 + 24)/15 = 59/15 = <b>3 14/15</b>.<br>"
         "<b>Q4. Reverse Discount:</b> &pound;280.00 &divide; 0.80 = <b>&pound;350.00</b>. Check: 350 &times; 0.80 = &pound;280.00.<br>"
         "<b>Q5. Concrete Ratio:</b> Ratio 1:2:4, total 7 parts of 2,100 kg. 1 part = 300 kg. Gravel = 4 &times; 300 = <b>1,200 kg</b>.<br>"
         "<b>Q6. Scale Conversion:</b> 8.4 cm &times; 50 = 420 cm = <b>4.2 metres</b>.<br>"
         "<b>Q7. Carton Division:</b> 1,485 &divide; 36 = 41.25 &rarr; <b>42 master cartons</b> required to hold all kits.")
    ],
    2: [
        ("Diagnostic Paper 2 Model Solutions (Maths Calculator)",
         "<b>Q1. Logistics Payroll:</b> (14 &times; 37.5 &times; &pound;11.44) + (3 &times; 40 &times; &pound;16.80) = &pound;6,006.00 + &pound;2,016.00 = <b>&pound;8,022.00</b>.<br>"
         "<b>Q2. Tarmac Resurfacing:</b> Net area = (28.0 &times; 15.5) - (4.0 &times; 3.0) = 434 - 12 = 422 m&sup2;. Bags = 422 &divide; 1.5 = 281.33 &rarr; 282 bags. Cost = 282 &times; &pound;18.20 = <b>&pound;5,132.40</b>.<br>"
         "<b>Q3. Estimated Mean Delivery Time:</b> Midpoints: 12 (8 &times; 12 = 96), 17 (18 &times; 17 = 306), 22 (16 &times; 22 = 352), 27 (8 &times; 27 = 216). Total &Sigma;fx = 970. N = 50. Mean = 970 &divide; 50 = <b>19.4 minutes</b>.<br>"
         "<b>Q4. Van Route Fuel:</b> 276 &divide; 46 = 6.0 gal &times; 4.55 = 27.3 L &times; &pound;1.52 = <b>&pound;41.50</b>.<br>"
         "<b>Q5. Cylindrical Tank Capacity:</b> 3.142 &times; 1.2&sup2; &times; 3.0 = 13.573 m&sup3; = <b>13,573 litres</b>.<br>"
         "<b>Q6. Operating Profit Margin:</b> Profit = &pound;36,400 - &pound;24,800 = &pound;11,600. Margin % = (&pound;11,600 &divide; &pound;36,400) &times; 100 = <b>31.9%</b>.<br>"
         "<b>Q7. Arrival Time:</b> 154 &divide; 44 = 3.5 hours = 3 hrs 30 mins. Departure = 11:35. Arrival = 11:35 + 3h 30m = <b>15:05</b>.<br>"
         "<b>Q8. Ramp Hypotenuse:</b> &radic;(1.5&sup2; + 5.5&sup2;) = &radic;(2.25 + 30.25) = &radic;32.5 = <b>5.70 metres</b>.")
    ],
    3: [
        ("Diagnostic Paper 3 Model Solutions (English Reading)",
         "<b>Q1. Statistics from Text A:</b> &pound;45,000 average graduate debt and 91% employment completion rate for apprentices.<br>"
         "<b>Q2. Fact and Opinion in Text B:</b> Fact: Apprentices spend twenty percent of working hours in off-the-job training. Opinion: Training burdens on small employers are overwhelming.<br>"
         "<b>Q3. Tone in Text A:</b> Encouraging and authoritative, using data-driven arguments: <i>'superior workplace resilience, immediate technical capability.'</i><br>"
         "<b>Q4. Definition:</b> 'Universal panacea' means a cure-all or miraculous solution that solves every single problem.<br>"
         "<b>Q5. Comparative Impact on Employers:</b> Text A portrays apprentices as loyalty-building and productive assets. Text B presents small employers struggling with production loss and mentor diversion.<br>"
         "<b>Q6. Organizational Features:</b> Bold headline, subheadings, cited authority quotation (Marcus Bennett), and comparative paragraphs.<br>"
         "<b>Q7. Synthesis:</b> Funding mentorship subsidies directly to SMEs while retaining the levy support will safeguard both apprentice welfare and small business profitability.")
    ],
    4: [
        ("Diagnostic Paper 4 Model Solutions (English Writing)",
         "<b>Task 1 Model (Formal Recommendation Report):</b><br>"
         "Layout: To: Operations Director; From: Subi, Apprentice Coordinator; Date: 14 October 2026; Subject: Technical Trainee Mentorship Proposal.<br>"
         "Sections: 1. Purpose &amp; Executive Summary, 2. Productivity Benefits, 3. Workload Mitigation, 4. Strategic Recommendations.<br>"
         "Content highlights: Establishes a 2-hour protected Friday morning mentor slot, pairs trainees with senior mentors, and schedules quarterly progress reviews.<br><br>"
         "<b>Task 2 Model (Persuasive Careers Evening Speech):</b><br>"
         "Opening: 'Good evening students, parents, and teachers.' Captures attention by contrasting &pound;45,000 university debt against earning &pound;22,000 while training.<br>"
         "Rhetorical devices: Tri-colon ('skills for today, qualifications for tomorrow, and careers for life'), rhetorical question ('Why spend three years accumulating debt when you could be accumulating experience?').<br>"
         "Call to action: Directs students to speak with vocational advisors at the exhibition stands.")
    ]
}
"""
    with open(REF_FILE, "a", encoding="utf-8") as f:
        f.write(bksb_ref_papers)
    print("BKSB Diagnostic Papers solutions appended to specialist_suite_reference.py!")

if __name__ == "__main__":
    run()
