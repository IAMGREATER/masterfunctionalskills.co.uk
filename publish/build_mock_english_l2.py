#!/usr/bin/env python3
"""
build_mock_english_l2.py
Compiles the complete 84-page publication:
MasterFunctionalSkills_Mock_Pack_English_L2.pdf

Contains 8 Complete Official-Style Exam Papers:
- Reading Component (Authentic Texts Inserts & Comprehension Questions, 35 Marks each)
- Writing Component (Task 1 Extended Writing 27 Marks & Task 2 Workplace Task 15 Marks)
- Full Ruled Candidate Response Booklets
- Comprehensive Examiner Mark Schemes & High-Scoring Band 4 Model Writing Answers.

Mapped strictly to Ofqual Functional Skills English Level 2 Subject Content.
Full CGP-style visual pedagogy, dyslexia-friendly warm cream styling (#FDFBF7).
"""

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from book_framework import (
    SHARED_CSS, render_book_to_pdf, BOOKS_IMG_DIR
)

def build_mock_english_l2_book():
    front_img = os.path.join(BOOKS_IMG_DIR, "mock_pack_english_l2_cover_page-1.png")
    back_img = os.path.join(BOOKS_IMG_DIR, "mock_pack_english_l2_cover_page-2.png")
    
    pages = []
    
    # -------------------------------------------------------------
    # PAGE 1: FRONT COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{front_img}" class="cover-full-img">
</div>
""")

    # -------------------------------------------------------------
    # PAGE 2: INSIDE COVER & BLUEPRINT
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Level 2</div>
    <div class="page-header-strand">Exam Specification &amp; Assessment Architecture</div>
  </div>

  <h2>Level 2 Functional English Examination Blueprint</h2>
  <p>The Level 2 Functional Skills English qualification certifies practical workplace literacy and is recognized by employers, apprenticeship standards, and universities as equivalent to GCSE English Grade 4/C. Regulated by Ofqual, it tests the ability to interpret complex informational texts and communicate persuasively in writing.</p>

  <div class="card-concept" style="border-left-color:#003366; background:#f0f9ff;">
    <h3 style="color:#003366; margin-top:0;">Official Examination Structure</h3>
    <table class="data-table" style="font-size:8pt;">
      <tr><th>Component</th><th>Duration</th><th>Marks Available</th><th>Key Assessment Objectives</th></tr>
      <tr>
        <td><strong>Component 1: Reading</strong></td>
        <td>1 Hour (60 mins)</td>
        <td>35 Marks (approx. 45%)</td>
        <td>Fact extraction, tone, bias, language devices, organizational features, comparing 2 texts.</td>
      </tr>
      <tr>
        <td><strong>Component 2: Writing</strong></td>
        <td>1 Hour 20 Mins (80 mins)</td>
        <td>42 Marks (approx. 55%)</td>
        <td>Task 1: Extended formal writing (27m). Task 2: Functional workplace communication (15m).</td>
      </tr>
      <tr style="background:#e0f2fe; font-weight:bold;">
        <td>COMBINED EXAM</td>
        <td>2 Hours 20 Mins</td>
        <td>77 Marks Total</td>
        <td>Pass Mark Threshold: ~65% to 70% (approx. 50/77 marks)</td>
      </tr>
    </table>
  </div>

  <div class="grid-2" style="margin-top:6px;">
    <div class="card-method">
      <h3 style="color:#16a34a; margin-top:0;">Writing Assessment Bands</h3>
      <p>Every writing task is marked across two independent criteria:</p>
      <p><strong>1. Content &amp; Organisation (60% of marks):</strong> Structural coherence, paragraphs, format conventions (headings, salutations), adapting tone to audience and purpose.</p>
      <p><strong>2. SPaG (40% of marks):</strong> Spelling of complex vocabulary, accurate punctuation (colons, semicolons, apostrophes), and grammatical sentence variety.</p>
    </div>
    <div class="card-tip">
      <h3 style="color:#d97706; margin-top:0;">Candidate Exam Record</h3>
      <table style="width:100%; border-collapse:collapse; font-size:7.5pt; margin-top:4px;">
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Candidate Name:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Centre / College:</strong></td><td style="border-bottom:1px solid #cbd5e1;"></td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 1 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 2 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 3 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 4 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 5 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 6 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 7 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
        <tr><td style="padding:2.5px; border-bottom:1px solid #cbd5e1;"><strong>Paper 8 Total:</strong></td><td style="border-bottom:1px solid #cbd5e1;">&nbsp;&nbsp;&nbsp;&nbsp; / 77</td></tr>
      </table>
    </div>
  </div>

  <div class="card-trap" style="margin-top:6px;">
    <strong>The Golden Rule for Level 2 Writing:</strong> Always plan your paragraphs before writing. Writing in continuous unbroken walls of text immediately caps your Content and Organisation mark at Band 1, regardless of how good your vocabulary is!
  </div>

  <div class="page-footer">
    <div>English Level 2 &bull; Official 8-Mock Exam Pack</div>
    <div class="page-num">Page 2</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 3: READING ASSESSMENT STRATEGIES & COMPARISON MASTERCLASS
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Level 2</div>
    <div class="page-header-strand">Reading Strategies &amp; Text Analysis</div>
  </div>

  <h2>Mastering the Level 2 Reading Assessment</h2>
  <p>Examiners evaluate reading comprehension across literal retrieval, inferential deduction, and comparative synthesis. Follow these strategic techniques:</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Key Reading Assessment Objectives</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Literal Retrieval:</strong> Quote or paraphrase directly from the specified text. Never assume facts not stated in the passage.</li>
        <li><strong>Inferential Deduction:</strong> Read between the lines. Identify the subtext, emotional connotations, and underlying motives of the writer.</li>
        <li><strong>Organisational Devices:</strong> Explain <em>how</em> layout aids meaning: bullet points break down complex procedures, bold headings anchor visual skimming, subheadings organise thematic shifts.</li>
        <li><strong>Comparing Texts (Q7):</strong> Synthesize ideas across both texts. Always use comparative connectives: <em>whereas, conversely, in contrast, similarly, likewise</em>.</li>
      </ul>
    </div>

    <div class="card-concept" style="border-left-color:#003366; padding:6px 10px;">
      <h3 style="color:#003366; margin-top:0;">Detecting Language Devices &amp; Bias</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Rhetorical Questions:</strong> Prompt reader reflection without expecting an answer; creates conversational rapport.</li>
        <li><strong>Rule of Three:</strong> Groups three rhythmic phrases for persuasive impact (e.g. <em>"broken connectors, conflicting apps, and staggering disparities"</em>).</li>
        <li><strong>Hyperbole:</strong> Deliberate exaggeration to dramatize urgency (e.g. <em>"suffocating under an avalanche"</em>).</li>
        <li><strong>Detecting Bias:</strong> One-sided emotive language, absence of counter-evidence, dismissive adjectives (<em>"glossy corporate rhetoric"</em>), and subjective value judgments presented as fact.</li>
      </ul>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px;">
    <h3 style="color:#d97706; margin-top:0;">The 10-Minute Reading Discipline</h3>
    <p style="font-size:8pt; margin:2px 0;">Never begin writing responses immediately. Use your highlighter to mark: (1) statistics and dates, (2) author viewpoints and tone shifts, (3) structural headings, and (4) opposing perspectives between Text A and Text B. This preparation ensures rapid, precise retrieval during the exam.</p>
  </div>

  <div class="page-footer">
    <div>English Level 2 &bull; Official 8-Mock Exam Pack &bull; Reading Masterclass</div>
    <div class="page-num">Page 3</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 4: WRITING ASSESSMENT MATRIX & FORMAT CONVENTIONS
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Level 2</div>
    <div class="page-header-strand">Writing Formats &amp; Assessment Matrix</div>
  </div>

  <h2>Writing Formats, Structural Architecture &amp; Tone</h2>
  <p>Level 2 Writing assesses your ability to adapt tone, format, and register to diverse workplace and civic scenarios.</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Structural Format Conventions</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Formal Report:</strong>
          <br>&bull; Header: <code>To: / From: / Date: / Subject:</code>
          <br>&bull; Formal subheadings: <em>1. Introduction, 2. Current Findings, 3. Analysis, 4. Recommendations</em>.
        </li>
        <li><strong>Formal Letter:</strong>
          <br>&bull; Sender address (top right), Recipient address (left).
          <br>&bull; Salutation: <em>Dear Mr Smith &rarr; Yours sincerely</em>; <em>Dear Sir/Madam &rarr; Yours faithfully</em>.
        </li>
        <li><strong>Professional Article:</strong>
          <br>&bull; Engaging headline, introductory hook, subheadings, concluding synthesis.
        </li>
        <li><strong>Workplace Email:</strong>
          <br>&bull; Accurate subject line, respectful salutation, bulleted action points, professional sign-off.
        </li>
      </ul>
    </div>

    <div class="card-concept" style="border-left-color:#003366; padding:6px 10px;">
      <h3 style="color:#003366; margin-top:0;">Band 4 Writing Descriptors (Examiner Rubric)</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Purpose &amp; Audience:</strong> Flawless formal or persuasive register maintained throughout. No casual slang or abbreviations.</li>
        <li><strong>Cohesion &amp; Structure:</strong> Ideas grouped into logical paragraphs. Sophisticated discourse markers (<em>Furthermore, Consequently, Notwithstanding</em>).</li>
        <li><strong>Vocabulary Range:</strong> Ambitious, context-appropriate vocabulary deployed accurately.</li>
        <li><strong>Sentence Architecture:</strong> Mix of compound, complex, and short emphatic sentences.</li>
      </ul>
    </div>
  </div>

  <div class="card-trap" style="margin-top:6px;">
    <strong>The Salutation / Sign-Off Trap:</strong> If you write <em>"Dear Sir/Madam"</em> and end with <em>"Yours sincerely"</em>, you lose format marks! Remember: Named recipient = <em>Sincerely</em>; Unnamed recipient = <em>Faithfully</em>.
  </div>

  <div class="page-footer">
    <div>English Level 2 &bull; Official 8-Mock Exam Pack &bull; Writing Matrix</div>
    <div class="page-num">Page 4</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 5: SPaG TOOLKIT, ADVANCED PUNCTUATION & PROOFREADING
    # -------------------------------------------------------------
    pages.append("""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Level 2</div>
    <div class="page-header-strand">SPaG &amp; Punctuation Toolkit</div>
  </div>

  <h2>Level 2 SPaG Toolkit: Punctuation &amp; Grammar Mastery</h2>
  <p>In Functional Skills Level 2, 40% of all writing marks are awarded strictly for Spelling, Punctuation, and Grammar (SPaG). To achieve Band 4, you must demonstrate sophisticated punctuation:</p>

  <div class="grid-2" style="font-size:7.8pt;">
    <div class="card-method" style="padding:6px 10px;">
      <h3 style="color:#16a34a; margin-top:0;">Advanced Punctuation Rules</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Semicolon (;):</strong> Links two closely related independent clauses without a conjunction:
          <br><em>"Electric vehicles reduce tailpipe emissions; however, charging infrastructure remains uneven."</em>
        </li>
        <li><strong>Colon (:):</strong> Introduces an explanation, quotation, or bulleted list:
          <br><em>"The survey revealed three urgent priorities: faster charging, clearer tariffs, and reliable hardware."</em>
        </li>
        <li><strong>Hyphen vs Dash:</strong>
          <br>&bull; Hyphen (-): Compounded words (<em>work-life balance, cost-effective</em>).
          <br>&bull; Em-dash (&mdash;): Emphatic parenthetical interruption.
        </li>
        <li><strong>Apostrophes:</strong>
          <br>&bull; Omission: <em>doesn't, it's</em> (it is).
          <br>&bull; Possession: <em>the company's fleet</em> (singular), <em>the employees' concerns</em> (plural).
        </li>
      </ul>
    </div>

    <div class="card-trap" style="padding:6px 10px;">
      <h3 style="color:#dc2626; margin-top:0;">Top 4 Examiner SPaG Traps</h3>
      <ul style="margin:2px 0 0 14px; padding:0;">
        <li><strong>Comma Splice:</strong> Joining two complete sentences with only a comma. (Wrong: <em>"The bus was late, I missed the meeting."</em> &rarr; Correct: <em>"The bus was late; consequently, I missed the meeting."</em>)</li>
        <li><strong>its vs it's:</strong> <em>its</em> = possessive pronoun (<em>"The car lost its wheel"</em>); <em>it's</em> = contraction of 'it is' or 'it has'.</li>
        <li><strong>Subject-Verb Inconsistency:</strong> <em>"A group of managers was present"</em> (singular subject 'group', not plural 'managers').</li>
        <li><strong>Homophone Confusion:</strong> <em>their / there / they're</em>; <em>affect / effect</em>; <em>compliment / complement</em>.</li>
      </ul>
    </div>
  </div>

  <div class="card-tip" style="margin-top:6px;">
    <h3 style="color:#d97706; margin-top:0;">The 5-Minute Proofreading Sweep</h3>
    <p style="font-size:8pt; margin:2px 0;">Never write right up to the final minute. Reserve 5 minutes at the end of Component 2. Read your text backwards sentence by sentence to isolate spelling and punctuation errors from narrative flow.</p>
  </div>

  <div class="page-footer">
    <div>English Level 2 &bull; Official 8-Mock Exam Pack &bull; SPaG Toolkit</div>
    <div class="page-num">Page 5</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 8 COMPLETE EXAM PAPERS (7 pages per paper = 56 pages, Pages 6 to 61)
    # -------------------------------------------------------------
    english_papers_data = [
        # Paper 1
        ("Mock Paper 1: Sustainable Energy & Electric Vehicle Infrastructure",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Department for Transport: National EV Charging Strategy</strong><br>
           The transition to zero-emission mobility represents the most significant transformation of the UK transport sector in over a century. Under government regulations, the sale of new petrol and diesel cars will be phased out to achieve legally binding Net Zero targets. To support this transition, the government has committed over £1.6 billion towards public charging infrastructure, with an expansion target of 300,000 public chargers by 2030.<br>
           Rapid chargers are being deployed across motorway service areas to ensure drivers can recharge within 20–30 minutes. Local authorities have been allocated dedicated funding to install on-street residential charge points, ensuring households without private driveways are not disadvantaged.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Motoring Journal: The Electric Reality &ndash; Are We Truly Ready?</strong><br>
           While ministers celebrate ambitious targets from comfortable Westminster offices, everyday motorists face a chaotic reality on the road. The public charging network remains plagued by broken connectors, conflicting mobile apps, and staggering regional disparities. In London and the South East, chargers are abundant; across northern rural communities, finding an operational rapid charger is like finding an oasis in a desert.<br>
           Furthermore, the astronomical upfront purchase price of electric vehicles places them well out of reach for working-class families. When coupled with soaring domestic electricity tariffs, the financial incentive has evaporated. For millions of motorists, the mandated deadline is unrealistic and punitive.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what target has the government set for public EV chargers by 2030, and how much funding is committed?"),
           ("Question 2 (Organisational Features)", "[2 Marks]", "Identify two organisational or presentational devices used in Text A to make information accessible."),
           ("Question 3 (Vocabulary in Context)", "[2 Marks]", "In Text A, what is meant by the phrase 'zero-emission mobility'?"),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two examples of emotive language or metaphor used by the writer, and explain their effect."),
           ("Question 5 (Bias & Perspective)", "[3 Marks]", "Explain how the perspective of the author in Text B differs from that of Text A regarding the EV transition."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one verifiable fact and one subjective opinion from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Both texts discuss electric vehicle infrastructure. Compare the points of view presented in Text A and Text B regarding public charging accessibility. (Refer to both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply when mentioning 'conflicting mobile apps' and 'regional disparities'?"),
           ("Question 9 (Text Purpose)", "[2 Marks]", "State the primary purpose of Text A and the primary purpose of Text B."),
           ("Question 10 (Critical Evaluation)", "[2 Marks]", "Explain why a motorist considering buying an electric vehicle should consult both Text A and Text B.")
         ],
         ("Task 1: Formal Workplace Article &bull; Renewable Energy Transition", 27,
          "You are the sustainability representative for your employer. Write a formal article (approx. 200–250 words) for the company newsletter evaluating whether the company should replace its commercial vehicle fleet with electric vans. You should include: potential cost savings on fuel, operational challenges (charging, range), impact on corporate environmental reputation, and a clear final recommendation."),
         ("Task 2: Professional Letter of Complaint &bull; Faulty Charging Station", 15,
          "You used a public rapid EV charger operated by VoltCharge Ltd at a retail park. The machine deducted £25 from your card but delivered no charge due to a software error. Write a formal letter of complaint (approx. 100–140 words) to Customer Services requesting a full refund, explaining what happened, and suggesting service improvements.")
        ),

        # Paper 2
        ("Mock Paper 2: Remote Working, Hybrid Culture & Employee Wellbeing",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Chartered Management Institute: The Hybrid Workplace Blueprint</strong><br>
           Hybrid working has permanently redefined modern commercial enterprise. Our national research indicates that 78% of UK knowledge-sector employees report enhanced work-life balance and reduced commuting stress when permitted to work flexibly. Organisations adopting structured hybrid policies have documented measurable reductions in office overheads, improved staff retention rates, and expanded recruitment pools.<br>
           To optimise productivity, employers should implement clear digital boundaries: scheduling core collaboration hours, discouraging out-of-hours emails, and conducting regular ergonomic desk assessments.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Opinion Editorial: The Silent Epidemic of Kitchen-Table Isolation</strong><br>
           Behind the glossy corporate rhetoric of 'flexibility', working from home has created an insidious culture of perpetual availability and social isolation. For junior employees, the spontaneous water-cooler mentorship that once built careers has been replaced by cold, transactional video calls.<br>
           The physical boundary between professional duty and domestic sanctuary has dissolved entirely. Employees find themselves tethered to laptops until late evening, battling digital fatigue and anxiety. True collaborative innovation requires spontaneous human synergy &mdash; something no video algorithm will ever replicate.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what percentage of knowledge-sector employees report enhanced work-life balance under hybrid working?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "In Text A, what is meant by 'ergonomic desk assessments'?"),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two formatting techniques used in Text A to present practical guidance to managers."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two emotive phrases used to describe working from home, and explain their psychological impact."),
           ("Question 5 (Author Bias)", "[3 Marks]", "How does the writer in Text B reveal a negative bias towards remote working?"),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one statistical fact from Text A and one opinion statement from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare the views expressed in Text A and Text B regarding the impact of remote working on employee wellbeing and connection. (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply about the prospects of younger workers starting their careers remotely?"),
           ("Question 9 (Text Purpose)", "[2 Marks]", "Identify the primary purpose of Text A and the primary purpose of Text B."),
           ("Question 10 (Practical Evaluation)", "[2 Marks]", "How could a manager use insights from both texts to design a balanced workplace policy?")
         ],
         ("Task 1: Formal Proposal Report &bull; Hybrid Working Policy Review", 27,
          "Write a formal proposal report (approx. 200–250 words) to your Operations Director evaluating your organisation's current remote working arrangements. Outline the benefits of flexible working, address potential concerns regarding staff isolation and communication, and make three practical recommendations for a sustainable hybrid policy."),
         ("Task 2: Staff Guidance Email &bull; Digital Wellbeing &amp; Boundaries", 15,
          "Write an internal email (approx. 100–140 words) to all team members providing practical guidance on maintaining digital wellbeing while working from home. Include: setting clear working hours, managing screen breaks, avoiding late-evening emails, and accessing company wellbeing support.")
        ),

        # Paper 3
        ("Mock Paper 3: Apprenticeships vs Traditional University Higher Education",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Institute for Apprenticeships: The Debt-Free Fast Track to Career Success</strong><br>
           Degree apprenticeships represent a revolutionary paradigm shift in UK higher vocational training. Candidates earn a competitive full-time salary from day one while completing a fully funded bachelor's or master's degree, entirely free of tuition debt. Employers across engineering, finance, software, and healthcare report that apprentices achieve commercial competence up to three years faster than traditional graduates.<br>
           With graduate employment rates exceeding 94% and zero student loans, degree apprenticeships combine rigorous academic theory with indispensable workplace acumen.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Academic Journal: The Enduring Value of the University Experience</strong><br>
           While the vocational utility of apprenticeships is undeniable, reducing higher education to mere job training fundamentally diminishes its transformative civil purpose. Universities cultivate critical intellectual enquiry, philosophical curiosity, and independent research skills that cannot be replicated on an office floor.<br>
           Moreover, the rich tapestry of campus life &mdash; student societies, international friendships, and self-discovery &mdash; fosters resilience and emotional maturity. Higher education is not simply an economic transaction; it is a life-shaping journey of intellectual enlightenment.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what is the graduate employment rate for degree apprentices, and what financial benefit is highlighted?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "Explain what the author in Text A means by 'commercial competence'."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two presentational techniques used in Text A to persuade potential applicants."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two examples of high-level or figurative language used to celebrate university life, and explain their effect."),
           ("Question 5 (Perspective & Tone)", "[3 Marks]", "Contrast the pragmatic economic tone of Text A with the idealistic academic tone of Text B."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one verifiable fact from Text A and one philosophical opinion from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare how Text A and Text B define the primary value of post-18 education. (Support your answer with evidence from both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply when referring to higher education as 'not simply an economic transaction'?"),
           ("Question 9 (Audience & Purpose)", "[2 Marks]", "State the intended target audience for Text A and the intended target audience for Text B."),
           ("Question 10 (Critical Synthesis)", "[2 Marks]", "Why might a prospective school leaver benefit from weighing the arguments in both texts?")
         ],
         ("Task 1: Formal Speech Script &bull; Sixth Form Careers Fair Presentation", 27,
          "You have been invited to deliver a formal speech (approx. 200–250 words) to Year 12 and 13 students at a regional Careers Fair on the topic: 'Degree Apprenticeships or Traditional University: Making the Right Choice for Your Future'. Weigh up earning while learning vs the university experience, and offer balanced advice on how to decide."),
         ("Task 2: Professional Email &bull; Seeking Apprentice Employer Mentorship", 15,
          "Write a professional email (approx. 100–140 words) to the Apprenticeship Lead at a local engineering firm requesting work shadowing or mentorship opportunities for vocational trainees. Detail your passion for practical engineering and explain how you would contribute to their workplace.")
        ),

        # Paper 4
        ("Mock Paper 4: Artificial Intelligence, Automation & Workplace Evolution",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Tech Innovation Whitepaper: Empowering the Modern Workforce with AI</strong><br>
           Artificial Intelligence is accelerating workplace transformation across every major economic sector. Far from eliminating human workers, generative AI algorithms act as cognitive copilots &mdash; automating repetitive administrative burdens, drafting routine documents, and rapidly synthesizing complex datasets.<br>
           This automation liberates human professionals to focus on high-value creative thinking, empathetic client interactions, and strategic leadership. Organisations integrating ethical AI systems report a 35% increase in operational productivity and significantly enhanced job satisfaction among frontline staff.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Trade Union Bulletin: The Devaluing of Human Labour in the Algorithmic Age</strong><br>
           Behind the utopian marketing hype of Silicon Valley, artificial intelligence poses an existential threat to white-collar livelihoods and worker autonomy. Across customer service, journalism, and creative industries, entry-level roles are being ruthlessly hollowed out by automated software.<br>
           Workers are increasingly subjected to algorithmic surveillance, robotic performance targets, and precarious digital contracts. When human judgment is outsourced to unaccountable algorithms, workers lose their professional dignity, and institutional accountability collapses entirely.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, by what percentage does operational productivity increase in organisations integrating ethical AI?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "Explain what the author in Text A means by describing AI as 'cognitive copilots'."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two formatting techniques used in Text A to highlight positive workforce outcomes."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, analyze two emotive or combative phrases used to critique AI adoption in business."),
           ("Question 5 (Tone & Bias)", "[3 Marks]", "How does the writer in Text B convey urgent hostility towards automated management systems?"),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one measurable fact from Text A and one subjective prediction from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare the differing attitudes towards workplace automation presented in Text A and Text B. (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the phrase 'algorithmic surveillance' in Text B suggest about management trust in automated workplaces?"),
           ("Question 9 (Text Purpose)", "[2 Marks]", "Identify the primary purpose of Text A and the primary purpose of Text B."),
           ("Question 10 (Critical Synthesis)", "[2 Marks]", "How can business leaders balance the productivity gains of Text A with the ethical concerns raised in Text B?")
         ],
         ("Task 1: Formal Discursive Article &bull; AI in the Modern Workplace", 27,
          "Write a formal discursive article (approx. 200–250 words) for a professional business magazine titled: 'AI in the Modern Workplace: Opportunity or Threat?'. Analyze both the productivity benefits of automated tools and the potential risks to job security and human wellbeing. Conclude with a clear set of ethical workplace guidelines."),
         ("Task 2: Professional Blog Post &bull; Future-Proofing Human Skills", 15,
          "Write a blog post (approx. 100–140 words) for a professional development website advising adult learners on how to develop 'AI-proof' human skills (such as communication, empathy, and creative problem solving) to succeed in automated workplaces.")
        ),

        # Paper 5
        ("Mock Paper 5: Eco-Tourism, Local Economies & Heritage Conservation",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; VisitBritain: Sustainable Tourism &amp; Economic Prosperity</strong><br>
           Cultural heritage and eco-tourism generate over £30 billion annually for rural communities across the UK. National Parks, historic market towns, and coastal conservation reserves support thousands of small hospitality enterprises, artisanal producers, and transport providers.<br>
           By encouraging sustainable 'slow tourism' &mdash; public transport travel, electric bike trails, and locally sourced food &mdash; destinations can protect fragile natural environments while securing year-round local employment.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Resident Association Letter: Over-Tourism is Killing Our Community</strong><br>
           Our picturesque coastal village is suffocating under an avalanche of holiday lets, gridlocked traffic, and seasonal litter. Second-home ownership has skyrocketed, driving house prices to astronomical levels and forcing young local families out of the village where their ancestors lived for generations.<br>
           When summer ends, our streets become dark, hollow ghost towns. A community cannot survive on four months of ice cream sales and souvenir shops while local schools and surgeries close due to falling permanent populations.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, how much does cultural heritage and eco-tourism generate for UK rural communities annually?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "Explain what is meant by 'slow tourism' in Text A."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two formatting techniques used in Text A to highlight commercial advantages."),
           ("Question 4 (Language Techniques)", "[3 Marks]", "In Text B, analyze the metaphor 'suffocating under an avalanche of holiday lets'."),
           ("Question 5 (Author Perspective)", "[3 Marks]", "Contrast the economic benefits emphasized in Text A with the community hardships highlighted in Text B."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one fact and one opinion from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare how the seasonal nature of tourism is portrayed in Text A and Text B. (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does Text B imply about the future viability of coastal village services (schools, GP clinics)?"),
           ("Question 9 (Purpose & Tone)", "[2 Marks]", "What is the primary purpose of Text B, and what tone does the resident association adopt?"),
           ("Question 10 (Critical Evaluation)", "[2 Marks]", "How could a local council reconcile the competing priorities described in both texts?")
         ],
         ("Task 1: Letter of Representation &bull; Tourism Management &amp; Housing", 27,
          "Write a formal letter of representation (approx. 200–250 words) to your local Member of Parliament (MP) addressing the impact of short-term holiday rentals on housing affordability and local services in your area. Propose constructive planning regulations, tourist levies, and affordable housing protections."),
         ("Task 2: Public Information Notice &bull; Eco-Tourism Code of Conduct", 15,
          "Draft a public information notice (approx. 100–140 words) for visitors to a National Nature Reserve. Include: protecting wildlife habitats, litter disposal, keeping dogs on leads, and supporting local farm shops.")
        ),

        # Paper 6
        ("Mock Paper 6: Active Travel, Public Transport & Urban Clean Air Zones",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Department for Transport: Clean Air Cities &amp; Active Mobility</strong><br>
           Air pollution represents the largest environmental risk to public health in the UK, contributing to thousands of premature deaths each year from respiratory and cardiovascular illnesses. In response, municipal authorities across the country are introducing Clean Air Zones (CAZ), accompanied by multi-million-pound investments in segregated cycle superhighways, zero-emission electric bus corridors, and school pedestrian streets.<br>
           International case studies prove that cities prioritizing walking, cycling, and dependable public transit experience not only a 40% reduction in harmful particulates, but also thriving high streets with increased footfall and vibrant civic life.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Small Business Federation: The Stranglehold of Anti-Motorist Schemes</strong><br>
           Under the sanctimonious guise of green health initiatives, city councils have declared an ideological war on motorists and independent retailers. Daily boundary charges, arbitrary road closures, and the elimination of short-stay parking have strangled customer access to independent town-centre businesses.<br>
           Tradespeople, couriers, and shift workers &mdash; who cannot carry ladders or equipment on bicycles &mdash; are being penalized by hundreds of pounds each month simply for doing their jobs. While suburban shopping malls offer free parking and convenient highway links, our historic high streets are being starved of oxygen by reckless bureaucratic zealotry.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what health illnesses are linked to urban air pollution, and what percentage reduction in particulates was recorded?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "Explain what is meant by 'segregated cycle superhighways' in Text A."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two formatting techniques used in Text A to persuade civic leaders."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two emotive or hyperbolic phrases used to describe clean air regulations, and explain their effect."),
           ("Question 5 (Perspective & Bias)", "[3 Marks]", "Explain how Text B displays an explicit bias against local council transport policies."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one verifiable fact from Text A and one opinion statement from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare the views on economic impact presented in Text A (high street footfall) and Text B (independent retailers). (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply about the fairness of clean air zone charges for tradespeople and shift workers?"),
           ("Question 9 (Purpose & Tone)", "[2 Marks]", "Identify the primary purpose of Text A and the primary purpose of Text B."),
           ("Question 10 (Critical Synthesis)", "[2 Marks]", "How could a town council balance environmental health priorities with small business economic viability?")
         ],
         ("Task 1: Formal Letter to City Council &bull; Urban Transport Consultation", 27,
          "Write a formal letter (approx. 200–250 words) to your City Council's Transport Committee responding to a public consultation on proposed Clean Air Zone charges and road changes. Evaluate both environmental health benefits and potential impacts on local businesses and vulnerable motorists, proposing constructive mitigation solutions."),
         ("Task 2: Staff Intranet Article &bull; Active Travel &amp; Cycle-to-Work Scheme", 15,
          "Write an engaging article (approx. 100–140 words) for your organisation's employee intranet promoting the company's new Cycle-to-Work Scheme and public transport season ticket loans. Highlight physical health benefits, cost savings, and secure on-site bike storage facilities.")
        ),

        # Paper 7
        ("Mock Paper 7: Mental Health in the Workplace & Employee Assistance",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Health and Safety Executive: Workplace Stress &amp; Corporate Duty of Care</strong><br>
           Work-related stress, depression, and anxiety account for 49% of all working days lost due to ill health in Great Britain, costing the national economy over £28 billion annually. Under the Health and Safety at Work Act, employers possess a statutory legal duty to assess and mitigate psychosocial risks in the workplace just as rigorously as physical machinery hazards.<br>
           Progressive organisations that implement comprehensive Mental Health First Aid programmes, manageable workloads, and confidential Employee Assistance Programmes (EAPs) achieve an estimated return of £5.30 in reduced absenteeism and boosted staff retention for every £1 invested.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Employee Testimonial: The Superficial Charade of 'Wellness Days'</strong><br>
           My company loves shouting about 'Mental Health Awareness Week' on social media, handing out branded water bottles, herbal tea bags, and lunchtime mindfulness webinars. Yet when our department lost three team members to cutbacks, management simply doubled the remaining staff's case allocations without a word of discussion.<br>
           We don't need patronizing yoga sessions or corporate platitudes about resilience. We need reasonable working hours, manageable caseloads, and managers who don't view taking scheduled annual leave as a personal betrayal. Corporate wellness initiatives are nothing more than a cosmetic band-aid over systemic burnout.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what percentage of lost working days is caused by work-related stress, and what is the return on investment per £1 spent?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "Explain what is meant by 'psychosocial risks' in Text A."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two formatting techniques used in Text A to highlight legal responsibilities."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two sarcastic or cynical phrases used by the writer, and explain their effect."),
           ("Question 5 (Author Perspective)", "[3 Marks]", "Contrast the formal administrative tone of Text A with the personal, frustrated tone of Text B."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one economic fact from Text A and one subjective grievance from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare how management initiatives regarding employee wellbeing are characterized in Text A and Text B. (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply about the true purpose of corporate 'wellness days'?"),
           ("Question 9 (Purpose & Audience)", "[2 Marks]", "State the intended audience of Text A and the intended audience of Text B."),
           ("Question 10 (Critical Evaluation)", "[2 Marks]", "What lessons should HR executives take from reading both texts alongside one another?")
         ],
         ("Task 1: Formal Workplace Wellbeing Report &bull; Managing Psychosocial Risk", 27,
          "Write a formal report (approx. 200–250 words) to your company's Board of Directors evaluating workplace stress and mental wellbeing. Detail current operational pressures (workloads, deadlines), evaluate existing support mechanisms, and make three practical recommendations to prevent employee burnout and foster a healthy working culture."),
         ("Task 2: Professional Support Email &bull; Phased Return to Work Plan", 15,
          "Write a supportive, professional email (approx. 100–140 words) as a line manager to a colleague returning to work after extended sick leave due to stress. Outline a proposed phased return schedule, modified duties, regular check-in meetings, and available workplace accommodations.")
        ),

        # Paper 8
        ("Mock Paper 8: Digital Privacy, Social Media Algorithms & Data Ethics",
         """<div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366; font-size:8pt;">Text A &bull; Information Commissioner's Office: Digital Rights &amp; Algorithmic Safety</strong><br>
           The modern digital economy relies upon personal data to personalize services, streamline e-commerce, and optimize educational software. Under UK GDPR and the Data Protection Act 2018, citizens enjoy fundamental statutory rights to transparent data processing, data rectification, and the right to erasure ('the right to be forgotten').<br>
           Furthermore, the Age Appropriate Design Code mandates that online platforms establish robust default privacy safeguards for adolescent users, restricting behavioural profiling, geo-location tracking, and automated nudge techniques designed to foster screen addiction.
         </div>
         <div style="background:#ffffff; border:1px solid #cbd5e1; padding:7px 10px; border-radius:4px; font-size:7.5pt;">
           <strong style="color:#003366; font-size:8pt;">Text B &bull; Cybersecurity Op-Ed: The Surveillance Machine Sells Your Attention</strong><br>
           Behind the slick interfaces of modern social media conglomerates lies a predatory business architecture known as surveillance capitalism. Our clicks, facial expressions, sleep cycles, and deepest vulnerabilities are harvested 24 hours a day and packaged into predictive behavioral models sold to commercial advertisers.<br>
           Algorithmic feeds are deliberately engineered to amplify sensationalist outrage, conspiracy theories, and body dissatisfaction because outrage generates clicks, and clicks generate advertising billions. Regulators are fighting an asymmetric war with paper decrees against multi-trillion-dollar behavioural engineering algorithms.
         </div>""",
         [
           ("Question 1 (Retrieval)", "[2 Marks]", "According to Text A, what two major statutes protect personal data in the UK, and what does the Age Appropriate Design Code restrict?"),
           ("Question 2 (Vocabulary)", "[2 Marks]", "In Text A, explain the legal concept of 'the right to erasure'."),
           ("Question 3 (Organisational Features)", "[2 Marks]", "Identify two structural techniques used in Text A to define statutory protections."),
           ("Question 4 (Language Devices)", "[3 Marks]", "In Text B, identify two powerful metaphors used to describe social media platforms, and analyze their impact."),
           ("Question 5 (Tone & Perspective)", "[3 Marks]", "Contrast the legalistic, reassuring tone of Text A with the urgent, confrontational tone of Text B."),
           ("Question 6 (Fact vs Opinion)", "[2 Marks]", "Identify one legal fact from Text A and one critical opinion from Text B.")
         ],
         [
           ("Question 7 (Comparison)", "[4 Marks]", "Compare the views on user protection and algorithmic control presented in Text A and Text B. (Quote both texts)."),
           ("Question 8 (Implicit Meaning)", "[3 Marks]", "What does the author of Text B imply by describing regulation as an 'asymmetric war'?"),
           ("Question 9 (Text Purpose)", "[2 Marks]", "Identify the primary purpose of Text A and the primary purpose of Text B."),
           ("Question 10 (Critical Synthesis)", "[2 Marks]", "How can individual citizens proactively protect their personal data in light of both texts?")
         ],
         ("Task 1: Formal Discursive Article &bull; Data Privacy in the Algorithmic Age", 27,
          "Write a formal article (approx. 200–250 words) for a national tech publication titled: 'Data Privacy in the Algorithmic Age: Regulating Big Tech'. Analyze how personal data is harvested and monetized, evaluate whether current regulations are sufficient, and propose tangible reforms to empower consumer digital rights."),
         ("Task 2: Formal Email of Inquiry &bull; GDPR Data Subject Access Request", 15,
          "Write a formal email (approx. 100–140 words) to the Data Protection Officer (DPO) of a major online retailer submitting a formal Subject Access Request (SAR) under UK GDPR. Request full copies of your browsing history, purchase tracking, and targeted marketing profiles, specifying legal response deadlines.")
        )
    ]

    for p_idx, (p_title, insert_html, read_q1, read_q2, w_task1, w_task2) in enumerate(english_papers_data, 1):
        # 7 Pages per Paper: Pages 6 to 61
        base_page = 6 + (p_idx - 1) * 7

        # Page 1 of paper: Reading Inserts (Text A & Text B)
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Component 1: Reading Inserts (Texts A &amp; B)</div>
  </div>

  <h2>{p_title}</h2>
  <div class="card-trap" style="margin-bottom:6px;">
    <strong>Reading Instructions:</strong> Read both Text A and Text B carefully before answering Questions 1 to 10 in the question booklet. You are advised to spend approximately 10 minutes reading and annotating.
  </div>

  {insert_html}

  <div class="card-tip" style="margin-top:auto;">
    <strong>Tutor Reading Tip:</strong> Underline key facts, statistics, and emotive phrases as you read. This will save you time when answering retrieval and language questions.
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Reading Inserts &bull; Page 1 of 3</div>
    <div class="page-num">Page {base_page}</div>
  </div>
</div>
""")

        # Page 2 of paper: Reading Questions (Q1-Q6)
        read_q1_html = ""
        for q_title, marks, q_text in read_q1:
            read_q1_html += f"""
<div style="margin-bottom:6px;">
  <div style="display:flex; justify-content:space-between;"><strong>{q_title}:</strong> <span class="mark-badge" style="background:#003366;">{marks}</span></div>
  <p style="margin:1px 0 3px 0; font-size:7.8pt;">{q_text}</p>
  <div class="workspace-ruled" style="min-height:36px; padding:4px 8px;">Show response here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Component 1: Reading Questions (Part 1)</div>
  </div>

  <h2>Reading Question Booklet &bull; Questions 1 to 6</h2>
  <p style="margin-bottom:6px;">Answer all questions based strictly on Text A and Text B. Ensure your handwriting is clear.</p>

  {read_q1_html}

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Reading Questions &bull; Page 2 of 3</div>
    <div class="page-num">Page {base_page + 1}</div>
  </div>
</div>
""")

        # Page 3 of paper: Reading Questions (Q7-Q10)
        read_q2_html = ""
        for q_title, marks, q_text in read_q2:
            read_q2_html += f"""
<div style="margin-bottom:8px;">
  <div style="display:flex; justify-content:space-between;"><strong>{q_title}:</strong> <span class="mark-badge" style="background:#003366;">{marks}</span></div>
  <p style="margin:2px 0 4px 0; font-size:8pt;">{q_text}</p>
  <div class="workspace-ruled" style="min-height:55px;">Show comparative analysis and evaluation here...</div>
</div>
"""

        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Component 1: Reading Questions (Part 2)</div>
  </div>

  <h2>Reading Question Booklet &bull; Questions 7 to 10</h2>
  <p style="margin-bottom:8px;">Questions 7 to 10 test comparative synthesis and critical evaluation. (Reading Total: 35 Marks).</p>

  {read_q2_html}

  <div class="card-tip" style="margin-top:auto;">
    <strong>End of Reading Component:</strong> Ensure you have compared BOTH texts in Question 7 before proceeding to Writing.
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Reading Questions &bull; Page 3 of 3</div>
    <div class="page-num">Page {base_page + 2}</div>
  </div>
</div>
""")

        # Page 4 of paper: Writing Task 1 Brief & Planning
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Component 2: Writing &bull; Task 1 (Extended Writing)</div>
  </div>

  <h2>{w_task1[0]}</h2>
  <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
    <div style="font-weight:700; color:#003366;">Recommended Time: 45 Minutes</div>
    <span class="mark-badge" style="background:#003366;">[{w_task1[1]} Marks]</span>
  </div>

  <div class="card-practice" style="border-left-color:#003366; margin-bottom:8px;">
    <strong>Task Brief:</strong><br>
    {w_task1[2]}
  </div>

  <div class="card-method" style="margin-bottom:8px;">
    <strong>Assessment Criteria &amp; Structural Checklist:</strong>
    <ul style="margin:2px 0 0 14px; padding:0; font-size:7.8pt;">
      <li>Clear layout suitable for format (title, subheadings, or salutation).</li>
      <li>Minimum 4 well-structured paragraphs: Intro, Point 1, Point 2, Recommendation.</li>
      <li>Formal, professional register maintained throughout.</li>
      <li>Advanced punctuation: colon (:), semicolon (;), and varied connectives.</li>
    </ul>
  </div>

  <div style="margin-top:4px;">
    <strong>Planning Workspace &bull; Brainstorm &amp; Outline:</strong>
    <div class="workspace-ruled" style="min-height:100px;">Plan your 4 main paragraphs, key vocabulary, and connectives here...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Task 1 Brief &amp; Plan &bull; Page 1 of 4</div>
    <div class="page-num">Page {base_page + 3}</div>
  </div>
</div>
""")

        # Page 5 of paper: Task 1 Candidate Ruled Writing Booklet
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Task 1: Candidate Writing Response Booklet</div>
  </div>

  <div style="font-weight:700; color:#003366; margin-bottom:4px;">Write your response to Task 1 below (Target: 200–250 words):</div>
  <div class="workspace-ruled" style="min-height:680px; line-height:22px; font-size:8.5pt;">Write your Task 1 response here...</div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Task 1 Response Booklet &bull; Page 2 of 4</div>
    <div class="page-num">Page {base_page + 4}</div>
  </div>
</div>
""")

        # Page 6 of paper: Writing Task 2 Brief & Planning
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Component 2: Writing &bull; Task 2 (Workplace Task)</div>
  </div>

  <h2>{w_task2[0]}</h2>
  <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
    <div style="font-weight:700; color:#003366;">Recommended Time: 30 Minutes</div>
    <span class="mark-badge" style="background:#003366;">[{w_task2[1]} Marks]</span>
  </div>

  <div class="card-practice" style="border-left-color:#003366; margin-bottom:8px;">
    <strong>Task Brief:</strong><br>
    {w_task2[2]}
  </div>

  <div class="card-method" style="margin-bottom:8px;">
    <strong>Assessment Criteria &amp; Structural Checklist:</strong>
    <ul style="margin:2px 0 0 14px; padding:0; font-size:7.8pt;">
      <li>Clear format conventions (email subject, letter addresses, or clear headings).</li>
      <li>Concise, functional, action-oriented workplace tone.</li>
      <li>Bullet points used effectively for clarity where appropriate.</li>
      <li>Polite, decisive sign-off with clear next steps.</li>
    </ul>
  </div>

  <div style="margin-top:4px;">
    <strong>Planning Workspace &bull; Brainstorm &amp; Outline:</strong>
    <div class="workspace-ruled" style="min-height:100px;">Plan your key factual details, tone, and action requests here...</div>
  </div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Task 2 Brief &amp; Plan &bull; Page 3 of 4</div>
    <div class="page-num">Page {base_page + 5}</div>
  </div>
</div>
""")

        # Page 7 of paper: Task 2 Candidate Ruled Writing Booklet
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English L2 &bull; Paper {p_idx}</div>
    <div class="page-header-strand">Task 2: Candidate Writing Response Booklet</div>
  </div>

  <div style="font-weight:700; color:#003366; margin-bottom:4px;">Write your response to Task 2 below (Target: 100–140 words):</div>
  <div class="workspace-ruled" style="min-height:680px; line-height:22px; font-size:8.5pt;">Write your Task 2 response here...</div>

  <div class="page-footer">
    <div>Paper {p_idx} &bull; Task 2 Response Booklet &bull; Page 4 of 4</div>
    <div class="page-num">Page {base_page + 6}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # 22 PAGES OF COMPREHENSIVE EXAMINER MARK SCHEMES (Pages 62 to 83)
    # -------------------------------------------------------------
    english_mark_schemes = [
        # Page 62: Paper 1 Mark Scheme (Reading Q1-Q10)
        ("Official Mark Scheme &bull; Paper 1 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>Target: 300,000 public chargers by 2030 [1 mark]. Funding committed: Over £1.6 billion [1 mark].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Award 1 mark each (max 2): (a) Bold title/subheadings, (b) Short readable paragraphs, (c) Statistics presented clearly.</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>Travel/transport that releases no tailpipe pollutants or carbon emissions into the atmosphere (e.g. electric/hydrogen vehicles) [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'plagued by broken connectors' (personification/disease metaphor conveying pervasive dysfunction) [1.5m]; 'like finding an oasis in a desert' (hyperbolic simile highlighting extreme rural scarcity) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Text A takes an optimistic, governmental perspective emphasizing investments and expansion targets [1.5m]; Text B takes a skeptical, consumer-advocate perspective highlighting daily driver frustration, cost barriers, and regional inequalities [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: 'Upfront purchase price... places them out of reach' or reference to tariffs [1m]. Opinion: 'the mandated deadline is unrealistic and punitive' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A asserts that rapid chargers are being deployed across motorway services and residential funding is allocated [2m]. Conversely, Text B highlights that chargers are concentrated in London/SE while northern rural drivers face broken hardware and conflicting apps [2m]. Comparative connective used [1m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that the charging network is fragmented, unregulated, poorly maintained, and geographically unjust [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Inform the public of government investment and strategic EV roadmap [1m]. Text B: Express opinion, challenge policy, and highlight motorist grievances [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Text A provides the official vision and infrastructure roadmap, while Text B provides real-world consumer cautions regarding reliability and running costs [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 63: Paper 1 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 1 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Newsletter Article:</strong><br>
           <strong>Electrifying Our Commercial Fleet: A Sustainable Roadmap for Growth</strong><br>
           As our company strives to meet ambitious corporate social responsibility benchmarks, transitioning our commercial delivery fleet from diesel vans to modern electric vehicles (EVs) represents a compelling strategic opportunity; nevertheless, it requires meticulous operational planning.<br>
           From a financial perspective, commercial electricity rates offer substantial long-term operational savings over diesel fuel. With diesel fluctuating above £1.45 per litre, our projected fuel expenditure would decrease by an estimated 42% across annual routes. Furthermore, adopting zero-emission vans eliminates costly daily Clean Air Zone charges and demonstrates genuine environmental stewardship to our eco-conscious client base.<br>
           However, operational hurdles must be addressed proactively. Driver range anxiety remains a valid concern, particularly during winter delivery peaks. Additionally, relying exclusively on public charging networks risks productivity bottlenecks due to fragmented app ecosystems and charger outages. Therefore, the transition must be accompanied by installing on-site rapid depot chargers.<br>
           In conclusion, the environmental and commercial benefits far outweigh the initial capital outlay. I recommend a phased transition: converting our urban distribution routes immediately while conducting a feasibility trial for long-haul journeys.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Letter of Complaint:</strong><br>
           14 Highfield Crescent, Sheffield, S10 2TN &bull; 12 October 2026<br>
           Customer Services Department, VoltCharge Ltd, London, EC2A 1AA<br>
           Dear Sir or Madam,<br>
           <strong>RE: Urgent Refund Request &ndash; Charger Station #4028 (Meadowhall Retail Park)</strong><br>
           I am writing to register a formal complaint regarding a defective rapid charger at your Meadowhall site on 10 October 2026. After tapping my debit card, the terminal pre-authorized a £25 transaction; however, the machine immediately displayed error code 'ERR-54' and failed to deliver any charge.<br>
           Despite calling your helpline immediately, the automated system failed to release the pre-authorization hold. I request an immediate £25 refund and recommend that your engineering team recalibrates the transaction software on unit #4028 to prevent other motorists experiencing similar financial inconvenience.<br>
           Yours faithfully,<br><em>[Candidate Name]</em>
         </div>"""),

        # Page 64: Paper 2 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 2 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>78% of UK knowledge-sector employees [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Workstation health and safety checks to ensure chairs, monitors, and posture prevent repetitive strain and physical injury [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Bullet points for actionable management steps, (b) Bold lead-in phrases, (c) Survey statistics [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'silent epidemic of kitchen-table isolation' (metaphor of disease framing loneliness as a public health hazard) [1.5m]; 'dissolved entirely' (conveys loss of safety boundaries) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Employs loaded negative vocabulary ('insidious', 'cold, transactional', 'tethered', 'reckless') and omits any acknowledgment of employee flexibility benefits [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: '78% of UK knowledge-sector employees report enhanced work-life balance' [1m]. Opinion: 'True collaborative innovation requires spontaneous human synergy' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A argues hybrid working reduces commuting stress and improves retention [2m]. In sharp contrast, Text B contends it leads to perpetual availability, burnout, and social detachment [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that junior staff will miss informal learning, peer networking, and career progression without daily face-to-face mentorship [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Provide evidence-based management guidance for hybrid policy [1m]. Text B: Provoke debate and challenge conventional wisdom on home working [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Allows employers to embrace the productivity and recruitment benefits of flexibility while introducing safeguards against isolation and burnout [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 65: Paper 2 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 2 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Proposal Report:</strong><br>
           <strong>To:</strong> Operations Director &bull; <strong>From:</strong> HR Project Lead &bull; <strong>Date:</strong> 14 October 2026<br>
           <strong>Subject:</strong> Strategic Review of Hybrid Working Arrangements<br>
           <strong>1. Executive Summary:</strong> This report evaluates our current hybrid model to optimize team collaboration while safeguarding staff wellbeing.<br>
           <strong>2. Operational Benefits:</strong> Since introducing flexible schedules, staff turnover has dropped by 18%; furthermore, employees consistently praise the elimination of arduous peak-hour commuting. Office utility overheads have reduced significantly.<br>
           <strong>3. Emerging Challenges:</strong> Despite commercial advantages, recent internal surveys reveal emerging difficulties: junior staff report feeling detached from team leaders, while several departments experience disjointed communication due to incompatible remote schedules.<br>
           <strong>4. Recommendations:</strong><br>
           &bull; Establish core 'in-office collaboration days' (Tuesdays and Thursdays) to foster team cohesion.<br>
           &bull; Mandate a 'Right to Disconnect' policy prohibiting non-urgent emails between 18:00 and 08:00.<br>
           &bull; Implement structured one-to-one weekly mentoring sessions for all newly hired apprentices.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Internal Guidance Email:</strong><br>
           <strong>To:</strong> All Staff &bull; <strong>Subject:</strong> Maintaining Healthy Digital Boundaries While Working Remotely<br>
           Dear Colleagues,<br>
           As part of our ongoing commitment to employee wellbeing, please review these key practices for remote days:<br>
           &bull; <strong>Define Your Working Day:</strong> Log off promptly at your scheduled finish time; do not feel obliged to monitor messages outside core hours.<br>
           &bull; <strong>Screen Breaks:</strong> Follow the 20-20-20 rule to prevent eye strain and take a full away-from-desk lunch break.<br>
           &bull; <strong>Support Resources:</strong> If you feel overwhelmed or isolated, our confidential Employee Assistance Programme is accessible 24/7 on extension 4402.<br>
           Kind regards,<br><em>[Candidate Name] &bull; Wellbeing Coordinator</em>
         </div>"""),

        # Page 66: Paper 3 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 3 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>Graduate employment rate exceeds 94% [1m]; candidates earn a salary with zero tuition debt [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Practical workplace skills, industry knowledge, and capability to perform commercial duties effectively without supervision [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Persuasive title with power words ('Debt-Free Fast Track'), (b) Statistical data (94%), (c) Sector listing [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'rich tapestry of campus life' (metaphor conveying intricate, colourful experiences) [1.5m]; 'life-shaping journey of intellectual enlightenment' (elevated academic register inspiring reverence) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Text A uses an economic, pragmatic register focusing on earnings, debt avoidance, and corporate utility [1.5m]; Text B uses an idealistic, philosophical tone focusing on critical thinking, personal growth, and intellectual curiosity [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: '94% graduate employment rate' [1m]. Opinion: 'reducing higher education to mere job training fundamentally diminishes its transformative civil purpose' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A defines value through financial independence, employment rates, and rapid workplace mastery [2m]. Conversely, Text B defines value through intellectual independence, critical enquiry, and cultural maturation [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that treating education solely as an investment for financial profit ignores deeper human development and democratic citizenship [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: School/college leavers and career changers [1m]. Text B: Educators, academics, and policy analysts [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Helps candidates assess whether their personal learning style aligns better with structured workplace application or theoretical exploration [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 67: Paper 3 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 3 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Speech Script:</strong><br>
           <strong>Degree Apprenticeships vs Traditional University: Charting Your Course</strong><br>
           Good morning, students, teachers, and guests. Standing at the threshold of post-18 choices can feel daunting; however, today you hold more extraordinary pathways than any generation before you.<br>
           For decades, university was viewed as the sole golden ticket to professional careers. The traditional campus experience offers unparalleled intellectual freedom, lifelong friendships, and the space to explore complex subjects in depth. Yet, this path carries substantial financial commitments: average student loan debts now exceed £45,000.<br>
           In stark contrast, degree apprenticeships have completely rewritten the rulebook. Imagine graduating with a fully accredited degree, three to four years of practical industry experience, and zero tuition debt; imagine receiving a monthly salary while learning from leading corporate mentors. In sectors from aerospace to cyber security, degree apprentices are advancing into senior management years ahead of university graduates.<br>
           My advice is simple: reflect honestly on how you learn best. If you thrive on independent research and theoretical debate, university remains unmatched. But if you are ambitious, eager to build tangible products, and keen to launch your career debt-free, an apprenticeship is the ultimate accelerator. Thank you.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Mentorship Request Email:</strong><br>
           <strong>To:</strong> apprenticeships@vanguard-engineering.co.uk &bull; <strong>Subject:</strong> Vocational Mentorship &amp; Work Shadowing Inquiry<br>
           Dear Mr Davies,<br>
           I am currently completing my Level 2 Functional Skills and Mechanical Engineering diploma at Oakridge Technical College. I am writing to express my strong admiration for Vanguard Engineering's renewable energy projects and to inquire about potential work shadowing or mentorship opportunities.<br>
           I possess dedicated practical skills in CAD drafting and workshop safety, combined with an eager work ethic. Gaining insight into your CNC manufacturing facility would provide invaluable context for my upcoming Advanced Apprenticeship application.<br>
           I would welcome the opportunity to discuss how I could assist your workshop team on a voluntary basis. Thank you for your consideration.<br>
           Yours sincerely,<br><em>[Candidate Name]</em>
         </div>"""),

        # Page 68: Paper 4 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 4 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>35% increase in operational productivity [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Collaborative digital assistants that work alongside human professionals to handle repetitive calculation and drafting tasks [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Clear corporate subheadings, (b) Quantitative percentage metrics, (c) Positive vocabulary highlights [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'ruthlessly hollowed out' (violent vocabulary conveying corporate brutality) [1.5m]; 'algorithmic surveillance' (dystopian Orwellian imagery suggesting loss of human trust) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Hostile tone achieved through militant vocabulary ('predatory', 'existential threat', 'unaccountable algorithms') and dismissal of opposing claims as 'utopian marketing hype' [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: '35% increase in operational productivity' [1m]. Opinion: 'worker autonomy is being hollowed out' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A portrays AI as an empowering tool that frees humans for creative leadership [2m]. Conversely, Text B portrays AI as an exploitative technology leading to job insecurity and surveillance [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Suggests that employers use software metrics to micromanage staff movements and output unfairly without understanding human nuance [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Promote adoption of ethical AI enterprise software [1m]. Text B: Defend union workers' rights and warn against unchecked technological displacement [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Enables policymakers to harness AI efficiency while enacting statutory protections against unfair automated dismissal and surveillance [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 69: Paper 4 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 4 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Magazine Article:</strong><br>
           <strong>Artificial Intelligence: Catalyzing Human Potential or Automating Obsolescence?</strong><br>
           The exponential rise of generative artificial intelligence has ignited impassioned debate across boardrooms and breakrooms alike. While Silicon Valley champions AI as the pinnacle of workplace evolution, sceptics warn of an impending crisis in human employment; the truth, however, lies in how responsibly business leaders steer this technological revolution.<br>
           Undeniably, automated software provides transformative efficiencies. Routine administrative tasks &mdash; such as scheduling meetings, cross-referencing spreadsheets, and drafting compliance summaries &mdash; can now be executed in seconds. By delegating cognitive drudgery to digital copilots, employees can redirect their expertise towards strategic problem solving, ethical governance, and empathetic customer relationships.<br>
           Nevertheless, valid anxieties regarding workplace equity must not be dismissed. Left unchecked, aggressive automation risks destabilizing entry-level vocations, while algorithmic performance tracking erodes employee morale. To ensure ethical integration, organisations must implement transparent governance: establishing clear AI usage policies, investing heavily in employee reskilling, and ensuring that human judgment remains the final arbiter in all personnel decisions.<br>
           Ultimately, artificial intelligence is neither an existential monster nor a panacea; it is a tool. Its ultimate legacy will depend entirely on whether we deploy it to devalue labour or elevate human capability.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Professional Blog Post:</strong><br>
           <strong>Future-Proofing Your Career: The Irreplaceable Power of Human Skills</strong><br>
           As automated algorithms master data processing and coding, what skills will ensure you remain indispensable in the workplace of tomorrow?<br>
           The answer is simple: your unique humanity. Algorithms can analyze numbers, but they cannot show genuine empathy to an upset customer; they can generate text, but they cannot mediate a sensitive workplace conflict. Focus on developing these three core human capabilities:<br>
           &bull; <strong>Active Emotional Intelligence:</strong> Listening deeply and inspiring trust within multidisciplinary teams.<br>
           &bull; <strong>Adaptive Problem Solving:</strong> Navigating ambiguous crises where historical data offers no clear precedent.<br>
           &bull; <strong>Ethical Judgment:</strong> Questioning whether automated solutions are fair, inclusive, and socially responsible.<br>
           Invest in your emotional intelligence today &mdash; it is the ultimate automated shield!
         </div>"""),

        # Page 70: Paper 5 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 5 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>Over £30 billion annually [2 marks].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Environmentally responsible, unhurried travel utilizing public transit, walking/cycling trails, and local farm produce to reduce carbon footprint [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Promotional branding header, (b) Em-dash parenthetical definitions, (c) Economic statistics [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'suffocating under an avalanche of holiday lets' (metaphor of suffocation/burial conveying overwhelming pressure and existential threat) [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Text A emphasizes commercial vibrancy, entrepreneurship, and rural job creation [1.5m]; Text B emphasizes community destruction, housing unaffordability, and the closure of local schools and surgeries [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: 'cultural heritage and eco-tourism generate over £30 billion' [1m]. Opinion: 'second-home ownership is killing our community' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A portrays seasonal tourism as a foundation for year-round local enterprise [2m]. Text B counters that seasonal visitors leave empty ghost towns during winter months, making permanent community life unsustainable [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that local infrastructure is facing collapse, forcing permanent families and young people to abandon their historic communities [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Promote UK domestic tourism and economic investment [1m]. Text B: Protest against unconstrained holiday rentals and demand urgent government intervention [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Assists planners in implementing tourist levies and housing quotas that capture tourism revenue while protecting affordable housing for locals [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 71: Paper 5 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 5 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Letter of Representation:</strong><br>
           42 Cliffside Way, St Ives, Cornwall, TR26 1AB &bull; 16 October 2026<br>
           Rt Hon. Eleanor Vance MP, House of Commons, London, SW1A 0AA<br>
           Dear Ms Vance,<br>
           <strong>RE: Urgent Planning Reform &ndash; Impact of Unregulated Short-Term Holiday Lets</strong><br>
           I am writing to you on behalf of the Coastal Community Housing Action Group to express grave concern regarding the proliferation of unregulated holiday lets across our constituency. While tourism remains an essential pillar of our coastal economy, the current crisis threatens the social fabric of our community.<br>
           Over the past four years, an estimated 35% of residential properties in our village have been converted into commercial vacation rentals. Consequently, long-term rental stock has vanished, driving local house prices beyond 14 times average regional earnings. Young teachers, nurses, and maritime workers are being displaced, resulting in falling school rolls and severe staffing deficits across local health surgeries.<br>
           To safeguard our historic communities, we urge you to champion statutory legislative reforms: introducing mandatory planning permission for holiday rental conversions, empowering councils to cap second-home ownership percentages, and implementing a 2% visitor tourist levy ring-fenced for affordable social housing.<br>
           We request an urgent meeting with you to discuss these proposals before our vibrant year-round community becomes a permanent winter ghost town.<br>
           Yours sincerely,<br><em>[Candidate Name] &bull; Secretary, CCHAG</em>
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Public Information Notice:</strong><br>
           <strong>Highland Nature Reserve &bull; Visitor Code of Conduct</strong><br>
           Welcome to the Highland Reserve! To protect our endangered nesting birds and fragile peat bog habitats, please observe these simple guidelines:<br>
           &bull; <strong>Stay on Marked Boardwalks:</strong> Wandering off designated trails causes severe soil erosion and damages delicate moss ecosystems.<br>
           &bull; <strong>Keep Dogs on Leads:</strong> Protect livestock and ground-nesting wildlife by keeping pets on short leads at all times.<br>
           &bull; <strong>Zero-Trace Policy:</strong> Take all litter, food wrappers, and dog waste home with you; bins are not provided in the wild interior.<br>
           &bull; <strong>Support Local Producers:</strong> Enjoy fresh refreshments at the community farm shop by the car park!<br>
           <em>Thank you for helping us preserve this wilderness for future generations.</em>
         </div>"""),

        # Page 72: Paper 6 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 6 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>Respiratory and cardiovascular illnesses [1m]; 40% reduction in harmful particulates [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Dedicated cycling corridors physically separated from motor vehicle traffic by kerbs or barriers to guarantee safety [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Statistical public health citations, (b) References to international case studies, (c) Formal authoritative vocabulary [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'sanctimonious guise' (attacks moral hypocrisy of regulators) [1.5m]; 'strangled customer access' (violent imagery framing regulations as an economic assault) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Reveals bias through hostile loaded words ('anti-motorist schemes', 'ideological war', 'bureaucratic zealotry') while completely ignoring documented health improvements [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: 'Air pollution contributes to thousands of premature deaths each year' [1m]. Opinion: 'Historic high streets are being starved of oxygen by reckless bureaucratic zealotry' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A argues that clean air zones create thriving high streets with increased pedestrian footfall [2m]. Conversely, Text B asserts that removing parking and imposing boundary fees starves independent retailers of customer revenue [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that clean air policies unfairly penalize blue-collar workers and tradespeople who have no viable public transit alternative [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Inform the public and justify transport decarbonisation policy [1m]. Text B: Advocate for small business owners and campaign against municipal traffic schemes [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Enables policymakers to design active travel zones with tailored exemptions for tradespeople, delivery couriers, and mobility badge holders [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 73: Paper 6 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 6 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Letter to Transport Committee:</strong><br>
           28 Victoria Parade, Birmingham, B15 3TR &bull; 18 October 2026<br>
           Transport Consultation Committee, Birmingham City Council, Council House, B1 1BB<br>
           Dear Committee Members,<br>
           <strong>RE: Public Consultation Response &ndash; Proposed Clean Air Zone Expansion &amp; Active Travel Corridors</strong><br>
           I am writing in response to the public consultation regarding the proposed expansion of our municipal Clean Air Zone (CAZ) and the installation of segregated cycleways along our arterial roads. As both an inner-city resident and a local business patron, I strongly support the objective of improving urban air quality while advocating pragmatic measures to protect independent commerce.<br>
           The public health imperative cannot be overstated. Chronic respiratory ailments disproportionately afflict children and elderly citizens along congested corridors; therefore, expanding electric bus routes and building segregated cycle networks is an indispensable investment. International evidence demonstrates that pedestrianized zones with cleaner air experience sustained growth in retail footfall over time.<br>
           However, transitional hardship for local tradespeople and small independent retailers must not be overlooked. Heavy commercial vehicles and service vans cannot be replaced overnight with cargo bikes. Therefore, I propose three targeted recommendations: granting a phased grace period for Euro 6 commercial diesel vehicles, introducing heavily subsidized electric cargo-van leasing schemes, and designating free 30-minute click-and-collect bays on adjacent streets.<br>
           By combining environmental ambition with practical commercial empathy, the council can deliver cleaner air without compromising independent livelihoods.<br>
           Yours sincerely,<br><em>[Candidate Name]</em>
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Employee Intranet Article:</strong><br>
           <strong>Ditch the Gridlock: Unlock Savings with Our Active Travel &amp; Cycle Schemes!</strong><br>
           Tired of sitting in morning rush-hour traffic and watching fuel prices eat into your monthly salary? We are thrilled to announce our newly expanded Active Travel Benefits package!<br>
           Through our tax-free <em>Cycle-to-Work Scheme</em>, you can save up to 40% on brand-new bicycles and electric bikes, spread across manageable monthly payroll deductions. To ensure your commute is seamless, our headquarters now features secure fob-access bike storage, heated drying lockers, and refurbished shower suites.<br>
           Prefer public transport? We also provide interest-free annual bus and rail season ticket loans. Visit the HR intranet portal today to calculate your monthly savings and embrace a healthier commute!
         </div>"""),

        # Page 74: Paper 7 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 7 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>49% of all working days lost [1m]; return of £5.30 for every £1 invested [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>Workplace organizational hazards related to stress, excessive workloads, lack of control, and interpersonal conflict affecting psychological health [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Statutory legal references (Health and Safety at Work Act), (b) Cost-benefit return figures, (c) Clear paragraph structure [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'superficial charade of wellness days' (exposes hypocrisy and performative management) [1.5m]; 'cosmetic band-aid over systemic burnout' (metaphor of minor first aid unable to heal deep structural wounds) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Text A adopts an objective, statistical, corporate governance register [1.5m]; Text B adopts a cynical, candid, emotionally exhausted first-person voice [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: 'Work-related stress costs the national economy over £28 billion annually' [1m]. Opinion: 'Corporate wellness initiatives are nothing more than a cosmetic band-aid' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A claims that Employee Assistance Programmes and mental health first aid yield measurable financial and productivity returns [2m]. Text B contends that wellness webinars and token gifts fail to address the core problem of unmanageable workloads and understaffing [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that corporate wellness events are PR exercises designed for social media rather than genuine concern for staff welfare [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Inform employers of statutory legal duties and economic advantages of wellbeing policies [1m]. Text B: Voice worker frustration and expose superficial corporate wellness initiatives [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Encourages leadership teams to look beyond superficial perks and address root structural causes of workplace stress (headcount, deadlines, overtime) [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 75: Paper 7 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 7 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; Board of Directors Report:</strong><br>
           <strong>To:</strong> Board of Directors &bull; <strong>From:</strong> Head of People &amp; Culture &bull; <strong>Date:</strong> 20 October 2026<br>
           <strong>Subject:</strong> Comprehensive Review of Workplace Mental Health &amp; Psychosocial Risk<br>
           <strong>1. Purpose:</strong> This report outlines systemic operational risks stemming from workplace stress and recommends robust interventions to protect staff retention.<br>
           <strong>2. Assessment of Pressures:</strong> Employee absence data indicates a 26% rise in stress-related leave across operational departments over the past 12 months. Exit interviews demonstrate that staff shortages, tight delivery deadlines, and chronic out-of-hours email traffic are contributing directly to burnout.<br>
           <strong>3. Evaluation of Support:</strong> While the company currently provides an Employee Assistance helpline, take-up remains low due to stigma and a perception that management favours cosmetic 'wellness days' over addressing core workload volumes.<br>
           <strong>4. Recommendations:</strong><br>
           &bull; <strong>Workload Rebalancing:</strong> Audit project resourcing to ensure realistic case allocations and prevent structural overtime.<br>
           &bull; <strong>Management Training:</strong> Train all department managers as accredited Mental Health First Aiders to recognize early warning signs of fatigue.<br>
           &bull; <strong>Right to Disconnect:</strong> Enforce server-level guidelines discouraging evening and weekend email exchanges.<br>
           Implementing these recommendations will fulfill our legal duty of care and ensure sustainable organizational performance.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Phased Return Support Email:</strong><br>
           <strong>To:</strong> j.miller@enterprise.co.uk &bull; <strong>Subject:</strong> Warm Welcome Back &ndash; Phased Return Plan<br>
           Dear James,<br>
           I hope you are keeping well. Ahead of your return next Monday, I want to reassure you that our primary priority is supporting your smooth, stress-free reintegration into the team.<br>
           To ensure you are not overwhelmed, we have arranged a three-week phased return schedule: working half-days for the first two weeks with zero out-of-hours on-call duties. I will personally manage your client inbox, and we will hold a relaxed, informal check-in every Friday morning.<br>
           Please let me know if you would like any additional workplace adjustments. We are thrilled to have you back!<br>
           Warm regards,<br><em>[Candidate Name] &bull; Team Leader</em>
         </div>"""),

        # Page 76: Paper 8 Mark Scheme (Reading Component)
        ("Official Mark Scheme &bull; Paper 8 (Reading Component)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Q</th><th>Reading Mark Scheme &amp; Acceptable Responses</th><th>Marks</th></tr>
           <tr><td><strong>1</strong></td><td>UK GDPR and the Data Protection Act 2018 [1m]; restrictions on profiling, geolocation tracking, and nudge techniques for adolescents [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>2</strong></td><td>The legal statutory entitlement under GDPR for individuals to request that an organisation delete their personal information without delay [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>3</strong></td><td>(a) Citation of statutory legislation, (b) Quoted legal definitions ('the right to be forgotten'), (c) Structured legal tone [2m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>4</strong></td><td>'surveillance capitalism' (evokes predatory commercial exploitation) [1.5m]; 'asymmetric war with paper decrees' (military metaphor highlighting regulatory impotence against tech giants) [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>5</strong></td><td>Text A uses an objective, statutory, reassuring legal register [1.5m]; Text B uses an aggressive, alarming, confrontational journalistic style [1.5m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>6</strong></td><td>Fact: 'Under UK GDPR citizens enjoy statutory rights to data rectification' [1m]. Opinion: 'Regulators are fighting an asymmetric war with paper decrees' [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>7</strong></td><td>Comparison: Text A emphasizes legal protections, individual control, and statutory age codes [2m]. In contrast, Text B argues that algorithms secretly harvest personal data 24 hours a day to monetize human attention [2m].</td><td><strong>[4]</strong></td></tr>
           <tr><td><strong>8</strong></td><td>Implies that official privacy regulations are hopelessly outmatched by the financial power, computational speed, and engineering sophistication of social media firms [3m].</td><td><strong>[3]</strong></td></tr>
           <tr><td><strong>9</strong></td><td>Text A: Inform citizens of their legal rights under data protection statutes [1m]. Text B: Expose behavioral tracking practices and sound a societal alarm [1m].</td><td><strong>[2]</strong></td></tr>
           <tr><td><strong>10</strong></td><td>Enables users to combine legal rights (such as SAR requests and cookie opt-outs) with proactive digital hygiene (ad blockers, tracking restrictions) [2m].</td><td><strong>[2]</strong></td></tr>
         </table>"""),

        # Page 77: Paper 8 Mark Scheme (Writing Band 4 Models)
        ("Official Mark Scheme &bull; Paper 8 (Band 4 Model Writing)",
         """<div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Task 1 Model Answer (Band 4 &bull; 27/27 Marks) &bull; National Tech Article:</strong><br>
           <strong>Data Privacy in the Algorithmic Age: Can Regulation Tame Big Tech?</strong><br>
           In our hyper-connected contemporary society, data is frequently heralded as the new oil. Yet while oil is extracted from subterranean rock, digital data is harvested directly from our private human lives: tracking our midnight anxieties, keystroke cadence, and intimate purchasing impulses. As multinational tech conglomerates monetize personal vulnerabilities, society faces an existential test of privacy and autonomy.<br>
           Proponents of algorithmic personalization argue that data profiling delivers tailored convenience: recommending educational tutorials, streaming entertainment, and accelerating commerce. However, this convenience masks an invasive infrastructure of behavioral surveillance. Algorithmic feeds deliberately amplify polarising outrage to maximize platform dwell-time, directly contributing to surging adolescent anxiety and the degradation of public discourse.<br>
           While the UK GDPR and the Age Appropriate Design Code establish commendable statutory benchmarks, enforcement mechanisms remain woefully under-resourced against trillion-dollar tech giants. To safeguard democratic rights, legislative bodies must move beyond reactive fines. We require mandatory algorithmic transparency audits, strict prohibitions on behavioral profiling of young people, and meaningful user-owned data portability.<br>
           Personal privacy is not a luxury good traded for mobile convenience; it is a fundamental human right. Until regulation matches the computational power of the platforms it seeks to govern, our digital freedom remains dangerously precarious.
         </div>
         <div class="card-method" style="font-size:7.5pt;">
           <strong style="color:#16a34a;">Task 2 Model Answer (Band 4 &bull; 15/15 Marks) &bull; Subject Access Request Email:</strong><br>
           <strong>To:</strong> dpo@nexusecommerce.co.uk &bull; <strong>Subject:</strong> Formal Subject Access Request (SAR) &ndash; UK GDPR Article 15<br>
           Dear Data Protection Officer,<br>
           Please accept this email as a formal Subject Access Request submitted under Article 15 of the UK General Data Protection Regulation (UK GDPR).<br>
           I request comprehensive copies of all personal data held regarding my account (Customer Reference: #NX-88402), including: my complete transaction history, algorithmic behavioural profiles, automated marketing tags, and third-party data-sharing logs.<br>
           Under statutory provisions, you are required to fulfill this request without undue delay and at the latest within one calendar month of receipt. Please furnish the data in an accessible, machine-readable digital format.<br>
           Yours sincerely,<br><em>[Candidate Name]</em>
         </div>"""),

        # Page 78: Examiner Marking Guide & Assessment Criteria Summary
        ("Official Examiner Writing Assessment Rubric &bull; Task 1 (27 Marks)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Assessment Criterion</th><th>Band 1 (1–3m)</th><th>Band 2 (4–6m)</th><th>Band 3 (7–10m)</th><th>Band 4 (11–16m)</th></tr>
           <tr>
             <td><strong>Content &amp; Organisation (16 Marks)</strong></td>
             <td>Minimal response; incomplete coverage of brief; fragmented ideas; lacks paragraphing.</td>
             <td>Basic ideas; simple paragraphing; emerging awareness of audience and purpose; inconsistent tone.</td>
             <td>Clear, detailed response addressing all bullet points; logical paragraph transitions; consistent formal register.</td>
             <td>Sophisticated, nuanced arguments; seamless structural discourse markers; compelling persuasive or formal tone adapted perfectly to audience.</td>
           </tr>
           <tr><th>Criterion</th><th>Band 1 (1–2m)</th><th>Band 2 (3–5m)</th><th>Band 3 (6–8m)</th><th>Band 4 (9–11m)</th></tr>
           <tr>
             <td><strong>SPaG &bull; Spelling, Punctuation &amp; Grammar (11 Marks)</strong></td>
             <td>Pervasive spelling errors; run-on sentences; comma splices; basic punctuation omitted.</td>
             <td>Simple words spelled correctly; basic full stops and capitals secure; limited punctuation range.</td>
             <td>Complex vocabulary spelled accurately; secure commas and apostrophes; compound sentence variety.</td>
             <td>Flawless spelling of ambitious terminology; sophisticated punctuation (colons, semicolons, dashes); varied syntactic structures.</td>
           </tr>
         </table>"""),

        # Page 79: Examiner Marking Guide & Assessment Criteria Summary
        ("Official Examiner Writing Assessment Rubric &bull; Task 2 (15 Marks)",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Assessment Criterion</th><th>Band 1 (1–2m)</th><th>Band 2 (3–4m)</th><th>Band 3 (5–6m)</th><th>Band 4 (7–9m)</th></tr>
           <tr>
             <td><strong>Content &amp; Organisation (9 Marks)</strong></td>
             <td>Brief or incomplete message; unclear purpose; lacks format conventions.</td>
             <td>Basic functional message; conventional format attempting email/letter; basic sentence flow.</td>
             <td>Clear functional focus; appropriate workplace register; organized layout (subject line, bullets).</td>
             <td>Highly effective workplace communication; concise, actionable tone; exemplary format conventions and salutations.</td>
           </tr>
           <tr><th>Criterion</th><th>Band 1 (1m)</th><th>Band 2 (2–3m)</th><th>Band 3 (4–5m)</th><th>Band 4 (6m)</th></tr>
           <tr>
             <td><strong>SPaG &bull; Spelling, Punctuation &amp; Grammar (6 Marks)</strong></td>
             <td>Frequent spelling and grammatical slips impeding understanding.</td>
             <td>Generally accurate with simple sentences; occasional punctuation slips.</td>
             <td>Good grammatical control; secure sentence boundaries; correct workplace vocabulary.</td>
             <td>Virtually error-free SPaG; sophisticated sentence construction; flawless proofreading.</td>
           </tr>
         </table>"""),

        # Page 80: High-Frequency Vocabulary & Connectives Reference
        ("Level 2 Writing Toolkit &bull; Advanced Connectives &amp; Vocabulary",
         """<div class="grid-2" style="font-size:7.5pt;">
           <div class="card-concept" style="border-left-color:#003366;">
             <strong style="color:#003366;">Comparative &amp; Contradictory Connectives:</strong>
             <ul style="margin:2px 0 0 12px; padding:0;">
               <li><em>Whereas / While:</em> Highlights contrasting conditions simultaneously.</li>
               <li><em>Conversely / In sharp contrast:</em> Introduces direct opposing evidence.</li>
               <li><em>Notwithstanding / Despite:</em> Acknowledges concessions before asserting conclusions.</li>
               <li><em>On the other hand:</em> Weighs opposing viewpoints.</li>
             </ul>
           </div>
           <div class="card-method">
             <strong style="color:#16a34a;">Causal &amp; Cumulative Connectives:</strong>
             <ul style="margin:2px 0 0 12px; padding:0;">
               <li><em>Furthermore / In addition:</em> Adds reinforcing arguments.</li>
               <li><em>Consequently / Therefore:</em> Establishes logical cause and effect.</li>
               <li><em>Significantly / Crucially:</em> Emphasizes paramount importance.</li>
               <li><em>Ultimately / In conclusion:</em> Synthesizes overarching recommendations.</li>
             </ul>
           </div>
         </div>
         <div class="card-practice" style="border-left-color:#003366; font-size:7.5pt; margin-top:6px;">
           <strong style="color:#003366;">Band 4 Ambitious Vocabulary Bank:</strong><br>
           <code>accelerate &bull; imperative &bull; detrimental &bull; indispensable &bull; paradigm &bull; sustainable &bull; profound &bull; rigorous &bull; nuance &bull; exacerbate &bull; disproportionate &bull; autonomous &bull; proliferation &bull; mitigate</code>
         </div>"""),

        # Page 81: Reading Assessment Standards & Question Taxonomy
        ("Official Reading Assessment Standards &bull; Question Analysis",
         """<table class="data-table" style="font-size:7.5pt;">
           <tr><th>Question Type</th><th>Assessment Focus</th><th>Examiner Advice for Candidates</th></tr>
           <tr><td><strong>Retrieval (Q1)</strong></td><td>Locate explicit facts &amp; figures</td><td>Quote directly from the text or state verbatim numbers. Never guess.</td></tr>
           <tr><td><strong>Vocabulary (Q2, Q3)</strong></td><td>Define terminology in context</td><td>Explain the specific meaning within the passage, not just dictionary definitions.</td></tr>
           <tr><td><strong>Language Devices (Q4)</strong></td><td>Metaphor, hyperbole, rule of 3</td><td>Name the technique AND explain the psychological/emotional impact on the reader.</td></tr>
           <tr><td><strong>Bias &amp; Tone (Q5)</strong></td><td>Detect author perspective</td><td>Identify loaded words, selective reporting, or cynical rhetoric.</td></tr>
           <tr><td><strong>Fact vs Opinion (Q6)</strong></td><td>Distinguish verifiable data</td><td>Facts can be empirically checked; opinions reflect personal value judgments.</td></tr>
           <tr><td><strong>Synthesis (Q7)</strong></td><td>Compare Text A &amp; Text B</td><td>You MUST mention both texts and draw explicit parallels or contrasts using connectives.</td></tr>
           <tr><td><strong>Implicit Meaning (Q8)</strong></td><td>Deduce subtext</td><td>Explain what the author suggests without saying it out loud.</td></tr>
           <tr><td><strong>Purpose (Q9, Q10)</strong></td><td>Evaluate communicative goal</td><td>State whether the text intends to inform, persuade, warn, or entertain.</td></tr>
         </table>"""),

        # Page 82: Common Candidate Writing Errors & How to Avoid Them
        ("Top 10 Examiner Pitfalls in Functional English Level 2 Writing",
         """<div class="grid-2" style="font-size:7.5pt;">
           <div class="card-trap">
             <strong style="color:#dc2626;">Top 5 Content Pitfalls:</strong>
             <ol style="margin:2px 0 0 14px; padding:0;">
               <li><strong>Ignoring Bullet Points:</strong> Missing one prompt immediately drops your task achievement mark.</li>
               <li><strong>Under-Length Responses:</strong> Writing fewer than 180 words for Task 1 limits Band progression.</li>
               <li><strong>Informal Slang:</strong> Using casual vernacular (<em>"kids", "gonna", "sort it out"</em>).</li>
               <li><strong>Unbroken Text Blocks:</strong> Writing without clear indentation or paragraph spacing.</li>
               <li><strong>Mismatched Format:</strong> Submitting a letter without addresses or a report without headings.</li>
             </ol>
           </div>
           <div class="card-tip">
             <strong style="color:#d97706;">Top 5 SPaG Pitfalls:</strong>
             <ol style="margin:2px 0 0 14px; padding:0;">
               <li><strong>The Comma Splice:</strong> Joining sentences with a comma instead of a full stop or semicolon.</li>
               <li><strong>Apostrophe Confusion:</strong> Misusing <em>its</em> (possessive) and <em>it's</em> (it is).</li>
               <li><strong>Homophone Lapses:</strong> Confusing <em>there, their, they're</em> and <em>affect / effect</em>.</li>
               <li><strong>Tense Inconsistency:</strong> Switching randomly between past and present narrative voice.</li>
               <li><strong>Lack of Proofreading:</strong> Leaving avoidable transcription slips that cost crucial SPaG marks.</li>
             </ol>
           </div>
         </div>"""),

        # Page 83: Official Grade Boundaries & Pass Threshold Guidance
        ("Official Level 2 Functional Skills English Grade Boundaries",
         """<div class="card-concept" style="border-left-color:#003366; font-size:7.5pt; margin-bottom:6px;">
           <strong style="color:#003366;">Official Passing Thresholds across Awarding Bodies (Edexcel, C&amp;G, NCFE, Highfield):</strong><br>
           <table class="data-table" style="font-size:7.5pt; margin-top:4px;">
             <tr><th>Component</th><th>Total Available Marks</th><th>Typical Pass Mark Range</th><th>Percentage Required</th></tr>
             <tr><td>Component 1: Reading</td><td>35 Marks</td><td>22 – 24 Marks</td><td>~63% – 68%</td></tr>
             <tr><td>Component 2: Writing</td><td>42 Marks</td><td>26 – 28 Marks</td><td>~62% – 67%</td></tr>
             <tr style="background:#e0f2fe; font-weight:bold;"><td>Combined Level 2 Qualification</td><td>77 Marks</td><td>48 – 52 Marks</td><td>~65% – 68%</td></tr>
           </table>
         </div>
         <div class="card-tip" style="font-size:7.5pt;">
           <strong>Advice for Candidates Reaching Band 4:</strong><br>
           High-scoring candidates secure passes with distinction by maintaining disciplined time management (allocating 45 minutes to Task 1 and 30 minutes to Task 2, with 5 minutes for proofreading), utilizing colons and semicolons with precision, and ensuring that every recommendation in Task 1 is supported by compelling operational logic.
         </div>""")
    ]

    for p_num, (p_title, p_content) in enumerate(english_mark_schemes, 62):
        pages.append(f"""
<div class="page">
  <div class="page-header">
    <div class="page-header-title">Master Functional Skills &bull; English Level 2</div>
    <div class="page-header-strand">Official Examiner Mark Scheme</div>
  </div>

  <h2>{p_title}</h2>
  <p style="margin-bottom:6px;">Review Reading mark allocations and high-scoring Band 4 benchmark model writing responses.</p>

  {p_content}

  <div class="page-footer">
    <div>English Level 2 &bull; Official 8-Mock Exam Pack &bull; Mark Scheme</div>
    <div class="page-num">Page {p_num}</div>
  </div>
</div>
""")

    # -------------------------------------------------------------
    # PAGE 84: BACK COVER
    # -------------------------------------------------------------
    pages.append(f"""
<div class="page cover-full-page">
  <img src="file://{back_img}" class="cover-full-img">
</div>
""")

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>English Level 2 Official 8-Mock Exam Pack</title>
{SHARED_CSS}
<style>
  :root {{
    --theme: #003366;
    --accent: #f59e0b;
  }}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    pdf_filename = "MasterFunctionalSkills_Mock_Pack_English_L2.pdf"
    count = render_book_to_pdf(full_html, pdf_filename)
    return count

if __name__ == "__main__":
    build_mock_english_l2_book()
