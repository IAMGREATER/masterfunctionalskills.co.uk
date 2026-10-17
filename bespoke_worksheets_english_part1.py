#!/usr/bin/env python3
"""
Bespoke Worksheets English Part 1: 11 Core Reading Topics.
Every question stem contains a genuine, self-contained reading excerpt, quote, or paired text comparison.
"""
from build_topic_dataset import make_english_topic

WORKSHEETS_ENGLISH_PART1 = [
    # 1. Comparing Texts
    make_english_topic(
        slug="reading-comparing-texts",
        title="Comparing Texts & Contrasting Perspectives",
        category="reading",
        spec_codes="L1.10 • L2.12 • L2.15",
        golden_rule="Never summarise Text A and Text B in isolated blocks. Always link both texts in the same sentence using comparative connectives ('similarly', 'both agree', 'whereas', 'in contrast') and support your points with short quotations from BOTH texts.",
        q1={
            "title": "Question 1 (Level 1 Identifying a Shared Similarity)",
            "marks": 2,
            "stem": "Read the two extracts about a hospital car park:<br><strong>Text A (Estates Notice):</strong> <em>'Due to severe morning congestion, the South Car Park will become staff-only from 1st November, with 80 new spaces added.'</em><br><strong>Text B (Patient Forum):</strong> <em>'Everyone knows morning congestion at the hospital is awful, but banning patients from the South Car Park will make us late for appointments!'</em><br><br>Identify <strong>one point of agreement</strong> between Text A and Text B, and quote a phrase from each text to prove it.",
            "lines": 3,
            "ans_label": "Shared Agreement & Quotes =",
            "choice_box": "Agreement: ________________ | Text A Quote: ____________ | Text B Quote: ____________",
            "step_rows": [
                ("1. Identify shared agreement: Both texts agree that morning traffic/parking congestion at the hospital is severe", "[A1]"),
                ("2. Supporting quotes: Text A ('severe morning congestion') and Text B ('morning congestion at the hospital is awful')", "[A1]")
            ],
            "final_answer": "Both agree morning parking congestion is bad ('severe morning congestion' / 'morning congestion... is awful').",
            "pitfall": "Stating a difference ( banning patients) when the question specifically asks for a point of agreement.",
            "reverse_check": "Check both quotes refer to the exact same issue (morning congestion)."
        },
        q2={
            "title": "Question 2 (Level 1 Identifying Contrasting Viewpoints)",
            "marks": 2,
            "stem": "Read the two extracts on cashless supermarket checkouts:<br><strong>Text A (Store Manager):</strong> <em>'Card-only self-checkouts halve queue waiting times and eliminate till cash-counting mistakes at closing time.'</em><br><strong>Text B (Senior Citizens' Group):</strong> <em>'Card-only rules exclude pensioners who rely on physical cash notes to budget their weekly pension.'</em><br><br>Using a comparative connective (e.g. <em>whereas</em>), explain how Text A and Text B disagree about card-only checkouts.",
            "lines": 3,
            "ans_label": "Comparative Statement =",
            "choice_box": "Text A views them as ________________, whereas Text B argues ________________",
            "step_rows": [
                ("1. State Text A's positive operational view: Halves queue times and stops cash-counting errors", "[A1]"),
                ("2. Link with 'whereas/in contrast' to Text B's negative social view: Excludes pensioners who budget using physical cash", "[A1]")
            ],
            "final_answer": "Text A praises card-only tills for halving queues and stopping cash errors, whereas Text B criticises them for excluding pensioners who budget with cash.",
            "pitfall": "Writing two separate sentences without a comparative connective linking the viewpoints.",
            "reverse_check": "Does your sentence contain 'whereas', 'however', or 'in contrast'?"
        },
        q3={
            "title": "Question 3 (Level 1/2 Comparing Factual Claims Across Workplace Texts)",
            "marks": 3,
            "stem": "Read the two extracts on open-plan offices:<br><strong>Text A (Facilities Architect):</strong> <em>'Removing partition walls cuts office heating bills by 25% and encourages spontaneous teamwork between departments.'</em><br><strong>Text B (Staff Survey Summary):</strong> <em>'While staff agree that cross-department teamwork has improved, 68% complain that constant phone noise ruins their concentration.'</em><br><br>Identify <strong>one similarity</strong> and <strong>two differences</strong> in the information given by Text A and Text B.",
            "lines": 4,
            "ans_label": "Similarity & Two Differences =",
            "choice_box": "Similarity: ____________ | Diff 1: ____________ | Diff 2: ____________",
            "step_rows": [
                ("1. Similarity: Both texts agree that open-plan offices improve teamwork between departments", "[A1]"),
                ("2. Difference 1 (Focus/Benefit): Text A highlights a 25% saving on heating bills, which Text B does not mention", "[A1]"),
                ("3. Difference 2 (Drawback): Text B highlights that 68% of staff suffer ruined concentration from noise, whereas Text A only presents positives", "[A1]")
            ],
            "final_answer": "Similarity: Both agree teamwork improves. Diff 1: Text A cites a 25% heating saving. Diff 2: Text B reports 68% of staff lose concentration due to noise.",
            "pitfall": "Giving only one difference when the 3-mark tariff requires one similarity and two differences.",
            "reverse_check": "1 similarity + 2 differences = 3 marks."
        },
        q4={
            "title": "Question 4 (Level 2 Comparing Writer Tone and Attitude)",
            "marks": 3,
            "stem": "Read the two extracts on a proposed four-day working week:<br><strong>Text A (HR Pilot Report):</strong> <em>'The six-month trial demonstrated a 40% reduction in staff sick leave while maintaining 100% customer service output.'</em><br><strong>Text B (Small Business Owner):</strong> <em>'This reckless fad will bankrupt high-street shops that cannot afford to pay full-time wages for part-time hours!'</em><br><br>Compare the <strong>tone</strong> of Text A and Text B, supporting your answer with <strong>one quotation from each text</strong>.",
            "lines": 4,
            "ans_label": "Tone Comparison & Quotes =",
            "choice_box": "Text A Tone & Quote: ________________ | Text B Tone & Quote: ________________",
            "step_rows": [
                ("1. Identify Text A tone & quote: Objective, formal, and measured tone ('demonstrated a 40% reduction in staff sick leave')", "[A1]"),
                ("2. Identify Text B tone & quote: Alarmist, angry, and emotive tone ('reckless fad will bankrupt high-street shops!')", "[A1]"),
                ("3. Use explicit comparative phrasing contrasting data-led calmness with emotional outrage", "[A1]")
            ],
            "final_answer": "Text A uses a formal, objective tone backed by statistics ('40% reduction'), whereas Text B uses an angry, alarmist tone with emotive language ('reckless fad will bankrupt...').",
            "pitfall": "Describing what the texts are about without naming the tone (objective vs alarmist/angry).",
            "reverse_check": "Have you named the tone AND copied a short quote for both Text A and Text B?"
        },
        q5={
            "title": "Question 5 (Level 2 Comparing Language Techniques Across Two Texts)",
            "marks": 4,
            "stem": "<strong>Text A (Electric Fleet Press Release):</strong><br><em>'Switching to zero-emission vans has cut our depot carbon footprint by 120 tonnes and lowered maintenance costs by 30%.'</em><br><br><strong>Text B (Delivery Driver Blog):</strong><br><em>'Being stranded on a freezing motorway with a dead battery is every driver's worst nightmare! How can we deliver on time when chargers are always broken?'</em><br><br>Compare how the writers of Text A and Text B use <strong>language techniques</strong> to convey their views on electric vans.",
            "lines": 5,
            "ans_label": "Comparative Language Analysis =",
            "choice_box": "Text A Techniques & Quotes: ____________ | Text B Techniques & Quotes: ____________",
            "step_rows": [
                ("1. Text A View & Technique 1: Positive view supported by statistics/numerical facts ('120 tonnes', '30%')", "[A1]"),
                ("2. Text A Technique 2: Professional, factual corporate diction ('zero-emission vans', 'lowered maintenance costs') to build logical credibility", "[A1]"),
                ("3. Text B View & Technique 1: Negative/frustrated view using emotive language and hyperbole ('freezing motorway', 'worst nightmare!')", "[A1]"),
                ("4. Text B Technique 2: Rhetorical question ('How can we deliver on time when chargers are always broken?') to challenge management", "[A1]")
            ],
            "final_answer": "Text A promotes electric vans using factual statistics ('120 tonnes', '30%') in a professional register, whereas Text B criticises their reliability using emotive hyperbole ('worst nightmare!') and a rhetorical question ('How can we deliver on time...?').",
            "pitfall": "Listing techniques from Text A only, or forgetting to explain how the techniques reflect contrasting views.",
            "reverse_check": "Verify at least two techniques/quotes from Text A are contrasted against two from Text B."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Three Sources)",
            "marks": 4,
            "stem": "Read all three extracts on night-shift working:<br><strong>Text A (Medical Journal):</strong> <em>'Rotating night shifts disrupt natural circadian rhythms and increase long-term cardiovascular risk by 19%.'</em><br><strong>Text B (Warehouse Worker):</strong> <em>'The 25% night-shift pay premium adds £350 a month to my wages, and the roads are completely traffic-free at 5 a.m.'</em><br><strong>Text C (Union Advisor):</strong> <em>'Night workers suffer higher fatigue rates, though free hot meals on night shifts significantly boost morale.'</em><br><br>Using evidence from <strong>all three texts</strong>, explain the <strong>advantages</strong> and <strong>disadvantages</strong> of night-shift work.",
            "lines": 5,
            "ans_label": "Summary of 3 Texts =",
            "choice_box": "Disadvantages (Texts A & C): ____________ | Advantages (Texts B & C): ____________",
            "step_rows": [
                ("1. Disadvantage from Text A: Disrupts circadian rhythms and raises cardiovascular risk by 19%", "[A1]"),
                ("2. Disadvantage from Text C: Higher fatigue rates among night workers", "[A1]"),
                ("3. Advantage from Text B: 25% pay premium (£350 extra per month) and traffic-free commuting at 5 a.m.", "[A1]"),
                ("4. Advantage from Text C: Free hot meals boost staff morale", "[A1]")
            ],
            "final_answer": "Disadvantages: Disrupts sleep/circadian rhythms and increases heart risk by 19% (Text A), plus higher fatigue (Text C). Advantages: £350/month (25%) extra pay and traffic-free travel (Text B), plus morale-boosting free hot meals (Text C).",
            "pitfall": "Omitting one of the three texts — you must draw evidence from Text A, Text B, and Text C to gain all 4 marks.",
            "reverse_check": "Did you cite Text A, Text B, and Text C explicitly?"
        }
    ),

    # 2. Investigating Image
    make_english_topic(
        slug="reading-investigating-image",
        title="Images, Diagrams, Charts & Captions",
        category="reading",
        spec_codes="L1.14 • L2.16 • L2.17",
        golden_rule="Images, diagrams, and charts are never merely decorative in Functional Skills exams. Always link the specific visual detail shown in the image (and any facts inside its caption) directly to the writer's core purpose and emotional/practical effect on the reader.",
        q1={
            "title": "Question 1 (Level 1 Extracting Information from an Image Caption)",
            "marks": 2,
            "stem": "A workplace fire safety leaflet includes a photograph of a silver CO2 fire extinguisher with a black horn nozzle. Beneath the photo, the caption reads:<br><em>'Figure 2: Carbon Dioxide (CO2) extinguishers (black label) are safe for live electrical server fires but must NEVER be used on chip-pan grease fires.'</em><br><br>Using the caption, state: (a) what colour label a CO2 extinguisher has, and (b) which type of fire it must <strong>never</strong> be used on.",
            "lines": 3,
            "ans_label": "Caption Facts =",
            "choice_box": "(a) Label colour: ________________ | (b) Never use on: ________________",
            "step_rows": [
                ("1. (a) Extract label colour from brackets in caption: Black label", "[A1]"),
                ("2. (b) Extract prohibited fire type: Chip-pan grease fires", "[A1]")
            ],
            "final_answer": "(a) Black label; (b) Chip-pan grease fires.",
            "pitfall": "Answering 'silver' (the cylinder body colour in the stem) instead of 'black label' as stated in the caption.",
            "reverse_check": "Check the exact bracketed text '(black label)' and 'chip-pan grease fires' in the caption."
        },
        q2={
            "title": "Question 2 (Level 1 Explaining the Purpose of an Instructional Diagram)",
            "marks": 2,
            "stem": "A flat-pack office desk manual includes a step-by-step line diagram showing how Cam Lock A twists 90 degrees clockwise using a crosshead screwdriver to lock Pin B into the wooden side panel.<br><br>Give <strong>two reasons</strong> why the writer included this diagram alongside the written instructions.",
            "lines": 3,
            "ans_label": "Two Reasons =",
            "choice_box": "Reason 1: ________________________ | Reason 2: ________________________",
            "step_rows": [
                ("1. Visual clarity: Shows the exact physical orientation and 90-degree clockwise twist of Cam Lock A and Pin B more clearly than words alone", "[A1]"),
                ("2. Error prevention: Helps the person assembling the desk identify the correct fittings and avoid damaging the wooden panel", "[A1]")
            ],
            "final_answer": "1. Visually shows how Cam Lock A and Pin B fit together and turn 90 degrees. 2. Prevents assembly mistakes and damage.",
            "pitfall": "Writing vague answers like 'it makes the manual look nice' or 'fills up space'.",
            "reverse_check": "Does your answer refer specifically to assembling the desk parts (Cam Lock A / Pin B)?"
        },
        q3={
            "title": "Question 3 (Level 1/2 Analysing Emotive Photographs in Charity Appeals)",
            "marks": 3,
            "stem": "A winter homelessness appeal leaflet features the headline <em>'No One Should Freeze on Our Streets Tonight'</em> alongside a black-and-white photograph of an elderly man huddled in a doorway under a thin wet blanket in the snow.<br><br>Explain how this photograph supports the headline and helps achieve the leaflet's purpose. (3 marks)",
            "lines": 4,
            "ans_label": "Visual & Emotional Analysis =",
            "choice_box": "Visual detail: ____________ | Emotion triggered: ____________ | Link to purpose: ____________",
            "step_rows": [
                ("1. Identify specific visual detail: Shows a vulnerable elderly man shivering in snow under a thin wet blanket (sombre black-and-white tone)", "[A1]"),
                ("2. Identify emotional impact: Provokes immediate empathy, sympathy, shock, and moral guilt in the reader", "[A1]"),
                ("3. Link to headline & purpose: Visually proves the urgency of 'No One Should Freeze' and persuades readers to donate money immediately", "[A1]")
            ],
            "final_answer": "The photo of a vulnerable elderly man in the snow reinforces the headline 'No One Should Freeze', evoking sympathy and urgency that persuades readers to donate.",
            "pitfall": "Simply stating 'it shows a homeless man' without explaining the emotional response (sympathy/urgency) and fundraising purpose.",
            "reverse_check": "Visual detail + Emotional effect + Link to donating = 3 marks."
        },
        q4={
            "title": "Question 4 (Level 2 Interpreting Data from a Embedded Bar Chart)",
            "marks": 3,
            "stem": "A council waste report includes a bar chart titled <strong>'Household Recycling Rates by Ward (%)'</strong>:<br>• <strong>Oakfield Ward:</strong> 64% (Green bar)<br>• <strong>Central Ward:</strong> 28% (Red bar)<br>• <strong>Riverside Ward:</strong> 51% (Amber bar)<br><em>Caption: 'Target statutory minimum across all wards: 50%.'</em><br><br>Using the chart and caption, identify which ward is failing the statutory target, by how many percentage points it falls short, and explain why the designer colour-coded the bars.",
            "lines": 4,
            "ans_label": "Ward, Shortfall & Colour Purpose =",
            "choice_box": "Failing Ward: ________ | Shortfall: ________% | Colour Purpose: ________________",
            "step_rows": [
                ("1. Identify failing ward: Central Ward (28% is below the 50% statutory minimum in the caption)", "[A1]"),
                ("2. Calculate exact shortfall: 50% - 28% = 22 percentage points (22%) short", "[A1]"),
                ("3. Explain colour coding: Traffic-light colours (red/amber/green) allow readers to spot failing (red) vs high-performing (green) wards at a glance", "[A1]")
            ],
            "final_answer": "Central Ward fails by 22 percentage points (28% vs 50% target); traffic-light colours let readers spot underperforming wards instantly.",
            "pitfall": "Missing the 50% target printed in the caption or forgetting to explain the red/amber/green colour coding.",
            "reverse_check": "50 - 28 = 22%; Central Ward is the red bar."
        },
        q5={
            "title": "Question 5 (Level 2 Evaluating Dual Images — Before and After Contrast)",
            "marks": 4,
            "stem": "An advert for ' HydroClean Patio Restoration' displays two side-by-side photographs:<br>• <strong>Photo 1 (Left — Labelled 'BEFORE'):</strong> Dull, black moss-covered paving slabs with slippery green algae.<br>• <strong>Photo 2 (Right — Labelled 'AFTER 1 HOUR'):</strong> Bright, clean golden sandstone slabs gleaming in the sun.<br><br>Analyse how the company uses these paired images and labels to persuade homeowners to book their service.",
            "lines": 5,
            "ans_label": "Paired Image Evaluation =",
            "choice_box": "Contrast Effect: ____________ | Proof of Speed: ____________ | Persuasive Impact: ____________",
            "step_rows": [
                ("1. Visual contrast: Places the dirty, slippery moss-covered slabs directly next to the gleaming golden sandstone to dramatise the transformation", "[M1]"),
                ("2. Evidence of effectiveness: Provides tangible visual proof that the cleaning treatment works thoroughly", "[A1]"),
                ("3. Impact of the label ('AFTER 1 HOUR'): Emphasises how rapid and effortless the results are", "[A1]"),
                ("4. Overall persuasive impact: Builds customer trust and desire to transform their own garden patio", "[A1]")
            ],
            "final_answer": "Side-by-side 'BEFORE' and 'AFTER 1 HOUR' photos dramatise the contrast between slippery moss and gleaming stone, proving the service is both fast (1 hour) and highly effective.",
            "pitfall": "Describing only one photo instead of explaining the persuasive power of the side-by-side 'Before vs After' contrast.",
            "reverse_check": "Did you mention both the visual transformation AND the '1 HOUR' speed label?"
        },
        q6={
            "title": "Question 6 (Level 2 Critiquing Image Suitability for Audience & Purpose)",
            "marks": 4,
            "stem": "A college is designing a leaflet to recruit <strong>mature adults aged 50+</strong> onto a beginner's Digital Skills &amp; Online Banking course. The draft leaflet includes two possible cover images:<br>• <strong>Image Option A:</strong> A cartoon graphic of a gaming teenager wearing neon VR goggles surrounded by binary code.<br>• <strong>Image Option B:</strong> A photograph of a smiling woman in her sixties comfortably using a tablet at a kitchen table with a cup of tea, captioned: <em>'Master everyday online banking safely at your own pace.'</em><br><br>Evaluate why <strong>Image Option B</strong> is suitable for the target audience and purpose, and why <strong>Image Option A</strong> is unsuitable.",
            "lines": 5,
            "ans_label": "Suitability Evaluation =",
            "choice_box": "Why Option B works: ____________________ | Why Option A fails: ____________________",
            "step_rows": [
                ("1. Evaluate Option B (Audience match): Shows a relatable adult in her sixties in a calm home setting, directly mirroring the 50+ target demographic", "[M1]"),
                ("2. Evaluate Option B (Purpose & Caption): The tablet and reassuring caption ('safely at your own pace') reduce tech anxiety and match the online banking topic", "[A1]"),
                ("3. Critique Option A (Audience mismatch): A teenager in neon VR gaming goggles alienates older learners and makes them feel the course is not for them", "[M1]"),
                ("4. Critique Option A (Topic mismatch): VR gaming and binary code look overly complex and intimidating rather than practical everyday banking", "[A1]")
            ],
            "final_answer": "Option B is suitable because it shows a relatable older learner in a relaxed setting with a reassuring caption ('at your own pace'). Option A is unsuitable because a teenager in VR goggles alienates 50+ adults and makes the course look intimidating and irrelevant.",
            "pitfall": "Only praising Option B without explaining why Option A fails the target audience.",
            "reverse_check": "Check that both age demographic (50+) and course subject (everyday online banking) are addressed."
        }
    ),

    # 3. Investigating Layout
    make_english_topic(
        slug="reading-investigating-layout",
        title="Layout Devices & Visual Signposting",
        category="reading",
        spec_codes="L1.14 • L2.16 • L2.17",
        golden_rule="Layout and structural devices (columns, tables, sidebars, Q&A headings, flowcharts, numbered lists) exist to organise complex information and speed up reader navigation. Always explain how a layout device helps a busy reader locate or process specific details.",
        q1={
            "title": "Question 1 (Level 1 Using Subheadings to Navigate a Document)",
            "marks": 2,
            "stem": "A community leisure centre guide is divided into four bold sections:<br><strong>Section 1: Pool &amp; Sauna Opening Hours</strong><br><strong>Section 2: Peak &amp; Off-Peak Membership Tariffs</strong><br><strong>Section 3: Crèche &amp; Junior Swim Rules</strong><br><strong>Section 4: Car Parking &amp; Bus Routes</strong><br><br>State which section a parent should read to check the minimum age for children in the pool, and explain how subheadings help readers navigate the guide.",
            "lines": 3,
            "ans_label": "Section & Navigation Benefit =",
            "choice_box": "Section: ________________ | Benefit of Subheadings: ________________",
            "step_rows": [
                ("1. Identify correct section: Section 3: Crèche & Junior Swim Rules", "[A1]"),
                ("2. Explain benefit: Subheadings divide the guide by topic so readers can scan and jump straight to the section they need without reading the whole text", "[A1]")
            ],
            "final_answer": "Section 3: Crèche & Junior Swim Rules. Subheadings allow readers to scan and go straight to their required topic without reading every word.",
            "pitfall": "Writing just 'Section 3' without explaining how subheadings aid reader navigation.",
            "reverse_check": "Does Section 3 cover children's swimming rules? Yes."
        },
        q2={
            "title": "Question 2 (Level 1 Numbered Lists vs Bullet Points)",
            "marks": 2,
            "stem": "A laboratory chemical spill card uses a <strong>bulleted list</strong> for <em>'Kit Inside the Spill Bucket (gloves, goggles, absorbent granules)'</em> and a <strong>numbered list (1, 2, 3, 4)</strong> for <em>'Emergency Clean-Up Procedure'</em>.<br><br>Explain why the writer used a <strong>numbered list</strong> for the clean-up procedure instead of ordinary bullet points.",
            "lines": 3,
            "ans_label": "Reason for Numbered List =",
            "choice_box": "Numbered list is used because: ________________________________________",
            "step_rows": [
                ("1. Chronological sequence: Numbers (1 to 4) show the exact step-by-step chronological order that must be followed", "[A1]"),
                ("2. Safety compliance: Ensures staff do not skip a step or perform emergency actions in the wrong order (unlike the non-sequential kit list)", "[A1]")
            ],
            "final_answer": "Numbers establish a strict chronological sequence (Step 1 before Step 2) so staff follow the emergency clean-up steps in the exact safe order.",
            "pitfall": "Saying 'it makes it easier to read' without mentioning chronological order or step-by-step sequence.",
            "reverse_check": "Bullet points = any order; Numbered list = strict chronological sequence."
        },
        q3={
            "title": "Question 3 (Level 1/2 Evaluating a Data Table vs Continuous Prose)",
            "marks": 3,
            "stem": "A courier company prints its parcel delivery prices in a three-column table:<br><strong>Column 1: Parcel Weight (Under 2kg / 2–10kg / Over 10kg) | Column 2: Standard 48-Hr Cost | Column 3: Express Next-Day Cost</strong>.<br><br>Explain <strong>three advantages</strong> of presenting these delivery tariffs in a table rather than a continuous paragraph of text.",
            "lines": 4,
            "ans_label": "Three Table Advantages =",
            "choice_box": "1: ________________ | 2: ________________ | 3: ________________",
            "step_rows": [
                ("1. Rapid cross-referencing: Aligns weight bands with 48-Hr and Next-Day prices in rows and columns for instant lookup", "[A1]"),
                ("2. Easy comparison: Allows customers to compare Standard vs Express prices side-by-side at a glance", "[A1]"),
                ("3. Prevents reading errors: Eliminates visual clutter so staff do not misread figures buried in dense sentences", "[A1]")
            ],
            "final_answer": "1. Aligns weights and prices in rows/columns for fast lookup. 2. Makes comparing 48-Hr vs Next-Day costs easy. 3. Reduces risk of misreading numbers in dense prose.",
            "pitfall": "Repeating the same point three times instead of giving three distinct functional benefits (speed, comparison, accuracy).",
            "reverse_check": "Check you mentioned row/column alignment, side-by-side comparison, and error reduction."
        },
        q4={
            "title": "Question 4 (Level 2 Purpose of a Dedicated Sidebar Panel)",
            "marks": 3,
            "stem": "A two-page NHS guide on managing asthma in schools is laid out with three main columns explaining inhaler types and triggers, plus a red-bordered vertical <strong>sidebar</strong> down the right-hand margin titled: <strong>'999 RED FLAG SYMPTOMS: WHEN TO CALL AN AMBULANCE'</strong>.<br><br>Analyse why the designer placed the 999 symptoms in a separate red-bordered sidebar and how this helps school staff.",
            "lines": 4,
            "ans_label": "Sidebar Analysis =",
            "choice_box": "Visual Separation: ________________ | Emergency Utility: ________________",
            "step_rows": [
                ("1. Structural separation: Physically isolates life-threatening emergency signs from the general background paragraphs on triggers", "[A1]"),
                ("2. Visual prominence: The red border and right-margin position draw the eye immediately to critical danger warnings", "[A1]"),
                ("3. Practical workplace benefit: Enables a teacher dealing with an acute asthma attack to check 999 criteria in seconds without hunting through three columns", "[A1]")
            ],
            "final_answer": "Isolates critical 999 danger signs from general background text; the red border draws immediate visual attention so teachers can verify ambulance criteria instantly during an attack.",
            "pitfall": "Summarising asthma symptoms instead of analysing the structural position and red border of the sidebar.",
            "reverse_check": "Does your answer explain both visual separation and speed of access in an emergency?"
        },
        q5={
            "title": "Question 5 (Level 2 Analysing Flowchart & Q&A Structural Devices)",
            "marks": 4,
            "stem": "An IT troubleshooting webpage for homeworkers combines two layout devices:<br>• <strong>Top Half:</strong> A <strong>decision flowchart</strong> with Yes/No arrows (<em>'Is the router power light green? &rarr; YES: Reboot VPN / NO: Check wall socket'</em>).<br>• <strong>Bottom Half:</strong> An <strong>FAQ (Frequently Asked Questions)</strong> section with bold question subheadings.<br><br>Explain how <strong>both</strong> layout devices work together to help an employee whose internet has just disconnected.",
            "lines": 5,
            "ans_label": "Flowchart & FAQ Evaluation =",
            "choice_box": "Flowchart Function: ____________________ | FAQ Function: ____________________",
            "step_rows": [
                ("1. Flowchart visual guidance: Uses Yes/No directional arrows to guide the worker step-by-step through diagnosing their router fault logically", "[M1]"),
                ("2. Flowchart efficiency: Saves time by steering the user only to the action that matches their light status (green vs off)", "[A1]"),
                ("3. FAQ navigation: Uses bold common questions as signposts so workers with specific follow-up queries can scan straight to the right answer", "[M1]"),
                ("4. Combined benefit: Makes complex technical troubleshooting accessible and stress-free for non-IT staff working alone at home", "[A1]")
            ],
            "final_answer": "The Yes/No flowchart guides workers logically through step-by-step fault diagnosis based on their router light, while the bold FAQ headings allow them to scan straight to specific follow-up answers.",
            "pitfall": "Analysing only the flowchart and ignoring the FAQ layout.",
            "reverse_check": "Verify both the Yes/No decision path (flowchart) and question scanning (FAQ) are explained."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Layout & Structure Across Two Documents)",
            "marks": 4,
            "stem": "Compare the layout of two texts about food allergens:<br><strong>Text A (Kitchen Wall Poster):</strong> Uses a single large page with a 14-icon allergen grid, bold red warning boxes, and bulleted rules.<br><strong>Text B (Food Standards Journal Article):</strong> Uses four pages of dense, two-column continuous prose paragraphs with numbered academic footnotes (¹ ²) and a bibliography at the end.<br><br>Compare how the layout of Text A and Text B is tailored to their different audiences and workplace uses.",
            "lines": 5,
            "ans_label": "Comparative Layout Evaluation =",
            "choice_box": "Text A Layout & Use: ____________________ | Text B Layout & Use: ____________________",
            "step_rows": [
                ("1. Text A layout & audience utility: Uses a 14-icon grid, red warning boxes, and bullets so busy chefs can check allergens at a glance during fast kitchen service", "[M1]"),
                ("2. Text B layout & audience utility: Uses dense multi-column prose, academic footnotes, and a bibliography suited for researchers or policy managers reading in depth", "[M1]"),
                ("3. Direct structural contrast: Whereas Text A prioritises instant visual scanning on a wall, Text B prioritises detailed scholarly citation and extended reading", "[A1]"),
                ("4. Explain footnotes in Text B: Footnotes/bibliography verify scientific sources without interrupting the formal academic narrative", "[A1]")
            ],
            "final_answer": "Text A uses an icon grid, red warning boxes, and bullets for instant wall-scanning by busy chefs. Conversely, Text B uses dense two-column prose and footnotes for in-depth study and source verification by researchers.",
            "pitfall": "Describing the topic of food allergies instead of comparing the structural layout features (icon grid/bullets vs prose columns/footnotes).",
            "reverse_check": "Have you linked Text A's layout to busy chefs and Text B's layout to researchers/in-depth study?"
        }
    ),

    # 4. Meaning
    make_english_topic(
        slug="reading-meaning",
        title="Words in Context, Synonyms & Implicit Meaning",
        category="reading",
        spec_codes="L1.9 • L1.10 • L2.10 • L2.11",
        golden_rule="Never define a word in isolation. Always read the surrounding sentence clues, match the exact part of speech (verb tense, plural noun, adjective), and plug your replacement word back into the original sentence to verify that it fits grammatically and contextually.",
        q1={
            "title": "Question 1 (Level 1 Replacing Words in Context — Grammatical Fit)",
            "marks": 2,
            "stem": "Read this sentence from a leisure centre notice:<br><em>'The swimming pool refurbishment has been <strong>postponed</strong> until November, so all current swimming lessons will continue as <strong>scheduled</strong>.'</em><br><br>Give <strong>one word or short phrase</strong> that can replace (a) <strong>'postponed'</strong> and (b) <strong>'scheduled'</strong> without changing the meaning or grammar of the sentence.",
            "lines": 3,
            "ans_label": "Replacement Words =",
            "choice_box": "(a) postponed = ____________________ | (b) scheduled = ____________________",
            "step_rows": [
                ("1. (a) Past participle matching 'postponed': delayed / put off / deferred / pushed back", "[A1]"),
                ("2. (b) Past participle/adjective matching 'scheduled': planned / arranged / timetabled", "[A1]")
            ],
            "final_answer": "(a) delayed / put off; (b) planned / arranged / timetabled.",
            "pitfall": "Writing present tense 'delay' or 'plan', which breaks the grammar ('has been delay' / 'as plan').",
            "reverse_check": "Substitute back: 'has been delayed... will continue as planned.' Grammatical fit is 100%."
        },
        q2={
            "title": "Question 2 (Level 1 Choosing the Correct Contextual Definition)",
            "marks": 2,
            "stem": "Read this sentence from a workplace appraisal report:<br><em>'The supervisor praised Nadia's <strong>acute</strong> attention to detail when spotting counterfeit £20 notes at the till.'</em><br><br>In this context, what does the word <strong>'acute'</strong> mean, and why would defining it as <em>'a sharp medical illness'</em> or <em>'an angle under 90 degrees'</em> be wrong here?",
            "lines": 3,
            "ans_label": "Contextual Meaning & Explanation =",
            "choice_box": "Meaning here: ________________ | Why other meanings fail: ________________",
            "step_rows": [
                ("1. State exact contextual meaning: Sharp, keen, perceptive, or highly observant", "[A1]"),
                ("2. Explain context match: The sentence describes Nadia's skill at spotting fake banknotes at a till, not a medical condition or geometry angle", "[A1]")
            ],
            "final_answer": "Meaning: Sharp, keen, or highly observant. Medical or geometry definitions do not fit the context of spotting counterfeit notes at a till.",
            "pitfall": "Giving a maths or medical definition of 'acute' that makes no sense when describing attention to detail.",
            "reverse_check": "'Keen/sharp attention to detail' fits the sentence seamlessly."
        },
        q3={
            "title": "Question 3 (Level 1/2 Decoding Unfamiliar Vocabulary Using Contrast Clues)",
            "marks": 3,
            "stem": "Read this extract from a company financial audit:<br><em>'Whereas the Manchester branch was <strong>frugal</strong> with its stationery budget and saved £1,200, the Leeds office was reckless and <strong>squandered</strong> thousands on luxury espresso machines.'</em><br><br>Using the contrast clues in the sentence, explain the meaning of (a) <strong>'frugal'</strong> and (b) <strong>'squandered'</strong>, and state which word in the sentence acts as the contrast signpost.",
            "lines": 4,
            "ans_label": "Definitions & Contrast Signpost =",
            "choice_box": "(a) frugal: ____________ | (b) squandered: ____________ | Signpost word: ____________",
            "step_rows": [
                ("1. (a) Define 'frugal': Careful, thrifty, economical, or cautious with money", "[A1]"),
                ("2. (b) Define 'squandered': Wasted, threw away, or spent recklessly", "[A1]"),
                ("3. Identify contrast signpost: 'Whereas' (sets up the opposite behaviour between Manchester and Leeds)", "[A1]")
            ],
            "final_answer": "(a) Frugal = thrifty/economical with money; (b) Squandered = wasted/spent recklessly; Signpost = 'Whereas'.",
            "pitfall": "Defining 'squandered' in the present tense ('waste') instead of past tense ('wasted').",
            "reverse_check": "'Saved £1,200' confirms frugal = thrifty; 'reckless' confirms squandered = wasted."
        },
        q4={
            "title": "Question 4 (Level 2 Explicit vs Implicit Meaning in a Workplace Email)",
            "marks": 3,
            "stem": "Read this email from a Project Manager to a contractor:<br><em>'It is now 4:30 p.m. on Friday. Five of the six scaffolding bays you promised to finish by noon are still lying in pieces on the lorry flatbed, and the safety inspector arrives at 8:00 a.m. on Monday.'</em><br><br>Identify <strong>one explicit fact</strong> stated in the email, and explain <strong>two implicit messages</strong> the Project Manager is communicating between the lines.",
            "lines": 4,
            "ans_label": "Explicit Fact & Two Implicit Messages =",
            "choice_box": "Explicit: ________________ | Implicit 1: ________________ | Implicit 2: ________________",
            "step_rows": [
                ("1. Explicit fact: Five of the six scaffolding bays are still on the lorry at 4:30 p.m. on Friday (or the inspector arrives at 8:00 a.m. Monday)", "[A1]"),
                ("2. Implicit message 1 (Tone/Dissatisfaction): The manager is angry/frustrated that the contractor broke their noon deadline", "[A1]"),
                ("3. Implicit message 2 (Urgent Action): The contractor must work over the weekend so the scaffolding is ready before the 8:00 a.m. Monday safety inspection", "[A1]")
            ],
            "final_answer": "Explicit: 5 of 6 bays are still unbuilt at 4:30 p.m. Friday. Implicit: 1. The manager is frustrated about the missed noon deadline. 2. The contractor must work over the weekend before Monday's 8:00 a.m. inspection.",
            "pitfall": "Repeating stated facts when asked for what is implied (suggested between the lines).",
            "reverse_check": "Explicit = printed on the page; Implicit = unstated frustration and urgent demand for weekend work."
        },
        q5={
            "title": "Question 5 (Level 2 Figurative & Idiomatic Meaning in Context)",
            "marks": 4,
            "stem": "Read this extract from a retail union article:<br><em>'Forcing shop workers to cover three tills at once is a <strong>recipe for disaster</strong>. Management cannot keep <strong>sweeping staff burnout under the carpet</strong> while turnover hits record highs.'</em><br><br>Explain in plain English what the writer means by the two bold idioms: (a) <strong>'a recipe for disaster'</strong> and (b) <strong>'sweeping staff burnout under the carpet'</strong>, and explain why the writer used idiomatic language instead of literal phrasing.",
            "lines": 5,
            "ans_label": "Idiom Meanings & Rhetorical Effect =",
            "choice_box": "(a) Meaning: ____________ | (b) Meaning: ____________ | Why used: ____________",
            "step_rows": [
                ("1. Explain (a) 'a recipe for disaster': A situation or combination of factors that is guaranteed to cause serious mistakes or problems", "[A1]"),
                ("2. Explain (b) 'sweeping staff burnout under the carpet': Deliberately hiding, ignoring, or refusing to address severe employee exhaustion", "[A1]"),
                ("3. Explain effect 1: Vivid visual metaphors make management's neglect sound deliberate and shameful", "[M1]"),
                ("4. Explain effect 2: Creates a punchy, relatable, and persuasive tone that rallies workers' support", "[A1]")
            ],
            "final_answer": "(a) Guaranteed to cause serious problems. (b) Deliberately hiding or ignoring staff exhaustion. Used to make management's neglect vivid and persuasive.",
            "pitfall": "Giving a literal explanation about cooking recipes or sweeping floors with a broom.",
            "reverse_check": "Translate both idioms into clear literal workplace English."
        },
        q6={
            "title": "Question 6 (Level 2 High-Tariff Synonym Precision Across Four Target Words)",
            "marks": 4,
            "stem": "Read this extract from a hospital estates inspection report:<br><em>'The subterranean pipework beneath Wing C has <strong>deteriorated</strong> significantly, causing <strong>intermittent</strong> heating failures. Engineers recommend an <strong>expedited</strong> replacement before winter temperatures <strong>plummet</strong>.'</em><br><br>Give <strong>one exact synonym or short phrase</strong> to replace each of the four bold words so the sentence retains its exact meaning and grammatical structure.",
            "lines": 5,
            "ans_label": "Four Grammatical Replacements =",
            "choice_box": "1. deteriorated: ________ | 2. intermittent: ________ | 3. expedited: ________ | 4. plummet: ________",
            "step_rows": [
                ("1. 'deteriorated' (past participle verb): worsened / degraded / decayed / worn down", "[A1]"),
                ("2. 'intermittent' (adjective): irregular / sporadic / on-and-off / occasional", "[A1]"),
                ("3. 'expedited' (adjective): accelerated / fast-tracked / rapid / speedy", "[A1]"),
                ("4. 'plummet' (present plural verb): plunge / drop sharply / fall rapidly", "[A1]")
            ],
            "final_answer": "1. deteriorated = worsened / degraded; 2. intermittent = irregular / sporadic; 3. expedited = fast-tracked / rapid; 4. plummet = drop sharply / plunge.",
            "pitfall": "Mismatching word class (e.g. writing 'quickly' an adverb for 'expedited' an adjective — 'an quickly replacement' is ungrammatical).",
            "reverse_check": "Plug all four back in: 'has worsened... causing irregular failures... a rapid replacement before temperatures plunge.'"
        }
    ),

    # 5. Point of View and Line of Argument
    make_english_topic(
        slug="reading-point-of-view-and-line-of-argument",
        title="Point of View, Bias & Line of Argument",
        category="reading",
        spec_codes="L1.9 • L2.11 • L2.14",
        golden_rule="A writer's Point of View is their overall stance (for, against, or balanced). Their Line of Argument is the logical chain of reasons leading to their conclusion. Bias occurs when a writer presents only one side, uses emotionally loaded words, or has a vested commercial/personal interest.",
        q1={
            "title": "Question 1 (Level 1 Identifying the Writer's Stance & Supporting Reasons)",
            "marks": 2,
            "stem": "Read this letter to a local newspaper:<br><em>'Replacing our town's weekly market with a luxury flat development is a short-sighted mistake. The market provides affordable fresh fruit for low-income families and supports 45 independent local traders.'</em><br><br>State the writer's <strong>point of view</strong> on the flat development and give the <strong>two reasons</strong> they use to support their view.",
            "lines": 3,
            "ans_label": "Stance & Supporting Reasons =",
            "choice_box": "Stance: ________________ | Reason 1: ________________ | Reason 2: ________________",
            "step_rows": [
                ("1. State writer's stance: Strongly against / opposed to replacing the weekly market with luxury flats", "[A1]"),
                ("2. Extract both supporting reasons: (1) Provides affordable fresh fruit for low-income families, and (2) supports 45 independent local traders", "[A1]")
            ],
            "final_answer": "Stance: Opposes the flat development. Reasons: 1. Market provides affordable fruit for low-income families. 2. Supports 45 local traders.",
            "pitfall": "Stating only 'the writer thinks it is a mistake' without extracting the two supporting reasons.",
            "reverse_check": "Stance (opposes) + 2 concrete reasons = 2 marks."
        },
        q2={
            "title": "Question 2 (Level 1 Distinguishing the Writer's View from an Opposing View)",
            "marks": 2,
            "stem": "Read this extract from a school governor's blog:<br><em>'Some parents argue that banning smartphones during the school day prevents them from contacting their children in an emergency. However, classroom trials prove that phone bans eliminate cyberbullying at breaktimes and boost maths test scores by 14%.'</em><br><br>Does the writer <strong>support or oppose</strong> banning smartphones in schools? Explain how the word <strong>'However'</strong> helps you know.",
            "lines": 3,
            "ans_label": "Writer's Stance & Pivot Explanation =",
            "choice_box": "Stance (Supports / Opposes): ________ | Role of 'However': ________________________",
            "step_rows": [
                ("1. Identify writer's true stance: The writer SUPPORTS banning smartphones during the school day", "[A1]"),
                ("2. Explain pivot word: The first sentence states the parents' opposing worry, and 'However' pivots to the writer's own evidence (stopping cyberbullying and boosting maths scores by 14%)", "[A1]")
            ],
            "final_answer": "Supports banning smartphones. The first sentence reports parents' concerns, while 'However' introduces the writer's own positive evidence (14% higher maths scores and no cyberbullying).",
            "pitfall": "Misreading the first sentence ('Some parents argue...') as the writer's own opinion.",
            "reverse_check": "Always look after pivot words ('However', 'In reality') to find the author's real stance."
        },
        q3={
            "title": "Question 3 (Level 2 Tracing a Three-Stage Line of Argument)",
            "marks": 3,
            "stem": "Read this extract from a logistics director's proposal:<br><em>'1. Diesel prices have risen by 22% over the past year, eroding our delivery profit margins. 2. Fitting aerodynamic roof fairings to our 30 HGV lorries costs just £400 per vehicle and cuts fuel drag by 11%. 3. Consequently, the board should approve £12,000 for fleet roof fairings this quarter.'</em><br><br>Trace how the director builds their <strong>line of argument</strong> across the three numbered sentences.",
            "lines": 4,
            "ans_label": "Three-Stage Line of Argument =",
            "choice_box": "Stage 1 (Problem): ________ | Stage 2 (Solution/Data): ________ | Stage 3 (Conclusion): ________",
            "step_rows": [
                ("1. Stage 1 (Identifies the financial problem): Rising diesel prices (up 22%) are shrinking company profit margins", "[A1]"),
                ("2. Stage 2 (Proposes a costed solution with evidence): Roof fairings cost £400 per lorry and cut fuel drag by 11%", "[A1]"),
                ("3. Stage 3 (Reaches logical conclusion/call to action): Uses 'Consequently' to urge the board to approve the £12,000 investment", "[A1]")
            ],
            "final_answer": "Stage 1 establishes the problem (22% diesel rise hurting profits); Stage 2 presents a proven solution (£400 roof fairings cutting drag by 11%); Stage 3 concludes with a £12,000 funding request.",
            "pitfall": "Just copying the sentences out instead of labelling how each stage builds the argument (Problem -> Evidence -> Conclusion).",
            "reverse_check": "Problem (22% fuel rise) -> Solution (11% drag cut) -> Conclusion (Approve £12,000)."
        },
        q4={
            "title": "Question 4 (Level 2 Detecting Loaded Language & One-Sided Bias)",
            "marks": 3,
            "stem": "Read this extract from a campaign flyer opposing a wind farm:<br><em>'Greedy energy corporations want to blight our breathtaking valley with monstrous 150-metre steel turbines that will wreck local house prices forever.'</em><br><br>Explain why this extract is <strong>biased</strong>, quoting <strong>two examples of loaded language</strong> and identifying what perspective has been left out.",
            "lines": 4,
            "ans_label": "Bias Explanation & Quotes =",
            "choice_box": "Loaded Quote 1: ____________ | Loaded Quote 2: ____________ | Omitted View: ____________",
            "step_rows": [
                ("1. Quote loaded pejorative language 1: 'Greedy energy corporations' or 'blight our breathtaking valley'", "[A1]"),
                ("2. Quote loaded hyperbole 2: 'monstrous 150-metre steel turbines' or 'wreck local house prices forever'", "[A1]"),
                ("3. Identify one-sided omission: Completely omits any environmental benefits of renewable clean wind energy or lower electricity bills", "[A1]")
            ],
            "final_answer": "Biased because it uses emotionally loaded words ('Greedy', 'blight', 'monstrous', 'wreck... forever') and presents a one-sided attack that omits the clean energy benefits of wind power.",
            "pitfall": "Calling '150-metre' biased when that is a physical height measurement; focus on 'Greedy', 'blight', and 'monstrous'.",
            "reverse_check": "2 loaded quotes + 1 explanation of omitted counter-arguments = 3 marks."
        },
        q5={
            "title": "Question 5 (Level 2 Evaluating Vested Commercial Interest & Credibility)",
            "marks": 4,
            "stem": "Read this article extract written by <strong>Marcus Vance, Managing Director of 'PureSpring Bottled Water Ltd'</strong>:<br><em>'Municipal tap water flows through century-old lead and iron pipes that taint its flavour. Drinking PureSpring mineral water is the only safe, refreshing choice for health-conscious families.'</em><br><br>Evaluate the credibility and objectivity of this argument. Refer to the <strong>author's identity</strong>, their <strong>use of language</strong>, and the <strong>evidence provided</strong>.",
            "lines": 5,
            "ans_label": "Credibility & Bias Evaluation =",
            "choice_box": "Vested Interest: ________________ | Language Analysis: ________________ | Evidence Gap: ________________",
            "step_rows": [
                ("1. Vested commercial interest: Written by the Managing Director of PureSpring Bottled Water Ltd, who profits directly from scaring people off tap water", "[M1]"),
                ("2. Scaremongering / loaded language: Uses alarmist words ('century-old lead... pipes', 'taint') to disgust readers", "[A1]"),
                ("3. Exaggerated exclusive claim: Claims PureSpring is 'the only safe, refreshing choice'", "[A1]"),
                ("4. Lack of scientific evidence: Provides zero independent water-quality test data or regulatory statistics to back up the safety claim", "[A1]")
            ],
            "final_answer": "Highly biased and low credibility: the author is the Managing Director of PureSpring Bottled Water with a financial motive to boost sales, using alarmist language ('lead... taint') and exaggerated claims ('the only safe... choice') without independent lab data.",
            "pitfall": "Failing to mention Marcus Vance's job title as Managing Director of the bottled water company.",
            "reverse_check": "Author's commercial motive + loaded quotes + lack of independent data = 4 marks."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing a Balanced Argument vs a Biased Argument)",
            "marks": 4,
            "stem": "<strong>Text A (Consumer Finance Guide):</strong><br><em>'Buy-Now-Pay-Later (BNPL) schemes allow shoppers to spread the cost of a new washing machine over three interest-free instalments. However, missed payments trigger £12 late fees and can damage your credit score.'</em><br><br><strong>Text B (PayLater App Advert):</strong><br><em>'Why wait for payday? Instant PayLater is the smartest, most stress-free way to upgrade your wardrobe today with zero catch!'</em><br><br>Analyse which text presents a <strong>balanced argument</strong> and which text is <strong>biased</strong>, using evidence from both texts.",
            "lines": 5,
            "ans_label": "Balanced vs Biased Analysis =",
            "choice_box": "Text A (Balanced): ________________________ | Text B (Biased): ________________________",
            "step_rows": [
                ("1. Classify Text A as balanced: Weighs up both the benefit (spreading cost over 3 interest-free instalments) and the risk (£12 late fees and credit score damage)", "[M1]"),
                ("2. Note Text A's measured tone: Uses the neutral connective 'However' and factual figures to let the reader decide", "[A1]"),
                ("3. Classify Text B as biased: Written by a commercial BNPL provider ('PayLater App Advert') promoting its own app", "[M1]"),
                ("4. Quote Text B's one-sided superlative claims: Uses persuasive superlatives ('smartest, most stress-free') and the false reassurance 'zero catch!' while hiding late fees", "[A1]")
            ],
            "final_answer": "Text A is balanced because it presents both pros (interest-free instalments) and cons (£12 late fees, credit score risk) in a neutral tone. Text B is biased because it is a commercial advert using superlatives ('smartest, most stress-free', 'zero catch!') while hiding debt risks.",
            "pitfall": "Not quoting the exact pros and cons from Text A that prove it is balanced.",
            "reverse_check": "Text A = pros + cons (balanced); Text B = commercial advert + 'zero catch!' (biased)."
        }
    ),

    # 6. Presentational Features
    make_english_topic(
        slug="reading-presentational-features",
        title="Presentational Features & Typographical Devices",
        category="reading",
        spec_codes="L1.14 • L2.16 • L2.17",
        golden_rule="Never confuse presentational features (visual formatting: bold, bullet points, subheadings, shaded boxes, hyperlinks) with language features (words/phrases). To score full marks, always state the feature name, what specific content it highlights, and how it helps the reader.",
        q1={
            "title": "Question 1 (Level 1 Identifying Presentational Features in a Safety Notice)",
            "marks": 2,
            "stem": "Look at this formatted extract from a workshop sign:<br><strong><u>EYE PROTECTION ZONE</u></strong><br>• Safety goggles must be worn past this line.<br>• Report scratched visors to the storeman.<br><em><strong>WARNING: Flying metal swarf can cause permanent blindness.</strong></em><br><br>Identify <strong>two presentational features</strong> used in this sign and state which words or details they highlight.",
            "lines": 3,
            "ans_label": "Two Features & Content =",
            "choice_box": "Feature 1: ________________________ | Feature 2: ________________________",
            "step_rows": [
                ("1. Feature 1: Bold, capitalised, underlined heading ('EYE PROTECTION ZONE') to announce the mandatory safety zone", "[A1]"),
                ("2. Feature 2: Bullet points (listing the two goggle rules) OR Bold/italic warning text ('WARNING: Flying metal swarf...')", "[A1]")
            ],
            "final_answer": "1. Bold underlined capitals on the heading ('EYE PROTECTION ZONE'). 2. Bullet points listing the two rules (or bold italics on the blindness warning).",
            "pitfall": "Naming 'imperative verbs' or 'emotive language' — those are language features, not presentational features!",
            "reverse_check": "Can you see bold, underlining, capitals, italics, and bullet points visually? Yes."
        },
        q2={
            "title": "Question 2 (Level 1 Explaining the Effect of a Shaded Callout Box)",
            "marks": 2,
            "stem": "A council council-tax leaflet prints a grey shaded rectangular box at the bottom of the page reading:<br><strong>STRUGGLING TO PAY? Call our confidential Hardship Team free on 0800 111 2222 (Mon–Fri, 9am–5pm).</strong><br><br>Explain why the designer placed this information inside a <strong>shaded box</strong> with <strong>bold capital letters</strong>.",
            "lines": 3,
            "ans_label": "Effect on Reader =",
            "choice_box": "Shaded box effect: ____________________ | Bold capitals effect: ____________________",
            "step_rows": [
                ("1. Shaded box effect: Visually separates the helpline number from the main body text so worried residents can find support details instantly", "[A1]"),
                ("2. Bold capitals effect: 'STRUGGLING TO PAY?' grabs the immediate attention of residents in financial difficulty", "[A1]")
            ],
            "final_answer": "The shaded box separates the free 0800 helpline number from the main text for instant lookup, while bold capitals ('STRUGGLING TO PAY?') grab the attention of residents needing help.",
            "pitfall": "Writing 'to make it stand out' without mentioning the helpline number or residents struggling to pay.",
            "reverse_check": "Always link 'stands out' to the specific content (the 0800 hardship helpline)."
        },
        q3={
            "title": "Question 3 (Level 1/2 Webpage Presentational Features)",
            "marks": 3,
            "stem": "A veterinary clinic webpage includes:<br>1. A top horizontal bar reading: <strong>[ Home ] &nbsp; [ Book a Vet ] &nbsp; [ Repeat Prescriptions ] &nbsp; [ 24hr Emergency ]</strong><br>2. Underlined blue text in the main paragraph: <em>'View our <u>2026 Vaccination Price List</u>.'</em><br>3. Customer review ratings showing: <strong>&#9733;&#9733;&#9733;&#9733;&#9733; (4.9 / 5 from 320 pet owners)</strong>.<br><br>Name each of these <strong>three webpage features</strong> and explain how each one helps a pet owner using the site.",
            "lines": 4,
            "ans_label": "Three Webpage Features & Functions =",
            "choice_box": "1: ________________ | 2: ________________ | 3: ________________",
            "step_rows": [
                ("1. Navigation bar / menu tabs: Lets pet owners click straight to key pages like '24hr Emergency' or 'Book a Vet'", "[A1]"),
                ("2. Hyperlink ('2026 Vaccination Price List'): Allows users to click directly to the price list without searching", "[A1]"),
                ("3. Star rating graphic (5 stars / 4.9): Gives instant visual reassurance that 320 pet owners trust the clinic", "[A1]")
            ],
            "final_answer": "1. Navigation menu bar (quick switching to bookings/emergencies). 2. Hyperlink (one-click access to vaccination prices). 3. Star rating (instant visual proof of high customer trust).",
            "pitfall": "Calling a hyperlink 'underlined words' without explaining that clicking it opens the price list page.",
            "reverse_check": "Menu bar + Hyperlink + Star rating = 3 distinct digital presentational features."
        },
        q4={
            "title": "Question 4 (Level 2 Analysing Pull Quotes and Straplines in Articles)",
            "marks": 3,
            "stem": "A trade magazine article is formatted with:<br>• <strong>Main Headline:</strong> <em>SOLAR ROOFS: THE BRIGHT SOLUTION FOR WAREHOUSES</em><br>• <strong>Strapline (Sub-headline underneath):</strong> <em>How three Midlands logistics depots cut their summer electricity bills by 60%.</em><br>• <strong>Boxed Pull Quote in large italics mid-page:</strong> <em>'\"Our solar panels paid for themselves in under four years!\" — Depot Director'</em>.<br><br>Explain how the <strong>strapline</strong> and the <strong>pull quote</strong> work together with the main headline to engage business readers.",
            "lines": 4,
            "ans_label": "Strapline & Pull Quote Analysis =",
            "choice_box": "Strapline role: ________________ | Pull Quote role: ________________ | Combined effect: ________________",
            "step_rows": [
                ("1. Role of strapline: Clarifies the pun in the main headline by summarizing the exact factual topic (Midlands depots cutting electricity bills by 60%)", "[A1]"),
                ("2. Role of pull quote: Breaks up the columns of text and highlights a dramatic real-world financial endorsement ('paid for themselves in under four years!')", "[A1]"),
                ("3. Combined effect on business readers: Hooks skimming warehouse managers with proven financial savings so they read the full article", "[A1]")
            ],
            "final_answer": "The strapline clarifies the headline by stating the 60% electricity saving, while the boxed pull quote breaks up the text and highlights the 4-year payback quote to persuade skimming managers to read on.",
            "pitfall": "Analysing the pun 'Bright Solution' (a language feature) instead of the functional role of the strapline and pull quote.",
            "reverse_check": "Strapline = clarifies headline topic (60% saving); Pull quote = highlights key testimonial."
        },
        q5={
            "title": "Question 5 (Level 2 Diagnosing Presentational vs Language Feature Confusion)",
            "marks": 4,
            "stem": "Read this extract from a health campaign poster:<br><strong>STOP SMOKING TODAY — PROTECT YOUR LUNGS, YOUR HEART, AND YOUR WALLET!</strong><br>• <em>Free nicotine patches delivered to your door</em><br>• <em>1-to-1 support from local NHS advisors</em><br><br>An exam candidate is asked for <strong>two presentational features</strong> and writes: <em>'1. Rule of three (lungs, heart, wallet). 2. Direct address (your).'</em><br>(a) Explain why the candidate scored <strong>0 marks</strong>. [2 Marks]<br>(b) Identify <strong>two genuine presentational features</strong> from the extract and explain their effect. [2 Marks]",
            "lines": 5,
            "ans_label": "Diagnostic & Correct Features =",
            "choice_box": "(a) Why 0 marks: ____________________ | (b) Correct Features & Effects: ____________________",
            "step_rows": [
                ("1. (a) Diagnose error: 'Rule of three' and 'Direct address' are LANGUAGE features (word/grammar choices), not visual presentational features", "[M1]"),
                ("2. (a) Clarify distinction: Presentational features must refer to visual formatting and layout on the poster", "[A1]"),
                ("3. (b) Correct Feature 1 & Effect: Bold ALL-CAPS heading ('STOP SMOKING TODAY...') visually commands attention and conveys urgency", "[A1]"),
                ("4. (b) Correct Feature 2 & Effect: Bullet points (and italics) separate the two free NHS support benefits into quick, easy-to-scan points", "[A1]")
            ],
            "final_answer": "(a) Rule of three and direct address are language features, not visual formatting. (b) 1. Bold capital letters ('STOP SMOKING TODAY') grab attention and show urgency. 2. Bullet points clearly list the free patches and 1-to-1 NHS support.",
            "pitfall": "Failing to explain the effect of the bold capitals and bullet points in part (b).",
            "reverse_check": "Language = words; Presentational = bold capitals, bullet points, italics."
        },
        q6={
            "title": "Question 6 (Level 2 Evaluating How Multiple Presentational Features Support Purpose)",
            "marks": 4,
            "stem": "A food allergy product recall notice in a supermarket uses:<br>1. A <strong>thick red-and-white striped hazard border</strong> around the edge of the poster<br>2. A <strong>colour photograph</strong> of the exact <em>'Crunchy Oat Granola 500g'</em> packet<br>3. <strong>Bold underlined text</strong> on the batch code: <strong><u>Batch Code: L4492 — Best Before: Oct 2026</u></strong><br>4. A <strong>shaded green footer box</strong> stating: <em>'Return to any customer service desk for a full £3.20 cash refund (no receipt needed).'</em><br><br>Evaluate how these four presentational features work together to achieve the notice's purpose.",
            "lines": 5,
            "ans_label": "Comprehensive Evaluation =",
            "choice_box": "1. Border: ________ | 2. Photo: ________ | 3. Bold/Underline: ________ | 4. Green Box: ________",
            "step_rows": [
                ("1. Red-and-white hazard border: Immediately signals an urgent safety alert to passing shoppers", "[A1]"),
                ("2. Product photograph: Allows customers to visually recognise the 'Crunchy Oat Granola' box in their kitchen cupboard instantly", "[A1]"),
                ("3. Bold underlined batch code: Draws the eye to the exact batch ('L4492') and date so shoppers can verify if their packet is affected", "[A1]"),
                ("4. Shaded green footer box: Separates the reassuring action step (getting a full £3.20 refund with no receipt)", "[A1]")
            ],
            "final_answer": "1. Hazard border grabs attention for a safety alert. 2. Photo helps shoppers recognise the granola box. 3. Bold underlining highlights Batch Code L4492 for checking. 4. Green box separates the £3.20 refund instructions.",
            "pitfall": "Listing the four features without linking each one to how a shopper uses it (spotting alert -> recognising packet -> checking batch -> claiming refund).",
            "reverse_check": "All 4 features explained with specific content links = 4 marks."
        }
    ),

    # 7. Specialist Words
    make_english_topic(
        slug="reading-specialist-words",
        title="Specialist, Technical & Vocational Vocabulary",
        category="reading",
        spec_codes="L1.11 • L2.10 • L2.16",
        golden_rule="When decoding specialist vocabulary or acronyms, first check for in-text definitions inside brackets ( ), dashes — —, or footnotes (*). If none are present, break compound technical words into prefixes and roots (e.g. 'hyper-' = high, 'mal-' = faulty, 'cardio-' = heart) and use the workplace context.",
        q1={
            "title": "Question 1 (Level 1 Extracting In-Text Definitions of Acronyms & Jargon)",
            "marks": 2,
            "stem": "Read this extract from a construction site induction sheet:<br><em>'All electrical subcontractors must hold a valid <strong>CSCS</strong> (Construction Skills Certification Scheme) smartcard and use <strong>PAT-tested</strong> — Portable Appliance Tested — power tools on site.'</em><br><br>Using the punctuation clues in the extract, state what the acronyms (a) <strong>CSCS</strong> and (b) <strong>PAT</strong> stand for.",
            "lines": 3,
            "ans_label": "Expanded Acronyms =",
            "choice_box": "(a) CSCS: ____________________________ | (b) PAT: ____________________________",
            "step_rows": [
                ("1. (a) Extract expansion from brackets ( ): Construction Skills Certification Scheme", "[A1]"),
                ("2. (b) Extract expansion from parenthetical dashes — —: Portable Appliance Tested", "[A1]")
            ],
            "final_answer": "(a) Construction Skills Certification Scheme; (b) Portable Appliance Tested.",
            "pitfall": "Guessing what CSCS or PAT stands for instead of copying the exact words inside the brackets and dashes.",
            "reverse_check": "Brackets and double dashes immediately after an acronym almost always contain its full expansion."
        },
        q2={
            "title": "Question 2 (Level 1 Defining Healthcare Specialist Vocabulary from Context)",
            "marks": 2,
            "stem": "Read this extract from a community nursing handover note:<br><em>'Mr Evans has been discharged following <strong>acute</strong> bronchitis; however, his wife requires ongoing support to manage her <strong>chronic</strong> arthritis.'</em><br><br>In medical and care contexts, explain the difference between an <strong>'acute'</strong> condition and a <strong>'chronic'</strong> condition.",
            "lines": 3,
            "ans_label": "Medical Definitions =",
            "choice_box": "Acute condition: ____________________ | Chronic condition: ____________________",
            "step_rows": [
                ("1. Define 'acute': A condition that comes on suddenly and lasts a short/limited time (often severe)", "[A1]"),
                ("2. Define 'chronic': A long-term, persistent, or ongoing medical condition that lasts for months or years", "[A1]")
            ],
            "final_answer": "Acute = sudden onset and short-term; Chronic = long-lasting, ongoing condition requiring long-term management.",
            "pitfall": "Thinking 'chronic' just means 'really bad pain' rather than 'long-term/ongoing'.",
            "reverse_check": "Notice the clue 'ongoing support' next to 'chronic arthritis'!"
        },
        q3={
            "title": "Question 3 (Level 1/2 Decoding Compound Words Using Prefixes & Roots)",
            "marks": 3,
            "stem": "Read this extract from an outdoor adventure centre safety manual:<br><em>'Kayaking instructors must carry thermal foil blankets to treat <strong>hypothermia</strong>, check lifejackets for strap <strong>malfunctions</strong>, and ensure all sunscreen provided is <strong>hypoallergenic</strong>.'</em><br><br>Break down and explain the meaning of the three bold specialist terms in this context.",
            "lines": 4,
            "ans_label": "Three Technical Definitions =",
            "choice_box": "1. hypothermia: ____________ | 2. malfunctions: ____________ | 3. hypoallergenic: ____________",
            "step_rows": [
                ("1. Define 'hypothermia' (hypo = low + therm = heat): Dangerously low body temperature caused by cold/wet exposure", "[A1]"),
                ("2. Define 'malfunctions' (mal = bad/faulty + function = working): Faults, breakdowns, or failures to work properly", "[A1]"),
                ("3. Define 'hypoallergenic' (hypo = low/less + allergen): Formulated to be unlikely to cause an allergic skin reaction", "[A1]")
            ],
            "final_answer": "1. Hypothermia = dangerously low body temperature; 2. Malfunctions = faults/failures to work properly; 3. Hypoallergenic = unlikely to cause an allergic reaction.",
            "pitfall": "Confusing 'hypothermia' (too cold) with 'hyperthermia' (overheating).",
            "reverse_check": "Clue: 'thermal foil blankets' confirms hypothermia is dangerously low body heat."
        },
        q4={
            "title": "Question 4 (Level 2 Financial & Administrative Jargon in Workplace Reports)",
            "marks": 3,
            "stem": "Read this extract from a charity treasurer's annual report:<br><em>'Due to a £14,000 budget <strong>deficit</strong> in Quarter 3, the trustees have placed a temporary <strong>moratorium</strong> on hiring new staff and tightened <strong>procurement</strong> rules for office equipment.'</em><br><br>Explain the meaning of (a) <strong>'deficit'</strong>, (b) <strong>'moratorium'</strong>, and (c) <strong>'procurement'</strong> in plain English.",
            "lines": 4,
            "ans_label": "Plain-English Definitions =",
            "choice_box": "(a) deficit: ____________ | (b) moratorium: ____________ | (c) procurement: ____________",
            "step_rows": [
                ("1. (a) 'deficit': A financial shortfall where spending exceeds income", "[A1]"),
                ("2. (b) 'moratorium': A temporary ban, freeze, or suspension on an activity (hiring freeze)", "[A1]"),
                ("3. (c) 'procurement': The process of buying, purchasing, or acquiring goods and equipment for an organisation", "[A1]")
            ],
            "final_answer": "(a) Deficit = financial shortfall/loss; (b) Moratorium = temporary freeze/ban; (c) Procurement = purchasing/buying supplies.",
            "pitfall": "Confusing 'deficit' (shortfall) with 'surplus' (extra profit).",
            "reverse_check": "Because there is a £14,000 shortfall (deficit), they froze hiring (moratorium) and tightened buying rules (procurement)."
        },
        q5={
            "title": "Question 5 (Level 2 Explaining WHY Writers Use Specialist Jargon)",
            "marks": 4,
            "stem": "Read this extract from an aviation maintenance log:<br><em>'Inspection of the port hydraulic actuator revealed micro-fissures in the titanium seal housing; the component was quarantined in accordance with CAA Airworthiness Directive 2026-09.'</em><br><br>(a) Explain the meaning of <strong>'micro-fissures'</strong> and <strong>'quarantined'</strong> in this context. [2 Marks]<br>(b) Give <strong>two reasons</strong> why the engineer used dense technical terminology rather than everyday informal language. [2 Marks]",
            "lines": 5,
            "ans_label": "Definitions & Register Purpose =",
            "choice_box": "(a) Meanings: ________________________ | (b) Two Reasons for Jargon: ________________________",
            "step_rows": [
                ("1. (a) 'micro-fissures': Tiny / microscopic cracks or splits in the metal housing", "[A1]"),
                ("2. (a) 'quarantined': Isolated and locked away safely so the faulty part cannot be accidentally fitted to an aircraft", "[A1]"),
                ("3. (b) Reason 1 (Precision & Safety): Delivers exact, unambiguous engineering precision so other licensed mechanics know the exact part and fault", "[M1]"),
                ("4. (b) Reason 2 (Regulatory Authority & Audience): Demonstrates legal compliance with CAA aviation safety rules for a specialist audience of inspectors", "[A1]")
            ],
            "final_answer": "(a) Micro-fissures = tiny cracks; Quarantined = isolated so the faulty part cannot be used. (b) 1. Provides exact technical precision to prevent aviation errors. 2. Meets legal regulatory standards for specialist engineers.",
            "pitfall": "Defining 'quarantined' as 'kept away because of a contagious medical virus' instead of isolating a faulty mechanical part.",
            "reverse_check": "Check that 'quarantined' is explained in the mechanical engineering context."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Specialist vs Accessible Language Across Two Texts)",
            "marks": 4,
            "stem": "Read two texts about high blood pressure:<br><strong>Text A (Medical Journal for GPs):</strong> <em>'Patients presenting with persistent stage-2 hypertension (&ge;160/100 mmHg) require antihypertensive pharmacotherapy to reduce myocardial infarction incidence.'</em><br><strong>Text B (Waiting Room Patient Poster):</strong> <em>'High blood pressure often has no warning signs, which is why doctors call it the silent killer. Taking your daily blood pressure tablets protects you from heart attacks.'</em><br><br>Compare how Text A and Text B use vocabulary differently, and explain why each style suits its target audience.",
            "lines": 5,
            "ans_label": "Comparative Vocabulary Analysis =",
            "choice_box": "Text A Vocabulary & Audience: ____________ | Text B Vocabulary & Audience: ____________",
            "step_rows": [
                ("1. Text A vocabulary & quote: Uses dense clinical Latinate jargon ('stage-2 hypertension', 'antihypertensive pharmacotherapy', 'myocardial infarction')", "[M1]"),
                ("2. Text A audience link: Tailored to trained GPs who need exact clinical diagnostic thresholds ('>=160/100 mmHg')", "[A1]"),
                ("3. Text B vocabulary & quote: Translates the exact same concepts into plain everyday English ('High blood pressure', 'daily... tablets', 'heart attacks') and a memorable metaphor ('the silent killer')", "[M1]"),
                ("4. Text B audience link: Tailored to non-specialist patients in a waiting room so they understand the risk easily and take their medication", "[A1]")
            ],
            "final_answer": "Text A uses clinical terminology ('hypertension', 'pharmacotherapy', 'myocardial infarction') for GPs who need diagnostic precision. In contrast, Text B uses plain English ('High blood pressure', 'tablets', 'heart attacks') and the metaphor 'silent killer' so general patients easily understand the importance of taking their pills.",
            "pitfall": "Not matching the equivalent terms across the two texts (e.g. 'myocardial infarction' in Text A = 'heart attacks' in Text B).",
            "reverse_check": "Notice how Text B translates every specialist term from Text A into everyday patient language!"
        }
    ),

    # 8. Styles of Writing and Voice
    make_english_topic(
        slug="reading-styles-of-writing-and-voice",
        title="Tone, Style, Register & Writer's Voice",
        category="reading",
        spec_codes="L1.15 • L2.15 • L2.16",
        golden_rule="Tone is the writer's emotional attitude (e.g. reassuring, urgent, apologetic, critical, sarcastic, authoritative). Style and Register refer to the level of formality, sentence length, and active vs passive voice. Never describe tone simply as 'good' or 'bad' — always use a precise adjective backed by a quote.",
        q1={
            "title": "Question 1 (Level 1 Identifying Tone in Workplace Communications)",
            "marks": 2,
            "stem": "Match the two extracts to their exact tone:<br><strong>Extract A (Maternity Ward Guide):</strong> <em>'Please do not worry if your newborn cries frequently during the first night; our experienced midwives are right next door at the touch of a button to help you settle your baby.'</em><br><strong>Extract B (Site Manager Memo):</strong> <em>'Any operative caught tampering with scaffolding safety tags will face immediate disciplinary dismissal and permanent removal from site.'</em><br><br>Choose from: <strong>Humorous &nbsp;|&nbsp; Reassuring &amp; Supportive &nbsp;|&nbsp; Stern &amp; Authoritative &nbsp;|&nbsp; Apologetic</strong>, and quote two words from each extract that prove your choice.",
            "lines": 3,
            "ans_label": "Matched Tones & Quotes =",
            "choice_box": "Extract A: ________________ (Quote: ________) | Extract B: ________________ (Quote: ________)",
            "step_rows": [
                ("1. Extract A: Reassuring & Supportive — proved by 'Please do not worry' / 'experienced midwives... to help you'", "[A1]"),
                ("2. Extract B: Stern & Authoritative — proved by 'immediate disciplinary dismissal' / 'permanent removal'", "[A1]")
            ],
            "final_answer": "Extract A: Reassuring & Supportive ('do not worry', 'help you'); Extract B: Stern & Authoritative ('immediate disciplinary dismissal').",
            "pitfall": "Selecting the right tone label without copying the supporting words from each extract.",
            "reverse_check": "Extract A calms anxious parents; Extract B enforces strict site discipline."
        },
        q2={
            "title": "Question 2 (Level 1 Conversational vs Formal Style)",
            "marks": 2,
            "stem": "Read this extract from a staff health newsletter:<br><em>'Fed up with paying £5 for a soggy supermarket sandwich? Why not batch-cook a delicious pot of chilli on Sunday night — your tastebuds (and your bank balance!) will love you for it.'</em><br><br>Identify the <strong>style/register</strong> of this extract and give <strong>two features</strong> from the text that create this style.",
            "lines": 3,
            "ans_label": "Style & Two Features =",
            "choice_box": "Style: ________________ | Feature 1: ________________ | Feature 2: ________________",
            "step_rows": [
                ("1. Identify style: Informal, conversational, chatty, and friendly", "[A1]"),
                ("2. Give two features: Colloquial opening question ('Fed up with... soggy supermarket sandwich?'), parenthetical aside with exclamation mark ('(and your bank balance!)'), or direct address ('your tastebuds')", "[A1]")
            ],
            "final_answer": "Style: Informal / conversational / friendly. Features: 1. Chatty questions ('Fed up with...?', 'Why not...?'). 2. Friendly aside and exclamation mark ('(and your bank balance!)').",
            "pitfall": "Saying the style is 'persuasive' (which is purpose) without stating that the register is 'informal/conversational'.",
            "reverse_check": "'Fed up with' and 'soggy' are classic informal conversational choices."
        },
        q3={
            "title": "Question 3 (Level 1/2 Analysing an Apologetic & Conciliatory Tone)",
            "marks": 3,
            "stem": "Read this letter from a broadband director to customers:<br><em>'We sincerely apologise for the unacceptable four-hour network outage across North Oxfordshire yesterday afternoon. We fully understand how disruptive this was for homeworkers, and we have automatically credited £15 to your next bill as a gesture of goodwill.'</em><br><br>Describe the <strong>tone</strong> of this extract [1 Mark], quote <strong>two phrases</strong> that create it [1 Mark], and explain why the writer chose this tone [1 Mark].",
            "lines": 4,
            "ans_label": "Tone, Quotes & Purpose =",
            "choice_box": "Tone: ____________ | Quotes: ________________ | Why chosen: ________________",
            "step_rows": [
                ("1. Describe tone: Apologetic, empathetic, polite, and professional", "[A1]"),
                ("2. Quote two phrases: 'sincerely apologise' / 'unacceptable four-hour network outage' / 'gesture of goodwill'", "[A1]"),
                ("3. Explain why chosen: Calms angry customers by taking full responsibility for the outage and offering automatic £15 compensation so they do not cancel their contract", "[A1]")
            ],
            "final_answer": "Tone: Apologetic, empathetic, and professional. Quotes: 'sincerely apologise' and 'gesture of goodwill'. Chosen to defuse customer anger and retain their loyalty after the outage.",
            "pitfall": "Describing the tone as 'sad' instead of the professional term 'apologetic / conciliatory'.",
            "reverse_check": "Tone label + 2 quotes + customer retention explanation = 3 marks."
        },
        q4={
            "title": "Question 4 (Level 2 Active vs Passive Voice & Sentence Pace)",
            "marks": 3,
            "stem": "Compare the style of these two workplace sentences:<br><strong>Sentence 1 (Accident Investigation Report):</strong> <em>'The warehouse fire alarm was triggered at 14:22, and the building was evacuated within three minutes.'</em><br><strong>Sentence 2 (Fire Warden Training Poster):</strong> <em>'Smash the glass! Sound the siren! Get everyone out now!'</em><br><br>Explain how the grammar and sentence length differ between Sentence 1 and Sentence 2, and how this affects the voice of each text.",
            "lines": 4,
            "ans_label": "Grammar & Pace Analysis =",
            "choice_box": "Sentence 1 Style & Effect: ____________________ | Sentence 2 Style & Effect: ____________________",
            "step_rows": [
                ("1. Sentence 1 grammar & voice: Uses the passive voice ('was triggered', 'was evacuated') and a longer compound structure to create a calm, detached, objective clinical voice", "[A1]"),
                ("2. Sentence 2 grammar & voice: Uses short, three-word imperative commands ('Smash', 'Sound', 'Get') and exclamation marks", "[A1]"),
                ("3. Contrast effect on pace: Sentence 1 sounds like an official factual record after the event, whereas Sentence 2 creates a fast, urgent, commanding pace for an active emergency", "[A1]")
            ],
            "final_answer": "Sentence 1 uses passive verbs ('was triggered', 'was evacuated') for a calm, detached, objective audit style. Sentence 2 uses short three-word imperatives and exclamation marks ('Smash the glass!') to create an urgent, commanding pace.",
            "pitfall": "Not naming 'passive voice' in Sentence 1 or 'short imperative sentences' in Sentence 2.",
            "reverse_check": "'was triggered' = passive voice; 'Smash the glass!' = short active imperative."
        },
        q5={
            "title": "Question 5 (Level 2 Detecting Sarcasm, Irony & Critical Voice)",
            "marks": 4,
            "stem": "Read this extract from a resident's column in a town newsletter:<br><em>'Congratulations to our brilliant council planners! Spending £800,000 on a \"smart\" traffic-light junction that has doubled morning tailbacks to three miles is truly a masterclass in modern engineering. Clearly, none of the committee ever drive to work at 8 a.m.'</em><br><br>Analyse the writer's <strong>tone and voice</strong> in this extract. Explain how the writer uses words and punctuation to convey their true attitude.",
            "lines": 5,
            "ans_label": "Sarcasm & Tone Analysis =",
            "choice_box": "True Tone: ____________ | Verbal Irony Quotes: ____________ | Punctuation Clues: ____________",
            "step_rows": [
                ("1. Identify true tone: Heavily sarcastic, ironic, bitter, and mocking (NOT genuinely praising the council)", "[M1]"),
                ("2. Analyse verbal irony quotes: Uses mock praise ('Congratulations to our brilliant council planners!', 'truly a masterclass') to mean the exact opposite because the £800,000 lights doubled tailbacks", "[M1]"),
                ("3. Analyse punctuation clues: Inverted commas (scare quotes) around '\"smart\"' mock the council's claim that the lights are intelligent", "[A1]"),
                ("4. Analyse closing remark: 'Clearly, none of the committee ever drive to work at 8 a.m.' delivers a biting criticism that councillors are out of touch", "[A1]")
            ],
            "final_answer": "The tone is sarcastic and mocking. The writer uses ironic praise ('brilliant council planners!', 'truly a masterclass') and scare quotes around '\"smart\"' to ridicule the £800,000 junction for doubling tailbacks to three miles.",
            "pitfall": "Taking the opening sentence literally and claiming the writer is 'happy and praising the council'.",
            "reverse_check": "Doubling tailbacks to three miles proves 'brilliant' and 'masterclass' are sarcastic!"
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Style, Voice & Register Across Two Texts)",
            "marks": 4,
            "stem": "<strong>Text A (Statutory Redundancy Notice):</strong><br><em>'Pursuant to Section 188 of the Trade Union and Labour Relations Act, formal consultation regarding the proposed closure of the Swindon packaging plant will commence on 1st November.'</em><br><br><strong>Text B (Plant Worker's Open Letter):</strong><br><em>'After twenty years of loyal service, we found out our factory is shutting down from a cold, heartless piece of paper pinned to the canteen wall. What happens to our families now?'</em><br><br>Compare the <strong>style, tone, and voice</strong> of Text A and Text B, supporting your analysis with quotations.",
            "lines": 5,
            "ans_label": "Comparative Voice Analysis =",
            "choice_box": "Text A Style/Voice: ____________________ | Text B Style/Voice: ____________________",
            "step_rows": [
                ("1. Text A style & tone: Highly formal, legalistic, impersonal, and detached corporate tone", "[M1]"),
                ("2. Text A evidence: Uses legal citations ('Pursuant to Section 188...') and formal Latinate verbs ('commence') with zero personal pronouns", "[A1]"),
                ("3. Text B style & tone: Deeply personal, emotional, betrayed, and anguished first-person plural voice ('we', 'our families')", "[M1]"),
                ("4. Text B evidence: Uses emotive adjectives ('loyal service', 'cold, heartless piece of paper') and a desperate rhetorical question ('What happens to our families now?')", "[A1]")
            ],
            "final_answer": "Text A adopts a cold, formal, legalistic voice ('Pursuant to Section 188', 'commence') with impersonal detachment. In contrast, Text B uses an emotional, betrayed first-person voice ('our families'), emotive adjectives ('cold, heartless'), and a rhetorical question to express workers' distress.",
            "pitfall": "Comparing only the topic (plant closure) instead of contrasting the legalistic detachment of Text A with the emotional first-person voice of Text B.",
            "reverse_check": "Check you quoted from both texts and contrasted legal formality vs personal emotion."
        }
    ),

    # 9. Text Types
    make_english_topic(
        slug="reading-text-types",
        title="Text Types, Genre Conventions & Target Audience",
        category="reading",
        spec_codes="L1.16 • L2.16 • L2.17",
        golden_rule="Identify any text type by combining its visual format conventions (e.g. addresses/salutations for letters; numbered findings/recommendations for reports; user handles/timestamps for forums) with its primary purpose and specific target audience.",
        q1={
            "title": "Question 1 (Level 1 Identifying Text Genres from Structural Fingerprints)",
            "marks": 2,
            "stem": "Identify the exact <strong>text type (genre)</strong> of each extract below from its formatting clues:<br><strong>Extract A:</strong> <em>'Thread: Best cordless combi drill under £120? | Posted by @ChippyPete (Yesterday at 19:14) [Reply] [Like (12)]'</em><br><strong>Extract B:</strong> <em>'14 Oak Lane, Bristol | 12 October 2026 | Dear Mr Henderson, Re: Boundary Wall Repair Quote... Yours sincerely, A. Kowalski'</em>",
            "lines": 3,
            "ans_label": "Identified Genres =",
            "choice_box": "Extract A Genre: ____________________ | Extract B Genre: ____________________",
            "step_rows": [
                ("1. Extract A: Online discussion forum / message board thread (confirmed by 'Thread:', '@ChippyPete', timestamp, and '[Reply] [Like]' buttons)", "[A1]"),
                ("2. Extract B: Formal business letter (confirmed by postal address, date, 'Dear Mr Henderson', 'Re:' line, and 'Yours sincerely')", "[A1]")
            ],
            "final_answer": "Extract A: Online discussion forum thread; Extract B: Formal business letter.",
            "pitfall": "Calling Extract A 'an email' or 'a blog' when it has a thread title, username handle, and Reply/Like buttons.",
            "reverse_check": "Forum = Thread + @username + Reply; Formal letter = Address + Dear Mr X + Yours sincerely."
        },
        q2={
            "title": "Question 2 (Level 1 Pinpointing the Specific Target Audience)",
            "marks": 2,
            "stem": "Read this extract from a community leaflet:<br><em>'Are you aged 60 or over and finding your garden lawn too heavy to mow? Our vetted volunteer gardeners offer free fortnightly grass cutting for retired householders across the borough.'</em><br><br>Identify the <strong>specific target audience</strong> for this leaflet and give <strong>two clues</strong> from the text that prove it.",
            "lines": 3,
            "ans_label": "Target Audience & Clues =",
            "choice_box": "Target Audience: ________________ | Clue 1: ________________ | Clue 2: ________________",
            "step_rows": [
                ("1. Define specific target audience: Retired householders / older residents aged 60 or over who have a garden and struggle with mowing", "[A1]"),
                ("2. Extract two textual clues: 'aged 60 or over' and 'retired householders across the borough' (or 'finding your garden lawn too heavy to mow')", "[A1]")
            ],
            "final_answer": "Target audience: Retired homeowners/residents aged 60+ who struggle to mow their lawn. Clues: 'aged 60 or over' and 'retired householders'.",
            "pitfall": "Writing a vague answer like 'everyone in the borough' or 'people who like gardening'.",
            "reverse_check": "Always include age/role specifics ('retired householders aged 60+') when given in the text."
        },
        q3={
            "title": "Question 3 (Level 1/2 Distinguishing Formal Reports from Magazine Articles)",
            "marks": 3,
            "stem": "Look at the structural features of two workplace documents:<br><strong>Document 1:</strong> Titled <em>'Q3 Warehouse Forklift Incident Investigation'</em>, divided into <strong>1.0 Executive Summary, 2.0 Audit Findings, 3.0 Cost Breakdown Table, 4.0 Mandatory Recommendations</strong>.<br><strong>Document 2:</strong> Headlined <em>'Forklift Futures: Why AI Sensors Are Taking Over the Aisle!'</em> by Sarah Jenkins, featuring a catchy strapline, two-column prose, and a boxed pull quote.<br><br>Identify the genre of Document 1 and Document 2, and explain how their purposes differ.",
            "lines": 4,
            "ans_label": "Genres & Contrasting Purposes =",
            "choice_box": "Doc 1 Genre: ____________ | Doc 2 Genre: ____________ | Purpose Difference: ________________",
            "step_rows": [
                ("1. Document 1 genre: Formal workplace investigation report (numbered sections 1.0–4.0, Findings, Recommendations)", "[A1]"),
                ("2. Document 2 genre: Trade magazine / newspaper feature article (punny headline, byline, columns, pull quote)", "[A1]"),
                ("3. Contrast purposes: Document 1 aims to objectively investigate warehouse accidents and mandate safety actions for management, whereas Document 2 aims to engage and inform industry readers about new AI forklift trends", "[A1]")
            ],
            "final_answer": "Doc 1: Formal workplace report (to investigate incidents and recommend actions for managers). Doc 2: Magazine article (to engage and inform readers about new AI forklift technology).",
            "pitfall": "Calling both documents 'articles' when Document 1 has numbered Executive Summary, Findings, and Recommendations.",
            "reverse_check": "Findings + Recommendations = Report; Headline + Byline + Pull Quote = Article."
        },
        q4={
            "title": "Question 4 (Level 2 Analysing Standard Operating Procedures / Instructional Texts)",
            "marks": 3,
            "stem": "Read this extract from a dental surgery wall card:<br><strong>AUTOCLAVE STERILISATION PROTOCOL (SOP-12)</strong><br><em><strong>Warning:</strong> Wear heat-resistant gauntlets.<br>1. Load unwrapped steel instruments onto perforated trays.<br>2. Select Cycle B (134°C at 2.1 bar pressure for 3 minutes).<br>3. Sign and staple the printout strip to the daily clinical logbook.</em><br><br>Identify the <strong>text type</strong>, state its <strong>exact purpose</strong>, and explain why it is unsuitable for a general patient waiting room.",
            "lines": 4,
            "ans_label": "Genre, Purpose & Audience Suitability =",
            "choice_box": "Text Type: ____________ | Purpose: ____________ | Why unsuitable for patients: ____________",
            "step_rows": [
                ("1. Identify text type: Standard Operating Procedure (SOP) / technical instruction manual", "[A1]"),
                ("2. State exact purpose: To instruct dental staff step-by-step on how to sterilise surgical instruments safely and legally in the autoclave", "[A1]"),
                ("3. Explain audience unsuitability: Uses specialist technical specifications ('134°C at 2.1 bar', 'Cycle B') and imperative staff duties that only trained dental nurses/technicians perform, not patients", "[A1]")
            ],
            "final_answer": "Text Type: Standard Operating Procedure (SOP) / instruction card. Purpose: To instruct dental staff on sterilising instruments safely. Unsuitable for patients because it contains technical operating steps ('134°C at 2.1 bar') meant only for trained clinical staff.",
            "pitfall": "Stating the purpose as simply 'to instruct' without mentioning sterilising dental instruments.",
            "reverse_check": "Check that all three parts (Genre, Purpose with topic, Audience reason) are answered."
        },
        q5={
            "title": "Question 5 (Level 2 Evaluating Dual-Purpose Texts)",
            "marks": 4,
            "stem": "Read this extract from a leaflet sent to householders by 'GreenHome Insulation Ltd':<br><em>'Did you know that 35% of your home's heat escapes straight through an uninsulated loft? Under the 2026 Great British Insulation Scheme, homes in Council Tax Bands A–D qualify for up to £1,500 towards mineral wool loft lagging. Do not shiver through another expensive winter — book your free 20-minute roof survey at greenhome.co.uk before 30th November!'</em><br><br>Analyse how this text operates as a <strong>dual-purpose text</strong>, quoting evidence for <strong>both</strong> purposes.",
            "lines": 5,
            "ans_label": "Dual-Purpose Analysis =",
            "choice_box": "Purpose 1 (Inform) & Quote: ________________ | Purpose 2 (Persuade/Promote) & Quote: ________________",
            "step_rows": [
                ("1. Identify Purpose 1 (To Inform): Informs householders about heat loss facts and government grant eligibility rules", "[M1]"),
                ("2. Quote evidence for Purpose 1: '35% of your home's heat escapes' and 'Council Tax Bands A–D qualify for up to £1,500'", "[A1]"),
                ("3. Identify Purpose 2 (To Persuade / Promote commercially): Persuades homeowners to book a survey with GreenHome Insulation Ltd before the deadline", "[M1]"),
                ("4. Quote evidence for Purpose 2: Rhetorical question ('Did you know...?'), emotive command ('Do not shiver through another expensive winter'), and call to action ('book your free 20-minute roof survey... before 30th November!')", "[A1]")
            ],
            "final_answer": "Dual purpose: 1. To inform householders about loft heat loss ('35%') and £1,500 grant eligibility ('Council Tax Bands A–D'). 2. To persuade them to book a commercial survey with GreenHome Insulation Ltd ('Do not shiver... book your free 20-minute roof survey').",
            "pitfall": "Identifying only the informative grant details and missing the commercial persuasive pitch at the end.",
            "reverse_check": "Both purposes (Inform + Persuade) must be named and backed by direct quotes."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Genre Conventions Across Three Extracts)",
            "marks": 4,
            "stem": "Read three short texts about a train strike:<br><strong>Text A (Rail Operator SMS Alert):</strong> <em>'ALERT: Strike action Weds 18 Nov. Zero trains on North Line. Claim full refund at rail.co.uk/refunds.'</em><br><strong>Text B (Union Press Release):</strong> <em>'Signallers have been forced into industrial action after management refused to address dangerous lone-working rosters.'</em><br><strong>Text C (Travel Advice Guide):</strong> <em>'If you must travel on Wednesday, consider booking an intercity coach early or car-sharing with colleagues.'</em><br><br>Identify the <strong>text type and primary purpose</strong> of Text A, Text B, and Text C, and explain why Text A uses fragmented sentences.",
            "lines": 5,
            "ans_label": "Three-Text Genre & Purpose Breakdown =",
            "choice_box": "Text A: ____________ | Text B: ____________ | Text C: ____________ | Why Text A is short: ____________",
            "step_rows": [
                ("1. Text A genre & purpose: Automated SMS/text alert — to inform passengers urgently of the 18 Nov line closure and how to claim a refund", "[A1]"),
                ("2. Text B genre & purpose: Union press release / statement — to justify the strike and persuade the public to blame management's safety record", "[A1]"),
                ("3. Text C genre & purpose: Commuter travel advice guide — to advise passengers on practical alternative travel options (coaches/car-sharing)", "[A1]"),
                ("4. Explain Text A's fragmented style: Mobile SMS alerts have strict character limits and must deliver critical cancellation facts instantly on a phone screen", "[A1]")
            ],
            "final_answer": "Text A: SMS alert to inform urgently of line closure/refunds (uses short fragments for instant mobile reading). Text B: Union press release to justify the strike and persuade the public. Text C: Travel guide to advise commuters on alternative transport.",
            "pitfall": "Forgetting to answer the final part explaining why Text A uses short fragmented sentences.",
            "reverse_check": "Text A = Inform (SMS); Text B = Persuade/Justify (Press release); Text C = Advise (Guide)."
        }
    ),

    # 10. The Exam
    make_english_topic(
        slug="reading-the-exam",
        title="Reading Exam Strategy, Command Words & Verification",
        category="reading",
        spec_codes="L1.9–L1.16 • L2.10–L2.18",
        golden_rule="Read the question stem FIRST before reading the passage. Underline the target text ('Using Text A...'), the command verb ('Identify', 'Replace', 'Explain', 'Compare'), any exclusion traps ('Apart from...'), and the mark tariff (1 mark = 1 point; 3 marks = 3 distinct points or Name + Quote + Effect).",
        q1={
            "title": "Question 1 (Level 1 Avoiding the 'Apart From' Exclusion Trap)",
            "marks": 2,
            "stem": "Read this extract from Text A (Allotment Rules):<br><em>'Plot holders are strictly prohibited from lighting bonfires before 6:00 p.m., keeping cockerels on site, erecting fences higher than 1.2 metres, or using hosepipes during July and August.'</em><br><br>Exam Question: <strong>Apart from keeping cockerels on site, identify two things plot holders are prohibited from doing. [2 Marks]</strong><br>Write a full 2-mark answer, and explain why writing <em>'Keeping cockerels'</em> scores 0.",
            "lines": 3,
            "ans_label": "Two Prohibited Actions & Rule =",
            "choice_box": "1: ________________ | 2: ________________ | Why 'cockerels' scores 0: ________________",
            "step_rows": [
                ("1. Extract two valid remaining rules: (1) Lighting bonfires before 6:00 p.m., (2) Erecting fences higher than 1.2 metres (or using hosepipes in July and August)", "[A1]"),
                ("2. Explain exclusion trap: The phrase 'Apart from keeping cockerels' explicitly excludes that point from the mark scheme", "[A1]")
            ],
            "final_answer": "1. Lighting bonfires before 6:00 p.m. 2. Erecting fences over 1.2m (or using hosepipes in July/August). 'Cockerels' scores 0 because 'Apart from' excludes it.",
            "pitfall": "Including 'keeping cockerels' in your answer when the question starts with 'Apart from keeping cockerels'.",
            "reverse_check": "Always cross out the 'Apart from' item in the text so you do not copy it by mistake."
        },
        q2={
            "title": "Question 2 (Level 1 Spotting 'NOT True / FALSE' Qualifier Traps)",
            "marks": 2,
            "stem": "Read this extract from a clinic notice:<br><em>'Walk-in blood tests run Monday to Thursday from 08:00 to 11:30. Patients aged under 16 must book a scheduled paediatric slot on Fridays. Fasting patients should drink plain water only.'</em><br><br>Which <strong>ONE</strong> of the following statements is <strong>FALSE</strong> according to the extract, and explain why:<br><strong>A.</strong> Walk-in blood tests finish at 11:30 on Wednesdays.<br><strong>B.</strong> Fasting patients are allowed to drink plain water.<br><strong>C.</strong> A 14-year-old can attend the Tuesday morning walk-in clinic.<br><strong>D.</strong> There is no walk-in blood test clinic on Fridays.",
            "lines": 3,
            "ans_label": "False Option & Text Proof =",
            "choice_box": "False Statement (A / B / C / D): ____ | Proof from text: ________________________________",
            "step_rows": [
                ("1. Identify false statement: Statement C is FALSE", "[A1]"),
                ("2. Cite proof from text: The text states 'Patients aged under 16 must book a scheduled paediatric slot on Fridays', so a 14-year-old cannot use the Tuesday walk-in clinic", "[A1]")
            ],
            "final_answer": "Statement C is false — patients under 16 (such as a 14-year-old) cannot use the Monday–Thursday walk-in clinic and must book a Friday paediatric slot.",
            "pitfall": "Ticking a TRUE statement (like A or B) because you misread 'Which statement is FALSE?'.",
            "reverse_check": "14 is under 16 -> must book Friday slot -> C is definitely false."
        },
        q3={
            "title": "Question 3 (Level 1/2 The 'Goldilocks' Quotation Precision Rule)",
            "marks": 3,
            "stem": "Read this extract from a council report:<br><em>'Following the installation of 14 speed cameras along ring-road junctions in March, serious collisions fell by 48% and average vehicle speeds dropped to 29 mph.'</em><br><br>Exam Question: <strong>Give one quotation from the text that shows the speed cameras reduced accidents. [1 Mark]</strong><br>Evaluate why Candidate A (who wrote <em>'48%'</em>) and Candidate B (who copied the entire 25-word sentence) both risk losing the mark, and write the ideal exact quotation.",
            "lines": 4,
            "ans_label": "Evaluation & Ideal Quote =",
            "choice_box": "Why A fails: ____________ | Why B fails: ____________ | Ideal Quote: ____________",
            "step_rows": [
                ("1. Why Candidate A ('48%') fails: Too short/incomplete — '48%' on its own does not state what fell by 48%", "[A1]"),
                ("2. Why Candidate B (whole sentence) fails: Too long/unfocused — copies camera counts, dates, and mph speeds instead of isolating the collision reduction", "[A1]"),
                ("3. Ideal Goldilocks quotation: 'serious collisions fell by 48%'", "[A1]")
            ],
            "final_answer": "Candidate A is too brief ('48%' lacks context); Candidate B copies irrelevant extra facts. Ideal quote: 'serious collisions fell by 48%'.",
            "pitfall": "Writing a single number ('48%') when a quotation question requires a meaningful phrase.",
            "reverse_check": "'serious collisions fell by 48%' is 5 words and answers the question with 100% precision."
        },
        q4={
            "title": "Question 4 (Level 2 Using ONLY Text Evidence vs Personal Knowledge)",
            "marks": 3,
            "stem": "Read this extract from Text B (Catering Kitchen Hygiene):<br><em>'To prevent cross-contamination, chefs must use red chopping boards for raw meat and blue chopping boards for raw fish. All boards must be sanitised in the commercial dishwasher at 82°C.'</em><br><br>Exam Question: <strong>According to Text B, give two ways chefs prevent cross-contamination in the kitchen. [2 Marks]</strong><br>A catering student writes: <em>'1. Wash hands with antibacterial soap for 20 seconds. 2. Tie long hair back under a hairnet.'</em><br>Explain why this student scored <strong>0 marks</strong>, and write the correct 2-mark answer.",
            "lines": 4,
            "ans_label": "Reason for 0 Marks & Correct Answer =",
            "choice_box": "Why 0 marks: ____________________ | Correct 1: ________________ | Correct 2: ________________",
            "step_rows": [
                ("1. Explain why 0 marks: Even though handwashing and hairnets are true in real-life kitchens, neither fact appears in Text B (external personal knowledge scores 0)", "[A1]"),
                ("2. Correct Point 1 from Text B: Use colour-coded chopping boards (red for raw meat, blue for raw fish)", "[A1]"),
                ("3. Correct Point 2 from Text B: Sanitise all chopping boards in the commercial dishwasher at 82°C", "[A1]")
            ],
            "final_answer": "Scored 0 because handwashing and hairnets are not mentioned in Text B. Correct answer: 1. Use red boards for raw meat and blue boards for raw fish. 2. Sanitise boards in the dishwasher at 82°C.",
            "pitfall": "Using your own workplace experience instead of lifting facts strictly from the printed text.",
            "reverse_check": "If it isn't printed in Text B, it doesn't exist for the examiner!"
        },
        q5={
            "title": "Question 5 (Level 2 Multi-Condition Eligibility Checking Question)",
            "marks": 4,
            "stem": "Read this extract from Text C (Apprentice Travel Grant Scheme):<br><em>'To qualify for the £500 Annual Bus Pass Grant, applicants must: (1) be aged between 16 and 24 on 1st September, (2) live more than 3 miles from their training college, (3) earn under £16,000 per year before tax, and (4) submit a signed employer attendance letter by 15th October.'</em><br><br>Your friend Chloe says: <em>'I turned 24 in August, I live 4.5 miles from college, and my apprenticeship wage is £14,200 a year — so I can send in my form on 20th October and get the £500 grant!'</em><br>Using Text C, evaluate whether Chloe will receive the grant. Check <strong>all four conditions</strong> in your answer.",
            "lines": 5,
            "ans_label": "Four-Point Eligibility Audit =",
            "choice_box": "Verdict (Yes/No): ____ | Met Conditions: ________________ | Failed Condition: ________________",
            "step_rows": [
                ("1. State overall verdict clearly: No, Chloe will NOT receive the £500 grant", "[A1]"),
                ("2. Verify Condition 1 & 2 (Met): She meets the age rule (aged 24 on 1st Sept, which is within 16–24) and distance rule (4.5 miles is more than 3 miles)", "[A1]"),
                ("3. Verify Condition 3 (Met): She meets the income rule (£14,200 is under the £16,000 cap)", "[A1]"),
                ("4. Identify failed Condition 4: She plans to apply on 20th October, which misses the strict 'by 15th October' deadline (and she must include a signed employer letter)", "[A1]")
            ],
            "final_answer": "No — although Chloe meets the age (24), distance (4.5 miles > 3 miles), and salary (£14,200 < £16,000) rules, applying on 20th October misses the mandatory 15th October deadline.",
            "pitfall": "Saying 'Yes' because you checked age, distance, and salary but overlooked the 15th October deadline at the end.",
            "reverse_check": "20th October is after 15th October -> application rejected."
        },
        q6={
            "title": "Question 6 (Level 2 Matching Answer Depth to Mark Tariffs — 1 vs 3 Marks)",
            "marks": 4,
            "stem": "Read this extract from a campaign leaflet:<br><em>'Every year, 250,000 tonnes of edible supermarket food are dumped into landfill while families go hungry. Sign our Zero-Waste Petition today!'</em><br><br>Compare how you must answer these two different exam questions on the extract:<br>• <strong>Question A [1 Mark]:</strong> <em>How many tonnes of edible supermarket food are dumped into landfill each year?</em><br>• <strong>Question B [3 Marks]:</strong> <em>Explain how the writer uses language to persuade the reader to sign the petition.</em><br><br>Write the full model answer for <strong>both</strong> Question A and Question B, and explain why Question B requires three distinct components.",
            "lines": 5,
            "ans_label": "Model Answers for Q.A and Q.B =",
            "choice_box": "Q.A Answer [1m]: ____________ | Q.B Answer [3m] (Technique + Quote + Effect): ________________",
            "step_rows": [
                ("1. Question A [1 Mark] Answer: '250,000 tonnes' (direct 1-point retrieval)", "[A1]"),
                ("2. Question B Component 1 (Name techniques): Statistic ('250,000 tonnes'), emotive contrast ('dumped into landfill while families go hungry'), and imperative command ('Sign our Zero-Waste Petition today!')", "[A1]"),
                ("3. Question B Component 2 (Accurate quotes): Includes exact short quotations from the extract", "[A1]"),
                ("4. Question B Component 3 (Specific effect): Explains that contrasting massive food waste against hungry families provokes moral outrage and guilt, compelling the reader to sign", "[A1]")
            ],
            "final_answer": "Q.A: 250,000 tonnes. Q.B: Uses a shocking statistic ('250,000 tonnes') contrasted with emotive language ('dumped into landfill while families go hungry') and an imperative ('Sign... today!') to provoke moral outrage and guilt so readers sign the petition.",
            "pitfall": "Writing a 1-sentence vague answer for a 3-mark language question instead of giving Technique + Quote + Specific Effect.",
            "reverse_check": "1 mark = 1 retrieval fact; 3 marks = Technique + Quote + Specific Reader Effect."
        }
    ),

    # 11. Why Do Writers Write
    make_english_topic(
        slug="reading-why-do-writers-write",
        title="The Writer's Purpose, Sub-Purpose & Audience Adaptation",
        category="reading",
        spec_codes="L1.16 • L2.17 • L2.18",
        golden_rule="Never write 'To inform' or 'To persuade' on its own! Always use the complete Pearson Edexcel formula: 'To [Purpose Verb: inform / persuade / instruct / advise / review] [the target audience] about [the specific topic and desired action].'",
        q1={
            "title": "Question 1 (Level 1 Writing a Full-Mark Purpose Statement)",
            "marks": 2,
            "stem": "Read this extract from a town council notice:<br><em>'From Monday 4th November, household green garden-waste bins will move from weekly to fortnightly winter collections. Normal weekly collections will resume on 3rd March.'</em><br><br>An exam candidate writes the main purpose as: <em>'To inform.'</em><br>(a) Explain why <em>'To inform'</em> scores <strong>0 marks</strong> on its own.<br>(b) Write a complete <strong>full-mark purpose statement</strong> for this notice.",
            "lines": 3,
            "ans_label": "Diagnostic & Full Purpose Statement =",
            "choice_box": "(a) Why 0 marks: ________________ | (b) Full statement: To inform residents about ________________",
            "step_rows": [
                ("1. (a) Explain mark scheme rule: One-word or two-word answers ('To inform') score 0 because they do not state WHAT topic the text is informing the reader about", "[A1]"),
                ("2. (b) Full-mark statement: To inform local residents that green garden-waste bin collections are changing to fortnightly over winter from 4th November until 3rd March", "[A1]")
            ],
            "final_answer": "(a) Scores 0 because it omits the specific topic. (b) To inform local residents that green garden-waste bin collections are changing to fortnightly between 4th November and 3rd March.",
            "pitfall": "Stopping after the verb 'To inform' without adding 'who' and 'about what'.",
            "reverse_check": "Verb (To inform) + Audience (residents) + Topic (winter garden-waste collection dates) = Full marks."
        },
        q2={
            "title": "Question 2 (Level 1 Distinguishing 'To Instruct' vs 'To Advise')",
            "marks": 2,
            "stem": "Compare these two extracts about winter driving:<br><strong>Extract A (Highway Code Rule 229):</strong> <em>'Before driving in snow, you MUST clear all snow and ice from every window, mirror, and number plate.'</em><br><strong>Extract B (Motoring Magazine Tip):</strong> <em>'To stop your windscreen wipers freezing to the glass overnight, you could try slipping an old pair of long socks over the wiper blades.'</em><br><br>State which extract is written <strong>to instruct</strong> and which is written <strong>to advise</strong>, and quote the modal verbs that prove your answer.",
            "lines": 3,
            "ans_label": "Purposes & Modal Clues =",
            "choice_box": "Extract A: ____________ (Verb: ________) | Extract B: ____________ (Verb: ________)",
            "step_rows": [
                ("1. Extract A: To instruct (mandatory legal command proved by 'you MUST clear')", "[A1]"),
                ("2. Extract B: To advise (optional helpful suggestion proved by 'you could try')", "[A1]")
            ],
            "final_answer": "Extract A = To instruct (proved by mandatory 'MUST'); Extract B = To advise (proved by optional 'could try').",
            "pitfall": "Confusing mandatory safety/legal instructions ('must') with optional tips ('could try').",
            "reverse_check": "'MUST' = compulsory instruction; 'could try' = optional advice."
        },
        q3={
            "title": "Question 3 (Level 1/2 Spotting Persuasive Purpose Behind Factual Statistics)",
            "marks": 3,
            "stem": "Read this extract from a leaflet delivered through letterboxes:<br><em>'Last year, burglary rates in Oakwood rose by 18%, with 7 out of 10 break-ins occurring through unbolted back doors. Protect your family and belongings today — order the GuardPro Smart Doorbell Camera before Friday and claim 30% off installation!'</em><br><br>Explain why the <strong>main purpose</strong> of this leaflet is <strong>to persuade/sell</strong> rather than simply to inform, and explain why the writer included the burglary statistics in the first sentence.",
            "lines": 4,
            "ans_label": "Main Purpose & Role of Statistics =",
            "choice_box": "Main Purpose: ________________ | Role of Statistics: ________________ | Call to Action: ________________",
            "step_rows": [
                ("1. State main purpose: To persuade Oakwood householders to buy the GuardPro Smart Doorbell Camera", "[A1]"),
                ("2. Explain role of statistics: The 18% burglary rise and '7 out of 10' stats are used to alarm homeowners and make them feel vulnerable", "[A1]"),
                ("3. Link to closing call to action: The final sentence ('order the GuardPro... before Friday and claim 30% off') proves the statistics are there to drive commercial sales", "[A1]")
            ],
            "final_answer": "Main purpose is to persuade householders to buy the GuardPro Doorbell Camera. The burglary statistics (18% rise, 7 out of 10) are included to alarm residents so they respond to the closing sales offer ('claim 30% off').",
            "pitfall": "Seeing percentages in the first sentence and immediately writing that the main purpose is 'to inform about crime'.",
            "reverse_check": "Always check the final sentence ('order... before Friday') to see what the writer is really trying to achieve!"
        },
        q4={
            "title": "Question 4 (Level 2 Analysing Sub-Purposes Within an Extended Text)",
            "marks": 3,
            "stem": "A workplace guide titled <em>'Switching to Our New Cloud Payroll Portal'</em> contains three paragraphs:<br>• <strong>Paragraph 1:</strong> Explains why the old paper payslips were slow and environmentally wasteful.<br>• <strong>Paragraph 2:</strong> Gives a numbered 4-step guide on how to log in and set your 8-digit PIN.<br>• <strong>Paragraph 3:</strong> Reassures staff that HR advisors will run drop-in help desks all week for anyone struggling.<br><br>Identify the <strong>specific sub-purpose</strong> of Paragraph 1, Paragraph 2, and Paragraph 3.",
            "lines": 4,
            "ans_label": "Three Sub-Purposes =",
            "choice_box": "Para 1 Purpose: ____________ | Para 2 Purpose: ____________ | Para 3 Purpose: ____________",
            "step_rows": [
                ("1. Paragraph 1 sub-purpose: To explain/justify why the company is replacing paper payslips with the cloud portal", "[A1]"),
                ("2. Paragraph 2 sub-purpose: To instruct staff step-by-step on how to log in and set up their 8-digit PIN", "[A1]"),
                ("3. Paragraph 3 sub-purpose: To reassure and support staff who may feel anxious about the new technology", "[A1]")
            ],
            "final_answer": "Para 1: To explain/justify the switch from paper payslips. Para 2: To instruct staff step-by-step on logging in. Para 3: To reassure staff with drop-in HR support.",
            "pitfall": "Giving the exact same verb for all three paragraphs instead of distinguishing Explain -> Instruct -> Reassure.",
            "reverse_check": "Para 1 = Why (Explain); Para 2 = How-to steps (Instruct); Para 3 = Help available (Reassure)."
        },
        q5={
            "title": "Question 5 (Level 2 Evaluating How a Writer Adapts a Text to Target Audience)",
            "marks": 4,
            "stem": "Read this extract from a financial guide aimed at <strong>18-year-old school leavers starting their first job</strong>:<br><em>'Just landed your first proper paycheque? Amazing! Before you blow it all on festival tickets and takeaway pizzas, let's decode the mystery letters on your payslip: \"PAYE\" is simply the income tax taken automatically by the government, and \"NI\" (National Insurance) builds your state pension and NHS cover.'</em><br><br>Analyse <strong>four ways</strong> the writer has adapted the <strong>language, examples, and explanations</strong> to suit 18-year-old school leavers.",
            "lines": 5,
            "ans_label": "Audience Adaptation Analysis =",
            "choice_box": "1. Tone/Hook: ________ | 2. Examples: ________ | 3. Slang: ________ | 4. Jargon Explanations: ________",
            "step_rows": [
                ("1. Enthusiastic conversational hook: Opens with a celebratory question and exclamation ('Just landed your first proper paycheque? Amazing!') to build rapport", "[A1]"),
                ("2. Age-relatable spending examples: References 'festival tickets and takeaway pizzas' which directly match an 18-year-old lifestyle", "[A1]"),
                ("3. Informal colloquial diction: Uses approachable slang ('landed', 'blow it all') so finance does not feel dry or intimidating", "[A1]"),
                ("4. Plain-English jargon decoding: Explicitly defines adult tax acronyms ('PAYE' and 'NI') in simple terms because first-time workers have never seen a payslip before", "[A1]")
            ],
            "final_answer": "1. Celebratory conversational hook ('Amazing!'). 2. Youth-focused examples ('festival tickets and takeaway pizzas'). 3. Informal slang ('blow it all'). 4. Plain-English definitions of unfamiliar payslip acronyms ('PAYE', 'NI') for first-time earners.",
            "pitfall": "Only mentioning 'informal language' without pointing out the plain-English explanations of PAYE and NI for first-time workers.",
            "reverse_check": "Tone + Youth examples + Slang + Acronym definitions = 4 distinct adaptations."
        },
        q6={
            "title": "Question 6 (Level 2 Comparing Writer's Purpose & Audience Across Two Texts)",
            "marks": 4,
            "stem": "<strong>Text A (Product Review in 'Practical Plumber Monthly'):</strong><br><em>'We tested the Vortex 30kW Combi Boiler across six winter installations. While the brass manifold is exceptionally durable and quick to solder, the cramped PCB wiring box makes servicing awkward. Verdict: 4/5 stars for trade installers.'</em><br><br><strong>Text B (Manufacturer's Customer Brochure):</strong><br><em>'Transform your home into a cosy sanctuary this winter with the whisper-quiet Vortex Combi Boiler — slashing your gas bills by up to £240 a year! Ask your local installer for Vortex today.'</em><br><br>Compare the <strong>purpose</strong> and <strong>target audience</strong> of Text A and Text B, supporting your answer with evidence from both texts.",
            "lines": 5,
            "ans_label": "Comparative Purpose & Audience =",
            "choice_box": "Text A Purpose & Audience: ____________________ | Text B Purpose & Audience: ____________________",
            "step_rows": [
                ("1. Text A purpose: To review and evaluate the pros and cons of the Vortex boiler objectively ('4/5 stars') for fellow tradespeople", "[M1]"),
                ("2. Text A audience & evidence: Professional plumbers/heating engineers, proved by trade jargon ('brass manifold', 'quick to solder', 'PCB wiring box')", "[A1]"),
                ("3. Text B purpose: To promote and persuade customers to buy the Vortex boiler ('Ask your local installer for Vortex today')", "[M1]"),
                ("4. Text B audience & evidence: Homeowners/householders, proved by domestic comfort imagery ('cosy sanctuary', 'whisper-quiet') and household bill savings ('up to £240 a year')", "[A1]")
            ],
            "final_answer": "Text A aims to review/evaluate the boiler objectively (giving pros, cons, and '4/5 stars') for professional plumbers ('quick to solder', 'PCB wiring box'). Conversely, Text B aims to persuade homeowners to buy the boiler using domestic comfort appeal ('cosy sanctuary') and £240 bill savings.",
            "pitfall": "Saying both texts have the same purpose ('to talk about the Vortex boiler') instead of contrasting objective trade review vs commercial homeowner promotion.",
            "reverse_check": "Text A = Review for plumbers; Text B = Persuade/sell to homeowners."
        }
    )
]

print(f"Loaded {len(WORKSHEETS_ENGLISH_PART1)} bespoke reading worksheet topics in bespoke_worksheets_english_part1.py")
