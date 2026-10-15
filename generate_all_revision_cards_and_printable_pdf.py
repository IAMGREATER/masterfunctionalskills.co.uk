#!/usr/bin/env python3
"""
Master Functional Skills - Comprehensive Revision Cards & Printable PDF Generator
Mapped strictly to UK Government (DfE) Subject Content & Ofqual Regulated Criteria.
Generates:
1. Interactive JS Dataset (assets/js/revision_cards_data.js)
2. Duplex Print-Ready HTML & PDFs (assets/downloads/)
"""
import json
import os
import subprocess

ALL_CARDS = [
    # =========================================================================
    # MATHEMATICS - LEVEL 2
    # =========================================================================
    {
        "id": "maths-l2-01",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS18",
        "title": "Area of a Trapezium",
        "prompt": "How do you calculate the area of a trapezium, and which measurement in the question must you immediately discard?",
        "context": "Commonly tested in NHS floor space renovations, landscaping quotes, or building construction costs.",
        "steps": [
            "Identify the two parallel horizontal sides (a and b) and add them together: (a + b).",
            "Divide the sum by 2 to find the average width: ((a + b) ÷ 2).",
            "Multiply this average width by the vertical perpendicular height (h)."
        ],
        "golden_rule": "Area = ((a + b) ÷ 2) × h  (Half the sum of parallel sides times perpendicular height)",
        "exam_trap": "Examiners will always give you the slanted side length. Cross it out immediately! Slanted sides are ONLY used for perimeter, never for area.",
        "drill_q": "A clinical bay has parallel sides of 6 m and 10 m, with a vertical height of 4 m and a slanted side of 5 m. What is the area?",
        "drill_a": "Area = ((6 + 10) ÷ 2) × 4 = (16 ÷ 2) × 4 = 8 × 4 = 32 m². Discard the 5 m slant!"
    },
    {
        "id": "maths-l2-02",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS18",
        "title": "Circumference vs Area of a Circle",
        "prompt": "What is the key difference between Circumference and Area of a circle, and what happens if you are given the diameter instead of the radius?",
        "context": "Tested in circular ward tables, circular running tracks, and lawn seed calculations.",
        "steps": [
            "Check given measurement: Is it Diameter (edge-to-edge through center) or Radius (center-to-edge)? If given diameter, halve it first to get radius (r = d ÷ 2).",
            "Circumference (Perimeter of circle): C = π × d (or 2 × π × r).",
            "Area (Space inside circle): A = π × r² (Square the radius first, then multiply by π)."
        ],
        "golden_rule": "Circumference = πd (think 'Cherry Pie Delicious'). Area = πr² (think 'Apple Pies R Too').",
        "exam_trap": "Squaring the diameter instead of the radius! If diameter = 10 cm, radius = 5 cm. Area = π × 5² = 25π ≈ 78.54 cm², NOT π × 10².",
        "drill_q": "A circular pond has a diameter of 8 metres. Calculate its area using π = 3.14.",
        "drill_a": "Radius = 8 ÷ 2 = 4 m. Area = 3.14 × (4²) = 3.14 × 16 = 50.24 m²."
    },
    {
        "id": "maths-l2-03",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "number",
        "strand_label": "Number & The Number System",
        "dfe_code": "DfE L2.N9",
        "title": "Reverse Percentages (Original Value)",
        "prompt": "How do you find the original price of an item when given the discounted price or a price including VAT?",
        "context": "Essential in retail salary calculations, VAT inclusive bills, and post-sale discounts.",
        "steps": [
            "Represent the original unknown price as 100%.",
            "Determine the new percentage: If a 20% discount, New Price = 80%. If 20% VAT added, New Price = 120%.",
            "Divide the final price by the percentage as a decimal (e.g. ÷ 0.80 or ÷ 1.20) to find the 100% original value."
        ],
        "golden_rule": "Original Value = New Value ÷ (1 ± decimal rate). NEVER calculate the percentage of the new number and add/subtract it!",
        "exam_trap": "Adding 20% back onto a discounted price! If £80 is 20% off, 20% of 80 is 16, giving £96 (WRONG!). The real original is £80 ÷ 0.8 = £100.",
        "drill_q": "A laptop costs £360 after a 25% discount. What was the original price before the sale?",
        "drill_a": "£360 represents 75% (100% - 25%). Original = 360 ÷ 0.75 = £480."
    },
    {
        "id": "maths-l2-04",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "number",
        "strand_label": "Number & The Number System",
        "dfe_code": "DfE L2.N8",
        "title": "Percentage Increase and Decrease",
        "prompt": "What is the fastest multiplier method to calculate percentage increase or decrease in one single step?",
        "context": "Energy bill price hikes, annual pay raises, and staff headcount adjustments.",
        "steps": [
            "For an Increase: Add the percentage to 100% and convert to decimal (e.g. +15% → 100% + 15% = 115% → multiplier = 1.15).",
            "For a Decrease: Subtract the percentage from 100% and convert to decimal (e.g. -15% → 100% - 15% = 85% → multiplier = 0.85).",
            "Multiply the starting amount by the multiplier."
        ],
        "golden_rule": "Multiplier Method: New Amount = Original × (1 + r) for increase; Original × (1 - r) for decrease.",
        "exam_trap": "For single-digit percentages (e.g. 5%), students mistakenly multiply by 1.5 instead of 1.05! 1.5 is a 50% increase, 1.05 is a 5% increase.",
        "drill_q": "A Band 5 NHS salary of £28,407 receives a 3.5% pay increase. Calculate the new salary.",
        "drill_a": "Multiplier = 1 + 0.035 = 1.035. New Salary = £28,407 × 1.035 = £29,401.25."
    },
    {
        "id": "maths-l2-05",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "number",
        "strand_label": "Number & The Number System",
        "dfe_code": "DfE L2.N11",
        "title": "Ratio: Sharing into Given Parts",
        "prompt": "How do you share an amount in a given ratio (e.g. 3 : 2), and how do you solve 'difference' or 'one person gets more' questions?",
        "context": "Mixing concrete/paint, medication dosages, and sharing inheritance or lottery winnings.",
        "steps": [
            "STANDARD SHARING: Add all ratio parts together to get Total Parts. Divide total amount by Total Parts to find Value of 1 Part. Multiply 1 Part by each ratio term.",
            "DIFFERENCE QUESTIONS: If person A gets £50 more than person B, divide £50 by the difference in parts, NOT the total parts!"
        ],
        "golden_rule": "Add parts → Divide to find 1 part → Multiply out. Always check your parts add back up to the original total!",
        "exam_trap": "Dividing the total by the ratio numbers individually, or dividing the difference by total parts instead of the part difference.",
        "drill_q": "Share £450 between Alex and Sam in the ratio 4 : 5.",
        "drill_a": "Total parts = 4 + 5 = 9. Value of 1 part = 450 ÷ 9 = £50. Alex = 4 × £50 = £200. Sam = 5 × £50 = £250. (Check: 200 + 250 = 450)."
    },
    {
        "id": "maths-l2-06",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "data",
        "strand_label": "Handling Information & Data",
        "dfe_code": "DfE L2.H24",
        "title": "Estimated Mean from Grouped Frequency Tables",
        "prompt": "How do you estimate the mean from a grouped frequency table, and why is it called an 'estimate'?",
        "context": "Waiting times in A&E, delivery dispatch times, and survey response brackets.",
        "steps": [
            "Find the Midpoint (mp) of each group: (Lower bound + Upper bound) ÷ 2.",
            "Multiply each group midpoint by its corresponding Frequency (f): mp × f.",
            "Sum all the (mp × f) products to get Total (Σfx).",
            "Divide Total (Σfx) by the Total Frequency (Sum of frequencies, NOT the number of rows!)."
        ],
        "golden_rule": "Estimated Mean = Σ(Midpoint × Frequency) ÷ Total Frequency. It is an estimate because exact individual raw values within groups are unknown.",
        "exam_trap": "Dividing by the number of table rows (e.g. dividing by 4 instead of the total frequency of 60 people!).",
        "drill_q": "Groups: 0-10 (freq 4), 10-20 (freq 6). Find the estimated mean.",
        "drill_a": "Midpoints: 5 and 15. Products: (5 × 4 = 20) + (15 × 6 = 90) = 110. Total frequency = 4 + 6 = 10. Estimated mean = 110 ÷ 10 = 11."
    },
    {
        "id": "maths-l2-07",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS15",
        "title": "Speed, Distance and Time Calculations",
        "prompt": "How do you calculate speed, distance, or time, and how must you convert decimal hours (e.g. 2.4 hours) into hours and minutes?",
        "context": "Ambulance transit times, travel logistics, and flight durations.",
        "steps": [
            "Use the DST Triangle: Distance = Speed × Time; Speed = Distance ÷ Time; Time = Distance ÷ Speed.",
            "DECIMAL TIME CONVERSION: Time in hours with decimals must NEVER be read as minutes! Multiply the decimal part by 60.",
            "Example: 2.4 hours = 2 hours + (0.4 × 60) = 2 hours and 24 minutes (NOT 2 hours 40 mins!)."
        ],
        "golden_rule": "Distance = Speed × Time. To convert minutes to decimal hours: divide by 60. To convert decimal hours to minutes: multiply decimal by 60.",
        "exam_trap": "Treating 1 hour 45 minutes as 1.45 on the calculator! 45 mins ÷ 60 = 0.75, so it must be entered as 1.75 hours.",
        "drill_q": "A driver travels 150 miles at an average speed of 60 mph. How long does the journey take in hours and minutes?",
        "drill_a": "Time = Distance ÷ Speed = 150 ÷ 60 = 2.5 hours. 0.5 × 60 = 30 mins. Answer: 2 hours 30 minutes."
    },
    {
        "id": "maths-l2-08",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS19",
        "title": "Volume and Capacity of Prisms & Cylinders",
        "prompt": "What is the universal formula for the volume of any prism or cylinder, and how do you convert cubic meters (m³) to liters?",
        "context": "Water tank capacities, medication liquid storage, and swimming pool filling rates.",
        "steps": [
            "Find the Area of the cross-section face (e.g. triangle for triangular prism, circle for cylinder).",
            "Multiply the cross-sectional area by the length/depth (h) of the prism.",
            "For a Cylinder: Volume = π × r² × h.",
            "CAPACITY CONVERSION: 1 m³ = 1,000 Litres. 1 cm³ = 1 millilitre (ml). 1,000 cm³ = 1 Litre."
        ],
        "golden_rule": "Volume of Any Prism = Area of Cross-Section × Length. Capacity = Volume in m³ × 1,000 to get Litres.",
        "exam_trap": "For a triangular prism, forgetting to halve the triangle base times height before multiplying by length!",
        "drill_q": "A cylindrical tank has a radius of 1 m and a height of 2 m. How many litres of water does it hold? (Use π = 3.142)",
        "drill_a": "Area of base = 3.142 × 1² = 3.142 m². Volume = 3.142 × 2 = 6.284 m³. Litres = 6.284 × 1,000 = 6,284 litres."
    },
    {
        "id": "maths-l2-09",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "data",
        "strand_label": "Handling Information & Data",
        "dfe_code": "DfE L2.H27",
        "title": "Probability of Combined Independent Events",
        "prompt": "How do you calculate the probability of two independent events both happening (e.g. rolling a 6 AND flipping Heads)?",
        "context": "Quality assurance defect checking, medical testing reliability, and risk assessment.",
        "steps": [
            "Find the probability of the first event P(A).",
            "Find the probability of the second event P(B).",
            "When both events must happen ('AND'), MULTIPLY the two probabilities together: P(A and B) = P(A) × P(B).",
            "When either event can happen ('OR'), ADD the probabilities (mutually exclusive)."
        ],
        "golden_rule": "AND means MULTIPLY probabilities. OR means ADD probabilities. Express answers as simplified fractions, decimals, or percentages.",
        "exam_trap": "Adding probabilities when calculating 'both happen'! Flipping two heads is 1/2 × 1/2 = 1/4 (25%), NOT 1/2 + 1/2 = 1 (100%).",
        "drill_q": "The chance of rain on Saturday is 0.3 and on Sunday is 0.4. Assuming independent days, what is the probability it rains on BOTH days?",
        "drill_a": "P(Both) = 0.3 × 0.4 = 0.12 (or 12%)."
    },
    {
        "id": "maths-l2-10",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "data",
        "strand_label": "Handling Information & Data",
        "dfe_code": "DfE L2.H25",
        "title": "Comparing Two Datasets (Average + Spread)",
        "prompt": "In exam questions asking to 'compare two sets of data', which two specific mathematical metrics MUST you compare and interpret in context?",
        "context": "Comparing ward recovery times, sales figures before and after a marketing campaign.",
        "steps": [
            "METRIC 1 (Average): Calculate and compare either the Mean or Median. State clearly which group had the higher average and what it means in context.",
            "METRIC 2 (Spread/Consistency): Calculate and compare the Range. The smaller range indicates greater consistency and reliability; the larger range indicates greater variation.",
            "Always write two full concluding sentences linking your numbers back to the scenario!"
        ],
        "golden_rule": "Always state ONE measure of average (Mean/Median) AND ONE measure of spread (Range) in two contextual comparison sentences.",
        "exam_trap": "Only stating the numbers without explaining what they mean in real life (e.g. writing 'Mean A is 24 and Mean B is 20' without saying 'On average, Group A was faster').",
        "drill_q": "Team A: Mean score = 75, Range = 12. Team B: Mean score = 68, Range = 28. Compare the two teams.",
        "drill_a": "1. Team A performed better on average because their mean score of 75 was 7 points higher than Team B's 68. 2. Team A was also more consistent because their range of 12 was much smaller than Team B's 28."
    },
    {
        "id": "maths-l2-11",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS17",
        "title": "Bearings (Three-Figure Direction)",
        "prompt": "What are the three golden rules for writing and measuring bearings in Functional Skills Mathematics?",
        "context": "Navigation, search and rescue paths, air traffic control, and orienteering.",
        "steps": [
            "RULE 1: Always measure from NORTH (000° line).",
            "RULE 2: Always measure in a CLOCKWISE direction.",
            "RULE 3: Always write bearings as THREE FIGURES (e.g. 045°, 008°, 180°).",
            "REVERSE BEARING: If bearing A to B is < 180°, add 180°. If > 180°, subtract 180°."
        ],
        "golden_rule": "North, Clockwise, 3 Figures. If measuring North-East, write 045°, never 45°.",
        "exam_trap": "Measuring anti-clockwise from North, or forgetting the leading zero for bearings under 100°.",
        "drill_q": "The bearing of Town B from Town A is 070°. What is the reverse bearing of Town A from Town B?",
        "drill_a": "Since 070° < 180°, add 180°: 70° + 180° = 250°."
    },
    {
        "id": "maths-l2-12",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L2.MSS16",
        "title": "Scale Drawings and Map Conversions",
        "prompt": "How do you calculate real-world distances from a map scale such as 1 : 50,000 or 1 cm = 4 m?",
        "context": "Architectural blueprints, site layout plans, and OS map hiking routes.",
        "steps": [
            "Measure or identify the length on the plan/map in centimeters.",
            "Multiply the map length by the scale factor (e.g. 5 cm × 50,000 = 250,000 cm).",
            "Convert to sensible real-world units: Divide by 100 to get metres (250,000 ÷ 100 = 2,500 m). Divide by 1,000 to get kilometres (2,500 ÷ 1,000 = 2.5 km)."
        ],
        "golden_rule": "Map distance × Scale factor = Real distance. Then convert cm → m (÷ 100) → km (÷ 1,000).",
        "exam_trap": "Forgetting to convert units, leaving real-world distances in thousands of centimeters!",
        "drill_q": "A map scale is 1 : 25,000. Two landmarks are 8 cm apart on the map. Find the real distance in kilometres.",
        "drill_a": "Real distance = 8 × 25,000 = 200,000 cm. Convert to metres: 200,000 ÷ 100 = 2,000 m. Convert to km: 2,000 ÷ 1,000 = 2 km."
    },

    # =========================================================================
    # ENGLISH - LEVEL 2
    # =========================================================================
    {
        "id": "eng-l2-01",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L2.W14",
        "title": "Formal Letter Conventions & Sign-Offs",
        "prompt": "What are the exact layout conventions of a formal letter, and what is the strict rule for signing off 'Yours faithfully' vs 'Yours sincerely'?",
        "context": "Official complaints, job applications, requests to local councils, or NHS patient correspondence.",
        "steps": [
            "Sender's Address in top-right corner; Date below it.",
            "Recipient's Name and Full Address on the left side below the date.",
            "Formal Salutation on the left: 'Dear Mr Jenkins,' or 'Dear Sir or Madam,'.",
            "Subject Heading underlined or in bold: 'RE: Application for Clinical Lead'.",
            "Structured Body: Introduction (purpose), 2-3 development paragraphs, Conclusion (clear call to action).",
            "SIGN-OFF RULE: If you named the recipient ('Dear Mr Jenkins'), sign off 'Yours sincerely'. If you did NOT name them ('Dear Sir or Madam'), sign off 'Yours faithfully'."
        ],
        "golden_rule": "S-S / N-F: Specific Name = Sincerely. No Name = Faithfully. Always sign your full name and job title below.",
        "exam_trap": "Mixing up the sign-off ('Dear Sir' with 'Yours sincerely'), or omitting the recipient address and subject line (which loses easy format marks!).",
        "drill_q": "You are writing a formal letter to Mrs Davies (Head of HR). Which sign-off must you use: 'Yours sincerely' or 'Yours faithfully'?",
        "drill_a": "Yours sincerely — because you know the recipient's name (Mrs Davies)."
    },
    {
        "id": "eng-l2-02",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L2.W15",
        "title": "Formal Report Structure & Formatting",
        "prompt": "What layout features are mandatory in a Level 2 Functional Skills Report, and what tone must be maintained?",
        "context": "Health and Safety audits, workplace recommendations, or investigation summaries.",
        "steps": [
            "Mandatory Header Block: To: [Name/Role], From: [Your Name/Role], Date: [Date], Subject: [Clear Title].",
            "Executive Summary / Purpose section: Clearly stating why the report was commissioned.",
            "Subheadings for each section (e.g. Findings, Current Challenges, Staff Feedback).",
            "Numbered or bulleted actionable recommendations at the conclusion.",
            "Tone: Strictly objective, professional, and impersonal (avoid emotional outbursts or slang)."
        ],
        "golden_rule": "A report MUST have a To/From/Date/Subject header block, distinct subheadings, and a final section of numbered recommendations.",
        "exam_trap": "Writing a report like an informal essay with continuous paragraphs and no subheadings or bullet points.",
        "drill_q": "What should always be the final section of a formal workplace report?",
        "drill_a": "Recommendations (or Conclusion and Recommendations), preferably formatted with clear bullet points or numbered action steps."
    },
    {
        "id": "eng-l2-03",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L2.W20",
        "title": "Punctuation Mastery: The Semicolon (;)",
        "prompt": "When is it grammatically correct to use a semicolon (;), and how does it elevate your Level 2 SPaG score?",
        "context": "Pearson Edexcel and Ofqual criteria specifically reward the accurate use of varied sentence structures and higher-level punctuation.",
        "steps": [
            "RULE 1: Joining two independent clauses that are closely linked in thought without using a conjunction (and, but, so).",
            "Both sides of the semicolon MUST be able to stand alone as complete, grammatically correct sentences.",
            "Example: 'The audit results were concerning; several wards failed to meet the hygiene standards.'",
            "RULE 2: In a complex list where individual list items already contain commas."
        ],
        "golden_rule": "If you can replace the semicolon with a full stop and both sides make complete sense, your semicolon is used correctly!",
        "exam_trap": "Using a semicolon where a comma or colon belongs, such as after an incomplete fragment: 'Because it was late; we left' (INCORRECT!).",
        "drill_q": "Correct this sentence using a semicolon: 'The new IT software was expensive, however it significantly reduced administrative errors.'",
        "drill_a": "'The new IT software was expensive; however, it significantly reduced administrative errors.' (Semicolon joins the two independent clauses before 'however')."
    },
    {
        "id": "eng-l2-04",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "reading",
        "strand_label": "Reading Comprehension",
        "dfe_code": "DfE L2.R12",
        "title": "Fact vs Opinion & Detecting Implicit Bias",
        "prompt": "How do you distinguish between an objective fact and a subjective opinion, and how do you spot implicit bias in a reading text?",
        "context": "Critical reading questions evaluating news articles, blog reviews, or promotional leaflets.",
        "steps": [
            "FACT: A statement that can be verified with objective evidence, data, dates, or statistics (e.g. 'The hospital opened in 1994').",
            "OPINION: A belief, feeling, or viewpoint that cannot be proven true or false, often marked by evaluative adjectives (e.g. 'The hospital offers the best atmosphere').",
            "BIAS: When an author favors one perspective by using emotive language, selective evidence, or loaded rhetoric without acknowledging the other side."
        ],
        "golden_rule": "Facts can be proven true or false with objective data. Opinions reflect personal values, emotions, or judgments.",
        "exam_trap": "Treating quotes from famous experts as facts. If an expert says 'I believe our service is unrivaled', it remains an opinion!",
        "drill_q": "Identify whether this is Fact or Opinion: 'According to NHS England data, waiting times decreased by 14% over the last quarter.'",
        "drill_a": "Fact — it refers to verifiable statistical data collected by an identified official body."
    },
    {
        "id": "eng-l2-05",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "reading",
        "strand_label": "Reading Comprehension",
        "dfe_code": "DfE L2.R19",
        "title": "Comparing Two Texts (Synthesis)",
        "prompt": "In Level 2 Reading papers, how do you successfully compare two texts on the same subject to achieve full marks?",
        "context": "Mandatory in Question 14/15 on Pearson Edexcel English Level 2 Reading papers.",
        "steps": [
            "Identify the common theme or question prompt (e.g. attitudes towards remote working).",
            "Extract Point 1 from Text A with supporting quote or paraphrase.",
            "Immediately connect to Text B using a comparative connective (e.g. 'In contrast, Text B argues...', 'Similarly, Text B suggests...').",
            "Explicitly compare their perspectives, tone, and presentation."
        ],
        "golden_rule": "Use the Point-Evidence-Compare framework: State Text A's viewpoint + evidence → Comparative Connective → State Text B's viewpoint + evidence.",
        "exam_trap": "Writing two separate summaries of Text A and Text B without explicitly comparing them using comparative phrases (in contrast, whereas, similarly).",
        "drill_q": "Which connective is best to show contrast between two texts: 'Furthermore', 'Consequently', or 'Conversely'?",
        "drill_a": "'Conversely' (or 'In contrast', 'Whereas') — it explicitly establishes a direct opposing comparison."
    },
    {
        "id": "eng-l2-06",
        "subject": "english",
        "subject_label": "English",
        "level": "l2",
        "level_label": "Level 2",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L2.W16",
        "title": "Persuasive Articles & AFOREST Devices",
        "prompt": "How do you structure an engaging article for a magazine or community website, and what rhetorical devices must you deploy?",
        "context": "Campaigning for better public transport, local environmental initiatives, or staff well-being.",
        "steps": [
            "Catchy, engaging Headline (e.g. 'Why Our Green Spaces Matter More Than Ever').",
            "Byline: 'By [Your Name]'.",
            "Hook introductory paragraph: Draw the reader in with a provocative rhetorical question or striking statistic.",
            "Use AFOREST techniques: Alliteration, Facts, Opinions, Rhetorical questions, Emotive language, Statistics, Tripling (rule of three).",
            "Memorable conclusion that calls the reader to take urgent action."
        ],
        "golden_rule": "Headline + Byline + Intro Hook + Balanced arguments with AFOREST + Strong Call to Action.",
        "exam_trap": "Writing an article like a formal letter with addresses and 'Dear Sir' salutations. An article requires a title and journalistic style!",
        "drill_q": "Give an example of 'Rule of Three' (tripling) to encourage recycling.",
        "drill_a": "'Reduce waste, protect wildlife, and preserve our planet for future generations.'"
    },

    # =========================================================================
    # MATHEMATICS - LEVEL 1
    # =========================================================================
    {
        "id": "maths-l1-01",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "number",
        "strand_label": "Number & The Number System",
        "dfe_code": "DfE L1.N7",
        "title": "Fractions, Decimals and Percentages (FDP) Equivalents",
        "prompt": "What are the essential benchmark FDP conversions you must memorize for instant recall in non-calculator tests?",
        "context": "Crucial for budgeting, discounts, and rapid mental math checks in Level 1 exams.",
        "steps": [
            "1/2 = 0.5 = 50%",
            "1/4 = 0.25 = 25%  |  3/4 = 0.75 = 75%",
            "1/10 = 0.1 = 10%  |  1/5 = 0.2 = 20%",
            "1/3 ≈ 0.33 = 33.3%  |  2/3 ≈ 0.67 = 66.7%",
            "To convert percentage to decimal: divide by 100 (move decimal 2 places left).",
            "To convert decimal to fraction: place over 10, 100, or 1000 and simplify."
        ],
        "golden_rule": "Divide % by 100 to get decimal. Multiply fraction by (100 ÷ denominator) to find percentage.",
        "exam_trap": "Confusing 0.05 with 50%. 0.05 is 5%; 0.5 is 50%!",
        "drill_q": "Convert 3/5 into both a decimal and a percentage.",
        "drill_a": "3 ÷ 5 = 0.60 (decimal) = 60% (percentage)."
    },
    {
        "id": "maths-l1-02",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L1.MSS16",
        "title": "Perimeter vs Area of Rectangles",
        "prompt": "How do you distinguish between Perimeter and Area of a rectangular space, and what are their respective units?",
        "context": "Flooring tiles (area) vs skirting boards / fencing (perimeter).",
        "steps": [
            "PERIMETER: The total distance all the way around the outside boundary. Add all 4 sides: P = 2L + 2W. Units are linear (cm, m, km).",
            "AREA: The flat surface space inside the boundary. Multiply length by width: A = L × W. Units are squared (cm², m²)."
        ],
        "golden_rule": "Perimeter = Add all sides (fencing). Area = Length × Width (carpeting/grass seed).",
        "exam_trap": "Adding only 2 sides for perimeter! A rectangle has 4 sides — don't forget the other two matching sides.",
        "drill_q": "A room is 5 m long and 3 m wide. Find the perimeter and the area.",
        "drill_a": "Perimeter = 5 + 3 + 5 + 3 = 16 m. Area = 5 × 3 = 15 m²."
    },
    {
        "id": "maths-l1-03",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "data",
        "strand_label": "Handling Information & Data",
        "dfe_code": "DfE L1.H23",
        "title": "Mean and Range from Raw Data",
        "prompt": "How do you calculate the Mean and the Range from a set of numbers?",
        "context": "Calculating average overtime hours, patient wait times, or test scores.",
        "steps": [
            "MEAN: Add all the numbers together to get the Total. Divide the Total by how many numbers there are: Mean = Sum ÷ Count.",
            "RANGE: Find the highest number and the lowest number. Subtract the lowest from the highest: Range = Highest - Lowest."
        ],
        "golden_rule": "Mean is the sharing average (Sum ÷ Count). Range is the spread (Highest - Lowest). Range is NOT an average!",
        "exam_trap": "Including 0 in the count? YES! If one of the numbers is 0, you must still count it when dividing by the total count.",
        "drill_q": "Scores: 4, 7, 0, 9. Find the Mean and the Range.",
        "drill_a": "Sum = 4 + 7 + 0 + 9 = 20. Count = 4. Mean = 20 ÷ 4 = 5. Range = 9 - 0 = 9."
    },
    {
        "id": "maths-l1-04",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "measures",
        "strand_label": "Measures, Shape & Space",
        "dfe_code": "DfE L1.MSS13",
        "title": "Metric Unit Conversions (m, cm, mm, kg, g, L, ml)",
        "prompt": "What are the core metric conversion factors, and do you multiply or divide when changing between units?",
        "context": "Converting recipe ingredients, measuring patients' heights/weights, and liquid volumes.",
        "steps": [
            "LENGTH: 1 cm = 10 mm | 1 m = 100 cm | 1 km = 1,000 m.",
            "WEIGHT / MASS: 1 kg = 1,000 g | 1 tonne = 1,000 kg.",
            "CAPACITY: 1 Litre = 1,000 ml.",
            "RULE OF DIRECTION: Going from BIGGER unit to SMALLER unit (e.g. m → cm) = MULTIPLY (×). Going from SMALLER to BIGGER (e.g. g → kg) = DIVIDE (÷)."
        ],
        "golden_rule": "Big to Small = Multiply (×). Small to Big = Divide (÷). Remember: 100 cm in a metre, 1,000 in 'kilo' or 'milli'.",
        "exam_trap": "Multiplying by 10 instead of 100 for meters to centimeters, or mixing up imperial and metric conversions.",
        "drill_q": "Convert 3.5 kilograms into grams.",
        "drill_a": "3.5 × 1,000 = 3,500 grams."
    },

    # =========================================================================
    # ENGLISH - LEVEL 1
    # =========================================================================
    {
        "id": "eng-l1-01",
        "subject": "english",
        "subject_label": "English",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L1.W12",
        "title": "Email Conventions & Tone (Level 1)",
        "prompt": "What are the required elements for an email at Level 1, and how do you ensure the tone matches the recipient?",
        "context": "Inquiring about job vacancies, confirming appointments, or contacting a supervisor.",
        "steps": [
            "Header Fields: Always write 'To: [email address]' and a clear, descriptive 'Subject: [e.g. Shift Query - 14 Oct]'.",
            "Polite Salutation: 'Dear Mr Thompson,' (formal) or 'Hi Sarah,' (colleague).",
            "Opening Sentence: State the exact purpose immediately.",
            "Structured Paragraphs: 2-3 short, clear paragraphs with connectives.",
            "Closing & Sign-off: 'Kind regards,' followed by your first and last name."
        ],
        "golden_rule": "Never submit an email without both a 'To:' line and a specific 'Subject:' line. Use capital letters for 'I' and names!",
        "exam_trap": "Using text speak (u, plz, thx, coz) or forgetting paragraphs. Functional Skills requires standard English spelling throughout.",
        "drill_q": "What two header lines must you write at the top of every exam email?",
        "drill_a": "1. 'To:' (recipient address) and 2. 'Subject:' (brief reason for the email)."
    },
    {
        "id": "eng-l1-02",
        "subject": "english",
        "subject_label": "English",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "reading",
        "strand_label": "Reading Comprehension",
        "dfe_code": "DfE L1.R4",
        "title": "Organizational & Layout Features",
        "prompt": "What are the key organizational features writers use to help readers locate information quickly, and how do you describe their purpose?",
        "context": "Exam questions asking 'Identify two layout features that make Text A easy to read'.",
        "steps": [
            "Headings and Subheadings: Divide text into logical sections and give readers a quick preview.",
            "Bullet points / Numbered lists: Break complex information into easy-to-digest chunks.",
            "Bold / Italic text: Draw immediate attention to crucial keywords, dates, or warnings.",
            "Images / Captions / Diagrams: Provide visual context and clarity.",
            "Hyperlinks / Navigation tabs: Allow readers to jump straight to relevant sections."
        ],
        "golden_rule": "Name the feature AND explain how it helps the reader (e.g. 'Bullet points are used to separate key rules clearly').",
        "exam_trap": "Just writing 'Font' or 'Words'. You must name specific layout tools: subheadings, bullet points, text boxes, or bold text.",
        "drill_q": "Give two organizational features used in an informational leaflet.",
        "drill_a": "1. Subheadings (to organize sections) and 2. Bullet points (to highlight key instructions)."
    },
    {
        "id": "eng-l1-03",
        "subject": "english",
        "subject_label": "English",
        "level": "l1",
        "level_label": "Level 1",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE L1.W15",
        "title": "Using Commas Correctly (Lists & Introductory Phrases)",
        "prompt": "What are the two most common situations where commas must be used in Level 1 English writing?",
        "context": "Scoring marks on punctuation and sentence clarity.",
        "steps": [
            "1. IN A LIST: Use commas to separate 3 or more items, with 'and' before the final item. (e.g. 'Please bring your passport, proof of address, and certificate.')",
            "2. AFTER AN INTRODUCTORY CLAUSE: Place a comma after an opening time or condition phrase before the main sentence. (e.g. 'Last Thursday, the clinic was closed.' / 'If you need help, please call me.')"
        ],
        "golden_rule": "Commas separate items in lists and separate introductory opening clauses from the main sentence.",
        "exam_trap": "Comma splices! Never use a comma to join two complete sentences: 'I arrived early, the doors were locked' (INCORRECT! Use 'early, but the doors...' or a full stop).",
        "drill_q": "Insert the missing comma: 'Although it was raining the outdoor event went ahead.'",
        "drill_a": "'Although it was raining, the outdoor event went ahead.'"
    },

    # =========================================================================
    # DIGITAL FUNCTIONAL SKILLS (DFSQ / EDSQ) - LEVEL 1 & ENTRY 3
    # =========================================================================
    {
        "id": "dfs-01",
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "l1",
        "level_label": "DFS Level 1",
        "strand": "safety",
        "strand_label": "Skill 5: Being Safe & Responsible Online",
        "dfe_code": "DfE DFS5.1",
        "title": "Spotting Phishing Scams & Social Engineering",
        "prompt": "What are the 5 red flags of a phishing email, and what immediate action must you take if you receive one at work?",
        "context": "Statutory UK GDPR compliance, NHS cybersecurity training, and bank fraud prevention.",
        "steps": [
            "RED FLAG 1: Suspicious sender address (e.g. '@paypal-security-update24.co' instead of '@paypal.com').",
            "RED FLAG 2: Urgent, threatening language ('Account suspended within 24 hours unless you verify').",
            "RED FLAG 3: Generic greeting ('Dear Customer' or 'Dear user' instead of your name).",
            "RED FLAG 4: Suspicious link: Hover over the link without clicking to preview the real URL.",
            "RED FLAG 5: Unprompted attachment (.zip, .exe, or password-protected PDF).",
            "ACTION: Never click links or enter passwords. Report to IT Security / mark as spam."
        ],
        "golden_rule": "Hover before you click. Legitimate organizations like banks and the NHS will never email asking for your password or PIN.",
        "exam_trap": "Trusting the sender's display name. Attackers spoof the name 'HR Department' while the actual address is a fake external mailbox.",
        "drill_q": "You receive an email from 'IT Helpdesk' asking you to click a link to keep your mailbox active. What is the safest first step?",
        "drill_a": "Do not click the link. Hover over the link to verify the true URL, and contact your IT department via verified internal channels."
    },
    {
        "id": "dfs-02",
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "l1",
        "level_label": "DFS Level 1",
        "strand": "create",
        "strand_label": "Skill 2: Creating & Editing (Spreadsheets)",
        "dfe_code": "DfE DFS2.3",
        "title": "Essential Spreadsheet Formulas: SUM, AVERAGE, and AutoFill",
        "prompt": "How do you correctly write a formula in Microsoft Excel or Google Sheets to add a range of cells or calculate an average?",
        "context": "Calculating weekly staff hours, patient attendance, or equipment budget totals.",
        "steps": [
            "RULE 1: Every formula MUST begin with an equals sign (=).",
            "SUM FORMULA: =SUM(B2:B10) adds all numbers from cell B2 down to B10.",
            "AVERAGE FORMULA: =AVERAGE(B2:B10) calculates the mean value of the range.",
            "COLON (:) vs COMMA (,): The colon (:) means a continuous range (from B2 TO B10). A comma (,) means individual cells (B2 AND B10).",
            "AutoFill: Drag the green bottom-right square handle down to copy the formula to other rows."
        ],
        "golden_rule": "Always start with '=' and use a colon for cell ranges: =SUM(A1:A20).",
        "exam_trap": "Forgetting the equals sign, or typing '=SUM(B2+B10)' instead of '=SUM(B2:B10)' or '=B2+B10'.",
        "drill_q": "Write the exact formula to calculate the average score of cells C2 to C15.",
        "drill_a": "=AVERAGE(C2:C15)"
    },
    {
        "id": "dfs-03",
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "e3",
        "level_label": "DFSQ Entry 3",
        "strand": "devices",
        "strand_label": "Skill 1: Using Devices & Handling Info",
        "dfe_code": "DfE DFS1.2",
        "title": "File Management: Folders, Renaming & Cloud Storage",
        "prompt": "How should files be named and organized so they can be easily retrieved, and what is the difference between Local Storage and Cloud Storage?",
        "context": "Managing documents in OneDrive, Google Drive, or local workplace PCs.",
        "steps": [
            "NAMING CONVENTIONS: Use meaningful, consistent names including topic and date (e.g. 'Minutes_TeamMeeting_2026-10-11.docx', NOT 'Doc1.docx').",
            "FOLDER HIERARCHY: Create nested folders (e.g. Work > 2026 > October > Invoices).",
            "LOCAL STORAGE: Saved only on the physical computer/hard drive (cannot be accessed from other devices).",
            "CLOUD STORAGE: Saved on secure remote internet servers (OneDrive, Google Drive), allowing access from any internet-connected device."
        ],
        "golden_rule": "Meaningful names + nested folders = instant retrieval. Cloud storage protects your work if your computer breaks or is lost.",
        "exam_trap": "Leaving files named 'Untitled.docx' or saving everything onto the Desktop without structured folders.",
        "drill_q": "Give two key advantages of saving your coursework in Cloud Storage instead of a local USB stick.",
        "drill_a": "1. Automatic backup (won't be lost if USB is misplaced/damaged); 2. Accessible from any phone, laptop, or college computer."
    },
    {
        "id": "dfs-04",
        "subject": "digital",
        "subject_label": "Digital Skills",
        "level": "l1",
        "level_label": "DFS Level 1",
        "strand": "transact",
        "strand_label": "Skill 4: Transacting Online",
        "dfe_code": "DfE DFS4.2",
        "title": "Secure Online Payments & Two-Factor Authentication (2FA)",
        "prompt": "How can you tell if a payment website is secure, and how does Two-Factor Authentication protect your account?",
        "context": "Paying for exam registrations, booking online services, or company procurement.",
        "steps": [
            "CHECK 1: URL begins with 'https://' (the 's' stands for secure encrypted connection).",
            "CHECK 2: Padlock icon displayed in the browser address bar.",
            "TWO-FACTOR AUTHENTICATION (2FA): Requires two separate layers of identification (e.g. password + one-time code sent to your phone/authenticator app).",
            "Even if a hacker steals your password, they cannot access your account without the second factor."
        ],
        "golden_rule": "Look for HTTPS + Padlock. Always enable 2FA for banking and email accounts.",
        "exam_trap": "Assuming an email with a padlock graphic means the sender is secure. Check the browser address bar directly, not email images!",
        "drill_q": "What two credentials are used in Two-Factor Authentication?",
        "drill_a": "Something you know (your password) and something you have (a temporary code sent to your mobile phone or authenticator app)."
    },

    # =========================================================================
    # ENTRY LEVEL 3 - MATHEMATICS & ENGLISH FOUNDATIONS
    # =========================================================================
    {
        "id": "maths-e3-01",
        "subject": "maths",
        "subject_label": "Mathematics",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand": "number",
        "strand_label": "Number & The Number System",
        "dfe_code": "DfE E3.N1",
        "title": "Rounding to the Nearest 10 and 100",
        "prompt": "What is the golden rule for rounding numbers to the nearest 10 or 100?",
        "context": "Estimating shopping totals, quick workplace counts, and checking calculations.",
        "steps": [
            "Identify the digit in the place value you are rounding to.",
            "Look at the decider digit immediately to its right.",
            "If the decider digit is 4 or less, ROUND DOWN (leave the digit alone).",
            "If the decider digit is 5 or more, ROUND UP (add 1 to the digit).",
            "Change all digits to the right into zeros."
        ],
        "golden_rule": "5 and above, give it a shove (round up). 4 and below, let it go (round down).",
        "exam_trap": "Rounding 245 to the nearest 100 and getting 200 because you looked at the 5! Look at the digit immediately to the right of hundreds (the 4 in tens), so 245 rounds to 200.",
        "drill_q": "Round 368 to: 1) the nearest 10; 2) the nearest 100.",
        "drill_a": "1) Nearest 10: Look at 8 → rounds up to 370. 2) Nearest 100: Look at 6 → rounds up to 400."
    },
    {
        "id": "eng-e3-01",
        "subject": "english",
        "subject_label": "English",
        "level": "e3",
        "level_label": "Entry Level 3",
        "strand": "writing",
        "strand_label": "Writing Composition & SPaG",
        "dfe_code": "DfE E3.W3",
        "title": "Capital Letters & Punctuation Rules (Entry 3)",
        "prompt": "When must you always use a capital letter in English writing?",
        "context": "Writing notes, simple forms, or short emails without losing marks for basic punctuation.",
        "steps": [
            "RULE 1: The first word of every sentence.",
            "RULE 2: The personal pronoun 'I' (always capital, never 'i').",
            "RULE 3: Proper nouns: Names of people (Sarah, Dr Smith), places (London, High Street), days of the week (Monday), months (October), and holidays.",
            "End every statement with a full stop (.), question with a question mark (?), and exclamation with (!)."
        ],
        "golden_rule": "Names, Places, Days, Months, Sentence Starters, and the letter 'I' ALWAYS get a capital letter.",
        "exam_trap": "Writing lowercase 'i' when talking about yourself ('Yesterday i went...'). This is an instant error on Functional Skills exams.",
        "drill_q": "Correct the capitals in this sentence: 'on tuesday, i visited my sister in manchester.'",
        "drill_a": "'On Tuesday, I visited my sister in Manchester.'"
    }
]

def generate_js_data(output_dir):
    js_path = os.path.join(output_dir, "assets", "js", "revision_cards_data.js")
    os.makedirs(os.path.dirname(js_path), exist_ok=True)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("/**\n * Master Functional Skills - Official Revision Cards Data\n */\n")
        f.write("window.MFS_REVISION_CARDS = ")
        f.write(json.dumps(ALL_CARDS, indent=2, ensure_ascii=False))
        f.write(";\n")
    print(f"Updated JS data: {js_path} ({len(ALL_CARDS)} cards)")

def render_printable_html(cards, deck_title):
    """
    Renders A4 duplex-compatible print pages:
    - 4 cards per page (2 columns x 2 rows)
    - Front Page (Cards 1, 2, 3, 4)
    - Back Page (Cards 2, 1, 4, 3) for perfect duplex alignment on flip-long-edge!
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{deck_title} - Printable Revision Cards | Master Functional Skills</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 10mm;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #ffffff;
      color: #0f172a;
    }}
    .sheet-page {{
      width: 190mm;
      height: 277mm;
      page-break-after: always;
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 6mm;
      position: relative;
      margin-bottom: 20mm;
    }}
    @media print {{
      .sheet-page {{
        margin-bottom: 0;
      }}
      .no-print {{
        display: none !important;
      }}
    }}
    /* Card Print Box */
    .print-card {{
      border: 1.5px solid #cbd5e1;
      border-radius: 12px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #ffffff;
      position: relative;
      overflow: hidden;
    }}
    .print-card.back-face {{
      background: #fafaf9;
      border-color: #94a3b8;
    }}
    .card-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}
    .badge-sub {{
      font-size: 8pt;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      color: #ffffff;
    }}
    .badge-maths {{ background: #2563eb; }}
    .badge-english {{ background: #7c3aed; }}
    .badge-digital {{ background: #059669; }}
    .badge-dfe-code {{
      font-family: monospace;
      font-size: 8pt;
      font-weight: 700;
      color: #334155;
      background: #f1f5f9;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px dashed #94a3b8;
    }}
    .card-h2 {{
      font-size: 11pt;
      font-weight: 800;
      color: #070d1e;
      margin: 0 0 6px 0;
      line-height: 1.25;
    }}
    .card-stem {{
      font-size: 9pt;
      font-weight: 700;
      color: #1e3a8a;
      background: #eff6ff;
      border-left: 3px solid #2563eb;
      padding: 6px 8px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 6px;
      line-height: 1.35;
    }}
    .card-context {{
      font-size: 7.8pt;
      color: #475569;
      background: #f8fafc;
      padding: 5px 8px;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      line-height: 1.3;
    }}
    /* Back Face Styles */
    .steps-ol {{
      margin: 0 0 6px 0;
      padding-left: 14px;
      font-size: 8pt;
      line-height: 1.35;
    }}
    .steps-ol li {{
      margin-bottom: 3px;
    }}
    .golden-box {{
      background: #ecfdf5;
      border: 1px solid #10b981;
      border-radius: 6px;
      padding: 4px 6px;
      font-size: 7.8pt;
      font-weight: 700;
      color: #065f46;
      margin-bottom: 5px;
    }}
    .trap-box {{
      background: #fff1f2;
      border: 1px solid #f43f5e;
      border-radius: 6px;
      padding: 4px 6px;
      font-size: 7.5pt;
      color: #9f1239;
      line-height: 1.25;
      margin-bottom: 5px;
    }}
    .drill-mini {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 4px 6px;
      font-size: 7.5pt;
      line-height: 1.25;
    }}
    .footer-bar {{
      display: flex;
      justify-content: space-between;
      border-top: 1px solid #e2e8f0;
      padding-top: 4px;
      font-size: 7pt;
      color: #64748b;
      margin-top: 4px;
    }}
    .cut-line-v {{
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      border-left: 1px dashed #cbd5e1;
      pointer-events: none;
    }}
    .cut-line-h {{
      position: absolute;
      left: 0;
      right: 0;
      top: 50%;
      border-top: 1px dashed #cbd5e1;
      pointer-events: none;
    }}
  </style>
</head>
<body>
  <div class="no-print" style="background:#070d1e; color:#fff; padding:12px 20px; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <strong>Master Functional Skills</strong> — {deck_title} (Printable Duplex Sheet)
    </div>
    <div>
      <button onclick="window.print()" style="background:#00b87c; color:#fff; font-weight:800; border:none; padding:8px 16px; border-radius:6px; cursor:pointer;">
        Print to Paper / PDF
      </button>
    </div>
  </div>
"""

    # Chunk into groups of 4 cards
    for i in range(0, len(cards), 4):
        chunk = cards[i:i+4]
        while len(chunk) < 4:
            chunk.append(None)

        # FRONT PAGE (Cards 0, 1, 2, 3)
        html += '<div class="sheet-page">\n'
        html += '  <div class="cut-line-v"></div><div class="cut-line-h"></div>\n'
        for card in chunk:
            if card:
                html += f"""
  <div class="print-card">
    <div>
      <div class="card-meta-row">
        <span class="badge-sub badge-{card['subject']}">{card['subject_label']} {card['level_label']}</span>
        <span class="badge-dfe-code">{card['dfe_code']}</span>
      </div>
      <div class="card-h2">{card['title']}</div>
      <div class="card-stem">{card['prompt']}</div>
      <div class="card-context">{card['context']}</div>
    </div>
    <div class="footer-bar">
      <span>Master Functional Skills • Pocket Cards</span>
      <span>Turn Over For Stepped Solution ➔</span>
    </div>
  </div>
"""
            else:
                html += '  <div class="print-card" style="visibility:hidden;"></div>\n'
        html += '</div>\n'

        # BACK PAGE (Duplex Swap: Cards 1, 0, 3, 2 for flip on long edge)
        back_chunk = [chunk[1], chunk[0], chunk[3], chunk[2]]
        html += '<div class="sheet-page">\n'
        html += '  <div class="cut-line-v"></div><div class="cut-line-h"></div>\n'
        for card in back_chunk:
            if card:
                steps_html = "".join([f"<li>{s}</li>" for s in card['steps']])
                html += f"""
  <div class="print-card back-face">
    <div>
      <div class="card-meta-row">
        <span style="font-size:7.5pt; font-weight:800; color:#1e293b; text-transform:uppercase;">Model Solution: {card['title']}</span>
        <span class="badge-dfe-code">{card['dfe_code']}</span>
      </div>
      <ol class="steps-ol">
        {steps_html}
      </ol>
      <div class="golden-box">★ {card['golden_rule']}</div>
      <div class="trap-box">⚠️ <strong>TRAP:</strong> {card['exam_trap']}</div>
      <div class="drill-mini"><strong>Drill:</strong> {card['drill_q']}<br><span style="color:#0369a1; font-weight:700;">Ans: {card['drill_a']}</span></div>
    </div>
    <div class="footer-bar">
      <span>Official Tutor Model Answer</span>
      <span>{card['level_label']} Specification</span>
    </div>
  </div>
"""
            else:
                html += '  <div class="print-card back-face" style="visibility:hidden;"></div>\n'
        html += '</div>\n'

    html += "</body>\n</html>"
    return html

def main():
    base_dir = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
    generate_js_data(base_dir)

    downloads_dir = os.path.join(base_dir, "assets", "downloads")
    os.makedirs(downloads_dir, exist_ok=True)

    decks = [
        ("maths-l2", "Maths Level 2 Pocket Revision Cards", [c for c in ALL_CARDS if c['subject'] == 'maths' and c['level'] == 'l2']),
        ("maths-l1", "Maths Level 1 Pocket Revision Cards", [c for c in ALL_CARDS if c['subject'] == 'maths' and c['level'] == 'l1']),
        ("english-l2", "English Level 2 Pocket Revision Cards", [c for c in ALL_CARDS if c['subject'] == 'english' and c['level'] == 'l2']),
        ("english-l1", "English Level 1 Pocket Revision Cards", [c for c in ALL_CARDS if c['subject'] == 'english' and c['level'] == 'l1']),
        ("digital-skills", "Digital Functional Skills Revision Cards", [c for c in ALL_CARDS if c['subject'] == 'digital']),
        ("entry-level-3", "Entry Level 3 Foundation Revision Cards", [c for c in ALL_CARDS if c['level'] == 'e3']),
        ("all-cards", "Master Functional Skills Complete Revision Cards Deck", ALL_CARDS)
    ]

    for slug, title, cards in decks:
        if not cards:
            continue
        html_content = render_printable_html(cards, title)
        html_path = os.path.join(base_dir, f"printable-{slug}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated printable HTML: {html_path}")

        # Compile PDF using headless chromium binary directly (bypassing wrapper flag locks)
        pdf_name = f"MasterFunctionalSkills_Revision_Cards_{slug.replace('-', '_')}.pdf"
        pdf_path = os.path.join(downloads_dir, pdf_name)
        import tempfile
        tmp_dir = tempfile.mkdtemp(prefix="chrome_pdf_")
        cmd = [
            "/usr/lib/chromium/chromium",
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--user-data-dir={tmp_dir}",
            f"--print-to-pdf={pdf_path}",
            f"file://{html_path}"
        ]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
            if os.path.exists(pdf_path):
                print(f"  ✓ Successfully compiled PDF: {pdf_name} ({os.path.getsize(pdf_path)} bytes)")
            else:
                print(f"  ✗ Failed to compile PDF {pdf_path}: {res.stderr.decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"  ✗ Exception while compiling PDF {pdf_path}: {e}")
        finally:
            import shutil
            shutil.rmtree(tmp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
