#!/usr/bin/env python3
import maths_domain3_measures

all_d3 = list(maths_domain3_measures.TOPICS_DOMAIN3)

more_d3 = [
    {
        "filename": "functional-skills-weight.html",
        "clean_topic": "Weight & Mass",
        "intro_lead": "Measure and calculate mass in grams, kilograms, and tonnes, solve postal package and baggage allowance limits, and convert between metric and imperial weight.",
        "next_file": "functional-skills-capacity.html",
        "next_name": "Capacity & Volume Units",
        "spec_points": [
            ("L1.18 / L2.20", "Calculate and convert with units of weight and mass in practical contexts.")
        ],
        "golden_rules": [
            {
                "icon": "fa-scale-balanced",
                "title": "Golden Rule 1: The 1,000 Factor for Mass",
                "desc": "1 tonne = 1,000 kg • 1 kg = 1,000 g • 1 g = 1,000 mg. Always multiply by 1,000 to go down a unit and divide by 1,000 to go up.",
                "badge": "Tonnes × 1000 → Kilograms × 1000 → Grams"
            },
            {
                "icon": "fa-truck-ramp-box",
                "title": "Golden Rule 2: Gross Weight vs Net Weight vs Tare Weight",
                "desc": "Gross Weight = Total weight (packaging + goods). Tare Weight = Weight of empty container. Net Weight = Goods only (Gross - Tare).",
                "badge": "Gross Weight = Net Goods + Tare Packaging"
            }
        ],
        "skills": [
            {
                "title": "Weight Unit Equivalences",
                "summary": "Powers of 1,000 in metric mass.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>3.4 kg = 3,400 grams.</li>
                    <li>250 grams = 0.25 kg.</li>
                    <li>1.8 tonnes = 1,800 kg.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Depot Freight Pallet Gross Weight Compliance",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Logistics & Freight Transport",
                "question": "A wooden freight pallet weighs <strong>24 kg</strong> when empty. It is loaded with <strong>45 boxes</strong> of clinical supplies. Each box has a mass of <strong>800 grams</strong>.<br>(a) Calculate the total gross weight of the loaded pallet in kilograms.<br>(b) The tail-lift has a safe working load of 75 kg. Can this pallet be safely lifted?",
                "steps": [
                    ("Step 1", "Calculate total weight of boxes in grams", "45 boxes × 800 g = 36,000 grams.", "M1: Multi-item mass multiplication"),
                    ("Step 2", "Convert box mass to kilograms", "36,000 g ÷ 1,000 = 36 kg.", "M1: Grams to kilograms conversion"),
                    ("Step 3", "Calculate gross pallet weight and evaluate limit", "Gross weight = 36 kg (boxes) + 24 kg (pallet) = 60 kg.<br>60 kg < 75 kg. Yes, the tail-lift can safely lift the pallet.", "A1: Accurate gross weight and safety confirmation")
                ],
                "final_answer": "(a) Gross Weight = 60 kg | (b) Yes, 60 kg is within the 75 kg safe working load.",
                "tutor_tip": "Notice how converting 36,000 g to 36 kg first makes adding the 24 kg pallet effortless."
            }
        ],
        "examiner_traps": [
            {
                "title": "Adding Grams and Kilograms Directly",
                "desc": "Adding 24 kg + 36,000 g = 36,024 is an error caused by failing to convert to common units.",
                "fix": "Always convert to the same unit before adding."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A parcel courier van can carry a maximum payload of 1.2 tonnes. The driver has loaded 950 kg of parcels. Can a further 320 kg parcel be loaded without exceeding the limit?",
                "solution_steps": "1. Max payload = 1.2 tonnes = 1,200 kg.<br>2. Current + new parcel = 950 + 320 = 1,270 kg.<br>3. 1,270 kg > 1,200 kg. No, it exceeds the limit by 70 kg.",
                "correct_answer": "No, it exceeds the payload limit by 70 kg (1,270 kg > 1,200 kg).",
                "tutor_tip": "Convert 1.2 tonnes to 1,200 kg before comparing."
            }
        ]
    },
    {
        "filename": "functional-skills-capacity.html",
        "clean_topic": "Capacity & Liquid Volume Units",
        "intro_lead": "Measure and convert liquid capacity in millilitres, centilitres, and litres, calculate container capacities, and solve clinical medication fluid dosage problems.",
        "next_file": "functional-skills-perimeter.html",
        "next_name": "Perimeter",
        "spec_points": [
            ("L1.18 / L2.20", "Calculate and convert with metric units of capacity and volume.")
        ],
        "golden_rules": [
            {
                "icon": "fa-glass-water",
                "title": "Golden Rule 1: 1 Litre = 1,000 Millilitres",
                "desc": "To convert litres to millilitres, multiply by 1,000. To convert millilitres to litres, divide by 1,000. Remember: 1 cm³ of volume holds exactly 1 ml of liquid.",
                "badge": "1 Litre = 1,000 ml | 1,000 cm³ = 1 Litre"
            },
            {
                "icon": "fa-droplet",
                "title": "Golden Rule 2: 1 Centilitre (cl) = 10 Millilitres",
                "desc": "Catering and beverage recipes often use centilitres: 75 cl = 750 ml = 0.75 litres.",
                "badge": "1 cl = 10 ml | 100 cl = 1 Litre"
            }
        ],
        "skills": [
            {
                "title": "Converting Metric Capacity Units",
                "summary": "Summary of liquid capacity conversions.",
                "content_html": """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li>2.5 litres = 2,500 ml.</li>
                    <li>750 ml = 0.75 litres.</li>
                    <li>33 cl = 330 ml = 0.33 litres.</li>
                  </ul>
                </div>
                """
            }
        ],
        "worked_models": [
            {
                "title": "Hospital Ward Oral Rehydration Fluid Dispensing",
                "marks": "3 Marks (Pearson Edexcel Level 1/2)",
                "context": "Clinical Ward Fluid Administration",
                "question": "A care home nurse prepares a <strong>2-litre jug</strong> of oral rehydration fluid. She pours <strong>150 ml</strong> into each resident's cup.<br>(a) How many full cups can she pour from the jug?<br>(b) How many millilitres of fluid remain in the jug?",
                "steps": [
                    ("Step 1", "Convert jug capacity from litres to millilitres", "2 litres × 1,000 = 2,000 ml.", "M1: Litres to ml conversion"),
                    ("Step 2", "Divide total volume by single cup volume", "2,000 ml ÷ 150 ml = 13.333... (13 remainder 50).", "M1: Division setup and execution"),
                    ("Step 3", "State whole cups and remaining volume", "Full cups = 13 cups.<br>Volume used = 13 × 150 ml = 1,950 ml.<br>Remaining = 2,000 - 1,950 = 50 ml.", "A1: Accurate cups and remainder in ml")
                ],
                "final_answer": "(a) 13 full cups | (b) 50 ml remains in the jug.",
                "tutor_tip": "Notice you cannot pour 13.33 cups; you round down to 13 full cups and 50 ml left over."
            }
        ],
        "examiner_traps": [
            {
                "title": "Dividing 2 by 150 Without Converting to Millilitres",
                "desc": "Doing 2 ÷ 150 gives 0.0133 — always convert litres to millilitres first!",
                "fix": "Both numbers must be in millilitres before dividing."
            }
        ],
        "practice_questions": [
            {
                "marks": "2 Marks",
                "question": "A bottle of cough linctus contains 300 ml. The recommended adult dose is 15 ml three times daily. How many days will this bottle last?",
                "solution_steps": "1. Daily dose = 15 ml × 3 = 45 ml per day.<br>2. Total days = 300 ÷ 45 = 6.666... days.<br>3. It will last for 6 full days (with 30 ml left over for day 7).",
                "correct_answer": "6 full days (or 6.67 days)",
                "tutor_tip": "Calculate daily total first before dividing the bottle size."
            }
        ]
    }
]

all_d3.extend(more_d3)

with open("/home/subi/Projects/masterfunctionalskills.co.uk/maths_domain3_measures.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write('"""Maths Domain 3: Measures, Time, Speed & Conversions (7 Core Topics)"""\n\n')
    f.write("TOPICS_DOMAIN3 = " + repr(all_d3) + "\n")

print(f"Domain 3 complete with {len(all_d3)} topics!")
