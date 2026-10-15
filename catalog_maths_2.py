#!/usr/bin/env python3
"""
Catalog Maths 2: Measures, Shape & Space.
Topics: Volume, Surface Area, Circles, 2D Shapes, 3D Shapes, Nets, Angles, Coordinates, Scale Drawings, Time, Speed, Density, Unit Conversions.
"""
from build_topic_dataset import make_maths_topic
from generate_all_worksheets_complete import get_svg_for_topic

CATALOG_MATHS_2 = [
    # Volume
    make_maths_topic(
        slug="volume",
        title="Volume & Capacity",
        spec_codes="L1.24 • L2.18",
        formula_hint="Cuboid Volume = Length × Width × Height. Cylinder Volume = 3.142 × Radius × Radius × Height. Remember: 1 m³ = 1,000 litres, and 1 cm³ = 1 ml.",
        q1={
            "title": "Question 1 (Level 1 Cuboid Volume)",
            "marks": 2,
            "stem": "Calculate the volume of a rectangular medical storage container measuring <strong>2.5 m long</strong>, <strong>1.4 m wide</strong>, and <strong>0.8 m high</strong>.",
            "lines": 3,
            "ans_label": "Volume =",
            "choice_box": "_____________ m³",
            "step_rows": [
                ("1. Cuboid formula: length × width × height = 2.5 × 1.4 × 0.8", "[M1]"),
                ("2. Evaluation: 3.5 × 0.8 = 2.8 m³", "[A1]")
            ],
            "final_answer": "2.8 m³",
            "pitfall": "Adding dimensions instead of multiplying (2.5 + 1.4 + 0.8 = 4.7).",
            "reverse_check": "2.8 ÷ 0.8 ÷ 1.4 = 2.5 m."
        },
        q2={
            "title": "Question 2 (Level 2 Cylinder Volume)",
            "marks": 2,
            "stem": "Calculate the volume of a cylindrical oxygen storage tank with radius <em>r</em> = <strong>0.6 m</strong> and height <em>h</em> = <strong>2.5 m</strong>.<br>Use π = 3.14. Round your answer to 2 decimal places.",
            "lines": 3,
            "ans_label": "Volume =",
            "choice_box": "_____________ m³",
            "step_rows": [
                ("1. Cylinder formula: π × r² × h = 3.14 × (0.6)² × 2.5", "[M1]"),
                ("2. 3.14 × 0.36 × 2.5 = 2.826 m³ → round to 2 d.p.: 2.83 m³", "[A1]")
            ],
            "final_answer": "2.83 m³",
            "pitfall": "Multiplying radius by 2 instead of squaring (using 1.2 instead of 0.36).",
            "reverse_check": "2.826 ÷ 2.5 ÷ 3.14 = 0.36; √0.36 = 0.6 m."
        },
        q3={
            "title": "Question 3 (Level 1 Aquarium / Hydrotherapy Tank Capacity)",
            "marks": 3,
            "stem": "A rectangular sensory aquarium in a children's ward measures <strong>120 cm long</strong>, <strong>50 cm wide</strong>, and <strong>60 cm high</strong>.<br><br>Calculate the maximum volume of water the tank can hold in <strong>litres</strong>.<br>(1 litre = 1,000 cm³)",
            "lines": 4,
            "ans_label": "Water Capacity =",
            "choice_box": "_____________ litres",
            "step_rows": [
                ("1. Calculate volume in cm³: 120 × 50 × 60 = 360,000 cm³", "[M1]"),
                ("2. Convert to litres: 360,000 ÷ 1,000", "[P1]"),
                ("3. Accurate capacity: 360 litres", "[A1]")
            ],
            "final_answer": "360 litres",
            "pitfall": "Dividing by 100 instead of 1,000 when converting cm³ to litres.",
            "reverse_check": "360 litres × 1,000 = 360,000 cm³; 360,000 ÷ (50 × 60) = 120 cm."
        },
        q4={
            "title": "Question 4 (Level 2 Sandpit Concrete Bag Calculation)",
            "marks": 3,
            "stem": "A community nursery builds a rectangular sandpit measuring <strong>3.2 m by 2.0 m</strong> with a sand depth of <strong>0.25 m</strong>.<br>Playground play-sand is sold in <strong>25 kg bags</strong>.<br>1 cubic metre of sand weighs <strong>1,600 kg</strong>.<br><br>How many 25 kg bags of sand are needed to fill the sandpit?",
            "lines": 5,
            "ans_label": "Bags of sand =",
            "choice_box": "_____________ bags",
            "step_rows": [
                ("1. Calculate sandpit volume: 3.2 × 2.0 × 0.25 = 1.6 m³", "[M1]"),
                ("2. Total weight of sand: 1.6 m³ × 1,600 kg/m³ = 2,560 kg", "[P1]"),
                ("3. Calculate bags: 2,560 ÷ 25 = 102.4 bags → round UP to 103 whole bags", "[A1]")
            ],
            "final_answer": "103 bags",
            "pitfall": "Rounding down to 102 bags, leaving the sandpit underfilled.",
            "reverse_check": "102 bags = 2,550 kg (< 2,560 kg). 103 bags = 2,575 kg (> 2,560 kg)."
        },
        q5={
            "title": "Question 5 (Level 2 Oil Drum Tank Drainage Rate)",
            "marks": 4,
            "stem": "A cylindrical waste oil storage tank at a transport depot has a radius of <strong>0.8 m</strong> and height of <strong>2.0 m</strong>.<br>The tank is currently <strong>3/4 full</strong>. Take π = 3.14.<br>A drainage pump removes oil at a steady rate of <strong>45 litres per minute</strong>.<br><br>How many minutes will it take the pump to completely empty the oil in the tank?<br>Give your answer to the nearest whole minute. (1 m³ = 1,000 litres)",
            "lines": 5,
            "ans_label": "Drainage time =",
            "choice_box": "_____________ minutes",
            "step_rows": [
                ("1. Full tank volume: 3.14 × (0.8)² × 2.0 = 3.14 × 0.64 × 2.0 = 4.0192 m³", "[P1]"),
                ("2. Convert to litres: 4.0192 × 1,000 = 4,019.2 litres", "[P1]"),
                ("3. 3/4 volume: 4,019.2 × 0.75 = 3,014.4 litres", "[M1]"),
                ("4. Drainage time: 3,014.4 ÷ 45 = 66.98... minutes → round to 67 minutes", "[A1]")
            ],
            "final_answer": "67 minutes (Accept 67.0)",
            "pitfall": "Draining the full 4,019.2 litres (89 minutes) without multiplying by 3/4.",
            "reverse_check": "67 mins × 45 L/min = 3,015 L ≈ 3,014.4 L."
        },
        q6={
            "title": "Question 6 (Level 2 Water Tank Capacity Justification)",
            "marks": 4,
            "stem": "An estates manager installs a new emergency water storage tank measuring <strong>2.4 m long, 1.5 m wide, and 1.2 m high</strong>.<br>Hospital safety regulations require a minimum emergency supply of <strong>4,000 litres</strong> of potable water.<br>The manager states: <em>'This tank easily provides the required 4,000 litres with at least 5% capacity to spare.'</em><br><br>Is the manager's statement correct?<br>Show your calculations with units and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Tank Capacity =",
            "choice_box": "Correct / Incorrect: Tank holds _____ L vs 4,000 L + 5%",
            "step_rows": [
                ("1. Calculate tank volume: 2.4 × 1.5 × 1.2 = 4.32 m³", "[M1]"),
                ("2. Convert to litres: 4.32 × 1,000 = 4,320 litres", "[P1]"),
                ("3. Calculate target with 5% spare: 4,000 × 1.05 = 4,200 litres", "[P1]"),
                ("4. Compare: 4,320 L > 4,200 L. Conclude: <strong>Yes, the manager is correct</strong>. The tank holds 4,320 L, which exceeds the 4,200 L threshold (exceeds 4,000 L by 8%).", "[A1]")
            ],
            "final_answer": "Correct (Tank holds 4,320 litres, which exceeds 4,000 L + 5% [4,200 L] by 120 litres)",
            "pitfall": "Comparing 4.32 m³ directly with 4,000 without converting m³ to litres.",
            "reverse_check": "4,320 ÷ 4,000 = 1.08 = 8% spare capacity (> 5%)."
        }
    ),
    # Circles
    make_maths_topic(
        slug="circles",
        title="Circles & Circumference",
        spec_codes="L1.25 • L2.19",
        formula_hint="Circumference = 3.142 × Diameter. Area = 3.142 × Radius × Radius. Remember: Radius is half the diameter (Radius = Diameter ÷ 2). Always use radius for Area, and diameter for Circumference.",
        q1={
            "title": "Question 1 (Level 1 Circumference)",
            "marks": 2,
            "stem": "Calculate the circumference of a circular roundabout with diameter <strong>18.0 metres</strong>.<br>Use π = 3.14.",
            "lines": 3,
            "ans_label": "Circumference =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Formula: π × d = 3.14 × 18.0", "[M1]"),
                ("2. Accurate calculation: 56.52 m", "[A1]")
            ],
            "final_answer": "56.52 m",
            "pitfall": "Using radius 9 instead of diameter 18 in circumference (yielding 28.26 m).",
            "reverse_check": "56.52 ÷ 3.14 = 18.0 m."
        },
        q2={
            "title": "Question 2 (Level 2 Circle Area from Diameter)",
            "marks": 2,
            "stem": "Calculate the area of a circular helicopter landing pad with a diameter of <strong>16.0 metres</strong>.<br>Use π = 3.14.",
            "lines": 3,
            "ans_label": "Area =",
            "choice_box": "_____________ m²",
            "step_rows": [
                ("1. Find radius: 16.0 ÷ 2 = 8.0 m. Area = π × r² = 3.14 × 8² = 3.14 × 64", "[M1]"),
                ("2. Evaluation: 200.96 m²", "[A1]")
            ],
            "final_answer": "200.96 m²",
            "pitfall": "Squaring diameter directly: 3.14 × 16² = 803.84 m² (4 times too large!).",
            "reverse_check": "200.96 ÷ 3.14 = 64; √64 = 8 m radius."
        },
        q3={
            "title": "Question 3 (Level 1 Running Track Circular Curve)",
            "marks": 3,
            "stem": "A hospital rehabilitation garden includes a circular walking track with a radius of <strong>14 metres</strong>.<br>A patient completes <strong>5 full laps</strong> around the track.<br><br>Calculate the total distance walked by the patient in metres. Use π = 22/7 or 3.14.",
            "lines": 4,
            "ans_label": "Total distance =",
            "choice_box": "_____________ m",
            "step_rows": [
                ("1. Find track circumference: 2 × π × r = 2 × (22/7) × 14 = 88 m (or 2 × 3.14 × 14 = 87.92 m)", "[M1]"),
                ("2. Multiply by 5 laps: 88 × 5 = 440 m (or 87.92 × 5 = 439.6 m)", "[P1]"),
                ("3. State total distance: 440 m (accept 439.6 m)", "[A1]")
            ],
            "final_answer": "440 m (or 439.6 m)",
            "pitfall": "Calculating the area of the track instead of the perimeter/circumference.",
            "reverse_check": "440 ÷ 5 = 88 m per lap; 88 ÷ (2 × 3.142) ≈ 14 m."
        },
        q4={
            "title": "Question 4 (Level 2 Circular Pond Safety Netting)",
            "marks": 3,
            "stem": "A care home installs a circular fish pond with a diameter of <strong>5.4 metres</strong>.<br>Protective safety netting is sold in square metres at <strong>£7.50 per m²</strong>.<br><br>Calculate the area of the pond and the cost to cover it with netting. Take π = 3.14.",
            "lines": 5,
            "ans_label": "Pond Area & Netting Cost =",
            "choice_box": "Area: _____ m² | Cost: £ _____",
            "step_rows": [
                ("1. Radius = 5.4 ÷ 2 = 2.7 m", "[P1]"),
                ("2. Area = 3.14 × (2.7)² = 3.14 × 7.29 = 22.8906 m²", "[M1]"),
                ("3. Cost = 22.8906 × £7.50 = £171.6795 → £171.68", "[A1]")
            ],
            "final_answer": "Area: 22.89 m²; Cost: £171.68",
            "pitfall": "Using 5.4 m directly as radius in the area formula.",
            "reverse_check": "£171.68 ÷ £7.50 ≈ 22.89 m²; 22.89 ÷ 3.14 = 7.29; √7.29 = 2.7 m."
        },
        q5={
            "title": "Question 5 (Level 2 Semi-Circular Pathway Border)",
            "marks": 4,
            "stem": "A semi-circular garden patio has a diameter of <strong>10.0 metres</strong>.<br>The estates team will install decorative brick edging completely around the perimeter of the patio (both the straight edge and the curved arc).<br>Each decorative brick is <strong>20 cm long</strong>.<br><br>How many bricks are required to complete the edging? Take π = 3.14.",
            "lines": 5,
            "ans_label": "Bricks required =",
            "choice_box": "_____________ bricks",
            "step_rows": [
                ("1. Curved arc length: (π × d) ÷ 2 = (3.14 × 10.0) ÷ 2 = 15.7 m", "[M1]"),
                ("2. Total perimeter = curved arc + straight diameter = 15.7 + 10.0 = 25.7 m", "[P1]"),
                ("3. Convert brick length: 20 cm = 0.20 m", "[P1]"),
                ("4. Calculate bricks: 25.7 ÷ 0.20 = 128.5 → round UP to 129 bricks", "[A1]")
            ],
            "final_answer": "129 bricks",
            "pitfall": "Forgetting the straight diameter edge (10.0 m), calculating bricks for the curved arc only (79 bricks).",
            "reverse_check": "128 bricks × 0.20 m = 25.6 m (< 25.7 m). 129 bricks required: 129 × 0.20 = 25.8 m."
        },
        q6={
            "title": "Question 6 (Level 2 Turf vs Paving Budget Justification)",
            "marks": 4,
            "stem": "A community nursery creates a circular sensory lawn with diameter <strong>12.0 m</strong>.<br>High-grade turf rolls cost <strong>£5.20 per square metre</strong>.<br>The nursery has a turfing budget of <strong>£600.00</strong>.<br>The groundskeeper claims: <em>'The budget is more than enough to turf the entire lawn with at least £10.00 left over.'</em><br><br>Is the groundskeeper correct? Take π = 3.14.<br>Show full step-by-step working and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Leftover Balance =",
            "choice_box": "Correct / Incorrect: Leftover balance is £ ____________",
            "step_rows": [
                ("1. Radius: 12.0 ÷ 2 = 6.0 m", "[P1]"),
                ("2. Area of circular lawn: π × r² = 3.14 × 6² = 3.14 × 36 = 113.04 m²", "[M1]"),
                ("3. Cost of turf: 113.04 × £5.20 = £587.808 → £587.81", "[P1]"),
                ("4. Leftover balance: £600.00 - £587.81 = £12.19. Compare: £12.19 > £10.00. Conclude: <strong>Yes, the groundskeeper is correct</strong> (£12.19 left over).", "[A1]")
            ],
            "final_answer": "Correct (Total cost is £587.81, leaving £12.19 surplus, which exceeds £10.00)",
            "pitfall": "Using diameter 12 in area formula: 3.14 × 144 = 452.16 m² (£2,351.23) and wrongly saying 'No'.",
            "reverse_check": "£587.81 + £12.19 = £600.00."
        }
    )
]

print(f"Loaded {len(CATALOG_MATHS_2)} topics in catalog_maths_2.py")
