"""Per-question Examiner Trap CCQs for Mock & Past Paper walkthroughs."""

# Exact per-question CCQs for multi-question Edexcel Maths VTTs whose cue labels are "Question 1".."Question 12"
EXACT_QUESTION_CCQS = {
    "edexcel-maths-l2-past-paper-10-section-b": {
        "Question 1": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Marta thinks she will pay less than £400 of the £720 rent (ratio 9 : 7). How do you lock in the final decision mark after finding £405?",
            "options": [
                "Write '£405' alone in the answer box",
                "Tick 'No' AND write '£405 is £5 more than £400' (clear verdict + comparison)",
                "Write 'Yes' because 9 parts > 7 parts",
            ],
            "correct": 1,
            "why": "Decision questions require BOTH an explicit Yes/No verdict AND a numerical comparison showing £405 > £400.",
        },
        "Question 2": {
            "archetype": "Examiner Trap",
            "question": "'One customer who bought a Mini phone is picked at random.' What goes in the denominator of this probability?",
            "options": [
                "50 (the grand total of all customers)",
                "18 (ONLY the Mini phone row/column subtotal — 7/18)",
                "7 (only the 128 GB Mini customers)",
            ],
            "correct": 1,
            "why": "Conditional wording ('who bought a Mini phone') restricts the denominator strictly to the Mini subtotal (18), not 50.",
        },
        "Question 3": {
            "archetype": "Unit & Capacity Trap",
            "question": "Emma needs flower garland around 2 straight 2 m edges plus two 2.8 m semicircles, and has 40 feet (1 m = 3.3 ft). What two mistakes lose easy marks?",
            "options": [
                "Leaving total perimeter in metres (12.792 m) without converting to feet (42.21 ft), OR omitting 'No' when 42.21 ft > 40 ft",
                "Joining the two semicircles into one full circle",
                "Using π ≈ 3.14 × 2.8",
            ],
            "correct": 0,
            "why": "Always convert into the unit you are comparing (42.21 ft vs 40 ft) AND write an explicit No comparison.",
        },
        "Question 4": {
            "archetype": "Reverse Check Trap",
            "question": "Jake's sorted times put 59 and 62 in the middle, giving median 60.5 mins. Which Part (b) check uses multiplication as requested?",
            "options": [
                "60.5 × 2 = 121, and 121 − 59 = 62 (matching the second middle value)",
                "62 − 59 = 3",
                "61 − 60.5 = 0.5",
            ],
            "correct": 0,
            "why": "When Part (b) specifies a method ('using multiplication'), show the exact inverse step: 60.5 × 2 = 121.",
        },
        "Question 5": {
            "archetype": "Examiner Trap",
            "question": "In Part (c), 'What percentage of students who revised for MORE than 15 hours scored over 70?' Which students belong in the denominator?",
            "options": [
                "All 31 students on the scatter diagram",
                "ONLY the 11 students strictly to the right of 15 hours (8/11 × 100 = 72.7%)",
                "Only students scoring exactly 70",
            ],
            "correct": 1,
            "why": "Filter to the condition FIRST ('more than 15 hours' = 11 students, NOT counting points sitting right on 15!), then find 8/11.",
        },
        "Question 6": {
            "archetype": "Reverse Check Trap",
            "question": "Alya uses 400 kg of flour in April and increases by 14% in May (400 × 1.14 = 456 kg). How can you reverse-check 456 kg on your calculator?",
            "options": [
                "456 ÷ 1.14 = 400 kg (matches April's flour!)",
                "456 × 0.86 = 392.16 kg",
                "456 − 14 = 442 kg",
            ],
            "correct": 0,
            "why": "To undo a ×1.14 multiplier increase, divide by 1.14 (never multiply by 0.86, which takes 14% of the larger May figure).",
        },
        "Question 7": {
            "archetype": "Unit & Capacity Trap",
            "question": "Karim's tank holds 62 litres (1 gallon = 4.546 litres). Should you multiply or divide 62 by 4.546, and how do you round 13.63836?",
            "options": [
                "Divide 62 ÷ 4.546 = 13.638... → 13.64 gallons to 2 d.p. (gallons are larger than litres, so fewer gallons!)",
                "Multiply 62 × 4.546",
                "Round down to 13.63 gallons",
            ],
            "correct": 0,
            "why": "1 gallon > 1 litre, so 62 litres equals FEWER gallons (divide!). Watch the 3rd decimal digit 8 rounding .638 up to 13.64.",
        },
        "Question 8": {
            "archetype": "Rounding Direction Trap",
            "question": "Amir needs 7.9 ÷ 0.215 = 36.74 bricks along the length and 8.6 ÷ 0.065 = 132.3 bricks across. How MUST both counts be rounded?",
            "options": [
                "Round UP to whole bricks (37 and 133) before multiplying by 9 bricks high — never buy half-bricks or round 132.3 down!",
                "Round 132.3 down to 132",
                "Multiply 36.74 × 132.3 × 9 and round at the end",
            ],
            "correct": 0,
            "why": "Every edge needs whole bricks covering the full dimension: 36.74 → 37 and 132.3 → 133; rounding 132.3 down leaves the wall short!",
        },
        "Question 9": {
            "archetype": "Unit & Capacity Trap",
            "question": "5 bricklayers finish 450 bricks in 6 ÷ 5 = 1.2 hours. If a follow-up asks for minutes or checks the time, what does 1.2 hours mean?",
            "options": [
                "1 hour 20 minutes",
                "1 hour 12 minutes (0.2 × 60 = 12 mins — leave as 1.2 when the answer box says 'hours')",
                "2 hours 5 minutes",
            ],
            "correct": 1,
            "why": "Check the answer-box unit! Writing 1.2 matches 'hours', while converting to minutes multiplies 0.2 × 60 = 12 mins (never 20 mins).",
        },
        "Question 10": {
            "archetype": "Examiner Trap",
            "question": "In Part (a), how must (13.608 ÷ 3.24)² be entered into a calculator?",
            "options": [
                "Type 13.608 ÷ 3.24² without brackets",
                "Divide 13.608 ÷ 3.24 (= 4.2) FIRST inside brackets, then square 4.2 (= 17.64)",
                "Square 13.608 first, then divide by 3.24",
            ],
            "correct": 1,
            "why": "Without brackets, calculators apply BIDMAS and square ONLY 3.24; always evaluate inside the brackets first.",
        },
        "Question 11": {
            "archetype": "Yes/No Verdict Trap",
            "question": "The pool holds 510 m³ and two pumps clear 523.8 m³ in 9 hours. Which answer secures Ben's decision mark?",
            "options": [
                "Write '523.8 m³' with no Yes/No",
                "Write 'Yes — 523.8 m³ > 510 m³ (they clear more than the pool volume in 9 hours)'",
                "Write 'No, 523.8 is larger'",
            ],
            "correct": 1,
            "why": "Notice bigger pump output (523.8 m³ > 510 m³) means YES they CAN empty it in under 9 hours — state Yes + both m³ values!",
        },
        "Question 12": {
            "archetype": "Reverse Check Trap",
            "question": "August's estimated mean is 13.24 visits (a 16% increase on July: 13.24 ÷ 1.16 = 11.41). How does Part (b) check the estimated mean 662 ÷ 50 = 13.24?",
            "options": [
                "Multiply 13.24 × 50 = 662 (matching the exact sum of Frequency × Midpoint)",
                "Multiply 11.41 × 16",
                "Divide 50 ÷ 13.24",
            ],
            "correct": 0,
            "why": "Reverse check multiplies your estimated mean (13.24) by total frequency (50) back to the exact ∑(f × midpoint) total of 662.",
        },
    },
    "edexcel-maths-l2-past-paper-8-section-b": {
        "Question 1": {
            "archetype": "Examiner Trap",
            "question": "Mandy spins a spinner twice and lists every outcome in a sample space. What common mistake costs marks in 'at least one' probability questions?",
            "options": [
                "Double-counting the overlap outcome (e.g. Pink + Pink) or forgetting the total outcomes is 5 × 5 = 25",
                "Writing the probability as a simplified fraction",
                "Listing pairs in a systematic 5 × 5 grid",
            ],
            "correct": 0,
            "why": "A 5 × 5 sample space has 25 equal pairs; count each matching cell once (never add row + column and double-count Pink/Pink!).",
        },
        "Question 2": {
            "archetype": "Reverse Check Trap",
            "question": "Habiba mixes butter and flour in ratio 4 : 9 using 650 g total. After finding 1 part = 50 g and butter = 200 g, how do you verify your ratio split?",
            "options": [
                "Check flour = 9 × 50 = 450 g, and confirm 200 g + 450 g = 650 g",
                "Check 650 ÷ 4 = 162.5 g",
                "Multiply 200 × 9",
            ],
            "correct": 0,
            "why": "Checking both shares add back to 650 g (200 + 450 = 650) guarantees you divided by 4 + 9 = 13 parts accurately.",
        },
        "Question 3": {
            "archetype": "Rounding Direction Trap",
            "question": "An ingredients list makes 12 cupcakes, and Habiba needs enough mixture for a larger batch. If she scales ingredients cleanly, what check stops under-baking?",
            "options": [
                "Scale EVERY ingredient by the same exact multiplier (desired ÷ 12) and round UP whole packs/eggs if needed",
                "Only scale flour and leave sugar at the 12-cupcake amount",
                "Round eggs down when a recipe needs 4.5 eggs",
            ],
            "correct": 0,
            "why": "Scale every ingredient proportionally, and round UP whole items (eggs, packs) so you never fall short.",
        },
        "Question 4": {
            "archetype": "Examiner Trap",
            "question": "Callum plots advert spend (0–350) vs enquiries (0–25) on a scatter diagram. When estimating enquiries for an advert spend inside the range, what must you draw?",
            "options": [
                "A ruled Line of Best Fit through the cluster, plus vertical/horizontal reading lines to the axis",
                "Only read the highest single dot",
                "Extend the line backwards past zero",
            ],
            "correct": 0,
            "why": "Examiners award method marks specifically for drawing a straight Line of Best Fit and reading cleanly off the graph grid.",
        },
        "Question 5": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Misha weighs 73.3 kg (BMI 25.31), bringing the 8-person team BMI total to 210.41 and mean 26.30 vs target 26.9. What finishes the answer?",
            "options": [
                "Write '26.30' alone",
                "State an explicit Yes/No verdict comparing 26.30 against 26.9 with clear reasoning",
                "Divide 210.41 by 7 people instead of 8",
            ],
            "correct": 1,
            "why": "Always include all 8 team members (210.41 ÷ 8 = 26.30) AND write the Yes/No comparison sentence against 26.9.",
        },
        "Question 6": {
            "archetype": "Examiner Trap",
            "question": "In Part (a), 'Write three million, six hundred and seventy-five thousand in figures.' Which placeholder mistake loses the mark?",
            "options": [
                "Writing 3,675,000 cleanly",
                "Dropping the final three zeros (3,675) or misplacing commas",
                "Using spaces every three digits (3 675 000)",
            ],
            "correct": 1,
            "why": "Three million sits in the 7th digit place (X,XXX,XXX) — count digits from right to left to keep all three trailing zeros in 3,675,000.",
        },
        "Question 7": {
            "archetype": "Reverse Check Trap",
            "question": "Nyam sees his screen time fell/rose by a percentage compared to last week. Why is it wrong to find the percentage of THIS week's new figure when working backwards?",
            "options": [
                "This week is already the changed amount (e.g. 100% ± %); divide by the decimal multiplier to recover LAST week's 100% original",
                "Last week's time is always 10 hours",
                "Percentages work identically forwards and backwards",
            ],
            "correct": 0,
            "why": "Reverse percentage problems always divide the new amount by the growth/reduction multiplier (e.g. ÷ 1.20 or ÷ 0.85).",
        },
        "Question 8": {
            "archetype": "Rounding Direction Trap",
            "question": "Frank's kitchen is 3.6 m × 4.5 m and heated underfloor area is 8.36 m² (Large kit £179.99). Why should Part (b)'s check test a reverse step?",
            "options": [
                "Confirming how area minus unheated fixtures gives 8.36 m², and checking any kit sizing covers AT LEAST 8.36 m² (never under-size!)",
                "Choosing a kit covering 8.0 m² because it's cheaper",
                "Using perimeter instead of area",
            ],
            "correct": 0,
            "why": "Heating/flooring kits must cover AT LEAST the calculated area (8.36 m²), and Part (b) requires a reverse arithmetic check.",
        },
        "Question 9": {
            "archetype": "Unit & Capacity Trap",
            "question": "Sammi's cylindrical sweet tin sits on a 1 cm grid showing DIAMETER = 6 squares (6 cm) and height = 8 cm. What radius goes into V = πr²h?",
            "options": [
                "r = 6 cm (using diameter directly)",
                "r = 3 cm (halving the 6 cm diameter → 3.14 × 3² × 8 = 226.08 cm³)",
                "r = 8 cm",
            ],
            "correct": 1,
            "why": "Halve the 6 cm diameter to r = 3 cm before computing πr²h = 226.08 cm³ — using r = 6 makes the tin 4× too huge!",
        },
        "Question 10": {
            "archetype": "Examiner Trap",
            "question": "Part (a) asks for 15/7 as a mixed number, and Part (b) asks for a Median from a dataset. What step comes BEFORE picking the middle value?",
            "options": [
                "Sort all numbers in order from smallest to largest (and convert 15 ÷ 7 = 2 remainder 1 → 2 1/7)",
                "Pick the middle number straight from the unsorted board",
                "Write 15/7 as 1.57",
            ],
            "correct": 0,
            "why": "Divide top by bottom for mixed numbers (15 ÷ 7 = 2 1/7), and ALWAYS sort data ascending before locating the median.",
        },
        "Question 11": {
            "archetype": "Unit & Capacity Trap",
            "question": "Part (a) converts 28% to a decimal (0.28). In Part (b), when converting currency AND adding a fee, what catches candidates out?",
            "options": [
                "Multiplying when they should divide (or adding a % fee in £ instead of the foreign currency, and forgetting 2 d.p. money format)",
                "Writing 28% as 0.28",
                "Keeping 2 decimal places on £",
            ],
            "correct": 0,
            "why": "Check the direction of the exchange rate (home → foreign vs foreign → home) and keep fees in matching currency before rounding to 2 d.p.",
        },
        "Question 12": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Bilal's usual pay is £8.70/h with Sunday uplift, plus a Range comparison for consistency. When comparing two ranges, which dataset is MORE consistent?",
            "options": [
                "The dataset with the SMALLER range (smaller gap between highest and lowest)",
                "The dataset with the larger range",
                "The one with more entries",
            ],
            "correct": 0,
            "why": "Smaller Range = values clustered closer together = MORE consistent! Pair with a clear Yes/No comparison statement.",
        },
    },
    "edexcel-maths-l1-past-paper-10-section-a": {
        "Question 1": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Samira finds 15% of 860 people without a calculator (10% = 86, 5% = 43 → 129). What must go in the official answer box?",
            "options": [
                "Write '129' only",
                "Tick/write 'Yes' AND state '129 people' to support the comparison",
                "Write '15%'",
            ],
            "correct": 1,
            "why": "A yes/no question always awards a dedicated mark for stating Yes/No backed by your calculated number (129 people).",
        },
        "Question 2": {
            "archetype": "Unit & Capacity Trap",
            "question": "Norbert's 12-hour shift starts Monday 8 pm, followed by 30 hours off. Why should you split 30 hours into 24 h + 6 h?",
            "options": [
                "Adding 24 hours lands cleanly on the same clock time next day (Tuesday 8 am → Wednesday 8 am), then +6 hours = Wednesday 2 pm (14:00)",
                "Because there are 10 hours in a day",
                "So you subtract 12 hours twice",
            ],
            "correct": 0,
            "why": "Jumping in 24-hour blocks keeps am/pm straight across midnight, avoiding the 12-hour am/pm flip mistake.",
        },
        "Question 3": {
            "archetype": "Unit & Capacity Trap",
            "question": "In Q3(b)–(c), you round 4.749 to 1 d.p. (4.7) and convert 0.9 kg into grams. How many grams is 0.9 kg?",
            "options": [
                "90 g (× 100)",
                "900 g (0.9 × 1,000 = 900 g, since 1 kg = 1,000 g)",
                "9,000 g",
            ],
            "correct": 1,
            "why": "There are 1,000 g in 1 kg — shifting 3 places left turns 0.9 kg into 900 g, and in 4.749 the second digit 4 means 4.7 (do NOT chain-round 9→5→8!).",
        },
        "Question 4": {
            "archetype": "Reverse Check Trap",
            "question": "Zac estimates 3/5 of 624 by rounding 624 → 600 (600 ÷ 5 × 3 = 360). How does Part (b) show a valid reverse check?",
            "options": [
                "360 ÷ 3 = 120, and 120 × 5 = 600 (reverses ×3 and ÷5 back to 600)",
                "600 × 3 = 1800",
                "624 − 360 = 264",
            ],
            "correct": 0,
            "why": "Reverse each operation in backwards order: divide by numerator 3 (= 120), then multiply by denominator 5 (= 600).",
        },
    },
    "edexcel-maths-l1-past-paper-10-section-b": {
        "Question 1": {
            "archetype": "Examiner Trap",
            "question": "In Part (a) Company A made 'three quarters of a million pounds' (£750,000), and Part (b) orders 2.39, 2.41, 2.89, 2.9, 3.09. Why is 2.9 LARGER than 2.89?",
            "options": [
                "Padding to 2 d.p. turns 2.9 into 2.90, and 2.90 > 2.89",
                "2.9 is smaller because 9 < 89",
                "Three quarters of a million is £75,000",
            ],
            "correct": 0,
            "why": "Pad decimals mentally to matching places (2.90 vs 2.89) and convert '3/4 of a million' to 750,000 carefully!",
        },
        "Question 2": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Alex won 60% of 90 (54) and Seamus won 55% of 80 (44). Alex claims she won 12 more. What goes in the answer box?",
            "options": [
                "Write '10' alone",
                "Write 'No, 10 more' (showing 54 − 44 = 10, which is not 12)",
                "Write 'Yes, 54 more'",
            ],
            "correct": 1,
            "why": "Always pair your explicit 'No' decision with the actual difference (10 more) to win the interpretation mark.",
        },
        "Question 3": {
            "archetype": "Rounding Direction Trap",
            "question": "Akeem's L-shaped room has area 29.23 m² and each pack covers 0.4 m², giving 29.23 ÷ 0.4 = 73.075 packs. Why does 73.075 round UP to 74?",
            "options": [
                "73 packs only cover 29.20 m², leaving 0.03 m² uncovered — you must buy 74 whole packs",
                "Because .075 is more than .5",
                "You can buy 0.075 of a pack",
            ],
            "correct": 0,
            "why": "Flooring/tiling/paint packs must ALWAYS round UP even at .075 so the whole room is covered!",
        },
        "Question 4": {
            "archetype": "Examiner Trap",
            "question": "When plotting 0.7 on a 0-to-1 scale split into 10 equal ticks and measuring the bearing FROM the hostel, what two things check accuracy?",
            "options": [
                "Count 7 tenths ticks along from 0, and centre your protractor at the hostel (after FROM) measuring clockwise from North",
                "Count from 1 backwards",
                "Measure anti-clockwise from the cave",
            ],
            "correct": 0,
            "why": "Bearings ALWAYS measure clockwise from North at the point named after FROM (e.g. from the hostel).",
        },
        "Question 5": {
            "archetype": "Examiner Trap",
            "question": "When drawing Jesse's 5-year bar chart, what three checklist items secure ALL chart marks?",
            "options": [
                "1) Chart title, 2) Labelled axes with uniform scale starting at 0, 3) Equal-width bars with neat gaps matching table heights",
                "Draw bars touching with no axis labels",
                "Skip the lowest year",
            ],
            "correct": 0,
            "why": "Titles, labelled axes, uniform linear scales starting at 0, and equal-width separated bars are strictly checked on Level 1 mark schemes.",
        },
        "Question 6": {
            "archetype": "Unit & Capacity Trap",
            "question": "Zelda's 20 m × 10 m × 1.8 m pool has a 0.3 m air gap at the top (water depth 1.5 m → 300 m³). How many LITRES is 300 m³?",
            "options": [
                "300 × 1,000 = 300,000 litres (1 m³ = 1,000 litres!)",
                "300 × 100 = 30,000 litres",
                "300 ÷ 1,000 = 0.3 litres",
            ],
            "correct": 0,
            "why": "Don't forget BOTH traps here: subtract the 0.3 m air gap FIRST (depth = 1.5 m), and convert m³ → litres by multiplying by 1,000!",
        },
        "Question 7": {
            "archetype": "Unit & Capacity Trap",
            "question": "If 1 cm on a map represents 3 km, what real distance does 5 cm represent (and how many lines of symmetry does a square have)?",
            "options": [
                "5 × 3 = 15 km; a square has 4 lines of symmetry",
                "5 ÷ 3 = 1.67 km; 2 lines",
                "5 + 3 = 8 km; 4 lines",
            ],
            "correct": 0,
            "why": "Keep units attached (15 km, not 15 cm!), and remember a square has 4 symmetry lines (unlike a rectangle which has 2).",
        },
        "Question 8": {
            "archetype": "Reverse Check Trap",
            "question": "Maya adds the three triangle edges: 180 + 120 + 215 = 515. How does Part (b) check this perimeter with subtraction?",
            "options": [
                "515 − 215 = 300 (which matches 180 + 120 = 300)",
                "180 − 120 = 60",
                "515 ÷ 3 = 171.6",
            ],
            "correct": 0,
            "why": "Subtracting one added edge from your total (515 − 215 = 300) verifies the remaining sum 180 + 120 cleanly.",
        },
        "Question 9": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Tim's 7-day total is 98 unsold sandwiches (mean 14/day × £1.95 = £27.30). What makes the final answer complete?",
            "options": [
                "Write 'Yes, £27.30' (not £27.3!) comparing against the threshold value",
                "Divide 98 by 5 weekdays instead of 7 days",
                "Write £27.3p",
            ],
            "correct": 0,
            "why": "Divide across all 7 days in the table (98 ÷ 7 = 14), format currency to 2 decimal places (£27.30), and write the Yes/No verdict.",
        },
        "Question 10": {
            "archetype": "Examiner Trap",
            "question": "The first group in Colin's table is 1–5 (5 values: 1, 2, 3, 4, 5). What are the next two EQUAL class intervals?",
            "options": [
                "6–10 and 11–15 (no overlaps and equal width of 5 integers each!)",
                "5–10 and 10–15 (overlapping boundaries)",
                "6–12 and 13–20",
            ],
            "correct": 0,
            "why": "Never overlap class boundaries (5–10 overlaps 1–5 at 5!), and verify your tallies add up to all 12 items.",
        },
        "Question 11": {
            "archetype": "Yes/No Verdict Trap",
            "question": "Offer A works out to £17.49 and Offer B is £17.25 (saving 24p, under Ashley's 50p guess). What must be written in the box?",
            "options": [
                "'Yes, saves 24p' (both the Yes verdict AND the 24p saving)",
                "'£17.25' only",
                "'No, saves £17.25'",
            ],
            "correct": 0,
            "why": "State 'Yes' because 24p IS less than 50p, AND show the 24p difference between £17.49 and £17.25.",
        },
    },
}

# Fallback 4-archetype set for the 18 older Edexcel Maths L2 Past Papers without VTT chapters yet
LEGACY_MATHS_MOCK_CCQS = {
    "sec_a": [
        {
            "archetype": "Unit & Capacity Trap",
            "question": "In Section A (Non-Calculator), you read a multi-step scale or volume/weight problem mixing kg and g (or cm and m). What check protects the accuracy mark?",
            "options": [
                "Convert all measurements into ONE matching unit before calculating, and write the unit clearly on the answer line",
                "Multiply mixed units together and guess the final unit",
                "Drop decimal places because calculators aren't allowed",
            ],
            "correct": 0,
            "why": "Unit mismatches (cm vs m, ml vs l, £ vs p) void accuracy marks even when the mental arithmetic is right.",
        },
        {
            "archetype": "Rounding Direction Trap",
            "question": "After dividing a non-calculator quantity in Section A, you get 14 remainder 3 (or 14.3) when packing people into minibuses or boxes. What is the right rounding direction?",
            "options": [
                "Round DOWN to 14",
                "Round UP to 15 so the remaining 3 people/items are included",
                "Leave as 14.3 on a bus count",
            ],
            "correct": 1,
            "why": "Real-life capacity constraints (vehicles, tins, flooring packs) require rounding UP so nobody/nothing is left short.",
        },
        {
            "archetype": "Yes/No Verdict Trap",
            "question": "When a Section A question ends with 'Is Samir correct? Show why you think this', what earns the final interpretation mark?",
            "options": [
                "Writing only your calculated number without Yes or No",
                "Writing an explicit Yes or No verdict PLUS comparing both calculated figures with units",
                "Writing 'Yes' with zero working",
            ],
            "correct": 1,
            "why": "Decision marks require BOTH the clear Yes/No conclusion AND the explicit numerical comparison proving it.",
        },
        {
            "archetype": "Reverse Check Trap",
            "question": "A question asks: 'Use a reverse calculation to check your answer' (e.g. after 48 × 15 = 720 or 3/5 of 450 = 270). What earns the check mark?",
            "options": [
                "Repeating 48 × 15 again",
                "Performing the true inverse step (e.g. 720 ÷ 15 = 48, or 270 ÷ 3 × 5 = 450)",
                "Rounding 720 to 700",
            ],
            "correct": 1,
            "why": "Repeating the same forward calculation scores zero for a check — use the opposite operation (÷ to check ×, + to check −).",
        },
    ],
    "sec_b": [
        {
            "archetype": "Unit & Capacity Trap",
            "question": "In Section B (Calculator), a tank or garden question gives dimensions in m and asks for Litres (or gives Diameter instead of Radius). What MUST you check?",
            "options": [
                "Halve diameter to radius for πr², and convert 1 m³ = 1,000 litres (or 1,000 cm³ = 1 litre)",
                "Use diameter directly in πr²",
                "Multiply m³ by 100 for litres",
            ],
            "correct": 0,
            "why": "Forgetting to halve diameter to radius (4× error) and forgetting 1 m³ = 1,000 litres are the top Section B capacity traps.",
        },
        {
            "archetype": "Yes/No Verdict Trap",
            "question": "When comparing two percentage offers, utility quotes, or mean/range values in Section B, how do you secure the final mark?",
            "options": [
                "Stop as soon as your calculator shows the first number",
                "Tick/write Yes or No explicitly AND state both compared numbers with correct units (£, mins, m²)",
                "Round money to £24.3 instead of £24.30",
            ],
            "correct": 1,
            "why": "Examiners look for a stated Yes/No verdict supported by both figures (and 2 decimal places on money like £24.30).",
        },
        {
            "archetype": "Rounding Direction Trap",
            "question": "Your calculator reads 18.14 tins of paint (or 18.14 m² tiles) needed for a wall, while another question asks how many full £12 tickets £220 can buy (18.33). How do they differ?",
            "options": [
                "Both round down to 18",
                "Materials covering an area round UP (19 tins), while items limited by a fixed budget round DOWN (18 tickets)",
                "Both round up to 19",
            ],
            "correct": 1,
            "why": "Coverage/capacity rounds UP so you finish the job; budget/stock limits round DOWN because you cannot exceed your cash or ribbon!",
        },
        {
            "archetype": "Reverse Check Trap",
            "question": "How do you apply a Reverse Check to a Grouped Mean or Reverse Percentage answer in Section B?",
            "options": [
                "Multiply Estimated Mean × Total Frequency = ∑(f × mid), OR multiply Original Price × Multiplier back to the given Sale Price",
                "Guess whether the answer looks big",
                "Divide the frequency by the number of table rows",
            ],
            "correct": 0,
            "why": "Running the inverse calculation confirms both your formula setup and every calculator button press.",
        },
    ],
}
