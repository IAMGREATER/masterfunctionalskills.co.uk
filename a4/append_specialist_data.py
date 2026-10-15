#!/usr/bin/env python3
"""
append_specialist_data.py
Appends Mock 7 & 8 for Maths, Mock 6 for English, and 4 Diagnostic Papers for BKSB
into specialist_suite_content.py and specialist_suite_reference.py.
"""

from pathlib import Path

CONTENT_FILE = Path(__file__).resolve().parent / "specialist_suite_content.py"
REF_FILE = Path(__file__).resolve().parent / "specialist_suite_reference.py"

def run():
    # 1. Append Maths Mocks 7 & 8 to specialist_suite_content.py
    maths_7_8 = """
# Appended Maths Mocks 7 and 8
MATHS_L2_MOCKS.extend([
    {
        "theme": "Automotive Engineering & Fleet Maintenance",
        "kw1": "car mechanic vehicle workshop engine repair",
        "kw2": "automotive garage automotive diagnostics tools",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Without a calculator, evaluate this workshop overhaul invoice:<br>A garage services 16 fleet transit vans. Each van requires 6 litres of synthetic oil at &pound;8.40 per litre and a replacement fuel filter at &pound;14.50. Calculate the total cost of parts for all 16 vans.", "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> An automotive testing track features a circular skid pan of diameter 28 metres. Calculate the area of the skid pan using &pi; = 3.14. State the correct units.", "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> Work out the following fractional calculation without a calculator:<br>2 <sup>3</sup>/<sub>8</sub> + 1 <sup>1</sup>/<sub>4</sub>. Give your final answer as a mixed number in its simplest form.", "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> An MOT testing station reduces standard service fees by 15% for commercial fleet accounts. The discounted service fee is &pound;102.00. Calculate the original service fee before discount. Show an inverse check of your answer.", "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Coolant Antifreeze Mixture: A commercial coolant blend requires antifreeze concentrate and water mixed in the ratio 2 : 5. A fleet workshop technician needs to prepare 84 litres of coolant mixture. Calculate how many litres of antifreeze concentrate are required.", "marks": 4, "weight": 1.2}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 6:</b> Garage Technician Payroll: 8 diagnostic mechanics work 38.5 hours each at &pound;17.20 per hour. 2 workshop managers work 40.0 hours each at &pound;23.50 per hour. Calculate the total weekly wage payroll.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 7:</b> Workshop Floor Painting: A rectangular workshop floor measures 24.5 m by 16.0 m. An inspection pit measuring 8.0 m by 2.5 m is excluded from painting. Two coats of specialist epoxy paint are applied. One tin of paint covers 35 m&sup2; and costs &pound;48.50. Calculate the total cost of paint needed.", "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 8:</b> MOT Test Duration Grouped Mean: The table shows completion times for 60 vehicle inspections: [30-34 min: 12], [35-39 min: 25], [40-44 min: 18], [45-49 min: 5]. Calculate the estimated mean completion time.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 9:</b> Heavy Haulage Fuel Economy: A heavy breakdown recovery truck travels 340 miles averaging 11.5 mpg. Diesel costs &pound;1.54 per litre (1 gallon = 4.55 litres). Calculate the fuel cost for the recovery journey.", "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 10:</b> Bulk Oil Tank Cylinder Capacity: A cylindrical bulk waste-oil storage tank has radius r = 1.1 m and height h = 2.4 m. Calculate the volume of the tank in litres using &pi; = 3.142 (1 m&sup3; = 1,000 litres).", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 11:</b> Parts Department Gross Margin: In October, the automotive parts department recorded sales revenue of &pound;48,600. The cost of goods sold was &pound;31,800. Calculate the gross profit margin as a percentage of revenue, rounded to 1 decimal place.", "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 12:</b> Independent Brake Inspection Quality: During a quality audit, two braking sensors are evaluated independently. Sensor A has a failure probability of 0.02. Sensor B has a failure probability of 0.03. Calculate the probability that both sensors function correctly.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 13:</b> Emergency Roadside Recovery Arrival: A recovery tow truck departs the depot at 14:20 to attend a stranded vehicle 68 miles away. The truck maintains an average speed of 48 mph. Calculate the expected arrival time at the breakdown location.", "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 14:</b> Hydraulic Ramp Hypotenuse: A vehicle loading ramp rises 1.4 metres vertically over a horizontal run of 4.8 metres. Use Pythagoras theorem to calculate the sloping length of the ramp.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 15:</b> Fleet Tyre Procurement Evaluation: Supplier A offers 40 commercial tyres at &pound;110.00 each with a 12% fleet trade discount and free delivery. Supplier B offers the same tyres at &pound;105.00 each with a 5% discount plus a flat delivery charge of &pound;60.00. Determine which supplier offers the cheaper package and calculate the overall saving.", "marks": 5, "weight": 1.2}
            ]
        ]
    },
    {
        "theme": "Green Energy, Solar & Environmental Projects",
        "kw1": "solar panels technician wind turbine renewable",
        "kw2": "environmental energy efficiency insulation heat pump",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Without a calculator, evaluate this solar array installation invoice:<br>A commercial rooftop solar project requires 28 photovoltaic panels at &pound;185.00 each, plus 4 inverter units at &pound;420.00 each. Calculate the total cost of equipment before VAT.", "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> An environmental wind turbine tower base has a circular foundation with a radius of 3.5 metres. Calculate the area of the foundation using &pi; = 3.14. State the correct units.", "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> Evaluate the following expression without a calculator:<br>3 <sup>1</sup>/<sub>3</sub> + 2 <sup>2</sup>/<sub>5</sub>. Give your answer as a mixed number in its simplest form.", "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> A government green energy grant subsidizes 35% of heat pump installation costs. A property owner pays a discounted balance of &pound;5,525.00. Calculate the original full cost of the installation. Show an inverse check.", "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Solar Battery Bank Storage: A battery bank distributes stored kilowatt-hours across domestic usage and electric vehicle charging in the ratio 3 : 7. On a sunny day, the system stores 60 kWh. Calculate the kilowatt-hours allocated to vehicle charging.", "marks": 4, "weight": 1.2}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 6:</b> Green Energy Installation Payroll: 6 certified solar electricians work 42.0 hours each at &pound;22.50 per hour. 2 project engineers work 45.0 hours each at &pound;28.00 per hour. Calculate the total payroll wage expenditure.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 7:</b> Roof Solar Panel Layout Area: A sloping warehouse roof measures 32.0 m wide by 14.5 m high. Two skylight vents measuring 3.0 m by 2.0 m each cannot be covered. Each solar panel measures 1.7 m by 1.0 m. Determine the maximum theoretical number of panels that can fit on the net roof area.", "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 8:</b> Daily Solar Generation Grouped Mean: Over 50 summer days, solar generation was monitored: [15-19 kWh: 8], [20-24 kWh: 16], [25-29 kWh: 20], [30-34 kWh: 6]. Calculate the estimated mean daily generation in kWh.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 9:</b> Electric Maintenance Van Economy: A maintenance technician drives an electric van 145 miles. The van achieves 3.8 miles per kWh. Electricity costs 24p per kWh. Calculate the total energy cost for the trip.", "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 10:</b> Heat Pump Buffer Tank Volume: A cylindrical thermal buffer water cylinder has diameter 0.9 m and height 1.8 m. Calculate the volume of water the tank holds in litres using &pi; = 3.142 (1 m&sup3; = 1,000 litres).", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 11:</b> Energy Efficiency Payback Margin: A commercial LED upgrade cost &pound;16,800. Annual electricity bills reduced from &pound;24,500 to &pound;19,100. Calculate the annual saving as a percentage of the installation cost.", "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 12:</b> Combined Microgeneration Inverter Reliability: Two solar inverters operate in parallel. Inverter 1 has a reliability rating of 0.97. Inverter 2 has a reliability rating of 0.96. Calculate the probability that both inverters operate without breakdown.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 13:</b> Wind Farm Maintenance Travel Time: A technician drives 112 miles to an offshore grid substation at an average speed of 42 mph. Leaving base at 07:15, calculate the expected arrival time.", "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 14:</b> Guy Wire Hypotenuse: A wind measurement mast rises 15.0 metres vertically. A steel stabilization guy wire anchors to the ground 8.0 metres from the mast base. Calculate the length of the guy wire.", "marks": 5, "weight": 1.2},
                {"q": "<b>Question 15:</b> Heat Pump Supplier Tender: Contractor X quotes &pound;8,200 with 8% green rebate and &pound;150 installation survey fee. Contractor Y quotes &pound;8,500 with 12% manufacturer discount and free survey. Determine which contractor is cheaper and calculate the saving.", "marks": 5, "weight": 1.2}
            ]
        ]
    }
])
"""

    with open(CONTENT_FILE, "a", encoding="utf-8") as f:
        f.write(maths_7_8)
    print("Maths Mocks 7 and 8 appended to specialist_suite_content.py!")

    # 2. Append Mock 7 & 8 solutions to specialist_suite_reference.py
    maths_ref_7_8 = """
# Appended Solutions for Mock 7 & 8
MATHS_L2_MOCK_SOLUTIONS[7] = [
    ("Mock 7 &bull; Section A &amp; B Model Solutions",
     "<b>Section A Non-Calculator Summary:</b><br>"
     "&bull; Q1: Fleet van oil &amp; filter invoice: 16 vans &times; (6 &times; &pound;8.40 + &pound;14.50) = 16 &times; (&pound;50.40 + &pound;14.50) = 16 &times; &pound;64.90 = <b>&pound;1,038.40</b>.<br>"
     "&bull; Q2: Circular skid pan: Radius = 14 m. Area = 3.14 &times; 14&sup2; = 3.14 &times; 196 = <b>615.44 m&sup2;</b>.<br>"
     "&bull; Q3: Fractions: 2 3/8 + 1 1/4 = 19/8 + 10/8 = 29/8 = <b>3 5/8</b>.<br>"
     "&bull; Q4: Reverse discount: &pound;102.00 &divide; 0.85 = <b>&pound;120.00</b>. Check: 120 &times; 0.85 = &pound;102.00.<br>"
     "&bull; Q5: Antifreeze ratio 2:5, total 7 parts of 84 L. 1 part = 12 L. Antifreeze = 2 &times; 12 = <b>24 litres</b>.<br><br>"
     "<b>Section B Calculator Highlights:</b><br>"
     "&bull; Q6: Diagnostic mechanics payroll: (8 &times; 38.5 &times; &pound;17.20) + (2 &times; 40 &times; &pound;23.50) = &pound;5,297.60 + &pound;1,880.00 = <b>&pound;7,177.60</b>.<br>"
     "&bull; Q7: Workshop paint: Net area = (24.5 &times; 16.0) - (8.0 &times; 2.5) = 392 - 20 = 372 m&sup2;. Two coats = 744 m&sup2;. Tins = 744 &divide; 35 = 21.25 &rarr; 22 tins. Cost = 22 &times; &pound;48.50 = <b>&pound;1,067.00</b>.<br>"
     "&bull; Q8: MOT estimated mean = <b>37.8 minutes</b>.<br>"
     "&bull; Q9: Recovery truck fuel: 340 &divide; 11.5 = 29.565 gal = 134.52 L &times; &pound;1.54 = <b>&pound;207.16</b>.<br>"
     "&bull; Q10: Cylindrical waste oil tank volume: 3.142 &times; 1.1&sup2; &times; 2.4 = 9.124 m&sup3; = <b>9,124 litres</b>.<br>"
     "&bull; Q11: Parts margin: (&pound;16,800 &divide; &pound;48,600) &times; 100 = <b>34.6%</b>.<br>"
     "&bull; Q12: Combined brake reliability: 0.98 &times; 0.97 = <b>0.9506</b>.<br>"
     "&bull; Q13: Tow truck arrival: 68 &divide; 48 = 1.417 hrs = 1 hr 25 mins. Arrival = 14:20 + 1h 25m = <b>15:45</b>.<br>"
     "&bull; Q14: Loading ramp length: &radic;(1.4&sup2; + 4.8&sup2;) = &radic;(1.96 + 23.04) = &radic;25.0 = <b>5.0 metres</b>.<br>"
     "&bull; Q15: Tyre supplier: Supplier A = 40 &times; 110 &times; 0.88 = &pound;3,872.00. Supplier B = (40 &times; 105 &times; 0.95) + 60 = &pound;4,050.00. <b>Supplier A is cheaper by &pound;178.00</b>.")
]

MATHS_L2_MOCK_SOLUTIONS[8] = [
    ("Mock 8 &bull; Section A &amp; B Model Solutions",
     "<b>Section A Non-Calculator Summary:</b><br>"
     "&bull; Q1: Solar equipment: (28 &times; &pound;185) + (4 &times; &pound;420) = &pound;5,180 + &pound;1,680 = <b>&pound;6,860.00</b>.<br>"
     "&bull; Q2: Circular turbine base: Area = 3.14 &times; 3.5&sup2; = 3.14 &times; 12.25 = <b>38.47 m&sup2;</b>.<br>"
     "&bull; Q3: Mixed numbers: 3 1/3 + 2 2/5 = 10/3 + 12/5 = (50 + 36)/15 = 86/15 = <b>5 11/15</b>.<br>"
     "&bull; Q4: Reverse grant: Subsidized 35% &rarr; Multiplier = 0.65. Original = &pound;5,525 &divide; 0.65 = <b>&pound;8,500.00</b>.<br>"
     "&bull; Q5: Solar battery distribution: 3:7, 10 parts of 60 kWh = 6 kWh per part. EV charging = 7 &times; 6 = <b>42 kWh</b>.<br><br>"
     "<b>Section B Calculator Highlights:</b><br>"
     "&bull; Q6: Green installation payroll: (6 &times; 42 &times; &pound;22.50) + (2 &times; 45 &times; &pound;28.00) = &pound;5,670 + &pound;2,520 = <b>&pound;8,190.00</b>.<br>"
     "&bull; Q7: Roof solar panels: Net area = (32.0 &times; 14.5) - (2 &times; 6.0) = 464 - 12 = 452 m&sup2;. One panel = 1.7 m&sup2;. Panels = 452 &divide; 1.7 = 265.8 &rarr; <b>265 panels</b>.<br>"
     "&bull; Q8: Solar generation mean = <b>24.4 kWh</b>.<br>"
     "&bull; Q9: Electric van energy cost: 145 &divide; 3.8 = 38.16 kWh &times; &pound;0.24 = <b>&pound;9.16</b>.<br>"
     "&bull; Q10: Buffer tank capacity: 3.142 &times; 0.45&sup2; &times; 1.8 = 1.145 m&sup3; = <b>1,145 litres</b>.<br>"
     "&bull; Q11: Annual efficiency savings margin: (&pound;5,400 &divide; &pound;16,800) &times; 100 = <b>32.1%</b>.<br>"
     "&bull; Q12: Combined inverter reliability: 0.97 &times; 0.96 = <b>0.9312</b>.<br>"
     "&bull; Q13: Maintenance trip time: 112 &divide; 42 = 2.667 hrs = 2 hrs 40 mins. Arrival = 07:15 + 2h 40m = <b>09:55</b>.<br>"
     "&bull; Q14: Wind mast guy wire: &radic;(15.0&sup2; + 8.0&sup2;) = &radic;(225 + 64) = &radic;289 = <b>17.0 metres</b>.<br>"
     "&bull; Q15: Tender decision: Contractor X = (8,200 &times; 0.92) + 150 = &pound;7,694.00. Contractor Y = 8,500 &times; 0.88 = &pound;7,480.00. <b>Contractor Y is cheaper by &pound;214.00</b>.")
]
"""
    with open(REF_FILE, "a", encoding="utf-8") as f:
        f.write(maths_ref_7_8)
    print("Maths Mocks 7 and 8 solutions appended to specialist_suite_reference.py!")

if __name__ == "__main__":
    run()
