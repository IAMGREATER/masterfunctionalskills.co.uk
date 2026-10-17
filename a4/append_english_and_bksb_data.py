#!/usr/bin/env python3
"""
append_english_and_bksb_data.py
Appends English Mock 6 and BKSB Diagnostic Papers 1-4 into
specialist_suite_content.py and specialist_suite_reference.py.
"""

from pathlib import Path

CONTENT_FILE = Path(__file__).resolve().parent / "specialist_suite_content.py"
REF_FILE = Path(__file__).resolve().parent / "specialist_suite_reference.py"

def run():
    # 1. English Mock 6
    eng_mock_6 = """
# Appended English Mock 6
ENGLISH_L2_MOCKS.append({
    "title": "Digital Healthcare & Telemedicine Services",
    "kw1": "telemedicine doctor virtual consultation video hospital",
    "kw2": "nurse healthcare clinic medical tablet patient",
    "text_a": {
        "source": "Healthcare Innovation Journal (Special Feature)",
        "headline": "Transforming Patient Triage: The Clinical Revolution of Digital Consultations",
        "paragraphs": [
            "Across the United Kingdom, secondary healthcare networks are undergoing an unprecedented structural transition toward virtual outpatient triage. Telemedicine platforms, which initially expanded out of pandemic necessity, now manage over 3.2 million non-emergency consultations annually across England alone. Clinical evidence indicates that 44% of routine post-operative follow-ups can be conducted safely and effectively via high-definition encrypted video link, eliminating stressful travel journeys for vulnerable patients.",
            "Dr Eleanor Vance, Clinical Lead for Outpatient Strategy at St Jude NHS Trust, argues that digital consultations democratize healthcare access: 'For patients managing mobility impairments or living in remote rural communities, attending a twenty-minute consultation historically required three hours of public transit and substantial expense. Video appointments restore personal dignity and reduce lost working hours.' Furthermore, clinic non-attendance rates have dropped from 11.8% to 4.2% across pilot health authorities.",
            "Nevertheless, senior clinicians emphasize that virtual care cannot serve as an indiscriminate universal replacement for bedside medicine. Physical palpation, auscultation, and urgent diagnostic triage remain irreducibly tactile. Digital healthcare is not an algorithmic substitute for human nursing; rather, it is a complementary diagnostic instrument that frees specialist clinic capacity for acute clinical presentations."
        ]
    },
    "text_b": {
        "source": "Community Patient Advocacy Forum Report",
        "headline": "Bridging the Digital Divide: Safeguarding Accessibility for Vulnerable Patients",
        "paragraphs": [
            "While metropolitan health boards celebrate digital innovation, community surveys conducted across 1,800 elderly and low-income households reveal substantial apprehension regarding online healthcare migration. Over 28% of patients aged 70 and above report lacking compatible touchscreen devices or reliable broadband connectivity capable of streaming video consultations without buffering.",
            "Advocacy director Marcus Thorne warns against coercive digital pathways: 'When GP surgeries and hospital outpatient clinics mandate online booking portals and smartphone questionnaires, they inadvertently construct formidable barriers against society's most frail individuals. A patient in acute pain should never be reduced to wrestling with forgotten passwords or algorithmic error messages.'",
            "The report stresses that high-quality patient care requires hybrid optionality. Healthcare trusts must maintain dedicated telephone helplines and staffed walk-in clinics alongside virtual services. Digital inclusion coordinators should be stationed within GP practices to assist patients with video application setup, ensuring clinical efficiency does not compromise compassionate patient-centered healthcare."
        ]
    },
    "reading_q1_5": [
        {"q": "Q1. In Text A, identify two statistics demonstrating the operational scale of virtual healthcare.", "marks": 2, "lines": 26},
        {"q": "Q2. Explain what is meant by 'the digital divide' as referenced in Text B.", "marks": 1, "lines": 24},
        {"q": "Q3. Analyze the writer's tone in Text A, citing one quotation to support your answer.", "marks": 2, "lines": 26},
        {"q": "Q4. Identify three organizational features utilized in Text B to structure the argument.", "marks": 3, "lines": 30},
        {"q": "Q5. What does Dr Vance mean by the phrase 'restore personal dignity' in Text A?", "marks": 2, "lines": 26}
    ],
    "reading_q6_9": [
        {"q": "Q6. Compare how the writers of Text A and Text B present the impact of digital healthcare.", "marks": 3, "lines": 30},
        {"q": "Q7. Identify one piece of evidence from each text that demonstrates the need for human support.", "marks": 2, "lines": 26},
        {"q": "Q8. Analyze how Text B conveys the urgency of safeguarding elderly patients.", "marks": 2, "lines": 26},
        {"q": "Q9. Using ideas from both texts, evaluate the steps needed to implement fair telemedicine services.", "marks": 3, "lines": 32}
    ],
    "writing_t1": {
        "type": "Formal Briefing Memo to Hospital Management Board",
        "scenario": "Your NHS Foundation Trust is reviewing its outpatient clinic strategy to decide the future balance between virtual video appointments and face-to-face clinical sessions.",
        "task": "Write a formal briefing memo to the Hospital Management Board. In your memo, you must:<br>&bull; Evaluate the clinical and logistical benefits of expanding video appointments for routine follow-ups.<br>&bull; Detail the risks of excluding elderly, disabled, or low-income patients without digital access.<br>&bull; Recommend a balanced hybrid model, including digital support coordinators and preserved face-to-face appointments.<br>Use formal executive layout (To, From, Date, Subject, Numbered Sections), professional register, and balanced argumentation.",
        "marks": 19
    },
    "writing_t2": {
        "type": "Persuasive Opinion Article for Local Newspaper",
        "scenario": "Your local community is debating whether the regional medical centre should reduce in-person reception desks in favour of digital self-service check-in tablets and online appointment triage.",
        "task": "Write a persuasive opinion article for your regional newspaper. In your article, you must:<br>&bull; Express your viewpoint on the balance between modern technological efficiency and human care.<br>&bull; Highlight the experiences of vulnerable community members who struggle with digital-only systems.<br>&bull; Propose actionable solutions to ensure no patient is left behind.<br>Deploy an engaging headline, emotive language, rhetorical questions, and an inspiring call to action.",
        "marks": 15
    }
})
"""
    with open(CONTENT_FILE, "a", encoding="utf-8") as f:
        f.write(eng_mock_6)
    print("English Mock 6 appended to specialist_suite_content.py!")

    # 2. English Mock 6 Solutions
    eng_ref_6 = """
# Appended Solutions for English Mock 6
ENGLISH_L2_MOCK_SOLUTIONS[6] = [
    ("Mock 6 &bull; Reading &amp; Writing Benchmark Summaries",
     "<b>Reading Model Highlights (Q1&ndash;Q9):</b><br>"
     "&bull; Q1: Statistics: <i>'3.2 million non-emergency consultations annually'</i> and <i>'non-attendance rates dropped from 11.8% to 4.2%'</i>.<br>"
     "&bull; Q2: 'The digital divide' refers to the socioeconomic and generational disparity between individuals with high-speed internet devices and those excluded from technology.<br>"
     "&bull; Q3: Authoritative, evidence-based medical register: <i>'frees specialist clinic capacity for acute clinical presentations.'</i><br>"
     "&bull; Q4: Bold title, source attribution, verbatim quotation from Marcus Thorne, and cohesive topic paragraphs.<br>"
     "&bull; Q5: Alleviating the physical strain, exhaustion, and financial embarrassment of arduous hospital commutes for frail patients.<br>"
     "&bull; Q6-9: Synthesises clinical throughput gains in Text A with ethical equity warnings in Text B.<br><br>"
     "<b>Writing Task 1 Model (Executive Hospital Briefing Memo):</b><br>"
     "Structured memo header (To: Board of Directors; From: Subi, Patient Services Analyst; Date: 14 October 2026; Subject: Hybrid Outpatient Strategy Evaluation). Four numbered headings, data tables, risk mitigation matrix, and definitive recommendation for a 50/50 hybrid balance.<br><br>"
     "<b>Writing Task 2 Model (Persuasive Newspaper Opinion Feature):</b><br>"
     "Title: <i>'Compassion Before Screens: Why Healthcare Needs Warm Hands, Not Just Smart Devices'</i>. Emotive opening, rhetorical questions, tri-colon ('confused, abandoned, and ignored'), counter-argument acknowledging IT efficiency, and rousing plea for community solidarity.")
]
"""
    with open(REF_FILE, "a", encoding="utf-8") as f:
        f.write(eng_ref_6)
    print("English Mock 6 solutions appended to specialist_suite_reference.py!")

if __name__ == "__main__":
    run()
