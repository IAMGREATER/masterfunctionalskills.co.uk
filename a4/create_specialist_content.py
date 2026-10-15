#!/usr/bin/env python3
"""
Creates books/a4/specialist_suite_content.py with authentic questions and texts.
"""
import sys
from pathlib import Path

content = '''# specialist_suite_content.py
# Authentic curriculum data for Specialist Suite (Maths Mocks, English Mocks, Digital Skills, BKSB Remediation)

MATHS_L2_MOCKS = [
    # Mock 1: Facilities & Commercial Catering
    {
        "theme": "Facilities Management & Event Operations",
        "kw1": "facilities event venue catering",
        "kw2": "conference delegate seating",
        "sec_a": [
            # Page 1: Q1 & Q2
            [
                {"q": "<b>Question 1:</b> Without a calculator, evaluate this commercial invoice:<br>"
                      "A conference venue orders 14 banquet table runners at &pound;18.50 each and 6 presentation lecterns at &pound;75.00 each. "
                      "A trade rebate of 5% is deducted from the combined subtotal. Calculate the final net invoice payable.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> An irregular conference hall has outer dimensions forming an L-shape with sides: "
                      "18 m, 12 m, 8 m, 5 m, 10 m, and 7 m. New skirting board costs &pound;4.20 per metre. "
                      "Calculate the total cost of skirting board needed around the entire perimeter.",
                 "marks": 4, "weight": 1.1}
            ],
            # Page 2: Q3 & Q4
            [
                {"q": "<b>Question 3:</b> Work out the following expression without a calculator:<br>"
                      "<strong>2 <sup>1</sup>/<sub>4</sub> + 1 <sup>2</sup>/<sub>3</sub> &minus; <sup>5</sup>/<sub>6</sub></strong><br>"
                      "Give your final answer as a mixed number in its simplest form. Show your common denominator working.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> An audio-visual equipment hire service applies an off-peak discount of 15%. "
                      "The discounted hiring fee is &pound;408.00. Calculate the original hiring fee before the discount was applied. "
                      "Show a check of your answer using multiplication.",
                 "marks": 4, "weight": 1.1}
            ],
            # Page 3: Q5 & Q6
            [
                {"q": "<b>Question 5:</b> A corporate banquet recipe for 12 guests requires 450 g of Arborio rice and 60 ml of truffle oil. "
                      "Calculate the exact quantities of rice (in kg) and truffle oil (in ml) required to cater for 45 guests.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A semicircular outdoor drinks patio has a straight boundary wall of length 7.0 metres (diameter = 7.0 m, radius = 3.5 m). "
                      "Calculate the area of the patio floor using &pi; = 3.14. State the correct units of measurement.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            # Page 4: Q7 & Q8
            [
                {"q": "<b>Question 7:</b> Staffing Payroll: An event operations crew consists of 12 hospitality stewards working 8.5 hours each at &pound;11.44 per hour, "
                      "and 2 senior event duty managers working 9.0 hours each at &pound;16.50 per hour. "
                      "Calculate the total gross staffing cost for the corporate event.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Water Cistern Capacity: A rectangular emergency water tank measures 3.2 m long, 2.4 m wide, and 1.8 m high. "
                      "During a facilities inspection, the tank is filled to 85% of its total capacity. "
                      "Calculate the volume of water stored in the tank in litres (1 m&sup3; = 1,000 litres).",
                 "marks": 5, "weight": 1.2}
            ],
            # Page 5: Q9 & Q10
            [
                {"q": "<b>Question 9:</b> Generator Fuel Logistics: A backup diesel generator consumes fuel at a steady rate of 4.2 litres per hour. "
                      "The generator must run continuously for a 72-hour international trade exhibition. "
                      "Red diesel costs &pound;1.42 per litre. Calculate the total expenditure required to fuel the generator.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Grouped Frequency Customer Ratings: An audit of 40 event delegate feedback scores records:<br>"
                      "1&ndash;2 stars: 4 delegates; 3&ndash;4 stars: 12 delegates; 5&ndash;6 stars: 16 delegates; 7&ndash;8 stars: 8 delegates.<br>"
                      "Calculate an estimate of the mean rating score. Show all midpoint multiplications clearly.",
                 "marks": 5, "weight": 1.2}
            ],
            # Page 6: Q11 & Q12
            [
                {"q": "<b>Question 11:</b> Architectural Scale Plan: On a 1 : 200 architectural site blueprint, an outdoor service yard measures "
                      "14.5 cm by 9.0 cm. Heavy-duty non-slip paving slabs cost &pound;26.00 per square metre. "
                      "Calculate the total actual cost to pave the entire service yard.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Commercial Margin: Total ticket sales for an entertainment gala generated &pound;24,000 in revenue. "
                      "Direct venue hire, security, and catering expenditure totaled &pound;16,500. "
                      "Calculate the net profit as a percentage of total revenue. Round your answer to 1 decimal place.",
                 "marks": 5, "weight": 1.2}
            ],
            # Page 7: Q13 & Q14
            [
                {"q": "<b>Question 13:</b> Quality Audit Probability: Two independent security scanner checkpoints inspect incoming cargo. "
                      "Checkpoint A has a 1 in 25 chance of scanner fault. Checkpoint B has a 1 in 40 chance of fault. "
                      "Calculate the probability that neither checkpoint experiences a fault during the morning shift.",
                 "marks": 4, "weight": 1.2},
                {"q": "<b>Question 14:</b> Pythagoras Loading Ramp: A vehicle loading ramp rises vertically by 1.4 metres from the ground "
                      "over a horizontal ground distance of 5.2 metres. "
                      "Calculate the sloping length of the ramp. Give your answer in metres to 2 decimal places.",
                 "marks": 5, "weight": 1.2}
            ],
            # Page 8: Q15
            [
                {"q": "<b>Question 15:</b> Comprehensive Supplier Evaluation:<br>"
                      "An operations manager must purchase 120 stacking conference chairs. The manufacturer list price is &pound;45.00 per chair.<br>"
                      "&bull; <b>Supplier A:</b> Offers a 15% trade discount on the total chair cost, plus a flat delivery charge of &pound;65.00.<br>"
                      "&bull; <b>Supplier B:</b> Offers a promotional deal: 'Buy 4 chairs, get 1 free' (pay for 4 out of every 5 chairs), with free delivery.<br>"
                      "Determine which supplier offers the cheaper overall deal. Calculate the exact saving made by choosing the cheaper supplier.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    },

    # Mock 2: Transport Logistics & Fleet Distribution
    {
        "theme": "Logistics, Transport Fleet & Distribution",
        "kw1": "warehouse forklift logistics delivery van",
        "kw2": "freight transport cargo container",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Without a calculator, evaluate the haulage delivery charges:<br>"
                      "A haulage fleet invoices a depot for 16 pallet drops at &pound;12.50 per drop, plus a fixed motorway toll surcharge of &pound;34.80. "
                      "Calculate the total delivery charge payable.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> A secure logistics compound is in the shape of a square with side length 22.5 metres. "
                      "Galvanised security fencing costs &pound;18.00 per metre. Calculate the total cost to fence all four sides of the compound.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> A delivery lorry carries three pallets of freight. The pallets weigh 3 <sup>1</sup>/<sub>2</sub> tonnes, "
                      "1 <sup>5</sup>/<sub>8</sub> tonnes, and <sup>3</sup>/<sub>4</sub> tonnes. "
                      "Calculate the total weight of the freight as a mixed number in its simplest form.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> A heavy commercial tyre costs &pound;288.00 including VAT at 20%. "
                      "Calculate the pre-VAT price of the tyre. Show an inverse check of your calculation.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> A logistics depot mixes diesel and bio-additive in the ratio 15 : 1. "
                      "The fleet manager prepares a total blend of 480 litres. How many litres of bio-additive are required?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A circular turning circle for lorries has a radius of 6.0 metres. "
                      "Calculate the circumference of the turning circle using &pi; = 3.14. Include correct units.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 7:</b> Driver Shift Payroll: A courier drives 38 standard weekday hours at &pound;13.20 per hour, "
                      "and 6 Sunday overtime hours at time-and-a-half (&pound;19.80 per hour). "
                      "Calculate the driver's total gross earnings for the week.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Cylindrical Tanker Capacity: A fuel delivery tanker has a horizontal cylindrical tank with internal radius "
                      "1.2 metres and length 6.5 metres. The tank is currently 75% full of heating oil. "
                      "Calculate the volume of heating oil inside the tanker in litres (Volume = &pi;r&sup2;h, &pi; = 3.142, 1 m&sup3; = 1,000 litres).",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 9:</b> Delivery Schedule & Arrival Time: An articulated lorry departs the central depot at 08:35 to complete a 145-mile journey. "
                      "The driver maintains an average speed of 52 mph along the motorway route. "
                      "Calculate the expected arrival time of the lorry, rounding travel duration to the nearest minute.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Courier Stop Times: A dispatch tracker records time spent per delivery stop across 50 deliveries:<br>"
                      "1&ndash;5 mins: 12 stops; 6&ndash;10 mins: 22 stops; 11&ndash;15 mins: 11 stops; 16&ndash;20 mins: 5 stops.<br>"
                      "Calculate an estimate of the mean time spent per delivery stop.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 11:</b> Depot Parking Grid: On a 1 : 500 scale site plan, an articulated lorry parking bay measures 18.0 cm by 11.0 cm. "
                      "Surface sealant costs &pound;3.50 per square metre. Calculate the total cost to seal the real parking area.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Haulage Profit Margin: A regional distribution contract generated &pound;52,000 in total billing. "
                      "Total fuel, vehicle maintenance, and driver wages amounted to &pound;39,500. "
                      "Calculate the operating profit percentage. Give your answer to 1 decimal place.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 13:</b> On-Time Delivery Probability: A freight company operates two independent delivery networks (North and South). "
                      "The probability of on-time delivery is 0.92 in the North and 0.88 in the South. "
                      "Calculate the probability that both networks experience delayed deliveries simultaneously.",
                 "marks": 4, "weight": 1.2},
                {"q": "<b>Question 14:</b> Loading Dock Hydraulic Ramp: A warehouse hydraulic ramp has a vertical height of 1.8 metres "
                      "and a sloping ramp length of 6.5 metres. Calculate the horizontal floor distance covered by the ramp base using Pythagoras.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 15:</b> Vehicle Lease Comparison:<br>"
                      "A logistics firm needs to lease 5 delivery vans for 3 years (36 months).<br>"
                      "&bull; <b>Lease Option Alpha:</b> Initial deposit of &pound;2,500 per van, plus monthly payments of &pound;340 per van.<br>"
                      "&bull; <b>Lease Option Beta:</b> No deposit required, with monthly payments of &pound;415 per van, and a year-end annual rebate of &pound;500 per van.<br>"
                      "Determine which lease option is cheaper across the full 3-year term for all 5 vans. State the overall financial difference.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    },

    # Mock 3: Commercial Construction & Surveying
    {
        "theme": "Construction, Civil Surveying & Building",
        "kw1": "construction site surveyor measuring level",
        "kw2": "building architectural bricklaying scaffolding",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Calculate without using a calculator:<br>"
                      "A builder purchases 45 lengths of timber studding at &pound;8.40 per length, plus 8 boxes of structural screws at &pound;14.50 each. "
                      "Delivery is charged at &pound;35.00. Calculate the total materials invoice.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> An L-shaped building plot has outer boundary edges: 24 m, 16 m, 10 m, 6 m, 14 m, and 10 m. "
                      "Security hoarding costs &pound;15.50 per metre. Calculate the total cost to erect hoarding around the entire boundary.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> Work out without a calculator: <strong>3 <sup>1</sup>/<sub>3</sub> &minus; 1 <sup>3</sup>/<sub>4</sub></strong>.<br>"
                      "Give your answer as an improper fraction and as a mixed number in simplest form.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> A trade power tool set is sold at &pound;540.00 after a 25% promotional discount. "
                      "Calculate the original retail price before the discount was applied. Show a check of your answer.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Concrete Mortar Mix: Cement, sand, and coarse aggregate are mixed in the ratio 1 : 2 : 4. "
                      "A bricklayer needs 840 kg of mortar in total. How many kilograms of sand are needed?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A circular manhole cover has a diameter of 0.80 metres (radius = 0.40 m). "
                      "Calculate the area of the cover using &pi; = 3.14. State the answer in square metres.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 7:</b> Construction Crew Payroll: A bricklaying team consists of 8 skilled masons working 40 hours at &pound;22.50 per hour, "
                      "and 4 apprentice labourers working 40 hours at &pound;12.80 per hour. "
                      "Calculate the total weekly payroll expenditure for the team.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Foundation Concrete Volume: A reinforced concrete foundation slab measures 16.5 m long, 8.4 m wide, and 0.45 m deep. "
                      "Ready-mix concrete costs &pound;115.00 per cubic metre delivered. Calculate the total cost of concrete for the slab.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 9:</b> Soil Core Sample Depth: Surveyors drill 40 ground test cores across a development site:<br>"
                      "1.0&ndash;1.9 m: 8 cores; 2.0&ndash;2.9 m: 15 cores; 3.0&ndash;3.9 m: 12 cores; 4.0&ndash;4.9 m: 5 cores.<br>"
                      "Calculate an estimate of the mean bedrock depth across the site.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Architectural Blueprint Scale: On a 1 : 100 architectural drawing, a residential living area measures "
                      "8.5 cm by 6.2 cm. Solid oak flooring costs &pound;38.00 per m&sup2;. Calculate the total cost of flooring required.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 11:</b> Waste Skip Logistics: A refurbishment project generates 54 cubic metres of rubble. "
                      "Each 8-yard skip has a usable volume of 6.1 m&sup3; and costs &pound;240.00 to hire. "
                      "How many skips must be hired to clear all waste, and what is the total skip hire cost?",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Commercial Tender Profit: A construction company submits a project tender of &pound;85,000. "
                      "The estimated costs for materials, plant hire, and subcontract labour total &pound;66,300. "
                      "Calculate the planned profit margin as a percentage of the tender price.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 13:</b> Building Inspection Probability: A site undergoes two independent quality compliance checks (Structural and Drainage). "
                      "The probability of passing the structural check is 0.95. The probability of passing the drainage check is 0.90. "
                      "Calculate the probability that the site fails at least one of the two compliance checks.",
                 "marks": 4, "weight": 1.2},
                {"q": "<b>Question 14:</b> Roof Truss Geometry: A timber roof truss forms a right-angled triangle. "
                      "The vertical king post rises 2.4 metres, and the horizontal half-span is 7.0 metres. "
                      "Calculate the length of the sloping timber rafter using Pythagoras' theorem. Round to 2 decimal places.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 15:</b> Scaffolding Contractor Comparison:<br>"
                      "A commercial development requires scaffolding surrounding a 4-storey facade for 12 weeks.<br>"
                      "&bull; <b>Contractor 1:</b> Fixed erection fee of &pound;3,200, plus a weekly hire charge of &pound;480.<br>"
                      "&bull; <b>Contractor 2:</b> Fixed erection fee of &pound;1,800, plus a weekly hire charge of &pound;620, with 10% discount on the total weekly hire fee.<br>"
                      "Determine which scaffolding contractor is cheaper over the 12-week period, and calculate the financial saving.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    },

    # Mock 4: Healthcare, Pharmacy & Clinical Logistics
    {
        "theme": "Healthcare, Pharmacy & Clinical Logistics",
        "kw1": "hospital pharmacy medicine nurse clinic",
        "kw2": "medical laboratory clinical healthcare equipment",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Calculate without a calculator:<br>"
                      "A clinical pharmacy orders 25 boxes of sterile dressing packs at &pound;16.40 each and 18 packs of disposable syringes at &pound;8.50 each. "
                      "Calculate the total order value before tax.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> A hospital rehabilitation suite is rectangular, measuring 14.5 metres by 8.5 metres. "
                      "Heavy-duty hospital wall bumper guard rails cost &pound;12.00 per metre. "
                      "Calculate the total cost to fit guard rails around the entire perimeter.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> A pharmacist has 4 <sup>1</sup>/<sub>2</sub> litres of liquid cough elixir. "
                      "Each dispensary bottle takes <sup>3</sup>/<sub>8</sub> of a litre. "
                      "How many full dispensary bottles can be prepared?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> A batch of medical monitoring units is purchased at &pound;720.00 following a 20% NHS procurement discount. "
                      "What was the original cost before the discount? Show an inverse check.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Saline Disinfectant Ratio: A sterilising fluid must be mixed with purified water in the ratio 1 : 9. "
                      "A clinical cleaner prepares 45 litres of cleaning solution. How many litres of sterilising fluid are needed?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A circular overhead surgical lighting beam covers a floor circle of diameter 2.4 metres (radius = 1.2 m). "
                      "Calculate the illumination area using &pi; = 3.14. State the units.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 7:</b> Ward Healthcare Staffing: A hospital ward shift requires 6 registered nurses working 11.5 hours at &pound;18.40 per hour, "
                      "and 4 healthcare assistants working 11.5 hours at &pound;12.20 per hour. "
                      "Calculate the total staffing wage cost for the shift.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Oxygen Cylinder Capacity: A medical gas cylinder has internal radius 0.25 m and height 1.6 m. "
                      "Calculate the internal volume in cubic metres and the total capacity in litres (&pi; = 3.142, 1 m&sup3; = 1,000 litres).",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 9:</b> Urgent Care Triage Wait Times: Triage records for 50 emergency patients:<br>"
                      "0&ndash;29 mins: 15 patients; 30&ndash;59 mins: 20 patients; 60&ndash;89 mins: 10 patients; 90&ndash;119 mins: 5 patients.<br>"
                      "Calculate an estimate of the mean triage waiting time in minutes.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Pharmacy Dispensary Scale Drawing: On a 1 : 50 plan of a clinic dispensing suite, the room measures 16 cm by 12 cm. "
                      "Anti-microbial flooring costs &pound;42.00 per m&sup2;. Calculate the total flooring installation cost.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 11:</b> Vaccine Wastage Rate: A vaccination clinic received 1,200 doses of seasonal vaccine. "
                      "At the end of the campaign, 1,092 doses were administered and the remaining doses expired. "
                      "Calculate the percentage of doses that were wasted.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Diagnostic Screening Probability: A clinic tests 200 patients for an antibody: 120 are female, 80 are male. "
                      "Among the females, 30 test positive. Among the males, 20 test positive. "
                      "What is the probability that a randomly chosen patient tests positive?",
                 "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 13:</b> Emergency Ambulance Transit: An emergency response vehicle travels 24 miles through city traffic at an average speed of 36 mph. "
                      "If the dispatch call was logged at 14:22, calculate the exact arrival time at the hospital.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 14:</b> Patient Stretcher Access Ramp: A hospital entrance ramp rises vertically by 0.9 metres "
                      "over a horizontal ground distance of 7.2 metres. Calculate the sloping length of the ramp using Pythagoras. Round to 2 decimal places.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 15:</b> Medical PPE Procurement Comparison:<br>"
                      "A healthcare trust procures 500 cases of nitrile examination gloves.<br>"
                      "&bull; <b>Supplier A:</b> &pound;28.00 per case, with 12% bulk discount, plus &pound;150 flat delivery fee.<br>"
                      "&bull; <b>Supplier B:</b> &pound;30.00 per case, with 'Buy 4 cases, get 1 free' deal, and free delivery.<br>"
                      "Determine which supplier is cheaper for 500 cases and calculate the total financial saving.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    },

    # Mock 5: Hospitality, Hotel & Event Management
    {
        "theme": "Hospitality, Commercial Catering & Hotel",
        "kw1": "commercial kitchen chef cooking food hotel",
        "kw2": "hospitality restaurant dining banquet event",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Calculate without a calculator:<br>"
                      "A luxury hotel orders 35 cases of organic sparkling water at &pound;14.80 per case and 12 cases of vintage wine at &pound;95.00 per case. "
                      "Calculate the total invoice cost before delivery.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> A hotel ballroom dancefloor is rectangular, measuring 15.0 metres by 9.5 metres. "
                      "Brass edging trim costs &pound;6.50 per metre. Calculate the total cost of trim needed around the perimeter.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> Evaluate without a calculator: <strong>2 <sup>2</sup>/<sub>5</sub> &times; 1 <sup>1</sup>/<sub>4</sub></strong>.<br>"
                      "Give your answer as a simplified fraction and as a decimal.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> An all-inclusive wedding reception package costs &pound;3,400.00 after a 15% promotional advance booking discount. "
                      "Calculate the original price before the discount. Show a check of your answer.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Cocktail Punch Recipe Ratio: Fruit juice, ginger beer, and sparkling water are blended in the ratio 4 : 2 : 1. "
                      "The head barman needs to prepare 35 litres of punch. How many litres of fruit juice are needed?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A circular dining table has a diameter of 1.8 metres (radius = 0.9 m). "
                      "Calculate the area of the tabletop using &pi; = 3.14. Round your answer to 2 decimal places.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 7:</b> Restaurant Front-of-House Payroll: A restaurant shift employs 8 waitstaff working 6.5 hours at &pound;11.44 per hour, "
                      "plus 2 head sommeliers working 7.0 hours at &pound;15.50 per hour. "
                      "Calculate the total front-of-house payroll cost.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Ornamental Water Fountain: An outdoor hotel fountain reservoir is cylindrical with radius 2.0 m and depth 0.85 m. "
                      "Calculate the volume of water the fountain holds in cubic metres and in litres (&pi; = 3.142, 1 m&sup3; = 1,000 litres).",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 9:</b> Hotel Guest Satisfaction Survey: Ratings from 60 hotel guests across 10 categories:<br>"
                      "1&ndash;3 points: 6 guests; 4&ndash;6 points: 18 guests; 7&ndash;8 points: 24 guests; 9&ndash;10 points: 12 guests.<br>"
                      "Calculate an estimate of the mean guest satisfaction score.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Marquee Scale Plan: On an architectural drawing of a marquee lawn (scale 1 : 250), the space measures "
                      "12.0 cm by 8.0 cm. Artificial turf costs &pound;18.50 per m&sup2;. Calculate the total cost to turf the area.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 11:</b> Food Cost Percentage: A 3-course banquet menu sells for &pound;65.00 per cover. "
                      "The chef calculates that raw ingredient costs average &pound;18.20 per cover. "
                      "Calculate the food cost percentage (raw cost / selling price &times; 100).",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Weekend Booking Cancellation Probability: Hotel records show a 0.08 probability of weekend booking cancellation. "
                      "For two independent weekend room reservations, calculate the probability that neither booking is cancelled.",
                 "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 13:</b> Airport Transfer Coach Timing: A luxury coach travels 68 miles from airport to hotel at an average speed of 40 mph. "
                      "If the flight lands and passengers board at 17:15, calculate the expected hotel arrival time.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 14:</b> Terrace Awning Support Diagonal: A retractable sun awning extends out horizontally by 4.5 metres, "
                      "and attaches vertically to the wall 2.8 metres above terrace level. "
                      "Calculate the length of the diagonal support arm using Pythagoras.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 15:</b> Commercial Laundry Contract Comparison:<br>"
                      "A 120-room hotel processes 800 kg of bed linen per week for 52 weeks.<br>"
                      "&bull; <b>Contractor A:</b> Charges &pound;0.95 per kg, with free delivery and a 5% prompt-payment annual rebate.<br>"
                      "&bull; <b>Contractor B:</b> Charges &pound;0.85 per kg, plus a fixed weekly collection charge of &pound;65.00.<br>"
                      "Determine which commercial laundry contractor is cheaper over the full 52 weeks, and calculate the annual cost saving.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    },

    # Mock 6: Green Energy, Solar Array & Eco-Renovation
    {
        "theme": "Green Energy, Solar & Environmental Projects",
        "kw1": "solar panels technician wind turbine renewable",
        "kw2": "environmental energy efficiency insulation heat pump",
        "sec_a": [
            [
                {"q": "<b>Question 1:</b> Calculate without a calculator:<br>"
                      "A renewable energy installer orders 16 solar micro-inverters at &pound;85.00 each and 4 rolls of UV-resistant DC cabling at &pound;65.00 per roll. "
                      "Calculate the total materials invoice before delivery.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 2:</b> A ground-mounted solar panel array perimeter is rectangular, measuring 18.5 metres by 6.0 metres. "
                      "Anti-vermin mesh skirting costs &pound;8.40 per metre. Calculate the total cost to fit mesh around the perimeter.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 3:</b> Work out without a calculator: <strong>5 <sup>1</sup>/<sub>2</sub> &divide; 1 <sup>3</sup>/<sub>8</sub></strong>.<br>"
                      "Give your answer as an exact whole number or simplified fraction.",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 4:</b> An air-source heat pump system costs &pound;4,250.00 after a 15% government eco-grant discount. "
                      "Calculate the full original cost of the system before the grant was applied. Show a check of your answer.",
                 "marks": 4, "weight": 1.1}
            ],
            [
                {"q": "<b>Question 5:</b> Solar Thermal Glycol Mix: Heat-transfer fluid mixes glycol and water in the ratio 2 : 5. "
                      "A solar heating circuit requires 35 litres of fluid. How many litres of glycol are needed?",
                 "marks": 4, "weight": 1.1},
                {"q": "<b>Question 6:</b> A domestic wind turbine has blades creating a circular rotor sweep of diameter 4.0 metres (radius = 2.0 m). "
                      "Calculate the swept area of the blades using &pi; = 3.14. State the units.",
                 "marks": 4, "weight": 1.1}
            ]
        ],
        "sec_b": [
            [
                {"q": "<b>Question 7:</b> Solar Installation Crew Payroll: An installation requires 4 certified solar technicians working 7.5 hours at &pound;26.00 per hour, "
                      "and 2 scaffolding riggers working 7.5 hours at &pound;18.00 per hour. "
                      "Calculate the total labor cost for the day's installation.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 8:</b> Thermal Storage Buffer Tank: A cylindrical hot water buffer tank has an internal radius of 0.60 metres "
                      "and an internal height of 1.75 metres. "
                      "Calculate the liquid capacity of the tank in litres (&pi; = 3.142, 1 m&sup3; = 1,000 litres).",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 9:</b> Daily Solar Generation Distribution: Daily kilowatt-hours (kWh) generated by an array over 50 autumn days:<br>"
                      "10&ndash;14 kWh: 10 days; 15&ndash;19 kWh: 18 days; 20&ndash;24 kWh: 14 days; 25&ndash;29 kWh: 8 days.<br>"
                      "Calculate an estimate of the mean daily energy generation in kWh.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 10:</b> Rooftop Scale Blueprint: On a 1 : 100 architectural roof drawing, a south-facing roof pitch measures "
                      "12.4 cm by 7.5 cm. Photovoltaic solar panels generate 200 Watts per m&sup2;. "
                      "Calculate the total potential electrical capacity of the roof in Kilowatts (kW).",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 11:</b> Energy Bill Reduction Percentage: A homeowner's annual electricity expenditure before solar installation was &pound;2,400. "
                      "Following the installation of solar panels and battery storage, the annual electricity bill dropped to &pound;840. "
                      "Calculate the percentage reduction in the annual electricity bill.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 12:</b> Solar Inverter Reliability Probability: Two identical micro-inverters operate independently on an array. "
                      "The probability of inverter failure in any 5-year period is 0.04. "
                      "Calculate the probability that at least one inverter fails within 5 years.",
                 "marks": 4, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 13:</b> Electric Vehicle Fleet Range & Speed: An electric commercial van has a 65 kWh battery pack and travels at an average "
                      "energy efficiency of 3.2 miles per kWh. A delivery run covers 144 miles at an average speed of 48 mph. "
                      "Calculate the total driving time and the remaining battery energy in kWh upon return.",
                 "marks": 5, "weight": 1.2},
                {"q": "<b>Question 14:</b> Roof Pitch Pythagoras Calculation: A pitched roof has a horizontal span of 8.0 metres (half-span = 4.0 m) "
                      "and a vertical apex rise of 3.0 metres. Calculate the sloping rafter length of the roof pitch using Pythagoras.",
                 "marks": 5, "weight": 1.2}
            ],
            [
                {"q": "<b>Question 15:</b> Home Battery Storage System Comparison:<br>"
                      "A commercial client plans to install a 20 kWh battery storage bank.<br>"
                      "&bull; <b>System Alpha:</b> Capital cost of &pound;8,500, with an expected annual energy savings of &pound;1,250.<br>"
                      "&bull; <b>System Beta:</b> Capital cost of &pound;9,800, with an expected annual energy savings of &pound;1,600, plus a manufacturer cashback rebate of &pound;400.<br>"
                      "Calculate the payback period (net cost / annual savings) for both systems in years. State which system achieves a faster payback and by how many months.",
                 "marks": 5, "weight": 1.3}
            ]
        ]
    }
]

print("MATHS_L2_MOCKS defined successfully: 6 full mocks!")
'''

with open('books/a4/specialist_suite_content.py', 'w') as f:
    f.write(content)

print("specialist_suite_content.py initialized with MATHS_L2_MOCKS!")
